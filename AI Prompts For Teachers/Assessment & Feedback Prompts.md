# Assessment & Feedback Prompts

Companion prompts to the main teachers guide for the assessment cycle: designing assessments that measure what was taught, building fair rubrics, writing feedback that students actually use, and keeping grading sustainable. AI drafts and structures — the professional judgment on every score and comment remains the teacher's.

***

## 1. Assessment Blueprint (Before Writing Questions)

**Prompt:**
```
Design an assessment blueprint before any questions get written.
Unit objectives: [LIST with Bloom levels]. Assessment type: [QUIZ/TEST/PROJECT].
Constraints: [TIME, FORMAT].
1. Build the blueprint table: each objective mapped to question count, weight,
   and Bloom level — so the test samples what was taught, proportionally.
2. The coverage check: which objectives are over- or under-weighted relative
   to instruction time and importance? Flag mismatches.
3. The difficulty spread: easy/medium/challenging ratios appropriate for
   [PURPOSE — formative check vs summative gate].
4. Question format guidance: which objectives genuinely need [WRITTEN/OPEN
   RESPONSE] versus being adequately measured by selected response?
5. Only after my approval of the blueprint: draft questions per cell.
```

- **Purpose:** Assessments with validity by construction — the blueprint comes first.
- **Why it works:** The objective-weight-alignment table prevents the classic invalidity: a test that measures reading stamina more than the taught content.
- **Use Case:** Unit tests, finals, project-based assessment design.
- **Expert Variation:**
```
Add the accommodation plan: which items will exist in alternate formats, which
timings flex, decided at blueprint stage rather than retrofitted.
```

***

## 2. Rubric Construction & Calibration

**Prompt:**
```
Build a rubric for: [TASK — e.g., lab report, persuasive essay, project].
Objectives assessed: [LIST]. Grade level: [LEVEL].
1. The criteria list: 4-6 dimensions, each observable and distinct — flag any
   proposed criterion that is really two criteria fused.
2. For each criterion: 4 performance levels described in OBSERVABLE terms —
   what a grader sees, not what a student "understands".
3. The anchor examples: for each level of the most important criterion, one
   sentence of what anchor student work would look like.
4. The boundary guide: descriptors for the two hardest calls — "is this a 2
   or a 3?" for each criterion.
5. Weighting suggestion with rationale — which criterion carries the grade's
   signal.
```

- **Purpose:** Rubrics that two graders apply the same way.
- **Why it works:** Observable-terms discipline and boundary descriptors attack the reliability problem where it lives — the fuzzy middle levels.
- **Use Case:** Essays, projects, performances, lab reports.
- **Expert Variation:**
```
Generate the calibration packet: 4 hypothetical student responses spanning
the quality range, for a grading team to score independently then reconcile
against my key.
```

**Limitations & verification:** Run any generated rubric against real student work samples before going live — descriptors that sound precise often break on the first messy submission.

***

## 3. Question Quality Audit

**Prompt:**
```
Audit these questions before I use them: [PASTE QUESTIONS].
1. Clarity: ambiguous stems, double-barreled questions, negative constructions
   ("which is NOT...") used without emphasis, stems that test reading more
   than content.
2. Selected-response specifics: implausible distractors, "all of the above"
   patterns, answer-position bias, clues in grammar.
3. Bias scan: cultural/interest contexts that advantage some students,
   name/example representation, socioeconomic assumptions.
4. Alignment: each question's objective and Bloom level — flag anything below
   the assessment blueprint's intent.
5. Output: verdict per question (use / fix / replace) with the specific fix.
```

- **Purpose:** Catching question flaws before students find them the hard way.
- **Why it works:** Reading-load and bias effects are exactly the flaws invisible to the author who wrote the questions.
- **Use Case:** Before any quiz or test administration.
- **Expert Variation:**
```
For every "fix" verdict, produce the revised item — then the parallel item
(for my retake/alternate version bank, psychometrically matched).
```

***

## 4. Feedback That Gets Used

