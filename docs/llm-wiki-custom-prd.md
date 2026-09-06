# llm-wiki Custom Build PRD

> Version: 1.4
> Status: implementation specification
> Language: configurable per vault/project; the setup must ask the user before creating knowledge content.

> **v1.2 quality correction (2026-09-05):** A parsed source, metadata shell, bibliography entry, or link-only wiki node is not a completed ingest. Completion now requires a source-grounded detailed summary, a populated synthesis connection, and content-aware QC. The default card state is `unsummarized` until that work is done.
>
> **v1.3 summary/schema correction (2026-09-06):** Deep summaries must be substantially developed, section-sensitive, and evidence-backed with direct source citations whenever the source text and relative page can be verified. Card YAML is consolidated: redundant identity/path/topic fields and `review_log` are removed; summary state lives under a `summary` block; verification remains the place for quote, claim, and human-review evidence.
>
> **v1.4 summary-efficiency correction (2026-09-06):** Summary agents read a temporary sanitized view of the parsed Markdown, never embedded Base64/data-URI image payloads, and do not reopen the PDF solely for page verification. Deep-summary detail and direct-citation requirements are unchanged. Page numbers are retained only when the parsed Markdown supplies a reliable locator; otherwise the page is blank, the exact quote is marked `source_text`, and human review remains required.

## 1. Purpose

Build a portable, llm-wiki-native research knowledge base that can be created in any working folder and operated through natural-language requests from Codex, Claude, GJC, Discord, Slack, or another file-and-shell-capable LLM agent.

This document is self-contained. The folder in which the implementation agent is started is called `${ROOT}`. Do not hard-code a Windows drive, OneDrive path, WSL path, or provider-specific project path.

The runtime contract supports both Windows native and WSL2. Each surface uses its own platform-native Python/Node environment, while the project Markdown root may be shared through a mounted folder. Global KM/search skills must be installed in each agent runtime that will execute them; a Windows plugin install does not automatically install the WSL plugin.

### 1.1 Independent paper and wiki language selection

The system has two language settings and must ask for them independently at first setup, or whenever either is missing:

1. “Which language should paper records use for parsed sources, cards, and summaries?” Offer English, Korean, and “another language (specify)”. This project defaults to English (`paper_language: en`).
2. “Which language should the wiki and synthesis/navigation pages use?” Offer English, Korean, and “another language (specify)”. This project currently uses Korean (`wiki_language: ko`).

Do not infer either answer from the conversation language, operating-system locale, PDF language, or model name. Record both choices in the local project configuration:

```json
{
  "paper_language": "en",
  "paper_language_name": "English",
  "wiki_language": "ko",
  "wiki_language_name": "한국어"
}
```

The output boundary is strict: `sources/`, `cards/`, paper summaries, and bibliographic metadata use `paper_language`; `wiki/`, overview/concept/question/project explanations, index labels, synthesis links, and user-facing navigation use `wiki_language`. Always preserve original paper titles, author names, quotations, and citation metadata. A Korean wiki must not cause the card or source to be written in Korean. Existing pages must not be bulk-translated without explicit user direction; a language change applies to new or explicitly refreshed wiki records.

The implementation must follow this order:

```text
create structure
  -> install local instructions and templates
  -> configure parsing and deterministic scripts
  -> ingest one PDF
  -> verify the complete record
  -> enable batch ingest
  -> connect global KM and project adapters
```

The current operating mode is manual ingest. Always-on monitoring, remote agents, Discord/Slack event handling, and scheduled assistants are later extensions, not prerequisites.

Before creating or installing any runtime, the implementation agent must ask and record the intended operating surface: Windows native, WSL/Linux, macOS, or mixed Windows+WSL. It must also ask and record the preferred ChatOps surface: Discord or Slack. These questions are required because Python environments are OS-specific even when the project files are shared, and ChatOps credentials/configuration are provider-specific. The agent may proceed without asking only when the user has already explicitly chosen both in the same setup request.

Environment setup is idempotent: detect the available Python runtime and required packages first; keep compatible installations and skip them; install only missing dependencies in the approved runtime; never reinstall or upgrade working packages unnecessarily. When `${ROOT}` is inside OneDrive, Dropbox, Google Drive, iCloud Drive, Synology Drive, or another sync-managed/cloud folder, do not create `.venv`, `venv`, virtualenv, conda env, package cache, model cache, or heavyweight runtime dependency folders under `${ROOT}`. Docling and related PDF dependencies must be installed in the global/user Python runtime or in an explicitly approved environment outside all cloud-synced folders. Windows-specific heavyweight Python environments must be centralized in a non-cloud path such as `D:\win-python\...`; when a Windows virtual environment is needed, create or reuse it under that approved base path, not under `${ROOT}`. WSL-specific environments must be centralized separately in a non-cloud path such as `D:\WSL\...`. A Windows environment and a WSL/Linux environment must not share the same `venv` or `site-packages` directory: they have different executable layouts, activation scripts, path semantics, and native binary wheels. They may share the same project source files and research data, but not the same Python environment folder. If an existing outside-cloud runtime is available, prefer reusing it after an import/version check. If installation requires unavailable permissions, network access, or credentials, stop before ingest and report the exact prerequisite instead of pretending the setup succeeded.

macOS must use its own macOS-native Python environment and package/cache locations outside cloud-synced folders. Do not reuse Windows or WSL/Linux environments on macOS, and do not place macOS virtual environments, Homebrew caches, pip caches, HuggingFace caches, Docling/OCR model caches, or other heavyweight runtime folders under iCloud Drive, Dropbox, Google Drive, OneDrive, or another sync-managed folder.

## 2. Authority and design baseline

This PRD is self-contained and is the implementation authority. An implementation agent must not require any companion file, local drive path, or previous conversation to build the system.

The design incorporates a source-to-wiki flow with parsed sources, synthesis links, verification evidence, audit reports, and explicit agent behavior. Knowledge Manager is an external search and capture layer, not a second canonical wiki.

The repository may contain separate rationale or user-guide documents, but they are optional documentation only. They are not installation prerequisites and must not be treated as runtime dependencies.

### 2.1 ChatOps selection

