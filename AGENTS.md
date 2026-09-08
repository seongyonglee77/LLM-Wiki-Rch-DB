# llm-wiki Local Operating Contract

This folder is the active llm-wiki root.

## Language contract

- `sources/`, `cards/`, paper summaries, bibliographic metadata, and `refs.bib` use English by default (`paper_language: en`). Preserve original titles, author names, quotations, and citation metadata; do not translate the paper record merely because the wiki language is Korean.
- `wiki/`, overview/concept/question/project explanations, navigation indexes, and their labels use the configured `wiki_language`. The current project setting is English (`wiki_language: en`).
- At setup, ask separately for the paper/card/source language and the wiki/synthesis language when either is unset. Offer English, Korean, or another specified language; never infer the choice from the model, operating-system locale, or chat language.
- All wiki content is in English. A paper record remains English while the navigation and explanatory synthesis layer is also in English.

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
- `registry/synthesis-links.json` is the canonical many-to-many relationship registry. Each paper must link to at least one relevant `overviews/` or `concepts/` page; `projects/` and `questions/` are optional and must be semantically justified. Relationship metadata is mirrored into card `related` YAML and rendered as bidirectional Markdown links.
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
2. Read `sources/` when the card is incomplete or a claim needs verification. For LLM summary work, first create a temporary sanitized view with `scripts/prepare_summary_input.py`; never modify the canonical source.
3. Do not read the PDF again solely for summary page verification. Use page markers present in the parsed Markdown; when no reliable page can be inferred, leave the page blank and mark the evidence for manual review. PDF reading remains part of deterministic ingest/extraction and an explicitly requested visual/source audit.
4. Use external web or scholarly search only when explicitly requested or when running metadata audit.
5. If local evidence is missing, say so. Do not invent citations, DOI values, results, or claims.

Deep-summary contract: `summary.status: summarized` requires source-grounded, detailed prose rather than an abstract-length recap. Evidence JSON must declare `summary_depth.level: deep`, provide a developed section overview and at least three substantive claims for Literature Review/Background, Findings/Results, and Discussion/Implications, and attach an exact quotation, interpretation, and why-it-matters explanation to every claim. Evidence is rendered inline under its claim; do not generate a duplicate `## Directly Citable Evidence` table.

## Ingest Trigger

**Mandatory routing rule:** Any user request whose intent is to ingest, including a bare
request such as "ingest" or "ingest해 줘", MUST mean: ingest every PDF directly inside
the active root's `inbox/` folder through the batch ingest pipeline. This rule applies
even when the terminal was opened at the repository root and even when the request
mentions a particular file. Never ingest a PDF directly from another folder, scan
`papers/` or the whole repository for ingest candidates, or reinterpret the request as
summarizing an existing paper. If a named PDF is not already in `inbox/`, report that it
is not eligible until it is placed there.

Before running the pipeline, inspect only `inbox/` for top-level `*.pdf` files. When one
or more PDFs are present, run the following command from this active root (or pass the
same root explicitly with `--root`):

```powershell
& 'D:\win-python\master_venv\Scripts\python.exe' scripts\ingest_batch.py --root .
```

Do not substitute a direct `parse_pdf.py` call or another input path for this command.
If `inbox/` contains no PDFs, do not call `ingest_batch.py` merely as a smoke test;
follow the no-ingest validation rule in Runtime Policy instead and report that there
was nothing to ingest.

When the user says "ingest this file", "ingest all new PDFs in inbox", or equivalent natural language, run the complete workflow:

```text
discover top-level inbox/*.pdf files
  -> detect duplicates
  -> parse with Docling
  -> validate extracted text
  -> create a provisional parsed source and move valid PDFs to papers/
  -> summarize the parsed source and finalize author/year/title metadata
  -> rekey PDF, source, card, and wiki to the final YYYY_Author_ShortTitle stem
  -> LLM judges synthesis connections: read the new card, identify relevant
     overviews/concepts/projects/questions, write registry entries with
     English labels and relation prose
  -> run scripts/rebuild_all.py --stem {stem}
     (propagates wiki page, synthesis reverse links, and card YAML in one pass)
  -> rebuild indexes, refs.bib, QC, and wiki-site from that final stem
  -> report success, failure, duplicate, excluded, and needs-review items
```

### Synthesis auto-propagation

`scripts/rebuild_all.py` is the single entry point for post-ingest cascade. After the LLM writes a registry entry to `synthesis-links.json`, running this script propagates the connection to every affected file:

1. **`build_wiki.py`** — regenerates `wiki/{stem}.md` with Synthesis Links section
2. **`build_synthesis_links.py`** — appends Related Papers (with relation prose) to every linked overview/concept/project/question page
3. **`sync_related_metadata.py`** — updates the card YAML `related` block

The LLM judges **what** to connect (which synthesis pages, what relation prose); the scripts execute **how** (deterministic, bidirectional, consistent). No manual registry editing or separate script calls are needed after the LLM writes the registry entry.

For batch ingest, run `rebuild_all.py` without `--stem` to cascade all papers.

The rebuild step also maintains `wiki/{overviews,concepts,projects,questions}/index.md` navigation pages without replacing their curated introductions. It appends newly created pages, and QC must resolve every wikilink to an actual Markdown file; a visible link with a missing target is a failure.

The optional static web layer lives in `wiki-site/`. It is generated from `wiki/` plus linked `cards/` and `sources/` pages by `scripts/build_html_site.py`, must remain separate from canonical Markdown, and must be safe to publish through GitHub Pages. Rebuild it after wiki, card, or source changes and verify that generated local HTML links and assets resolve.

Use `scripts/ingest_batch.py` for deterministic file operations. LLM judgment is used for improving summaries after source extraction; scripts do not call another LLM.

Filename normalization has two stages. Parsing creates a provisional stem so the source can be admitted and passed to the summary skill. After summary metadata is finalized, the canonical writer rekeys the PDF, source, card, wiki, and parse manifest to the final stem. The PDF remains a `.pdf`; the final stem is reused for `sources/`, `cards/`, `wiki/`, registry, and bibliography outputs. The final stem uses `YYYY_Author_ShortTitle`, with at most three author surnames and three meaningful title words; collisions receive deterministic author suffixes (`Lee-a`, `Lee-b`, ...). This rekey uses summary metadata, not a second full-document LLM read.

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
