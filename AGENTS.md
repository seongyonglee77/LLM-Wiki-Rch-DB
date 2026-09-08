# llm-wiki Local Operating Contract

This folder is the active llm-wiki root.

## Public repository profile

This repository uses `km-config.json` with `publication_profile: public-summary-only`. PDFs may exist in a local untracked `papers/` or `inbox/` folder for future ingest, but they must never be committed. Cards, parsed sources, wiki pages, registry/index outputs, and `wiki-site/` are the publishable layers. QC ignores the deliberately absent PDF layer only under this explicit profile; all other required layers and links must still exist.

## Language contract

- `sources/`, `cards/`, paper summaries, bibliographic metadata, and `refs.bib` use English by default (`paper_language: en`). Preserve original titles, author names, quotations, and citation metadata; do not translate the paper record merely because the wiki language is Korean.
- `wiki/`, overview/concept/question/project explanations, navigation indexes, and their labels use the configured `wiki_language`. The current project setting is Korean (`wiki_language: ko`).
- At setup, ask separately for the paper/card/source language and the wiki/synthesis language when either is unset. Offer English, Korean, or another specified language; never infer the choice from the model, operating-system locale, or chat language.
- A Korean wiki does not permit Korean card/source summaries. A paper record remains English while the navigation and explanatory synthesis layer may be localized.

## Startup

- Read this file and `km-config.json` at the start of each session.
- Do not rely on memory from earlier sessions.
- Inspect `indexes/`, `wiki/`, and `cards/` before scanning the whole tree.
- State the active root and write scope before broad or destructive changes.
- This root is inside OneDrive. Never create `.venv`, `venv`, virtualenv, conda env, package cache, model cache, or heavyweight dependency folders here.
- Docling and PDF dependencies must use the global/user Python runtime or an explicitly approved environment outside all cloud-synced folders.
- Approved Docling runtime for this installation: Windows path `D:\win-python\master_venv`, Python command `D:\win-python\master_venv\Scripts\python.exe`.
- Secondary WSL Docling runtime: Windows path `D:\WSL\docling\venv`, WSL path `/mnt/d/WSL/docling/venv`, Python command `wsl -e /mnt/d/WSL/docling/venv/bin/python`.
- Windows and WSL may share this project's source files and research data, but must not share the same Python environment folder. Keep Windows venvs under `D:\win-python` and WSL/Linux venvs under `D:\WSL` or another approved non-cloud WSL path.
- Before adding runtime dependencies, confirm the intended operating surface: Windows native, WSL/Linux, macOS, or mixed Windows+WSL. Use a platform-specific environment for each selected surface.

### Windows + WSL operating surfaces

- Windows native remains supported with `D:\win-python\master_venv\Scripts\python.exe` and PowerShell commands.
- WSL2 is also a supported operating surface. Use `/mnt/d/OneDrive/2_rch_db` for this root and `/mnt/d/WSL/docling/venv/bin/python` for the approved WSL Docling runtime; do not invoke the Windows Python executable from WSL.
- The native WSL Codex CLI and the global `km@knowledge-manager` plugin are installed under `/home/seongyong_lee/.nvm` and `/home/seongyong_lee/.codex`. The project-local `.agents/skills/llm-wiki-ops` is shared through the mounted project root.
- When running in WSL, use an interactive login shell so the native Node/Codex path is loaded. Windows PATH shims must not be mistaken for Linux installations.

## Storage Contract

- `inbox/` is the manual intake folder for new PDFs.
- Successful ingests move PDFs to `papers/`.
- `sources/{stem}.md` is the canonical parsed source Markdown.
- `cards/{stem}.md` is the detailed human-readable research card.
- `wiki/{stem}.md` is the synthesis/navigation node.
- `refs.bib` is generated output. Do not manually edit it.
- `registry/legacy/refs.bib` may store old Zotero/Better BibTeX exports, but it is not canonical.

## Paper Scope and Locked Records

Every ingest, audit, correction, and refresh must resolve an exact `record_id` before writing. The default write scope is only that paper's PDF, source, card, wiki node, registry entry, index rows, bibliography entry, and QC evidence.

- Do not modify another paper's card, YAML, source, wiki node, registry entry, index entry, `refs.bib` entry, or QC evidence unless the user explicitly requests a multi-paper operation.
- A `locked` card and its matching `refs.bib` entry may change only after explicit paper-specific user direction or approval.
- Audit-only work may write audit reports and QC evidence, but must not change cards or bibliography entries.
- If a generated aggregate file cannot preserve non-target records during a single-paper task, stop before writing.

