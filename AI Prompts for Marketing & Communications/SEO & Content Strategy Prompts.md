# SEO & Content Strategy Prompts

Companion prompts to the main marketing guide for the search and content planning layer. One structural caveat before any of them: search behavior, algorithm factors, and AI-driven search features change constantly, so treat current search engine documentation and your own analytics as ground truth over any general guidance — including what a model tells you.

***

## 1. Search Intent Mapping

**Prompt:**
```
Act as a content strategist. Our business: [DESCRIBE]. Target audience:
[WHO]. Products/services: [LIST].
1. Map our keyword universe by intent stage: informational ("what is/
   how to"), comparison ("best X for Y", "X vs Y"), transactional
   ("pricing", "buy", "demo"), and navigational (brand terms).
2. For 10 priority queries per stage: the searcher's actual question,
   the content format that answers it best (guide / comparison table /
   calculator / product page), and where in our funnel it sits.
3. The intent mismatch flag: queries where our product page would be the
   WRONG answer (searchers want education, not a pitch) — ranking our
   homepage there would bounce.
4. The gap pass: intent stages where we have NO content answering the
   audience's questions — our competitors' FAQ pages are usually the
   map of what we're missing.
```

- **Purpose:** Content planned against what searchers actually want, not what we want to rank.
- **Why it works:** The intent-mismatch flag prevents the classic SEO failure: forcing commercial pages onto informational queries and wondering about bounce rates.
- **Use Case:** Content strategy; site architecture; editorial calendars.
- **Expert Variation:**
```
Add the question-mining layer: the 15 real questions our audience asks
(support tickets, sales calls, community threads — paste examples) that
no keyword tool surfaces, and the content each one deserves.
```

***

## 2. Content Brief That Ranks AND Reads

**Prompt:**
```
Create a content brief for: [TARGET QUERY + AUDIENCE + FUNNEL STAGE].
1. The brief essentials: primary query + 3-5 secondary queries woven
   naturally, the searcher's core question answered in the first 100
   words, and the format decision ([GUIDE/LIST/COMPARISON/CALCULATOR])
   with reasoning.
2. The outline: H2/H3 structure where each section answers a sub-question
   the searcher actually has — derived from the query, not from our
   product structure.
3. The differentiation requirement: what must this page do BETTER than
   what currently ranks — name the specific gaps in existing results
   (freshness, depth, tools, examples, clarity) that we can close.
4. The E-E-A-T layer: what first-hand experience, credentials, data, or
   original perspective goes in — generic AI-drafted text without these
   signals underperforms for quality-sensitive queries.
5. The internal linking plan: 3-5 existing pages to link from/to, with
   the anchor logic.
```

- **Purpose:** Briefs that produce content worth ranking.
- **Why it works:** The "better than what ranks" requirement forces genuine value creation — the only durable ranking strategy — instead of content-shaped objects.
- **Use Case:** Working with writers; scaling content production.
- **Expert Variation:**
```
Add the update clause: the maintenance plan for this page — what
refreshes it needs quarterly and which sections decay fastest (prices,
statistics, screenshots, tool names).
```

**Limitations & verification:** Query characteristics and ranking factors shift — validate priority queries against current search results and your Search Console data before committing an editorial calendar to them.

***

## 3. Content Audit & Pruning

**Prompt:**
```
Audit our content inventory: [PASTE — URLs with traffic, conversions,
top query, last-updated date].
1. The portfolio sort: KEEP (performs or serves strategy), UPDATE
   (declining but salvageable — name the likely decay cause), CONSOLIDATE
   (overlapping pages competing with each other — specify which merges
   into which), PRUNE (zero traction, no strategic role, and safe to
   remove or redirect).
2. The cannibalization check: pages competing for the same queries —
   which should own the term, which should cede and differentiate.
3. The quick-win list: pages where a title/meta/structure refresh has
   the best ratio of effort to expected return.
4. The pruning risk flags: pages with backlinks or serving conversions
   that LOOK prunable but are not — check before cutting.
```

- **Purpose:** A content library that earns its maintenance cost.
- **Why it works:** The four-way sort with named decay causes turns the paralyzing "audit everything" into an actionable disposition list.
- **Use Case:** Annual content audits; site migration prep; performance recovery.
- **Expert Variation:**
```
Add the decay forecast: which KEEP pages will slide into UPDATE within
a year based on their content type — and the scheduled refreshes that
prevent it.
```

***

## 4. Topic Cluster Architecture

