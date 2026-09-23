# Handoff — where the project stands

A living note for whoever picks this up next, human or agent. **Update it when you finish a session**, so the next reader starts from fact rather than from a chat log they cannot see.

Last updated: 2026-09-19

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
| Branch | `setup/dual-agent-scaffold`, 4 commits ahead of `main` |
| `main` | still the original empty commit |
| Remote | **none — nothing is on GitHub yet** |
| Upstream mod | **not cloned** — belongs at `../upstream-unipolar` |
| Commit hook | installed (`core.hooksPath = scripts/hooks`) |
| Commit email | still personal; owner may switch to a GitHub no-reply address |
| Checks | `make check` green as of the last run on macOS |
| Approved specs | none. `MON-001` is drafted in `specs/proposed/economic/` and deliberately not yet approved |
| Simulation code | two files: a debt accounting identity and a seeded RNG. Nothing else exists yet |

## Where the owner is right now

Part-way through Session 0 of `docs/workflow/` setup (the runbook lives outside the repo). Completed: repo moved out of Downloads, virtual environment rebuilt, toolchain verified, commit hook installed.

**The next action is:** decide the commit email, then push `main` and the branch to a new public GitHub repo, open a pull request, watch CI run for the first time, and merge it by hand.

After that, in order:

1. Clone the upstream mod as a **sibling** directory: `git clone https://github.com/bamcat/vic3-unipolar.git ../upstream-unipolar`. Never inside this repo — it has no licence file.
2. Run `make audit UPSTREAM=../upstream-unipolar` and commit the raw inventory before anyone interprets it.
3. The owner reads the mod himself for two to three hours. This step is not delegable.
4. Map the subsystems into `research/audits/subsystems/`, factual columns only.
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
- **`make approve` refusing is not a bug.** Placeholder sources and null parameters are what it is there to catch, and there is deliberately no override flag.
- **`brew install --cask codex` fails on this machine** with a `--cask`/`--git` conflict, some local Homebrew config. Use `npm install -g @openai/codex` instead, or the desktop app.
- **CI has never run.** Expect one or two environment surprises on the first pull request.

## What good work looks like here

A smaller repository the owner fully understands beats a large one he cannot defend. If you are about to generate a lot of code into `sim/`, you are probably the wrong agent for the task. If you are about to write a sentence about how a real institution behaves without a citation, stop and find one.
