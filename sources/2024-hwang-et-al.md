---
stem: "2024-hwang-et-al"
pdf_path: "papers\\2024-hwang-et-al.pdf"
source_path: "sources\\2024-hwang-et-al.md"
source_hash: "7cfac6dec6abe85c18ac065791e727bcc0278c5b053167e7ececfbc99204c693"
parsed_with: "docling"
parsed_at: "2026-09-05T17:01:21+00:00"
warnings: []
---
<!-- image -->

## Innovation in Language Learning and Teaching

ISSN: 1750-1229 (Print) 1750-1237 (Online) Journal homepage: www.tandfonline.com/journals/rill20

## AI-enhanced video drama-making for improving writing and speaking skills of students learning English as a foreign language

## Wu-Yuin Hwang, Muhammad Irfan Luthfi &amp; Yi-Fan Liu

To cite this article: Wu-Yuin Hwang, Muhammad Irfan Luthfi &amp; Yi-Fan Liu (06 Dec 2024): AI-enhanced video drama-making for improving writing and speaking skills of students learning English as a foreign language, Innovation in Language Learning and Teaching, DOI: 10.1080/17501229.2024.2437655

To link to this article:

[https://doi.org/10.1080/17501229.2024.2437655](https://doi.org/10.1080/17501229.2024.2437655)

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

<!-- image -->

CrossMark Published online: 06 Dec 2024.

<!-- image -->

[Submit your article to this journal](https://www.tandfonline.com/action/authorSubmission?journalCode=rill20&show=instructions&src=pdf)

Article views: 877

[View related articles](https://www.tandfonline.com/doi/mlt/10.1080/17501229.2024.2437655?src=pdf)

[View Crossmark data](http://crossmark.crossref.org/dialog/?doi=10.1080/17501229.2024.2437655&domain=pdf&date_stamp=06%20Dec%202024)

[Citing articles: 2 View citing articles](https://www.tandfonline.com/doi/citedby/10.1080/17501229.2024.2437655?src=pdf)

<!-- image -->

<!-- image -->

<!-- image -->

## AI-enhanced video drama-making for improving writing and speaking skills of students learning English as a foreign language

<!-- image -->

<!-- image -->

Wu-Yuin Hwang a,b ,  Muhammad Irfan Luthfi b,c and  Yi-Fan Liu d

a Department of Computer Science and Information Engineering, National Dong Hwa University, Hualien, Taiwan;

c Departement of Electronics and Informatics Engineering Education, Universitas Negeri Yogyakarta, Yogyakarta, Indonesia; d National Academy for Educational Research, New Taipei, Taiwan

b Graduate Institute of Network Learning Technology, National Central University Taiwan, Taoyuan, Taiwan;

## ABSTRACT

Advanced technologies, such as artificial intelligence (AI), have been used by  teachers  to  enhance  English  as  a  Foreign  Language  (EFL)  learning. However, few studies have employed AI in the making of video dramas to  facilitate  EFL  learning.  In  this  study,  AI  was  used  to  recognize  the authentic  context  of  a  drama  and  provide  students  with  meaningful lexical resources, including vocabulary and sentence structures, to inspire  them  in  their  writing.  Video-to-text  recognition  (VTR)  and  AI methods  were  used  to  develop  an  AI-enhanced  video  drama  (AI-EVD) application  for  EFL  learning,  and  its  effectiveness  for  improving  EFL writing and speaking was investigated by recruiting 77 university students  in  three  groups:  an  experimental  group  (EG),  which  used  the app,  and  control  groups,  which  used  the  app  without  AI  features  (CG1) or  participated  in  conventional  learning (CG2).  Learning achievement in the  EG  was  significantly  higher  than  that  in  CG1  or  CG2.  An  analysis  of the  correlation  between  learning  behavior  and  learning  achievement showed that VTR-generated vocabulary, generative pretrained transformer  (GPT)-generated  sentences,  and  a  pronunciation  correction mechanism  significantly  improved  the  students'  performance.  Further analysis  with  a  stepwise  multiple  regression  model  revealed  that  the GPT-generated  sentences  feature  was  the  learning  behavior  with  the strongest  effect  on  writing  and  speaking  skills.  Moreover,  the  AI-EVD application  was  perceived  as  being  easy  to  use,  helpful,  and  engaging according to the results of student questionnaires and  interviews. Therefore,  the  AI-EVD  application  can  motivate  EFL  students,  enable them  to  produce  meaningful  video  dramas,  and  improve  their  writing and speaking skills.

## 1. Introduction

Drama-making is a dynamic approach to language learning that has gained recognition for its trans­ formative  potential  in  various  dimensions  for  EFL  students  (Angelianawati  2019;  Kovac  2016; McNaughton 2010; Moghadam and Ghafarsamar 2018; Zhang et al. 2019). Kovac (2016) suggested that  drama-making tasks involving real-time  communication and improvisation can enhance per­ ceived  fluency  by  causing  students  to  spontaneously  produce  language.  Gałązka  and  Trinder (2018) stated that drama-making can meet the basic psychological needs of EFL students and is a practical activity for fostering a supportive learning environment.

<!-- image -->

## ARTICLE HISTORY

Received 17 January 2024 Accepted 27 November 2024

## KEYWORDS

Artificial  intelligence (AI)- enhanced video drama; video recognition; generative pre-trained transformer (GPT); English as a Foreign Language (EFL); speaking and writing Artificial intelligence (AI)-enhanced technology is another novel aspect of modern language edu­ cation. It offers new possibilities for providing authentic and ubiquitous learning experiences for EFL students (Song and Song 2023; Wei 2023). AI innovations have transformed EFL teaching by provid­ ing personalized, interactive, and adaptive learning environments that enhance learners' language skills  and  motivation  (Halkiopoulos  and  Gkintoni  2024;  Jiang  2022).  AI  recognition  technologies, such as speech recognition to improve pronunciation or text generation to bolster comprehension, are essential in supporting the EFL learning process (Shadiev and Liu 2023; Shadiev and Sun 2020). Additionally,  AI  can  inspire  EFL  students  to  speak  and  write  by  providing  meaningful  lexical resources  and  generating  new  text  from  authentic  materials  (Hwang  et  al.  2023).  Xiao  and  Yue (2023)  emphasized  ChatGPT's  role  in  providing  personalized  feedback  and  promoting  autonomy and demonstrated its potential as a valuable tool for refining prompts and encouraging critical judg­ ment in language tasks. Wang and Xue (2024) found that AI-driven chatbots significantly enhanced academic  engagement  for  Chinese  EFL  students  by  improving  their  behavioral,  cognitive,  and emotional participation. These two studies highlight how AI tools, such as ChatGPT and chatbots, can enhance students' interaction and engagement in language learning. In summary, AI-enhanced technologies offer innovative tools that can transform language acquisition, providing personalized support and improving learner outcomes.

<!-- image -->

Both drama-making and recognition-based AI authentic learning are effective for EFL. Therefore, we developed an AI-enhanced video drama (AI-EVD) application to facilitate the making of EFL video dramas. We then explored its effects on EFL writing and speaking to identify the potential benefits and implications of the approach. Our proposed AI-EVD uses AI recognition technology in authentic contexts to generate meaningful texts and sentences for helping EFL students learn to write and speak.  We  conducted  experiments  to  evaluate  the  application's  performance.  EFL  students  were divided  into  three  groups:  an  experimental  group  (EG)  that  used  the  app  with  AI  features  and VTR  and  control  groups  that  used  only  VTR  (CG1)  and  that  participated  in  traditional  teaching (CG2). The research questions were as follows:

1. Does speaking and writing learning achievement significantly differ among EG, CG1, and CG2?
2. Are learning behaviors and learning achievement significantly correlated in the EG?
3. Do students perceive the AI-EVD application to be effective and useable?

This study is a key step forward in exploring how EFL students can use AI alongside drama for learning. We expect that the AI-EVD application will enhance EFL writing and speaking skills by com­ bining AI and drama-making in an authentic context. It can also make EFL learning more engaging and enjoyable for students, in turn improving their EFL writing and speaking skills.

## 2. Literature review

## 2.1. Enhancing EFL students' productive skills

Enhancing EFL students' productive skills, specifically speaking and writing, is crucial for improv­ ing  their  communication  ability.  In  recent  years,  researchers  have  performed  several  in-depth studies  on  this  topic.  These  studies  have  explored  the  use  of  YouTube  videos  for  developing speaking skills  (Saed  et  al.  2021);  the  use  of  Instagram-based  tasks  for  grammar  learning  (Teng et  al.  2022);  the  perceived  functions  of  playfulness  in  language  learning  (Barabadi  et  al.  2022); mobile  and  supervised  question-driven  collaborative  dialogs  (QDCDs)  for  improving  oral  per­ formance (Cai and Zhang 2023); flipped listening instruction for reducing anxiety and improving listening  performance  (Qiu  and  Luo  2022);  integration  of  intercultural  communicative  compe­ tence into  online  EFL  classrooms  (Lee,  Kim,  and  Sung  2023);  and  technology-enhanced  instruc­ tion  for  improving  writing  achievement  (Dousti  and  Amirian  2023).  This  variety  of  approaches demonstrates  the  wide  range  of  methodologies  that  have  been  used  to  address  different aspects  of  language  learning.  Moreover,  these  studies  highlight  how  technology  has  become central  to  these  efforts.

Saed et al. (2021) investigated the effectiveness of using YouTube videos to teach speaking skills to EFL students in Jordan. They found that pronunciation and fluency improved more in students taught with YouTube videos than in those taught using traditional methods. Similarly, Teng et al. (2022)  found  that  a  group  that  learned  grammar  through  Instagram-based  tasks  outperformed  a control group, demonstrating the effectiveness of social media tools in language learning. Barabadi et al. (2022) took the different approach of examining playfulness in language learning. They ident­ ified four categories of playfulness: fun and laughter, creativity, mastery orientation, and cultivating relationships.  These  categories  align  with  the  components  of  adult  playfulness,  and  the  study suggested that integrating playfulness into language learning can boost both interpersonal inter­ actions and language proficiency.

Cai and Zhang (2023) explored mobile and supervised QDCDs for enhancing speaking skills and found significant improvements in word production and linguistic complexity. They also noted that students' reliance on their first language (L1) decreased when they were using QDCDs, suggesting a reduction in L1 interference. Flipped instruction is another promising method and was applied by Qiu and Luo (2022) for the listening practice of Chinese EFL students; they found that it significantly improved listening performance and reduced anxiety. Lee, Kim, and Sung (2023) focused on inter­ cultural communicative competence by integrating intercultural learning into online EFL classrooms. Their study showed that this method improved students' motivation, intercultural competence, and English proficiency much more than did traditional instruction.

Finally,  Dousti  and  Amirian  (2023)  studied  the  effects  of  different  technology-enhanced instruction  methods  on  writing  achievement  in  Iranian  EFL  students.  Although  writing  skills improved  for  all  students,  the  web-mediated  and  blended  groups  outperformed  the  groups that used purely online methods. The reviewed research provides practical insights for educators by  highlighting  the  potential  benefits  of  incorporating  various  tools  and  techniques-from YouTube videos, social media, playfulness, and QDCDs to flipped instruction, intercultural com­ petence,  and  technology-enhanced  learning-to  enhance  EFL  students'  productive  skills.  The results  offer  valuable  strategies  for  practitioners  and  researchers  seeking  to  improve  language production in EFL learners.

## 2.2. Drama-making in EFL learning

Drama-making, which involves creating and performing dramatic scenes, has been recognized for its potential to enhance the language acquisition, communication skills, and pragmatic competence of EFL  learners.  Not  only  does  drama-making  provide  students  with  opportunities  for  authentic language use,  it  also  fosters  active  engagement.  Several  studies  have  highlighted  the  benefits  of drama-based  approaches,  such  as  role-playing  and  improvisation,  in  terms  of  promoting  oral fluency  and  accuracy  among  EFL  students  (Moradi  and  Ghabanchi  2019;  Omar  and  Razı  2022). Although these studies offer promising findings and contribute valuable insights into the positive effects  of  drama-making  on  the  development  of  speaking  skills,  further  studies  regarding  the impact  of  drama-making  on  fluency  and  accuracy  are  required  to  expand  understanding  of  this approach.

Building on this research, Zhang and Han (2021) investigated the effects of drama-making on the fluency and accuracy of speech in EFL learners. Their study employed a quasi experimental design involving two groups engaging in drama-making or conventional speaking exercises. The dramamaking  group  achieved  significantly  higher  fluency  levels  than  did  the  control  group;  however, the accuracy of the two groups did not significantly differ, suggesting that drama-making improves fluency but may not enhance grammar. Although drama-making can be a valuable tool for improv­ ing speaking skills, its influence on other aspects of language learning, such as grammatical accuracy, remains unclear.

4

Moreover, in addition to improving language use, drama-making may facilitate the development of intercultural communicative competence in EFL students. As Byram (1997) stated, cultural under­ standing is vital in effective language communication. Incorporating cultural elements into a drama context can enhance students' awareness of and sensitivity to different cultural perspectives. Chen et al. (2020) explored the role of drama-making in developing intercultural communicative compe­ tence for EFL students. They implemented a mixed-methods approach of combining qualitative data from  interviews  and  observations  with  quantitative  data  from  pretests  and  posttests,  and  their findings indicated that drama-making facilitated the development of intercultural communicative competence by providing opportunities for students to engage with diverse cultural contexts, chal­ lenge  stereotypes,  and  develop  empathy  for  others.  Thus,  drama-making  appears  to  offer  major benefits beyond improved language proficiency.

However, despite the advantages of drama-making, implementing it in EFL classrooms presents various challenges and limitations that must be addressed. For example, although technology and digital tools are increasingly critical in EFL, effectively integrating them into drama-based language teaching may be difficult. Peachey (2012) stated that digital technologies offer novel possibilities for incorporating multimedia elements, virtual environments, and online collaboration platforms within drama-making  activities.  However,  the  benefits  and  drawbacks  of  technology  integration  in  this context must be critically evaluated to ensure the effectiveness of such integration.

For example, Liyanawatta et al. (2022) investigated technology integration in a study on dramabased language teaching for EFL students. Their study revealed that although technology-enhanced drama-making can increase engagement, enable access to authentic resources, and provide oppor­ tunities for self-reflection, it also poses several challenges, such as technical difficulties, the need to address a lack of teacher training, and potential distractions caused by overreliance on digital tools. This study underscores the importance of carefully considering how technology can best support drama-making  activities  without  overshadowing  or  detracting  from  their  inherent  pedagogical goals.

In conclusion, integrating drama and technology into EFL instruction can enhance EFL students' fluency and intercultural communicative competence. However, as highlighted, challenges arise in achieving  effective  integration  of  drama  and  technology,  and  these  challenges  must  be  carefully managed if the full potential of this approach is to be realized.

## 2.3. AI recognition technology for EFL learning

Several studies have explored using AI recognition technologies in EFL instruction and have reported their  significant  potential  to  transform  language  learning  experiences.  For  example,  Shadiev,  Wu, and Huang (2020) demonstrated the effectiveness of image-to-text recognition technology in facil­ itating the acquisition of vocabulary in authentic contexts. Learners using AI-based systems signifi­ cantly outperformed those using traditional approaches. As AI recognition technology evolves, it will increasingly be able to deliver personalized, interactive, and adaptive learning approaches, offering real-time feedback and autonomous practice to enhance language skills (Bonneton-Botté et al. 2023; Lee and Yumi 2022). In particular, adaptive vocabulary systems (Duarte et al. 2012; Nation 2013) have been proven effective in context-specific learning environments.

In addition to AI recognition technologies, mobile-assisted language learning (MALL) is crucial in promoting situated learning. Lee, Kim, and Sung (2023) developed an AI system on the basis of the Learner-Generated  Context  (LGC)  framework  that  provides  personalized  feedback  and  adaptive content  recommendations for Korean  students.  Although  the  system  shows  promise,  they  stated that  further  research  is  necessary  to  refine  its  capabilities  for  diverse  student  populations.  Wong and Looi (2010) demonstrated that mobile devices support content creation, enabling learners to engage  in  real-world  tasks  that  foster  linguistic  development.  Similarly,  Kukulska-Hulme  and Shield  (2008)  emphasized the  benefits  of  mobile  technologies  in  creating  interactive  and  contex­ tually rich environments. Advances in AI have also been applied to language production. Warschauer and  Grimes  (2008)  showed  that  AI-powered  writing  assistants  can  help  students  improve  their grammar and  style,  and  Lee  et  al.  (2023)  developed  an  AI  chatbot  for  spoken  language  practice that  provides  immediate  feedback  on  fluency  and  accuracy.  Additionally,  AI-powered  multimedia systems and augmented reality tools are increasingly used to enhance engagement and situated learning  (Adams  Becker  et  al.  2017;  Shadiev,  Yang  and  Huang  2022;  Shih  2010;  Wang  and  Liang 2024). Xiao and Zhi (2023) explored ChatGPT in EFL learning and found that it was helpful in provid­ ing  immediate  feedback  and  personalized  learning.  Crompton  et  al.  (2024)  identified  both  the benefits and challenges of using AI in English language teaching. They noted its potential for sup­ porting speaking, writing, and self-regulation but cautioned about issues such as technology break­ downs  and  the  standardization  of  language.  These  technologies  can  reshape  how  EFL  learners interact  with  content,  and  AI's  personalization  can  be  blended  with  MALL's  real-world  relevance to create immersive, contextually rich learning environments.

<!-- image -->

Despite  the  technological  advancements,  integrating  AI  in  EFL  settings  raises  ethical  con­ cerns.  Pikhart  (2020)  highlights  issues  related  to  privacy,  data  security,  and  transparency  in algorithmic  decisions;  moreover,  bias  exists  in  machine  translation  and  speech  recognition systems.  Crompton  et  al.  (2024)  similarly  stressed  the  importance  of  ethical  considerations, noting that developers of AI systems must address concerns about equity, access, and fairness in their deployment. These challenges necessitate careful implementation to ensure ethical use and adherence to privacy regulations. Moreover, effective pedagogical design, guided by theor­ etical frameworks such as self-efficacy theory and self-regulatory learning theory, is essential for maximizing  AI's  benefits  (Lee,  Kim,  and  Sung  2023;  Pikhart  2020).  Therefore,  ethical  consider­ ations  and  robust  pedagogical  strategies  are  crucial  for  ensuring  the  responsible  use  of  AI  in educational  settings.

To  conclude,  AI  recognition  technology  has  the  potential  to  revolutionize  EFL  instruction  by offering  personalized  and  adaptive  learning  experiences  that  improve  vocabulary  acquisition, language production, and situated learning. However, addressing ethical challenges and implement­ ing sound pedagogical strategies are crucial for ensuring the responsible and effective use of AI in education.

## 3. AI-EVD application

A  video  drama  task  was  designed  for  immersing  EFL  students  in  an  authentic  language  learning context.  Students  were  tasked  with  creating  short  dramas  based  on  real-world  scenarios,  such  as classroom interactions, campus life, and food topics. The specific instructions were as follows: The students first  selected  a  topic  and  brainstormed  ideas  for  scenes  that  involved  English  communi­ cation. They were then required to film these scenes in an authentic setting, leveraging their every­ day environments to capture realistic language use (Figure 1). The students then added dialog to the filmed  scenes  that  reflected  natural  conversation  patterns  to  improve  their  speaking  and  writing skills. For example, a typical video involved students filming a scene in a campus cafeteria in which they acted out the ordering of food and interaction with staff. They later added appropriate English dialog.

Figure 1. Step-by-step process of video drama creation and language learning for EFL students.

<!-- image -->

<!-- image -->

Table 1. Comparisons of AI-EVD Features between EG and CG1.

| #                             | EG                                                                                                                                          | CG1                                                                      |
|-------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------|
| VTR-Generated Vocabulary      | Students receive AI-provided, context-related vocabulary after recording a video.                                                           | Students receive course-related vocabulary after video recording.        |
| GPT-Generated Sentences       | Students receive AI-provided, context-related example sentences after recording a video.                                                    | Students receive course-related example sentences after video recording. |
| Writing Assistant             | Students receive assistance to improve text structure, word choice, and grammar.                                                            |                                                                          |
| Speaking Correction Mechanism | Students receive scores based on fluency, accuracy, pronunciation, and overall speaking performance, with TTS for pronunciation assistance. |                                                                          |

As presented in Table 1, in the AI-EVD system used by the EG, the learning process was consider­ ably enriched by AI tools that supported the creation and refinement of both written and spoken English. The AI-EVD application featured a VTR module to analyze video footage and generate voca­ bulary and sentences, helping students write dialog for their scenes. To ensure active engagement with the material, the  students  were required  to manually input  or  modify  the  AI-generated sen­ tences. To further enhance writing, a writing assistant was included that provided real-time correc­ tions for spelling, grammar, and word choice (Figure 2).

The 'watch and apply' feature (Figure 2) allowed students to practice an English conversation by interacting with a robot; they took turns reciting dialog from the drama scenes. After they recited the dialog, a speaking correction mechanism was used to evaluate the students' pronunciation, accu­ racy,  and  fluency,  and  feedback  was  provided  (Figure  3).  When  satisfied  with  their  performance, the students moved to the next line. This method reinforced learning through real-time correction.

The core of the AI-EVD application is the making of video dramas. Specifically, the students cap­ tured videos in authentic contexts, and VTR-generated vocabulary was input to a generative GPT

Figure 2. Screenshot of the 'watch and apply' feature with which students could practice speaking lines from the drama scene with a robot.

<!-- image -->

<!-- image -->

Figure 3. Detailed speaking correction mechanism showing pronunciation feedback and performance scoring.

<!-- image -->

Figure 4. Drama dialog creator supported by VTR and GPT.

<!-- image -->

model to generate meaningful sentences. The students then created dialog from these sentences. To foster creativity, the copy and paste functionality was disabled; the students had to write the gen­ erated sentences or words manually. Moreover, the AI-EVD application included a writing assistant to correct spelling, grammar, and word choice errors. The implementation of these features is depicted in Figure 4.

The VTR-generated vocabulary, GPT-generated sentences, and 'watch and apply' feature of the AIEVD  application  empowered  the  students  to  create  and  enact  dramas  in  authentic  contexts  to improve their EFL writing and speaking skills.

<!-- image -->

## 4. Method

## 4.1. Research design

We investigated the effects of the AI-EVD application on the writing and speaking skills of 77 firstyear university students aged 18-20 years. These participants were enrolled in an English language course at a university in Taiwan; all had a basic level of English proficiency according to their initial placement tests. The students were divided into three groups: the EG, CG1, and CG2. The EG had access to the AI-EVD application's advanced features, including VTR-generated vocabulary, GPT-gen­ erated sentences, and a writing assistant. The CG1 used the AI-EVD app but could not access its AI features, whereas the CG2 completed traditional paper-based classroom activities.

The students first participated in a pretest to assess their initial speaking and writing abilities. The pretest  had  three  sections:  simple  conversation,  video  description  writing,  and  video  description speaking (Figure 5). In the simple conversation section, the students engaged in basic dialogue scen­ arios designed to test their ability to conduct everyday conversations in English. The video descrip­ tion writing section required the students to write a detailed description of a given video, focusing on their ability to express themselves coherently and use appropriate vocabulary. The video descrip­ tion  speaking  section  assessed  their  oral  communication  skills;  the  students  had  to  describe  the content of a video and were graded with a focus on their fluency, accuracy, and ability to articulate ideas clearly. Two experienced English teachers evaluated the students' performance by using stan­ dardized rubrics for assessing written and spoken English skills. The assessment criteria for writing included coherence, grammar, and vocabulary use, and those for speaking focused on pronuncia­ tion, fluency, and grammar. The pretest served as a baseline for identifying the students' progress. After the pretest, the students created video dramas regarding campus life, food, and restaurants to immerse them in real-world language scenarios and promote language acquisition through auth­ entic engagement and interaction. Before they began the drama-making, we spent a week familiar­ izing the students with the AI-EVD application. This training ensured that the students in the EG and CG1 were familiar with using the application and its features.

Figure 5. Study research design.

<!-- image -->

In weeks two and three, the EG and CG1 participated in video drama-making activities by using the AI-EVD app, whereas the CG2 engaged in traditional, paper-based classroom exercises aimed at achieving the same language learning objectives but without the aid of AI technology. All groups were instructed by the same teacher and covered the same materials during the in-class sessions, which  lasted  40  min  each.  After  class,  the  EG  and  CG1  students  were  assigned  to  work  on  their drama-making task as homework to continue applying the language skills that they had practiced during  class.  Regarding  the  drama-making  task,  the  students  in  EG  and  CG1  were  given  specific instructions  to  create  a  short  video  drama  related  to  classroom  activities,  campus  life,  or  food. They  were  asked  to  film  these  dramas  in  an  authentic,  real-world  context  and  then  use  tools  to write dialog and perform their scenes. The EG students used advanced AI tools to generate vocabu­ lary and sentences, whereas the CG1 students relied on traditional methods. The CG2 students, by contrast,  completed  traditional  paper-based  writing  and  speaking  tasks  on  the  same  topics  but without the drama-creation component. After the initial class, all groups were expected to spend additional  time  outside  of  class-around  30  to  60  min  per  day-to  complete  their  respective tasks.  The  EG  and  CG1  focused on drama creation, whereas the CG2 continued with paper-based exercises.

In weeks four and five, the students in the EG and CG1 went to the authentic settings of the video dramas  of  each  group  and  practiced  their  speaking  skills  by  recreating  the  dialog  in  each  video drama.  They  received  feedback  and  were  comprehensively  scored.  If  a  student  in  the  EG  or  CG1 received  feedback  indicating  incorrect  pronunciation,  they  used  a  speaking  correction  feature. The  CG2  continued  their  paper-based  classroom  activities  and  conventional  oral  communication practice activities during this period.

In the sixth week, the students took the posttest of their writing and speaking skills to measure their learning progress and determine the effectiveness of the AI features for language development.

Finally, the EG and CG1 completed a questionnaire and were interviewed to understand their per­ ceptions  of  the  study's  approach  to  integrating  AI  and  drama-making  through  the  AI-EVD  appli­ cation for enhancing their EFL writing and speaking skills.

We structured the research to facilitate a comprehensive evaluation of the effect of the AI-EVD application on English writing and speaking skills through a pretest, learning activities, and a postt­ est.  This  multifaceted  approach  yielded  robust  conclusions  regarding  the  efficacy  of  AI-enhanced language learning for EFL students and the potential of AI tools to enhance EFL writing and speaking in authentic contexts.

## 4.2. Data collection and analysis

We analyzed the students' interactions with the AI-EVD application and the application's effects on EFL writing and speaking (Table 2). Data were categorized as indicating learning behavior or achieve­ ment. Learning behavior data included the use of system features by students, interactions, and per­ formance  scores  during  drama  activities,  whereas  achievement  data  comprised  EFL  performance scores. Statistical analyses-including  descriptive  statistics,  analysis  of  covariance  (ANCOVA), Pearson correlation, linear regression, and Cronbach's alpha calculations-were used to identify cor­ relations between learning behavior and outcomes.

<!-- image -->

Table 2. Research Variables.

|   # | Code      | Category             | Variables                                              |
|-----|-----------|----------------------|--------------------------------------------------------|
|   1 | #vtr      | Learning Behavior    | VTR-generated vocabulary                               |
|   2 | #gpt      |                      | GPT-generated sentences used                           |
|   3 | #wr-asst  |                      | Writing assistants                                     |
|   4 | #gpt-sim  |                      | Similarity between writing and GPT-generated sentences |
|   5 | #sp-cm    |                      | Speaking correction mechanism                          |
|   6 | #sp-pract |                      | Speaking Practices                                     |
|   7 | #wr-score |                      | Score in writing                                       |
|   8 | #sp-score |                      | Score in speaking                                      |
|   9 | post-c    | Learning Achievement | Post-test score in simple conversation                 |
|  10 | post-d    |                      | Post-test score in video description writing           |
|  11 | post-s    |                      | Post-test score in video description speaking          |
|  12 | post-test |                      | Post-test score total                                  |

## 5. Results &amp; discussion

## 5.1. Learning achievement

Learning  achievement  was  measured  by  comparing  the  pretest  and  posttest  results.  The  pretest scores  of  the  three  groups  were  not  significantly  different  for  simple  conversation  ( p = 0.641), written  video  descriptions  (F = 0.275, p &gt; 0.05),  verbal  video  descriptions  (F = 0.423, p &gt; 0.05),  or overall (F = 0.529, p &gt; 0.05). This indicated that the students' EFL abilities did not differ significantly before  the  learning  activity;  this  was  also  supported  by  the  least  significant  difference  analysis (Table 3).

However,  the  posttest  results  revealed  significant  differences  between  the  three  groups  for simple  conversation  (F = 364.266, p &lt; 0.01),  written  video  descriptions  (F = 1612.322, p &lt; 0.01), verbal video descriptions (F = 1537.175, p &lt; 0.01), and overall performance (F = 1729.422, p &lt; 0.01); the LSD analysis in Table 3 confirms these differences. The students improved more in terms of con­ versation  and  writing  tasks  than  verbal  video  descriptions.  In  the  conversation  and  verbal  video description tasks, the students only read aloud sentences they had already written. The difference in results was attributable to the task structure; in the conversation task, the students selected sen­ tences that matched the conversation, which helped them organize their ideas. In the verbal video description task, they simply needed to read the descriptions; quick thinking was not necessary. This difference explains the smaller improvements in the verbal video description task compared with the conversation and writing tasks.

The effectiveness of the learning activity was also evaluated. The EG had a mean pretest score of 26.43  (standard  deviation  [SD] = 19.80)  and  a  significantly  improved  mean  score  in  the  posttest (mean = 86.35,  SD = 1.83).  The  CG1  had  a  mean  pretest  score  of  31.07  (SD = 21.50)  and  moderate posttest gains (mean = 54.65, SD = 0.79). Furthermore, the CG2 had a mean pretest score of 23.57 (SD = 22.43) but a lower posttest score (M = 28.21, SD = 5.31). This result indicated that the learning activity effectively improved learning achievement in both the EG and CG1; however, the increase was larger for the EG. This was attributable to their access to the AI features.

Table 3. Post-Hoc Comparison of the Three Groups.

|                    |                    |    |                 |            |      | 95% Confidence Interval   | 95% Confidence Interval   |
|--------------------|--------------------|----|-----------------|------------|------|---------------------------|---------------------------|
| Dependent Variable | Dependent Variable |    | Mean Difference | Std. Error | Sig. | Lower Bound               | Upper Bound               |
| Pretest Score      | 1                  |  2 | - 4.64141       | 5.12303    | .367 | - 14.7941                 | 5.5112                    |
|                    |                    |  3 | 2.85872         | 5.06949    | .574 | - 7.1878                  | 12.9053                   |
|                    | 2                  |  1 | 4.64141         | 5.12303    | .367 | - 5.5112                  | 14.7941                   |
|                    |                    |  3 | 7.50012         | 4.73000    | .116 | - 1.8736                  | 16.8739                   |
|                    | 3                  |  1 | - 2.85872       | 5.06949    | .574 | - 12.9053                 | 7.1878                    |
|                    |                    |  2 | - 7.50012       | 4.73000    | .116 | - 16.8739                 | 1.8736                    |
| Post-test Score    | 1                  |  2 | 31.70307*       | .81650     | .000 | 30.0850                   | 33.3212                   |
|                    |                    |  3 | 58.14686*       | .80797     | .000 | 56.5457                   | 59.7481                   |
|                    | 2                  |  1 | - 31.70307*     | .81650     | .000 | - 33.3212                 | - 30.0850                 |
|                    |                    |  3 | 26.44379*       | .75386     | .000 | 24.9498                   | 27.9378                   |
|                    | 3                  |  1 | - 58.14686*     | .80797     | .000 | - 59.7481                 | - 56.5457                 |
|                    |                    |  2 | - 26.44379*     | .75386     | .000 | - 27.9378                 | - 24.9498                 |

<!-- image -->

The  differences  in  the  posttest  scores  indicated  that  the  learning  activity  affected  learning achievement.  After  the  learning  activity,  the  EG  outperformed  both  the  CG1  and  CG2,  indicating that  the  EG's  learning  activity  was  the  most  effective.  This  is  consistent  with  findings  from  Qiao and Zhao (2023), who reported that AI-based instruction caused significantly greater improvements in L2 speaking skills and self-regulation in EFL learners than did traditional methods. Furthermore, the  LSD  analysis  performed  in  this  study  revealed  significant  differences  in  the  mean  posttest score  between  the  CG1  and  CG2.  The  EG  showed  the  most  improvement,  the  CG1  exhibited  a small  improvement,  and  the  performance  of  the  CG2  decreased  slightly;  this  is  similar  to  Wei's (2023) results in which AI-mediated instruction led to superior learning outcomes and greater motiv­ ation. These results emphasize the role of AI in enhancing learning achievement.

## 5.2. Correlations between learning behaviors and learning achievement in EG

To understand how the students engaged with the AI-EVD system's features, we calculated descrip­ tive statistics of the system features that are part of learning behavior. As presented in Table 4, the writing assistant was the most frequently used tool, with an average of 141.64 uses per student (SD = 45.96), indicating that the students frequently relied on assistance for their writing tasks; some stu­ dents used it nearly 200 times. Speaking practice was also used frequently, with an average count of 68.32  (SD = 20.51),  suggesting  that  the  students  actively  participated  in  improving  their  speaking skills. Feedback through the text-to-speech feature, which helped the students with pronunciation and speaking accuracy, was used an average of 67.32 times (SD = 14.14). The use of AI-generated vocabulary  was  lower,  with  an  average  of  38  uses  (SD = 2.16).  GPT-generated  sentences  had  low average use of 5.14 (SD = 1.81). Despite this low usage, the GPT-generated sentences were crucial in improving the students' writing.

The effects of the AI-EVD application in the EG were evaluated using Pearson correlation analysis (Table 5). Use of GPT-generated sentences was significantly correlated with posttest score (r = 0.951, p &lt; 0.01), particularly for description writing (r = 0.472, p &lt; 0.05), suggesting that GPT-generated sen­ tences significantly enhanced EFL writing performance. These results emphasize the valuable role of AI-generated sentences and vocabulary for enhancing student performance. Furthermore, using a writing assistant to correct writing errors was significantly correlated with description writing per­ formance (r = 0.427, p &lt; 0.05).

Speaking  practice  behavior  was  significantly  correlated  with  posttest  score  (r = 0.625, p &lt; 0.01) and simple conversation score (r = 0.558, p &lt; 0.01). Furthermore, speaking practice score was signifi­ cantly  correlated  with  the  total  posttest  score  (r = 0.680, p &lt; 0.01),  simple  conversation  score  (r = 0.542, p &lt; 0.01),  and  the  number  of  speaking  practices  (r = 0.959, p &lt; 0.01).  This  finding  indicates that the students who engaged in more active speaking practice tended to achieve higher scores on  the  posttest,  particularly  for  simple  conversation.  Use  of  the  speaking  correction  mechanism

Table 4. Descriptive Statistics of System Features Used by Students in EG.

| System Features   |   Min. |   Max |   Mean |   Std. Deviation |
|-------------------|--------|-------|--------|------------------|
| #vtr              |     35 |    45 |     38 |             2.16 |
| #gpt              |      1 |     8 |   5.14 |            1.807 |
| #wr-asst          |     48 |   196 | 141.64 |            45.96 |
| #sp-cm            |     43 |    87 |  67.32 |           14.137 |
| #sp-pract         |     34 |    98 |  68.32 |           20.506 |

#vtr: VTR-generated vocabulary; #gpt: GPT-generated sentences; #wr-asst: writing assistants; #sp-cm: speaking correction mech­ anism; #sp-pract: speaking practices.

Table 5. Pearson Correlation Between Learning Behavior and Learning Achievement.

|           | post-test   | post-s   | post-d   | post-c   | #vtr    | #gpt    | #wr-asst   | #gpt-sim   |   #sp-cm | #sp-pract   | #wr-score   |   #sp-score |
|-----------|-------------|----------|----------|----------|---------|---------|------------|------------|----------|-------------|-------------|-------------|
| post-test | 1           |          |          |          |         |         |            |            |          |             |             |             |
| post-s    | 0.19        | 1        |          |          |         |         |            |            |          |             |             |             |
| post-d    | .455*       | - 0.06   | 1        |          |         |         |            |            |          |             |             |             |
| post-c    | .826**      | - 0.131  | - 0.003  | 1        |         |         |            |            |          |             |             |             |
| #vtr      | .467*       | 0.112    | 0.324    | 0.315    | 1       |         |            |            |          |             |             |             |
| #gpt      | .951**      | 0.298    | .472*    | .719**   | 0.366   | 1       |            |            |          |             |             |             |
| #wr-asst  | - 0.159     | - 0.002  | .427*    | - 0.416  | 0.262   | - 0.185 | 1          |            |          |             |             |             |
| #gpt-sim  | - 0.06      | - 0.019  | 0.05     | - 0.089  | - 0.162 | 0.051   | - 0.293    | 1          |          |             |             |             |
| #sp-cm    | .426*       | - 0.312  | 0.171    | .513*    | 0.29    | 0.365   | - 0.218    | - 0.027    |        1 |             |             |             |
| #sp-pract | .625**      | - 0.1    | 0.36     | .558**   | 0.124   | .604**  | - 0.159    | - 0.013    |    0.268 | 1           |             |             |
| #wr-score | 0.203       | - 0.148  | 0.099    | 0.236    | 0.328   | 0.147   | 0.146      | - 0.153    |    0.111 | - 0.154     | 1           |             |
| #sp-score | .680**      | - 0.064  | .480*    | .542**   | 0.209   | .664**  | - 0.053    | - 0.055    |    0.228 | .959**      | - 0.051     |           1 |

post-test: total post-test score; post-s: post-test score in oral video descriptions; post-d: post-test score in video description writing; post-c: post-test score in simple conversation; #vtr: VTR-generated vocabulary; #gpt: GPT-generated sentences; #wr-asst: writing assistants; #gpt-sim: similarity between writing and GPT-generated sentences; #sp-cm: speaking correction mechanism; #sp-pract: speaking practices; #wr-score: writing score; #sp-score: speaking score.

*.  significant at the 0.05 level (2-tailed)

**.  significant at the 0.01 level (2-tailed)

Table 6. Regression Coefficients for Predictor Variables.

|                         | Unstandardized Coefficients   | Unstandardized Coefficients   | Standardized Coefficients   |         |      |
|-------------------------|-------------------------------|-------------------------------|-----------------------------|---------|------|
| Model                   | B                             | Std. Error                    | Beta                        | T       | Sig. |
| 1 (Constant)            | 81.215                        | .393                          |                             | 206.768 | .000 |
| GPT-generated sentences | .994                          | .072                          | .951                        | 13.746  | .000 |

was significantly  correlated  with  higher  posttest  scores  (r = 0.426, p &lt; 0.05),  particularly  for  simple conversation (r = 0.513, p &lt; 0.05). This correlation indicated that using the speaking correction mech­ anism increased posttest scores, highlighting the effectiveness of the speaking correction mechan­ ism  in  enhancing  EFL  speaking  performance.  No  correlation  was  discovered  between  learning behavior  and  posttest  verbal  video  description  score.  This  indicates  that  the  designed  learning activity  of  making  and  playing  dramas  only  strengthened  the  students'  EFL  speaking  skills  in terms of conversation.

We employed a stepwise linear regression model to explore which variables predicted the postt­ est scores. Use of GPT-generated sentences significantly enhanced the posttest score for description writing  (Table  6).  Thus,  the  AI-EVD  application,  particularly  the  GPT-generated  sentences,  signifi­ cantly improved learning achievement. This result is consistent with findings reported in the litera­ ture.  El  Shazly  (2021)  investigated  English  speaking anxiety and speaking performance and found that AI use positively influenced speaking skills (El Shazly 2021). Additionally, Chen (2024) demon­ strated  that  technology-enhanced  language  learning  effectively  reduced  public  speaking  anxiety among  EFL  learners.  Marzuki,  Rusdin,  Darwin,  and  Indrawati  (2023)  explored  the  effects  of  AI writing  tools  on  the  content  and  organization  of  students'  writing.  Hwang  and  Nurtantyana (2022) integrated multiple recognition technologies and AI to facilitate EFL writing in authentic con­ texts  and  provided  valuable  insights  into  synergies  between  technology  and  language  learning. Their subsequent research (Hwang et al. 2023) emphasized the potential of AI recognition technol­ ogies for enhancing the writing skills of EFL students in authentic contexts; this is consistent with the present  study's  findings.  Collectively,  these  findings  encourage  further  investigation  to  optimize language learning experiences with AI-enhanced tools in EFL contexts.

## 5.3. Student perceptions of the AI-EVD application

The questionnaire results (Table 7) revealed that the EG and CG1 students found the AI-EVD appli­ cation easy to use; the mean scores for the five ease-of-use items ranged from 3.90 to 4.04. Further­ more, 52 students expressed positive views regarding the AI-EVD application's usefulness, with the mean scores for relevant items ranging from 3.81 to 4.04. Although the CG1 students had slightly lower scores than the EG on several items, these differences were nonsignificant. Thus, the overall evaluation of the AI-EVD application's utility was favorable. The students in both groups had a mod­ erately positive attitude to the AI-EVD application, with the mean scores for relevant items ranging from 3.62 to 4.02. Although the mean ratings in the CG1 were slightly lower, the findings suggest that both groups had similar overall perceptions of the system.

An assessment of the students' behavior while using the AI-EVD application revealed that both the  EG  and  CG1  students  engaged  in  various  system-related  activities;  mean  scores  for  these items  ranged  from  3.85  to  4.08,  indicating  that  the  students  in  both  groups  engaged  with  the system  strongly.  Overall,  the  students  in  these  groups  positively  perceived  the  AI-EVD,  actively engaged with it, and stated that it was easy to use and useful. The differences in the mean scores between the groups were nonsignificant. Consequently, the results indicated that the AI-EVD appli­ cation  was  well-received  by  the  students  and  could  enhance  drama-making  activities.  Therefore, continuing  to  develop  and  integrate  AI-enhanced  tools  in  educational  settings  to  improve  the overall learning experience may benefit future learners.

<!-- image -->

Table 7. Perceptions of the AI-EVD ( n = 52).

|   # | Questionnaire Item                                                                     | Strongly Agree   | Agree   | Neutral   | Disagree   | Strongly Disagree   |   Mean |    SD |
|-----|----------------------------------------------------------------------------------------|------------------|---------|-----------|------------|---------------------|--------|-------|
|   1 | Using this system is easy for me.                                                      | 11.54%           | 82.69%  | 3.85%     | 1.92%      | 0.00%               |   4.04 | 0.484 |
|   2 | Learning to operate this system is simple.                                             | 9.62%            | 84.62%  | 5.77%     | 0.00%      | 0.00%               |   4.04 | 0.394 |
|   3 | I find it easy to become skillful at using this system.                                | 19.23%           | 69.23%  | 1.92%     | 9.62%      | 0.00%               |   3.98 | 0.779 |
|   4 | Interacting with this system is uncomplicated.                                         | 17.31%           | 73.08%  | 5.77%     | 3.85%      | 0.00%               |   4.04 | 0.625 |
|   5 | Using this system requires very little effort on my part.                              | 11.54%           | 75.00%  | 5.77%     | 7.69%      | 0.00%               |   3.90 | 0.693 |
|   6 | This system improves my English ability (writing and speaking).                        | 21.15%           | 69.23%  | 1.92%     | 7.69%      | 0.00%               |   4.04 | 0.740 |
|   7 | I believe this system enhances my English learning.                                    | 13.46%           | 71.15%  | 5.77%     | 9.62%      | 0.00%               |   3.88 | 0.758 |
|   8 | Using this system makes my English learning more efficient.                            | 17.31%           | 73.08%  | 1.92%     | 7.69%      | 0.00%               |   4.00 | 0.714 |
|   9 | This system helps me achieve my goals.                                                 | 13.46%           | 71.15%  | 7.69%     | 7.69%      | 0.00%               |   3.90 | 0.721 |
|  10 | I find this system valuable in my English learning.                                    | 7.69%            | 75.00%  | 7.69%     | 9.62%      | 0.00%               |   3.81 | 0.715 |
|  11 | I have a positive attitude toward using this system.                                   | 17.31%           | 69.23%  | 7.69%     | 5.77%      | 0.00%               |   3.98 | 0.700 |
|  12 | I feel favorable about the benefits this system offers.                                | 23.08%           | 61.54%  | 9.62%     | 5.77%      | 0.00%               |   4.02 | 0.754 |
|  13 | I think using this system is a good idea.                                              | 1.92%            | 73.08%  | 9.62%     | 15.38%     | 0.00%               |   3.62 | 0.771 |
|  14 | I have a generally positive feeling about this system.                                 | 11.54%           | 82.69%  | 1.92%     | 3.85%      | 0.00%               |   4.02 | 0.542 |
|  15 | I am enthusiastic about using this system.                                             | 7.69%            | 80.77%  | 3.85%     | 7.69%      | 0.00%               |   3.88 | 0.646 |
|  16 | I use this system frequently in my English learning.                                   | 5.77%            | 84.62%  | 3.85%     | 5.77%      | 0.00%               |   3.90 | 0.569 |
|  17 | I have recommended this system to others.                                              | 17.31%           | 75.00%  | 5.77%     | 1.92%      | 0.00%               |   4.08 | 0.555 |
|  18 | I have attended training sessions or sought help to improve my usage of this system.   | 7.69%            | 76.92%  | 13.46%    | 1.92%      | 0.00%               |   3.90 | 0.534 |
|  19 | I have explored advanced features or functionalities of this system beyond basic use.  | 11.54%           | 76.92%  | 5.77%     | 5.77%      | 0.00%               |   3.94 | 0.639 |
|  20 | I have made modifications or customizations to adapt this system to my specific needs. | 9.62%            | 73.08%  | 9.62%     | 7.69%      | 0.00%               |   3.85 | 0.697 |

The interview data further supported these findings. The interview findings underscore the value of  integrating  the  AI-EVD  application  into  learning  activities.  The  students  reported  increased engagement  and  motivation,  suggesting  that  technology-driven  language  learning  methods appeal  to  their  digital  preferences.  Specifically,  the  results  indicated  that  the  AI-EVD  application can  significantly  improve  oral  language  skills.  However,  the  interviews  also  revealed  limitations. For  example,  some  students  encountered  technical  issues  while  using  the  application,  such  as app  crashes,  slow  responses,  and  difficulties  with  specific  features,  including  receiving  feedback. Most  of  these  problems  were  due  to  device  limitations,  such  as  low  memory  or  old  operating systems. Others were related to server load or poor internet connectivity. Addressing these issues could improve the user experience and ensure smoother system functionality.

Another  aspect  highlighted  in  the  interviews  was  the  concern  about  overreliance  on  AI.  The students  noted  that,  although  AI  can  play  a  crucial  role  in  language  learning,  excessive  reliance on  it  could  weaken  their  ability  to  write  or  speak  independently.  This  observation  supports  the need  for  a  balanced  approach  to  language  learning.  Because  of  this  potential  concern,  the study  was  designed  to  focus  on  pragmatic  competence  by  deliberately  removing  features,  such as  copy-paste,  that  might  have  fostered  overreliance  on  AI.  Instead,  the  students  had  to  write or  speak  all  of  the  vocabulary  and  sentences  themselves.  This  intentional  design  choice  may have  contributed  to  the  effectiveness  of  the  app  in  enhancing  both  the  learners'  speaking  and writing  skills.

## 6. Conclusion

This study explored the effect of the AI-EVD application on the language skills and behaviors of EFL students. The improvement of the EG between the pretest and posttest was significantly larger than that of the control groups in terms of speaking and writing, highlighting the effectiveness of the AIEVD application. Various app-based learning behaviors, such as using AI-generated sentences, were correlated with improvements in language skills. The most impactful behavior was the use of GPT to generate sentences. The student participants stated that using the AI-EVD application was easy and beneficial;  they  particularly  appreciated  its  instant  feedback  and  reported  that  it  increased  their motivation.  However,  they  raised  concerns  about  technical  issues  and  dependence  on  AI.  These insights suggest the AI-EVD application's potential in language learning but caution that a balanced approach should be taken to promote human interaction.

This  study  demonstrated  that  the  AI-EVD  application  improves  language  skills,  particularly  in speaking  and  writing.  Limitations  affecting  its  generalizability  include  a  focus  on  language  skills, the  short  duration  of  the  study,  and  the  study's  limited,  specific  student  sample.  Future  research could involve longitudinal studies, more diverse samples, and studies comparing AI-based and tra­ ditional language learning methods. This could lead to refinement of the AI-EVD application and its integration into teaching, maximizing student benefits. Despite its limitations, this study greatly con­ tributes to research on AI in language learning, indicating the potential of AI for enhancing education.

## Acknowledgments

I extend my gratitude to the reviewer, advisors, the High Interaction in Multimedia Lab team, the Research Assistants in Videoto-Text Recognition, the EFL Study group, as well as the teachers and students of Yuan Ze University who were involved.

## Disclosure statement

No potential conflict of interest was reported by the author(s).

## Funding

This work was supported by National Science and Technology Council of the Republic of China: [Grant Number MOST 112-2410-H-656 -010-, 113-2410-H-656 -012 -].

## Notes on contributors

Wu-Yuin Hwang Dr. Wu-Yuin Hwang is a Professor affiliated with both the Department of Computer Science and Infor­ mation Engineering, College of Science and Engineering, National Dong Hwa University, Taiwan, and the Institute of Network Learning Technology, National Central University, Taiwan. His current research interests are related to the inte­ gration of IOT, AI, and multimedia sensors of mobile devices for learning and interactions among humans and all things in AR contexts like smart buildings and campuses. Dr. Hwang received the Outstanding Research Award, from the Min­ istry of Science and Technology, Taiwan in 2021. He is also ranked in the top 7 scholars of the world in terms of highquality journal publication performance of instructional design and technology.

Muhammad Irfan Luthfi is a Ph.D. student at the Graduate Institute of Network Learning Technology, College of Elec­ trical  Engineering  &amp;  Computer  Science,  National  Central  University,  ROC,  Taiwan.  He  received  B.Ed.  Degree  in  Infor­ matics Engineering Education from the Faculty of Engineering, Universitas Negeri Yogyakarta, Indonesia &amp; obtained M.Ed. Degree in Informatics Engineering Education from the Graduate School of Electronics and Informatics Engineer­ ing Education, Universitas Negeri Yogyakarta, Indonesia. He also obtained M.Sc. in Network Learning Technology from the College of Electrical Engineering &amp; Computer Science, National Central University, Taiwan. He is also working as a lecturer at the Faculty of Engineering, Universitas Negeri Yogyakarta, Indonesia. His research interests are in the areas of Human-Computer Interaction, Software Engineering, and Computer Vision.

Yi-Fan Liu serves as an Associate Research Fellow at the Research Center for Testing and Assessment, which is part of the National Academy for Educational Research in New Taipei City, Taiwan. His research primarily focuses on Technol­ ogy-assisted  Language  Learning,  note-taking  behaviors,  human  factors  in  learning,  and  mobile  learning.  This background indicates a comprehensive engagement with the intersection of technology and education, particularly in the context of language acquisition and the cognitive processes involved in learning.

<!-- image -->

## ORCID

Muhammad Irfan Luthfi http://orcid.org/0000-0001-8806-9704 Yi-Fan Liu http://orcid.org/0000-0002-1238-8749

## References

- Adams  Becker, Samantha,  Michael Cummins,  Alex Davis, Allan Freeman, Camille Hall Giesinger, and Vibha Ananthanarayanan. 2017. NMC Horizon Report: 2017 Higher Education Edition . Austin, TX: The New Media Consortium. Angelianawati, Lilis. 2019. 'Using Drama in EFL Classroom.' Journal of English Teaching 5 (2): 125-134. https://doi.org/10. 33541/jet.v5i2.1066.
- Barabadi,  Ehsan,  Mohammad,  Elahi  Shirvan,  Mahsa,  Shahnama,  and  Rene  T.  Proyer.  2022.  'Perceived  Functions  of Playfulness  in  Adult  English  as  a  Foreign  Language  Learners:  An  Exploratory  Study.' Frontiers  in  Psychology 12:823123. https://doi.org/10.3389/fpsyg.2021.823123.
- Bonneton-Botté, Nathalie, Laura, Miramand, Romain, Bailly and Christophe, Pons 2023. 'Teaching and Rehabilitation of Handwriting for Children in the Digital Age: Issues and Challenges.' Children (Basel) 10 (7): 1096. https://doi.org/10. 3390/children10071096.
- Byram, Michael. 1997. ''Cultural Awareness' as Vocabulary Learning.' Language Learning Journal 16 (1): 51-57. https:// doi.org/10.1080/09571739785200291.
- Cai, Ying, and Lawrence Jun Zhang. 2023. 'Effects of Mobile-Supervised Question-Driven Collaborative Dialogues on EFL Students' Communication Strategy Use and Academic Oral English Performance.' Frontiers in Psychology 14:1142651. https://doi.org/10.3389/fpsyg.2023.1142651.
- Chen, Yu-Chih. 2024. 'Effects of Technology-Enhanced Language Learning on Reducing EFL Learners' Public Speaking Anxiety.' Computer Assisted Language Learning 37 (4): 789-813. https://doi.org/10.1080/09588221.2022.2055083.
- Chen, I-Chun, Gwo-Jen, Hwang, Chun-Lan, Lai, and Wen-Chih, Wang. 2020. 'From Design to Reflection: Effects of PeerScoring and Comments on Students' Behavioral Patterns and Learning Outcomes in Musical Theater Performance.' Computers &amp; Education 150:103856. https://doi.org/10.1016/j.compedu.2020.103856.
- Crompton,  Helen,  Amy  Edmett,  Natasha  Ichaporia,  and  David  Burke.  2024.  'AI  and  English  Language  Teaching: Affordances and Challenges.' British  Journal  of  Educational  Technology 55 (6): 2503-2529. https://doi.org/10.1111/ bjet.13460.
- Dousti, Mohsen, and Zahra. Amirian. 2023. 'The Effect of Web-Mediated, Blended, and Purely Online Learning on EFL Students' Writing Achievement  in  the Iranian Context: A  Comparative  Study.' Education and Information Technologies 28 (2): 1675-1696. https://doi.org/10.1007/s10639-022-11215-0.
- Duarte Carlos, Luís Carriço, Joaquim Jorge, Sharon Oviatt, Daniel Gonçalves, Carrie Demmans Epp, Justin Djordjevic, Shimu Wu, Karyn Moffatt, and Ronald M, Baecker. 2012. 'Towards Providing Just-in-Time Vocabulary Support for Assistive  and  Augmentative  Communication.' In Proceedings of the 2012 ACM  International Conference on Intelligent  User Interfaces ,  33-36. https://doi.org/10.1145/2166966.2166973.
- El Shazly, Rania. 2021. 'Effects of Artificial Intelligence on English Speaking Anxiety and Speaking Performance: A Case Study.' Expert Systems 38:e12667. https://doi.org/10.1111/exsy.12667.
- Gałązka, Anna, and Marius. Trinder. 2018. 'Creating a 'Positive Environment' Through Drama in the EFL Classroom.' The New Educational Review 54: 193-205. https://doi.org/10.15804/tner.2018.54.4.16.
- Halkiopoulos,  Constantinos,  and  Evgenia  Gkintoni.  2024.  'Leveraging  AI  in  E-Learning:  Personalized  Learning  and Adaptive Assessment through Cognitive Neuropsychology-A Systematic Analysis.' Electronics 13 (18): 3762. https://doi.org/10.3390/electronics13183762.
- Hwang,  W.  -Y.,  and  R.  Nurtantyana.  2022.  'The  Integration  of  Multiple  Recognition  Technologies  and  Artificial Intelligence  to  Facilitate  EFL  Writing  in  Authentic  Contexts.'  In 2022  6th  International  Conference  on  Information Technology (InCIT) ,  379-383. Nonthaburi, Thailand.
- Hwang,  W.-Y.,  R.  Nurtantyana,  Y.-F.  Lai,  I.-C.  N.  Chiang,  G.  Ghenia,  and  M.  H.  M.  Tsai.  2023.  'The  Combination  of Recognition  Technology  and  Artificial  Intelligence  for  Questioning  and  Clarification  Mechanisms  to  Facilitate Meaningful EFL Writing in Authentic Contexts.' In Innovative  Technologies  and  Learning.  ICITL  2023.  Lecture  Notes in  Computer Science ,  edited by Y. M. Huang and T. Rocha. Cham: Springer.
- Jiang, Rui. 2022. 'How Does Artificial Intelligence Empower EFL Teaching and Learning Nowadays? A Review on Artificial Intelligence in the EFL Context.' Frontiers in Psychology 13, https://doi.org/10.3389/fpsyg.2022.1049401.
- Kovac, Miroslav M. 2016. 'The Influence of Task Type on Perceived Fluency.' Studies in English Language Teaching 4 (2), https://doi.org/10.22158/selt.v4n2p241.

<!-- image -->

- Kukulska-Hulme, Agnes, and Lesley Shield. 2008. 'An Overview of Mobile Assisted Language Learning: From Content Delivery to Supported Collaboration and Interaction.' ReCALL 20 (3): 271-289. http://dx.doi.org/10.1017/ S0958344008000335.
- Lee, Ji Young, and Yu Mi, Hwang. 2022. 'A Meta-Analysis of the Effects of Using AI Chatbot in Korean EFL Education.' Studies in English Language &amp; Literature 48 (1): 213-243. https://doi.org/10.21087/nsell.2022.11.83.213.
- Lee, Dongjun, Hyun Hye, Kim and Sang Hoon, Sung. 2023. 'Development Research on an AI English Learning Support System to Facilitate Students'-Generated-Context-Based Learning.' Educational Technology Research and Development 71 (2): 629-666. https://doi.org/10.1007/s11423-022-10172-2.
- Liyanawatta, Malshani, Shan Hua, Yang, Yi Ting, Liu, Yao, Zhuang, and Gwo-dong Chen. 2022. 'Audience Participation Digital  Drama-Based  Learning  Activities  for  Situational  Learning  in  the  Classroom.' British  Journal  of  Educational Technology 53 (1): 189-206. https://doi.org/10.1111/bjet.13160.
- Marzuki, Utami Widiati, Diyenti Rusdin, Darwin, and Inda Indrawati. 2023. 'The Impact of AI Writing Tools on the Content and Organization of Students' Writing: EFL Teachers' Perspective.' Cogent Education 10 (2), https://doi.org/10.1080/ 2331186X.2023.2236469.
- McNaughton, Marie J. 2010. 'Educational Drama in Education for Sustainable Development: Ecopedagogy in Action.' Pedagogy, Culture &amp; Society 18 (3): 289-308. https://doi.org/10.1080/14681366.2010.505460.
- Moghadam,  Saeed  M.,  and  Reza.  Ghafarsamar.  2018.  'Using  Drama  and  Drama  Techniques  to  Teach  English Conversations  to  EFL  Learners.' Global  Journal  of  Foreign  Language  Teaching 8  (2):  92-101.  https://doi.org/10. 18844/gjflt.v8i2.3319.
- Moradi, Elham, and Zargham Ghabanchi. 2019. 'Intercultural Sensitivity: A Comparative Study among Business English Undergraduate Learners in two Countries of Iran and China' Journal  of  Ethnic  and  Cultural  Studies 6 (3):  134-146. https://doi.org/10.29333/ejecs/278.
- Nation, I. S. P. 2013. 'My Ideal Vocabulary Teaching Course.' In Case Studies in Language Curriculum Design , edited by J. Macalister and I. S. P. Nation, 49-62. New York: Routledge.
- Omar, Fauziah R., and Özlem. Razı. 2022. 'Impact of Instruction Based on Movie and TV Series Clips on EFL Students' Pragmatic  Competence:  Speech  Acts  in  Focus.' Frontiers  in  Psychology 13:  974757.  https://doi.org/10.3389/fpsyg. 2022.974757.
- Peachey, Peter. 2012. 'The 'Pleasure Principle' in Blended Learning Approaches.' In Blended Learning Environments for Adults: Evaluations and Frameworks ,  75-91. IGI Global, https://doi.org/10.4018/978-1-4666-0939-6.ch005.
- Pikhart, Marcel. 2020. 'Intelligent Information Processing for Language Education: The Use of Artificial Intelligence in Language Learning Apps.' Procedia Computer Science 176: 1412-1419. https://doi.org/10.1016/j.procs.2020.09.151.
- Qiao, Hui, and An. Zhao. 2023. 'Artificial Intelligence-Based Language Learning: Illuminating the Impact on Speaking Skills  and  Self-Regulation  in  Chinese  EFL  Context.' Frontiers  in  Psychology 14:  1255594.  https://doi.org/10.3389/ fpsyg.2023.1255594.
- Qiu, Yan, and Wei. Luo. 2022. 'Investigation of the Effect of Flipped Listening Instruction on the Listening Performance and Listening Anxiety of Chinese EFL Students.' Frontiers in Psychology 13: 1043004. https://doi.org/10.3389/fpsyg. 2022.1043004.
- Saed,  Hamza  A.,  Ali  S.,  Haider,  Saed  Al-Salman,  and  Rafat  F  Hussein.  2021.  'The  Use  of  YouTube  in  Developing  the Speaking Skills of Jordanian EFL University Students.' Heliyon 7 (7): e07543. https://doi.org/10.1016/j.heliyon.2021. e07543.
- Shadiev, Rustam, and Jen W. Liu. 2023. 'Review of Research on Applications of Speech Recognition Technology to Assist Language Learning.' ReCALL 35 (1): 74-88. https://doi.org/10.1017/S095834402200012X.
- Shadiev, Rustam, and Aiqun. Sun. 2020. 'Using Texts Generated by STR and CAT to Facilitate Student Comprehension of Lecture Content in a Foreign Language.' Journal of Computing in Higher Education 32 (3): 561-581. https://doi.org/10. 1007/s12528-019-09246-7.
- Shadiev, Rustam, Ting-Ting Wu, and Yueh-Min Huang. 2020. 'Using Image-to-Text Recognition Technology to Facilitate Vocabulary Acquisition in Authentic Contexts.' ReCALL 32 (2): 195-212. https://doi.org/10.1017/S0958344020000038.
- Shadiev,  Rustam,  Liuxin  Yang,  and  Yueh  Min  Huang.  2022.  'A  Review  of  Research  on  360-degree  Video  and  its Applications to Education.' Journal of Research on Technology in Education 54 (5): 784-799.
- Shih,  Ru-Chu.  2010.  'Blended  Learning  using  Video-based  Blogs:  Public  Speaking  for  English  as  a  Second  Language Students.' Australasian Journal of Educational Technology 26 (6). http://dx.doi.org/10.14742/ajet.1048.
- Song,  Chang,  and  Yuan  Song.  2023.  'Enhancing  Academic  Writing  Skills  and  Motivation:  Assessing  the  Efficacy  of ChatGPT in AI-Assisted  Language  Learning  for  EFL  Students.' Frontiers  in  Psychology ,  14,  https://doi.org/10.3389/ fpsyg.2023.1260843.
- Teng, Chih, Taha Heydarnejad, Mohamad K. Hasan, Atheer Omar, and Laiq Sarabani. 2022. 'Mobile Assisted Language Learning  in  Learning  English  Through  Social  Networking  Tools:  An  Account  of  Instagram  Feed-Based  Tasks  on Learning  Grammar  and  Attitude  among  English  as  a  Foreign  Language  Students.' Frontiers in Psychology 13:1012004. https://doi.org/10.3389/fpsyg.2022.1012004.
- Wang, Yuhui, and Liang Xue. 2024. 'Using AI-Driven Chatbots to Foster Chinese EFL Students' Academic Engagement: An Intervention Study.' Computers in Human Behavior 159:108353. https://doi.org/10.1016/j.chb.2024.108353.

<!-- image -->

- Warschauer,  Mark,  and  Douglas  Grimes.  2008.  'Automated  Writing  Assessment  in  the  Classroom.' Pedagogies:  An International Journal 3 (1): 22-36. http://dx.doi.org/10.1080/15544800701771580.
- Wei, Li. 2023. 'Artificial Intelligence in Language Instruction: Impact on English Learning Achievement, L2 Motivation, and Self-Regulated Learning.' Frontiers in Psychology 14:1261955. https://doi.org/10.3389/fpsyg.2023.1261955.
- Wong, Lung-Hsiang, and Chee-Kit Looi. 2010. 'Vocabulary Learning by Mobile-Assisted Authentic Content Creation and Social Meaning-Making: Two Case Studies.' Journal of Computer Assisted Learning 26 (5): 421-433. https://doi.org/10. 1111/j.1365-2729.2010.00357.x.
- Xiao,  Yan,  and  Yue.  Zhi.  2023.  'An  Exploratory  Study  of  EFL  Learners'  Use  of  ChatGPT  for  Language  Learning  Tasks: Experience and Perceptions.' Languages 8 (3): 212. https://doi.org/10.3390/languages8030212.
- Zhang, Huan, and Xianghua. Han. 2021. 'Influence of Vocalized Reading Practice on English Learning and Psychological Problems of Middle School Students.' Frontiers in Psychology 12: 709023. https://doi.org/10.3389/fpsyg.2021.709023.
- Zhang, Huan, Wu-Yuin Hwang, Shiang-Yi Tseng, and Hung-Shan Chen. 2019. 'Collaborative Drama-Based EFL Learning in Familiar Contexts.' Journal of Educational Computing  Research 57 (3): 697-722.  https://doi.org/10.1177/ 0735633118757731.
