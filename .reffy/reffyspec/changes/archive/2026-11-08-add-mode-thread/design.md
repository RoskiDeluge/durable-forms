## Context
The source artifacts are an idea log and a response to it, both written against an implementation of the stack. This design sorts their ideas the way the Wittgenstein note and the reified-frame design did: what goes in, where, at what length, and what stays out. It is read against `main` at draft 0.34, after `add-wittgenstein-thread` and `add-reified-frame-thread` landed, and it keeps their ground rules: import the philosophy, not the rig; keep claims sized to their tests; Langer keeps the last word; no fifth prediction without results.

The author has set two decisions and one constraint for this change:
- **Name lithography and ASML** openly, as an inspiration.
- **Adopt "mode" as the name of the unit**, despite the word's history in computing.
- **Keep it high level.** Apart from the obvious nods (ASML, Spinoza), name no implementation of the stack.

### Problem Summary
- The book's unit is the bit (Ch2), and the bit is the unit of transmission. The book has no named unit for what the assembly keeps. The Ch10 summary promises the question, but the text never poses it.
- The swap test (Ch8 §IV) measures how much meaning survives. Nothing measures how fine the meaning is.
- The preface gives Wasm as the name's source and is silent on the ambition's.
- Ch1's relay reaches Deleuze's immanence without its source.

## Goals / Non-Goals
- Goals:
  - Introduce the mode once, in Ch8, as the loop's unit, with its Spinozist sense set up in Ch1 and its horizon reading in Ch10.
  - Give the book a measure of fineness (resolution) and of disagreement (overlay error), stated as proposed measures, not findings.
  - Name ASML in the preface as the inspiration for the ambition.
  - Bring in Spinoza as an ancestor in the relay, not a new protagonist.
- Non-Goals:
  - Naming or describing any implementation of the stack: no services, products, endpoints, event stores, runtimes, witnesses or schemas by name. The mapping is done in the book's own vocabulary: the assembly, its entries, evaluations, agents, gates, rulings and the diff queue.
  - A seventh component. A mode is not an entry. It is what an entry and an act make together at a gate.
  - A fifth prediction. A resolution prediction is available (e.g. "the swap changes the light but not the resolution, if the pair is held"). It rests on no results, so it is deferred like the last two.
  - Rewriting Ch7's scoping rule. The granularity test (split an entry; if agreement collapses, you are below resolution) is stated in Ch8 §III, not added to Ch7 as a second rule.
  - Spinoza's ethics, his politics, or *conatus*. Only parallelism, attribute and mode are imported.
  - "Photon of meaning", "witnessed judgment", "Spinozist ledger" as terms. They are scaffolding from the idea log. The book has one name for the unit.

## Decisions
- **Decision: The mapping from lithography to the book's vocabulary.**
  - **Light** is the machine's reading of conduct: the judgment a model or an evaluation makes about what an act was. It is the replaceable part, the thing the swap test changes.
  - **The mask** is the organization's resolved meaning, in two forms (see the two-masks decision).
  - **The pattern** is the *mode*: an act as read against the assembly and shaped by what the organization has resolved, recorded with its address and enforced at a gate.
  - Rationale: every term already exists in the book (Ch7 §IV, Ch8 §I–II). Nothing new is introduced except the name and the two measures.

- **Decision: The preface gets one or two paragraphs on ASML, placed after the hindsight paragraph and before the genre paragraph.**
  - Content: the name was borrowed from one piece of infrastructure, the ambition from another. To print features finer than its light could resolve, the chip industry needed a new light. ASML spent decades building an extreme-ultraviolet source at 13.5 nanometres, made by striking droplets of molten tin with a laser. Light does nothing alone: it passes through a mask carrying the designer's intent, and what it etches is the pattern. The book's ambition is the same in another field: a new source of light for meaning, and the discipline that lets it print something that holds. Machines that read meaning at scale may be that light. They are not the book's subject; the mask and the process are. This keeps runtime-independence intact. The unit is named in Ch8 and only foreshadowed here.
  - The idea log's beach-and-clouds origin (Aristophanes' *Clouds*) is left out unless the author opts it in (see Open Questions).

