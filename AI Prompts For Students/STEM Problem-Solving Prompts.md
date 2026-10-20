# STEM Problem-Solving Prompts

Companion prompts to the main students guide for quantitative courses: working problem sets honestly, debugging your own solutions, and using AI to understand methods without letting it do the doing. The integrity rule from the Academic Integrity file applies throughout: if the problem set is graded, the work you submit must be yours.

***

## 1. The Guided Solution (Socratic Mode)

**Prompt:**
```
You are a problem-solving tutor for [SUBJECT]. Here is my problem: [PASTE
PROBLEM]. Strict rules:
1. Do NOT solve it for me.
2. Start by asking me what the problem is asking, what's given, and what
   principles might apply — one question at a time.
3. When I take a wrong turn, don't correct me directly — ask the question that
   will make me notice ("what are the units of that term?").
4. If I am truly stuck after an attempt, give ONE hint. Escalate hints only
   after another attempt.
5. When I have a solution, check it and identify errors the same way — by
   questioning, not correction.
```

- **Purpose:** Getting unstuck on problem sets while the learning stays in your head.
- **Why it works:** The Socratic structure mirrors how office hours work when they work — the moment you see your own error is the moment it stops recurring.
- **Use Case:** Weekly problem sets, textbook exercises.
- **Expert Variation:**
```
After we solve it, generate the transfer problem: same principle, different
context — so I verify I learned the method, not this problem.
```

***

## 2. Solution Autopsy (After Getting It Wrong)

**Prompt:**
```
I got this problem wrong. My work: [PASTE]. The correct answer: [ANSWER if
known].
1. Find the FIRST step where my work goes wrong — the error, not the symptom.
   (A wrong final number is a symptom; a sign error in step 3 is the disease.)
2. Classify the error: concept misunderstanding / procedure slip / notation
   confusion / misread problem / arithmetic.
3. Ask me the diagnostic question that tests whether I now see it — do not
   explain yet. If I cannot find it, THEN walk me to it.
4. Prescribe the fix for THIS error class: what to drill, what to write at the
   top of my page next time, what to double-check.
```

- **Purpose:** Extracting the maximum learning from every wrong answer.
- **Why it works:** First-wrong-step analysis prevents the classic failure of re-doing the problem correctly and learning nothing — because you never located your actual error.
- **Use Case:** Returned problem sets, practice exams, mock tests.
- **Expert Variation:**
```
Add the error journal entry: my error, in my words, plus the trigger ("when I
see [X pattern], watch for [this error]") — my personalized errata sheet.
```

***

## 3. Method Selection Trainer

**Prompt:**
```
I am studying [TOPIC — e.g., integration techniques / hypothesis tests /
circuit analysis]. Train me on METHOD SELECTION, the exam skill:
1. Present a problem WITHOUT telling me the topic or method: [generate or use
   my list].
2. I must first say WHICH method applies and WHY — before any computation.
3. Then I attempt it. You check both the method choice and the execution.
4. After [5] problems: my selection accuracy, my confusion patterns (which
   two methods do I mix up?), and what discriminates them.
```

- **Purpose:** Training the recognition step that exams test first and students practice never.
- **Why it works:** Exams mix methods; blocked practice (10 problems of the same type) never exercises selection — this fixes that.
- **Use Case:** Exam prep for cumulative material.
- **Expert Variation:**
```
Include 2 problems that require TWO methods in sequence — where the hard part
is seeing that step 1's output is step 2's input.
```

**Limitations & verification:** Generated problems occasionally have typos or unsolvable setups — if a problem seems wrong, verify against the textbook or ask the model to re-check its own problem statement before assuming you are confused.

***

## 4. Concept-Formula Bridge

**Prompt:**
```
Formula: [PASTE]. I can use it but I want to UNDERSTAND it:
1. Explain what each term IS physically/geometrically — not its units only,
   its meaning.
2. Walk through a minimal example where the formula does something I can
   verify by intuition or by hand.
3. The boundary: when does this formula NOT apply? What do people wrongly
   apply it to?
4. Where does it come from — the one-paragraph derivation sketch that makes
   its shape feel inevitable rather than memorized?
5. Quiz me: 3 questions testing meaning, not symbol manipulation.
```

- **Purpose:** Converting memorized formulas into usable understanding.
- **Why it works:** The "when does it not apply" question is where exam traps and real-world mistakes live — and where rote learning is silent.
- **Use Case:** Physics, chemistry, engineering courses; statistics formulas.
- **Expert Variation:**
```
Connect it: what more advanced concept generalizes this formula, and what
special case reduces to it — my map of the formula's neighborhood.
```

***

## 5. Proof Comprehension (Read-Then-Reproduce)

**Prompt:**
```
Here is a theorem and proof from my course: [PASTE].
1. Structure it: what is the proof's strategy in one sentence? What are its
   load-bearing steps?
2. For each load-bearing step: the justification — and if the proof skips
   justification ("clearly...", "it follows that..."), flag it and make me
   supply the missing reason.
3. The purpose test: why THIS theorem — what breaks in later material if it
   were false?
4. Now hide the proof from both of us: I reproduce it from the strategy
   outline alone. You compare and mark what I dropped — dropped steps are
   gaps in understanding, not memory lapses.
```

- **Purpose:** Proof-based courses: comprehension that survives reproduction.
- **Why it works:** Strategy-first reproduction tests exactly what "understanding a proof" means — being able to rebuild it, not recite it.
- **Use Case:** Mathematics, theoretical CS, logic-heavy courses.
- **Expert Variation:**
```
The modification drill: change one hypothesis of the theorem — does the proof
survive? Where exactly does it break? That breakpoint is the theorem's real
content.
```

***

## 6. Lab & Data Report Reasoning

**Prompt:**
```
My lab data: [PASTE or describe]. Intended analysis: [PLANNED TEST/MODEL].
Before I write anything:
1. Sanity check the data: outliers, impossible values, units, precision —
   list anything I should look at before trusting my own analysis.
2. Does my planned analysis actually answer the lab question? What would
   answer it better if not?
3. The uncertainty story: what are my error sources, and how should they be
   propagated/reported for THIS lab?
4. Draft the results-section skeleton: what a complete report includes, so I
   fill in the reasoning myself.
Do not perform the analysis — check my plan and my data, then hand it back.
```

- **Purpose:** Lab reports with sound reasoning and honest uncertainty.
- **Why it works:** Pre-analysis sanity checking catches the garbage-in problem before it becomes a graded garbage-out problem.
- **Use Case:** Physics/chemistry/biology labs, statistics projects.
- **Expert Variation:**
```
Add the pre-submission audit: the 5 things lab graders check (units, sig figs,
error treatment, question answered, conclusion supported by data) as a
self-grade checklist.
```

**Limitations & verification:** Recompute all statistics and error propagation yourself — arithmetic from AI assistance must be verified line by line before it enters a graded report, and your course's AI policy governs what assistance is permitted at all.

***

## Shared Verification Rules for All STEM Prompts

1. **Graded work is your work.** These prompts are tutors and checkers; check each course's policy and keep the submission trail authentically yours.
2. **Verify every computation.** AI assistance makes arithmetic and algebra errors exactly where humans do — final answers get independent checking.
3. **Generated problems may be flawed.** Treat suspicious problem statements as error-spotting practice; verify against course materials.
4. **First-wrong-step discipline.** When reviewing errors, never settle for "the answer was wrong" — find the exact step where it went wrong, or the learning moment is lost.