- Discord and Slack are supported as parallel ChatOps surfaces for notifications, operational commands, and future event-triggered workflows.
- During setup, ask the user to choose one preferred surface: Discord or Slack. Configure the selected provider and record the choice in the local adapter/config.
- During setup, ask the user to choose the paper-record language and wiki/synthesis language independently of the ChatOps surface and record both in the local adapter/config.
- The core workflow, file contracts, and scripts must remain usable without either provider or its credentials. Provider-specific adapters must call the same underlying deterministic scripts and must not become a second source of truth.

Do not copy the baseline blindly. Preserve its useful structure while applying these custom decisions:

- one canonical record per paper;
- PDF, parsed source, card, wiki node, registry entry, and bibliography use the same stable stem and record ID;
- Docling is the default PDF parser;
- `sources/` is the canonical parsed source for content verification;
- `cards/` uses the detailed research-summary template embedded in this PRD;
- initial paper nodes stay flat under `wiki/`; category expansion requires a proposal and human approval;
- `refs.bib` is generated from approved card metadata and registry data;
- `open` and `locked` status is human-controlled;
- Crossref and OpenAlex produce audit evidence and recommendations, not silent metadata overwrites;
- Zotero data is legacy input only, not a full-library ingest dependency;
- the system is usable without Zotero after the legacy bibliography has been imported.

## 3. Portable root and folder contract

`${ROOT}` means the current implementation or research database folder. All paths below are relative to it.

```text
${ROOT}/
├── AGENTS.md
├── CLAUDE.md
├── README.md
├── index.md
├── inbox/                         # user drops new PDFs here
├── papers/                        # admitted canonical PDFs
├── papers-supplementary/          # supplementary files when needed
├── sources/                       # Docling parsed source Markdown
├── cards/                         # one detailed summary card per paper
├── wiki/                          # paper nodes and synthesis layer
│   ├── overviews/
│   ├── concepts/
│   ├── questions/
│   └── projects/
├── agenda/
│   ├── projects/
│   ├── citation-packets/
│   ├── search-notes/
│   ├── km-inbox/
│   └── backlog/
├── materials/
│   └── km-captures/
├── registry/
│   └── legacy/                    # imported old Zotero refs.bib only
├── indexes/
├── qc/
├── logs/
├── scripts/
├── templates/
├── .agents/
│   └── skills/
├── refs.bib                       # generated canonical bibliography
└── km-config.json                 # local adapter for globally installed KM
```

### 3.1 Storage rules

- `inbox/` is the only simple intake location for the current manual workflow.
- After successful validation, the PDF moves from `inbox/` to `papers/`.
- `sources/{stem}.md` is the parsed source and must remain available for detailed verification.
- `cards/{stem}.md` is the detailed human-readable research record.
- `wiki/{stem}.md` is the navigational/synthesis node. It is not a replacement for the card.
- Do not duplicate a card merely because a paper belongs to multiple topics.
- `refs.bib` at the root is generated output. Never manually edit it.
- An old Better BibTeX export may be stored as `registry/legacy/refs.bib` and may be searched for candidates, but it is not canonical until the paper is admitted and its card is verified.
- Do not create category folders during the first ingest. Ask the LLM to report category candidates only.
- Obsidian reads this Markdown tree; it is not the execution engine and Obsidian Sync is not required.

### 3.2 Stable identity

Every admitted paper must have:

- `record_id`: stable internal ID;
- `stem`: filesystem-safe shared stem;
- `citation_key`: unique Pandoc/ BibTeX key;
- matching PDF, source, card, and wiki paths;
- a registry entry with status, provenance, and timestamps.

Canonical new-ingest stem and filename format:

```text
YYYY_Author_ShortTitle
```

The canonical PDF filename is `YYYY_Author_ShortTitle.pdf`; source, card, wiki, registry, and bibliography records reuse the same `stem`. `ShortTitle` is at most three content words. Include up to the first three detected author surnames in the author component. If year, author, and short-title collide, append a deterministic suffix to the author component, for example `2024_Lee_AI_Teacher_Agency`, `2024_Lee-a_AI_Teacher_Agency`, then `2024_Lee-b_AI_Teacher_Agency`.

### 3.3 Paper-scoped maintenance and isolation

Every ingest, audit, correction, and refresh task must resolve an exact `record_id` before writing. By default, the write scope is limited to the identified paper and its corresponding PDF, source, card, wiki node, registry entry, index entries, bibliography entry, and QC records.

- Do not modify any other paper's card, YAML, source, wiki node, registry entry, index entry, `refs.bib` entry, or QC evidence unless the user explicitly requests a multi-paper operation.
- A user correction to one card must update only that paper's derived records. Generated aggregate files may be updated through a targeted merge, but non-target records and bibliography entries must remain unchanged, including their existing order and content.
- A `locked` card and its corresponding `refs.bib` entry are protected from audit-driven or inferred changes. They may change only after the user explicitly directs or approves that specific paper's correction, and the evidence and approval must be recorded.
- A global rebuild is not a reason to rewrite unrelated paper records. If a tool cannot preserve non-target records, it must stop before writing and report the limitation.

Do not bulk-rename legacy files without a migration manifest. For a new record, keep the same stem across all layers.

## 4. Canonical ingest workflow

The default user request is short:

```text
이 파일 ingest해 줘.
```

or:

```text
inbox의 새 PDF를 전부 ingest해 줘.
```

The LLM must interpret this as the complete workflow below. The user must not need to name Python scripts.

```text
discover inbox PDFs
  -> identify duplicate / already processed files
  -> extract text with Docling
  -> save source Markdown and provenance
  -> validate PDF and extracted text
  -> derive canonical YYYY_Author_ShortTitle stem from parsed source metadata
  -> rename parsed source to sources/{canonical-stem}.md
  -> move valid PDF to papers/{canonical-stem}.pdf
  -> create detailed card from templates/template-paper-summary.md
  -> create paper wiki node and synthesis links
  -> rebuild registry and indexes
  -> regenerate refs.bib
  -> run QC
  -> report success, failure, duplicate, excluded, and needs-review items
```

The workflow is idempotent. Repeating it must not create a second record for the same DOI, file hash, or stable stem. Failed files remain in `inbox/` with a log entry and are not silently moved.

Filename normalization happens after parsing and before card creation. The parser may create a provisional `sources/{provisional-stem}.md`, but ingest must then derive the canonical stem from already extracted source metadata near the beginning of the parsed source, rename the source, move the PDF under the same stem, and pass that canonical source path to card/wiki generation. This must not trigger a second full-document LLM read. LLM judgment is reserved for the later summary-writing stage, where the active agent reads the canonical parsed source and writes the detailed card.

