# llm-wiki Research Database

Release: **v0.2.2** — portable installation, project workflow, and agent setup

This is a portable llm-wiki-native research knowledge base.

Language: **EN** · [한국어 README (KO)](README.ko.md)

This repository is a public, empty-by-default llm-wiki template. It contains the workflow, templates, scripts, wiki navigation, and static HTML shell. Personal cards, sources, PDFs, and generated research records are intentionally absent from the initial repository.

The implementation specification is preserved at [`docs/llm-wiki-custom-prd.md`](docs/llm-wiki-custom-prd.md).

## What this repository provides

- An empty-by-default research DB template with no bundled personal papers, PDFs, or project records.
- Evidence-grounded ingest, citation metadata, wiki synthesis, index, bibliography, QC, and static-site workflows.
- Portable project initialization and literature-evidence tools, plus DB-bound Knowledge Manager search and DB-only operations skills.
- Install-time path binding: the DB root is detected from the downloaded repository; research-project and agent roots are chosen by the user.

## Recommended two-pass summary profile

The repository is model-agnostic: its Python scripts do not call an LLM. In a Codex workflow, use the selected model for both summary and source-grounded verification passes:

```text
Docling parse
  -> temporary sanitized Markdown view
  -> the selected model writes the detailed summary and evidence JSON
  -> a second pass verifies claims and quotations against the source
  -> deterministic scripts validate exact quotations and required sections
  -> final filename rekey and registry/index/QC/HTML rebuild
```

The second verification pass is a practical critic layer, not a guarantee of independent truth. Exact-quote checks, page-marker rules, QC, and human review remain necessary. The verification pass must not reopen the PDF solely to locate page numbers; when the parsed Markdown has no reliable page marker, retain the exact quote with `source_text` and leave the page blank.

## Installation

Clone the repository, then use a Python environment outside the repository. Do not create a virtual environment inside a OneDrive, Dropbox, or other cloud-synced folder.

### Windows PowerShell

Before running the commands, replace `YOUR_GITHUB_USERNAME/YOUR_REPOSITORY` with the HTTPS repository path you intend to install (for example, your own fork), and choose `DB_FOLDER` plus `PYTHON_ENV` on your computer. The commands create the parent and final DB folder. The installer detects the DB root from its own location inside that folder, so no machine-specific DB path is embedded in the scripts. Keep `PYTHON_ENV` outside the repository and any cloud-sync folder.

```powershell
$REPOSITORY_URL = 'https://github.com/YOUR_GITHUB_USERNAME/YOUR_REPOSITORY.git'
$DB_FOLDER = 'C:\Research\llm-wiki-db' # replace with a location you choose
$PYTHON_ENV = 'C:\ResearchTools\llm-wiki-venv' # choose a non-synced location
New-Item -ItemType Directory -Force -Path (Split-Path $DB_FOLDER) | Out-Null
New-Item -ItemType Directory -Force -Path (Split-Path $PYTHON_ENV) | Out-Null
git clone $REPOSITORY_URL $DB_FOLDER
Set-Location $DB_FOLDER
py -3 -m venv $PYTHON_ENV
& "$PYTHON_ENV\Scripts\python.exe" -m pip install --upgrade pip
& "$PYTHON_ENV\Scripts\python.exe" -m pip install pyyaml docling
```

These paths are examples; choose locations that exist on your computer. Keep the environment outside OneDrive/Dropbox/iCloud and outside the repository. The repository itself contains no Python environment or dependency cache.

### WSL/Linux

Set `REPOSITORY_URL` to the repository or fork you intend to install. Set `DB_FOLDER` and `PYTHON_ENV` to locations you choose; the commands create their parent directories, and `git clone` creates the final DB folder. The installer derives the DB root from its own location.

```bash
REPOSITORY_URL="https://github.com/YOUR_GITHUB_USERNAME/YOUR_REPOSITORY.git"
DB_FOLDER="$HOME/research/llm-wiki-db" # replace with a location you choose
PYTHON_ENV="$HOME/.local/venvs/llm-wiki" # OS-local; never put this in cloud sync
mkdir -p "$(dirname "$DB_FOLDER")"
mkdir -p "$(dirname "$PYTHON_ENV")"
git clone "$REPOSITORY_URL" "$DB_FOLDER"
cd "$DB_FOLDER"
python3 -m venv "$PYTHON_ENV"
"$PYTHON_ENV/bin/python" -m pip install --upgrade pip
"$PYTHON_ENV/bin/python" -m pip install pyyaml docling
```

Keep Windows and WSL environments separate. `km-config.json` is portable and points Obsidian at the repository root; do not copy a Windows environment into WSL.

### macOS

Set `REPOSITORY_URL` to the repository or fork you intend to install. Set `DB_FOLDER` and `PYTHON_ENV` to locations you choose; the commands create their parent directories, and `git clone` creates the final DB folder. The installer derives the DB root from its own location.

