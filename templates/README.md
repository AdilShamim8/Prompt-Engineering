# Prompt Templates

Reusable prompt skeletons for the techniques taught in this repository. Copy, fill the placeholders, and adapt the wording to your context — the structure is the reusable part.

## How to use these templates

1. **Pick by job, not by novelty.** Each template states when it is the right tool. The universal five-component structure below covers most everyday needs; the advanced templates are for programmatic or multi-stage work.
2. **Fill every placeholder.** A placeholder left in place (`[TASK]`) is the most common copy-paste failure. Placeholders use the convention `[ROLE]`, `[CONTEXT]`, `[TASK]`, `[FORMAT]`, `[CONSTRAINTS]`, `[PASTE X HERE]`.
3. **Delete what does not apply.** Templates are checklists, not contracts — an over-specified prompt for a trivial task wastes tokens and dilutes the instruction.
4. **Test, then save your variant.** When a customized version works, keep it as your own template with the variable parts marked — see [Prompt Versioning and Maintenance](../Advanced%20Prompt%20Engineering%20Techniques/Prompt%20Versioning%20and%20Maintenance.md).

## Template index

| Template | Use when | Curriculum |
|---|---|---|
| [Five-component universal prompt](./universal-prompt-templates.md#the-five-component-universal-prompt) | Any substantive single-turn task | Stage 1 |
| [Few-shot task definition](./universal-prompt-templates.md#few-shot-task-definition) | The model must follow a specific input→output pattern | §3.2 |
| [Iterative refinement](./universal-prompt-templates.md#iterative-refinement) | A good draft needs targeted improvement, not rewriting | Stage 1 |
| [Debugging an underperforming prompt](./universal-prompt-templates.md#debugging-an-underperforming-prompt) | Output is wrong and the cause is unclear | Stage 1 |
| [Structured output extraction](./advanced-prompt-templates.md#structured-output-extraction) | Output must be machine-parseable JSON | §3.1 |
| [Two-stage prompt chain](./advanced-prompt-templates.md#two-stage-prompt-chain) | Task splits into extraction then generation | §3.3 |
| [RAG grounded answer](./advanced-prompt-templates.md#rag-grounded-answer) | Answer must come from supplied sources only | §3.5 |
| [Evaluation rubric](./advanced-prompt-templates.md#evaluation-rubric) | Outputs must be scored consistently | §3.10 |

Curriculum references point to [`CURRICULUM.md`](../CURRICULUM.md) sections.

## Relationship to other content

- The [Beginners guide §10.2](../AI%20Prompt%20for%20Beginners/Prompt%20Engineering%20for%20Beginners.md) teaches template construction from first principles — read that before relying on these.
- The domain collections contain specialized templates for business, research, HR, and other contexts; these files hold the domain-neutral core set.
- Terminology follows [`glossary/glossary.md`](../glossary/glossary.md).
