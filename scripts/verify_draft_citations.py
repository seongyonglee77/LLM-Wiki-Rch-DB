from __future__ import annotations

import argparse
import re
from pathlib import Path


def bib_keys(path: Path) -> set[str]:
    if not path.exists():
        raise SystemExit(f"Bibliography not found: {path}")
    return set(re.findall(r"(?m)^@\w+\{([^,]+),", path.read_text(encoding="utf-8")))


def draft_keys(path: Path) -> set[str]:
    text = path.read_text(encoding="utf-8")
    keys = set()
    for group in re.findall(r"\[@([^\]]+)\]", text):
        for part in re.split(r"[;,\s]+", group):
            part = part.strip().lstrip("@")
            if part:
                keys.add(part)
    return keys


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("draft")
    parser.add_argument("bibliography")
    parser.add_argument("--out", default=None)
    args = parser.parse_args()
    draft = Path(args.draft).resolve()
    bib = Path(args.bibliography).resolve()
    cited = draft_keys(draft)
    available = bib_keys(bib)
    missing = sorted(cited - available)
    unused = sorted(available - cited)
    lines = ["key\tstatus"]
    for key in sorted(cited):
        lines.append(f"{key}\t{'missing' if key in missing else 'ok'}")
    if args.out:
        Path(args.out).write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"cited={len(cited)} missing={len(missing)} unused_bib={len(unused)}")
    if missing:
        print("missing: " + ", ".join(missing))
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