- **Decision: Spinoza enters Ch1 through Deleuze, in ≤ 2 paragraphs in §IV, after the virtual/actual paragraph and before "We do not follow Deleuze all the way down".**
  - Rationale: Deleuze's overturning of Platonism runs through Spinoza's immanence; Deleuze wrote two books on him. Arriving this way makes Spinoza an ancestor in the relay, the same way Wittgenstein arrives as Langer's source, rather than a new protagonist.
  - Content: one substance, known under two attributes, extension and thought. A *mode* is a particular thing, expressed under both at once, as a body and as an idea: not two things, one thing seen two ways. *Ethics* II, proposition 7: the order and connection of ideas is the same as the order and connection of things. Spinoza never builds the wall Kant would later build between things as they appear and things as they are, and he is not a mechanist: neither attribute reduces to the other. For the book this licenses holding an act and its meaning as a single record rather than a fact plus an annotation.
  - Kant is brought in by name as Spinoza's counterweight (author's answer, 2026-11-08): the ultimate tension is between the two. The second paragraph gives Kant's wall (appearances and things in themselves, the transcendental as the conditions of possible experience) and shows that the book's other line, the *Tractatus* ("logic is transcendental", 6.13) and Langer, runs through it. The tension is marked, not resolved. The book takes Spinoza's account of what a kept record *is* and keeps the transcendental strand's account of what any frame *cannot* hold (Ch10 §I, §IV).
  - Ch1 §VII ("What Remains") is not changed.

