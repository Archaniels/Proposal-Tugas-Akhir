---
name: research-proposal-writing
description: Plan, draft, critique, and improve research proposals (usulan penelitian / proposal Tugas Akhir), including the title, abstract, introduction, literature review, methodology, timeline, budget, references, and appendices. Use this skill whenever the user mentions a research proposal, thesis or final-project (Tugas Akhir / TA) proposal, problem statement, research question, research gap, literature review, methodology section, desk evaluation, seminar proposal, or asks to narrow a topic, test a research question, check alignment between problem, method and analysis, or review a proposal draft. Also use it for the Telkom University Faculty of Informatics course "Penulisan Proposal" (CCK4CAB2, S1 Rekayasa Perangkat Lunak), even if the user only says "help me with my proposal", "my LR assignment", or "DE". Trigger on research-planning tasks in general, not only when the word "proposal" appears.
---

# Research Proposal Writing

This skill turns an AI agent into a disciplined research-proposal collaborator. It encodes the reasoning behind good proposals (what reviewers look for, why proposals get sent back) so the agent can draft, coach, and critique, not just fill in templates.

Source material: two lecture decks for *Penulisan Proposal* (CCK4CAB2), Fakultas Informatika, Telkom University: "Research Proposal Writing" (Meeting 1 of 4) and the course-administration deck for S1 Rekayasa Perangkat Lunak (edited September 2026). Part 1 is general and applies to any discipline. Part 2 is specific to that course and should be applied only when the user is in it.

## How to use this skill

1. Identify which mode the user needs (see "Choose a mode").
2. Read the relevant sections below; do not dump the whole skill on the user.
3. Ask at most one clarifying question if a blocking fact is missing (topic, level, institution template). Otherwise state your assumption in one line and proceed.
4. Always run the Golden Thread alignment check (Section 8) before declaring any draft finished.
5. Follow the integrity rules (Section 12). They are non-negotiable, especially for citations.

## Choose a mode

| User says or needs | Mode | Go to |
|---|---|---|
| "I have a topic / idea" | Narrow the topic into a researchable question | Sections 9, 10, 11 |
| "Review my draft / proposal" | Critique against failure patterns and alignment | Sections 8, 13, 14 |
| "Write my introduction / abstract / methods / title" | Section drafting | Sections 4, 5, 6, 7 |
| "Find literature / write the literature review" | Literature workflow | Section 6 and Section 12 |
| "What is expected in the course, deadlines, grading?" | Course context | Part 2 |
| "Explain what a proposal is" | Teaching mode | Sections 1, 2, 3 |

---

# PART 1: General principles of research proposal writing

## 1. What a research proposal is

A research proposal is a **structured, persuasive, prospective** document describing an investigation that has not yet been carried out, and arguing that the work is worth doing, can be done, and that the author is able to do it.

- **Structured**: it follows conventions readers already expect. An invented format costs credibility; it earns no points for originality. Save originality for the ideas.
- **Persuasive**: it is an argument, not a neutral description. Every section is evidence that the study deserves approval, time, and resources.
- **Prospective**: it describes work in the future tense. There are no findings, only a defensible plan and a justified expectation.

### The three claims

Every section exists to support one of three claims. **A paragraph that supports none of them does not belong in the document.** Use this as the cutting test when editing.

| Claim | Reader's question | Evidence the proposal must supply |
|---|---|---|
| This is **worth doing** | "So what?" | A real, bounded problem; prior work has not settled it (a gap); someone benefits from an answer |
| This **can be done** | "Really?" | Scope fits the time; access to data or participants is secured; resources and skills are in place |
| This is **the right way to do it** | "How?" | Method matches the question; procedures are specific enough to repeat; limits are acknowledged, not hidden |

### What a proposal does for the author

1. Secures approval (supervisors, committees, ethics boards, funders).
2. Becomes the working plan (what to read, whom to contact, what to collect, and when).
3. Sets the scope (records what was agreed, and just as usefully, what was not).
4. Attracts early critique (a weakness found at proposal stage costs a paragraph; found later it costs a semester).

