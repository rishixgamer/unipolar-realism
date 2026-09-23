.PHONY: setup check lint typecheck test provenance compile audit approve authorship

setup:
	uv sync --all-extras

check: lint typecheck test provenance compile authorship

lint:
	uv run ruff check .

typecheck:
	uv run pyright sim/src

test:
	uv run pytest

provenance:
	uv run python tools/check_provenance.py

compile:
	uv run python compiler/compile.py

authorship:
	uv run python tools/check_authorship.py $(RANGE)

audit:
	@test -n "$(UPSTREAM)" || (echo "Usage: make audit UPSTREAM=../upstream-unipolar" && exit 2)
	uv run python tools/audit_upstream.py "$(UPSTREAM)"

# The human approval gate. Agents are blocked from this target.
approve:
	@test -n "$(ID)" || (echo "Usage: make approve ID=MON-001" && exit 2)
	uv run python tools/approve_spec.py "$(ID)"
