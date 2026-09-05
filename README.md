# llm-wiki Research Database

This is a portable llm-wiki-native research knowledge base.

Language: **EN** · [한국어 README (KO)](README.ko.md)

This repository is a public, empty-by-default llm-wiki template. It contains the workflow, templates, scripts, wiki navigation, and static HTML shell. Personal cards, sources, PDFs, and generated research records are intentionally absent from the initial repository.

The implementation specification is preserved at [`docs/llm-wiki-custom-prd.md`](docs/llm-wiki-custom-prd.md).

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

## GitHub publication scope

After a local ingest and review, the repository can publish English summary cards, parsed source Markdown, the Korean wiki layer, indexes, generation scripts, and the static `wiki-site/` presentation. Personal records are not bundled here, and original PDFs in `papers/`, `papers-supplementary/`, and intake files in `inbox/` are excluded.

## Quick Use

1. Keep the public repository clean; place approved PDFs in the local `inbox/` only when preparing a new record.
2. Ask the coding agent: `inbox의 새 PDF를 전부 ingest해 줘.`
3. Review generated files in `sources/`, `cards/`, `wiki/`, `registry/`, `indexes/`, `qc/`, and `refs.bib` before publishing.

## Simple user guide

You can work through an LLM in natural language; you do not need to memorize the script names.

1. Open the LLM with this repository as the working folder so it can read `AGENTS.md`.
2. Put an approved PDF in `inbox/`.
3. Ask: `Ingest every new PDF in inbox.`
4. Review the generated `sources/`, `cards/`, `wiki/`, `refs.bib`, and `qc/` files.
5. Ask for a consistency check when needed: `Check this card's claims and direct quotations against the source, and verify the wiki links.`
6. Commit only reviewed records. Keep PDFs and private working notes outside the public repository.

Useful requests:

```text
Find papers about my topic inside llm-wiki.
Audit open-card metadata and report differences without changing locked records.
Update the registry, indexes, refs.bib, and QC after my approved card changes.
Propose wiki links for this paper without duplicating its card or source.
```

For the full natural-language command guide, see the Korean and English guide used as the project reference: the workflow is designed around one canonical paper record, evidence-backed summaries, explicit wiki links, generated bibliography, and QC before publication.

## Ingest and rebuild

Place an approved PDF in the local `inbox/` directory and run the complete workflow from the repository root:

```powershell
& 'D:\win-python\llm-wiki-venv\Scripts\python.exe' scripts\ingest_batch.py
```

The workflow parses the PDF, creates the English source/card layers, creates the configured wiki-language layer, rebuilds the registry, indexes, bibliography, QC report, and static HTML site. PDFs remain local and are excluded from GitHub. Review the generated files and QC report before committing.

For an empty-repository validation or a rebuild without ingesting a PDF:

```powershell
& 'D:\win-python\llm-wiki-venv\Scripts\python.exe' scripts\build_registry.py
& 'D:\win-python\llm-wiki-venv\Scripts\python.exe' scripts\build_indexes.py
& 'D:\win-python\llm-wiki-venv\Scripts\python.exe' scripts\export_refs_bib.py
& 'D:\win-python\llm-wiki-venv\Scripts\python.exe' scripts\qc_report.py
& 'D:\win-python\llm-wiki-venv\Scripts\python.exe' scripts\build_html_site.py --output wiki-site
```

The paper/source language and wiki language are independent settings in `km-config.json`. The public template defaults to English paper records and Korean wiki explanations; change `paper_language` and `wiki_language` before ingest if needed.

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

## GitHub Pages

The workflow in `.github/workflows/pages.yml` publishes the checked-in `wiki-site/` directory when `main` is pushed. In the GitHub repository, enable Pages with **GitHub Actions** as the source if it is not enabled automatically. The initial site is intentionally an empty public shell; only reviewed records should be committed.

## Status Model

- `open`: metadata can be audited and proposed for correction, but is not silently changed.
- `locked`: metadata and the corresponding `refs.bib` entry are protected unless the user explicitly approves that specific paper's correction.
