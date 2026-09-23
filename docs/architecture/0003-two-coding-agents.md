# ADR 0003 — Two coding agents from different model families

**Status:** accepted
**Date:** 2026-09-18

## Decision

Development uses two coding agents on existing subscriptions: **Codex** as the primary implementer and **Claude Code** for research, upstream mapping and adversarial review. Whichever agent writes a piece of work does not review it.

`AGENTS.md` is the single constitution; Codex reads it natively and `CLAUDE.md` defers to it. Shared playbooks live in `docs/workflow/` and are invoked by path in either tool, so neither vendor's prompt or skill format becomes a dependency.

## Rationale

The earlier design routed four roles through one orchestration harness against Azure-hosted frontier models. That failed on availability and cost: the primary model is behind a limited-access programme that a student subscription cannot enter, the critic model's documentation requires a subscription with a valid payment method, and the per-token pricing would have exhausted the available credit within days.

Two flat-rate subscriptions cost less and, more importantly, preserve the property the original design was reaching for: **the model family that produced an abstraction is not the sole judge of it.** A single model reviewing its own output reliably approves it, which is precisely the failure the specification pipeline exists to prevent.

## Consequences

- Handoffs go through git — branches, commits and pull requests — rather than through a chat window, so review history becomes part of the artifact.
- Losing programmatic orchestration means the owner sequences the work by hand. At one mechanic per fortnight, that cost is negligible.
- Both plans meter usage, so research and implementation run in parallel on different agents rather than serialized through one.
- Portability: the constitution and the playbooks are plain Markdown at known paths. Swapping either agent out costs one config file.
