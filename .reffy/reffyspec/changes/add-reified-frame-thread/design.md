## Context
The source artifact is a conversation, not a suggestions note, so this design does the sorting the earlier Wittgenstein note did for itself: which of the conversation's ideas go in, where, at what length, and which stay out. It is read against `main` after `add-wittgenstein-thread` landed (commit 19f52e3), and it respects that change's decisions (translations, the non-Kripkean reading, Langer's last word, the deferred fifth prediction).

### Problem Summary
- The book never states what a Lasm guarantees. The nearest it comes is "the cycle time bounds how far a divergence can travel" (Ch5 §I, Ch8 §II).
- Ch10 §II claims the assembly "can never be as blind as the artifacts it replaced." The scoping rule excludes unchecked entries, not unreached reality. The book has no account of what happens when the world arrives at no gate, and no answer to the closed-world assumption.
- Ch6 §V says organizations inherit no loop. They inherit one, solvency, and naming it both strengthens the asymmetry argument and supplies the exogenous validation Ch10 §II's outer loop quietly needs.
- Ch10 §I calls adopting a Lasm "choosing a constitution for its meaning" but gives the constitution no floor and no amendment clause.

## Goals / Non-Goals
- Goals:
  - State the guarantee once, in Chapter 8, and have Chapter 10 inherit it.
  - Give Chapter 10 a third exposure, the closed world, with the residue channel as its architectural answer, and correct the "never as blind" sentence so it no longer contradicts the new section.
  - Add the hinge floor to the constitution figure using *On Certainty*, in the book's existing Wittgenstein register.
  - Keep each other import to one paragraph or less.
- Non-Goals:
  - Adding a seventh component to the anatomy. The residue is a property of the gates (what they turn away) and an obligation on the organization (someone reads it), not a kind of entry. Chapter 7's six components and four properties stand.
  - Importing the foundations-of-mathematics panorama (Frege, Russell, Hilbert, Gödel, Turing). The relocation of the circle to the frame can be stated without it, and the book has no apparatus for diagonal arguments.
  - Adding a fifth prediction to Ch10. A residue prediction is available ("organizations whose gates record what they turn away detect frame shifts earlier") but it is hard to falsify and rests on no results. Same deferral as the previous change.
  - Any rig material, probes, or measurements.

## Decisions
- **Decision: The residue gets its own section in Chapter 10, placed as the third exposure.**
  - Rationale: Ch10 is organized as boundary, exposures, predictions. The closed world is an exposure of the same rank as the commitment (§II) and correlated loss (§III), and it is the one the book currently denies. Putting it in §II as a qualification would bury the correction. New order: §I Boundary, §II Commitment, §III Correlated Loss, §IV The Closed World, §V The Predictions, §VI What Is Kept.
  - Content the section must carry, from the transcript: hubris has a formal signature, the closed-world assumption; the residue is what the gates reject or cannot parse; it must stay the *least* typed part of the system, because structuring it annexes it into the frame and the true residue moves outside again (the `other` category that gets three subcategories and resets the gauge); what can be typed is its dynamics (volume, recurrence, clustering, which gate it arrived at); zero residue is the alarm condition; clustering residue is reality proposing a category, and the diff queue is where the proposal is heard; the assembly can detect accumulation but cannot judge what it means, so the standing obligation that someone with authority reads it is a commitment of §II's kind.
- **Decision: The "never as blind" sentence in §II is qualified, not deleted.**
  - Rationale: It is true of what the assembly checks. Revise it to say so ("as blind to what it checks") and point forward to §IV for what reaches no gate.
- **Decision: Hinges go at the end of Ch10 §I as a coda, not as a fourth category.**
  - Rationale: The three categories are things that land on the adjudication table and should be declined. Hinges never land on the table, because they are what makes the table a table. The coda extends the constitution figure already in §I with its amendment clause: declared, visible, chosen rather than inherited, outside the ordinary diff queue, changed only by a slower and costlier process. Cite *On Certainty* §§341–343. Quote "my spade is turned" from PI §217 if quoted at all. The transcript attributes it to *On Certainty*; that is wrong.
  - The Kodak example from the transcript is not used unless the author pins a source. The stock version (Kodak missed digital) is contested; the transcript's version (the residue was logged, the judgment failed) is the useful one but needs a citation the book does not have.
- **Decision: The guarantee is stated in Ch8 §II, right after "latency is this loop's clock".**
  - Rationale: That is where the loop's clock is introduced, and the guarantee is a statement about the clock. Three sentences at most. Ch10 §IV then inherits it: the bound covers only what reaches a gate.
- **Decision: Solvency goes in Ch6 §V, after the line-item sentence.**
  - Rationale: It is a refinement of the asymmetry, not a new argument. One paragraph: organizations inherit one loop, selection by solvency; it validates the frame as a whole, runs at the speed of liquidation, and names no entry. Observable, never attributable, fatally late. The built loops bring the verdict forward from the balance sheet to the gate. Do not cite Simon; the point is made in the book's own vocabulary.
- **Decision: Ch5 gets two short insertions, and no new section.**
  - §I, after the latency paragraph: divergence breaks on the representation's side, always; enforcement does not prevent the break, it places it (silent and diffuse downstream, or loud and named at the gate). The crumple-zone image may be used once. No "parse, don't validate" slogan.
  - §III, after the maintenance-allocation paragraph: Hyrum's Law. The as-built load surface exceeds the as-designed one; silence at a gate is evidence of a partition, not proof. Cite Winters, Manshreck and Wright (2020), chapter 1. This is also the first signpost toward Ch10 §IV.
- **Decision: Ch7 §IV gets the binding-time paragraph, with a kill switch.**
  - Rationale: It is the one place in the book that is already about agents as consumers, and the point is sharp: an agent fixes the meaning of a request at inference time, from the record of use, unless the domain's terms were bound earlier; the assembly is that earlier binding, and a bound meaning is an artifact that can be read, diffed and rerun where an interpretation is ephemeral. No Futamura, no JIT. If the author finds it pulls the book toward LLM engineering, drop it; nothing else depends on it.
- **Decision: Ch8 §III second tax gets its instruments.** Two sentences naming the strain gauges at the admission boundary: rising rejections, swelling catch-all categories, free-text fields carrying structure the schema has no column for. This is the telemetry mode of enforcement already named there, made concrete, and it is where Ch10 §IV's residue is measured.
- **Decision: Length budgets.** Ch10 new section ≤ 5 paragraphs. Ch10 §I coda ≤ 2 paragraphs. Ch10 §II revision ≤ 1 sentence changed. Every other insertion ≤ 1 paragraph. Ch8 §II ≤ 3 sentences. Ch8 §III ≤ 2 sentences.
- **Decision: Keep the set-aside list set aside.** Foundations panorama; the reading of TLP proposition 1 as definition by exclusion (Ch7 §I's colour-exclusion gloss already does that work); Futamura and JIT; Simon's satisficing; Lakatos's hard core and protective belt; Conant–Ashby's good regulator theorem (a fourth derivation is available here, but the theorem says a regulator must contain a model, not that the model must be enforced, and three lines is enough); Peirce's abduction; "the language game is the API"; the compile/interpret amortization argument.

## Risks / Trade-offs
- **Chapter 10 grows by a section.** Mitigation: the length budget; and the section replaces an overclaim, so it earns its place.
- **The residue reads as a seventh component.** Mitigation: the section says explicitly that it is not one, and Chapter 7 is untouched.
- **Hinges are read as "some entries are unrevisable", which contradicts the diff discipline.** Mitigation: hinges are not entries, and they are amendable; the amendment process is slower, not absent. Say so.
- **Too many new authorities.** Mitigation: only two new Works Cited entries (*On Certainty*; Winters, Manshreck and Wright). Everything else is said in the book's voice.
- **Summary drift.** The Chapter 10 summary is kept in three places (`docs/index.md`, `docs/part-4.md`, the chapter's front-matter `description`). All three are edited together.

## Reffy Inputs
- lasm-conversation-transcript.md

## Open Questions
- Section placement in Chapter 10: a new §IV with renumbering (recommended), or the residue folded into §II as a second paragraph? The spec assumes the former.
<!-- let's go with the new section -->
- Keep the Chapter 7 §IV binding-time paragraph, or drop it as the one import most likely to pull the book toward LLM engineering?
<!-- I'm not sure what you're referring to here. I've read that section, but don't see where the LLM engineering is mentioned. I see ideas about agents as a new consumer. -->
- Kodak: include with a pinned source, or leave out? The spec leaves it out.
<!-- leave out -->
- Hyrum's Law citation: the O'Reilly book (recommended) or hyrumslaw.com?
<!-- book -->
