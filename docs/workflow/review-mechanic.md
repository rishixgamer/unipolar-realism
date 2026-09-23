# Playbook: adversarially review an implemented mechanic

**Agent:** whichever one did *not* write the code. Read-only throughout. A reviewer that edits has stopped being a reviewer.

## Order of attack

1. **Spec fidelity** — does the code implement the approved specification, or something adjacent? Quote spec line and code line together.
2. **Silent assumptions** — has an economic or political assumption entered the code that is not in the spec? This is the highest-value finding and the easiest to miss.
3. **Invariants** — enforced every tick, or asserted once in a happy-path test?
4. **Calibration honesty** — fitted and evaluated on the same window? Is the reported error reproducible from a seeded run?
5. **Pathological behavior** — zero, bounds, large shock, long run, parameter approaching a limit.
6. **Victoria 3 abstraction** — is the divergence documented, or quietly smoothed over?
7. **Tests** — does every bug fix carry a regression test? Is any test asserting the implementation rather than the requirement?

## Output

Blockers first, then non-blocking suggestions, each with file and line. If nothing serious turns up, say so plainly and still name the two weakest points — a review with no findings is usually a review that did not look.

Findings go in the pull request, not a chat window. The review history is part of what makes this repository interesting to read.
