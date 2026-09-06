from __future__ import annotations

import argparse
import json
import shutil
from pathlib import Path

from build_card import create_or_update_card
from build_html_site import build as build_html_site
from build_indexes import build_indexes
from build_registry import build_registry
from build_wiki import build_wiki
from export_refs_bib import export_refs
from filename_normalizer import canonicalize_paths
from llm_wiki_common import add_root_arg, file_sha256, load_registry, read_yaml_md, utc_now, write_yaml_md
from parse_pdf import parse_pdf
from qc_report import qc_report


def known_hashes(root: Path) -> set[str]:
    hashes = set()
    for row in load_registry(root):
        h = row.get("provenance", {}).get("source_hash")
        if h:
            hashes.add(h)
    return hashes


def ingest_one(root: Path, pdf: Path, hashes: set[str]) -> dict:
    try:
        h = file_sha256(pdf)
        if h in hashes:
            return {"file": str(pdf), "status": "duplicate", "reason": "source_hash already exists"}
        manifest = parse_pdf(pdf, root)
        provisional_stem = manifest["stem"]
        source_path = root / manifest["source_path"]
        source_meta, source_body = read_yaml_md(source_path)
        # Parse first, then normalize from the extracted first-page metadata. This
        # avoids a second full-document LLM read and gives all downstream layers
        # one canonical YYYY_Author_ShortTitle stem.
        stem, source_path = canonicalize_paths(root, provisional_stem, source_path, source_body)
        target_pdf = root / "papers" / f"{stem}.pdf"
        if target_pdf.exists() and file_sha256(target_pdf) != h:
            return {"file": str(pdf), "status": "failure", "reason": f"target PDF already exists: {target_pdf.name}"}
        source_meta.update({"stem": stem, "record_id": f"paper:{stem}", "pdf_path": str(target_pdf.relative_to(root)), "source_path": str(source_path.relative_to(root))})
        write_yaml_md(source_path, source_meta, source_body)
        shutil.move(str(pdf), str(target_pdf))
        manifest.update({"provisional_stem": provisional_stem, "stem": stem, "record_id": f"paper:{stem}", "pdf_path": str(target_pdf.relative_to(root)), "source_path": str(source_path.relative_to(root))})
        (root / "logs" / f"parse-{stem}.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
        card = create_or_update_card(root, source_path)
        wiki = build_wiki(root, card)
        rows = build_registry(root)
        record_id = next((row["record_id"] for row in rows if row.get("stem") == stem), f"paper:{stem}")
        build_indexes(root)
        export_refs(root, {record_id})
        qc_report(root)
        build_html_site(root, root / "wiki-site")
        hashes.add(h)
        return {"file": str(target_pdf), "status": "success", "record_id": record_id, "stem": stem, "card": str(card.relative_to(root)), "wiki": str(wiki.relative_to(root))}
    except Exception as exc:
        return {"file": str(pdf), "status": "failure", "reason": str(exc)}


def ingest_batch(root: Path) -> list[dict]:
    inbox = root / "inbox"
    pdfs = sorted(inbox.glob("*.pdf"))
    hashes = known_hashes(root)
    results = [ingest_one(root, pdf, hashes) for pdf in pdfs]
    if not pdfs:
        build_registry(root)
        build_indexes(root)
        export_refs(root)
        qc_report(root)
        build_html_site(root, root / "wiki-site")
    log = {"generated_at": utc_now(), "results": results}
    (root / "logs" / f"ingest-{utc_now().replace(':', '').replace('+', 'Z')}.json").write_text(json.dumps(log, ensure_ascii=False, indent=2), encoding="utf-8")
    return results


def main() -> int:
    parser = argparse.ArgumentParser()
    add_root_arg(parser)
    args = parser.parse_args()
    root = Path(args.root).resolve() if args.root else Path.cwd().resolve()
    results = ingest_batch(root)
    print(json.dumps(results, ensure_ascii=False, indent=2))
    return 1 if any(r["status"] == "failure" for r in results) else 0


if __name__ == "__main__":
    raise SystemExit(main())
