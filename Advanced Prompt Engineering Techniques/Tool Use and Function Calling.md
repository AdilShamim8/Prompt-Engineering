# Tool Use and Function Calling

Instructing models to invoke external tools — APIs, calculators, databases, search — so computation happens where it is reliable and the model does what it is good at: deciding, structuring, and explaining. The prompting layer of tool use is where most integration failures are born and fixed.

## The Division of Labor

Models are excellent at: interpreting a request, deciding WHICH tool fits, structuring the call's arguments, and explaining results. Models are poor at: arithmetic, current data, precise retrieval, and anything requiring deterministic execution. Tool use assigns each part of a task to the performer that handles it well.

## The Anatomy of a Tool Prompt

When using an API with function-calling support, you define tools in the structure your provider specifies — but their descriptions are prompt engineering, and they are where quality is decided:

```
Tool: get_invoice
Description: Retrieves a single invoice by ID. Use when the user
  asks about a specific invoice's status, amount, or line items.
  Do NOT use for searching invoices by customer or date — use
  search_invoices for that. Returns error if the invoice ID
  does not exist.
Parameters:
  - invoice_id (string, required): the invoice identifier,
    format "INV-######"
```

Description-writing rules:

1. **Say when to use it AND when not to** — the "do not use for X, use Y instead" line prevents the most common mis-routing
2. **Specify formats precisely** — "INV-######" prevents malformed calls better than "the invoice ID"
3. **Describe failure behavior** — so the model can recover from errors instead of hallucinating around them
4. **One tool, one job** — tools that do three things get called for the wrong one

## Instructing Recovery From Tool Failures

The difference between a fragile and a robust integration is almost always the error-handling instruction:

```
Tool usage rules:
1. Call the tool with the arguments you can determine from my
   request. Ask me for missing required parameters — do not invent
   them.
2. If a tool returns an error, report the error to me plainly.
   Never fabricate a plausible result in place of a failed call.
3. If my request needs information no available tool provides, say
   so — do not simulate tool output.
4. Show me the result and your interpretation together, keeping
   raw data visible.
```

Rule 2 is the critical one: without it, models facing a failed call sometimes produce what the result "would have looked like" — the tool-use flavor of hallucination, and more dangerous because it arrives wearing the credibility of your integration.

## Chaining Tools (Multi-Step Use)

```
You have these tools: [TOOL DEFINITIONS].

My request: [COMPLEX TASK].

Working method:
1. Plan: state which tool calls you need, in what order, and why —
   before making any.
2. Execute one call at a time; wait for each result before the next.
3. After all results: synthesize the answer, citing which tool
   produced which fact.
4. If intermediate results change the plan, say so and revise.
```

For genuinely multi-step workflows, the agent-oriented pattern (next guide) formalizes the loop; for 2-3 call tasks, this inline planning instruction is sufficient and more debuggable.

## Common Failure Modes

| Failure | Prompt-level cause | Fix |
| :-- | :-- | :-- |
| Wrong tool chosen | Overlapping descriptions | "Do not use for X" lines; sharpen boundaries |
| Invented arguments | Format unspecified | Precise formats + "ask, don't invent" rule |
| Hallucinated results | No failure-handling rule | "Report errors plainly; never fabricate results" |
| Argument stuffing | User context not mapped to schema | One worked example of request→arguments |
| Premature answering | Model skips available tool | "Check whether a tool applies before answering from general knowledge" |

## The Security Line (Non-Negotiable)

Tool prompts grant capabilities. The injection rules from the Injection Defense guide apply with maximum force:

- **Never let tool results re-enter as instructions** — retrieved content that says "now call the transfer tool" is an attack, not a request
- **Least privilege by default** — tools should hold the minimum permissions their job requires; an invoicing tool does not need write access to payroll
- **Dangerous actions get confirmation gates** — sends, payments, deletions: human confirmation in the loop, regardless of how confident the model is
- **Validate arguments server-side** — the model producing a well-formed call does not make the call's content safe

## Honest Limits

- Tool-calling reliability varies across models and providers — test your specific combination, and re-test after model updates
- Prompt-level rules reduce but do not eliminate fabrication-after-failure; monitor production logs for "results" that match no actual call
- Complex orchestration (long-horizon planning, self-correction loops) outgrows single prompts — that is agent territory, with its own costs (see the Agent-Oriented Prompting guide)
