---
stem: 2023_Brandt-Hazel-Mckinnon_From-Writing-Dialogue
pdf_path: papers\2023_Brandt-Hazel-Mckinnon_From-Writing-Dialogue.pdf
source_path: sources\2023_Brandt-Hazel-Mckinnon_From-Writing-Dialogue.md
source_hash: 728b8ac47cf689f085f05c35106d3a70f40c12cf6d7428796e43ead731a674e6
parsed_with: docling
parsed_at: '2026-09-07T14:31:17+00:00'
warnings: []
record_id: paper:2023_Brandt-Hazel-Mckinnon_From-Writing-Dialogue
---
## From Writing Dialogue to Designing Conversation: Considering the potential of Conversation Analysis for Voice User Interfaces

Adam Brandt Newcastle University adam.brandt@newcastle.ac.uk Spencer Hazel Newcastle University spencer.hazel@newcastle.ac.uk

Kleopatra Sideridou Newcastle University k.sideridou2@newcastle.ac.uk

## ABSTRACT

Conversation design at least partly aspires to create Voice User Interfaces which emulate human speech production. And yet, there is no established approach for the development of naturalistic conversational infrastructure for VUIs; conversation designers are advised to work from their common sense understanding of conversation, producing written scripts, based on memory and imagination, which are later converted into speech. This is a shortcoming in conversation design which needs to be addressed. In this provocation paper, we argue that the starting point in the development of any VUI should be the examination of natural spoken conversation, preferably from the same interactional context in which the VUI will be deployed. We provide a short example to illustrate how the current process of conversation scriptwriting can be a barrier to this, and demonstrate how this can be overcome using the social scientific approach of Conversation Analysis (CA).

## CCS CONCEPTS

· Computing methodologies → Artificial intelligence; Natural language processing; Discourse, dialogue and pragmatics; · Human-centered computing → Interaction design; Interaction design, theory, concepts and paradigms.

## KEYWORDS

Conversation design, Voice user interfaces, Social interaction, Conversation Analysis

## ACMReference Format:

