# Responsible AI Use in Research

Guidance companion to the researcher prompt collections: where AI legitimately accelerates research, where it introduces unacceptable risk, and how to use it so that your work remains — demonstrably — yours. This file complements the citation-verification collection by covering the ethics and disclosure layer.

***

## 1. Where the Lines Are

**Appropriate AI use in research:**
- Polishing prose you wrote and understand
- Structuring literature you supply
- Generating search strategies and screening support under human review
- Brainstorming alternative explanations and study designs
- Formatting, code review, documentation scaffolding

**Never appropriate:**
- Generating references or literature claims from model memory
- Authoring interpretive claims you could not defend in a viva or a seminar
- Producing "data" — simulated values presented as observations
- Reviewing manuscripts or grant applications confidential to others (see Section 4)
- Circumventing your venue's or institution's explicit prohibitions

**The ownership test:** for every sentence, figure, and claim in your work, you should be able to say "I know why this is here and I can defend it without the tool." Where you cannot, the tool has crossed from assistant to author.

***

## 2. The Fabrication Problem, Stated Plainly

Language models generate plausible continuations of text. In research contexts this produces three specific hazards:

1. **Fabricated references** — the best-documented failure. Handled by the Citation Verification collection: never cite from model memory; verify existence and claim-support for every reference.
2. **Fabricated findings** — confident descriptions of results that do not exist. Never ask a model what a paper found without providing the paper; never ask it to "summarize the literature on X" without supplying the literature.
3. **Fabricated data** — synthetic values that look real. Synthetic data is legitimate only when explicitly labeled as such (e.g., for methods piloting); it is misconduct when presented as observation.

The consistent remedy is architectural, not behavioral: position the model downstream of your evidence, never upstream of it.

```
Evidence (papers, data, notes YOU verified)
          ↓ you paste it in
      AI assistance
          ↓ you verify output
   Your manuscript / analysis
```

***

## 3. Authorship & Attribution

**AI tools cannot be authors.** Authorship criteria (substantial intellectual contribution, accountability for the work) are not met by tools, and major publishers and institutions have converged on this position. The human authors bear full responsibility for everything in the work — including the parts AI drafted.

**What you should do:**

1. **Check your venue's current AI policy** at submission time — journals and conferences have been updating these; the policy that applied to your last paper may not apply now.
2. **Disclose substantive use** where the policy requires it, and as good practice even where it does not — typically in methods or acknowledgments: which tools, for what tasks, and how outputs were verified.
3. **Keep the verification evidence** — the search logs, verification worksheets, and prompt records that show your diligence. This is your protection if questions arise after publication.
4. **Apply the venue rule to your own name.** If a co-author used AI in ways the policy prohibits, the work is not compliant; the corresponding author owns that question, not each contributor privately.

**Thesis and coursework contexts:** institutional academic-integrity policies increasingly address AI explicitly. The safe default is the same as for journals: disclose, document, and be able to defend every component unaided.

***

## 4. Confidentiality in the Review Process

Peer review operates on confidentiality that AI use can silently breach:

- **Never paste a manuscript you are reviewing** into a general-purpose AI tool. You are trusted with unpublished, confidential work; the tool's data handling does not inherit that trust.
- **Never paste grant applications** or theses under examination.
- If you want writing support for your own review, write the review yourself first, and use AI only on your own prose — never on the material under review.

The same logic extends to supervision: student theses, unpublished departmental data, and manuscript drafts from colleagues deserve the same boundary. Where in doubt, treat unpublished others' work as private by default.

***

## 5. Bias and the Composition of Knowledge

Models carry the biases of their training corpora, which matter in research in specific ways:

- **Literature visibility bias**: models trained on English-language, index-inclusive sources under-represent work from other languages, regions, and venues — a literature review scaffolded by model suggestions inherits that skew. Counteract with the coverage-audit prompts in the Literature Review collection.
- **Interpretation defaults**: when asked to "explain" a finding, models reach for Western-centric, WEIRD-sample framings by default. Your population and context knowledge must override.
- **Question framing**: AI-suggested "interesting research directions" cluster where training data clustered. Treat them as a starting inventory, not a shortlist.

The remedy in every case is the same: the model proposes, your domain judgment and your databases dispose.

***

## 6. A Personal AI-Use Protocol for Researchers

```
Before starting a project:
[ ] I know my venue's / institution's current AI policy
[ ] I have decided which tasks AI will and will not touch
[ ] My citation workflow does not allow model-memory references

During the work:
[ ] Every AI-drafted claim is verified against sources I hold
[ ] Every reference is confirmed in a database
[ ] Unpublished others' work never enters a general-purpose tool
[ ] My data handling follows the Data Management collection's rules

Before submission / deposit:
[ ] Disclosure statement written per policy
[ ] Verification evidence archived (searches, worksheets, prompts)
[ ] I can defend every sentence and number without the tool
[ ] Contribution statement reflects what I actually did
```

Researchers who can honestly run through that list have nothing to fear from any integrity process — the checklist is the process, run early.

***

## When Policy Is Unclear

AI policies in academia are still stabilizing. Where your venue or institution is silent or ambiguous:

1. Default to the stricter reasonable interpretation
2. Disclose more than seems required
3. Ask — editors respond well to direct policy questions, and silence-then-discovery is the worst sequence
4. Document your practices contemporaneously, so "what did you do in 2026" has an answer written in 2026

Honest over-disclosure has never ended a career. The alternative has.
