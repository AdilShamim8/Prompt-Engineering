# Email & Lifecycle Marketing Prompts

Companion prompts to the main marketing guide for the highest-ROI channel and the journeys that turn one-time buyers into relationships: email programs, lifecycle automation, deliverability, and the list hygiene that keeps all of it working.

***

## 1. Lifecycle Journey Architecture

**Prompt:**
```
Design our lifecycle email architecture. Business: [MODEL — SaaS / e-com /
services]. Key funnel moments: [SIGNUP, FIRST PURCHASE, USAGE PATTERNS,
RENEWAL POINTS]. List maturity: [SIZE, ENGAGEMENT STATE].
1. The journey map: the 4-6 lifecycle stages (welcome → activation →
   habit → retention/expansion → winback) — with the BEHAVIORAL
   trigger that moves a person between stages (behavior beats time for
   everything except time-based products).
2. The program inventory: per stage, the sequence(s), their single
   job, and their success metric — one job per sequence, no sequence
   trying to do three things.
3. The global guardrails: frequency caps across ALL programs (the sum
   of sequences, not each one, is what the subscriber experiences),
   suppression rules, and the preference center that lets people
   choose topics instead of leaving entirely.
4. The empty-state honesty: what we need BEFORE this works (data
   triggers firing, content for each stage, the exit conditions for
   every sequence — including "stop emailing someone who just
   converted").
```

- **Purpose:** A lifecycle system designed around behavior, with the global frequency view most programs lack.
- **Why it works:** Frequency caps across programs and exit conditions are the two systematic failures that quietly destroy engagement while each individual sequence looks innocent.
- **Use Case:** Program design; CRM migrations; engagement recovery.
- **Expert Variation:**
```
Add the decay design: what happens when a subscriber stops engaging —
the sunsetting path (reduction → re-engagement attempt → sunset) that
protects deliverability by letting go.
```

***

## 2. Welcome Sequence Engineering

**Prompt:**
```
Design our welcome sequence for: [WHO JUST JOINED + WHY — what they
opted in FOR]. The promise we made: [THE SPECIFIC LEAD MAGNET /
SIGNUP PROMISE].
1. The promise-keeping audit: email 1 delivers [THE THING] within
   minutes, with zero friction — everything else waits. (The promise
   is the contract; breaking it in email 1 is why sequences die.)
2. The arc: 4-6 emails over [TIMELINE] — each with one job, sequenced
   from highest-value-first: deliver, orient, prove, invite, convert.
3. The subject line discipline: expectation-setting over cleverness —
   the welcome sequence trains recipients on what your emails are;
   clickbait training produces clickbait-openers, not customers.
4. The personalization reality: what data do we ACTUALLY have at
   signup — and the personalization built only on real data, not the
   imagined kind.
5. The measurement: open-to-click by email, the drop-off email, and
   the one number that defines welcome success: [DEFINE — e.g.,
   activation rate within 14 days].
```

- **Purpose:** The sequence with the highest engagement any brand will ever send, engineered to earn the next hundred.
- **Why it works:** Promise-keeping as the organizing principle converts the welcome from a sales ramp into trust-building — which is what the data rewards anyway.
- **Use Case:** New lists; lead magnet funnels; onboarding-email redesigns.
- **Expert Variation:**
```
Add the segment-aware version: how the sequence branches for [KNOWN
SEGMENTS AT SIGNUP] — and the honest note when segmentation's lift
does not justify its complexity at our list size.
```

***

## 3. Deliverability Health Check

**Prompt:**
```
Diagnose our deliverability. Symptoms: [OPEN DECLINE / INBOX PLACEMENT
ISSUES / SPIKE IN COMPLAINTS / BOUNCES]. Current state: [VOLUME,
FREQUENCY, LIST GROWTH METHOD, ENGAGEMENT BY SEGMENT].
1. The diagnostic order: authentication (SPF/DKIM/DMARC — the
   foundational layer, check first), then list hygiene (aged,
   unengaged, purchased-ish), then content/engagement signals, then
   infrastructure (sending domain strategy, warm-up state for new
   programs).
2. The engagement math: what share of our list has opened NOTHING in
   90/180/365 days — and the hard truth about what that means for
   our sender reputation (ISPs grade us by our worst sends, not our
   best).
3. The hygiene plan: the sunset sequence design, the removal criteria,
   and the segment we should stop mailing entirely — with the
   short-term metrics sacrifice stated honestly (removing names
   hurts average metrics immediately and improves delivery
   everywhere).
4. The monitoring setup: what to watch weekly (complaint rate,
   bounce rate, authentication pass) — with the thresholds that
   trigger action.
```

- **Purpose:** Deliverability treated as the system property it is, rather than a content-tweak mystery.
- **Why it works:** The diagnostic order (authentication → hygiene → engagement → infrastructure) matches how deliverability actually fails, and the "worst sends" framing explains why list pruning raises results while lowering averages.
- **Use Case:** Declining engagement; platform migrations; pre-launch preparation.
- **Expert Variation:**
```
Add the platform checklist: our ESP's specific deliverability tooling
(postmaster tools, dedicated vs shared IP decision logic) — and the
questions to ask their support that we should have asked months ago.
```

