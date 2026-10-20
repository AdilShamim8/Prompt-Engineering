# References and Further Reading

Curated sources used across this repository. Every entry is real and verifiable; entries making claims about changing products or APIs carry a **reviewed** date, per the maintenance policy in [`ROADMAP.md`](../ROADMAP.md) — re-verify anything older than six months before relying on it. When a guide cites a specific claim, it cites one of these.

## Official provider documentation

Provider documentation is the authority on provider-specific behavior (structured output features, tool-calling semantics, model naming, limits). URLs move; if a link fails, search the provider's docs for the page title.

| Source | What it is authoritative for | Reviewed |
|---|---|---|
| [OpenAI — Prompt engineering guide](https://platform.openai.com/docs/guides/prompt-engineering) | Tactics and examples from the GPT API provider | 2026-10-20 |
| [OpenAI — Introducing structured outputs in the API](https://openai.com/index/introducing-structured-outputs-in-the-api/) | Schema-constrained decoding: what it guarantees and does not | 2026-10-20 |
| [Anthropic — Prompt engineering overview](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview) | Claude-specific prompting: XML structuring, roles, thinking, chaining | 2026-10-20 |
| [Google — Gemini prompt design strategies](https://ai.google.dev/gemini-api/docs/prompting-strategies) | Gemini-specific prompt design and multimodal prompting | 2026-10-20 |

## Foundational research

Peer-reviewed or widely-cited preprint research behind the core techniques. Links are to arXiv abstract pages, which are stable.

| Paper | Established what | Link |
|---|---|---|
| Wei et al. (2022), *Chain-of-Thought Prompting Elicits Reasoning in Large Language Models* | Intermediate reasoning steps improve multi-step performance (few-shot CoT) | [arXiv:2201.11903](https://arxiv.org/abs/2201.11903) |
| Kojima et al. (2022), *Large Language Models are Zero-Shot Reasoners* | "Let's think step by step" — zero-shot CoT | [arXiv:2205.11916](https://arxiv.org/abs/2205.11916) |
| Wang et al. (2022), *Self-Consistency Improves Chain of Thought Reasoning in Language Models* | Majority-vote over sampled reasoning paths | [arXiv:2203.11171](https://arxiv.org/abs/2203.11171) |
| Zhou et al. (2022), *Least-to-Most Prompting Enables Complex Reasoning in Large Language Models* | Decomposition into ordered subproblems | [arXiv:2205.10625](https://arxiv.org/abs/2205.10625) |
| Yao et al. (2022), *ReAct: Synergizing Reasoning and Acting in Language Models* | Interleaving reasoning traces with tool actions | [arXiv:2210.03629](https://arxiv.org/abs/2210.03629) |
| Liu et al. (2023), *Lost in the Middle: How Language Models Use Long Contexts* | Position effects in long contexts (edges favored over middles) | [arXiv:2307.03172](https://arxiv.org/abs/2307.03172) |
| Ji et al. (2022), *Survey of Hallucination in Natural Language Generation* | Taxonomy and causes of fabrication | [arXiv:2202.03629](https://arxiv.org/abs/2202.03629) |
| Greshake et al. (2023), *Not What You've Signed Up For: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection* | The indirect injection threat model | [arXiv:2302.12173](https://arxiv.org/abs/2302.12173) |
| White et al. (2023), *A Prompt Pattern Catalog to Enhance Prompt Engineering with ChatGPT* | Pattern-language treatment of reusable prompt designs | [arXiv:2302.11382](https://arxiv.org/abs/2302.11382) |
| Zamfirescu-Pereira et al. (2023), *Why Johnny Can't Prompt* | How non-experts naturally fail at prompting (CHI 2023) | [arXiv:2307.06873](https://arxiv.org/abs/2307.06873) |
| Sahoo et al. (2024), *A Systematic Survey of Prompt Engineering in Large Language Models* | Broadest recent survey of the technique landscape | [arXiv:2402.07927](https://arxiv.org/abs/2402.07927) |

## Security and safety

| Source | Why it matters here | Reviewed |
|---|---|---|
| [OWASP Top 10 for LLM Applications](https://genai.owasp.org/) | Industry-standard risk taxonomy; prompt injection ranks among the top risks | 2026-10-20 |
| [Simon Willison — prompt injection series](https://simonwillison.net/tags/prompt-injection/) | The clearest ongoing practitioner analysis of injection since 2022 | 2026-10-20 |

## Community learning resources

| Source | What it offers |
|---|---|
| [DAIR.AI — Prompt Engineering Guide](https://www.promptingguide.ai/) | Broad, community-maintained technique guide with research links |
| [Awesome Prompt Engineering](https://github.com/promptslab/Awesome-Prompt-Engineering) | Curated list of papers, tools, and guides |
| [Anthropic — Prompt engineering tutorial (GitHub)](https://github.com/anthropics/prompt-eng-interactive-tutorial) | Interactive exercises (written for Claude 3; fundamentals transfer) |

## Companion repositories in this learning ecosystem

| Repository | Scope |
|---|---|
| [Context-Engineering](https://github.com/AdilShamim8/Context-Engineering) | Everything the model sees at inference time: retrieval, memory, state, budgeting, security architecture, evaluation |
| This repository | The instruction layer: prompts, patterns, techniques, domain applications |

## Citation policy for contributors

Adding a source to this file requires: (1) a real, checkable link; (2) one sentence on what it is authoritative for; (3) a reviewed date if it describes a changing product. Fabricated or unverifiable references are treated as content bugs — see [`CONTRIBUTING.md`](../CONTRIBUTING.md).
