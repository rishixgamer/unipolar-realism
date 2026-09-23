# ADR 0001 — Separate research, reference simulation, and Victoria implementation

**Status:** accepted  
**Date:** 2026-09-17

## Context

Victoria 3 provides useful population, production, market, political, diplomatic, and map systems, but it cannot natively express many modern political-economic institutions with literal fidelity. Encoding "realism" directly as modifiers would make assumptions difficult to inspect, test, or reuse.

## Decision

Maintain three distinct layers:

1. research/specification;
2. executable Python reference model;
3. Victoria 3 approximation.

The reference model defines intended causal behavior. The Victoria layer documents deviations rather than redefining reality to fit the engine.

## Consequences

Positive:

- assumptions become inspectable;
- mechanics can be unit/property/scenario tested;
- calibration and counterfactual work is possible outside the game engine;
- the project remains technically meaningful even where Victoria 3 imposes hard limits.

Costs:

- duplicate representations must be kept consistent;
- a compiler/mapping layer is required;
- some mechanics may be judged "blocked" for Victoria even when the reference model supports them.
