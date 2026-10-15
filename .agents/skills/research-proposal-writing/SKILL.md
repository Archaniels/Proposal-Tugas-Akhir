---
name: research-proposal-writing
description: Plan, draft, critique, and improve research proposals (usulan penelitian / proposal Tugas Akhir), covering title, abstract, introduction (background, problem statement, gap, questions, objectives, scope), literature review (search strings, screening, literature matrix, synthesis), methodology (design, sampling, instruments, validity, procedure, analysis, ethics), timeline, budget, references. Use whenever the user mentions a research proposal, thesis or Tugas Akhir (TA) proposal, research question, research gap, literature review, methodology, desk evaluation, or seminar proposal, or asks to narrow a topic, check alignment between problem, method and analysis, or review a draft. Also use for the Telkom University Faculty of Informatics course "Penulisan Proposal" (CCK4CAB2, S1 Rekayasa Perangkat Lunak), even if the user only says "help me with my proposal", "my LR assignment", or "DE".
---

# Research Proposal Writing

This skill turns an AI agent into a disciplined research-proposal collaborator. It encodes the reasoning behind good proposals (what reviewers look for, why proposals get sent back) so the agent can draft, coach, and critique, not just fill in templates.

Source material: lecture decks for *Penulisan Proposal* (CCK4CAB2), Fakultas Informatika, Telkom University: "Research Proposal Writing" (Meeting 1 of 4), "The Introduction Section" (Meeting 2 of 4), "The Literature Review" (Meeting 3 of 4), "The Methodology Section" (Meeting 4 of 4, 100 minutes each), and the course-administration deck for S1 Rekayasa Perangkat Lunak (edited September 2026). Part 1 is general and applies to any discipline; Sections 5, 6, and 7 carry the detailed content of Meetings 2, 3, and 4. Part 2 is specific to the course and should be applied only when the user is in it.

The Meeting 2 to 4 decks use education and social-science examples (feedback timing, student engagement, asynchronous courses). Treat these as illustrations of the reasoning, not as topics to impose on the user; where this skill adds guidance for software-engineering work beyond the slides, it says so.

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
| "Background / problem statement / gap / objectives / hypotheses / scope" | Introduction drafting | Section 5 (5.6 to 5.9) |
| "Find literature / search string / screening / literature matrix / synthesis" | Literature workflow | Section 6 and Section 12 |
| "Which design / sample size / instrument / validity / analysis / ethics section" | Methodology drafting | Section 7 |
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

*Source: Meeting 2 deck, "The Introduction Section".*

**Job**: turn a topic into a problem. The introduction gives the reader enough context to understand the situation, evidence that a specific difficulty is real and unresolved, and a precise statement of what this study will do about it. It earns attention by showing **relevance, clarity, and direction, in that order**.

### 5.1 What the introduction does (three verbs, five jobs)

- **It orients**: the reader may know the field but not your context. Supply exactly the background needed, no more.
- **It justifies**: argue that a real gap exists and that answering it is worth someone's time, money, and permission.
- **It commits**: by the last paragraph you have publicly promised what will be studied, with whom, and within what boundaries.

Five jobs: (1) set the stage with just enough background; (2) state the problem so it is clear, real, and worth solving; (3) present the questions, showing exactly what the study will answer; (4) explain the significance (for knowledge, practice, or policy); (5) preview the approach briefly (how the study will be done, without method detail).

### 5.2 The funnel (five levels)

The introduction moves from a situation the reader already accepts to one question only this study will answer. Never the reverse.

| Level | Content |
|---|---|
| 1. The field | The wider situation or phenomenon, established with citations |
| 2. Your context | The specific setting, population, or practice you are concerned with |
| 3. What is known | What prior work has already established about that context |
| 4. What is missing | The gap: the question prior work leaves unanswered |
| 5. This study | Your purpose, your questions, and the boundaries you set |

Test: a reader should be able to point at the paragraph where each of the five levels begins.

### 5.3 Components and indicative shares

Shares are indicative only; the order of components follows the institution's template.

| Component | What it must accomplish | Typical share |
|---|---|---|
| Background of the study | Establishes the situation and shows, with evidence, that a difficulty exists | 40 to 50% |
| Problem statement | Names the specific gap or difficulty this study addresses | 10 to 15% |
| Research questions | States precisely what will be answered, in answerable form | 5 to 10% |
| Objectives | Restates the questions as actions the study will perform | 5% |
| Scope and delimitations | Marks the boundaries deliberately set, and why | 5 to 10% |
| Significance | Explains who benefits from the answer and in what way | 10% |
| Definition of key terms | Fixes the meaning of terms used throughout the proposal | 5% |

### 5.4 A classic model: CARS (Swales)

Almost every strong introduction makes three moves, in this order:

1. **Establish the territory**: show the area matters, give necessary background, summarise prior work. Goal: the reader says "yes, this is important."
2. **Establish a niche**: indicate a gap or tension, question a prior finding, or note an untested context. Goal: the reader sees a gap worth filling. (Example move: "However, little of this work examines first-year students...")
3. **Occupy the niche**: state your purpose, announce your questions, preview scope and value. Goal: the reader accepts your place in the gap.

Takeaway: move from what is known, to what is missing, to what your study will do about it.

### 5.5 What the reader is asking, paragraph by paragraph

| Reader question | Answered by |
|---|---|
| What is this about? | The opening of the background, in the first two or three sentences, not on page three |
| Why should I care? | Evidence of consequence: who is affected, and what happens if nothing is known |
| What is not yet known? | The gap: a specific, defensible statement of what prior work left unresolved |
| What exactly will you do? | The purpose statement and research questions, in one place, unambiguously |
| What are you not doing? | Scope and delimitations, which protect the author as much as they inform the reader |

Answer early, clearly, and in order. If a question is answered late, the reader assumes the author does not know the answer either.

### 5.6 The background (build context from evidence, not assumption)

"It is likely that..." weakens the case; "Studies show that..." (with a citation) strengthens it.

**What the background must achieve**
- **Orient a non-specialist**: the examiner may not work in the exact area. Give the minimum context needed to follow the problem, nothing decorative.
- **Show the situation is real**: replace "nowadays it is very important" with data, documented practice, policy, or prior findings a reader can verify.
- **Narrow toward your variables**: each paragraph closer to the specific problem than the one before (broad field, context, focus, your variables).
- **Open the door to the gap**: by the final paragraph the reader should already sense what is missing, before it is named.

**Where background evidence comes from**

| Source type | Examples | Note |
|---|---|---|
| Official statistics | BPS, UNESCO, WHO, ministry reports | Cite the release itself, not a news summary of it |
| Prior empirical studies | Journal articles, theses, conference papers | Peer-reviewed findings on what is already observed |
| Policy and regulation | National curriculum, laws, institutional guidelines | Rules that define the situation studied |
| Documented practice | Program reports, audit reports, observation notes | How things are actually done |
| Theory | Models, frameworks, conceptual theories | Explains why the phenomenon behaves as it does |
| **Not acceptable alone** | Personal impression, unsourced blogs, generative-AI output, "it is well known that..." | Anecdotes and opinion pieces do not carry a background |

Rule of thumb: every claim about the state of the world in the background carries a citation.

**The first paragraph.** The opening sentence sets the reader's expectation of seriousness. It should signal relevance, context, and credibility.
- Empty (do not write): "In this era of globalisation, technology is developing very rapidly. Everyone uses the internet nowadays. Therefore, the researcher is interested in studying online learning." (too broad, obvious, no evidence)
- Evidenced (write like this): a specific situation in the user's context with an early citation, for example "Asynchronous delivery has remained a permanent component of undergraduate teaching in many Indonesian universities since 2020 (Author, Year). Institutional data show that completion rates in fully asynchronous courses lag behind those in scheduled classes (Author, Year)."
- Do: start with the situation in your context; use evidence early; show the topic matters. Don't: open with broad history or general facts; define terms in the opening; make claims you do not cite.