Do not use `ingest_batch.py` as a harmless no-op validation unless `inbox/` has first been inspected and confirmed empty. `ingest_batch.py` is an ingest command and may move admitted PDFs from `inbox/` to `papers/`. For setup validation that must not ingest anything, run registry, index, bibliography, and QC builders directly.

### 4.1 Source parsing policy

- Docling is the default parser.
- Preserve relative page markers where available.
- Store parser name, version, source hash, parse timestamp, and warnings in source frontmatter or the ingest manifest.
- If parsing fails, do not fabricate a source or summary. Report the failure and retain the original PDF.
- The parsed source is the first content-verification source; the PDF is the final visual/source check.
- Parsing and ingest may inspect the PDF as required by the extractor, but summary writing must not reopen or send the PDF merely to locate or verify page numbers. Page-level checks for summaries are manual unless reliable page markers already exist in the parsed Markdown.

Before the first ingest, the implementation agent must check whether Python and Docling are available in the approved runtime. If Docling is present and importable, reuse it. If it is missing, install the required package in the global/user Python runtime or another explicitly approved environment outside all cloud-synced folders, then run a minimal import/version check. Never create or use a project `.venv` under a OneDrive-backed or otherwise cloud-synced `${ROOT}`. WSL and Windows/PowerShell have separate runtimes and must be checked independently; do not point both platforms at the same environment directory. Windows-native commands may use a Windows Python environment under the approved Windows base path, while WSL commands may use a WSL environment under the approved WSL base path. When using a WSL runtime from Windows, invoke it through `wsl` and record both the Windows path and the WSL path. The agent must report whether the parser was reused, installed, or unavailable, and must record where the runtime lives.

`opendataloader-pdf` and `pdftotext` are optional fallback extractors, not replacements for Docling. Before installing them, the agent must tell the user which operating surfaces are missing them and let the user choose whether to install Windows only, WSL/Linux only, macOS only, or multiple platform-specific installations. Install each fallback extractor in the matching OS environment only; do not assume that installing it in WSL makes it available to Windows, or that installing it in Windows makes it available to WSL.

For Windows, install Windows-native fallback tools into or alongside the approved Windows runtime base such as `D:\win-python`. For WSL/Linux, install Linux fallback tools from inside WSL, preferably through the WSL distribution's package manager or that WSL environment's Python package manager. For macOS, install macOS-native fallback tools only in macOS-approved locations outside cloud-synced folders.

### 4.2 Summary and wiki policy

The detailed card is generated first from the parsed source and the embedded template. Before the LLM reads it, the implementation must create a temporary sanitized summary view with `scripts/prepare_summary_input.py`; this view removes embedded Base64/data-URI image payloads without modifying the canonical source. The active LLM agent reads that view once and writes the summary/evidence; deterministic scripts may create the record shell but must never mark a shell as summarized. The wiki node is a navigational and synthesis layer that links to the card, source, and relevant overview/concept/question pages.

Summary verification is token-efficient and source-first. `scripts/fill_summary_cards.py` and `scripts/qc_report.py` perform local validation and do not call an LLM. They may read the canonical parsed source locally to check exact quote matches, but they must not send it to another model. A summary agent must not reopen the PDF for page verification. When a reliable page marker is present in the parsed Markdown, evidence uses `page: N` and `verification: source_page`; when it is absent, evidence uses `page: ""` and `verification: source_text`, and the card records that page-level verification is pending manual review. No page number may be invented. The deep-summary depth, section coverage, and direct-quotation requirements below remain mandatory.

#### 4.2.1 Summary completion gate

A paper is `summarized` only when its card contains source-grounded prose in all applicable sections. A template copied without substantive content is `unsummarized`, regardless of whether its YAML is complete. A `deep` summary is not an abstract-length recap: it must reconstruct the paper's argument, evidence base, major results, interpretation, limitations, and relevance at a level suitable for later literature-review reuse.

At minimum:

- `One-sentence Summary` states the paper's central contribution;
- `Purpose` identifies the problem, aim, or research questions;
- `Method`/`Methodology` describes the actual design, participants/data or review procedure when reported;
- `Theory & Literature Review` or the equivalent background section identifies the intellectual context, main constructs, prior-study pattern, and stated gap;
- `Findings`/`Results`/`Key Claims` contains multiple substantive claims grounded in the source, preserving distinctions among themes, quantitative/statistical results, examples, or review synthesis strands when present;
- `Discussion`/`Conclusion` explains the authors' interpretation, contribution, implications, caveats, and relationship to the stated problem;
- `Limitations` and `Relevance to My Study` are completed when applicable;
- review, conceptual, theoretical, and book sources follow their actual structure and do not receive invented empirical sections;
- substantive claims in the Literature Review/Background, Findings/Results, and Discussion sections are supported by direct quotations with verified relative pages whenever reliable page markers are available in the parsed source; otherwise each claim retains an exact source-text quotation, uses a blank page, and is explicitly labelled `source_text`/`page unavailable` for manual page review;
- the `Directly Citable Evidence` table collects the strongest quotes for later reuse and records claim/page verification status;
- no required section may contain only template instructions, an empty heading, or generic text such as “see the original.”

The implementation must record `verification.summary_verified`, quote/claim verification status, and `requires_human_review` independently. `summary.status: summarized` does not mean that page-level quotation verification or human approval is complete.

#### 4.2.2 Synthesis and navigation completion gate

Every admitted paper must have both:

1. a paper node linking to its card and parsed source; and
2. at least one bidirectional link to an existing `overviews/` or `concepts/` page, with a sentence explaining the paper's relationship to that page.

If no suitable synthesis page exists, the ingest must create an explicit unresolved-link QC item and a dated backlog entry. A generic “Needs overview…” placeholder is not a passing result. `indexes/papers.md` is the paper catalog; `wiki/index.md` is the Obsidian study start page; category indexes are navigational pages and must contain real links or an explicit empty-state reason.

Every admitted paper must connect to at least one synthesis target, or create an explicit unresolved-link entry in QC. A paper is not considered fully ingested merely because a PDF and a summary file exist.

During ingest and maintenance, also perform a supersede/correction/retraction check when the source or metadata indicates a newer version. Record the result in verification/QC evidence and the registry; do not use a card-level `review_log`. Rebuild indexes after every accepted structural change, and preserve dated logs for batch, metadata, link, and citation audits outside the card YAML.

