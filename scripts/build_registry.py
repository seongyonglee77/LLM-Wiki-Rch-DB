from __future__ import annotations

import argparse
from pathlib import Path

from llm_wiki_common import add_root_arg, iter_cards, read_yaml_md, utc_now, write_jsonl


def registry_row(root: Path, card: Path) -> dict:
    data, _ = read_yaml_md(card)
    stem = data.get("stem") or card.stem
    return {
        "record_id": data.get("record_id") or f"paper:{stem}",
        "stem": stem,
        "paths": {
            "card": str(card.relative_to(root)),
            "source": data.get("provenance", {}).get("source_path", f"sources/{stem}.md"),
            "wiki": f"wiki/{stem}.md",
            "pdf": data.get("provenance", {}).get("pdf_path", ""),
        },
        "title": data.get("title", ""),
        "authors": data.get("authors", []),
        "year": data.get("year", ""),
        "citation_key": data.get("citation_key", ""),
        "doi": data.get("doi", ""),
        "metadata_status": data.get("metadata_status", "open"),
        "publication_stage": data.get("publication_stage", ""),
        "provenance": data.get("provenance", {}),
        "updated_at": utc_now(),
    }


def build_registry(root: Path) -> list[dict]:
    rows = [registry_row(root, card) for card in iter_cards(root)]
    rows.sort(key=lambda row: (str(row.get("citation_key", "")), str(row.get("record_id", ""))))
    write_jsonl(root / "registry" / "works.jsonl", rows)
    return rows


def main() -> int:
    parser = argparse.ArgumentParser()
    add_root_arg(parser)
    args = parser.parse_args()
    root = Path(args.root).resolve() if args.root else Path.cwd().resolve()
    rows = build_registry(root)
    print(f"wrote {len(rows)} records")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

