from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

from llm_wiki_common import add_root_arg, iter_cards, load_registry, read_yaml_md, utc_now
from synthesis_map import synthesis_links_for


def qc_report(root: Path) -> dict:
    rows = load_registry(root)
    issues = []
    stems = {}
    dois = {}
    for row in rows:
        rid = row.get("record_id")
        stem = row.get("stem")
        doi = row.get("doi")
        stems.setdefault(stem, []).append(rid)
        if doi:
            dois.setdefault(str(doi).lower(), []).append(rid)
        for label, rel in row.get("paths", {}).items():
            if rel and not (root / rel).exists():
                issues.append({"record_id": rid, "type": "missing_layer", "path_type": label, "path": rel})
    for stem, ids in stems.items():
        if stem and len(ids) > 1:
            issues.append({"type": "duplicate_stem", "stem": stem, "record_ids": ids})
    for doi, ids in dois.items():
        if len(ids) > 1:
            issues.append({"type": "duplicate_doi", "doi": doi, "record_ids": ids})
    for card in iter_cards(root):
        data, body = read_yaml_md(card)
        summary = data.get("summary", {}) or {}
        status = summary.get("status", data.get("status", "unsummarized"))
        if status != "summarized":
            continue
        mapped_links = synthesis_links_for(root, card.stem)
        if not any(item["category"] in {"overviews", "concepts"} for item in mapped_links):
            issues.append({"record_id": data.get("record_id", f"paper:{card.stem}"), "type": "synthesis_orphan", "message": "A summarized paper must link to at least one overview or concept page."})
        for item in mapped_links:
            synthesis_page = root / "wiki" / f"{item['path']}.md"
            if synthesis_page.exists():
                synthesis_text = synthesis_page.read_text(encoding="utf-8")
                if not re.search(rf"\[\[\.\./{re.escape(card.stem)}(?:\||\]\])", synthesis_text):
                    issues.append({"record_id": data.get("record_id", f"paper:{card.stem}"), "type": "missing_reverse_synthesis_link", "target": item["path"]})
        required = ("# Deep Summary", "## Theory & Literature Review", "## Findings", "## Discussion")
        missing = [section for section in required if section not in body]
        evidence_count = len(re.findall(r"\((?:p\.\s*\d+;\s*(?:source_page|pdf)-verified|page unavailable;\s*source-text-verified)\)", body))
        if missing or evidence_count < 9:
            issues.append({"record_id": data.get("record_id", f"paper:{card.stem}"), "type": "summary_evidence_gate", "missing_sections": missing, "verified_evidence_count": evidence_count})
        if "## Directly Citable Evidence" in body:
            issues.append({"record_id": data.get("record_id", f"paper:{card.stem}"), "type": "redundant_direct_evidence_section", "message": "Inline claim evidence is canonical; the legacy duplicate evidence table must be removed."})
        related = data.get("related", {}) or {}
        missing_related = []
        if not isinstance(related.get("wiki"), list) or not related.get("wiki"):
            missing_related.append("wiki")
        if not any(isinstance(related.get(key), list) and related.get(key) for key in ("overviews", "concepts")):
            missing_related.append("overviews_or_concepts")
        if missing_related:
            issues.append({"record_id": data.get("record_id", f"paper:{card.stem}"), "type": "incomplete_related_metadata", "missing_fields": missing_related})
        if "## Related Synthesis Pages" not in body:
            issues.append({"record_id": data.get("record_id", f"paper:{card.stem}"), "type": "missing_synthesis_links", "message": "Every summarized card must expose its related synthesis pages."})
        else:
            related_section = body.split("## Related Synthesis Pages", 1)[1].split("## Related Links", 1)[0]
            if not any(f"../wiki/{category}/" in related_section for category in ("overviews", "concepts")):
                issues.append({"record_id": data.get("record_id", f"paper:{card.stem}"), "type": "incomplete_synthesis_links", "missing_categories": ["overviews_or_concepts"]})
    markdown_files = list(root.rglob("*.md"))
    targets = {p.resolve().with_suffix("") for p in markdown_files}
    for page in markdown_files:
        text = page.read_text(encoding="utf-8")
        if page.parent.name in {"concepts", "overviews", "projects", "questions"} and page.name != "index.md" and len(text.strip()) < 150:
            issues.append({"type": "empty_synthesis_page", "path": str(page.relative_to(root))})
        for target in re.findall(r"\[\[([^\]|#]+)", text):
            resolved = (page.parent / target).resolve()
            if resolved not in targets:
                issues.append({"type": "broken_wikilink", "path": str(page.relative_to(root)), "target": target})
    report = {"generated_at": utc_now(), "record_count": len(rows), "issue_count": len(issues), "issues": issues}
    (root / "qc").mkdir(exist_ok=True)
    (root / "qc" / "qc_report.json").write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    md = ["# QC Report", "", f"- Generated at: `{report['generated_at']}`", f"- Records: `{len(rows)}`", f"- Issues: `{len(issues)}`", ""]
    for issue in issues:
        md.append(f"- `{issue.get('type')}`: {json.dumps(issue, ensure_ascii=False)}")
    (root / "qc" / "qc_report.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    return report


def main() -> int:
    parser = argparse.ArgumentParser()
    add_root_arg(parser)
    args = parser.parse_args()
    root = Path(args.root).resolve() if args.root else Path.cwd().resolve()
    report = qc_report(root)
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
