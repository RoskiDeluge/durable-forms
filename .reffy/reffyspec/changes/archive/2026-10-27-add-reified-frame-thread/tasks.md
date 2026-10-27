## 1. Sources
- [x] 1.1 Pin *On Certainty* (Anscombe and von Wright, eds.; Paul and Anscombe, trans.; Blackwell, 1969) and check §§341–343 against the author's copy.
  - Note: the §341 and §343 wordings match the standard Paul–Anscombe text as the implementer recalls them; no physical edition was consulted. The author confirms against the copy on hand.
- [x] 1.2 Confirm "my spade is turned" is PI §217 in Anscombe's wording, if the coda quotes it. The transcript misattributes it to *On Certainty*.
  - Note: quoted in Ch10 §I from PI §217; same caveat as 1.1.
- [x] 1.3 Pin the Hyrum's Law source: Winters, Manshreck and Wright, *Software Engineering at Google* (O'Reilly, 2020), chapter 1, or hyrumslaw.com, per the author's answer to the open question.

## 2. Argument (Chapters 5–6)
- [x] 2.1 Ch5 §I: add the paragraph on where the break surfaces (≤ 1 paragraph) after the latency paragraph.
- [x] 2.2 Ch5 §III: add the Hyrum's Law paragraph (≤ 1 paragraph) after the maintenance-allocation paragraph, with a forward pointer to Chapter 10.
- [x] 2.3 Ch6 §V: add the solvency paragraph (≤ 1 paragraph) after "a line item is negotiable in a way that extinction is not."

## 3. Construction (Chapters 7–8)
- [x] 3.1 Ch7 §IV: add the binding-time paragraph (≤ 1 paragraph), unless the author drops it.
  - Note: included (author's answer, 2026-10-26). Self-contained; delete the one paragraph to drop it.
- [x] 3.2 Ch8 §II: state the guarantee as bounded staleness at the load-bearing points (≤ 3 sentences) after "latency is this loop's clock".
- [x] 3.3 Ch8 §III: name the strain gauges at the admission boundary in the second tax (≤ 2 sentences).

## 4. Horizon (Chapter 10)
- [x] 4.1 §I: add the hinge coda (≤ 2 paragraphs) after the third category, extending the constitution figure with its amendment clause.
- [x] 4.2 §II: qualify "it can never be as blind as the artifacts it replaced" to cover what the assembly checks, with a forward pointer to §IV.
- [x] 4.3 Insert "§IV. The Closed World" (≤ 5 paragraphs) between "Correlated Loss" and "The Predictions". Renumber "The Predictions" to §V and "What Is Kept" to §VI.
- [x] 4.4 Check that the new section states the guarantee's limit in Ch8's terms: the bound covers only what reaches a gate.
- [x] 4.5 Check that nothing in the new section reads as a seventh component.

## 5. Front matter
- [x] 5.1 Update the Chapter 10 summary, identically, in `docs/index.md`, `docs/part-4.md` and the front-matter `description` of `docs/10-boundary-conditions.md`, adding the closed world and residue to the list of exposures.
- [x] 5.2 Works Cited: add *On Certainty* and the Hyrum's Law source, in alphabetical order and the existing style.

## 6. Verification
- [x] 6.1 Every edit is within its length budget in `design.md`.
- [x] 6.2 Search the manuscript for Gödel, Turing, Futamura, Simon, Lakatos, Ashby, Peirce, Kodak: zero matches (unless the author opts Kodak in with a source).
- [x] 6.3 Every work cited in the new text appears in Works Cited, and every new Works Cited entry is cited in the text.
- [x] 6.4 The three copies of the Chapter 10 summary match.
- [x] 6.5 Chapter 7's component count and property count are unchanged.
- [x] 6.6 Build locally (`cd docs && bundle exec jekyll serve`). Check Chapter 10's section numbering and anchors, and search for "residue" and "hinge".
- [x] 6.7 Run `reffy plan validate add-reified-frame-thread`.
