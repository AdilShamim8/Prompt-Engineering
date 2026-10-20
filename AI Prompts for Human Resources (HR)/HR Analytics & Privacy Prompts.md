# HR Analytics & Privacy Prompts

Companion prompts to the main HR guide for the measurement layer of people work: building people analytics that answer real questions, reading attrition and hiring data honestly, and — above all — doing it within the privacy and ethics boundaries that distinguish people analytics from surveillance. The main guide's CARE framework applies here in its strongest form.

***

## 1. The Question Before the Dashboard

**Prompt:**
```
Act as a people analytics advisor. Leadership wants "HR dashboards."
The actual decisions they're trying to make: [LIST — e.g., where to
invest in retention, whether hiring velocity supports the growth plan].
1. For each decision: the question restated precisely, the metric that
   would inform it, and — critically — whether that metric is even
   measurable with our data (name what's missing).
2. The vanity-metric filter: which classic HR metrics (aggregate
   engagement score, total headcount, applications received) would NOT
   answer any real question here — and would consume attention while
   informing nothing.
3. The minimum viable dashboard: the 4-6 metrics that actually serve
   the stated decisions, each with: definition, source, refresh cadence,
   and the decision it feeds.
4. The measurement-honesty rules: small-n suppression (no metrics shown
   for groups under [N=8]), and segment boundaries that prevent
   re-identification through slicing.
```

- **Purpose:** Analytics built backward from decisions, not forward from available data.
- **Why it works:** The vanity-metric filter and minimum-viable-dashboard discipline attack the standard failure: a dashboard built because data existed, consuming attention while answering nothing.
- **Use Case:** HR analytics programs; leadership reporting; tool selection.
- **Expert Variation:**
```
Add the metric lifecycle: for each metric, when it should be RETIRED —
decisions change, and metrics that outlive their decisions become
cargo-cult dashboards.
```

***

## 2. Attrition Analysis (Honest Version)

**Prompt:**
```
Analyze our attrition honestly. Data available: [LEAVERS by quarter,
role, tenure, performance where held; plus context — reorgs, market
events, comp changes].
1. The decomposition: attrition by tenure band, by team/function, by
   performance tier (where ethically permitted) — showing which cut
   explains the most variance, not just which is easiest to compute.
2. The base-rate discipline: which "spikes" are actually normal
   variation? Apply basic significance thinking before anyone reacts
   to a number.
3. The regrettable distinction: separating regretted from non-regretted
   attrition — total attrition treats great losses and healthy turnover
   as identical, which makes the metric actively misleading.
4. The cause hypotheses: for genuine patterns, the testable explanations
   (comp drift, manager changes, workload, career ceilings) — and the
   data that would distinguish them from stories.
5. The ethical boundary: what this analysis must NOT become — individual
   flight-risk scoring and manager-shaming leaderboards flagged as
   misuse explicitly.
```

- **Purpose:** Attrition insight without attrition theater or surveillance drift.
- **Why it works:** The regrettable/non-regrettable split and base-rate discipline are the two analytical habits that separate useful attrition work from reactive number-flailing.
- **Use Case:** Retention strategy; board reporting; post-reorg assessment.
- **Expert Variation:**
```
Add the stay-interview design: for the teams where patterns concentrate,
the structured conversations that surface causes the data cannot —
conducted before people become leavers.
```

**Limitations & verification:** Verify all counts and rates from the HR system of record; small-group suppression is mandatory (patterns in groups under ~8 are usually noise AND are re-identifiable).

***

## 3. Hiring Funnel Analysis

**Prompt:**
```
Analyze our hiring funnel. Stage data: [APPLICANTS → SCREEN → INTERVIEW →
OFFER → ACCEPT → 90-DAY RETAINED, by role family and period].
1. The conversion map: where the funnel actually loses candidates, with
   the biggest constraint stage named (the one bottleneck that, fixed,
   changes the outcome most).
2. The stage-efficiency questions: is our screen rejecting people who
   would have passed later stages? Are offers declining at a rate that
   signals comp or process problems?
3. The equity audit: conversion rates by demographic group at each
   stage — with the statistical honesty of small-n flagging, and the
   explicit note that disparities are findings to investigate
   (bias in process, sourcing, or criteria), not conclusions.
4. The quality loop: 90-day retention and early performance of hires
   by source and stage-passing-profile — closing the loop from
   "filled the req" to "hired well".
5. What this data cannot tell me: the candidates who never applied
   (employer brand, market), and the ones our process discouraged
   silently.
```

- **Purpose:** A hiring process understood as a system with measurable behavior.
- **Why it works:** The constraint-stage logic (fix the bottleneck, not everything) and the quality loop (retention, not just fills) reflect how funnels actually improve.
- **Use Case:** Recruiting operations; DEI monitoring (with care); growth planning.
- **Expert Variation:**
```
Add the candidate-experience overlay: where in OUR funnel do candidates
report friction, and where does that correlate with declined offers —
the link between experience and outcome.
```

