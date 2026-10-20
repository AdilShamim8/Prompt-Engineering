# Operations & Process Optimization Prompts

Companion prompts to the main business guide for documenting, streamlining, and scaling how work actually gets done. The guiding principle: AI can structure process knowledge and expose waste, but the people doing the work hold the ground truth.

***

## 1. Process Documentation from an Interview

**Prompt:**
>Act as a process analyst. I will describe how we currently handle [PROCESS] — my description will be messy. Interview me first: ask the 5 questions whose answers would most improve a process map. Wait for my answers. Then produce:
>
>1. A step-by-step map (numbered, with the responsible role per step)
>2. Decision points, marked where the path forks
>3. Handoffs between people or systems, flagged as risk points
>4. Any step where my description was ambiguous — listed as "unverified"

- **Purpose:** Turning tribal knowledge into documented process without a consultant.
- **Why it works:** The interview-first pattern gathers the context that process descriptions always omit.
- **Use Case:** Onboarding documentation, SOP creation, audit preparation.
- **Expert Variation:**
>Add a RACI summary (Responsible, Accountable, Consulted, Informed) per step, and flag steps where the same person holds R and A with no review.

**Limitations & verification:** The map is only as complete as your memory. Validate the draft with a second person who runs the process — the differences between their account and yours are usually the most valuable finding.

***

## 2. Waste Pattern Analysis

**Prompt:**
>Here is our process for [PROCESS]: [paste or describe steps with rough time per step]. Analyze it for the classic waste patterns:
>
>1. Waiting (queue time between steps)
>2. Rework (steps that fix earlier steps' outputs)
>3. Overprocessing (work beyond what the customer needs)
>4. Handoff friction (approvals, format conversions, re-entry)
>5. Batch problems (work piling up at specific steps)
>
>For each pattern found: quote the step(s), estimate the drag, and propose one experiment to reduce it. Rank the findings by expected improvement per unit of effort.

- **Purpose:** A structured efficiency review that goes beyond "make it faster."
- **Why it works:** Named waste categories turn vague frustration into specific, attackable problems.
- **Use Case:** Cycle-time reduction, cost-per-unit improvement, quality programs.

**Limitations & verification:** Estimates of "drag" are hypotheses, not measurements. Instrument the process (timestamps, counts) before and after any change; kill experiments that the data does not support.

***

## 3. SOP Drafting with Edge Cases

**Prompt:**
>Draft a standard operating procedure for [TASK]. Context: performed by [ROLE], frequency [RATE], current failure modes: [list what goes wrong today].
>
>Structure:
>1. Purpose and scope (when NOT to use this SOP)
>2. Prerequisites and access needed
>3. Steps, numbered, each with: action, expected result, and what to do if the expected result does not occur
>4. Escalation path with specific triggers
>5. 3 common mistakes and how to avoid them
>6. A 5-item checklist for the performer to run before declaring done

- **Purpose:** SOPs that survive contact with reality, including its failure modes.
- **Why it works:** Building known failure modes into the procedure beats pretending they do not happen.
- **Use Case:** Operations handbooks, support runbooks, compliance documentation.
- **Expert Variation:**
>Add a "last reviewed" header, a change log section, and a 5-question comprehension check for new hires to confirm the SOP is understandable by someone who has never done the task.

**Limitations & verification:** Run the draft alongside the real task once, and correct it where reality diverges. An SOP nobody has executed as written is a hypothesis.

***

## 4. Capacity & Bottleneck Diagnosis

**Prompt:**
>Act as an operations consultant. Demand arriving: [describe volume and pattern]. Resources: [people/stations/hours and their rates]. Current throughput: [actual output per period].
>
>1. Calculate the theoretical capacity of each stage — show your work.
>2. Identify the bottleneck and explain why it, specifically, limits throughput.
>3. Distinguish utilization problems (busy but not bottlenecked) from bottleneck problems.
>4. Propose 3 interventions: one that adds capacity, one that reduces demand on the bottleneck, one that smooths arrival variability.
>5. State what happens to total throughput if each works — with the arithmetic.

- **Purpose:** Finding the constraint mathematically instead of by who complains loudest.
- **Why it works:** Requires shown calculations that you can check against your own numbers.
- **Use Case:** Production planning, support staffing, fulfillment, hiring plans.
- **Expert Variation:**
>Add cost per unit of throughput gained for each intervention, and identify the next bottleneck that will appear once this one is relieved.

**Limitations & verification:** Recompute all capacity arithmetic yourself. Real systems hide variability (setup times, breaks, quality escapes) that simple rates miss; validate the diagnosis with a week of observed data.

***

## 5. Vendor & Tool Rationalization

**Prompt:**
>Help us consolidate overlapping tools. Current inventory: [list tools, purposes, costs, contract end dates, owner teams].
>
>1. Group tools by the job they do, and flag overlaps.
>2. For each overlap: the consolidation candidate, what we lose by consolidating, and what we save.
>3. Identify tools with no clear owner or no usage evidence — the "audit first" list.
>4. Build a 12-month consolidation sequence respecting contract dates and migration effort.
>5. List the risks specific to each migration (data loss, integration breakage, workflow disruption).

- **Purpose:** Turning tool sprawl into a deliberate portfolio.
- **Why it works:** Sequencing by contract dates makes the plan executable rather than aspirational.
- **Use Case:** SaaS cost reduction, IT portfolio management, post-merger integration.

**Limitations & verification:** Usage and integration claims must be verified in your admin consoles — the model sees only what you list. Never cancel based on the "no owner" flag alone; owners exist but are unrecorded more often than tools are truly orphaned.

***

## 6. Meeting & Workflow Overhead Audit

**Purpose-built for the most universal process problem: coordination cost.*
>
>**Prompt:**
>Here is how our team spends coordination time: [list recurring meetings with length, attendees, purpose; and our main async channels]. Audit this overhead:
>
>1. For each meeting: what decision or information transfer it exists for, and whether that could happen async.
>2. Total hours per week of coordination per person — show the arithmetic.
>3. The 3 changes with the best time-saved versus disruption ratio.
>4. What we would lose by making each change (be honest — some meetings earn their cost).

- **Purpose:** Reclaiming maker time without destroying necessary coordination.
- **Why it works:** Forces the arithmetic and the honest counter-argument together.
- **Use Case:** Team retro actions, org design, post-growth process cleanup.

**Limitations & verification:** Meeting value is partly invisible (trust, ambient context). Trial changes with a defined revert date rather than deciding permanently on paper.

***

## Shared Verification Rules for All Operations Prompts

1. **Watch the arithmetic.** Capacity math, time totals, and cost sums must be recomputed — calculation slips are the most common failure in operations prompts.
2. **The people doing the work are the ground truth.** Every documented process, waste finding, and SOP must be validated by the operators, not just their managers.
3. **Change with experiments, not edicts.** Prefer reversible trials with measured baselines over permanent redesigns based on analysis alone.
4. **Process documentation often contains sensitive detail.** System names, access patterns, and failure modes belong in internal repositories, not public AI tools (see repository privacy guidance).
