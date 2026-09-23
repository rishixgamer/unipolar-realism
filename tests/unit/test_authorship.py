import pytest

from tools.check_authorship import AGENTS, OWNERSHIP, owners_of


@pytest.mark.parametrize(
    ("path", "agent", "allowed"),
    [
        ("specs/approved/economic/MON-001.yaml", "human", True),
        ("specs/approved/economic/MON-001.yaml", "claude-code", False),
        ("specs/approved/economic/MON-001.yaml", "antigravity", False),
        ("sim/src/unipolar_sim/economics/monetary.py", "codex", True),
        ("sim/src/unipolar_sim/economics/monetary.py", "antigravity", False),
        ("specs/proposed/economic/MON-001.yaml", "claude-code", True),
        ("specs/proposed/economic/MON-001.yaml", "antigravity", False),
        ("compiler/templates/laws.txt.j2", "antigravity", True),
        ("compiler/compile.py", "antigravity", False),
        ("AGENTS.md", "codex", False),
        (".agents/rules/00-constitution.md", "antigravity", False),
        ("tools/approve_spec.py", "codex", False),
        ("data/registry.yaml", "antigravity", True),
        ("data/registry.yaml", "codex", True),
        ("data/registry.yaml", "claude-code", False),
        ("mod/common/laws/realism_laws.txt", "antigravity", True),
        ("mod/common/laws/realism_laws.txt", "claude-code", False),
        ("research/audits/upstream-inventory.json", "antigravity", True),
        ("research/audits/upstream-inventory.json", "claude-code", True),
        ("research/audits/upstream-inventory.json", "codex", False),
        ("research/mechanics/MON-001.md", "codex", False),
        ("specs/proposed/economic/MON-001.yaml", "codex", False),
        ("tests/unit/test_fiscal_state.py", "antigravity", True),
    ],
)
def test_path_ownership(path, agent, allowed):
    owners = owners_of(path)
    permitted = owners is None or agent in owners
    assert permitted is allowed


def test_more_specific_prefix_wins():
    # compiler/templates/ is shared; the rest of compiler/ is not.
    assert owners_of("compiler/templates/x.j2") != owners_of("compiler/compile.py")


def test_every_owner_is_a_known_agent():
    for _prefix, allowed in OWNERSHIP:
        assert allowed <= set(AGENTS)


def test_human_may_write_everywhere():
    for _prefix, allowed in OWNERSHIP:
        assert "human" in allowed


def test_owner_directed_exemption_is_narrow():
    """Owner-Directed lifts owner-only paths, not every boundary."""
    from tools.check_authorship import owners_of

    # Owner-only: exemptible.
    assert owners_of("AGENTS.md") == frozenset({"human"})
    # Shared between specific agents: not owner-only, so never exemptible.
    assert owners_of("sim/src/unipolar_sim/core/state.py") != frozenset({"human"})
    assert owners_of("specs/proposed/economic/MON-001.yaml") != frozenset({"human"})
