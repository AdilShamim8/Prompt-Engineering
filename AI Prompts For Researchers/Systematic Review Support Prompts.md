# Systematic Review Support Prompts

Companion prompts to the main researchers guide for the systematic and scoping review workflow: protocol drafting, screening, PRISMA documentation, and the quality assessment passes. These prompts accelerate the mechanical layers so human judgment concentrates where it belongs — on inclusion decisions and synthesis.

***

## 1. Protocol Skeleton (PRISMA-Aligned)

**Prompt:**
```
Draft a systematic review protocol skeleton for: [QUESTION]. Field: [FIELD].
Structure it with these sections, and prompt me with the questions I must answer
in each:
1. Background & rationale (2-3 sentences scope)
2. Eligibility criteria: PICOS — population, intervention/exposure, comparator,
   outcomes, study designs — plus explicit EXCLUSIONS with reasons
3. Information sources: which databases, registers, and gray-literature routes,
   with date ranges
4. Search strategy: the concept blocks and one full example query
5. Selection process: who screens what, how disagreements resolve
6. Data extraction: the fields I will pull from each included study
7. Risk-of-bias assessment: which tool, applied by whom, at what stage
8. Synthesis plan: what I will and will NOT attempt to pool, and why
Where I have not decided something, write [DECISION NEEDED] — do not invent
positions for me.
```

- **Purpose:** A protocol that makes every consequential decision explicit before screening begins.
- **Why it works:** The [DECISION NEEDED] discipline keeps the model from papering over the undecided parts that post-hoc bias exploits.
- **Use Case:** Review registration (PROSPERO-style), thesis review chapters.
- **Expert Variation:**
```
Add the amendment log section: how protocol changes get recorded, justified,
and reported — the difference between a deviation and a bias.
```

***

## 2. Screening Decision Support (Human-in-the-Loop)

**Prompt:**
```
I am screening records for eligibility. My criteria: [paste criteria].
Here is a batch of titles+abstracts: [paste batch].
For each record, output:
1. Include / Exclude / Full-text-needed — strictly per my criteria
2. The single criterion that drove the decision
3. The ambiguity flag: what information would change this call
Do not soften borderline cases toward inclusion. Borderline = full-text.
```

- **Purpose:** Accelerating first-pass screening while keeping every borderline case for human eyes.
- **Why it works:** One-criterion-per-decision creates an auditable rationale trail; "borderline = full-text" defaults toward recall.
- **Use Case:** Title/abstract screening at scale.
- **Expert Variation:**
```
Calibrate first: here are 10 records I already decided [with my decisions].
Check your decision rules against mine, tell me where you would have diverged,
and adjust before screening the next batch.
```

**Limitations & verification:** The screener of record is you — model recommendations are a second reader, not a co-author of the PRISMA flow. Log your verification sampling: periodically re-screen records yourself and measure agreement.

***

## 3. PRISMA Flow Accounting

**Prompt:**
```
My screening numbers: [databases searched with results, duplicates removed,
records screened, excluded at title/abstract, full-texts assessed, excluded at
full-text WITH reasons by category, included studies].
1. Generate the PRISMA flow narrative and check the arithmetic: do the numbers
   reconcile at every stage (identification → screening → eligibility →
   included)? Show each subtraction.
2. Flag any stage where my numbers look implausible (exclusion rates outside
   typical ranges for my review type).
3. Draft the flow-diagram text for each box in order.
4. List the exclusions-at-full-text by reason category, sorted by frequency —
   this becomes my "characteristics of excluded studies" appendix.
```

- **Purpose:** A flow diagram whose numbers actually add up — the first thing methodologists check.
- **Why it works:** The reconciliation pass catches the transcription and arithmetic errors that plague flow diagrams.
- **Use Case:** Manuscript preparation, review updates.
- **Expert Variation:**
```
Add the update plan: search dates, re-run triggers, and how new records merge
into this flow — so the review can be revived rather than redone.
```

***

