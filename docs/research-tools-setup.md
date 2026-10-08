# Research Tools Setup

This document describes the live helper tooling for this llm-wiki DB. It is intentionally generic: replace `<downloaded DB>` with the folder that contains this repository.

## What Is Installed

The installer manages four research skills and an optional bounded research-agent root:

- `project-init`: initialize one active project from `templates/phd-project/`.
- `project-literature`: record candidate/selected/excluded literature, verify source quotations, render human Markdown, create citation packets, and export selected BibTeX.
- `km-search`: search the bound DB with GraphRAG/CLI/MCP/text fallback while keeping the corpus read-only and scoped.
- `llm-wiki-ops`: DB-root-only PDF ingest, summary finalization, rebuild, and QC workflow; not a substitute for project KM search.
- `research-agents`: optional root with `rch-db` and `rch-projects` roles. These folders are for reports, candidates, and briefings only. No bots, credentials, MCP server, or scheduler is installed by this script.

The DB root is detected from `scripts/install_research_tools.py` by default, so a clean clone works without personal paths.

## Install Commands

Preview only:

```sh
cd "<downloaded DB>"
python3 scripts/install_research_tools.py
```

Windows native:

```powershell
cd "<downloaded DB>"
py -3 scripts\install_research_tools.py --apply --fetch-km --path-style windows
```

WSL/Linux:

```sh
cd "<downloaded DB>"
python3 scripts/install_research_tools.py --apply --fetch-km --path-style native
```

macOS:

```sh
cd "<downloaded DB>"
python3 scripts/install_research_tools.py --apply --fetch-km --path-style native
```

`--fetch-km` clones or reuses Knowledge Manager under `~/.local/share/llm-wiki/knowledge-manager` by default, outside cloud-synced folders. This does not mean every upstream Knowledge Manager feature is installed, nor that GraphRAG has been built or proven available.

Use repeated `--skills-dir` flags for multiple clients. Example shape:

```sh
python3 scripts/install_research_tools.py --apply --fetch-km \
  --skills-dir "$HOME/.codex/skills" \
  --skills-dir "$HOME/.gjc/agent/skills"
```

For Windows-side clients, pass the corresponding native Windows skill directory from PowerShell. Use `--path-style windows` when the generated `SKILL.md` and `binding.json` should display Windows paths.

## Research Agents Root

By default, the installer creates a sibling `research-agents` folder next to the DB. You can choose a different location:

```sh
python3 scripts/install_research_tools.py --apply \
  --agents-root "<research-agents>" \
  --phd-root "<PhD root>"
```

Current intended structure:

```text
research-agents/
├── AGENTS.md
├── rch-db/
│   ├── AGENTS.md
│   ├── config.json
│   ├── reports/
│   ├── candidates/
│   └── briefings/
└── rch-projects/
    ├── AGENTS.md
    ├── config.json
    ├── reports/
    ├── candidates/
    └── briefings/
```

`rch-db` is DB-only. `rch-projects` may read PhD `PROJECT.md` and `STATUS.md` only after projects are explicitly allowlisted in its config. Do not put a new `agents/` folder inside the DB.

## Project Initialization

From a project session, ask naturally:

```text
이 프로젝트 표준 초기화해 줘.
```

The skill runs a preview and then applies the safe creation step:

```sh
python3 "<DB>/scripts/project_init.py" --project "<project>"
python3 "<DB>/scripts/project_init.py" --project "<project>" --apply
```

Useful options:

- `--project`: target project; defaults to current directory.
- `--db-root`: llm-wiki DB root; defaults to the script's parent DB.
- `--folder`: additional project folder to create; repeatable.
- `--apply`: create missing files and directories. Without it, JSON preview only.

The initializer preserves existing files, refuses conflicting bindings, and rejects project roots inside the DB.

## Project Literature Commands

Canonical state lives in `literature-evidence.json`. `literature-evidence.md`, `citation-packets/`, and `references.bib` are generated views.

```sh
python3 "<DB>/scripts/project_literature.py" --project "<project>" validate
python3 "<DB>/scripts/project_literature.py" --project "<project>" upsert --input "<update.json>"
python3 "<DB>/scripts/project_literature.py" --project "<project>" upsert --input "<update.json>" --approve-selection
python3 "<DB>/scripts/project_literature.py" --project "<project>" render
python3 "<DB>/scripts/project_literature.py" --project "<project>" packet --record-id "<record-id>"
python3 "<DB>/scripts/export_project_bib.py" --project "<project>"
```

`--approve-selection` is required for records marked `selected`. This separates recording candidates from adopting literature for the project.

Evidence states:

- `source_text`: exact quote exists in the canonical source Markdown.
- `page_verified`: quote exists under a matching page marker section.
- `unverified`: record the uncertainty rather than fabricating proof.

These checks do not prove semantic support for the research claim; the interpretation still needs scholarly review.

## KM Search Bridge

The KM adapter is read-only unless another project skill is explicitly invoked after retrieval.

```sh
python3 "<DB>/scripts/km_search_bridge.py" context
python3 "<DB>/scripts/km_search_bridge.py" rag --query "<query>" [--deep]
python3 "<DB>/scripts/km_search_bridge.py" text --query "<query>" [--deep] [--sources]
```

Engine order is GraphRAG, Obsidian CLI, Obsidian MCP, then restricted text fallback. Reading priority is a separate axis: `indexes/`, `wiki/`, `cards/`, then `sources/` only when evidence verification is needed.

GraphRAG results are usable only when the bridge proves the note belongs to this DB corpus. Foreign or unproven RAG notes are rejected and fallback is required. Do not claim GraphRAG availability until an actual verified result has been observed.

## Post-Install Validation

Run targeted checks after setup:

```sh
python3 scripts/project_init.py --project /tmp/llm-wiki-project-preview
python3 scripts/km_search_bridge.py context
python3 -m pytest tests/test_project_init.py tests/test_project_literature.py tests/test_install_research_tools.py tests/test_km_search_bridge.py
```

If `pytest` is unavailable in the current runtime, use the project's approved Python environment outside OneDrive. Do not create `.venv`, package caches, model caches, or dependency folders inside this DB.

After installing skills for Codex/GJC/AGY, restart or reload the app/session and verify the skill is discovered. The installer can prove files were written; it cannot prove every app UI has refreshed its skill catalog.

## Important Non-Claims

- No app UI end-to-end skill execution is claimed until tested in that app session.
- No Discord bot, MCP server, OAuth connection, scheduler, or daemon is installed by this script.
- No GraphRAG index is automatically built by this script.
- No upstream Knowledge Manager feature outside the bound adapter is automatically safe for this DB.
- No external web or scholarly search is used unless the user explicitly requests it.
- No DB canonical files are edited from a project-scoped literature operation.
