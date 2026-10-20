# Financial Forecasting & Budgeting Prompts

Companion prompts to the main business guide, focused on financial planning, budgeting, and forecasting tasks. Every prompt follows the RTFD structure (Role, Task, Format, Details) and includes verification guidance — financial outputs from AI are starting points for analysis, never final numbers.

***

## 1. Baseline Budget Review

**Prompt:**
>Act as a financial analyst reviewing a department budget. Here is our current budget versus actuals for the last 4 quarters: [paste table]. Identify the 3 largest variances, explain the most likely causes to investigate, and flag any line items where spending patterns look unusual quarter over quarter.

- **Purpose:** A structured first pass over budget data before you commit to conclusions.
- **Why it works:** Explicit input data, ranked output, and a focus on "what to investigate" rather than "what to conclude."
- **Use Case:** Quarterly business reviews, budget preparation.
- **Expert Variation:**
>Extend the analysis with a variance decomposition (volume vs. price vs. timing effects) for each major line item, and propose one corrective action per variance with an estimated financial impact.

**Limitations & verification:** The model sees only the numbers you paste. Verify every variance explanation against the people who own those line items — plausible-sounding causes are frequently wrong in both directions.

***

## 2. Forecast Scenario Construction

**Prompt:**
>Act as a finance business partner. Help me build 3 forecast scenarios (base, optimistic, pessimistic) for [METRIC, e.g., next year's subscription revenue].
>
>Current facts: [existing customers, churn, average deal size, pipeline value, growth history].
>
>For each scenario:
>1. State the 2-3 key assumptions and why they differ between scenarios
>2. Show the calculation logic step by step
>3. Give the resulting range, not a single number
>4. List the leading indicators that would tell us early which scenario is unfolding

- **Purpose:** Scenario-based forecasting that surfaces assumptions instead of hiding them in a model.
- **Why it works:** Requires numbered assumptions and calculation logic, making the forecast auditable.
- **Use Case:** Annual planning, board decks, investor updates.
- **Expert Variation:**
>Add sensitivity analysis: which single assumption, moved by 10%, changes the outcome most? Present as a ranked list with the resulting metric range for each sensitivity.

**Limitations & verification:** AI-generated forecasts extrapolate from the assumptions you provide; they contain no information about your actual market. Recompute the arithmetic independently (models make calculation errors), and treat the scenarios as framing devices for discussion, not predictions.

***

## 3. Budget Cut Triage

**Prompt:**
>We need to reduce [DEPARTMENT] spend by [X]% within [TIMEFRAME]. Here is the current budget: [paste breakdown].
>
>1. Categorize every line item as: protected (legal/safety/core operations), high-impact reduction, or low-impact reduction.
>2. Propose a reduction package that hits the target, showing the math.
>3. For each proposed cut, state: expected savings, likely side effects, and a mitigation.
>4. Explicitly list what you would NOT cut and why.

- **Purpose:** A defensible, structured approach to cost reduction rather than across-the-board slicing.
- **Why it works:** Forces categorization before cutting and requires the model to argue against cuts too.
- **Use Case:** Cost programs, downturn response, restructuring preparation.
- **Expert Variation:**
>Model the second-order effects: for each cut, estimate impact on revenue, headcount morale risk (qualitative), and reinvestment needs in 12 months. Rank cuts by net value destroyed, not gross savings.

**Limitations & verification:** The model does not know which costs are contractually locked or politically sensitive — that knowledge must come from you. Validate the categorization with department owners before acting.

***

## 4. Cash Flow Stress Test Narrative

**Prompt:**
>Act as a CFO advisor for a [STAGE, e.g., seed-stage] company. Our monthly cash position: [paste last 6 months]. Burn rate: [amount]. Runway today: [months].
>
>Walk through, step by step:
>1. What happens to runway if revenue delays 60 days, costs stay flat?
>2. What happens if we lose our largest customer ([%] of revenue)?
>3. At what point must we trigger contingency plans, and which contingencies are realistic at that stage?
>
>Show your arithmetic for each case.

- **Purpose:** Turning raw cash data into decision triggers before a crisis.
- **Why it works:** Concrete scenarios plus required arithmetic make the analysis checkable.
- **Use Case:** Startup financial planning, board reporting.
- **Expert Variation:**
>Propose a monitoring dashboard: the 5 earliest measurable indicators of each scenario, with specific trigger thresholds and the pre-agreed response for each.

**Limitations & verification:** Every number the model produces must be recomputed — arithmetic is the single most common AI failure in finance prompts. Legal and fiduciary obligations (loan covenants, payroll) require professional review, not AI analysis.

***

## 5. Investment Proposal Critique (Pre-Approval)

**Prompt:**
>Act as a skeptical investment committee member. Here is a proposal for [CAPITAL EXPENDITURE / HIRE / PROJECT]: [paste proposal or describe].
>
>Critique it:
>1. Which claimed benefits are unsupported by the evidence presented?
>2. Which costs appear omitted or underestimated?
>3. What is the strongest argument AGAINST approval?
>4. What information, if it existed, would most change the decision?
>5. Finally: 3 questions the committee should ask the proposer.

- **Purpose:** Pre-mortem scrutiny that surfaces weaknesses before money moves.
- **Why it works:** The adversarial role assignment counteracts the proposal's own advocacy bias.
- **Use Case:** CapEx reviews, hiring business cases, project approvals.

**Limitations & verification:** This critique is only as good as the proposal text you paste. It cannot detect omissions you did not describe. Pair it with human due diligence on any material commitment.

***

## 6. Financial Communication for Non-Financial Audiences

**Prompt:**
>Translate this financial analysis for [AUDIENCE, e.g., engineering leads with no finance background]: [paste analysis].
>
>Rules:
>1. Keep every number exact — no rounding that changes meaning.
>2. Replace jargon with plain language on first use (e.g., "runway — months of cash left at current burn").
>3. Lead with the one decision this analysis supports.
>4. End with "what this means for you" specific to the audience.
>5. Flag any figure whose interpretation requires context I have not provided.

- **Purpose:** Making financial reality legible outside the finance team.
- **Why it works:** Rules 1 and 5 guard against the two failure modes of translation: distortion and false certainty.
- **Use Case:** All-hands updates, cross-functional planning, board-to-team cascades.

**Limitations & verification:** Check that no simplification changed a number's meaning — the most dangerous translation error is invisible to non-financial readers, which is exactly who receives the output.

***

## Shared Verification Rules for All Financial Prompts

1. **Recompute every calculation.** Models handle financial reasoning patterns well and arithmetic unreliably. Spreadsheet first, prose second.
2. **Treat all outputs as drafts for human judgment.** Budgets, forecasts, and cuts affect people's jobs — those decisions belong to accountable humans.
3. **Never paste unreleased financials into consumer AI tools.** Material non-public numbers are exactly the data class that should stay in approved enterprise systems (see the repository's privacy guidance).
4. **Distinguish extrapolation from information.** A forecast generated from your assumptions tells you about your assumptions, not about the future.