Adam Brandt, Spencer Hazel, Rory Mckinnon, Kleopatra Sideridou, Joe Tindale, and Nikoletta Ventoura. 2023. From Writing Dialogue to Designing Conversation: Considering the potential of Conversation Analysis for Voice User Interfaces. In ACM conference on Conversational User Interfaces (CUI '23), July 19-21, 2023, Eindhoven, Netherlands. ACM, New York, NY, USA, 6 pages. https://doi.org/10.1145/3571884.3603758

Permission to make digital or hard copies of part or all of this work for personal or classroom use is granted without fee provided that copies are not made or distributed for profit or commercial advantage and that copies bear this notice and the full citation on the first page. Copyrights for third-party components of this work must be honored. For all other uses, contact the owner/author(s).

CUI '23, July 19-21, 2023, Eindhoven, Netherlands

ACM ISBN 979-8-4007-0014-9/23/07.

© 2023 Copyright held by the owner/author(s).

[https://doi.org/10.1145/3571884.3603758](https://doi.org/10.1145/3571884.3603758)

Joe Tindale Ufonia Limited

jt@ufonia.com

## 1 INTRODUCTION

Guidance and principles to underpin the design and development of Voice User Interfaces (VUIs) remain in infancy [6, 19-21]. Among what support is available, aspirations of 'naturalness' are central, often with a stated aim to emulate language as it is produced by humans, for humans, in everyday conversation. Conversation designers themselves report the use of language as it is spoken (as opposed to as it is written) and the use of appropriate prosody (such as intonations, pauses and stress) as among the most important characteristics of 'naturalness' [14]. Similarly, prevalent conversation design guides promise to provide support in 'creating a natural sounding conversation' [1] or 'craft[ing] conversations that are natural and intuitive for users' [2].

In essence, this issue is due to a current shortcoming of VUI design: the disconnection between the dialogue generator and the speech synthesiser, which needs to be improved. The root for this problem is arguably the fact that traditionally, and currently, Language Models are trained primarily on text data. So conversation designers are tasked with the challenge of producing written text which then sound realistic, or at least plausible, when converted into spoken output by the speech synthesiser.

However, conversation designers report 'making interaction which is natural' among their major challenges [23]. Reasons cited for this include the limitations of synthesized voice technology for aspects of speech (like prosody and non-lexical vocalisations), difficulties in writing scripts for spoken language during the conversation design process, and the lack of sufficient guidance or resources to help with this [14].

Despite the reported importance of, and difficulty in, emulating natural spoken language, there does not appear to be a fixed approach for the development of naturalistic conversational infrastructure for VUIs, with conversation designers recommended to write scripts based on their common sense understanding of conversation. Among over 100 VUI designers surveyed [23], none reported examining natural conversation at the design stage. Instead, common practices included checking similar existing VUIs, accessing online resources, and discussing with colleagues.

Since as early as the 1990s, there have been calls for speech interface designers to look to natural human conversation for inspiration [3]. Such calls have increased in the last few years, with a number of very recent collaborative explorations involving researchers of spoken conversation and conversation design practitioners [22, 24, 28]. This provocation paper comes from another such collaboration -

Rory Mckinnon Ufonia Limited

rm@ufonia.com

Nikoletta Ventoura Ufonia Limited

nv@ufonia.com bringing together AI Conversation Engineers and Software Engineers, and Conversation Analysts - and builds on such work.

As others have argued [33], we believe conversation design should be informed by the examination of natural human-human interactions. And in this provocation paper, we argue that the starting point in the development of any VUI should be the examination of natural spoken conversation, preferably from the same interactional context. Further, rather than conceiving of the process of conversation design as 'writ[ing] dialogs' [1], 'scripts', or 'prompts', conversation design work should be conceptualised as the design of talk-in-interaction, and approached accordingly. We provide an example, taken from a healthcare clinical consultation context, to illustrate.

## 2 CONVERSATION ANALYSIS - A NATURAL OBSERVATIONAL APPROACH TO THE STUDY OF SOCIAL INTERACTION

The last 50 years has seen Conversion Analysis (CA) emerge as the go-to social scientific approach for understanding and explicating what people do in their interactions with one another. What sets CA apart from other approaches is its avoidance of hypothetical dialogue analysis or a reliance on elicited accounts of how people think interaction works. Rather, Conversation Analysts work exclusively on recordings of naturally-occurring interaction (i.e. those happening regardless of the research activity), and as such align more closely with natural observational sciences that study subjects in their natural environments.

When we examine naturally-occurring interactional data, we immediately see that there are levels of formatting in how people design their contributions that are intricate, complex and often ingrained to such a degree that they are almost impossible to articulate, or even imagine. These may include features that at first glance appear inconsequential, minor details amongst the more important elements of content and speech. They may be excluded from our recollections or imaginings of interactional events, or replaced by false assumptions. For example, a common assumption is that a question is formatted with turn-final rising intonation, while a non-question statement has falling turn-final intonation. On closer empirical observation, however, we can see that this is not always the case. This is demonstrated in the below examples of questions transcribed from recordings of real doctor-patient telephone consultations (diagonal arrows indicate intonation contours, and vertical arrow indicate shifts in pitch):

```
DOC: okay and have you had any flashing lights or floaters ↘ --- DOC: has that settled though ↘ = it's not ↗ (0.2) it's not kind of consta:nt ↘ Likewise, we find non-question utterances formatted with turnfinal rising intonation: DOC: it's ↓ doctor grey calling from the trentwood u:h cataract clinic ---
```

```
DOC: I think we can do that
```

Data such as these demonstrate the danger of relying on common understandings for how particular social actions are formatted, as they do not always match up with reality. For a conversation designer, it is then important to understand when these turn-formats in intonation are mobilised by speakers, and how they are understood by recipients.

Aside from the intricate formatting of individual turns-at-talk, an equally important focus of CA is how these are sequentially organised in relation to one another. A turn-at-talk is constructed to 'fit' what precedes it and what possible types of turn are required in response. Such sequential organisational formatting also involves issues of timing, for example what a delay in response can signify, or what an early onset of a response. These considerations are also essential for conversation designers, who may need to design their conversational agent's talk in ways that 'nudge' a human interlocutor to respond in a certain way.

Understanding such phenomena is the aim of CA, primarily concerned with uncovering the particular recognisable patterns of conduct that members orient to in how they design their contributions, and how these are treated by their co-participants. Even at the level of speech alone, there is an extensive set of resources that CA has been interested in unpacking. These include such patterns as variations in the syntactic organization, or pitch and intonation contouring, timing of onset and of completion of a turn, intra- and inter-turn pauses, non-lexical vocalizations, voice timbre, volume and speed. Moreover, these constitute strands of communicative resources that are woven together to produce not only the complexity evidenced in a single turn at talk, but also additional levels of meaning. As Sacks [30] argues, 'the detailed study of small phenomena may give an enormous understanding of the ways humans do things and the kinds of objects they use to construct and order their affairs' (p24). These objects are the building blocks through which we construct our talk and through which we perceive meaning in that of others. For the conversation designer, they can also be the building blocks for constructing the prompts for any VUI system.

To summarise, although CA research has not been concerned with the content of talk, nor any intention behind talk, it has been instrumental in unpacking the 'how' of talk-in-interaction. With conversation designers building their products by mobilising the interactional architecture of talk-in-interaction, it would appear prescient for us to explore how CA research can feed into the design process, and ultimately the products.

## 3 CA AND VOICE USER INTERFACES

As noted above, there have been increasing calls for CUI research and practice to be informed by other academic disciplines. CA, which traverses sociology and linguistics, is particularly equipped to address what are seen to be the major needs of CUI research and design: (1) to help understand differences between human-human and CUI interactions/dialogue, and (2) to 'provide a set of methods that can be tailored towards CUI relevant contexts' [7, p2].

There is a growing body of CA studies which contribute to our understanding of how humans interact with various kinds of VUIs: voice assistants, such as Alexa [3, 9, 27, 29]; call centre conversational agents [5], and social robots [25, 26, 34]. Moore et al [18] suggest that such research provides valuable insights, but such insights come too late to be helpful in the design and development process. However, they argue, general findings from CA can also be used as a framework to lead design. The IBM Natural Conversation Framework [16, 17] provides just this, offering designers the resource of 'generic, reusable interaction patterns adapted from the Conversation Analysis literature' [19, p5].

To our knowledge, these discussions and proposals so far have yet to suggest (1) drawing on CA understanding of natural social interaction at the level of the format of specific turns at talk, and (2) doing so by using actual examples of turn design from the humanhuman equivalent of the specific context in question.

More broadly, central CA principles and analytic procedures have been employed to argue that prevalent VUI concepts such as 'intent', 'tone', and 'personality' are insufficient for understanding what people do with language [12], and to demonstrate the limitations of voice technologies, which (at least currently) can only recognise language, not social actions [4]. In addition to this, there are emerging further considerations of how CA research can inform conversation design, and what the limits of this may be [24].

In this paper, we provide an example of how this can be done, and in doing so argue that conversation designers should be approaching their work not as 'writing scripts' or 'dialogs', to be converted into voice by a text-to-speech (TTS) synthesizer, but as designing their agents' turns-at-talk.

## 4 EXPLOITING NATURAL INTERACTION DATA FOR CONVERSATION DESIGN

In order to be able to draw upon natural interactional patterns to design conversational agent outputs, access to data recordings from equivalent types of interactional events are ideal. Many of the products developed by conversation design teams build on equivalent human-human interactions. Having access to such equivalent human-human interactions and being able to generate recorded data from those settings can make for a rich resource for the conversation design process [10].

Taking as example a call from clinician to a patient, we can consider how the participants structure the overall interaction, and how they format their contributions, with a view to building a toolkit for designing this specific interactional type. We will focus especially on the talk of the clinician (please note: this call has been anonymised, and also only includes the talk of the clinician):

```
((patient answers phone)) 01 (0.6) 02 DOC: ↑ hi: 03 good afternoo:n → 04 it's ↓ doctor grey calling from the 05 trentwood u:h ↑ cataract clinic 06 · h [i'm looking for:]= 07 PAT: [((responds)) ] 08 DOC: =missus green → 09 (0.4) 10 PAT: ((responds)) 11 (0.2) 12 DOC: oh hi missus green → 13 thanks for picking up → 14 um: so my name is doctor grey
```

```
15 (one of X) just doing u:h follow up 16 calls today
```

As source material, such data provide an incredibly rich resource, one which evidences a range of turn-formatting features which could subsequently be used in the design of an agent. We can use this for example as a basis for understanding the order of actions that are routine in such interactional episodes: the presence or absence of a greeting sequence, of identification/recognition sequences, or a business disclosure, or 'how are you' sequences [31]. We can also consider: lexical choices ('hey' or 'hi', or 'good afternoon', or 'greetings'); syntactic features ('It's doctor Grey' or 'Doctor Grey here', or 'I am' or 'I'm'); means of self-identification, as well as issues of recognisability ('It's Dr Grey calling from the Trentwood Cataract Clinic'); intonation contouring, and what this does in terms of inflecting the turn ('It's Dr Grey calling from the Trentwood Cataract Clinic.' or 'It's Dr Grey calling from the Trentwood Cataract Clinic?'); how the institutionality of the call invoked ('Dr Grey' versus 'Marjorie Grey'; 'thanks for picking up').

This extract is taken from a follow-up call to a patient in the UK following a cataract operation, and it follows a canonical pattern for opening such calls (although each interaction is unique, there still are patterns that we find across call openings of this type).

What is more, we can compare an opening such as this with other types of call openings, to identify further specificities to the patterns produced here. How does this differ from calls from a patient to a clinic, rather than the other way around [32]? How might it differ from call openings between acquaintances [32]? How are these calls carried out differently in different cultural groups [13]? How do technological developments impact interactional features of call-openings [15]?

## 4.1 Developing the Design

Once particular regularities have been identified across cases, pointing to a set of practices that speakers orient to as normatively appropriate for the activity at hand, then the conversation designer is able to turn this into code for TTS. Working from data representations of the human interaction, including transcript and any other data treatment (for example acoustic analysis of the vocal output), the designer can construct lines of transcoding that produce speech which is recognisable as the same kind of object as the original. This can be achieved by manipulating TTS to behave in a way that approximates the original. At a lexical level, this means adopting the kinds of language items also drawn on in the original interactions. But this is only a starting point:

Hi. Good afternoon. It's Dora, calling from the Trentwood Hospital Cataract Clinic.

Although a line of dialogue such as this includes all the same lexical items as found in the human interaction, it is still using formatting features for written text which are not part of speech production (i.e. punctuation marking). This impacts how the script is converted to speech, as represented in this transcription:

```
01 DOR: hi (0.3) good afternoon (0.3) it's dora (0.3) calling from the trentwood cataract clinic
```

Figure 1: Comparison of clinician and TTS-generated conversational agent intonation contouring

<!-- image -->

Although the agent's words are produced in exactly the same order as the clinician, the punctuation marking in the script introduces elements into the speech (namely pauses) that are not present in the human turn.

In transcript form, we see these differences highlighted by the intonation marking. With the human clinician:

Further, processing the data through an acoustic analyser (here, Praat), we can clearly see the difference in intonation contouring as well as pauses (Figure 1). The use of punctuation marking in the script also triggers intonation patterns that are not aligned with natural speech (note the blue pitch lines).

```
01 DOC: hi → good afternoon → 02 it's doctor grey calling 03 from the trentwood uh cataract clinic And with the conversational agent: 01 DOR: hi ↘ (0.3) good afternoon ↘ (0.3) 02 it's dora ↘ 03 (0.3) calling from the trentwood cataract 04 clinic ↘
```

Even if we were to remove one of the two greeting components, the downward inflection and ensuing pause would still differ from the formatting seen in human interaction. Normatively, at this point we find callers building on the greeting with talk that identifies them to the call-taker, as we see in the clinician call. For the agent,

From here, we can then consider what a call-receiver might make of the unfolding turn when answering the automated call, in comparison to how they might treat the human-produced turn. In both cases, the call-receiver would answer with a greeting, which makes relevant a return greeting, which we see from the human clinician in the 'hi good afternoon', produced with flat intonation and following which the clinician moves onto an identification sequence. However, here the agent produces the 'hi' with falling intonation which is followed by a pause (triggered by the full stop punctuation in the script), before the second greeting component is added, following the same pattern, with subsequent pause and downward inflection.

however, the pause could be understood by the call-taker as marking a transition relevance place, where they might be expected to produce a next turn. However, they would also know that this would violate the normative pattern for the caller to expand on their return greeting with an identification turn. In short, this presents a potential interactional conundrum for the call-taker, in just the initial seconds of the call.

Finally, we note that these identification turns include different turn final intonation, with the clinician formatting the turn with high rising intonation, and the automated clinical assistant producing falling intonation, triggered by the 'full stop' punctuation in the script. Where the clinician indexes hedging through this rising intonation, acknowledging that the call-recipient may not yet be able to identify the caller or purpose of the call, the formatting of the conversational agent neglects to include any hedging by producing the turn as an affirmative statement.

In a similar fashion, where the identification of the caller in the clinician call is produced as a single unit ('it's doctor grey calling from the trentwood uh cataract clinic ⇑ '), the formatting of the written script prompts the automated clinical assistant to produce this as two separate pieces of information. The first ('it's Dora ↘ ') is formatted as a recognitional, inviting the recipient to identify who is speaking. If the ensuing pause is understood as a transition relevance place, the call-recipient would normatively be expected to acknowledge here that they know who they are speaking with. But it is the second part ('calling from the trentwood cataract clinic ↘ ') that contextualises who the caller is.

## 4.2 Mobilising SSML for transcoding speech

To approximate the kinds of formatting of human turn design, we need to produce the kinds of transcode that prompt the speech synthesizer to produce acoustic patterns that emulate equivalent human speech formatting. To achieve this, the conversation designer can first explore how the synthesizer responds to different text input. For example, we can strategically deploy a question mark in place of a full stop or comma, or vice versa, to trigger different behaviours in the synthesizer. Where we come up against limitations, then using speech synthesis markup language (SSML) opens up a wide range of possibilities for manipulating the speech output.

SSML. English (United States) - Neural Voice 2 - en-US-Neural2H (Speed 1.0; Pitch 0.0)

We noted above how the punctuation marking in the text caused the speech synthesizer to format output in ways that deviated from the natural speech it was based on. It introduced gaps in the speech flow, and the prosodic curves of intonation were wholly at odds with the human speech. However, processed with SSML, we arrive at a much closer approximation of the human turn at talk (Figure 2). We invite readers to compare between TTS, and the below SSML markup:

```
https://cloud.google.com/text-to-speech#section-2 <speak> <prosody rate="90\%" pitch="+4st" > hai </prosody> <prosody rate="98\%" pitch="+2st" > good afternoon </prosody> <prosody rate="105\%" pitch="+4st" > this </prosody> <prosody rate="105\%" pitch="+8st" > is </prosody> <prosody pitch="+3st">DORA</prosody>
```

Figure 2: Comparison of clinician and SSML-transcoded conversational agent intonation contours

<!-- image -->

&lt;prosody rate="120\%"&gt;the clinical assistant from &lt;/prosody&gt; &lt;prosody rate="110\%"&gt; trentwood cataract clinic? &lt;/prosody&gt; &lt;/speak&gt;

In comparing the acoustic analysis of the SSML-produced speech with that of the human production, we see now that similarities are emerging that were missing in the earlier TTS output. As can be seen in the visualisation, the gaps in the flow of speech introduced by the TTS have been removed, and the intonation contouring of the overall speech segment follows a similar trajectory, starting out with relatively flat contouring on the greeting element, dropping on the identification and formatted with upward intonation at the end. We now have a VUI turn-at-talk which much more closely replicates that of a human equivalent.

## 5 SUMMARY

'Naturalness' is at the centre of conversation design. However, not all VUIs are designed to emulate a natural interaction experience. At the very least, there may be aspects of natural human-human interaction that the designer may choose to exclude. The design of a conversational agent may on the one hand emulate organisational features characteristic of turn-taking in everyday interaction; but mayfor example avoid those features of everyday interaction where human traits such as sentience, empathy, or cognition, are implied.

However, where a conversation designer does want some semblance of naturalism evoked in the CUI, knowledge of how social interaction works, how it is produced, organized and managed, in general and in that particular setting, will be crucial. Without a deeper understanding of the particular practices humans draw on in their dealings with one another, the conversation designer is left to the whims of personal intuition (or recollection). More than this, conversation designers should, where possible, base the formatting of their agent's turns-at-talk, on equivalent turn formatting produced by humans from the same context, be that clinical consultations, customer service encounters, cold-call sales, counselling support, etc. We have demonstrated one possible way to begin to address this challenge.

While this proposed approach is more time-consuming in the preparatory change of conversation design process, the benefits would vastly outweigh any limits. The aim of a VUI-interaction in a given setting is to elicit certain responses from the user (whether that is disclosing symptoms following surgery, or providing details of a customer support query). The most effective way to do this is to invoke the norms of interaction that the user will be expecting. And again, these norms vary across institutional contexts. So it will be for conversation designers (and collaborating CA practitioners) to determine what aspects of a conversation need to be specifically type-fitted for the setting in order for the VUI to support the user in achieving the institutional aims of the interaction.

The context-specific nature of this proposal is key. While all individual interactions are unique, over 60 years of CA research has demonstrated that normative patterns are to be found across individual cases from a different context [8, 11]. While there are general principles of conversation which remain true across all settings (for example, turn-taking and repair), research has shown that the application of these principles can, and does, vary according to the institutional goals of a given interaction, and the institutional roles of those involved. This can include aspects of interaction such as lexical choices, politeness markers, interactional rights to allocate turns, and so on. It is therefore problematic to assume, for example, that the way two acquainted parties ask one another questions in an informal setting will be the same as the way a clinician asks a patient a series of questions.

## ACKNOWLEDGMENTS

This project is supported by a British Academy Innovation Fellowship (IF2223/230141). The authors would like to thank the anonymous reviewers and Area Chairs for their helpful feedback and comments on a previous draft.

## REFERENCES

- [1] Natural Speech | Alexa Design Guide. https://developer.amazon.com/en-US/alexa/ alexa-haus/natural-speech
- [3] Saul Albert and Magnus Hamann. 2021. Putting wake words to bed: We speak wake words with systematically varied prosody, but CUIs don't listen. In Proceedings of the 3rd Conference on Conversational User Interfaces (CUI '21). Association for Computing Machinery, New York, NY, USA, Article 13, 1-5. https://doi.org/10.1145/3469595.3469608
- [2] Conversation Design. https://developers.google.com/assistant/ conversation- design/welcome
- [4] Saul Albert, William Housley, and Elizabeth Stokoe. 2019. In case of emergency, order pizza: an urgent case of action formation and recognition. In Proceedings of the 1st International Conference on Conversational User Interfaces (CUI '19). Association for Computing Machinery, New York, NY, USA, Article 15, 1-2. https://doi.org/10.1145/3342775.3342800
- [6] Leigh Clark, Nadia Pantidi, Orla Cooney, Philip Doyle, Diego Garaialde, Justin Edwards, Brendan Spillane, Emer Gilmartin, Christine Murad, Cosmin Munteanu, Vincent Wade, and Benjamin R. Cowan. 2019. What Makes a Good Conversation? Challenges in Designing Truly Conversational Agents. In Proceedings of the 2019 CHI Conference on Human Factors in Computing Systems (CHI '19). Association for Computing Machinery, New York, NY, USA, Paper 475, 1-12. https://doi.org/ 10.1145/3290605.3300705
- [5] Iuliia Avgustis, Aleksandr Shirokov, and Netta Iivari. 2021. 'Please Connect Me to a Specialist': Scrutinising 'Recipient Design' in Interaction with an Artificial Conversational Agent. In Human-Computer Interaction - INTERACT 2021: 18th IFIP TC 13 International Conference, Bari, Italy, August 30 - September 3, 2021, Proceedings, Part IV. Springer-Verlag, Berlin, Heidelberg, 155-176. https://doi. org/10.1007/978-3-030-85610-6\_10

- [7] Benjamin R. Cowan, Leigh Clark, Heloisa Candello and Janice Tsai. 2023. Introduction to this special issue: guiding the conversation: new theory and design perspectives for conversational user interfaces, Human-Computer Interaction. 38, 3-4 (2023), 159-167. DOI: 10.1080/07370024.2022.2161905
- [9] Joel E. Fischer, Stuart Reeves, Martin Porcheron, and Rein Ove Sikveland. 2019. Progressivity for voice interface design. In Proceedings of the 1st International Conference on Conversational User Interfaces (CUI '19). Association for Computing Machinery, New York, NY, USA, Article 26, 1-8. https: //doi.org/10.1145/3342775.3342788
- [8] Paul Drew and John Heritage. 1992. Talk at Work: Interaction in Institutional Settings. Cambridge University Press.
- [10] Spencer Hazel and Adam Brandt. forthcoming. Enhancing the Natural Conversation Experience through Conversation Analysis - a design method. In HCI International 2022-Late Breaking Papers. 25th International Conference on Human-Computer Interaction, HCII 2023, 23-28 July. Springer.
- [12] William Housley, Saul Albert, and Elizabeth Stokoe. 2019. Natural Action Processing. In Proceedings of the Halfway to the Future Symposium 2019 (HTTF 2019). Association for Computing Machinery, New York, NY, USA, Article 34, 1-4. https://doi.org/10.1145/3363384.3363478
- [11] John Heritage and Steven Clayman. 2010. Talk in Action: Interactions, Identities, and Institutions. Wiley-Blackwell.
- [13] Hanneke Houtkoop-Steenstra. 1991. Opening sequences in Dutch telephone conversations. In Talk and social structure: Studies in ethnomethodology and conversation analysis, Deirdre Boden and Don H. Zimmerman (Eds). Cambridge: Polity, 232-50.
- [15] Eric Laurier. 2001. Why People Say Where They are during Mobile Phone Calls. Environment and Planning D: Society and Space, 19, 4 (2001). 485-504. https: //doi.org/10.1068/d228t
- [14] Yelim Kim, Mohi Reza, Joanna McGrenere, and Dongwook Yoon. 2021. Designers Characterize Naturalness in Voice User Interfaces: Their Goals, Practices, and Challenges. In Proceedings of the 2021 CHI Conference on Human Factors in Computing Systems (CHI '21). Association for Computing Machinery, New York, NY, USA, Article 242, 1-13. https://doi.org/10.1145/3411764.3445579
- [16] Robert J. Moore, Margaret H. Szymanski, Raphael Arar, Guang-Jie Ren (Eds) 2018. Studies in Conversational UX Design. Springer.
- [18] Robert J. Moore, Sungeun An and Guang-Jie Ren. 2023. The IBM natural conversation framework: a new paradigm for conversational UX design, HumanComputer Interaction. 3, 3-4 (2023). 168-193. DOI: 10.1080/07370024.2022.2081571
- [17] Robert J. Moore and Raphael Arar. 2019. Conversational UX Design: A Practitioner's Guide to the Natural Conversation Framework. Association for Computing Machinery, New York, NY, USA.
- [19] Christine Murad and Cosmin Munteanu. 2019. "I don't know what you're talking about, HALexa": the case for voice user interface guidelines. In Proceedings of the 1st International Conference on Conversational User Interfaces (CUI '19). Association for Computing Machinery, New York, NY, USA, Article 9, 1-3. https://doi.org/10.1145/3342775.3342795
- [21] Christine Murad, Cosmin Munteanu, Benjamin R. Cowan, and Leigh Clark. 2021. Finding a New Voice: Transitioning Designers from GUI to VUI Design. In Proceedings of the 3rd Conference on Conversational User Interfaces (CUI '21). Association for Computing Machinery, New York, NY, USA, Article 22, 1-12. https://doi.org/10.1145/3469595.3469617
- [20] Christine Murad and Cosmin Munteanu. 2020. Designing Voice Interfaces: Back to the (Curriculum) Basics. In Proceedings of the 2020 CHI Conference on Human Factors in Computing Systems (CHI '20). Association for Computing Machinery, New York, NY, USA, 1-12. https://doi.org/10.1145/3313831.3376522
- [22] Christine Murad, Cosmin Munteanu, Benjamin R. Cowan, Leigh Clark, Martin Porcheron, Heloisa Candello, Stephan Schlögl, Matthew P. Aylett, Jaisie Sin, Robert J. Moore, Grace Hughes, and Andrew Ku. 2021. Let's Talk About CUIs: Putting Conversational User Interface Design Into Practice. In Extended Abstracts of the 2021 CHI Conference on Human Factors in Computing Systems (CHI EA '21). Association for Computing Machinery, New York, NY, USA, Article 98, 1-6. https://doi.org/10.1145/3411763.3441336
- [24] Cathy Pearl, Saul Albert, and Elizabeth Stokoe. 2022. What insights from conversation analysis can, should, and should not be leveraged when collaborating in conversation design? 4th International Conference on Conversational User Interfaces (CUI '22), Glasgow, UK. 26-28 July
- [23] Christine Murad, Humaira Tasnim, and Cosmin Munteanu. 2022. 'Voice-First Interfaces in a GUI-First Design World': Barriers and Opportunities to Supporting VUI Designers On-the-Job. In Proceedings of the 4th Conference on Conversational User Interfaces (CUI '22). Association for Computing Machinery, New York, NY, USA, Article 17, 1-10. https://doi.org/10.1145/3543829.3543842
- [25] Hannah R.M. Pelikan and Mathias Broth. 2016. Why That Nao? How Humans Adapt to a Conventional Humanoid Robot in Taking Turns-at-Talk. In Proceedings of the 2016 CHI Conference on Human Factors in Computing Systems (CHI '16). Association for Computing Machinery, New York, NY, USA, 4921-4932. https://doi.org/10.1145/2858036.2858478
- [27] Martin Porcheron, Joel E. Fischer, Stuart Reeves, and Sarah Sharples. 2018. Voice Interfaces in Everyday Life. In Proceedings of the 2018 CHI Conference on Human Factors in Computing Systems (CHI '18). Association for Computing Machinery, New York, NY, USA, Paper 640, 1-12. https://doi.org/10.1145/3173574.3174214
- [26] Hannah R. M. Pelikan, Mathias Broth, and Leelo Keevallik. 2020. "Are You Sad, Cozmo?": How Humans Make Sense of a Home Robot's Emotion Displays. In Proceedings of the 2020 ACM/IEEE International Conference on Human-Robot Interaction (HRI '20). Association for Computing Machinery, New York, NY, USA, 461-470. https://doi.org/10.1145/3319502.3374814
- [28] Stuart Reeves, Martin Porcheron, Joel E. Fischer, Heloisa Candello, Donald McMillan, Moira McGregor, Robert J. Moore, Rein Sikveland, Alex S. Taylor, Julia Velkovska, and Moustafa Zouinar. 2018. Voice-based Conversational UX Studies and Design. In Extended Abstracts of the 2018 CHI Conference on Human Factors in Computing Systems (CHI EA '18). Association for Computing Machinery, New York, NY, USA, Paper W38, 1-8. https://doi.org/10.1145/3170427.3170619
- [30] Harvey Sacks. 1984, Notes on methodology. In Structures of Social Action: Studies in Conversation Analysis, John Heritage, and J. Maxwell Atkinson (Eds). Cambridge: Cambridge University Press, 2-27.
- [29] Stuart Reeves, and Martin Porcheron. 2022. Conversational AI: Respecifying participation as regulation. In The SAGE Handbook of Digital Society, William Housley, Adam Edwards, Roser Beneito-Montagut, and Richard Fitzgerald (Eds). SAGE.
- [31] Emanuel A. Schegloff. 1986. The routine as achievement. Human Studies. 9, 2 (1986). 111-151.
- [33] Elizabeth Stokoe, Saul Albert, Sophie Parslow, and Cathy Pearl. 2021. Conversation design and conversation analysis: Where the moonshots are. Medium. https://elizabeth-stokoe.medium.com/conversation-design-andconversation-analysis-c2a2836cb042
- [32] Rein Sikveland, Elizabeth Stokoe, Jon Symonds. 2016. Patient burden during appointment-making telephone calls to GP practices. Patient Education and Counselling. 99, 8 (2016). 1310-1318.
- [34] Sylvaine Tuncer, Christian Licoppe, Paul Luff, and Christian Heath. 2023. Recipient design in human-robot interaction: the emergent assessment of a robot's competence. AI &amp; Society. https://doi.org/10.1007/s00146-022-01608-7