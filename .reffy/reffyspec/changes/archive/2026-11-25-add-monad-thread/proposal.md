# Change: Add the monad thread: Leibniz, the participant, and three altitudes

## Why
The suggestion `suggestion-monads-and-three-altitudes.md` is written against Draft 0.35 and targets Draft 0.36. It confirms that 0.35 already holds most of the earlier thread: Spinoza and the mode (Ch1 §IV, Ch8 §III), Kant's wall named and declined (Ch1 §IV), and the hinges and "no frame draws itself" (Ch10 §I, §IV). It revises none of those. It finds two gaps that remain:

- **The loop has a unit but no participant.** Chapter 8 §III names the mode as "the one thing" each turn of the loop produces. Nothing names the party that reads the assembly, acts through it, and keeps its own derived view of what is recorded there. Leibniz's monad fits that party closely. Monads are windowless (*Monadology* §7). Each mirrors the whole from its own point of view (§56). They agree through a harmony (§78), not through interaction. The assembly is that harmony: participants agree because each reads the same declared meaning, not because they call one another. That is the narrow waist seen from the side of the parties it serves. Leibniz's harmony is *pre-established*, guaranteed by God, which is Plato's flaw again. The book already knows how to correct it: the harmony is kept, not given, just as Chapter 1 calls the assembly's authority "positional and earned, not essential and given".
- **Chapter 1 leaves the Spinoza–Kant question open with nowhere to hold it.** The book takes something from each side but never says how both can stand. Three altitudes would hold the question without settling it. At the record, Spinoza's single order holds, with the mode as its unit. At the participants, Leibniz's many points of view hold, kept in agreement. At the frame, Kant, the later Wittgenstein and Langer hold: the conditions under which anything can appear in the assembly at all, and the judgment that draws and amends them. Leibniz also completes the relay historically. He visited Spinoza in 1676 and read the *Ethics* in manuscript, and Kant's critical turn was largely a reaction against the Leibniz–Wolff school.

## What Changes
- **Chapter 1 §IV:** add one paragraph on Leibniz between the Spinoza paragraph and the Kant paragraph. It covers the monad, windowlessness, mirroring and pre-established harmony, and sets them up for Chapter 8. Adjust the Kant paragraph so Kant reacts to Leibniz as well as to Spinoza, and end it with a short forecast of the three altitudes.
- **Chapter 8 §III:** after the mode is named, add a passage naming the participant ("if the mode is the loop's unit, the monad is its participant"). It gives the five questions in prose, as a proposed form and not a demonstrated one, and reads the assembly as the harmony and each participant's derived state as its mirror. It gives the identity of indiscernibles as a practical test and corrects the harmony from pre-established to kept. It also keeps *participant* and *projection* apart.
- **Chapter 10 §VI:** add one paragraph setting out the three altitudes, before Langer's paragraph. It places Kant's judgment (the *Critique of Judgment*) at the frame altitude, pointing back to "no frame draws itself" (§IV). It says plainly that Spinoza and Leibniz were rivals used here as levels. Langer keeps the last word.
- **Front matter:** update the Chapter 1, Chapter 8 and Chapter 10 summaries wherever they appear. Add Works Cited entries for the *Monadology* and the *Critique of Judgment*.

The book stays high level. Leibniz is the only new proper-noun protagonist. The applied work's term ("use case") and any implementation of the stack go unnamed.

## Impact
- Affected specs: `inheritance`, `construction`, `horizon`, `front-matter`
- Affected content:
  - `docs/01-inherited-forms.md`
  - `docs/08-gates-and-swaps.md`
  - `docs/10-boundary-conditions.md`
  - `docs/99-works-cited.md`
  - `docs/index.md`
  - `docs/part-1.md`
  - `docs/part-3.md`
  - `docs/part-4.md`
- Not affected: the Preface, Chapters 2–7 and 9. Chapter 7's six components and four properties are unchanged, because a participant is not a seventh component. Chapter 9's account of projections as "derived, plural, disposable" is unchanged; the new text keeps to it. Chapter 10's predictions are unchanged. No site configuration or theme changes. `scripts/push.sh` bumps the draft version to 0.36 on push.

## Supersedes
None

## Reffy References
- `suggestion-monads-and-three-altitudes.md` - Leibniz between Spinoza and Kant; the monad as participant and the assembly as kept harmony; the five questions; the identity of indiscernibles as a test; the participant/projection tension; the three altitudes; and the cautions (rivals used as levels, self-referential evidence, the book's own word for "use case")
