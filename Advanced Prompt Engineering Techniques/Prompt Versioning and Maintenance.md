# Prompt Versioning and Maintenance

Managing prompts as maintained production assets rather than copied-and-pasted folklore. A prompt that runs a real workflow is software: it has behavior, dependencies, failure modes, and a lifecycle. This guide covers the practices that keep prompt libraries trustworthy over months and across team members.

## Before You Start

**Learning objectives** — after this guide you can: keep a minimum viable prompt record (version, owner, dependencies, test set); apply the retirement discipline that kills zombie prompts; wire prompt changes into review and regression gates; and budget the real maintenance cost.

**Prerequisites** — [Prompt Evaluation and Testing](./Prompt%20Evaluation%20and%20Testing.md) (versioning without a test set is bookkeeping without feedback). Curriculum position: [§3.13](../CURRICULUM.md#tier-e--operate-and-maintain) — the final advanced guide, where the curriculum's techniques become an operated library.

## The Minimum Viable Prompt Record

Every prompt worth keeping gets a record:

```
name: support-ticket-classifier
version: 2.3 (2026-09-14)
owner: [who answers questions about this prompt]
purpose: classify inbound tickets for routing; feeds the
  dispatch queue
prompt: |
  [the full text, placeholders in {BRACES}]
inputs: {ticket_text} — raw customer message
outputs: JSON: {category, urgency, confidence}
dependencies: none / [tools, context sources, model name+version]
test set: tests/support-classifier.jsonl (24 cases, incl. 3
  adversarial)
known issues: misroutes "cancel my subscription" to account
  instead of retention (see issue #12)
changelog:
  2.3 — added fallback label rule; +4 test cases (regression
       from 2.2 fixed)
  2.2 — switched category order; urgency rubric tightened
  2.0 — breaking: output schema changed, downstream updated
```

The changelog's breaking-change notation matters most: prompt 2.0-to-2.1 with a changed output schema is an API change, and downstream consumers (scripts, chains, agents) break exactly the way code does.

## Versioning Semantics

- **Major (2.x → 3.0)**: output schema, contract, or behavior changes that break consumers
- **Minor (2.3 → 2.4)**: quality improvements, new examples, same contract
- **Patch (2.3.1)**: typo/format fixes with no behavioral intent

Where do prompts live? The same place your code does — version control (this repository is itself an example), with the same review discipline for prompts that drive anything real. Prompt changes to production workflows get code-review treatment: diff shown, test results attached, a human approves.

## The Maintenance Triggers

Prompts decay without anyone touching them. The events that should trigger a maintenance pass:

**Model updates.** When the provider updates or deprecates the model your prompt runs on, re-run the full test set before assuming continuity. Behavioral drift after upgrades is real; the test set is how you see it early rather than in user complaints.

**Input drift.** The world your prompt sees changes — new products, new customer phrasings, new edge cases. Quarterly, sample real production inputs against your test set: if today's inputs look unlike your saved cases, the test set is stale and the prompt's real performance is unknown.

**Failure reports.** Every reported failure becomes: a test case (reproduce it), a diagnosis (prompt fix / unfixable / out of scope), and if fixed, a version bump. Unlogged fixes evaporate; the next person relearns them.

**Contract changes.** When downstream consumers' needs change (a new field needed, a field deprecated), the prompt's output schema changes — major version, coordination with consumers, updated tests.

## Team Practices

**Ownership.** Every production prompt has a named owner — the person paged when it misbehaves, who approves changes. Unowned prompts are abandoned regardless of how critical they are.

**The library is the interface.** Team members should be able to find prompts by task, understand inputs/outputs/limits from the record alone, and trust the test status. A library needing oral tradition to operate is not a library.

**Reuse before creation.** Before writing a new prompt, search the library for the task — adapting a tested prompt inherits its hardening. Divergent near-duplicates ("classify-support" vs "ticket-sort") rot separately and drift apart; merge or explicitly differentiate.

**Deletion is healthy.** Retired prompts leave the active library with a tombstone record (what it did, why retired, what replaced it). Graveyards answer "did we try that already?" — the question that otherwise re-runs failed experiments annually.

## Prompt CI (When Scale Justifies It)

Organizations with dozens of production prompts converge on automation:

```
On every prompt change (PR):
  → Lint: placeholders documented, no secrets, structure present
  → Run test suite against the changed prompt
  → Compare to baseline: per-case diff, regression gate
  → Report attached to the PR; human approves

Scheduled:
  → Nightly/weekly: re-run suites unchanged (catches provider-
    side model drift)
  → Monthly: sample production inputs vs test sets (staleness)
```

This is ordinary engineering discipline applied to a new artifact type — the tools are the same (version control, CI, code review); the test runners are LLM-specific (see the Evaluation guide for the scoring layers that make regression gates meaningful).

## The Maintenance Budget

The honest accounting: production prompts cost ongoing attention. A useful planning ratio — for every hour spent writing a prompt, expect 15-30 minutes per quarter maintaining it (test refresh, drift checks, incident response), more for prompts on fast-changing inputs. Budgeting zero maintenance means budgeting eventual silent failure; the prompt keeps responding while its quality quietly erodes, and nothing announces the rot until the audit, the incident, or the embarrassing screenshot.

## Practice

Create the minimum viable record for three prompts you actually use: name, version and date, owner, purpose, model it was tested against, dependencies, and — the load-bearing field — its test set (five saved inputs with expected key facts, per [Lab 3](../labs/lab-03-evaluation-and-regression-testing.md)). Store them as Markdown files in one folder: that is a versioned prompt library in miniature, diffable in any version control system. Then set the review cadence: a recurring calendar reminder to re-run each test set. The habit, not the tooling, is the deliverable.

## Further Reading

- [White et al. — A Prompt Pattern Catalog](https://arxiv.org/abs/2302.11382) — pattern names give a shared vocabulary for library documentation
- This repository's [templates/](../templates/) — skeletons to seed your own library records
