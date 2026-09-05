from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

from llm_wiki_common import add_root_arg, read_yaml_md, write_yaml_md


def wiki_language(root: Path) -> str:
    try:
        config = json.loads((root / "km-config.json").read_text(encoding="utf-8"))
        return str(config.get("wiki_language", "en")).lower()
    except (OSError, ValueError):
        return "en"


def build_wiki(root: Path, card: Path) -> Path:
    data, card_body = read_yaml_md(card)
    stem = data.get("stem") or card.stem
    wiki_path = root / "wiki" / f"{stem}.md"

    def section(name: str) -> str:
        match = re.search(rf"^## {re.escape(name)}\s*$([\s\S]*?)(?=^## |^# |\Z)", card_body, re.MULTILINE)
        return re.sub(r"\s+", " ", match.group(1)).strip() if match else ""

    summary = section("One-sentence Summary")
    findings = section("Findings")
    ko = wiki_language(root) == "ko"
    labels = ("요약", "핵심 결과", "메모", "상세 요약 카드", "전체 추출 원문") if ko else ("Summary", "Key Findings", "Notes", "summary card", "parsed source")
    note = "이 문서는 탐색과 종합을 위한 위키 노드입니다. 상세한 근거와 주장은 영어 카드와 source에서 확인합니다." if ko else "This node is a navigation layer. Detailed evidence belongs in the English card and parsed source."
    body = f"""# {data.get('title') or stem}

- Card: [[../cards/{stem}|{labels[3]}]]
- Source: [[../sources/{stem}|{labels[4]}]]
- Bibliography key: `@{data.get('citation_key', '')}`

## {labels[0]}

{summary or ('요약은 ingest 후 작성됩니다.' if ko else 'Summary is written after ingest.')}

## {labels[1]}

{findings or ('핵심 결과는 ingest 후 작성됩니다.' if ko else 'Key findings are written after ingest.')}

## {labels[2]}

{note}
"""
    wiki_data = {
        "record_id": data.get("record_id", ""),
        "stem": stem,
        "metadata_status": data.get("metadata_status", "open"),
        "citation_key": data.get("citation_key", ""),
    }
    write_yaml_md(wiki_path, wiki_data, body)
    return wiki_path


def main() -> int:
    parser = argparse.ArgumentParser()
    add_root_arg(parser)
    parser.add_argument("card")
    args = parser.parse_args()
    root = Path(args.root).resolve() if args.root else Path.cwd().resolve()
    print(build_wiki(root, Path(args.card).resolve()))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
