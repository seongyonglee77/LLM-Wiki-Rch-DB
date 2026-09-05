from __future__ import annotations

import argparse
import json
from pathlib import Path

from llm_wiki_common import add_root_arg, iter_cards, read_yaml_md, utc_now


def audit(root: Path, include_locked: bool = False) -> dict:
    records = []
    for card in iter_cards(root):
        data, _ = read_yaml_md(card)
        status = data.get("metadata_status", "open")
        if status == "locked" and not include_locked:
            continue
        records.append(
            {
                "record_id": data.get("record_id", f"paper:{card.stem}"),
                "stem": data.get("stem", card.stem),
                "metadata_status": status,
                "classification": "unavailable",
                "recommendation": "No external audit source was queried by this offline script.",
                "card_changed": False,
                "refs_changed": False,
            }
        )
    result = {"generated_at": utc_now(), "include_locked": include_locked, "records": records}
    (root / "qc" / "metadata_audit.json").write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    lines = ["# Metadata Audit", "", f"- Generated at: `{result['generated_at']}`", f"- Include locked: `{include_locked}`", ""]
    for item in records:
        lines.append(f"- `{item['record_id']}` - `{item['metadata_status']}` - `{item['classification']}`")
    (root / "qc" / "metadata_audit.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    add_root_arg(parser)
    parser.add_argument("--include-locked", action="store_true")
    args = parser.parse_args()
    root = Path(args.root).resolve() if args.root else Path.cwd().resolve()
    print(json.dumps(audit(root, args.include_locked), ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

