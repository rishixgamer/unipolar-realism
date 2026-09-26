# Upstream subsystem maps

Step 4 of the audit in `docs/workflow/handoff.md`: a factual map of how the upstream UNIPOLAR mod implements each subsystem. These files describe **the mod, not the world**. They carry no realism classification and no claim about how any real institution works; classifying each subsystem `KEEP`/`CALIBRATE`/`REWORK`/`REPLACE`/`REMOVE`/`UNKNOWN` is the owner's step 5.

| | |
| --- | --- |
| Upstream | `bamcat/vic3-unipolar` at `9f3854f84c0cc5ea15cff126c8bb902a4cdb7285`, read in place at `../upstream-unipolar` |
| Raw inventory | `research/audits/upstream-inventory.json` |
| Mapped | 2026-09-26 |
| Method | One `upstream-scout` read per subsystem, then Claude Code re-checked every count and every `file:line` citation below against the checkout. Claims that could not be re-checked were dropped |

No upstream file is copied here. Short quotations of upstream comments are included only where they are the evidence for a provenance statement.

## Paths and counts

- Every path is relative to `mod/` in the upstream checkout.
- A **count** is the number of column-0 `key = {` or `REPLACE_OR_CREATE:key = {` blocks with the stated key prefix, counted per file (a UTF-8 byte-order mark is ignored). Where no prefix is given, every column-0 block in the directory was counted, which can include helper blocks that are not definitions.
- `REPLACE_OR_CREATE:` is the mod's marker for overriding a definition of the same key in the base game; a bare key adds a new definition.

## Subsystems

| Map | Upstream directories |
| --- | --- |
| [Economy and production](economy-production.md) | `goods`, `buildings`, `building_groups`, `production_methods`, `production_method_groups`, `company_types`, `buy_packages`, `pop_needs`, `prestige_goods`, `state_traits`, `terrain_manipulators` |
| [Politics and government](politics-government.md) | `laws`, `law_groups`, `amendments`, `institutions`, `government_types`, `decrees`, `interest_groups`, `interest_group_traits`, `parties`, `political_movements`, `ideologies` |
| [Diplomacy and international order](diplomacy-international-order.md) | `diplomatic_actions`, `diplomatic_plays`, `treaty_articles`, `subject_types`, `power_bloc_identities`, `war_goal_types`, `country_ranks`, `ai_strategies` |
| [Military](military.md) | `combat_unit_types`, `combat_unit_groups`, `mobilization_options`, `mobilization_option_groups`, `ship_*`, `commander_orders`, `battle_conditions` |
| [Scripted content](scripted-content.md) | `events/`, `journal_entries`, `journal_entry_groups`, `decisions`, `scripted_buttons`, `scripted_progress_bars`, `scripted_guis`, `objectives`, `objective_subgoals`, `objective_subgoal_categories`, `on_actions` |
| [Population and society](population-society.md) | `pop_types`, `social_classes`, `cultures`, `religion`, `character_templates`, `character_traits` |
| [Starting state and geography](starting-state-geography.md) | `history/`, `country_definitions`, `country_creation`, `country_formation`, `dynamic_country_names`, `geographic_regions`, `strategic_regions`, `map_data/` |
| [Core rules, modifiers and technology](core-rules-technology.md) | `defines`, `static_modifiers`, `modifier_type_definitions`, `script_values`, `scripted_effects`, `scripted_triggers`, `scripted_modifiers`, `technology` |

## Not mapped: presentation only

These directories affect how the game looks or sounds, not what it simulates, and were not scouted. File counts:

| Directory | Files |
| --- | ---: |
| `gfx/` | 5,305 |
| `localization/` | 656 |
| `common/dna_data` | 73 |
| `music/` | 52 |
| `common/coat_of_arms` | 28 |
| `gui/` | 18 |
| `common/ship_name_definitions` | 15 |
| `sound/` | 10 |
| `fonts/` | 8 |
| `common/customizable_localization` | 6 |
| `common/flag_definitions` | 5 |
| `common/trigger_localization` | 3 |
| `common/dynamic_country_map_colors`, `common/messages`, `common/themes` | 2 each |
| `common/alert_groups`, `common/alert_types`, `common/game_concepts`, `common/named_colors` | 1 each |

`mod/classification_summary_v4.txt` is covered in the politics map.

## Findings that cut across subsystems

- **No numeric value in the mapped directories carries an external source.** The only source-like comments found are in `common/history/pops/New folder/`, and they describe 1830s population estimates (see the population map).
- **A nuclear-weapons system spans several subsystems**: `common/static_modifiers/99_nuclear.txt`, `common/scripted_effects/00_smd_nuclear_scripted_effects.txt`, `common/script_values/smd_nuclear_script_values.txt`, `common/journal_entries/99_nukes.txt`, `common/on_actions/99_nuclear_on_actions.txt`, `common/war_goal_types/00_disarm_nukes.txt`, `common/diplomatic_actions/99_threaten_nuclear_hostilities.txt`, and per-country `nukes` variables in `common/history/countries/`. No single map covers it end to end.
- **Starting GDP is not set as a number.** `common/history/countries/00_streamlining.txt:24` calls `fake_gdp_effect = yes`, but no definition of `fake_gdp_effect` exists anywhere in `mod/`.
