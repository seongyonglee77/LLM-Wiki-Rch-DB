# llm-wiki Operations

Use this local router for natural-language llm-wiki operations in this root.

## Language contract

- Keep `sources/`, `cards/`, paper summaries, and bibliographic metadata in English by default (`paper_language: en`), while preserving original paper titles, authors, quotations, and citation fields.
- Localize only `wiki/`, overview/concept/question/project explanations, index labels, and synthesis navigation through `wiki_language` (currently `ko`).
- Setup must ask for paper language and wiki language independently when missing, offering English, Korean, or a specified alternative. Do not infer either value from the model or conversation language.

## Intents

- `ingest`: discover inbox PDFs, parse, validate, admit a provisional stem, summarize, rekey all paper artifacts from final summary metadata to `YYYY_Author_ShortTitle`, then rebuild source/card/wiki, registry/indexes/refs.bib/QC.
- `search`: inspect indexes, wiki, cards, then sources and PDFs as needed.
- `summarize`: prepare a temporary token-efficient view with `scripts/prepare_summary_input.py <source>` (the canonical source is never modified), read that parsed Markdown once, and prepare paper-specific evidence. Do not reopen or send the PDF for summary/page verification. Use a source page marker when the Markdown provides one; otherwise leave `page` blank and use `verification: source_text` for an exact source-text match. Then run `scripts/fill_summary_cards.py <source> --evidence <json>` for that exact record.
- `audit`: write metadata/link/citation audit reports without silently changing cards or bibliography entries.
- `draft`: use project AGENTS, citation packets, project bibliography, and citation verification.
- `taxonomy`: write a proposal only; wait for explicit user approval before structural moves.

## Required Behavior

- Load root `AGENTS.md` and `km-config.json`.
- State active root, read scope, write scope, and whether records are `open` or `locked`.
- For single-paper maintenance, resolve exact `record_id` and preserve unrelated cards, records, QC evidence, and `refs.bib` entries.
- A summary can become `summarized` only when its evidence JSON supplies source-grounded claims for Theory & Literature Review, Findings, and Discussion. Each claim requires an exact direct quotation. Use a positive page number plus `source_page` when the parsed Markdown provides a reliable page marker; otherwise use a blank page plus `source_text` and require manual review. Never write an unverified paraphrase as a verified citation.
- Page-level verification is intentionally manual for summaries. The summary agent must not reread the PDF solely to locate or verify pages. If the parsed Markdown has no reliable page locator, retain the exact quotation, leave the page blank, mark it `source_text`, and set human review as required. The local builder verifies source-text matches without invoking an LLM.
- Before the summary read, remove embedded Base64/data-URI image payloads from a temporary input view; preserve the canonical parsed Markdown unchanged. This is an input-token optimization only and must not reduce the required deep-summary detail.
- Filename normalization has an admission stage and a finalization stage. Use a provisional stem after parser extraction to admit the record and pass the parsed source to the summary skill. After summary metadata is finalized, `scripts/fill_summary_cards.py` rekeys the PDF, source, shell card, wiki node, and parse manifest to `YYYY_Author_ShortTitle`, updates `stem`, `record_id`, provenance paths, and internal links, and returns the final card path. Include at most three author surnames and three short-title words, then suffix same-year/same-author collisions as `Lee-a`, `Lee-b`, and so on. Do not spend a second full-document LLM read for filename decisions.
- Card YAML keeps `record_id`, `stem`, bibliographic fields, one `tags` list, `summary`, `provenance`, and `verification`. Wiki synthesis remains owned by `scripts/build_wiki.py`; do not add a card-level `related` source of truth.
- Report failures instead of claiming completion.
- A single ingest/refresh operation must run the complete rebuild, including wiki category indexes. Preserve curated index prose, append new pages, and fail QC on broken wikilinks or synthesis pages that are empty/link-only.
- The optional presentation layer is `wiki-site/`, generated from canonical `wiki/`, `cards/`, and `sources/` Markdown by `scripts/build_html_site.py`. It is static, dependency-free, GitHub Pages-compatible, and never replaces or edits the canonical Markdown records. Original PDFs and private intake material remain local and are never part of the public site.
