# llm-wiki Research Database

Release: **v0.2.1** — evidence-backed ingest pipeline

This is a portable llm-wiki-native research knowledge base.

Release: **v0.2.1**

## v0.2.1

The implementation specification is preserved at [`docs/llm-wiki-custom-prd.md`](docs/llm-wiki-custom-prd.md).

## What changed in v0.2.0

- A paper is admitted with a provisional stem, then renamed automatically after the summary metadata is finalized.
- The final `YYYY_Author_ShortTitle` stem is applied consistently to the PDF, source, card, wiki node, parse manifest, registry, indexes, bibliography, QC, and generated HTML.
- Summary cards use a consolidated YAML schema and require source-grounded evidence for Theory & Literature Review, Findings, and Discussion.
- Direct quotations are checked against the parsed source. Reliable page markers are preserved; otherwise the claim is marked `source_text` and remains subject to human page review.
- The static site now renders `wiki/`, `cards/`, and `sources/`, while original PDFs remain local and outside the public repository.
- Regression tests cover filename normalization, record rekeying, sanitized summary input, and evidence-backed card generation.

## Recommended Luna–Luna summary profile

The repository is model-agnostic: its Python scripts do not call an LLM. In the Codex operating profile, the recommended workflow is to use Luna for both passes:

```text
Docling parse
  -> temporary sanitized Markdown view
  -> Luna writes the detailed summary and evidence JSON
  -> Luna performs a second source-grounded verification pass
  -> deterministic scripts validate exact quotations and required sections
  -> final filename rekey and registry/index/QC/HTML rebuild
```

The second Luna pass is a practical critic layer, not a guarantee of independent truth. Exact-quote checks, page-marker rules, QC, and human review remain necessary. The verification pass must not reopen the PDF solely to locate page numbers; when the parsed Markdown has no reliable page marker, retain the exact quote with `source_text` and leave the page blank.

## Installation

Clone the repository, then use a Python environment outside the repository. Do not create a virtual environment inside a OneDrive, Dropbox, or other cloud-synced folder.

### Windows PowerShell

```powershell
git clone https://github.com/seongyonglee77/LLM-Wiki-Rch-DB.git
Set-Location LLM-Wiki-Rch-DB
py -3 -m venv D:\win-python\llm-wiki-venv
& 'D:\win-python\llm-wiki-venv\Scripts\python.exe' -m pip install --upgrade pip
& 'D:\win-python\llm-wiki-venv\Scripts\python.exe' -m pip install pyyaml docling
```

If Docling is already installed in `D:\win-python\master_venv`, that runtime can be used instead. The repository itself contains no Python environment or dependency cache.

### WSL/Linux

```bash
git clone https://github.com/seongyonglee77/LLM-Wiki-Rch-DB.git
cd LLM-Wiki-Rch-DB
python3 -m venv /mnt/d/WSL/llm-wiki-venv
/mnt/d/WSL/llm-wiki-venv/bin/python -m pip install --upgrade pip
/mnt/d/WSL/llm-wiki-venv/bin/python -m pip install pyyaml docling
```

Keep Windows and WSL environments separate. `km-config.json` is portable and points Obsidian at the repository root; update its local paths only for your machine.
- Added the Brown et al. (2024) *Trash in Motion* research record and synthesis links.
- Repaired 17 legacy cards with inline source-text evidence and removed duplicate evidence tables.
- Added the legacy-card QC repair utility and regenerated indexes, bibliography, QC, and static-site outputs.

## GitHub publication scope

The repository publishes the English summary cards, parsed source Markdown, Korean wiki layer, indexes, generation scripts, and the static `wiki-site/` presentation. The static site renders linked summary cards and parsed sources as HTML under `wiki-site/cards/` and `wiki-site/sources/`. Original PDFs in `papers/`, `papers-supplementary/`, and intake files in `inbox/` are intentionally excluded.

## Quick Use

1. Put new PDFs in `inbox/`.
2. Ask the coding agent: `inbox의 새 PDF를 전부 ingest해 줘.`
3. Review generated files in `sources/`, `cards/`, `wiki/`, `registry/`, `indexes/`, `qc/`, and `refs.bib`.

Ingest parses each PDF first, then deterministically renames it to `YYYY_Author_ShortTitle.pdf` (up to three authors and a three-word short title, with `Lee-a`/`Lee-b` collision suffixes). The canonical stem is reused for the source, card, and wiki filenames.

Deep summaries are source-grounded and section-sensitive: Literature Review/Background, Findings/Results, and Discussion/Implications each require a developed overview plus at least three substantive claims when available. Each claim carries its interpretation, why-it-matters context, and exact quotation inline; the deprecated duplicate `Directly Citable Evidence` table is not generated. The implementation PRD is kept at [docs/llm-wiki-custom-prd.md](docs/llm-wiki-custom-prd.md).

## Runtime Rule

This folder is inside OneDrive. Do not create `.venv`, `venv`, conda environments, package caches, model caches, or heavyweight dependency folders here. Install Docling in the global/user Python runtime or another approved environment outside all cloud-synced folders.

Approved external runtime locations:

- Windows Docling runtime: `D:\win-python\master_venv`
- Secondary WSL Docling runtime: `D:\WSL\docling\venv`

Windows and WSL can share this project folder, scripts, PDFs, cards, and Markdown outputs. They should not share the same Python environment folder. Use `D:\win-python` for Windows-native venvs and `D:\WSL` for WSL/Linux venvs.

Before adding runtime dependencies, choose the operating surface explicitly: Windows native, WSL/Linux, macOS, or mixed Windows+WSL. macOS also needs its own macOS-native environment outside iCloud Drive or any other cloud-synced folder.

`opendataloader-pdf` and `pdftotext` are optional fallback extractors after Docling. Install them separately per selected OS environment; a WSL install does not make them Windows-native, and a Windows install does not make them available inside WSL.

Current approved Docling runtime:

```powershell
& 'D:\win-python\master_venv\Scripts\python.exe'
```

Example ingest command from PowerShell:

```powershell
& 'D:\win-python\master_venv\Scripts\python.exe' scripts\ingest_batch.py
```

## Generated Outputs

- `refs.bib` is generated from card YAML and registry data.
- `registry/works.jsonl` is rebuilt from cards and generated layers.
- `indexes/` contains search and status views.
- `qc/` contains validation and audit reports.

Do not manually edit generated bibliography files. Correct the relevant card, then ask the agent to refresh that paper's registry, indexes, `refs.bib`, and QC records.

## Status Model

- `open`: metadata can be audited and proposed for correction, but is not silently changed.
- `locked`: metadata and the corresponding `refs.bib` entry are protected unless the user explicitly approves that specific paper's correction.