```bash
REPOSITORY_URL="https://github.com/YOUR_GITHUB_USERNAME/YOUR_REPOSITORY.git"
DB_FOLDER="$HOME/research/llm-wiki-db" # replace with a location you choose
PYTHON_ENV="$HOME/.local/venvs/llm-wiki" # macOS-native; never put this in cloud sync
mkdir -p "$(dirname "$DB_FOLDER")"
mkdir -p "$(dirname "$PYTHON_ENV")"
git clone "$REPOSITORY_URL" "$DB_FOLDER"
cd "$DB_FOLDER"
python3 -m venv "$PYTHON_ENV"
"$PYTHON_ENV/bin/python" -m pip install --upgrade pip
"$PYTHON_ENV/bin/python" -m pip install pyyaml docling
```

Use a macOS-native Python environment outside iCloud Drive and other sync folders. Check PDF extractor and hardware support on that Mac; do not reuse Windows or Linux executables.

### Install and configure the research workflow

The repository includes `project-init`, `project-literature`, a DB-bound `km-search` adapter, and DB-root-only `llm-wiki-ops`. Run a preview first, then apply. `--fetch-km` optionally fetches the upstream Knowledge Manager checkout outside the cloud-synced DB. The default agent root is `research-agents/` beside the DB; choose the research-project root explicitly if you want project-aware agent access.

```powershell
py -3 scripts\install_research_tools.py
py -3 scripts\install_research_tools.py --apply --fetch-km --path-style windows
```

```bash
python3 scripts/install_research_tools.py
python3 scripts/install_research_tools.py --apply --fetch-km --path-style native
```

To install into multiple assistants, repeat `--skills-dir <assistant-skill-directory>`. Inspect the preview, preserve unrelated configuration, and restart/reload assistants after installation.

The installer uses the downloaded repository location as the DB root. It does not guess the location of your research projects: omit `--phd-root` to keep project reads disabled, or explicitly pass the research-project root you choose. The current CLI option is still named `--phd-root`; it sets the research-project root. By default, the shared `research-agents` folder is created beside the DB folder; override it with `--agents-root <chosen-path>` if desired. These paths are local installation settings, not repository-wide constants.

To enable access to your research projects, set both paths explicitly. Use native paths for the operating system running the installer:

```powershell
py -3 scripts\install_research_tools.py --apply --fetch-km --path-style windows --phd-root '<YOUR_RESEARCH_PROJECTS_ROOT>' --agents-root '<YOUR_AGENTS_ROOT>'
```

```bash
python3 scripts/install_research_tools.py --apply --fetch-km --path-style native --phd-root '<YOUR_RESEARCH_PROJECTS_ROOT>' --agents-root '<YOUR_AGENTS_ROOT>'
```

For first-time installation, use the preview without `--apply`, inspect the paths it plans to create, then run the same command with `--apply`. If Windows and WSL clients both use the same synced DB, install once per client surface with its own native `--skills-dir` paths and `--path-style`; use `--skip-agents` on a second pass to avoid rewriting the shared agent hub. Do not share Python environments between Windows, WSL/Linux, and macOS.

### Recommended folder layout

Keep the literature DB, active research projects, and agent workspaces as siblings, not nested copies. The names and parent location below are examples; choose paths that fit your setup.

```text
<chosen-workspace>/
├── research-db/                 downloaded llm-wiki repository; DB root auto-detected here
├── research-projects/           your research projects; not copied into the DB
│   └── <project>/               one isolated project folder per manuscript/study
│       ├── AGENTS.md             project-specific rules and safe DB connection
│       ├── PROJECT.md / STATUS.md
│       ├── literature-evidence.json + literature-evidence.md
│       ├── citation-gaps.md / references.bib
│       ├── citation-packets/ / drafts/ / outlines/
│       └── methods/ / resources/ / submission/ (as needed)
├── research-agents/             bounded shared agent roles, outside the DB corpus
│   ├── rch-db/                   searches DB; writes only reports/candidates/briefings
│   └── rch-projects/             reads only explicitly allowed project status files
└── research-ops/                optional cross-project CFP, ideas, schedules, reports
```

`project-init` creates only missing project files and binds `project-config.json` to the detected DB root. It does not invent study details. The installer detects the DB path from its own location; it does **not** infer the research-project root. Project reads are disabled unless `--phd-root` is supplied; this existing CLI option names the research-project root. `--agents-root` chooses the shared agent hub location (default: sibling `research-agents/`).

### Initialize and use a research project

Open the target research-project directory in the coding assistant and ask: **“Initialize this research project using the standard template.”** The skill previews the plan and creates only missing files; existing drafts are preserved. The generated `project-config.json` binds that project to the downloaded DB root and the fixed search scope (`indexes`, `wiki`, `cards`, `sources`). For explicit CLI use:

```bash
python3 "<path-to-db>/scripts/project_init.py" --project "<path-to-project>" --apply
```

Each computer must resolve paths on its own operating system. Rebind explicitly if the DB or project path changes; do not assume that a Windows path is valid inside WSL or macOS.

Typical natural-language requests (run the coding assistant with the project folder as its workspace):

