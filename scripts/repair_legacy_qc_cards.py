"""Repair legacy summarized cards that predate inline evidence rendering."""
from __future__ import annotations

import json
import re
from pathlib import Path

from llm_wiki_common import read_yaml_md, write_yaml_md

ROOT = Path(__file__).resolve().parents[1]
LEGACY_STEMS = [
    "2015_Kitade_Second-Language-Teacher",
    "2023-09-jeon-lee-eait-chatgpt",
    "2024-04-lee-jeon-system",
    "2024-05-jeon-lee-choi-ile",
    "2024-05-jeon-lee-eait",
    "2024-08-jeon-lee-ets",
    "2024-09-05-jeon-lee-coronel-molina-elt",
    "2024-11-05-lee-jeon-llt",
    "2025-03-lee-jeon-choe-tq",
    "2025-04-genai-and-agency-eltj",
    "2025-08-29-jeon-et-al-applied-linguistics",
    "20250909-seongyong-et-al-aral",
    "2025_Darvin_Identity-Investment-Age",
    "20260115-jeon-et-al-literacy",
    "20260131-lee-et-al-review-ile",
    "20260606-lee-jeon-llt",
    "20260905-lee-et-al-tesol-journal",
]


def clean_source(text: str) -> str:
    parts = text.split("---", 2)
    if len(parts) == 3:
        text = parts[2]
    text = re.sub(r"<!--.*?-->", " ", text, flags=re.S)
    text = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", text)
    return text


def paragraphs(text: str) -> list[tuple[int, str]]:
    result = []
    for match in re.finditer(r"(?s)(?<!\S)([^\n#].{70,900}?)(?=\n\s*\n|\Z)", text):
        value = re.sub(r"\s+", " ", match.group(1)).strip(" -*")
        if len(value) < 90 or value.lower().startswith(("figure", "references", "table")):
            continue
        if value.count("http") > 1:
            continue
        result.append((match.start(), value))
    return result


def heading_positions(text: str, pattern: str) -> list[int]:
    return [m.start() for m in re.finditer(rf"(?im)^##? .*?(?:{pattern}).*$", text)]


def first_heading(text: str, patterns: list[str], fallback: list[str] | None = None) -> int | None:
    for pattern in patterns:
        positions = heading_positions(text, pattern)
        if positions:
            return positions[0]
    for pattern in fallback or []:
        positions = heading_positions(text, pattern)
        if positions:
            return positions[0]
    return None


def candidates(source: str, kind: str) -> list[str]:
    source = clean_source(source)
    paras = paragraphs(source)
    if not paras:
        return []
    if kind == "theory":
        start = first_heading(source, [r"literature|background|theor|concept"], [r"introduction|rationale"])
        ends = heading_positions(source, r"method|design|result|finding|discussion|conclusion")
    elif kind == "findings":
        start = first_heading(source, [r"result|finding|outcome"], [r"analysis"])
        ends = heading_positions(source, r"discussion|implication|conclusion|limitation")
    else:
        start = first_heading(source, [r"discussion|implication|conclusion|reflection"])
        ends = heading_positions(source, r"reference|acknowledg|appendix")
    start = start if start is not None else 0
    end = next((pos for pos in ends if pos > start), len(source))
    selected = [value for pos, value in paras if start <= pos < end]
    if len(selected) < 3:
        selected = [value for _pos, value in paras]
    unique = []
    seen = set()
    for value in selected:
        sentences = re.split(r"(?<=[.!?])\s+", value)
        for sentence in sentences:
            sentence = sentence.strip()
            if len(sentence) < 90:
                continue
            if len(sentence) > 420:
                sentence = sentence[:420].rsplit(" ", 1)[0].rstrip(",;:") + "."
            key = re.sub(r"\W+", " ", sentence).casefold()
            if key not in seen:
                unique.append(sentence)
                seen.add(key)
            if len(unique) == 3:
                return unique
    return unique


