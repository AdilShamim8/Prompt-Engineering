# Statistical Rigor & Uncertainty Prompts

Companion prompts to the main DS/ML guide for keeping statistical claims honest: stating uncertainty, testing the right hypothesis, respecting assumptions, and resisting the most common inference traps in data work.

***

## 1. Assumption Check Before the Test

**Prompt:**
```
I plan to run [STATISTICAL TEST] on this data: [describe structure, sample sizes,
distributions if known].
1. List the assumptions this test makes about my data.
2. For each assumption: how to check it with my data, and what to do if it fails.
3. If the checks fail, what is the appropriate fallback (transformation,
   nonparametric alternative, or different design)?
4. What would make this test's p-value misleading even if all checks pass?
```

- **Purpose:** Matching the test to the data instead of to habit.
- **Why it works:** Assumption-first ordering prevents the run-then-rationalize pattern.
- **Use Case:** A/B analysis, survey inference, any formal comparison.
- **Expert Variation:**
```
For my specific data structure, rank the 3 candidate tests by robustness to my
likely violations, and state the practical difference in interpretation between
their results.
```

***

## 2. Uncertainty Statement Generator

**Prompt:**
```
I am reporting: [POINT ESTIMATE, e.g., "conversion is 4.2%"]. Sample: [N, design].
Generate the honest uncertainty statement:
1. The interval estimate with the method appropriate to my data (show the computation).
2. What the interval does and does NOT mean — in language my audience [TECHNICAL/
   EXECUTIVE] will not misread.
3. The sample size needed to halve the interval width, if it matters.
4. One sentence version for a slide, one footnote version for the appendix.
```

- **Purpose:** Point estimates without intervals are the most-circulated statistical sin in business data work.
- **Why it works:** Produces audience-calibrated phrasings, attacking misreading at the communication layer.
- **Use Case:** Dashboards, exec reporting, experiment readouts.
- **Expert Variation:**
```
Add the Bayesian framing: with a weakly-informed prior, what is my posterior
probability that the true value exceeds [DECISION-RELEVANT THRESHOLD]?
```

**Limitations & verification:** Interval methods assume your sampling design is what you claim. Clustered, time-correlated, or selection-biased data silently invalidates the computation — state the design honestly in the prompt.

***

## 3. The Multiple Comparisons Audit

**Prompt:**
```
This analysis: [describe how many metrics/slices/segments were examined, and
whether any selection happened after looking at results].
1. How many effective comparisons were made — including the implicit ones from
   slicing and metric variants?
2. What is the expected number of "significant" findings under pure noise at
   my alpha level?
3. Apply a correction (state which and why) and identify which findings survive.
4. Which "findings" in my list look most like survivorship of noise?
```

- **Purpose:** Counteracting the garden-of-forking-paths effect that inflates false discoveries.
- **Why it works:** The "expected significant findings under noise" calculation makes the multiple-comparisons problem visceral.
- **Use Case:** Dashboards with many tiles, slice analyses, metric landscapes.
- **Expert Variation:**
```
Design the confirmation plan: which surviving findings get a held-out validation
run, and what prior probability should I assign them given the selection process?
```

***

## 4. Correlation-to-Causation Guardrail

**Prompt:**
```
I found: [CORRELATION/ASSOCIATION, with strength and sample]. I am tempted to
conclude: [CAUSAL CLAIM].
1. Steelman the non-causal explanations: confounding (list plausible confounders),
   selection, reverse causation, coincidence at my sample size.
2. What observational evidence would narrow the gap between association and
   causation here (natural experiments, lagged effects, dose-response)?
3. What experiment would settle it, and its cheapest viable version?
4. Rewrite my claim at three honesty levels: what the data shows / what it
   suggests / what I wish it showed.
```

- **Purpose:** The discipline of separating what data shows from what we want it to mean.
- **Why it works:** The three-level rewrite gives stakeholders calibrated language instead of a binary accept/reject of the causal story.
- **Use Case:** Exploratory analyses, management requests for "the driver of X."
- **Expert Variation:**
```
For the most plausible confounder, estimate from available variables how strong it
would need to be to explain away my association entirely (sensitivity analysis
logic).
```

***

## 5. Missing Data Mechanism Assessment

**Prompt:**
```
My dataset has missingness: [which columns, what %, any pattern notes].
1. Help me reason about the mechanism: MCAR, MAR, or MNAR — what evidence in my
   data could distinguish these, and what typically remains unknowable?
2. For each plausible mechanism: the defensible handling strategy (and the
   indefensible ones, named).
3. How does each strategy bias the specific analysis I plan: [ANALYSIS]?
4. Generate a missingness-pattern exploration script (matrix of missingness by
   column pair, missingness versus observed values).
```

- **Purpose:** Treating missingness as information about the data-generating process, not a nuisance.
- **Why it works:** Ties the mechanism to the bias in YOUR analysis rather than generic advice.
- **Use Case:** Survey data, sensor data, clinical and operational datasets.
- **Expert Variation:**
```
Design a sensitivity analysis: run my analysis under (a) best-case and (b)
worst-case imputation of the missing values, and report how much my conclusion
moves — the range IS the finding when missingness is heavy.
```

**Limitations & verification:** MNAR is fundamentally unidentifiable from observed data — no prompt or method dissolves that; only domain reasoning and sensitivity ranges address it honestly.

***

## 6. Statistical Review of a Claimed Finding

**Prompt:**
```
Act as a hostile statistical reviewer. Here is a claimed finding: [paste summary
or abstract]. Data context: [design, N, how measured].
1. Attack the finding: the 3 strongest methodological objections.
2. Check the numbers for internal consistency — do the claims arithmetically
   fit the stated sample and effect?
3. What alternative analysis of the same data would test the same question?
4. What evidence would make you, the hostile reviewer, concede?
```

- **Purpose:** An adversarial pass before the finding meets a real skeptical audience.
- **Why it works:** The hostile-reviewer frame licenses the criticism that politeness suppresses.
- **Use Case:** Pre-submission review, internal decision memos, due diligence.
- **Expert Variation:**
```
Write the two-sentence verdict a careful statistician would actually put in a
review of this finding — the one I would not enjoy reading but need to.
```

***

## Shared Verification Rules for All Statistics Prompts

1. **Recompute everything.** Generated statistics code runs, but runs wrong more often than you fear — verify on known-answer examples before production use.
2. **Name the design before the test.** Most invalid statistics come from analyzing clustered or time-ordered data as if it were simple random sampling.
3. **Intervals are part of the estimate.** Any number you report without its uncertainty is a placeholder pretending to be a result.
4. **The mechanism of missingness and selection is a scientific claim** — treat it as something to argue with evidence, not to assume by convenience.
