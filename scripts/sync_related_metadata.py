"""Synchronize card YAML and rendered links from registry/synthesis-links.json."""
from __future__ import annotations

import argparse
from pathlib import Path

from llm_wiki_common import add_root_arg, iter_cards, read_yaml_md, write_yaml_md
from synthesis_map import related_metadata, render_links


def sync_card(root: Path, card: Path) -> None:
    data, body = read_yaml_md(card)
    stem = str(data.get("stem") or card.stem)
    data["related"] = related_metadata(root, stem)
    data.pop("review_log", None)
    heading = "## Related Synthesis Pages"
    section = f"{heading}\n\n{render_links(root, stem, '../wiki/') or '- No mapped overview or concept page yet; record the synthesis gap in QC.'}"
    if heading in body:
        before = body.split(heading, 1)[0].rstrip()
        after = body.split(heading, 1)[1]
        if "## Related Links" in after:
            after = "## Related Links" + after.split("## Related Links", 1)[1]
        else:
            after = ""
        body = before + "\n\n" + section + ("\n\n" + after.lstrip() if after else "\n")
    elif "## Related Links" in body:
        before, after = body.split("## Related Links", 1)
        body = before.rstrip() + "\n\n" + section + "\n\n## Related Links" + after
    else:
        body = body.rstrip() + "\n\n" + section + "\n"
    write_yaml_md(card, data, body)


def main() -> int:
    parser = argparse.ArgumentParser()
    add_root_arg(parser)
    args = parser.parse_args()
    root = Path(args.root).resolve() if args.root else Path.cwd().resolve()
    cards = list(iter_cards(root))
    for card in cards:
        sync_card(root, card)
    print(f"synchronized {len(cards)} cards")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
