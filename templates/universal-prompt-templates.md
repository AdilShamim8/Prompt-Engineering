# Universal Prompt Templates

Domain-neutral templates for everyday prompting. Every template here is the compressed form of a technique taught in the [Beginners guide](../AI%20Prompt%20for%20Beginners/Prompt%20Engineering%20for%20Beginners.md); see [the index](./README.md) for when to reach for each.

## The Five-Component Universal Prompt

The default structure for any substantive single-turn task. Works because it answers the model's four implicit questions — who are you, what do you know, what do I want, and in what shape — plus the guardrails.

```
ROLE: [Who the model should act as, with the relevant expertise]

CONTEXT: [Background the model needs: situation, audience, what
has been tried, what "good" means here]

TASK: [The specific, verifiable action — one task, stated once]

FORMAT: [Output structure: sections, table, length, language]

CONSTRAINTS: [Boundaries: what to exclude, always do, or refuse;
edge-case behavior for missing or out-of-scope information]

[PASTE INPUT MATERIAL HERE]
```

**Common failure:** filling CONTEXT with everything you know instead of what changes the answer. Test by deletion: remove a context sentence; if output quality is unchanged, it did not belong.

## Few-Shot Task Definition

When the model must follow a specific input→output pattern that instructions alone describe poorly. Two to five well-chosen examples usually beat more words; selection guidance is in [Few-Shot Mastery](../Advanced%20Prompt%20Engineering%20Techniques/Few-Shot%20Mastery%20and%20Example%20Selection.md).

```
TASK: [One-line definition of the transformation]

I'll show you [N] examples, then you apply the same pattern.

INPUT: [example input 1 — a typical case]
OUTPUT: [example output 1]

INPUT: [example input 2 — a different-looking case]
OUTPUT: [example output 2]

INPUT: [example input 3 — an edge case: missing data, unusual form]
OUTPUT: [example output 3 — shows how edges are handled]

Now apply the pattern to:

INPUT: [PASTE ACTUAL INPUT]
OUTPUT:
```

**Selection rule:** include at least one example shaped like your real input, and at least one edge case showing what to do when information is missing.

## Iterative Refinement

When a draft exists and needs targeted improvement — the highest-leverage, lowest-effort loop in everyday use.

```
Here is a draft [DOCUMENT TYPE]:

"""
[PASTE DRAFT]
"""

Improve it: [ONE SPECIFIC DIMENSION — e.g., "cut 30% of the length
without losing the action items" / "make the opening paragraph
concrete instead of generic"].

Keep everything else about the draft unchanged, especially:
[PRESERVE LIST — tone, facts, structure]

Output the revised [DOCUMENT TYPE] only.
```

**Common failure:** asking for "make it better." Unidimensional, measurable instructions ("cut 30%", "replace jargon with plain English in every sentence") converge; vague praise-requests wander.

## Debugging an Underperforming Prompt

A structured interview with the model about its own output — the diagnostic step before editing a failing prompt (the full procedure is Beginners guide §6.3).

```
I'm going to show you a prompt and the response it produced.

PROMPT:
"""
[PASTE THE PROMPT]
"""

RESPONSE:
"""
[PASTE THE RESPONSE]
"""

The response is not what I wanted. Before I rewrite anything,
diagnose it:

1. Restate what you believe the prompt was asking for.
2. List points where the response deviates from that reading.
3. For each deviation, say whether the cause is ambiguity in the
   prompt, missing context, or an unreasonable request.
4. Suggest the smallest prompt change that would fix each cause.

Do not rewrite the prompt yet — diagnose first.
```

**Why it works:** most "bad outputs" are faithful answers to a prompt that asked for something other than what the author meant. The diagnosis separates those cases from genuinely missing context before you start editing.
