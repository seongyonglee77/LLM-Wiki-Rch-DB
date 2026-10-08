from __future__ import annotations

import argparse
import json
import os
import platform
import re
import tempfile
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


LEDGER_NAME = "literature-evidence.json"
REPORT_NAME = "literature-evidence.md"
STATUS_NAME = "STATUS.md"
PACKET_DIR = "citation-packets"

LEDGER_SCHEMA_VERSION = 1
CONFIG_SCHEMA_VERSION = 1
DECISIONS = {"candidate", "selected", "excluded"}
VERIFICATIONS = {"source_text", "page_verified", "unverified"}
EXPECTED_SEARCH_PATHS = ["indexes", "wiki", "cards", "sources"]
RECORD_FIELDS = {
    "record_id",
    "card_path",
    "citation_key",
    "decision",
    "decision_reason",
    "argument_role",
    "evidence",
    "unknowns",
    "reference",
}
EVIDENCE_FIELDS = {"source_path", "quote", "locator", "verification", "interpretation"}


class ValidationError(ValueError):
    pass


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def normalize_rel(value: str) -> str:
    return value.replace("\\", "/").strip()


def normalize_ws(value: str) -> str:
    return re.sub(r"\s+", " ", value).strip()


def host_kind() -> str:
    if os.name == "nt":
        return "windows"
    release = platform.uname().release.lower()
    if "microsoft" in release or os.environ.get("WSL_DISTRO_NAME") or Path("/mnt/d").exists():
        return "wsl"
    return "posix"


def portable_path_text(value: str, *, kind: str | None = None) -> str:
    text = value.replace("\\", "/")
    kind = kind or host_kind()
    drive_match = re.match(r"^([A-Za-z]):/(.*)$", text)
    mount_match = re.match(r"^/mnt/([A-Za-z])/(.*)$", text)
    if drive_match and kind == "wsl":
        text = f"/mnt/{drive_match.group(1).lower()}/{drive_match.group(2)}"
    elif mount_match and kind == "windows":
        text = f"{mount_match.group(1).upper()}:/{mount_match.group(2)}"
    elif drive_match and kind != "windows":
        raise ValidationError("Windows drive paths require WSL on non-Windows hosts; rebind this path explicitly")
    elif mount_match and kind != "wsl":
        raise ValidationError("WSL /mnt/<drive> paths require Windows/WSL pairing; rebind this path explicitly")
    return text


def portable_path(value: str, base: Path | None = None) -> Path:
    text = portable_path_text(value)
    path = Path(text).expanduser()
    if not path.is_absolute() and base is not None:
        path = base / path
    return path.resolve()


def assert_not_nested_project(db_root: Path, project: Path) -> None:
    try:
        project.relative_to(db_root)
    except ValueError:
        return
    raise ValidationError("project_root must not be the db_root or nested inside db_root")


def preflight_output_path(root: Path, path: Path) -> Path:
    root = root.resolve()
    resolved_parent = path.parent.resolve()
    try:
        resolved_parent.relative_to(root)
    except ValueError as exc:
        raise ValidationError(f"Output path escapes project root: {path}") from exc
    if path.exists() and path.is_symlink():
        raise ValidationError(f"Output path must not be a symlink: {path}")
    current = root
    relative_parts = path.parent.relative_to(root).parts
    for part in relative_parts:
        current = current / part
        if current.exists() and current.is_symlink():
            raise ValidationError(f"Output parent must not contain symlinks: {current}")
    return path


def preflight_outputs(root: Path, paths: list[Path]) -> None:
    for path in paths:
        preflight_output_path(root, path)


def atomic_write_text(path: Path, text: str, *, root: Path | None = None) -> None:
    if root is not None:
        path = preflight_output_path(root, path)
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp_name = tempfile.mkstemp(prefix=f".{path.name}.", suffix=".tmp", dir=str(path.parent))
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="\n") as handle:
            handle.write(text)
        os.replace(tmp_name, path)
    except Exception:
        try:
            os.unlink(tmp_name)
        except FileNotFoundError:
            pass
        raise


def load_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise ValidationError(f"Malformed JSON in {path}: {exc}") from exc


def require_object(value: Any, label: str) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise ValidationError(f"{label} must be an object")
    return value