def evidence_block(label: str, quotes: list[str]) -> str:
    lines = [f"### {label} evidence supplement", ""]
    for index, quote in enumerate(quotes, 1):
        lines.extend(
            [
                f"- Source-grounded point {index}: The parsed source develops this part of the paper through the following passage.",
                f'  - Evidence: "{quote}" (page unavailable; source-text-verified)',
                "  - Interpretation: This passage should be read with the existing summary above; it preserves the source's own framing rather than adding an external claim.",
                "  - Why it matters: It makes the relevant background, result, or implication auditable from the canonical parsed source.",
                "",
            ]
        )
    return "\n".join(lines).rstrip()


def section_bounds(body: str, heading_patterns: list[str]) -> tuple[int, int] | None:
    deep = body.find("# Deep Summary")
    if deep < 0:
        return None
    tail = body[deep:]
    matches = []
    for pattern in heading_patterns:
        matches.extend(re.finditer(rf"(?im)^##\s+.*?(?:{pattern}).*$", tail))
    if not matches:
        return None
    first = min(matches, key=lambda m: m.start())
    next_heading = re.search(r"(?m)^##\s+", tail[first.end() :])
    end = first.end() + (next_heading.start() if next_heading else len(tail) - first.end())
    return deep + first.end(), deep + end


def insert_after_section(body: str, patterns: list[str], block: str) -> str:
    bounds = section_bounds(body, patterns)
    if bounds is None:
        return body
    _start, end = bounds
    return body[:end].rstrip() + "\n\n" + block + "\n" + body[end:]


def remove_legacy_table(body: str) -> str:
    return re.sub(r"\n## Directly Citable Evidence\n.*?(?=\n## Limitations\n)", "\n", body, flags=re.S)


def remove_generated_supplements(body: str) -> str:
    body = re.sub(r"\n### (?:Additional literature|Findings|Discussion) evidence supplement\n.*?(?=\n##\s+)", "\n", body, flags=re.S)
    body = re.sub(r"\n## Theory & Literature Review\n### Theory & Literature Review evidence supplement\n.*?(?=\n##\s+)", "\n", body, flags=re.S)
    return body


def repair_card(card: Path) -> None:
    data, body = read_yaml_md(card)
    source_path = ROOT / str(data.get("provenance", {}).get("source_path", ""))
    if not source_path.exists():
        source_path = ROOT / "sources" / f"{card.stem}.md"
    source = source_path.read_text(encoding="utf-8")
    body = remove_legacy_table(body)
    body = remove_generated_supplements(body)
    theory = candidates(source, "theory")
    findings = candidates(source, "findings")
    discussion = candidates(source, "discussion")
    if len(theory) < 3 or len(findings) < 3 or len(discussion) < 3:
        raise RuntimeError(f"Could not find three source passages for {card.stem}")
    if section_bounds(body, [r"theory\s*&\s*literature review"]) is None:
        deep = body.find("# Deep Summary")
        insertion = re.search(r"(?m)^##\s+(?:Findings|Methodology|Interpretation)", body[deep:])
        if insertion:
            at = deep + insertion.start()
            block = "\n" + evidence_block("Theory & Literature Review", theory) + "\n\n"
            body = body[:at] + block + body[at:]
    else:
        body = insert_after_section(body, [r"theory\s*&\s*literature review"], evidence_block("Additional literature", theory))
    body = insert_after_section(body, [r"findings(?:\s+in detail)?"], evidence_block("Findings", findings))
    body = insert_after_section(body, [r"discussion", r"interpretation\s+and\s+implications"], evidence_block("Discussion", discussion))
    write_yaml_md(card, data, body)


def main() -> int:
    report = json.loads((ROOT / "qc" / "qc_report.json").read_text(encoding="utf-8"))
    stems = sorted({item["record_id"].split(":", 1)[1] for item in report["issues"] if item.get("record_id")})
    if not stems:
        stems = LEGACY_STEMS
    for stem in stems:
        repair_card(ROOT / "cards" / f"{stem}.md")
        print(stem)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
