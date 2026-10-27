## ADDED Requirements
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
