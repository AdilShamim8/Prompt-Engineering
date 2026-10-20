# Data Leakage Prevention & Validation Prompts

Companion prompts to the main DS/ML guide. Data leakage — information from outside the training window contaminating your validation — is the most common cause of models that look great in notebooks and fail in production. These prompts build leakage checks into every stage of the workflow.

***

## 1. Pre-Modeling Leakage Audit

**Prompt:**
```
Act as a senior ML reviewer. I am building a [MODEL TYPE] to predict [TARGET] from
these features: [LIST]. Data setup: [how data is split, time range, any aggregation].
Before I train anything, audit my setup for leakage:
1. Which features may encode information unavailable at prediction time?
2. Are any features derived from the target or computed using future data?
3. Is the train/test split method appropriate for the temporal structure?
4. Should I use time-based splits instead of random splits? Why?
Do not write modeling code yet — audit only.
```

- **Purpose:** Catching leakage before it produces an untrustworthy model.
- **Why it works:** The explicit "audit only, no code" constraint forces a review rather than a solution jump.
- **Use Case:** Starting any supervised learning project.
- **Expert Variation:**
```
For each feature I listed, classify it as: safe / suspect / leaky-by-construction,
and for each "suspect" feature, describe the test I would run to decide.
```

***

## 2. Target Leakage Interrogation

**Prompt:**
```
Here is my feature engineering code: [paste code]. The target is [DEFINE TARGET].
Interrogate every feature it creates:
1. Could this feature be computed at prediction time in production? If not, it leaks.
2. Does this feature statistically correlate with the target because of how the data
   was collected (selection bias, survivorship, post-outcome recording)?
3. Are any aggregates (means, counts, ranks) computed over the full dataset rather
   than the training fold only?
Output: table of Feature | Verdict (safe/leaks/needs-test) | Reasoning.
```

- **Purpose:** Systematically checking derived features, the most common leakage vector in practice.
- **Why it works:** The table format forces a per-feature verdict instead of a vague "looks fine."
- **Use Case:** Reviewing feature pipelines before and after changes.

**Limitations & verification:** The model reasons from the code you paste. Verify its verdicts by timing: for each feature, ask "in production, when would this value become available?" — if the answer is "after the prediction," it leaks regardless of what the review said.

***

## 3. Correct Cross-Validation for Time Series

**Prompt:**
```
I am evaluating a model on time-series data spanning [RANGE] with [FREQUENCY] samples.
My current setup: [describe CV strategy]. Target: [TYPE].
1. Explain why my current strategy can over- or under-estimate performance, in plain language.
2. Recommend a validation scheme appropriate to the temporal structure
   (walk-forward, expanding window, or blocked splits) and state when each is preferable.
3. Generate the scikit-learn compatible code for your recommended scheme.
4. List the two ways people most often implement this incorrectly.
```

- **Purpose:** Avoiding the random-split trap that silently invalidates time-series evaluation.
- **Why it works:** Asking for failure modes alongside the code inoculates against copy-paste misuse.
- **Use Case:** Forecasting, churn, fraud, any temporally ordered outcome.
- **Expert Variation:**
```
Add a purge gap between train and validation periods to exclude overlapping-label
contamination, and explain how the gap size should relate to my label horizon.
```

**Limitations & verification:** Run the generated code on data where you know the answer — e.g., verify that no validation timestamp precedes the latest training timestamp.

***

## 4. Pipeline Integrity Check (Fit on Train Only)

**Prompt:**
```
Review this scikit-learn pipeline for data leakage through preprocessing: [paste code].
Check specifically:
1. Are scalers, encoders, imputers, feature selectors fit inside the pipeline
   (fit on train folds only) rather than on the full dataset before splitting?
2. Do any custom transformers leak information across folds?
3. Is the target encoding (if used) properly cross-fitted?
4. Is the same row ever processed differently in train versus validation?
Output: a verdict per check with the offending lines quoted, then corrected code.
```

- **Purpose:** Catching the subtle leakage where preprocessing silently sees test data.
- **Why it works:** Scoping to the four canonical preprocessing leak paths makes the review exhaustive rather than impressionistic.
- **Use Case:** Any pipeline with scaling, encoding, imputation, or feature selection.
- **Expert Variation:**
```
Rewrite my pipeline so that leakage is structurally impossible (all learning inside
Pipeline/ColumnTransformer), and add an assertion-based test that fails if any
transformer is fit on the full dataset.
```

***

## 5. Suspiciously Good Results Review

**Prompt:**
```
My model achieves [METRIC = VALUE] on [TASK]. This is [BETTER/SUSPICIOUSLY BETTER]
than [BASELINE/PRIOR RESULTS/INDUSTRY NORM]. Act as a skeptical reviewer and give me
a ranked leakage-and-cheating checklist:
1. The 5 most likely explanations for performance this good, ordered by prior probability
2. For each: the specific test that would confirm or rule it out
3. Which explanation I should eliminate FIRST before celebrating
Context: [data description, split method, feature sources].
```

- **Purpose:** Institutionalized suspicion when results exceed expectations.
- **Why it works:** Models that "beat expectations" are usually broken in an interesting way; this prompt assumes that upfront.
- **Use Case:** Any surprisingly strong benchmark result.
- **Expert Variation:**
```
Design the simplest possible experiment whose result would prove my model is NOT
cheating (e.g., a feature-ablation run, a temporal holdout from a later period,
or a deployment shadow test).
```

**Limitations & verification:** The definitive test is always out-of-time or out-of-sample evaluation the model has never touched. Treat the checklist as your route to that test, not a substitute for it.

***

## 6. Production Drift vs. Leakage Differential Diagnosis

**Prompt:**
```
Model performance: [TRAIN/VALID METRICS] offline, [PRODUCTION METRIC] live.
Gap appeared [WHEN/GRADUALLY/SUDDENLY]. Production data available: [describe].
Help me differentiate between two diagnoses:
A) Offline evaluation was inflated by leakage (the model was never that good)
B) The model is fine but the world changed (drift or breakage)
1. What evidence distinguishes A from B? List the checks in order of cost.
2. Which artifacts would I need to re-run the original evaluation honestly?
3. If it is drift: which type (covariate, concept, or label shift) and how to test?
```

- **Purpose:** The post-incident differential that most teams get wrong under pressure.
- **Why it works:** Frames the two hypotheses as competing diagnoses with distinguishing evidence, like a medical workup.
- **Use Case:** Production monitoring, model governance reviews.

**Limitations & verification:** Requires artifacts you should already be keeping (see the Experiment Design & Reproducibility prompts). If you cannot re-run the original evaluation, that absence is itself a finding.

***

## Shared Verification Rules for All Leakage Prompts

1. **Never trust a validation score you have not tried to break.** The prompts above exist because leakage is invisible from inside the notebook — someone (you) must actively attack the result.
2. **Test generated code on known-answer data.** Before using any validation code, run it on a small dataset where you know exactly which rows should be in train and validation.
3. **Timing is the ground truth for leakage.** Every feature and every split decision reduces to: "what would I have known at prediction time?" No statistical test substitutes for that question.
4. **Keep the honest evaluation immutable.** Once you build a leak-free out-of-time holdout, freeze it: it is the one number that cannot lie to you, and reusing it for tuning slowly poisons it too.
