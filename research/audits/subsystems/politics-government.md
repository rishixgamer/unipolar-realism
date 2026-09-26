# Politics and government — upstream map

Upstream `bamcat/vic3-unipolar` at `9f3854f`. Paths relative to `mod/`. Facts about the mod only; see [README](README.md) for method.

## Files

| Directory | Contents |
| --- | --- |
| `common/laws/` | 36 files, mostly one per law group (`00_abortion.txt` … `00_welfare.txt`, `05_central_banking.txt` … `05_media_regulations.txt`) |
| `common/law_groups/` | `00_laws.txt`, the law-group containers |
| `common/amendments/` | `smd_amendments.txt` |
| `common/institutions/` | `00_institutions.txt`; `institution_intelligence_agency` is commented out at line 72 |
| `common/government_types/` | 9 files: `00_chiefdoms` (2), `01_colonial_administrations` (10), `01_monarchies` (101), `01_regencies` (64), `02_presidential_republics` (32), `03_parliamentary_republics` (19), `04_theocracies` (20), `05_council_republics` (10), `06_corporate_states` (9) |
| `common/decrees/` | `00_decree.txt` |
| `common/interest_groups/` | 10 files; `00_servants.txt` is 4 bytes and defines nothing |
| `common/interest_group_traits/` | 8 files, one per trait set (armed forces, devout, industrialists, intelligentsia, landed interest, petty bourgeoisie, rural folk, trade unions) |
| `common/parties/` | 57 party files plus `party_ig_ideology_mapping_summary.txt` |
| `common/political_movements/` | 7 files plus `political_movements.md` |
| `common/ideologies/` | 7 files, including `io_sidebar_ideology.txt` |
| `classification_summary_v4.txt` (mod root) | See below |

## Counts

| Definition | Count |
| --- | ---: |
| Law groups (`lawgroup_`) | 32 |
| Laws (`law_`) | 152 (58 `REPLACE_OR_CREATE:`) |
| Amendments | 11 |
| Institutions | 12 active |
| Government types (`gov_`) | 267 blocks, 260 distinct keys |
| Decrees | 10 |
| Interest groups | 9, all `REPLACE_OR_CREATE:` |
| Ideologies | 123 |
| Political movements (`movement_`) | 27 |

## As scripted

**Laws.** Each law sets a `progressiveness` value, enactment triggers, a `modifier` block and a pop-support formula. Examples: `common/laws/00_governance_principles.txt:10` gives the chiefdom law `progressiveness = -100`; `:46` gives monarchy `0`.

**Government types** are chosen by a `possible` trigger per `gov_` entry, conditioned on laws and other country state (e.g. `common/government_types/02_presidential_republics.txt:11`).

**Amendments** are tied to named countries and events. The 11 keys are `medicaid` (line 13), `affordable_care_act` (54), `federal_assault_weapons_ban` (100), `authorization_military_force` (141), `patriot_act` (185), `crime_bill_1994` (233), `china_tax_reform_1994` (284), `one_child_policy` (321), `socialist_market_economy` (352), `35_hour_work_week` (389) and `pasqua_law` (435). Several are restricted with `c:USA ?= this` (e.g. lines 28, 68). Repeal requires `legitimacy >= legitimacy_to_repeal_amendment` (e.g. line 44).

**Institutions** apply modifiers directly, e.g. `state_welfare_payments_add = 0.2` at `common/institutions/00_institutions.txt:13`. Some carry comments saying the displayed modifier is informational and the real cost is applied elsewhere (lines 29–33 for schools; see the public-service expense scripts in [core rules](core-rules-technology.md)).

**`classification_summary_v4.txt`** lists the 260 distinct government-type keys under five headings with counts: theocratic 19, left-authoritarian 15, left-democratic 35, right-democratic 14, right-authoritarian 177. Every key in it exists in `common/government_types/`. No file in `mod/` refers to it, so it is not loaded by the game.

## Where the numbers come from

No citation or external source appears in these directories. Comments present explain mechanics (e.g. the institution cost notes above), not where values came from.

## Dependencies

- **Out:** ideologies and interest groups reference each other; parties reference leader ideologies and interest-group types; amendments reference country tags and parent laws; institution costs are delivered through scripts in `common/script_values/` and `common/on_actions/`.
- **In:** buildings test laws and interest groups; starting laws, amendments and institution levels are set in `common/history/countries/` (see [starting state](starting-state-geography.md)).

## Open questions about the mod

- What produced `classification_summary_v4.txt`, and what were versions 1–3?
- Why do 267 government-type blocks resolve to 260 keys — which keys are defined twice, and which definition wins?
- Is `institution_intelligence_agency` planned or abandoned?
- Is `00_servants.txt` a leftover?
