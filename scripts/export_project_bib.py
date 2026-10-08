from __future__ import annotations

import argparse
import re
from pathlib import Path

from project_literature import (
    ValidationError,
    append_status,
    atomic_write_text,
    load_registry,
    normalize_ws,
    preflight_outputs,
    selected_records,
    validate_project,
)


def split_bib_entries(text: str) -> list[str]:
    entries: list[str] = []
    index = 0
    length = len(text)
    while index < length:
        at = text.find("@", index)
        if at == -1:
            break
        cursor = at + 1
        while cursor < length and (text[cursor].isalpha() or text[cursor] == "_"):
            cursor += 1
        while cursor < length and text[cursor].isspace():
            cursor += 1
        if cursor >= length or text[cursor] not in "{(":
            index = cursor
            continue
        open_char = text[cursor]
        close_char = "}" if open_char == "{" else ")"
        depth = 1
        cursor += 1
        in_quote = False
        escape = False
        while cursor < length and depth:
            char = text[cursor]
            if escape:
                escape = False
            elif char == "\\":
                escape = True
            elif char == '"':
                in_quote = not in_quote
            elif not in_quote and char == open_char:
                depth += 1
            elif not in_quote and char == close_char:
                depth -= 1
            cursor += 1
        if depth:
            raise ValidationError("Malformed refs.bib: unterminated entry")
        entries.append(text[at:cursor].strip())
        index = cursor
    return entries


def parse_entry_key(entry: str) -> str | None:
    match = re.match(r"(?is)\s*@\s*([A-Za-z_]+)\s*[{(]\s*([^,\s]+)", entry)
    if not match:
        return None
    kind = match.group(1).lower()
    if kind in {"comment", "preamble", "string"}:
        return None
    return match.group(2).strip()


def parse_fields(entry: str) -> dict[str, str]:
    start = entry.find("{")
    if start == -1:
        start = entry.find("(")
    if start == -1:
        return {}
    comma = entry.find(",", start)
    if comma == -1:
        return {}
    end = len(entry) - 1
    body = entry[comma + 1 : end]
    fields: dict[str, str] = {}
    index = 0
    while index < len(body):
        while index < len(body) and (body[index].isspace() or body[index] == ","):
            index += 1
        name_start = index
        while index < len(body) and (body[index].isalnum() or body[index] in "_-"):
            index += 1
        if index == name_start:
            break
        name = body[name_start:index].lower()
        while index < len(body) and body[index].isspace():
            index += 1
        if index >= len(body) or body[index] != "=":
            break
        index += 1
        while index < len(body) and body[index].isspace():
            index += 1
        value, index = read_bib_value(body, index)
        fields[name] = value.strip()
    return fields


def read_bib_value(text: str, index: int) -> tuple[str, int]:
    if index >= len(text):
        return "", index
    if text[index] == "{":
        depth = 1
        index += 1
        start = index
        while index < len(text) and depth:
            if text[index] == "\\":
                index += 2
                continue
            if text[index] == "{":
                depth += 1
            elif text[index] == "}":
                depth -= 1
                if depth == 0:
                    return text[start:index], index + 1
            index += 1
        raise ValidationError("Malformed refs.bib: unterminated braced field")
    if text[index] == '"':
        index += 1
        start = index
        escape = False
        while index < len(text):
            char = text[index]
            if escape:
                escape = False
            elif char == "\\":
                escape = True
            elif char == '"':
                return text[start:index], index + 1
            index += 1
        raise ValidationError("Malformed refs.bib: unterminated quoted field")
    start = index
    while index < len(text) and text[index] != ",":
        index += 1
    return text[start:index].strip(), index


def load_bib_entries(path: Path) -> dict[str, tuple[str, dict[str, str]]]:
    entries: dict[str, tuple[str, dict[str, str]]] = {}
    duplicates: set[str] = set()
    for entry in split_bib_entries(path.read_text(encoding="utf-8")):
        key = parse_entry_key(entry)
        if key is None:
            continue
        if key in entries:
            duplicates.add(key)
        entries[key] = (entry, parse_fields(entry))
    if duplicates:
        raise ValidationError(f"Duplicate refs.bib citation keys: {', '.join(sorted(duplicates))}")
    return entries


def export_project_bib(project_arg: str) -> Path:
    context, _registry, ledger = validate_project(project_arg)
    registry = load_registry(context["db_root"])
    selected = selected_records(ledger)
    refs_path = context["db_root"] / "refs.bib"
    if not refs_path.exists():
        raise ValidationError("db_root refs.bib is missing")
    entries = load_bib_entries(refs_path)

    output_entries: list[str] = []
    for record in selected:
        registry_row = registry.get(record["record_id"])
        if registry_row is None:
            raise ValidationError(f"Selected record missing from registry: {record['record_id']}")
        if registry_row["citation_key"] != record["citation_key"]:
            raise ValidationError(f"Selected record citation key mismatch: {record['record_id']}")
        if record["citation_key"] not in entries:
            raise ValidationError(f"Selected citation key missing from refs.bib: {record['citation_key']}")
        entry, fields = entries[record["citation_key"]]
        bib_record_id = fields.get("recordid")
        if bib_record_id and normalize_ws(bib_record_id) != record["record_id"]:
            raise ValidationError(f"refs.bib recordid mismatch for {record['citation_key']}")
        output_entries.append(entry)

    if output_entries:
        content = "% Generated project bibliography. Do not edit manually.\n\n" + "\n\n".join(output_entries) + "\n"
    else:
        content = "% Generated project bibliography. No selected literature evidence records.\n"
    output_path = context["project"] / "references.bib"
    preflight_outputs(context["project"], [output_path, context["project"] / "STATUS.md"])
    atomic_write_text(output_path, content, root=context["project"])
    append_status(context["project"], f"exported references.bib with {len(output_entries)} selected record(s)")
    return output_path


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Export selected project literature records to references.bib.")
    parser.add_argument("--project", required=True, help="Project directory containing project-config.json")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        path = export_project_bib(args.project)
    except ValidationError as exc:
        raise SystemExit(f"error: {exc}") from exc
    print(path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