Initial wiki behavior:

```text
wiki/{stem}.md
```

Later category behavior is proposal-driven. A paper that belongs to several topics keeps one card and one record; multiple wiki pages or overview links may point to it.

## 5. AGENTS.md contract

The implementation must create a root `AGENTS.md` containing the following behavior, adapted only for the local `${ROOT}` paths.

### 5.1 Startup

- Read `AGENTS.md`, `km-config.json`, and relevant project instructions at the beginning of every session.
- Do not rely on memory from a previous session.
- Inspect the relevant indexes before scanning the entire tree.
- Report the active root and scope before destructive or broad changes.

### 5.2 Retrieval policy

1. Search `indexes/`, `wiki/`, and `cards/` first.
2. Read `sources/` when the card is incomplete, uncertain, or a claim needs verification.
3. Read the PDF in `papers/` when parsed text or page/figure context is insufficient.
4. Use external web or scholarly search only when explicitly requested or when running metadata audit.
5. If the repository does not contain evidence, say so. Do not improvise a citation, DOI, result, or claim.

### 5.3 Ingest trigger

When the user says “ingest this file”, “ingest all new PDFs in inbox”, or equivalent natural language, execute the complete ingest workflow in Section 4. Do not stop after parsing or summary creation.

The final report must classify every input as:

- success;
- failure;
- duplicate;
- excluded;
- needs human review.

### 5.4 Bibliography policy

- Card YAML and registry are inputs.
- Root `refs.bib` is generated output.
- After a card metadata change, rebuild registry, indexes, root `refs.bib`, and QC in the same task.
- Project `references.bib` files are generated subsets and must not be manually edited.
- Use only citation keys present in the relevant generated bibliography.

### 5.5 Metadata policy

- New cards start as `metadata_status: open` unless the user explicitly approves a locked state.
- Crossref is the primary automated metadata comparison source.
- OpenAlex is a complementary source for DOI matching, topics, citation graph, and open-access locations.
- Publisher page and final PDF outrank API disagreement.
- An audit may recommend changes, but must not overwrite `locked` metadata.
- A human approval changes `open` to `locked`; the approval and evidence are recorded.

### 5.6 Taxonomy policy

Do not automatically split categories. Generate a proposal when one or more signals appear:

- a category is difficult to navigate because of volume or link density;
- a repeated theme cannot be described by existing categories;
- two categories repeatedly contain the same papers and overview links;
- an overview would connect several categories around one question, method, or theory.

Write the proposal to `qc/taxonomy-review-YYYY-MM-DD.md`. Only a user-approved proposal may create, merge, or move wiki category paths. Cards, sources, and registry records remain single canonical records.

## 6. Embedded summary card template

The implementation must write the following content to `templates/template-paper-summary.md`. The external template is not a runtime dependency.

```markdown
---
record_id: ""
stem: ""
type: "paper" # paper | book_chapter | conference_paper | review | conceptual | theoretical | book | report | other
research_design: "" # empirical | review | conceptual | theoretical | book | mixed | not_applicable

title: ""
year: ""

authors:
  - "Last Name, First Name"

citation_key: ""
doi: ""
url: ""

metadata_status: "open" # open | locked
metadata_authority: "publisher_pdf" # publisher_pdf | crossref | openalex | legacy_zotero | human_verified
publication_stage: "" # online_first | version_of_record | in_press | book | chapter | conference | unknown

citation_info:
  source_type: "journal"
  source_title: ""
  editors: []
  volume: ""
  issue: ""
  pages: ""
  article_number: ""
  publisher: ""

tags: []

summary:
  level: "deep" # quick | structured | deep
  status: "unsummarized" # unsummarized | summarized | needs_review
  structure_policy: "source_structure" # empirical_sections | source_structure | selective_sections

provenance:
  pdf_path: "papers/"
  source_path: "sources/"
  parsed_with: "docling"
  source_hash: ""
  metadata_checked_at: ""
  metadata_sources: []

verification:
  summary_verified: false
  quote_verification_status: "partial" # verified | partial | failed | not_applicable
  quote_verification_pass_rate: 0.0
  claim_verification_pass_rate: 0.0
  requires_human_review: true
  verified_at: ""
---

# Quick Card

## Bibliographic Metadata

## One-sentence Summary

## Keywords

# Structured Summary

## Purpose

## Background (Theory & Literature Review)

## Method

## Findings

## Discussion & Conclusion

# Deep Summary

> Write a developed, reusable research summary, not a short abstract. Preserve the source's actual argument and section structure.
> For each substantive claim, provide a short, exact direct quotation. Add `(p. N)` only when the parsed source supplies a reliable page marker. If page alignment is unavailable, leave the page blank and label the evidence `source_text`/`page unavailable` for manual review; never invent a page or reopen the PDF solely for this purpose.
> Prioritize direct citation support in the Literature Review/Background, Findings/Results, and Discussion sections. The temporary summary input must omit embedded Base64/data-URI image payloads, while the canonical parsed source remains unchanged. These token-saving steps must not shorten or simplify the required deep summary.

## Summary Mode and Source Structure

- `empirical`: use Methodology and Findings when present.
- `review`: summarize scope, organization, synthesis, gaps, and implications; omit absent empirical sections.
- `conceptual` or `theoretical`: summarize concepts, framework, propositions, argument, contribution, and limitations.
- `book` or `book_chapter`: follow the actual book or chapter structure.
- `mixed` or `other`: follow the source headings and explain the chosen structure.

Do not create artificial Method, Participants, Data, or Findings sections for a non-empirical source. Omit non-applicable sections and record the reason in `Citation Notes`.

## Purpose

## Theory & Literature Review

- Theme:
  - Evidence: "Direct quotation" (p. N) when a parsed-source page marker exists; otherwise (page unavailable; source-text-verified) for manual review
  - Interpretation:
  - Relationship to the paper's gap or research questions:

## Gaps & Research Questions

## Theoretical Framework

## Methodology

### Context

### Participants

### Data Sources

### Procedure

### Analysis Methods

## Findings

For each major finding/result/theme, state the claim, describe the evidence or analytic basis, include at least one direct quotation when available, and explain why the result matters for the paper's argument.

## Key Claims

## Directly Citable Evidence

| Claim or theme | Direct quotation or labelled paraphrase | Relative page | Verification |
|---|---|---:|---|
|  |  |  | verified / partial / failed / not_applicable |

## Discussion

Explain how the authors interpret the findings or argument, what contribution they claim, what implications they draw, and which caveats shape the interpretation. Support major interpretive claims with direct citations or labelled page-unverified paraphrases.

## Conclusion

## Unique Contributions

## Limitations

## Future Work

## Relevance to My Study

## Possible Use in Literature Review

## Citation Notes
```

