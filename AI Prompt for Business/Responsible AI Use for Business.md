# Responsible AI Use for Business

Guidance companion to the business prompt collections. The main guide and its companion files produce drafts, analyses, and options — this file defines the guardrails that keep those outputs safe to act on. It exists because the highest-value business uses of AI (research, forecasting, communications, people decisions) are also the ones with the highest cost of being wrong.

***

## 1. The Fabrication Risk in Business Content

Language models generate plausible text. Plausible is not the same as correct, and business use amplifies the difference: a fabricated statistic in an internal memo becomes a decision input; in a client deck it becomes a liability.

**Where fabrication bites hardest in business contexts:**

- **Market data**: "The market is growing at 15% annually" — invented growth rates, market sizes, and competitor revenues stated with full confidence
- **Citations**: articles, reports, and studies that do not exist, or exist but say something different
- **Competitor claims**: capabilities, pricing, and strategies the model cannot actually know
- **Regulatory statements**: rules that sound right but are outdated, jurisdiction-wrong, or invented
- **Quotes and precedents**: attributed statements no one made

**The working rule:** treat every factual claim in AI output as a placeholder marked "verify" — because that is what it is. The prompt patterns in the other business files consistently ask the model to separate evidence from inference; this habit exists precisely to make verification tractable.

***

## 2. Market Research Prompts Without Fabricated Data

The safest architecture for market questions separates what the model does well (structuring the research) from what it does badly (supplying the facts):

**Use AI for:**
- Designing research plans and question lists
- Structuring frameworks (segmentation axes, competitive dimensions, TAM logic)
- Synthesizing documents YOU provide
- Drafting interview guides and survey questions
- Challenging your conclusions with structured skepticism

**Do not use AI for:**
- Actual market sizes, growth rates, or shares — source these from reports you possess, filings, or paid databases
- Competitor internals — no model knows a private company's roadmap
- Anything where "confidently plausible" is indistinguishable from "made up" until it is too late

**Verification prompt pattern:**

```
Here is my draft market analysis: [paste]. Review it as a skeptical analyst:
1. List every factual claim that requires an external source to stand.
2. Mark each claim: [I have a source] / [I need to find one] / [I assumed this].
3. For each "I assumed this": what would change if the assumption is wrong?
Do not add new claims — only audit what I wrote.
```

***

## 3. Confidentiality & Data Handling

**Before pasting into an AI tool, classify the material:**

| Classification | Examples | Handling |
| :-- | :-- | :-- |
| Public | Published reports, released products, job posts | Fine anywhere |
| Internal | Unreleased plans, budgets, org changes | Enterprise tools with data agreements only |
| Confidential | Customer data, contracts, pricing, M&A | Anonymize heavily or do not use AI |
| Regulated | PII, health, financial records subject to law | Only in compliant, approved systems |

**Anonymization that actually works for business prompts:**

```
Before: "Acme Corp, our biggest customer at $2.4M ARR, is threatening to churn."
After:  "CUSTOMER_A (annual revenue band: $2-3M) is showing churn signals."
```

The analysis survives; the leak surface shrinks. Re-identify on your side of the tool, in your documents.

**The "would I email this to a stranger?" test:** if the answer is no, it does not belong in a consumer AI tool — regardless of how useful the output would be.

***

## 4. Human Judgment Boundaries

Some business decisions must remain human even when AI has informed them:

**Decisions affecting people** — hiring, firing, promotion, compensation: AI may structure criteria or draft communications, but the decision and its justification belong to accountable managers, with HR oversight. (See the HR collection for the full framework.)

**Decisions with legal exposure** — contracts, regulatory filings, public commitments: AI drafting is a first pass; attorneys and compliance own the final word.

**Decisions under genuine uncertainty** — strategy, investment, market entry: use AI to widen the option set and stress-test reasoning (pre-mortems, red teams, scenario matrices). Do not use it to outsource the judgment: the model bears none of the consequences, and its "recommendation" is a continuation of your framing, not independent wisdom.

**The signature failure mode** is not AI making bad decisions — it is humans deferring responsibility to AI output as if it were diligence. "The analysis said so" is never a defense; "here is the analysis, here is what we verified, here is our reasoning" is a workflow.

***

## 5. Attribution & Disclosure Practices

**Internally:** if AI materially shaped an analysis your name is on, say so in the document's method note ("AI-assisted draft; data and conclusions verified by [name]"). Your credibility compounds; unacknowledged shortcuts eventually surface.

**With clients:** follow the disclosure norms of your industry and jurisdiction, which are tightening. Where the output is substantially AI-generated analysis, clients generally deserve to know the methodology — the same way they deserve to know the methodology of any consulting work.

**In published content:** marketing claims generated by AI require the same substantiation as any other claim (see the Marketing collection's verification prompts) — regulators do not grade on a curve for AI-assisted claims.

***

## 6. A Business AI-Use Policy Starter

For small teams adopting AI without a formal policy, this five-line starter prevents most incidents:

```
1. Verify before circulating: every fact, number, and citation in AI output is
   checked by the human who sends it.
2. Classify before pasting: public / internal / confidential / regulated —
   and match the tool to the class.
3. People decisions stay human: AI never decides, scores, or filters on hiring,
   promotion, or termination.
4. Label AI involvement: method notes for internal analysis; disclosure where
   clients or the public would expect it.
5. Log the load-bearing uses: which recurring decisions use AI, so we can
   review them when tools change.
```

Review the policy quarterly — the tools change faster than policies do.

***

## Verification Checklist for Business AI Outputs

```
[ ] Every number traced to a source I can point to
[ ] Market/competitor claims sourced from documents I hold, not model memory
[ ] Citations exist and say what the output claims
[ ] Confidential data was never pasted into an unapproved tool
[ ] People-affecting content reviewed by the accountable human (and HR where applicable)
[ ] Legal-adjacent content reviewed by counsel
[ ] The recommendation's assumptions are stated and I could defend them
[ ] My name on it means I verified it
```
