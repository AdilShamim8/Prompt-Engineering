# Research Question & Methodology Prompts

Companion prompts to the main researchers guide for the design layer of research: sharpening questions until they are answerable, choosing methods that can actually answer them, and anticipating the methodological critiques that reviewers will raise.

***

## 1. Research Question Sharpener

**Prompt:**
```
Act as a methods advisor. My draft question: [QUESTION]. Help me sharpen it:
1. Restate it as: population, exposure/intervention or phenomenon, outcome, and
   (if applicable) comparison — flag which parts are currently vague.
2. Generate the 3 sharpest versions that are actually answerable with feasible
   data — each one sentence.
3. For each version: what it excludes that my vague original implied (narrowing
   is a feature — make the trade-offs visible).
4. The falsification check: what result would prove each version's premise
   wrong?
5. One "too sharp" version that would require data I probably cannot get —
   so I can see the feasibility frontier.
```

- **Purpose:** Questions specific enough to be answered and falsified.
- **Why it works:** The PICO-style decomposition surfaces vagueness that survives casual reading.
- **Use Case:** Thesis proposals, grant drafts, study kickoffs.
- **Expert Variation:**
```
For my chosen version, draft the null and alternative hypotheses with the
exact testable quantities named — no "associated with" hand-waving.
```

***

## 2. Method-Question Fit Assessment

**Prompt:**
```
My research question: [FINAL QUESTION]. My candidate methods: [LIST with your
constraints — sample access, timeline, budget, skills].
For each candidate:
1. What this method CAN answer about my question, precisely.
2. What it structurally CANNOT answer (claim-type limits, not skill limits).
3. The threat to validity it handles best, and the one it leaves wide open.
4. Feasibility verdict given my constraints, with the binding constraint named.
5. The hybrid: which two methods, in what sequence, cover each other's blind
   spots for this question?
```

- **Purpose:** Method choice as a fit decision, not a fashion decision.
- **Why it works:** Claim-type limits (what a method can never support) prevent the misapplications that methods sections get rejected for.
- **Use Case:** Proposal design, defending a methods choice to a committee.
- **Expert Variation:**
```
Role-play the methods reviewer: write the 3 harshest but fair critiques of my
chosen design, then my best response to each — or the design change each
critique forces.
```

***

## 3. Validity Threat Brainstorm

**Prompt:**
```
My design: [DESCRIBE — sample, procedure, measures, timing]. Question: [QUESTION].
1. Internal validity: list the threats that could produce my expected finding
   even if the underlying premise is false (selection, history, maturation,
   instrumentation, attrition, testing effects).
2. External validity: to whom and to what settings would my findings NOT
   generalize, and why — concretely?
3. Construct validity: where might my measures measure something adjacent to
   my construct?
4. For each threat: the design feature or analysis that addresses it — or the
   honest acknowledgment that it is unaddressed and how I will word the
   limitation.
```

- **Purpose:** Anticipating the reviewer's validity critique before the data exist.
- **Why it works:** The four validity families give the brainstorm exhaustive structure; the "honest acknowledgment" branch prevents defensive overclaiming.
- **Use Case:** Pre-registration, IRB/ethics protocols, proposal defenses.
- **Expert Variation:**
```
Convert the top 3 unaddressed threats into future-study designs, so my
limitations section reads as a research agenda rather than an apology.
```

***

## 4. Operationalization & Measurement Plan

**Prompt:**
```
I need to measure [CONSTRUCT] in [POPULATION/SETTING]. Help me operationalize:
1. The definition I will use — with one sentence on the boundary cases it
   deliberately excludes.
2. Candidate measures: for each, what it actually captures, its known
   weaknesses for MY population, and its practical cost.
3. The triangulation option: what second measure would most strengthen claims
   about this construct, and what disagreement between the two measures would
   mean?
4. Preregistration language: the exact decision rules for scoring, missing
   data, and exclusions — written so a stranger could apply them.
```

- **Purpose:** Turning constructs into procedures specific enough to preregister.
- **Why it works:** The stranger-test on decision rules exposes the ambiguity that post-hoc flexibility feeds on.
- **Use Case:** Survey design, experiment protocols, qualitative coding schemes.
- **Expert Variation:**
```
Draft the reliability and validity evidence table: for my chosen measure, what
I will report (internal consistency, inter-rater agreement, prior validation
in this population) and where each number comes from.
```

***

## 5. Qualitative Rigor Planning

**Prompt:**
```
My qualitative study: [design — interviews/ethnography/content analysis].
Question: [QUESTION].
1. Saturation plan: how I will decide data collection can stop — with criteria
   fixed in advance, not after fatigue sets in.
2. Reflexivity memo: generate the prompt questions I should answer about my own
   position relative to this topic, population, and expected findings.
3. Trustworthiness: for each criterion (credibility, transferability,
   dependability, confirmability), the concrete technique I will use — audit
   trail, member checking, thick description, negative-case analysis.
4. Coding discipline: the process from open coding to a codebook that a second
   coder could apply — including how disagreements get resolved.
```

- **Purpose:** Qualitative work with the rigor that survives "is this just your interpretation?" review.
- **Why it works:** Converts the trustworthiness vocabulary from jargon into named, scheduled techniques.
- **Use Case:** Qualitative proposals, IRB protocols, mixed-methods components.
- **Expert Variation:**
```
Add the negative-case analysis protocol: how I will actively search for data
that disconfirms my emerging interpretation, and document that search.
```

***

## 6. Scope & Feasibility Reality Check

**Prompt:**
```
My study plan: [DESIGN, SAMPLE, TIMELINE, RESOURCES]. Question: [QUESTION].
1. The scope check: is this question answerable at this scale, or is it a
   career-scale question wearing a thesis-scale costume? Name what to cut.
2. The timeline stress test: which steps have optimistic durations, and what
   is the realistic total if each slips by its typical factor?
3. The single-point-of-failure list: what could make this study die entirely
   (access, funding, one dataset, one instrument)?
4. The minimum viable study: the version I could complete even in the worst
   realistic timeline — define it now, not under deadline panic later.
5. The kill criteria: under what conditions should I abandon or pivot this
   study, written now while I am objective?
```

- **Purpose:** Research plans that survive contact with reality.
- **Why it works:** The minimum viable study and kill criteria are the two planning artifacts researchers most often lack and most need.
- **Use Case:** Grant budgeting, thesis planning, industry research roadmaps.

**Limitations & verification:** Feasibility judgments depend on your actual access and constraints — the model optimizes the plan you describe, so describe honestly, including the parts you are tempted to hide from yourself.

***

## Shared Verification Rules for All Design Prompts

1. **The model is a thinking partner, not an oracle.** Its design suggestions generalize across fields; your discipline's norms and your committee's expectations override generic advice.
2. **Preregister what matters.** Questions, hypotheses, measures, and analysis choices fixed in advance are your protection against post-hoc storytelling — yours and the model's.
3. **Every design has unaddressed threats.** The honest limitation section beats the defensive one; reviewers trust candor and punish discovery.
4. **Feasibility is a design constraint, not a confession.** A smaller question answered well outperforms a grand question abandoned at year two.
