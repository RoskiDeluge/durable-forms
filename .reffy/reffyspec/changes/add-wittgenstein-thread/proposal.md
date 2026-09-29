# Change: Add a Wittgenstein thread to Durable Forms

## Why
*Durable Forms* tells its inheritance as a relay of corrections: keep Plato's architecture, amend his physics. It never mentions Wittgenstein, yet he is the one thinker who carried out that amendment within a single career. The *Tractatus* is a total, fixed logical space that nothing maintains. The *Investigations* puts meaning in use and makes a rule's content depend on a practice. The ideation note `weaving-wittgenstein-into-durable-forms.md`, written in response to `logical-space-latent-space-and-lasm.md` (project `in-vitro-patching`, workspace `lasm-v1`), shows that bringing him in does more than decorate the book:

- The load-bearing thesis gains a third independent derivation from the rule-following remarks. The existing two are the graveyard and constructor theory.
- It repairs a real tension in Chapter 10 §III, where "the organization's meaning by definition" reads as though whatever review admits is correct.
- It gives Chapter 9 a principled account of what a foundation model lacks and why the assembly supplies it.

The author has settled the open questions: Wittgenstein is a *thread* running through the book, not a single station in Chapter 1; the Preface changes; the *Investigations* is quoted in Anscombe's translation; and Langer's debt to the *Tractatus* is asserted as it stands.

## What Changes
- **Preface:** stop setting aside the philosophical lineage of "Logical" and add a sentence on Tractarian logical form next to ANSI/SPARC.
- **Chapter 1:** add a short section on Wittgenstein between §I and §II. Name the *Tractatus* as the source of Langer's "logical form". Update the chapter intro and §VI to include him in the relay.
- **Chapters 5–6:** add the rule-following argument (PI §202, §258) as a third independent derivation of the load-bearing thesis. Update Chapter 6's convergence claim from two lines of argument to three.
- **Chapter 7:** gloss constraints as material exclusions (TLP 2.061, 6.3751; the 1929 paper). Add a "not a logical space" fence to §III.
- **Chapter 9:** in §III, describe the dense substrate as the *record of use* and name what that record does not contain. In §II, introduce the binding as a downward projection.
- **Chapter 10:** in §I, set the formalization boundary against the Tractarian say/show line and Langer's answer to it. In §III, ground "an entry ages, it is not wrong" in PI §50 and §142. In §V, add Wittgenstein to the arrival of the relay.
- **Front matter:** update the Chapter 1 summary everywhere it appears. Add Wittgenstein, Janik and Toulmin, and the rule-following reading to Works Cited.

## Impact
- Affected specs: `front-matter`, `inheritance`, `argument`, `construction`, `horizon` (all new; `specs/` was empty)
- Affected content:
  - `docs/00-preface.md`
  - `docs/01-inherited-forms.md`
  - `docs/05-load-bearing.md`
  - `docs/06-the-physics-of-persistence.md`
  - `docs/07-anatomy-of-a-logicalassembly.md`
  - `docs/09-projections-and-substrates.md`
  - `docs/10-boundary-conditions.md`
  - `docs/99-works-cited.md`
  - `docs/index.md`
  - `docs/part-1.md`
- Not affected: Chapters 2, 3, 4 and 8, which stay as they are. No site configuration or theme changes.

## Supersedes
None

## Reffy References
- `weaving-wittgenstein-into-durable-forms.md` - planning input artifact: suggestions 1–9, ground rules, and the author's answers to the open questions
- `logical-space-latent-space-and-lasm.md` (`in-vitro-patching`, `lasm-v1`) - upstream source of the philosophical reading; not linked locally
