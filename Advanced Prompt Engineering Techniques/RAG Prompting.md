# RAG Prompting

Retrieval-augmented generation: supplying the model with retrieved source material at prompt time so its answers are grounded in your documents rather than its training data. This guide covers the prompting layer of RAG — the architecture around it (embeddings, vector stores, chunking) is a systems topic, but the prompts are what determine whether retrieval actually helps.

## Why RAG Changes the Prompting Problem

Without retrieval, the model answers from training data: broad, stale, unverifiable. With retrieval, it answers from the passages you supply — current, scoped, citable. But retrieved context only helps if the prompt makes the model USE it correctly, and the characteristic RAG failure is a model that ignores, over-trusts, or hallucinates past its sources.

## The Core RAG Prompt Pattern

```
Answer the question using ONLY the provided context.

Context passages:
<passage source="handbook-2026.pdf, section 4.2">
[RETRIEVED PASSAGE 1]
</passage>
<passage source="faq-updated-march.docx">
[RETRIEVED PASSAGE 2]
</passage>

Rules:
1. Ground every claim in a passage — cite the source as [handbook-2026,
   4.2] style references.
2. If the context does not contain the answer, respond exactly:
   "I don't have that in the provided sources." Do not use outside
   knowledge to fill gaps.
3. If passages conflict, present both with their sources rather than
   choosing silently.
4. Distinguish: direct statements from sources versus your inferences
   from them (label inferences).

Question: [USER QUESTION]
```

The four load-bearing elements: **only-the-context scoping**, **verbatim-source citation**, **the refusal hatch** (rule 2 — the difference between a grounded system and a decorated hallucinator), and **conflict transparency**.

## Tuning the Failure Modes

| Failure | What happens | Prompt-level fix |
| :-- | :-- | :-- |
| Context ignored | Answer from training data anyway | Strengthen scoping; put the question AFTER the context; cite-requirement enforcement |
| Hallucinated citations | Cites sources that don't say that | Verbatim-quote requirements for key claims; audit samples against passages |
| Refusal over-firing | "Not in sources" when it IS there | Passage-labeling clarity; rephrase rule 2 to "the answer is not contained or derivable" |
| Context contamination | Answer blends passages that address different questions | Source labels + "answer only the question asked" |
| Weak synthesis | Lists passages without connecting | "Synthesize across passages where they agree" instruction |
| Stale-context trust | Old document overrides new one | Date metadata in source labels + recency rule when applicable |

Important honesty: when retrieval quality is the problem (wrong passages retrieved), no prompt fixes it. If the right passage isn't in the context, the refusal hatch fires — which is correct behavior, and your signal to fix retrieval, not the prompt.

## Prompting the Retrieval Side: Query Formulation

In a RAG system, the user's question is not always the best search query. Prompt engineering applies before retrieval, too:

```
Given this conversation and question, generate the search query or
queries most likely to retrieve relevant passages.
- Reformulate the question into retrieval-friendly form (keywords,
  synonyms, removing conversational references like "the second one")
- If the question has distinct parts, generate one query per part
- Output queries only, one per line.

Conversation: [HISTORY]
Question: [QUESTION]
```

Multi-hop questions ("compare our 2026 policy to the old one") need query decomposition — one query per hop — or retrieval returns one side of the comparison and the answer sounds complete while being half-grounded.

## Structured Output in RAG Answers

For systems where answers feed downstream processes, combine RAG with the Structured Outputs pattern:

```
Respond in JSON:
{
  "answer": "the grounded answer, 2-4 sentences",
  "citations": ["source-id, section"],
  "confidence": "grounded" | "partial" | "not-in-sources",
  "unresolved": "what the sources don't settle, if anything"
}
```

The confidence field routes automated handling: "not-in-sources" responses can trigger different retrieval or human escalation instead of presenting a confident gap-filler.

## Evaluation: RAG Needs It Most

RAG systems fail silently — they always produce fluent answers; the grounding quietly varies. Evaluation (see the Evaluation guide) should cover both halves:

1. **Retrieval metrics**: did the right passages get retrieved? (Test with questions whose correct source passages you know.)
2. **Grounding metrics**: is the answer faithful to the retrieved passages? (Sample and check citations against source text — automated faithfulness checkers exist but deserve the same skepticism as any LLM-as-judge.)

A test set of ~50 known-question/known-source/known-answer triples catches most RAG regressions before users do.

## Honest Limits

- RAG grounds the model in retrieved text; it does not make the retrieved text correct, current, or unbiased — source quality is still your problem
- The refusal hatch means RAG systems answer "I don't know" more than raw models do — that is a feature, and stakeholders should be briefed to expect it
- Prompt-level RAG patterns do not substitute for the system-level security layers described in the Injection Defense guide: retrieved documents are untrusted input, and RAG systems are a primary injection surface in production
