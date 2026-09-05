from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

from llm_wiki_common import add_root_arg, load_registry, utc_now


def qc_report(root: Path) -> dict:
    rows = load_registry(root)
    config_path = root / "km-config.json"
    try:
        config = json.loads(config_path.read_text(encoding="utf-8")) if config_path.exists() else {}
    except json.JSONDecodeError:
        config = {}
    public_summary_only = config.get("publication_profile") == "public-summary-only"
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
            if public_summary_only and label == "pdf":
                continue
            if rel and not (root / rel).exists():
                issues.append({"record_id": rid, "type": "missing_layer", "path_type": label, "path": rel})
    for stem, ids in stems.items():
        if stem and len(ids) > 1:
            issues.append({"type": "duplicate_stem", "stem": stem, "record_ids": ids})
    for doi, ids in dois.items():
        if len(ids) > 1:
            issues.append({"type": "duplicate_doi", "doi": doi, "record_ids": ids})
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
