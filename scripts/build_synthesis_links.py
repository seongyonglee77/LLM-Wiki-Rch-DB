"""Rebuild reverse links from the relationship registry into synthesis pages."""
from __future__ import annotations

import argparse
from pathlib import Path

from llm_wiki_common import add_root_arg, read_yaml_md
from synthesis_map import CATEGORIES, _registry, synthesis_links_for

START = "<!-- GENERATED:RELATED-PAPERS:START -->"
END = "<!-- GENERATED:RELATED-PAPERS:END -->"


def build_synthesis_links(root: Path) -> int:
    papers = (_registry(root).get("papers") or {})
    reverse: dict[str, list[tuple[str, str, str]]] = {}
    for stem in papers:
        for item in synthesis_links_for(root, stem):
            reverse.setdefault(item["path"], []).append((stem, item.get("relation", ""), item["label"]))

    changed = 0
    for category in CATEGORIES:
        folder = root / "wiki" / category
        for page in folder.glob("*.md"):
            if page.name == "index.md":
                continue
            page_key = f"{category}/{page.stem}"
            rows = reverse.get(page_key, [])
            papers_block = [START, "", "## Related Papers", ""]
            for stem, relation, _label in sorted(rows):
                card = root / "cards" / f"{stem}.md"
                title = stem
                if card.exists():
                    data, _ = read_yaml_md(card)
                    title = str(data.get("title") or stem)
                papers_block.append(f"- [[../{stem}|{title}]]" + (f" — {relation}" if relation else ""))
            papers_block.extend(["", END])
            text = page.read_text(encoding="utf-8")
            if START in text and END in text:
                before = text.split(START, 1)[0].rstrip()
                after = text.split(END, 1)[1].lstrip()
                replacement = "\n".join(papers_block)
                new_text = before + "\n\n" + replacement + ("\n\n" + after if after else "\n")
            else:
                new_text = text.rstrip() + "\n\n" + "\n".join(papers_block) + "\n"
            if new_text != text:
                page.write_text(new_text, encoding="utf-8")
                changed += 1
    return changed


def main() -> int:
    parser = argparse.ArgumentParser()
    add_root_arg(parser)
    args = parser.parse_args()
    root = Path(args.root).resolve() if args.root else Path.cwd().resolve()
    print(f"updated {build_synthesis_links(root)} synthesis pages")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
