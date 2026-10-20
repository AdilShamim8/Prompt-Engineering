# Performance Management & Feedback Prompts

Companion prompts to the main HR guide for the performance cycle: goal setting, check-ins, reviews, and difficult conversations. The boundary from the main guide applies with full force — AI structures the process and drafts communications; evaluation, ratings, and employment decisions belong exclusively to accountable humans applying defined criteria.

***

## 1. Goal-Setting Facilitation

**Prompt:**
```
Act as a performance management facilitator. Help me convert this raw
aspiration into well-formed goals: [DESCRIBE ROLE + WHAT THE EMPLOYEE AND
MANAGER WANT TO ACHIEVE THIS PERIOD].
For each goal:
1. The outcome phrasing — what changes in the world, not what activities
   happen.
2. The measure: how we'll know it happened, with the evidence source.
3. The stretch calibration: is this achievable-in-period or aspirational?
   Flag any goal that is actually two goals fused together.
4. The dependency audit: what this goal assumes others will do — and what
   happens to the goal if they don't.
5. The controllability check: how much of the outcome does the employee
   actually control? Flag goals that measure team or market results where
   individual contribution is partial.
```

- **Purpose:** Goals that measure the employee's actual work, not luck or other people's output.
- **Why it works:** The controllability check fixes the most demoralizing goal-design failure: being measured on outcomes you cannot fully influence.
- **Use Case:** Quarterly/annual goal setting; OKR facilitation.
- **Expert Variation:**
```
Add the mid-period tripwire: for each goal, the leading indicator that says
early whether it is off track — check-in questions attach to that, not to
the deadline.
```

***

## 2. The Ongoing Check-In Template

**Prompt:**
```
Design the lightweight check-in for [CADENCE — weekly/biweekly] between
[ROLE] and their manager. Constraints: 20 minutes max, must surface
blockers early, must not feel like surveillance.
1. The three fixed questions — progress, obstacles, needs — phrased to get
   specifics ("what's slowing you down" not "how's it going").
2. The goal-attachment: how current goals stay visible without dominating
   every conversation.
3. The psychological safety layer: how the format makes surfacing problems
   early the NORM — what the manager does with bad news the first time
   determines whether it ever gets shared again.
4. The capture rule: what gets recorded (one line) and what stays
   conversational — over-documentation kills honesty.
```

- **Purpose:** Frequent, honest signal between review cycles.
- **Why it works:** The "what the manager does with bad news" clause addresses the real mechanism of check-in failure — it is a trust behavior, not a template.
- **Use Case:** Managers at any level; especially remote teams.
- **Expert Variation:**
```
Add the skip-level variant: how a manager-of-managers checks in without
undermining the direct reporting line.
```

***

## 3. Review Drafting (Evidence First)

**Prompt:**
```
I am writing a performance review for [ROLE]. My evidence file: [PASTE —
specific accomplishments, incidents, metric contributions, gathered over
the period]. Rating framework: [YOUR COMPANY'S FRAMEWORK].
1. Organize the evidence into: strengths demonstrated (with examples),
   impact delivered (with measures where available), growth areas (with
   examples), and questions the evidence does NOT answer.
2. Draft the narrative sections in factual, specific language — every
   claim tied to the evidence I provided; flag any claim I am tempted to
   make that the evidence does not support.
3. The calibration check: does my draft language match the rating I intend
   — or does the prose say "met expectations" while the rating says
   "exceeds"? Inconsistencies here drive appeals.
4. The feedforward section: next period's growth focus, phrased as
   opportunities with support, not verdicts.
5. What's missing: what evidence should I gather before finalizing?
```

- **Purpose:** Reviews built from evidence rather than recency and halo effects.
- **Why it works:** The narrative-rating consistency check prevents the single most common review failure mode — prose and score disagreeing, which every appeals process exploits.
- **Use Case:** Annual/semiannual reviews; probation conclusions.
- **Expert Variation:**
```
Add the bias self-audit: against my draft — did recency dominate? Did one
strong incident color everything? Is language warmer for some employees
than others for equivalent evidence? (Check adjectives specifically.)
```