## Retrieval Policy

1. Search `indexes/`, `wiki/`, and `cards/` first.
2. Read `sources/` when the card is incomplete or a claim needs verification.
3. Read the PDF in `papers/` when parsed text or page/figure context is insufficient.
4. Use external web or scholarly search only when explicitly requested or when running metadata audit.
5. If local evidence is missing, say so. Do not invent citations, DOI values, results, or claims.

## Ingest Trigger

When the user says "ingest this file", "ingest all new PDFs in inbox", or equivalent natural language, run the complete workflow:

```text
discover inbox PDFs
  -> detect duplicates
  -> parse with Docling
  -> validate extracted text
  -> create a provisional parsed source and move valid PDFs to papers/
  -> summarize the parsed source and finalize title/author/year metadata
  -> rekey the PDF, source, card, wiki, and parse manifest to the final stem
  -> rebuild registry, indexes, refs.bib, QC, and wiki-site
  -> report success, failure, duplicate, excluded, and needs-review items
```

The rebuild step also maintains `wiki/{overviews,concepts,projects,questions}/index.md` navigation pages without replacing their curated introductions. It appends newly created pages, and QC must resolve every wikilink to an actual Markdown file; a visible link with a missing target is a failure.

The optional static web layer lives in `wiki-site/`. It is generated from `wiki/`, `cards/`, and `sources/` by `scripts/build_html_site.py`, must remain separate from canonical Markdown, and must be safe to publish through GitHub Pages. Rebuild it after wiki, card, or source changes and verify that generated local HTML links and assets resolve.

Use `scripts/ingest_batch.py` for deterministic file operations. LLM judgment is used for improving summaries after source extraction; scripts do not call another LLM.

Filename normalization has two stages. Parsing creates a provisional stem so the source can be admitted and passed to the summary workflow. After summary metadata is finalized, the canonical writer rekeys the PDF, source, card, wiki, and parse manifest to the final `YYYY_Author_ShortTitle` stem. The same final stem is used by registry, index, bibliography, QC, and HTML outputs. Collisions receive deterministic author suffixes; filename decisions do not require a second full-document LLM read.

PDF extraction order is Docling first, then `opendataloader-pdf`, then `pypdf`, then `pdftotext`. Record the extractor used and any earlier fallback failures in the parse manifest.

## Runtime Policy

- Preferred runtime command: `D:\win-python\master_venv\Scripts\python.exe`.
- From PowerShell, run root scripts with the Windows runtime, for example: `& 'D:\win-python\master_venv\Scripts\python.exe' scripts\ingest_batch.py`.
- Do not install dependencies into this folder.
- If Docling is missing, install it only in a global/user runtime or explicitly approved environment outside cloud-synced folders, then verify `import docling` before ingest.
- If a Windows-native runtime is needed, use an approved non-cloud environment under `D:\win-python`, not this OneDrive root.
- Do not reuse a WSL `venv` as a Windows `venv`, or a Windows `venv` as a WSL `venv`. Native wheels, scripts, executable names, and path handling differ.
- `opendataloader-pdf` and `pdftotext` are optional fallback extractors. Before installing them, report which platforms are missing them and let the user choose Windows only, WSL/Linux only, macOS only, or multiple platform-specific installs.
- Do not use `ingest_batch.py` as a harmless empty smoke test unless `inbox/` has first been inspected and confirmed empty. For no-ingest validation, run `build_registry.py`, `build_indexes.py`, `export_refs_bib.py`, and `qc_report.py` directly.
- Record runtime checks in `logs/setup-validation.md`.

## Bibliography Policy

- Card YAML and `registry/works.jsonl` are inputs.
- Root `refs.bib` is generated output.
- After a card metadata change, rebuild only the targeted paper's registry/index/bibliography/QC records unless a multi-paper operation was explicitly requested.
- Project `references.bib` files are generated subsets and must not be manually edited.
- Drafts may cite only keys present in the relevant generated bibliography.

## Taxonomy Policy

Do not automatically create, split, merge, or move category folders. Write taxonomy proposals to `qc/taxonomy-review-YYYY-MM-DD.md`; only user approval may authorize category path changes.
