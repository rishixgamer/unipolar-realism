# Playbook: research a mechanic and draft its specification

**Agent:** Claude Code, `researcher` subagent. **Output:** two files. **Not** an implementation.

## Steps

1. State the mechanic's ID, domain and scope. IDs are `<PREFIX>-<NNN>`: `MON` monetary, `FIS` fiscal, `BNK` banking, `POL` political, `IMF`/`EU`/`UN` institutional.

2. Gather evidence from primary and official-statistical sources — central bank documentation, statistical agencies, treaty and statute text, official institutional procedure — then high-quality academic literature for the formalization and its known failures. Open every source. A search snippet is not a source.

3. Write `research/mechanics/<ID>.md` as a short paper:
   - what the institution actually does, procedurally;
   - the standard formalization(s), stated as equations;
   - where the literature disagrees, and what turns on the disagreement;
   - parameter values and ranges reported in the literature, with citations;
   - the historical period over which the description holds;
   - what Victoria 3 cannot represent faithfully.

4. Write `specs/proposed/<domain>/<ID>.yaml` against `compiler/schemas/mechanic.schema.json`, `status: draft`. Fill `observables`, `endogenous`, `exogenous`, `parameters`, `sources`, `assumptions`, `limitations`, `validation`, `implementation`.

5. Stop. Report the open questions the owner must settle: contested assumptions, parameter choices, scope boundaries, and anything the sources did not answer.

## Quality bar

- Every `sources` entry has `title`, `url`, `kind` and a `notes` line saying what it supports.
- Assumptions are labelled as assumptions, not smuggled in as facts.
- At least one documented limitation that is genuinely uncomfortable. A limitations section with nothing awkward in it has not been thought about.
- No parameter left null without the research note saying why the literature does not pin it down.

## Then: approval

You read the spec in full and run:

```bash
make approve ID=<MECHANIC-ID>
```

It re-validates, refuses on placeholders or null parameters, prints the spec, makes you type a confirmation sentence, then moves the file into `specs/approved/` and sets `status: approved`. Commit that move yourself, with a message saying why you are satisfied.
