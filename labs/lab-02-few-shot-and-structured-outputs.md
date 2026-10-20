# Lab 2 — Few-Shot and Structured Outputs

Build a working extractor: examples that teach the pattern, a schema that constrains the shape, and edge rules that survive messy input.

## Objective

Combine few-shot example selection with schema-constrained output to build a **product-review classifier** that survives edge cases. The artifact is your extractor prompt plus a record of how each edge case behaved across revisions.

## Prerequisites

- [Structured Outputs and Schema Prompting](../Advanced%20Prompt%20Engineering%20Techniques/Structured%20Outputs%20and%20Schema%20Prompting.md) (§3.1)
- [Few-Shot Mastery and Example Selection](../Advanced%20Prompt%20Engineering%20Techniques/Few-Shot%20Mastery%20and%20Example%20Selection.md) (§3.2)
- [Lab 1](./lab-01-prompt-anatomy-and-baselines.md) recommended but not required

## Materials

Synthetic reviews (all fictional):

| ID | Review |
|---|---|
| R1 | "Third one I've bought. Battery still holds a charge after a year, and the case survived a drop down the stairs." |
| R2 | "Arrived with a cracked screen. Support offered a replacement in 48h, so three stars for the recovery." |
| R3 | "It's fine I guess. Does what it says. Nothing more." |
| R4 | "DO NOT BUY. Company spams you with marketing emails forever after purchase." |
| R5 | "Haven't opened it yet — it's a gift for my daughter. Packaging looked nice though." |

Target schema:

```json
{
  "reviews": [
    {
      "id": "string",
      "sentiment": "positive" | "negative" | "mixed" | "unclear",
      "product_experience": boolean,
      "topics": ["battery", "durability", "shipping", "support", "marketing", "packaging", "other"],
      "verbatim_quote": "string, max 15 words"
    }
  ]
}
```

## Steps

### 1. Write the zero-shot version first

Instruct the task in prose with the schema, no examples. Run it on R1–R5. Record where it hesitates or errs — this is your baseline, and the point of comparison for what examples buy you.

**Likely trouble spots to watch for:** R2 (mixed feelings — does `sentiment` collapse to one pole?), R5 (no product experience at all — what happens to `product_experience` and `topics`?), and quote-length violations.

### 2. Select three examples deliberately

Following few-shot selection guidance, write three input→output example pairs (use new fictional reviews, not R1–R5):

- **Example A — typical case:** clear sentiment, clean topics
- **Example B — mixed case:** complaint plus praise, showing `"mixed"` and multiple topics
- **Example C — edge case:** a gift/unopened-type review, showing `"unclear"`, `product_experience: false`, and how topics handle experience-free reviews

Insert them between the task statement and the real input. Run on R1–R5 again and record the deltas against step 1.

### 3. Tighten the edge rules

Add or sharpen rules for: missing fields (`"n/a"`, never omit), restricted values (anything not in the topic list goes to `other` — or a `notes` field), and quote discipline (verbatim, truncated at 15 words with an ellipsis). Run and record.

**Checkpoint:** R5 is the acid test. Before running, write down what your prompt *should* make the model do with R5, then check whether it did.

### 4. Break it on purpose

Feed one input you design to be hostile to the schema: a review in a different structure ("Product: X. Pros: ... Cons: ..."), one with no text at all, one that is pure emoji. Record failures. (A prompt that only works on well-formed input is a demo, not an extractor.)

### 5. Write up the artifact

Keep: (a) the final prompt, (b) the edge-case record — a table of input → observed output → pass/fail → which rule or example fixed it, (c) one sentence on what the examples achieved that the rules could not, and vice versa.

## Self-assessment

You pass this lab when:

- [ ] The zero-shot vs. few-shot delta is recorded, not assumed
- [ ] All five target reviews produce schema-valid JSON with no omitted fields
- [ ] R5 is handled by explicit rule, not luck — you can point to the rule
- [ ] The hostile-input table exists with at least one observed failure and its fix
- [ ] You can state one thing schema constraints do NOT guarantee (if unsure, re-read the structured outputs guide's honesty section)

## Going further

- Port the same task to your provider's native structured-output feature and compare reliability on the same inputs
- Add a second dimension (e.g., `severity: 1–3` with justification) and observe how criteria without examples drift
- This extractor becomes the test subject in [Lab 3](./lab-03-evaluation-and-regression-testing.md)