**Prompt:**
```
Design our topic cluster architecture for: [CORE TOPIC the business
should own]. Audience: [WHO]. Existing assets: [LIST what we already
have].
1. The pillar page: what comprehensive means for THIS topic — the
   subtopics it must cover to be the definitive hub, and what it should
   deliberately delegate to cluster pages.
2. The cluster pages: 8-12 supporting pieces, each answering ONE
   sub-question deeply, with the internal link structure that makes
   the topical relationship legible to readers and crawlers.
3. The coverage sequencing: which cluster pieces first (existing demand
   + business priority), which later — a 6-month order.
4. The depth discipline: how cluster pages stay distinct instead of
   converging into five versions of the same article.
```

- **Purpose:** Content architecture that compounds authority instead of accumulating pages.
- **Why it works:** Explicit pillar/cluster delegation prevents the self-competition that kills most "content hubs".
- **Use Case:** New content programs; reorganizing existing sprawl.
- **Expert Variation:**
```
Add the authority-gap analysis: for the topically most important
queries, what the current winners have that we lack (links, tools,
original data, brand) — the honest build-versus-wait decision per
cluster.
```

***

## 5. SERP Feature & Format Strategy

**Prompt:**
```
For our priority queries: [LIST], design the format strategy:
1. For each: what the current results page actually rewards — featured
   snippets (definition-style answers?), video, "people also ask",
   AI-generated summaries — based on [paste what you see in current
   results, since only live SERPs tell the truth].
2. The snippet-capture structure: for snippet-eligible queries, the
   40-60 word direct answer, formatted to win the feature without
   becoming content-shaped-for-bots.
3. The PAA (People Also Ask) mapping: the follow-up questions our page
   should answer as sub-sections.
4. The honest AI-summary assessment: where AI overviews change the
   click calculus — which queries may lose clicks no matter what we
   do, and which still earn visits (transactional, comparison, tools,
   depth beyond the summary).
```

- **Purpose:** Format strategy matched to how results pages actually render today.
- **Why it works:** Insists on live-SERP evidence rather than model memory — the format layer changes too fast for anything else.
- **Use Case:** Format planning; snippet optimization; AI-era traffic strategy.
- **Expert Variation:**
```
Add the measurement adaptation: how we'll know if AI summaries are
eroding our clicks — the dashboards that separate impressions, position,
and click-through so we see erosion early instead of mystified.
```

**Limitations & verification:** Only the live results page reflects the live algorithm — the model's description of what "SERPs reward" is a starting hypothesis, not data. Check current results for every priority query.

***

## 6. Content-Data Flywheel

**Prompt:**
```
Design our content flywheel: turning our proprietary data/experience
into content assets competitors cannot copy.
Our assets: [WHAT WE UNIQUELY HAVE — customer patterns (anonymized),
pricing data, benchmark data, practitioner experience, tools].
1. The original-data opportunities: 3-5 assets (reports, calculators,
   benchmark pages, surveys) built on what only we can show.
2. The packaging ladder: each dataset as (a) a headline statistic for
   PR and social, (b) an in-depth page for search, (c) a downloadable
   for lead capture — one research effort, three assets.
3. The refresh economics: which data assets justify annual updates
   (link equity + citation magnetism compounds), and which are
   one-time.
4. The privacy and ethics gates: anonymization thresholds and
   aggregation rules before any customer-derived data sees daylight —
   [DEFINE OUR RULES: e.g., no segments under N=8, no re-identifiable
   patterns].
```

- **Purpose:** The only sustainable content advantage: things only we can publish.
- **Why it works:** Original data earns links and citations the way commodity content cannot — and the packaging ladder multiplies return per research effort.
- **Use Case:** Differentiation strategy; PR/link building; lead generation.
- **Expert Variation:**
```
Add the citation-bait audit: which of our existing data points get
referenced already (search for them), and how the next report makes
citing us the path of least resistance for writers.
```

***

## Shared Verification Rules for All SEO Prompts

1. **Live SERPs outrank everything.** What actually ranks today — and what AI summaries do to click patterns — is visible only in current results pages and your analytics; treat model guidance as hypotheses to verify.
2. **Search engine documentation is the ground truth** for technical requirements (structured data, robots, indexing) — check it directly rather than trusting recalled specifications.
3. **Anonymize any customer-derived data** before it enters prompts or content — the privacy rules from the repository's other collections apply fully to marketing data.
4. **Quality gates beat volume goals.** Content that is merely content-shaped underperforms on modern search quality systems — the differentiation and E-E-A-T requirements in these briefs are not optional polish.