def require_string(value: Any, label: str, *, allow_empty: bool = False) -> str:
    if not isinstance(value, str):
        raise ValidationError(f"{label} must be a string")
    if not allow_empty and not value.strip():
        raise ValidationError(f"{label} must not be empty")
    return value


def require_string_list(value: Any, label: str) -> list[str]:
    if not isinstance(value, list) or any(not isinstance(item, str) for item in value):
        raise ValidationError(f"{label} must be a list of strings")
    return list(value)


def resolve_within(base: Path, rel_value: str, label: str, *, must_exist: bool) -> Path:
    rel = normalize_rel(require_string(rel_value, label))
    pure = Path(rel)
    if pure.is_absolute() or ".." in pure.parts:
        raise ValidationError(f"{label} must be a relative path inside its allowed root")
    path = (base / rel).resolve()
    try:
        path.relative_to(base.resolve())
    except ValueError as exc:
        raise ValidationError(f"{label} escapes its allowed root") from exc
    if must_exist and not path.exists():
        raise ValidationError(f"{label} does not exist: {rel}")
    if must_exist and path.is_symlink():
        raise ValidationError(f"{label} must not be a symlink: {rel}")
    return path


def normalize_source_path(value: str, label: str) -> str:
    source_path = normalize_rel(require_string(value, label))
    if "/" not in source_path:
        source_path = f"sources/{source_path}"
    if not source_path.startswith("sources/"):
        raise ValidationError(f"{label} must be DB-relative under sources/")
    return source_path


def page_section_contains_quote(source_text: str, quote: str, locator: str) -> bool:
    if not locator.strip():
        return False
    escaped = re.escape(locator.strip())
    marker = re.compile(
        rf"(?im)^\s*(?:<!--\s*)?(?:page|p\.?)\s*[:#-]?\s*{escaped}\b.*(?:-->)?\s*$|^\s*\[\s*page\s+{escaped}\s*\]\s*$"
    )
    matches = list(marker.finditer(source_text))
    normalized_quote = normalize_ws(quote)
    for index, match in enumerate(matches):
        start = match.end()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(source_text)
        if normalized_quote in normalize_ws(source_text[start:end]):
            return True
    return False


def load_project_config(project_arg: str) -> dict[str, Any]:
    project = portable_path(project_arg)
    config_path = project / "project-config.json"
    if not config_path.exists():
        raise ValidationError(f"Missing project config: {config_path}")
    config = require_object(load_json(config_path), "project-config.json")
    expected = {"schema_version", "db_root", "project_root", "search_paths"}
    unknown = sorted(set(config) - expected)
    missing = sorted(expected - set(config))
    if unknown:
        raise ValidationError(f"Unknown project-config fields: {', '.join(unknown)}")
    if missing:
        raise ValidationError(f"Missing project-config fields: {', '.join(missing)}")
    if config["schema_version"] != CONFIG_SCHEMA_VERSION:
        raise ValidationError("project-config schema_version must be 1")

    configured_project = portable_path(require_string(config["project_root"], "project_root"), project)
    if configured_project != project:
        raise ValidationError("project-config project_root does not match --project")

    db_root = portable_path(require_string(config["db_root"], "db_root"), project)
    if not (db_root / "registry" / "works.jsonl").exists():
        raise ValidationError("db_root must point to an llm-wiki root with registry/works.jsonl")
    assert_not_nested_project(db_root, project)

    search_paths = require_string_list(config["search_paths"], "search_paths")
    if [normalize_rel(item) for item in search_paths] != EXPECTED_SEARCH_PATHS:
        raise ValidationError(f"search_paths must be exactly: {', '.join(EXPECTED_SEARCH_PATHS)}")
    for index, rel in enumerate(search_paths):
        resolve_within(db_root, rel, f"search_paths[{index}]", must_exist=True)

    return {"project": project, "db_root": db_root, "search_paths": search_paths}


