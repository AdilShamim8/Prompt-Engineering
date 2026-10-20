# Meta-Prompting and Prompt Optimization

Using AI to design, critique, and improve prompts — treating the model as a collaborator in prompt engineering rather than only an executor of prompts. Done well, this surfaces blind spots and generates variations you would not have written. Done naively, it produces confident-sounding generic advice. The difference is in how you drive it.

## Before You Start

**Learning objectives** — after this guide you can: run the four meta-patterns (critique, generation, adversarial testing, library audit) with the inputs that make them produce specifics; avoid the recursion trap; and keep evaluation — not model opinion — as the acceptance test.

**Prerequisites** — [Beginners guide](../AI%20Prompt%20for%20Beginners/Prompt%20Engineering%20for%20Beginners.md) fundamentals (Stage 2); you must already write structured prompts to critique them productively. Curriculum position: [§3.12](../CURRICULUM.md#tier-e--operate-and-maintain); the discipline that keeps meta-prompting honest is [Evaluation](./Prompt%20Evaluation%20and%20Testing.md).

## The Meta-Patterns

**Pattern 1: Prompt Critique (the workhorse)**

```
Act as a senior prompt engineer. Critique this prompt for a [MODEL TYPE,
e.g., chat model used for customer support triage]:

[PASTE YOUR PROMPT]

1. Ambiguities: which phrases could be interpreted two ways? Quote each.
2. Missing specification: what does the prompt leave to the model's
   discretion that should be pinned down?
3. Conflict: do any instructions contradict or compete?
4. Edge cases: what inputs would break this prompt's assumptions?
5. Rewrite the two weakest parts. Leave the rest untouched — I want a
   diff, not a redesign.
```

The "diff, not redesign" instruction is what makes this useful — uncontrolled, meta-prompting produces enthusiastic rewrites that lose your intent.

**Pattern 2: Prompt From Intent (generation)**

```
I need a prompt that: [GOAL + AUDIENCE + INPUT TYPES + DESIRED OUTPUT].
Constraints: [LENGTH, TONE, MUST/MUST-NOT rules].
1. Draft the prompt.
2. Then critique YOUR OWN draft against my requirements — list what a
   careful prompt engineer would flag.
3. Produce the revised version incorporating those fixes.
```

The self-critique step (draft → critique → revise) measurably improves generation quality — it forces the model to check its work against your requirements rather than declaring victory at the draft.

**Pattern 3: Variation Generation (for testing)**

```
Here is my working prompt: [PASTE]. Generate 4 meaningfully different
variations, each changing ONE dimension:
a) restructured (task-first, numbered rules)
b) example-augmented (adds 2 few-shot examples)
c) persona-framed (adds role and audience)
d) constraint-tightened (adds output contract and fallback rules)
Explain what each variation is testing. Do not claim which is best —
that's what my test set is for.
```

**Pattern 4: Failure Autopsy Assistant**

```
My prompt failed on this input: [INPUT] — produced [OUTPUT] instead of
[EXPECTED]. Here is the prompt: [PASTE].
1. Diagnose: which part of the prompt allowed or caused this failure?
2. Propose the minimal fix — smallest change that addresses the cause.
3. What regression risk does the fix introduce (where might it break
   inputs that currently work)?
```

## What Meta-Prompting Is Good and Bad At

**Good at:** spotting ambiguity, generating variations, identifying missing edge-case handling, restructuring for clarity, producing critique checklists, translating a goal into a first draft.

**Bad at:** knowing your data, your users, or your domain's failure patterns; predicting which variation will actually perform better (only your test set knows); anything requiring the taste that comes from having run the prompt on real inputs.

**The cardinal rule:** meta-prompting output is a hypothesis. Every AI-proposed prompt and variation gets tested on your real inputs before adoption (see the Evaluation guide). Prompts proposed by models have exactly the same epistemic status as prose written by models: plausible until proven.

## Meta-Prompting a Prompt Library

For teams maintaining prompt collections (see the Versioning guide), meta-prompting scales into maintenance operations:

```
Here are 5 prompts from our library with their purposes: [PASTES].
1. Consistency audit: where do they diverge in structure, terminology,
   or output contracts for equivalent tasks?
2. Consolidation candidates: which two could merge, and what would be
   lost?
3. Each prompt's weakest element, one line each.
```

Run periodically, applied by a human who knows the library's history — the model sees text; you see context.

## The Recursion Trap

Meta-prompting can nest: prompts that critique prompts that critique prompts. Each layer adds confident-sounding analysis and subtracts grounding. Two layers is the practical ceiling — a prompt, and a critique of the prompt. If the critique of the critique seems needed, the real problem is usually that you haven't tested anything yet. Stop abstracting; go run the prompt on real inputs.

## Practice

Take one prompt you actually use and run the critique pattern with real artifacts attached: your prompt, two real outputs it produced (one good, one bad), and the task description. Require numbered, ranked weaknesses with quoted evidence — reject any critique that could apply to any prompt (the genericity test). Then implement exactly the top-ranked fix and re-run on the same inputs. If the fix does not measurably change the weak output, the critique was flattery, not analysis — note what that teaches you about meta-prompting's acceptance test.

## Further Reading

- [Zamfirescu-Pereira et al. — Why Johnny Can't Prompt](https://arxiv.org/abs/2307.06873) — why end-users' natural prompting fails, and what tooling must compensate
- [Anthropic — prompt generator / metaprompt recipe](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview) — provider's own meta-prompting tooling (reviewed 2026-10-20; verify against current docs)
