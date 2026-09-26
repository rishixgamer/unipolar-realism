# Military — upstream map

Upstream `bamcat/vic3-unipolar` at `9f3854f`. Paths relative to `mod/`. Facts about the mod only; see [README](README.md) for method.

## Files

| Directory | Contents |
| --- | --- |
| `common/combat_unit_types/` | `00_combat_unit_types.txt` holds every unit type. `00_land_combat_unit_types.txt` and `01_navy_combat_unit_types.txt` are 4-byte files containing only `#` |
| `common/combat_unit_groups/` | `00_combat_unit_groups.txt` |
| `common/mobilization_options/`, `common/mobilization_option_groups/` | One definitions file each |
| `common/ship_types/`, `ship_groups/`, `ship_modifications/`, `ship_modification_slots/` | `00_ship_types.txt`; `00_ship_groups.txt`; `00_ship_modifications.txt` and `01_utility_modifications.txt`; `00_ship_modification_slots.txt` |
| `common/commander_orders/` | `00_advance.txt`, `00_defend.txt`, `00_interception.txt` |
| `common/battle_conditions/` | `00_aerial_conditions.txt` |

Most directories also contain a `.md` notes file.

## Counts

| Definition | Count |
| --- | ---: |
| Combat unit types | 20 |
| Ship types | 14 |
| Mobilization options | 24 |

## As scripted

**Land and air units** (`common/combat_unit_types/00_combat_unit_types.txt`). Infantry runs from `combat_unit_type_irregular_infantry` (line 10) to `combat_unit_type_mech_infantry` (359). Artillery runs from mortar (424) to `combat_unit_type_orbital_strike` (690). Aircraft run from `fixed_wing_aircraft` (731) to `autonomous_aircraft` (1006). Marines, spec ops and `space_marines` follow at lines 1047–1109.

- `combat_unit_type_foot_infantry` (line 74): 1,000 manpower and supply capacity 12 (lines 76–77); upkeep of 2 small arms, 1 ammunition and 1 radios (80–82); offense 20, defense 30 (86–87); unlocked by `gunsmithing` (91).
- `combat_unit_type_mech_infantry` (line 359): upkeep includes 10 microchips and 10 computers (lines 374–375); offense and defense 55 (379–380); unlocked by `mobile_armor` (386).
- `combat_unit_type_orbital_strike` (line 690): upkeep includes spacecraft (705); unlocked by `military_aviation` (722).

Unlocking technologies do not follow the unit order: `multirole_aircraft` is unlocked by `line_infantry` (830), `stealth_aircraft` by `modern_nursing` (900), `spec_ops` by `power_of_the_purse` (1097).

**Ships** (`common/ship_types/00_ship_types.txt`). The 14 types run from `ship_type_battleship` (line 3) to `ship_type_stealth_destroyer` (1010). Nine use `REPLACE_OR_CREATE:`; five are new: supercarrier (192), nuclear_submarine (663), littoral_combat_ship (807), helicopter_carrier (924) and stealth_destroyer (1010). Battleship hit points are 4,800 (line 13). Lines 672–688 of `ship_type_nuclear_submarine` are byte-identical to lines 605–621 of `ship_type_submarine`.

**Chemical weapons.** The mobilization option at `common/mobilization_options/00_mobilization_option.txt:781` is blocked for countries with the modifier `io_treaty_cwc_signatory` (line 785).

**Air superiority.** `common/battle_conditions/00_aerial_conditions.txt` compares `allied_air_dominance` with `ennemy_air_dominance` (spelled that way, lines 15, 57). `battle_condition_deathfromabove` (line 38) requires a drone share of at least 0.35 (line 54).

## Where the numbers come from

No citation or external source appears in these directories. `00_ship_modifications.txt` has number comments beside `construction_goods` blocks (e.g. `# 200`), which appear to be the author's cost totals.

## Dependencies

- **Out:** technologies (`unlocking_technologies`), goods (unit upkeep and ship construction), laws (conscription), international-organisation modifiers (`io_treaty_cwc_signatory`).
- **In:** the nuclear-weapons system listed in the [README](README.md) sits alongside these units; no nuclear unit type exists in this directory.

## Open questions about the mod

- Are the unlocking technologies deliberate, or placeholders?
- Is `ship_type_nuclear_submarine` meant to differ from `ship_type_submarine` only in its non-stat fields?
- Where is air dominance computed?
- How does `combat_unit_type_orbital_strike` relate to the separate nuclear system?
