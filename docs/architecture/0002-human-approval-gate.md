# ADR 0002 — Human-only mechanic approval, enforced by the filesystem

**Status:** accepted
**Date:** 2026-09-17, revised 2026-09-18

## Decision

LLM agents may propose, research, critique and implement mechanics. They may not transition a specification to `status: approved`.

The gate is a directory boundary rather than an instruction:

- `specs/proposed/` — agents write here; `status` may be `draft` or `review`.
- `specs/approved/` — only the project owner writes here; `status` is `approved` or `implemented`.

The compiler reads `specs/approved/` only. Promotion runs through `tools/approve_spec.py` (`make approve ID=<ID>`), which re-validates the spec, refuses it while placeholder sources or null parameters remain, requires a matching `research/mechanics/<ID>.md`, prints the specification in full and demands a typed confirmation.

## Rationale

The original version of this decision stated the rule in `AGENTS.md` and relied on agents honoring it. An instruction that an agent can violate without any mechanism noticing is a convention, not a gate.

Three layers now enforce it:

1. **Permissions** — `.claude/settings.json` denies `Edit(/specs/approved/**)` and execution of the approval script.
2. **Validation** — `validate_spec` rejects a spec claiming `approved` outside the approved tree, and one sitting in the approved tree without that status.
3. **CI** — the approval and compiler gates run on every push, so a bypass fails the build rather than reaching the mod.

## Consequences

- An agent that believes a spec is ready must say so and stop. It cannot act on that belief.
- The approval commit is authored by a human and is visible in the history as a distinct, deliberate act.
- Promotion costs about a minute of reading, which is the intended price.

## Rejected alternative

Requiring cryptographically signed approval commits. Stronger, but the friction is disproportionate for a single-maintainer project, and the permission plus CI layers already defeat the realistic failure mode — an agent being helpful, not an agent being adversarial.