Heuristic: *a proposal is cheap to change and expensive to ignore.*

## 2. Who reads it, and what they ask

| Reader | Behaviour | Questions |
|---|---|---|
| Supervisor and examiners | Expert in the field, not in the exact topic | Is the problem genuinely researchable? Does the student understand the literature? Can this be finished on time? |
| Reviewers and ethics boards | Read many documents quickly against a fixed checklist | Are participants protected? Is the method defensible? Does it meet institutional requirements? |
| The author, six months later | The reader everyone forgets | What exactly did I promise? What was the analysis plan? Why did I choose this design? |

Write so all three are served. The third reader is why decisions need their *reasons* written down.

### The first five minutes

Experienced readers judge early. Within roughly the first two pages a reader should be able to answer:

1. What exactly is the problem being addressed? (clear problem statement, defined scope)
2. Why does it matter, and to whom? (significance, beneficiaries)
3. What is already known, and what is still missing? (literature context, gap)
4. What will the researcher actually do, step by step? (feasible plan, logical method)
5. Can it be finished with the time, access, and resources available? (feasibility, acknowledged risks)

If these are not answerable after two pages, the rest is rarely read with patience. When drafting or reviewing an introduction, test it against these five questions explicitly.

## 3. Proposal versus final thesis or report

The two share structure but do different work. Most weak first drafts fail because they mix them.

| Aspect | Research proposal | Final thesis / report |
|---|---|---|
| Time frame | Work that has not happened yet | Work that has been completed |
| Dominant tense | Future: "data **will be** collected" | Past: "data **were** collected" |
| Purpose | Convince a reader to approve; guide the author's work | Report findings and defend the interpretation |
| Findings | None; only expected outcomes and their significance | Actual results with analysis and discussion |
| Risk | Feasibility argued in advance; contingencies stated | Limitations reported honestly after the fact |
| Length | Short, often 10 to 25 pages (institution-dependent) | Long; the full account |

Rule for the agent: never write results, "findings showed", or past-tense data collection into a proposal. Use future tense for the plan and present tense for established facts from the literature.

### Types of proposal (conventions differ, the argument does not)

- **Undergraduate thesis**: shortest form; a clear, narrow problem and a method the student can execute alone in one or two semesters.
- **Master's thesis**: a defensible gap in the literature and analytical depth, not only description.
- **Doctoral proposal**: an original contribution to knowledge that survives a formal defence.
- **Grant or funding proposal**: adds budget justification, deliverables, and impact; judged competitively.
- **Ethics committee submission**: narrower; participants, consent, risk, and data handling.
- **Institutional or applied study**: written for a client; usefulness is weighted as heavily as rigour.

Always check the user's own institution template first. Section names and order vary; the functions do not.

## 4. Standard structure

Three parts guide the reader from context to plan to evidence.

**Front matter** (orientation; read first, written last)
- Title page: identifies the work and author.
- Abstract: summary of problem, method, expected outcomes.
- Table of contents: navigation map.

**The body** (the argument itself)
1. Introduction: context, problem statement, objectives, significance.
2. Literature review: what is known, what is missing, why the study is needed.
3. Methodology: design, data, participants, procedures, analysis plan.

**Back matter** (evidence of planning and rigour)
- Timeline: schedule of activities and milestones.
- Budget (if required): resources and cost justification.
- References: sources cited.
- Appendices: supporting documents and tools.

Flow: front matter sets the stage, the body makes the case, back matter proves it is feasible and well planned.

### Title

The title is read by everyone and re-read by no one. It should name the variables or phenomenon, the population, and the context, and signal the design or relationship examined.

A good title is **specific, informative, concise (usually under 15 to 20 words), searchable, and sober** (no slogans, no questions, no promotional adjectives).

