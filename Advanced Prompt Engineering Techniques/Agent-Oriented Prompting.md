# Agent-Oriented Prompting

Patterns for systems where a model plans, acts via tools, observes results, and iterates — and for multi-agent designs where specialized prompts collaborate. Agents are the most powerful and most dangerous prompt architecture: everything that makes them useful (autonomy, iteration) makes their failures compounding. This guide covers the prompting patterns and the guardrails.

## What Makes a Prompt "Agentic"

A standard prompt says: "do this task." An agent prompt says: "pursue this goal using these tools, in this loop, under these rules, until this stop condition." The prompt defines a process, not just a task:

```
ROLE: You are a research assistant with these tools: [TOOL LIST].

GOAL: [THE OBJECTIVE — specific, verifiable].

WORKING LOOP:
1. PLAN: state your next action and why (one line).
2. ACT: make exactly one tool call (or produce one work step).
3. OBSERVE: report the result plainly, including failures.
4. REPEAT until the goal is met or a stop condition fires.

STOP CONDITIONS (mandatory):
- Goal achieved: [VERIFIABLE COMPLETION CRITERIA]
- Stalled: 3 consecutive actions without progress
- Out of scope: the task requires [FORBIDDEN ACTIONS]
- Budget: maximum [N] tool calls / [TIME] — then report status
honestly, including what remains undone.

RULES:
- Report tool errors; never fabricate results.
- Never repeat an identical action that already failed; change
  approach or report the blocker.
- Final output: what you accomplished, what you could not, evidence.
```

The three elements standard prompts lack: **verifiable completion criteria**, **stop conditions**, and **failure honesty**. Without them, agents loop, fabricate success, or wander past their mandate.

## Guardrails Are the Design

The honest hierarchy for agent reliability: **hard constraints in code first, prompts second**. Budgets, permissions, and action limits belong in the orchestration layer where they cannot be talked around; the prompt states them so the model plans within them. Never rely on prompt text alone to bound a system that takes actions.

The confirmation gate for irreversible or high-stakes actions:

```
Actions requiring explicit human confirmation before execution:
[payments, sends, deletions, anything affecting external systems
beyond read operations]

When such an action seems needed: STOP and present the proposed
action, its parameters, and your reasoning. Do not execute.
```

## Multi-Agent Patterns

**Pattern 1: Specialized Pipeline (the reliable default)**

```
Agent A (extractor) → structured output → Agent B (analyzer)
→ structured output → Agent C (drafter)
```

Each agent has one role, one prompt, one job. Hand-offs are structured data (see the Structured Outputs guide). This is just prompt chaining with agency inside each stage — and it inherits chaining's debuggability. **Most "multi-agent" needs are this pattern.**

**Pattern 2: Generator–Critic**

```
Agent A: produce [WORK PRODUCT] per [SPEC].
Agent B: critique against the spec — list violations, ranked,
        with quotes. Do not rewrite.
Loop: A revises; B re-critiques; max [N] rounds or until B
      reports the spec met.
```

The separation matters: the critic never drafts, so its critique stays unseduced by draft-authorship. Cap the rounds — uncapped critique loops converge to timid mush.

**Pattern 3: Debate / Multi-Perspective**

```
Agent A argues position 1; Agent B argues position 2; Agent C
(a non-participant chair) summarizes the strongest points of each
and identifies what evidence would settle the disagreement.
```

Useful for genuinely contested analysis; theater when the answer is checkable. Don't debate arithmetic.

**When NOT to use multi-agent designs:** single-agent + tools handles most tasks; each additional agent adds failure surface, cost, and debugging complexity. Add agents when a task genuinely needs separated concerns (maker/checker, different context windows, different permissions) — not because the architecture sounds impressive.

## Agent Failure Modes

| Failure | Symptom | Countermeasure |
| :-- | :-- | :-- |
| Goal drift | Agent pursues adjacent interesting work | Narrow goal + verifiable criteria; reject scope expansion |
| Looping | Repeats failed action | "Never repeat a failed identical action" rule + code-level loop detection |
| Success fabrication | Reports done without evidence | Evidence-requiring final report ("cite tool outputs") |
| Runaway cost | Endless tool calls | Hard budget in code; prompt states it |
| Injection capture | Retrieved content redirects the agent | Untrusted-content rules + tool permissions + confirmation gates |
| Compounding error | Early mistake cascades through steps | Checkpoint reviews; structured intermediate outputs; human gates at stage boundaries |

## Human-in-the-Loop Design

The maturity model worth building toward:

1. **Agent drafts, human executes** — everything reviewed (start here for anything consequential)
2. **Agent executes low-risk, human approves high-risk** — with a crisp risk taxonomy in the rules
3. **Agent executes, human audits samples** — only for reversible, bounded-impact actions

Moving up this ladder is a decision about blast radius, not a milestone to rush past. The organizations that get agents wrong treat autonomy as the goal; the ones that get them right treat it as a cost-benefit choice per action class.

## Honest Limits

- Agent systems are the least deterministic prompt artifact: identical runs diverge, and "it worked in the demo" is the weakest evidence class — production agents need the full evaluation discipline (see the Evaluation guide) plus monitoring
- Self-correction has a ceiling: agents asked to check their own work inherit their own blind spots; the maker-checker separation exists precisely because self-review underperforms
- Current models' long-horizon planning degrades with task length — decompose into stages with checkpoints rather than hoping for one heroic run
