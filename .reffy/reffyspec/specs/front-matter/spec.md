# front-matter Specification

## Purpose
TBD - created by archiving change add-wittgenstein-thread. Update Purpose after archive.

## Requirements

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

### Requirement: Chapter 10 summary names the closed world consistently
The Chapter 10 summary SHALL add the closed world and its residue to the list of exposures, and its text SHALL be identical in `docs/index.md`, `docs/part-4.md`, and the front-matter `description` of `docs/10-boundary-conditions.md`.

#### Scenario: Summaries compared
- **WHEN** the three copies of the Chapter 10 summary are compared
- **THEN** all three mention the closed world
- **AND** the three texts match

### Requirement: Works Cited covers the reified-frame thread
Works Cited SHALL add *On Certainty* (Wittgenstein; Anscombe and von Wright, eds.; Blackwell, 1969) and the pinned source for Hyrum's Law (Winters, Manshreck and Wright, *Software Engineering at Google*, O'Reilly, 2020, or hyrumslaw.com). Entries SHALL follow the existing alphabetical order and citation style.

#### Scenario: Citation audit
- **WHEN** each work cited in the new manuscript text is checked against Works Cited
- **THEN** every such work has an entry
- **AND** every new entry is cited somewhere in the text
- **AND** no entry is added for a work the design lists as set aside

### Requirement: Preface names ASML as the inspiration for the ambition
The Preface SHALL add, after the paragraph on understanding the name in hindsight and before the closing word on genre, no more than two paragraphs naming ASML and extreme-ultraviolet lithography as the book's second inspiration: WebAssembly for the name, ASML for the ambition. They SHALL say that the chip industry had to invent a new source of light to print finer features, that light passes through a mask carrying intent before it etches a pattern, and that the book's ambition is a new source of light for meaning together with the discipline that lets it print something that holds. They SHALL keep the book's runtime-independence: machines that read meaning MAY be named generically as the light, and SHALL NOT be named as products. They SHALL NOT name or describe any implementation of the stack.

#### Scenario: Reader finishes the Preface
- **WHEN** a reader reaches the closing word on genre
- **THEN** both inspirations have been named, Wasm for the name and ASML for the ambition
- **AND** the image of light, mask and pattern has been set up for Chapter 8
- **AND** no foundation model, vendor or stack component is named

### Requirement: Summaries name the mode thread consistently
The Preface summary in `docs/index.md` SHALL mention ASML. The Chapter 1 summary SHALL mention Spinoza, the Chapter 8 summary SHALL mention the mode, resolution and overlay error, and the Chapter 10 summary SHALL name the mode in its retention-era sentence. Each summary SHALL be identical everywhere it appears (`docs/index.md`, the part page, and the chapter's front-matter `description`).

#### Scenario: Summaries compared
- **WHEN** the copies of the Chapter 1, Chapter 8 and Chapter 10 summaries are compared
- **THEN** each copy carries the new material
- **AND** the copies of each summary match

### Requirement: Works Cited covers the mode thread
Works Cited SHALL add Spinoza's *Ethics* in the pinned translation and the pinned source for the ASML and extreme-ultraviolet history. It SHALL add Kant's *Critique of Pure Reason* and Tesler's history of modeless editing as the sources for the passages that name them. It SHALL add a work by Deleuze on Spinoza only if the new text quotes or names that work. Entries SHALL follow the existing alphabetical order and citation style. Rayleigh's criterion SHALL NOT get an entry.

#### Scenario: Citation audit
- **WHEN** each work cited in the new manuscript text is checked against Works Cited
- **THEN** every such work has an entry
- **AND** every new entry is cited somewhere in the text
