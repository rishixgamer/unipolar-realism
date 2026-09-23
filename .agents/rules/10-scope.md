# Scope — what this agent may write

## Yours

| Path | Work |
| --- | --- |
| `research/audits/` | Upstream inventories, subsystem maps, the Realism Gap Register's factual columns |
| `data/` | Dataset intake: registry entries, transformation scripts, processed data |
| `mod/` | Generated Victoria 3 output, via the compiler |
| `compiler/templates/` | Paradox templates the compiler renders |
| `tools/` | Mechanical utilities — not `approve_spec.py` |
| `tests/` | Test boilerplate and fixtures for behavior already defined elsewhere |
| `docs/` | Documentation cleanup, excluding architecture decision records |

## Not yours

| Path | Owner | Why |
| --- | --- | --- |
| `sim/src/unipolar_sim/` | Codex, with the project owner | The reference model is the intellectual core of the project. It is implemented once, deliberately, by one agent working from an approved specification — and the owner must be able to defend every line of it. |
| `specs/proposed/` | Claude Code (`researcher`) | A specification is a claim about the world and needs source discipline, not throughput. |
| `specs/approved/` | the project owner only | The approval gate. |
| `docs/architecture/` | the project owner | Architecture decisions are judgments, not tasks. |
| `AGENTS.md`, `CLAUDE.md`, `.agents/`, `.claude/` | the project owner | An agent editing its own constraints defeats the point of having them. |

## The Realism Gap Register

You may fill in what a subsystem currently does — files, triggers, modifiers, values. You may **not** fill in the `classification` column (`KEEP` / `CALIBRATE` / `REWORK` / `REPLACE` / `REMOVE`) or the `real_world_target` column. Those are judgments about reality; leave them `UNKNOWN` and report what evidence would settle them.

## If a task needs you to cross a line

Say which line and why, and stop. The task is probably aimed at the wrong agent.
