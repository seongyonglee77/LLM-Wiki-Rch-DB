# {{PROJECT_NAME}}

## Purpose

Describe the thesis, article, chapter, or proposal this project supports.

## Database Context

- Database root: `{{DB_ROOT}}`
- Project root: `{{PROJECT_ROOT}}`
- Project config: `{{PROJECT_ROOT}}/project-config.json`
- Shared workflow: `{{DB_ROOT}}/docs/project-workflow.md`

The database is a read-only evidence source for this project. Project-specific notes, drafts, outlines, citation packets, and generated bibliography files stay in this project root.

## Working Principles

- No forced linear pipeline is required. Move between reading, outlining, drafting, and verification as the project needs.
- Read database material in this order: `indexes/`, `wiki/`, `cards/`, then `sources/`.
- Evidence must be verified before it supports a claim.
- Literature selection is not autonomous after evidence verification. Record project decisions in `literature-evidence.json`.
- Use external sources only when explicitly requested.
- Treat `references.bib` as generated output.
- Update `STATUS.md` after project mutations.

## Current Questions

- What argument is this project making?
- Which database records are candidates?
- Which records are selected, excluded, or still undecided?
- What evidence gaps remain?