def load_registry(db_root: Path) -> dict[str, dict[str, Any]]:
    path = db_root / "registry" / "works.jsonl"
    records: dict[str, dict[str, Any]] = {}
    keys: set[str] = set()
    cards: set[str] = set()
    for line_no, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        row = require_object(json.loads(line), f"works.jsonl line {line_no}")
        record_id = require_string(row.get("record_id"), f"works.jsonl line {line_no} record_id")
        citation_key = require_string(row.get("citation_key"), f"works.jsonl line {line_no} citation_key")
        paths = require_object(row.get("paths"), f"works.jsonl line {line_no} paths")
        card_path = normalize_rel(require_string(paths.get("card"), f"works.jsonl line {line_no} paths.card"))
        source_path = normalize_rel(require_string(paths.get("source"), f"works.jsonl line {line_no} paths.source"))
        if record_id in records:
            raise ValidationError(f"Duplicate registry record_id: {record_id}")
        if citation_key in keys:
            raise ValidationError(f"Duplicate registry citation_key: {citation_key}")
        if card_path in cards:
            raise ValidationError(f"Duplicate registry card_path: {card_path}")
        keys.add(citation_key)
        cards.add(card_path)
        records[record_id] = {
            "record_id": record_id,
            "citation_key": citation_key,
            "card_path": card_path,
            "source_path": source_path,
            "reference": row.get("title", citation_key),
        }
    return records


def empty_ledger() -> dict[str, Any]:
    return {"schema_version": LEDGER_SCHEMA_VERSION, "records": []}


def load_ledger(project: Path) -> dict[str, Any]:
    path = project / LEDGER_NAME
    if not path.exists():
        return empty_ledger()
    ledger = require_object(load_json(path), LEDGER_NAME)
    validate_ledger_shape(ledger)
    return ledger


def validate_ledger_shape(ledger: dict[str, Any]) -> None:
    if set(ledger) != {"schema_version", "records"}:
        raise ValidationError(f"{LEDGER_NAME} must contain only schema_version and records")
    if ledger["schema_version"] != LEDGER_SCHEMA_VERSION:
        raise ValidationError(f"{LEDGER_NAME} schema_version must be 1")
    if not isinstance(ledger["records"], list):
        raise ValidationError(f"{LEDGER_NAME} records must be a list")
    seen_ids: set[str] = set()
    seen_keys: set[str] = set()
    for index, record in enumerate(ledger["records"]):
        obj = require_object(record, f"records[{index}]")
        record_id = require_string(obj.get("record_id"), f"records[{index}].record_id")
        citation_key = require_string(obj.get("citation_key"), f"records[{index}].citation_key")
        if record_id in seen_ids:
            raise ValidationError(f"Duplicate ledger record_id: {record_id}")
        if citation_key in seen_keys:
            raise ValidationError(f"Duplicate ledger citation_key: {citation_key}")
        seen_ids.add(record_id)
        seen_keys.add(citation_key)


