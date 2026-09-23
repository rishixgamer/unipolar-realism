"""Promote one mechanic specification from specs/proposed/ to specs/approved/.

This is the project's human approval gate. Coding agents are blocked from running it
(see .claude/settings.json) and from writing to specs/approved/. Run it yourself, read
the diff it prints, and commit the move under your own name.
"""

from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "sim" / "src"))

from unipolar_sim.validation.specs import (
    APPROVED_ROOT,
    PROPOSED_ROOT,
    load_yaml,
    placeholder_errors,
    validate_spec,
)

CONFIRMATION = "I have read this specification and I stand behind it"


def find_proposed(mechanic_id: str) -> Path:
    matches = [p for p in PROPOSED_ROOT.rglob("*.yaml") if p.stem == mechanic_id]
    if not matches:
        raise SystemExit(f"No proposed specification found for {mechanic_id}")
    if len(matches) > 1:
        raise SystemExit(f"Ambiguous: {[str(m) for m in matches]}")
    return matches[0]


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mechanic_id", help="e.g. MON-001")
    parser.add_argument("--yes", action="store_true", help="skip the typed confirmation")
    args = parser.parse_args()

    source = find_proposed(args.mechanic_id)
    data = load_yaml(source)

    errors = validate_spec(source)
    errors = [e for e in errors if "not in specs/approved/" not in e]
    errors.extend(placeholder_errors(data))
    if errors:
        print(f"Cannot approve {args.mechanic_id}:")
        for error in errors:
            print(f"  - {error}")
        raise SystemExit(1)

    research_note = Path("research/mechanics") / f"{args.mechanic_id}.md"
    if not research_note.exists():
        raise SystemExit(f"Missing research record: {research_note}")

    print(f"\n--- {source} ---")
    print(source.read_text(encoding="utf-8"))
    print("--- end ---\n")

    if not args.yes:
        print(f'Type exactly: "{CONFIRMATION}"')
        if input("> ").strip() != CONFIRMATION:
            raise SystemExit("Not approved.")

    destination = APPROVED_ROOT / source.relative_to(PROPOSED_ROOT)
    destination.parent.mkdir(parents=True, exist_ok=True)
    text = source.read_text(encoding="utf-8").replace("status: draft", "status: approved", 1)
    text = text.replace("status: review", "status: approved", 1)
    destination.write_text(text, encoding="utf-8")
    source.unlink()
    shutil.rmtree(source.parent) if not any(source.parent.iterdir()) else None

    print(f"Approved: {destination}")
    print("Now commit this move yourself:")
    print(f'  git add specs && git commit -m "Approve {args.mechanic_id}"')


if __name__ == "__main__":
    main()
