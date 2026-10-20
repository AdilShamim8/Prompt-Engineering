# Business Presentations & Storytelling Prompts

Companion prompts to the main business guide for building presentations and business narratives that survive a skeptical room. The consistent theme: structure and evidence first, slides second.

***

## 1. Presentation Storyline (Before Any Slides)

**Prompt:**
>Help me structure a [DURATION] presentation for [AUDIENCE] with the goal of [DECISION/OUTCOME]. Key evidence available: [list your facts, data, examples]. Counter-arguments I expect: [list].
>
>Build the storyline:
>1. The one-sentence takeaway — what the audience should believe or do when I stop talking
>2. The 3 supporting points, each with its strongest single piece of evidence
>3. The narrative arc: situation, complication, resolution — in my actual context
>4. Where the skeptic in the room will push back, and the slide/answer ready for each point
>5. What to cut: the 3 things I want to say that do not serve the takeaway

- **Purpose:** Deciding the argument before decorating it.
- **Why it works:** The "what to cut" requirement attacks presentation bloat at the source.
- **Use Case:** Board decks, steering committees, investor meetings, all-hands.
- **Expert Variation:**
>Draft the same storyline as a 300-word memo first. If the memo does not convince, the slides will not either — and this is the cheapest possible test.

**Limitations & verification:** The model cannot judge your credibility with this specific audience. Where it recommends assertive framing, calibrate to the trust you have actually earned.

***

## 2. Executive Summary Slide

**Prompt:**
>Draft the summary slide for: [paste presentation storyline or memo]. Rules:
>
>1. Headline states the message as a full sentence with the key number — not a topic label ("Revenue up 12% from retention, not price" not "Revenue Update")
>2. Maximum 4 supporting bullets, each under 15 words
>3. One visual concept suggested in words (what the chart would show)
>4. The "so what" line: the decision or action requested
>5. A version note: what changes if the audience is [ALTERNATE AUDIENCE]

- **Purpose:** The slide that gets photographed, forwarded, and quoted — make it carry the argument.
- **Why it works:** Message headlines (assertions, not labels) are the single highest-leverage slide habit.
- **Use Case:** Deck openings, one-pagers, leave-behinds.
- **Expert Variation:**
>Write three headline variants — analytical, outcome-focused, and challenge-framed — and pick based on the audience's current mood toward the topic.

**Limitations & verification:** Every number in the headline must be traceable to your source data. The model will happily round 11.6% into "12%" — check that rounding does not change the story.

***

## 3. Data Storytelling

**Prompt:**
>Help me present this data honestly and memorably: [paste table or describe dataset]. Audience: [WHO]. Decision it supports: [WHAT].
>
>1. The 3 candidate stories this data could tell — including the boring one
>2. For the strongest story: the chart type and why (state what it hides, too)
>3. The annotation plan: the single number, label, or comparison line that makes the point unmissable
>4. The honest-caveats list: what this data does not support, stated in audience-safe language
>5. One sentence I say while the chart is up — the words that do the work

- **Purpose:** Charts that argue rather than decorate, without crossing into manipulation.
- **Why it works:** Requiring "what it hides" and honest caveats keeps the storytelling on the right side of the line.
- **Use Case:** Results reviews, metric deep-dives, board reporting.
- **Expert Variation:**
>Add a pre-mortem: if this chart gets taken out of context on social media, what does it falsely suggest? Fix the design so it survives screenshotting.

**Limitations & verification:** Verify chart-type advice against your actual data shape (time series, distribution, comparison). A beautifully argued chart on the wrong data structure misleads everyone, including you.

***

## 4. Objection Handling Structure

**Prompt:**
>I am presenting [PROPOSAL] to [AUDIENCE]. Strongest likely objections: [list, or ask me to brainstorm]. For each:
>
>1. The valid core of the objection — steelman it in 2 sentences
>2. My response: evidence-first, one paragraph, acknowledging any real trade-off
>3. The visual or proof point that makes the response land
>4. A fallback position if the objection wins on the merits — what I can concede without losing the proposal

- **Purpose:** Walking in with answers prepared for the pushback you know is coming.
- **Why it works:** Steelmanning first keeps responses from sounding defensive.
- **Use Case:** Budget approvals, strategy proposals, contentious findings.
- **Expert Variation:**
>Role-play the two hardest audience members: write their opening attack on my proposal, then my first 2 sentences in response.

**Limitations & verification:** If any prepared response relies on numbers, verify them twice — an objection-handling slide with a wrong figure converts a skeptic into an opponent.

***

## 5. Narrative for Change Communication

**Prompt:**
>Draft the narrative for announcing [CHANGE] to [AUDIENCE]. Context: [what is changing, why, who is affected, what stays the same].
>
>Structure:
>1. The honest headline — no euphemisms; name the change in the first sentence
>2. The "why now": the situation that makes this change necessary, told without villainizing anyone
>3. What it means for you, concretely — the 3 most common questions answered preemptively
>4. What is NOT changing — the stability anchor
>5. The feedback path: where questions go and when they get answers
>6. Tone check: flag any phrase that would read as corporate spin to a skeptical reader

- **Purpose:** Change communications people actually believe.
- **Why it works:** Naming the change immediately and including a stability anchor addresses the two things every reader scans for.
- **Use Case:** Reorgs, policy changes, strategy pivots, layoffs-adjacent announcements (use with extreme care and HR/legal review).
- **Expert Variation:**
>Draft the FAQ: the 10 questions people will ask in private but not in the town hall, answered as honestly as policy allows.

**Limitations & verification:** Announcements affecting people's jobs, pay, or legal rights require HR and legal review before any draft leaves the room. The model does not know your obligations; your counsel does.

***

## 6. Talk Track & Timing

**Prompt:**
>Turn this outline into a talk track for a [DURATION] talk: [paste outline]. Audience: [WHO].
>
>1. Time allocation per section, summing to [DURATION minus Q&A]
>2. The verbatim opening 3 sentences — the part that cannot be improvised
>3. Transitions between sections: one sentence each, written as spoken language
>4. The planned pause point: where I stop and ask for questions mid-talk (and the 2 questions to plant if the room is silent)
>5. The verbatim closing 2 sentences and the single call to action
>6. Cut list: what to drop if I am running 5 minutes behind by the midpoint

- **Purpose:** A rehearsal-ready script skeleton with timing discipline built in.
- **Why it works:** Verbatim openers and closers concentrate preparation where improvisation fails most.
- **Use Case:** Conference talks, key presentations, recorded walkthroughs.
- **Expert Variation:**
>Generate the 60-second version of the same talk — the answer to "can you give me the short version?" that always comes.

**Limitations & verification:** Timing estimates assume your speaking pace — calibrate against one real rehearsal. Never present data slides whose numbers you have not personally verified.

***

## Shared Verification Rules for All Presentation Prompts

1. **Every figure must trace to a source.** Presentation errors are the most public kind — re-verify any number, quote, or claim the model places in a headline.
2. **Slides about people require people review.** Change communications, performance narratives, and org announcements need HR/legal sign-off where they touch jobs and rights.
3. **Respect confidentiality in draft content.** Unreleased results and strategy belong in approved internal tools; sanitize before prompting (see repository privacy guidance).
4. **The story serves the evidence, never the reverse.** If a narrative requires hiding an inconvenient data point, the problem is the proposal, not the slide.
