## ADDED Requirements
### Requirement: Preface acknowledges the philosophical lineage of "Logical"
The Preface's paragraph on the word "Logical" SHALL keep ANSI/SPARC data independence as the word's primary lineage. It SHALL NOT set the philosophical lineage aside, and it SHALL name Tractarian logical form, the form a representation must share with what it represents, as the same layer named from the other end. The addition SHALL be no longer than three sentences.

#### Scenario: Reader reaches the "Logical" paragraph
- **WHEN** a reader reads the Preface's paragraph on "Logical"
- **THEN** ANSI/SPARC is still presented as the lineage closest to the book's subject
- **AND** the paragraph no longer says the philosophical lineage is less relevant
- **AND** it names the early Wittgenstein's (and Langer's) logical form

### Requirement: Chapter 1 summary names Wittgenstein consistently
The Chapter 1 summary SHALL include Wittgenstein's place in the relay, and its text SHALL be identical in `docs/index.md`, `docs/part-1.md`, and the front-matter `description` of `docs/01-inherited-forms.md`.

#### Scenario: Summaries compared
- **WHEN** the three copies of the Chapter 1 summary are compared
- **THEN** all three mention Wittgenstein
- **AND** the three texts match

### Requirement: Works Cited covers the Wittgenstein thread
Works Cited SHALL list every work the thread cites: the *Tractatus Logico-Philosophicus* in the pinned translation; the *Philosophical Investigations* in Anscombe's translation; "Some Remarks on Logical Form" (1929); Janik and Toulmin, *Wittgenstein's Vienna* (1973); and the adopted rule-following reading (Baker and Hacker 1984, or McDowell 1984). Entries SHALL follow the existing alphabetical order and citation style.

#### Scenario: Citation audit
- **WHEN** each work cited in the new manuscript text is checked against Works Cited
- **THEN** every such work has an entry
- **AND** every new entry is cited somewhere in the text
