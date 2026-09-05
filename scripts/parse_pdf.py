from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
from pathlib import Path

from llm_wiki_common import add_root_arg, file_sha256, slugify, utc_now


def extract_with_docling(pdf: Path) -> tuple[str, str]:
    from docling.document_converter import DocumentConverter

    result = DocumentConverter().convert(str(pdf))
    doc = result.document
    if hasattr(doc, "export_to_markdown"):
        return doc.export_to_markdown(), "docling"
    if hasattr(doc, "export_to_text"):
        return doc.export_to_text(), "docling"
    raise RuntimeError("Docling converted the PDF but exposed no Markdown/text exporter")


def extract_with_pypdf(pdf: Path) -> tuple[str, str]:
    from pypdf import PdfReader

    reader = PdfReader(str(pdf))
    parts = []
    for idx, page in enumerate(reader.pages, start=1):
        text = page.extract_text() or ""
        parts.append(f"\n\n<!-- page: {idx} -->\n\n{text.strip()}")
    return "\n".join(parts).strip(), "pypdf_fallback"


def extract_with_opendataloader(pdf: Path) -> tuple[str, str]:
    executable = shutil.which("opendataloader-pdf")
    if not executable:
        raise RuntimeError("opendataloader-pdf executable not found")
    result = subprocess.run(
        [executable, str(pdf)],
        check=True,
        capture_output=True,
        text=True,
        timeout=180,
    )
    text = result.stdout.strip()
    if not text:
        raise RuntimeError("opendataloader-pdf produced no stdout text")
    return text, "opendataloader-pdf_fallback"


def extract_with_pdftotext(pdf: Path) -> tuple[str, str]:
    executable = shutil.which("pdftotext")
    if not executable:
        raise RuntimeError("pdftotext executable not found")
    result = subprocess.run(
        [executable, "-layout", str(pdf), "-"],
        check=True,
        capture_output=True,
        text=True,
        timeout=180,
    )
    text = result.stdout.strip()
    if not text:
        raise RuntimeError("pdftotext produced no stdout text")
    return text, "pdftotext_fallback"


def extract_with_fallbacks(pdf: Path, warnings: list[str]) -> tuple[str, str]:
    extractors = [
        ("Docling", extract_with_docling),
        ("opendataloader-pdf", extract_with_opendataloader),
        ("pypdf", extract_with_pypdf),
        ("pdftotext", extract_with_pdftotext),
    ]
    errors = []
    for name, extractor in extractors:
        try:
            text, parser = extractor(pdf)
            if len(text.strip()) < 200:
                raise RuntimeError("extracted text is under 200 characters")
            if errors:
                warnings.extend(errors)
            return text, parser
        except Exception as exc:
            errors.append(f"{name} unavailable or failed: {exc}")
    warnings.extend(errors)
    raise RuntimeError("All PDF extractors failed")


def guess_stem(pdf: Path, text: str, source_hash: str) -> str:
    # Prefer the curated file name for stable identity. Extracted first lines often
    # contain generic Docling artifacts such as "image" or section labels.
    base = slugify(pdf.stem, fallback=source_hash[:12])
    return base[:90].strip("-") or source_hash[:12]


def parse_pdf(pdf: Path, root: Path, out_dir: Path | None = None, stem: str | None = None, allow_fallback: bool = True) -> dict:
    if not pdf.exists() or pdf.suffix.lower() != ".pdf":
        raise SystemExit(f"PDF not found: {pdf}")
    out_dir = out_dir or root / "sources"
    source_hash = file_sha256(pdf)
    warnings: list[str] = []
    if allow_fallback:
        text, parser = extract_with_fallbacks(pdf, warnings)
    else:
        text, parser = extract_with_docling(pdf)
    if len(text.strip()) < 200:
        raise RuntimeError("Extracted text is empty or structurally unusable")
    stem = stem or guess_stem(pdf, text, source_hash)
    source_path = out_dir / f"{stem}.md"
    manifest = {
        "stem": stem,
        "pdf_path": str(pdf),
        "source_path": str(source_path.relative_to(root)),
        "source_hash": source_hash,
        "parsed_with": parser,
        "parsed_at": utc_now(),
        "warnings": warnings,
    }
    frontmatter = ["---"] + [f"{k}: {json.dumps(v, ensure_ascii=False)}" for k, v in manifest.items()] + ["---", ""]
    source_path.parent.mkdir(parents=True, exist_ok=True)
    source_path.write_text("\n".join(frontmatter) + text, encoding="utf-8")
    manifest_path = root / "logs" / f"parse-{stem}.json"
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    return manifest


def main() -> int:
    parser = argparse.ArgumentParser()
    add_root_arg(parser)
    parser.add_argument("pdf")
    parser.add_argument("--out-dir", default=None)
    parser.add_argument("--stem", default=None)
    parser.add_argument("--no-fallback", action="store_true")
    args = parser.parse_args()
    root = Path(args.root).resolve() if args.root else Path.cwd().resolve()
    manifest = parse_pdf(Path(args.pdf).resolve(), root, Path(args.out_dir).resolve() if args.out_dir else None, args.stem, not args.no_fallback)
    print(json.dumps(manifest, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
