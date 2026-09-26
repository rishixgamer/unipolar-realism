# Core rules, modifiers and technology — upstream map

Engine defines, static modifiers, reusable scripts and the technology tree. Upstream `bamcat/vic3-unipolar` at `9f3854f`. Paths relative to `mod/`. Facts about the mod only; see [README](README.md) for method.

## Files

| Directory | Contents |
| --- | --- |
| `common/defines/` | `00_defines.txt` (engine constants), `00_time_defines.txt`, `00_ai.txt`, `00_roads.txt` |
| `common/static_modifiers/` | 22 files, including `99_central_bank.txt`, `99_imf_modifiers.txt`, `99_nuclear.txt`, `60_public_service_expenses.txt`, `99_smd_enactment.txt`, `00_code_static_modifiers.txt`, and storyline files (Arab Spring, cartels, Great Polarization, Rise of the Right, Olympics, term limits) |
| `common/modifier_type_definitions/` | 5 files plus `modifier_types.md` |
| `common/script_values/` | `gdp_value.txt`, `ideology_values.txt`, `smd_nuclear_script_values.txt`, `smd_public_service_expenses.txt`, `smd_script_values.txt`, `tgs_air_fighting_system.txt` |
| `common/scripted_effects/` | 18 files, including `00_starting_tech.txt`, `00_starting_buildings_smd.txt`, `00_starting_pop_literacy.txt`, `00_smd_nuclear_scripted_effects.txt`, `60_public_service_expenses_effects.txt` |
| `common/scripted_triggers/` | 8 files |
| `common/scripted_modifiers/` | Only `scripted_modifiers.md`; no definitions |
| `common/technology/technologies/` | `10_production.txt`, `20_military.txt`, `30_society.txt` |

## Counts

| Definition | Count |
| --- | ---: |
| Technologies | 175 (production 57, military 54, society 64), all `REPLACE_OR_CREATE:` |
| By era | era_1 39, era_2 38, era_3 41, era_4 37, era_5 20 |
| Distinct technologies granted by the starting bundles | 47, none from era_5 |

## As scripted

**Time.** `START_DATE = "1992.1.1"` (`common/defines/00_time_defines.txt:2`).

**Economic defines** in `common/defines/00_defines.txt`, with the mod's own inline comments:

| Define | Value | Line |
| --- | --- | ---: |
| `STATE_BUREAUCRACY_BASE_COST` | 10 | 174 |
| `STATE_BUREAUCRACY_POP_BASE_COST` | 4 | 175 |
| `STATE_BUREAUCRACY_POP_MULTIPLE` | 100000 | 176 |
| `DEFAULT_GOODS_TAX_COST` | 100 | 274 |
| `IN_DEFAULT_DAYS_TO_FULL_PENALTY` | 365 | 367 |
| `DECLARE_BANKRUPTCY_PENALTY_DURATION_YEARS` | 10 | 368 |
| `COUNTRY_MIN_CREDIT_SCALED` | 0.5 ("Added to the total Building Cash Reserves to determine credit limit (multiplied by GDP)") | 469 |
| `GOLD_RESERVE_LIMIT_FACTOR` | 0.2 | 527 |
| `COLLECTIVIZATION_DEBT_RATIO` | 0.5 | 677 |
| `INDIVIDUALS_TAXED_PER_TAX_CAPACITY` | 10000 | 1581 |

**IMF and war-bond modifiers** in `common/static_modifiers/99_imf_modifiers.txt` set a loan-interest multiplier of 0.50 for `imf_loan_modifier` (line 7) and 0.25 for `imf_refused_loan_modifier` (line 24). The war-bonds modifier sets a tax multiplier of 0.05 (line 48) and an interest multiplier of 0.15 (line 50).

**Central-bank policy** in `common/static_modifiers/99_central_bank.txt` is a ladder of steps. Its header (lines 1–4) states banking throughput ±5% and financial-district throughput ∓5% per step away from neutral.

**GDP values.** `common/script_values/gdp_value.txt` opens with `# faked GDP values` (line 1). `cwp_gdp` multiplies by 64 (line 4), and `cwp_market_gdp_value` multiplies by 3500 (line 16).

**Public-service expenses.** `common/modifier_type_definitions/30_public_service_expense_types.txt` defines display-only expense modifier types (header lines 2–4). The cost itself is applied through `country_expenses_add`, computed in `common/script_values/smd_public_service_expenses.txt` and applied by `common/scripted_effects/60_public_service_expenses_effects.txt`.

**Technology.** The 175 technologies use base-game keys and five eras. The era_5 set is: analytical_philosophy, antibiotics, arc_welding, behaviorism, chemical_warfare, compression_ignition, concrete_fortifications, dough_rollers, flamethrowers, flash_freezing, macroeconomics, mass_propaganda, mass_surveillance, military_aviation, mobile_armor, modern_financial_instruments, nco_training, oil_turbine, paved_roads, stormtroopers. The starting bundles in `common/scripted_effects/00_starting_tech.txt` (`smd_low_tech_effect` from line 1, then medium, high and a USA bundle) grant none of them. Two of them, `mobile_armor` and `military_aviation`, unlock the top infantry and artillery units in [military](military.md).

## Where the numbers come from

No citation or external source appears in these directories. Comments explain what a define or modifier does, not why it has its value. `gdp_value.txt` labels its own values as faked.

## Dependencies

- **Out:** defines are read by the engine; static modifiers are applied by events, journal entries, decisions and history.
- **In:** every other subsystem uses these defines, modifiers, script values and effects.

## Open questions about the mod

- What reads the `cwp_*` GDP values, and why multiply by 64 and 3,500?
- Is era_5 technology reachable in play, and what triggers its research, since no starting bundle grants it?
- Where is the central-bank policy step chosen and applied?
- Which defines differ from the base game's values? This map lists the mod's values but did not compare them with the base game.
