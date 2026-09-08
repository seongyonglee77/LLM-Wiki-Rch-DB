---
record_id: paper:2024_Addlesee-Eshghi_You-Have-Interrupted
stem: 2024_Addlesee-Eshghi_You-Have-Interrupted
title: 'You have interrupted me again! : making voice assistants more dementia friendly
  with incremental clarification'
authors:
- Angus Addlesee
- Arash Eshghi
year: '2024'
type: paper
research_design: Corpus construction and computational evaluation of interruption
  recovery pipelines and LLM-generated incremental clarification requests.
citation_key: addlesee-2024-interrupted
doi: 10.3389/frdem.2024.1343052
url: 10.3389/frdem.2024.1343052
metadata_status: open
metadata_authority: publisher_pdf
publication_stage: ''
citation_info:
  source_type: journal article
  source_title: Front. Dement.
  editors: []
  volume: '3'
  issue: ''
  pages: '1343052'
  article_number: ''
  publisher: ''
tags:
- dementia
- voice assistant
- accessibiity
- artificial intellegence
- conversational AI
provenance:
  pdf_path: papers\2024_Addlesee-Eshghi_You-Have-Interrupted.pdf
  source_path: sources\2024_Addlesee-Eshghi_You-Have-Interrupted.md
  parsed_with: docling
  source_hash: ad3723998e016b609acb7667f3c9f8c8535cac517621688c140e56dcefad4f49
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
  - wiki/2024_Addlesee-Eshghi_You-Have-Interrupted
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

- Authors: Angus Addlesee; Arash Eshghi
- Year: 2024
- Design: Corpus construction and computational evaluation of interruption recovery pipelines and LLM-generated incremental clarification requests.

## One-sentence Summary

The article argues that clarification-based interruption recovery can preserve downstream task performance and that larger LLMs, when prompted with examples, can generate and interpret incremental clarification exchanges in ways that could make voice assistants more accessible for people with dementia.

## Keywords

dementia; voice assistant; accessibiity; artificial intellegence; conversational AI

# Structured Summary

## Purpose

To evaluate whether incremental clarification requests can help everyday voice assistants recover from interrupted or paused utterances, with a particular accessibility motivation for people with dementia.

## Findings

Prediction-based recovery performs worse than interactive recovery because predicted completions often amount to arbitrary guesses. The interactive QA pipeline nearly preserves complete-question performance. The best AMR interruption recovery pipeline loses only a small amount of semantic graph similarity. SLUICE-CR contributes 3,000 human-produced clarification requests tied to interrupted questions. The strongest iCR generation results are concentrated in larger models exposed to examples from SLUICE-CR.

## Discussion & Conclusion

The combined experiments indicate that several strong LLMs can treat clarification exchanges similarly to uninterrupted turns. The authors argue that EVAs should be adapted to natural user speech rather than training users to suppress natural speech phenomena. The paper explicitly limits the present contribution because it must be implemented in a full EVA and validated with users. Privacy concerns prevent using GPT-4 in the planned hospital deployment, motivating on-premise LLM use.

# Deep Summary

## Research Problem and Purpose

To evaluate whether incremental clarification requests can help everyday voice assistants recover from interrupted or paused utterances, with a particular accessibility motivation for people with dementia.

## Theory & Literature Review

The literature review frames voice assistants as potentially autonomy-enhancing tools whose accessibility failures are partly caused by assumptions about fluent, average-user speech. It connects dementia-related pausing and disfluency to theories of incremental language processing and clarification requests, then argues that current systems should adapt to natural speech phenomena rather than requiring users to speak in system-friendly ways.

- Claim: Existing dementia-friendly EVA work demonstrates value for users and caregivers, but it leaves the underlying speech-processing problem largely unresolved.
  - Interpretation: The authors distinguish between application-level dementia-friendly features and deeper interactional robustness. Their target is not another skill or reminder function but the speech-understanding layer that mishandles natural pauses.
  - Evidence: "As illustrated, there is an abundance of work to create EVAs that have dementia-friendly features and show that they can be used to benefit both PwDs and their caregivers. This work is both important and commendable, but a gap remains, as they all use offthe-shelf speech processing ." (page unavailable; source-text-verified)
  - Why it matters: This justifies the article's focus on interruption recovery as an accessibility problem rather than a convenience feature.

- Claim: The paper grounds its approach in the idea that human language comprehension and production are incremental.
  - Interpretation: Because speakers and listeners process partial utterances as they unfold, a voice assistant that waits only for complete clean turns will miss a central property of everyday talk.
  - Evidence: "Spoken language unfolds over time. People process each token as it is uttered, maintaining a partial representation of what has been said (Marslen-Wilson, 1973; Madureira and Schlangen, 2020a; Kahardipraja et al., 2021)." (page unavailable; source-text-verified)
  - Why it matters: Incrementality supplies the theoretical basis for treating mid-sentence clarification as natural interaction rather than system error handling.

