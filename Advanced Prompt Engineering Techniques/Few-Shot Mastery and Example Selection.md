# Few-Shot Mastery and Example Selection

Few-shot prompting — showing the model 2–5 worked examples — is the highest-leverage technique for controlling format, style, and edge-case behavior. It is also the technique most often used badly: examples chosen for convenience rather than strategy. This guide covers the selection and engineering of examples.

## Before You Start

**Learning objectives** — after this guide you can: select examples that sit on decision boundaries instead of easy cases; format examples for consistent pattern-following; recognize the five example pathologies and their fixes; and grow an example set error-driven, like an engineer.

**Prerequisites** — the [Beginners guide](../AI%20Prompt%20for%20Beginners/Prompt%20Engineering%20for%20Beginners.md) fundamentals (§3 covers few-shot basics). Curriculum position: [§3.2](../CURRICULUM.md#tier-a--make-outputs-usable); pairs naturally with [Structured Outputs](./Structured%20Outputs%20and%20Schema%20Prompting.md) — schemas constrain the shape, examples teach the judgment.

## What Examples Actually Do

Examples communicate what instructions cannot: the exact shape of "good," the handling of ambiguous cases, and the register of the output. Instructions say "extract the key claims"; examples show what counts as key. When your instructions and your examples disagree, **the examples usually win** — which makes them load-bearing, not decorative.

## Selecting Examples (The Part Everyone Skips)

**Cover the decision boundaries, not the easy cases.**

If you are classifying support tickets, the easy examples (clearly billing, clearly technical) teach nothing — the model gets those right zero-shot. Your examples should sit ON the boundaries:

```
# Example set for ticket classification:

"my card got charged twice this month"        → billing
"refund not showing up even though you sent it" → billing   (sounds technical, is billing)
"app won't stop crashing on upload"           → technical
"how do I export my data"                      → technical (phrased as a question)
"your pricing is ridiculous, cancel me"        → billing   (angry, not abuse)
"you people are scammers"                      → other     (not actionable billing)
```

Every example earns its place by resolving an ambiguity the instructions leave open.

**Selection checklist:**

- [ ] Each example demonstrates something the others do not
- [ ] At least one handles a genuinely ambiguous/borderline input
- [ ] At least one shows the fallback behavior ("n/a", "other", empty output)
- [ ] No two examples are near-duplicates (they crowd out coverage)
- [ ] The hardest/most representative case is LAST (models weight recent context more)

## Formatting Examples

```
Input:  "The delivery arrived in 3 days but the box was crushed."
Output: {"delivery": "positive", "packaging": "negative", "product": "n/a"}

Input:  "Doesn't fit my phone and support never replied."
Output: {"product": "negative", "support": "negative", "delivery": "n/a"}

Input:  [NEW TICKET TO CLASSIFY]
Output:
```

The consistency rules that matter:

1. **Identical structure across all examples** — same field order, same punctuation habits, same missing-value convention
2. **Consistent labels for consistent logic** — if "refund" maps to billing twice, never to support
3. **The trailing incomplete example** (input present, output absent) invites completion in the established pattern
4. **Keep instructions AND examples** — "Classify each review by aspect: [examples]" outperforms examples alone for boundary clarity

## Example Pathologies

| Pathology | Symptom | Fix |
| :-- | :-- | :-- |
| Example bias | Model copies example content into outputs | Use placeholder-flavored content in examples, distinct from your real inputs |
| Label drift | Outputs invent new categories | Every example uses only allowed labels; add one example demonstrating the fallback label |
| Format overfit | Model outputs example-style even when wrong | Ensure examples show varied lengths/shapes within the required format |
| Too many examples | Degraded attention to instructions, context bloat | 2–5 well-chosen beats 10 convenient; delete any example that adds no boundary |
| Stale examples | Quality decay over months as inputs shift | Revisit example sets quarterly against recent errors (see Evaluation guide) |

## Iterating Examples Like an Engineer

When outputs are wrong in a repeated, specific way, the fix is usually an example, not an exhortation:

1. Find a real input the model got wrong
2. Add it (with the correct output) to the example set
3. Re-run on your test inputs; confirm the fix and check nothing else broke
4. If the example set grows past ~7, prune the least-earning example

This error-driven example curation compounds: your example set becomes a memory of every failure mode you have encountered — something instructions alone can never be.

## When Few-Shot Is the Wrong Tool

- **Simple, unambiguous tasks**: zero-shot with clear instructions is cheaper and just as good
- **Task the model already does canonically** (sentiment, summarization of standard documents): examples can even hurt by over-narrowing
- **Reasoning tasks**: examples of conclusions without reasoning can suppress the model's own chain of thought — prefer explicit reasoning instructions (see the Beginners guide, Section 3.3)
- **Very long outputs**: two full-length examples consume context; use structural skeletons instead

## Practice

Write a zero-shot instruction for classifying your own work items (emails, tickets, tasks — fictional stand-ins), run it on 10 inputs, and record the errors. Then add exactly three examples chosen against the selection checklist — one typical, one boundary, one fallback — and re-run. Compare error counts and note which specific errors the examples fixed and which they did not touch. The guided version with edge-case testing is [Lab 2](../labs/lab-02-few-shot-and-structured-outputs.md).

## Further Reading

- [Few-shot task definition template](../templates/universal-prompt-templates.md#few-shot-task-definition) — the copy-paste skeleton
- [Anthropic — prompting best practices](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview): effective example use (reviewed 2026-10-20; provider-specific)
