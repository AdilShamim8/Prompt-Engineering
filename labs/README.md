# Labs

Guided practice that turns the curriculum's reading into demonstrated skill. Each lab states its prerequisites, produces a concrete artifact, and ends with self-assessment criteria you check yourself against.

## Lab philosophy

- **Any major chat model works.** Labs are provider-neutral: use the model you already have. Where model choice changes the exercise, the lab says so.
- **Artifacts over impressions.** Every lab ends with something you can keep — a baseline table, a working extractor, a scored test set. "I read about it" is not the deliverable; the artifact is.
- **Honest measurement.** Where a lab asks you to compare prompt variants, it asks for recorded observations, not feelings. Small samples are labeled as small samples.
- **Fictional inputs only.** Use the provided synthetic material or your own fictional equivalents. Do not paste real personal or confidential data into any model.

## Lab index

| # | Lab | Practices | Prerequisites | Effort |
|---|---|---|---|---|
| 1 | [Prompt Anatomy and Baselines](./lab-01-prompt-anatomy-and-baselines.md) | Restructuring a vague request; measuring the gain | [Stage 1](../CURRICULUM.md#stage-1--foundations) | 45–60 min |
| 2 | [Few-Shot and Structured Outputs](./lab-02-few-shot-and-structured-outputs.md) | Example selection; schema-constrained extraction; edge behavior | [§3.1–3.2](../CURRICULUM.md#tier-a--make-outputs-usable) | 60–90 min |
| 3 | [Evaluation and Regression Testing](./lab-03-evaluation-and-regression-testing.md) | Golden sets; rubrics; measured iteration | [§3.10](../CURRICULUM.md#tier-d--trust-and-reliability) | 60–90 min |

## Lab format

Every lab follows the same structure:

1. **Objective** — the skill being practiced and the artifact produced
2. **Prerequisites** — curriculum sections to have completed first
3. **Materials** — synthetic inputs provided in the lab
4. **Steps** — numbered, with checkpoints that ask you to record observations
5. **Self-assessment** — specific criteria to judge your own result
6. **Going further** — optional extensions, including a design-your-own challenge

## Suggested sequencing

Labs 1 → 2 → 3 follow the curriculum's tiers A and D, and each builds on the previous lab's artifact: Lab 2's extractor becomes Lab 3's test subject. If you skip ahead, Lab 3 provides starter material so it stands alone.

Contributing new labs (chain design, long-context position effects, injection red-teaming are the current gaps — see [ROADMAP.md](../ROADMAP.md)) follows the format above and the standards in [CONTRIBUTING.md](../CONTRIBUTING.md).
