# llm-wiki Operations

Use this local router for natural-language llm-wiki operations in this root.

## Language contract

- Keep `sources/`, `cards/`, paper summaries, and bibliographic metadata in English by default (`paper_language: en`), while preserving original paper titles, authors, quotations, and citation fields.
- Localize only `wiki/`, overview/concept/question/project explanations, index labels, and synthesis navigation through `wiki_language` (currently `ko`).
- Setup must ask for paper language and wiki language independently when missing, offering English, Korean, or a specified alternative. Do not infer either value from the model or conversation language.

## Intents

- `ingest`: discover inbox PDFs, parse, validate, create source/card/wiki, rebuild registry/indexes/refs.bib/QC.
- `search`: inspect indexes, wiki, cards, then sources and PDFs as needed.
- `audit`: write metadata/link/citation audit reports without silently changing cards or bibliography entries.
- `draft`: use project AGENTS, citation packets, project bibliography, and citation verification.
- `taxonomy`: write a proposal only; wait for explicit user approval before structural moves.

## Required Behavior

- Load root `AGENTS.md` and `km-config.json`.
- State active root, read scope, write scope, and whether records are `open` or `locked`.
- For single-paper maintenance, resolve exact `record_id` and preserve unrelated cards, records, QC evidence, and `refs.bib` entries.
- Report failures instead of claiming completion.
- A single ingest/refresh operation must run the complete rebuild, including wiki category indexes. Preserve curated index prose, append new pages, and fail QC on broken wikilinks or synthesis pages that are empty/link-only.
- The optional presentation layer is `wiki-site/`, generated from canonical `wiki/` Markdown by `scripts/build_html_site.py`. It is static, dependency-free, GitHub Pages-compatible, and never replaces or edits the canonical Markdown records.
