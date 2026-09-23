# UNIPOLAR Realism

A research-engineering fork of **UNIPOLAR** targeting a deeper political-economic simulation of the post-1992 world.

The project separates four things that ordinary modding conflates:

1. **research and specification** — what the real-world mechanism is, and on what evidence;
2. **reference simulation** — an executable Python model of the intended causal behavior;
3. **Victoria 3 implementation** — the closest practical mapping into Paradox scripting;
4. **validation** — software invariants, historical plausibility, and counterfactual sensitivity.

Victoria 3 is the playable environment, not the source of truth for the model.

## Status

**Pre-development scaffold / v0.1 architecture.** The upstream audit and the first approved mechanic specification come before any gameplay rewrite.

## Core principles

- Accuracy over feature count.
- Every substantive mechanic carries provenance and explicit limitations.
- AI agents may research, implement and critique. They may not **approve**.
- Python is the executable reference model; Paradox script is an approximation of it.
- Generated code is never hand-edited.
- Historical fit is evidence, not proof that a model is uniquely correct.
- Competing political-economic assumptions are documented and, where practical, configurable.

## The approval gate

```
specs/proposed/   agents may write here      status: draft | review
specs/approved/   only the project owner     status: approved | implemented
```

The compiler reads `specs/approved/` only, so nothing reaches the mod without passing the gate. Promotion runs through `make approve ID=<MECHANIC-ID>`, which re-validates the spec, refuses on placeholder sources or null parameters, prints it in full, and requires a typed confirmation. Coding agents are blocked from that script and from writing into `specs/approved/`.

## Three coding agents

| Work | Agent |
| --- | --- |
| Upstream inventory, dataset intake, generated output, boilerplate | Antigravity |
| Research and specification drafting | Claude Code |
| Approval | you, by hand |
| Reference model and compiler | Codex |
| Adversarial review | the agent that did not write the code |
| Realism classifications, merge | you |

Two rules sit behind the split: **the reviewer is never the author**, and **the high-volume agent never writes `sim/`** — because the reference model is the part you have to be able to defend line by line.

Path ownership is tabulated in `AGENTS.md` and checked by `make authorship`. Setup and the handoff protocol are in `docs/workflow/agent-roles.md`.

## Repository map

```text
mod/                  Victoria 3 implementation (generated; upstream is NOT vendored here)
sim/                  executable Python reference simulation
specs/proposed/       agent-drafted mechanic specifications
specs/approved/       human-approved specifications — the only input to the compiler
research/             research records, bibliography, upstream audits
data/                 dataset registry and calibration data
compiler/             approved specs -> generated Paradox artifacts
validation/           historical, counterfactual and invariant validation
tests/                unit / property / integration / scenario / mod tests
tools/                audit, provenance and approval utilities
docs/workflow/        playbooks all three agents follow
docs/architecture/    architecture decision records
.claude/              Claude Code subagents, commands and permission rules
.agents/              Antigravity rules and skills
AGENTS.md             the constitution — binds every agent and the owner
```

## Quick start

```bash
# Toolchain (macOS)
brew install uv

# Dependencies
uv sync --all-extras

# Verify
./scripts/check_environment.sh
make check

# Label your commits by author (once per clone)
git config core.hooksPath scripts/hooks
```

Then get the upstream mod as a **sibling** directory — never inside this repository:

```bash
git clone https://github.com/bamcat/vic3-unipolar.git ../upstream-unipolar
```

## First real task

Not new mechanics. Build the Realism Gap Register:

```bash
make audit UPSTREAM=../upstream-unipolar
```

then follow `docs/workflow/audit-upstream.md` to classify each subsystem `KEEP` / `CALIBRATE` / `REWORK` / `REPLACE` / `REMOVE` / `UNKNOWN`, and pick the first vertical slice.

## Development loop

See `docs/workflow/00-loop.md`. Eight steps, one mechanic at a time, and the first mechanic through the loop is about proving the loop works rather than about the mechanic.

## Licensing / upstream notice

The upstream UNIPOLAR repository has no licence file. A public GitHub repository can be forked through GitHub's own functionality, but the absence of an explicit licence means you should **not assume** rights to redistribute a derivative standalone release. See `THIRD_PARTY.md` before publishing anything containing upstream material. Any licence chosen here covers new original code only.
