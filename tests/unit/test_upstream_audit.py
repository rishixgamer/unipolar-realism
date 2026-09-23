from pathlib import Path

from tools.audit_upstream import audit, gap_register_seed


def test_audit_is_structural_and_does_not_invent_realism_classification(tmp_path: Path) -> None:
    target = tmp_path / "mod" / "common" / "buildings"
    target.mkdir(parents=True)
    (target / "example.txt").write_text("building = { }", encoding="utf-8")

    inventory = audit(tmp_path)
    register = gap_register_seed(inventory)

    assert inventory["file_count"] == 1
    assert register["entries"][0]["classification"] == "UNKNOWN"
