# Literature Review & Synthesis Prompts

Companion prompts to the main researchers guide for the core scholarly skill: turning a pile of verified papers into an honest map of what is known, contested, and missing. All synthesis prompts assume you supply full texts or abstracts — synthesizing from model memory reproduces its training data's biases plus fabrication risk.

***

## 1. Evidence Matrix Construction

**Prompt:**
```
Build an evidence matrix from these papers I have read: [paste abstracts or your
structured notes per paper]. Question of interest: [REVIEW QUESTION].
1. For each paper: design type, sample/setting, key finding, and the specific
   claim it supports — restricted to what the provided text states.
2. Group the papers by the claim they inform, not by topic similarity.
3. Mark convergent findings (multiple independent papers agree) versus single-
   source findings (one paper only) — count matters for confidence.
4. Flag contradictions: where two papers' findings conflict, note the most
   likely methodological reason (population, measure, era) if the texts allow.
```

- **Purpose:** The foundation artifact of any honest review — evidence organized by claim, not by author.
- **Why it works:** Convergence counting forces the review to distinguish established findings from interesting single results.
- **Use Case:** Narrative reviews, thesis chapters, grant background sections.
- **Expert Variation:**
```
Add a confidence column per claim: high (3+ independent, consistent), moderate
(2 or consistent-but-similar methods), low (single study) — and state what new
evidence would upgrade each.
```

***

## 2. The Gap Finder

**Prompt:**
```
Based on this evidence matrix / these paper notes: [paste], and my knowledge of
the field's practical challenges: [describe], identify research gaps:
1. Population gaps: who/what has not been studied?
2. Methodological gaps: what designs or measures have not been applied — and
   why they might matter here?
3. Contradiction gaps: where findings conflict and no study has resolved why?
4. Temporal gaps: where might older findings have aged badly (measurement
   technology, context changes)?
5. For each gap: the strongest objection to it being a "real" gap (e.g., the
   research exists but in another discipline's literature — name where I should
   look before claiming the gap).
```

- **Purpose:** Gap statements that survive the reviewer who knows the adjacent literature.
- **Why it works:** The objection requirement prevents the most embarrassing review outcome: claiming a gap that a neighboring field filled years ago.
- **Use Case:** Introduction sections, grant proposals, thesis proposals.
- **Expert Variation:**
```
For the strongest gap, draft the one-paragraph justification in the format:
despite X (established), Y remains unknown (gap), because Z (methodological or
practical barrier), which matters because W (consequence).
```

***

## 3. Synthesis Paragraph Drafting (From Verified Sources Only)

**Prompt:**
```
Draft a synthesis paragraph from these verified source notes: [paste your notes
with citations]. Rules:
1. Every factual statement carries an inline citation drawn ONLY from the
   provided notes — no added references, no "studies show" without a named
   source.
2. Lead with the convergent finding, then qualifications, then the open
   question.
3. Distinguish explicitly: "consistently found" (3+ sources) vs "has been
   reported" (1-2 sources) vs "one group reported" (single team).
4. Where sources conflict, present the conflict rather than averaging it away.
5. Mark any sentence where you were tempted to generalize beyond the notes with
   [CHECK SCOPE].
```

- **Purpose:** Synthesis prose whose confidence calibration matches the underlying evidence.
- **Why it works:** The three-level hedging vocabulary ("consistently found" / "has been reported" / "one group") encodes evidence strength into the writing itself.
- **Use Case:** Related-work sections, review articles, evidence summaries for practice.
- **Expert Variation:**
```
Produce the 3-sentence version for an abstract or proposal — preserving the
calibration, compressed to the essentials.
```

**Limitations & verification:** Every citation in the output must be checked against your notes and then against the actual papers — the model may attach the right-sounding citation to the wrong claim.

***

## 4. Contradiction Analysis

**Prompt:**
```
These papers report conflicting results: [paste the conflicting findings with
methods sections or your notes on methods].
Analyze the conflict systematically:
1. Reconciling explanations, ranked: population differences, measurement
   differences, design differences (confounds controlled), era/context
   differences, publication biases, or genuine heterogeneity of effect.
2. For each explanation: what evidence in the provided texts supports it, and
   what study would test it directly?
3. Which explanation is most testable with a reasonable next study?
4. Draft the 4-sentence version of this analysis for my discussion section —
   presenting the conflict as informative, not embarrassing.
```

- **Purpose:** Treating contradictions as data about the field, not noise to hide.
- **Why it works:** The ranked-reconciling-explanations structure mirrors how mature fields digest disagreement.
- **Use Case:** Discussion sections, review articles, rebuttal letters.

***

## 5. Escaping the Echo Chamber (Coverage Audit)

**Prompt:**
```
Here is my current source list: [paste]. Audit its coverage as a skeptical
reviewer would:
1. Concentration risks: single labs, single country, single method, single
   dataset, single era? Name what is missing.
2. Disciplinary silos: which adjacent fields likely study this question under
   different vocabulary? Suggest the search terms EACH field would use.
3. Publication-flow blind spots: where would null results and replication
   attempts live, and am I citing any?
4. Author-balance check: whose citations would a critical reader say I
   over-rely on?
5. Output: the coverage-gap search plan — 5 specific searches I should run
   before I call this review complete.
```

- **Purpose:** Reviews that reflect the literature, not the first twenty results.
- **Why it works:** Names the four structural biases (lab, geography, method, era) that reviewers probe and literature searches systematically encode.
- **Use Case:** Pre-submission, systematic review calibration, grant defense prep.
- **Expert Variation:**
```
Add the citation-justice angle: whose relevant work might be under-cited due to
venue prestige or language bias — and how to search for it honestly
(non-English databases, regional journals, conference tracks).
```

***

## 6. Reading Queue Triage

**Prompt:**
```
I have [N] papers collected for my review: [paste titles + one-line notes].
My review question: [QUESTION]. Time available: [HOURS].
1. Triage into: core (full-text read), context (abstract + skim), and
   citation-only (for a specific claim I already know it supports).
2. Justify each core assignment in one line tied to my question.
3. Sequence the core reads: which first, so each read builds context for the
   next?
4. The exit test: after reading [the core set], what should I be able to say
   that I cannot say now?
```

- **Purpose:** Reading strategically under real time constraints.
- **Why it works:** The exit test converts a reading pile into a defined capability, making "enough" measurable.
- **Use Case:** Literature review kickoff, exam preparation, entering a new subfield.

**Limitations & verification:** Triage is only as good as your one-line notes — the model has not read the papers. Re-classify anything whose abstract surprises you when you open it.

***

## Shared Verification Rules for All Literature Prompts

1. **Supply the texts, always.** Synthesis from model memory is fabrication with academic formatting. Paste abstracts, your notes, or full text.
2. **Check every inline citation** the output produces against your notes and then the source — plausible mismatches are the signature failure.
3. **Count your evidence.** Convergent, single-source, and conflicting claims deserve different prose; the matrix makes those counts visible.
4. **Log your searches.** The databases, strings, and dates you used belong in your review's methods — and are your defense against "did you miss..." reviewer questions.