**Building the background in four moves** (a workable default of four to eight paragraphs):

1. **Situate**: the wider phenomenon and why it matters, with checkable sources.
2. **Localise**: bring it to your setting, population, or institution. This is where most drafts stop too early.
3. **Summarise**: state briefly what prior work has established here. A preview, not the literature review.
4. **Unsettle**: show the tension (findings conflict, contexts differ, or the question was never asked). This hands the reader to the problem statement; if it does not, the problem will feel like it arrived from nowhere.

**Citing inside the background**
1. Cite what you read. If a source is known only through another author, cite the source that quoted it, correctly.
2. Balance recent work (the problem is live) and seminal work (you know where the ideas came from).
3. Paraphrase by default; quote only when exact wording carries meaning a paraphrase would lose.
4. One claim, one citation. Do not stack five references after a general sentence to look thorough; reviewers read it as padding.
5. Match the required style (APA, IEEE, Chicago) consistently, including secondary sources.
6. Keep it in the background: detail belongs in the literature review.

A citation that does not say what the author claims it says is treated as a factual error, not a formatting slip.

### 5.7 The problem statement and the gap

The problem statement transforms the tension from the background into a clear, researchable problem and identifies the specific gap. It is not a topic; it is the specific issue the study will solve.

**It is**: a statement of a specific difficulty, discrepancy, or unknown; grounded in evidence presented in the background; bounded to a population, context, and period; written so a reader can see what an answer would look like; usually one focused paragraph, sometimes two.

**It is not**: a restatement of the topic in longer words; a description of the method or instrument; a list of research questions; a statement that the researcher personally finds the topic interesting; a complaint that "little research has been done" with no evidence.

Good example: "First-year students in asynchronous courses at Indonesian universities experience lower completion rates than those in scheduled classes during the 2020 to 2024 period." Not a problem statement: "This study discusses online learning in higher education and uses surveys to find out students' opinions about it."

**Test**: could someone disagree with the problem statement? If not, it is a description, not a problem.

**The five-part structure** (one to three sentences per part, in this order; revise afterwards for flow; five sentences, one paragraph, no method detail):

| Part | Content |
|---|---|
| 1. Ideal | What should be happening, according to theory, policy, or standards |
| 2. Reality | What is actually happening, shown with evidence from the background |
| 3. Gap | The discrepancy, or what remains unknown about it, stated precisely |
| 4. Consequence | What it costs to leave this unresolved, and to whom |
| 5. Response | What this study will therefore do: one sentence, no method detail |

Most rejected problem statements contain parts 1, 2, and 5 and quietly skip the gap and the consequence. **Those two are the argument.**

Worked example (stronger version): "Course design standards assume that students in asynchronous courses receive feedback promptly enough to act on it (Author, Year). In practice, feedback in large first-year courses is often returned after the next task has begun (Author, Year). Although several studies link feedback quality to engagement, few examine feedback timing in asynchronous undergraduate settings, and none report evidence from Indonesian universities. As a result, institutions redesign these courses without knowing which element of feedback actually sustains engagement. This study therefore examines how feedback timing and peer interaction relate to engagement among first-year students in asynchronous courses." (Weak version to contrast: "Many students today take online courses and many of them do not finish. This is an interesting problem. Therefore the researcher wants to research student engagement in online learning." No evidence, gap, consequence, or clear response.)

**Six kinds of research gap** (name which one the study addresses):

1. **Knowledge gap**: a relationship or phenomenon has simply not been examined yet.
2. **Context or population gap**: examined, but not in your setting, culture, level, or sector.
3. **Methodological gap**: prior work used designs that could not answer the question convincingly.
4. **Conflicting findings**: studies disagree and the disagreement is unresolved or unexplained.
5. **Practice gap**: what research recommends and what practitioners do have diverged.
6. **Theory application gap**: an established theory has not been tested against this case.

"No one has studied this" is almost never true and is easy for an examiner to disprove.

**Where problem statements fail** (reviewers test this section first): (1) the topic is restated, not problematised; (2) the gap is asserted, not shown (show it with evidence from the review); (3) no consequence is given ("so what?"); (4) the problem is too large for a semester project; (5) method appears too early (instruments and sampling belong in the methodology chapter); (6) personal motivation stands in for evidence. Quick check: does the statement show Ideal, Reality, Gap, Consequence, Response in one clear paragraph?

### 5.8 Questions, objectives, hypotheses, and boundaries

**From gap to questions.** Turn the problem into one main question, then two or three sub-questions. Example main question: "How are feedback timing and peer interaction related to student engagement in asynchronous first-year courses?" with sub-questions on (1) patterns of feedback timing reported by students, (2) how perceived timing relates to reported engagement, (3) the role of peer interaction in sustaining engagement between tasks. The set must:
- **cover the whole problem** (together, the sub-questions fully answer the main question);
- be **answerable** by data the author can realistically obtain;
- be **consistent** (none introduces a variable that never appeared in the problem).

**Question stems signal the design.** Mismatched stems are the first sign of a misaligned proposal.

| Design | Focus | Typical stems |
|---|---|---|
| Quantitative | Measurement and comparison | To what extent does X predict Y...; What is the relationship between...; Is there a significant difference between...; How frequently do participants... |
| Qualitative | Meaning and understanding | How do participants experience...; What meanings do X attach to...; In what ways does X shape...; Why do participants describe... |
| Mixed methods | Integration of numbers and meanings | How do measured patterns of X compare with participants' accounts of X...; To what extent do interview findings explain the survey results... (requires both strands and an explicit reason for combining) |

Keep it clear: avoid yes/no questions; ask one thing at a time; every question answerable with data that can be collected.

**Six tests for every research question**

| # | Test | Meaning |
|---|---|---|
| 1 | Answerable with data | You can name the evidence (LMS logs, survey results, interview transcripts) and imagine obtaining it |
| 2 | Single and specific | One question per sentence, with a named population and context |
| 3 | Free of hidden assumptions | Avoid "why" questions that assume what should be demonstrated ("Why is feedback timing important?" becomes "How does feedback timing relate to student engagement?") |
| 4 | Neutral in wording | No leading words like "best," "most effective," or "should" |
| 5 | Consistent with the design | A "how do they experience" question cannot be answered by a Likert scale alone |
| 6 | Traceable to the problem | Every term in the question appeared earlier in the problem statement |

**From questions to objectives.** An objective has the same content as the question, written as an action the study will perform. Most templates ask for one general objective matching the main question, followed by specific objectives matching each sub-question; keep the numbering identical so alignment is visible at a glance.
- Verbs that work (measurable or observable): to describe, compare, examine, measure, evaluate, analyse, identify, develop, test.
- Verbs that do not work (intention, not action; cannot be shown as achieved): to understand, to know, to learn about, to appreciate, to explore deeply, to be aware of.
- Use the same key terms (variables, population, context, timeframe); state what you will do, not what you hope to find.

**Hypotheses, only where they belong.** Required in most experimental and correlational designs; usually absent in qualitative and purely descriptive studies.
- **Null (H0)**: no relationship or difference exists; the statement the analysis actually tests (for example, no significant relationship between feedback timing and student engagement).
- **Alternative (H1)**: the relationship or difference expected, based on theory or prior findings. Directional ("higher than") only when prior evidence or theory justifies it; otherwise non-directional ("differs from").
- Never write hypotheses because the template has a heading for them. A hypothesis you cannot test is a liability in the defence.

**Scope, delimitations, and limitations**

| Term | Meaning | Where it belongs | Example |
|---|---|---|---|
| Scope | Who, what, where, when; sets the exact coverage | Introduction | First-year students in three asynchronous courses at one university, in one semester |
| Delimitations | Boundaries you choose, with the reason for each | Introduction | Only asynchronous courses are included, because feedback timing is not comparable in live sessions |
| Limitations | Constraints you cannot control that may affect findings | Methodology; revisited in the final report | Self-reported engagement may differ from observed engagement |

