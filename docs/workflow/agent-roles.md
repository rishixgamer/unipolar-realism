# Running three coding agents on this repository

Three subscriptions, three model families, one repository: **Antigravity** (Google AI Pro) for volume, **Codex** (ChatGPT Plus) for the reference model, **Claude Code** (Claude Pro) for research and review.

This is not about capacity. It is about two properties the project's methodology depends on.

## The two rules

**The reviewer is never the author.** A model reviewing its own work reliably approves it. That is the exact failure the specification pipeline exists to prevent, and it is worth the friction of switching windows.

**The owner must be able to defend the reference model line by line.** So the high-volume agent never touches `sim/`. Everything Antigravity writes is either mechanical, generated, or factual-and-checkable — categories where "an agent wrote this" is an honest and uninteresting answer. Everything in `sim/` is a modeling decision you will be asked about.

## Who does what

| Stage | Agent | Why this one |
| --- | --- | --- |
| Upstream mod inventory, subsystem mapping | **Antigravity** | Hundreds of Paradox files, mostly uninteresting. Pure throughput, and its artifacts and walkthroughs suit a survey. |
| Dataset intake, transformation scripts, registry | **Antigravity** | Mechanical, and the correctness criterion is reproducibility rather than judgment. |
| Generated Paradox output, templates, localization | **Antigravity** | Volume work against a spec that already exists. |
| Test boilerplate, fixtures, mechanical refactors | **Antigravity** | Behavior already defined elsewhere. |
| Research and specification drafting | **Claude Code** (`researcher`) | Source discipline matters more than speed; the `researcher` subagent is built for it. |
| **Approval** | **you, by hand** | `make approve ID=<ID>` |
| Reference model in `sim/`, the compiler | **Codex** | Long autonomous runs from an approved spec, in a sandbox. One agent, deliberately, so the model stays coherent. |
| Adversarial review | **Claude Code** (`auditor`), or **Codex** when Claude Code wrote the code | Never the author. |
| Realism classifications, merge | **you** | Judgments about the world, not tasks. |

## The honest risk

Three agents is more coordination than one person needs at six to eight hours a week. The failure mode is spending the semester tuning the harness instead of building the simulation.

Two guards against it. First, the harness is done — this document and the config files are the whole of it; resist extending them. Second, if a week passes with no commit touching `sim/` or `specs/`, the harness is winning. Drop back to one agent until a mechanic is through the loop.

## Setup

### Antigravity

Reads `.agents/rules/*.md` from the repository root automatically — the constitution and the scope boundaries are already there and are version-controlled. `.agents/skills/` holds the two task packages it needs now (`upstream-inventory`, `dataset-intake`).

Its permissions are **user-level, not repo-committable**, so set these yourself under Settings → Projects for this folder:

| Action | Target | Effect |
| --- | --- | --- |
| `write_file` | `specs/approved/**` | Deny |
| `write_file` | `sim/src/**` | Deny |
| `write_file` | `specs/**` | Deny |
| `write_file` | `docs/architecture/**` | Deny |
| `write_file` | `AGENTS.md`, `CLAUDE.md`, `.agents/**`, `.claude/**` | Deny |
| `command` | `git push`, `git reset --hard` | Deny |
| `command` | `uv run pytest`, `uv run ruff`, `make check` | Allow |

Deny beats Ask beats Allow, and allowing `write_file` on a path implies read. The rules files state the same boundaries, but a rule is an instruction and a permission is a wall — set both.

### Codex

Reads `AGENTS.md` from the repository root automatically. Recommended `~/.codex/config.toml`:

```toml
approval_policy = "on-request"
sandbox_mode    = "workspace-write"

[sandbox_workspace_write]
network_access = false   # flip to true only when a task genuinely needs it
```

Sandbox settings are machine-local; a project-level `.codex/config.toml` cannot set them. Start Codex from the repository root.

Codex custom prompts are user-level only and are being deprecated in favour of skills, so this repository ships none. Point it at a playbook instead:

```
Follow docs/workflow/implement-mechanic.md for MON-001.
```

That phrasing works in all three tools and survives any vendor changing its config format.

### Claude Code

Nothing to install. `.claude/settings.json`, `.claude/agents/` and `.claude/commands/` are checked in. Run `/status` once to confirm the settings file loaded.

## Handoff protocol

Agents do not talk to each other. Git does.

1. Work happens on a branch named for the mechanic: `mechanic/MON-001`.
2. The handing-off agent commits, with an `Agent:` trailer and its reasoning in the body.
3. The receiving agent starts from `git log` and `git diff main...HEAD` — never from a pasted summary, which is how context gets quietly lost.
4. Review findings go in the pull request. They are part of the artifact.

The trailer has two routes, and the first is the reliable one:

1. **The agent writes it** as the last line of its own commit message. Works everywhere, including desktop apps, which do not inherit your shell environment.
2. **The hook adds it** from a shell variable, for commits you make yourself in a terminal:

   ```bash
   git config core.hooksPath scripts/hooks
   export UNIPOLAR_AGENT=human   # or codex, claude-code, antigravity
   ```

The hook refuses a commit with neither, instead of defaulting to `human`. Silently attributing an agent's work to yourself is the one failure this record cannot survive, and it fails in the flattering direction, which is exactly why it needs to be loud.

`make authorship` then checks every labelled commit on the branch against the path-ownership table in `AGENTS.md`.

## Usage limits

All three plans meter on rolling windows, and all three change their numbers periodically. The practical consequence: run research on one agent while another implements, rather than serializing through whichever one you like best. If you hit a cap mid-mechanic, commit first — an interrupted agent with uncommitted work is how a day disappears.
