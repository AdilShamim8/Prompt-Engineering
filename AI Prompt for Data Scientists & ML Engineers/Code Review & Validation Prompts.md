# Code Review & Validation Prompts

Companion prompts to the main DS/ML guide for the code layer of data work: reviewing generated code before it runs, testing data code correctly, and validating AI-assisted programming. Generated code is a draft from a fast collaborator who never runs what it writes — these prompts supply the review discipline that difference demands.

***

## 1. Pre-Run Review of Generated Code

**Prompt:**
```
Review this generated code before I run it: [paste code]. Intended behavior:
[ONE SENTENCE]. Review in this order:
1. Does it do what I said — trace the logic line by line against the intent.
2. Edge cases: empty input, single row, NULLs/NaNs, duplicate keys, timezone
   boundaries — which ones break it?
3. Side effects: what does it modify, write, delete, or send? List every one.
4. Quiet failure modes: where would it produce wrong values without raising?
5. Library misuse: deprecated APIs, version-sensitive behavior, pandas
   SettingWithCopy-style traps.
Output: verdict per check, then the corrected code for any failure found.
```

- **Purpose:** A systematic gate between "the model wrote it" and "it runs on my data."
- **Why it works:** Ordered checks prevent the halo effect where clean style reads as correctness.
- **Use Case:** Any AI-generated code touching real data.
- **Expert Variation:**
```
Rank every issue by blast radius if wrong: crashes (visible) versus wrong values
(silent) — and fix the silent ones first.
```

***

## 2. Test Design for Data Code

**Prompt:**
```
I need tests for this data function: [paste function]. Help me design them:
1. The 5 test cases that matter: typical, empty, single-item, boundary (first/last
   timestamp, group boundary), and adversarial (duplicate keys, unsorted input,
   mixed types).
2. For each: input, expected output, and what bug class it catches.
3. The property-based test: what invariant should hold for ALL inputs (e.g.,
   output row count == unique key count)?
4. Generate pytest code including fixtures that construct realistic small inputs
   — no external data files.
5. One test that should FAIL if someone breaks the function's core contract.
```

- **Purpose:** Testing data logic where the failure mode is wrong numbers, not exceptions.
- **Why it works:** Property invariants catch the bug classes that example tests systematically miss.
- **Use Case:** Pipeline functions, metric calculations, feature transformers.
- **Expert Variation:**
```
Add a data snapshot test: how to freeze a small realistic input-output pair so
refactors can be verified against known-good results.
```

**Limitations & verification:** Run the generated tests; confirm the failure-path test actually fails when it should (mutate the function deliberately and watch the suite catch it). A test suite that never caught a bug is unverified infrastructure.

***

## 3. Reproducibility Gap Check

**Prompt:**
```
This notebook/code will be re-run by [COLLEAGUE/FUTURE ME] in [TIMEFRAME].
[Paste or describe the code and its data access.]
1. List everything the re-run depends on that is NOT in the code: file paths,
   environment variables, package versions, data versions, random state,
   execution order, hidden notebook state.
2. For each gap: the minimal fix (config cell, requirements pin, data snapshot,
   explicit seed).
3. Generate the header cell that captures environment, versions, and data
   provenance at run time.
4. What will still not be reproducible, honestly?
```

- **Purpose:** Making re-runs produce the same numbers — the definition of analysis you can stand behind.
- **Why it works:** Attacks notebook hidden state and implicit dependencies, the two silent killers of reproducibility.
- **Use Case:** Shared analyses, publication work, recurring reports.
- **Expert Variation:**
```
Convert the critical cells into a parameterized script with a --dry-run mode,
and list which notebook conveniences we lose and accept losing.
```

***

## 4. Refactoring with Behavior Preservation

**Prompt:**
```
I want to refactor this working code: [paste]. Goal: [READABILITY / SPEED /
MODULARITY]. Constraints: [must not change behavior on any input].
1. Propose the refactor plan in steps, each independently verifiable.
2. For each step: how to verify behavior is preserved (characterization tests,
   output comparison on representative inputs, checksum of results).
3. Generate the characterization harness FIRST — capture current outputs on
   [describe representative inputs] before touching anything.
4. Flag any part of the current behavior that looks like a bug — so we can
   decide deliberately whether to preserve or fix it (never fix silently in a
   refactor).
```

- **Purpose:** Refactors that cannot quietly change results.
- **Why it works:** Characterization-before-change and the preserve-or-fix decision rule eliminate the two classic refactor sins.
- **Use Case:** Cleaning notebook-to-pipeline migrations, performance work on metric code.
- **Expert Variation:**
```
Add the performance comparison protocol: timing methodology, warm-up runs, and
the variance-aware threshold for claiming 'faster'.
```

***

## 5. Dependency & Environment Audit

**Prompt:**
```
Audit my project's dependencies for silent risk: [paste requirements/environment
or describe imports].
1. Which imports come from transitive dependencies (will break unpredictably)?
2. Which packages are pinned exactly, loosely, or not at all — and which lack
   of pinning is actually dangerous given my usage?
3. Known deprecation/versioning landmines in the libraries I use heavily?
   [State your library versions.]
4. Generate the lockfile-compatible requirements with justified pins, and a
   one-line reason per pin.
5. The upgrade test: a 10-line script that verifies my core workflows still
   produce identical outputs after a dependency bump.
```

- **Purpose:** Environments that mean the same thing next quarter.
- **Why it works:** Distinguishes dangerous unpinned dependencies from harmless ones, focusing effort.
- **Use Case:** Team projects, shared images, CI stability.
- **Expert Variation:**
```
Design the dependency-refresh cadence: which packages to track closely
(fast-moving, break-prone) versus lazily (stable, low-risk), and why the
categorization fits my usage.
```

**Limitations & verification:** The model's knowledge of specific library versions may lag — verify deprecation claims against official changelogs before acting on them, and run the upgrade test rather than trusting the categorization.

***

## 6. Security Review of Data Code

**Prompt:**
```
Security review this code that handles data: [paste code]. Check specifically:
1. Injection surfaces: any string-built SQL, path construction from user input,
   eval/exec/pickle usage.
2. Secret handling: credentials in code, logged tokens, secrets in notebook
   outputs that will be shared.
3. Unsafe deserialization: pickle, yaml.load without safe loader, reading
   untrusted files.
4. Data exposure: what gets written to logs, error messages, or temp files that
   should not be?
5. Excess privilege: database accounts with rights beyond what this code needs?
Output: Issue | Attack scenario | Fix, ranked by exploitability.
```

- **Purpose:** The security pass data code never receives but increasingly needs.
- **Why it works:** Enumerates the concrete attack surfaces of data workflows rather than generic web-app advice.
- **Use Case:** Pipelines touching PII, notebooks leaving the laptop, code destined for shared infrastructure.
- **Expert Variation:**
```
For each finding, classify: fix now / fix this quarter / accept-and-document —
using my actual threat model: [WHO could plausibly attack or accidentally
expose this, and what is at stake?]
```

***

## Shared Verification Rules for All Code Review Prompts

1. **Run it yourself, every time.** No amount of review replaces execution — generated code must run on known-answer inputs before touching real data.
2. **Silent wrongness beats crashes on severity.** Prioritize verification of code paths that produce values without raising exceptions.
3. **Never execute destructive generated code outside a transaction or dry-run twin.** UPDATE/DELETE/DELETE-file operations get a SELECT preview first, always.
4. **Assume version drift.** Library claims in review output are hypotheses; confirm against the documentation and versions you actually run.