Delimitations are decisions with reasons; limitations are constraints with consequences. Confusing the two suggests the author does not know which is which.

**Significance: who benefits, and how.** Four kinds: **theoretical** (extends, tests, or refines an existing account; name the theory), **practical** (gives named practitioners something to act on), **policy** (informs a named decision an institution or authority must make), **methodological** (an instrument, adaptation, or procedure others can reuse; claim only if genuinely new). Test each claim by finishing: "Because of this study, ______ will be able to ______." If both blanks cannot be filled with something specific, delete the claim. Good: "course designers will be able to revise feedback policies to boost engagement." Weak: "people will be able to understand the topic better."

**Defining key terms.** Define only the terms that carry weight in the questions, the ones a reader could interpret differently.
- **Conceptual definition**: what the term means in the literature, with a citation (for example, student engagement as the behavioural, emotional, and cognitive investment a student makes in a learning task).
- **Operational definition**: how the term will be observed or measured in this study (for example, the score on a twelve-item engagement scale combined with discussion posts per module).
- Use the same definition throughout. Every variable in a quantitative study needs an operational definition; without one, the methodology cannot be written or judged.

### 5.9 The alignment test (problem, question, objective, evidence)

Lay the draft out in this form. If any row breaks, the introduction is not finished.

| Problem element | Research question | Objective | What would answer it |
|---|---|---|---|
| Feedback is returned too late to act on | How does feedback timing relate to engagement? | To examine the relationship between feedback timing and engagement | Reported timing and engagement scores from the same students |
| Students disengage between tasks | What role does peer interaction play between tasks? | To describe the role of peer interaction between tasks | Interview accounts and discussion-forum activity |
| Institutions redesign courses without evidence | Which element most strongly relates to engagement? | To compare the strength of the two relationships | Comparative analysis of the two sets of results |

Quick check: every term in column two already appears in column one (anything new means the problem was under-stated); objectives use action verbs the author can actually do; the evidence listed is realistic to obtain; if a new term appears anywhere, refine the problem statement.

### 5.10 Introduction checklist (before submitting the draft)

1. The opening paragraph names the situation and carries a citation.
2. Every claim about the state of the world is sourced.
3. The background narrows steadily toward the problem.
4. The gap is named as a specific type, not asserted vaguely.
5. The problem statement contains ideal, reality, gap, consequence, response in one coherent paragraph.
6. One main question and two or three sub-questions are stated in one place, aligned and answerable with the planned data.
7. Objectives mirror the questions, using demonstrable verbs.
8. Scope, delimitations, significance, and key terms are all present, specific, realistic, and in the right place.

Final reminder: check against a **printed** draft, not on screen; more problems surface.

**Five things to remember (introduction)**: (1) the introduction turns a topic into a problem; (2) evidence, not adjectives, establishes context; (3) name the gap and name its type; (4) questions must be answerable and aligned; (5) boundaries protect you.

Agent behaviour when drafting or reviewing an introduction: run the five-minute test (Section 2), the five-part problem statement check, the six question tests, and the alignment table; identify which of the five funnel levels is missing; never write the background from unsourced general knowledge, and flag every sentence that needs a citation the user must supply and verify.

## 6. Section 2: The Literature Review

*Source: Meeting 3 deck, "The Literature Review".*

**Job**: an argument about what is known, not a catalogue of what was read. The review is a structured argument that selects, organises, and evaluates prior work so a reader can see the shape of the field and the precise point at which the study becomes necessary. Synthesis, comparison, and critical analysis lead to the research gap.

### 6.1 Three properties of a real review

