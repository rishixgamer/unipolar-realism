from pathlib import Path

import pytest
import yaml
from unipolar_sim.validation.specs import (
    APPROVED_ROOT,
    PROPOSED_ROOT,
    iter_specs,
    placeholder_errors,
    validate_spec,
)


def test_every_shipped_spec_validates():
    specs = list(iter_specs())
    assert specs, "expected at least one specification in specs/"
    for path in specs:
        assert validate_spec(path) == [], f"{path} failed validation"


def test_approved_tree_holds_only_approved_specs():
    for path in APPROVED_ROOT.rglob("*.yaml"):
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
        assert data["status"] in {"approved", "implemented"}


def test_proposed_spec_cannot_claim_approved_status(tmp_path: Path):
    source = next(PROPOSED_ROOT.rglob("*.yaml"))
    data = yaml.safe_load(source.read_text(encoding="utf-8"))
    data["status"] = "approved"
    forged = PROPOSED_ROOT / "economic" / "ZZZ-999.yaml"
    forged.write_text(yaml.safe_dump(data), encoding="utf-8")
    try:
        errors = validate_spec(forged)
        assert any("not in specs/approved/" in e for e in errors)
    finally:
        forged.unlink()


@pytest.mark.parametrize(
    "spec",
    [
        {"sources": [{"title": "Placeholder starting source"}], "parameters": {}},
        {"sources": [], "parameters": {"smoothing": None}},
    ],
)
def test_placeholders_block_approval(spec):
    assert placeholder_errors(spec)
