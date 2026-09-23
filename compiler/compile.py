"""Compile approved mechanic specifications into generated artifacts.

Only specs/approved/ is read. A specification that has not passed the human approval
gate cannot reach the Victoria 3 layer, by construction rather than by convention.
"""

from __future__ import annotations

import argparse
import json
from datetime import UTC, datetime
from pathlib import Path

from unipolar_sim.validation.specs import APPROVED_ROOT, iter_specs, load_yaml, validate_spec


def build_manifest(spec_root: Path, output: Path) -> dict:
    compiled: list[dict[str, str]] = []
    rejected: list[dict[str, str]] = []

    for path in iter_specs(spec_root):
        errors = validate_spec(path)
        if errors:
            rejected.append({"path": str(path), "reason": "; ".join(errors)})
            continue
        spec = load_yaml(path)
        compiled.append(
            {
                "id": str(spec["id"]),
                "name": str(spec["name"]),
                "path": str(path),
                "victoria3_mapping": str(spec["implementation"]["victoria3_mapping"]),
            }
        )

    manifest = {
        "generated_at_utc": datetime.now(UTC).isoformat(),
        "spec_root": str(spec_root),
        "compiled": compiled,
        "rejected": rejected,
        "note": "Scaffold stage: emits a manifest only. Paradox generation is added per mechanic.",
    }
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    return manifest


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--spec-root", type=Path, default=APPROVED_ROOT)
    parser.add_argument("--output", type=Path, default=Path("generated/manifest.json"))
    args = parser.parse_args()

    manifest = build_manifest(args.spec_root, args.output)
    print(f"Compiled {len(manifest['compiled'])} approved mechanic(s)")
    if manifest["rejected"]:
        print(f"Rejected {len(manifest['rejected'])}:")
        for row in manifest["rejected"]:
            print(f"- {row['path']}: {row['reason']}")
        raise SystemExit(1)


if __name__ == "__main__":
    main()
