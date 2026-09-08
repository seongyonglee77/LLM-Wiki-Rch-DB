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

related:
  wiki: []
  overviews: [] # at least one of overviews/concepts is populated after final mapping
  concepts: [] # at least one of overviews/concepts is populated after final mapping
  projects: [] # optional; only when semantically relevant
  questions: [] # optional; only when semantically relevant
  supersedes: []
  superseded_by: []
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

### Deep-summary extraction standard (mandatory)

Deep summary means a sufficiently detailed reconstruction of the paper's reasoning, evidence, and implications—not a short abstract or a list of generic takeaways. Extract as much source-grounded detail as the paper supports, especially for **Theory & Literature Review**, **Findings/Results**, and **Discussion/Implications**. For each of these major sections, provide:

1. a developed overview explaining the section's role in the paper;
2. at least three distinct substantive claims when the source provides them (more when needed to preserve important comparisons, themes, mechanisms, or quantitative results);
3. an interpretation of what each claim means;
4. an exact direct quotation as evidence for each claim, with a reliable page marker when available or `source_text` verification otherwise; and
5. a brief explanation of why the claim matters for the research question, contribution, limitation, or future work.

Do not compress multiple findings into one vague sentence, replace results with unsupported paraphrase, or repeat the same evidence in a separate evidence table. Evidence belongs inline beneath the claim it supports. Preserve disagreements, null or mixed results, subgroup differences, analytical examples, and author caveats whenever they are present in the source.

## Summary Mode and Source Structure

- `empirical`: use Methodology and Findings when present.
- `review`: summarize scope, organization, synthesis, gaps, and implications; omit absent empirical sections.
- `conceptual` or `theoretical`: summarize concepts, framework, propositions, argument, contribution, and limitations.
- `book` or `book_chapter`: follow the actual book or chapter structure.
- `mixed` or `other`: follow the source headings and explain the chosen structure.

Do not create artificial Method, Participants, Data, or Findings sections for a non-empirical source. Omit non-applicable sections and record the reason in `Citation Notes`.

## Purpose

## Theory & Literature Review

### Section synthesis

Write a developed synthesis of the intellectual context: the main constructs, prior-study pattern, theoretical tension, and the gap that motivates this paper. Include at least three distinct evidence-backed claims when the source provides them.

- Claim: state a substantive literature-review claim.
  - Interpretation: explain how the claim relates to the paper's problem or gap.
  - Evidence: "Direct quotation" (p. N; source_page-verified), or (page unavailable; source-text-verified) when no page marker exists
  - Why it matters: explain its role in the paper's argument.

## Gaps & Research Questions

## Theoretical Framework

## Methodology

### Context

### Participants

### Data Sources

### Procedure

### Analysis Methods

## Findings

For empirical papers, report the major findings/results separately rather than compressing them into one paragraph. Preserve distinctions among themes, comparisons, quantitative results, examples, and analytic patterns. Include at least three distinct evidence-backed findings when the source provides them. For review or conceptual papers, use this heading only when the source has a results/argument section; otherwise omit it and explain the omission in `Citation Notes`.

- Finding/result: state the substantive result.
  - Interpretation: explain what the result shows.
  - Evidence: "Direct quotation" (p. N; source_page-verified), or (page unavailable; source-text-verified) when no page marker exists
  - Why it matters: connect the result to the research question or argument.

## Key Claims

## Discussion

Explain how the authors interpret the findings or argument, what contribution and implications they claim, what caveats shape the interpretation, and how the discussion returns to the stated gap. Include at least three distinct evidence-backed interpretive claims when the source provides them.

- Interpretation: state a substantive discussion claim.
  - Interpretation: explain the authors' reasoning and implication.
  - Evidence: "Direct quotation" (p. N; source_page-verified), or (page unavailable; source-text-verified) when no page marker exists
  - Why it matters: connect the discussion to contribution, limitations, or future work.

## Conclusion

## Unique Contributions

## Limitations

## Future Work

## Relevance to My Study

## Possible Use in Literature Review

## Citation Notes

## Related Synthesis Pages

> The summary builder populates this section with links to the applicable `wiki/overviews/`, `wiki/concepts/`, `wiki/projects/`, and `wiki/questions/` pages. A summarized record must not remain a synthesis orphan.

## Related Links
