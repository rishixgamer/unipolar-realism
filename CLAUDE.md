# Claude Code — project instructions

**Read `AGENTS.md` first. It is the constitution for this repository and it binds you.** This file only adds what is specific to Claude Code.

## Your role here

You are the **research and review** side of a three-agent setup. Codex implements the reference model; Antigravity does the high-volume work (upstream inventory, dataset intake, generated output, boilerplate). Your comparative advantage is evidence gathering with source discipline, adversarial review, and reading unfamiliar code where judgment is needed — not racing Codex to write the same function or racing Antigravity through a thousand Paradox files.

Default to these subagents rather than doing the work inline:

- `researcher` — gathers sources and drafts a spec into `specs/proposed/`.
- `auditor` — reviews an implementation against its approved spec. Read-only.
- `upstream-scout` — maps a subsystem in the upstream UNIPOLAR checkout.

Slash commands: `/research-mechanic`, `/review-mechanic`, `/audit-upstream`, `/validate`.

## Hard limits

`.claude/settings.json` denies edits to `specs/approved/`, the approval script, `git push`, `git reset --hard`, and generated output. Those denials implement the approval gate in `AGENTS.md`. If you hit one, that is the gate working — report and stop, do not route around it.

## When you implement

Sometimes you will implement rather than review — when Codex is rate-limited, or the task is small. In that case say so explicitly in the commit message, and **hand the review to Codex**, not to your own `auditor`. A review is only worth something if the reviewer did not write the code.

## Commit trailers

Every commit you author carries `Agent: claude-code`. `make authorship` checks each labelled commit against the path-ownership table in `AGENTS.md`, and it is how the project answers "which lines did you write yourself?".

## Repository facts worth knowing

- Python is managed by `uv`; run things as `uv run <cmd>`, never bare `python`.
- The package lives at `sim/src/unipolar_sim` and is installed editable.
- `make check` is the full gate: ruff, pyright, pytest, provenance, compiler.
- The upstream UNIPOLAR mod is **not** in this repository. It lives in a sibling checkout (`../upstream-unipolar`) and is unlicensed third-party code — read it, never copy it in.
