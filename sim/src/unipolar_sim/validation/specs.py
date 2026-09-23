from __future__ import annotations

import argparse
import json
from collections.abc import Iterator
from pathlib import Path
from typing import Any

import yaml
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[4]
DEFAULT_SCHEMA = ROOT / "compiler" / "schemas" / "mechanic.schema.json"
SPEC_ROOT = ROOT / "specs"
PROPOSED_ROOT = SPEC_ROOT / "proposed"
APPROVED_ROOT = SPEC_ROOT / "approved"

PLACEHOLDER_MARKERS = ("placeholder", "tbd", "to be defined", "replace-me")


def load_yaml(path: Path) -> dict[str, Any]:
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError(f"{path}: top-level YAML value must be a mapping")
    return data


def load_schema(schema_path: Path = DEFAULT_SCHEMA) -> Draft202012Validator:
    return Draft202012Validator(json.loads(schema_path.read_text(encoding="utf-8")))


def validate_spec(path: Path, schema_path: Path = DEFAULT_SCHEMA) -> list[str]:
    """Return schema errors plus the placement rules that the schema cannot express."""

    validator = load_schema(schema_path)
    data = load_yaml(path)
    errors = [e.message for e in sorted(validator.iter_errors(data), key=lambda e: list(e.path))]

    status = data.get("status")
    in_approved = APPROVED_ROOT in path.parents
    if in_approved and status not in {"approved", "implemented"}:
        errors.append(f"lives in specs/approved/ but status is {status!r}")
    if not in_approved and status in {"approved", "implemented"}:
        errors.append(f"status is {status!r} but the file is not in specs/approved/")
    if in_approved:
        errors.extend(placeholder_errors(data))
    return errors


def placeholder_errors(data: dict[str, Any]) -> list[str]:
    """An approved spec may not still carry scaffold placeholders."""

    problems: list[str] = []
    for index, source in enumerate(data.get("sources") or []):
        blob = " ".join(str(v) for v in (source or {}).values()).lower()
        if any(marker in blob for marker in PLACEHOLDER_MARKERS):
            problems.append(f"source[{index}] still reads as a placeholder")
    for key, value in (data.get("parameters") or {}).items():
        if value is None:
            problems.append(f"parameter {key!r} is still null")
    tolerance = (data.get("implementation") or {}).get("abstraction_tolerance")
    if tolerance is None or any(m in str(tolerance).lower() for m in PLACEHOLDER_MARKERS):
        problems.append("implementation.abstraction_tolerance is not defined")
    return problems


def iter_specs(root: Path = SPEC_ROOT) -> Iterator[Path]:
    yield from sorted(root.rglob("*.yaml"))


def main() -> None:
    parser = argparse.ArgumentParser(description="Validate mechanic specifications.")
    parser.add_argument("--spec-root", type=Path, default=SPEC_ROOT)
    args = parser.parse_args()

    failures = 0
    for path in iter_specs(args.spec_root):
        errors = validate_spec(path)
        rel = path.relative_to(ROOT) if ROOT in path.parents else path
        if errors:
            failures += 1
            print(f"FAIL {rel}")
            for error in errors:
                print(f"  - {error}")
        else:
            print(f"OK   {rel}")
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
