---
record_id: paper:2024_Brandt_Educating-Dora-Teaching
stem: 2024_Brandt_Educating-Dora-Teaching
title: 'Educating Dora: Teaching a conversational agent to talk'
authors:
- Brandt, Adam
- Hazel, Spencer
- McKinnon, Rory
- Sideridou, Kleopatra
- Tindale, Joe
- Ventoura, Nikoletta
year: '2024'
type: paper
research_design: empirical
citation_key: brandt2024dora
doi: 10.1177/17504813241267109
url: https://doi.org/10.1177/17504813241267109
metadata_status: open
metadata_authority: publisher_pdf
publication_stage: version_of_record
citation_info:
  source_type: journal
  source_title: Discourse & Communication
  editors: []
  volume: ''
  issue: ''
  pages: ''
  article_number: ''
  publisher: SAGE
tags:
- conversational AI
- conversation analysis
- voice user interfaces
- speech synthesis
- clinical telephone consultation
summary:
  level: deep
  status: summarized
  structure_policy: source_structure
provenance:
  pdf_path: papers\\2024_Brandt_Educating-Dora-Teaching.pdf
  source_path: sources\\2024_Brandt_Educating-Dora-Teaching.md
  parsed_with: docling
  source_hash: 705a55ee9478a56e2ea5d98f791642f7b15f3f1264d00b095e4d3e0bf6b9095a
  metadata_checked_at: ''
  metadata_sources:
  - publisher PDF
  - DOI embedded in publisher PDF
verification:
  summary_verified: true
  quote_verification_status: partial
  quote_verification_pass_rate: 1.0
  claim_verification_pass_rate: 1.0
  requires_human_review: true
  verified_at: '2026-09-08'
related:
  wiki:
  - wiki/2024_Brandt_Educating-Dora-Teaching
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

