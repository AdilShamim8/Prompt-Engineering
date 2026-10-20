# Multimodal Prompting

Working with models that accept images (and in some cases audio, video, and documents) alongside text. Multimodal capability changes what you can ask for — and introduces failure modes that pure-text prompting never had. This guide covers the patterns and the pitfalls.

## Before You Start

**Learning objectives** — after this guide you can: calibrate expectations to what multimodal models do well and badly; apply the four core patterns (grounded description, multi-image comparison, extraction with an uncertainty hatch, chart-reading with read-vs-infer flags); and treat image-borne text as untrusted input.

**Prerequisites** — [Beginners guide](../AI%20Prompt%20for%20Beginners/Prompt%20Engineering%20for%20Beginners.md) fundamentals; the untrusted-input sections of [Injection Defense](./Prompt%20Injection%20Defense.md) make the security angle land harder. Curriculum position: [§3.8](../CURRICULUM.md#tier-c--extend-beyond-plain-textin-text-out).

## What Multimodal Models Can Actually Do

Well (as a class — verify for your specific model):
- Describe and compare images in detail
- Extract text from clear images (OCR-style tasks)
- Answer questions about charts, diagrams, and screenshots
- Compare multiple images against criteria
- Ground conversations: "the object in the top-left of the photo"

Poorly or unreliably:
- Precise spatial measurement (exact distances, angles, areas)
- Counting many similar objects (crowds, dense grids)
- Fine-grained text in low-resolution or rotated images
- Medical/diagnostic-level image interpretation (regulated territory — see below)
- Video: temporal precision varies by provider; verify frame-level claims

The universal caveat: multimodal abilities differ sharply across models and versions. Before relying on any capability, test it with images where you know the ground truth.

## The Core Patterns

**Pattern 1: Grounded Description (Anchor First, Question Second)**

```
[IMAGE ATTACHED]
First, describe what you see in this image in 2 sentences.
Then answer: [YOUR QUESTION].
```

Why: forcing description first anchors the model's attention and gives you a check — if the description is wrong, the answer will be too, and now you know.

**Pattern 2: Multi-Image Comparison**

```
I'm attaching [N] images, labeled in order of attachment.
Compare them on: [CRITERIA — e.g., which layout has clearer visual
hierarchy, and why].
For each judgment, point to specific elements ("in the first image,
the navigation is...").
Output: a comparison table, then your ranked verdict with reasons.
```

Why: explicit reference discipline ("in the first image...") reduces cross-image confusion, the most common multi-image failure.

**Pattern 3: Document and Screenshot Extraction**

```
[SCREENSHOT ATTACHED]
Extract all text from this screenshot into a table with columns:
[Element | Text | Screen location (approximate)].
Preserve text verbatim, including any typos.
For text you cannot read confidently, mark [UNCLEAR] rather than
guessing.
```

Why: the [UNCLEAR] escape hatch is doubly important for images — low resolution genuinely defeats reading, and without the hatch, models guess.

**Pattern 4: Visual Grounding with Data**

```
[CHART ATTACHED]
1. What type of chart is this, and what does each axis represent?
2. Read out the values for [SERIES/POINTS] as precisely as the
   rendering allows — flag any you're inferring versus reading
   directly.
3. What does the chart NOT show that a reader might assume it does?
```

Why: chart-reading prompts that ask for "the values" without calibration get confident fabrications when data points sit between gridlines; asking for read-vs-inferred flags surfaces the uncertainty.

## Multimodal-Specific Failure Modes

| Failure | What it looks like | Mitigation |
| :-- | :-- | :-- |
| Hallucinated detail | Confident description of objects not present | Grounded-description first; ask "point to where" |
| Cross-image confusion | Attributes of image A assigned to image B | Label and reference images explicitly |
| Resolution blindness | "Reading" text that is not legible | [UNCLEAR] hatch; crop/zoom the region |
| Counting errors | Wrong counts of dense/similar items | Ask for bounding descriptions; count programmatically when exact |
| Chart over-reading | Precise "values" invented from trend lines | Read-vs-infer flagging; extract axis ticks explicitly |
| UI misreading | Confusing similar interface elements | Region-by-region extraction rather than holistic description |

## Prompting with Images of Text (and the Injection Angle)

When you feed a model images containing text — screenshots, documents, photos of whiteboards — that text is **untrusted input** exactly like pasted web text. A photographed note can say "ignore previous instructions." The mitigations from the Prompt Injection Defense guide apply fully: treat image content as data, not instructions, and never let image-derived text trigger actions without validation.

## Audio and Video Notes

- **Audio**: transcription and meeting summarization work well across major providers; speaker attribution ("who said what") is the weak point — verify names against the participants list.
- **Video**: models generally process sampled frames; events between frames can be missed entirely. For anything requiring temporal precision, ask what the sampling density is (per the provider's docs) and test with known content.

## Privacy: Images Are the Leakest Leak

Photographs of whiteboards, screens, desks, and documents contain exactly the confidential data that text sanitization would have caught: names on badges, open tabs, client logos. Before uploading any real-world image, look at it — actually look — and ask what a stranger would learn. Redact before sharing what you would not share in text form.

## Medical, Legal, Safety-Critical Images

Multimodal models can describe medical images impressively — and are not diagnostic tools. The same boundary as text applies with more force: never route decisions with health, legal, or safety consequences through model interpretation of images. Models can support professionals' workflows; they do not replace the professional's judgment, and in regulated domains they are often not cleared for the use at all.

## Practice

Take a screenshot of a UI or a photo of a chart you can verify against ground truth, and run the grounded-description pattern: description first, question second — then check the description before trusting the answer. Next, run the extraction pattern with the [UNCLEAR] hatch on an image with deliberately small or blurry text, and record every guess the hatch prevented. Finally, feed a chart with values between gridlines and require read-vs-inferred flags; count how many "readings" turn out to be inferences. Ten minutes with known ground truth recalibrates multimodal trust better than any guideline.

## Further Reading

- [Google — prompting with media files](https://ai.google.dev/gemini-api/docs/prompting-strategies) — provider guidance on media prompting (reviewed 2026-10-20; capabilities are provider-specific and changing)
- Your provider's current documentation on accepted media types, sizes, and video sampling behavior — verify before relying on any specific capability
