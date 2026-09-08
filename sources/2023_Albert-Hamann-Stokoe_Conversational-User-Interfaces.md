---
stem: 2023_Albert-Hamann-Stokoe_Conversational-User-Interfaces
pdf_path: papers\2023_Albert-Hamann-Stokoe_Conversational-User-Interfaces.pdf
source_path: sources\2023_Albert-Hamann-Stokoe_Conversational-User-Interfaces.md
source_hash: ce0d80caddbaadde729776295d7d7a02f02a61bc4d3999d3426d0038fc86fc6a
parsed_with: docling
parsed_at: '2026-09-07T14:25:23+00:00'
warnings: []
record_id: paper:2023_Albert-Hamann-Stokoe_Conversational-User-Interfaces
---
.

<!-- image -->

<!-- image -->

<!-- image -->

.

.

<!-- image -->

.

.

.

.

.

.

.

.

## [Latest updates: hps://dl.acm.org/doi/10.1145/3571884.3597140](https://dl.acm.org/doi/10.1145/3571884.3597140)

.

.

RESEARCH-ARTICLE

## Conversational User Interfaces in Smart Homecare Interactions: A Conversation Analytic Case Study

SAUL ALBERT , Loughborough University, Loughborough, Leicestershire, U.K. MAGNUS HAMANN , Loughborough University, Loughborough, Leicestershire, U.K. ELIZABETH STOKOE , London School of Economics and Political Science, London, U.K.

Open Access Support provided by: Loughborough University London School of Economics and Political Science

<!-- image -->

.

.

.

.

.

.

PDF Download 3571884.3597140.pdf 08 April 2026 Total Citations: 8 Total Downloads: 1319

.

.

Published: 19 July 2023

