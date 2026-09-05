from __future__ import annotations

import argparse
import re
from pathlib import Path

import yaml

from llm_wiki_common import add_root_arg, read_yaml_md, slugify, utc_now, write_yaml_md


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
        data["status"] = "unsummarized"
    data.update(
        {
            "paper_id": data.get("paper_id") or record_id,
            "record_id": data.get("record_id") or record_id,
            "stem": stem,
            "file_name": data.get("file_name") or Path(source_meta.get("pdf_path", "")).name,
            "title": data.get("title") or parse_title(source_body, stem),
            "citation_key": data.get("citation_key") or slugify(parse_title(source_body, stem)).replace("-", "")[:24],
            "metadata_status": data.get("metadata_status") or "open",
            "status": data.get("status") or "needs_review",
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
    review_log = data.setdefault("review_log", [])
    if not any(isinstance(item, dict) and item.get("event") == "card_created" for item in review_log):
        review_log.append({"event": "card_created", "at": utc_now(), "source": str(source.relative_to(root))})
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