- Authors: Adam Brandt, Spencer Hazel, Rory McKinnon, Kleopatra Sideridou, Joe Tindale, and Nikoletta Ventoura
- Year: 2024
- DOI: [10.1177/17504813241267109](https://doi.org/10.1177/17504813241267109)
- Venue: *Discourse & Communication*
- Design: Empirical conversation-analytic case study based on anonymized clinical telephone consultations and comparative human-clinician interaction data.

## One-sentence Summary

This paper reports an EMCA-informed collaboration that redesigned the opening of Dora, an automated NHS clinical telephone assistant, by comparing its scripted and synthesized talk with human clinician–patient call openings.

## Keywords

Conversational AI; conversation analysis; voice user interfaces; conversation design; paralinguistics; text-to-speech; clinical telephone consultations.

# Deep Summary

## Purpose

The study examines whether ethnomethodological conversation analysis (EMCA) can inform the design of a conversational agent so that its interactional conduct more closely fits users' prior experience of human telephone consultations. The authors focus on call openings because greeting, identification, reason-for-call, and permission sequences establish the activity and make turn-taking expectations visible.

## Theory & Literature Review

The paper starts from the observation that VUIs are often designed through scripts based on designers' intuitions about how people speak. It argues instead for feeding empirical evidence from equivalent human–human interactions into conversation design. EMCA is presented as useful because it treats talk as systematic social action whose sequential organization is recognizable to participants.

- **Claim 1 — VUI design often begins from imagined naturalness rather than interactional evidence.** The authors state that VUI talk is generated through scripts and that guidance encourages designers to base those scripts on “their imaginings of how humans might speak in that particular context” (page unavailable; source-text-verified). **Interpretation:** the design process can reproduce assumptions about conversation without testing how users actually organize the activity. **Why it matters:** the paper's intervention is to replace intuition-only design with evidence from naturally occurring interaction.
- **Claim 2 — Call openings are structured activity environments.** The paper describes openings as “particular ‘routine ritual[s] of conversational openings’” through which speakers transition into a call (page unavailable; source-text-verified). **Interpretation:** greeting, identification, recognition, and the reason for the call are not interchangeable script fragments but sequential resources. **Why it matters:** a VUI that changes their order or timing can make the user's expected next action unclear.
- **Claim 3 — EMCA provides a method for identifying design-relevant interactional detail.** The authors explain that an EMCA approach examines how interlocutors build social actions and organize them sequentially in ways recognizable to social members (page unavailable; source-text-verified). **Interpretation:** design can be grounded in observable practices rather than a generic ideal of natural language. **Why it matters:** this supplies the theoretical bridge between conversation analysis and product development.

## Methodology

The research formed part of a collaboration between EMCA researchers and Ufonia, the developer of Dora, an automated clinical assistant used for telephone consultations with NHS patients. With ethical approval, the team accessed anonymized recordings in which patients' personal information had been removed. A random selection of approximately 50 calls was transcribed using Jeffersonian conventions adapted for CLAN. A smaller set of calls between patients and human clinicians was also transcribed and analyzed sequentially. The researchers compared the turn formatting, sequence organization, lexical choices, and intonation of Dora's outputs with equivalent clinician–patient interaction, then revised Dora's scripts through text-to-speech manipulation.

## Findings

- **Finding 1 — System latency disrupts the expected summons–greeting sequence.** In the early Dora calls, patients produced a greeting after answering the phone, but Dora's response could be delayed by several seconds. The paper states that “Dora can take up to a few seconds to process a patient utterance, determine an appropriate textual response, and convert that response to talk through TTS” (page unavailable; source-text-verified). **Interpretation:** patients initially treat the delay as a possible interactional problem and repeat their greeting. **Why it matters:** processing latency is experienced not only as a technical property but as a disruption to the sequential organization of the call.
- **Finding 2 — Patients recalibrate their expectations during the call.** After encountering the system's latency, patients allow longer gaps and stop treating later silences as immediate trouble. The authors write that this “suggests that there has already been a recalibration, adjusting his expectancy regarding turn-transition to the speed at which the Dora system works” (page unavailable; source-text-verified). **Interpretation:** users actively adapt their conduct to the system's limitations. **Why it matters:** a system can operate despite interactional mismatch, but the burden of adaptation is shifted to the patient.
- **Finding 3 — Punctuation in the TTS script creates unintended interactional cues.** Commas, full stops, and question marks were converted into pauses and intonation contours that could project a transition or response point. The authors summarize that punctuation “introduces intonation contours and silences into the interface speech production that patients treat as indexing possible transition relevance” (page unavailable; source-text-verified). **Interpretation:** written script conventions become social-action cues when synthesized as speech. **Why it matters:** conversation designers must treat punctuation and prosody as interactional design parameters, not merely text formatting.
- **Finding 4 — The early Dora sequence differed from human clinician practice.** The human clinician data confirmed patient identity before announcing the reason for the call, while the early Dora design announced the call purpose before establishing who was speaking. The paper notes that the human sequence protects confidentiality, whereas the early Dora design “announces the reason for the call before ascertaining the identity of the speaker” (page unavailable; source-text-verified). **Interpretation:** sequence order carries institutional and privacy consequences. **Why it matters:** EMCA comparison exposes risks that would be missed by evaluating only grammatical correctness or task completion.
- **Finding 5 — A revised script produced more interactional flow.** The authors modified Dora's opening to align more closely with clinician data, including its greeting, self-identification, identity confirmation, reason for the call, and permission request. They report that the revised system allowed “greater interactional flow with the patient able to project more easily what response is required and when” (page unavailable; source-text-verified). **Interpretation:** evidence-informed changes to sequence organization and prosody can reduce the user's need to guess how to participate. **Why it matters:** the study demonstrates a concrete pathway from interaction analysis to conversational-agent redesign.

## Discussion & Conclusion

The discussion emphasizes that AI-mediated interaction is not identical to human conversation, but users still monitor and tailor their conduct as if the system were an interactional partner. The design problem is therefore not solved by asking users to adapt indefinitely; systems should be redesigned to reduce avoidable mismatches.

- **Interpretive claim 1 — Users adapt to system limitations, but adaptation is not evidence of successful design.** The authors argue that users “engage with the system as they would in a human-human interaction, but that there is already a preparedness to adapt when the design of the system diverges” from natural interaction (page unavailable; source-text-verified). **Interpretation:** apparent task completion can conceal extra interactional work by users. **Why it matters:** evaluation should include who bears the cost of mismatch.
- **Interpretive claim 2 — EMCA-informed design can move VUIs closer to users' interactional expectations.** The paper argues that human–human data, EMCA analysis, TTS manipulation, and SSML can help VUIs “more closely simulate talk produced by humans” (page unavailable; source-text-verified). **Interpretation:** the goal is not generic human imitation but context-sensitive alignment with recognizable activity patterns. **Why it matters:** this provides a practical design methodology for voice systems.
- **Interpretive claim 3 — The desirability of human-like design depends on the setting.** The authors qualify their proposal by noting that “the extent to which this is desirable may depend on the type of VUI and the interactional setting” (page unavailable; source-text-verified). **Interpretation:** naturalness is not an unconditional design objective; institutional purpose, privacy, safety, and user expectations also matter. **Why it matters:** the paper supports situated design rather than a universal conversational-agent template.

## Unique Contributions

- Demonstrates an empirical EMCA-informed conversation-design workflow rather than only proposing that conversation analysis might be useful.
- Connects sequential organization, latency, punctuation, intonation, and TTS behavior to concrete user experience in clinical telephone consultations.
- Shows how comparison with human clinician calls can identify both interactional-flow and confidentiality problems in an automated assistant.

## Limitations

The paper analyzes a focused set of call openings within one clinical assistant and one institutional setting. The parsed source reports approximately 50 transcribed Dora calls and a smaller comparative set of human clinician calls, but it does not provide a general population-level evaluation of all users or all VUI contexts. Because page markers were not preserved reliably in the parsed Markdown, quotation verification is source-text based and requires manual page review.

## Future Work

The demonstrated workflow supports further testing of revised scripts across broader call types, users, clinical activities, and interactional settings. Future work should examine whether improved sequence organization reduces user repair and adaptation, while also evaluating privacy, accessibility, safety, and the institutional consequences of automated clinical talk.

## Relevance to My Study

This paper provides a direct model for analyzing interactional agency in conversational AI: system timing, prosody, and sequence design distribute the work of maintaining interaction between the agent and the user. It is especially relevant to research on turn design, repair, accessibility, and human–AI complementarity.

## Possible Use in Literature Review

Use it to support the claim that conversational-agent quality cannot be assessed only through task accuracy or language-model output. Interactional timing, sequence organization, prosody, privacy-sensitive ordering, and the user's repair burden must also be examined.

## Citation Notes

The canonical source was parsed with Docling. The PDF's embedded DOI is `10.1177/17504813241267109`; the parsed source did not preserve reliable page markers, so evidence is marked `source-text-verified` and requires manual page review.

## Related Synthesis Pages

- [[../wiki/overviews/conversational-ai-and-interaction|Conversational AI and Human Interaction]]
- [[../wiki/concepts/interactional-agency-and-turn-design|Interactional Agency and Turn Design]]
- [[../wiki/projects/ai-mediated-language-and-care-interaction|AI-Mediated Language and Care Interaction]]
- [[../wiki/questions/how-should-ai-support-human-interaction|How Should AI Support Human Interaction?]]

## Related Links

- Source: [[../sources/2024_Brandt_Educating-Dora-Teaching|parsed source]]
- Wiki: [[../wiki/2024_Brandt_Educating-Dora-Teaching|synthesis node]]
