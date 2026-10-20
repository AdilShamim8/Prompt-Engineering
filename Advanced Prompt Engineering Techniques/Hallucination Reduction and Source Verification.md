# Hallucination Reduction and Source Verification

Techniques that measurably reduce fabrication — and the verification discipline that catches what remains. The honest premise: hallucination cannot be prompted away entirely. It is a property of how these systems generate. The goal is reducing its frequency, containing its blast radius, and building the checks that catch it before it matters.

## Why Models Fabricate

Understanding the mechanism guides the countermeasures:

- Models generate the most plausible continuation — plausibility and truth overlap often but not always
- Gaps in knowledge are filled with fluent, confident text (they don't feel like gaps from inside)
- Pressure to complete a format (a citation field, a date column) fabricates what the format demands
- Ambiguous or leading prompts resolve the ambiguity toward whatever pattern is strongest in context

The countermeasures target each mechanism: remove the pressure, supply the knowledge, and make guessing more expensive than admitting gaps.

## The Reduction Techniques

**1. Ground or Refuse (the highest-impact pattern)**

```
Answer using ONLY the sources provided below. If they do not contain
the answer, say "not in sources" — do not fill from general knowledge.

Sources:
"""
[PASTE]
"""
```

Grounded prompts trade coverage for verifiability. The refusal hatch is what makes it work — without it, models bridge gaps invisibly.

**2. Make Uncertainty Sayable**

```
After your answer, list:
- Claims you are confident are supported by the sources/input
- Claims that are inferences or general knowledge — mark each [UNVERIFIED]
- What you could not determine
```

Calibration improves when uncertainty has a sanctioned channel. Unprompted, models default to uniform confidence.

**3. Remove the Format Pressure**

Fabrication peaks when a structure demands values the material lacks:

```
Instead of: "Extract: name, date, amount, and reference number for
            every transaction."
Use:        "Extract: name, date, amount, and reference number where
            present. Use 'not stated' for absent fields. List ONLY
            transactions that appear in the text."
```

**4. Decompose the Confidence Trick**

```
Before answering: rate your familiarity with this specific topic as
high / medium / low. If medium or low, say so first, then answer with
appropriate hedging and flag which parts need independent verification.
```

Not bulletproof — models misjudge their own knowledge — but it shifts tone and flags the zones for your verification.

**5. Ask for Evidence, Not Just Answers**

```
For each factual claim in your response, quote the supporting
sentence from the provided material. Claims without support: mark
[UNSUPPORTED] or remove them.
```

Requiring quotes turns hallucination into a visible failure (a fabricated quote won't match the source) instead of an invisible one.

## What Does NOT Work (Popular but Weak)

- **"Do not hallucinate"** — the model does not know when it is hallucinating; the instruction has no operational handle
- **"Be accurate"** — accuracy is not a dial the model can choose
- **Confidence theater** — demanding "only 100% certain facts" yields the same text with a confident tone, not better calibration
- **Watermark self-reports** — asking "did you make anything up?" reliably produces "no"

These fail for the same reason: they address the symptom (confident fabrication) rather than the cause (generating plausible continuations under pressure).

## The Verification Layer (Non-Negotiable)

Reduction techniques lower the rate; verification catches the residue:

```
The verification triage — which outputs deserve which checking:

HIGH STAKES (numbers in circulated docs, citations, health/legal/
financial claims, anything published):
  → Every factual claim checked against a primary source, by a human

MEDIUM (internal drafts, working analyses):
  → Spot-check: verify the load-bearing claims (the ones your
    conclusion depends on), especially statistics and anything
    the model marked [UNVERIFIED]

LOW (brainstorms, first drafts, format experiments):
  → Read with default skepticism; verify before anything escalates
```

**Citation verification specifically** (see the Researchers collection for the full protocol): AI-generated citations must be confirmed to (a) exist, via a real database, and (b) actually support the claim. Both failures occur; the second is sneakier.

**Numbers specifically:** recompute independently, always. Arithmetic is the most reliable hallucination surface in the entire stack — models produce wrong sums with perfect fluency.

## Measuring Hallucination Rates

For prompts in repeated use, make fabrication a tracked metric (see the Evaluation guide):

- Maintain 20+ test inputs where you know the ground truth
- Score outputs: fabricated claims / total claims (per sample, by a human or a well-calibrated judge)
- Track the rate over prompt versions — grounding patterns that work on your tasks become visible; regressions after model updates surface early

## The Honest Ceiling

Even with every technique applied, hallucination rates go down, not to zero — and the residual failures are the fluent, plausible ones that evade casual reading. That is why this guide's title has two parts: reduction techniques AND verification. Any workflow that deploys the first without the second is choosing to be surprised eventually. The verification layer is not an admission of failure; it is the professional operating procedure for a tool whose fluency and reliability are separate dials.