**Limitations & verification:** Authentication and platform specifics are verifiable facts — confirm actual SPF/DKIM/DMARC state with your technical team or domain tools rather than assumptions; inbox placement varies by recipient provider and is only truly known through seed testing and platform data.

***

## 4. Re-Engagement & Winback

**Prompt:**
```
Design the winback program for our lapsed audience: [DEFINE LAPSED —
no purchase in X / no opens in Y]. Business context: [PRODUCT,
REPURCHASE CYCLE, WHY PEOPLE LAPSE IF KNOWN].
1. The lapse taxonomy: distinguish accidental lapsers (never
   re-onboarded, payment failed, life happened) from deliberate
   lapsed (product fit gone) — the messages that work for one insult
   the other.
2. The sequence: 3-4 touches over [TIMELINE] — the honest "are we
   still relevant to you" question beats the fake party ("We miss
   you!!"). Offer escalation only if the relationship merits it.
3. The exit design: the final email that makes leaving clean —
   including the one-click unsubscribe that protects both their time
   and our deliverability.
4. The measurement: winback rate by segment, the long-term value of
   re-won subscribers versus new ones (often better — they already
   knew how to buy), and the sunset criteria that end the program's
   chasing.
```

- **Purpose:** Winning back the winnable, releasing the rest with grace.
- **Why it works:** The lapse taxonomy prevents the tone failure that dominates winback programs: celebrating at people who quietly decided to leave.
- **Use Case:** E-com repurchase; subscription lapses; newsletter dormancy.

***

## 5. Email Content System (Sustainable Production)

**Prompt:**
```
Build our email content system. Sending cadence: [FREQUENCY]. Content
sources available: [BLOG, PRODUCT UPDATES, COMMUNITY, CUSTOMER
STORIES, DATA]. Team capacity: [HOURS PER WEEK].
1. The format portfolio: 3-5 repeatable formats (e.g., one big idea /
   link roundup / product story / customer proof / quick tip) —
   recurring formats lower production cost and train reader
   expectations.
2. The template architecture: one flexible template covering all
   formats (consistent sender identity; modular body) — and the
   plain-text-vs-designed decision per format with its honest
   tradeoffs (plain text often outperforms for relationship
   emails; designed wins for product showcase).
3. The subject line system: our voice rules, length discipline,
   A/B testing cadence (one variable, real sample), and the banned
   moves (deceptive urgency, false personalization, ALL CAPS
   desperation).
4. The production calendar: sustainable weekly rhythm with named
   inputs per format — designed so a bad week produces a smaller
   email, not a missed one.
```

- **Purpose:** Email production that survives real team capacity.
- **Why it works:** The recurring-format portfolio and the "smaller email, not missed email" degradation rule keep consistency — the variable email marketing actually rewards above all others.
- **Use Case:** Newsletter programs; lifecycle content feeds; solo marketers.
- **Expert Variation:**
```
Add the repurposing map: each format's source content reused across
[OUR OTHER CHANNELS] — one production effort, multi-channel assets.
```

***

## 6. Privacy & Preference Hygiene

**Prompt:**
```
Audit our email program's consent and preference practices. Current
setup: [HOW PEOPLE JOIN, WHAT THEY AGREE TO, UNSUBSCRIBE PATH,
PREFERENCE OPTIONS IF ANY].
1. The consent clarity audit: what subscribers actually agreed to —
   and where our sending exceeds it (the "signed up for a whitepaper,
   now gets 3 promos weekly" gap that regulations and reputations
   both punish).
2. The unsubscribe friction test: how many clicks, how fast, does it
   actually work — and the sneaky frictions (login walls, "tell us
   more" interruptions) that convert unsubscribes into spam
   complaints.
3. The preference center design: topic choice, frequency choice —
   giving subscribers control as the retention alternative to
   leaving.
4. The regulatory flag list: consent documentation, special
   categories, and jurisdictional requirements — flagged for the
   privacy/legal owner, never self-certified by marketing.
```

- **Purpose:** The email program's license to operate, kept clean.
- **Why it works:** The consent-exceeded gap and friction test target the two practices that feel like marketing wins and function as reputation debt.
- **Use Case:** Annual audits; pre-platform-migration; complaint-rate recovery.
- **Expert Variation:**
```
Add the trust dividend argument: how making leaving easy paradoxically
increases staying — the data-backed case for marketing to fewer
people more respectfully.
```

**Limitations & verification:** Email marketing law (CAN-SPAM, GDPR, CASL, and others) varies by jurisdiction and is the compliance owner's call — this audit surfaces the questions; counsel and your privacy team answer them.

***

## Shared Verification Rules for All Email Prompts

1. **Test sends before real sends.** Rendering across clients, links, merge fields, and the plain-text version — every campaign gets the checklist.
2. **List data is personal data.** Segmentation dumps and subscriber details stay in your ESP and approved systems; prompts need patterns and structures, not exports.
3. **One variable per test.** Subject line tests that also changed send time measured nothing; keep experimental discipline even under campaign pressure.
4. **Averages lie at scale.** Segment results before concluding — one strong cohort routinely disguises a failing program in blended metrics.
