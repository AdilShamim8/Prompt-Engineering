# SQL & Data Engineering Prompts

Companion prompts to the main DS/ML guide for the data-layer work that surrounds analysis: writing and reviewing SQL, designing pipelines, schema work, and backfills — with the correctness and safety checks that production data demands.

***

## 1. SQL From a Stated Question

**Prompt:**
```
Act as a senior analytics engineer. Schema: [paste tables with columns and types,
or describe]. Question to answer: [BUSINESS QUESTION].
1. Restate the question as a precise data question — including the grain of the
   result (one row per what?).
2. Write the SQL, with a comment per CTE explaining its role.
3. State the assumptions that could make this answer wrong (joins fan-out,
   timezone, dedup logic, NULL handling).
4. Provide a sanity-check query that validates the row count and a couple of
   known rows.
```

- **Purpose:** SQL that answers the intended question, not the adjacent one.
- **Why it works:** Forcing the grain statement first prevents the most common analytics error: silent fan-out from joins.
- **Use Case:** Ad-hoc analysis, metric definitions, dashboard queries.
- **Expert Variation:**
```
Add the window-function version that avoids the fan-out entirely, and explain
when each formulation is safer.
```

***

## 2. Query Review for Correctness and Cost

**Prompt:**
```
Review this SQL before it runs on [PLATFORM, TABLE SIZES]: [paste query].
Check in order:
1. Correctness: join conditions (missing keys, many-to-many), WHERE vs ON in outer
   joins, NULL equality traps, implicit casts, DISTINCT masking real duplicates.
2. Cost: full scans on large tables, functions on indexed columns, explode-style
   fan-outs, ORDER BY on huge intermediates.
3. Portability: dialect-specific syntax I should know about.
4. Readability: aliasing that hides what tables contribute.
Output: findings ranked by severity, with the fix for the top 3 shown as code.
```

- **Purpose:** A pre-flight review that catches both wrong answers and accidental table scans.
- **Why it works:** Separates correctness (wrong numbers) from cost (slow queries) — different severities, different fixes.
- **Use Case:** Before running anything against production-sized tables.
- **Expert Variation:**
```
Rewrite the query for [WAREHOUSE, e.g., BigQuery/Snowflake/Spark] with its
specific optimizations, and note which rewrite changes results subtly.
```

**Limitations & verification:** The model cannot see your actual data distribution or indexes. Test reviewed queries on a sample or with LIMIT first; verify row counts against a known-aggregate before trusting output.

***

## 3. Incremental Pipeline Design

**Prompt:**
```
I need an incremental pipeline for [DATASET]. Current state: [how it is built
today, volume, frequency]. Source: [append-only log / mutable upserts / snapshot
files — be precise].
1. Classify my source's mutation pattern and what it implies (idempotent appends
   vs. late updates vs. deletions I must handle).
2. Design the incremental logic: watermarks, dedup keys, and what happens to
   late-arriving or out-of-order data.
3. Write the SQL/pseudocode with idempotency: running twice for the same window
   must not double-count.
4. List the failure modes: what silently corrupts this design, and the check
   that catches each.
```

- **Purpose:** Incremental processing that does not quietly drift from the full rebuild.
- **Why it works:** Idempotency and late-data handling are designed in, not patched after the first incident.
- **Use Case:** Warehouse ingestion, feature pipelines, reporting tables.
- **Expert Variation:**
```
Design the reconciliation job: a scheduled full-vs-incremental comparison with
alert thresholds, and the backfill procedure when they diverge.
```

***

## 4. Backfill & Migration Safety Runbook

**Prompt:**
```
Draft a safe-run checklist for this backfill/migration: [describe the change,
tables, row counts, downtime tolerance].
The runbook must include:
1. Preconditions: snapshots/backups taken, blast radius stated, rollback trigger
   defined BEFORE starting.
2. The staged execution: can this run on a copy first? In batches? With a
   row-count and checksum comparison per batch?
3. Invariants to verify after: counts, sums of key columns, orphan checks,
   sample row diffs.
4. The rollback procedure, written so someone else can execute it at 2 AM.
5. What must NOT be done in the same maintenance window as this change.
```

- **Purpose:** Data migrations that are boring, in the best sense of the word.
- **Why it works:** Preconditions, staged execution, and rollback-before-start convert catastrophic risks into scheduled ones.
- **Use Case:** Schema changes, historical repairs, partition management.
- **Expert Variation:**
```
Add the communication plan: who is informed at start, at each stage gate, and at
completion — and the status page/Slack template for each.
```

**Limitations & verification:** Never run generated DDL/DML on production without executing it first against a restored copy or staging with production-scale data. The runbook's value is only realized if every step is actually performed — checklist discipline is the control.

***

## 5. Data Contract & Schema Documentation

**Prompt:**
```
Draft a data contract for [TABLE/DATASET]: [paste schema and purpose].
Include:
1. Grain statement: one row per what, enforced by which key
2. Column dictionary: type, meaning, units/timezone, and allowed NULL-ness with
   the reason
3. Freshness and completeness SLAs: how stale is acceptable, how missingness is
   signaled (versus indistinguishable from zero)
4. Explicit non-guarantees: what downstream consumers must NOT assume
5. Breaking-change policy: what counts as breaking, and how changes are announced
Where information is unknown, insert [TO CONFIRM] — do not invent.
```

- **Purpose:** The document that prevents the silent breakage of downstream consumers.
- **Why it works:** Non-guarantees are listed as carefully as guarantees — assumptions others make are the ones that hurt.
- **Use Case:** Cross-team datasets, ML feature stores, analytics marts.
- **Expert Variation:**
```
Add the consumer questionnaire: the 5 questions every new downstream user should
answer before building on this table, which double as an integration test.
```

***

## 6. Debugging a Wrong Number

**Prompt:**
```
A stakeholder reports [METRIC] differs between [SOURCE A] and [SOURCE B] by
[AMOUNT/PATTERN — e.g., always 3-5%, spike since Tuesday].
Help me debug systematically:
1. Generate the differential-diagnosis list: definition mismatch, timezone
   boundaries, filter differences, fan-out, freshness lag, backfill drift,
   row duplication, NULL vs zero semantics.
2. For each: the cheapest query that confirms or eliminates it.
3. Order the checks to maximize information per query.
4. Draft the response to the stakeholder that explains the likely cause and the
   timeline to certainty — without blaming either source prematurely.
```

- **Purpose:** The recurring 2 AM of analytics: two numbers that should match and do not.
- **Why it works:** Differential diagnosis with cheapest-test ordering is dramatically faster than attacking causes in sequence of annoyance.
- **Use Case:** Metric incidents, audit prep, post-merge discrepancies.
- **Expert Variation:**
```
Once the cause is found (I will report back), design the permanent guardrail:
the test, alert, or contract clause that prevents this exact discrepancy class
from recurring silently.
```

***

## Shared Verification Rules for All Data Engineering Prompts

1. **Never run generated SQL blind.** EXPLAIN it, LIMIT it, sample it — then run it. Generated code that "looks right" is the leading cause of accidental full-table mutations.
2. **Row counts are the canary.** Before and after any data operation, counts and key-column checksums are the cheapest truth available.
3. **Destructive operations get a dry run.** Every UPDATE/DELETE earns itself a SELECT twin first, and a transaction wrapper where the platform supports it.
4. **The model does not know your data.** Cardinalities, skew, NULL semantics, and stale partitions are invisible to it; supply them or verify against them.
