"""Data-driven paper-to-synthesis relationships.

The relationship registry is curated data, not renderer code. A paper may link
to zero or more pages in each synthesis category; the only mandatory rule is
at least one relevant overview or concept page, with a reverse link.
"""
from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any, TypedDict


class SynthesisLink(TypedDict, total=False):
    category: str
    path: str
    label: str
    relation: str


CATEGORIES = ("overviews", "concepts", "projects", "questions")


def _registry(root: Path) -> dict[str, Any]:
    path = root / "registry" / "synthesis-links.json"
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return {"papers": {}}
    return value if isinstance(value, dict) else {"papers": {}}


def _label(path: str) -> str:
    return re.sub(r"[-_]+", " ", path.rsplit("/", 1)[-1]).strip().title()


def _normalise(category: str, item: Any) -> SynthesisLink | None:
    if isinstance(item, str) and item.strip():
        return {"category": category, "path": item.strip(), "label": _label(item)}
    if isinstance(item, dict) and isinstance(item.get("path"), str) and item["path"].strip():
        result: SynthesisLink = {
            "category": category,
            "path": item["path"].strip(),
            "label": str(item.get("label") or _label(item["path"])),
        }
        if item.get("relation"):
            result["relation"] = str(item["relation"])
        return result
    return None


def synthesis_links_for(root: Path, stem: str) -> list[SynthesisLink]:
    record = (_registry(root).get("papers") or {}).get(stem, {})
    if not isinstance(record, dict):
        return []
    links: list[SynthesisLink] = []
    for category in CATEGORIES:
        values = record.get(category, [])
        if not isinstance(values, list):
            continue
        for item in values:
            link = _normalise(category, item)
            if link:
                links.append(link)
    return links


def related_metadata(root: Path, stem: str) -> dict[str, list[str]]:
    """Return the generated card-YAML relationship block for a paper."""
    links = synthesis_links_for(root, stem)
    return {
        "wiki": [f"wiki/{stem}"],
        **{category: [f"wiki/{item['path']}" for item in links if item["category"] == category] for category in CATEGORIES},
        "supersedes": [],
        "superseded_by": [],
    }


def render_links(root: Path, stem: str, prefix: str) -> str:
    """Render links relative to the current Markdown page."""
    return "\n".join(
        f"- [[{prefix}{item['path']}|{item['label']}]]"
        for item in synthesis_links_for(root, stem)
    )