Card YAML must not include redundant or workflow-only fields such as `paper_id`, `file_name`, `topics`, `projects`, `related`, or `review_log`. Use `record_id` as the stable internal identity, `stem` as the shared filesystem stem, `tags` for lightweight user-facing labels, `summary.*` for summary state, and `verification.*` for quote/claim/human-review evidence. Source/PDF paths belong in `provenance`; wiki/synthesis links are maintained by the wiki layer and QC outputs, not by a duplicated `related` YAML block.

### 6.1 Flexible document-type and evidence rules

The template is deliberately section-flexible. Before writing the summary, classify the source as empirical, review, conceptual, theoretical, book/chapter, mixed, or other.

- For empirical research, complete Methodology and Findings using the source's actual sections.
- For review papers, summarize review scope, search or selection procedure when reported, organizing themes, synthesis, gaps, and implications. Do not invent participants or findings.
- For conceptual or theoretical papers, summarize the problem, concepts, framework, propositions, argument structure, contribution, and limitations. Method and Findings may be omitted.
- For books and chapters, follow the actual chapter/book structure and argument. Do not force journal-style headings.
- For all document types, make the deep summary detailed enough to support later drafting: capture the paper's argumentative sequence, not only isolated bullet points.
- Omit sections that do not exist or are not applicable, and record the omission in `Citation Notes`.
- Every substantive summary claim should be supported by a direct quotation with a relative page marker, such as `"..." (p. 12)`, when the parsed source provides reliable page alignment; this is mandatory for major Literature Review/Background, Findings/Results, and Discussion claims when such markers are available.
- If page alignment is unavailable, retain the exact quotation with a blank page, mark it `source_text`/`page unavailable`, and set the relevant verification status for manual review. Do not reopen the PDF solely to locate or verify summary pages, and do not invent a page number.
- The `Directly Citable Evidence` table must not be ornamental. It must contain reusable evidence rows for the main claims, especially those from Literature Review/Background, Findings/Results, and Discussion.
- Do not invent DOI, pages, publisher, methods, findings, quotations, or page numbers.

The LLM must extract all authors and exact bibliographic information when present, leave unknown fields empty, and flag uncertainty.

## 7. Script contracts

Create scripts under `scripts/`. The PRD does not prescribe implementation language beyond Python compatibility, but each script must be deterministic where possible, idempotent, log its inputs and outputs, and return a non-zero status on an incomplete required operation.

### 7.0 `prepare_summary_input.py`

- Input: one canonical parsed Markdown source.
- Output: a temporary Markdown view for the summary agent; the canonical source is never edited.
- Must replace embedded `data:image/...;base64,...` image payloads with a short omission marker and preserve all textual content, headings, metadata, and existing page markers.
- Must not call an LLM, open the PDF, or perform page verification.
- Removing image payloads is an input-token optimization only; it must not shorten, filter, or otherwise simplify the required deep-summary content.

### 7.1 `parse_pdf.py`

- Input: one PDF path, output directory, parser configuration.
- Output: `sources/{stem}.md`, parse manifest, warnings.
- Default parser: Docling.
- Fallback chain: Docling first; if it fails or produces unusable text, try `opendataloader-pdf`; then `pypdf`; then `pdftotext`. Record which extractor succeeded and every earlier failure in the parse manifest.
- Must preserve source hash and parse provenance.
- Must fail visibly when text extraction is empty or structurally unusable.

### 7.2 `ingest_batch.py`

- Input: `${ROOT}/inbox/*.pdf`.
- Output: admitted PDFs in `papers/`, sources, cards, wiki nodes, manifest, logs, and QC updates.
- Must parse first, then normalize the filename/stem from parsed metadata before card creation.
- Must use `YYYY_Author_ShortTitle` for newly admitted PDFs and all downstream Markdown layers; `ShortTitle` is at most three words and author names include up to the first three detected surnames.
- Must handle same-year/same-author/same-short-title collisions by suffixing the author component deterministically, for example `2024_Lee_AI_Teacher_Agency`, `2024_Lee-a_AI_Teacher_Agency`, `2024_Lee-b_AI_Teacher_Agency`.
- Must avoid duplicate token spend by reusing the parsed source text for filename normalization rather than asking an LLM to read the full PDF again.
- Must detect duplicate hash, DOI, and citation key conflicts.
- Must continue processing independent files while classifying failures.
- Must not call another LLM CLI or spawn an uncontrolled agent. LLM reasoning is performed by the active agent; scripts handle file operations, parsing, indexing, and validation.

### 7.3 `build_card.py`

- Input: parsed source, metadata candidates, embedded template.
- Output: `cards/{stem}.md` with consolidated YAML and detailed sections. A newly created shell must use `summary.status: unsummarized`; this script must not claim that an LLM summary exists.
- Must generate the current YAML schema: `record_id`, `stem`, bibliographic metadata, `citation_info`, `tags`, `summary`, `provenance`, and `verification`. It must not generate `paper_id`, `file_name`, `topics`, `projects`, `related`, or `review_log`.
- Must preserve human edits when updating an existing card unless a field is explicitly targeted.
- Must mark unresolved fields and claims for review.
- Summary preparation must use `scripts/prepare_summary_input.py` to remove embedded Base64/data-URI images from a temporary LLM input view; it must preserve the canonical source and must not reduce deep-summary detail.
- Summary verification must not reopen or send the PDF to an LLM solely for page mapping. A reliable parsed-source page marker uses `source_page`; otherwise a blank page with `source_text` is retained for manual review.
- Must not silently convert an empty/template body to `summary.status: summarized`.
- The completion validator must reject a card whose applicable summary sections are empty, instruction-only, generic placeholder prose, or too shallow to reconstruct the paper's argument and evidence.
- The completion validator must check direct-citation coverage for major Literature Review/Background, Findings/Results, and Discussion claims. It must record pass rates and `requires_human_review` in `verification`; page-unavailable claims may pass source-text quote validation but remain flagged for manual page review.

