"""Write one source- and citation-grounded deep summary card.

This command deliberately does not call an LLM or invent a summary. An agent
prepares one evidence JSON file after reading the sanitized parsed source.
Page locators are optional: when the parsed source has no reliable page map,
the claim is marked source-text-verified and the page cell is left blank.
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any

from llm_wiki_common import add_root_arg, read_yaml_md, slugify, write_yaml_md
from rekey_record import rekey_record

REQUIRED_EVIDENCE_SECTIONS = ("Theory & Literature Review", "Findings", "Discussion")
PAGE_MARKER = re.compile(r"<!--\s*page:\s*(\d+)\s*-->", re.I)


def normalise(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip().casefold()


def source_pages(source_body: str) -> dict[int, str]:
    matches = list(PAGE_MARKER.finditer(source_body))
    return {
        int(match.group(1)): source_body[match.end() : matches[index + 1].start() if index + 1 < len(matches) else len(source_body)]
        for index, match in enumerate(matches)
    }


def require_string(value: Any, label: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{label} must be a non-empty string")
    return value.strip()


def validate_claim(claim: dict[str, Any], source_body: str, pages: dict[int, str]) -> dict[str, Any]:
    if not isinstance(claim, dict):
        raise ValueError("Each claim must be an object")
    text = require_string(claim.get("claim"), "claim")
    quote = require_string(claim.get("quote"), "quote")
    page, verification = claim.get("page"), claim.get("verification")
    if page in (None, ""):
        page = None
    elif not isinstance(page, int) or page < 1:
        raise ValueError(f"Claim '{text}' must have a positive integer page or a blank page")
    if verification not in {"source_page", "source_text"}:
        raise ValueError(f"Claim '{text}' verification must be source_page or source_text")
    if verification == "source_text" and page is not None:
        raise ValueError(f"Claim '{text}' with source_text verification must leave page blank")
    if normalise(quote) not in normalise(source_body):
        raise ValueError(f"Quote for claim '{text}' was not found in the parsed source")
    if verification == "source_page":
        if page is None:
            raise ValueError(f"Claim '{text}' with source_page verification must declare a page")
        if page not in pages:
            raise ValueError(f"Claim '{text}' declares source page {page}, but that page is unavailable")
        if normalise(quote) not in normalise(pages[page]):
            raise ValueError(f"Quote for claim '{text}' was not found on source page {page}")
    return {"claim": text, "quote": quote, "page": page, "verification": verification}


def validate_evidence(evidence: dict[str, Any], source_body: str) -> list[dict[str, Any]]:
    sections = evidence.get("sections")
    if not isinstance(sections, list):
        raise ValueError("Evidence must contain a sections list")
    pages, validated, headings = source_pages(source_body), [], set()
    for section in sections:
        if not isinstance(section, dict):
            raise ValueError("Each section must be an object")
        heading = require_string(section.get("heading"), "section heading")
        claims = section.get("claims")
        if not isinstance(claims, list) or not claims:
            raise ValueError(f"Section '{heading}' must contain at least one evidence-backed claim")
        headings.add(heading)
        validated.append({"heading": heading, "claims": [validate_claim(item, source_body, pages) for item in claims]})
    missing = [heading for heading in REQUIRED_EVIDENCE_SECTIONS if heading not in headings]
    if missing:
        raise ValueError(f"Evidence is missing required deep-summary sections: {', '.join(missing)}")
    return validated


def render_section(section: dict[str, Any]) -> str:
    lines = [f"## {section['heading']}", ""]
    for item in section["claims"]:
        locator = f"p. {item['page']}; source_page-verified" if item["page"] is not None else "page unavailable; source-text-verified"
        lines += [f"- {item['claim']}", f"  - Evidence: \"{item['quote']}\" ({locator})", ""]
    return "\n".join(lines).rstrip()


def build_body(data: dict[str, Any], evidence: dict[str, Any], sections: list[dict[str, Any]]) -> str:
    keywords = evidence.get("keywords", [])
    if not isinstance(keywords, list):
        raise ValueError("keywords must be a list")
    purpose = require_string(evidence.get("purpose"), "purpose")
    one_sentence = require_string(evidence.get("one_sentence"), "one_sentence")
    limitations = require_string(evidence.get("limitations"), "limitations")
    relevance = require_string(evidence.get("relevance"), "relevance")
    rows = ["| Claim | Direct quotation | Page | Verification |", "|---|---|---:|---|"]
    for section in sections:
        for item in section["claims"]:
            page = item["page"] if item["page"] is not None else ""
            rows.append(f"| {item['claim']} | \"{item['quote']}\" | {page} | {item['verification']} |")
    claims = lambda heading: " ".join(item["claim"] for section in sections if section["heading"] == heading for item in section["claims"])
    return f'''# Quick Card

## Bibliographic Metadata

- Authors: {"; ".join(data.get("authors", []))}
- Year: {data.get("year", "")}
- Design: {data.get("research_design", "")}

## One-sentence Summary

{one_sentence}

## Keywords

{"; ".join(str(item) for item in keywords)}

# Structured Summary

## Purpose

{purpose}

## Findings

{claims("Findings")}

## Discussion & Conclusion

{claims("Discussion")}

# Deep Summary

## Research Problem and Purpose

{purpose}

{"\n\n".join(render_section(section) for section in sections)}

## Directly Citable Evidence

{"\n".join(rows)}

## Limitations

{limitations}

## Relevance to My Study

{relevance}

## Citation Notes

Every claim above is linked to an exact quotation checked against the parsed source. `source_page` denotes a parsed-source page marker; `source_text` denotes an exact source-text match where no reliable page locator was available. PDF re-reading is not part of summary verification; page-level checking is left for manual review.

## Related Links

- Source: [[../sources/{data['stem']}|parsed source]]
- Wiki: [[../wiki/{data['stem']}|synthesis node]]
'''


def migrate_card_schema(data: dict[str, Any]) -> dict[str, Any]:
    summary = data.pop("summary", None) or {}
    summary.setdefault("level", data.pop("summary_level", "deep"))
    summary.setdefault("status", data.pop("status", "unsummarized"))
    summary.setdefault("structure_policy", data.pop("structure_policy", "source_structure"))
    data["summary"] = summary
    for obsolete in ("paper_id", "file_name", "topics", "projects", "related", "review_log"):
        data.pop(obsolete, None)
    return data


def build_summary_card(root: Path, source: Path, evidence: dict[str, Any]) -> Path:
    source_meta, source_body = read_yaml_md(source)
    stem, record_id = source_meta.get("stem") or source.stem, source_meta.get("record_id") or f"paper:{source.stem}"
    if evidence.get("record_id") and evidence["record_id"] != record_id:
        raise ValueError("evidence record_id does not match the source record_id")
    sections = validate_evidence(evidence, source_body)
    final_title = require_string(evidence.get("title"), "title")
    final_design = require_string(evidence.get("research_design"), "research_design")
    final_authors = evidence.get("authors", [])
    if not isinstance(final_authors, list) or not final_authors:
        raise ValueError("authors must be a non-empty list")
    if not isinstance(evidence.get("keywords", []), list):
        raise ValueError("keywords must be a list")
    for field in ("purpose", "one_sentence", "limitations", "relevance"):
        require_string(evidence.get(field), field)
    # The finalized summary metadata becomes the final identity of the record.
    # Rekey before writing the canonical card so all downstream rebuilds use
    # the same stem for PDF, source, card, wiki, and generated indexes.
    source, stem, record_id = rekey_record(root, source, evidence)
    source_meta, source_body = read_yaml_md(source)
    card_path = root / "cards" / f"{stem}.md"
    data, _ = read_yaml_md(card_path if card_path.exists() else root / "templates" / "template-paper-summary.md")
    data = migrate_card_schema(data)
    data.update({"record_id": record_id, "stem": stem, "title": final_title, "authors": final_authors, "year": str(evidence.get("year", "")), "research_design": final_design, "citation_key": evidence.get("citation_key") or slugify(f"{final_authors[0]} {evidence.get('year', '')}"), "tags": evidence.get("keywords", [])})
    if evidence.get("doi"):
        data["doi"] = str(evidence["doi"])
        data["url"] = str(evidence["doi"])
    citation_info = data.setdefault("citation_info", {})
    for field in ("source_type", "source_title", "volume", "issue", "pages", "publisher"):
        if evidence.get(field) not in (None, ""):
            citation_info[field] = evidence[field]
    data.setdefault("provenance", {}).update({"source_path": str(source.relative_to(root))})
    data["summary"].update({"level": "deep", "status": "summarized", "structure_policy": "source_structure"})
    quote_status = "partial" if any(item["verification"] == "source_text" for section in sections for item in section["claims"]) else "verified"
    data["verification"] = {"summary_verified": False, "quote_verification_status": quote_status, "quote_verification_pass_rate": 1.0, "claim_verification_pass_rate": 1.0, "requires_human_review": True, "verified_at": ""}
    write_yaml_md(card_path, data, build_body(data, evidence, sections))
    return card_path


def main() -> int:
    parser = argparse.ArgumentParser(description="Write one source- and citation-grounded deep summary card.")
    add_root_arg(parser)
    parser.add_argument("source", help="Path to sources/{stem}.md")
    parser.add_argument("--evidence", required=True, help="Per-paper evidence JSON")
    args = parser.parse_args()
    root = Path(args.root).resolve() if args.root else Path.cwd().resolve()
    evidence = json.loads(Path(args.evidence).read_text(encoding="utf-8"))
    if not isinstance(evidence, dict):
        raise SystemExit("Evidence JSON must be an object")
    print(build_summary_card(root, Path(args.source).resolve(), evidence).relative_to(root))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
