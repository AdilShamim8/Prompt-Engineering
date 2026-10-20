# Structured Outputs and Schema Prompting

Getting AI outputs that machines can parse reliably — JSON, tables, and schema-constrained responses. This is the bridge between "chatting with an AI" and "building software on top of an AI."

## When You Need This

- Output feeds a script, spreadsheet, API, or database
- You run the same extraction/classification repeatedly and need consistency
- Multiple team members or systems consume the output
- You want to validate outputs automatically before a human sees them

## The Core Pattern

Ask for the exact structure, define what every field means, and specify behavior at the edges (missing data, out-of-scope values):

```
Extract product reviews into JSON. Respond ONLY with JSON — no text
before or after.

Schema:
{
  "reviews": [
    {
      "id": integer,
      "sentiment": "positive" | "negative" | "mixed",
      "topics": string[],          // from: pricing, quality, shipping, support
      "would_recommend": boolean,
      "quoted_phrase": string       // verbatim, max 15 words
    }
  ]
}

Rules:
1. Every field is required — use "n/a" or [] when information is absent.
2. Use only the listed topic values; anything else goes in a "notes"
   field? No — it gets DROPPED, per this rule.
3. Quote verbatim from the review only.

Reviews:
"""
[PASTE REVIEWS]
"""
```

The three load-bearing elements: **exact shape** (the schema), **edge behavior** (rules for missing/out-of-scope), and **isolation** ("respond ONLY with JSON").

## Prompt-Level vs API-Level Structured Outputs

**If you are using an API, prefer the provider's structured-output features** (JSON mode, schema-constrained decoding). These enforce validity at the decoding level — the model literally cannot produce malformed JSON — and are more reliable than any prompt instruction. Check the current documentation of your provider: OpenAI, Anthropic, Google, and others all offer structured output support with different capabilities and constraints.

Prompt-level structuring (the pattern above) remains useful when:
- You are in a chat interface, not an API
- The structure is informal (Markdown tables, labeled sections)
- You are prototyping before building the API version

## Common Failure Modes and Fixes

| Failure | Cause | Fix |
| :-- | :-- | :-- |
| Prose before/after the JSON | No isolation instruction | "Respond ONLY with..." + strip in your parser as backup |
| Invented enum values | No closed-set rule | List allowed values explicitly; define the fallback |
| Missing fields on hard inputs | No edge behavior | "Every field required; use n/a when absent" |
| Wrong nesting | Schema ambiguous | Show one fully-worked example row |
| Inconsistent types ("age": "42") | Type unstated | Type every field; give one example |

## Validation Layer (Do This Always)

Prompting for structure does not guarantee structure. Validate outputs before use:

```
Parse → schema check (types, enums, required fields)
     → sanity check (values in plausible ranges, counts match)
     → route failures to: retry with error message, or human review
```

The retry pattern: feed the validation error back — "Your output failed schema validation: `sentiment` must be one of [positive, negative, mixed]; you wrote 'somewhat positive'. Regenerate." This self-correction loop recovers most failures.

## Nested and Complex Schemas

For complex structures, shrink the blast radius: **one entity type per call**, chained (see the Prompt Chaining guide), beats one giant schema that half-fails. A pipeline of extract-then-assemble is easier to debug than a single prompt returning a deeply nested object with a 40% malformed rate.

## Honest Limits

- Structured outputs constrain **format, not truth** — a perfectly valid JSON can contain perfectly fabricated values. Validation checks shape; verification of content is still your job.
- Schema adherence degrades as instructions multiply — keep the rule list short and the schema as simple as the use case allows.
- Model behavior differs across providers and versions; re-test schema prompts when you switch models (see the Evaluation guide).