- Claim: Mid-utterance pauses are especially consequential for people with dementia because current EVAs often treat short silences as turn completion.
  - Interpretation: The accessibility problem arises when a normal or dementia-associated speech pattern is interpreted by the system as a signal that the user has finished speaking.
  - Evidence: "When interacting with voice assistants, however, this short silence often triggers end-of-turn detection-interrupting and frustrating the user (Nakano et al., 2007; Jiang et al., 2013; Panfili et al., 2021; Liang et al., 2022)." (page unavailable; source-text-verified)
  - Why it matters: This connects the technical problem of endpointing and dialogue management to user frustration and repeated utterance burden.

- Claim: Incremental clarification requests are defined as mid-sentence, split-utterance continuations that ask how the speaker would have completed a truncated turn.
  - Interpretation: The target phenomenon is narrower than clarification in general: iCRs are syntactically tied to the interrupted utterance and probe the missing continuation.
  - Evidence: "Throughout this article, we focus on incremental surface CRs (henceforth iCRs; Healey et al., 2011; Howes and Eshghi, 2021): those that (1) occur mid-sentence; (2) are constructed as a split utterance (Purver et al., 2009), that is, a continuation or completion of the truncated sentence; and (3) are intended to elicit how the speaker would have gone on to complete their partial turn [see Figures 2A-C, which does not satisfy (2)]." (page unavailable; source-text-verified)
  - Why it matters: This definition shapes the corpus annotation, model-evaluation criteria, and claim that iCRs test incremental processing in LLMs.

## Findings

The findings show that interactive recovery pipelines outperform prediction-based recovery, that SLUICE-CR provides a human reference corpus for iCR generation, and that larger LLMs perform best when prompted with corpus examples. The paper reports strong preservation of QA and AMR performance under interactive recovery and strong GPT-4 performance on generation and clarification-exchange interpretation.

- Claim: Prediction-based recovery performs worse than interactive recovery because predicted completions often amount to arbitrary guesses.
  - Interpretation: Completing a partial utterance without user input can sound plausible but still recover the wrong missing content.
  - Evidence: "The two T5 prediction models perform poorly compared to the interactive approach, with the model fine-tuned on SLUICE outperforming the SQuAD v1.1 model. From a manual inspection, this poor performance is caused by arbitrary guesses (e.g., completing 'Who wrote')." (page unavailable; source-text-verified)
  - Why it matters: This supports the design choice to ask a clarification request rather than silently guessing what the user intended.

- Claim: The interactive QA pipeline nearly preserves complete-question performance.
  - Interpretation: The system can recover the missing information through interaction while losing less than one percentage point relative to a baseline that receives the full question.
  - Evidence: "The interactive pipeline is the best of our IRPs-answering only 0.77% fewer questions correctly than the baseline given complete questions." (page unavailable; source-text-verified)
  - Why it matters: This is the central evidence that clarification-based recovery can maintain downstream utility rather than merely improve conversational naturalness.

- Claim: The best AMR interruption recovery pipeline loses only a small amount of semantic graph similarity.
  - Interpretation: Interactive recovery generalizes beyond QA into broader sentence-level semantic parsing, though it still involves measurable loss.
  - Evidence: "Looking at only the Smatch Loss, the 'Split' pipeline performed the best, only losing 1.6% graph similarity f-score." (page unavailable; source-text-verified)
  - Why it matters: This broadens the result from a task-specific KBQA pipeline to a more general account of recovering disrupted sentences.

- Claim: SLUICE-CR contributes 3,000 human-produced clarification requests tied to interrupted questions.
  - Interpretation: The corpus gives the authors a human reference set for evaluating whether LLM outputs resemble natural iCRs.
  - Evidence: "SLUICE-CRcontains 250 interrupted questions, each paired with 12 CRs elicited from AMT annotators, yielding a total of 3, 000 CRs." (page unavailable; source-text-verified)
  - Why it matters: This corpus contribution is necessary for both the model-generation experiments and future work on interruption recovery.

- Claim: The strongest iCR generation results are concentrated in larger models exposed to examples from SLUICE-CR.
  - Interpretation: The paper does not claim that all LLMs naturally produce useful iCRs; performance depends on model capacity and prompt context.
  - Evidence: "Table 6 is broadly consistent with the standard metrics reported in Table 5: GPT-4, Llama-70-b-chat, and Vicuna-13b-v1.5 were the leading models in generating appropriate CRs when given only a few examples from SLUICE-CR in the Annotation and Reasoning prompt conditions." (page unavailable; source-text-verified)
  - Why it matters: This qualifies the technological optimism and identifies prompting with human examples as an important condition for success.

## Discussion

The discussion translates the technical results back into accessibility implications. It argues that clarification requests can reduce the need for full repetition, but also stresses that the contribution must be embedded in a full EVA, tested with people with dementia, and deployed under strict privacy and safety constraints.

