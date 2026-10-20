# AI Literacy for Students Prompts

Companion prompts to the main teachers guide — with a twist: these prompts are FOR use WITH students, turning the AI tool itself into the object of study. Students who understand what these systems are (and are not) make better decisions with them than students who were merely warned about them.

***

## 1. The Hallucination Demonstration

**Prompt (teacher runs this live with the class, or prepares it beforehand):**
```
I am teaching students how AI models can produce confident falsehoods.
Generate for me, on a topic I know well: [TEACHER'S TOPIC — e.g., your own
school's fictional history, a niche hobby, a local landmark]:
1. A short paragraph of 5 factual-sounding claims, where exactly 2 are subtly
   wrong — realistic, plausible, confident.
2. An answer key identifying the false claims and the specific tells that
   could reveal them (no source, impossible date, conflated details).
3. 3 discussion questions: why do the false ones FEEL true? What would it
   take to check each? When does confidence become a red flag?
```

- **Purpose:** Letting students experience, in controlled conditions, that fluent is not the same as correct.
- **Why it works:** The demonstration lands because the errors are about something the teacher knows and students can verify — the visceral version of the lesson "verify before you trust."
- **Use Case:** Digital literacy units, research-skills courses, orientation for AI use.
- **Expert Variation:**
```
Repeat with a topic STUDENTS know well (their town, their game, their music
scene) — the errors become immediately, embarrassingly visible, and the lesson
transfers.
```

***

## 2. Interrogating the Machine

**Prompt (students use this with any AI tool, as a class exercise):**
```
Students: interview an AI about itself and fact-check what it says.
1. Ask the AI: "What are you? How do you work? What can't you do?" — record
   its answers.
2. Compare its self-description with what your teacher/textbook says about
   how language models actually work (next-token prediction, training data
   cutoffs, no live knowledge by default).
3. Where did the AI's self-description differ from the technical reality?
   Why might a system built from text patterns describe itself imperfectly?
4. The takeaway question: if a system can be wrong about ITSELF, what does
   that suggest about its other claims?
```

- **Purpose:** Grounding the abstract lesson "AI has limits" in direct, observable evidence.
- **Why it works:** Students discovering the discrepancy themselves beats being told about it — the Socratic method applied to the machine.
- **Use Case:** Computer science courses, technology units, homeroom digital citizenship.
- **Expert Variation:**
```
Extend to capability probing: design 5 tasks — one the AI should do well,
one it should fail (recent events), one it should approximate (arithmetic),
one where it confabulates (obscure citations), one where it refuses. Test
and map the results.
```

***

## 3. Bias Detective Exercise

**Prompt:**
```
I am teaching students to detect bias patterns in AI output. Design the
exercise:
1. Three short, innocuous prompts that typically reveal default patterns —
   e.g., "write a story about a nurse and an engineer", "describe a
   typical CEO", "give baby names for a future scientist".
2. For each: what default pattern to look for (gender, culture, age,
   geography), and the tally sheet students use to record what appeared.
3. The re-run: students rewrite each prompt to request diversity explicitly
   — and compare what changes.
4. Discussion questions: where do these defaults come from (training data)?
   What does it mean that they surface without anyone asking? What does
   requiring explicit instruction to include diversity imply about default
   settings?
```

- **Purpose:** Making representation defaults visible rather than argued about.
- **Why it works:** The tally-and-rerun structure produces the students' own evidence, which converts an abstract social concept into observed data.
- **Use Case:** Media literacy, social studies, language arts.
- **Expert Variation:**
```
Add the swap test: students exchange the identity of characters in AI output
and re-read — noting what suddenly feels 'off' and what that reveals about
the original default.
```

***

## 4. Prompt Comparison Lab

**Prompt (structure for a student lab):**
```
Lab design: students compare prompt quality systematically.
1. Students receive a task: [AGE-APPROPRIATE TASK — e.g., "get a good
   explanation of photosynthesis for a 5th grader"].
2. Each writes 3 prompts: a lazy one ("tell me about photosynthesis"), a
   specific one (audience + format + scope), and their own best attempt.
3. They run all three and score outputs with a simple rubric I provide:
   correct, clear, right level, useful (each 1-5).
4. Class data pooling: which prompt characteristics correlated with higher
   scores? Students derive the principles (specificity, context, format)
   from THEIR OWN data.
```