def validate_record(
    raw: Any,
    *,
    db_root: Path,
    registry: dict[str, dict[str, Any]],
    approve_selection: bool,
    label: str,
) -> dict[str, Any]:
    record = dict(require_object(raw, label))
    unknown_fields = sorted(set(record) - RECORD_FIELDS)
    if unknown_fields:
        raise ValidationError(f"{label} has unknown fields: {', '.join(unknown_fields)}")
    record.setdefault("decision", "candidate")
    missing = sorted(RECORD_FIELDS - set(record))
    if missing:
        raise ValidationError(f"{label} missing fields: {', '.join(missing)}")

    record_id = require_string(record["record_id"], f"{label}.record_id")
    card_path = normalize_rel(require_string(record["card_path"], f"{label}.card_path"))
    citation_key = require_string(record["citation_key"], f"{label}.citation_key")
    decision = require_string(record["decision"], f"{label}.decision")
    if decision not in DECISIONS:
        raise ValidationError(f"{label}.decision must be candidate, selected, or excluded")
    if decision == "selected" and not approve_selection:
        raise ValidationError("selected records require --approve-selection")

    registry_row = registry.get(record_id)
    if registry_row is None:
        raise ValidationError(f"{label}.record_id is not in registry: {record_id}")
    if registry_row["citation_key"] != citation_key:
        raise ValidationError(f"{label}.citation_key does not match registry for {record_id}")
    if registry_row["card_path"] != card_path:
        raise ValidationError(f"{label}.card_path does not match registry for {record_id}")
    resolve_within(db_root, card_path, f"{label}.card_path", must_exist=True)

    evidence = record["evidence"]
    if not isinstance(evidence, list):
        raise ValidationError(f"{label}.evidence must be a list")
    cleaned_evidence: list[dict[str, str]] = []
    for evidence_index, raw_item in enumerate(evidence):
        item_label = f"{label}.evidence[{evidence_index}]"
        item = dict(require_object(raw_item, item_label))
        unknown_evidence = sorted(set(item) - EVIDENCE_FIELDS)
        missing_evidence = sorted(EVIDENCE_FIELDS - set(item))
        if unknown_evidence:
            raise ValidationError(f"{item_label} has unknown fields: {', '.join(unknown_evidence)}")
        if missing_evidence:
            raise ValidationError(f"{item_label} missing fields: {', '.join(missing_evidence)}")
        source_path = normalize_source_path(item["source_path"], f"{item_label}.source_path")
        resolved_source = resolve_within(db_root, source_path, f"{item_label}.source_path", must_exist=True)
        source_rel_to_db = resolved_source.relative_to(db_root).as_posix()
        if normalize_rel(registry_row["source_path"]) != source_rel_to_db:
            raise ValidationError(f"{item_label}.source_path does not match registry source for {record_id}")
        quote = require_string(item["quote"], f"{item_label}.quote")
        verification = require_string(item["verification"], f"{item_label}.verification")
        if verification not in VERIFICATIONS:
            raise ValidationError(f"{item_label}.verification must be source_text, page_verified, or unverified")
        source_text = resolved_source.read_text(encoding="utf-8")
        if normalize_ws(quote) not in normalize_ws(source_text):
            raise ValidationError(f"{item_label}.quote was not found exactly in normalized source text")
        locator = require_string(item["locator"], f"{item_label}.locator", allow_empty=True)
        if verification == "page_verified" and not page_section_contains_quote(source_text, quote, locator):
            raise ValidationError(f"{item_label}.page_verified requires a matching page marker section")
        cleaned_evidence.append(
            {
                "source_path": source_path,
                "quote": quote,
                "locator": locator,
                "verification": verification,
                "interpretation": require_string(item["interpretation"], f"{item_label}.interpretation"),
            }
        )

    cleaned = {
        "record_id": record_id,
        "card_path": card_path,
        "citation_key": citation_key,
        "decision": decision,
        "decision_reason": require_string(record["decision_reason"], f"{label}.decision_reason", allow_empty=True),
        "argument_role": require_string(record["argument_role"], f"{label}.argument_role", allow_empty=True),
        "evidence": cleaned_evidence,
        "unknowns": require_string_list(record["unknowns"], f"{label}.unknowns"),
        "reference": require_string(record["reference"], f"{label}.reference"),
    }
    return cleaned


def validate_records(
    records: list[dict[str, Any]],
    *,
    db_root: Path,
    registry: dict[str, dict[str, Any]],
    approve_selection: bool,
) -> list[dict[str, Any]]:
    cleaned = [
        validate_record(item, db_root=db_root, registry=registry, approve_selection=approve_selection, label=f"input[{index}]")
        for index, item in enumerate(records)
    ]
    seen_ids: set[str] = set()
    seen_keys: set[str] = set()
    for record in cleaned:
        if record["record_id"] in seen_ids:
            raise ValidationError(f"Duplicate input record_id: {record['record_id']}")
        if record["citation_key"] in seen_keys:
            raise ValidationError(f"Duplicate input citation_key: {record['citation_key']}")
        seen_ids.add(record["record_id"])
        seen_keys.add(record["citation_key"])
    return cleaned


def load_input_records(path: Path) -> list[dict[str, Any]]:
    raw = load_json(path)
    if isinstance(raw, list):
        return raw
    if isinstance(raw, dict):
        return [raw]
    raise ValidationError("--input must be a JSON object or list of objects")


def validate_project(project_arg: str) -> tuple[dict[str, Any], dict[str, dict[str, Any]], dict[str, Any]]:
    context = load_project_config(project_arg)
    registry = load_registry(context["db_root"])
    ledger = load_ledger(context["project"])
    ledger = {"schema_version": LEDGER_SCHEMA_VERSION, "records": validate_ledger_records(context, registry, ledger)}
    return context, registry, ledger


