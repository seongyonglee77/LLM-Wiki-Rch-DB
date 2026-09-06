"""Create a token-efficient, temporary source view for the summary agent.

The canonical parsed Markdown is never modified. Embedded Base64 images are
replaced with a short placeholder because they carry no useful text for a
paper summary and can dominate the model input.
"""
from __future__ import annotations

import argparse
import os
import re
import tempfile
from pathlib import Path

IMAGE_DATA_URI = re.compile(
    r"!\[[^\]]*\]\(data:image/[^;\s]+;base64,[^)]*\)",
    re.IGNORECASE,
)


def sanitize_summary_source(text: str) -> str:
    return IMAGE_DATA_URI.sub("![embedded image omitted for summary]", text)


def main() -> int:
    parser = argparse.ArgumentParser(description="Prepare a non-canonical, token-efficient source view for summarization.")
    parser.add_argument("source", type=Path)
    parser.add_argument("--output", type=Path, default=None, help="Optional output path; otherwise use the OS temporary directory")
    args = parser.parse_args()
    source = args.source.resolve()
    if not source.exists() or source.suffix.lower() != ".md":
        raise SystemExit(f"Markdown source not found: {source}")
    if args.output:
        output = args.output.resolve()
    else:
        fd, temp_name = tempfile.mkstemp(prefix="llm-wiki-summary-", suffix=".md")
        os.close(fd)
        output = Path(temp_name)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(sanitize_summary_source(source.read_text(encoding="utf-8")), encoding="utf-8")
    print(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
