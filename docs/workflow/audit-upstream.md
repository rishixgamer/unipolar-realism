# Playbook: audit the upstream mod

**Goal:** a Realism Gap Register — one row per meaningful subsystem — that tells you what to work on and in what order. Not a change to the mod.

**Preconditions:** the upstream UNIPOLAR checkout exists as a sibling directory (`../upstream-unipolar`). It is unlicensed third-party code: read it, never copy it into this repository.

## Steps

1. Run the structural inventory:

   ```bash
   uv run python tools/audit_upstream.py ../upstream-unipolar
   ```

   This writes `research/audits/upstream-inventory.json` and a gap register seeded entirely with `UNKNOWN`. The `UNKNOWN` is deliberate — a classification without evidence is worse than no classification.

2. **Read the mod yourself first.** Two or three hours in `common/`, the economy files, the laws, the journal entries. You cannot design a realism fork of a system you have never read, and you will be asked about this.

3. For each subsystem, use the `upstream-scout` subagent to map how it is actually implemented — scripts and values, not localization text.

4. Fill in each register row: subsystem · current implementation · the real-world mechanism · evidence still needed · severity · dependencies · next research task.

5. Classify each row `KEEP` / `CALIBRATE` / `REWORK` / `REPLACE` / `REMOVE` / `UNKNOWN`. **You write the classification**, informed by the agents. A classification is a judgment about the world, which is exactly the thing agents may not make unsupervised here.

6. End with at most ten candidate mechanics for the first vertical slice, ordered by intellectual substance per unit of implementation risk.

## Done when

`research/audits/realism-gap-register.json` has no `UNKNOWN` rows in the subsystems you intend to touch first, and you can say in one sentence why the top candidate is the top candidate.
