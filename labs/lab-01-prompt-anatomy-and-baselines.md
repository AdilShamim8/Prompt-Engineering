# Lab 1 — Prompt Anatomy and Baselines

Measure, don't assume: take one vague request through three prompt revisions and record what actually improves.

## Objective

Practice the five-component prompt structure (role, context, task, format, constraints) and produce a **baseline comparison table** — the same task attempted with three prompt levels, with results recorded side by side. This artifact is the foundation for every evaluation habit in the rest of the curriculum.

## Prerequisites

- [Beginners guide §1–3](../AI%20Prompt%20for%20Beginners/Prompt%20Engineering%20for%20Beginners.md): prompt anatomy, core techniques
- The [five-component universal template](../templates/universal-prompt-templates.md#the-five-component-universal-prompt)

## Materials

Use this synthetic task (or your own fictional equivalent — nothing confidential):

> You need a short customer-service email reply. The customer, R. Okafor, wrote: "I bought the Deskif standing desk mat on the 3rd and the edge is already peeling. This is the second issue I've had with you people. I want to know what you're going to do about it." The company policy allows a full refund or replacement within 30 days for verified defects. The reply should acknowledge the frustration, state the two options, and give one clear next step. Deskif is a fictional brand.

## Steps

### 1. Run the vague baseline (V0)

Send only: `Reply to this customer email: [paste the customer message]`

Record the output. Note three specific weaknesses: what did it get wrong, omit, or invent? (Common results: generic tone, no options stated, invented policies like "we've issued a 20% coupon".)

### 2. Add structure (V1)

Rewrite using all five components — role, context (including the real policy), task, format (e.g., "under 120 words, three short paragraphs"), and constraints (e.g., "do not invent compensation beyond the two options; do not blame the customer"). Run and record.

**Checkpoint:** before comparing, predict one thing V1 will still get wrong. Write the prediction down — you are calibrating your expectations, not just admiring the output.

### 3. Sharpen the edges (V2)

Take V1 and improve only its *edge behavior*: add explicit rules for what happens when information is missing (e.g., "if the defect cannot be verified, say what verification is needed — do not promise a refund"), and specify tone with a concrete example sentence the reply's voice should match. Run and record.

### 4. Build the comparison table

Create this artifact (Markdown or spreadsheet):

| Dimension | V0 — vague | V1 — structured | V2 — edge-sharpened |
|---|---|---|---|
| States both policy options correctly | ☐ | ☐ | ☐ |
| No invented facts/policies | ☐ | ☐ | ☐ |
| Acknowledges frustration without groveling | ☐ | ☐ | ☐ |
| One clear next step | ☐ | ☐ | ☐ |
| Format/length compliant | ☐ | ☐ | ☐ |
| Word count (approx.) | | | |

Mark each cell pass/fail by checking the output against the criterion — quoting the offending line for every fail.

### 5. Run the deletion test

From V2, delete the CONTEXT paragraph entirely and re-run. Record whether output quality drops. If it does not, your context was decoration, not information. (Either result is a finding — record it honestly.)

## Self-assessment

You pass this lab when:

- [ ] Your table shows three genuinely scored variants, with quoted evidence for failures — not impressions
- [ ] You can name, for each of the five components, the specific failure it prevented (or confirm it prevented none, and why)
- [ ] Your step-2 prediction was written down before you looked at V1's output
- [ ] The deletion test produced a recorded conclusion

## Going further

- Repeat with a task from your own work, using fictional stand-ins for real names and numbers
- Add a V3 that uses a different role — observe what the role actually changes (usually register, rarely facts)
- Keep the winning prompt as your first entry in a personal prompt library (see [Prompt Versioning](../Advanced%20Prompt%20Engineering%20Techniques/Prompt%20Versioning%20and%20Maintenance.md))