- Too broad: "A Study About Social Media and Students".
- Bounded and searchable: "Short-Term Video Use and Sleep Quality Among Undergraduate Students in Bandung".

Test: could a stranger predict your method and population from the title alone?

### Abstract (write it last, typically 150 to 300 words)

Five moves, in order:

1. **Context**: one or two sentences on the situation the reader must accept as real.
2. **Problem**: the specific gap, tension, or unanswered question, not the general area.
3. **Aim**: what the study sets out to do, and its main question.
4. **Method**: design, participants, and how data will be produced.
5. **Contribution**: what will be known or usable once the study is finished.

If the abstract cannot be written clearly, the problem is usually in the proposal, not the abstract. Treat a hard-to-write abstract as a diagnostic signal and go back to Sections 9 to 11.

## 5. Section 1: The Introduction

**Job**: convince the reader that a specific problem exists and deserves attention.

Typical components:
- **Background**: the wider situation, established with citations.
- **Problem statement**: the specific difficulty or unknown.
- **Research questions and objectives**: what will be answered or achieved.
- **Scope and delimitations**: what is deliberately excluded.
- **Significance**: who benefits from an answer.
- **Definition of key terms**: defined once, used consistently.

Shape it as a **funnel** that only narrows: broad context, general issues, specific problem, focused aim, research question. Never reverse the direction. Write for a smart reader outside the exact field.

Agent checklist for a drafted introduction:
- Does the problem statement appear explicitly (not implied)?
- Is the problem supported by a citation, data, or documented practice?
- Does every research question follow from the stated problem?
- Are scope limits stated?
- Would an outsider know why this matters after page two?

## 6. Section 2: The Literature Review

**Job**: show what is already known, and prove the problem is genuinely unresolved.

What it must achieve:
- **Map the field**: main positions, findings, debates (key theories, major studies, common methods).
- **Synthesize**: group sources by idea, not one paragraph per article; compare, contrast, connect.
- **Establish the gap**: what has not been settled and why it matters (contradictions, limitations, missing populations or contexts).
- **Build the framework**: the conceptual or theoretical lens (key constructs and how they relate).
- **Justify your choices**: why the chosen methods fit the literature.

**Synthesis, not summary.** A chain of "Author A said... Author B said..." is a reading list, not a review. When drafting, organize by theme, then state the gap.

Recommended agent workflow:
1. Search systematically (see search hygiene below), collecting candidate sources.
2. Read efficiently; record for each source: problem, purpose or core idea, method or algorithm, advantages and limitations, relation to the user's topic.
3. Cluster sources thematically.
4. Write the gap statement: what is known, what is not, and why the user's study addresses it.

Search hygiene (integrity-critical):
- Prefer indexed journal articles and authoritative books in the user's field.
- Verify that each source exists (title, authors, year, venue, DOI where available) using search or fetch tools before citing it.
- Never invent authors, years, DOIs, or findings. If a source cannot be verified, say so and omit it.
- Do not reproduce long passages; paraphrase and cite.
- Recommend a reference manager from day one; reconstructing citations at the end costs far more than it saves.

## 7. Section 3: The Methodology

**Job**: describe the plan in enough detail that another competent researcher could carry it out. Clarity equals credibility.

Six components:
1. **Research design**: qualitative, quantitative, or mixed, and why that choice fits the question.
2. **Participants and sampling**: population, sampling technique, sample size, how access is obtained.
3. **Instruments**: questionnaires, interview protocols, tests, observation schedules, with validity evidence.
4. **Procedure**: sequence of steps from first contact to final data set.
5. **Analysis plan**: specific techniques or analytical framework applied to the data.
6. **Ethics and rigour**: consent, confidentiality, approval, and how trustworthiness is protected.

The research process at a glance: Design, Sample, Measure, Analyze, Report.

Quality test: imagine handing the methodology to another researcher. If they would have questions, add detail. "Data will be analysed using thematic analysis" alone is too vague; specify procedure, coder(s), framework, and decision rules.