**Limitations & verification:** Reviews contain sensitive personal data — draft in approved systems with anonymized prompting only (see the main guide's privacy rules). The rating decision and its justification are the manager's, with HR oversight per your process; AI organizes evidence and language, nothing more.

***

## 4. The Difficult Feedback Conversation

**Prompt:**
```
Prepare a performance conversation about: [THE ISSUE — pattern of missed
commitments, quality below role expectations, behavioral friction].
Facts I can cite: [SPECIFIC INCIDENTS WITH DATES/EFFECTS — no character
interpretations].
1. The SBI-D draft: Situation, Behavior, Impact, and the specific Desired
   change — in under 5 sentences, no euphemisms, no stack of adjectives.
2. The opener: the first 2 sentences verbatim — the part that cannot be
   improvised well.
3. Their likely responses (defensiveness, deflection, agreement-with-no-
   change, genuine surprise) — and my reply to each that acknowledges
   without conceding the issue.
4. The support offer: what help I can genuinely provide — training,
   workload adjustment, clearer priorities — offered as real options, not
   rhetoric.
5. The documentation: what I record afterward, factual and dated.
6. If this is a formal performance warning track: flag it — that process
   follows HR procedure and this prep does not substitute for it.
```

- **Purpose:** Hard conversations delivered clearly, fairly, and with a path forward.
- **Why it works:** Pre-scripted openings and anticipated responses keep the manager composed through the moments where composure usually fails.
- **Use Case:** Performance issues; behavior corrections; quality conversations.
- **Expert Variation:**
```
Add the dignity audit: read the draft as the employee would at their most
vulnerable — is anything needlessly wounding? Clarity is required; cruelty
is optional and counterproductive.
```

**Limitations & verification:** Anything entering formal performance management follows your organization's HR process with proper documentation and, where applicable, union and legal considerations. This preparation supports the conversation; the process governs the consequences.

***

## 5. Underperformance Diagnosis (Cause Before Cure)

**Prompt:**
```
An employee's performance has declined: [DESCRIBE THE CHANGE — from what
to what, over what period, in what areas].
1. The differential diagnosis, ordered by how often each cause is missed:
   role ambiguity, skill gap, workload saturation, broken tools/processes,
   interpersonal friction, manager relationship, personal circumstances,
   health, values mismatch, burnout.
2. For each plausible cause: the observable evidence that would confirm or
   eliminate it — and who holds that information.
3. The conversation plan that explores causes WITH the employee rather than
   presenting a conclusion.
4. The matched responses: what support fits each confirmed cause — and the
   honest cases where the right answer is a role change rather than
   improvement plans.
5. What I should NOT do yet — premature formal processes based on
   undiagnosed causes create legal risk and destroy trust.
```

- **Purpose:** Diagnosing before prescribing — most "performance problems" are system or situation problems wearing a person's name.
- **Why it works:** The cause-matching and the "what not to do yet" section counteract the reflex to jump to performance improvement plans when the actual cause is workload or ambiguity.
- **Use Case:** Any sustained performance change; also for teams (multiple employees declining = look at the system first).

**Limitations & verification:** Health, family, and personal circumstances belong to the employee to share or not — the exploration creates space; it never interrogates. Formal processes and accommodations involve HR and follow legal requirements.

***

## 6. Calibration Meeting Preparation

**Prompt:**
```
Prepare the manager for the calibration meeting. Our proposed ratings:
[PASTE — anonymized: role level, proposed rating, one-line evidence basis
per employee].
1. The consistency audit: for each pair of similar-evidence employees with
   different proposed ratings — what justifies the difference? Flag any
   gap that cannot be articulated.
2. The distribution sanity check: does our proposed spread match the
   company's guidance? Where we deviate, is it defensible evidence-wise
   or comfort-wise?
3. The language audit: are our one-line evidence summaries equally
   specific across employees — or vaguer for some (a classic bias
   hiding spot)?
4. The challenge preparation: for the 3 ratings most likely to be
   challenged in calibration, the 30-second evidence case each.
5. The appeal risk: which ratings, if appealed, have the weakest
   documentation trail — and what to strengthen before submitting.
```

- **Purpose:** Fair, defensible ratings that survive calibration and appeals.
- **Why it works:** The pairwise consistency audit and specificity audit target the documented mechanisms by which bias survives "objective" processes.
- **Use Case:** Review cycles; promotion committees (adapted).

**Limitations & verification:** All data here must be anonymized before prompting — calibration material is exactly the sensitive class that belongs in approved systems. Final ratings follow your company's governance, not this preparation.

***

## Shared Verification Rules for All Performance Prompts

1. **Decisions stay human.** AI may structure evidence, draft language, and prepare conversations — ratings, consequences, and employment decisions belong to accountable managers with HR oversight.
2. **Anonymize before prompting.** Performance data is sensitive personal data; patterns and roles, not names and details, are what these prompts need (see the main guide's privacy rules).
3. **Evidence precedes language.** Write from documented specifics gathered over the period; a review is testimony, not literature.
4. **The process is protection.** For formal tracks — warnings, PIPs, terminations — your organization's procedure, documentation requirements, and legal review govern everything; these prompts operate in the preparation layer only.
