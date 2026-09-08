---
stem: 2024_Brown-Bu-Mandel_Trash-Motion-Emergent
pdf_path: papers\2024_Brown-Bu-Mandel_Trash-Motion-Emergent.pdf
source_path: sources\2024_Brown-Bu-Mandel_Trash-Motion-Emergent.md
source_hash: 0ae143b075e738342bfaa1f38d656ee07a151ff18b9ba28caea8b89bb84b66c7
parsed_with: docling
parsed_at: '2026-09-08T10:03:47+00:00'
warnings: []
record_id: paper:2024_Brown-Bu-Mandel_Trash-Motion-Emergent
---
.

<!-- image -->

<!-- image -->

.

.

<!-- image -->

<!-- image -->

<!-- image -->

## [Latest updates: hps://dl.acm.org/doi/10.1145/3613904.3642610](https://dl.acm.org/doi/10.1145/3613904.3642610)

<!-- image -->

.

.

.

.

.

.

.

.

.

.

.

.

.

RESEARCH-ARTICLE

## Trash in Motion: Emergent Interactions with a Robotic Trashcan

[BARRY BROWN , Stockholm University, Stockholm, Stockholm, Sweden](https://dl.acm.org/institution/60028378)

[FANJUN BU , Cornell Tech, New York, NY, United States](https://dl.acm.org/institution/60104837)

[ILAN MANDEL](https://dl.acm.org/profile/99659320416)

[, Cornell Tech, New York, NY, United States](https://dl.acm.org/institution/60104837)

[WENDY JU , Cornell Tech, New York, NY, United States](https://dl.acm.org/institution/60104837)

[Open Access Support provided by:](https://libraries.acm.org/acmopen)

[Stockholm University](https://dl.acm.org/institution/60028378)

[Cornell Tech](https://dl.acm.org/institution/60104837)

.

.

.

.

.

.

PDF Download 3613904.3642610.pdf 08 April 2026 Total Citations: 24 Total Downloads: 8590

.

.

Published: 11 May 2024

[Citation in BibTeX format](https://dl.acm.org/doi/10.1145/3613904.3642610#download-citation)

CHI '24: CHI Conference on Human Factors in Computing Systems May 11 - 16, 2024

HI, Honolulu, USA

Conference Sponsors:

[SIGCHI](https://dl.acm.org/sig/sigchi)

<!-- image -->

## Trash in Motion: Emergent Interactions with a Robotic Trashcan

## [Barry Brown](https://orcid.org/0000-0002-9710-6607)

barry.brown@me.com Stockholms Universitet Stockholm, Sweden University of Copenhagen Copenhagen, Denmark

## [Ilan Mandel](https://orcid.org/0000-0002-8569-5176)

Jacobs Technion-Cornell Institute at Cornell Tech New York, New York, USA im334@cornell.edu

## [Fanjun Bu](https://orcid.org/0000-0002-9953-7347)

Jacobs Technion-Cornell Institute at Cornell Tech New York, New York, USA fb266@cornell.edu

Wendy Ju Jacobs Technion-Cornell Institute at Cornell Tech New York, New York, USA wendyju@cornell.edu

Figure 1: Two robotic trashcans (one recycling and one landfll) moving around the square during our one-week study

<!-- image -->

## ABSTRACT

The introduction of robots in public spaces raises many questions concerning emergent interactions with robots. In this paper, we use video analysis to study two robotic trashcans deployed in a busy city square. We focus on the movement-based practices that emerged between the robot, the robot operators, and the inhabitants of the square. These practices spanned ways of attracting the robot and disposing of trash, the robot 'asking' for trash, 'demonstrations' by those in the square, as well as passersby in the square navigating around and in coordination with the robots. In discussion, we document these 'spontaneous simple sequential systematics' - interactions that were systematic (they had an order), sequential (they had parts that happened one at a time), simple (in that they could be understood and copied by an observer) and spontaneous (they could be produced with no prompting or training). Building on this we discuss how we might think of robotic motion as a design space, along with HCI contributions to urban robotics.

Permission to make digital or hard copies of all or part of this work for personal or classroom use is granted without fee provided that copies are not made or distributed for proft or commercial advantage and that copies bear this notice and the full citation on the frst page. Copyrights for components of this work owned by others than the author(s) must be honored. Abstracting with credit is permitted. To copy otherwise, or republish, to post on servers or to redistribute to lists, requires prior specifc permission and/or a fee. Request permissions from permissions@acm.org.

CHI '24, May 11-16, 2024, Honolulu, HI, USA

© 2024 Copyright held by the owner/author(s). Publication rights licensed to ACM. ACM ISBN 979-8-4007-0330-0/24/05 https://doi.org/10.1145/3613904.3642610

## CCS CONCEPTS

- Human-centered computing → Field studies .

## KEYWORDS

Public interaction, human-robot interaction, ethnomethodology

## ACM Reference Format:

Barry Brown, Fanjun Bu, Ilan Mandel, and Wendy Ju. 2024. Trash in Motion: Emergent Interactions with a Robotic Trashcan. In Proceedings of the CHI Conference on Human Factors in Computing Systems (CHI '24), May 1116, 2024, Honolulu, HI, USA. ACM, New York, NY, USA, 17 pages. https: //doi.org/10.1145/3613904.3642610

## 1 INTRODUCTION

Recent advances have made autonomous robots feasible and usable in many new situations. This has enabled the introduction of robots to a number of non-controlled public-focused situations such as city streets, urban sidewalks, and city squares [42]. These developments raise a host of interesting questions about how ordinary city inhabitants can interact with, understand, or use robots where there is little or no training information given about their use and behaviour. In this paper, we document our experiments with introducing a robotic trashcan to a public square, and how city inhabitants made use of that trashcan in diferent ways. Over fve days, we deployed two robot trashcans (Figure 1) built around conventional 32-gallon trashcans, augmented with cameras and a hoverboard base that allowed the trashcan to move around a public space. The trashcan was stable enough to move quickly around a city square, across pavement bumps and holes, and collect garbage through an open top. The trashcan was controlled independently by two 'wizard' [43] operators who could control where the trashcan moved in the square. Our study participants (and sometimes users of the trashcan) were those who made use of the square, including passersby walking through, local businesses, their customers, and those who chose to sit and eat or drink there. As a busy urban space, this square provided a rich environment in which to test robotic interactions--not only how unacquainted individuals interact with a robot, but also how an urban space is changed by the introduction of a robot [65]. Having a 'wizard' setup [43, 59] allowed us to explore how a robot's behaviour could react and change from interactions over time, as well as the likely 'best possible' performance that a robot could achieve, in terms of safe and efcient movement and reaction to user behaviours.

Our discussion documents some lessons for robot design from this work. Drawing on ethnomethodological and conversation analytic work on robot interaction [54, 72], we frame these interactions as 'Spontaneous Simple Sequential Systematics'-interactions that were Systematic (they had an order), Sequential (they had parts that happened one at a time), Simple (in that they could be understood and copied by an observer) and Spontaneous (they could be produced with no prompting or training). We build on this to discuss how we might design for this form of activity, and how HCI researchers could contribute to the challenge of designing 'SSSS'

Building on recent interest in how robots communicate in public space [11, 33, 52], we focus on the question how do people respond to non-anthropomorphic robots deployed in public spaces? Focusing on this question leads us to examine the emergent forms of humanrobot communication that arose in the trial. The robot operators could rotate and move the trashcan around the square, with a highresolution 360-degree view of the square from onboard cameras. This supported the development of some basic sequential patterns of interaction between the robot, its operations and its users-the trashcan could move in response to users' movements, and vice versa . Users would, for example, 'catch and release'-they would beckon the robot holding up some garbage and then release garbage into the trashcan when it was close enough. In contrast, the robot operators developed an 'ask and receive' behaviour where they would wait at the side of a user who had fnished eating, or had some trash, prompting users to put trash into the trashcan in response. A third systematic pattern involved a 'driveby use' where the trashcan was used by a passerby who changed their trajectory to intercept a moving trashcan, or alternatively made use of the trashcan moving past them while they remained seated. As a moving object in the square, we also observed how users and operators had to manage their motion collaboratively, and in particular how they managed their future trajectories through navigating collectively with the trashcan around objects in the square, such as by yielding to each other. While a moving trashcan is a somewhat unusual object in a city square, passersby who came across the trashcan for the frst time successfully managed their movement around the trashcan in diferent ways. Lastly, we describe how users in the square used 'demonstrations' of their robot trashcan use as a way of both playing with the trashcan and instructing others both in the square and remote about the uses of such a system.

robots. Lastly, refecting on the use of the robot in a busy urban space raises some questions about how a robotic urban space might take shape, in particular, how robots might help or hinder visions of convivial public space [24, 78]. We conclude by discussing the role of waste disposal and how the introduction of 'trashbots' could ofer both the possibility of reducing littering and ways of supporting playful interactions [6, 38] in public spaces.

## 2 BACKGROUND

In this study, we deployed two trash barrel robots to an urban setting to facilitate the collection of trash, building upon earlier research projects studying how people interact with trash-related robots [19, 21, 53, 70, 80, 82]. Having a study that takes place in an urban public setting is particularly salient because of recent trends towards urban robotics [42, 44]. Urban robotics include not only autonomous cars but also delivery robots, security robots, entertainment drones, or companion robots [79]. As While et al. [77] note, urban robotics raise "questions of whether humans and robotics can coexist in the public realm and what sorts of infrastructures and regulations might be required to enable experimental robotic-human symbiosis and co-evolution."

## 2.1 Robots in public space

While human robotics researchers have been striving to conduct robot studies "in the wild," their arguments for these often focus on the public environments as being the "ultimate test" for robots-to understand how they will be used [62], what people consider to be normal or breaches of expectation [76], or what features will lead people to engage with robots more [48], outside of the confnes of the lab.

Consider, for example, studies of delivery robots: Weinberg et al. [75] observed the results of a delivery robot pilot program in Pittsburgh and found that some people found them cute while others were openly antagonistic. From an urban robotics standpoint, the critical interactions that govern the reception of the robots are not those of the vendors who are putting their pizzas in the robot or the users who receive pizzas: it is the many casual interactions the robots have along the way. This highlights how these emergent interactions are critical to study to understand how urban robots are integrated into the community fabric. Similarly, Dobrosovestnova et al's [13] study of delivery robots in Tahlin describes how passersby help robots stuck in the snow, arguing for the importance of the 'kawaii' nature of these delivery robots to encourage passersby to help them. This 'coexistance' between robots and others in a public space was also examined by Babel [2], who looked at interactions with an airport-based cleaning robot. This study

The urban robotics perspective brings a diferent perspective to human-robot interaction, a focus on the "emerging properties" that result from the interaction between system elements [65]. This perspective subverts the testing of hypotheses, the profling of user population behaviors or the qualities of robots ft or unft for the urban environment. It replaces this with a view that center the discovery of unintended forms of interactions that robots might have with bystanders or passersby. In this view, the naive and untrained responses of people incidentally interacting with the technology are the most important to understand [12].

described a number of interesting emergent interactions, such as noticing and evading the robot.

Clearly, the ways that urban robots are taken up-or rejectedhave much to do with larger factors that undergird the reasons and context for urban robot deployment. While et al. [77], for example, compare case studies of robots in urban environments in San Francisco, Tokyo, and Dubai. The diversity in the rationales for robotic application refects diferences in the economic, social, and political contexts in each of these urban centers, which, fascinatingly, manifest themselves in the attitudes and responses that citizens have to the robots themselves.

## 2.2 Interaction through Motion

One interesting aspect of both Yang et al. [82] and Yamaji et al. [80]'s trash bin robots was that they communicated with passersby primarily through motion rather than sound or speech. Ju [33] notes that using motion as a communication modality keeps robot interaction in people's attentional periphery. "Dialogue-based interactions tend to be focal; it is difcult to carry on more than one dialogue at a time. The implicit interactions we have been exploring, however, make only occasional bids for attention. This makes them more appropriate for placement in everyday environments."

Communication through movement has been a central part of ethnomethodological and conversation analysis (jointly referred to as 'EMCA') work on robotics, which we drew upon for this paper. The EMCA has a distinctive perspective on social activity in that it focuses attention on the publicly available aspects of interaction, such as motion, and disavows discussion of inward phenomena such as mental states. Early EMCA work on human robot interaction includes research on interaction with tour guide robots [81], Kuzuoka and colleagues explorations of mutual orientation between humans and robots [34], and Pitsch's work on pauses and restarts in robot interaction [56]. More recently Pelikan's and Hofstetter have explored how delays can afect human robot interaction [54], and Tuncer et al [72] have used the concept of recipient design

Fischer et al. [20] analyzed the interactions that people had with Yang et al. [82]'s trashbarrel robot deployed at a university dining areas. People who wanted to interact with the robot actively displayed their willingness to interact by body torque, eye gaze, waving, gesturing, and verbal utterances to interact with the robot. In turn, important from the perspective of robot designers who are looking to pick up cues predicting interaction availability, users signaled their unwillingness to interact by withholding social signals, for example, by avoiding eye gaze and averting body orientation. Interestingly Fischer et al [ibid] also noted discrepancies in the interaction between groups of people and people who were alone: "None of the people alone at their table smiled, laughed, waved ostensibly or talked at the robot in ways similar to behaviors exhibited by people in company." [8]. This project, then, also suggests that grouping is an important factor in the interaction but further suggests that the demonstration to others in the public interaction with the robot is critical to the emergence of social interaction patterns. From that perspective, urban settings are a good place to explore social interactions with robots, because of the abundance of opportunities for social interaction.

to understand how humans make assessments about the interactional competence (or not) of a robot. EMCA furnished much of our analytic approach here, in terms of how we conducted our video analysis but also our theoretical framing for understanding how interaction unfolded. We will return to this in our discussion when we introduce our "Spontaneous Simple Sequential Systematics" framework.

## 2.3 The Sociology of Trash

The use of urban robots to aid with trash collection also brings the role of trash in the city into focus. As Douglas [14] famously observed, dirt, waste, and trash are socially constructed as 'matter out of place'. Culture dominates both what is considered waste and the ways waste is handled at individual and societal scales. Whereas 'Germans happily sort 65 percent of their waste into an array of color-coded bins' the United States only recycles 35 percent of its waste [17]. In New York City, 'the public at large doesn't generally understand that garbage, as a category of material and as a management challenge, is handled by diferent entities depending on its genesis and where it accumulates' [50]. As journalist and photographer Jacob Riis noted, sanitation and waste removal are necessary for any functioning public space [60]. People rarely notice the infrastructure of waste removal until it breaks down [49]. In the 1890s, when the city was fnally rid of shin-deep muck [49] Riis wrote 'It was Colonel Waring's broom that frst let light into the slum... His broom saved more lives in the crowded tenements than a squad of doctors. It did more: it swept the cobwebs out of our civic brain and conscience' [60].

In recent years, the practice of trash removal has been a topic of renewed interest with growing concerns over circularity, waste, and sustainability. Building on Leigh Star's discussions of infrastructure [68], Thieme et al. [70] refect upon social persuasion around sustainability, as part of a series of arguments around the sustainability of smart cities [32], and the balance of responsibilities between individuals, states, civic bodies, and politics more broadly [15, 61]. Since this work understandably focuses mainly on questions of trash and sustainability, less attention has been given to more fne-grained practices of trash disposal and management. Within sociology, work such as Evans [18] documents the ways in which household waste is routinized, such as what can be 'thrown away' without being wasteful. In terms of waste in public, urban sociology work, such as Duneier's classic Sidewalk [16], documents the role of those who live on the street in managing or at least dealing with various types of garbage, and conficts over what actually is 'matter out of place' in an urban space. Perry, Juhlin, and Normak similarly document the collaborative public practices around trash [55]. In their video analysis of a city park, they describe how trash is collected at the end of eating together and disposed of by one party member, the ways in which multiple people use a trash can by taking turns, and how children come to be instructed in the proper disposal of waste. This work underlines that there is social understanding of our joint responsibility and interest in waste disposal.

## 3 TRIAL

## 3.1 Method

We designed a trial to study robot interaction in public by "submitting [social robots'] interactions with humans outside the laboratory to detailed observation and analytical scrutiny" [76]. Using a "Wizard of Oz" deployment gave us a powerful tool for answering questions like 'how do people respond to non-anthropomorphic robots deployed in public spaces?,' 'How do people respond to this motion?,' and 'How do human Wizards respond to, or improvise with, common participant responses?' [43, 83] Following this work, our approach then was to create as realistic a deployment situation as possible, with no consideration for how an actual robot could make sense of interactions and the space, and instead use a wizard approach to focus on the varied human-robot interactions that emerged.

## 3.2 Apparatus/Robot

We developed two trash barrel robots that could be remotely controlled, broadcasting and recording video from the viewpoint of the trash robots. The robots were designed to be similar to the trash barrel robot deployed by Yang et al. and used in feld experiments at Stanford University [82]. Some diferences in our implementation included a more robust hoverboard base that provided more power and speed, which allowed the robots to move over more varied terrain. This allowed us to explore a trial in a less controlled environment, in this case a public open-air city square. Having a 360 degree camera mounted on the top of the trash robot also made it clearer that the robot could perceive the environment, and provided a wider feld of view than in the previous study. The trial also consisted of two trash robots-one recycling and one landfll. As with Yang et al's work, our robots have some key diferences from earlier public interaction trials (robots such as Roboceptionist, Ace, or Octavia [25, 48, 76]) in that our trash barrel robots are clearly not humanoid and do not gaze or speak to people; the interaction, then, is primed only by the robot's form and movement.

Visually, the trash barrel robots are almost indistinguishable from standard trash barrels on dollies pushed around by janitors on the street. Two salient features that separate the robot from the standard trash barrel are the hoverboard-powered dolly, the onboard camera, and the ability of the robot to move without visible human assistance. The robots' color matched the standard municipal coloring scheme in the U.S. to represent the robots' roles: a blue barrel was used for recycling, and a gray barrel was used for landfll. The blue barrel was also decorated with vinyl recycling decals to reinforce the recycling concept.

## 3.3 Instrumentation

Each trash barrel robot was equipped with a 360 degree camera at the top front edge of the barrel. These cameras captured both audio and 360 degree video footage during every deployment. Since there were two robots deployed at the same time, the cameras collectively provided both a frst-person view and a third-person view of every encounter. In addition, we also mounted two GoPro cameras on the exterior wall of a cafe shop located at the southeast corner of the plaza. These two GoPro cameras overlooked the entire square. The footage from 360 degree cameras was synchronized and exported in equirectangular projection for video coding. Through software, the video could toggle between 360 view mode (no distortion, pan and drag to change view angle) and equirectangular mode (like a world map, distort the 360 degree video to show entire 360 degree images in 2D).

## 3.4 Deployment

The robots were trialed for one-hour-long periods on fve diferent days, making a total of fve hours of deployment. Since data recording in public spaces is allowed in the U.S., no signs were provided in the square to avoid priming. There were two wizards on-site every day, each controlling a robot individually. The wizards sat at a table on the edge of the square, controlling the robots at a distance. They were encouraged to communicate with each other during deployment regarding their controlling plans and assist each other in case of blind spots.

## 3.5 Wizard instructions

Each day, two members of the research lab (including associated visiting researchers), with backgrounds in computer science and information science, teleoperated the robots during the deployment as wizards. The wizards were told that the robots should stay closely together during the deployments so that people were aware of the diferent purposes of the robots. Again, in contrast to the constrained instructions given to the wizards in [82], we attempted to have more dynamic control of the robot. We gave only brief instructions to the wizards, asking them to interact 'naturally' with the users in the square, and gave them the fexibility to choose to operate the trashcan as they see ft.

## 3.6 Authorization and Consent

The study protocol was approved under the Cornell University IRB#1806008080; in this protocol, elements of informed consent are altered, based on the fnding that the research involves no more than minimal risk to the participants, that the research could not practicably be carried out without the alteration, and that alteration will not adversely afect the rights and welfare of participants (see [73], §46.116(e)(2)). As much as possible, where people were recorded actively interacting with the robot, we obtained consent post-interaction, and also asked for permission to use images and footage they are featured in.

The consent and interview process occurred post-interaction. The researcher waited for a clear signal of termination of interaction activities (e.g. the robots drove away, the participants walked away, etc.) before approaching and instrumenting consent procedure to avoid any potential interruption to the interaction. To avoid contaminating interactions with other participants, researchers were recommended not to approach the participants immediately after the interaction, with the exception when participants were leaving the study area, to avoid revealing the researcher's afliation with the robots to other bystanders. Often, then, there was a period of interaction with robots, and then another period where many people who were co-present were interviewed, although separately. This said, asking for consent in this way does introduce some limitations in to the experiment. While we kept our presence in the square outwith the robots themselves to a minimum, those in the square could potentially connect the author asking for consent with the robots, and this could potentially afect the 'illusion' we aimed for.

Consent was documented through recorded verbal assent based on [73] §46.117(c)(1), as signed consent would be the only record linking the subject and the research, and the principal risk would be potential harm resulting from a breach of confdentiality, with the research itself presenting no more than minimal risk. Consistent with feld research conducted in public spaces, we did not ask for consent from passersby who were only incidentally involved in the study, even though it could be argued that the use of the unseen "wizard" operators constitutes deception. (A deeper ethical discussion of such studies is found in [67].) We also had written permission from the business improvement district that manages the location to conduct the experiment in that space, as well as a certifcate of insurance to cover damages that might inadvertently result from the deployment.

## 4 METHOD AND ANALYSIS

## 4.1 Data

We were focused on the developing interactions between the humans in the square, the trashcan robots, and the robot operators. Using the video recordings of the square overall, and from the trashcans themselves, we were able to build up a data corpus of over 5 hours of video from the trial. Our data involved recordings of the trashcan's interactions in the square, with two video recordings from the perspective of each robot, and one video recording overall of the square. As we have described, the trashcan users were not 'primed' by being interviewed in advance, asked for consent, or provided information in advance, beyond what they observed themselves from being in the square. This allowed us to treat these fve hours as a somewhat naturalistic recording of interactions during the trial.

## 4.2 Approach

In terms of analyzing our data, our approach was informed by the longstanding tradition of work within HCI and CSCW that uses video to look closely at the moment-by-moment interaction with technology [7, 10, 30]. We also drew heavily on ethnomethodology and conversation analysis as an approach to understanding human interaction. [47] This work has pioneered looking at interaction in terms of sequences of action, with an intense focus on small sections of data in an attempt to provide a 'deep' rather than 'broad' summary analysis of the phenomena. That is to say we had an approach that [22, 31], documented the 'seen but un-noticed' aspects of robot interaction.

We started by building a corpus of video data from the fve-day deployment of the video. Two of the authors watched the video recordings of each day, extracting incidents from the videos focusing on cases of trash interactions between those in the square and the robotic trashcans. From these we selected a collection of 164 interaction 'highlights'-looking for cases where the interaction seemed noteworthy-either because something went wrong, or an interaction was particularly smooth, or cases that seemed particularly unusual or typical. Interactions in the square with the trashcans were very frequent, and while interactions overlapped or were simultaneous, we estimated over 300 or so interactions across the fve days. Our 164 interaction highlights spanned 135 minutes or 32% of the overall trial time.

## 4.3 Selection

From these clips, we selected a smaller corpus for more in-depth group analysis. We extracted 20 clips that featured interactions that were smooth, problematic, or seemed unusual or typical. These twenty clips also explored diferent variations on the emergent analytic themes, which structured our results below. We then took these twenty fragments in two group data sessions [30]. In these sessions, our analysis took the form not of the application of a formal method, but a more crafted set of analysis sessions and informed inspection of clips. Each extract was thus looked at as an individual, unique incident-but also inspected for exemplifying patterns that we could extrapolate to understand robotic interaction. This analytic approach builds on earlier analyses of robotic interaction using video methods [72], but also more broadly on approaches that attempt to explore unanticipated usage rather than more formal or quantitative results [20]. For this reason, in our results, our focus is not on how frequent or common diferent actions were, but instead to ofer an informed analysis of what happened with the robots in the square. Lastly, from the twenty group analysis clips we extracted the clips that we document in this paper to illustrate our analytic themes.

## 5 RESULTS

Because our robots were controlled by wizard-of-oz operators, the interactions between the robots and the people in the square developed over time, and adapted to the setting. The robot operators experimented with moving around urban space, in tandem with those passing through the square, who themselves coordinated their motion with the trashcan and other space users. Some participants might only see the robot trashcan for a few seconds, yet despite the unusual nature of a moving trashcan in a city square, it seems that pedestrians quickly applied their taken-for-granted expectations for how things move in an urban space [37, 78] and applied them to this new case.

Our results focus on how some simple patterns of using the trashcan arose in its use. These patterns, or as we will describe them systematics , developed over the very short time that each user encountered the trashcans in the square. In describing these systematics we also describe their sequential nature, in that they had parts that happened one after another, as the operators and users, did diferent things.

## 5.1 Giving and getting trash

We start by looking at how the robotic trashcan was used, unsurprisingly, as a receptacle for trash. Clearly when static and non-moving the trashcan played the role of a conventional 'ordinary' trashcanone blue to receive recycling materials and another gray to receive other trash. Yet the trashcans were nearly always in motion around the square and this supported some interesting uses of the trashcan in the square.

5.1.1 Ofer and release. Figure 2 shows an example of an 'ofer and release'. In 'ofer and release' an item of trash is ofered to CHI

'24, May

11-16,

2024, Honolulu, HI, USA

Brown et al.

Figure 2: Ofer and release : Pre-, Ofer, Move, Adjust, Throw: Trash is ofered to the robot which comes closer in response, and the trash is released into the trashcan. This storyboard makes use of the comic presentation style developed by Laurier, [36], and also used in earlier video analysis work presented at CHI such as [1].

<!-- image -->

the trashcan by a user extending their hand with the trash ofered visibly to the trashcan. This then prompts the trashcan to approach the user, and the trash item is positioned where it can reach the trashcan, and then it is released (or thrown).

After the 'pre-, ' trash is then picked up and ofered with a stretchedout arm, with the arm positioning the trash where the trashcan could potentially position itself 'under' or 'aside' the item for disposalan 'ofer.' This positioning of the trash acts then makes clear what the 'trash' is (clearly moving the trash away from the body and table of the user), is distinctively an ofer (and potentially one that could

We can identify some diferent parts of this sequence. First, we can identify a 'pre-' where something like mutual gaze is attempted between the user and the trashcan, although this might be shortened. In most cases, at least a glance was made before the trash was held out. 'Pre-' glances at the beginning of interactions are common in initiations of face-to-face human interaction, where gaze is often used to initiate an interaction, with a speaker making eye contact and waiting until mutual gaze is then achieved to start talking [28]. In our data, the pre- could be extended if a user decides that a trashcan was busy in another interaction, or too far away to see them. The pre- then may be extended until there is the possibility for the proximal interaction to start.

be interpreted to some extent by a machine), as well as ofering a destination for the trash to approach to (such as left, or to the right of the user). In some cases, the held trash 'projects' a particular position for the trashcan to approach from.

With the trashcan fnally within range of the user, the item is then positioned for disposal-raised or moved to a relevant position, leaving space so that the trashcan can position itself suitably to receive the trash, or the item raised to be thrown into the trashcan. As with object transfers between humans [71], there is something of a continuous mutual adjustment that goes on so as to make the passing of the object as efcient as possible-so in this case (Figure 2) there is going to be a 'throw' so the projected motion of the trashcan is used to start the throw before the trashcan is close enough, with the throw actually happening just as the trashcan gets close enough for a straightforward throw of the item into the trashcan. In some cases, the movement of the trashcan could make

The consequential motion of the trashcan is then seen as responding to the ofer - going towards the trash - accepting the ofer, or alternatively moving away - refusing the ofer. If the ofer is refused by the trashcan, the user might then revoke the ofer, or maintain it until the trashcan fnally approaches.

a straight throw more challenging since the trash was being thrown towards a moving object.

With this 'ofers and release' there is the possibility of it being refused. Object ofers do not need to be taken up, they make an object transfer possible but not necessary [71]. In Figure 3, the trashcan approaches a user ofering trash but then the trashcan changes direction halfway (image 2) through its approach. The user moves the trash back to the table (image 3). While the user is doing this the trashcan then resumes its motion but approaches from (our) right side instead of the left. The user resumes their ofer but now from the right side (4), and the trash is thrown (5), and the user disengages (puts her hand in her hair, image 6). What is interesting here is how the 'take up' of the ofer by the trashcan is displayed in its motion towards the user. As the trashcan rotates, delaying its motion for a few seconds, this is enough to cause the user to withdraw the ofer. Ofer and acceptance are connected, and delay is seen here as a rejection of the ofer, resulting in the ofer being retracted. In this case, the change in the direction of the trashcan almost results in the withdrawal of the trash item, although the ofer actually gets resumed when the trashcan resumes motion.

Finally, post-sequence we see usually a very quick dis-attending to the trashcan by the user, perhaps as a way of indicating that this interaction is complete and there is no more trash to share. This move away quickly closes the interaction and attention moves on to something else. It also works to underlie the functional nature of a particular trash use-now that the trash has been disposed of there is nothing more to do, and the trash can should not be given any more attention. As Sacks again points out, we regulate what we give attention to in public places to be seen as 'normal.' We do not, for example, usually stare for minutes at street furniture [63]

While this use of the robotic trashcan is perhaps not the most advanced of operations, it is notable how it spontaneously arose, without any instructions, training, or prompting by ourselves. It is a use that appears 'simple' (to some extent), one that fts with the scene, and with the projected ability of a robot by its users. As the robot operators responded to it, seeing it themselves as an ofer that they could accept, we can see something close to a spontaneous use. Again, we fnd this behaviour perhaps even surprising from users who had encountered the robotic trashcan only a few minutes earlier, and with no training or instruction.

5.1.2 Ask and receive. As the trashcan moved its way around the square it would at times wait at particular spots, or perhaps more accurately 'hover' near particular tables and people. The operators took the opportunity to gently tap the trashcan on a table or a seat adjacent to where someone was sitting. This could be seen, again in the context of the collection of trash, as requesting trash. This was perhaps better described as an 'ask' or a 'beg' since it involved the trashcan stopping by a potential user, who had something that could potentially be disposed of, close enough that they could dispose of that trash, and waiting. The user might then ignore this 'ofer', but in many cases, the ofer was responded to by the user them fnding something to dispose of (even just a napkin), and then throwing it into the trashcan.

In Figure 4, the trashcan approaches the table of a user who has just fnished eating lunch. After approaching the user, the trashcan rotates slightly but keeps its position. While the trashcan is approaching the user glances at both the landfll and recycling trashcans that are both in his vicinity. The trashcan 'hovers' at his table for around 3 seconds, after which the user speaks quietly, looks down, and then takes his now used paper bowl and tosses it into the trashcan. After doing so he nods slightly and smiles and dis-attends and returns to looking at his phone.

As in the other clips, in Figure 4 this user appears at least initially unfamiliar with the trashcan and spends some seconds looking around to try and understand what it is doing. Indeed, this clip comes from the frst day of recording. This 'asking' can be seen not as simply a way of collecting trash but also a way of instructing users that they are allowed to, and encouraged to use the trashcans, as well as that the trashcans are not simply moving around the square on a random or pre-fxed pattern, but are responsive to and interact with those in the square. 'Asking for trash', then, perhaps has a special role in that it is a trashcan-initiated interaction. This allows the operators to some extent 'instruct' potential users in how the trashcan could be used, and to interact with users giving them a sense of how the trashcan can respond to their actions-such as moving towards trash, and understanding to some extent how to interact with the trashcan.

In some cases the trashcan operators became somewhat more insistent and would lightly hit the table, sometimes receiving a verbal response-perhaps an account of why no trash was being given. In other cases users would have items they were keeping for the recycle bin, so would withhold trash, even if the landfll trashcan 'asked' for trash (or vice versa). For those familiar with having a dog as a pet, many interactions take place across the species boundary, such as 'begging for scraps at the table'. Here, the motion of the trashcan at the table is particularly reminiscent of Fischer et al. [20]. However, as Figure 4 shows we did not fnd evidence for more reserved or hesitant interactions with the trashcan from solo eaters.

5.1.3 Driveby. Our last disposal 'systematic' use (Figure 5) we characterized as 'driveby' disposal. Driveby disposal makes use of the existing movement of the trashcan or user to deposit trash with minimal interaction before the trash is delivered.

For example, in Figure 5 the trashcan is passing by behind a sitting user who has some waste. They lean over and drop the waste in the trashcan, making use of its motion to time an efective disposal without having to move from the chair. In this case, of course, the trajectory of the trashcan must pass by close enough to be able to throw or drop the trash without having to get up and move. This usage is perhaps most like the use of a conventional trashcan-in that, the user makes use of the positioning of the trashcan next to where they are (such as sitting in a chair). A second variant on the 'driveby' disposal was when the participants themselves were moving, and they needed to pass by where the trashcan was and drop their garbage of. Figure 6, a pedestrian enters the square and needs to intersect the trajectory of the trashcan, walk towards the moving object, deposit, and continue their walk away. One complication with this is that these trashcans were almost continually in motion. This means that a pedestrian needs to make predictions about where the trashcan is moving to, what its likely future motion will be, to be able to intersect the trashcan, and also to choose the right moment to drop the trash. If the user plans to drop of the trash while the trashcan is passing by (Figure 5) then the trajectory CHI

'24, May

11-16,

2024, Honolulu, HI, USA

Brown et al.

Figure 3: Ofer and release : Ofer is started, retracted and then resumed. The robot approaches a woman sitting down, she holds out a paper plate in her hand. As the robot approaches it needs to rotate to be able to go in that direction, but while it is rotating the woman retracts the trash and starts to move it down to the table again. This motion moves the plate from our right side to our left, and so the trashcan changes course and starts approaching her from the other side. On seeing this the woman lifts the plate again and then throws into the trashcan when it is close enough.

<!-- image -->

must pass by close enough to be able to throw or drop the trash without moving.

Interestingly in Figure 6 the disposal of the trash takes place less than 10 seconds after the trashcan is seen for the frst time by the passerby. The user also changes their trajectory when they notice the trashcan is moving, walking to (our) right of the trashcan rather

Some interesting diferences are noticeable in this form of trash delivery. First, the 'pre-' phase can be minimized, and little gaze or visual attention paid to the trashcan before the trash delivery. Where the user has to actually go to the trashcan we see the trashcan looked directly at as the user approaches, a functional 'pre-' that also communicates a user's intent-they are going to (or past) the trashcan. Once the dropof of the garbage is attempted then eyegaze is shared with the trashcan to get the trash into the right place-i.e. into the trashcan itself. The 'driveby' can also rely upon not just being able to get to the trashcan but also continuing on one's journey, and so takes the form of a path passing via the trashcan on the right or left side. This means that if the trashcan changes direction this can interfere with the pedestrians' motion, in that they need to themselves divert to catch the moving target.

than to the left of the trashcan. This is quite the 'one shot' training example-with the user not only seeing that it is a trashcan, that it is a moving trashcan that they need to move around but also that they can dispose of garbage most efectively from one side and not the other. Just as they take an extra step to move around the trashcan they transfer their garbage from their left to right hand, queuing up the garbage for its disposal as they walk by. All this, in the frst 10 seconds of spontaneous robotic interaction in a public space.

## 5.2 Moving in the square

Movements of robots around and with pedestrians have been a major focus of social robotics [45]. Even though our wizard operators mostly moved around the square unproblematically, moving safely in a crowded urban space is not simple. In our data, we observed again some simple emergent systematics in how pedestrians and robots worked together in their movements. For example, in Figure 7, a trashcan moves towards a gap between two tables while a Trash in Motion:

Emergent Interactions with

a

Robotic Trashcan CHI

'24, May

11-16,

2024, Honolulu, HI, USA

<!-- image -->

and receive

:

The trashcans move around

a

man sitting in the square, with one trashcan moving

which it then receives.

As the man puts the trash into the trashcan be smiles and nods his head to Left hand is raised displaying trash held in ball

Figure 4: Ask 'asking' for trash, the trashcans.

then stoppingacknowledge

<!-- image -->

Figure 5: Driveby : Sequence of use when the robot drives by a seated man who uses its motion to dispose of trash. He is holding trash in his left hand and as the trashcan moves past he quickly throws the trash into the trashcan, all the while holding his phone in his right hand.

<!-- image -->

Figure 6: Driveby : Use of the trashcan by a pedestrian walking through the square. The pedestrian enteres the square and changes their trajectory as they see the moving trashcan, going past the trashcan on the opposite side. If they had maintained the same direction they would have likely walked directly into the trashcan. As they pass by they throw some trash into the trashcan, moving the trash from one had to another to do so.

pedestrian walking through the square walks towards the gap simultaneously. In this fgure, we are recording from the perspective of the trashcan, with the trashcan visible on the bottom left of the frst image. In these fgures, we have included cropped images from the 360 camera view that is available to the robot operators, with a focus on the trashcan's interactions with pedestrians in the square. After the frst image, the trashcan pauses slightly a small distance from the set of tables and chairs-'yielding' for the pedestrian who continues at the same speed. As the pedestrian passes through the gap she 'curves' slightly to the left to be able to go around a chair, and then curves slightly to the right to get around the moving trashcan. In this short (2-second) clip the pedestrian does not look directly at the trashcan, even as the trashcan moves and she curves her way around. However, just at the end, she glances at the trashcan, acknowledging that perhaps a trashcan moving in the middle of the pavement is not a usual occurrence in a city square.

Although a quite simple operation, it is interesting to see how it displays both the robot operator and pedestrians' skill at navigating a dense public space, how these skills become transferred in navigating a robot, as well as navigating around a robot. Recent work on interaction around self-driving cars has underlined the importance of yielding [5] as a basic form of interaction, and here we can similarly see the importance of a sequential interaction to be able to smoothly have one actor 'yield' (the trashcan) and one 'go.' The operator here draws upon their own skills as a walker in urban space, walkers who, as in this case, will politely yield for another pedestrian, or go frst if a pedestrian yields for them. The operators' motion then shows us both the best a robot could do, in how the operators themselves decide when and where to move the trashcan, but also in the reactions of those the trashcan encounters-be that puzzlement, annoyance, or as in this case, a very ordinary and efcient walk past.

One important point to make about this data is that the work of the wizard-of-oz robot operator here is itself also part of our study; the wizard's intuition for how a competent robot should potentially interact in a public space is as much a part of what we hope to learn as what the passersby do. The trash can here stops a sufcient distance before the narrow gap between the table and the chair, leaving space that the pedestrian needs to be able to walk forward, but also enough space so they can walk between the trash can and the chair. The operator, by slowing and stopping the trashcan at the chair on the left preempts the future path of the pedestrian and yields not just for where they are now, but also leaves space for their future path. As well as leaving a space the operator by stopping here communicates with the pedestrian implicitly that it is yielding- 'I will wait here and you can go there'. This allows the pedestrian to not have to adjust their pace and they then walk between the chairs but also curving to the right to walk around the trashcan.

The trashcan's motion here also shows how operators can predict the future movement of pedestrians and move accordingly. In other videos the trashcans move towards a pedestrian with a subtle movement of the trashcan either to the left or right of the pedestrian, allowing the pedestrian to remain on the same trajectory and to avoid a potential collision or space confict. This would also at times be responded to by a movement by the pedestrian in response, adjusting their trajectory slightly in the opposite direction to make sufcient space for both the trashcan and the person in the space (cf fgure 6). In Figure 7 by waiting on the left of the chairs the trashcan leaves space for the pedestrian to pass on the right (which they then do). This is not a direct straight line, but rather the reasonable expectation that by leaving a path where a pedestrian need only make a slight deviation, this will be taken by the pedestrian. In this case, the trashcan is actually blocked on its own left from moving to leave more space for the pedestrian, so it has to stay here, yet as can be seen all passes very smoothly and quickly.

This is not to say that all pedestrian moving interactions with the trashcan were smooth. In Figure 8 we see how this space confict causes momentary confusion, or at least hesitation, by a pedestrian. As the pedestrian approaches the square the trashcan is moving, positioned on the right in frame one. Just before getting to the trashcan, the pedestrian stops dead and stands with her feet side by side. As the trashcan is rotating, she then turns her body to the left to go past on the left, but the delay that the trashcan makes (since it is rotating not moving) is taken by the pedestrian as a 'yield' and she then turns to the right and passes by the trashcan between the shopfront at the trashcan.

A moving trashcan is obviously not a particularly usual object to encounter in an urban space, and while there is certainly the case that for some pedestrians crossing the square, this was not their frst encounter with the trashcan (as they might pass through the square multiple times); for most, it was their frst encounter. Yet rather than the trashcan causing confusion, pedestrians treated the trashcan like any other human or human-controlled moving object in the city and interpreted and made use of its motion in their own motion. One way of understanding this is as a 'same but diferent' mode of interaction-to make sense of and use the trashcan users (even just passersby) would treat the trashcan as reasonably just like a conventional trashcan, possibly a conventional trashcan on wheels, moved by a human actually present pushing it. So long as the trashcan does manage to pull of its motion as 'the same', then it seems users to an extent simply treated it in a similar way.

This interaction, although it resolves quite quickly, both delays the passerby (they have to stop), as well as results in some small confusion about whether the pedestrian should pass on the right or left of the trashcan. That is to say, is the trashcan yielding and not moving to the left any further, or does the passerby need to pass by on the other side? This is not so diferent from the sort of interactions that cars and pedestrians make on pedestrian crossing, where a pedestrian might choose to go 'ahead' of a car if it slows and yields for them, or pass 'behind' the car [5] if it is already going through the crossing. In this case, the source of the confusion could in part be the way in which the trashcan rotates in space when it is stopped, which the pedestrian could mistake for being part of its motion, or simply the pedestrian could be confused about what this sort of object is and how it will behave. We note that in during the interaction the pedestrian breaks into a smile, a recognition in some way that something noticeable has happened-that is to say, the unusual presence of a robot trashcan, even if it is in this case slowing her movement in a small way.

## 5.3 Demonstrations

Some of the interactions that we recorded rested to some extent on the novelty of having robots in a public space. As Reyes-Cruz et al. [58] discuss 'demonstrations' are a common part of all kinds of ordinary use of technology, playing the role of instructing others in the use of new technologies alongside dealing with novelty and Figure

(1) Trial space.

<!-- image -->

<!-- image -->

<!-- image -->

(2) Curve left.

(3) Curve right.

7:

Moving in the square

:

Pedestrian and trashcan navigate around each other.

As the woman walks towards the trashcan

it yields so that she can walk past, and she changes her trajectory slightly to pass on one side of the trashcan and not the other.

Figure 8: Moving in the square : the pedestrian and the trashcan negotiate who will go frst and if the pedestrian should pass on the right or left.

<!-- image -->

newness. Their paper quotes Gofman [26], who gives a classic defnition of how demonstrations act as 'performances of a tasklike activity out of its usual functional context in order to allow someone who is not the performer to obtain a close picture of the doing of the activity'. Demonstrations feature a demonstrator and an audience; are staged; and are to a large extent implicit in that they feature carefully selected and limited events that can be read to indicate other functionality and behavior. So while a demonstration might only show one specifc use, it is organized in such a way that it implicitly communicates the broader functionalities and abilities of the particular technology.

The demonstrator takes an item of trash, makes it visible, has the trashcan approach them, and then places the item into the trashcan. This produces a clear demonstration of robotic trashcan use. There is a 'pre' action-the confguration and attention are given to the trashcan by the user looking at the trashcan. The looking also identifes for the viewer what is the important object for the demonstration-it confgures a user and the trashcan. The trash is then raised in the hand and shown to the trashcan. This acts as an 'ofer' to the trashcan, which is responded to by the trashcan moving towards the user. Then the item is disposed of in the trashcan, and the sequence is closed by the user dis-attending to the trashcan and moving onto their next preoccupation. The demonstration works as a self-complete episode to a potential viewer, either co-present or watching the video. It also works for us as analysts, producing an analyzable unit. As Reyes-Cryz (ibid) documents this sort of demonstration acts as an implicit indicator of other functionality and behavior-the trashcan recognizes gestures, trash, ofers, and can even understand the closure of the sequence at the end (in how it moves away and disengages from the interaction alongside the dis-engagement of users).

Applying this to the uses of our robot lets us explore how participants often managed and arranged their use of the trashcan in small 'instructional units' that served the purpose of demonstrating both how this robotic trashcan could be used, but also more broadly some of its basic abilities (such as recognition and movement), to hint at use more broadly. An example of this is in Figure 9. Here pedestrians are flming the robot with their cellphone camera while another makes use of the trashcan to dispose of some rubbish. From our data, we can identify some key parts of these demonstrations. First, staging work-the confguration of an audience, a device to be demonstrated (the trash can), and a demonstrator. The introduction of the cell phone adds the possibility of a future audience who will view the video, and the importance of framing correctly (in portrait) the video to capture the event.

These actions that take place and are captured on the video are not radically diferent from many of the other uses of the trashcan. But this usage works to communicate a sort of 'ideal case' of use in a public visible way. It was popular to video interactions with the trashcan, with users videoing not only their own use and others' use but also just videoing the motion of the trashcan around the square. Having these events recorded adds another level to Gofman's concept of a demonstration since it creates its potential availability for those who are not local to a scene, but might be instructed through video should they come face-to-face in the future.

It is worth pointing out that we do not normally 'demonstrate' with ordinary street furniture, much fewer trashcans which by their unclean and taken-for-granted nature are seldom the center of cellphone recording. Clearly, a robotic trashcan is unusual enough that it prompts a demonstration in this way. In this way, it is important to acknowledge that many aspects of use were not purely functional but were also about the 'fun' of an unusual trashcan. Children often used the trashcan as their parents watched and smiled.

These demonstrations might then be seen more in terms of test uses, trying to see what and what not the trashcan will do, similar to how users explored robot functionality in [72].

There were also demonstrations without cameras, what might be called 'test uses'. In these cases, there is no audience as such, beyond the local participants in the test. A small item (like a napkin) might be disposed of, but the use is not focused on the need to dispose of an item at that moment (such as prior to leaving or having fnished a drink) but to explore what will happen, how the trashcan will react to the disposal of the item (for example, in Figure 10).

## 6 DISCUSSION

The research question that motivated this work was how do people respond to non-anthropomorphic robots deployed in public spaces? Using video analysis, we have attempted to provide fne-grained documentation of the interactions that take place around the robot, how the robot came to be reacted to by others, and also how they formed patterns of interaction in their use. Experimental human-robot interaction deployments often focus on the acceptance [2, 76, 82], or attitudes of human users of a robot technology [3, 13]. Instead in this paper, we have mostly ignored the attitudes of the users in this robot trial but focused on their behavior interacting with the robot. In this way, we have documented the disposal of garbage, but also how our trashcan could be a topic for video recording, or even just an amusing object to share with a lunch companion. We anticipate that the fndings from this deployment could generalize beyond trash robot interactions to inform understanding of how people can interact with a wide variety of service robots that might be deployed in urban spaces. Using a close analysis of video allows us, as Sabanovic et al. [62] advocate, "fne-grained observational analysis of the robot interacting in a real-world environment" to discover how "humans react to and interact with the robot; how humans interact with each other while interacting with the robot; which aspects of the robot's, and human's, [and how] actions lead to breakdowns in the interaction."

## 6.1 Spontaneous Simple Sequential Systematics

Clearly, some of what we discovered here has been touched on in earlier human-robot interaction literature, and in particular EMCA inspired work. Therefore, to focus our discussion we have drawn our observations together in the form of a sensitising framework for future design. This lightweight framework describes the diferent aspects of public HRI behavior that we describe, also conceptualizing the emergent behaviors we observed and in what form. As Crabtree et al put it, a sensitising framework acts as a "snapshot of a setting's work and salient activities that may drawn upon to 'pump prime' design reasoning" [9]. A sensitizing framework can be thought of as a tool to inspire and generate diferent designs. We call our framework "SSSS" - that is to say characterizing these observed behaviors as "Spontaneous Simple Sequential Systematics".

<!-- image -->

Figure 10: Demonstrations : Two trashcan users work together to demonstrate the use of the trashcan

<!-- image -->

Figure 9: Demonstrations: Users' demonstrations of the trashcan while being recorded. Users make use of the trashcan while a companion records their interaction on a mobile phone.

<!-- image -->

<!-- image -->

<!-- image -->

6.1.1 Systematics. We go through each "S" in turn: frst, the interactions we observed were 'systematic'-small practices or patterns in interaction that were repeated across uses and across users. Users demonstrated their use of the trashcan, they ofered trash to the trashcan in a systematic way, gave trash when the trashcan likewise asked for trash, and made use of the trashcan when their movement trajectories coincided. These systematics were not designed as features of the trashcan by ourselves or the operators but emerged from the interactions of the robot operators, the robot, the city square, and those inhabiting the square. This notion of systematics draws both on Sacks et al's [64] use of the term, but also in how EMCA holds that interaction is 'orderly at all points' [22], that is to say that our actions often are understandable in terms of systematic forms of action [23].

6.1.2 Sequential. In documenting these interactions we would also argue for their sequential [66] nature. By this, we mean that they involve multiple diferent actions, from both the robot and the user, arranged in turn over time. This means that garbage is waved before it is deposited, for example, or that a user needs to get close enough to the trashcan to be able to throw or deposit an item. As is broadly true in human-to-human multi-modal interaction, the notion of sequence is fundamental. These points draw on arguments from conversation analysis that interaction is often sequentially [66] organized. This is, our actions can, at times, be divided into individual elements with each action setting up the conditions for the next, and the previous getting its sense in some ways refexively from what happens after.

6.1.3 Simple. That said, it is also worth pointing out that these interactions are relatively simple . What we mean by this is that not only do they often consist of just one or two parts but also that they ft in the context, both in terms of what happened before but also with what generally happens in that setting. The trashcan is in the square where people are eating food, something that produces trash. Ofering trash to a trashcan makes sense in terms of what can happen next since the trashcan has the ability to move and then receive the trash. Ofering trash to a trashcan that does not move would make little sense. Users' actions ft with what the robot can do [72]. An item that can be seen as trash (a paper bag, not a mobile phone), is held out in a way that the trashcan could approach it (such as to the side, not over a table or above the user). A trashcan receives trash, and then as it moves around the square, it can then respond to the ofer and collect the trash. This refers to what in EMCA is known as 'natural accountability' - that we often do things in such a way that their legibility to others is 'designed in'.

This also means that, for example, holding out a phone is not an ofer because we would not usually drop our phones into the trashcan. Some aspects of the interaction (such as the use of gaze), and the ability to abandon them in progress, also show that they could be fexibly adopted to ft the usage desired by a user-such as depositing trash in one can and not the other. This simplicity means that our actions are often simple enough to be seen and understood 'at a glance'.

6.1.4 Spontaneous. Lastly, the use of the trashcan developed spontaneously - by just observing the moving trashcan, or perhaps other demonstrations in the square. Indeed, some users just made use of the trashcan on their way through the square, with only very brief interactions. Others were the frst to interact with the trashcan that day or did not observe anyone else during their visit to the square. This justifes us calling these interactions spontaneous-they develop within the square from the short periods of each trial.

As ordinary city inhabitants we know how to use a trashcan, and having a moving robotic trashcan, while quite diferent is close enough that we can almost instantaneously decide how to make use of this. In this sense, the use of the trashcan made use of our "taken for granted" [63] knowledge that any inhabitant of a city would know - what a trash can is for, how to put rubbish into the trashcan, what not to put in the trashcan, and so on. We can contrast this with technologies (perhaps even most robots) that usually involve some following of instructions or a tutorial to work out how they work. Our users very quickly could learn to save themselves walking across the square by ofering trash and having the trashcan come to them, or could fnd trash to deposit when a trashcan came by 'begging'. Making use of a passing-by trashcan, they could also make use of the trashcan's motion to shorten their own journey when dropping trash of. We should mention that these actions were not exclusively spontaneous - they could also be 'learned at a glance' by others in the square. We observed users clearly watching other users and 'learning' from their demonstrations. But these learned behaviors were still endogenous to the square, and did not come from (for example) instructions provided in the square or provided some other way.

## 6.2 Designing for Spontaneous Simple Sequential Systematics

Together, we can characterize the interactions in our data in terms of "spontaneous simple sequential systematics." Our feldwork, along with concepts from EMCA, informs this 'SSSS' framework. But what could this enable in terms of robot design?

Similarly, we have argued above for how sequentiality is also important. In our examples above a robot needed to respond to an ofer by approaching in sufcient time, and then slowing down where the trash can be released. Sequentiality here is specifc to the particular interaction but in these cases, the responsive motion needs to happen timely after the initial ofer. Clearly, this would depend upon a robot recognizing that some actions happen after others' actions. One important example we discussed is from previous work on yielding. Waiting in space while a pedestrian moves towards a gap has a particular meaning - a yield - whereas stopping at another time could have a diferent meaning (such as when we stop when we recognize or see someone for the frst time). Designing robot motion then requires that a robot has some understanding of how its motions will be seen as responding to others' actions.

Our work here rather than focus on the look (such as how humanoid [46, 69] or cute [4, 35] a robot should be) focuses on the complexity of movement as part of unfolding interaction. Indeed, social robotics has long explored how robots could move to be safe and efective inhabitants of space. For example, robot navigation among pedestrians is a quickly growing feld [45, 57]. In terms of design, we would underlie the importance of designing robot motion not just in terms of safety, or efciency, but in terms of how it can be understood by those around. So how should the motion of a robot should be designed to be systematic? A robot should move in a way that its actions are understood by others as examples of particular actions, and understandable as particular actions. So a robot might 'go' somewhere, and be seeable as going somewhere, and this is diferent from a robot moving in a certain way as to be seen as 'looking around'. The goal in designing these diferent systematic motions here would be to produce actions that can be read by others in specifc ways.

Our third "s" was simple - that the interactions designed for are simple enough that anyone can observe them in context and understand what is happening. Context is important here - it is perhaps not clear what we would make of (say) a trashcan driving on the road. In terms of design this encourages a refection on what goes on in a setting, what might be reasonable to see there, and how that reasonableness can be borrowed in the design of a particular robot and its actions in that setting.

These sensitizing concepts clearly do not give exact design guidelines, but instead encourage robot designers to think through how a robot, and in particular its movement, can be designed. Most specifically our focus is on the communicative nature of movements for a robot. In particular, starting with a Wizard-of-Oz method was powerful in that it let us understand what the 'best case' of robot motion might be, which gave us a powerful ground for understanding what motions a computer-controlled robot could potentially produce. Starting with human-human understanding then gives us a powerful foundation for thinking about what shape robot motion might potentially take, albeit in a much more limited manner since a computer could not hope to have the same level of understanding of a human in space.

Lastly, how can we design a robot's motion such that others' interactions with the robot are spontaneous? By spontaneous we meant that others can interact with the robot without any need for training. In our case clearly, the taken-for-granted existing interactions with a trashcan contributed here - looking similar enough to a trashcan provided a suggestion of possible future actions for those going by. Why not simply use the trashcan as a trashcan (despite its rather unusual extra moving functionality)? Addresing this in desing means thinking about what systematic sequences might develop spontaneously in use.

## 6.3 Urban robotics: in the space or of the space?

Lastly, it is worth adding a few remarks about the urban environment the robots were tested in. With the growth in deployments of urban robots such as delivery robots and autonomous vehicles [5, 74], confict around what rights robots have in public space is also growing [41]. The companies deploying these systems treat public space as an infrastructure they travel through. Although this use of space is a common feature of road and public highways, it highlights some of the longstanding conficts between those who live in a space, and those who pass through[39]. More specifcally, when robotic systems move erratically or end up blocking urban roads, there is pronounced backlash, such as that around the interactions between self-driving cars and emergency vehicles [40]. Being in public space without participating in it, urban robots might potentially themselves become 'matter out of place.'

While our robotic trashcans are also moving through space, they take their lead from the existing fabric of the city-the thousands of litter baskets already installed. The trashcan robots are therefore not passing through but are a mode of automating the infrastructure that is already embedded in the environmental context. The robots are simple but functionally tied to the city square. The familiarity of their form-standard trashcans-informed people's predisposition to treat them as a part of the public architecture. Indeed, in our postinterviews with interactants, the trashcans were assumed to be a municipal initiative because that's who typically deals with the trash . In the contention around technology-driven urban renewal-for example, the debates around Toronto's Sidewalk Labs initiative[27]- we see potential aligning technology with community goals rather than focusing on transforming cities around new technologies[29, 51].

This said, our methods here were perhaps limited in terms of addressing changes to the long-term character of city space. City squares are already active spaces, with often diferent forms of entertainment taking place on the street-such as eavesdropping on others' interactions or more focused events such as street performers, buskers, and the like. So while our introduction of a moving trashcan certainly was somewhat unusual it was not completely out of place as a sort of 'intervention' that one might potentially encounter on the city streets. It is important then to realize that while trashcans are usual technology, there is something already in the character of busy public spaces that can be sites for the unexpected or the unusual, and this is part of their charm. Our trashcan deployment, a diferent sort of city infrastructure, also played a role as part of the background of a space-like buskers or street performers, something unusual to be observed in the background but not necessarily something that needed to be directly interacted with. While the trashcans did have a role in the city space beyond just their functional role, we would argue that it was still in keeping with the 'sort of things that happen' in a busy urban place.

## 7 CONCLUSION

Urban life depends on trash to be disposed of in a timely and efcient manner. As others in HCI have explored, trash presents an interesting and challenging case where the demands of sustainability, digital civics, but also basics of usability, come together. In this paper, we have documented our experiments with trash robots, robots that could potentially be part of this essential infrastructure of urban life. Our focus has been mainly on how users and robots can communicate through motion, developing some simple practices together. We have explored and documented public human-robot interactions in depth, using this to develop a design approach around designing the motion of robots in concert with their human users.

Designing robots that can co-exist and provide mutual beneft in busy urban spaces is, in turn, clearly a huge challenge. This challenge spans not only the functional but also our savvy-can we build playful robots and enable convivial interactions in urban space? We are hopeful that, studying interactions around trash, we can learn lessons not only for future trash robots but more broadly for the emergent feld of urban robotics .

## ACKNOWLEDGMENTS

This research was conducted under Cornell Tech's IRB Protocol #IRB0145711, with sponsorship from Tata Consultancy Services and seed grant funding from Cornell Tech's Urban Tech Hub. The project was also funded by the WASP-HS project "AI in motion" (MMW2020.0086). We thank the members of the Future Automation Lab for being the wizards behind the robots and we also appreciate the support of Village Alliance for the access to the public square.

## REFERENCES

- [1] Iuliia Avgustis. 2023. Respecifying Phubbing: Video-Based Analysis of Smartphone Use in Co-Present Interactions. In Proceedings of the 2023 CHI Conference
2. on Human Factors in Computing Systems . 1-15.
- [3] Christoph Bartneck, Tatsuya Nomura, Takayuki Kanda, Tomohiro Suzuki, and Kennsuke Kato. 2005. Cultural diferences in attitudes towards robots. In AISB Symposium on Robot Companions: Hard Problems And Open Challenges In HumanRobot Interaction . AISB, 1-4.
- [2] Franziska Babel, Johannes Kraus, and Martin Baumann. 2022. Findings From A Qualitative Field Study with An Autonomous Robot in Public: Exploration of User Reactions and Conficts. International Journal of Social Robotics 14, 7 (2022), 1625-1655.
- [4] Andrea Bertolini and Rachele Carli. 2022. Human-robot interaction and user manipulation. In International Conference on Persuasive Technology . Springer, 43-57.
- [6] Barry Brown and Oskar Juhlin. 2015. Enjoying machines . MIT Press.
- [5] Barry Brown, Mathias Broth, and Erik Vinkhuyzen. 2023. The Halting problem: Video analysis of self-driving cars in trafc. In Proceedings of the 2023 CHI Conference on Human Factors in Computing Systems . 1-14.
- [7] Barry Brown, Moira McGregor, and Eric Laurier. 2013. iPhone in vivo: video analysis of mobile device use. In Proceedings of the SIGCHI conference on Human Factors in computing systems . ACM, 1031-1040.
- [9] Andrew Crabtree, Mark Rouncefeld, and Peter Tolmie. 2012. Doing design ethnography . Springer Science &amp; Business Media.
- [8] Robert B Cialdini. 2003. Infuence: Science and Practice . Pearson.
- [10] Grace de la Flor, Paul Luf, Marina Jirotka, John Pybus, Ruth Kirkham, and Annamaria Carusi. 2010. The Case of the Disappearing Ox: Seeing Through Digital Images to an Analysis of Ancient Texts. In Proceedings of the SIGCHI Conference on Human Factors in Computing Systems (CHI '10) . ACM, New York, NY, USA, 473-482. https://doi.org/10.1145/1753326.1753397 event-place: Atlanta, Georgia, USA.
- [12] Alan Dix. 2002. Beyond intention-pushing boundaries with incidental interaction. In Proceedings of Building Bridges: Interdisciplinary Context-Sensitive Computing, Glasgow University , Vol. 9. 1-6.
- [11] Eric Deng, Bilge Mutlu, Maja J Mataric, et al. 2019. Embodiment in socially interactive robots. Foundations and Trends® in Robotics 7, 4 (2019), 251-356.
- [13] Anna Dobrosovestnova, Isabel Schwaninger, and Astrid Weiss. 2022. With a little help of humans. an exploratory study of delivery robots stuck in snow. In 2022 31st IEEE International Conference on Robot and Human Interactive Communication (RO-MAN) . IEEE, 1023-1029.
- [15] Paul Dourish. 2010. HCI and environmental sustainability: the politics of design and the design of politics. In Proceedings of the 8th ACM conference on Designing Interactive Systems . 1-10.
- [14] Mary Douglas. 2003. Purity and danger: An analysis of concepts of pollution and taboo . Routledge.
- [16] Mitchell Duneier. 1999. Sidewalk . Macmillan.
- [18] David Evans. 2012. Beyond the throwaway society: Ordinary domestic practice and a sociological approach to household food waste. Sociology 46, 1 (2012), 41-56.
- [17] M Eddy. 2016. Germany Gleefully Leads List of World's Top Recyclers. New York Times (2016).
- [19] Gabriele Ferri, Alessandro Manzi, Pericle Salvini, Barbara Mazzolai, Cecilia Laschi, and Paolo Dario. 2011. DustCart, an autonomous robot for door-to-door garbage collection: From DustBot project to the experimentation in the small town of Peccioli. In 2011 IEEE International Conference on Robotics and Automation . IEEE, 655-660.
- [21] Marlena R Fraune, Satoru Kawakami, Selma Sabanovic, P Ravindra S De Silva, and Michio Okada. 2015. Three's company, or a crowd?: The efects of robot number and behavior on HRI in Japan and the USA.. In Robotics: Science and systems , Vol. 10.
- [20] Kerstin Fischer, Stephen Yang, Brian Mok, Rohan Maheshwari, David Sirkin, and Wendy Ju. 2015. Initiating interactions and negotiating approach: a robotic trash can in the feld. In 2015 AAAI Spring Symposium Series . AAAI.
- [22] Harold Garfnkel. 1967. Studies in ethnomethodology . Prentice-Hall.
- [24] Jan Gehl. 1989. A changing street life in a changing society. Places 6, 1 (1989).
- [23] Harold Garfnkel and Harvey Sacks. 2005. On formal structures of practical actions. In Ethnomethodological studies of work . Routledge, 165-198.
- [25] Rachel Gockley, Allison Bruce, Jodi Forlizzi, Marek Michalowski, Anne Mundell, Stephanie Rosenthal, Brennan Sellner, Reid Simmons, Kevin Snipes, Alan C Schultz, et al. 2005. Designing robots for long-term social interaction. In 2005 IEEE/RSJ International Conference on Intelligent Robots and Systems . IEEE, IEEE, 1338-1343.
- [27] Ellen P Goodman and Julia Powles. 2019. Urbanism under google: lessons from sidewalk Toronto. Fordham L. Rev. 88 (2019), 457.
- [26] Erving Gofman and Bennett Berger. 1986. Frame Analysis: An Essay on the Organization of Experience (later reprint edition ed.). Northeastern University Press, Boston.
- [28] Charles Goodwin. 1987. Forgetfulness as an interactive resource. Social psychology quarterly (1987), 115-130.
- [29] André Gorz. 1973. The social ideology of the motorcar. Sitio Reclaim the streets. Internet (1973).

- [30] Christian Heath, Jon Hindmarsh, and Paul Luf. 2010. Video in qualitative research . Sage Publications.
- [32] Sara Heitlinger, Nick Bryan-Kinns, and Rob Comber. 2019. The right to the sustainable smart city. In Proceedings of the 2019 CHI Conference on Human Factors in Computing Systems . 1-13.
- [31] Christian Heath and Paul Luf. 2000. Technology in action . Cambridge university press.
- [33] Wendy Ju. 2015. The design of implicit interactions . Morgan Claypool.
- [35] Cherie Lacey and Catherine Caudwell. 2019. Cuteness as a 'dark pattern'in home robots. In 2019 14th ACM/IEEE International Conference on Human-Robot Interaction (HRI) (Daegu, Korea). IEEE, IEEE, 374-381.
- [34] Hideaki Kuzuoka, Karola Pitsch, Yuya Suzuki, Ikkaku Kawaguchi, Keiichi Yamazaki, Akiko Yamazaki, Yoshinori Kuno, Paul Luf, and Christian Heath. 2008. Efect of restarts and pauses on achieving a state of mutual orientation between a human and a robot. In Proceedings of the 2008 ACM conference on Computer supported cooperative work . 201-204.
- [36] Eric Laurier. 2014. The graphic transcript: Poaching comic book grammar for inscribing the visual, spatial and temporal aspects of action. Geography Compass 8, 4 (2014), 235-248.
- [38] Wen-Ying Lee and Malte Jung. 2020. Ludic-HRI: Designing Playful Experiences with Robots. In Companion of the 2020 ACM/IEEE International Conference on Human-Robot Interaction (Cambridge, UK). ACM/IEEE, 582-584.
- [37] John Lee and D. Rod Watson. 1993. Final Report to the Plan Urbain: Public Space as an Interactional Order . Technical Report Unnumbered. Department of Sociology, University of Manchester, Manchester.
- [39] Anastasia Loukaitou-Sideris and Renia Ehrenfeucht. 2011. Sidewalks: Confict and negotiation over public space . MIT Press.
- [41] Yiwen Lu. 2023. San Francisco Balks at Expanding Driverless Car Services on City's Roads. The New York Times (Aug. 2023). https://www.nytimes.com/2023/ 08/09/technology/san-francisco-driverless-cars.html
- [40] Yiwen Lu. 2023. Driverless Taxis Blocked Ambulance in Fatal Accident, San Francisco Fire Dept. Says. The New York Times (Sept. 2023). https://www. nytimes.com/2023/09/02/technology/driverless-cars-cruise-san-francisco.html
- [42] Rachel Macrorie, Simon Marvin, and Aidan While. 2021. Robotics and automation in the city: a research agenda. Urban Geography 42, 2 (2021), 197-217.
- [44] Simon Marvin, Aidan While, Mateja Kovacic, Andy Lockhart, and Rachel Macrorie. 2018. Urban robotics and automation: Critical challenges, international experiments and transferable lessons for the UK. (2018).
- [43] Nikolas Martelaro. 2016. Wizard-of-oz interfaces as a step towards autonomous hri. In 2016 AAAI Spring Symposium series (Stanford, CA). AAAI.
- [45] Christoforos Mavrogiannis, Francesca Baldini, Allan Wang, Dapeng Zhao, Pete Trautman, Aaron Steinfeld, and Jean Oh. 2023. Core challenges of social robot navigation: A survey. ACM Transactions on Human-Robot Interaction 12, 3 (2023), 1-39.
- [47] Lorenza Mondada. 2018. Multiple temporalities of language and body in interaction: Challenges for transcribing multimodality. Research on language and social interaction 51, 1 (2018), 85-106.
- [46] Blanca Miller and David Feil-Seifer. 2016. Embodiment, situatedness, and morphology for humanoid robots interacting with people. Humanoid Robotics: A Reference (2016), 1-23.
- [48] Lilia Moshkina, Susan Trickett, and J Gregory Trafton. 2014. Social engagement in public places: a tale of one robot. In Proceedings of the 2014 ACM/IEEE international conference on Human-robot interaction . 382-389.
- [50] Robin Nagle. 2017. The job is in the feld: notes from municipal anthropology. Journal of Business Anthropology 6, 1 (2017), 41-57.
- [49] Robin Nagle. 2013. Picking up: on the streets and behind the trucks with the sanitation workers of New York City . Macmillan.
- [51] Peter D Norton. 2011. Fighting trafc: the dawn of the motor age in the American city . Mit Press.
- [53] Eric Paulos and Tom Jenkins. 2005. Urban probes: encountering our emerging urban atmospheres. In Proceedings of the SIGCHI conference on Human factors in computing systems . 341-350.
- [52] Max Pascher, Uwe Gruenefeld, Stefan Schneegass, and Jens Gerken. 2023. How to Communicate Robot Motion Intent: A Scoping Review. In Proceedings of the 2023 CHI Conference on Human Factors in Computing Systems . 1-17.
- [54] Hannah Pelikan and Emily Hofstetter. 2023. Managing Delays in Human-Robot Interaction. ACM Transactions on Computer-Human Interaction 30, 4 (Aug. 2023), 1-42. https://doi.org/10.1145/3569890
- [56] Karola Pitsch, Hideaki Kuzuoka, Yuya Suzuki, Luise Sussenbach, Paul Luf, and Christian Heath. 2009. 'The frst fve seconds': Contingent stepwise entry into an interaction as a means to secure sustained engagement in HRI. In RO-MAN 2009-The 18th IEEE International Symposium on Robot and Human Interactive Communication . IEEE, 985-991.
- [55] Mark Perry, Oskar Juhlin, and Daniel Normark. 2010. Laying waste together: The shared creation and disposal of refuse in a social context. Space and Culture 13, 1 (2010), 75-94.
- [57] Ashwini Pokle, Roberto Martín-Martín, Patrick Goebel, Vincent Chow, Hans M Ewald, Junwei Yang, Zhenkai Wang, Amir Sadeghian, Dorsa Sadigh, Silvio
29. Savarese, et al. 2019. Deep local trajectory replanning and control for robot navigation. In 2019 international conference on robotics and automation (ICRA) . IEEE, 5815-5822.
- [59] Laurel D Riek. 2012. Wizard of oz studies in hri: a systematic review and new reporting guidelines. Journal of Human-Robot Interaction 1, 1 (2012), 119-136.
- [58] Gisela Reyes-Cruz, Joel E. Fischer, and Stuart Reeves. 2022. Demonstrating Interaction: The Case of Assistive Technology. ACM Transactions on ComputerHuman Interaction 29, 5 (Oct. 2022), 1-37. https://doi.org/10.1145/3514236
- [60] Jacob A Riis. 1899. Letting in the light. Atlantic Monthly (1899), 495-505.
- [62] Selma Sabanovic, Marek P Michalowski, and Reid Simmons. 2006. Robots in the wild: Observing human-robot social interaction outside the lab. In 9th IEEE International Workshop on Advanced Motion Control, 2006. IEEE, IEEE, 596-601.
- [61] Chiara Rossitto, Rob Comber, Jakob Tholander, and Mattias Jacobsson. 2022. Towards Digital Environmental Stewardship: the Work of Caring for the Environment in Waste Management. In Proceedings of the 2022 CHI Conference on Human Factors in Computing Systems . 1-16.
- [63] H. Sacks. 1984. On doing 'being ordinary'. In Structures of social action. , J.M. Atkinson and J. Heritage (Eds.). Cambridge university press, New York, 413-429.
- [65] Pericle Salvini. 2018. Urban robotics: Towards responsible innovations for our cities. Robotics and Autonomous Systems 100 (2018), 278-286.
- [64] H. Sacks, E.A. Scheglof, and G. Jeferson. 1974. A Simplest Systematics for the Organization of Turn Taking for Conversation. Language 50 (1974), 696-735.
- [66] Emanuel A. Scheglof. 2007. Sequence Organization in Interaction: Volume 1: A Primer in Conversation Analysis . Cambridge University Press.
- [68] Susan Leigh Star. 1999. The ethnography of infrastructure. American behavioral scientist 43, 3 (1999), 377-391.
- [67] Roseanna Sommers and Franklin G Miller. 2013. Forgoing debriefng in deceptive research: Is it ever ethical? Ethics &amp; Behavior 23, 2 (2013), 98-116.
- [69] Steven J Stroessner and Jonathan Benitez. 2019. The social perception of humanoid and non-humanoid robots: Efects of gendered and machinelike features. International Journal of Social Robotics 11 (2019), 305-315.
- [71] Sylvaine Tuncer and Pentti Haddington. 2020. Object transfers: An embodied resource to progress joint activities and build relative agency. Language in Society 49, 1 (2020), 61-87.
- [70] Anja Thieme, Rob Comber, Julia Miebach, Jack Weeden, Nicole Kraemer, Shaun Lawson, and Patrick Olivier. 2012. " We've bin watching you" designing for refection and social persuasion to promote sustainable lifestyles. In Proceedings of the SIGCHI conference on human factors in computing systems (Austin, USA). ACM, 2337-2346.
- [72] Sylvaine Tuncer, Christian Licoppe, Paul Luf, and Christian Heath. 2023. Recipient design in human-robot interaction: the emergent assessment of a robot's competence. AI &amp; SOCIETY (Jan. 2023). https://doi.org/10.1007/s00146-022-01608-7
- [74] Shianne van Mierlo. 2021. Field observations of reactions of incidentally copresent pedestrians to a seemingly autonomous sidewalk delivery vehicle: An exploratory study. (2021).
- [73] U.S. Department of Health and Human Services. 2018. Code of Federal Regulations, 45 CFR 46, Protection of Human Subjects. 45 CFR 46. https://www. ecfr.gov/cgi-bin/retrieveECFR?gp=&amp;SID=83cd09e1c0f5c6937cd9d7513160fc3f&amp; pitd=20180719&amp;n=pt45.1.46&amp;r=PART&amp;ty=HTML
- [75] David Weinberg, Healy Dwyer, Sarah E Fox, and Nikolas Martelaro. 2023. Sharing the Sidewalk: Observing Delivery Robot Interactions with Pedestrians during a Pilot in Pittsburgh, PA. Multimodal Technologies and Interaction 7, 5 (2023), 53.
- [77] Aidan H While, Simon Marvin, and Mateja Kovacic. 2021. Urban robotic experimentation: San Francisco, Tokyo and Dubai. Urban Studies 58, 4 (2021), 769-786.
- [76] Astrid Weiss, Regina Bernhaupt, Manfred Tscheligi, Dirk Wollherr, Kolja Kuhnlenz, and Martin Buss. 2008. A methodological variation for acceptance evaluation of human-robot interaction in public places. In RO-MAN 2008-The 17th IEEE International Symposium on Robot and Human Interactive Communication (Munich, Germany). IEEE, 713-718.
- [78] William Hollingsworth Whyte et al. 1980. The social life of small urban spaces . Conservation Foundation, Washington, DC.
- [80] Yuto Yamaji, Taisuke Miyake, Yuta Yoshiike, P Ravindra S De Silva, and Michio Okada. 2011. STB: Child-dependent sociable trash box. International Journal of Social Robotics 3, 4 (2011), 359-370.
- [79] Jesse Woo, Jan Whittington, and Ronald Arkin. 2020. Urban robotics: Achieving autonomy in design and regulation of robots and cities. Conn. L. Rev. 52 (2020), 319.
- [81] Keiichi Yamazaki, Akiko Yamazaki, Mai Okada, Yoshinori Kuno, Yoshinori Kobayashi, Yosuke Hoshi, Karola Pitsch, Paul Luf, Dirk Vom Lehn, and Christian Heath. 2009. Revealing Gauguin: engaging visitors in robot guide's explanation in an art museum. In Proceedings of the SIGCHI conference on human factors in computing systems . 1437-1446.
- [82] Stephen Yang, Brian Ka-Jun Mok, David Sirkin, Hillary Page Ive, Rohan Maheshwari, Kerstin Fischer, and Wendy Ju. 2015. Experiences developing socially acceptable interactions for a robotic trash barrel. In 2015 24th IEEE International Symposium on Robot and Human Interactive Communication (RO-MAN) . IEEE, IEEE, Kobe, Japan, 277-284.

- [83] J.D. Zamfrescu-Pereira, David Sirkin, David Goedicke, Ray LC, Natalie Friedman, Ilan Mandel, Nikolas Martelaro, and Wendy Ju. 2021. Fake It to Make It: Exploratory Prototyping in HRI. In Companion of the 2021 ACM/IEEE International Conference on Human-Robot Interaction (Boulder, CO, USA) (HRI '21

Companion) . Association for Computing Machinery, New York, NY, USA, 19-28. https://doi.org/10.1145/3434074.3446909