For software-engineering and informatics topics, the same logic applies to design-and-build studies: state the requirements source, the algorithm or method, datasets or test subjects, evaluation metrics, baselines for comparison, and how the solution will be validated. The method must produce evidence that answers the research question.

## 8. The Golden Thread (coherence)

Each element must follow from the one before it. Misalignment between question and method is the single most common structural failure.

Chain: **Problem, Questions, Literature, Method, Analysis, Contribution.** If one link is weak the whole chain breaks.

Alignment check (run on every draft):

| Check | What good looks like |
|---|---|
| Does every research question come directly from the stated problem? | Questions are specific, answerable, and necessary |
| Does the literature review discuss the concepts the questions actually use? | Sources inform the variables and framework |
| Can the chosen method produce data that answers those exact questions? | Method fits the question, not the reverse |
| Does the analysis plan match the type of data the method produces? | Techniques suit the data and objectives |

Final read-through: reread left to right; each section should feel like the only logical next step. When reporting alignment problems, name the two elements that fail to connect and propose a specific fix (change the question, change the method, or add the missing literature).

## 9. From topic to researchable question

A topic is what you are interested in. A research question is what you can answer with evidence. Narrow in four steps:

1. **Topic**: online learning (broad area of interest).
2. **Focused area**: student engagement in online learning.
3. **Problem**: engagement drops sharply in asynchronous courses, but the reasons are not well established in the Indonesian context.
4. **Question**: how are feedback timing and peer interaction related to student engagement in asynchronous undergraduate courses?

Each step should make the focus smaller, clearer, and more answerable: broad, then specific, then clear, then answerable. Narrow further than feels comfortable; scope is the most common cause of a study that never finishes.

### What makes a problem researchable (five qualities)

1. **Bounded**: it has edges; you can say what is inside and what is left out.
2. **Supported by evidence**: something citable shows the problem exists (data, prior studies, documented practice).
3. **Answerable with data**: settled by observation or measurement, not only opinion.
4. **Not already settled**: existing work has not answered it, or only in a different context.
5. **Consequential**: someone (a field, an institution, a group) is better off once it is answered.

A problem that is too broad, unsupported, opinion-based, already solved, or inconsequential will struggle.

### FINER test for a research question

| Letter | Criterion | Ask |
|---|---|---|
| F | Feasible: answerable with the time, participants, funding, expertise actually available | Do I have what I need? |
| I | Interesting: worth the attention of supervisor, field, and the author for a whole semester | Will I stay motivated? |
| N | Novel: adds a new population, context, variable, method, or a needed confirmation | What new knowledge will it create? |
| E | Ethical: no harm to participants; will pass institutional review | Is it the right thing to do? |
| R | Relevant: connects to real concerns in the discipline, practice, or policy | Who will care about the answer? |

Procedure: write the draft question, run it through F-I-N-E-R, revise until it earns all five. A question that fails one letter will likely fail the proposal later.

### Questions, objectives, and hypotheses

| Statement | Function | Form | Example |
|---|---|---|---|
| Research question | What you want to find out | Interrogative; one main question plus two or three sub-questions | How is feedback timing related to student engagement in asynchronous undergraduate courses? |
| Objective | What you will do to answer it | Action, beginning with an infinitive verb (to examine, to compare, to describe) | To examine the relationship between feedback timing and student engagement in asynchronous courses. |
| Hypothesis | What you expect to find, stated so it can be tested | Testable statement; only where the design allows testing (not most qualitative studies) | Students receiving feedback within 24 hours show higher engagement than those receiving it after 72 hours. |

They lead into one another: ask a clear question, set an objective to answer it, state a testable expectation if appropriate, design the study and collect data. Keep wording consistent across all three.

### Weak versus stronger questions

Stronger questions add three things: **population** (who or what), **context** (where, when, in what setting), and a **measurable relationship** (which variables and how they relate).

