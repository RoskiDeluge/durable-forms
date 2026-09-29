## 1. Sources
- [x] 1.1 Pin the editions: *Tractatus* (Pears–McGuinness 1961, unless the author chooses Ogden) and *Investigations* (Anscombe 1953).
- [ ] 1.2 Check every quotation against the pinned edition: TLP 2.0124, 2.0271, 2.061, 2.18, 3.42, 6.3751; PI §43, §50, §130–131, §142, §202, §258.
  - Note: the quoted wordings match the standard P–M and Anscombe texts as the implementer recalls them, but no physical edition was consulted. The author confirms against the copies on hand.
- [ ] 1.3 Record the *Philosophy in a New Key* passages that support Langer's debt to the *Tractatus* (chapter and page).
  - Note: needs the author's copy.
- [ ] 1.4 Confirm the Janik and Toulmin "Platonic myth" and "sphere of what can only be shown" passages (page numbers).
  - Note: needs the author's copy. The "Platonic myth" wording is taken from the excerpt in `phase-logical-latent-space.md`.

## 2. Inheritance (Chapter 1)
- [x] 2.1 Add the Wittgenstein section between §I and §II (≤ 3 paragraphs): the *Tractatus* as the most rigorous Platonism, the *Investigations* as the correction, the "Platonic myth" line. Renumber later sections.
- [x] 2.2 Name the *Tractatus* as the source of Langer's "logical form" in §II.
- [x] 2.3 Add Wittgenstein to the chapter intro's list of the relay.
- [x] 2.4 Reflect Wittgenstein's correction in §VI "What Remains".

## 3. Argument (Chapters 5–6)
- [x] 3.1 Add the rule-following paragraph (PI §202, §258) at the end of Ch5 §IV, and adjust the handoff sentence ("That derivation exists. It comes from physics") so it no longer implies physics is the only independent derivation.
- [x] 3.2 Update Ch6 §IV's convergence claim from two arguments to three, keeping "convergence is not proof".

## 4. Construction (Chapters 7 and 9)
- [x] 4.1 Ch7 §I: add a gloss (≤ 2 sentences) on constraints as exclusions (TLP 2.061, 6.3751; "Some Remarks on Logical Form", 1929).
- [x] 4.2 Ch7 §III: add the "not a logical space" fence (PI §130–131).
- [x] 4.3 Ch9 §III: add the "record of use" passage (PI §43), naming what the substrate lacks: invariants, policies, authority.
- [x] 4.4 Ch9 §II: add the binding paragraph, describing it as a downward projection that is derived, model-specific, re-measured at every swap and never frozen into weights.

## 5. Horizon (Chapter 10)
- [x] 5.1 §I: set the tacit category against the Tractarian say/show line and Langer's answer to it (≤ 2 sentences). Langer keeps the emphasis.
- [x] 5.2 §III: revise "the organization's meaning by definition … What an entry can do is age" using PI §50 (the entry as a standard) and §142 (losing its point), in the non-Kripkean reading.
- [x] 5.3 §V: add Wittgenstein to "The relay of Chapter 1 arrives with it" (≤ 2 sentences), leaving Langer's last word intact.

## 6. Front matter
- [x] 6.1 Preface: revise the "Logical" paragraph so it no longer dismisses the philosophical lineage, and add Tractarian logical form (≤ 3 sentences).
- [x] 6.2 Update the Chapter 1 summary to include Wittgenstein, identically, in `docs/index.md`, `docs/part-1.md` and the front-matter `description` of `docs/01-inherited-forms.md`.
- [x] 6.3 Works Cited: add the *Tractatus*, the *Investigations*, "Some Remarks on Logical Form", Janik and Toulmin, and Baker and Hacker (or McDowell), in alphabetical order and the existing style.

## 7. Verification
- [x] 7.1 Every edit is within its length budget in `design.md`.
- [x] 7.2 Search the manuscript for Nuveris, vindex, patchrig, LARQL and PRH: zero matches.
- [x] 7.3 Every work cited in the new text appears in Works Cited, and every new Works Cited entry is cited in the text.
- [x] 7.4 The three copies of the Chapter 1 summary match.
- [x] 7.5 Build locally (`cd docs && bundle exec jekyll serve`). Check Chapter 1's section numbering and anchors, the sidebar, and search for "Wittgenstein".
- [x] 7.6 Run `reffy plan validate add-wittgenstein-thread`.
