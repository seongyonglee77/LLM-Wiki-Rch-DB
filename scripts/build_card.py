from __future__ import annotations

import argparse
import re
from pathlib import Path

from llm_wiki_common import add_root_arg, read_yaml_md, slugify, write_yaml_md


def parse_title(source_body: str, stem: str) -> str:
    generic = {"image", "introduction", "research article", "media review", "article"}
    for line in source_body.splitlines():
        clean = re.sub(r"[#*_`]+", "", line).strip()
        clean = re.sub(r"<!--.*?-->", "", clean).strip()
        if len(clean) >= 12 and clean.lower() not in generic:
            return clean[:240]
    return stem.replace("-", " ").title()


def create_or_update_card(root: Path, source: Path) -> Path:
    source_meta, source_body = read_yaml_md(source)
    stem = source_meta.get("stem") or source.stem
    record_id = source_meta.get("record_id") or f"paper:{stem}"
    card_path = root / "cards" / f"{stem}.md"
    if card_path.exists():
        data, body = read_yaml_md(card_path)
    else:
        template = root / "templates" / "template-paper-summary.md"
        data, body = read_yaml_md(template)
        # Ingest creates the record shell only.  A card is not summarized until
        # a human/LLM summary pass has actually populated its body.
        data["summary"]["status"] = "unsummarized"
    # Migrate only the card being maintained.  Legacy fields are intentionally
    # removed because provenance owns the PDF path and wiki synthesis is owned
    # by build_wiki.py rather than card YAML.
    summary = data.pop("summary", None) or {}
    summary.setdefault("level", data.pop("summary_level", "deep"))
    summary.setdefault("status", data.pop("status", "unsummarized"))
    summary.setdefault("structure_policy", data.pop("structure_policy", "source_structure"))
    data["summary"] = summary
    for field in ("paper_id", "file_name", "topics", "projects", "related", "review_log"):
        data.pop(field, None)
    data.update(
        {
            "record_id": data.get("record_id") or record_id,
            "stem": stem,
            "title": data.get("title") or parse_title(source_body, stem),
            "citation_key": data.get("citation_key") or slugify(parse_title(source_body, stem)).replace("-", "")[:24],
            "metadata_status": data.get("metadata_status") or "open",
        }
    )
    provenance = data.setdefault("provenance", {})
    provenance.update(
        {
            "pdf_path": source_meta.get("pdf_path", provenance.get("pdf_path", "papers/")),
            "source_path": str(source.relative_to(root)),
            "parsed_with": source_meta.get("parsed_with", provenance.get("parsed_with", "docling")),
            "source_hash": source_meta.get("source_hash", provenance.get("source_hash", "")),
        }
    )
    verification = data.setdefault("verification", {})
    verification.setdefault("requires_human_review", True)
    write_yaml_md(card_path, data, body)
    return card_path


def main() -> int:
    parser = argparse.ArgumentParser()
    add_root_arg(parser)
    parser.add_argument("source")
    args = parser.parse_args()
    root = Path(args.root).resolve() if args.root else Path.cwd().resolve()
    print(create_or_update_card(root, Path(args.source).resolve()))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
