# Handoff — where the project stands

A living note for whoever picks this up next, human or agent. **Update it when you finish a session**, so the next reader starts from fact rather than from a chat log they cannot see.

Last updated: 2026-09-26

## Read these first, in order

1. `AGENTS.md` — the constitution. It binds you. Non-negotiable.
2. This file — current state and the next action.
3. `docs/workflow/00-loop.md` — the eight-step development loop.
4. `docs/workflow/agent-roles.md` — who does what, and why the split exists.

If you are Gemini or Antigravity, also read `.agents/rules/` — it is written for you specifically.

## What this project is

A research fork of UNIPOLAR, a 1992 total-conversion mod for Victoria 3. The goal is **not** a better mod. It is a source-backed, empirically testable political-economic simulation of the post-1992 world, of which the mod is the playable front end.

Four layers, deliberately separated: sourced specifications → an executable Python reference model → the Victoria 3 approximation → validation. Victoria 3 is never the source of truth for how the world works.

## The four rules that are not up for negotiation

1. **The approval gate.** `specs/proposed/` is agent-writable; `specs/approved/` is the owner's alone. The compiler reads only `approved/`. No agent sets `status: approved`, writes into `specs/approved/`, or runs `tools/approve_spec.py`. If you think a spec is ready, say so and stop.
2. **Path ownership.** The table in `AGENTS.md` says who may write where. The high-volume agent never writes `sim/`, because the owner must be able to defend the reference model line by line.
3. **The reviewer is never the author.** Whichever agent wrote the code, a different one reviews it.
4. **Evidence, not intuition.** Nothing describing the real world enters this repository without a primary or official-statistical source. The mod is evidence about the mod, never about the world.

## Repository state

| | |
| --- | --- |
| Location | `~/Projects/unipolar-realism` |
| Branch | `claude/busy-volta-c0h8gk` (2026-09-26 cloud session, PR #3): this handoff update and the subsystem maps |
| `main` | PR #4 merged (`891bd16`) |
| Remote | `origin`: `https://github.com/rishixgamer/unipolar-realism.git` |
| Upstream mod | Sibling clone at `../upstream-unipolar` (`bamcat/vic3-unipolar`). The audit ran against `9f3854f84c0cc5ea15cff126c8bb902a4cdb7285` (7,894 files) |
| Upstream audit | Raw output committed by the owner (`64f9db4`, PR #4), uninterpreted: `research/audits/upstream-inventory.json` and `research/audits/realism-gap-register.json`. Every register entry is `UNKNOWN`. 6,299 of the 7,894 files fall in the tool's `other` bucket, so its path-based subsystem heuristic is coarse |
| Commit hook | installed (`core.hooksPath = scripts/hooks`) |
| Commit email | `267394493+rishixgamer@users.noreply.github.com` |
| Checks | CI has run green; `make check` green on macOS, and green on Linux in the 2026-09-26 cloud session |
| Approved specs | none. `MON-001` is drafted in `specs/proposed/economic/` and deliberately not yet approved |
| Simulation code | two files: a debt accounting identity and a seeded RNG. Nothing else exists yet |

## Where the owner is right now

Session 0 repository setup is complete: the remote exists, PR #1 is merged, CI has run green, and the commit email uses GitHub's no-reply address.

Steps 1–4 are done: upstream is cloned, the raw audit is committed (PR #4), the owner has read the mod, and eight factual subsystem maps are in `research/audits/subsystems/` (PR #3). Start from its `README.md`, which lists findings that cut across subsystems.

**The next action is:** the owner classifies each subsystem (step 5). Agents must not.

For the audit and following work:

1. **Done.** Use the upstream mod as a **sibling** directory at `../upstream-unipolar`; a local clone is already present. Never place it inside this repo — it has no licence file.
2. **Done (`64f9db4`, PR #4).** Run `make audit UPSTREAM=../upstream-unipolar` and commit the raw inventory before anyone interprets it.
3. **Done.** The owner reads the mod himself for two to three hours. This step is not delegable.
4. **Done (PR #3).** Map the subsystems into `research/audits/subsystems/`, factual columns only.
5. The owner classifies each subsystem `KEEP`/`CALIBRATE`/`REWORK`/`REPLACE`/`REMOVE`/`UNKNOWN`. Agents must not.
6. Research `MON-001` properly, then the owner approves it with `make approve ID=MON-001`.
7. Implement it, review it with a different agent, merge.

## Commit trailers

Every commit ends with a line naming who wrote it:

```
Agent: antigravity | codex | claude-code | human
```

Write it into your own commit message — a desktop app does not inherit the shell variable the hook reads, and the hook refuses a commit that has neither rather than guessing. `make authorship` checks each labelled commit against the path-ownership table.

If the owner directed you to change an owner-only file, add `Owner-Directed: yes` as well. That lifts owner-only paths for that commit and nothing else.

## Known gotchas

- **The virtual environment is macOS-specific.** Do not let a Linux environment run `uv sync` against it; it will try to rebuild it and break it for the owner.
- **A cloud (Linux) session has its own fresh venv**, separate from the macOS one. There, run `uv sync --all-extras` before `make check`, or pytest falls through to system Python and fails on `import yaml`.
- **Claude Code cannot push from a cloud session under the current `.claude/settings.json`.** `git push` is denied, `git send-pack` and self-edits to the settings file are refused by Claude Code's auto-mode safety check, and the GitHub API tools cannot carry large files such as the 1.3 MB audit inventory. Small text changes can go through the GitHub API tools; anything large needs the owner to push, or to narrow the push rule (still denying pushes to `main` and force pushes).
- **`scripts/cloud_session_start.sh` does not exist.** It has been asked for by name; `scripts/check_environment.sh` is the closest existing script.
- **`make approve` refusing is not a bug.** Placeholder sources and null parameters are what it is there to catch, and there is deliberately no override flag.
- **`brew install --cask codex` fails on this machine** with a `--cask`/`--git` conflict, some local Homebrew config. Use `npm install -g @openai/codex` instead, or the desktop app.

## What good work looks like here

A smaller repository the owner fully understands beats a large one he cannot defend. If you are about to generate a lot of code into `sim/`, you are probably the wrong agent for the task. If you are about to write a sentence about how a real institution behaves without a citation, stop and find one.
