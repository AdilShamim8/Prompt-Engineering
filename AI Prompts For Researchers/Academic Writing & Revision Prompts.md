# Academic Writing & Revision Prompts

Companion prompts to the main researchers guide for drafting and — more importantly — revising scholarly text: clarity passes, argument strengthening, journal formatting, and responding to reviewers. The rule throughout: AI polishes your prose and clarifies your structure; the thinking, the evidence, and every citation remain yours.

***

## 1. Clarity Pass (Preserving Voice)

**Prompt:**
```
Revise this passage for clarity without changing my meaning or voice: [paste].
1. Flag sentences over 35 words and propose splits.
2. Replace nominalizations with their verbs where it helps ("conduct an analysis
   of" → "analyze") — but keep discipline-specific terms.
3. Untangle stacked modifiers and ambiguous antecedents ("this", "it" with no
   clear noun).
4. Preserve my terminology choices and citation placement exactly.
5. List what you changed in categories, so I can reject whole categories at once.
```

- **Purpose:** Clearer text that still sounds like the author.
- **Why it works:** Change-categorization lets the writer accept/reject by type, keeping editorial control.
- **Use Case:** Pre-submission polish, thesis chapters, non-native-language support.
- **Expert Variation:**
```
Do the reverse pass: flag where my compression created ambiguity, and where a
discipline convention requires more precision than plain style allows.
```

***

## 2. Argument Structure Audit

**Prompt:**
```
Audit the argument structure of my [SECTION TYPE — introduction/discussion]:
[paste].
1. Map the argument: each paragraph's claim, its evidence, and its link to the
   next paragraph — as a numbered outline.
2. Flag: claims without evidence, evidence without claims, and links that rely
   on the reader's goodwill ("clearly", "obviously", "it follows").
3. Identify the strongest objection a skeptical reviewer would raise at each
   juncture — and whether my text already handles it.
4. The one-sentence version of my whole argument, as a reader would extract it.
   Does it match what I intend?
```

- **Purpose:** Argument-level review that no line edit can substitute for.
- **Why it works:** The extracted one-sentence version reveals the gap between intended and delivered argument instantly.
- **Use Case:** Introductions that must earn the study, discussions that must earn the claims.
- **Expert Variation:**
```
Reorder the paragraphs into the strongest possible sequence, and justify each
move — sometimes the best revision is structural, not linguistic.
```

***

## 3. Abstract Engineering

**Prompt:**
```
Draft my abstract from the manuscript's own content: [paste intro, results
summary, and conclusion — or the full sections]. Target venue limit: [WORDS].
Structure:
1. Background: 1 sentence with the gap named
2. Objective: 1 sentence, precise
3. Methods: 2-3 sentences — design, sample, measures, analysis (name them)
4. Results: 2-3 sentences with the key numbers and confidence/precision
5. Conclusion: 1-2 sentences answering the objective, without overreach
Rules: no claims not present in the provided text; no citations; every number
must appear in the pasted results.
```

- **Purpose:** The abstract that determines whether the paper gets read.
- **Why it works:** Deriving from pasted content (not memory) keeps the abstract honest to the paper.
- **Use Case:** Submission preparation, conference deadlines.
- **Expert Variation:**
```
Generate the structured-abstract variant (labeled sections) AND the flowing
variant — then check both against the venue's actual format requirements.
```

**Limitations & verification:** Verify every number in the output against your results tables — transposition errors between paper and abstract are a classic submission bug.

***

## 4. Reviewer Response Letter

**Prompt:**
```
Draft responses to these reviewer comments: [paste comments]. My manuscript
changes: [describe what I changed / refused to change and why].
For each comment:
1. Restate the concern in one sentence — generously, as the reviewer would
   recognize it.
2. The response: what we changed (with section/page references) or the
   evidence-based defense — never defensive tone, never gratitude theater.
3. Where I disagree: the respectful, evidence-cited refusal — quote the
   manuscript passage or literature that supports keeping it as-is.
4. Flag any comment that is actually two comments wearing one paragraph — split
   and answer both.
```

- **Purpose:** Response letters that get papers accepted by taking concerns seriously.
- **Why it works:** The "generous restatement" plus "never gratitude theater" rules produce the tone editors actually reward.
- **Use Case:** Journal revisions, grant resubmissions, committee responses.
- **Expert Variation:**
```
Add the summary-of-changes table (comment | change | location) for the editor's
cover letter — reviewers love not hunting for changes.
```

***

## 5. Journal Fit & Formatting Pass

**Prompt:**
```
My target journal: [JOURNAL]. Their stated requirements: [paste guide excerpts
or describe]. My manuscript: [paste abstract or outline].
1. Fit check: does my framing, methods visibility, and claim strength match
   this venue's typical papers? What to adjust for THIS audience?
2. Formatting checklist: word limits, abstract structure, heading levels,
   reference style — converted into a copyable pre-submission checklist.
3. The title: 3 candidates that are informative first, clever second — under
   [LIMIT] characters.
4. Cover letter draft: 3 paragraphs — contribution, fit to journal scope,
   confirmations (originality, no concurrent submission).
```

- **Purpose:** Clearing the administrative gates that return papers unread.
- **Why it works:** Fit-checking before formatting avoids polishing for the wrong venue entirely.
- **Use Case:** First submission, resubmission to a new venue after rejection.
- **Expert Variation:**
```
Adapt the same manuscript for a second venue: what changes in framing, length,
and reference style — a diff-style migration plan.
```

**Limitations & verification:** Journal requirements change — verify every limit and format rule against the journal's current author guidelines page rather than the model's recollection of them.

***

## 6. Plagiarism-Adjacent Self-Check

**Prompt:**
```
Self-check my draft for academic integrity risks: [paste draft, or key passages].
1. Flag passages that read as boilerplate phrasing common enough across the
   literature that similarity checkers will flag them — suggest rewordings
   that carry my specific meaning.
2. Flag anywhere my paraphrase of a source drifts too close to the source's
   likely phrasing (I will compare against originals — list the passages and
   their claimed sources).
3. Flag "accidental overclaim": sentences that state as established what I
   cited as single-study or preliminary.
4. Confirm citation presence: every factual claim from a source carries one.
```

- **Purpose:** Catching the unintentional integrity risks before Turnitin or a reviewer does.
- **Why it works:** Separates the three distinct risks — boilerplate similarity, paraphrase drift, and overclaim — which need different fixes.
- **Use Case:** Pre-submission, thesis deposit.
- **Expert Variation:**
```
Add the AI-disclosure paragraph for the methods/acknowledgments, matching the
policies of: [VENUE] — stating what AI tools were used for and how outputs
were verified.
```

**Limitations & verification:** This check is advisory — it cannot see the actual sources or run similarity detection. Compare flagged paraphrases against the originals yourself, and run the venue's official checks.

***

## Shared Verification Rules for All Writing Prompts

1. **AI assists revision; authorship stays yours.** Every sentence in the final text must be one you understand, can defend, and would claim in a conversation.
2. **Never let AI add citations.** Writing prompts here are citation-neutral by design; any reference the model inserts from memory gets deleted or replaced with one you verified.
3. **Check venue policy on AI use.** Journals differ; the disclosure you write should match the current policy, checked at submission time.
4. **Numbers cross-checked, always.** Abstract-to-results, response-letter-to-revision — transcription errors are the failure mode of every deadline rush.
