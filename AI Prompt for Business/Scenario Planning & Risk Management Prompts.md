# Scenario Planning & Risk Management Prompts

Companion prompts to the main business guide for anticipating what could go wrong — and what to do about it — before it does. These prompts are designed to produce assumptions you can argue with, not predictions you can lean on.

***

## 1. Scenario Matrix Construction

**Prompt:**
>Act as a strategy facilitator. Our business: [2-3 sentence description]. Planning horizon: [TIMEFRAME].
>
>1. Identify the 2 most important and most uncertain external forces affecting us (not things we control).
>2. Build a 2x2 scenario matrix from those forces: name each quadrant with a vivid, neutral label.
>3. For each scenario, describe a day-in-the-life of our company in 5 sentences.
>4. List which current strategies succeed in ALL four scenarios (robust bets) versus only one or two (fragile bets).

- **Purpose:** Classic scenario planning that separates robust strategies from scenario-dependent ones.
- **Why it works:** The 2x2 structure forces genuinely different futures rather than three versions of the same outlook.
- **Use Case:** Annual strategy offsites, long-range planning, board discussions.
- **Expert Variation:**
>Add early indicators per scenario (what would we read, hear, or measure first?) and assign an owner and a review date to each indicator.

**Limitations & verification:** Scenario quality depends on the honesty of your uncertainty framing. If your "most uncertain force" is actually settled internally, the exercise produces theater. Validate the forces with people outside the strategy team.

***

## 2. Pre-Mortem

**Prompt:**
>It is [DATE, 12 months from now]. Our project [PROJECT NAME] has failed completely. Working backward, write the story of what went wrong.
>
>Structure the post-mortem:
>1. The 3 most probable causes of failure, ranked
>2. For each: the early warning signs that were available but ignored
>3. The decisions that looked reasonable at the time but contributed
>4. Close with: the 3 cheapest things we could do NOW to prevent the top cause

- **Purpose:** Failure-mode imagination before commitment, when prevention is still cheap.
- **Why it works:** Framing failure as already-happened defeats the optimism bias that afflicts planning discussions.
- **Use Case:** Project kickoffs, major launches, organizational changes.
- **Expert Variation:**
>Run the same exercise from the perspective of our most vocal internal skeptic and our most demanding customer. Merge the failure lists and deduplicate.

**Limitations & verification:** Pre-mortems surface plausible failure modes, not probabilities. Use them to generate your risk register, then estimate likelihoods with data wherever it exists.

***

## 3. Risk Register Drafting

**Prompt:**
>Draft a risk register for [PROJECT/DECISION]. Context: [scope, stakeholders, timeline, dependencies].
>
>For each risk, provide:
>- Risk statement in the form: "Because of [cause], [event] may occur, resulting in [impact]"
>- Category (strategic, operational, financial, compliance, reputational)
>- Likelihood and impact as Low/Medium/High, with a one-line rationale each
>- Mitigation (action to reduce likelihood) and contingency (plan if it occurs anyway)
>- Owner role (not a name — I will assign people)
>
>Include at least 2 risks a novice would miss (e.g., key-person dependency, single-supplier concentration, regulatory change).

- **Purpose:** A complete first-draft register that a team can argue with, correct, and adopt.
- **Why it works:** The cause-event-impact grammar prevents vague "risks" that are actually just worries.
- **Use Case:** Project governance, vendor selection, new market entry.

**Limitations & verification:** Likelihood ratings from a model are pattern-based guesses, not statistics. Replace them with historical data or expert judgment during review; keep only the register structure.

***

## 4. Black Swan Exposure Scan

**Prompt:**
>List the assumptions our business model depends on that would sound absurd if questioned 5 years ago but sound safe today. Context: [business model description]. Then, for each: what would break first if the assumption reversed, and how quickly would we notice?

- **Purpose:** Surfacing the invisible assumptions that normal risk registers skip.
- **Why it works:** Inverts the question — not "what could go wrong" but "what are we sure about that we shouldn't be."
- **Use Case:** Annual strategy reviews, portfolio companies, long-term contracts.
- **Expert Variation:**
>For the 2 most consequential assumptions, design a cheap hedge or an early-abort trigger, and state the maximum you would pay for that protection.

**Limitations & verification:** The model can list generic "unknown unknowns" categories but has no access to your industry's specific fragilities. Bring in operators with scar tissue for this one; use the prompt as the warm-up.

***

## 5. Decision Journal Entry

**Prompt:**
>Help me write a decision journal entry. Decision: [describe what was decided and by whom]. Alternatives considered: [list]. Key uncertainty at decision time: [describe].
>
>Write the entry with these sections:
>1. What we expect to happen, and by when — as falsifiable predictions
>2. What would make us conclude we were wrong
>3. Confidence level (high/medium/low) and what drives it
>4. What information we chose not to gather and why
>
>Do not editorialize about whether the decision was good.

- **Purpose:** Capturing decision context while it is fresh, enabling honest review later.
- **Why it works:** Falsifiable predictions create accountability that memory quietly destroys.
- **Use Case:** Major investments, strategy pivots, senior hires.
- **Expert Variation:**
>Schedule the review: propose check-in dates matched to each prediction's deadline, and draft the review questions now while no one knows the outcome.

**Limitations & verification:** The value comes from the discipline, not the document. An unreviewed decision journal is a diary; set the calendar reminders at entry time.

***

## 6. Crisis Simulation Tabletop

**Prompt:**
>Run a tabletop exercise. Scenario: [CRISIS, e.g., our payment processor goes down for 48 hours during peak season]. Roles at the table: [list, e.g., CEO, ops lead, comms lead, support lead].
>
>Simulate the first 6 hours in 3 moves:
>- Move 1: immediate decisions each role must make in the first hour
>- Move 2: the second-order problems that emerge by hour 3
>- Move 3: the communication decisions — customers, staff, public — with draft holding statements
>End with: the 3 gaps this simulation revealed in our preparedness.

- **Purpose:** Practicing crisis coordination when the stakes are zero.
- **Why it works:** Structured role simulation surfaces handoff and information gaps that org charts hide.
- **Use Case:** Business continuity planning, incident response preparation.

**Limitations & verification:** Simulations compress and simplify; real crises add stress, incomplete information, and politics. Treat revealed gaps as real, but treat the timeline as optimistic.

***

## Shared Verification Rules for All Risk Prompts

1. **Probability estimates are the model's weakest output.** Use its structure and imagination; supply the likelihoods yourself or from data.
2. **Risk work is confidential by nature.** Vulnerability and concentration details should stay within approved enterprise tools (see repository privacy guidance).
3. **A risk register nobody owns is a wish list.** Every adopted mitigation needs a named human and a date — assign them in the meeting, not after.
4. **Scenarios are for decision quality, not prediction.** The test of good scenario work is whether robust strategies were identified, not whether any scenario "came true."