### 7.4 `build_wiki.py`

- Input: card, source, existing wiki index.
- Output: `wiki/{stem}.md`, links to synthesis pages, a concise source-grounded summary, and an unresolved-link report if no suitable anchor exists.
- Must not create category splits without an approved taxonomy proposal.
- Must reject or flag a link-only node that has no summary and no synthesis connection.
- Must own wiki/synthesis relationships separately from card YAML. Related overview/concept/question links may be generated from maintained mapping logic, existing wiki pages, or explicit user curation, but they must not require or duplicate a card-level `related` YAML block.

### 7.5 `build_registry.py`

- Input: cards, sources, wiki nodes, ingest manifest.
- Output: `registry/works.jsonl` or an equivalent transparent structured registry.
- Required fields: record ID, stem, paths, title, authors, year, citation key, DOI, metadata status, publication stage, provenance, and last update.

### 7.6 `export_refs_bib.py`

- Input: registry and approved card YAML.
- Output: root `refs.bib`; optional project subset under `agenda/projects/{name}/references.bib`.
- Must produce stable keys and valid BibTeX.
- Must support filtering by `open`, `locked`, project, or explicit record list.
- Must never modify card YAML.
- For a single-paper maintenance task, it must update only the targeted `record_id` entry and preserve all non-target entries, order, and content.

### 7.7 `metadata_audit.py`

- Input: cards with `metadata_status: open` by default; locked cards only when drift audit is explicitly requested.
- Sources: Crossref, OpenAlex, publisher or official landing page when available, and the PDF.
- Output: `qc/metadata_audit.json` and a human-readable report.
- Must distinguish exact match, probable match, conflict, missing, and unavailable.
- Must not overwrite locked metadata.
- An audit report alone must not change any card or `refs.bib` entry. It may write only the audit report and related QC evidence.

### 7.8 `verify_draft_citations.py`

- Input: Markdown draft, project bibliography, optional citation packet.
- Output: `qc/citation_map.tsv` or JSON report.
- Must detect missing keys, unused bibliography entries, duplicate keys, provisional web items, and citation claims without linked evidence.
- Non-zero status when required citations are missing or invalid.

### 7.9 `build_indexes.py` and `qc_report.py`

- `build_indexes.py` rebuilds root and category indexes from current records without deleting human-authored notes. It must keep `indexes/papers.md`, `wiki/index.md`, and category indexes navigable, append newly created category pages, and never replace populated human-authored pages with placeholders.
- `qc_report.py` summarizes broken links, duplicate stems/DOIs, missing source/card/wiki layers, unresolved metadata, unverified quotes, stale generated outputs, empty required summary sections, shallow deep summaries, missing direct-citation coverage, template-instruction remnants, synthesis orphans, and placeholder wiki prose. It must resolve every wikilink to an actual Markdown file. Any such content-quality issue makes the record needs-review and prevents a batch from being reported as fully successful.

### 7.10 Local operations skill and routing

Create one local skill, for example `.agents/skills/llm-wiki-ops/SKILL.md`, rather than many user-facing skills. This is an internal router; users continue to use natural language.

The skill maps intents to the existing contracts:

| Intent | Required sequence |
|---|---|
| `ingest` | discover inbox → parse → validate → source/card/wiki → registry/indexes/refs.bib/QC |
| `search` | indexes → wiki → cards → sources → PDF when necessary |
| `audit` | metadata/link/citation checks → dated QC report |
| `draft` | project AGENTS → citation packet → project references.bib → Markdown → citation verification |
| `taxonomy` | analyze signals → proposal only → human approval before structural change |

The skill must load the root or project `AGENTS.md`, state the active scope, call the appropriate deterministic scripts, and report failures instead of claiming completion. It must not require a provider-specific command name.

Use `metadata_audit.py` as the canonical metadata-audit script name. If compatibility with an existing `audit_metadata.py` name is needed, make it a thin alias and document one source of truth.

## 8. Open/locked and bibliography lifecycle

The lifecycle is:

```text
new card
  -> open
  -> metadata audit
  -> human review
  -> locked approval or open retention
  -> card YAML update
  -> registry/indexes/refs.bib/QC regeneration
```

The initial system has no always-on monitor. Periodic metadata maintenance is a manual natural-language operation with this default cadence: newly ingested cards immediately, open cards weekly or monthly, long-running open cards quarterly, and locked cards only when correction, retraction, or explicit drift is reported. The audit must list the last checked date and classify each record as match, changed, conflict, or unavailable. Human approval is required before changing card YAML; approved changes then trigger registry, indexes, `refs.bib`, and QC regeneration.

When a user edits a card in Obsidian, the next natural-language maintenance request must detect the changed card and regenerate derived outputs. When the LLM edits the card, regeneration is part of the same task.

All such regeneration is paper-scoped. A changed card must be resolved to its exact `record_id`; unrelated cards, locked records, and unrelated `refs.bib` entries must not be modified. An open-card audit may report proposed changes, but must not apply them until the user explicitly approves or directs the change. A locked card or its `refs.bib` entry must remain unchanged unless that specific paper is explicitly approved for correction. Aggregate generated files must use a targeted merge that preserves non-target records; if that cannot be guaranteed, the operation must stop before writing.

Use this natural-language request:

```text
최근 변경된 카드의 metadata와 summary를 반영해서 registry, indexes, refs.bib, QC를 갱신해 줘.
```

For audit:

```text
open 카드의 metadata를 Crossref와 OpenAlex, publisher/PDF와 비교하고 차이만 보고해 줘.
locked 카드는 자동 수정하지 말고 drift만 기록해 줘.
```

For approval:

```text
이 카드의 metadata를 locked로 승인해 줘.
승인 근거를 기록하고 registry, indexes, refs.bib, QC를 갱신해 줘.
```

## 9. Project writing contract

Research projects are consumers of the shared llm-wiki, not alternate copies of the canonical cards.

For each project, create a local `AGENTS.md`, `references.bib`, `citation-packets/`, `drafts/`, `outlines/`, and `review-notes/`. The project config points to `${ROOT}` using a relative path or an explicitly supplied local path at setup time.

