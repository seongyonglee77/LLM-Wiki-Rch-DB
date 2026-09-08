---
record_id: ""
stem: ""
title: ""
authors:
  - "Last Name, First Name"
year: ""
type: "paper" # paper | book_chapter | conference_paper | review | conceptual | theoretical | book | report | other
research_design: "" # empirical | review | conceptual | theoretical | book | mixed | not_applicable
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

> A card may be marked `summary.status: summarized` only through `scripts/fill_summary_cards.py` with per-paper evidence JSON. Every substantive claim must have an exact direct quotation. Add a positive page number only when the parsed source provides a reliable page marker; otherwise leave it blank, use `source_text`, and require manual page review. Do not invent quotations or page numbers or reopen the PDF solely for summary page verification.

## Summary Mode and Source Structure

- `empirical`: use Methodology and Findings when present.
- `review`: summarize scope, organization, synthesis, gaps, and implications; omit absent empirical sections.
- `conceptual` or `theoretical`: summarize concepts, framework, propositions, argument, contribution, and limitations.
- `book` or `book_chapter`: follow the actual book or chapter structure.
- `mixed` or `other`: follow the source headings and explain the chosen structure.

Do not create artificial Method, Participants, Data, or Findings sections for a non-empirical source. Omit non-applicable sections and record the reason in `Citation Notes`.

## Purpose

## Theory & Literature Review

- Claim supported by a direct quotation and page locator.
  - Evidence: "Direct quotation" (p. N; source_page-verified), or (page unavailable; source-text-verified) when no page marker exists

## Gaps & Research Questions

## Theoretical Framework

## Methodology

### Context

### Participants

### Data Sources

### Procedure

### Analysis Methods

## Findings

- Finding supported by a direct quotation and page locator.
  - Evidence: "Direct quotation" (p. N; source_page-verified), or (page unavailable; source-text-verified) when no page marker exists

## Key Claims

## Directly Citable Evidence

| Claim or theme | Direct quotation or labelled paraphrase | Relative page | Verification |
|---|---|---:|---|
|  |  |  | verified / partial / failed / not_applicable |

## Discussion

- Interpretation supported by a direct quotation and page locator.
  - Evidence: "Direct quotation" (p. N; source_page-verified), or (page unavailable; source-text-verified) when no page marker exists

## Conclusion

## Unique Contributions

## Limitations

## Future Work

## Relevance to My Study

## Possible Use in Literature Review

## Citation Notes

## Related Links
