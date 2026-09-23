"""Check that each agent stayed inside the paths it owns.

Every commit should carry a trailer naming its author:

    Agent: antigravity | codex | claude-code | human

This reads the trailers on a commit range and compares the files each commit touched
against the path-ownership table in AGENTS.md. A labelled commit that wrote outside its
lane fails the check. An unlabelled commit is reported but does not fail unless --strict
is passed, so that history predating the convention stays usable.

An agent may write to an owner-only path when the owner directed that specific change,
by adding a second trailer:

    Agent: claude-code
    Owner-Directed: yes

Those commits are listed separately rather than hidden. The point of the trailer is an
accurate record of who typed what, so labelling such a commit "human" would be worse
than useless — the exemption exists so the honest label is also the passing one.

The check is after the fact by design: Antigravity's permissions are per-user IDE
settings and cannot be committed, so the repository cannot block the write itself.
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from dataclasses import dataclass, field

AGENTS = ("antigravity", "codex", "claude-code", "human")

# Prefix -> agents allowed to write there. First matching prefix wins, so list the
# most specific paths first. A path matching nothing is unrestricted.
OWNERSHIP: tuple[tuple[str, frozenset[str]], ...] = (
    ("specs/approved/", frozenset({"human"})),
    ("docs/architecture/", frozenset({"human"})),
    ("AGENTS.md", frozenset({"human"})),
    ("CLAUDE.md", frozenset({"human"})),
    (".agents/", frozenset({"human"})),
    (".claude/", frozenset({"human"})),
    ("specs/proposed/", frozenset({"claude-code", "human"})),
    ("research/mechanics/", frozenset({"claude-code", "human"})),
    ("sim/src/", frozenset({"codex", "human"})),
    ("compiler/templates/", frozenset({"antigravity", "codex", "human"})),
    ("compiler/", frozenset({"codex", "human"})),
    ("tools/approve_spec.py", frozenset({"human"})),
)


@dataclass
class Violation:
    commit: str
    subject: str
    agent: str
    path: str
    allowed: frozenset[str]


@dataclass
class Report:
    violations: list[Violation] = field(default_factory=list)
    unlabelled: list[tuple[str, str]] = field(default_factory=list)
    owner_directed: list[tuple[str, str, str]] = field(default_factory=list)
    checked: int = 0


def git(*args: str) -> str:
    return subprocess.run(
        ["git", *args], check=True, capture_output=True, text=True
    ).stdout.strip()


def trailers_of(commit: str) -> tuple[str | None, bool]:
    """Return (agent, owner_directed) from the commit's trailers."""

    agent: str | None = None
    owner_directed = False
    for line in git("show", "-s", "--format=%B", commit).splitlines():
        lowered = line.lower()
        if lowered.startswith("agent:"):
            value = line.split(":", 1)[1].strip().lower()
            if value in AGENTS:
                agent = value
        elif lowered.startswith("owner-directed:"):
            owner_directed = line.split(":", 1)[1].strip().lower() in {"yes", "true"}
    return agent, owner_directed


def owners_of(path: str) -> frozenset[str] | None:
    for prefix, allowed in OWNERSHIP:
        if path == prefix or path.startswith(prefix):
            return allowed
    return None


def check_range(rev_range: str) -> Report:
    report = Report()
    commits = git("rev-list", rev_range).splitlines() if rev_range else []
    for commit in commits:
        subject = git("show", "-s", "--format=%s", commit)
        agent, owner_directed = trailers_of(commit)
        if agent is None:
            report.unlabelled.append((commit[:8], subject))
            continue
        report.checked += 1
        if owner_directed and agent != "human":
            report.owner_directed.append((commit[:8], agent, subject))
        changed = git("show", "--pretty=", "--name-only", commit).splitlines()
        for path in filter(None, changed):
            allowed = owners_of(path)
            if allowed is None or agent in allowed:
                continue
            if owner_directed and allowed == frozenset({"human"}):
                continue
            report.violations.append(Violation(commit[:8], subject, agent, path, allowed))
    return report


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("range", nargs="?", default="main..HEAD")
    parser.add_argument(
        "--strict", action="store_true", help="also fail on commits with no Agent trailer"
    )
    args = parser.parse_args()

    try:
        report = check_range(args.range)
    except subprocess.CalledProcessError as error:
        print(f"git failed: {error.stderr.strip()}", file=sys.stderr)
        raise SystemExit(2) from error

    for commit, subject in report.unlabelled:
        print(f"unlabelled  {commit}  {subject}")

    for commit, agent, subject in report.owner_directed:
        print(f"owner-led   {commit}  {agent}  {subject}")

    for v in report.violations:
        owners = ", ".join(sorted(v.allowed))
        print(f"VIOLATION   {v.commit}  {v.agent} wrote {v.path} (owned by: {owners})")
        print(f"            {v.subject}")

    if report.violations:
        print(f"\n{len(report.violations)} path-ownership violation(s) in {args.range}")
        raise SystemExit(1)
    if args.strict and report.unlabelled:
        print(f"\n{len(report.unlabelled)} commit(s) without an Agent trailer")
        raise SystemExit(1)

    print(f"Authorship check passed ({report.checked} labelled commit(s) in {args.range})")


if __name__ == "__main__":
    main()
