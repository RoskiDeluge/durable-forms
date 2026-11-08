# Logical Assembly: Resolution, Overlay, and Mode

*Response to [[logical-assembly-a-new-source-of-light]], November 8, 2026 (Claude Code session)*

## Context
In an earlier exchange, the ASML analogy ended with a question: ASML's rigor is legible because it comes in numbers (resolution, overlay error, wafers per hour, yield), so **what is Logical Assembly's nanometer?** That is, what single quantity, measured on every invocation, tells you the assembly is holding tolerance? The source-of-light idea log answered with a fundamental unit, the *pattern*. This artifact records the response to that log.

The beach origin suits it. Aristophanes put Socrates in a basket among the clouds to mock philosophers for looking up, and you came down from the clouds with an architecture.

## A unit is not a tolerance
The idea log moves the question forward, though it answers a neighboring one. **The pattern is the fundamental unit, and a unit is something you count.** The nanometer was a *tolerance*: the finest distinction you can reliably hold. You need both, and with the unit in hand the tolerance is easier to see.

## Rayleigh's criterion, mapped onto the stack
Lithography's resolution equation maps onto the stack almost term by term. Rayleigh's criterion is roughly *resolution = k₁ · λ / NA*:

- **λ, the wavelength**, is how fine the light itself is. That's the mind: the model's semantic fineness. This is what EUV changed, and what LLMs changed for meaning.
- **NA, the numerical aperture**, is how much light the optics gather. That's how much context Patch Rig takes in before it judges.
- **k₁, the process factor**, is all the cleverness that pushes past the raw physics. That's Auto Bench plus the code book, the schema discipline that lets a coarse light print fine features.

So Logical Assembly's nanometer could be the **resolution of the code book**: the finest semantic distinction at which witness judgments and human decisions still reliably agree. If you split a code-book section into two sub-codes and agreement collapses, you've gone below your resolution. That's measurable on every pattern: the disagreement between light and mask is the **overlay error**. It also tells you which lever to pull. Use a better model for λ, give the witness more context for NA, or sharpen the schema for k₁.

## A wrinkle in the mask mapping: two masks
In a real scanner the mask is designed *before* the light passes through it. In the idea log's sketch, some decisions come *after* a judgment, when a person rules on what a witness saw. That suggests two masks:

1. **The code book as the standing mask.** This is intent designed in advance, which every judgment passes through. It's closest to the reticle.
2. **Case decisions as mask corrections.** Fabs do this too, adjusting the reticle with optical proximity correction (OPC) once they see how patterns actually print. A decision that overrules a judgment is a correction to how the mask prints, and enough of them should feed back into a revised code book.

This bears directly on the Auto Bench open question. A pattern may need to record *which* mask shaped it: the code-book version it passed through, plus any decision that corrected it.

## A name from Spinoza: mode
In the *Ethics*, a **mode** is a particular thing, an affection of the one substance. Every mode is expressed under both attributes at once: as a body under extension and as an idea under thought. Not two things, one thing seen two ways. That matches the idea log's definition exactly: "an event's cause and its meaning stored as one thing." Rastro holds a pattern under the attribute of extension (the causal order), and Auto Bench holds it under the attribute of thought (the conceptual order).

"Mode" is overloaded in software, so it may not survive as an API term, but as the philosophical name in *Durable Forms* it does a lot of work. It also has the advantage over qualia that it is public by nature.

## Closing the loop with the five elements
Patch Rig *is* a micro-agent. The code book is its behavior, the model is its mind, the data source it watches is its world, and its emitted judgments go to Rastro as its memory. The "light" is literally a mind running inside the being paseo provides, and paseo enforcement is where the pattern actually gets etched. The pieces built separately converge here.

## Open question
When you picture the overlay check, where a witness's judgment meets a human decision and they disagree, which one does the system treat as the error? In lithography the mask is always right. In Logical Assembly that may not always be true, and the answer may be the most interesting part of the philosophy.