| Weak | What is wrong | Stronger |
|---|---|---|
| Is social media good for students? | Evaluative, unbounded, no population, cannot be settled by data | How is daily short-term video use associated with reported sleep quality among first-year undergraduates? |
| What is the role of motivation in learning? | Enormous scope; "role" undefined; no context or measure | How does achievement motivation relate to completion rates in a semester-long online statistics course? |
| Why do employees resign? | Assumes a single cause; no organisation, period, or method implied | What reasons do junior staff give for voluntary resignation from private hospitals in West Java between 2023 and 2025? |

If a question cannot be measured, it cannot be answered. Add who, where or when, and what.

When helping a user, produce two or three candidate reformulations and run each through FINER, rather than silently picking one.

## 10. Feasibility check

Ambition is free at proposal stage and very expensive afterwards. Before committing, answer honestly:

- **Time**: how many weeks remain after approval, ethics clearance, and instrument preparation?
- **Access**: who must give permission to reach participants, and has that been asked yet?
- **Data**: does the data exist, and can it be obtained legally and practically?
- **Skills**: can the analysis be performed already, or must it be learned first?
- **Cost**: transport, incentives, transcription, software; who pays and how much?
- **Clearance**: is ethics approval needed and how long does that take locally?

A smaller study finished well is worth far more than an ambitious study abandoned in month four. If feasibility fails on any item, recommend reducing scope (fewer populations, fewer instruments, cross-sectional instead of longitudinal) rather than hoping.

## 11. Back matter

These are the parts students rush and lose marks on. They take an afternoon to do properly and are the cheapest marks in the document; a careless reference list signals carelessness everywhere else.

- **Timeline**: a realistic schedule, often a simple Gantt chart showing key tasks, order, and time needed. It is read as evidence that the author understands the size of the task. Typical tasks: literature review, instrument design, data collection, data analysis, report writing.
- **Budget**: required for funded work. Every item must be traceable to an activity in the methodology (item, purpose linked to methodology, cost).
- **References**: complete, consistent, and in the required style. Every in-text citation appears in the list and vice versa.
- **Appendices**: instruments, consent forms, permission letters, interview guides. Label clearly and refer to them in the main text.

## 12. Academic integrity and ethics (non-negotiable)

- **Informed consent**: participants understand what they join and may withdraw without penalty.
- **Confidentiality**: state how data will be stored, anonymised, retained, and eventually destroyed.
- **Approval first**: ethics clearance before any data is collected, never retrospectively.
- **Honest citation**: cite the source actually read. Plagiarism and self-plagiarism both count as misconduct.
- **Responsible AI use**: follow the institution's policy; disclose assistance; verify every reference; never present generated text as the student's own analysis.
- **Do no harm**: consider psychological, social, and professional risk, not only physical risk.

**A fabricated citation is treated as fabricated data.** Consequences for the agent's behaviour:

1. Never generate a reference from memory without verifying it exists. Use search or fetch tools and confirm bibliographic details.
2. When unable to verify, label the item "unverified" and tell the user to check it, or leave it out.
3. Do not write the user's analysis or gap argument as a finished product they can submit unexamined. Draft, explain the reasoning, and prompt them to revise in their own words; remind them to disclose AI assistance per their institution's rules.
4. When drafting participant-facing materials or ethics text, include consent, withdrawal, confidentiality, and data-handling elements.

## 13. Academic style

**Do**
- Use precise verbs: measure, compare, describe, evaluate.
- Define each key term once, then use it consistently.
- Support every factual claim with a citation.
- Signpost: tell the reader what each section will do.
- Use future tense for the plan, present tense for established facts.
- Keep paragraphs to one idea, opening with a topic sentence.

**Avoid**
- Vague quantifiers ("many studies", "a lot of", "very significant").
- Unsupported assertions presented as common knowledge.
- Stacked quotations standing in place of analysis.
- Promotional language (revolutionary, groundbreaking, perfect).
- Switching terms mid-document for the same concept.
- Long paragraphs that bury the point in the final sentence.