- **Decision: Ch8 gains "§III. Resolution" (≤ 5 paragraphs), after "The Loop". "The Taxes", "The Swap Test" and "The Pair" renumber to §IV–§VI.**
  - Rationale: the mode is the loop's unit, so it belongs right after the loop. Placing it before the swap test lets the λ lever explain why meaning survives the swap.
  - Content the section must carry:
    1. **The unit.** Each turn of the loop produces one thing: an act, read against an entry, ruled on where a ruling was needed, recorded with its address. The book calls it a *mode*, after Spinoza (pointer to Ch1): it sits in the causal order as an event that happened and in the conceptual order as a meaning it had, and the assembly keeps it as one record. One clause on why not *qualia*: qualia are private by definition, and a mode is public by nature. One sentence acknowledging that "mode" has a contested history in computing (Tesler's campaign against modal interfaces), and that the sense here is Spinoza's. Not a seventh component.
    2. **A unit is not a tolerance.** ASML's rigor is legible because it comes in numbers. The assembly's equivalent is its **resolution**: the finest distinction at which the machine's reading and the organization's ruling still reliably agree. The test: split an entry into two finer ones, and if agreement collapses, the assembly has gone below its resolution. **Overlay error** is their disagreement, measurable on every mode.
    3. **Three levers.** Rayleigh's criterion, resolution = k₁ · λ / NA, maps term by term. λ, the wavelength, is the fineness of the reading: the model. NA, the aperture, is how much context the reading gathers before it judges. k₁, the process factor, is the discipline that lets coarse light print fine features: the assembly itself. The swap test changes λ. If the pair is held, k₁ is what keeps the resolution.
    4. **Two masks.** In a scanner the mask is designed before the light passes. The assembly is that standing mask. But some rulings come after a reading, when a person decides what an act was. Fabs correct their masks once they see how patterns print (optical proximity correction), and rulings are the same kind of correction. Enough of them in one direction belong in the diff queue as a revision. A mode should therefore record which mask shaped it: the entry's version, and any ruling that corrected it.
    5. **Which side is wrong.** In lithography the mask is always right. In an assembly it is not: an entry cannot be falsified, but it can lose its point (Ch10 §III). So overlay error is ambiguous by design. Either the reading is off or the entry has aged. Deciding which is the work of the outer loop and of people, and the assembly's job is to make the disagreement visible and addressed, not to settle it. Forward pointer to Ch10.
  - Claims are sized: resolution and overlay are *proposed measures*. Nothing is reported as measured.

- **Decision: Ch10 §VI gets ≤ 1 paragraph naming the mode as the candidate unit of the retention era, after the relay paragraph and before Langer's paragraph.**
  - Content: the bit opened the book as the unit of transmission, the atom of distinction. If the retention era has a unit, the candidate is the mode, the atom of kept meaning: a distinction that was enforced and recorded with its address. Offered as labeled speculation. The book declines to assert it and hands the question to the reader, as the summary already promises.
  - Langer's paragraph is untouched and remains last.

- **Decision: Summaries.** Each summary is kept in three places (preface: `docs/index.md` only). All copies are edited together and stay identical:
  - Preface (`index.md`): add ASML.
  - Ch1 (`index.md`, `part-1.md`, front-matter `description`): add Spinoza as the source of Deleuze's immanence.
  - Ch8 (`index.md`, `part-3.md`, front-matter `description`): add the mode, resolution and overlay error.
  - Ch10 (`index.md`, `part-4.md`, front-matter `description`): name the mode in the retention-era sentence.

- **Decision: Works Cited.** Add Spinoza's *Ethics* (Curley translation recommended). Add a source for the ASML/EUV history (Miller, *Chip War*, 2022, recommended). Add Deleuze's *Spinoza: Practical Philosophy* or *Expressionism in Philosophy* only if quoted. Add Kant's *Critique of Pure Reason* (Guyer and Wood translation), which the Spinoza passage names. Add Tesler's modeless-editing history (*interactions*, 2012) if the acknowledgment sentence cites it. Rayleigh's criterion is stated as standard optics and is not cited.

- **Decision: Length budgets.** Preface ≤ 2 paragraphs. Ch1 ≤ 2 paragraphs. Ch8 new section ≤ 5 paragraphs. Ch10 ≤ 1 paragraph. The Rayleigh formula appears once, inline, the way Shannon's H appears in Ch2.

## Risks / Trade-offs
- **The mode reads as a seventh component.** Mitigation: Ch8 §III says explicitly that a mode is not an entry; Ch7 is untouched.
- **Spinoza and Kant take over Ch1.** Mitigation: Spinoza enters through Deleuze, the pair stays within a two-paragraph budget, and the tension is named rather than adjudicated. Langer still closes the book.
- **The lithography mapping overclaims.** Mitigation: it is introduced as an inspiration in the preface and as an analogy with named terms in Ch8, and the measures are proposed, not reported.
- **"Mode" collides with computing's usage.** Mitigation: one sentence acknowledges it. The author has accepted the collision.
- **Stack leakage.** Mitigation: a verification grep for implementation names.
- **Summary drift.** Mitigation: all copies are edited together and compared in tasks.

## Reffy Inputs
- logical-assembly-a-new-source-of-light.md
- logical-assembly-resolution-overlay-and-mode.md

## Open Questions
- Aristophanes: include one sentence in the preface on where the idea came from (philosophers looking up at the clouds, Socrates in his basket), or leave it out? The spec leaves it out.
<!-- Leave out. -->
- The Rayleigh formula: show it inline once (recommended, matching Shannon's H in Ch2), or keep the three levers in prose only?
<!-- I thought it was nice to see the formula and it unpacked in prose. -->
- Tesler: acknowledge computing's history with "mode" in one sentence (recommended), or say nothing?
<!-- Yes, acknowledge. -->
- Name Kant in the Spinoza passage (recommended, one clause), or describe the transcendental wall without naming him?
<!-- Yes, the ultimate philosophical tension is between Spinoza and Kant, so we should bring Kant in. -->
