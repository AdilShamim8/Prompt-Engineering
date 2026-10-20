# Ethical Marketing & Claims Verification Prompts

Companion guide to the main marketing collection. Marketing sits under more legal and ethical scrutiny than any other business function — and AI has raised the stakes by making fabricated testimonials, invented statistics, and confident-sounding claims nearly free to produce. This file builds the verification and ethics layer that keeps the rest of the collection's output publishable.

***

## 1. The Claims Substantiation Discipline

Every factual claim in marketing copy is a legal and ethical commitment. The working rule across most advertising regimes: claims must be substantiated BEFORE they run — not defended after.

**The claim inventory habit:**

```
Before any campaign ships, extract every checkable claim:
- Product performance claims: "fastest", "2x quicker", "saves 10 hours"
  → SOURCE: what test, what methodology, when?
- Comparative claims: "better than [competitor]"
  → SOURCE: what comparison, measured how, current?
- Statistics: "73% of users report..."
  → SOURCE: what study, whose sample, verifiable where?
- Superlatives and absolutes: "best", "only", "never"
  → each is a claim requiring proof or a rewrite
- Implied claims: imagery and demos implying outcomes
  → would a reasonable viewer infer something we cannot support?
```

**The verification prompt:**

```
Audit this marketing copy as an advertising-standards reviewer: [PASTE].
1. List every factual and comparative claim.
2. For each: what substantiation it requires, and the classification
   — [WE HAVE THE EVIDENCE] / [EVIDENCE EXISTS SOMEWHERE — FIND IT] /
   [UNSUPPORTABLE — REWRITE OR CUT].
3. Flag implied claims from imagery, demonstrations, and examples the
   copy pairs with.
4. Rewrite the unsupportable claims at honest strength levels.
```

***

## 2. Fabricated Testimonials & Social Proof

AI can generate person-shaped testimonials, reviews, and case studies on demand. Using them as if real is both illegal in most jurisdictions (fake reviews and undisclosed testimonials attract enforcement) and strategically corrosive (fabrication discovered is a brand-ending event).

```
THE HARD LINES:
- Never generate testimonials, reviews, or quotes attributed to real-
  sounding people and present them as authentic customer voices.
- Never fabricate statistics about customer satisfaction or results.
- Never invent case-study details — company size, outcomes, timelines.
- Never create fake "user" accounts, ratings, or engagement.

THE HONEST ALTERNATIVES:
- Real testimonials, with permission and required disclosures.
- Clearly labeled illustrative scenarios ("Here's how it works for a
  team like this one..." — not "Here's what Sarah from Denver said").
- Aggregate claims from real, methodologically defensible surveys.
- If proof does not exist yet: run the pilot, collect the evidence,
  then market it. The wait is shorter than a retraction.
```

**The disclosure prompt:**

```
Here are our real testimonials and endorsements: [PASTE]. Check:
1. Disclosure needs: which are paid, incentivized, or from affiliates —
   and the disclosure language each requires per advertising rules in
   [OUR JURISDICTIONS].
2. Material connections: anything about the endorser (employee,
   investor, free product) a reasonable consumer would want to know.
3. Typicality: results claimed that are NOT typical — needing "results
   vary" honesty or reselection.
4. Permission status: flag any testimonial lacking documented consent
   to use [WHERE, HOW LONG].
```

***

## 3. AI-Generated Marketing Content Boundaries

Where the tools genuinely help, and where they cross lines:

**Appropriate:** drafts for human editing, variation generation for testing, translation with review, accessibility adaptations, internal brainstorming, summarizing real customer feedback, formatting and repurposing verified content.

**Requires strict control:**
- Any factual content (statistics, comparisons, feature descriptions) — model memory is not substantiation; every claim traces to a real source or gets cut
- Imagery of "customers" and realistic people — check platform and jurisdiction rules on synthetic media disclosure; undisclosed photorealistic fakes erode the trust everything else depends on
- Anything resembling reviews, testimonials, or user voices — see Section 2

