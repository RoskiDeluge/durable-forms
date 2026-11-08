## ADDED Requirements
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
