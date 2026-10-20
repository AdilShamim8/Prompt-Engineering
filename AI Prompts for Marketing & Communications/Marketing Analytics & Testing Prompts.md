# Marketing Analytics & Testing Prompts

Companion prompts to the main marketing guide for the measurement layer: experiment design, attribution honesty, dashboard sense, and reading results without fooling yourself. Marketing analytics is where enthusiasm meets statistics — these prompts keep the meeting civilized.

***

## 1. Experiment Design (Before Touching Data)

**Prompt:**
```
Act as an experimentation advisor. Hypothesis: [e.g., "Changing our CTA
from X to Y will increase signups"]. Current baseline: [METRIC + RATE].
Traffic/volume: [PER PERIOD]. Constraints: [TECH, TIMELINE].
1. The hypothesis sharpened: mechanism stated — WHY would this change
   move the metric? (No mechanism, no test worth running.)
2. The math check: is our volume sufficient to detect a [EXPECTED EFFECT
   SIZE] change? Show the power reasoning — and if we can't detect it,
   say so before we burn two weeks.
3. The design: unit of randomization (user vs session — and the
   contamination risks of each), required duration including full
   business cycles (minimum one full week to capture day-of-week), and
   one-metric discipline: primary metric named, guardrails listed.
4. The pre-registration: success criterion fixed NOW, in writing —
   including what result makes us ship, iterate, or kill.
5. The validity threats: novelty effects, seasonality, interleaving
   with other campaigns, and the peeking rule (no early stopping
   without a sequential design).
```

- **Purpose:** Tests designed before the data arrives, with the discipline that makes results trustworthy.
- **Why it works:** The mechanism requirement and pre-registered criteria kill the two great testing sins: testing trivia and moving goalposts after results.
- **Use Case:** A/B and A/B/n tests; pricing experiments; channel tests.
- **Expert Variation:**
```
Add the downside asymmetry check: what is the cost of a false positive
(shipping a worse winner) versus a false negative (missing a good
idea)? The ratio should set our significance threshold and test
direction.
```

**Limitations & verification:** Power calculations from a model are approximations — recompute with a proper sample-size calculator, and respect platform-specific experiment requirements where you test on rented land (ad platforms often govern their own experiments).

***

## 2. Attribution Honesty Session

**Prompt:**
```
Our attribution story: [PASTE CURRENT MODEL/SOURCED CLAIMS — e.g., "last-
click says X, platform dashboards say Y, our MMM says Z"]. Actual
questions leadership asks: [WHICH CHANNELS DRIVE REVENUE, WHAT SHOULD
WE CUT].
1. The frame-up: why the models disagree — the structural reason each
   attribution model (last-click, multi-touch, platform-reported,
   incrementality-based) tells a different truth, without jargon.
2. The overlap audit: where platform-reported conversions double-count
   the same human — and the magnitude of the disagreement between
   dashboards that should alarm us.
3. The honest hierarchy: for each decision type (budget cut, scale-up,
   creative kill), which evidence is decision-grade versus directional
   — and what incrementality test would upgrade the critical ones.
4. The communication version: how to present attribution to leadership
   without false precision — ranges and confidence instead of decimal
   points that imply knowledge we lack.
```

- **Purpose:** Attribution treated as inherently uncertain evidence, not a spreadsheet oracle.
- **Why it works:** The "structural reason models disagree" framing converts dashboard conflicts from a mystery into a known property of measurement — which is the actual starting point of honest budgeting.
- **Use Case:** Budget cycles; platform dashboard chaos; marketing-mix reviews.
- **Expert Variation:**
```
Design the incrementality check: the geo-based or holdout test that
would settle our biggest attribution dispute — cost, duration, and the
decision it would actually change.
```

***

## 3. Campaign Readout (No Self-Congratulation)

**Prompt:**
```
Campaign readout, honest version. The campaign: [GOALS, TARGETS, SPEND,
CREATIVE/CHANNEL MIX]. Results: [METRICS + BASELINE COMPARISON].
1. Against target, plainly: hit / missed / exceeded — each with the
   number, before any narrative.
2. The baseline discipline: compared to WHAT? (Prior period, control,
   forecast, last year's comparable?) Flag any "success" defined
   against no baseline at all.
3. The confessional: what else changed during the campaign window
   (season, PR events, competitor moves, site changes) that could
   explain the numbers — honestly weighted.
4. The decomposition: which creative/channel/audience carried, which
   dragged — and the confidence level on each read, given cell sizes.
5. The decision output: continue / iterate / kill — with the next
   experiment each implies, so the readout feeds the testing loop
   instead of the slide archive.
```

- **Purpose:** Readouts that improve decisions rather than decorate them.
- **Why it works:** The against-target-before-narrative ordering prevents the standard readout failure: a wall of selective framing around a number never plainly stated.
- **Use Case:** Campaign post-mortems; agency reviews; channel investment cases.
- **Expert Variation:**
```
Add the pre-mortem audit: what did we predict for this campaign before
launch, and where were we wrong? Prediction-versus-outcome tracking is
how marketing judgment compounds.
```

