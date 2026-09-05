"""Optional migration hook for a project with existing cards.

This public template deliberately contains no bundled paper records or
paper-specific summaries. An agent should write source-grounded English
content into a card after ingest, then run the deterministic rebuild steps.
"""

from __future__ import annotations

import argparse
from pathlib import Path

from llm_wiki_common import add_root_arg


def main() -> int:
    parser = argparse.ArgumentParser()
    add_root_arg(parser)
    args = parser.parse_args()
    root = Path(args.root).resolve() if args.root else Path.cwd().resolve()
    cards = sorted((root / "cards").glob("*.md"))
    print(f"No bundled summaries are included in this public template; found {len(cards)} local card(s).")
    print("Write source-grounded English summaries through the agent workflow, then rebuild registry, indexes, refs.bib, wiki, HTML, and QC.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
