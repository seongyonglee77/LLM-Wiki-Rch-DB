# llm-wiki Research Database

This is a portable llm-wiki-native research knowledge base.

This repository is a public, empty-by-default llm-wiki template. It contains the workflow, templates, scripts, wiki navigation, and static HTML shell. Personal cards, sources, PDFs, and generated research records are intentionally absent from the initial repository.

The implementation specification is preserved at [`docs/llm-wiki-custom-prd.md`](docs/llm-wiki-custom-prd.md).

## GitHub publication scope

After a local ingest and review, the repository can publish English summary cards, parsed source Markdown, the Korean wiki layer, indexes, generation scripts, and the static `wiki-site/` presentation. Personal records are not bundled here, and original PDFs in `papers/`, `papers-supplementary/`, and intake files in `inbox/` are excluded.

## Quick Use

1. Keep the public repository clean; place approved PDFs in the local `inbox/` only when preparing a new record.
2. Ask the coding agent: `inbox의 새 PDF를 전부 ingest해 줘.`
3. Review generated files in `sources/`, `cards/`, `wiki/`, `registry/`, `indexes/`, `qc/`, and `refs.bib` before publishing.

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