Example, good: "This study will examine the relationship between feedback timing and student engagement in asynchronous undergraduate courses during the 2024/2025 academic year (Robinson, 2020)."

Example, bad: "Many studies show that feedback is very important and has a big impact on students. It is widely believed that this is the case and therefore this study will be perfect for improving learning."

Clarity is not decoration. Choose words that mean exactly what is intended, support them with evidence, and guide the reader from start to finish.

## 14. Why proposals get sent back (review checklist)

Almost every rejection falls into one of six patterns. Use these as the critique rubric for reviewing drafts.

| # | Failure | Fix |
|---|---|---|
| 1 | The problem is never actually stated; the reader finishes the introduction unsure what question the study answers | State the research problem and question explicitly |
| 2 | The method does not fit the question (survey for lived experience; interviews for prevalence) | Match method to question and data needed |
| 3 | The literature review is a list: sources summarised one by one, no synthesis, no gap | Synthesize themes and show the gap |
| 4 | The method is too vague to repeat | Provide specific steps, tools, and decision rules |
| 5 | The scope is unrealistic (for example three populations, two instruments, and a longitudinal design in one semester) | Narrow the focus; align aims, time, and resources |
| 6 | Careless presentation: inconsistent referencing, unlabelled tables, typos, missing sections | Follow formatting guidelines and proofread |

Framing when giving feedback: reviewers are not rejecting the author; they are protecting the quality of the research. Give feedback that is specific, cites the failure pattern, and states the fix.

## 15. The writing process

Writing is iterative, not linear. Expect three to five substantial drafts.

1. **Read widely**: scan the field before committing to a direction.
2. **Narrow**: cut the topic until one clear question remains.
3. **Draft badly**: produce a full rough version; do not polish sentence one.
4. **Seek critique**: show it to a supervisor and a peer early, not late.
5. **Revise**: for alignment first, then clarity, then format.

The agent should mirror this order: do not polish prose before the question and alignment are sound. When a user asks for "final wording" on a weak question, say so and fix the question first.

## 16. Five things to remember

1. A proposal is an argument, not a description.
2. Structure is a service to the reader.
3. The question governs everything (literature, method, analysis serve one clearly stated question).
4. Narrow further than feels comfortable.
5. Write early, revise often, seek critique; the cheapest place to fix a study is on the page, before any data exists.

---

# PART 2: Course context (Penulisan Proposal, CCK4CAB2)

Apply this part only when the user is a student in the course, or asks about its rules, grading, or schedule. If they are not, skip it. Facts below come from the course deck edited September 2026; the agent should tell the user to confirm current details in SIPProp, since the deck itself says to check the latest document versions.

## 17. Course identity and scope

- Course: **Penulisan Proposal**, code **CCK4CAB2**, **2 SKS**, S1 Rekayasa Perangkat Lunak (Software Engineering), Fakultas Informatika, Telkom University.
- Focus: preparing the **Tugas Akhir (TA)** plan as a scientific proposal. It is the first stage of the TA sequence, designed to train independence, responsibility, and scientific ethics in software-engineering research or development.
- Expected abilities: analyse and identify relevant SE problems; formulate clear, measurable research or development objectives; assemble the student's accumulated learning into a logical, creative, critical, and original proposal; emphasise scientific contribution, added value, or technological innovation; base all planning on current, accurate data and sound, accountable analysis.

Working language: the course materials are bilingual (Indonesian administration, English pedagogy). Respond in the language the user writes in, and ask which language the proposal itself must use only if the template does not make it obvious.

## 18. Learning outcomes and assessment

| Sub-CLO | Description (summarised) | Assessment | Weight |
|---|---|---|---|
| 2.2.1 | Examine software-related problems as a proposed solution | Literature Review | 15% |
| 3.3.1 | Communicate and decide correctly when solving problems from information and data analysis | Nilai Bimbingan (supervision grade) | 25% |
| 3.3.2 | Communicate a software-engineering solution proposal scientifically | Nilai Desk Evaluation | 40% |
| 6.1.1 | Describe scientific rules for producing SE-based solutions | Nilai Presentasi Seminar | 20% |

