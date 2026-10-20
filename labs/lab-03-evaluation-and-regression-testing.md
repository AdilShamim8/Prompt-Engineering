# Lab 3 — Evaluation and Regression Testing

Stop iterating by vibes: build a golden set, score changes against it, and catch the improvement that quietly broke something else.

## Objective

Build a small **golden set with a scoring rubric**, then make a deliberate prompt change and measure whether it is a net improvement or a hidden regression. The artifact is your test set plus a before/after score record.

## Prerequisites

- [Prompt Evaluation and Testing](../Advanced%20Prompt%20Engineering%20Techniques/Prompt%20Evaluation%20and%20Testing.md) (§3.10)
- [Lab 2](./lab-02-few-shot-and-structured-outputs.md) recommended: its extractor is the ideal test subject. A standalone starter task is provided below if you skipped it.

## Materials

**Test subject (choose one):**

- **Option A:** Your Lab 2 review-classification prompt.
- **Option B (standalone):** A meeting-notes summarizer. Prompt: given raw notes, produce a summary with sections `Decisions`, `Action items` (each with owner if stated), and `Open questions`. Everything must come from the notes — no invented items.

**Starter test material (fictional; use or write your own):**

```text
Sprint planning — Tue. Present: Dana (lead), Marcus, Priya.
Agenda: release date, hiring, infra budget.

Dana: pushing release to the 14th, QA needs two full days.
Marcus: two days ok if freeze lands Monday EOD. Agreed.
Priya: candidate loop for the backend role starts Thursday,
needs a question panel — volunteers? Dana will ask the team.
Marcus: AWS bill up 18%, mostly the staging cluster left
running. He'll set an auto-shutdown and report next week.
Dana: open question — do we need the legacy API for the
October customers? Nobody knew; she'll check with sales.
```

Note the built-in traps: one action item has no owner (volunteers), one is self-assigned mid-discussion, and the open question must not become an action item.

## Steps

### 1. Build the golden set (10 cases)

Write 10 test inputs with known-correct key facts — the answers a careful human would extract. Include:

- 3 typical cases (clean, well-formed)
- 3 edge cases (missing information, ambiguity, tangents)
- 2 adversarial cases (tempting-to-invent gaps: e.g., notes that never state a date when the task implies one)
- 2 regression candidates (cases your current prompt handles well — these are what changes usually break)

**Record the expected key facts per case, not full expected outputs** — exact-match grading punishes valid phrasing variance.

### 2. Write the rubric

Four to six criteria, each 0/1/2 with a one-line definition of what "2" requires (borrow the structure from the [evaluation rubric template](../templates/advanced-prompt-templates.md#evaluation-rubric)). Example criteria for the summarizer: factual fidelity, action-item completeness, no invented content, format compliance, open-question separation.

### 3. Baseline run

Run your current prompt on all 10 cases. Score each against the rubric (you score, or model-assisted scoring with your spot-checks on at least three cases). Record the total and per-case scores.

**Sample-size honesty:** 10 cases is a smoke test, not a statistic — it catches regressions reliably, fine differences unreliably. Say so in your record; do not claim significance you don't have.

### 4. Make one deliberate change

Pick a real weakness from the baseline (e.g., "invents owners for unowned action items") and change ONE thing in the prompt to fix it. One change per iteration — with two changes you cannot attribute the effect.

### 5. Re-run and compare

Score all 10 cases with the changed prompt. Build the before/after table: per-case delta, total delta, and specifically what happened to your regression candidates.

**Decision rule:** ship the change only if (a) the target case(s) improved and (b) no regression candidate got worse. If a case regressed, you've found exactly what unmeasured iteration does silently — record it.

### 6. Keep the loop

Store the golden set and rubric next to the prompt (same file or folder — see [Prompt Versioning](../Advanced%20Prompt%20Engineering%20Techniques/Prompt%20Versioning%20and%20Maintenance.md)). Any future prompt change re-runs this suite first.

## Self-assessment

You pass this lab when:

- [ ] The golden set contains all four case categories, with expected facts recorded
- [ ] Baseline and post-change scores exist for all 10 cases
- [ ] You made exactly one change, and can attribute the delta to it
- [ ] The regression candidates were explicitly checked, with a stated ship/hold decision
- [ ] Your record states the sample-size limitation honestly

## Going further

- Add a "frozen copy" workflow: never edit the live prompt in place; copy, change, test, then swap (the versioning guide's minimal discipline)
- Have a model score outputs model-blind (prompts and outputs labeled A/B, no "which is mine") and check its agreement with your scores — agreement is a finding, disagreement is a bigger one
- Extend to 20 cases and observe when per-case scoring starts to feel like overhead — that is where lightweight automation earns its place
