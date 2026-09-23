from __future__ import annotations

import argparse
from pathlib import Path


def brace_balance(text: str) -> int:
    # Lightweight smoke check only. A real Clausewitz/Jomini parser should replace this later.
    return text.count("{") - text.count("}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Basic Paradox-script smoke checks.")
    parser.add_argument("root", type=Path, nargs="?", default=Path("mod"))
    args = parser.parse_args()

    failures = []
    for path in sorted(args.root.rglob("*.txt")):
        balance = brace_balance(path.read_text(encoding="utf-8-sig", errors="replace"))
        if balance:
            failures.append((path, balance))

    if failures:
        for path, balance in failures:
            print(f"{path}: brace imbalance {balance:+d}")
        raise SystemExit(1)
    print("Basic Paradox smoke checks passed")


if __name__ == "__main__":
    main()