- **Purpose:** Students discovering prompt craft as an empirical discipline, not a list of tips.
- **Why it works:** The pooled class data converts anecdote into pattern — the same evidence-based mindset the science classroom teaches, applied to language.
- **Use Case:** Any course beginning to permit AI use; information skills courses.
- **Expert Variation:**
```
Round 2: students exchange their best prompts with a partner who tries to
BREAK them (ambiguous terms, missing edge cases) — introducing the idea that
prompts are drafts that need testing.
```

***

## 5. The Verification Habit Builder

**Prompt:**
```
I am building students' verification reflex before they use AI for schoolwork.
Design a 15-minute recurring exercise:
1. I provide an AI-generated paragraph on current course content: [TEACHER
   PASTES ONE THEY HAVE PRE-CHECKED].
2. Students play fact-checker: every claim sorted into VERIFIED (they found
   it in the textbook/notes), UNVERIFIED (couldn't confirm), CONTRADICTED
   (textbook says otherwise).
3. The tally and discussion: how many claims were checkable? How long did
   verification take versus generation? What does that ratio mean for
   trusting AI output on deadline?
4. The habit line: "AI drafts, you verify" — co-authored with the class as
   a poster/syllabus statement.
```

- **Purpose:** The single most important AI-era study habit, rehearsed until automatic.
- **Why it works:** The generation-versus-verification time comparison makes the hidden cost of AI trust tangible — students feel why "it's faster" is only true when you skip the safety step.
- **Use Case:** Any course allowing AI assistance; research units; library partnerships.
- **Expert Variation:**
```
Escalate over the semester: paragraph → statistics → citations (the hard
case — fabricated references that look perfect).
```

***

## 6. Designing a Class AI Agreement

**Prompt:**
```
Facilitate my class creating its own AI use agreement. My course context:
[GRADE, SUBJECT, CURRENT POLICY IF ANY].
1. The framing questions for discussion: What should AI be allowed to do in
   OUR class, and why? What would make its use unfair to classmates? What
   would make it unfair to your future self?
2. Draft the agreement structure: permitted uses / prohibited uses /
   disclosure convention / consequences — in student language, not policy
   language.
3. The scenario cards: 5 realistic gray-zone scenarios (used AI to brainstorm
   but wrote it myself; AI explained a concept before the exam; AI drafted
   my intro paragraph) — the class debates where each falls under OUR
   agreement.
4. The revisit clause: scheduled re-negotiation date — because both tools
   and norms will change before the year ends.
```

- **Purpose:** An AI policy the class owns rather than evades.
- **Why it works:** Co-authored norms get enforced by peers; imposed norms get tested by them. The gray-zone scenario cards do the real teaching.
- **Use Case:** Start of term, or when a violation reveals the current policy is failing.
- **Expert Variation:**
```
Add the parallel professional conversation: how do working adults in
[FIELD] handle the same questions? Students draft advice to a hypothetical
new hire — connecting classroom norms to career norms.
```

**Limitations & verification:** Final authority stays with school policy — the class agreement works WITHIN it, not around it. Check district and school rules before the negotiation starts, and surface conflicts as part of the lesson about real-world policy layers.

***

## Shared Verification Rules for All AI Literacy Prompts

1. **Pre-check every demonstration.** AI output prepared for classroom display must be verified by the teacher beforehand — an unexpected fabrication in the fabrication demonstration is still a fabrication on your screen.
2. **Age and policy appropriate.** Tool access for students must respect the platform's age terms and district approval (see the Student Privacy file in this collection).
3. **The goal is judgment, not rules.** Every exercise here builds the student's own evaluative instincts — the technology will change every year, but the habits of verification, skepticism, and honest disclosure are the durable curriculum.