**Never:** fabricated data presented as research, competitor misinformation, deceptive dark patterns, engagement bait engineered to mislead, or disclosure evasion of any kind.

**The pre-flight check for AI-assisted campaigns:**

```
[ ] Every factual claim verified against sources we hold
[ ] Every testimonial/review is real, permitted, and disclosed
[ ] Every statistic has a methodology we could defend publicly
[ ] Imagery of people: either real-with-rights or clearly-labeled synthetic
[ ] Comparisons are current, measured, and fair
[ ] Nothing implies outcomes the product cannot deliver
[ ] The person approving this could defend every element on a recorded call
```

***

## 4. Copyright & IP Considerations

Marketing constantly borrows — language, imagery, music, formats. AI has made accidental infringement easier and clearance discipline more important.

```
THE WORKING RULES:
1. Generated text can echo existing works: distinctive slogans, taglines,
   and lyrics can be reproduced from training data. Run uniqueness checks
   on anything that will appear large on a billboard or in a trademark
   filing.
2. Generated images carry unresolved legal questions about ownership and
   similarity to artists' work — for commercial use, prefer tools with
   explicit commercial terms, keep generation records, and treat
   lookalike-of-known-style requests as a no.
3. Music, fonts, stock: each has license terms marketing teams violate
   casually — the license file for every campaign asset should be as
   findable as the asset itself.
4. Competitor material: never paste competitor copy into AI tools to
   "rewrite" it — the output can retain protectable expression and the
   intent looks bad in discovery.
5. When in doubt: counsel reviews assets BEFORE launch, when changes
   cost hours, not after, when they cost campaigns.
```

***

## 5. Vulnerable Audiences & Fair Persuasion

Persuasion has an ethical gradient even where it has a legal green light:

**Prompt (for campaign review):**

```
Review this campaign for persuasion ethics beyond legal compliance:
[PASTE CAMPAIGN].
1. Vulnerability check: does the targeting or messaging exploit
   [FINANCIAL HARDSHIP / HEALTH ANXIETY / AGE / INSECURITY] — where
   our persuasion pressure lands on someone's weakest moment?
2. The clarity test: would the average target customer, seeing only
   the subject line or thumbnail, accurately predict what they're
   getting? (Curiosity is fine; bait-and-switch is not.)
3. The pressure audit: countdown timers, scarcity claims, "last chance"
   — which are TRUE, and which are manufactured urgency?
4. The unsubscribe-of-the-mind: does our funnel make saying "no" as
   easy as saying "yes"? Dark patterns convert by trapping, and
   trapped customers become detractors with receipts.
5. The defense test: if this campaign were read aloud in a room of our
   sharpest customers, would we be comfortable — or explaining?
```

***

## 6. Responsible Marketing Policy Starter

For teams formalizing this without a large legal function:

```
OUR CLAIMS STANDARDS:
1. Substantiation before publication — every claim traces to evidence
   we hold, or it does not run.
2. Real testimonials only, with permission and disclosure.
3. No fabricated statistics, reviews, or social proof, ever.
4. Comparisons: current, measured, fairly framed.
5. AI-generated content: verified line-by-line like any junior
   copywriter's work — enthusiasm is not evidence.

OUR PRACTICES:
6. Urgency only when real; scarcity only when true.
7. Easy exit from every funnel — the "no" path as smooth as the "yes".
8. Vulnerable audiences get extra care, not extra targeting.
9. Licensing records for every external asset, before launch.
10. A named human signs off on every campaign's claims — AI drafts,
    humans own.
```

Review quarterly: advertising rules, platform policies, and AI capabilities all move — and the enforcement climate has been tightening, not loosening.

***

## Where the Authority Lives

This file encodes widely shared advertising-standards principles (truthful claims, substantiation, disclosure) — but the binding versions are your jurisdictions' advertising regulations and platform policies, which vary and change. Before campaigns with material exposure, marketing leadership and counsel confirm current requirements. **Treat this collection's prompts as the compliance culture, and counsel as the compliance authority** — working together, in that order.
