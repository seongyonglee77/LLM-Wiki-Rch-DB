"""Orchestrate the full synthesis rebuild pipeline.

After a new paper is ingested and its registry entry is written to
synthesis-links.json, this script propagates the connections to every
affected file in a single deterministic pass:

    1. build_wiki            — wiki/{stem}.md (paper page + Synthesis Links)
    2. build_synthesis_links — overviews/concepts/projects/questions Related Papers
    3. sync_related_metadata — card YAML related block

Usage:
    python scripts/rebuild_all.py                  # rebuild everything
    python scripts/rebuild_all.py --stem {stem}    # rebuild one paper + cascade
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from llm_wiki_common import add_root_arg, iter_cards, read_yaml_md
from build_wiki import build_wiki
from build_synthesis_links import build_synthesis_links
from sync_related_metadata import sync_card


def rebuild_all(root: Path, stem: str | None = None) -> dict[str, int]:
    """Run the full rebuild pipeline. Returns counters per stage."""
    stats: dict[str, int] = {}

    # Stage 1: rebuild wiki paper pages
    if stem:
        card = root / "cards" / f"{stem}.md"
        if card.exists():
            build_wiki(root, card)
            stats["wiki_pages"] = 1
        else:
            print(f"  WARN: card not found: {card}", file=sys.stderr)
            stats["wiki_pages"] = 0
    else:
        count = 0
        for card in iter_cards(root):
            build_wiki(root, card)
            count += 1
        stats["wiki_pages"] = count

    # Stage 2: rebuild synthesis reverse links (always full — links cascade)
    stats["synthesis_pages"] = build_synthesis_links(root)

    # Stage 3: sync card YAML related metadata
    if stem:
        card = root / "cards" / f"{stem}.md"
        if card.exists():
            sync_card(root, card)
            stats["cards_synced"] = 1
        else:
            stats["cards_synced"] = 0
    else:
        cards = list(iter_cards(root))
        for card in cards:
            sync_card(root, card)
        stats["cards_synced"] = len(cards)

    return stats


def main() -> int:
    parser = argparse.ArgumentParser(description="Rebuild synthesis pipeline")
    add_root_arg(parser)
    parser.add_argument("--stem", default=None, help="Rebuild only this paper (plus cascade)")
    args = parser.parse_args()
    root = Path(args.root).resolve() if args.root else Path.cwd().resolve()

    scope = f"stem={args.stem}" if args.stem else "ALL"
    print(f"=== Rebuild synthesis pipeline ({scope}) ===")
    stats = rebuild_all(root, args.stem)
    for stage, count in stats.items():
        print(f"  {stage}: {count}")
    print("Done.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