***

## 4. Dashboard Sense-Making

**Prompt:**
```
Our dashboard shows: [PASTE/DISCRIBE — METRICS, MOVEMENTS, TIME WINDOWS].
1. The real-change triage: which movements exceed normal fluctuation?
   (Apply basic control-limit thinking: what does week-over-week noise
   normally look like for each metric?)
2. The metric-relationship check: which movements are mechanically
   linked (impressions up + CTR down = usual auction dynamics, not two
   separate stories) — collapse the redundant explanations.
3. The investigation routes: for each genuine anomaly, the two most
   likely causes and the cheapest query that distinguishes them.
4. The dashboard critique: which metrics on here answer no decision —
   and which decision has no metric serving it? Propose the swap.
```

- **Purpose:** Turning dashboard-watching into signal detection.
- **Why it works:** Normal-fluctuation baselines and mechanical-link awareness are the two habits that separate analysts from dashboard-starers.
- **Use Case:** Weekly reviews; anomaly triage; dashboard redesign.
- **Expert Variation:**
```
Add the automation plan: which anomaly checks deserve alerting (with
thresholds set from the noise baseline) versus scheduled review — so
detection runs without someone watching.
```

***

## 5. Cohort & Retention Analysis

**Prompt:**
```
Design our cohort analysis for: [PRODUCT/SERVICE + ACQUITION CONTEXTS].
Available data: [SIGNUPS, ACTIVITY/ORDERS BY COHORT, ACQUISITION SOURCE].
1. The cohort definition: by [START WEEK/MONTH + ACQUISITION SOURCE] —
   with the alignment decision (all cohorts measured on identical
   maturity windows).
2. The retention curve: cohort-by-cohort, with the questions that
   matter: does newer retention improve or decay? Where is the curve's
   elbow (the point of "stayed = staying")?
3. The source comparison: retention by acquisition channel — which
   sources bring people who STAY versus people who sample? (Cheap
   acquisition of churning cohorts is expensive.)
4. The segment honesty: minimum cohort sizes, and the refusal to read
   patterns in cells too small to support them.
5. The action translation: what this says about where to spend the next
   dollar — and what it cannot yet tell us.
```

- **Purpose:** Retention analysis that guides acquisition strategy rather than decorating a monthly deck.
- **Why it works:** Source-level retention ("which channels bring stayers") is the highest-leverage cohort cut and the one most analyses stop short of.
- **Use Case:** Growth reviews; channel budgeting; product-market fit monitoring.
- **Expert Variation:**
```
Add the LTV honesty check: with our cohort sizes and time-in-market,
which LTV claims are actually supportable versus extrapolated — and
the language that presents each appropriately.
```

***

## 6. The Marketing Data Governance Pass

**Prompt:**
```
Audit our marketing analytics stack for governance: [TOOLS, TRACKING
SETUP, DATA FLOWS — describe honestly].
1. The instrumentation audit: which events/params are reliably tracked,
   which fire inconsistently, which were deprecated but still "report" —
   and the tracking plan gaps where the data we cite does not match the
   data we collect.
2. The consent and privacy layer: how tracking respects consent choices
   and applicable regulations — flagged for the privacy/legal owner's
   review, not self-certified.
3. The definition registry: the metric definitions (a "conversion", an
   "active user") that different dashboards compute differently —
   the source of most "why don't these match" meetings.
4. The access hygiene: who can see customer-level data from marketing
   tools, and whether that matches policy.
5. The fix list, prioritized: the 5 corrections that most reduce
   decision-making error, with effort estimates.
```

- **Purpose:** Analytics infrastructure trustworthy enough to argue from.
- **Why it works:** The definition registry addresses the root cause of analytics theater: metrics whose meaning varies by who opens the dashboard.
- **Use Case:** New leadership inheriting a stack; periodic hygiene; post-migration validation.
- **Expert Variation:**
```
Add the sunset test: reports nobody reads and events nobody uses —
carrying maintenance and privacy surface for zero decision value.
Retirement list, please.
```

**Limitations & verification:** Privacy and consent compliance is a legal determination — this audit surfaces issues for the accountable owner; it never certifies compliance.

***

## Shared Verification Rules for All Analytics Prompts

1. **Recompute every number.** Rates, percentages, and cohort sizes from AI output are verified against source data before anyone presents them — transposition errors compound downstream.
2. **Platform dashboards self-report favorably.** Where ad platforms grade their own homework, treat their numbers as one claim among several, and triangulate with your own analytics and incrementality tests.
3. **Statistical claims get statistical scrutiny.** Sample sizes, confidence levels, and multiple-comparison risks checked before "significant" appears in any slide.
4. **Decisions, not dashboards.** Every analysis here ends in a decision or a next experiment — analysis that feeds nothing is an expense wearing a costume.
