from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "sim" / "src"))

import yaml
from unipolar_sim.validation.specs import SPEC_ROOT, iter_specs

REQUIRED = {"title", "url", "kind"}


def main() -> None:
    failures: list[str] = []
    for path in iter_specs(SPEC_ROOT):
        data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
        mechanic_id = data.get("id", path.stem)
        sources = data.get("sources") or []
        if not sources:
            failures.append(f"{path}: no sources")
        for index, source in enumerate(sources):
            missing = REQUIRED - set(source or {})
            if missing:
                failures.append(f"{path}: source[{index}] missing {sorted(missing)}")
        note = Path("research/mechanics") / f"{mechanic_id}.md"
        if not note.exists():
            failures.append(f"{path}: missing research record {note}")

    if failures:
        print("Provenance check failed:")
        for failure in failures:
            print(f"- {failure}")
        raise SystemExit(1)
    print("Provenance check passed")


if __name__ == "__main__":
    main()
