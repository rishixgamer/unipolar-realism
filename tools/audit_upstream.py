from __future__ import annotations

import argparse
import json
from collections import Counter
from datetime import UTC, datetime
from pathlib import Path

CLASSIFICATIONS = ["KEEP", "CALIBRATE", "REWORK", "REPLACE", "REMOVE", "UNKNOWN"]


def subsystem_for(path: Path) -> str:
    parts = {p.lower() for p in path.parts}
    if "events" in parts:
        return "events"
    if "journal_entries" in parts:
        return "journal_entries"
    if "laws" in parts or "law_groups" in parts:
        return "politics_laws"
    if "buildings" in parts or "production_methods" in parts or "goods" in parts:
        return "economy_production"
    if "technology" in parts:
        return "technology"
    if "diplomatic_actions" in parts or "international_organizations" in parts:
        return "diplomacy_institutions"
    if "combat_unit_types" in parts or "mobilization_options" in parts:
        return "military"
    if "localization" in parts:
        return "localization"
    return "other"


def audit(root: Path) -> dict:
    if not root.exists() or not root.is_dir():
        raise SystemExit(f"Not a directory: {root}")

    tracked = []
    subsystem_counts: Counter[str] = Counter()
    extension_counts: Counter[str] = Counter()

    for path in sorted(root.rglob("*")):
        if not path.is_file() or ".git" in path.parts:
            continue
        rel = path.relative_to(root)
        suffix = path.suffix.lower() or "<none>"
        subsystem = subsystem_for(rel)
        subsystem_counts[subsystem] += 1
        extension_counts[suffix] += 1
        tracked.append(
            {
                "path": rel.as_posix(),
                "subsystem": subsystem,
                "extension": suffix,
                "bytes": path.stat().st_size,
            }
        )

    return {
        "source_root": str(root.resolve()),
        "generated_at_utc": datetime.now(UTC).isoformat(),
        "file_count": len(tracked),
        "subsystem_counts": dict(subsystem_counts.most_common()),
        "extension_counts": dict(extension_counts.most_common()),
        "files": tracked,
    }


def gap_register_seed(inventory: dict) -> dict:
    systems = []
    for subsystem, count in inventory["subsystem_counts"].items():
        if subsystem == "localization":
            continue
        systems.append(
            {
                "id": f"AUDIT-{len(systems) + 1:03d}",
                "subsystem": subsystem,
                "files": count,
                "classification": "UNKNOWN",
                "current_implementation": "Requires agent/human inspection",
                "real_world_target": "Requires sourced research",
                "evidence_needed": [],
                "severity": "unrated",
                "dependencies": [],
                "next_research_task": "Inspect representative files and define system boundaries",
            }
        )
    return {
        "allowed_classifications": CLASSIFICATIONS,
        "entries": systems,
        "warning": (
            "UNKNOWN is intentional. "
            "Do not assign realism classifications without evidence."
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Inventory an upstream UNIPOLAR checkout without modifying it."
    )
    parser.add_argument("upstream", type=Path)
    parser.add_argument("--output-dir", type=Path, default=Path("research/audits"))
    args = parser.parse_args()

    inventory = audit(args.upstream)
    register = gap_register_seed(inventory)

    args.output_dir.mkdir(parents=True, exist_ok=True)
    (args.output_dir / "upstream-inventory.json").write_text(
        json.dumps(inventory, indent=2) + "\n", encoding="utf-8"
    )
    (args.output_dir / "realism-gap-register.json").write_text(
        json.dumps(register, indent=2) + "\n", encoding="utf-8"
    )
    print(f"Inventoried {inventory['file_count']} files")
    print(f"Wrote {args.output_dir / 'upstream-inventory.json'}")
    print(f"Wrote {args.output_dir / 'realism-gap-register.json'}")


if __name__ == "__main__":
    main()
