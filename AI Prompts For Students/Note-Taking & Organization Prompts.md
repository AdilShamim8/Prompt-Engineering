# Note-Taking & Organization Prompts

Companion prompts to the main students guide for the systems layer of studying: capturing lectures well, building notes that support retrieval practice, and keeping a semester's chaos navigable. Notes are infrastructure — these prompts build them for the way memory actually works.

***

## 1. Lecture Note Conversion (Raw to Usable)

**Prompt:**
```
Here are my raw lecture notes: [PASTE — messy, abbreviations, gaps].
Convert them into working notes WITHOUT adding content I did not write:
1. Reorganize into: main concepts, supporting details, examples, and
   open questions I flagged.
2. Preserve my abbreviations' meaning — expand only ones I define here:
   [LIST or "ask me"].
3. Mark every gap clearly as [MISSING — get from: classmate/textbook/next
   lecture] rather than filling it with plausible content.
4. End with a 5-question self-quiz on what IS there.
```

- **Purpose:** Turning lecture scribbles into retrieval-ready notes without fabricated content.
- **Why it works:** The "no filling gaps" rule keeps the model honest — the most dangerous note-taking failure is a plausible invented patch over what you missed.
- **Use Case:** After every lecture, within 24 hours while context remains.
- **Expert Variation:**
```
Also produce the Cornell layout version: cue column questions, notes column,
summary — so each page supports active recall, not just re-reading.
```

***

## 2. Concept Map Construction

**Prompt:**
```
From my notes on [TOPIC]: [PASTE], build a concept map specification:
1. The 7-10 core concepts as nodes — only ones that appear in my notes.
2. The edges: for each relationship, name the TYPE (causes, is-part-of,
   contrasts-with, requires, example-of) and the direction.
3. Flag relationships I asserted but my notes do not support — I need to
   verify those.
4. Output as an indented text tree I can also draw, plus a DOT/Graphviz
   snippet for a rendered version.
```

- **Purpose:** Structure knowledge so retrieval has multiple pathways.
- **Why it works:** Typed, directional edges force precision about relationships — the sloppiness in most "concept maps" is unlabeled arrows.
- **Use Case:** Cumulative topics, exam review synthesis, thesis planning.
- **Expert Variation:**
```
Add the isolation test: which single concept, if I fail to understand it,
breaks the most edges? That is my priority for review.
```

***

## 3. The Anki-Ready Question Factory

**Prompt:**
```
From my notes: [PASTE], generate spaced-repetition flashcards.
Rules:
1. Atomic: one fact, one question — no compound cards ("list and explain X,
   Y, and Z" is three cards).
2. Bidirectional where it matters: term→definition AND definition→term for
   concepts that must be recognized both ways.
3. Application cards, not just recall: "You see [SCENARIO] — which concept
   applies and why?" for every major concept.
4. Cloze deletions for dense factual sentences, with the deletions chosen so
   each card tests one gap.
5. Flag cards that are ambiguous or could be argued two ways — I will fix or
   delete rather than memorize ambiguity.
Output in [Anki CSV / question-tab, answer-tab] format.
```

- **Purpose:** Notes that convert directly into the retrieval-practice system.
- **Why it works:** Atomicity and application-orientation follow spaced-repetition best practice — the card quality determines whether the system works at all.
- **Use Case:** Vocabulary-heavy courses, medicine/law-style memorization loads.
- **Expert Variation:**
```
Add a "leech detector": which of these cards will I probably keep forgetting
(because they test rote pairs with no meaning)? For each, generate a
meaning-based variant instead.
```

**Limitations & verification:** Verify every generated card against your course materials — a wrong card is worse than no card, because you review it repeatedly.

***

## 4. Reading Notes That Don't Lie

**Prompt:**
```
I am reading [TEXT] for [COURSE]. Help me take reading notes that capture what
is actually there:
1. I paste each section; you structure MY summary attempts: main claim, evidence
   given, and the author's transition to the next section.
2. Distinguish explicitly: what the author claims / what the author shows /
   what the author assumes.
3. Mark where I drifted into paraphrasing so close to the original that I
   should either quote it properly or re-say it in my own words.
4. After the full text: the one-paragraph summary, the three questions this
   reading raises, and how it connects to [PREVIOUS READING].
```

- **Purpose:** Reading notes that support essays later — with quotation hygiene built in.
- **Why it works:** The claim/show/assume distinction is the analytic habit that essays are graded on.
- **Use Case:** Reading-heavy humanities and social science courses.
- **Expert Variation:**
```
Maintain a running glossary across readings: every term the course defines,
where it was defined, and how definitions shift between authors.
```

***

## 5. Semester Command Center

**Prompt:**
```
Design my semester organization. Courses: [LIST with workloads]. Deadlines I
know: [LIST]. My constraints: [JOB/COMMUTE/OTHER].
1. The master calendar structure: how to track every deadline in one view —
   with a weekly review ritual that keeps it truthful.
2. The per-course pipeline: inbox (unprocessed) → active (this week) →
   archived, adapted to my tools: [NOTION/PAPER/NOTES APP].
3. The early-warning layer: for each course, what signal tells me I am falling
   behind BEFORE the deadline crisis — and what to do when it fires.
4. The weekly template: my realistic schedule with study blocks placed where
   my energy actually is: [MORNING/EVENING PERSON].
```

- **Purpose:** A system that catches problems weeks before deadlines do.
- **Why it works:** The early-warning layer converts organization from record-keeping into prevention.
- **Use Case:** Semester start, mid-semester rescue.
- **Expert Variation:**
```
Add the crunch protocol: the pre-planned triage for the week where everything
lands at once — what gets done properly, what gets done minimally, what gets
negotiated with instructors, decided NOW rather than in panic.
```

***

## 6. The Friday Review Ritual

**Prompt:**
```
Design my 20-minute Friday review for [SEMESTER/ COURSES]:
1. The checklist: what to update (calendar truth vs plan), what to capture
   (next week's deadlines, reading assignments), what to file (this week's
   notes into the archive).
2. The two reflection questions: what worked this week / what will I change —
   answered in writing, one line each.
3. The lookahead: next week's known demands against available time — flag the
   overload day NOW, while there is still a choice about it.
4. Format it as a repeatable template I can run in a notebook or [APP].
```

- **Purpose:** Twenty minutes a week that prevent the month-end avalanche.
- **Why it works:** The written micro-reflection closes the planning loop; systems without feedback loops decay quietly.
- **Use Case:** Any semester, any workload — the ritual is workload-agnostic.

***

## Shared Verification Rules for All Note Prompts

1. **Never let AI patch your gaps with invented content.** The [MISSING] marker is a feature — a plausible fabrication in your notes is a landmine that survives until the exam.
2. **Course materials outrank AI output.** Where the structured version of your notes disagrees with the textbook or lecturer, the course wins; investigate the discrepancy.
3. **Notes are for retrieval, not storage.** If a note format cannot generate a self-quiz question, it is archiving, not learning.
4. **The system you maintain beats the system that is perfect.** Choose the format you will actually touch weekly.