[Citation in BibTeX format](https://dl.acm.org/doi/10.1145/3571884.3597140#download-citation)

CUI '23: ACM conference on Conversational User Interfaces July 19 - 21, 2023 Eindhoven, Netherlands

Conference Sponsors:

[SIGCHI](https://dl.acm.org/sig/sigchi)

## Conversational User Interfaces in Smart Homecare Interactions: A Conversation Analytic Case Study

## [Saul Albert ∗](https://orcid.org/0000-0003-1043-1237)

s.b.albert@lboro.ac.uk Loughborough University Loughborough, Leicestershire, UK

## ABSTRACT

Policymakers are increasingly interested in using virtual assistants to augment social care services in the context of a demographic ageing crisis. At the same time, technology companies are marketing conversational user interfaces (CUIs) and smart home systems as assistive technologies for elderly and disabled people. However, we know relatively little about how today's commercially available CUIs are used to assist in everyday homecare activities, or how care service users and human care assistants interpret and adapt these technologies in practice. Here we report on a longitudinal conversation analytic case study to identify, describe, and share how CUIs can be used as assistive conversational agents in practice. The analysis reveals that, while CUIs can augment and support new capabilities in a homecare environment, they cannot replace the delicate interactional work of human care assistants. We argue that CUI design is best inspired and underpinned by a better understanding of the joint coordination of homecare activities

## CCS CONCEPTS

- Social and professional topics → People with disabilities ;
- Human-centered computing → Activity centered design ; Empirical studies in HCI ; Empirical studies in accessibility ; · Computing methodologies → Discourse, dialogue and pragmatics .

## KEYWORDS

conversational user interfaces, conversation analysis, ethnomethodology, disability, social care

## ACMReference Format:

Saul Albert, Magnus Hamann, and Elizabeth Stokoe. 2023. Conversational User Interfaces in Smart Homecare Interactions: A Conversation Analytic Case Study. In ACM conference on Conversational User Interfaces (CUI '23), July 19-21, 2023, Eindhoven, Netherlands. ACM,NewYork,NY,USA,12pages. https://doi.org/10.1145/3571884.3597140

<!-- image -->

This work is licensed under a Creative Commons Attribution International 4.0 License.

CUI '23, July 19-21, 2023, Eindhoven, Netherlands © 2023 Copyright held by the owner/author(s). ACM ISBN 979-8-4007-0014-9/23/07. https://doi.org/10.1145/3571884.3597140

## [Magnus Hamann](https://orcid.org/0000-0001-8666-3427)

m.hamann@lboro.ac.uk Loughborough University Loughborough, Leicestershire, UK

The London School of Economics and Political Science London, UK e.stokoe@lse.ac.uk

## 1 INTRODUCTION

Policymakers are increasingly looking to new assistive technologies to augment social care services in the context of a demographic ageing crisis [55], suggesting that '[d]ata-driven services and emerging robotic and artificial intelligence (AI) technologies could provide services to help maintain independence for older people' [70]. At the same time, technology companies are promoting conversational user interfaces (CUIs) and smart home systems as assistive technologies for elderly and disabled people. In Amazon's [2019a] 'Sharing is Caring' advert, for example, a stereotypical elderly man learns to use an Amazon Echo by watching his (human) personal assistant interact with the Echo's virtual assistant Alexa . However, HumanComputer Interaction (HCI) research in this area tends to adopt a medical model of assistive technology design that focuses on hightech 'fixes' for individuals' impairments (e.g., [11, 62, 69]), and there is still little evidence available to practitioners and policymakers as to how these technologies work within real health and care settings [60, 100].

This paper reports on a case study exploring how CUIs are integrated into the daily routines of a naturalistic homecare setting. Specifically, we focus on how a disabled person and their personal assistant manage and distribute their work during homecare routines such as eating, getting out of bed, or using the toilet. We used conversation analysis to examine 180 interactions with CUIs drawn from over 100 hours of recordings to understand how users adapt their interactions to work with a CUI and a range of smart home devices. Our analyses focus on how users encounter and resolve practical and interactional troubles that emerge when using the CUI as a functional component of the homecare environment. By examining these moments in detail, we develop a distributed, interactionally informed analysis that aims to enable designers and engineers to develop CUIs that manage the contingencies of the smart homecare setting.

## 1.1 Models of disability in assistive technology research

Finding an appropriate user model is a core concern for HCI, especially when designing systems for disabled users [24]. Within the social sciences more broadly, more abstract conceptual models also provide a framework for understanding the construction of social categories such as 'able bodied' or 'disabled'. In this context, there is a long-standing, debate about competing models of disability [92] with significant implications for assistive technology design. Assistive technology research often builds on a 'medical model' of disability that conceives of the user as an individual with a specific physical or cognitive deficit that requires a technical fix [43]. For

## [Elizabeth Stokoe](https://orcid.org/0000-0002-7353-4121)

example, studies of the potential of CUIs for accessibility in a survey by Clark et al. 2019 tend to focus on the potential of speech technologies to enable people with a range of impairments to complete a specific set of performance-measurable tasks (see e.g., [5, 61, 71, 72]). This medical model of disability is often criticized for focusing on individuals and impairments rather than on the disabling impact of poorly adapted environments, for reducing people's experience of disability to a narrow range of functional parameters, and for promoting expensive, stigmatizing, and impractical technologies over simpler adaptations [66] 1 .

Conceptual models of disability are essential for the design of assistive technology because they help identify user needs and match them to overall system goals [15, 16]. Different conceptual models of disability can guide researchers' choices about design frameworks, processes of requirements gathering, and goal-setting in smart homecare systems design. In the following section, we review the goals and challenges of developing user models for developing smart homecare systems.

Conversely, studies of disability and technology that adopt a 'social model' of disability attribute disabling factors to poorly adapted environments and social stigma [15] and promote social and environmental interventions that de-stigmatize the individual as the locus of the 'problem' that assistive technology aims to solve [29]. The social model has successfully fostered the inclusion of disabled people and in challenging the dominant, medical model of disabled users in assistive technology design [42]. However, the social model has also been criticized for focusing solely on social constructs, for effacing the individuality and diversity of disabled people [18], and for overlooking the support needs of people with learning disabilities [83]. Drawing on Hughes and Paterson's 1997 sociological analysis of impairment [48], Cluley et al. 2020 suggest that both the medical model and social model misconceive impairment and disability, either by commission (medicalizing impairment as an individual, physiological issue), or by omission (minimizing individual-in favor of social-issues) [14].

## 1.2 The goal of independence in smart homecare systems

When informed by either medical or social models of disability, user-centered design frameworks and other methods for identifying users' personal and contextual requirements tend to emphasize the independence of disabled users as an end-goal [23, 90]. However, the goal of independence itself is not necessarily empowering for disabled people. Clinicians frequently cite the goal of independence in terms of reduced reliance on (human) personal assistance as a primary reason for recommending assistive technologies [46]. Accordingly, assistive technologies that involve conversational agents or social robots are often promoted as supporting the independence of elderly and disabled people. This image of technology-enabled independence is prominent both in the marketing of consumer 'smart home' devices (see e.g., [21, 22]), and in the design of research prototypes for socially assistive robotics (e.g., [52, 63, 64]).

1 For example, the 2019 'Topol report' on the future of healthcare [91] illustrates its section on assistive technology with an image of a young disabled boy encased in a huge robotic exoskeleton, lumbering across a walk track in a high-tech laboratory.

Unrealistic representations of futuristic care robots that are promoted in media reports are reflected in public perceptions about the potential role of such technologies in the future of health and social care [93, 100]. This technological imaginary of autonomous assistive robots and high-tech 'independence', in turn, can shape healthcare investment and policy (e.g., [75, 91]) as well as the legal, ethical, and functional frameworks that will inform the technical specifications of future homecare systems [58, 79, 101]. However, there is still little evidence to support the efficacy of this approach [60, 98, 99], and critical questions remain as to how the goal of independence will be interpreted and embedded into the future technical infrastructures that underpin smart homecare systems.

While these two interpretations of independence as a goal (making decisions for oneself, or doing things for oneself), are not mutually exclusive, the former-prioritizing the decisions and needs of disabled people-is clearly more empowering than the latter, which is vulnerable to paternalistic and utilitarian design and policymaking that prioritizes the apparent efficiencies and cost-savings of automation [6, 12, 84]. The danger of emphasizing this less empowering notion of independence is that it embeds a deficit-based medical model of disability into the technical process of user modelling. This approach defines disabled users primarily in relation to their impairment (rather than their social environment), and seeks to 'enable' them to operate as an autonomous individual [82]. However, even for ostensibly able-bodied users, technologies designed for this 'default' individualized user tend to be poorly adapted for the inherently interdependent, multi-party interactional settings that we all inhabit in our everyday lives [1, 3, 74].

Assistive technology development projects are often stuck between incompatible understandings of independence. On the one hand, the social model of disability has informed the concept of 'independent living' developed within the disability civil rights movement [95], focusing on disabled people making decisions about their own care needs. This notion of independence is empowering in that it gives disabled people choices about how to structure their everyday lives. In more medicalized approaches to assistive technology, on the other hand, independence is often cited as a goal for systems that promise to enable users to do things for themselves. This concept of independence assumes that people can find practical, social, and emotional support (that would otherwise require human assistants or residential care facilities), from relatively cheap virtual agents and smart homecare systems (e.g., [9, 27, 34]).

## 1.3 The centrality of interdependence for homecare interactions

This paper reports on a longitudinal case study exploring how a disabled person and their (human) care assistant interact while using an Amazon Echo to collaborate on shared tasks as they work through their daily care routine together. Our focal phenomena here are the homecare interactions, rather than (as is more usual) individual users, specific impairments, or particular assistive technologies. This approach builds on the results of over thirty years of interactional research showing how people with apparently severe language impairments still communicate effectively as they engage in intrinsically interdependent courses of social action [30, 32, 96]. For example, Goodwin's 2004 study showed how his father Chil, whohadbeen a noted raconteur before he developed aphasia following a stroke, was still able to tell complex stories and reminiscences, despite only being able to articulate the words 'yes', 'no', and 'and'. By eliciting stories from his family and timing his gestures along with his positive, negative, or conjunctive vocalizations, Chil was able to shape storytellings in progress, co-constructing stories by harnessing others' verbal contributions [32] 2 . For this reason, we use methods that draw on evidence for the centrality of interdependence and cooperative action , (rather than independence and autonomy ) for interactional processes in general [31, 33], and for the social construction of ability and disability through interaction in particular [7, 32]. Our analyses focus on describing the organization of interaction between participants and its 'distributions and linkages across human and technological realms' [1], rather than on characterizing autonomous individuals and discrete technologies as such. This approach avoids essentializing disability and assistive technology as entirely either socially or medically determined [18], and aims to inspire CUI developers to design for the interdependent contingencies of interaction in everyday homecare settings. In the following section, we outline our methods for studying CUIs as part of an assistive environment in which 'interdependency and collective action are the focus' [14] by shifting from analysis of users and devices to center on mechanisms of social interaction.

## 2 DATA AND METHODS

The video data used in this case study was drawn from over 100 hours of naturalistic recordings featuring interactions between a disabled man, his personal assistant, and a virtual assistant. The data were recorded by the participants over the course of a year during which they used two IP cameras to capture footage to a cloud server continuously for several days at a time. To ensure their control over any potentially sensitive recordings, they were shown how to review, save, and delete footage before sharing it as open data for research purposes. Both agreed to share the research recordings openly to encourage further research into the development of accessible CUIs and smart home systems. 3 Whenever the Amazon Echo device was successfully activated with the 'wake word' 'Alexa', interactions with the system were recorded on the user's 'Alexa Voice History Log' linked to an Amazon account. These logs were shared with the research team and used as a searchable index for the video data.

Our data selection rationale drew on methods of mapping the affordances of new technologies in HCI by identifying moments of trouble or 'breakdown' [94] in user experience, then observing how users work to resolve them. Related empirical studies of 'repair' practices [51, 56, 81] in human social interaction suggest that this approach could provide tractable starting points for analyzing interactional trouble [4, 38] and moments of possible intersubjective 'breakdown' [68] in both human-human and human-machine interaction. We searched the Alexa logs to identify situations in which the wake word 'Alexa' was used repeatedly to activate and reactivate the Amazon Echo device. This process yielded an initial collection of 180 cases of miscommunication between the human users and the virtual assistant that allowed us to observe how they worked together to resolve interactional problems.

2 At least he was until his wife died, leaving him unable to retrieve and relate any new stories based on their shared biographies together.

3 This data collection and sharing protocol was approved by Loughborough University's research ethics procedures (8-8-2019).

Perhaps because they are designed for studying conversation, these methods are becoming established within a branch of CUI research that shows, in detail, how CUIs can reflexively shape the socio-material and interactional environments they constitute [3, 25, 44, 74]. The descriptive findings of these CA studies derive their reliability from this reflexive, inductive process rather than from concepts of generalizability based on hypothetico-deductive reasoning and probability sampling [2]. CA aims, instead, for the transferability of findings between cases [59] by building and testing analytic 'collections' of many cases of procedurally and pragmatically similar actions [45]. Since the focus is on the structure and function of social actions rather than on persons , note that the n in this research context is denominated in cases rather than e.g., numbers of participants or user tests, as is more common in HCI. To avoid reproducing a medical model of disability, and since interactional structure can be observed and described accurately without including biographical, medical, and relational information about the individuals involved, we do not include these details in our analysis. Similarly, since our analysis focuses on sequences of action rather than on a particular technical implementation, we do not focus on the specific make and model of the CUIs featured.

We then used (CA) [86] to transcribe, annotate, and describe these interactions in detail. Unlike qualitative methods that focus primarily on the propositional content of speech or text, CA aims to identify the 'repetitive, uniform, typical and cohort-independent' practices [39] that organize talk and social interaction. The analytic object of CA is interaction itself, so the analytic process tracks how social actions such as greetings, instructions, and requests are designed, recognized, and accomplished in specific settings. The analytic process involves recording interaction in naturalistic settings, then creating technical transcripts including annotations of details such as intonation, prosody, and overlap, along with multi-modal resources such as gesture, gaze, and body orientation [40]. Because observational analyses are inherently reliant on researchers' own interactional competencies and interpretations, analysts use two main methods to test the robustness of their inductive findings. Firstly, instead of relying on analyst's inductive interpretations of meaning, each observation relies on endogenous evidence provided in the data itself using a next turn 'proof procedure' [36]. For example, when, an action (e.g., a question) is produced by one participant in a recorded conversation, this utterance would only be analyzed as a question if that is how it is treated by a recipient in the next turn (e.g., by giving an answer). Secondly, to enhance the reliability of these observations, CA researchers conduct 'data sessions' as a form of rapid, iterative panel review for work-in-progress [35]. During data sessions, a mix of expert interaction analysts, domain experts, (and, in some cases, participants themselves [19]), review video clips and use detailed transcripts to check and, very often, contest each other's analyses [8]. Each analysis presented below were reviewed at least one CA data session.

In our initial review of 180 cases, we noticed that Ted, the disabled person in the clips below, would often need assistance from Anna, his human care assistant to summon the virtual assistant (VA) Alexa . Ted would also often use his VA to summon Anna. The extracts below feature a range of methods that Ted and Anna use for summoning and commanding Alexa , and for dealing with summons/command responses. All cases involve Ted and Anna using a range of methods to summon and 'recruit' various types of assistance from each other, often while using Alexa . We use the terms 'assistance' and 'recruitment' technically here to mean 'the linguistic and embodied ways in which assistance may be sought-requested or solicited-or in which we come to perceive another's need and offer or volunteer assistance' [54]. Examining recruitment in these terms also opens opportunities for analyzing interactional practices for the design (prosodic, grammatical, and embodied) of requests for-and offers of-assistance [17]. These practices range from explicit methods for requesting assistance and 'getting others to do things' on the one hand [26], to tacit, embodied methods for noticing and meeting others' immediate wants and needs on the other [53]. Recruitment events appear to be a universal prosocial human behavior that occur very frequently (every 2-3 minutes) in everyday interaction across cultures and languages [78]. The goal here is to describe, in detail, how the interactional matrix for assistance-seeking and assistance-granting [41] operates in a smart homecare setting and to ask how, if at all, this fundamental practice of human sociality can be organized to involve CUIs.

## 3 ANALYSIS

Before exploring instances of how users configure more complex interactional environments to work with CUIs, our first example features simple failures to summon a virtual assistant 4 . In Figure 1, Ted is alone in his room when he inadvertently initiates a conversation with two 'smart' virtual agents simultaneously, both of which use the 'wake word' method of initiating interactions with a CUI. Note that the line running down the left of the transcripts below represents the pattern of 'wake light' activation.

We can break this episode down into a series of two summonsresponse sequences and one instruction/response sequence that intersect with one another. The first sequence starts with the wake word at line 1 and immediately gets a response from Alexa when the wake light comes on (and stays on until line 17). The second summons-response sequence, this time directed to Siri, starts at line 11, and is responded to in line 13 when Siri produces its audible 'wake beep' sound to indicate its readiness for a command. The third sequence, however, is initiated in line 14 when Alexa responds to Ted's 'Hey Siri' with a pre-programmed wisecrack response, 'I think you've got me confused with someone else'. Siri treats Alexa's wisecrack as a new command and offers to search the web for the phrase. Ted finally abandons his attempts to initiate an interaction with Siri.

Ted summons Alexa on his Amazon Echo when he means to summon Apple's VA Siri on his iPhone. This is clear from the way that Ted repeats the wake word 'Alexa' in lines 1 and 5 while gazing towards his iPhone (behind the cup on his desk), then briefly shifts his gaze to Alexa while saying 'ahh wrong one' in line 9 before summoning Siri on his iPhone in the next turn.

It is striking that even though Alexa's designers had (rightly) anticipated precisely this situation, they chose to program Alexa to make a wisecrack rather than simply suppressing a response to a turn that is clearly intended for 'someone else'. As is clear from Siri's pro-forma response, Siri's designers had not fully anticipated this situation leading to a miscued 'fallback': offering to search the web for the prior command (whatever it was). In both these failures, we see how CUIs can struggle to deal with the presence of other wake-word activated voice technologies. Both responses also suggest a flawed assumption in the basic user/dialogue model, i.e., that a user in a room without other wake-word activated devices requires the CUI to respond to the last utterance. The following extracts show how designers could take advantage of the wider interactional environment of CUIs, and how users configure their multi-party interactions to include CUIs in effective and inventive ways.

4 For a more detailed analysis of this extract see [3].

Figure 1: Ted summons Alexa then immediately self-corrects to summon Siri (video)

<!-- image -->

## 3.1 Acting independently with a virtual assistant

In some situations, such as when going to the toilet, an interactional environment in which one is entirely independent of others may be more desirable. One of the complications of homecare is that personal assistants are only there for given times in the day, so going to the toilet cannot necessarily be spontaneous, but must be integrated into a homecare routine. When the following extract begins, Ted is on his commode. His personal assistant Anna has lifted him onto the commode using the ceiling track hoist and is waiting in the adjoining room. Ted has set a timer alarm for 15 minutes, which is about to go off.

Figure 2: Ted completes part of a care routine then summons Anna to help finish it (video)

<!-- image -->

Figure 3 provides another example of using the VA to summon the human care assistant. The extract begins just after Ted's afternoon nap when he is using the CPAP breathing machine that he must wear whenever he is sleeping. Since the mask covers Ted's face, he cannot summon or instruct Alexa himself. For this situation, Ted and Anna have repurposed an 'echo button' (a simple controller intended to be used for quizzes and games with the Echo) as a 'call button' for Anna. When Ted presses the button, the Echo has been configured to play the request 'please remove the mask now' on all the Echo devices in the house-summoning Anna to come and help with the next phase of the homecare routine.

This series of summons, command and response sequences shows Ted using the Echo device to do as much as he can achieve without Anna's help: stopping the alarm and turning off the heater that is keeping him warm during the toilet routine. Getting off the commode, however, requires assistance, so Ted summons and instructs Alexa to summon his Anna for the next task in the care routine. While this episode is still ostensibly a 'single user' interaction with a CUI, we see how the summons/command/response sequence can begin to involve others when the final command 'Call Anna." operates something like a 'switchboard request' 5 : handing the interaction-in-progress over to someone else.

Ted is still wearing his mask when he asks Anna the time in line 4 and she relays that question directly to Alexa in line 7, eliciting a time announcement that Ted can hear. Once Anna removes Ted's mask and begins to take off his blankets, Ted then takes on the task of commanding Alexa to turn on the heater in line 17.

5 A 'switchboard request' involves asking to speak to someone other than the initial call-answerer in a pre-caller-ID telephone opening [80]).

Figure 3: Ted presses an Echo Button to summon Anna to remove his CPAP breathing mask (video)

<!-- image -->

Through these elegant hand-overs, we see how Anna and Ted implicate a CUI in the coordination of their joint activities. In the following extracts we will see further examples where Ted takes on tasks himself by using a CUI to act within the participation framework of his joint activity with Anna.

Note that the request to remove the mask in line 1 is directed to Anna, but spoken by Alexa, and initiated by Ted - and will be repeated every time Ted presses the Echo button. The hand-over of the task of interacting with Alexa highlights how closely Ted and Anna monitor one another's activities and coordinate their availability for doing part of their shared activity using the CUI. For example, while Anna could easily have turned on the heater herself (as a familiar part of this 'waking up from a nap' care routine), we see her take off Ted's mask and then get on with her part of the next task in the routine, allowing Ted to take the initiative with Alexa to turn off the heater.

## 3.2 Sharing joint activities with the virtual assistant

In the examples we have seen so far, the methods used for recruiting assistance are mostly explicit command/request sequences or information-seeking questions such as time-checks. Where these CUI-directed requests are troubled by miscommunication, we see more clearly they can provide participants with opportunities to coordinate joint activities.

In Figure 4, Ted has just woken up and Anna is unclipping the wheels on his bed so she can roll it underneath the ceiling track and hoist him into his wheelchair (see Figure 1). Before moving the bed, the heater needs to be turned off and moved out of the way. Note that the smart plug that (in other extracts) we have seen Ted refer to as 'heater' when controlling the fan heater in his room was previously named 'blue' in the Echo's device configuration. The trouble Ted has with the command 'turn off blue' in line 5 is partly due to 'blue' being mistranscribed by Alexa's speech recognition system as 'moon'.

Figure 4: Anna waits for Ted to resolve a miscommunication with Alexa before proceeding with her part of their joint care routine (video)

<!-- image -->

When the extract begins, Alexa is playing music. Both times Ted summons Alexa at lines 2 and 10, Alexa pauses the music in response to the summons as the wake-light comes on. Notice how, just after Ted's redoes the summons 'Alexa::,' more emphatically in line 10, Anna also pauses her activity of unclipping the bed wheels and waits, glancing at the wake light until Ted re-does the command 'Turn off blu:e.' in line 14-this time successfully. Anna then resumes her activity and continues moving around the bed, pushing the heater out of the way as the music re-starts.

Figure 5: Ted assists Anna in using Alexa to brighten the lights in the room (video)

<!-- image -->

Note that since Anna must move the heater in any case, she could have continued with unclipping the bed wheels and turned it off with her foot as she put it away. Instead, Anna waits and monitors Ted's interaction with Alexa until he resolves the miscommunication and achieves his part in the-now shared-activity before she continues with her task.

## 3.3 Assistance with using the virtual assistant

Ted and Anna also share an activity in Figure 5, though this time Ted assists Anna. Just before the video clip starts, Anna has been squinting at a care plan she is about to read to Ted, but the lights in the room are dim (set to ten percent brightness). When Anna summons and instructs Alexa to 'turn lights ten percent' in line 2, the device's wake light comes on, but Alexa does not respond, and the lights remain dim until Ted intervenes.

After the 4.8 second gap in line 3 where Alexa does not respond, Anna glances up at the lights then turns to move towards Alexa just as Ted begins his first summons/command turn in lines 4-5. Here Ted has taken the initiative by formulating his instruction with an embedded correction [49] of Anna's prior turn: substituting 'a hundred percent' instead of 'ten percent'. Ted's action shows that he is monitoring Anna's activities here by offering assistance, and by treating her unsuccessful instruction/response sequence with Alexa as an opportunity to join the (thereby) shared task rather than letting Anna try again (as Anna did for Ted in Extract 4). Note also how Anna supports Ted's intervention despite him also then encountering trouble with Alexa. At first she glances at Ted while he produces the first part of the command at line 11 'turn lights', then Anna looks down, visibly disengaging from her interaction with Alexa. She remains standing, glancing up occasionally from the care plan while Ted goes through multiple rounds of unsuccessful summons/instruction and response sequences before successfully getting Alexa to turn up the lights, at which point Anna proceeds

```
1 TED: Alexa (1.0) turn off h- (0.9) ((coughs)) 2 (3.5)((Ted looks at Anna)) 3 ANN: He:ater, 4 (0.4) 5 TED: ((shaking head)) Hye_uh. 6 (1.0) 7 ANN: >D'you want me to do it?< 8 TED: *Yep. 9 (0.5) 10 ANN: Alexa, (0.4) turn off heater. 11 (2.4) 12 ALE: ((heater turns off)) Okay. 13 (0.3) 14 ANN: You're not feeling the cold so much no_w?
```

Figure 6: Anna checks that Ted wants assistance before helping him interact with Alexa (video)

```
1 TED: Alexa:, (1.2) turn (.) off (0.4) blue:. ((20 lines omitted)) 22 ANN: ALEXA:.= _ 23 TED: =NO GI- I- I- I'll do it >(I can do it)<. 24 (0.5) 25 ANN: °Alright°, 26 (0.7) 27 TED: (°Thanks°). 28 (3.8) 29 TED: ALEXA::? (0.9) TU::rn_(.) 0:ff _ 30 (0.3) blu:e.
```

with her next step in the process by reading the care plan out loud to Ted. This episode shows that Ted can also offer assistance to Anna: he shares activities by instructing Alexa to do something that facilitates the progress of Anna's current task. Anna's withdrawal from her interaction with Alexa and her waiting while Ted interacts (and often encounters trouble) with Alexa suggests that here, Anne is prioritizing Ted's initiative and task-sharing over the progressivity of the joint activity.

In this extract, Ted halts his turn at 'turn on', then looks up at Anna, who treats Ted's halt and sustained gaze as a word search by offering 'heater' as a candidate (other-repair) solution [37]. Ted's response 'Hye:uh' confirms that 'heater' was, indeed, the correct solution (at least this is how Anna treats it in her next turn), but he does not use this solution to re-do his summons/instruction to Alexa. Instead, he shakes and drops his head, facing away from the Alexa device. After offering Ted the opportunity to confirm that he wants her assistance with the task, which he does, Anna re-does the summons/command for him.

In some situations, however, Ted is not able to use Alexa. For example, when he has just come off the CPAP machine and his voice is too weak.

Anna saying 'You're not feeling the cold so much no:w?' in line 16 functions like the 'optimistic projections' [50], 'bright side tellings' [47, 87] or 'good news exits' [65] that are often used to 'balance out' bad news delivery sequences. In this case, the bad news or unwelcome event seems to be Ted's inability to use Alexa and take his part in their shared activity. This suggests that Anna is also monitoring Ted's ability to use Alexa partly as an indication of his wellbeing. While Anna is clearly monitoring Ted's interactions with Alexa and could intervene on Ted's behalf, there seems to be a relatively high threshold before she will offer him assistance with a task he can do using the CUI. In the examples above, when Ted encounters trouble with Alexa, Anna tends to wait and suspend her activities while Ted tries again, and in Figure 6 she also explicitly checks whether he wants help before instructing Alexa on Ted's behalf. Anna's careful checking before she helps Ted shows her orientation to the task as being owned by Ted.

Figure 7: Ted resists unsolicited assistance from Anna (video)

This analysis is underscored in Figure 7 where we see a deviant case of an unsolicited intervention by Anna. Ted's response highlights how this high threshold for recruitment and Anna offering assistance with one of 'Ted's tasks' is mutually maintained. Anna assists Ted in using Alexa after Ted has been unsuccessfully re-issuing summons/instructions to Alexa for almost a minute (omitted in the transcript below), but without checking that he wants help first.

When Ted first summons Alexa in line 1, Anna is crouching on the floor, organizing some homecare materials. After multiple failed summons/instructions from Ted, in line 22 Anna assists Ted by summoning Alexa herself while standing, gazing at the Echo device. As Anna produces this summons, Ted quickly and explicitly and sanctions her intervention, saying 'I can do it' in line 23, before re-doing his summons/instructions more loudly, and with more stress on each word. This kind of explicitness in the coordination of tasks within their shared activities is unusual, and here it hghlights how important it is to Ted to be able to take part in shared activities (using Alexa).

## 3.4 The tacit coordination of assistance in a smart homecare setting

The handing-over of initiative between Ted and Anna operates far more subtly than e.g., verbal requests for assistance [54]. Our final example in Figure 8 uses multimodal transcription conventions [67] to show how Ted and Anna combine tacit, embodied displays of attentiveness, availability, and formulations of 'trouble' [53] in ways that prioritize Ted's initiative, but without obliging him to struggle to do things for himself. The multimodal transcript starts at line 10 after 28 seconds of transcript (and repeated summons/command initiations) have been omitted from the transcript.

When Extract 8 begins, Ted is alone in the room and his voice sounds quiet and hoarse. Ted tries twice to summon Alexa in lines 1 and 3 but is unsuccessful. After each summons the wake light does not turn on. Ted then abandons the task of turning on the lights for 28 seconds and only resumes his attempts after Anna walks in the room. However, instead of directing an explicit request for help to Anna, Ted re-does his summons/command to Alexa in line 12-within earshot of Anna-then drops his head. Ted then remains visibly disengaged from his interaction with Alexa: neither looking towards the device, nor towards the ceiling lights, nor retrying his summons/command. Although she is turned away from Ted during his summons/command initiation, when Anna gets up immediately afterwards and turns, she glances first towards Ted, then to the ceiling and the (still off) lights, then towards Alexa. As Anna turns away from Ted and starts to walk towards Alexa, Ted lifts his head and tracks her movement into a position where he can monitor Anna's actions and Alexa's wake light. Ted's visible disengagement after initiating an interaction with Alexa functions as a resource for Anna to recognize Ted's need for assistance. She is able to provide assistance without leaving him struggling with Alexa or having to check before intervening bysummoning and instructing Alexa to turn on the lights in line 10. Once the lights turn on, Ted's acknowledgement 'Nice one Anna' in line 22 confirms her assumption that Ted had disengaged from the task and was recruiting Anna to operate Alexa on his behalf.

Figure 8: Ted's failure to summon Alexa gets Anna involved in his task of turning on the lights (video)

<!-- image -->

## 4 DISCUSSION/CONCLUSION

We can now briefly summarize our analysis and reflect on how these findings contribute to our understanding of disability, independence, and interdependence in the use of CUIs as assistive technologies.

## 4.1 Summary

Webegan by analyzing an instance of miscommunication involving multiple CUIs in Extract 1 that highlights how the user model of the solo individual user is designed into such systems. Extract 2 showed how a disabled person uses a CUI to accomplish tasks for themselves within a daily care routine e.g., setting and de-activating alarms and managing features of the environment such as lighting and heating. This specific use of the CUI fits with the model of the individualized user and, in this case, provides a straightforward form of technologically-enabled independence to do things for oneself. The limitations of that model also become clear as soon as the routine requires additional assistance, or, as in Extract 3 where Ted is wearing a breathing mask, when the user cannot speak. We can see the modularity and adaptability of the smart homecare system (including both technical and interactional components) in the configuration of the 'Echo Button' gaming device to summon assistance from a human care assistant, and from the hand-over between users interacting with the CUI as the mask comes off. Extracts 4 and 5 showed how the daily activities of a homecare routine can be shared between the disabled person, and how either can offer assistance to the other using the CUI to initiate and accomplish tasks within a shared activity structure. These two extracts also showed how the care assistant prioritizes the involvement of the disabled person in shared activities by e.g., waiting while they complete their interaction with the CUI before proceeding with the next step in the homecare routine. Extract 6, 7, and 8 showed how the humans in this smart homecare setting coordinate their displays of attention, availability, and needs for assistance in a way that supports and prioritizes the disabled person's independence embedded within an interdependent participation framework.

## 4.2 Models of ability and interdependence

This paper has focused on the shifts of agency and task-ownership between participants as they co-produce both the technical infrastructures and the interactional environment of the homecare setting. So what does this participation framework involving disabled people working with personal and virtual assistants tell us about how these systems could be designed? And what does it tell us about concepts of ability and disability, independence and interdependence that we could-or should-adopt when designing CUIs?

However, the elegant coordination of the care routine we have witnessed here between a disabled person, a personal assistant, and a virtual assistant point to opportunities to identify more empowering uses of smart homecare systems.

On the one hand, 'smart home' systems as they exist today do offer a useful and viable form of practical 'independence', and we see this model of independence in Ted's solo uses of Alexa to e.g., spend time alone while toileting (see Extract 2), providing opportunities to reclaim solitary time within a hectic care routine. On the other hand, if this model of independence is the main priority, CUI designers and the systems they build might lend themselves to agendas that prioritize cost-saving and utilitarian social policy-making.

Firstly, on a practical level, these analyses show how disabled people and care teams can adapt CUI devices (e.g., Ted's use of the Echo Buttons in Extract 3) to manage everyday care activities. These are relatively cheap, mass consumer devices, which are heavily discounted by large corporations such as Google and Amazon that have an interest in establishing new sales channels. As such, CUI design can support disabled people's independence by fostering and supporting this form of bottom-up innovation.

Thirdly, the ways that we see the virtual assistant being drawn into interaction as a resource for coordination points to the inadequacy of the single-user model, especially in the busy homecare environment (not to mention the inadequacy of this user model in everyday muti-party/family settings [74]). There is already a growing literature of empirical interactional research that points to more suitable user models. For example, studies of triadic and multiparty participation frameworks include virtual assistants and social robots in joint activities [57]. Similarly, research on distributed cognition and the extended mind provide theoretical starting points for studies of the role of CUIs in smart homecare [10]. Interactional research showing the limitations of simulation and role-play training and evaluation processes also highlight the flawed assumptions that often underpin the design of conversational agents [73, 88]. While CUI evaluation and design is a multi-disciplinary field, the conversation analytic methods used here provide an empirical approach that suits an expanded model of the user by focusing on the sociomateriality of interaction [31, 44] rather than by constructing the user as a reductive 'model of man' [28, 89].

Secondly, we observed the recruitment of assistance beyond the explicit, unmitigated summons/command format that is most often used to interact with a CUI. Indeed, our analyses show how a range of methods for recruiting and offering assistance [41] allow Ted to calibrate his displays of need and capacity, and for Anna to offer only as much assistance is currently necessary to provide interactional 'scaffolding' [76, 77] for Ted's participation in their shared tasks. As Bennett et al. [2018] suggest, a paradigm of interdependence in accessible technology design might provide for more abilitycentered or 'strengths-based' approaches [85] to designing CUIs within smart homecare systems.

Finally, this study suggests that CUI designers use concepts of ability, disability, and agency that acknowledge how 'we are all interdependent' [97], and recognize how the details of our interactions reveal our inherent interdependence with one another and with our environment. It shows how CUIs, integrated into deft, mundane homecare interactions, can prioritize the separable but interconnected 'relational autonomy' of social action that involves us all as 'assistants' for and with one another - personal, virtual and disabled alike [20].

## 4.3 Conclusion

For policymakers, the most salient conclusion from our findings is that virtual assistants may expand the affordances of a smart homecare setting but cannot, on their own, replace the work of human personal assistants. We have highlighted how CUIs work as part of a resourceful sociomaterial homecare environment, constituted by the skillful and adaptive interactional work of both disabled people and personal assistants. This suggests an alternative analytic starting point to essentializing uses of both medical and social models of disability that often start by specifying individual impairments, social roles, or institutional priorities. Instead, we suggest that a central empirical focus on interactional structure could help policymakers understand the inherent states of interdependence and contingency involved in everyday homecare work.

Finally, to inspire the design of future CUIs and smart homecare systems, we have identified, described, and shared some examples of how people can draw CUIs into the interactional structure of recruitments. Future studies could enable virtual 'assistants' and 'assistive' technologies worthy of that name: designed to join in with the prosocial human activities through which we seek and provide one another with assistance.

Although this study focuses specifically on a use case for CUIs involving disabled people and personal assistants, we also suggest that the findings and methods used here are transferable to other settings, and could have broader implications for the design of CUIs and both industry and academic research. Specifically, we have aimed to show how CA can provide valuable insights for the design and evaluation of CUIs and the ways they are used and adapted in everyday life. These methods allow us to track the shifting participation frameworks of social interaction, and can help to expand CUI designers' conceptualizations of the solo 'user' to include the wider sociomaterial environment.

## ACKNOWLEDGMENTS

Thanks to Crispin Coombs, Thorsten Gruber, Mark Harrison, Donald Hislop, and Elizabeth Stokoe for their work on the project that produced the data used for this study: Adept at Adaptation: Disability, AI, and Voice Technologies in Social Care Services, supported by a BA/Leverhulme Small Research Grant: SRG19/191529.

## REFERENCES

- [1] Morana Alač, Yelena Gluzman, Tiffany Aflatoun, Adil Bari, Buhang Jing, and German Mozqueda. 2020. How Everyday Interactions with Digital Voice Assistants Resist a Return to the Individual. Evental Aesthetics 9, 1 (2020), 51.
- [3] Saul Albert and Magnus Hamann. 2021. Putting wake words to bed: We speak wake words with systematically varied prosody, but CUIs don't listen. In CUI 2021 - 3rd Conference on Conversational User Interfaces (CUI '21) . Association for Computing Machinery, New York, NY, USA, 1-5. https://doi.org/10.1145/ 3469595.3469608
- [2] Saul Albert and J. P. De Ruiter. 2018. Improving Human Interaction Research through Ecological Grounding. Collabra: Psychology 4, 1 (July 2018), 24. https: //doi.org/10.1525/collabra.132
- [4] Saul Albert and J. P. de Ruiter. 2018. Repair: The Interface Between Interaction and Cognition. Topics in Cognitive Science 10, 2 (April 2018), 279-313. https: //doi.org/10.1111/tops.12339
- [6] Mandy M. Archibald and Alan Barnard. 2018. Futurism in nursing: Technology, robotics and the fundamentals of care. Journal of Clinical Nursing 27, 11-12 (2018), 2473-2480. https://doi.org/10.1111/jocn.14081 \_eprint: https://onlinelibrary.wiley.com/doi/pdf/10.1111/jocn.14081.
- [5] Norman Alm, John Todman, Leona Elder, and A. F. Newell. 1993. Computer Aided Conversation for Severely Physically Impaired Non-Speaking People. In Proceedings of the INTERACT '93 and CHI '93 Conference on Human Factors in Computing Systems (Amsterdam, The Netherlands) (CHI '93) . Association for Computing Machinery, New York, NY, USA, 236-241. https://doi.org/10.1145/ 169059.169187
- [7] Peter Auer, Angelika Bauer, and Ina Hörmeyer. 2020. How Can the 'Autonomous Speaker' Survive in Atypical Interaction? The Case of Anarthria and Aphasia. In Atypical Interaction: The Impact of Communicative Impairments within Everyday Talk , Ray Wilkinson, John P. Rae, and Gitte Rasmussen (Eds.). Springer International Publishing, Cham, 373-408. https://doi.org/10.1007/978-3-03028799-3\_13
- [8] R. Ayass. 2015. Doing data: The status of transcripts in Conversation Analysis. Discourse Studies 17, 5 (July 2015), 505-528. https://doi.org/10.1177/ 1461445615590717

- [9] Sandra Bedaf, Gert Jan Gelderblom, Luc de Witte, Dag Syrdal, Hagen Lehmann, Farshid Amirabdollahian, Kerstin Dautenhahn, and David Hewson. 2013. Selecting services for a service robot: Evaluating the problematic activities threatening the independence of elderly persons. In 2013 IEEE 13th International Conference on Rehabilitation Robotics (ICORR) . IEEE Explore, New York, 1-6. https://doi.org/10.1109/ICORR.2013.6650458 ISSN: 1945-7901.
- [11] Mark A. Blythe, Andrew F. Monk, and Kevin Doughty. 2005. Socially dependable design: The challenge of ageing populations for HCI. Interacting with Computers 17, 6 (Dec. 2005), 672-689. https://doi.org/10.1016/j.intcom.2005.09.005 Conference Name: Interacting with Computers.
- [10] Cynthia L. Bennett, Erin Brady, and Stacy M. Branham. 2018. Interdependence as a Frame for Assistive Technology Research and Design. In Proceedings of the 20th International ACM SIGACCESS Conference on Computers and Accessibility (ASSETS '18) . Association for Computing Machinery, New York, NY, USA, 161173. https://doi.org/10.1145/3234695.3236348
- [12] Dympna Casey, Heike Felzmann, Geoff Pegman, Christos Kouroupetroglou, Kathy Murphy, Adamantios Koumpis, and Sally Whelan. 2016. What People with Dementia Want: Designing MARIO an Acceptable Robot Companion. In Computers Helping People with Special Needs (Lecture Notes in Computer Science) , Klaus Miesenberger, Christian Bühler, and Petr Penaz (Eds.). Springer International Publishing, Cham, 318-325. https://doi.org/10.1007/978-3-31941264-1\_44
- [14] Victoria Cluley, Rachel Fyson, and Alison Pilnick. 2020. Theorising disability: a practical and representative ontology of learning disability. Disability &amp; Society 35, 2 (Feb. 2020), 235-257. https://doi.org/10.1080/09687599.2019.1632692 Publisher: Routledge \_eprint: https://doi.org/10.1080/09687599.2019.1632692.
- [13] Leigh Clark, Philip Doyle, Diego Garaialde, Emer Gilmartin, Stephan Schlögl, Jens Edlund, Matthew Aylett, João Cabral, Cosmin Munteanu, Justin Edwards, and Benjamin R Cowan. 2019. The State of Speech in HCI: Trends, Themes and Challenges. Interacting with Computers 31, 4 (June 2019), 349-371. https: //doi.org/10.1093/iwc/iwz016
- [15] Albert M. Cook and Jan Miller Polgar. 2015. Assistive technologies: principles and practice (fourth edition ed.). Elsevier/Mosby, St. Louis, Missouri.
- [17] Traci S. Curl and Paul Drew. 2008. Contingency and action: A comparison of two forms of requesting. Research on Language and Social Interaction 41, 2 (2008), 129-153.
- [16] Albert M. Cook, Jan Miller Polgar, and Nigel J. Livingston. 2010. Need- and Task-Based Design and Evaluation. In Design and Use of Assistive Technology: Social, Technical, Ethical, and Economic Challenges , Meeko Mitsuko K. Oishi, Ian M. Mitchell, and H. F. Machiel Van der Loos (Eds.). Springer, New York, NY, 41-48. https://doi.org/10.1007/978-1-4419-7031-2\_5
- [18] Guy Dewsbury, Karen Clarke, Dave Randall, Mark Rouncefield, and Ian Sommerville. 2004. The anti-social model of disability. Disability &amp; Society 19, 2 (March 2004), 145-158. https://doi.org/10.1080/0968759042000181776 Publisher: Routledge \_eprint: https://doi.org/10.1080/0968759042000181776.
- [20] Sandra Dowling, Val Williams, Joe Webb, Marina Gall, and Deborah Worrall. 2019. Managing relational autonomy in interactions: People with intellectual disabilities. Journal of Applied Research in Intellectual Disabilities 32, 5 (2019), 1058-1066. https://doi.org/10.1111/jar.12595 \_eprint: https://onlinelibrary.wiley.com/doi/pdf/10.1111/jar.12595.
- [19] Jemima Dooley. 2020. Involving people with experience of dementia in analysis of video recorded doctor-patient-carer interactions in care homes. International Journal of Social Research Methodology 25, 1 (Oct. 2020), 1-13. https://doi.org/10.1080/13645579.2020.1826648 Publisher: Routledge \_eprint: https://doi.org/10.1080/13645579.2020.1826648.
- [21] Amazon Echo. 2019. Amazon Alexa: Sharing is Caring. https://www.youtube. com/watch?v=225Wlg3pkdo
- [23] Carl Evans, Lindsey Brodie, and Juan Carlos Augusto. 2014. Requirements Engineering for Intelligent Environments. In 2014 International Conference on Intelligent Environments . IEEE, New York, 154-161. https://doi.org/10.1109/IE. 2014.30
- [22] Amazon Echo. 2019. Amazon Echo &amp; Alexa - Morning Ritual (60s). https: //www.youtube.com/watch?v=rHsO-rXrLLo
- [24] Gerhard Fischer. 2001. User Modeling in Human-Computer Interaction. User Modeling and User-Adapted Interaction 11, 1 (March 2001), 65-86. https://doi. org/10.1023/A:1011145532042
- [26] Simeon Floyd, Giovanni Rossi, and N.J. Enfield. 2020. Getting others to do things: A pragmatic typology of recruitments . Language Science Press, Berlin. https://doi.org/10.5281/ZENODO.4017493
- [25] Joel E. Fischer, Stuart Reeves, Martin Porcheron, and Rein Ove Sikveland. 2019. Progressivity for voice interface design. In Proceedings of the 1st International Conference on Conversational User Interfaces (CUI '19) . Association for Computing Machinery, New York, NY, USA, 1-8. https://doi.org/10.1145/3342775. 3342788
- [27] Álvaro García-Soler, David Facal, Unai Díaz-Orueta, Lucia Pigini, Lorenzo Blasi, and Renxi Qiu. 2018. Inclusion of service robots in the daily lives of frail older users: A step-by-step definition procedure on users' requirements. Archives of
20. Gerontology and Geriatrics 74 (Jan. 2018), 191-196. https://doi.org/10.1016/j. archger.2017.10.024
- [29] Ed Giesbrecht. 2013. Application of the Human Activity Assistive Technology model for occupational therapy research. Australian Occupational Therapy Journal 60, 4 (2013), 230-240. https://doi.org/10.1111/1440-1630.12054 arXiv:https://onlinelibrary.wiley.com/doi/pdf/10.1111/1440-1630.12054
- [28] Harold Garfinkel. 1967. Studies in ethnomethodology . Prentice-Hall, Englewood Cliffs, New Jersey.
- [30] Charles Goodwin. 1995. Co-constructing meaning in conversations with an aphasic man. Research on language and social interaction 28, 3 (1995), 233-260.
- [32] Charles Goodwin. 2004. A competent speaker who can't speak: The social life of aphasia. Journal of Linguistic Anthropology 14, 2 (2004), 151-170.
- [31] Charles Goodwin. 2000. Action and embodiment within situated human interaction. Journal of pragmatics 32, 10 (2000), 1489-1522. https://doi.org/10.1016/ S0378-2166(99)00096-X
- [33] Charles Goodwin. 2017. Co-Operative Action . Cambridge University Press, Cambridge. https://doi.org/10.1017/9781139016735
- [35] Jessica Harris, Maryanne Agnes Theobald, Susan J. Danby, Edward Reynolds, and Sean Rintel. 2012. 'What's going on here?' The pedagogy of a data analysis session. In Reshaping doctoral education: International Approaches and Pedagogies , Alison Lee and Susan J. Danby (Eds.). Routledge, London, 83-96. http://eprints. qut.edu.au/43733
- [34] P. Harmo, T. Taipalus, J. Knuuttila, J. Vallet, and A. Halme. 2005. Needs and solutions - home automation and service robots for the elderly and disabled. In 2005 IEEE/RSJ International Conference on Intelligent Robots and Systems . IEEE, New York, 3201-3206. https://doi.org/10.1109/IROS.2005.1545387 ISSN: 2153-0866.
- [36] Emanuel A. Schegloff Harvey Sacks and Gail Jefferson. 1974. A simplest systematics for the organization of turn-taking for conversation. Language 50, 4 (1974), 696-735. http://www.jstor.org/stable/412243
- [38] Patrick G. T. Healey, Jan P. de Ruiter, and Gregory J. Mills. 2018. Editors' Introduction: Miscommunication. Topics in Cognitive Science 10, 2 (April 2018), 264-278. https://doi.org/10.1111/tops.12340
- [37] Makoto Hayashi. 2003. Language and the body as resources for collaborative action: A study of word searches in Japanese conversation. Research on Language and Social Interaction 36, 2 (2003), 109-141. tex.ids= hayashi2003a.
- [39] James L. Heap. 1990. Applied ethnomethodology: Looking for the local rationality of reading activities. Human Studies 13, 1 (Jan. 1990), 39-72. https: //doi.org/10.1007/BF00143040
- [41] John Heritage. 2016. The Recruitment Matrix. Research on Language and Social Interaction 49, 1 (Jan. 2016), 27-31. https://doi.org/10.1080/08351813.2016. 1126440
- [40] Alexa Hepburn and Galina B Bolden. 2017. Transcribing for social research . Sage, London.
- [42] Marion A. Hersh and Michael A. Johnson. 2008. Disability and Assistive Technology Systems. In Assistive Technology for Visually Impaired and Blind People , Marion A. Hersh and Michael A. Johnson (Eds.). Springer, London, 1-50. https://doi.org/10.1007/978-1-84628-867-8\_1
- [44] Jon Hindmarsh and Nick Llewellyn. 2018. Video in Sociomaterial Investigations: A Solution to the Problem of Relevance for Organizational Research. Organizational Research Methods 21, 2 (2018), 412-437. https://doi.org/10.1177/ 1094428116657595 arXiv:https://doi.org/10.1177/1094428116657595
- [43] Marion A. Hersh, Michael A. Johnson, and David Keating (Eds.). 2008. Assistive technology for visually impaired and blind people . Springer, London. OCLC: ocm86168232.
- [45] Elliott M. Hoey and Kobin H. Kendrick. 2017. Conversation Analysis. In Research Methods in Psycholinguistics: A Practical Guide , A. M. B. de Groot and P.Hagoort (Eds.). WileyBlackwell, Hoboken, NJ, 151-173.
- [47] Elizabeth Holt. 1993. The structure of death announcements: Looking on the bright side of death. Text-Interdisciplinary Journal for the Study of Discourse 13, 2 (Nov. 1993), 189-212. https://doi.org/10.1515/text.1.1993.13.2.189
- [46] S. A. Holme, E. M. Kanny, M. R. Guthrie, and K. L. Johnson. 1997. The use of environmental control units by occupational therapists in spinal cord injury and disease services. The American Journal of Occupational Therapy: Official Publication of the American Occupational Therapy Association 51, 1 (Jan. 1997), 42-48. https://doi.org/10.5014/ajot.51.1.42
- [48] Bill Hughes and Kevin Paterson. 1997. The Social Model of Disability and the Disappearing Body: Towards a sociology of impairment. Disability &amp; Society 12, 3 (June 1997), 325-340. https://doi.org/10.1080/09687599727209 Publisher: Routledge \_eprint: https://doi.org/10.1080/09687599727209.
- [50] Gail Jefferson. 1988. On the sequential organization of troubles-talk in ordinary conversation. Social problems 35, 4 (1988), 418-441. https://doi.org/10.2307/ 800595
- [49] Gail Jefferson. 1987. On exposed and embedded correction in conversation. In Talk and social organization , G Button and J. R. E. Lee (Eds.). Multilingual Matters, Clevedon, 86-100.
- [51] Gail Jefferson, Jörg R. Bergmann, and Paul Drew. 2018. Repairing the broken surface of talk: managing problems in speaking, hearing, and understanding in

- conversation . Oxford University Press, New York, NY.
- [53] Kobin H. Kendrick. 2021. The 'Other' side of recruitment: Methods of assistance in social interaction. Journal of Pragmatics 178 (June 2021), 68-82. https: //doi.org/10.1016/j.pragma.2021.02.015
- [52] Reza Kachouie, Sima Sedighadeli, Rajiv Khosla, and Mei-Tai Chu. 2014. Socially Assistive Robots in Elderly Care: A Mixed-Method Systematic Literature Review. International Journal of Human-Computer Interaction 30, 5 (May 2014), 369393. https://doi.org/10.1080/10447318.2013.873278 Publisher: Taylor &amp; Francis \_eprint: https://doi.org/10.1080/10447318.2013.873278.
- [54] Kobin H. Kendrick and Paul Drew. 2016. Recruitment: Offers, Requests, and the Organization of Assistance in Interaction. Research on Language and Social Interaction 49, 1 (Jan. 2016), 1-19. https://doi.org/10.1080/08351813.2016.1126436 Publisher: Routledge \_eprint: https://doi.org/10.1080/08351813.2016.1126436.
- [56] Celia Kitzinger. 2012. Repair. In The Handbook of Conversation Analysis , Jack Sidnell and Tanya Stivers (Eds.). John Wiley &amp; Sons, Oxford, 229-256.
- [55] Andrew Kingston, Adelina Comas-Herrera, and Carol Jagger. 2018. Forecasting the care needs of the older population in England over the next 20 years: estimates from the Population Ageing and Care Simulation (PACSim) modelling study. The Lancet Public Health 3, 9 (Sept. 2018), e447-e455. https://doi.org/10.1016/S2468-2667(18)30118-X tex.ids= kingston2018a publisher: Elsevier.
- [57] Antonia Lina Krummheuer, Matthias Rehm, and Kasper Rodil. 2020. Triadic Human-Robot Interaction. Distributed Agency and Memory in Robot Assisted Interactions. In Companion of the 2020 ACM/IEEE International Conference on Human-Robot Interaction (HRI '20) . Association for Computing Machinery, New York, NY, USA, 317-319. https://doi.org/10.1145/3371382.3378269
- [59] Jessica N. Lester and Michelle O'Reilly. 2019. Establishing Quality in Applied Conversation Analysis Research. In Applied Conversation Analysis: Social Interaction in Institutional Settings . SAGE Publications, Inc, 2455 Teller Road, Thousand Oaks California 91320, 198-214. https://doi.org/10.4135/9781071802663
- [58] Ronald Leenes, Erica Palmerini, Bert-Jaap Koops, Andrea Bertolini, Pericle Salvini, and Federica Lucivero. 2017. Regulatory challenges of robotics: some guidelines for addressing legal and ethical issues. Law, Innovation and Technology 9, 1 (Jan. 2017), 1-44. https://doi.org/10.1080/17579961.2017.1304921 Publisher: Routledge \_eprint: https://doi.org/10.1080/17579961.2017.1304921.
- [60] David Maguire, Matthew Honeyman, Deborah Fenney, and Joni Jabbal. 2021. Shaping the future of digital technology in health and social care . Technical Report. The King's Fund. https://www.kingsfund.org.uk/publications/futuredigital-technology-health-social-care
- [62] Fabio Masina, Valeria Orso, Patrik Pluchino, Giulia Dainese, Stefania Volpato, Cristian Nelini, Daniela Mapelli, Anna Spagnolli, and Luciano Gamberini. 2020. Investigating the Accessibility of Voice Assistants With Impaired Users: Mixed Methods Study. Journal of Medical Internet Research 22, 9 (Sept. 2020), e18431. https://doi.org/10.2196/18431
- [61] Sergio Mascetti, Lorenzo Picinali, Andrea Gerino, Dragan Ahmetovic, and Cristian Bernareggi. 2016. Sonification of guidance data during road crossing for people with visual impairments or blindness. International Journal of HumanComputer Studies 85 (2016), 16-26. https://doi.org/10.1016/j.ijhcs.2015.08.003 Data Sonification and Sound Design in Interactive Systems.
- [63] Maja Matarić, Adriana Tapus, Carolee Winstein, and Jon Eriksson. 2009. Socially Assistive Robotics for Stroke and Mild TBI Rehabilitation. Advanced Technologies in Rehabilitation 145 (2009), 249-262. https://doi.org/10.3233/978-1-60750-0186-249 Publisher: IOS Press.
- [65] Douglas W. Maynard. 2003. Bad News, Good News: Conversational Order in Everyday Talk and Clinical Settings . University of Chicago Press, Chicago.
- [64] Maja J. Matarić and Brian Scassellati. 2016. Socially Assistive Robotics. In Springer Handbook of Robotics , Bruno Siciliano and Oussama Khatib (Eds.). Springer International Publishing, Cham, 1973-1994. https://doi.org/10.1007/ 978-3-319-32552-1\_73
- [66] Mara Mills and Meredith Whittaker. 2019. Disability, Bias, and AI . Technical Report. AI Now Institute Report. https://ainowinstitute.org/disabilitybiasai2019.pdf
- [68] Thomas P. Moran and R. J. Anderson. 1990. The workaday world as a paradigm for CSCW design. In Proceedings of the 1990 ACM conference on Computersupported cooperative work (CSCW '90) . Association for Computing Machinery, New York, NY, USA, 381-393. https://doi.org/10.1145/99332.99369
- [67] Lorenza Mondada. 2018. Multiple Temporalities of Language and Body in Interaction: Challenges for Transcribing Multimodality. Research on Language and Social Interaction 51, 1 (Jan. 2018), 85-106. https://doi.org/10.1080/08351813. 2018.1413878
- [69] Francisco Nunes, Nervo Verdezoto, Geraldine Fitzpatrick, Morten Kyng, Erik Grönvall, and Cristiano Storni. 2015. Self-Care Technologies in HCI: Trends, Tensions, and Opportunities. ACMTransactions on Computer-Human Interaction 22, 6 (Dec. 2015), 33:1-33:45. https://doi.org/10.1145/2803173
- [70] House of Lords. 2021. Ageing: Science, Technology and Healthy Living . Technical Report. House of Lords Science and Technology Select Committee. 132 pages. https://publications.parliament.uk/pa/ld5801/ldselect/ldsctech/183/183.pdf
- [71] Richard Pak, Sara J. Czaja, Joseph Sharit, Wendy A. Rogers, and Arthur D. Fisk. 2006. The role of spatial abilities and age in performance in an auditory computer navigation task. Computers in Human Behavior 24, 6 (2006), 3045-3051. https://doi.org/10.1016/j.chb.2008.05.010
- [73] Martin Porcheron, Joel E. Fischer, and Stuart Reeves. 2021. Pulling Back the Curtain on the Wizards of Oz. Proceedings of the ACM on Human-Computer Interaction 4, CSCW3 (Jan. 2021), 243:1-243:22. https://doi.org/10.1145/3432942
- [72] Anne Marie Piper and James D. Hollan. 2008. Supporting Medical Conversations between Deaf and Hearing Individuals with Tabletop Displays. In Proceedings of the 2008 ACM Conference on Computer Supported Cooperative Work (San Diego, CA, USA) (CSCW '08) . Association for Computing Machinery, New York, NY, USA, 147-156. https://doi.org/10.1145/1460563.1460587
- [74] Martin Porcheron, Joel E. Fischer, Stuart Reeves, and Sarah Sharples. 2018. Voice Interfaces in Everyday Life. In Proceedings of the 2018 CHI Conference on Human Factors in Computing Systems (Montreal QC, Canada) (CHI '18) . Association for Computing Machinery, New York, NY, USA, 1-12. https://doi.org/10.1145/ 3173574.3174214
- [76] Julie Radford, Paula Bosanquet, Rob Webster, and Peter Blatchford. 2015. Scaffolding learning for independence: Clarifying teacher and teaching assistant roles for children with special educational needs. Learning and Instruction 36 (April 2015), 1-10. https://doi.org/10.1016/j.learninstruc.2014.10.005
- [75] Tony Prescott and Praminda Caleb-Solly. 2017. Robotics in Social Care: A Connected Care EcoSystem for Independent Living . UKRAS White Papers. EPSRC UK-RAS Network. https://doi.org/10.31256/WP2017.3 Edition: 1 Series: UKRAS White Papers.
- [77] Julie Radford, Paula Bosanquet, Rob Webster, Peter Blatchford, and Christine Rubie-Davies. 2014. Fostering learner independence through heuristic scaffolding: A valuable role for teaching assistants. International Journal of Educational Research 63 (Jan. 2014), 116-126. https://doi.org/10.1016/j.ijer.2013.02.010
- [79] Pericle Salvini. 2015. On Ethical, Legal and Social Issues of Care Robots. In Intelligent Assistive Robots: Recent Advances in Assistive Robotics for Everyday Activities , Samer Mohammed, Juan C. Moreno, Kyoungchul Kong, and Yacine Amirat (Eds.). Springer International Publishing, Cham, 431-445. https://doi. org/10.1007/978-3-319-12922-8\_17
- [78] Giovanni Rossi, Mark Dingemanse, Simeon Floyd, Julija Baranova, Joe Blythe, Kobin H. Kendrick, Jörg Zinken, and N. J. Enfield. 2023. Shared cross-cultural principles underlie human prosocial behavior at the smallest scale | Scientific Reports. Scientific Reports 13, 1 (April 2023), 6057. https://doi.org/10.1038/ s41598-023-30580-5
- [80] Emanuel A Schegloff. 1968. Sequencing in Conversational Openings. American Anthropologist 70, 6 (Dec. 1968), 1075-1095. https://doi.org/10.1525/aa.1968.70. 6.02a00030
- [82] Marcia J. Scherer. 2020. It is time for the biopsychosocialtech model. Disability and Rehabilitation: Assistive Technology 15, 4 (May 2020), 363-364. https: //doi.org/10.1080/17483107.2020.1752319 Publisher: Taylor &amp; Francis \_eprint: https://doi.org/10.1080/17483107.2020.1752319.
- [81] Emanuel A Schegloff, Gail Jefferson, and Harvey Sacks. 1977. The Preference for Self-Correction in the Organization of Repair in Conversation. Language 53, 2 (1977), 361-382. https://doi.org/10.2307/413107
- [83] Torn Shakespeare and Nicholas Watson. 2001. The social model of disability: An outdated ideology? In Exploring Theories and Expanding Methodologies: Where we are and where we need to go , Sharon N. Barnartt and Barbara M. Altman (Eds.). Research in Social Science and Disability, Vol. 2. Emerald Group Publishing Limited, Bingley, 9-28. https://doi.org/10.1016/S1479-3547(01)80018-X
- [85] Karrie A. Shogren, Michael L. Wehmeyer, Jonathan Martinis, and Peter Blanck. 2018. Strengths-based frameworks for understanding disability and support needs. In Supported decision-making: Theory, research, and practice to enhance self-determination and quality of life . Cambridge University Press, Cambridge, 27-96. tex.collection: Cambridge Disability Law and Policy Series.
- [84] Perry Share and John Pender. 2018. Preparing for a Robot Future? Social Professions, Social Robotics and the Challenges Ahead. Irish Journal of Applied Social Studies 18, 1 (March 2018), 45-62. https://doi.org/10.21427/D7472M
- [86] Jack Sidnell and Tanya Stivers. 2012. The Handbook of Conversation Analysis . John Wiley &amp; Sons, Oxford.
- [88] Elizabeth Stokoe, Rein Ove Sikveland, Saul Albert, Magnus Hamann, and William Housley. 2020. Can humans simulate talking like other humans? Comparing simulated clients to real customers in service inquiries. Discourse Studies 22, 1 (Feb. 2020), 87-109. https://doi.org/10.1177/1461445619887537 tex.ids= stokoe2020a publisher: SAGE Publications.
- [87] Tanya Stivers and Stefan Timmermans. 2017. Always Look on the Bright Side of Life: Making Bad News Bivalent. Research on Language and Social Interaction 50, 4 (2017), 404-418. https://doi.org/10.1080/08351813.2017.1375804 arXiv:https://doi.org/10.1080/08351813.2017.1375804
- [89] Lucy Suchman. 2007. Human-machine reconfigurations: Plans and situated actions . Cambridge University Press, Cambridge.
- [90] Alistair Sutcliffe, Stephen Fickas, and McKay Moore Sohlberg. 2006. PC-RE: a method for personal and contextual requirements engineering with some experience. Requirements Engineering 11, 3 (June 2006), 157-173. https://doi.

[org/10.1007/s00766-006-0030-0](https://doi.org/10.1007/s00766-006-0030-0)

- [92] Claire Tregaskis. 2002. Social Model Theory: The story so far. Disability &amp; Society 17, 4 (June 2002), 457-470. https://doi.org/10.1080/09687590220140377 Publisher: Routledge \_eprint: https://doi.org/10.1080/09687590220140377.
- [91] Eric Topol. 2019. The Topol Review: Preparing the healthcare workforce to deliver the digital future . Technical Report. Health Education England, London. 103 pages. https://topol.hee.nhs.uk/wp-content/uploads/HEE-Topol-Review-2019. pdf
- [93] Outi Tuisku, Satu Pekkarinen, Lea Hennala, and Helinä Melkas. 2018. 'Robots do not replace a nurse with a beating heart': The publicity around a robotic innovation in elderly care. Information Technology &amp; People 32, 1 (Jan. 2018), 4767. https://doi.org/10.1108/ITP-06-2018-0277 Publisher: Emerald Publishing Limited.
- [95] Glen W. White, Jamie Lloyd Simpson, Chiaki Gonda, Craig Ravesloot, and Zach Coble. 2010. Moving from Independence to Interdependence: A Conceptual Model for Better Understanding Community Participation of Centers for Independent Living Consumers. Journal of Disability Policy Studies 20, 4 (March 2010), 233-240. https://doi.org/10.1177/1044207309350561 Publisher: SAGE Publications Inc.
- [94] Phil Turner. 2005. Affordance as context. Interacting with Computers 17, 6 (Dec. 2005), 787-800. https://doi.org/10.1016/j.intcom.2005.04.003
- [96] Ray Wilkinson. 2019. Atypical Interaction: Conversation Analysis and Communicative Impairments. Research on Language and Social Interaction 52, 3 (July 2019), 281-299. https://doi.org/10.1080/08351813.2019.1631045 Publisher: Routledge \_eprint: https://doi.org/10.1080/08351813.2019.1631045.
- [98] James Wright. 2020. Technology in social care: review of the UK Policy landscape . Technical Report. Centre for Care. http://circle.group.shef.ac.uk/2020/10/27/ scpaper-tech-in-socialcare/ Section: Sustainable Care.
- [97] Val Williams. 2011. Disability and discourse: analysing inclusive conversation with people with intellectual disabilities . Wiley, Hoboken, N.J.
- [99] James Wright. 2021. The Alexafication of Adult Social Care: Virtual Assistants and the Changing Role of Local Government in England. International Journal of Environmental Research and Public Health 18, 2 (Jan. 2021), 812. https:// doi.org/10.3390/ijerph18020812 Number: 2 Publisher: Multidisciplinary Digital Publishing Institute.
- [101] Gary Chan Kok Yew. 2021. Trust in and Ethical Design of Carebots: The Case for Ethics of Care. International Journal of Social Robotics 13, 4 (July 2021), 629-645. https://doi.org/10.1007/s12369-020-00653-w
- [100] James Wright. 2023. Robots won't save Japan: an ethnography of eldercare automation . ILR Press, an imprint of Cornell University Press, Ithaca.

Received 26 February 2023