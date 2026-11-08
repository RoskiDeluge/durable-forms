# Logical Assembly: A New Source of Light

*Idea log, Saturday, November 7, 2026*

## Where the idea came from

While at the beach with the kids, lying on a beach mat and looking up at the clouds, I thought about Aristophanes and about how philosophers have always looked at clouds and imagined what might be there. That brought me back to a question from yesterday's session in the Logical Assembly repo: what is the most consequential unit of Logical Assembly?

## The ASML inspiration

ASML builds the extreme ultraviolet (EUV) lithography machines that chipmakers use to make chips. What inspires me most is that they had to invent a new source of light to do it. My ambition for Logical Assembly is the same thing in a different field. I want to create a new source of light for semantics and human meaning: a technological artifact that can capture human meaning in an organizational context.

## What Logical Assembly is

Logical Assembly is three things at once: a guiding philosophy, an architecture, and a technical artifact. The artifact is a stack of components:

- **Logical Assembly (control plane):** where people make decisions.
- **Rastro (world ledger):** an append-only event store.
- **Patch Rig (witness):** observes a data source and emits judgments, such as matching an input to a section of a code book. It uses the decisions endpoint under the hood.
- **Auto Bench (Logical Assembly core):** the event schema, defined per domain, that every event must follow before it reaches Rastro.
- **Paseo (runtime):** actors (workers) on Cloudflare, exposed through a REST API, that enforce decisions by referencing the decisions endpoint.

In short: people decide, Patch Rig observes and judges, Auto Bench defines the shape, Rastro records, and Paseo enforces.

## Looking for the fundamental unit

**First idea: qualia.** It was a tempting word, but in philosophy of mind qualia means the felt quality of an experience, and its defining trait is that it is private and can't be put into words. That clashes with the goal, which is meaning that can be captured, shared and checked across an organization.

**Second idea: a photon of meaning.** This is a small, standard packet that carries meaning reliably. One candidate is the witnessed judgment: a single observation, tied to a passage in a code book, in a standard format, with its origin preserved.

**Two kinds of meaning.** The system has two sources of meaning:

1. The meaning the system picks up on its own, which is Patch Rig's judgments.
2. The meaning a person commits to, which is decisions made in the control plane.

## The answer for now: the pattern

In lithography, light does nothing on its own. It has to pass through a mask, which carries the designer's intent, before it can etch a pattern onto the wafer. Mapped onto Logical Assembly:

- **Light:** Patch Rig's judgments
- **Mask:** human decisions
- **Pattern:** the fundamental unit, a judgment shaped by a decision, recorded in Rastro and enforced by Paseo

## A later thread: Spinoza

I've started reading Spinoza's *Ethics*, and it seems to reopen possibilities in his view that concepts and causes are coextensive. In Part II, Spinoza holds that the order and connection of ideas is the same as the order and connection of things. Explaining something causally and understanding it conceptually are one act seen from two sides.

**The transcendental impasse.** It may be a big leap, but perhaps metaphysics and the transcendental tradition are a response to an imaginative impasse that Spinoza chose to get around in an immanent way. Kant builds a wall between how things appear to us and how they are in themselves. Spinoza never separates the two in the first place.

**Not a mechanist.** Spinoza isn't really a mechanist. Extension and thought are parallel attributes of one substance, so neither reduces to the other. A purely mechanistic interpretation of all phenomena keeps only one side, and may be deeply flawed. Until now, though, we haven't had the instruments to get close to the true limits of mechanism.

**LLMs as the new instrument.** Beyond what they do for knowledge work that depends on linguistic and semantic fluency, LLMs may be the first combination of fuel, spark and oxygen for a new light source. They are a place where a causal process (computation) and a conceptual order (meaning) visibly run together, so we can probe where one stops tracking the other.

**Mapping onto the stack.**

- **Rastro** records the order of events (causes).
- **Auto Bench** defines the order of concepts.
- **The pattern**, the fundamental unit, sits where the two coincide.

Read this way, Logical Assembly is a Spinozist ledger, where an event's cause and its meaning are stored as one thing.

## Open questions

- What exactly does one unit (one pattern) contain?
- What should the unit be called, now that qualia doesn't fit well?
- How should Auto Bench's schema represent the link between a judgment and the decision that shaped it?
- How should Spinoza be woven through the *Durable Forms* manuscript, while holding the tension with the transcendental strand in Langer and Wittgenstein?
