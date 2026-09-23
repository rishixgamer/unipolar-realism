# Running Codex and Claude Code on this repository

Two subscriptions, two model families, one repository. The split is not about capacity — it is the adversarial review that the project's methodology depends on.

## Who does what

| Stage | Agent | Why |
| --- | --- | --- |
| Upstream mapping | Claude Code (`upstream-scout`) | Large unfamiliar codebase, read-only |
| Research and specification | Claude Code (`researcher`) | Web research with source discipline |
| **Approval** | **You, by hand** | `make approve ID=<ID>` |
| Implementation | Codex | Long autonomous coding runs inside a sandbox |
| Review | Claude Code (`auditor`) | Did not write the code |
| Merge | You | After both agents and CI are clean |

Reverse the last two when Claude Code wrote the implementation. The invariant is: **the reviewer is never the author.**

## Why not one agent

A single agent reviewing its own work reliably approves it. That is the failure mode the whole specification pipeline exists to prevent, and it is worth the small friction of switching windows.

## Codex setup

Codex reads `AGENTS.md` from the repository root automatically — no extra configuration is needed for the constitution to apply.

Recommended `~/.codex/config.toml`:

```toml
# Workspace-write lets Codex edit this repo and run tests without prompting
# on every file, while still blocking writes outside the working tree.
approval_policy = "on-request"
sandbox_mode    = "workspace-write"

[sandbox_workspace_write]
network_access = false   # flip to true only when a task genuinely needs it
```

Sandbox settings are machine-local: a project-level `.codex/config.toml` cannot set them, which is why they live in your home config. Start Codex from the repository root so it picks up `AGENTS.md`.

Codex custom prompts are user-level only (`~/.codex/prompts/`) and are on their way out in favour of skills, so this repository does not ship any. Instead, point Codex at a playbook directly:

```
Follow docs/workflow/implement-mechanic.md for MON-001.
```

That works identically in both tools and survives either vendor changing its config format.

## Claude Code setup

Nothing to install. `.claude/settings.json`, `.claude/agents/` and `.claude/commands/` are checked in and load when you start Claude Code in this directory. Run `/status` once to confirm the settings file loaded.

## Handoff protocol

Agents do not talk to each other. Git does.

1. Work happens on a branch named for the mechanic: `mechanic/MON-001`.
2. The handing-off agent commits and writes what it did in the commit body.
3. The receiving agent starts from `git log` and `git diff main...HEAD` — never from a pasted summary, which is how context gets quietly lost.
4. Review findings go in the pull request, not in a chat window. They are part of the artifact.

## Usage limits

Both plans meter usage on rolling windows and weekly caps, and both change their numbers periodically. The practical consequence: run research on one agent while the other implements, rather than serializing everything through whichever one you like best. If you hit a cap mid-mechanic, commit first — an interrupted agent with uncommitted work is how a day disappears.