- **Selective**: include what bears on the research questions. Volume is not a virtue; a reviewer counts relevance, not references.
- **Synthesised**: sources are grouped by idea, compared with one another, and made to speak to a claim that is the author's. Organise by themes or concepts; compare agreements and differences.
- **Evaluative**: judge what is cited (how it was done, how well, in what context, how far it travels to the author's study). Quality, relevance, context, contribution. Not just summary; critical judgment, showing the trajectory to the study.

Shape: prior work (what is known), then the gap (what is missing), then the study (fills the gap).

### 6.2 Four jobs the review must do

| Job | What it does | Goal |
|---|---|---|
| 1. Map the field | Show what has been established, by whom, and where the main lines of agreement and disagreement lie | A clear picture of the current knowledge landscape |
| 2. Demonstrate the gap | Turn the gap claimed in the introduction into a conclusion the reader reaches from the evidence | Make the need for the study inevitable and evidence-based |
| 3. Supply the framework | Define the concepts and relationships the study will use, drawn from theory rather than invented | The theoretical lens connecting what is known to what will be investigated |
| 4. Inform the method | Show which designs, instruments, and samples have worked before, and justify own choices by precedent | Confidence that the methods are appropriate and rigorous |

Padding test: if a paragraph does none of these four things, it is padding, however interesting the study it describes.

### 6.3 Three things it is often confused with

| Feature | Annotated bibliography | Chapter summary | Literature review |
|---|---|---|---|
| Organised by | One entry per source | One paragraph per source | Theme, concept, or debate |
| Whose voice leads | Each source in turn | Each source in turn | The author's; sources supply evidence |
| Sources compared? | No | Rarely | Constantly; that is the work |
| Purpose | Record what you read | Show you read it | Argue what is known and what is missing; build the case for the study |
| Ends with | The last entry | The last source | A gap the reader now accepts, leading to the research questions |

The most common failed review is a good annotated bibliography with the headings removed. Without synthesis and comparison there is no argument, only description.

### 6.4 Types of review (choose, then say which one it is)

1. **Narrative review**: the default for a thesis proposal. Selective, thematic, argued; transparent about scope but not exhaustive.
2. **Systematic review**: follows a pre-registered protocol with explicit search, screening, and appraisal steps; reproducible by design.
3. **Scoping review**: maps the extent and nature of evidence when a field is new or fragmented, without appraising every study.
4. **Meta-analysis**: statistically pools results across comparable quantitative studies to estimate an overall effect.
5. **Integrative review**: combines findings from different designs (qualitative and quantitative) into one synthesis.
6. **Rapid review**: a streamlined systematic method used when a decision cannot wait; limits stated openly.

Whichever is used, say which one it is and describe how the search was done. An unstated method is the mark of an unsystematic review. (Course note: the Telkom assignment is worded as a "systematic literature review"; see Section 22 for how to reconcile this with the narrative default.)

### 6.5 How the review connects to the other sections

| Introduction | Literature review | Methodology |
|---|---|---|
| Claims a gap and states questions; sets the problem and direction | Proves the gap and defines the concepts; builds the case with evidence and definitions | Justifies how the gap will be closed; plans the solution and shows feasibility |

Four rules that follow:
1. **Define all concepts here**: every concept named in the questions must be defined from published work.
2. **Support what was claimed**: every claim about "what is known" in the introduction must be supported here.
3. **Justify the method**: every methodological choice in the methodology should have a precedent cited here.
4. **Stay focused and aligned**: nothing new may appear in the review that the questions never mentioned.

### 6.6 Finding the literature (a search you can describe, repeat, and defend)

Three steps: **Find** (clear keywords; document search strategy and sources), **Select** (screen with explicit criteria so others can see what was kept and why), **Record** (save full details and search strings so the search can be reproduced exactly). Good searches are transparent.

**From question to search terms.** Break the question into concepts, then list the words other authors might have used for each one.

1. Start with the research question.
2. Break it into key concepts (the main ideas or variables).
3. Find synonyms and variants (look at keywords in relevant papers; their keyword lists show the field's vocabulary).
4. Build search strings and search, combining terms with Boolean operators.

Worked example. Question: how are feedback timing and peer interaction related to student engagement in asynchronous first-year courses?

| Concept | Synonyms and variants | Narrower or broader terms |
|---|---|---|
| Feedback timing | delayed feedback, immediate feedback, feedback latency, turnaround time | formative feedback, assessment feedback |
| Student engagement | behavioural engagement, participation, involvement, persistence | motivation, retention, dropout |
| Asynchronous course | online learning, e-learning, distance education, self-paced course | blended learning, MOOC |

Example search string: ("feedback timing" OR "delayed feedback" OR "feedback latency") AND ("student engagement" OR "participation" OR "involvement") AND ("asynchronous course" OR "online learning" OR "distance education").

**Search syntax**

| Operator | Effect | Example |
|---|---|---|
| AND | Narrows: all terms must appear; combines different concepts | feedback AND engagement |
| OR | Widens: any term may appear; use inside brackets for synonyms | (engagement OR participation) |
| NOT | Excludes a term; handle with care, it removes relevant work too | engagement NOT marketing |
| "  " | Keeps a phrase together as one unit | "feedback timing" |
| * | Truncates the stem to catch variants | engag* retrieves engage, engaging, engagement |
| Filters | Limit by year, language, type, or subject | 2015 to 2026, English, article |

**Where to search** (use the right source for the right purpose):

| Source | Strength |
|---|---|
| Multidisciplinary indexes (Scopus, Web of Science) | Curated, citation-linked; the usual reference point for "indexed" journals; comprehensive, high-quality literature |
| Discipline databases (ERIC for education, PubMed for health, IEEE Xplore for engineering, JSTOR for humanities) | In-depth coverage within a field |
| National and open sources (Garuda, SINTA, DOAJ) | Indonesian and open-access journals global indexes may miss; local context |
| Google Scholar | Broad and fast but unfiltered; useful for leads and starting points; never sufficient as the only source |
| Repositories and theses | Grey literature, datasets, theses, instruments; especially local context and instruments |
| Citation chaining | Follow references backwards from a key paper and citations forwards to newer work; builds a complete, up-to-date evidence trail |

Document the search: where searched, when, with which string, and how many results each returned. The author will be asked.

**Deciding what counts (inclusion and exclusion criteria).** Set these before screening starts; deciding case by case as you go is how bias enters a review.

| Typical inclusion | Typical exclusion |
|---|---|
| Time window (for example the last ten years) | Insufficient text (abstracts, posters, conference papers without full text) |
| Source quality (peer-reviewed articles, or theses from recognised institutions) | Poor-quality source (journals with no discernible review process) |
| Population and setting of interest | Unclear method (not described well enough to judge) |
| Study type: empirical work reporting data, not opinion pieces | Different population where transfer cannot be argued |
| Language the author can read accurately | Duplicate reports of the same dataset |

Good practice: seminal older work is included by name, not by date rule; say so explicitly when stating the window.

**The screening workflow** (thousands of results down to the reading list):
1. **Identify**: run each search string in each database; export all results, with duplicates, to the reference manager.
2. **Screen**: read titles and abstracts only; decide against the criteria. Most results die here; that is normal.
3. **Assess**: read the full text of what survived; check the method section before the findings.
4. **Include**: keep what is relevant and defensible; record the reason each excluded study was dropped.

Track numbers at each stage: Found, After duplicates, After title screening, After full text, Included. Reviewers ask for them; a simple flow diagram answers in one glance.

**Judging what you find (source quality)**

| Check | Ask |
|---|---|
| Peer review status | Was the work reviewed before publication, and by whom? Check the journal's stated review process |
| Indexing and standing | Is the journal in a recognised database (Scopus, Web of Science, discipline databases)? Avoid predatory or unknown journals |
| Methodological transparency | Can sample, instrument, and analysis be seen clearly enough to judge the finding? Missing methods mean weak evidence |
| Relevance of context | Do population, setting, and period allow the finding to travel to this study? |
| Citation trail | Who cites it, and how? Approving citation by others is a useful signal |
| Warning signs | Advertised fees above review standards, unrealistic turnaround times, no editorial board or contact details, aggressive email invitations |

Citation counts measure attention, not correctness; a highly cited paper can still be the one the study corrects. When in doubt, be conservative: better to exclude now than build on weak evidence later.

### 6.7 Reading and synthesising

Pipeline: organise (collect, name, and sort PDFs), read actively (skim, then read closely), extract (data, concepts, evidence that matter), synthesise (group, compare, contrast, find patterns), build the argument (a clear logical story that answers the question). Read with purpose, extract what matters, connect the dots.

**Reading in three passes.** You cannot read fifty papers closely; decide early which deserve the third pass.

| Pass | Time | Activity | Outcome |
|---|---|---|---|
| 1. Triage | about 5 minutes | Title, abstract, conclusion; skim headings and figures | Relevant, maybe, or discard. Most sources stop here, and should |
| 2. Extract | about 20 minutes | Introduction, method, results; record design, sample, findings; note limitations the authors admit | This is where the matrix gets filled |
| 3. Engage | an hour or more | Read fully and critically; question whether data support the claim; trace key references | Reserved for the handful of core studies |

Goal: not to read everything but to understand what matters.

**What to record for every source**

| Field | Content | Example |
|---|---|---|
| Full citation and DOI | Captured once in the reference manager, in the department's required style | Smith, J. (2022). Title. *Journal*, 10(2), 123-140. https://doi.org/... |
| Question and purpose | What the authors set out to find, condensed into one line | To examine the effect of feedback timing on engagement in asynchronous courses |
| Context and participants | Country, setting, level, sample size; determines transferability | Indonesia; first-year students; online course; n = 256 |
| Design and instrument | How the data were produced; reused in the methodology | Quantitative survey; engagement scale validated in prior studies |
| Key findings | The result that matters for the question, not every result | Timely feedback positively associated with engagement |
| Limitations and your comment | What the authors admit, plus one line on how the study relates to yours | Small single-institution sample; my study extends this to multiple institutions |

Tip: record page numbers with every quotation as you read; reconstructing them later is the most avoidable waste of a week.

**The literature matrix** (a tool that writes the review for you). One row per source, one column per thing to compare. When the table is full, the themes are already visible.

| Source | Context | Design | Key finding | Relevance to my study |
|---|---|---|---|---|
| Author (2019), DOI | Undergraduates, blended courses, Europe | Survey, n = 412 | Faster feedback associated with higher participation | Supports the timing-engagement link; different delivery mode |
| Author (2021), DOI | First-year students, fully online, Asia | Interviews, n = 18 | Students describe disengaging while waiting for marks | Gives the mechanism the survey cannot capture |
| Author (2023), DOI | Postgraduates, asynchronous, Australia | Quasi-experiment | No timing effect once workload is controlled | Contradicts the two above; the tension to be examined |

Tips: keep the same column headings; be brief but precise and link to page numbers; add columns if needed (limitations, theory, country); update as sources are read. Notice the last row: disagreement between sources is not a problem for the review; it is the reason the study exists. (The rows above are illustrative placeholders; never present placeholder authors as real sources.)

**Summary versus synthesis (the central skill)**

- *Summary, source by source*: "Author (2019) studied 412 students and found faster feedback increased participation. Author (2021) interviewed 18 students and found they disengage while waiting. Author (2023) ran a quasi-experiment and found no effect." This retells each study in turn.
- *Synthesis, claim first, sources as evidence*: "Evidence linking feedback timing to engagement is consistent in self-report studies (Author, 2019; Author, 2021) but weakens under controlled conditions (Author, 2023). The divergence follows the design rather than the setting: studies that measured perceived timing report an effect, while the one study that manipulated timing and controlled for workload does not. Whether timing matters independently of workload therefore remains unresolved in asynchronous undergraduate courses."

Three moves: (1) **open with your claim** (a thesis, not a bibliography); (2) **compare, don't queue** (group studies by what they show; explain why they agree or differ; look for patterns in methods, measures, and conditions); (3) **end by narrowing the gap** (state what is still uncertain; point to the question the study will answer).

### 6.8 Organising the review

**Four structures** (choose the one that fits the question and the story):

1. **Thematic**: grouped by concept or debate. The default, and the easiest to end in a gap.
2. **Chronological**: grouped by period. Use only when the field genuinely shifted over time.
3. **Methodological**: grouped by how studies were done (surveys, interviews, experiments). Useful when designs explain conflicting results.
4. **Theoretical**: grouped by competing frameworks. Use when the study takes a side.

Announce the structure in the first paragraph; use headings that name themes (for example "Timing Effect," "Student Experience"), not authors.

**The argument arc** (each layer narrows the field until the gap is the only place left to stand):
1. **What the field agrees on**: established findings not to be re-argued; show consensus and move on.
2. **What is contested**: where results conflict and the explanations offered so far; identify disagreements and why they matter.
3. **What is untested here**: findings established elsewhere but never in this context.
4. **What remains unexamined**: the specific question no included study has answered; define the precise gap.

Then: **therefore, this study**. The questions arrive as the reader's own conclusion. If the last paragraph could be deleted without the reader noticing, the review had no destination.

**The conceptual framework**
- *Theoretical framework*: an existing theory adopted to explain the phenomenon, taken from published work and cited as such.
- *Conceptual framework*: the author's own map of the variables and the relationships expected between them, assembled from the literature just reviewed.
- Example: feedback timing and peer interaction as inputs to student engagement (outcome), with course workload as a controlled variable held constant to isolate effects.
- Rules for the diagram: every box must appear in the research questions; every arrow must be supported by a cited source; explain it in prose, because a diagram alone is not a framework. Keep the model simple, including only variables needed to answer the questions.

### 6.9 Writing the section

**Layout and indicative length**

| Part | What goes in it | Length |
|---|---|---|
| Opening | Scope of the review; how searched (databases, keywords, dates); how the section is organised | 2 to 3 paragraphs |
| Themes 1, 2, 3... | Evidence grouped under headings naming ideas; compare and contrast; evaluate quality and relevance | The bulk of the section |
| Conceptual framework | Variables and relationships; include a diagram and explain it | 1 to 2 pages |
| Synthesis and gap | What the reviewed work establishes; where results conflict or are unclear; the specific question or gap | 2 to 3 paragraphs |

Flow: opening (set the stage), themes (what is known), framework (how things connect), synthesis and gap (narrow to what is still unknown). Every statement of fact or interpretation needs a citation. **The final paragraph of the review and the problem statement in the introduction must agree word for word about what the gap is.**

**Paragraph craft.** One idea per paragraph; open with a topic sentence showing how it fits the argument; develop with evidence and analysis; end with a sentence leading to the next step. Four moves in a synthesis paragraph:
1. **Claim**: the point this paragraph makes; the author's, not a source's.
2. **Evidence**: two or more sources that agree with the claim, put together.
3. **Evaluation**: compare, qualify, or explain the difference between studies (similar or different, and why it matters).
4. **Link**: point forward; what remains unsettled and what comes next.

If a paragraph needs two claims, it needs two paragraphs.

**Citations and reporting verbs**
- *Integral citation*: the author is the subject ("Author (2021) argued that..."); use when the person or study matters.
- *Non-integral citation*: the finding is the subject ("Students disengage while waiting for marks (Author, 2021)."); use most of the time in a synthesis.
- Quick guide: is the author or study the focus of the sentence? Integral. Is the idea, finding, or result the focus? Non-integral.
- Use one consistent style (for example APA 7th); include page numbers for direct quotations; let citations support claims, not replace them.

| Verb strength | Examples | Signal |
|---|---|---|
| Neutral | reported, examined, measured, observed, described | Relaying what was done or found, without endorsing it |
| Stance | argued, suggested, proposed, claimed, questioned | The author advanced a position others might contest |
| Strong | demonstrated, established, confirmed, showed | The finding is accepted as settled; use sparingly and only with strong evidence |

The verb is an argument: "claimed" and "demonstrated" describe the same sentence very differently. Let verbs do the arguing, not adjectives; vary verbs to show nuance.

**Keeping the argument yours**
- Do: start paragraphs with the claim, not a citation; group several sources behind one sentence where they agree; name disagreements openly and offer an explanation; paraphrase in your own sentence structure, then cite; use headings naming themes; return regularly to what this means for the question.
- Avoid: "Author X said... Author Y said..." paragraph after paragraph; long quotations instead of your own explanation; reporting every study at the same level of detail; accepting a finding simply because it is published; reviewing sources that never reappear in the proposal; ending the section without saying what is missing.

A reviewer should be able to read only the first sentences and still follow the whole argument.

### 6.10 Where literature reviews fail, integrity, and checklist

| # | Failure | Description |
|---|---|---|
| 1 | It is a list, not a review | One paragraph per source in reading order, no comparison |
| 2 | No gap emerges | Thirty pages of competent summary ending without saying what is missing |
| 3 | Only recent, or only old | Nothing before 2020 has no foundations; nothing after has no relevance |
| 4 | Uncritical acceptance | Every study reported as fact with no attention to sample, design, or context |
| 5 | Sources that go nowhere | Work reviewed at length that never informs a question, a variable, or a method |
| 6 | Citations that do not match | In-text citations missing from the reference list, or references never cited |

**Integrity in the literature review (non-negotiable)**
1. **Paraphrase properly**: changing a few words while keeping the sentence structure is patchwriting and is treated as plagiarism. Rewrite in your own structure, then cite.
2. **Cite what you actually read**: if a study is known only through another author, cite it "as cited in" that author's work.
3. **Quote with page numbers**: direct wording needs quotation marks and a locator, every time, however short.
4. **Verify every reference**: AI tools produce plausible citations that do not exist. Check the DOI and open the paper before citing it.
5. **Represent findings fairly**: do not report only the result that suits the argument while omitting the authors' qualifications.
6. **Follow the institution's AI policy**: disclose assistance where required; undeclared use in a submitted proposal is misconduct in most institutions.

A fabricated citation is treated as fabricated data, not as a formatting error.

**Literature review checklist (before submitting the draft)**
1. The search strategy is described: sources, terms, dates, and limits.
2. Inclusion and exclusion criteria are stated and applied consistently.
3. Sources are grouped by theme, with headings that name ideas.
4. Every theme paragraph opens with a claim of the author's own.
5. Disagreements between studies are named and explained.
6. The conceptual framework matches the variables in the questions.
7. The section ends with a gap that matches the problem statement.
8. Every in-text citation appears in the reference list, and vice versa.

Quick test: print the section and read only the first sentence of each paragraph. If that alone tells the story, the synthesis works.

**Five things to remember (literature review)**: (1) a review argues, a summary reports; (2) describe your search and defend it; (3) themes come from the sources; (4) disagreement is an opportunity; (5) the section must end in your gap.

Agent behaviour for this section: build the matrix and the search string with the user, but never supply sources from memory; locate and verify each source with tools, mark anything unverified, and hand the synthesis back as a draft the user must rewrite and own.

## 7. Section 3: The Methodology

*Source: Meeting 4 deck, "The Methodology Section".*

**Job**: turn the question into a procedure. The methodology states what data will be produced, from whom, by what means, and how those data will be analysed, in enough detail that another competent researcher could carry out the same study. It is the section where vagueness is punished hardest. It must prove the approach is **clear, justified, and repeatable**.

### 7.1 Three standards and four reader questions

| Standard | Meaning |
|---|---|
| **Replicable** | Someone else could follow the steps and produce comparable data. A step that exists only in the author's head is not written yet |
| **Justified** | Every choice is defended with a reason and, wherever possible, a precedent from the reviewed literature |
| **Feasible** | The plan can be executed with the time, access, budget, and skills the author actually has this semester |

Clarity + justification + feasibility = a methodology that earns trust.

**Four questions the reader will ask** (answer with enough detail to replicate):

1. **From whom will the data come?** Population (who the results apply to), sample (who will actually be studied), selection (how chosen), size (how many and why), reach (how contacted and included).
2. **By what means will it be produced?** Instrument or protocol (name and version), items or steps, response format or scale, evidence of why it measures what is claimed.
3. **In what order will you act?** Consent (how and when), distribution (how materials or data are given), timing (when each step occurs), follow-up (reminders, additional contacts), withdrawal (what happens if someone leaves).
4. **How will the data become findings?** Analysis plan (techniques), data to be used (which variables or sources), purpose (which question each analysis answers), assumptions and checks (how results will be verified).

Goal: leave no room for "I'm not sure."

### 7.2 Components and their common headings

| Component | What it must accomplish | Common heading |
|---|---|---|
| Research design | Names the overall approach and defends it against alternatives | Research Design |
| Participants and sampling | Defines population, technique, size, and access | Population and Sample |
| Instruments | Describes each tool and the evidence for its quality | Research Instruments |
| Procedure | Sets out the steps from first contact to a complete data set | Data Collection Procedure |
| Analysis plan | States the techniques applied to each type of data | Data Analysis |
| Quality assurance | Validity and reliability, or trustworthiness in qualitative work | Validity and Reliability |
| Ethics | Consent, confidentiality, approval, and risk to participants | Ethical Considerations |

A research timeline, and a budget where the work is funded, usually follow this section.

### 7.3 Method, methodology, and approach

| Term | Meaning | Examples |
|---|---|---|
| **Approach** | The broad stance toward evidence: what counts as knowledge in the study | Quantitative, qualitative, mixed methods |
| **Methodology** | The reasoned justification: why this design, sample, and instrument can answer the questions | "A quasi-experimental design is appropriate because random assignment is not possible in intact classes." |
| **Method** | The concrete technique or tool used to produce and treat data | A 24-item questionnaire; semi-structured interviews; thematic analysis |

Most sections labelled "Methodology" in student proposals contain only methods. **The reasoning is the part that earns marks.** When drafting, always attach a "because" to each choice.

### 7.4 Choosing a research design

The design is whatever can answer the question already committed to. The research question comes first; the design is the plan that best answers it. Cycle: question (what do I want to find out?), design (what plan will best answer it?), evidence (collect and analyse the right data).

**The design follows the question.** Work down this table with the user's own question; if no row fits, the question is still too vague.

| If the question asks... | You need data that... | Typical design |
|---|---|---|
| How prevalent or frequent something is | Describes a population numerically (for example, what percentage of students use AI tools weekly) | Descriptive survey |
| Whether two variables move together | Measures both variables in the same people (study time and GPA) | Correlational |
| Whether an intervention makes a difference | Compares groups before and after treatment | Experimental or quasi-experimental |
| How people experience or interpret something | Captures accounts in participants' own words | Phenomenology, case study, narrative |
| How a process unfolds in one setting | Follows events and actors over time | Case study or ethnography |

**Three broad approaches**

| Approach | Characteristics | Answers |
|---|---|---|
| Quantitative | Measures variables numerically; tests relationships or differences; larger samples, statistical analysis; aims for generalisation | How much, how many, how strongly, is there a difference |
| Qualitative | Produces textual or visual data; interprets meaning and process; smaller purposive samples; aims for depth and transferability | How, why, what does this mean to participants |
| Mixed methods | Combines both strands deliberately; requires a reason for combining; states sequence and priority; integrates, not just reports both | What happens, and why it happens that way |

Mixed methods is not "both, to be safe." It doubles the work and must be justified by a question neither strand can answer alone.

**Common quantitative designs**
- **Descriptive survey**: current state of variables in a population; no manipulation, no causal claim.
- **Correlational**: whether and how strongly variables move together; association, never causation on its own.
- **Causal-comparative**: compares groups that already differ, looking backwards for an explanation of the difference.
- **Quasi-experimental**: compares treated and untreated intact groups; common in education, where randomising classes is impossible.
- **True experimental**: random assignment to conditions with a controlled intervention; the strongest basis for causal claims.
- **Longitudinal**: repeated measurement of the same participants over time; powerful, and expensive in attrition.

How to choose: start with the question, identify the data needed, pick the simplest design that can answer it well; if no design fits, refine the question. Tip: name the design with the term the field recognises and state in one sentence why it fits the question.

**Common qualitative designs**
- **Case study**: one bounded system in depth, using several data sources.
- **Phenomenology**: the shared essence of how a group experiences one phenomenon, usually through in-depth interviews.
- **Grounded theory**: builds a theory from data through iterative coding and constant comparison.
- **Ethnography**: a culture or community through prolonged engagement and observation in its own setting.
- **Narrative inquiry**: the stories individuals tell about their experience, keeping chronology and voice intact.
- **Action research**: researcher and participants change a practice together (plan, act, observe, reflect) and study the change as it happens.

Do not label a study "qualitative descriptive" by default. Name the tradition and follow its procedures.

**Three mixed-methods designs.** State (1) the sequence, (2) the priority of each strand, and (3) the point at which the two are integrated.

| Design | Sequence | Use when |
|---|---|---|
| Convergent parallel | Both strands at the same time, independently, compared at interpretation | Measurement and meaning should corroborate one another |
| Explanatory sequential | Quantitative first; qualitative afterwards to explain surprising or unclear results | Numbers show what happened but not why |
| Exploratory sequential | Qualitative first; findings shape an instrument or hypothesis tested quantitatively | No suitable instrument exists for the context |

Example statement: "Explanatory sequential design: quantitative survey first, qualitative interviews second, integration during interpretation."

**Justifying the design: four sentences, one per point** (usually enough, and more than most proposals manage):
1. **Start from the question**: show that the data the design produces can, in principle, answer what was asked.
2. **Cite a precedent**: name studies from the literature review that used this design for a similar question.
3. **Rule out an alternative**: say briefly what was not chosen and why; this distinguishes a justification from an assertion.
4. **Acknowledge what it cannot do**: for example, a correlational design cannot establish cause. Saying so protects the author; hiding it invites the question.

### 7.5 Participants and sampling

Pipeline (each level narrows who the findings can legitimately speak about):

1. **Target population**: everyone the findings are meant to describe (all first-year undergraduates in Indonesia).
2. **Accessible population**: the part actually reachable (first-year students at the author's own institution).
3. **Sampling frame**: the list sampled from (enrolment records for three asynchronous courses).
4. **Sample**: those selected and invited (220 students drawn from that frame).
5. **Participants**: those who consented and provided usable data; the number actually reported.

**Generalisation stops at the accessible population.** Claiming more is the most common overreach in student work.

**Sampling techniques**

| Probability (every unit has a known chance) | Non-probability (selected for a reason) |
|---|---|
| Simple random: drawn at random from the full frame | Purposive: chosen because they have the experience studied |
| Systematic: every kth unit from a random start | Convenience: those available; state the limitation openly |
| Stratified: random within groups, preserving proportions | Quota: fixed numbers per category, without randomisation |
| Cluster: whole groups sampled, then all or some units inside | Snowball: participants recruit others, for hard-to-reach groups |
| Supports statistical generalisation; expected in most survey and experimental work | Standard in qualitative work, where the aim is depth and relevance rather than statistical representativeness |

Name the technique, state the criteria, and say how many. "Random" used loosely to mean "whoever replied" is a red flag.

**How many participants?** The right size depends on the study, the goal, and the reality of data collection.
1. **Quantitative: justify the number.** Base it on the planned analysis (number of groups or predictors, expected effect, precision needed) and cite the rule or calculation. Example: power analysis for multiple regression with 5 predictors, medium effect (f² = 0.15), power = 0.80, alpha = 0.05, giving a minimum of about 92.
2. **Qualitative: justify the depth.** Size is judged by whether the data answer the question. Explain the reasoning and how it was decided enough was collected (for example, 18 interviews; no new themes after the 15th, i.e. data saturation).
3. **Plan for attrition.** Declined invitations, incomplete responses, and withdrawals mean recruiting above the minimum. Example: need 92 complete surveys, expect 20% non-response, so invite at least 115.
4. **Defend it, do not guess.** "Thirty respondents, because that is a common number" is not a justification. State the basis, show the calculation or rule, report assumptions, plan for attrition.

Whatever number is proposed, write the sentence that begins "This number was chosen because...".

### 7.6 Instruments and operationalisation

Different tools collect different kinds of data. Name each clearly, describe how it works, and include it in the appendix.

| Instrument | Produces | What to state |
|---|---|---|
| Questionnaire | Numeric data and/or short text | Scale and number of items; closed items give numbers, open items give short text |
| Interview protocol | Detailed qualitative data in participants' words | Structured, semi-structured, or unstructured; attach the guide as an appendix, not a description of it |
| Observation schedule | Observed events, frequencies, or field notes | Defined categories or field notes; who observes, when, and for how long |
| Test or task | Scores, accuracy, time, task outcomes | How items were built or adopted; how scores are calculated |
| Documents and artefacts | Textual or visual evidence for content analysis or document review | Define the corpus and the period it covers |
| System and log data | Behavioural traces and usage metrics | Who owns the data and how access is authorised |

**Every instrument named must appear in full in an appendix. A described instrument cannot be judged.**

**Turning concepts into items (operationalisation).** Every variable must travel from concept (an idea in the model) to indicator (what it means in practice) to item (a question or statement) to response (what participants answer).

| Variable | Indicator | Sample item | Scale |
|---|---|---|---|
| Feedback timing | Perceived delay between submission and feedback | "I usually receive feedback in time to use it on the next task." | 5-point agreement |
| Behavioural engagement | Participation in course activities | "I contribute to the discussion forum in most modules." | 5-point frequency (Never to Very often) |
| Peer interaction | Exchanges with other students about coursework | "I discuss course tasks with other students during the week." | 5-point frequency |

Best practice: adapting a published, validated instrument is almost always better than writing your own; cite the source, state what was changed, and report permission where required.

### 7.7 Quality: validity and reliability, or trustworthiness

**Quantitative (validity and reliability)**: the instrument measures the right thing, in the right way, consistently. Pipeline: design (define construct), develop (create items), evaluate (test validity and reliability), use.

| Type | Meaning | Typical evidence |
|---|---|---|
| Content validity | Items cover the concept fully | Expert panel review against a blueprint; content validity index (CVI) |
| Construct validity | Measures the intended construct, shown by relationships with other measures | Correlations with related constructs; factor analysis; known-groups comparison |
| Criterion validity | Scores agree with an external standard, at the same time or later | Correlation with a gold standard or predictive validity |
| Internal consistency | Items intended to measure one construct behave consistently together | Cronbach's alpha (0.70 or above is acceptable) |
| Test-retest reliability | Same respondents give similar scores when measured again after an interval | Correlation (r or ICC) between Time 1 and Time 2 |
| Inter-rater reliability | Two independent raters classify the same material the same way | Agreement statistics (Cohen's kappa, ICC) |

Plan it in the timeline: state which types will be established, how, and when (for example a pilot study before main data collection). Pilot testing belongs in the timeline, not in a footnote.

**Qualitative (trustworthiness)**: findings are believable, relevant, and dependable. Use strategies that fit the design and report them clearly.

| Criterion | Question | How to do it |
|---|---|---|
| Credibility | Do the findings represent what participants meant? | Member checking, prolonged engagement, triangulation of sources, peer debriefing |
| Transferability | Could a reader judge whether this applies elsewhere? | Thick description of context, participants, and setting; purposeful sampling |
| Dependability | Would the process hold up to inspection? | Audit trail of decisions, documented methods, code-recode strategy, external audit if possible |
| Confirmability | Are the findings grounded in data rather than the researcher's assumptions? | Reflexivity (researcher journal), documented coding, data extracts supporting claims, independent review |

Do not borrow the words "valid and reliable" for a qualitative design. Use the criteria the tradition recognises, apply them consistently, and report how.

### 7.8 Writing the procedure

Written as a sequence a reader could follow. Past tense in the report; **future tense in the proposal**. Six steps:

1. **Obtain approvals**: ethics clearance, institutional permission, any gatekeeper consent, with dates; record approval IDs and dates.
2. **Pilot the instrument**: a small trial to check wording, timing, and the analysis pipeline; document what was tested and the changes made.
3. **Recruit and consent**: how participants are invited, what they are told, how consent is recorded; include inclusion and exclusion criteria.
4. **Collect the data**: when, where, in what form, how long each session or response window lasts; specify tool or platform and mode (online, in person).
5. **Manage and store**: naming, anonymisation, storage location, access control, retention period; state who can access the data and for how long.
6. **Prepare for analysis**: cleaning, transcription, coding of missing responses, exclusion rules; define rules before analysing the data.

Good practice: write in a clear sequence, use enough detail to replicate the steps, and report any deviations.

### 7.9 The analysis plan

Principle: a plan that does not map onto the research questions is not a plan. Map every analysis to a research question **and name the software** (for example SPSS, R, JASP, Jamovi).

**Quantitative analysis plan (five steps)**
1. **Prepare**: clean the data; handle missing responses by a stated rule; reverse-score items where needed.
2. **Describe**: report distributions (histograms); means and standard deviations for every variable; explore outliers.
3. **Check assumptions**: normality (Shapiro-Wilk, histogram, Q-Q plot); homogeneity of variance (Levene's test); independence of observations; any assumption the planned test requires.
4. **Test**: apply the technique chosen in advance for each question; state the significance level (for example alpha = .05); use appropriate post-hoc or follow-up tests if needed.
5. **Report**: effect sizes (Cohen's d, eta squared, r); confidence intervals; test statistics with df and p-values; focus on meaning, not p-values alone.

**Matching question to technique** (indicative only; the right technique depends on assumptions, design, and data; confirm with the supervisor or a statistician before collecting anything):

| Question | Data | Commonly used technique |
|---|---|---|
| Do two independent groups differ? | One continuous outcome, two groups | Independent-samples t-test, or a rank-based alternative |
| Do three or more groups differ? | One continuous outcome, several groups | One-way ANOVA, or a rank-based alternative |
| Do two variables move together? | Two continuous variables | Pearson correlation, or Spearman for ranked data |
| Does one variable predict another? | One outcome, one or more predictors | Linear or multiple regression |
| Are two categories associated? | Two categorical variables | Chi-square test of independence |

**Qualitative analysis plan** (thematic analysis shown as the most widely used example; whichever approach is used, name it and cite its source, for example Braun and Clarke, 2006):
1. **Familiarise**: transcribe, read repeatedly, note first impressions before coding anything.
2. **Code**: label segments systematically across the whole data set, keeping a codebook.
3. **Search for themes**: group codes into candidate themes that say something about the question.
4. **Review and define**: check themes against the data, merge or discard, name each precisely.
5. **Report**: write the account, evidenced with quotations that are attributed and anonymised.

State who codes, whether a second coder is involved, and how disagreements are resolved.

### 7.10 Ethics in the methodology (non-negotiables)

Ethics protects participants, strengthens the study, and builds trust. Write this section as if it will be audited; a study that would be ethical only if nobody checked is not ethical.

1. **Approval before collection**: ethics clearance and institutional permission before any data; describe the approval process and include dates.
2. **Informed consent**: tell participants the purpose, what is asked of them, risks (if any), benefits, and that they may withdraw at any time without penalty.
3. **Confidentiality and anonymity**: remove identifiers (names, IDs, contact details); state where data are stored, who has access, and when data will be destroyed.
4. **Care with vulnerable groups**: minors, patients, employees, and the author's own students need extra safeguards and, where required, guardian consent.
5. **Power and coercion**: no pressure or implied consequences for saying no; participation must never be linked to grades, jobs, or services.
6. **Tools and data handling**: do not upload identifiable participant data to external or public AI tools or services; follow the institution's policy on AI and data handling.

### 7.11 Research timeline, failure patterns, and checklist

**Research timeline** (indicative twelve-week schedule; the author's should match their own calendar, including approval waiting time): ethics approval and permissions (weeks 1 to 3), instrument preparation and pilot (weeks 2 to 4, refine after pilot before full launch), data collection (weeks 4 to 8), data analysis (weeks 8 to 10), writing the findings (weeks 9 to 11), revision and submission (weeks 10 to 12). **Ethics approval is the step students underestimate most**: ask the department how long it actually takes and schedule backwards from the deadline. (This is the lecture's generic example, not the 16-week course calendar in Part 2.)

**Where methodologies fail**

| # | Failure | Why it is a problem |
|---|---|---|
| 1 | Too vague to repeat ("Data will be analysed thematically" with no procedure, coder, software, or framework) | Others cannot repeat the steps or trust the findings |
| 2 | Design does not fit the question (interviews for a prevalence question; a survey for lived experience) | The method cannot produce the evidence the question needs |
| 3 | Sampling described loosely ("random sampling" for whoever responded to a broadcast link) | Not truly random; introduces bias and limits generalisability |
| 4 | Instrument neither cited nor attached | Readers cannot review items, scales, or validity |
| 5 | No quality evidence (no validity, reliability, or trustworthiness strategy) | Unclear if findings are credible or dependable |
| 6 | Ethics reduced to one sentence ("Ethical principles will be observed") | Does not show how participants' rights and wellbeing are protected |

Good methods are clear, justified, and verifiable.

**Methodology checklist (before submitting the draft)**
1. The design is named, justified, and linked to the research questions (for example cross-sectional survey, with why it fits).
2. Population, sampling technique, size, and access are all stated.
3. Each instrument is described, sourced (with citation), and attached as an appendix.
4. Variables are operationalised: concept, indicator, item, scale.
5. Validity and reliability, or trustworthiness, strategies are specified (pilot test, Cronbach's alpha, member checking, triangulation).
6. The procedure reads as steps another researcher could follow: what, where, when, how, by whom, for how long.
7. The analysis plan names techniques, maps them to each question, and names the software.
8. Ethics covers approval, consent, confidentiality, storage, retention, and potential risks.

Quick test: give the section to someone outside the topic and ask them to describe what they would do. What they cannot repeat is not written clearly enough.

**Five things to remember (methodology)**: (1) the question chooses the design (not familiarity, convenience, or what a friend used last semester); (2) replicability is the standard (a competent stranger could carry out the study without asking anything); (3) justify, do not merely describe (reason, precedent, acknowledged limitation); (4) quality evidence is part of the plan, designed in, not claimed afterwards; (5) ethics is written before data exists (approval, consent, and storage planned in the proposal, never retrofitted).

### 7.12 Applying the methodology to software-engineering and informatics studies

For software-engineering and informatics topics, the same logic applies to design-and-build studies: state the requirements source, the algorithm or method, datasets or test subjects, evaluation metrics, baselines for comparison, and how the solution will be validated. The method must produce evidence that answers the research question.

Agent guidance (an adaptation, not taken from the lecture slides): the decks use education and social-science examples. When the user's study builds or evaluates an artefact, translate the same four reader questions: *from whom or what* (datasets, repositories, systems, users), *by what means* (benchmark, instrumented prototype, usability test, log collection), *in what order* (build, evaluate, iterate, with a pilot and frozen test set), and *how data become findings* (named metrics, baselines, statistical comparison of runs or users). The "justify, cite a precedent, rule out an alternative, state the limit" pattern from 7.4 applies unchanged, as do operationalisation (define each metric precisely), quality evidence (reproducibility: fixed seeds, versioned data and code, stated environment), and ethics (user studies, personal data in datasets, scraped data terms of use).

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

For the deck's additional checks on questions (the six tests, question stems by design, general versus specific objectives, hypothesis rules), see Section 5.8; for the alignment table, see 5.9. For choosing a design from the question, see 7.4.

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

- **Timeline**: a realistic schedule, often a simple Gantt chart showing key tasks, order, and time needed. It is read as evidence that the author understands the size of the task. Typical tasks: ethics approval, literature review, instrument design and pilot, data collection, data analysis, report writing. Include approval waiting time and pilot testing explicitly; see 7.11 for the lecture's indicative twelve-week schedule.
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
- **Paraphrase, do not patchwrite**: changing a few words while keeping the sentence structure is plagiarism; quote with quotation marks and a page number every time; cite "as cited in" when a study was not read directly (see 6.10).
- **No coercion; protect vulnerable groups**: participation must never be linked to grades, jobs, or services; minors, patients, employees, and the author's own students need extra safeguards (see 7.10).
- **Participant data and AI tools**: never upload identifiable participant data to external or public AI tools; follow the institution's policy (see 7.10).

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

Section-specific failure lists from the lectures supplement this table: problem statements (5.7), literature reviews (6.10), and methodologies (7.11). Name the specific pattern when critiquing.

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

Weeks 1 to 4 syllabus: (1) course introduction and overview of research proposal writing; (2) Introduction section; (3) Literature Review section; (4) Methodology section. Lecture-deck cross references: Sections 5, 6, and 7 of Part 1 carry the content of Meetings 2, 3, and 4. Hand-offs stated in the decks: bring a **draft introduction and ten sources to Week 3**; bring your **literature matrix to Week 4**; Meeting 4 closes the four-week series. Use these to check whether a student is ready for the next meeting.

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

Reconciling with the lecture: the Meeting 3 deck calls the narrative review the default for a thesis proposal, while this assignment is worded as a "systematic literature review" with a prescribed format. Follow the assignment guide and rubric as authoritative. In practice that means borrowing the systematic habits from 6.6 (documented search strings, databases, dates, explicit inclusion and exclusion criteria, a tracked screening count), keeping the per-source attributes the rubric scores, and then writing the synthesis as an argument (6.7 to 6.9). The literature matrix (6.7) is the working tool for both. If the guide and the lecture conflict, ask the lecturer or supervisor.

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

Five-part problem statement skeleton (Section 5.7): Ideal (what should happen, with citation). Reality (what happens, with citation). Gap (type of gap, stated precisely). Consequence (cost, and to whom). Response (one sentence, no method detail).

Alignment table (Section 5.9):

| Problem element | Research question | Objective (action verb) | Evidence that would answer it |
|---|---|---|---|
| | | | |

Search plan (Section 6.6): research question; concept table (concept, synonyms and variants, narrower or broader terms); search string with Boolean operators; databases; date; filters; inclusion and exclusion criteria; counts at each stage (Found, After duplicates, After title screening, After full text, Included).

Literature matrix columns (Section 6.7): Source (with DOI), Context, Design, Key finding, Relevance to my study; add Limitations, Theory, or Country as needed.

Synthesis paragraph skeleton (Section 6.9): Claim (the author's point). Evidence (two or more sources that agree). Evaluation (compare, qualify, explain the difference). Link (what remains unsettled and what comes next).

Design justification (Section 7.4), four sentences: (1) this design generates data that answers the research question because...; (2) it was used for a similar question by (verified sources), who found...; (3) alternatives considered were ... and are less suitable because...; (4) its limits are ... and they will be handled by...

Sample size sentence (Section 7.5): "This number was chosen because [rule or calculation, with assumptions], and [expected attrition] was added, giving [n invited] for [n required]."

Operationalisation table (Section 7.6):

| Variable (concept) | Indicator | Sample item or metric | Scale or measure |
|---|---|---|---|
| | | | |

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
- For introductions: insist on evidence in the background, the five-part problem statement with gap and consequence, a named gap type, and objectives with demonstrable verbs; run the alignment table.
- For literature reviews: build the search string, criteria, and matrix with the user; never supply sources from memory; the last paragraph must state the same gap as the problem statement.
- For methodologies: require the reasoning ("because"), not only the methods; name design, sampling technique and size basis, instruments (attached), quality strategy, procedure, analysis mapped to each question with software, and ethics in full; warn that ethics approval and pilot time are the most underestimated items.
- Keep responses proportionate: a quick question gets a short answer; a full draft or review gets the templates above.
