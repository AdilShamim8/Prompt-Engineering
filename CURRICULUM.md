# Curriculum — Prompt Engineering

This document is the authoritative map of the learning curriculum. It defines what prompt engineering means in this repository, how the content is sequenced, what each stage teaches, and the criteria for moving on. The build status of every module is tracked in [`ROADMAP.md`](ROADMAP.md).

## How to read this document

- **Stages** are ordered by dependency. Each stage lists its modules with focus, prerequisites, and outcomes.
- **Two tracks through the same material**: the *foundations track* (Stages 1–2) is for everyone; the *practitioner track* (Stages 3–5) is for people building or seriously optimizing AI-assisted workflows. Domain collections (Stage 4) can be entered after Stage 1 in any order — they are parallel, not sequential.
- **Provider neutrality**: all modules teach techniques that work across major chat models (ChatGPT, Claude, Gemini, and others). Where behavior differs across providers, the guides say so and direct you to current official documentation. Nothing here depends on a specific tool staying still.
- **Numbering convention**: existing guide filenames are stable and unlinked from numbering (see [`ROADMAP.md`](ROADMAP.md) scope decisions). The numbers below define the recommended study order.

## Working definition

**Prompt engineering** is the discipline of designing the inputs to a language model — instructions, examples, context, and output specifications — so that the model's outputs are reliably useful, correct, and safe for a given purpose.

It is distinct from — and complementary to — these adjacent disciplines:

| Discipline | Owns | Relationship to prompt engineering |
|---|---|---|
| Prompt engineering (this repo) | Instructions, examples, constraints, output expectations | The design of what you *say* to the model |
| [Context engineering](https://github.com/AdilShamim8/Context-Engineering) | Everything the model sees at inference time — retrieval, memory, state, tools | The umbrella system in which prompts are one component |
| Fine-tuning | Changing model weights through training | An alternative when prompting cannot express the behavior; far heavier investment |
| Model / product evaluation | Measuring system quality | The feedback loop that tells you whether a prompt change helped |
| AI application engineering | Orchestration, UIs, deployment | Consumes prompt designs as production assets |

## Stage 0 — Orientation

| Module | Focus | Prerequisites |
|---|---|---|
| [Repository README](README.md) | What is here, how it is organized, quick-start examples | None |
| This curriculum | Learning sequence, stage map, mastery criteria | None |

**Outcomes:** you know what the repository contains and can choose a path through it that matches your background and goal.

## Stage 1 — Foundations

All modules in this stage are sections of [Prompt Engineering for Beginners](./AI%20Prompt%20for%20Beginners/Prompt%20Engineering%20for%20Beginners.md).

| # | Module | Focus | Prerequisites |
|---|---|---|---|
| 1.1 | Introduction (§1) | What prompt engineering is and why it matters; how to use the guide | None |
| 1.2 | Core Concepts (§2) | Prompt anatomy, how LLMs process prompts, prompting types | §1 |
| 1.3 | Fundamental Techniques (§3) | Zero-shot, few-shot, chain-of-thought, role-based prompting | §2 |
| 1.4 | Advanced Instruction Techniques (§4) | Instruction engineering, context and constraints, output formatting, iteration | §3 |
| 1.5 | Worked Examples (§5) | End-to-end walkthroughs: content, data analysis, code, problem solving | §3 |
| 1.6 | Pitfalls and Best Practices (§6) | Common mistakes, effective habits, the debugging procedure | §3 |

**Outcomes:** you can write a structured prompt (role, context, task, format, constraints), explain what each component does, recognize why a weak prompt fails, and run the systematic debugging procedure on a prompt that underperforms.

**Mastery criteria:** the Stage 1 exercises in §9 feel straightforward; you can take a vague one-line request and restructure it into a five-component prompt without looking at the template.

## Stage 2 — Responsible and Effective Use

Continues in the Beginners guide; adds your first domain application.

| # | Module | Focus | Prerequisites |
|---|---|---|---|
| 2.1 | Ethical Considerations (§7) | Responsible use, bias mitigation, privacy and security | Stage 1 |
| 2.2 | Tools and Workflows (§8) | Prompt management, testing, A/B methodology | Stage 1 |
| 2.3 | Practice Exercises (§9) | Beginner through advanced exercises and projects | Stages 1–2.2 |
| 2.4 | Reference Materials (§10) | Glossary, templates, checklists, further reading | — (reference) |
| 2.5 | One domain collection | Apply the fundamentals in the collection matching your work (see Stage 4 table) | Stage 1 |

**Outcomes:** you use AI assistance with an accurate mental model of its failure modes, you keep prompts as reusable assets instead of one-off text, and you have applied the fundamentals inside at least one real domain workflow.

## Stage 3 — Core Production Techniques

All modules are guides in [Advanced Prompt Engineering Techniques](./Advanced%20Prompt%20Engineering%20Techniques/), studied in the order below. The tiers build: outputs you can consume → tasks bigger than one prompt → systems that act, not just answer.

### Tier A — Make outputs usable

| # | Guide | Focus | Prerequisites |
|---|---|---|---|
| 3.1 | [Structured Outputs and Schema Prompting](./Advanced%20Prompt%20Engineering%20Techniques/Structured%20Outputs%20and%20Schema%20Prompting.md) | Schema-constrained, machine-parseable responses | Stage 1 |
| 3.2 | [Few-Shot Mastery and Example Selection](./Advanced%20Prompt%20Engineering%20Techniques/Few-Shot%20Mastery%20and%20Example%20Selection.md) | Choosing, formatting, and stress-testing examples | Stage 1 |

### Tier B — Scale to complex tasks

| # | Guide | Focus | Prerequisites |
|---|---|---|---|
| 3.3 | [Prompt Chaining and Multi-Stage Workflows](./Advanced%20Prompt%20Engineering%20Techniques/Prompt%20Chaining%20and%20Multi-Stage%20Workflows.md) | Decomposing tasks into reliable pipelines | 3.1 |
| 3.4 | [Long-Context and Context Management](./Advanced%20Prompt%20Engineering%20Techniques/Long-Context%20and%20Context%20Management.md) | Large documents, position effects, what to include | Stage 1 |
| 3.5 | [RAG Prompting](./Advanced%20Prompt%20Engineering%20Techniques/RAG%20Prompting.md) | Grounding answers in retrieved source material | 3.3, 3.4 |

### Tier C — Extend beyond plain text-in/text-out

| # | Guide | Focus | Prerequisites |
|---|---|---|---|
| 3.6 | [Tool Use and Function Calling](./Advanced%20Prompt%20Engineering%20Techniques/Tool%20Use%20and%20Function%20Calling.md) | Instructing models to call APIs and external tools | 3.1 |
| 3.7 | [Agent-Oriented Prompting](./Advanced%20Prompt%20Engineering%20Techniques/Agent-Oriented%20Prompting.md) | Autonomous loops, planning, multi-agent patterns | 3.3, 3.6 |
| 3.8 | [Multimodal Prompting](./Advanced%20Prompt%20Engineering%20Techniques/Multimodal%20Prompting.md) | Images, audio, and mixed inputs | Stage 1 |

### Tier D — Trust and reliability

| # | Guide | Focus | Prerequisites |
|---|---|---|---|
| 3.9 | [Hallucination Reduction and Source Verification](./Advanced%20Prompt%20Engineering%20Techniques/Hallucination%20Reduction%20and%20Source%20Verification.md) | Techniques that measurably reduce fabrication | Stage 1 |
| 3.10 | [Prompt Evaluation and Testing](./Advanced%20Prompt%20Engineering%20Techniques/Prompt%20Evaluation%20and%20Testing.md) | Test sets, rubrics, regression discipline | 3.1 |
| 3.11 | [Prompt Injection Defense](./Advanced%20Prompt%20Engineering%20Techniques/Prompt%20Injection%20Defense.md) | Threat model and layered mitigations | Stage 1 |

### Tier E — Operate and maintain

| # | Guide | Focus | Prerequisites |
|---|---|---|---|
| 3.12 | [Meta-Prompting and Prompt Optimization](./Advanced%20Prompt%20Engineering%20Techniques/Meta-Prompting%20and%20Prompt%20Optimization.md) | Using AI to design, critique, and improve prompts | Stage 2 |
| 3.13 | [Prompt Versioning and Maintenance](./Advanced%20Prompt%20Engineering%20Techniques/Prompt%20Versioning%20and%20Maintenance.md) | Prompts as versioned production assets | 3.10 |

**Outcomes:** you can select the right technique for a task (and articulate why), produce schema-valid outputs a program can consume, decompose a complex task into a chain, ground answers in supplied sources, and explain both the value and the limits of each technique — including which problems belong to architecture, not prompting.

**Mastery criteria:** given an unfamiliar task, you can classify it (extraction? generation? reasoning? multi-step?) and propose a technique combination with a fallback plan, before writing any prompt.

## Stage 4 — Domain Specialization

The audience collections apply the full technique set inside specific professional contexts. Enter after Stage 1 (fundamentals are assumed); each is self-contained.

| Collection | Best for | Companion advanced guides |
|---|---|---|
| [Business](./AI%20Prompt%20for%20Business/) | Strategy, operations, finance, leadership | Chaining (3.3), Evaluation (3.10) |
| [Data Science & ML](./AI%20Prompt%20for%20Data%20Scientists%20%26%20ML%20Engineers/) | Analysis, modeling, code quality | Structured Outputs (3.1), Evaluation (3.10) |
| [Researchers](./AI%20Prompts%20For%20Researchers/) | Literature review, methodology, academic writing | RAG (3.5), Hallucination Reduction (3.9) |
| [Students](./AI%20Prompts%20For%20Students/) | Study skills, writing, integrity | Long-Context (3.4) |
| [Teachers](./AI%20Prompts%20For%20Teachers/) | Instruction design, assessment, accessibility | Few-Shot (3.2) |
| [HR](./AI%20Prompts%20for%20Human%20Resources%20%28HR%29/) | Compliance-aware people processes | Injection Defense (3.11), Structured Outputs (3.1) |
| [Marketing & Communications](./AI%20Prompts%20for%20Marketing%20%26%20Communications/) | Campaigns, content, claims verification | Hallucination Reduction (3.9), Chaining (3.3) |

**Outcomes:** domain collections are reference material more than sequence — the outcome is fluency in the collection's workflows, with prompts adapted to its constraints (compliance in HR, citation integrity in research, claims verification in marketing).

## Stage 5 — Guided Practice (labs)

Hands-on labs in [`labs/`](labs/) turn the curriculum into demonstrated skill. Each lab states its curriculum prerequisites, works with any major chat model, and ends with self-assessment criteria.

| # | Lab | Practices | Prerequisites |
|---|---|---|---|
| 5.1 | [Prompt Anatomy and Baselines](./labs/lab-01-prompt-anatomy-and-baselines.md) | Structuring a vague request; measuring the improvement | Stage 1 |
| 5.2 | [Few-Shot and Structured Outputs](./labs/lab-02-few-shot-and-structured-outputs.md) | Example selection; schema-constrained extraction | 3.1, 3.2 |
| 5.3 | [Evaluation and Regression Testing](./labs/lab-03-evaluation-and-regression-testing.md) | Test sets, rubrics, iteration with measurement | 3.10 |

**Outcomes:** you have artifacts (baseline comparisons, a working few-shot extractor, a scored test set) that demonstrate the skills, not just familiarity with the reading.

## Time expectations

Honest ranges for a working professional, reading actively and doing exercises:

| Stage | Reading | With exercises |
|---|---|---|
| 1–2 | 4–6 hours | 10–15 hours |
| 3 | 5–7 hours | 15–25 hours |
| 4 (one collection) | 2–4 hours | 5–8 hours |
| 5 (all labs) | — | 6–10 hours |

## What this curriculum deliberately does not cover

- **System building**: retrieval pipelines, memory, agent infrastructure → the [Context-Engineering](https://github.com/AdilShamim8/Context-Engineering) repository.
- **Model training and fine-tuning**: weight-level adaptation is out of scope; this repo covers the instruction layer.
- **Provider API specifics**: taught as concepts with verify-against-current-docs notes, because API details change faster than curriculum.
