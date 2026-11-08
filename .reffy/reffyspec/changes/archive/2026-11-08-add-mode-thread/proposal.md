# Change: Add the mode thread: ASML, Spinoza, and the resolution of meaning

## Why
Two new artifacts reach the book from a direction it has not used yet: optics. The idea log `logical-assembly-a-new-source-of-light.md` takes ASML's extreme-ultraviolet lithography as the model of the ambition. To print finer features, the industry had to invent a new source of light. The log asks what the fundamental unit of a LogicalAssembly is, rejects *qualia*, and finds Spinoza's parallelism on the way: the order and connection of ideas is the same as the order and connection of things. The response `logical-assembly-resolution-overlay-and-mode.md` separates the unit from the tolerance, maps Rayleigh's resolution criterion onto the assembly, splits the mask in two, and proposes Spinoza's *mode* as the unit's name.

Read against the manuscript on `main` (draft 0.34), these ideas fill four gaps:

- **The book has a unit for the transmission era and none for the retention era.** Chapter 2 is built on the bit. The Chapter 10 summary promises the question "whether something with the Lasm's properties becomes the unit of the retention era", but the chapter text never asks it. The *mode* answers it: one act, read against the assembly and recorded with its address, kept as one thing under two descriptions, the event that happened and the meaning it had.
- **The book measures durability but not fineness.** The swap test measures how much meaning survives a change of runtime. Nothing in the book says how *fine* a distinction the assembly can hold and still enforce. Lithography's two numbers, resolution and overlay error, supply that: the finest distinction at which the machine's reading of conduct and the organization's ruling on it still agree, and the size of their disagreement on each act.
- **The preface credits the name's inspiration but not the ambition's.** WebAssembly gave the book its name. ASML gave it its ambition, and the book should say so where it says the rest.
- **Spinoza is the missing ancestor of the book's anti-dualism.** Chapter 1 reaches Deleuze without the philosopher Deleuze took his immanence from. Spinoza supplies the one thing the relay lacks: a reason to hold an event and its meaning as a single record rather than two linked ones. The tension with the transcendental strand (the *Tractatus*, Langer) is real, and the book should hold it openly rather than resolve it.

## What Changes
- **Preface:** add ASML and extreme-ultraviolet lithography as the second, named inspiration: Wasm for the name, ASML for the ambition, a new source of light for meaning.
- **Chapter 1:** in §IV, introduce Spinoza as the ancestor of Deleuze's immanence. Cover parallelism, the mode, and the refusal of Kant's wall, and mark the tension with the transcendental strand.
- **Chapter 8:** add a new section, "Resolution", after "The Loop". Name the mode as the loop's unit. State resolution and overlay error, the three levers, the two masks, and the open question of which side is wrong when they disagree. Later sections renumber.
- **Chapter 10:** in §VI, name the mode as the candidate unit of the retention era, as labeled speculation, so the chapter text finally matches its summary. Langer keeps the last word.
- **Front matter:** update the Preface, Chapter 1, Chapter 8 and Chapter 10 summaries everywhere they appear. Add Works Cited entries for Spinoza, the ASML source, and anything else the new text cites.

The book stays high level. ASML and Spinoza are named. No component, service or product of any implementation of the stack is named or described.

## Impact
- Affected specs: `front-matter`, `inheritance`, `construction`, `horizon`
- Affected content:
  - `docs/00-preface.md`
  - `docs/01-inherited-forms.md`
  - `docs/08-gates-and-swaps.md`
  - `docs/10-boundary-conditions.md`
  - `docs/99-works-cited.md`
  - `docs/index.md`
  - `docs/part-1.md`
  - `docs/part-3.md`
  - `docs/part-4.md`
- Not affected: Chapters 2–7 and 9. Chapter 7's six components and four properties are unchanged: a mode is not an entry and not a seventh component. Chapter 10's predictions are unchanged. No site configuration or theme changes.

## Supersedes
None

## Reffy References
- `logical-assembly-a-new-source-of-light.md` - the ASML ambition (a new source of light for meaning), the rejection of qualia, light / mask / pattern, Spinoza's parallelism and the transcendental impasse, models as a new instrument for probing the limits of mechanism
- `logical-assembly-resolution-overlay-and-mode.md` - unit versus tolerance, Rayleigh's criterion and its three levers, resolution of the codebook, overlay error, the two masks (standing mask and corrections), *mode* as the name, and the question of which side is wrong
