# Long-Context and Context Management

Working with large inputs — long documents, many documents, extended conversations — inside models whose context windows are large but not unlimited, and whose attention to long inputs is imperfect. Context length is a budget; this guide is about spending it well.

## The Mental Model

A context window is not RAM: putting something inside it does not guarantee reliable use. Attention is uneven — content in the middle of very long inputs gets less effective attention than content at the beginning and end (the "lost in the middle" pattern from long-context research). Practical consequences:

- A detail buried at token 40,000 of a 100,000-token prompt may be handled worse than the same detail in a 4,000-token prompt
- More context is not more knowledge: irrelevant content competes for attention with what matters
- Every token you include costs money and latency on API usage

The design question is never "can I fit it?" but "what does each section earn its tokens with?"

## Pattern 1: The Extraction-First Compression

```
Stage 1: "From the attached [80-page document], extract ONLY the
         passages that relate to [YOUR QUESTION] — verbatim quotes
         with page references. Do not summarize yet."

Stage 2: "Using ONLY these extracted passages, answer [YOUR QUESTION].
         Cite which passage supports each claim."
```

Why: you trade one attention-diluted mega-prompt for one extraction pass plus one focused prompt. The verbatim-quote requirement makes the second stage auditable — you can check the answer against the actual passages.

## Pattern 2: Map-Reduce Over Many Documents

```
Map:    per document — "Summarize this document's content relevant to
        [TOPIC]: 5 bullets, all numbers preserved verbatim, note
        explicitly what is absent."
Reduce: "Here are summaries of [N] documents: [SUMMARIES].
        Synthesize: agreements, contradictions, gaps. Cite which
        document(s) support each point."
```

Why it works: each map call is a short-context problem; the reduce call works over compressed, topic-relevant content instead of raw noise. The "note what is absent" instruction turns each summary into a coverage check, not just a compression.

## Pattern 3: Structured Anchoring for Long Documents

When you must send the full document (contract review, clause analysis):

```
The document is between <doc> tags. It contains [N] sections.

TASK: [YOUR TASK].

Method:
1. First output a section map: section number + heading + one line.
2. Then process section by section, quoting the exact language you
   rely on.
3. If the task cannot be completed from this document, say so
   explicitly rather than filling gaps with assumptions.

<doc>[FULL DOCUMENT]</doc>
```

Why: the section map forces a first pass over the whole document (countering mid-document drift), and quote-reliance keeps the analysis grounded in actual text rather than remembered gist.

## Conversation Context: The Silent Accumulation

In long chats, every prior turn stays in context. This produces three failure modes:

1. **Context creep**: early irrelevant details shape later answers ("you're still writing for that audience from message 2")
2. **Attention dilution**: the model's grasp of your current question weakens as history grows
3. **Overflow**: the conversation truncates silently or errors — often at the worst moment

The countermeasure is deliberate context hygiene:

- Start a fresh session when the task changes
- For long sessions, periodically post a compact state summary ("Here's what we've established: ...") and continue from it in a new session
- Never rely on a chat session as storage — save important outputs to files as you go

## Context Budgeting Checklist

```
[ ] Does every section of my prompt change the answer? (Delete what doesn't.)
[ ] Is the most critical information near the beginning or end, not the middle?
[ ] Could extraction-first replace whole-document inclusion?
[ ] Are multiple documents better served by map-reduce than concatenation?
[ ] Am I re-sending stable context every turn (system prompts handle this in APIs)?
[ ] Do I know my model's actual context limit — input AND output share it?
```

## Honest Limits

- **Context ≠ comprehension at full strength**: models handle long inputs imperfectly; critical details deserve structural emphasis (labels, repetition at start and end), not just inclusion somewhere
- **Provider limits differ and change**: verify current window sizes and pricing in your provider's documentation, and re-test long-context prompts when switching models
- **Retrieval is often the better architecture**: for recurring access to a large corpus, RAG (next guide) beats re-sending everything — the question is corpus size × query frequency, not raw capability
