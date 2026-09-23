# Playbook: implement an approved mechanic

**Agent:** Codex (primary). **Precondition:** the specification is in `specs/approved/`. If it is not, stop — you are not permitted to move it.

## Steps

1. Read `specs/approved/<domain>/<ID>.yaml` and `research/mechanics/<ID>.md` in full. Derive the acceptance tests from the spec before writing any implementation.

2. Branch: `git switch -c mechanic/<ID>`.

3. Implement the reference model in `sim/src/unipolar_sim/<domain>/`. Pure functions over explicit state where possible; every random draw takes a seed.

4. Write tests in this order, and watch each fail before it passes:
   - **invariants** — accounting identities that must hold at every tick;
   - **a pathological case** — zero, bounds, a large shock, a long run;
   - **a counterfactual direction test** — the sign and rough magnitude the spec predicts;
   - **unit tests** for the arithmetic.

5. Data, if the mechanic needs it: record the dataset in `data/registry.yaml` (publisher, URL, retrieval date, licence) and write the transformation script. `data/raw/` is gitignored — the registry and the script are what make it reproducible.

6. Calibrate on one window, evaluate on another. Report RMSE and directional accuracy on the **holdout**. Never report error on the fitting window as a result.

7. Run `make check`. Fix what it reports. Do not weaken a test to make it pass — if a test is wrong, say why in the commit message.

8. Commit with the reasoning in the body, push the branch, open a pull request. **Do not merge.**

## Hard rules

- If an implementation decision would change the economic or political meaning of the approved spec, stop and report the ambiguity. Do not invent the rule.
- Never hand-edit generated Paradox files.
- Never set `status: approved`, never write into `specs/approved/`.
- The Victoria 3 mapping comes after the reference model is tested and reviewed, not alongside it.