Project initialization is an explicit workflow, not a side effect of opening a folder. When an LLM is opened in a new project folder, it must create the local `AGENTS.md`, connect the shared root, generate the project `references.bib` as a subset of the shared root `refs.bib`, create the project directories, and register the citation-verification procedure. A local `AGENTS.md` controls later project sessions, but it does not generate a bibliography by itself.

The project `AGENTS.md` must state:

- the shared llm-wiki root and its read scope;
- the project bibliography path;
- that cards and the shared root `refs.bib` are canonical inputs;
- that project `references.bib` is generated output and must not be manually edited;
- that drafts use only project bibliography keys in `[@citation_key]` form;
- that web candidates outside the registry go to `citation-gaps.md`;
- that citation verification runs before a draft is reported complete;
- that DOCX References are generated by Pandoc/Quarto citeproc.

When shared cards or the root bibliography changes, the project must be refreshed explicitly:

```text
Check the changed shared cards and refs.bib, then regenerate this project's references.bib.
Report removed keys, new eligible keys, and unresolved citation gaps.
```

The drafting contract is:

- search indexes, wiki, and cards first;
- create a citation packet from selected cards;
- use only the project-generated bibliography;
- write Pandoc citations as `[@citation_key]`;
- never invent author-year citations, DOI, or references;
- place web-found but not-yet-admitted items in `citation-gaps.md` or project search notes;
- run `verify_draft_citations.py` before reporting a draft as complete;
- use Pandoc or Quarto citeproc to generate docx and References.

Example conversion contract:

```text
Markdown draft + project references.bib + CSL
  -> citeproc
  -> docx with formatted in-text citations and References
```

## 10. Global Knowledge Manager integration

Knowledge Manager must be installed globally as a skill/plugin so `/km:search` is available from any project folder. Each project receives a local adapter/config that points to the shared `${ROOT}`.

The global KM installation is the executable command surface; it must not be copied into every project. Each project-local `km-config.json` is only routing/configuration. For the current Codex KM plugin, the shared database target is declared in the plugin-readable field `storage.obsidian.vaultPath` (use Windows forward slashes), while `llm_wiki_root` and `search_paths` document the llm-wiki adapter contract. A project may therefore run `/km:search` from its own working directory while reading `D:/OneDrive/2_rch_db` (or another explicitly configured database root). If no local config exists, the command must not guess a sibling or backup folder; it must report the missing target configuration.

Canonical shared-database adapter shape:

```json
{
  "llm_wiki_root": "D:/OneDrive/2_rch_db",
  "storage": {
    "primary": "obsidian",
    "obsidian": {
      "enabled": true,
      "vaultPath": "D:/OneDrive/2_rch_db",
      "defaultFolder": "wiki"
    }
  },
  "search_paths": ["indexes", "wiki", "cards", "sources"]
}
```

`vaultPath` identifies the read/search root; it does not authorize KM to write canonical cards, wiki pages, registry data, or `refs.bib`. Search results may be saved only to the configured project-safe capture paths.

KM responsibilities:

- search the shared llm-wiki and the active project;
- collect external pages, PDFs, OCR, and notes;
- write captures only to `agenda/km-inbox/`, `agenda/search-notes/`, or `materials/km-captures/`;
- separate internal wiki results from external search candidates;
- hand approved paper candidates to the llm-wiki ingest workflow.

KM must not directly edit `cards/`, `wiki/`, `registry/`, or root `refs.bib`. It must not create a competing canonical wiki.

`km-config.json` must contain the local root, search paths, write-safe paths, and canonical ingest handoff. Secrets and API keys must remain outside the repository.

## 11. Runtime and collaboration adapters

Any agent capable of reading/writing files and running the scripts may operate the system. Provider-specific behavior must not change the workflow contract.

- Codex/WSL and GJC/Windows may use different runtimes, but they must share the same relative file contracts and generated outputs.
- Discord and Slack are parallel ChatOps interfaces; neither is a database.
- Each bot session must have one explicit `cwd` and permission boundary: the root for ingest/maintenance or a project folder for drafting.
- A bot must not receive unrestricted access to the entire OneDrive tree.
- Obsidian is for reading, linking, and manual card review; it is not required for ingest execution.

### 11.1 Role boundaries

- Wiki maintainer: ingest, card/source consistency, synthesis links, registry, indexes, and QC.
- Project researcher: internal retrieval, evidence matrix, citation packet, and project notes.
- Draft writer: outline and Markdown manuscript using the project bibliography.
- Critic/reviewer: unsupported claims, citation gaps, evidence quality, and argument structure.
- PI/coordinator: approve taxonomy changes, metadata locking, project priorities, and external communication.

The same LLM may perform several roles, but each task must state its read scope, write scope, and completion report.

### 11.2 Optional operational surfaces

After the core workflow is stable, projects may add `agenda/`, `interactives/`, `slides/`, `peer-review/`, and `note-meeting/` outputs. These are operational views or deliverables, not replacements for `cards/`, `wiki/`, `registry/`, or `refs.bib`.

### 11.3 Optional static HTML presentation layer

The project may expose the structured wiki through a separate, GitHub Pages-compatible static site in `${ROOT}/wiki-site/`. This layer is a presentation copy, not a second source of truth.

- `scripts/build_html_site.py` generates the site from `wiki/**/*.md` without external runtime dependencies.
- The site must include a clean archive/library navigation page, category and paper pages, visible counts, and lightweight client-side title/category search.
- Preserve the language boundary: wiki explanations and navigation use `wiki_language`; paper titles and linked card/source records preserve their English/original form.
- Convert internal wiki links to working `.html` links. Links to canonical `cards/` and `sources/` may point back to repository Markdown paths for later GitHub hosting.
- Rebuilding the site must be idempotent and must not edit `wiki/`, `cards/`, `sources/`, `registry/`, or `refs.bib`.
- The normal refresh/ingest completion path should rebuild `wiki-site/` after Markdown and index generation, then validate that generated HTML, CSS, JavaScript, and local links exist.
- The site must use a responsive layout and avoid framework, build-service, credential, or server requirements so it can be published as a static GitHub Pages artifact.
- When the project is hosted on GitHub, `.github/workflows/pages.yml` should publish `wiki-site/` through GitHub Pages on pushes to `main` and support manual dispatch. The deployment URL and workflow result belong in the completion report.

## 12. Natural-language operation examples

The implementation must support these intents without requiring the user to name scripts:

