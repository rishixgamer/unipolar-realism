---
name: upstream-inventory
description: Map a subsystem of the upstream UNIPOLAR mod and record what it actually does. Use during the upstream audit and whenever the Realism Gap Register needs a factual row filled in.
---

# Upstream inventory

Read the upstream UNIPOLAR checkout and write down what is there. This is the bulk-reading task the project needs done well and done fast — hundreds of Paradox script files, most of them uninteresting, a few of them load-bearing.

The upstream lives in a **sibling directory** (`../upstream-unipolar` by default), outside this repository. It is unlicensed third-party code: read it, never copy it in, never modify it.

## Steps

1. Run the structural pass if it has not been run:

   ```bash
   make audit UPSTREAM=../upstream-unipolar
   ```

   This writes `research/audits/upstream-inventory.json` and a gap register seeded with `UNKNOWN`.

2. For the requested subsystem, write `research/audits/subsystems/<name>.md` containing:
   - every file that implements it, with paths relative to the upstream root;
   - the mechanics **as the scripts define them** — triggers, effects, modifiers, scopes — not as the localization text describes them;
   - every numeric constant, with the file and line it comes from;
   - what the subsystem reads from and writes to elsewhere in the mod;
   - which parts are inherited from base Victoria 3 versus written by the mod, where you can tell.

3. Fill the factual columns of the matching gap register rows: `subsystem`, `files`, `current_implementation`, `dependencies`.

## Hard limits

- Leave `classification` as `UNKNOWN` and `real_world_target` empty. Those are judgments about the real world, and they belong to the project owner working from sourced research. Filling them from intuition is the single most damaging thing that can happen to this project.
- Never infer how reality works from mod code. If a script implements a 2% modifier, that is a fact about the script.
- Where you think the mod is wrong, write it as an open question: "the mod applies X unconditionally; does the real mechanism have a threshold?" — never as a verdict.

## Done when

Someone who has never opened the upstream can tell, from your file alone, what the subsystem does and which files to open to change it — and there is not a single claim about the real world anywhere in it.
