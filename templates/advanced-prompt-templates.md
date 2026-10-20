# Advanced Prompt Templates

Templates for programmatic and multi-stage work, each paired with the guide that teaches the underlying technique in depth. All follow the repository's honesty rules: format constraints shape structure, not truth; chains organize work, not correctness — verification stays in the loop.

## Structured Output Extraction

For outputs consumed by a script, spreadsheet, or API. If your provider offers schema-constrained decoding (JSON mode or structured outputs), **use that instead of this prompt** — decoding-level enforcement beats instruction-level requests. Template below is the prompt-only fallback and the conceptual core.

```
Extract [DOMAIN] records from the input into JSON. Respond with
ONLY valid JSON — no text before or after, no markdown fences.

Schema:
{
  "[records_key]": [
    {
      "[field_1]": [type],
      "[field_2]": "allowed_value_1" | "allowed_value_2",
      "[field_3]": [type][],
      "[field_4]": boolean
    }
  ]
}

Rules:
1. Every field is required — use "n/a" or [] when the information
   is absent. Never omit a field.
2. Use only the listed values for restricted fields; anything else
   goes into "notes": string.
3. Quote verbatim from the input; never paraphrase quoted material.
4. If NO records are found, return {"[records_key]": []}.

Input:
"""
[PASTE INPUT]
"""
```

Edge behavior (rules 1, 2, 4) is the load-bearing part: unconstrained edge cases are where extraction silently fails. Full technique: [Structured Outputs and Schema Prompting](../Advanced%20Prompt%20Engineering%20Techniques/Structured%20Outputs%20and%20Schema%20Prompting.md).

## Two-Stage Prompt Chain

The minimal chain: separate extraction from generation, because asking for analysis and polished writing in one prompt degrades both. Each stage gets a focused prompt; you (or code) verify the handoff.

```
── Stage 1: Extract ──

From the input below, extract [INFORMATION] as a bullet list.
Quote the source for each bullet. Do not interpret or summarize
beyond extraction. If something is absent, write "ABSENT: [item]".

Input:
"""
[PASTE INPUT]
"""

── verify stage 1 output before continuing ──

── Stage 2: Generate ──

Using ONLY this extracted material (do not invent facts):

"""
[PASTE VERIFIED STAGE 1 OUTPUT]
"""

[TASK: e.g., draft X, decide Y, summarize for Z audience]

FORMAT: [structure]
CONSTRAINTS: [boundaries; flag any gap in the material rather
than filling it]
```

**Chain rule:** every stage's output must be checkable before it feeds the next — chains propagate errors as well as they propagate correctness. Full technique: [Prompt Chaining](../Advanced%20Prompt%20Engineering%20Techniques/Prompt%20Chaining%20and%20Multi-Stage%20Workflows.md).

## RAG Grounded Answer

When the answer must come from supplied sources. The three non-negotiables: sources are the *only* permitted basis, "I don't know" is an acceptable answer, and every claim carries a citation.

```
Answer the question using ONLY the sources below. If the sources
do not contain the answer, say exactly that — do not use outside
knowledge to fill gaps.

Citation rule: every factual sentence ends with [S1], [S2], ...
matching the source labels. If two sources conflict, state the
conflict and quote both.

Question: [PASTE QUESTION]

Sources:
[S1]
"""
[PASTE SOURCE 1]
"""
[S2]
"""
[PASTE SOURCE 2]
"""
```

**Honesty note:** grounding reduces fabrication; it does not eliminate it. Verification of consequential answers against the cited sources remains necessary. Full technique: [RAG Prompting](../Advanced%20Prompt%20Engineering%20Techniques/RAG%20Prompting.md).

## Evaluation Rubric

For scoring outputs consistently, by hand or model-assisted (model-assisted scoring still needs human spot-checks). This template is the backbone of the golden-set workflow in [Prompt Evaluation and Testing](../Advanced%20Prompt%20Engineering%20Techniques/Prompt%20Evaluation%20and%20Testing.md).

```
Score the following output against this rubric. For each
criterion: score 0 (fail), 1 (partial), or 2 (pass), with a
one-line justification quoting the output.

Rubric:
- Accuracy: every factual claim is correct and verifiable
- Completeness: covers all required elements of the task
- Format compliance: matches the requested structure exactly
- Edge behavior: handles missing/ambiguous input as specified
- [DOMAIN CRITERION: e.g., No unverifiable claims]

Task that produced the output:
"""
[PASTE PROMPT]
"""

Output to score:
"""
[PASTE OUTPUT]
"""

Report as: criterion | score | justification, then TOTAL / [max].
```

**Regression use:** score the same fixed test set before and after any prompt change; a change that fixes one case but breaks two others is a regression, not an improvement.