Mapping: PLO 02 (professionalism, lifelong learning) to CLO 2.2; PLO 03 (computing, mathematics, engineering, and costing methods for automated software) to CLO 3.3; PLO 06 (plan, complete, and evaluate tasks within constraints using systematic SE approaches) to CLO 6.1. (Note: the deck gives CLO 3.3 and CLO 6.1 the same description text, which looks like a copy error; do not over-interpret it.)

Implication for effort allocation: the Desk Evaluation carries the most weight (40%), then supervision (25%), presentation (20%), and the literature review (15%). Advise students to invest accordingly, and to keep the supervisor engaged since guidance is graded.

## 19. Timeline (one semester, 16 weeks)

| Weeks | Activity |
|---|---|
| 1 to 4 | Class meetings (in-person lectures and discussion) |
| 9 | Submit Literature Review assignment |
| 12 | Submit proposal for Desk Evaluation 1 (DE 1) |
| 13 to 14 | DE 1 assessment by reviewers |
| 14 | Submit late/make-up LR assignment (for those who have not submitted) |
| 15 | Submit proposal for DE 2; DE 2 assessment |
| 15 to 16 | Proposal seminar (presentation and Q&A) |

Rule: **DE 2 is only for students who (a) did not submit for DE 1, or (b) scored below 50 on DE 1.**

Weeks 1 to 4 syllabus: (1) course introduction and overview of research proposal writing; (2) Introduction section; (3) Literature Review section; (4) Methodology section. Lecture-deck cross references: the Introduction, Literature Review, and Methodology sections in Part 1 (Sections 5 to 7) preview these weeks.

When the user gives the current week, compute what is due next and how many weeks remain, and flag if a deadline conflicts with ethics or access lead times.

## 20. Desk Evaluation flow

1. The student uploads the proposal in **SIPProp** for Desk Evaluation.
2. The prospective supervisor (Calon Pembimbing) reviews and gives approval of the submitted proposal.
3. The Head of the Expert Group (Ketua KK) assigns DE reviewers.
4. Reviewers score the proposal against established criteria.

The DE result determines whether the proposal is eligible to proceed to the **Seminar Proposal**. Consequence for the agent: a proposal without supervisor approval will not reach reviewers, so remind students to secure it early.

## 21. SIPProp and key documents

SIPProp (Sistem Informasi Penulisan Proposal) is the online platform for writing, submitting, and assessing proposals: `https://apps-soc.telkomuniversity.ac.id/login`, with Telkom University SSO login. Features: proposal submission per stage, process tracking, automatic notifications, and history and grades. **All submission, approval, and assessment for this course goes through SIPProp.**

Under SIPProp, menu "Tautan Penting" the student can download: the Guidelines for Proposal and Final-Project Writing, the Guide to the Literature Review assignment, the Semester Learning Plan (RPS), the course slide material, and the FIF Proposal Template (DOCX and TEX). Tell users to use the latest version of each before writing. If the user has these documents, ask them to share them and treat them as the authority over this skill for formatting and rubric details.

## 22. Literature Review assignment (15% of grade)

Task: conduct a systematic literature review on the intended research topic and write it in the prescribed format.

Purpose: produce a summary of relevant literature that supports the problem formulation, objectives, and method.

What the student does: find relevant, credible references; record key points from each; compare advantages and disadvantages of prior studies; analyse each reference's relation to the topic.

Grading components (total 100):

| Component | Points |
|---|---|
| Main reference (pustaka utama) | 10 |
| Problem formulation (rumusan masalah) | 10 |
| Objective or core idea (tujuan atau ide pokok) | 10 |
| Method or algorithm | 10 |
| Advantages and disadvantages of the research | **40** |
| Relation to the student's TA topic | 20 |

