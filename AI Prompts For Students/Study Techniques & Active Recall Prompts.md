# Study Techniques & Active Recall Prompts

Companion prompts to the main students guide. The science of learning is unambiguous: testing yourself beats re-reading, spacing beats cramming, and explaining beats highlighting. These prompts turn AI into a study partner that makes you do the cognitive work — instead of doing it for you.

***

## 1. The Reverse Tutor (AI as Quizmaster, Not Answerer)

**Prompt:**
```
You are my study partner for [TOPIC]. My level: [e.g., second-semester biology].
Rules of engagement:
1. Ask me ONE question at a time, starting easy and adapting to my answers.
2. Never give me the answer until I have attempted it — if I'm stuck, give a hint,
   not the solution.
3. When I answer, tell me what was right AND what was incomplete, then ask a
   follow-up that probes the incomplete part.
4. After 10 questions, summarize: what I have down, what's shaky, what to review
   tomorrow.
Start now with your first question.
```

- **Purpose:** Converting passive review into retrieval practice — the highest-evidence study technique there is.
- **Why it works:** The "hint, not solution" and "one question at a time" rules keep the cognitive effort where learning happens.
- **Use Case:** Any exam prep, concept mastery, interview practice.
- **Expert Variation:**
```
Add spaced repetition: track which questions I got wrong, and re-ask them after
3 intervening questions, then after 10 — approximating spaced recall within the
session.
```

***

## 2. Feynman Technique Partner

**Prompt:**
```
I will explain [CONCEPT] to you as if you were a [e.g., curious 12-year-old /
first-year student]. My explanation: [PASTE YOUR EXPLANATION].
1. Point out where my explanation becomes vague, circular, or jargon-hiding.
2. Ask me the 3 questions a smart 12-year-old would ask that expose gaps.
3. Do NOT rewrite my explanation — tell me what to fix and let me try again.
4. After my second attempt, rate the explanation: complete / mostly there /
   still glossing over something — and name the something.
```

- **Purpose:** Finding what you only think you understand.
- **Why it works:** The refusal to rewrite keeps you doing the synthesizing; the gap-probing questions target the illusion of explanatory depth.
- **Use Case:** True mastery checks before exams; thesis defense prep.

**Limitations & verification:** The model cannot verify factual accuracy of your explanation from nothing — have your course materials open, and ask it to flag claims that need checking against your textbook.

***

## 3. Interleaved Practice Generator

**Prompt:**
```
I am studying for [EXAM] covering these topics: [LIST TOPICS with rough
difficulty]. Generate an interleaved practice set:
1. 15 problems mixing the topics in a scrambled order — not blocked by topic
   (mixing forces me to identify which method applies, which is the exam skill).
2. For each problem, label the topic AFTER an answer-check prompt, not before.
3. Include 2 problems that combine two topics — these are where understanding
   shows.
4. Answers in a separate section at the end, with the method named, not just
   the number.
```

- **Purpose:** Practice that trains problem-identification, not just problem-execution.
- **Why it works:** Blocked practice (10 problems of the same type) creates false confidence; interleaving matches exam conditions where you must first recognize which tool applies.
- **Use Case:** Math, statistics, physics, any methods course.
- **Expert Variation:**
```
Weight the set toward my weak topics: here is my self-assessment per topic
[LIST with confidence 1-5] — generate proportionally more problems where I am
weak, but keep the interleaving.
```

**Limitations & verification:** AI-generated practice problems can contain errors — verify answers against your course materials, and treat any problem whose answer disagrees with your textbook as a practice problem in error-spotting.

***

## 4. Spaced Review Scheduler

**Prompt:**
```
I just finished learning [TOPIC] today. My exam is in [WEEKS] weeks. I also
need to maintain [OTHER TOPICS].
1. Build a spaced review schedule: reviews at expanding intervals (e.g., day 1,
   day 3, day 7, day 14...), adjusted to the exam date.
2. Each review session: specify what to do — not "review notes" but "retrieval
   attempt: write everything you remember about X from memory, then check."
3. Keep total daily review time under [MINUTES] by prioritizing what decays
   fastest.
4. Output as a copyable weekly plan with checkboxes.
```

- **Purpose:** Fighting the forgetting curve with scheduling instead of willpower.
- **Why it works:** Forgetting-curve spacing (expanding intervals) is one of the most replicated findings in learning science.
- **Use Case:** Semester-long retention, cumulative finals, language learning.

**Limitations & verification:** Adjust the schedule to reality — a missed review is rescheduled, not skipped; the expanding-interval pattern matters more than exact dates.

***

## 5. Elaborative Interrogation Drill

**Prompt:**
```
I am studying: [FACT/CONCEPT]. Turn my passive reading into elaborative
interrogation:
1. Ask me "why is this true?" and "why does this happen?" for the key claims —
   one at a time, waiting for my answer each time.
2. Push back once on each of my answers with "but what about [edge case /
   counterexample / simpler system]?" — gently, like a curious friend.
3. Connect each answer to something I likely already know from [MY FIELD/
   EVERYDAY LIFE] — but ask me to make the connection first.
```

- **Purpose:** Building the explanatory connections that make knowledge stick and transfer.
- **Why it works:** Elaborative interrogation (systematic "why" questioning) reliably outperforms re-reading in learning research.
- **Use Case:** Heavy conceptual courses — biology, psychology, economics, history.

***

## 6. The Pre-Study Priming Pass

**Prompt:**
```
Tomorrow's lecture covers [TOPIC]. Give me a 10-minute priming session tonight:
1. The 5 core questions this topic will answer — phrased so that the lecture
   will feel like receiving answers rather than hearing information for the
   first time.
2. A skeleton outline with the key terms left BLANK — I fill them in during
   the lecture.
3. One surprising fact or controversy in the area (label it clearly if you are
   not certain it is accurate — I will verify against the lecture).
4. What I should already know going in: the 3 prerequisite concepts, phrased
   as self-test questions.
```

- **Purpose:** Arriving at lectures with hooks to hang new knowledge on.
- **Why it works:** Pre-questions create a testing effect even before instruction, and prior exposure reduces the cognitive load of first contact.
- **Use Case:** Dense lecture courses, entering unfamiliar subfields.

**Limitations & verification:** The priming outline is a scaffold, not a source — where it conflicts with your lecturer or textbook, the course materials win, and the discrepancy is itself worth noting.

***

## Study Technique Quick Reference

| Technique | The prompt above | Why it works |
| :-- | :-- | :-- |
| Active recall | Reverse Tutor, Priming Pass | Retrieval strengthens memory more than review |
| Spaced repetition | Review Scheduler | Expanding intervals counter the forgetting curve |
| Interleaving | Practice Generator | Mixing topics trains method-selection |
| Elaboration | Interrogation Drill | "Why" questions build transferable understanding |
| Self-explanation | Feynman Partner | Gaps in explanations reveal gaps in knowledge |

**The golden rule for all of them:** the moment AI starts doing the thinking instead of prompting yours, it has stopped being a study tool and started being a crutch — every prompt above is built to prevent exactly that.
