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

Three coding agents work this repository. The split is deliberate and has two rules behind it.

**Rule one: the reviewer is never the author.** The model family that produced an abstraction does not get to be the sole judge of it.

**Rule two: the owner must be able to defend every line of the reference model.** So the high-volume agent never writes it.

| Work | Agent |
| --- | --- |
| Upstream mod inventory and subsystem mapping | Antigravity |
| Dataset intake, transformation scripts, registry | Antigravity |
| Generated Paradox output, templates, localization | Antigravity |
| Test boilerplate and mechanical refactors | Antigravity |
| Research and specification drafting | Claude Code (`researcher`) |
| Reference model in `sim/`, and the compiler | Codex |
| Adversarial review | Claude Code (`auditor`) for Codex and Antigravity; Codex for Claude Code |
| Realism classifications, approval, merge | the project owner |

### Path ownership

| Path | May be written by |
| --- | --- |
| `sim/src/unipolar_sim/` | Codex, the owner |
| `compiler/` (except `templates/`) | Codex, the owner |
| `specs/proposed/` | Claude Code, the owner |
| `specs/approved/` | **the owner only** |
| `research/mechanics/` | Claude Code, the owner |
| `research/audits/` | Antigravity, Claude Code, the owner |
| `data/`, `mod/`, `compiler/templates/` | Antigravity, Codex, the owner |
| `tests/` | any agent |
| `docs/architecture/` | **the owner only** |
| `AGENTS.md`, `CLAUDE.md`, `.agents/`, `.claude/` | **the owner only** |

An agent editing the file that constrains it defeats the purpose of the file.

### Commit trailers

Every commit carries a trailer naming who wrote it:

```
Agent: antigravity | codex | claude-code | human
```

`tools/check_authorship.py` checks each labelled commit against the table above and fails CI on a boundary violation.

When you direct an agent to change one of the owner-only files, that commit carries both trailers:

```
Agent: claude-code
Owner-Directed: yes
```

which lifts the owner-only restriction for that commit and lists it separately in the check output. The exemption exists so that the honest label is also the passing one — labelling such a commit `human` would corrupt the very record the trailer is for. It does not lift any other boundary: Antigravity writing `sim/` fails whether or not you directed it, because that rule is about defensibility rather than authority. It is also the project's record of who wrote what, which is what makes "which lines did you write yourself?" an answerable question.

End every commit message you write with that trailer. An agent running in a desktop app does not inherit the shell variable below, so writing the trailer yourself is the reliable route.

Install the hook that adds it when it is missing:

```bash
git config core.hooksPath scripts/hooks
export UNIPOLAR_AGENT=human   # or codex | claude-code | antigravity
```

The hook refuses a commit that has neither the trailer nor the variable, rather than defaulting to `human`. A commit labelled `human` that an agent actually wrote is worse than no label at all.

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