**Limitations & verification:** Demographic analysis for fairness purposes follows legal guidance (what may be collected and when varies by jurisdiction) — coordinate with counsel on the equity audit's design before running it, and treat all demographic data with maximum access restriction.

***

## 4. Privacy-by-Design for People Analytics

**Prompt:**
```
Review our planned people-analytics project for privacy and ethics:
[DESCRIBE THE PROJECT — data involved, population, questions, who sees
outputs].
1. The necessity test: for each data element, which analysis question
   requires it? Flag everything collected because it was available
   rather than needed.
2. The minimization pass: aggregation levels, suppression thresholds
   (groups under [N]), and retention limits that make re-identification
   impractical — with special rigor for small teams and intersectional
   slices.
3. The purpose-creep audit: what else could this data or dashboard be
   used for once it exists? Name the realistic misuse (individual
   monitoring, manager surveillance) and the governance that prevents
   it.
4. The consent and transparency questions: do employees know this data
   is analyzed? What does our jurisdiction and works-council/employee-
   representation context require?
5. The employee-impact test: if this analysis's existence were fully
   disclosed to the people analyzed, would it feel fair? That feeling
   is a legitimate design requirement, not an inconvenience.
```

- **Purpose:** Analytics infrastructure that employees would find fair if they saw it fully.
- **Why it works:** The "disclosed, would it feel fair?" test operationalizes the ethics that regulations only approximate — and catches the projects that are technically compliant and culturally corrosive.
- **Use Case:** Before any new analytics initiative; annual review of existing ones.
- **Expert Variation:**
```
Add the governance charter: who may request what analyses, the approval
path for sensitive ones, and the sunset rule for datasets and dashboards
that outlive their purpose.
```

**Limitations & verification:** Employee data processing is regulated (GDPR and equivalents, works-council agreements, sector rules) — the privacy officer or counsel defines the binding requirements; this review structures the compliance and ethics conversation, never replaces it.

***

## 5. Survey Design & Honest Reading

**Prompt:**
```
Design our people survey — or audit the one we have: [CURRENT/PAST
SURVEY STRUCTURE + any results].
1. The question audit: leading questions, double-barreled items, scale
   problems (odd/even, unlabeled points), and questions whose answers
   we cannot act on (asking without acting destroys future response
   rates).
2. The anonymity engineering: how anonymity is actually protected
   (aggregation thresholds, demographic minimums, timing) — and how we
   communicate that protection so people believe it.
3. The action loop: for each theme area, what leadership can and will
   do with results — surveys without visible action are trust
   extraction.
4. The honest reading of results: participation-rate caveats,
   nonresponse bias (who stopped answering, and why that matters more
   than the scores), and the trend-over-snapshot discipline.
```

- **Purpose:** Surveys that measure honestly and keep the permission to keep asking.
- **Why it works:** "Asking without acting destroys response rates" is the survey discipline most organizations learn empirically and expensively.
- **Use Case:** Engagement surveys; pulse checks; exit surveys (adapted).

***

## 6. Analytics Storytelling for Leadership

**Prompt:**
```
Turn this people-analytics finding into a leadership-ready narrative:
[THE FINDING + ITS UNCERTAINTY + THE DECISION IT SHOULD INFORM].
1. The headline: the finding and its confidence in one sentence —
   uncertainty stated upfront, not buried.
2. The "so what": what decision this changes, and what it would cost
   to ignore it.
3. The nuance layer: the two most likely alternative explanations, and
   why the finding survives them (or doesn't).
4. The guardrails: small-n caveats, correlation-not-causation flags,
   and what we do NOT yet know — stated in leadership language that
   respects their intelligence.
5. The follow-up: the next analysis that would strengthen or kill
   this finding, with a timeline.
```

- **Purpose:** Analytics communication that informs decisions without overclaiming.
- **Why it works:** The alternative-explanations layer and upfront uncertainty build the credibility that lets findings actually drive action — overclaimed findings get discovered and then nothing gets believed.
- **Use Case:** Leadership reviews; board packets; analytics function credibility-building.

***

## Shared Verification Rules for All Analytics Prompts

1. **Anonymize before prompting — always.** People analytics works with the most sensitive data class in any organization: patterns and aggregates only in AI tools, source data in approved systems (the main guide's privacy rules at full strength).
2. **The privacy officer defines the boundaries.** Regulations, works-council agreements, and internal governance override any prompt's convenience — when they conflict, governance wins, every time.
3. **Suppression thresholds are non-negotiable.** Metrics for groups under ~8 people are statistical noise and re-identification risks simultaneously — publish neither.
4. **Analytics serves employees, not surveillance.** The test is disclosure fairness: work that employees would not find fair if fully revealed is not made acceptable by being technically compliant.
