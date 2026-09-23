# ADR 0004 — Antigravity as the high-volume agent, fenced out of the reference model

**Status:** accepted
**Date:** 2026-09-19

## Decision

Add **Antigravity** (Google AI Pro) as a third coding agent, owning high-volume mechanical work: upstream mod inventory, dataset intake, generated Paradox output, templates, localization, test boilerplate.

It is fenced out of `sim/src/unipolar_sim/`, `specs/`, `docs/architecture/` and the agent configuration files. Those boundaries are stated in `.agents/rules/10-scope.md`, restated in the path-ownership table in `AGENTS.md`, set as `write_file` denials in the user's Antigravity project permissions, and checked after the fact by `tools/check_authorship.py` against commit trailers.

## Rationale

Two different arguments point the same way.

**Throughput belongs somewhere.** Reading several hundred Paradox script files, pulling and transforming historical series, and generating repetitive definitions are real work that the project needs done, and they are a poor use of the agent doing research or the agent implementing the model. A third flat-rate subscription absorbs them at no marginal cost.

**But the reference model must stay defensible.** The project's value rests on the owner being able to answer, without notes, why a variable is endogenous, what happens as a coefficient approaches zero, and which lines are his. Every line the high-volume agent writes into `sim/` is a line that has to be re-learned before it can be defended. Volume and defensibility pull in opposite directions, so they are separated by path rather than by intention.

The categories Antigravity owns share a property: "an agent wrote this" is an honest and uninteresting answer, because correctness is checkable mechanically — a transformation script either reproduces its output or does not, a generated file either matches its specification or does not, an inventory either cites the file and line or does not.

## Consequences

- Three agents is more coordination overhead than one maintainer strictly needs. `docs/workflow/agent-roles.md` records the tripwire: a week with no commit touching `sim/` or `specs/` means the harness is winning, and the answer is to drop back to one agent until a mechanic is through the loop.
- Antigravity permissions cannot be version-controlled — they are per-user IDE settings — so the repository cannot guarantee the boundary at write time. It is asserted three ways instead: a committed rules file the agent reads, user-side permission denials, and a CI check on commit trailers.
- Commit trailers become load-bearing. An unlabelled commit is not a boundary violation, but it is a gap in the record of who wrote what.
- The review rule is unchanged and now rotates across three agents: Claude Code reviews Codex and Antigravity; Codex reviews Claude Code.

## Rejected alternatives

**Antigravity as the primary implementer**, given it is the fastest of the three. Rejected: it inverts the defensibility argument, putting the most-generated code in the part of the repository that most needs to be owned.

**Dropping Codex and running two agents.** Rejected: the reference model and the research would then share a provider with the reviewer, and the adversarial split — the reason for more than one agent in the first place — collapses.
