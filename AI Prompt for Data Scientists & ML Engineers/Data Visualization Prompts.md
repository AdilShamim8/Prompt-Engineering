# Data Visualization Prompts

Companion prompts to the main DS/ML guide for charts that inform rather than decorate: choosing the right encoding, designing for the question, avoiding the standard chart mistakes, and making figures that survive being screenshot out of context.

***

## 1. Chart Selection by Question

**Prompt:**
```
Act as a data visualization designer. My question: [THE QUESTION THE CHART MUST
ANSWER]. Data shape: [variables, types, cardinality, time range if temporal].
1. Recommend the chart type — and defend it: what this encoding makes easy to see.
2. Name the runner-up chart type and the question IT would answer better — so I
   can notice if I asked the wrong question.
3. Flag chart types I might reach for that would mislead with this data shape.
4. Provide matplotlib/seaborn code with correct, labeled axes; no defaults left
   unexamined (bin count, baseline, aspect ratio).
```

- **Purpose:** Choosing encodings that answer the actual question.
- **Why it works:** The runner-up question exposes the mismatch between chart and intent before the chart ships.
- **Use Case:** EDA, reporting, stakeholder decks.
- **Expert Variation:**
```
Add the small-multiples version: how would this chart change if I needed to show
[GROUPING VARIABLE] as well, and when is faceting better than encoding it in
color?
```

***

## 2. Honesty Audit of an Existing Chart

**Prompt:**
```
Audit this chart description for honesty problems: [describe the chart, or paste
the plotting code]. Check:
1. Axis games: truncated baselines, inverted axes, mismatched scales on dual axes
2. Proportion sins: 3D pie charts, area encodings on 1D data, inconsistent units
3. Sampling tricks: cherry-picked windows, smoothed-over anomalies, aggregated
   away variance
4. Annotation bias: labels that editorialize beyond what the data shows
5. Missing context: no sample size, no uncertainty, no definition of what a
   "point" is
Output: Issue | Severity (misleads/confuses/cosmetic) | Fix.
```

- **Purpose:** Catching the difference between "technically true" and "honestly displayed."
- **Why it works:** The severity tiers separate real deception from mere ugliness, so fixes get prioritized correctly.
- **Use Case:** Reviewing others' charts, cleaning up one's own older work.
- **Expert Variation:**
```
Reproduce the chart in its most honest form given the same data, listing every
judgment call where honesty and clarity pulled in different directions.
```

***

## 3. Distribution Visualization Done Right

**Prompt:**
```
I need to show the distribution of [VARIABLE] for [AUDIENCE/PURPOSE]. Data:
[n, range, known skew/outliers].
1. Compare the candidate encodings for THIS data: histogram (bin sensitivity?),
   box plot (hides multimodality?), violin (smoothing artifacts?), ECDF (harder
   to read — worth it?), strip/swarm (overplotting at my n?).
2. Recommend one and defend the choice against the data's specific pathologies.
3. Generate the code with: sample size annotated, outliers visible not clipped,
   and bin count chosen by a stated rule rather than default.
4. If my variable is clustered by [GROUP], show the per-group comparison without
   the pitfalls of side-by-side violins.
```

- **Purpose:** Distributions are where default settings lie most fluently.
- **Why it works:** Each candidate encoding is evaluated against the data's actual pathologies rather than in the abstract.
- **Use Case:** EDA reporting, SLA discussions, model residual checks.
- **Expert Variation:**
```
Add a log-scale variant with guidance: when does my variable's skew make log
display more honest, and how do I label it so the audience notices?
```

**Limitations & verification:** Always look at the rendered chart — generated code that runs can still produce visually wrong output (overplotted points, clipped axes) that only eyes catch.

***

## 4. Time Series Display Discipline

**Prompt:**
```
Help me display this time series honestly: [describe data, frequency, gaps, any
known events]. Audience: [WHO]. Message: [WHAT THE READER SHOULD TAKE AWAY — if
any].
1. How to handle the gaps and irregular sampling (interpolation disclosure? gap
   markers?).
2. Seasonality: should I show raw, de-seasonalized, or both — and how to label
   which is which so no one is deceived?
3. Scale traps: what does truncating the y-axis exaggerate here, and when is a
   truncated axis still the right call?
4. Event annotation: where do genuine events belong, and how to mark them
   without implying causation.
5. Generate the code with all choices made explicit as commented judgment calls.
```

- **Purpose:** Time series charts are the most screenshot—and the most abused—figures in business.
- **Why it works:** Treats every display choice (gaps, scales, smoothing) as a disclosed judgment call.
- **Use Case:** Operational dashboards, exec reviews, incident write-ups.
- **Expert Variation:**
```
Design the "out of context" test: how should this chart be titled and labeled so
that it remains truthful if cropped and shared without the surrounding prose?
```

***

## 5. Dashboard Tile Design

**Prompt:**
```
Design one dashboard tile for [METRIC]. Consumer: [ROLE — e.g., support lead,
weekly, 30 seconds of attention]. Decisions it feeds: [WHICH DECISIONS].
1. The tile's single question, phrased as the consumer would ask it.
2. Encoding choice for 30-second comprehension — and what gets cut to achieve it.
3. The context the tile needs inline (target/benchmark, sample window, minimum
   count) so it cannot mislead when read alone.
4. The drill-down path: what does the consumer click to answer the obvious
   follow-up question?
5. Write the tile's honest caption: what this number is, is not, and how often
   it refreshes.
```

- **Purpose:** Tiles that support decisions instead of decorating walls.
- **Why it works:** The 30-second attention budget forces ruthless prioritization, and the caption prevents the tile from being over-read.
- **Use Case:** Ops dashboards, metric standardization programs.
- **Expert Variation:**
```
Add the failure modes: the 3 ways this tile could show green while the underlying
reality is degrading, and what second tile guards against each.
```

***

## 6. Accessibility & Perception Basics

**Prompt:**
```
Review my chart design for perception and accessibility: [paste code or describe:
colors, sizes, channel choices]. Check:
1. Color: is information carried ONLY by hue (fails for colorblind readers and
   grayscale printing)? Suggest redundant encodings.
2. The palette: is it perceptually ordered where the data is ordered?
3. Pre-attentive attributes: is the most important element the most visually
   salient, or is it competing with gridlines and legends?
4. Text: label sizes, contrast, and whether direct labeling can replace the
   legend entirely.
5. Cognitive load: how many distinct visual elements must the reader track to
   get the message?
```

- **Purpose:** Charts that work for every reader, including the ones you did not picture.
- **Why it works:** Grounds design taste in testable perception failures.
- **Use Case:** Public-facing figures, org-wide dashboards, print collateral.
- **Expert Variation:**
```
Produce two variants of my chart: one optimized for the presentation screen
(dark background) and one for the printed handout (grayscale-safe), with the
redundant encoding applied to both.
```

***

## Shared Verification Rules for All Visualization Prompts

1. **Render and look.** Generated plotting code must be executed and the output inspected — visual bugs (overplotting, clipping, label collisions) are invisible in code review.
2. **Every chart answers a question.** If you cannot state the question, the chart is decoration; delete it or find the question.
3. **Screenshot survival test.** Assume the chart will travel without its context; titles, units, sample sizes, and caveats must be self-contained.
4. **Check the numbers on the axes.** Generated charts occasionally mislabel or mis-scale; verify tick values against the source data before shipping.
