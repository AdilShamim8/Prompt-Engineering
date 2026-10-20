# Model Evaluation & Interpretation Prompts

Companion prompts to the main DS/ML guide for evaluating models honestly and interpreting them usefully — metric choice, error analysis, slice performance, and explaining models to non-experts without overclaiming.

***

## 1. Metric Selection by Decision Cost

**Prompt:**
```
Act as an ML advisor. Model use case: [DESCRIBE]. Decision it drives: [WHO DECIDES
WHAT based on the output]. Error costs: [describe what a false positive versus a
false negative costs in this domain].
1. Rank the 3 most appropriate evaluation metrics for this decision, with the
   reasoning tied to the error costs I described.
2. State what each candidate metric hides.
3. Recommend ONE primary metric and 2 guardrail metrics, and the thresholds that
   would make the model unusable regardless of the primary metric.
```

- **Purpose:** Choosing metrics because they match the decision, not because they are default.
- **Why it works:** Anchoring to false-positive/false-negative costs converts metric choice from taste to reasoning.
- **Use Case:** New model projects, stakeholder alignment on "what good means."
- **Expert Variation:**
```
Translate the recommended thresholds into expected business outcomes per month
(escapes, false alarms, review hours) at current volumes, showing the arithmetic.
```

***

## 2. Beyond the Average: Slice Analysis Design

**Prompt:**
```
My model scores [OVERALL METRIC]. Data: [describe population and available
dimensions]. Design a slice analysis:
1. Which 6-8 slices should I evaluate, and why these (impact x likelihood of
   differential performance)?
2. Which slices am I tempted to evaluate that would be misleading (too small,
   overlapping, or proxy-collinear)?
3. What disparity between best and worst slice should trigger action in my context?
4. Generate the pandas code to compute per-slice metrics with confidence intervals,
   including a minimum-sample-size guard.
```

- **Purpose:** Finding the populations your average silently fails.
- **Why it works:** The "slices to avoid" question is the one most analyses skip, and the reason most slice analyses mislead.
- **Use Case:** Pre-launch review, fairness assessment, quality dashboards.
- **Expert Variation:**
```
Add intersectional slices (e.g., segment x volume band) with a multiple-comparisons
caution: which disparities survive a correction for testing many slices at once?
```

**Limitations & verification:** Statistical significance in small slices is treacherous — respect the minimum-sample guard, and re-run the generated code before trusting any number it prints.

***

## 3. Error Autopsy

**Prompt:**
```
Here are my model's worst errors: [paste 20-50 example rows with predictions,
actuals, and available context]. Conduct an error autopsy:
1. Group the errors into patterns (data quality, genuinely hard cases, labeling
   mistakes, distribution edge, model blind spot).
2. For each group: estimated share of errors, and whether fixing it requires
   data work, labeling work, or modeling work.
3. Which single pattern, if fixed, removes the most errors?
4. Which errors might actually be correct-but-mislabeled? List suspects.
```

- **Purpose:** Converting "the model is 87% accurate" into an actionable defect list.
- **Why it works:** Grouping by cause rather than severity points directly at the cheapest fix.
- **Use Case:** Model debugging, iteration planning, labeling pipeline improvements.
- **Expert Variation:**
```
For each error group, design the minimal dataset addition (n rows, from where,
labeled how) that would most improve this failure mode, and the experiment to
verify the improvement is real.
```

***

## 4. Calibration & Threshold Sanity

**Prompt:**
```
My classifier outputs probabilities. Use case: [DESCRIBE]. Volume: [N predictions
per period]. I plan to act when P > [THRESHOLD].
1. Explain what miscalibration would do to my operation at this threshold —
   concretely, in terms of over/under-triggering.
2. Recommend how to assess calibration with my data (reliability curves, Brier
   score — and what each would show).
3. If miscalibrated, compare the correction options (Platt, isotonic,
   threshold-tuning) and when each is appropriate.
4. Generate code for a reliability diagram with proper binning for [CLASS BALANCE].
```

- **Purpose:** Making probability outputs mean what users assume they mean.
- **Why it works:** Links calibration (abstract) to operational consequences (concrete) at the user's actual threshold.
- **Use Case:** Any system where a probability triggers a workflow.
- **Expert Variation:**
```
Show how my expected costs change across 5 candidate thresholds, using my error
costs and class balance, and identify the cost-optimal threshold — with the
uncertainty around that optimum.
```

***

## 5. Feature Importance — Carefully

**Prompt:**
```
I want to explain my model to stakeholders. Model: [TYPE]. Features: [LIST]. I have
computed [SHAPE/permutation/coefficients — describe what you have].
1. Explain what my importance measure actually measures — and what it does NOT
   (causality, in particular).
2. Which features' importance is likely inflated by correlation with other features?
3. Draft the stakeholder explanation: 5 bullet points, plain language, that conveys
   "these associations drive predictions" without implying causation.
4. List the 3 questions stakeholders will ask (e.g., "so if we increase X...") and
   the honest answer to each.
```

- **Purpose:** Interpretation that informs without deceiving.
- **Why it works:** Pre-empts the causal misreading that every feature-importance chart invites.
- **Use Case:** Model governance, executive reviews, customer-facing explanations.
- **Expert Variation:**
```
Design one validation experiment per top-3 feature that could distinguish
"the model uses this feature" from "changing this feature changes the outcome."
```

**Limitations & verification:** No prompt makes importance causal. If decisions will change real-world feature values (pricing, treatment, resource allocation), the only honest path is an experiment — say so in the stakeholder meeting.

***

## 6. Model Card Drafting

**Prompt:**
```
Draft a model card for my model. Facts I can supply: [intended use, training data
summary, evaluation setup and metrics, known limitations, slice performance if
available].
Structure:
1. Intended use AND out-of-scope uses — named explicitly
2. Evaluation data versus training data: what differs
3. Metrics overall AND per slice
4. Known failure modes and their operational warning signs
5. Human oversight requirements in deployment
Where I have not supplied a fact, write [TO VERIFY] rather than filling it in.
```

- **Purpose:** The documentation artifact that makes future audits, handoffs, and incident reviews possible.
- **Why it works:** The "[TO VERIFY] rather than inventing" rule prevents the model card from becoming confident fiction.
- **Use Case:** Production launches, regulated contexts, team handoffs.
- **Expert Variation:**
```
Add a "decommission triggers" section: the measurable conditions under which this
model should be pulled or retrained, and who owns that decision.
```

***

## Shared Verification Rules for All Evaluation Prompts

1. **Never report a number you have not recomputed.** Generated analysis code must be executed and its outputs spot-checked against a manual calculation on a small sample.
2. **Averages conceal; slices reveal.** Any headline metric shipped without a slice breakdown is a hypothesis, not an evaluation.
3. **Interpretation is not causation.** Every explanation of "why the model decided" must survive the question "and what experiment would confirm that?"
4. **Evaluation sets are consumables.** Every model-selection decision made against a test set spends a little of its honesty; budget accordingly and keep a final, untouched holdout.