def validate_ledger_records(context: dict[str, Any], registry: dict[str, dict[str, Any]], ledger: dict[str, Any]) -> list[dict[str, Any]]:
    validate_ledger_shape(ledger)
    return validate_records(
        ledger["records"],
        db_root=context["db_root"],
        registry=registry,
        approve_selection=True,
    )


def append_status(project: Path, message: str) -> None:
    path = project / STATUS_NAME
    existing = path.read_text(encoding="utf-8") if path.exists() else "# Status\n"
    if existing and not existing.endswith("\n"):
        existing += "\n"
    atomic_write_text(path, f"{existing}- {utc_now()} {message}\n", root=project)


def write_ledger(project: Path, ledger: dict[str, Any]) -> None:
    text = json.dumps(ledger, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    atomic_write_text(project / LEDGER_NAME, text, root=project)


def selected_records(ledger: dict[str, Any]) -> list[dict[str, Any]]:
    return [record for record in ledger["records"] if record["decision"] == "selected"]


def render_markdown(ledger: dict[str, Any], *, db_root: Path) -> str:
    lines = [
        "# Literature Evidence",
        "",
        "<!-- Generated by scripts/project_literature.py. Do not edit manually. -->",
        "",
        f"- DB root: `{db_root.as_posix()}`",
        "- Verification note: exact quoted text is checked against source text; interpretation remains an argument to review.",
        "- `source_text` means the quote exists in the canonical source. `page_verified` additionally requires a matching page marker section.",
        "",
    ]
    if not ledger["records"]:
        lines.extend(["No literature evidence records.", "", "## References", "", "No references selected.", ""])
        return "\n".join(lines)
    for record in ledger["records"]:
        lines.extend(
            [
                f"## {record['citation_key']}",
                "",
                f"- Record ID: `{record['record_id']}`",
                f"- Card path: `{record['card_path']}`",
                f"- Decision: {record['decision']}",
                f"- Role: {record['argument_role'] or 'unspecified'}",
                f"- Reason: {record['decision_reason'] or 'unspecified'}",
                "",
                "### Evidence",
                "",
            ]
        )
        if not record["evidence"]:
            lines.extend(["No evidence recorded.", ""])
        for index, evidence in enumerate(record["evidence"], 1):
            locator = f" ({evidence['locator']})" if evidence["locator"] else ""
            missing = " - MISSING VERIFICATION" if evidence["verification"] == "unverified" else ""
            lines.extend(
                [
                    f"{index}. `{evidence['source_path']}`{locator} [{evidence['verification']}]{missing}",
                    "",
                    f"   > {evidence['quote']}",
                    "",
                    f"   Interpretation: {evidence['interpretation']}",
                    "",
                ]
            )
        if record["unknowns"]:
            lines.extend(["### Unknowns", ""])
            lines.extend(f"- {item}" for item in record["unknowns"])
            lines.append("")
    lines.extend(["## References", ""])
    refs = [record["reference"] for record in selected_records(ledger)]
    if refs:
        lines.extend(f"- {reference}" for reference in refs)
    else:
        lines.append("No references selected.")
    lines.append("")
    return "\n".join(lines)


def safe_packet_name(record: dict[str, Any]) -> str:
    base = re.sub(r"[^A-Za-z0-9_.-]+", "-", record["citation_key"]).strip(".-")
    return f"{base or 'citation'}-{re.sub(r'[^A-Za-z0-9_.-]+', '-', record['record_id']).strip('.-')}.md"


def packet_markdown(record: dict[str, Any]) -> str:
    adoption = "adopted" if record["decision"] == "selected" else "not adopted"
    lines = [
        f"# Citation Packet: {record['citation_key']}",
        "",
        f"- Record ID: `{record['record_id']}`",
        f"- Decision: {record['decision']}",
        f"- Selection status: {adoption}",
        f"- Argument role: {record['argument_role'] or 'unspecified'}",
        f"- Reference: {record['reference']}",
        "",
        "## Evidence",
        "",
    ]
    for index, evidence in enumerate(record["evidence"], 1):
        locator = f" ({evidence['locator']})" if evidence["locator"] else ""
        lines.extend(
            [
                f"### Evidence {index}{locator}",
                "",
                f"- Source: `{evidence['source_path']}`",
                f"- Verification: {evidence['verification']}",
                "",
                f"> {evidence['quote']}",
                "",
                evidence["interpretation"],
                "",
            ]
        )
    if record["unknowns"]:
        lines.extend(["## Unknowns", ""])
        lines.extend(f"- {item}" for item in record["unknowns"])
        lines.append("")
    return "\n".join(lines)


def upsert(project_arg: str, input_path: str, approve_selection: bool) -> None:
    context, registry, ledger = validate_project(project_arg)
    incoming = validate_records(
        load_input_records(Path(input_path)),
        db_root=context["db_root"],
        registry=registry,
        approve_selection=approve_selection,
    )
    by_id = {record["record_id"]: record for record in ledger["records"]}
    for record in incoming:
        by_id[record["record_id"]] = record
    merged = validate_records(
        [by_id[key] for key in sorted(by_id)],
        db_root=context["db_root"],
        registry=registry,
        approve_selection=True,
    )
    next_ledger = {"schema_version": LEDGER_SCHEMA_VERSION, "records": merged}
    preflight_outputs(
        context["project"],
        [context["project"] / LEDGER_NAME, context["project"] / REPORT_NAME, context["project"] / STATUS_NAME],
    )
    write_ledger(context["project"], next_ledger)
    atomic_write_text(
        context["project"] / REPORT_NAME,
        render_markdown(next_ledger, db_root=context["db_root"]),
        root=context["project"],
    )
    append_status(context["project"], f"upserted {len(incoming)} literature evidence record(s) and rendered report")
    print(f"upserted {len(incoming)} record(s)")


def render(project_arg: str) -> None:
    context, _registry, ledger = validate_project(project_arg)
    preflight_outputs(context["project"], [context["project"] / REPORT_NAME, context["project"] / STATUS_NAME])
    atomic_write_text(context["project"] / REPORT_NAME, render_markdown(ledger, db_root=context["db_root"]), root=context["project"])
    append_status(context["project"], "rendered literature-evidence.md")
    print(context["project"] / REPORT_NAME)


def packet(project_arg: str, record_id: str) -> None:
    context, _registry, ledger = validate_project(project_arg)
    matches = [record for record in ledger["records"] if record["record_id"] == record_id]
    if not matches:
        raise ValidationError(f"Record not found in ledger: {record_id}")
    record = matches[0]
    packet_path = context["project"] / PACKET_DIR / safe_packet_name(record)
    preflight_outputs(context["project"], [packet_path, context["project"] / STATUS_NAME])
    atomic_write_text(packet_path, packet_markdown(record), root=context["project"])
    append_status(context["project"], f"wrote citation packet for {record_id}")
    print(packet_path)


def validate_cmd(project_arg: str) -> None:
    context, registry, ledger = validate_project(project_arg)
    print(
        json.dumps(
            {
                "project": str(context["project"]),
                "db_root": str(context["db_root"]),
                "registry_records": len(registry),
                "ledger_records": len(ledger["records"]),
                "selected_records": len(selected_records(ledger)),
            },
            ensure_ascii=False,
            sort_keys=True,
        )
    )


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Manage project-scoped literature evidence ledgers.")
    parser.add_argument("--project", required=True, help="Project directory containing project-config.json")
    subparsers = parser.add_subparsers(dest="command", required=True)
    subparsers.add_parser("validate")
    upsert_parser = subparsers.add_parser("upsert")
    upsert_parser.add_argument("--input", required=True, help="JSON record or list of records")
    upsert_parser.add_argument("--approve-selection", action="store_true")
    subparsers.add_parser("render")
    packet_parser = subparsers.add_parser("packet")
    packet_parser.add_argument("--record-id", required=True)
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        if args.command == "validate":
            validate_cmd(args.project)
        elif args.command == "upsert":
            upsert(args.project, args.input, args.approve_selection)
        elif args.command == "render":
            render(args.project)
        elif args.command == "packet":
            packet(args.project, args.record_id)
        else:
            raise ValidationError(f"Unknown command: {args.command}")
    except ValidationError as exc:
        raise SystemExit(f"error: {exc}") from exc
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
