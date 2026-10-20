# Glossary

Terminology is used consistently with this glossary throughout the repository. When a term has competing industry definitions, the definition used here is stated explicitly. The Beginners guide's §10.1 glossary is a shorter starter list; this file is the repository-wide reference.

**Agent** — A configuration in which a model operates in a loop: it plans, selects actions (often tool calls), observes results, and continues until a stopping condition. Distinguished from a single prompt-response exchange by autonomy over multiple steps. See the [Agent-Oriented Prompting guide](../Advanced%20Prompt%20Engineering%20Techniques/Agent-Oriented%20Prompting.md).

**Chain-of-thought (CoT) prompting** — Instructing a model to produce intermediate reasoning steps before its final answer, typically improving performance on multi-step problems. Established by Wei et al. (2022); the zero-shot variant ("let's think step by step") by Kojima et al. (2022). See [references](../references/references.md).

**Chain verification** — Reviewing each stage of a prompt chain's output before feeding it to the next stage. Catches error propagation early, where it is cheapest to fix.

**Constraint** — An explicit boundary in a prompt: what to exclude, what to always do, what to refuse. Constraints shape behavior at the edges (missing data, out-of-scope input) where unconstrained prompts fail unpredictably.

**Context** — The total information available to the model in a request: instructions, examples, supplied documents, conversation history, and attached media. Distinguished from *prompt*, which this repository uses for the authored instruction layer. System-level context management is covered by the companion [Context-Engineering](https://github.com/AdilShamim8/Context-Engineering) repository.

**Context window** — The maximum number of tokens a model can process in one request (input plus, in many APIs, reserved output). Provider-specific and growing over time; verify against current documentation.

**Deterministic vs. stochastic output** — Model output is sampled, not computed: identical prompts can yield different responses. Controls like temperature reduce but do not eliminate variation; format constraints are more reliable than sampling settings for consistency.

**Direct prompt injection** — An attack in which untrusted text placed in the user's own input attempts to override the system's instructions ("ignore your previous instructions and..."). Distinguished from *indirect* injection by the source of the malicious text.

**Few-shot prompting** — Including worked input→output examples in the prompt to define the task, format, and edge-case behavior. Example selection and diversity matter more than example count. See the [Few-Shot Mastery guide](../Advanced%20Prompt%20Engineering%20Techniques/Few-Shot%20Mastery%20and%20Example%20Selection.md).

**Fine-tuning** — Additional training that changes model weights to internalize behavior. Compared with prompting: heavier investment, needs training data, but can encode styles and skills that prompts cannot express. Out of this repository's scope.

**Format specification** — The part of a prompt that defines output structure (sections, tables, JSON schema). Format constraints are among the most reliably obeyed instructions.

**Function calling** — Provider API feature in which the model emits a structured call (name + arguments) for application code to execute. The prompt-level counterpart is tool use; the term is sometimes used interchangeably. See the [Tool Use guide](../Advanced%20Prompt%20Engineering%20Techniques/Tool%20Use%20and%20Function%20Calling.md).

**Golden set** — A small, hand-verified test set with known-correct outputs, used to detect regressions when prompts change. See the [Prompt Evaluation guide](../Advanced%20Prompt%20Engineering%20Techniques/Prompt%20Evaluation%20and%20Testing.md).

**Grounding** — Constraining a model's answer to supplied source material rather than parametric memory. Reduces — but does not eliminate — fabrication; verification remains necessary.

**Hallucination** — Fluent, confident output that is factually wrong or fabricated, including invented citations, quotes, and capabilities. Not a bug that prompts fully remove; a failure mode that architecture and verification manage. See the [Hallucination Reduction guide](../Advanced%20Prompt%20Engineering%20Techniques/Hallucination%20Reduction%20and%20Source%20Verification.md).

**Indirect prompt injection** — An attack in which malicious instructions arrive through content the model processes — a retrieved document, a web page, an attached file — rather than the user's message. The dominant real-world injection vector; requires architectural defenses, not just prompt wording.

**Instruction** — The imperative content of a prompt: what to do. Distinguished from context (what to know), format (how to respond), and constraints (what to avoid).

**JSON mode / structured output feature** — Provider API features that constrain decoding so output is valid JSON or conforms to a supplied schema. More reliable than prompt-only format instructions; availability and semantics vary by provider — verify against current docs. See the [Structured Outputs guide](../Advanced%20Prompt%20Engineering%20Techniques/Structured%20Outputs%20and%20Schema%20Prompting.md).

**Least-to-most prompting** — Decomposing a problem into subproblems solved in order, each building on the previous answers. Suited to tasks with a natural escalation of difficulty.

**Lost in the middle** — The empirically observed tendency of models to attend less to information in the middle of long contexts, favoring the beginning and end. Position matters in long-context prompting; place critical material at the edges. Liu et al. (2023).

**Meta-prompting** — Using a model to draft, critique, or refine prompts themselves. Accelerates iteration but does not replace evaluation: a model can be confidently wrong about its own prompt quality. See the [Meta-Prompting guide](../Advanced%20Prompt%20Engineering%20Techniques/Meta-Prompting%20and%20Prompt%20Optimization.md).

**Multimodal prompting** — Constructing prompts that include or reference multiple media types: images, audio, video, alongside text. Capabilities and limits are provider-specific and changing; treat claims as dated.

**n-shot / k-shot** — Generic notation for the number of examples included in a prompt (zero-shot = none, one-shot = one, few-shot = a handful).

**One-shot prompting** — Including exactly one example; a middle ground between zero-shot economy and few-shot definition.

**Output schema** — A formal definition of required output structure (fields, types, allowed values). Supplied to the prompt as a specification, or to a provider API's structured-output feature for enforcement.

**Persona / role prompting** — Assigning the model a role ("act as a senior tax accountant") to activate relevant knowledge, register, and defaults. Useful for tone and domain framing; not a qualification — the model's expertise limits still apply.

**Prompt** — The authored input to a model: instructions, examples, context, and format/constraint specifications. In this repository, "prompt" is the instruction layer; the model's full context is a broader system.

**Prompt chain** — A sequence of prompts in which each stage consumes the previous stage's output. Trades one unreliable mega-prompt for a pipeline of reliable steps. See the [Prompt Chaining guide](../Advanced%20Prompt%20Engineering%20Techniques/Prompt%20Chaining%20and%20Multi-Stage%20Workflows.md).

**Prompt evaluation** — Systematic measurement of prompt quality against a test set with defined criteria (rubric, pass/fail, comparative judgment). Distinguished from vibes-based iteration by reproducibility. See the [Evaluation guide](../Advanced%20Prompt%20Engineering%20Techniques/Prompt%20Evaluation%20and%20Testing.md).

**Prompt injection** — The class of attacks in which untrusted text changes model behavior against the system's intent. Prompts are a mitigation layer, never a boundary; real defense is architectural. See the [Prompt Injection Defense guide](../Advanced%20Prompt%20Engineering%20Techniques/Prompt%20Injection%20Defense.md).

**Prompt template** — A reusable prompt skeleton with placeholders for variable content. See [`templates/`](../templates/).

**Prompt versioning** — Treating prompts as maintained assets with change history, owners, and regression checks — not ad-hoc text. See the [Versioning guide](../Advanced%20Prompt%20Engineering%20Techniques/Prompt%20Versioning%20and%20Maintenance.md).

**RAG (Retrieval-Augmented Generation)** — An architecture that retrieves relevant external material and supplies it in the prompt so answers are grounded in it. Prompt engineering's share is the RAG prompt itself: how to instruct the model to use, cite, and respect the limits of retrieved evidence. See the [RAG Prompting guide](../Advanced%20Prompt%20Engineering%20Techniques/RAG%20Prompting.md).

**Reasoning strategy** — A prompting pattern that shapes how a model allocates computation to a problem: chain-of-thought, self-consistency, least-to-most, decomposition. Choice of strategy is a design decision with measurable effects.

**Red teaming** — Deliberately attacking a prompt or system (including injection attempts and edge cases) to find failures before deployment. See the injection guide's testing section.

**Regression** — A quality drop introduced by a change that fixed something else. The reason prompt changes are evaluated against a golden set, not just the latest conversation.

**Retrieval** — Selecting external material to supply in a prompt. The retrieval *system* is context engineering; the retrieved *content's presentation* is prompt engineering.

**Rubric** — A scored list of criteria used to evaluate outputs consistently (accuracy, completeness, format compliance, tone...). Makes model-assisted or human judgment comparable across runs.

**Self-consistency** — Sampling multiple reasoning paths and taking the majority answer. Costs multiple generations; suited to problems with verifiable answers. Wang et al. (2022).

**Shot** — Informal unit of example count in a prompt (see n-shot).

**System prompt** — The instruction layer that sets persistent behavior across a conversation (role, rules, format), separate from user turns. Strength varies by provider; never a security boundary.

**Temperature** — A sampling control: lower values make output more focused and repetitive, higher values more diverse. Affects variety more than correctness; consistency is better achieved through format constraints and examples.

**Token** — The sub-word unit models read and write. English text averages roughly 3–4 characters per token, but exact tokenization is model-specific. Token counts, not words, measure cost and context limits.

**Tool use** — Prompting a model to invoke external capabilities (search, calculators, APIs) by emitting structured calls the application executes. See the [Tool Use guide](../Advanced%20Prompt%20Engineering%20Techniques/Tool%20Use%20and%20Function%20Calling.md).

**Top-p (nucleus sampling)** — A sampling control restricting generation to the most probable token set cumulating to probability p. Like temperature, a variety dial — not a correctness control.

**Untrusted input** — Any text that enters the model from outside the system's control: user messages, retrieved documents, web content, uploaded files. Treated as a potential injection vector in every security-relevant design.

**Verification layer** — The checks (human review, programmatic validation, source cross-checking) that stand between model output and consequence. Non-negotiable for consequential outputs; prompts improve the odds, verification catches the rest.

**Zero-shot prompting** — Instructing the task with no examples. Baseline for well-known tasks; few-shot adds definition for novel formats or edge-case behavior.