**Prompt:**
```
Help me write feedback for this student work: [PASTE WORK + RUBRIC SCORES +
MY NOTES]. Feedback rules:
1. Lead with one strength that is specific and true — quote the line that
   shows it.
2. The ONE highest-leverage improvement — not every issue I found. Which
   single change would move this work up a level?
3. The feedback must be actionable as a next step, not a verdict on ability:
   "rework this paragraph so that..." not "your analysis is weak".
4. One question that prompts the student's own revision thinking.
5. End with what I will look for when they revise.
Keep it under 120 words — feedback length beyond that is not read twice.
```

- **Purpose:** Feedback students can act on, at a length they will process.
- **Why it works:** One-lever feedback respects the research consensus: more comments do not produce more improvement; one clear next step does.
- **Use Case:** Essay returns, project checkpoints, lab reports.
- **Expert Variation:**
```
Produce the class-level pattern report instead of individual comments first:
what did MOST students miss? That becomes my reteach mini-lesson, and
individual feedback then only covers what deviates from the pattern.
```

**Limitations & verification:** Every drafted comment is reviewed and owned by the teacher before it reaches a student — the teacher saw the work; the model saw the excerpt. Verify quoted lines actually appear in the work.

***

## 5. Grading Workflow & Sustainability

**Prompt:**
```
Design my grading workflow for: [ASSESSMENT, N STUDENTS, DEADLINE].
1. The batching plan: grade criterion-by-criterion across all papers (not
   paper-by-paper) — where does this improve consistency, and where is it
   wrong for my assessment type?
2. The calibration sequence: 3 anchor papers first (high/medium/low), scored
   against the rubric, to lock my internal standard before speed begins.
3. Fatigue management: where to take breaks, and the drift check — re-score
   one early paper at the end; if it moved, my standard drifted.
4. The comment efficiency system: my frequently-needed feedback phrases
   pre-drafted for the pattern issues, personalized per student with one
   specific line each.
5. The integrity check: name-blind grading where feasible — re-order so I
   cannot track whose paper is whose.
```

- **Purpose:** Grading that is consistent at paper 40 as at paper 1, and survives the week.
- **Why it works:** Anchors-then-batch-then-drift-check is the reliability protocol adapted for a single grader with a stack.
- **Use Case:** Essay-heavy weeks, finals seasons, project portfolios.
- **Expert Variation:**
```
Add the moderation sample plan: which subset a colleague double-scores for
inter-rater reliability, and the conversation protocol if we diverge.
```

***

## 6. Post-Assessment Analysis

**Prompt:**
```
Here are my item-level results: [PASTE — per-question correctness/distribution,
plus any rubric-level patterns]. Help me read them honestly:
1. Item diagnosis: which questions discriminate well, which everyone missed
   (bad item or untaught content?), which everyone got (wasted measurement?).
2. The distractor analysis: for the most-missed selected-response item, what
   did the wrong answers attract — and what misunderstanding does each
   popular distractor reveal?
3. The reteach decision: which ONE concept gets a reteach cycle, based on
   weight in the blueprint and miss pattern — not on my surprise alone.
4. The assessment autopsy: what should I change about the assessment itself
   before next administration?
5. Note where results could mislead: small n, timing issues, known
   accommodations — before I over-interpret.
```

- **Purpose:** Assessment data as instruction feedback, not just grades.
- **Why it works:** The distractor-as-window framing turns wrong answers into diagnosis — the highest-value read of any item analysis.
- **Use Case:** After every summative assessment; quarterly pattern reviews.
- **Expert Variation:**
```
Track it: build the longitudinal view — this concept's performance across my
last [N] assessments/years of teaching it, and what has changed.
```

**Limitations & verification:** Recompute all percentages and distributions from raw data — and remember that student data is sensitive: anonymize class-level data in any prompt (see the privacy file in this collection).

***

## Shared Verification Rules for All Assessment Prompts

1. **Scores and decisions are the teacher's.** AI drafts rubrics, questions, and feedback; the professional judgment that assigns grades and shapes a student's trajectory never transfers to a tool.
2. **Never feed identifiable student work into consumer AI tools.** Anonymize before pasting; see the Student Privacy file — this is both an ethics and (in many jurisdictions) a legal requirement.
3. **Pilot generated assessments.** Every AI-drafted question is a hypothesis about clarity and difficulty until a colleague or a small trial run checks it.
4. **Feedback is a relationship, not a message.** Whatever the draft says, the teacher's voice and knowledge of the student make it land — edit every comment into words you would say aloud.
