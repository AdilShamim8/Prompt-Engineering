# Prompt Chaining and Multi-Stage Workflows

Decomposing complex tasks into sequences of smaller prompts, where each output feeds the next. Chaining is the single most reliable upgrade from "impressive demos" to "dependable results" — it trades one magical prompt for several controllable ones.

## Why Chain Instead of One Big Prompt

- **Reviewability**: you can inspect and correct each stage before it contaminates the next
- **Recoverability**: a failure at stage 3 costs a re-run of stage 3, not everything
- **Specialization**: each stage's prompt does one job, so its instructions stay simple and followable
- **Debuggability**: when output disappoints, you know exactly which stage failed

One big prompt asks a model to hold task, context, format, and multiple rules simultaneously — and loses some of each. Chains keep each step within what models reliably handle.

## The Canonical Patterns

**Pattern 1: Extract → Transform → Draft**

```
Stage 1: "Extract every commitment from these meeting notes.
         Output a table: quote, owner, deadline. Mark missing
         owners 'unclear'. [NOTES]"

Stage 2: "Here is the commitment table: [TABLE]. Group by owner,
         sort by deadline, flag items due within 48 hours."

Stage 3: "Draft a 150-word follow-up email from this organized
         list: [TABLE 2]. Direct, friendly, bullets."
```

**Pattern 2: Draft → Critique → Revise**

```
Stage 1: "Write the first draft of [THING] for [AUDIENCE]."
Stage 2: "Critique this draft as a demanding editor: [DRAFT].
         List the 3 weaknesses, ranked, with reasons. Do not rewrite."
Stage 3: "Revise the draft addressing these critiques: [CRITIQUES].
         Preserve what works. [DRAFT]"
```

The critique stage is where quality comes from — self-revision without explicit critique tends to be cosmetic.

**Pattern 3: Map → Reduce (for many items)**

```
Map:    "Summarize document [i] in 5 bullets with key numbers."
        (run per document, in parallel if your tooling allows)
Reduce: "Synthesize these 12 summaries into: the 5 cross-cutting
         themes, agreements, and contradictions. [SUMMARIES]"
```

**Pattern 4: Gate → Branch**

```
Gate:   "Classify this support ticket: billing / technical / abuse /
         other. Output the label only. [TICKET]"
Branch: route to the specialized prompt for each label
```

## Design Rules for Chains

1. **Each stage outputs exactly what the next stage needs — no more.** Extra content in intermediate outputs becomes noise the next prompt must ignore.
2. **Make intermediate outputs inspectable.** If stage 2's input is garbage, you want to see it before blaming stage 2.
3. **Pass forward only what's needed** — long accumulations of context degrade later stages; a compact structured summary (see the Structured Outputs guide) often works better than raw prose.
4. **Name the failure mode of each stage** and decide what happens on failure: retry, route to human, or halt.
5. **Version the chain as a unit.** A change to stage 2's output format silently breaks stage 3's input expectations — chains need regression tests (see the Evaluation guide) more than single prompts do.

## Failure Modes

| Symptom | Likely stage | Fix |
| :-- | :-- | :-- |
| Final output generic | Stage 1 (extraction thin) | Tighten extraction schema |
| Content correct, structure wrong | Final stage | Isolate the formatting instruction |
| Errors compound wildly | Every stage | Add gates: verify each stage's output before passing |
| Works once, brittle on repeat | Variance across stages | Temperature settings, few-shot anchors in weak stages |
| Context overflow at stage 4+ | Accumulation | Pass structured summaries, not full history |

## When NOT to Chain

Chains add latency and failure surface. For simple tasks, one well-specified prompt is more reliable than three stages. Chain when: outputs need review between steps, the task genuinely decomposes, or single-prompt quality has plateaued after honest iteration.

## From Manual to Automated Chains

Manually copying outputs between prompts is how everyone starts — and it stays fine for irregular work. When a chain becomes routine (daily runs, volume processing), move to programmatic orchestration: API calls with the prompt templates as code, automatic passing of outputs, validation between stages, and logging of every intermediate result. The major LLM application frameworks (LangChain, LlamaIndex, and similar) exist for exactly this — evaluate them when manual copying becomes your bottleneck, not before.
