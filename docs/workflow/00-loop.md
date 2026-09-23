# The development loop

Every mechanic follows the same eight steps. The loop is the project; the mod is its output.

```
1. Pick one mechanic from the Realism Gap Register
2. Research it from primary sources          -> research/mechanics/<ID>.md
3. Draft the specification                   -> specs/proposed/<domain>/<ID>.yaml
4. YOU read it and approve it                -> make approve ID=<ID>
5. Implement the reference model + tests     -> sim/, tests/
6. Independent adversarial review            -> the agent that did not write it
7. Map into Victoria 3, document the gap     -> compiler/, mod/
8. make check, pull request, merge
```

Rules that make the loop worth running:

- **Never skip step 4.** An agent that can approve its own specification is an agent generating plausible-sounding economics.
- **Never let step 6 be done by the author of step 5.**
- **Never start a second mechanic before finishing the first.** The first one through the loop is not about the mechanic; it is about proving the loop works.
- **Step 7 is last, not first.** Deciding what Victoria 3 can express before deciding what is true is how a realism project turns into a modifier-tuning project.
