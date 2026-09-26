# Diplomacy and international order — upstream map

Upstream `bamcat/vic3-unipolar` at `9f3854f`. Paths relative to `mod/`. Facts about the mod only; see [README](README.md) for method.

## Files

| Directory | Contents |
| --- | --- |
| `common/diplomatic_actions/` | 56 files, mostly one action group each. Mod-specific ones include `99_impose_sanctions.txt`, `99_opec.txt`, `99_threaten_nuclear_hostilities.txt`, `99_diplomatic_unification.txt`, `99_humanitarian_aid.txt`, `99_support_revolution.txt`, `99_smd_new.txt` |
| `common/diplomatic_plays/` | `00_diplomatic_plays.txt`, `00_unify_china.txt` |
| `common/treaty_articles/` | 35 files, one per article (e.g. `00_alliance.txt`, `00_host_military_bases.txt`, `33_strait_access.txt`) |
| `common/subject_types/` | `00_subject_types.txt` |
| `common/power_bloc_identities/` | `00_power_bloc_identities.txt` |
| `common/war_goal_types/` | 31 files, including `00_disarm_nukes.txt` |
| `common/country_ranks/` | `00_country_ranks.txt` |
| `common/ai_strategies/` | 5 files: default, admin, diplomatic, subject-diplomatic and political strategies |

## Counts

| Definition | Count |
| --- | ---: |
| Diplomatic actions (all column-0 blocks) | 68 |
| Diplomatic plays (`dp_`) | 49 |
| Treaty-article files | 35 |
| Subject types | 10 |
| Power bloc identities | 7 |
| War-goal files | 31 |
| Country ranks | 8, all `REPLACE_OR_CREATE:` |
| AI strategies (`ai_strategy_`) | 35 |

## As scripted

**Sanctions** (`common/diplomatic_actions/99_impose_sanctions.txt`) are a pact with `cost = 50` (line 64) that transfers income: `income_transfer = 0.05`, capped at `max_paying_country_income_to_transfer = 0.10` (lines 72–73). They require relations at or below `poor` (line 47), and neither side may have `law_isolationism` (lines 55–56). On acceptance the sanctioner gains 15 infamy unless the target is already infamous (lines 137–140), and relations drop by 50 (line 144). AI `evaluation_chance` is 0.25 (line 160).

**Nuclear threats** (`common/diplomatic_actions/99_threaten_nuclear_hostilities.txt`) require the `nuclear_capable` variable (line 13). Acceptance sets 180-day durations (lines 65, 70) and a relations change of −20 (line 77). AI `evaluation_chance` is 0.01 (line 84).

**Nuclear disarmament war goal** (`common/war_goal_types/00_disarm_nukes.txt`) requires the claimant to be at least a major power (lines 19, 33). When enforced, the target loses 20 legitimacy (line 153) and gets a 120-month modifier (line 156); the enforcer gains 10 legitimacy (line 173) and a 60-month modifier (line 171).

**Alliances** (`common/treaty_articles/00_alliance.txt`): `cost = 150` (line 3), `relations_progress_per_day = 1.5`, `relations_improvement_max = 80`, `max_target_involvement = 3000` (lines 5–8).

**OPEC embargo vote** (`common/diplomatic_actions/99_opec.txt`) requires the actor to be in the global list `io_opec_members` (line 20).

**Power bloc identities.** `identity_trade_league` (from line 1), `identity_european_community` (163; checks the list `io_eec_members` at line 194), `identity_sovereign_empire` (326), `identity_ideological_union` (465), `identity_military_treaty_organization` (632), `identity_religious` (800), `identity_cultural` (993).

**Country ranks.** Eight ranks from `great_power` (line 16) to `decentralized_power` (248). Influence: great power 15,500 (line 41), major power 13,750 (80), minor power 8,000 (112). Aggressor infamy scaling: great power 0.20 (28), major power 0.10 (67). `unrecognized_major_power` has aggressor scaling 0.50 and target scaling −0.30 (lines 166–167).

## Where the numbers come from

No citation or external source appears in these directories. The header of `common/country_ranks/00_country_ranks.txt` explains what each field means, not where values came from.

## Dependencies

- **Out:** engine defines (`define:NDiplomacy|…`, `define:NPowerBlocs|…`), laws, interest groups, global lists such as `io_opec_members` and `io_eec_members`, and the nuclear variables listed in the [README](README.md).
- **In:** international-organisation decisions, buttons and events in [scripted content](scripted-content.md); starting relations and pacts in `common/history/diplomacy/`.

## Open questions about the mod

- Where are `io_opec_members` and `io_eec_members` filled and updated?
- Is there a multilateral sanctions mechanism, or only this bilateral pact?
- Why do `identity_trade_league` and `identity_european_community` repeat near-identical cohesion formulas?
- What effect is the asymmetric infamy scaling for unrecognized powers meant to produce?
