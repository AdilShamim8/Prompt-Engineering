# Roadmap and Build Status

This file tracks what exists, what is planned, and what comes next. The curriculum itself is specified in [`CURRICULUM.md`](CURRICULUM.md); this page records execution status and maintenance decisions.

## Current status (updated 2026-10-20)

| Area | Contents | Status |
|---|---|---|
| Stage 0 — Orientation | README, CURRICULUM.md, this file | Complete |
| Stage 1 — Foundations | Beginners guide §1–6 (concepts, techniques, worked examples, pitfalls) | Complete |
| Stage 2 — Responsible use | Beginners guide §7–10 (ethics, tools, exercises, reference) | Complete |
| Stage 3 — Core techniques | 13 advanced guides, tiers A–E (CURRICULUM §3.1–3.13) | Complete |
| Stage 3 — Guide standards | Objectives/prerequisites headers and practice sections per guide | In progress |
| Stage 4 — Domain collections | 8 collections: Business, Data Science, Researchers, Students, Teachers, HR, Marketing | Complete |
| Stage 5 — Labs | 3 labs (baselines, few-shot + structured outputs, evaluation) | Complete — more welcome |
| Templates | Universal and advanced reusable prompt templates | Complete — more welcome |
| Glossary | Repository-wide terminology | Complete — extend as terms appear |
| References | Curated sources with review dates | Complete — review every 6 months |
| Validation | `scripts/validate.py` (links, structure) | Complete |

## Deliberate scope decisions

1. **Existing filenames are stable.** Guides keep their descriptive filenames rather than gaining numeric prefixes. The study order is defined by [`CURRICULUM.md`](CURRICULUM.md) (§3.1–3.13) and the section README, not by filenames. Renaming would break inbound links and the cross-references recently added across collections, for cosmetic gain.
2. **Provider-neutral content.** Techniques must work across major chat models. Provider-specific behavior is taught as a concept with a verify-against-current-docs note. Provider claims carry a review date in [`references/references.md`](references/references.md).
3. **No code dependencies.** This is a reading and practice repository. The only executable is `scripts/validate.py`, which runs on the Python standard library alone (3.8+).
4. **PDFs are snapshots.** Each collection's PDF is a frozen export of an earlier revision; the Markdown files are the maintained source of truth (the Beginners README documents this explicitly). Regenerating PDFs is a possible future task, not a standing obligation.
5. **Honest limits are content.** Guides state what a technique cannot do (prompts are not security boundaries; format constraints are not truth constraints). Overselling techniques is treated as a content bug.
6. **Scope boundary.** System-level topics (retrieval pipelines, memory, agent infrastructure) live in the companion [Context-Engineering](https://github.com/AdilShamim8/Context-Engineering) repository. This repo stays on the instruction layer.

## Suggested next iterations

Ordered by learning value; each is a self-contained contribution (see [`CONTRIBUTING.md`](CONTRIBUTING.md)):

1. **More labs** — the highest-value gap. Candidates: a chain-design lab (§3.3), a long-context position-effects lab (§3.4), an injection red-team lab (§3.11).
2. **Guide standards rollout** — complete the objectives/prerequisites and practice sections across all 13 advanced guides (tracked above).
3. **Capstone projects** — 2–3 multi-week projects that combine tiers, e.g. "build and evaluate a domain-specific extraction chain."
4. **PDF refresh** — regenerate collection PDFs from current Markdown for readers who want offline copies.
5. **CI integration** — run `scripts/validate.py` on push once a runner configuration is chosen.

## Maintenance policy

- Technical claims about provider capabilities are dated in [`references/references.md`](references/references.md). Claims older than six months should be re-verified before being relied upon.
- Every new guide must follow the module template in [`CONTRIBUTING.md`](CONTRIBUTING.md); `scripts/validate.py` must pass before a commit.
- Terminology is used consistently with [`glossary/glossary.md`](glossary/glossary.md); new terms get added there when introduced.
- Broken links are content bugs: run `python scripts/validate.py` locally before pushing.
