"""Deterministic post-parse paper filename normalization.

The parser has already read the PDF before this module runs.  No LLM is used:
the first source heading, author line, and nearby publication year are enough to
produce a stable human-readable stem.  Ambiguous metadata falls back safely and
is left for metadata review rather than blocking ingest.
"""
from __future__ import annotations

import re
from html import unescape
from pathlib import Path


STOPWORDS = {"a", "an", "and", "for", "in", "of", "on", "the", "to", "with"}
YEAR_RE = re.compile(r"\b((?:19|20)\d{2})\b")
HEADING_SKIP = {
    "research article",
    "article",
    "abstract",
    "a b s t r a c t",
    "references",
}


def _clean_token(value: str) -> str:
    value = re.sub(r"[^A-Za-z0-9-]+", "-", value).strip("-")
    return value[:40]


def _body_lines(source: str) -> list[str]:
    lines = source.splitlines()
    if lines and lines[0].strip() == "---":
        try:
            end = next(index for index, line in enumerate(lines[1:], 1) if line.strip() == "---")
            lines = lines[end + 1 :]
        except StopIteration:
            pass
    return lines


def _author_surnames(line: str) -> list[str]:
    """Extract surname-like tokens from one compact author line."""
    line = unescape(re.sub(r"\[[^\]]+\]\([^)]*\)", "", line))
    if "@" in line or line.lstrip().startswith(("-", "*")):
        return []
    surnames: list[str] = []
    for part in re.split(r"\s+(?:and|&)\s+|\s*,\s*", line, flags=re.I):
        part = re.sub(r"\b[a-z](?:\s*,\s*\*)?\s*$", "", part.strip())
        part = re.sub(r"[*†‡]+", "", part).strip()
        tokens = re.findall(r"[A-Z][A-Za-z'’-]*", part)
        if len(tokens) >= 2:
            surnames.append(tokens[-1])
    if not surnames:
        tokens = re.findall(r"[A-Z][A-Za-z'’-]*", line)
        if len(tokens) >= 2:
            surnames.append(tokens[-1])
    return surnames


def _title_index(lines: list[str]) -> int | None:
    headings = [(index, unescape(line[3:].strip())) for index, line in enumerate(lines) if line.startswith("## ")]
    for index, candidate in headings:
        lowered = candidate.casefold()
        if lowered in HEADING_SKIP or lowered.startswith("j. "):
            continue
        if re.match(r"^\d+(?:\.\d+)*\.", candidate) or "doi.org/" in lowered:
            continue
        if candidate.startswith("[http") or "journal homepage" in lowered:
            continue
        if any("journal homepage" in nearby.casefold() for nearby in lines[index + 1 : index + 3]):
            continue
        for nearby in lines[index + 1 : index + 7]:
            if not nearby.strip() or nearby.lstrip().startswith("<!--"):
                continue
            if _author_surnames(nearby):
                return index
            if nearby.startswith("## "):
                break
    for index, candidate in headings:
        lowered = candidate.casefold()
        if lowered not in HEADING_SKIP and not re.match(r"^\d+(?:\.\d+)*\.", candidate):
            return index
    return None


def _title(source: str) -> str:
    lines = _body_lines(source)[:100]
    index = _title_index(lines)
    return lines[index][3:].strip() if index is not None else "Untitled Paper"


def _authors(source: str) -> list[str]:
    lines = _body_lines(source)[:100]
    index = _title_index(lines)
    if index is not None:
        for line in lines[index + 1 : index + 8]:
            if not line.strip() or line.lstrip().startswith("<!--"):
                continue
            names = _author_surnames(line)
            if names:
                return names[:3]
    return ["Unknown"]


def _year(source: str) -> str:
    lines = _body_lines(source)[:120]
    for line in lines:
        if "©" in line or re.search(r"\bcopyright\b", line, re.I):
            match = YEAR_RE.search(line)
            if match:
                return match.group(1)
    for line in lines:
        if re.search(r"\b(cite this article|published|accepted|available online)\b", line, re.I):
            years = YEAR_RE.findall(line)
            if years:
                return years[-1]
    for line in lines:
        match = YEAR_RE.search(line)
        if match:
            return match.group(1)
    return "0000"


def canonical_stem(source: str, fallback: str = "untitled") -> str:
    head = source[:12000]
    return canonical_stem_from_metadata(_title(head), _authors(head), _year(head), fallback)


def _metadata_surname(author: object) -> str:
    """Return a stable filename token from a summary-card author value."""
    text = unescape(str(author or "")).strip()
    if not text:
        return ""
    if "," in text:
        text = text.split(",", 1)[0].strip()
    else:
        text = text.split()[-1]
    return _clean_token(text)


def canonical_stem_from_metadata(
    title: object,
    authors: object,
    year: object,
    fallback: str = "untitled",
) -> str:
    """Build the canonical YYYY_Author_ShortTitle stem from final metadata."""
    year_match = YEAR_RE.search(str(year or ""))
    year_token = year_match.group(1) if year_match else "0000"
    title_text = str(title or "").strip()
    title_words = []
    for word in re.findall(r"[A-Za-z0-9]+(?:-[A-Za-z0-9]+)?", title_text):
        if word.casefold() not in STOPWORDS:
            title_words.append(_clean_token(word.title()))
        if len(title_words) == 3:
            break
    title_words = title_words or [_clean_token(str(fallback).replace("-", " ").title()) or "Paper"]
    author_values = authors if isinstance(authors, list) else [authors]
    author_tokens = [_metadata_surname(value) for value in author_values[:3]]
    author_tokens = [value for value in author_tokens if value] or ["Unknown"]
    return "_".join([year_token, "-".join(author_tokens), "-".join(title_words)])[:180].rstrip("_")


def collision_stem(stem: str, existing: set[str]) -> str:
    if stem not in existing:
        return stem
    parts = stem.split("_", 2)
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for suffix in alphabet:
        candidate = f"{parts[0]}_{parts[1]}-{suffix}_{parts[2]}" if len(parts) == 3 else f"{stem}-{suffix}"
        if candidate not in existing:
            return candidate
    number = 2
    candidate = f"{parts[0]}_{parts[1]}-{number}_{parts[2]}" if len(parts) == 3 else f"{stem}-{number}"
    while candidate in existing:
        number += 1
        candidate = f"{parts[0]}_{parts[1]}-{number}_{parts[2]}" if len(parts) == 3 else f"{stem}-{number}"
    return candidate


def existing_layer_stems(root: Path, source_path: Path) -> set[str]:
    stems: set[str] = set()
    for folder, pattern in (("sources", "*.md"), ("cards", "*.md"), ("wiki", "*.md"), ("papers", "*.pdf")):
        base = root / folder
        if not base.exists():
            continue
        for path in base.glob(pattern):
            if path.resolve() != source_path.resolve():
                stems.add(path.stem)
    return stems


def canonicalize_paths(root: Path, provisional_stem: str, source_path: Path, source_text: str) -> tuple[str, Path]:
    """Rename a parsed source to a collision-safe canonical stem."""
    proposed = canonical_stem(source_text, provisional_stem)
    existing = existing_layer_stems(root, source_path)
    stem = collision_stem(proposed, existing)
    target = source_path.with_name(f"{stem}.md")
    if target != source_path:
        source_path.replace(target)
    return stem, target