- Claim: The combined experiments indicate that several strong LLMs can treat clarification exchanges similarly to uninterrupted turns.
  - Interpretation: The paper's end-to-end argument depends on both generating an iCR and interpreting the user's completion afterward.
  - Evidence: "Finally, we combined all this work to show that GPT-4, Llama-2-70b-chat, and Vicuna-13b-v1.5 can interpret clarification exchanges as if they were simply one uninterrupted turn." (page unavailable; source-text-verified)
  - Why it matters: This shows how the recovery strategy could become a practical dialogue-system behavior rather than a standalone corpus task.

- Claim: The authors argue that EVAs should be adapted to natural user speech rather than training users to suppress natural speech phenomena.
  - Interpretation: The accessibility stance is system-centered: conversational technology should change to fit vulnerable users' interaction patterns.
  - Evidence: "Instead of teaching people to adapt their speech to EVAs (O'Connor et al., 2023), EVAs should be adapted to understand natural speech phenomena." (page unavailable; source-text-verified)
  - Why it matters: This makes the work relevant to inclusive design and not only to model benchmarking.

- Claim: The paper explicitly limits the present contribution because it must be implemented in a full EVA and validated with users.
  - Interpretation: The experiments demonstrate feasibility, but they do not yet prove real-world accessibility benefit in deployed dementia-care contexts.
  - Evidence: "The work in this article has one major limitation: it is not practically useful in isolation. It must, therefore, be implemented within a full EVA to improve EVA accessibility. In order to determine whether this work improves accessibility in practice, a user study must be carried out." (page unavailable; source-text-verified)
  - Why it matters: This is the main boundary on how strongly the paper can be cited for practical impact.

- Claim: Privacy concerns prevent using GPT-4 in the planned hospital deployment, motivating on-premise LLM use.
  - Interpretation: The best-performing model in experiments is not automatically the deployable model in healthcare settings.
  - Evidence: "Unfortunately, there is no way to use GPT-4 without sending data to OpenAI's servers. As our planned deployment is in a hospital, we cannot do this due to data privacy concerns." (page unavailable; source-text-verified)
  - Why it matters: This is an important implementation constraint for dementia and hospital contexts where users may disclose personal information.

## Unique Contributions

- Establishes interactive clarification requests as an effective interruption recovery strategy using QA and AMR-based recovery pipelines.
- Creates and analyzes SLUICE-CR, a corpus of 3,000 crowdsourced human incremental clarification requests for interrupted questions.
- Evaluates several LLMs under different prompting conditions for generating iCRs and processing clarification exchanges.

## Limitations

The authors state that the work is not practically useful by itself and must be embedded in a full everyday voice assistant, evaluated through user studies with people with dementia, and adapted to privacy-sensitive deployment constraints because GPT-4 cannot be used in their planned hospital setting without sending data to OpenAI servers.

## Relevance to My Study

This paper is relevant to dementia-friendly conversational AI because it links a common interactional problem, mid-utterance pausing, to a concrete recovery strategy and evaluates that strategy across semantic parsing, corpus collection, LLM generation, and clarification-exchange interpretation.

## Future Work

The authors plan to deploy the integrated system in a hospital memory clinic with real patients, conduct end-to-end user studies with people with dementia, use an on-premise LLM for privacy-sensitive settings, and encourage broader work adapting speech processing to other user groups and natural speech phenomena.

## Possible Use in Literature Review

The paper uses prior work on disability and voice-assistant accessibility, dementia-related speech phenomena, incremental language processing, clarification requests, semantic formalisms such as AMR/RDF/SPARQL, and LLM prompting/evaluation to motivate and structure its experiments.

## Citation Notes

The source citation and DOI are present in the sanitized source. The parsed source contains no reliable page markers, so all quote evidence uses source_text verification with page set to null.

Every substantive claim above is linked to an exact quotation checked against the parsed source. `source_page` denotes a parsed-source page marker; `source_text` denotes an exact source-text match where no reliable page locator was available. PDF re-reading is not part of summary verification; page-level checking is left for manual review.

## Related Synthesis Pages

- [[../wiki/overviews/conversational-ai-and-interaction|Conversational AI and Human Interaction]]
- [[../wiki/concepts/interactional-agency-and-turn-design|Interactional Agency and Turn Design]]
- [[../wiki/projects/ai-mediated-language-and-care-interaction|AI-Mediated Language and Care Interaction]]
- [[../wiki/questions/how-should-ai-support-human-interaction|How Should AI Support Human Interaction?]]

## Related Links

- Source: [[../sources/2024_Addlesee-Eshghi_You-Have-Interrupted|parsed source]]
- Wiki: [[../wiki/2024_Addlesee-Eshghi_You-Have-Interrupted|synthesis node]]
