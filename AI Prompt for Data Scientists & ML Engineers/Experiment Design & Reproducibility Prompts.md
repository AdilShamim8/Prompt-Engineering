# Experiment Design & Reproducibility Prompts

Companion prompts to the main DS/ML guide for running experiments you can trust and that others can replay. The theme: decide before you look, record before you move on, and freeze everything a future auditor (including you) would need.

***

## 1. Pre-Registration for ML Experiments

**Prompt:**
```
Act as an experiment reviewer. I am about to run: [DESCRIBE CHANGE — new features,
new model, hyperparameter search, threshold change]. Baseline: [current setup and
its metrics on the same validation].
Draft my pre-registration:
1. The single hypothesis, stated so it can fail
2. The primary metric and the exact evaluation protocol (splits, seeds, folds)
3. The success criterion, fixed BEFORE results — including the minimum improvement
   that counts as meaningful in my context
4. The secondary metrics I will look at but not decide on
5. What I commit to reporting even if the result is negative
```

- **Purpose:** Pre-committing to success criteria so results cannot be nudged into significance afterward.
- **Why it works:** Pre-registration is the single cheapest defense against self-deception in iterative ML work.
- **Use Case:** Model improvements, A/B-infra changes, feature engineering campaigns.
- **Expert Variation:**
```
Add the "what would change my mind" section: the two outcomes that would make me
abandon this direction entirely, written now while I am still objective.
```

***

## 2. Seed & Environment Control Audit

**Prompt:**
```
I need my experiment to be re-runnable in 6 months. Current setup: [describe
libraries, hardware if known, any GPU use, how randomness enters].
1. List every source of nondeterminism in my setup (seeds, thread scheduling,
   library versions, GPU ops, data ordering).
2. For each: whether it matters for my conclusion, and how to pin it.
3. Generate the reproducibility boilerplate: fixed seeds for random/numpy/torch,
   deterministic algorithms where applicable, environment capture (requirements
   freeze), and a run-manifest (git commit, data version, config) printed at start.
4. State honestly what CANNOT be made deterministic in my setup, and how much
   run-to-run variance that introduces.
```

- **Purpose:** Making "I'll document it later" unnecessary by generating the discipline upfront.
- **Why it works:** Enumerates nondeterminism sources systematically instead of discovering them during a failed replication.
- **Use Case:** Any experiment whose result will be cited, reused, or audited.
- **Expert Variation:**
```
Add a re-run verification protocol: run twice, and define the metric variance I
should expect between identical runs — so future-me can tell a real change from
noise instantly.
```

**Limitations & verification:** Deterministic flags can slow training and some operations cannot be pinned on GPU hardware — the honest variance estimate matters more than false determinism. Test the boilerplate by actually re-running.

***

## 3. Sample Size & Power Sanity Check

**Prompt:**
```
I want to detect an improvement from [BASELINE METRIC] to [TARGET METRIC].
Data: [describe volume, class balance if relevant, clustering — e.g., multiple
rows per user].
1. Estimate the sample needed to detect this effect with reasonable confidence —
   show the reasoning and the formula used.
2. What if my rows are not independent (clustered by user/session)? How does that
   change the effective sample size?
3. If I cannot get that sample: what effect size COULD I detect with what I have?
4. What is the risk of running anyway and over-interpreting a noisy win?
```

- **Purpose:** Knowing before the experiment whether it can possibly answer the question.
- **Why it works:** The "what could I detect instead" question turns an underpowered design into an informed scope decision.
- **Use Case:** Test-set sizing, online experiments, any before/after comparison.
- **Expert Variation:**
```
Design the sequential testing plan if I must peek at results before full collection:
what boundaries keep false-positive rates honest, and when to stop early.
```

**Limitations & verification:** Power calculations from a model are approximations — recompute with a proper stats library or power calculator, and treat clustered-data corrections as mandatory, not optional.

***

## 4. The Experiment Log Entry

**Prompt:**
```
Draft the log entry for my completed experiment. I will give you: [hypothesis,
what I actually ran, results including negative ones, what I concluded].
Format the entry:
1. Original hypothesis (in pre-registered words, not retrospective words)
2. What actually happened — deviations from plan, honestly
3. Result: primary metric with uncertainty, and whether the pre-registered
   criterion was met
4. What I now believe, and with what confidence
5. The follow-up experiment this suggests, if any
6. Links/artifacts: code commit, data version, config, raw metrics file
Do not polish the narrative — accuracy over story.
```

- **Purpose:** An experiment record whose value compounds, written while memory is fresh.
- **Why it works:** The "no retrospective words" rule kills the narrative drift that makes old logs useless.
- **Use Case:** Team experiment registries, thesis work, production model governance.
- **Expert Variation:**
```
Add a one-line index entry for a summary table: [date | hypothesis | result |
decision] — and remind me to update the table, not just the entry.
```

***

## 5. Multi-Run Variance Discipline

**Prompt:**
```
I am comparing model A vs B. My evaluation involves [CV folds / random inits /
bootstrap samples]. Currently I run [N] repeats and compare means.
1. Explain why my comparison may be noise, with reference to my setup's variance
   sources.
2. Recommend: how many repeats, and whether a paired design (same folds/seeds for
   A and B) applies here.
3. Generate code for a paired comparison with an uncertainty estimate on the
   A-minus-B difference, not just on each model's score.
4. Tell me the smallest A-over-B gap my setup can actually resolve.
```

- **Purpose:** Comparing models with uncertainty on the difference, not theatre around two point estimates.
- **Why it works:** Paired designs and difference-level uncertainty are the correct tools most comparisons skip.
- **Use Case:** Model selection, library/version upgrades, hyperparameter finals.
- **Expert Variation:**
```
Add the decision rule: given the uncertainty on the difference, when should I
prefer the SIMPLER model even when it slightly loses — and quantify "slightly"
for my context.
```

***

## 6. Artifact Freezing Checklist

**Prompt:**
```
Generate the artifact-freezing checklist for my project: [describe project,
data sources, models, environment]. Include:
1. Everything needed to re-create the training data from raw sources
2. Everything needed to re-run training exactly (code, config, environment, seeds)
3. Everything needed to re-run evaluation (splits, metrics code, thresholds)
4. Everything needed to serve the model (serialized artifact, preprocessing,
   version contract)
5. A directory structure that makes all of the above findable in 12 months
Output as a copyable checklist with [ ] boxes and a "stored where" column.
```

- **Purpose:** The boring discipline that separates replayable research from archaeology.
- **Why it works:** Enumerates the four artifact classes (data, training, evaluation, serving) that get lost in different ways.
- **Use Case:** Project completion, role handoffs, publication preparation.

**Limitations & verification:** A checklist freezes what you remember to list — walk through an actual cold-start re-run of one old experiment; whatever you reach for and cannot find belongs on the list.

***

## Shared Verification Rules for All Experiment Prompts

1. **Pre-register, then respect it.** The value dies the moment success criteria move after seeing results. If scope changes, register the change with a reason.
2. **Re-run generated code before trusting it.** Statistical code especially: verify on a case with a known answer before applying to your experiment.
3. **Negative results are results.** Log them with the same care — the experiment registry that only records wins is a fiction machine.
4. **Your future auditor is you.** Freeze artifacts and write entries for the version of yourself who remembers nothing; that person runs every serious post-mortem.
