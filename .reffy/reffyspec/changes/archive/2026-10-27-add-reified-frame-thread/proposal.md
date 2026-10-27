# Change: Add the reified-frame thread: bounded staleness, hinges, and residue

## Why
The transcript `lasm-conversation-transcript.md` reaches the book's own thesis from a different door. Starting from binding time and the first line of the *Tractatus*, it asks whether an event log escapes the Gödel–Turing circle, answers that the circle is only *relocated* to the frame (who drew the domain?), and then describes the LogicalAssembly as the move that reifies the frame: not the map but the map plus instrumentation on the places where the map is holding weight. Read against the manuscript as it stands on `main` (draft 0.21 plus the Wittgenstein thread), four of its ideas fill gaps the book currently papers over:

- **The guarantee is never named.** Chapters 5 and 8 say the loop's cycle time bounds how far staleness travels, but the book never says what a Lasm promises. The transcript does: not correctness but *bounded staleness at the load-bearing points*. The assembly cannot promise the map is right; it can promise that the places where the map is stood on are watched, and that detected divergence reaches a revision within the loop's clock.
- **Chapter 10 §II overclaims.** It says the assembly "can never be as blind as the artifacts it replaced, because blindness — divergence that no consequence reaches — is the specific condition the scoping rule was written to exclude." The scoping rule excludes *entries* nothing checks. It cannot exclude *reality* that reaches no gate. A frame registers stress only through the sensors it has, and the transcript's closed-world diagnosis (treating "not representable in my schema" as "not real") names the failure the book has no section for. The repair is a residue channel: what the gates turn away, kept deliberately unschematized, with its dynamics monitored and someone obliged to read it.
- **The regress is truncated, not dissolved, and the book should say by what.** Chapter 5 §III says the consequence-map regress "never starts" under enforcement. Chapter 10 §II supplies an outer loop but never says what validates the frame as a whole. The transcript's answer belongs in Chapter 6 §V: organizations do inherit one free loop, selection by solvency, and it is enforcement with no address, observable, never attributable, and fatally late. That is exactly why the loops must be built: to bring the verdict forward from the balance sheet to the gate.
- **The constitution figure in Chapter 10 §I lacks its amendment clause.** The archaeology surfaces commitments that are not entries at all: the things that define what load *means* ("we make money by selling cars"). On the later Wittgenstein's account these are hinges (*On Certainty* §§341–343), exempt from doubt because doubting them unravels the practice. A Lasm needs a declared floor of such commitments, chosen rather than inherited, outside the ordinary diff queue and amendable only by a slower process, so that the meta-level stays slow relative to the object level.

Three smaller imports sharpen existing passages without adding machinery: "reality never breaks" (enforcement does not prevent the break, it places it), Hyrum's Law (silence at a gate is evidence of a partition, not proof), and the agent as the latest-binding interpreter yet built (which says precisely why the assembly must bind the domain's terms before inference).

## What Changes
- **Chapter 5:** in §I, state that divergence always breaks on the representation's side and that enforcement chooses where and when the break surfaces. In §III, add Hyrum's Law: the as-built load surface exceeds the as-designed one, so an entry's silence at the gates is evidence of a partition, not proof.
- **Chapter 6:** in §V, name the one loop organizations do inherit, selection by solvency, as enforcement at the level of the organism rather than the entry.
- **Chapter 7:** in §IV, describe the agent as a late-binding interpreter and the assembly as what binds the domain's terms before inference.
- **Chapter 8:** in §II, name the loop's guarantee as bounded staleness at the load-bearing points. In §III, give the second tax its strain gauges at the admission boundary.
- **Chapter 10:** in §I, add the hinge floor and the amendment clause to the constitution figure. In §II, qualify the "never as blind" sentence. Add a new section, "The Closed World", between "Correlated Loss" and "The Predictions", on the residue channel; later sections renumber.
- **Front matter:** update the Chapter 10 summary everywhere it appears. Add *On Certainty* and the Hyrum's Law source to Works Cited.

## Impact
- Affected specs: `argument`, `construction`, `horizon`, `front-matter` (all pending from `add-wittgenstein-thread`; `specs/` is still empty, so these are ADDED requirements layered on that change's deltas)
- Affected content:
  - `docs/05-load-bearing.md`
  - `docs/06-the-physics-of-persistence.md`
  - `docs/07-anatomy-of-a-logicalassembly.md`
  - `docs/08-gates-and-swaps.md`
  - `docs/10-boundary-conditions.md`
  - `docs/99-works-cited.md`
  - `docs/index.md`
  - `docs/part-4.md`
- Not affected: the Preface, Chapters 1, 2, 3, 4 and 9. The six components and four properties of Chapter 7 are unchanged: the residue is an obligation on the gates, not a seventh component. No site configuration or theme changes.

## Supersedes
None

## Reffy References
- `lasm-conversation-transcript.md` - source of every idea in this change: bounded staleness as the guarantee, the closed-world diagnosis and residue channel, hinges and the amendment clause, solvency as the exogenous validator, "reality never breaks", Hyrum's Law, and binding time
- `weaving-wittgenstein-into-durable-forms.md` - ground rules carried over: import the philosophy not the rig, keep flagged analogies out, non-Kripkean reading, Langer keeps the last word, no fifth prediction without results
