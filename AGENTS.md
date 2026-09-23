# UNIPOLAR Realism — repository instructions

These rules bind every agent working in this repository — Codex, Claude Code, or a human.
`CLAUDE.md` defers to this file; there is one constitution, not two.

## Mission

Build a source-backed, empirically testable political-economic simulation of the post-1992 world, within the practical limits of Victoria 3.

**Accuracy takes priority over feature count.** A small, defensible model beats a large, plausible one.

## Layers

1. `research/` + `specs/` — what the real mechanism is, and on what evidence.
2. `sim/` — the executable Python reference model. This is the source of truth for behavior.
3. `mod/` — the Victoria 3 approximation. Generated, never hand-written.
4. `validation/` — invariants, historical plausibility, counterfactual sensitivity.

Never weaken the reference model because Victoria 3 cannot express something. Document the approximation instead.

## The approval gate

This is the rule the project exists to enforce.

```
specs/proposed/   agents may write here        status: draft | review
specs/approved/   only the project owner       status: approved | implemented
```

- The compiler reads `specs/approved/` only. Nothing reaches the mod without passing the gate.
- Promotion happens through `make approve ID=<MECHANIC-ID>`, run by the project owner, interactively, after reading the specification in full.
- **No agent may run `tools/approve_spec.py`, write into `specs/approved/`, or set `status: approved`.** Claude Code enforces this through `.claude/settings.json`; Codex is expected to honor it; CI fails the build either way.
- If you believe a spec is ready, say so and stop. Do not move it.

## Source-of-truth requirements

Every substantive mechanic needs:

1. `research/mechanics/<ID>.md` — the research record;
2. primary or official-statistical sources, opened and read, not search snippets;
3. `specs/proposed/<domain>/<ID>.yaml` conforming to `compiler/schemas/mechanic.schema.json`;
4. explicit assumptions;
5. known limitations;
6. validation criteria;
7. tests appropriate to the mechanic.

Do not infer how reality works from existing UNIPOLAR code. The mod is evidence about the mod.

## Modeling discipline

Always distinguish: observed data · assumptions · endogenous variables · exogenous shocks · calibration parameters · normative judgments.

Where serious empirical or academic disagreement exists, document the competing formulations and make the assumption configurable when practical. Never encode a political or economic value judgment as an objective model fact.

## Division of labor

Two coding agents work this repository, and the split is deliberate: whichever agent writes a piece of work does not review it.

| Role | Agent | May write |
| --- | --- | --- |
| Research and specification | Claude Code (`researcher` subagent) | `research/`, `specs/proposed/` |
| Implementation | Codex | `sim/`, `compiler/`, `tests/`, `tools/`, `mod/` sources |
| Adversarial review | Claude Code (`auditor` subagent) | nothing |
| Upstream mapping | Claude Code (`upstream-scout` subagent) | nothing |
| Approval and merge | the project owner | `specs/approved/`, `main` |

When Claude Code implements something instead of Codex, Codex reviews it. The point is that the model family that produced an abstraction is never the sole judge of it.

## Generated code

Never hand-edit generated Paradox files. Change the specification or the compiler and regenerate. Generated artifacts must carry provenance metadata where the format allows, or be recorded in a generated manifest.

## Testing

For each substantive mechanic, as applicable: unit tests · accounting and state invariants · at least one pathological case · property-based tests where useful · historical plausibility validation · counterfactual sensitivity.

Calibrate on one window and evaluate on another. Reporting error on the window you fitted is not a result.

Every bug fix requires a regression test.

## Reproducibility

- Every random process takes an explicit seed.
- Every calibration dataset is recorded in `data/registry.yaml` with publisher, URL, retrieval date and licence.
- `data/raw/` is gitignored; the registry plus the transformation script is what makes a figure reproducible.
- Every chart in the documentation regenerates from a seeded scenario with one command.

## Git

Never push to `main`, force push, `git reset --hard`, or amend a commit you did not write in this session. One conceptual change per commit. Work on a branch and open a pull request even when working alone — the review history is part of the artifact.

## Required checks before claiming completion

```bash
make check
```

which runs ruff, pyright, pytest, the provenance check, and the compiler gate. If a change affects generated Paradox output, also run the mod validators for the changed files.

## Definition of "implemented"

- the specification is in `specs/approved/`;
- tests pass and invariants hold;
- assumptions, limitations and provenance are recorded;
- reference behavior is implemented in `sim/`;
- the Victoria 3 mapping is documented, including where it diverges;
- an independent review by the *other* agent found no unresolved blocker.

## Honesty rule

If the project owner cannot explain a piece of code in this repository — why that architecture, why that variable is endogenous, why that calibration method, what happens as a coefficient goes to zero — it does not belong here. Prefer a smaller repository that is fully understood.
