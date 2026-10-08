# {{PROJECT_NAME}} Agent Instructions

This project uses the shared llm-wiki database at:

```text
{{DB_ROOT}}
```

The active project root is:

```text
{{PROJECT_ROOT}}
```

## Shared Rules

At startup, read these project files before doing substantive work:

- `project-config.json`
- `PROJECT.md`
- `STATUS.md`
- `AGENTS.md`

Read the shared workflow before project work:

```text
{{DB_ROOT}}/docs/project-workflow.md
```

If the shared workflow and this project file disagree, follow the stricter rule and record the uncertainty in `STATUS.md`.

## Boundaries

- Treat the database as read-only from this project. Do not edit database `cards/`, `sources/`, `wiki/`, `indexes/`, `registry/`, or root bibliography files from here.
- Write only inside this project root unless the user explicitly authorizes a database operation.
- The Knowledge Manager context is internally bound to the `db_root` declared in `project-config.json` by default.
- Use external web or scholarly search only when the user explicitly requests it.
- Verify evidence before using it in an argument. Do not autonomously select sources for the project after verification; selection decisions belong in `literature-evidence.json`.
- This project's `references.bib` is generated output, normally as a subset of database records. Do not hand-edit it.
- Do not run project initialization automatically. Use the explicit project root and database root from `project-config.json`; translate Windows and WSL paths deliberately when crossing operating surfaces.
- After any project mutation, update `STATUS.md` with the current state or relevant next step.

## Search Order

Search the database in this order before broader reads:

1. `indexes/`
2. `wiki/`
3. `cards/`
4. `sources/`

## Evidence and Decisions

- Canonical literature decisions live in `literature-evidence.json`.
- `literature-evidence.md` is a human-readable generated view of that JSON.
- Do not hand-edit `literature-evidence.md` for durable changes. Edit the JSON or use `project_literature.py`.
- Unknown literature decisions should remain `Undecided` until the user or project process records a decision.

## Drafting

- Drafts belong in `drafts/`.
- Outlines belong in `outlines/`.
- Citation packets belong in `citation-packets/`.
- Draft citations must use keys present in generated `references.bib`.
- Regenerate `references.bib` with `export_project_bib.py`.
- Record missing or externally discovered citation needs in `citation-gaps.md`.