## 4. Data Extraction Table Generation

**Prompt:**
```
Generate my data extraction template for these included studies: [paste study
list or describe designs]. Must capture:
1. Bibliographic fields
2. Design and methods: design type, sample and setting, exposure/intervention
   details, comparator, outcomes and their measurement timing
3. Results: effect estimates with precision (OR/RR/MD/SMD + CI) or qualitative
   finding statements — never bare p-values alone
4. Risk-of-bias: domain-level ratings from [TOOL NAME] with the supporting quote
5. Funding source and declared conflicts
6. Two free-text fields: "author-claimed limitations" and "reviewer-observed
   limitations" — keep them separate
Output as a table specification with one worked example row.
```

- **Purpose:** Extraction structured for synthesis and audit, not just description.
- **Why it works:** Separating author-claimed from reviewer-observed limitations preserves the critical voice extraction tables usually lose.
- **Use Case:** Extraction piloting, multi-reviewer standardization.
- **Expert Variation:**
```
Add the second-reviewer protocol: which fields get dual extraction, the target
agreement threshold, and the reconciliation procedure.
```

***

## 5. Risk-of-Bias Consistency Pass

**Prompt:**
```
Here are my risk-of-bias ratings for these studies: [paste ratings with
justification quotes per domain, using MY tool's domains].
1. Consistency check: flag ratings where the justification quote does not
   clearly support the rating assigned — either the quote or the rating needs
   to change.
2. Calibration check: flag studies whose overall pattern diverges from how I
   rated very similar designs (rating drift across the extraction timeline).
3. The skepticism check: where might I be under-rating bias in studies whose
   findings I like? Name them and why they are suspect.
4. Generate the traffic-light summary table for the appendix.
```

- **Purpose:** Bias ratings that mean the same thing on day 1 and day 30.
- **Why it works:** Drift and motivated skepticism are the two documented failure modes of long extraction campaigns — both are named and checked.
- **Use Case:** Quality assessment completion, sensitivity-analysis planning.
- **Expert Variation:**
```
Design the sensitivity analyses my ratings imply: which exclusion scenarios
(low-quality-only, high-loss-only) would test whether my conclusions depend
on weak studies?
```

**Limitations & verification:** The consistency pass reads your ratings and quotes — it cannot see the studies. Every flagged discrepancy gets resolved by returning to the source paper, not by adjusting the rating to match the quote.

***

## 6. Scoping Review Variant

**Prompt:**
```
I am doing a scoping review (not systematic): [QUESTION]. Purpose: map the
field's scope, not appraise its evidence quality.
1. Adjust the workflow: where does risk-of-bias assessment drop out, and what
   replaces it as the quality gate (reporting completeness, methodological
   transparency)?
2. Charting framework: the data charting fields that map volume, nature, and
   gaps — by concept, population, and method over time.
3. The gap-map output: structure the findings as a matrix of [CONCEPTS x
   POPULATIONS/SETTINGS] with study counts per cell — empty cells are findings.
4. Draft the limitations paragraph honest to scoping reviews: no quality
   appraisal, no pooled effects — what my map can and cannot claim.
```

- **Purpose:** Scoping reviews that claim scoping-sized conclusions.
- **Why it works:** The empty-cells-as-findings framing turns the review's inherent shallowness into its actual product.
- **Use Case:** Emerging fields, multi-disciplinary questions, thesis scoping chapters.

***

## Shared Verification Rules for All Systematic Review Prompts

1. **You are the screener of record.** Model support accelerates first passes, but inclusion decisions, bias ratings, and synthesis judgments belong to named humans — document who did what.
2. **Arithmetic is on you.** Every count, subtraction, and percentage in the PRISMA flow must be recomputed manually before submission.
3. **Log model assistance.** Note in your methods (or per venue policy) where AI support was used in screening and extraction — with your verification procedure.
4. **Calibrate, then trust — partially.** Periodic re-screening of model-recommended decisions by your own eyes is the ongoing price of speed.
