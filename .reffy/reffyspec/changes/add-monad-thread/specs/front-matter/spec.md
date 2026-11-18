## ADDED Requirements
### Requirement: Summaries name the monad thread consistently
The Chapter 1 summary SHALL mention Leibniz between Spinoza and Kant. The Chapter 8 summary SHALL mention the participant and the assembly as its kept harmony. The Chapter 10 summary SHALL mention the three altitudes. Each summary SHALL be identical everywhere it appears (`docs/index.md`, the part page, and the chapter's front-matter `description`).

#### Scenario: Summaries compared
- **WHEN** the copies of the Chapter 1, Chapter 8 and Chapter 10 summaries are compared
- **THEN** each copy carries the new material
- **AND** the copies of each summary match

### Requirement: Works Cited covers the monad thread
Works Cited SHALL add Leibniz's *Monadology* and Kant's *Critique of Judgment*, each in its pinned translation. Entries SHALL follow the existing alphabetical order and citation style. The 1676 visit SHALL NOT get an entry unless the text names a source for it.

#### Scenario: Citation audit
- **WHEN** each work cited in the new manuscript text is checked against Works Cited
- **THEN** every such work has an entry
- **AND** every new entry is cited somewhere in the text
