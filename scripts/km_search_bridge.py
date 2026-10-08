#!/usr/bin/env python3
"""Read-only KM corpus guard and deterministic restricted search; no dependencies."""
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import re
import urllib.error
import urllib.parse
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
SEARCH_PATHS = ("indexes", "wiki", "cards", "sources")


def context(root: Path) -> dict:
    root = root.resolve(strict=True)
    config = json.loads((root / "km-config.json").read_text(encoding="utf-8-sig"))
    endpoint = config.get("linking", {}).get("semantic_adapter", {}).get("endpoint")
    return {"db_root": str(root), "search_paths": list(SEARCH_PATHS),
            "endpoint": endpoint or os.environ.get("GRAPHRAG_API_URL", "http://127.0.0.1:8400"),
            "engine_order": ["GraphRAG", "Obsidian CLI", "Obsidian MCP", "text"],
            "read_order": list(SEARCH_PATHS), "mode": "read-only"}


def note_path(root: Path, value: str, allow_sources: bool = False) -> Path:
    candidate = (root / value.replace("\\", "/")).resolve(strict=True)
    relative = candidate.relative_to(root.resolve())
    allowed = SEARCH_PATHS if allow_sources else SEARCH_PATHS[:3]
    if relative.parts[0] not in allowed or candidate.suffix.lower() != ".md" or not candidate.is_file():
        raise ValueError("Result outside permitted Markdown corpus")
    return candidate


def normal(text: str) -> str:
    return " ".join(text.split())


def text_search(root: Path, query: str, deep: bool = False, sources: bool = False) -> list[dict]:
    words = [w.casefold() for w in re.findall(r"[\w-]+", query) if len(w) > 1]
    if not words:
        return []
    hits = []
    for stage, folder in enumerate(SEARCH_PATHS if sources else SEARCH_PATHS[:3]):
        for raw in sorted((root / folder).rglob("*.md")):
            try:
                path = note_path(root, str(raw), sources)
                body = path.read_text(encoding="utf-8-sig")
            except (ValueError, OSError):
                continue
            folded = body.casefold()
            matched = sum(word in folded for word in words)
            if matched:
                lines = [line for line in body.splitlines() if any(w in line.casefold() for w in words)]
                hits.append({"path": path.relative_to(root).as_posix(), "score": matched / len(words),
                             "stage": stage, "snippet": " ".join(lines[:2])[:500]})
    hits.sort(key=lambda x: (-x["score"], x["stage"], x["path"]))
    return hits[:10 if deep else 5]


def fetch_json(url: str) -> dict:
    with urllib.request.urlopen(url, timeout=15) as response:
        return json.load(response)


def validate_rag_result(root: Path, result: dict, note: dict) -> dict:
    path = note_path(root, str(result.get("source_note", "")))
    returned = note_path(root, str(note.get("note_path", "")))
    if returned != path:
        raise ValueError("GraphRAG note path mismatch")
    body = normal(str(note.get("body", "")))
    if not body or body not in normal(path.read_text(encoding="utf-8-sig")):
        raise ValueError("GraphRAG corpus/content unproven")
    return {"path": path.relative_to(root).as_posix(), "entity": result.get("entity", ""),
            "score": result.get("score"), "corpus_verified": True}


def rag_search(root: Path, query: str, deep: bool = False) -> dict:
    cfg = context(root)
    endpoint = cfg["endpoint"].rstrip("/")
    if urllib.parse.urlparse(endpoint).scheme not in {"http", "https"}:
        raise ValueError("GraphRAG endpoint must be HTTP(S)")
    params = urllib.parse.urlencode({"q": query, "top_k": 10 if deep else 5, "mode": "hybrid"})
    rejected = []
    accepted = []
    try:
        payload = fetch_json(f"{endpoint}/api/search?{params}")
        rows = payload.get("results", []) if isinstance(payload, dict) else []
        if not isinstance(rows, list):
            raise ValueError("Invalid GraphRAG response shape")
        for result in rows:
            try:
                note_path(root, str(result.get("source_note", "")))
                params = urllib.parse.urlencode({"name": result.get("entity", ""), "max_chars": 2500})
                note = fetch_json(f"{endpoint}/api/note?{params}")
                accepted.append(validate_rag_result(root, result, note))
            except (OSError, ValueError, TypeError, AttributeError) as exc:
                rejected.append(str(exc))
        return {**cfg, "engine": "GraphRAG", "state": "verified" if accepted else "empty-or-unproven-corpus",
                "results": accepted, "rejected": rejected, "fallback_required": not bool(accepted)}
    except (OSError, ValueError) as exc:
        return {**cfg, "engine": "GraphRAG", "state": "unreachable-or-invalid", "reason": str(exc),
                "results": [], "fallback_required": True}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--db-root", type=Path, default=ROOT)
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("context")
    for command in ("rag", "text"):
        p = sub.add_parser(command)
        p.add_argument("--query", required=True)
        p.add_argument("--deep", action="store_true")
        if command == "text":
            p.add_argument("--sources", action="store_true")
    args = parser.parse_args()
    root = args.db_root.resolve()
    try:
        if args.command == "context":
            result = context(root)
        elif args.command == "rag":
            result = rag_search(root, args.query, args.deep)
        else:
            result = {**context(root), "engine": "text", "results": text_search(root, args.query, args.deep, args.sources)}
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0
    except (OSError, ValueError) as exc:
        parser.exit(1, f"KM binding error: {exc}\n")


if __name__ == "__main__":
    raise SystemExit(main())
