# AI Prompt for Data Scientists & ML Engineers

Prompt collections for the full data workflow — from cleaning and EDA to production monitoring and the rigor practices that keep analysis trustworthy.

## Contents

| File | What it covers |
| :-- | :-- |
| [Prompt Engineering for Data Scientists & ML Engineers](./Prompt%20Engineering%20for%20Data%20Scientists%20%26%20ML%20Engineers.md) | The main playbook: cleaning, EDA, feature engineering, model building and debugging, paper summarization, communication, and advanced ML techniques |
| [Data Leakage Prevention & Validation](./Data%20Leakage%20Prevention%20%26%20Validation%20Prompts.md) | Pre-modeling audits, target-leakage interrogation, time-series CV, pipeline integrity, suspiciously-good-results review, drift-vs-leakage diagnosis |
| [Model Evaluation & Interpretation](./Model%20Evaluation%20%26%20Interpretation%20Prompts.md) | Metric selection by decision cost, slice analysis, error autopsies, calibration, careful feature importance, model cards |
| [Experiment Design & Reproducibility](./Experiment%20Design%20%26%20Reproducibility%20Prompts.md) | Pre-registration, seed and environment control, power checks, experiment logs, paired comparisons, artifact freezing |
| [Statistical Rigor & Uncertainty](./Statistical%20Rigor%20%26%20Uncertainty%20Prompts.md) | Assumption checks, uncertainty statements, multiple-comparisons audits, causation guardrails, missing-data mechanisms, hostile review |
| [Data Visualization](./Data%20Visualization%20Prompts.md) | Chart selection by question, honesty audits, distribution display, time-series discipline, dashboard tiles, accessibility |
| [SQL & Data Engineering](./SQL%20%26%20Data%20Engineering%20Prompts.md) | Question-first SQL, query review, incremental pipelines, backfill safety runbooks, data contracts, wrong-number debugging |
| [Code Review & Validation](./Code%20Review%20%26%20Validation%20Prompts.md) | Pre-run review of generated code, test design for data logic, reproducibility gaps, behavior-preserving refactors, dependency audits, security review |

## How to Use This Collection

The main playbook covers the core workflow with beginner-to-expert progression. The companion files add the rigor layer — leakage prevention, evaluation, reproducibility, statistics — that separates exploratory work from defensible work. Every companion prompt includes verification rules; in data work, "the model wrote plausible code" and "the code is correct" are different statements, and the prompts are built around that difference.

For the underlying prompt-technique patterns (structured outputs for pipelines, chaining for multi-stage analysis, evaluation infrastructure), see the [Advanced Prompt Engineering Techniques](../Advanced%20Prompt%20Engineering%20Techniques/) section.

## A Note on the PDF

The PDF in this directory is a snapshot of the main guide from an earlier revision. The Markdown files are the maintained, expanded versions — treat the PDF as a convenient read-only copy, not the source of truth.
