---
description: Adversarial review of an implemented mechanic against its approved spec.
argument-hint: <MECHANIC-ID>
---

Review mechanic $1 against `specs/approved/**/$1.yaml`, its research record, the reference implementation, its tests, and any Victoria 3 mapping. Follow `docs/workflow/review-mechanic.md`.

Delegate to the `auditor` subagent. Report blockers first. Do not fix anything in this pass — a reviewer who edits stops being a reviewer.
