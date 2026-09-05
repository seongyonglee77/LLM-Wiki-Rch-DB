from __future__ import annotations

import argparse
import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import yaml


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def root_from_arg(value: str | None = None) -> Path:
    return Path(value).resolve() if value else Path.cwd().resolve()


def ensure_root(root: Path) -> None:
    required = ["cards", "sources", "wiki", "registry", "indexes", "qc", "logs"]
    missing = [name for name in required if not (root / name).exists()]
    if missing:
        raise SystemExit(f"Not an llm-wiki root; missing: {', '.join(missing)}")


def file_sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def slugify(text: str, fallback: str = "untitled") -> str:
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    text = re.sub(r"-+", "-", text).strip("-")
    return text or fallback


def split_frontmatter(text: str) -> tuple[dict[str, Any], str]:
    if not text.startswith("---\n"):
        return {}, text
    end = text.find("\n---\n", 4)
    if end == -1:
        return {}, text
    raw = text[4:end]
    body = text[end + 5 :]
    data = yaml.safe_load(raw) or {}
    if not isinstance(data, dict):
        data = {}
    return data, body


def read_yaml_md(path: Path) -> tuple[dict[str, Any], str]:
    return split_frontmatter(path.read_text(encoding="utf-8"))


def write_yaml_md(path: Path, data: dict[str, Any], body: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    raw = yaml.safe_dump(data, sort_keys=False, allow_unicode=True).strip()
    path.write_text(f"---\n{raw}\n---\n{body.lstrip()}", encoding="utf-8")


def iter_cards(root: Path) -> list[Path]:
    return sorted((root / "cards").glob("*.md"))


def load_registry(root: Path) -> list[dict[str, Any]]:
    path = root / "registry" / "works.jsonl"
    if not path.exists():
        return []
    rows: list[dict[str, Any]] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.strip():
            rows.append(json.loads(line))
    return rows


def write_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("".join(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n" for row in rows), encoding="utf-8")


def add_root_arg(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--root", default=None, help="llm-wiki root; defaults to current directory")

