#!/usr/bin/env bash
set -euo pipefail

echo "Toolchain:"
for command in git uv python3; do
  if command -v "$command" >/dev/null 2>&1; then
    echo "  OK      $command -> $(command -v "$command")"
  else
    echo "  MISSING $command"
  fi
done

echo
echo "Coding agents:"
for command in codex claude; do
  if command -v "$command" >/dev/null 2>&1; then
    echo "  OK      $command -> $(command -v "$command")"
  else
    echo "  absent  $command (fine if you only use its desktop app)"
  fi
done

echo
echo "Upstream UNIPOLAR checkout:"
UPSTREAM="${UPSTREAM:-../upstream-unipolar}"
if [[ -d "$UPSTREAM" ]]; then
  echo "  OK      $UPSTREAM ($(find "$UPSTREAM" -type f -not -path '*/.git/*' | wc -l | tr -d ' ') files)"
else
  echo "  MISSING $UPSTREAM"
  echo "          git clone https://github.com/bamcat/vic3-unipolar.git $UPSTREAM"
fi

echo
echo "Approval gate:"
echo "  proposed: $(find specs/proposed -name '*.yaml' | wc -l | tr -d ' ') spec(s)"
echo "  approved: $(find specs/approved -name '*.yaml' | wc -l | tr -d ' ') spec(s)"
