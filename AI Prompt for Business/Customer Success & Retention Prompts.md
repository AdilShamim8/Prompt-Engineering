# Customer Success & Retention Prompts

Companion prompts to the main business guide for keeping the customers you already have — analyzing feedback, running health reviews, intervening before churn, and recovering from service failures. Retention work depends on real customer data; these prompts help you think with it, not replace it.

***

## 1. Churn Signal Review

**Prompt:**
>Act as a customer success analyst. Here is usage and account data for [N] at-risk or recent accounts: [paste table: account, tenure, plan, usage trend, support tickets, last contact].
>
>1. Group the accounts by churn pattern (e.g., declining engagement, unresolved pain, silent drift, price pressure).
>2. For each pattern: the most likely underlying cause and the intervention with the best odds.
>3. Rank all accounts by urgency × recoverability — who to call today, this week, this month.
>4. List what this data CANNOT tell us about churn — the questions I need answered by a human conversation.

- **Purpose:** Turning account data into a prioritized save list instead of a wall of numbers.
- **Why it works:** Pattern grouping before intervention prevents one-size-fits-all outreach.
- **Use Case:** Quarterly retention reviews, QBR preparation, at-risk escalations.
- **Expert Variation:**
>For the top 3 accounts, draft the opening message for a save conversation — specific to their pattern, no template smell, one clear next step.

**Limitations & verification:** Churn is decided by humans with context your data lacks (budget cycles, leadership changes). Treat the ranking as a starting hypothesis; the model cannot know which "healthy" account just got a new CFO.

***

## 2. Feedback Synthesis Across Channels

**Prompt:**
>Synthesize customer feedback from these sources for [PERIOD]: [paste NPS verbatims / support tickets / sales call notes / review-site excerpts].
>
>1. Separate: what customers literally said (quotes, grouped) versus what we infer (interpretations, labeled).
>2. The 5 most frequent themes, each with: representative quotes, affected segment if visible, and trend versus last period if prior data is included.
>3. Themes that appear in ONE channel only — these often indicate channel bias, not customer truth.
>4. One page maximum: what leadership needs to know, what we recommend, what we still don't know.

- **Purpose:** One honest picture from many noisy sources.
- **Why it works:** The said-versus-inferred discipline is the difference between evidence and editorial.
- **Use Case:** Voice-of-customer reports, product council inputs, board summaries.
- **Expert Variation:**
>Add a "cost of silence" estimate per theme: for the top 3, what would churn/effort look like if we fixed it, based on the data provided — with the assumptions shown.

**Limitations & verification:** Quote fidelity matters — spot-check that quotes in the output are verbatim from the input. Any volume or percentage claims must be recomputed from the raw data.

***

## 3. Service Failure Recovery Plan

**Prompt:**
>We failed a customer: [describe what happened, when, who was affected, current state]. Draft a recovery plan.
>
>1. Customer communication: one message that acknowledges specifically, takes responsibility without legal overreach, states the fix and the safeguard. 120 words max.
>2. Internal sequence: who does what in the next 24 hours, in order.
>3. The proportionality check: is this response proportionate, over-the-top, or insufficient for the failure described?
>4. The follow-through: what we commit to and how we will verify we kept it — dated.
>5. What NOT to say: 3 tempting phrases that would make it worse (e.g., unearned apologies, blaming vendors, premature root-cause claims).

- **Purpose:** Recovering trust after failure with speed and proportion.
- **Why it works:** The proportionality check and "what not to say" guard against the twin failures of groveling and minimizing.
- **Use Case:** Outages, missed commitments, quality escapes, billing errors.
- **Expert Variation:**
>Draft the 30-day follow-up message that proves the safeguard actually shipped — the message most companies never send and trust never recovers without.

**Limitations & verification:** Contractual and legal exposure varies — run externally facing language past legal or your escalation policy for material failures. The customer's account manager must own the send, not a committee.

***

## 4. Health Score Design

**Prompt:**
>Help me design a customer health score. Our product: [TYPE]. What we can measure: [usage events, support signals, contract data, engagement touchpoints]. What we know predicts churn from experience: [list, even if informal].
>
>1. Propose 5-7 components, each with: definition, direction (more is healthier or unhealthier), and why it should correlate with retention.
>2. Flag which components are leading indicators versus lagging.
>3. Suggest weights as a starting point — then explain what evidence would make us change them.
>4. Define the score's failure mode: what would make this score systematically wrong (e.g., seasonal usage, power-user noise, small-sample accounts)?

- **Purpose:** An early-warning system built from the signals you actually have.
- **Why it works:** Explicit component reasoning makes the score debatable and improvable — a black-box score helps no one.
- **Use Case:** CS operations build-outs, renewal forecasting, segmentation.

**Limitations & verification:** Weights and thresholds are hypotheses until back-tested against actual churn history. Validate with at least a few quarters of labeled outcomes before letting the score drive resource allocation.

***

## 5. Renewal Conversation Preparation

**Prompt:**
>Prepare me for a renewal conversation with [ACCOUNT]. History: [tenure, outcomes, usage, past issues, current stakeholder map]. Objective: [renew / expand / graceful terms].
>
>1. Their likely position: value received, doubts, and the internal case they must make to their leadership.
>2. My value narrative: 3 specific outcomes with evidence, phrased in their terms.
>3. The 3 objections I should expect, each with a response that is honest about our weaknesses.
>4. Two paths: one if momentum is positive, one if they raise leaving — both ending in concrete next steps.
>5. The one question I should ask that opens up what they have not said.

- **Purpose:** Walking into renewals with the customer's perspective prepared, not just our pitch.
- **Why it works:** Requiring "honest about our weaknesses" produces answers that survive contact with a skeptical buyer.
- **Use Case:** CS renewal cycles, account expansion planning, save plays.
- **Expert Variation:**
>Draft the pre-renewal value summary email (150 words, evidence-first) to send two weeks before the conversation.

**Limitations & verification:** Renewal outcomes hinge on stakeholder politics the model cannot see. Confirm your stakeholder map with recent interactions before relying on the plan.

***

## 6. Win/Loss Debrief Analysis

**Prompt:**
>Analyze these win/loss notes from [PERIOD]: [paste sales or CS notes]. For each loss, note the stated reason versus the plausible real reason where they differ.
>
>1. Frequency table of stated reasons (price, features, timing, incumbent, other).
>2. Where the notes suggest deeper causes: pattern, evidence quoted, confidence (high/medium/low).
>3. Which losses were preventable versus not — with the reasoning shown.
>4. The one question our sales/CS process should start asking in every debrief to make the next quarter's analysis better.

- **Purpose:** Learning from losses honestly instead of defaulting to "price."
- **Why it works:** The stated-versus-real distinction addresses the core epistemic problem of win/loss data.
- **Use Case:** Quarterly revenue reviews, positioning adjustments, product roadmap inputs.

**Limitations & verification:** Loss reasons recorded by the losing team are notoriously self-serving. Where stakes are high, invest in third-party or buyer-side interviews before changing strategy on the analysis.

***

## Shared Verification Rules for All Customer Success Prompts

1. **Customer-identifying data is sensitive.** Anonymize accounts in prompts where possible, and keep detailed customer records in your CRM and approved systems (see repository privacy guidance).
2. **Recompute every statistic.** Frequencies, percentages, and trends from AI output must be recounted from the source data before circulating.
3. **The model meets neither your customers nor your team.** Interventions, tone, and timing decisions belong to the humans holding the relationships.
4. **Never send AI-drafted customer communications unedited.** They are skeletons for your voice, not finished messages — customers recognize template language faster than you think.
