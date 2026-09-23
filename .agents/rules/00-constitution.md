# UNIPOLAR Realism — binding rules

`AGENTS.md` at the repository root is this project's constitution. **Read it before acting.** The rules below are the subset that must never be violated, restated here because they are the ones that cost the most when missed.

## 1. The approval gate

A mechanic specification in `specs/proposed/` may not be implemented. Only specifications in `specs/approved/` may reach the reference model or the mod.

- Never write into `specs/approved/`.
- Never set `status: approved` or `status: implemented`.
- Never run `tools/approve_spec.py` or `make approve`.

Only the project owner promotes a specification, by hand. If you believe one is ready, say so and stop.

## 2. Stay in your lane

You are the high-volume agent. You own bulk reading, generated output, data intake and mechanical work. You do **not** write the reference simulation or the specifications — see `.agents/rules/10-scope.md` for the exact paths.

## 3. Evidence, not intuition

Never state how a real institution works from memory, from intuition, or from reading the existing UNIPOLAR mod. The mod is evidence about the mod, not about the world. Anything describing reality needs a primary or official-statistical source, and belongs in a specification drafted by the research agent.

## 4. Generated code stays generated

Never hand-edit a generated Paradox file. Change the specification or the compiler and regenerate.

## 5. Git

Never push to `main`, force push, `git reset --hard`, or amend a commit you did not write in this session. One conceptual change per commit.

Every commit you author carries this trailer:

```
Agent: antigravity
```

`tools/check_authorship.py` uses it to verify that no agent wrote outside its lane. Omitting it is not a way around the check; it is a gap in the project's record of who wrote what, which is the thing that makes this repository defensible.

## 6. When a rule blocks you

Report it and stop. Do not route around a boundary. A blocked action here is almost always the gate working as designed.
