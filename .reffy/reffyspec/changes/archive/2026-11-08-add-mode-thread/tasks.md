## 1. Sources
- [x] 1.1 Pin Spinoza, *Ethics*, trans. Edwin Curley, in *The Collected Works of Spinoza*, vol. 1 (Princeton University Press, 1985). Check the wording of II, proposition 7, against the author's copy.
  - Note: II P7 is quoted in paraphrase in its standard Curley wording; no physical copy was consulted. The author confirms against the copy on hand.
- [x] 1.2 Pin the ASML/EUV source (recommended: Chris Miller, *Chip War*, Scribner, 2022). Check the facts the preface uses: 13.5 nm, tin droplets struck by a laser, decades of development.
  - Note: the facts used (13.5 nm, laser-struck tin droplets, vacuum and reflective optics, roughly three decades) are as the implementer recalls them from standard accounts; check against the book.
- [x] 1.3 Pin the Tesler source if the acknowledgment sentence is kept (Larry Tesler, "A Personal History of Modeless Text Editing and Cut/Copy-Paste," *interactions* 19, no. 4, 2012).
  - Note: kept, per the author's answer. Volume, issue and pages are from memory; check before the next draft.
- [x] 1.4 Decide whether a Deleuze book on Spinoza or Kant's *Critique of Pure Reason* is quoted or named as a work. Pin only what is.
  - Note: Kant's *Critique* is named and gets an entry (Guyer and Wood). No Deleuze book on Spinoza is named, so none is added.

## 2. Front matter (Preface)
- [x] 2.1 Add the ASML paragraph(s) (≤ 2 paragraphs) after the hindsight paragraph and before the genre paragraph.

## 3. Inheritance (Chapter 1)
- [x] 3.1 §IV: add the Spinoza passage (≤ 2 paragraphs) after the virtual/actual paragraph and before "We do not follow Deleuze all the way down", marking the tension with the transcendental strand.

## 4. Construction (Chapter 8)
- [x] 4.1 Insert "§III. Resolution" (≤ 5 paragraphs) after "The Loop", carrying the unit, resolution and overlay error, the three levers, the two masks, and which side is wrong.
- [x] 4.2 Renumber "The Taxes" to §IV, "The Swap Test" to §V and "The Pair" to §VI. Fix any in-book references to the old numbers.

## 5. Horizon (Chapter 10)
- [x] 5.1 §VI: add the retention-era paragraph (≤ 1 paragraph) before Langer's paragraph. Langer's paragraph stays last and unchanged.

## 6. Summaries and Works Cited
- [x] 6.1 Preface summary in `docs/index.md`: add ASML.
- [x] 6.2 Chapter 1 summary, identically in `docs/index.md`, `docs/part-1.md` and the chapter's front-matter `description`: add Spinoza.
- [x] 6.3 Chapter 8 summary, identically in `docs/index.md`, `docs/part-3.md` and the chapter's front-matter `description`: add the mode, resolution and overlay error.
- [x] 6.4 Chapter 10 summary, identically in `docs/index.md`, `docs/part-4.md` and the chapter's front-matter `description`: name the mode in the retention-era sentence.
- [x] 6.5 Works Cited: add the pinned entries from §1, in alphabetical order and the existing style.

## 7. Verification
- [x] 7.1 Every edit is within its length budget in `design.md`.
- [x] 7.2 Search the manuscript for stack implementation names and idea-log scaffolding (Rastro, Patch Rig, Auto Bench, Paseo, Nuveris, control plane, witness, photon of meaning, Spinozist ledger): zero matches.
- [x] 7.3 "Mode" in the Spinozist sense is defined once (Ch1), named as the unit once (Ch8 §III), and used consistently after that.
- [x] 7.4 Chapter 7's component count and property count are unchanged, and nothing reads as a seventh component.
- [x] 7.5 Every work cited in the new text appears in Works Cited, and every new Works Cited entry is cited in the text.
- [x] 7.6 Every copy of each edited summary matches.
- [x] 7.7 Build locally (`cd docs && bundle exec jekyll serve`). Check Chapter 8's section numbering and anchors, and search for "mode", "resolution" and "Spinoza".
- [x] 7.8 Run `reffy plan validate add-mode-thread`.