```text
이 프로젝트 표준 초기화해 줘.
KM으로 내 DB에서 teacher agency 관련 문헌을 찾아 후보 표에 정리해 줘.
후보 2와 4의 원문 근거를 확인하고 citation packet을 만들어 줘.
선택 문헌으로 문헌고찰 아웃라인을 작성해 줘.
이 초안의 인용을 검증하고 STATUS.md에 다음 작업을 기록해 줘.
최신 논문을 웹/학술 검색으로 찾아 줘.   # external search only when requested
```

KM search is read-only and targets the bound DB. Candidate selection, evidence ledger updates, citation packets, and project Bib generation are separate project-literature actions. A search result is not an approved citation; the researcher decides whether to select it.

## GitHub publication scope

After a local ingest and review, the repository can publish English summary cards, parsed source Markdown, the configured wiki layer (English by default), indexes, generation scripts, and the static `wiki-site/` presentation. Personal records are not bundled here, and original PDFs in `papers/`, `papers-supplementary/`, and intake files in `inbox/` are excluded.

The ingest pipeline uses a two-stage filename policy. A parsed paper first receives a provisional stem. After the summary metadata is finalized, the PDF, source, card, wiki node, and parse manifest are rekeyed together to one canonical `YYYY_Author_ShortTitle` stem. This prevents the summary card from having a different identity from the rest of the record.

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
python3 scripts/ingest_batch.py
```

The workflow parses the PDF, creates the English source/card layers, creates the configured wiki-language layer, finalizes the canonical filename after summary metadata is known, and rebuilds the registry, indexes, bibliography, QC report, and static HTML site. The site includes generated pages for `wiki/`, `cards/`, and `sources/`; PDFs remain local and are excluded from GitHub. Review the generated files and QC report before committing.

For an empty-repository validation or a rebuild without ingesting a PDF:

```powershell
python3 scripts/build_registry.py
python3 scripts/build_indexes.py
python3 scripts/export_refs_bib.py
python3 scripts/qc_report.py
python3 scripts/build_html_site.py --output wiki-site
```

The paper/source language and wiki language are independent settings in `km-config.json`. The public template defaults to English for both; change `paper_language` and `wiki_language` before ingest if needed.

## Runtime Rule

Treat this repository as potentially cloud-synced. Do not create `.venv`, `venv`, conda environments, package caches, model caches, or heavyweight dependency folders here. Install Docling in the global/user Python runtime or another approved environment outside all cloud-synced folders.

Put each runtime outside this repository and cloud-sync folders. Windows, WSL/Linux, and macOS can share source files and Markdown outputs, but must use separate OS-native Python environments.

Before adding runtime dependencies, choose the operating surface explicitly: Windows native, WSL/Linux, macOS, or mixed Windows+WSL. macOS also needs its own macOS-native environment outside iCloud Drive or any other cloud-synced folder.

`opendataloader-pdf` and `pdftotext` are optional fallback extractors after Docling. Install them separately per selected OS environment; a WSL install does not make them Windows-native, and a Windows install does not make them available inside WSL.

Example ingest command from PowerShell (use the Python executable in your selected environment):

```powershell
py -3 scripts\ingest_batch.py
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

## Static wiki site

`wiki-site/` is a generated, read-only presentation of the wiki, cards, and parsed sources. The ingest/rebuild workflow refreshes it after canonical content changes; open `wiki-site/index.html` locally to browse it without Obsidian. Publishing to GitHub Pages is optional: review every generated page for private or copyrighted material first, then enable Pages with GitHub Actions. Do not publish original PDFs or unreviewed project notes.

## Release notes

### v0.2.2

- Added a portable install guide that asks each user to choose the repository URL, DB location, Python environment, optional research-project root, and agent workspace.
- Documented DB-root auto-detection from the downloaded repository, while keeping research-project access opt-in and explicitly configured.
- Added the recommended parallel DB / research-project / research-agent folder layout, project-init and project-literature natural-language examples, and local/static wiki-site guidance.
- Replaced maintainer-specific GitHub and local path examples with user-configurable placeholders.

### v0.2.1

- Empty-by-default public template; research records are intentionally excluded.
- Retains the ingest workflow, templates, scripts, navigation, tests, and static HTML shell.

### v0.2.0

- A paper is admitted with a provisional stem, then renamed automatically after the summary metadata is finalized.
- The final `YYYY_Author_ShortTitle` stem is applied consistently to the PDF, source, card, wiki node, parse manifest, registry, indexes, bibliography, QC, and generated HTML.
- Summary cards use a consolidated YAML schema and require source-grounded evidence for Theory & Literature Review, Findings, and Discussion.
- Direct quotations are checked against the parsed source. Reliable page markers are preserved; otherwise the claim is marked `source_text` and remains subject to human page review.
- The static site renders `wiki/`, `cards/`, and `sources/`, while original PDFs remain local and outside the public repository.
- Regression tests cover filename normalization, record rekeying, sanitized summary input, and evidence-backed card generation.
