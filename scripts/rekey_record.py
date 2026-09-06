"""Rename one paper record after its summary metadata is finalized."""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from filename_normalizer import canonical_stem_from_metadata, collision_stem, existing_layer_stems
from llm_wiki_common import read_yaml_md, write_yaml_md


def _rooted(root: Path, value: object) -> Path | None:
    if not value:
        return None
    path = Path(str(value))
    return path if path.is_absolute() else root / path


def _move_checked(source: Path | None, target: Path) -> None:
    if source is None or not source.exists():
        return
    if source.resolve() == target.resolve():
        return
    if target.exists():
        raise FileExistsError(f"Cannot rekey record; target already exists: {target}")
    target.parent.mkdir(parents=True, exist_ok=True)
    source.replace(target)


def rekey_record(root: Path, source: Path, evidence: dict[str, Any]) -> tuple[Path, str, str]:
    """Make final summary metadata the canonical filename/record identity.

    Returns ``(new_source_path, new_stem, new_record_id)``. Generated registry,
    index, bibliography, QC, and HTML outputs are rebuilt by the caller.
    """
    source = source.resolve()
    source_meta, source_body = read_yaml_md(source)
    old_stem = str(source_meta.get("stem") or source.stem)
    old_record_id = str(source_meta.get("record_id") or f"paper:{old_stem}")
    proposed = canonical_stem_from_metadata(
        evidence.get("title"), evidence.get("authors"), evidence.get("year"), old_stem
    )
    existing = existing_layer_stems(root, source)
    existing.discard(old_stem)
    new_stem = collision_stem(proposed, existing)
    if new_stem == old_stem:
        return source, old_stem, old_record_id

    old_paths: dict[str, Path] = {
        "source": source,
        "card": root / "cards" / f"{old_stem}.md",
        "wiki": root / "wiki" / f"{old_stem}.md",
        "pdf": _rooted(root, source_meta.get("pdf_path")) or root / "papers" / f"{old_stem}.pdf",
        "parse_log": root / "logs" / f"parse-{old_stem}.json",
    }
    new_paths = {key: path.with_name(f"{new_stem}{path.suffix}") for key, path in old_paths.items()}
    new_paths["parse_log"] = root / "logs" / f"parse-{new_stem}.json"
    for old_path, new_path in zip(old_paths.values(), new_paths.values()):
        if old_path.exists() and old_path.resolve() != new_path.resolve() and new_path.exists():
            raise FileExistsError(f"Cannot rekey record; target already exists: {new_path}")

    old_card_data: dict[str, Any] | None = None
    old_card_body = ""
    if old_paths["card"].exists():
        old_card_data, old_card_body = read_yaml_md(old_paths["card"])
        if old_card_data.get("metadata_status") == "locked":
            raise PermissionError(f"Cannot rekey locked record: {old_record_id}")
    old_wiki_data: dict[str, Any] | None = None
    old_wiki_body = ""
    if old_paths["wiki"].exists():
        old_wiki_data, old_wiki_body = read_yaml_md(old_paths["wiki"])

    # All target names were preflighted above, so no existing record is
    # overwritten during this rename transaction.
    for key in ("pdf", "source", "card", "wiki", "parse_log"):
        _move_checked(old_paths[key], new_paths[key])

    new_record_id = f"paper:{new_stem}"
    source_meta.update(
        {
            "stem": new_stem,
            "record_id": new_record_id,
            "pdf_path": str(new_paths["pdf"].relative_to(root)),
            "source_path": str(new_paths["source"].relative_to(root)),
        }
    )
    write_yaml_md(new_paths["source"], source_meta, source_body)

    if old_card_data is not None:
        old_card_data.update({"stem": new_stem, "record_id": new_record_id})
        provenance = old_card_data.setdefault("provenance", {})
        provenance.update(
            {
                "pdf_path": str(new_paths["pdf"].relative_to(root)),
                "source_path": str(new_paths["source"].relative_to(root)),
            }
        )
        write_yaml_md(new_paths["card"], old_card_data, old_card_body.replace(old_stem, new_stem))

    if old_wiki_data is not None:
        old_wiki_data.update({"stem": new_stem, "record_id": new_record_id})
        write_yaml_md(new_paths["wiki"], old_wiki_data, old_wiki_body.replace(old_stem, new_stem))

    if new_paths["parse_log"].exists():
        try:
            manifest = json.loads(new_paths["parse_log"].read_text(encoding="utf-8"))
            provisional_stem = manifest.get("provisional_stem")
            manifest.update(
                {
                    "provisional_stem": provisional_stem or old_stem,
                    "stem": new_stem,
                    "record_id": new_record_id,
                    "pdf_path": str(new_paths["pdf"].relative_to(root)),
                    "source_path": str(new_paths["source"].relative_to(root)),
                }
            )
            new_paths["parse_log"].write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
            if provisional_stem and provisional_stem != new_stem:
                stale_log = root / "logs" / f"parse-{provisional_stem}.json"
                if stale_log.exists() and stale_log.resolve() != new_paths["parse_log"].resolve():
                    stale_log.unlink()
        except (OSError, json.JSONDecodeError):
            pass

    return new_paths["source"], new_stem, new_record_id
