---
record_id: paper:2023_Brandt-Hazel-Mckinnon_From-Writing-Dialogue
stem: 2023_Brandt-Hazel-Mckinnon_From-Writing-Dialogue
title: 'From Writing Dialogue to Designing Conversation: Considering the potential
  of Conversation Analysis for Voice User Interfaces'
authors:
- Adam Brandt
- Spencer Hazel
- Rory Mckinnon
- Kleopatra Sideridou
- Joe Tindale
- Nikoletta Ventoura
year: '2023'
type: paper
research_design: Provocation/conceptual conference paper using Conversation Analysis
  and an illustrative healthcare call-opening example to propose a design approach
  for Voice User Interfaces.
citation_key: brandt-2023-writing-dialogue
doi: 10.1145/3571884.3603758
url: 10.1145/3571884.3603758
metadata_status: open
metadata_authority: publisher_pdf
publication_stage: ''
citation_info:
  source_type: conference paper
  source_title: ACM conference on Conversational User Interfaces (CUI '23)
  editors: []
  volume: ''
  issue: ''
  pages: 6 pages
  article_number: ''
  publisher: ACM, New York, NY, USA
tags:
- conversation design
- voice user interfaces
- social interaction
- conversation analysis
provenance:
  pdf_path: papers\2023_Brandt-Hazel-Mckinnon_From-Writing-Dialogue.pdf
  source_path: sources\2023_Brandt-Hazel-Mckinnon_From-Writing-Dialogue.md
  parsed_with: docling
  source_hash: 728b8ac47cf689f085f05c35106d3a70f40c12cf6d7428796e43ead731a674e6
  metadata_checked_at: ''
  metadata_sources: []
verification:
  summary_verified: false
  quote_verification_status: partial
  quote_verification_pass_rate: 1.0
  claim_verification_pass_rate: 1.0
  requires_human_review: true
  verified_at: ''
summary:
  level: deep
  status: summarized
  structure_policy: source_structure
related:
  wiki:
  - wiki/2023_Brandt-Hazel-Mckinnon_From-Writing-Dialogue
  overviews:
  - wiki/overviews/conversational-ai-and-interaction
  concepts:
  - wiki/concepts/interactional-agency-and-turn-design
  projects:
  - wiki/projects/ai-mediated-language-and-care-interaction
  questions:
  - wiki/questions/how-should-ai-support-human-interaction
  supersedes: []
  superseded_by: []
---
# Quick Card

## Bibliographic Metadata

- Authors: Adam Brandt; Spencer Hazel; Rory Mckinnon; Kleopatra Sideridou; Joe Tindale; Nikoletta Ventoura
- Year: 2023
- Design: Provocation/conceptual conference paper using Conversation Analysis and an illustrative healthcare call-opening example to propose a design approach for Voice User Interfaces.

## One-sentence Summary

The paper argues that conversation designers should move from writing dialogue scripts toward designing turns-at-talk informed by Conversation Analysis and context-specific human-human interaction data.

## Keywords

conversation design; voice user interfaces; social interaction; conversation analysis

# Structured Summary

## Purpose

To argue that VUI conversation design should begin from natural spoken interaction data, preferably from the same interactional context where the VUI will be deployed.

## Findings

Equivalent human-human interaction data can be a rich resource for conversation design. Punctuation in a written script can add pauses absent from the human source turn. SSML is presented as a way to approximate human turn design more closely.

## Discussion & Conclusion

Naturalistic CUI design requires knowledge of how social interaction is produced, organized, and managed in the target setting. The proposed CA-informed design process is slower but justified by its expected benefits. VUI design should invoke the interactional norms users expect in the specific institutional context.

# Deep Summary

## Research Problem and Purpose

To argue that VUI conversation design should begin from natural spoken interaction data, preferably from the same interactional context where the VUI will be deployed.

## Theory & Literature Review

The paper reviews the immaturity of VUI design guidance, the limits of script-based naturalness, and the value of CA as a naturalistic method for studying actual interactional practices rather than imagined dialogue.

- Claim: VUI design guidance remains underdeveloped even though naturalness is a central aspiration.
  - Interpretation: The authors position current design guidance as insufficient for reliably producing natural spoken interaction.
  - Evidence: "Guidance and principles to underpin the design and development of Voice User Interfaces (VUIs) remain in infancy [6, 19-21]." (page unavailable; source-text-verified)
  - Why it matters: This establishes the design problem that CA is proposed to address.

- Claim: Conversation designers currently face the problem of making written text sound like realistic speech after synthesis.
  - Interpretation: The paper locates a core shortcoming in the separation between scriptwriting and speech production.
  - Evidence: "So conversation designers are tasked with the challenge of producing written text which then sound realistic, or at least plausible, when converted into spoken output by the speech synthesiser." (page unavailable; source-text-verified)
  - Why it matters: This explains why written dialogue conventions can distort spoken VUI output.

- Claim: CA is presented as a method based on naturally occurring recordings rather than hypothetical or elicited accounts.
  - Interpretation: The authors treat CA as a strong alternative to intuition because it examines real interactional conduct.
  - Evidence: "What sets CA apart from other approaches is its avoidance of hypothetical dialogue analysis or a reliance on elicited accounts of how people think interaction works." (page unavailable; source-text-verified)
  - Why it matters: This justifies using CA evidence as a design input for VUI turns.

## Findings

The illustrative analysis shows how equivalent clinical call data can inform VUI turn design and how ordinary script punctuation can introduce pauses and intonation patterns that diverge from the human clinician's talk, while SSML can produce a closer approximation.

- Claim: Equivalent human-human interaction data can be a rich resource for conversation design.
  - Interpretation: The authors argue that recordings from comparable settings provide concrete models for interactional structure and turn formatting.
  - Evidence: "Having access to such equivalent human-human interactions and being able to generate recorded data from those settings can make for a rich resource for the conversation design process [10]." (page unavailable; source-text-verified)
  - Why it matters: This moves VUI design from general naturalness principles to situated empirical materials.

- Claim: Punctuation in a written script can add pauses absent from the human source turn.
  - Interpretation: The example demonstrates that lexical equivalence does not guarantee interactional or prosodic equivalence after TTS.
  - Evidence: "Although the agent's words are produced in exactly the same order as the clinician, the punctuation marking in the script introduces elements into the speech (namely pauses) that are not present in the human turn." (page unavailable; source-text-verified)
  - Why it matters: This is the concrete design failure that motivates CA-informed transcoding.

- Claim: SSML is presented as a way to approximate human turn design more closely.
  - Interpretation: The authors use SSML to manipulate speech output toward the prosodic and timing pattern of the human clinician.
  - Evidence: "We now have a VUI turn-at-talk which much more closely replicates that of a human equivalent." (page unavailable; source-text-verified)
  - Why it matters: This gives conversation designers a practical route from CA evidence to implementable VUI output.

## Discussion

The paper concludes that designers need deeper, context-specific knowledge of interactional practices, that CA-informed work is worth the additional preparation time, and that VUIs should be fitted to institutional norms rather than generic assumptions about conversation.

- Claim: Naturalistic CUI design requires knowledge of how social interaction is produced, organized, and managed in the target setting.
  - Interpretation: The authors reject generic intuition as an adequate basis for designing naturalistic agent turns.
  - Evidence: "However, where a conversation designer does want some semblance of naturalism evoked in the CUI, knowledge of how social interaction works, how it is produced, organized and managed, in general and in that particular setting, will be crucial." (page unavailable; source-text-verified)
  - Why it matters: This sets the epistemic standard for conversation design work.

- Claim: The proposed CA-informed design process is slower but justified by its expected benefits.
  - Interpretation: The paper acknowledges implementation cost while arguing that better interactional fit outweighs the limitation.
  - Evidence: "While this proposed approach is more time-consuming in the preparatory change of conversation design process, the benefits would vastly outweigh any limits." (page unavailable; source-text-verified)
  - Why it matters: This frames the approach as a practical tradeoff rather than a frictionless method.

- Claim: VUI design should invoke the interactional norms users expect in the specific institutional context.
  - Interpretation: The argument is that interactional effectiveness depends on setting-specific normative patterns, not on a universal script style.
  - Evidence: "The most effective way to do this is to invoke the norms of interaction that the user will be expecting." (page unavailable; source-text-verified)
  - Why it matters: This has direct implications for designing healthcare, customer service, sales, counseling, and other domain-specific voice agents.

## Unique Contributions

The paper reframes VUI work from writing scripts to designing turns-at-talk and shows how CA-informed analysis of equivalent human-human interaction can guide lexical, prosodic, sequential, and SSML design choices.

## Limitations

The sanitized source has no reliable page markers. The paper is a provocation/conceptual argument with an illustrative example rather than an empirical evaluation of user outcomes, and it notes that the proposed approach is more time-consuming and context-specific.

## Relevance to My Study

Relevant for conversation design, voice-user-interface design, SSML/TTS output formatting, naturalistic interaction design, and applying Conversation Analysis to human-computer interaction.

## Future Work

The paper implies further collaboration between conversation designers and CA practitioners to identify context-specific interactional norms and determine which features of natural human-human talk should or should not be emulated in VUIs.

## Possible Use in Literature Review

The paper draws on conversation design guidance, VUI designer studies, CUI research, natural conversation frameworks, institutional interaction studies, and Conversation Analysis to argue for context-fitted turn design.

## Citation Notes

All claims below are grounded in exact quotations from the sanitized Markdown generated by scripts/prepare_summary_input.py. No reliable page markers were available in the sanitized source, so every claim uses verification source_text and page null.

Every substantive claim above is linked to an exact quotation checked against the parsed source. `source_page` denotes a parsed-source page marker; `source_text` denotes an exact source-text match where no reliable page locator was available. PDF re-reading is not part of summary verification; page-level checking is left for manual review.

## Related Synthesis Pages

- [[../wiki/overviews/conversational-ai-and-interaction|Conversational AI and Human Interaction]]
- [[../wiki/concepts/interactional-agency-and-turn-design|Interactional Agency and Turn Design]]
- [[../wiki/projects/ai-mediated-language-and-care-interaction|AI-Mediated Language and Care Interaction]]
- [[../wiki/questions/how-should-ai-support-human-interaction|How Should AI Support Human Interaction?]]

## Related Links

- Source: [[../sources/2023_Brandt-Hazel-Mckinnon_From-Writing-Dialogue|parsed source]]
- Wiki: [[../wiki/2023_Brandt-Hazel-Mckinnon_From-Writing-Dialogue|synthesis node]]