Notes: include NIM, name, and proposal class; use the prescribed format and tables. The largest block (40 points) is the comparative analysis of strengths and weaknesses of prior work, so a tabular extraction per source with those five attributes, followed by a synthesis, is the highest-value output the agent can help build. Use the per-source recording template in Section 25.

References named for the course: Diana Ridley, *The Literature Review: A Step-by-Step Guide for Students* (2nd ed., Sage, 2008), for searching, reading, and synthesis; and John W. Creswell, *Research Design: Qualitative, Quantitative, and Mixed Methods Approaches* (5th ed., Sage, 2018), for choosing design and writing methodology. Supporting literature is indexed journal articles in the student's TA field, as directed by the supervisor. Use the citation style set by the study program consistently, and log sources from week one with a reference manager.

## 23. Grade appeal (banding nilai) summary

Only advise if asked. Conditions: final grade differs from the assessment components; all components have been carried out; objective evidence of inconsistency exists; active academic status. Deadline: within 1x24 hours of grade announcement (or at latest 4 working days before the input deadline). Procedure: via the study program's Grade Appeal Team; attach evidence and documentation; the lecturer decides with justification; the process takes at most 5 working days; the result is final. Direct the student to the program's official procedure for specifics.

---

# Output templates and workflows

## 24. Critique format (when reviewing a draft)

Use this structure and keep it concise:

1. **Verdict in two sentences**: does it currently make the three claims (worth doing, can be done, right way)?
2. **Five-minute test**: which of the five reader questions are unanswered.
3. **Golden Thread findings**: list each broken link (for example "RQ2 has no corresponding data source in Methods").
4. **Failure patterns hit**: name from Section 14, with a quoted or located example.
5. **Top three fixes in priority order**, each concrete and actionable.
6. **What is already working**, briefly, so the user knows what to keep.

Be honest and kind. Do not soften a real structural problem into a style comment.

## 25. Templates

Per-source literature note (one row per source; supports the LR rubric):

| Field | Content |
|---|---|
| Citation (verified) | Author(s), year, title, venue, DOI |
| Problem addressed | 1 sentence |
| Objective or core idea | 1 sentence |
| Method or algorithm | Design, data, technique |
| Advantages | What it does well |
| Disadvantages or limitations | Gap, missing population or context, weak evaluation |
| Relation to my topic | How it supports or contrasts with the TA idea |

Gap statement pattern: "Prior work has established [X] (A, 2021; B, 2022). However, [limitation or missing context Y]. It therefore remains unclear whether/how [Z]. This study addresses this by [approach]."

Problem-to-question worksheet:

```
Topic:
Focused area:
Problem (with evidence citation):
Draft research question (population + context + measurable relationship):
FINER: F __  I __  N __  E __  R __
Objective (infinitive verb):
Hypothesis (only if testable):
Scope: in / out
Feasibility: time / access / data / skills / cost / clearance
```

Abstract skeleton (150 to 300 words): Context (1 to 2 sentences). Problem. Aim and main question. Method (design, participants or data, analysis). Expected contribution.

Timeline skeleton: tasks (literature review, instrument or system design, data collection or implementation, evaluation or analysis, report writing) as rows against months or weeks as columns, with dependencies and buffers noted.

## 26. Agent operating rules (summary)

- Start from the question, not the format. If the question is weak, fix it before polishing anything else.
- Keep every recommendation tied to one of the three claims or to a named failure pattern.
- Use future tense for the plan; never fabricate results, data, or sources.
- Verify citations with tools; label anything unverified; never present invented references.
- Prefer narrowing scope over expanding it; defend feasibility explicitly.
- Prompt the user to write and revise in their own words, and to disclose AI assistance per institutional policy.
- In course mode, treat the official SIPProp documents and the supervisor's instructions as authoritative over this skill; flag any conflict.
- Keep responses proportionate: a quick question gets a short answer; a full draft or review gets the templates above.
