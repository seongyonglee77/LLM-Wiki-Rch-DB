from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

from llm_wiki_common import add_root_arg, load_registry


def build_indexes(root: Path) -> None:
    rows = load_registry(root)
    (root / "indexes").mkdir(exist_ok=True)
    (root / "indexes" / "records.json").write_text(json.dumps(rows, ensure_ascii=False, indent=2), encoding="utf-8")
    lines = ["# Paper Index", ""]
    for row in rows:
        stem = row.get("stem", "")
        title = row.get("title") or stem
        key = row.get("citation_key", "")
        status = row.get("metadata_status", "open")
        lines.append(f"- [[../wiki/{stem}|{title}]] - `@{key}` - `{status}`")
    (root / "indexes" / "papers.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    _ensure_wiki_navigation_indexes(root)


def _ensure_wiki_navigation_indexes(root: Path) -> None:
    """Keep curated introductions, but append any newly created local pages."""
    for category in ("overviews", "concepts", "projects", "questions"):
        folder = root / "wiki" / category
        index = folder / "index.md"
        if not folder.exists() or not index.exists():
            continue
        text = index.read_text(encoding="utf-8")
        additions = []
        for page in sorted(folder.glob("*.md")):
            if page.name == "index.md":
                continue
            stem = page.stem
            if not re.search(rf"\[\[{re.escape(stem)}(?:\||\]\])", text):
                additions.append(f"- [[{stem}|{page.stem.replace('-', ' ')}]]")
        if additions:
            index.write_text(text.rstrip() + "\n\n## Pages\n\n" + "\n".join(additions) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    add_root_arg(parser)
    args = parser.parse_args()
    root = Path(args.root).resolve() if args.root else Path.cwd().resolve()
    build_indexes(root)
    print("indexes built")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
