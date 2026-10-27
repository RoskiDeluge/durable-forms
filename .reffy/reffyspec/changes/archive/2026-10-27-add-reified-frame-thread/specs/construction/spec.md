## ADDED Requirements
### Requirement: The agent is described as a late-binding interpreter
Chapter 7 §IV SHALL add a paragraph of no more than one paragraph describing the compile/interpret distinction as a question of when meaning is bound, the agent as the latest-binding interpreter yet built (fixing the meaning of a request at inference time, from the record of use), and the assembly as what binds the domain's terms before inference, so that what is bound at the moment of action is the task and not the terms. It SHALL say that a bound meaning is an artifact that can be read, diffed and rerun, where an interpretation is ephemeral. It SHALL NOT mention the Futamura projections, JIT compilation, or the amortization argument. The paragraph is optional: the author may drop it without affecting any other requirement in this change.

#### Scenario: Reader reaches "The Missing Consumer"
- **WHEN** a reader reads why an agent needs meaning present at the moment of action
- **THEN** the reason is stated in terms of binding time
- **AND** Chapter 9 §III's "record of use" is echoed, not restated

### Requirement: The loop's guarantee is stated as bounded staleness
Chapter 8 §II SHALL add, after "What Chapter 5 called latency is this loop's clock", no more than three sentences stating what the loop guarantees: not correctness but bounded staleness at the load-bearing points. The assembly SHALL be said not to promise that the map is right, but to promise that the places where the map is stood on are watched and that detected divergence reaches a revision within the loop's clock.

#### Scenario: Reader reaches "The Loop"
- **WHEN** a reader reads the five-arrow circuit
- **THEN** the circuit's guarantee is named in one place
- **AND** Chapter 10's closed-world section can refer to it as a bound that covers only what reaches a gate

### Requirement: The second tax names its strain gauges
Chapter 8 §III SHALL add, to the second tax (constraints checked in production), no more than two sentences naming the instruments at the admission boundary: rising rejections, swelling catch-all categories, and free-text fields carrying structure the schema has no column for. It SHALL present these as the telemetry mode of enforcement made concrete.

#### Scenario: Reader reaches the second tax
- **WHEN** a reader reads that constraints must run in production and not only at the gate
- **THEN** they are told what the monitors watch at the boundary where reality is admitted
- **AND** Chapter 10's residue section can refer to these instruments without redefining them