```text
이 PDF ingest해 줘.
inbox의 새 PDF를 전부 ingest해 줘. 성공·실패·중복·제외·검토필요로 나눠 보고해 줘.
이 논문의 source, 상세 summary card, wiki node가 연결되어 있는지 점검해 줘.
현재 taxonomy에서 분리·통합·overview가 필요한지 제안만 해 줘.
open 카드의 metadata를 점검하고 Crossref, OpenAlex, publisher/PDF 차이를 보고해 줘.
최근 변경된 카드 기준으로 registry, indexes, refs.bib, QC를 갱신해 줘.
llm-wiki 안에서 이 연구 질문과 관련된 카드만 찾아 citation packet을 만들어 줘.
이 citation packet과 project references.bib만 사용해서 Markdown 초안을 작성해 줘.
초안의 citation key와 References를 검증해 줘.
KM 검색 결과 중 PDF가 있고 published paper인 후보만 llm-wiki ingest 대상으로 분류해 줘.
24시간 자동 ingest로 전환할 준비가 되었는지 점검해 줘. 실제 전환은 하지 마.
```

## 13. Future automation gates

Do not create or enable these in the initial build:

- `paper_monitor.py`;
- RSS or continuous external paper discovery;
- 24-hour remote LLM agent;
- Discord/Slack event-triggered ingest;
- scheduler-driven metadata updates;
- automatic category splitting;
- calendar/email assistant.

The LLM may generate a readiness report when requested. It may propose the extension only when one of these signals exists:

- manual inbox processing is delayed or repeated;
- audit logs show recurring failures or stale records;
- category navigation becomes difficult;
- recurring research questions justify a backlog;
- team collaboration requires controlled reporting.

The user approves the proposal before the implementation agent adds a monitor, scheduler, remote credential, external adapter, or category migration.

The evolution path may be represented as five optional operating loops:

- Paper Monitor: discover and report new paper candidates;
- Ingest: convert admitted PDFs into source, card, wiki, and bibliography records;
- External Posting: publish approved summaries or meeting material to the selected Discord or Slack surface, with optional Notion or static-site adapters;
- Audit/Cleanup: detect duplicates, broken links, stale metadata, and superseded records;
- Question to Backlog: turn recurring wiki questions into structured project analysis tasks.

Only the Ingest loop is part of the current manual build. The others remain disabled until their entry conditions and approval are recorded.

## 14. Acceptance tests

The implementation is complete only when all of the following pass:

1. The system can be created in an arbitrary `${ROOT}` without hard-coded machine paths.
2. The root contains AGENTS.md, the embedded summary template, config, scripts, and required folders.
3. One PDF in `inbox/` can be ingested through a short natural-language request.
4. The result contains matching PDF, source, card, wiki, registry, index, bibliography, and QC records.
5. Batch ingest processes all inbox files and classifies every file.
6. Re-running ingest does not duplicate records.
6a. New ingest normalizes filenames after parsing into `YYYY_Author_ShortTitle.pdf`, uses the same canonical stem for source/card/wiki/registry/bibliography, and resolves collisions with author suffixes such as `Lee-a` and `Lee-b`.
7. A card edit regenerates registry, indexes, `refs.bib`, and QC.
8. `open` metadata is audited but not silently locked; `locked` metadata is never silently overwritten.
9. Crossref/OpenAlex disagreement is visible in the audit report.
10. A draft containing an unknown `[@key]` fails citation verification.
11. KM can search from a project folder while writing only to its allowed capture paths.
12. A single-paper correction changes only the targeted record and preserves non-target registry, index, QC, and `refs.bib` records.
13. Audit-only work changes no card or bibliography entry, and a locked record changes only after explicit paper-specific user approval or direction.
14. The system reports that monitoring and remote automation are future extensions rather than pretending they are active.
15. Setup asks the user to choose Discord or Slack, records the choice, and configures the selected ChatOps adapter without changing the core workflow.
16. A newly ingested card has the consolidated YAML schema, uses `summary.status: unsummarized`, and contains no `paper_id`, `file_name`, `topics`, `projects`, `related`, or `review_log` field.
17. A newly ingested card remains `summary.status: unsummarized` until the active agent has written source-grounded content; template-only content cannot pass QC.
18. A representative empirical paper card contains non-empty purpose, method, findings/results, discussion, limitations, and relevance sections, with a developed deep summary and multiple substantive findings rather than one repeated sentence.
19. Literature Review/Background, Findings/Results, and Discussion claims are backed by direct quotations with verified relative pages when available; when page mapping is unavailable, retain the exact quote with a blank page and `source_text`/manual-review verification rather than inventing a page.
19a. Summary preparation strips embedded Base64/data-URI image payloads only in a temporary LLM input view; canonical source Markdown is unchanged, the PDF is not reopened for summary page verification, and unavailable page numbers remain blank with `source_text` evidence for manual review.
20. A representative review/conceptual paper follows its source structure and does not contain invented participants, methods, or findings.
21. Every admitted paper has a bidirectional synthesis link or an explicit unresolved-link QC item; no paper is silently left as a synthesis orphan.
22. `wiki/index.md`, `indexes/papers.md`, and `wiki/{overviews,concepts,questions,projects}/index.md` are navigable and contain real links or a documented empty-state reason.
23. QC fails on empty required sections, untouched template instructions, generic placeholder prose, shallow deep summaries, missing direct-citation coverage, broken links (including links from category indexes), or a `summary.status: summarized` card whose substantive summary gate is not met.
24. Setup asks for and records paper language and wiki language separately; cards/sources/paper summaries use paper language, wiki synthesis/navigation uses wiki language, and original titles, names, quotations, and citation metadata are preserved.
25. The optional HTML layer can be regenerated in one command from `wiki/`, contains working pages for all wiki Markdown files, and does not replace canonical Markdown records.

## 15. Implementation handoff

The implementation agent must:

1. create the folder tree and files under `${ROOT}`;
2. write the AGENTS.md contract and project adapter templates;
3. write the embedded summary template exactly once under `templates/`;
4. implement scripts according to Section 7;
5. run the single-PDF smoke test before batch behavior;
6. run acceptance tests and write a concise result to `logs/setup-validation.md`;
7. preserve existing user files and never delete legacy material without an explicit migration instruction.

No Python source code is required inside this PRD. The script contracts above are the authoritative implementation requirements; generated scripts must be reviewed against them and tested with fixture PDFs and Markdown records.
