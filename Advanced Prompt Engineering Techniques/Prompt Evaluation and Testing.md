# Prompt Evaluation and Testing

The evaluation discipline for prompts used seriously — in production systems, repeated workflows, or anything where quality matters more than novelty. The Beginners guide covers personal-scale testing (its Section 8); this guide covers the systematic version: test design, automated evaluation, regression pipelines, and the honest limits of each.

## Before You Start

**Learning objectives** — after this guide you can: place yourself on the five-level evaluation stack honestly; build a tiered test set with pass/fail, rubric, and judge layers; score with the benchmark trap in mind; and wire evaluation into prompt changes as a regression gate.

**Prerequisites** — [Structured Outputs](./Structured%20Outputs%20and%20Schema%20Prompting.md) (Tier 1 checks are schema validation) and Beginners guide §8. Curriculum position: [§3.10](../CURRICULUM.md#tier-d--trust-and-reliability); this discipline is what [Versioning](./Prompt%20Versioning%20and%20Maintenance.md) depends on.

## The Evaluation Stack

```
Level 0: Vibe check        — ran it once, looks fine (where everyone starts)
Level 1: Test set          — N saved inputs, scored consistently
Level 2: Regression suite  — re-run on every prompt change, compare
Level 3: Automated eval    — programmatic scoring with spot-checked judges
Level 4: Production monitor— live quality signals, drift alerts
```

Each level earns the next. Skip levels and you get confidence without evidence.

## Building the Test Set

The test set is 10-50 real inputs with known-good expected behavior:

```
Composition for a [CLASSIFICATION/EXTRACTION/GENERATION] prompt:
- 40% typical cases (the everyday shape)
- 20% edge cases (empty, huge, malformed, mixed-language)
- 20% hard/boundary cases (where past versions failed)
- 10% adversarial cases (injection attempts, trick questions)
- 10% out-of-scope cases (should trigger the refusal/fallback path)

For each, record:
  input / expected behavior (not always exact output) / why it's
  in the set (what failure it guards against)
```

"Expected behavior" beats "expected output" for generation tasks: exact-match goldens only work for classification and extraction; for prose, define the checklist the output must satisfy (contains X, excludes Y, format Z, length band).

## The Scoring Rubric (Machine-Checkable First)

Order checks from cheap-and-objective to expensive-and-judgment:

```
Tier 1 — Deterministic (free, instant):
  [ ] Output parses (JSON/schema validity)
  [ ] Required fields present
  [ ] Enum values within allowed set
  [ ] Length/format constraints met
  [ ] Forbidden content absent (banned phrases, PII patterns)

Tier 2 — Reference checks (cheap with goldens):
  [ ] Classification matches expected label
  [ ] Extraction matches expected values (with tolerance)
  [ ] Contains required factual elements

Tier 3 — Judgment (expensive, needs care):
  [ ] Correctness of reasoning/conclusions
  [ ] Completeness and relevance
  [ ] Tone/quality fit
  [ ] Hallucination check (claims traceable to provided source)
```

Automate Tiers 1-2 fully. Tier 3 gets human review or an LLM judge — with the judge caveats below.

## LLM-as-Judge: Use With Eyes Open

Automated judges make evaluation scale; they also import failure modes:

- **Verbosity bias**: judges favor longer answers
- **Self-preference**: models grade their own outputs more favorably
- **Position bias**: first-presented option wins more often
- **Rubric blindness**: judges miss subtle factual errors while nailing structure

Countermeasures that work:

1. **Judge with a checklist, not a vibe** — "Score 1-5: does the output cite a source for every factual claim? List each uncited claim" outperforms "is this a good answer, 1-10?"
2. **Calibrate against humans** — have humans score 20 outputs; measure judge-human agreement; trust the judge only where agreement is high
3. **Swap positions** for comparative judging; randomize order
4. **Use a different model than the one being evaluated** where feasible
5. **Audit samples monthly** — read the judge's reasoning on random cases; drift is invisible from the aggregate score alone

## The Regression Pipeline

Once a prompt ships, changes must prove non-regression:

```
On every proposed prompt change:
1. Run the full test set on the OLD prompt (baseline, if not cached)
2. Run the full test set on the NEW prompt
3. Compare: per-case deltas, not aggregate only
4. Gate: adopt only if no case regresses below threshold AND
   intended improvement holds
5. Record: version, diff, results, decision, date
```

Per-case comparison is the point: aggregate scores hide the case that flipped from right to wrong while averages improved.

## Production Monitoring

Test sets sample reality; production tells you what actually arrives:

- **Log inputs and outputs** (with data governance — see the injection/privacy guides) and sample them monthly: what input shapes did the test set miss?
- **Track Tier 1 failure rates live** — parse failures, refusals, fallback triggers; spikes are your earliest regression alarm
- **Watch drift after model updates**: when the provider updates the model, re-run the suite before assuming continuity — silent behavior changes after model upgrades are a documented production phenomenon, and the suite is your detection layer
- **Feed errors back**: every production failure becomes a test case; the test set is a living artifact (see the Versioning guide)

## Honest Limits

- **Evaluation measures your distribution, not the world**: prompts passing every test still fail on inputs unlike any you saved — the test set is a sample, refreshed or it rots
- **Judges are models too**: every judge limitation above applies, and a judge that agrees with humans today can drift with the next model version — recalibrate on updates
- **The benchmark trap**: optimizing scores past the point of user-noticeable improvement is wasted effort and, worse, invites overfitting the test set; hold out a final set you never optimize against, and refresh test sets when scores saturate
- **No automated check verifies truth**: Tier 3's hallucination check and human verification remain the only truth layers; everything else validates form

## Practice

[Lab 3](../labs/lab-03-evaluation-and-regression-testing.md) is this guide's full guided exercise: a 10-case golden set across four case categories, a four-criterion rubric, one deliberate prompt change, and a before/after regression decision. If you want the one-session version: take any prompt you use weekly, save 10 real inputs (fictionalized), define two pass/fail checks and two rubric criteria, score the current prompt, make one improvement, and re-score. The [evaluation rubric template](../templates/advanced-prompt-templates.md#evaluation-rubric) is the scoring skeleton.

## Further Reading

- [Sahoo et al. — A Systematic Survey of Prompt Engineering](https://arxiv.org/abs/2402.07927) — the evaluation landscape section situates these practices
- Your provider's current evaluation-tooling documentation (evals harnesses, judge modes) — provider-specific and changing (reviewed 2026-10-20)
