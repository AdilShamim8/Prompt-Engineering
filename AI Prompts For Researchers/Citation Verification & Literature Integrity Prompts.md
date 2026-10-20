# Citation Verification & Literature Integrity Prompts

Companion prompts to the main researchers guide. Fabricated citations are the most documented failure of AI in academic work: models produce references that look perfectly plausible — real authors, real journals, plausible titles — and do not exist. These prompts build the verification habits that make AI-assisted literature work defensible.

***

## 1. The Golden Rule: AI Proposes, Databases Dispose

No prompt can make a model cite honestly, because the failure is not stylistic — the model does not have a lookup failure, it generates references the way it generates sentences. The workflow must therefore be:

```
AI's role (safe):
- Suggesting search terms, keywords, and query strings
- Summarizing papers YOU provide in full text or abstract
- Structuring a review around sources you have verified
- Drafting prose that cites your verified source list

AI's role (unsafe — never do this):
- Generating a reference list from memory
- Supplying DOIs, page numbers, or years "it remembers"
- Summarizing a paper from title alone
- Telling you what an author "argues" without the text in front of it
```

***

## 2. Reference List Audit

**Prompt:**
```
Act as a research librarian auditing a reference list for authenticity signals.
I will paste references I HAVE NOT yet verified: [paste].
For each reference, flag:
1. Existence risk: high/medium/low — based on plausibility patterns (year vs.
   journal volume, author-field fit, too-perfect title-match to the topic)
2. What to check first: the fastest database/lookup that would confirm or refute
   it exists (Google Scholar, DOI resolver, PubMed, publisher site)
3. Mismatch risk: even if it exists, does the cited claim likely match this
   paper's scope?
Do NOT confirm any reference as real — you cannot. Classify risk and route to
verification only.
```

- **Purpose:** Triage for verifying references at speed, without ever treating AI output as verification itself.
- **Why it works:** Explicitly denies the model the authority to confirm — it can only route to actual databases.
- **Use Case:** Auditing AI-drafted text, reviewing collaborators' citations, pre-submission checks.
- **Expert Variation:**
```
Generate the verification worksheet: a table (Reference | Database to check |
Search string to use | Result | Verified by/date) I can attach to my methods
section as evidence of citation diligence.
```

***

## 3. Search Strategy Design (Where AI Is Genuinely Useful)

**Prompt:**
```
I am researching: [QUESTION]. Field: [FIELD]. Databases I access: [LIST].
1. Generate the concept blocks: 3-4 concept groups with synonyms, related terms,
   spelling variants, and discipline-specific vocabulary.
2. Build 2 boolean query variants: a precision-focused one and a
   recall-focused one — and explain the trade-off.
3. Suggest the filters to apply (date, study type, language) and what each
   filter excludes that I might regret.
4. List 3 highly-cited starting papers likely to anchor the search — and label
   them "UNVERIFIED LEADS: confirm existence before use."
```

- **Purpose:** Using the model's strength (vocabulary breadth) while fencing its weakness (factual recall).
- **Why it works:** The "UNVERIFIED LEADS" label bakes the verification boundary into the output format.
- **Use Case:** Starting literature reviews, systematic review protocol design.

**Limitations & verification:** Run the queries; treat the anchor-paper leads as hypotheses until each is confirmed in a database. If a suggested paper does not surface in the database search, that is itself information about the lead.

***

## 4. Claim-to-Source Tracing

**Prompt:**
```
Here is my draft text with citations: [paste]. For every claim-citation pair:
1. Classify the support level: DIRECT QUOTE (words appear in source) / PARAPHRASE
   (idea appears) / DIRECTIONAL (source is related but does not make this claim)
   / ORPHAN (no source supports this).
2. For each PARAPHRASE and DIRECTIONAL: the exact passage I should be able to
   point to, phrased as a verification question for me to check against the
   source.
3. List every ORPHAN claim — these need a source found or a claim deleted.
```

- **Purpose:** Ensuring every sentence that needs support has support that actually supports it.
- **Why it works:** The four-level classification distinguishes "cited" from "supported" — the gap where retractions live.
- **Use Case:** Pre-submission review, thesis checkpoints, responding to reviewer critique of citations.
- **Expert Variation:**
```
Add the strength audit: for each DIRECT/PARAPHRASE support, is one source enough
for this claim strength, or does the claim need convergent evidence?
```

**Limitations & verification:** The model classifies from the text you paste — it cannot see the sources. Every classification is a pointer for YOUR check against the actual paper, not a verification.

***

## 5. Abstract-Only Summarization Guardrail

**Prompt:**
```
Summarize this paper from the abstract I provide: [paste abstract].
Rules:
1. Restrict every statement to what the abstract literally supports.
2. Label clearly: (a) what the authors report, (b) what they conclude,
   (c) what they say about limitations.
3. Explicitly list what CANNOT be known from the abstract: sample details,
   methods specifics, effect sizes, robustness checks.
4. End with: "Full-text needed before citing for: [list of claims I might want
   to make]."
```

- **Purpose:** Preventing the common shortcut where abstract-level summaries get cited for full-text-level claims.
- **Why it works:** The cannot-know list and full-text-needed note make the epistemic boundary explicit and hard to forget at writing time.
- **Use Case:** Screening large numbers of papers, drafting related work before full-text passes.
- **Expert Variation:**
```
Produce the screening decision: based only on this abstract, should this paper
advance to full-text review for MY question: [QUESTION]? Give the include/exclude
rationale in PRISMA-screening style.
```

***

## 6. Fabrication Self-Check Before You Submit

**Prompt:**
```
Act as an integrity reviewer for my manuscript before submission. I will paste
my reference list and key claims: [paste].
1. Flag any reference whose format looks AI-generated: suspiciously well-aligned
   titles, generic-but-plausible phrasing, author combinations that do not
   co-occur in the field.
2. Flag claims that "sound cited" — where a specific number, finding, or
   attribution appears without inline anchoring.
3. Generate my verification statement for the methods or acknowledgments:
   a 3-sentence disclosure of how AI tools were used in this work and how
   outputs were verified.
4. Produce my final pre-submission checklist for citation integrity.
```

- **Purpose:** The last gate between draft and submission.
- **Why it works:** Combines detection heuristics with the disclosure statement many venues now expect.
- **Use Case:** Journal submission, conference deadlines, thesis deposit.
- **Expert Variation:**
```
Draft the reviewer-response paragraph for citation questions: how I would
document my verification process if a reviewer challenges any reference.
```

**Limitations & verification:** Every flagged item still requires a human database check — the model's suspicion is a triage signal, not evidence. Maintain the verification worksheet as your proof of diligence.

***

## Shared Verification Rules for All Research Citation Prompts

1. **Never cite from model memory.** A reference that did not come from your own database search, full-text reading, or citation chaining does not exist until verified.
2. **Verify existence AND claim-support.** A real paper that does not make the claim you attribute to it is as serious an error as a fabricated one.
3. **Keep the evidence trail.** The verification worksheet (what you checked, where, when) is your protection when citations are questioned — in peer review or after publication.
4. **Disclose AI use per venue policy.** Journals and institutions increasingly require it; honesty here is cheap, and its absence is expensive.
