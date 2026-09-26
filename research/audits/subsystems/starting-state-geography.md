# Starting state and geography — upstream map

What exists on the first day and where it sits on the map. Upstream `bamcat/vic3-unipolar` at `9f3854f`. Paths relative to `mod/`. Facts about the mod only; see [README](README.md) for method.

## Files

`common/history/` has 679 files in 17 subdirectories:

| Subdirectory | Files | Sets |
| --- | ---: | --- |
| `countries/` | 284 | One per country, plus `00_streamlining.txt`, which runs for every country. Sets laws, tax level, institution levels, amendments, ruling interest groups, journal entries, nuclear variables and a starting-technology bundle |
| `population/` | 270 | Per-country pop wealth and literacy (see [population](population-society.md)) |
| `characters/` | 50 | |
| `pops/` | 23 | Pop sizes by state, including `New folder/` |
| `buildings/` | 20 | 16 regional `.txt` files, 3 Python scripts (`fd_ownership.py`, `remove_barracks_from_buildings.py`, `remove_military_shipyards.py`) and `barrack_buildings_removed_log.csv` |
| `military_formations/` | 13 | |
| `diplomacy/` | 9 | Relations, customs unions, embargoes, favors, guarantees, rivalries, subjects, trade agreements, truces |
| `ai/`, `diplomatic_plays/`, `global/`, `government_setup/`, `military_deployments/`, `political_movements/`, `power_blocs/`, `states/`, `trade/`, `treaties/` | 1 each | `global/00_global.txt` line 1: `# This is executed last among all history` |

Other directories:

| Directory | Contents |
| --- | --- |
| `common/country_definitions/` | 7 files: `00_countries.txt`, `01_africa.txt`, `01_pacific_and_australasia.txt`, `99_2acw_country_definitions.txt`, `CMP_countries.txt`, `smd_countries.txt`, `zz_1992_formables_pack.txt` |
| `common/country_creation/` | `00_normal_countries.txt`, `00_releasable_countries.txt` |
| `common/country_formation/` | `00_formable_countries.txt`, `00_major_formables.txt`, `zz_1992_formables_pack.txt` |
| `map_data/` | A full map set (`default.map`, `provinces.png`, `heightmap.heightmap`, `rivers.png`, `adjacencies.csv`, `nodes.dat`, `province_terrains.txt` and heightmap images) plus 17 `state_regions/` files |

## Counts

| Definition | Count |
| --- | ---: |
| Country-tag declarations in `common/country_definitions/` | 1,567 (column-0 `TAG =`, with the `{` on the same line or the next) |
| Distinct tags | 1,349; 218 tags are declared more than once |

## As scripted

**Start date.** `START_DATE = "1992.1.1"` (`common/defines/00_time_defines.txt:2`).

**Country setup.** `common/history/countries/usa - usa.txt` sets the next election for 1993.01.20 (line 3), `nuclear_capable` (6), `nukes = 176` (7), `set_tax_level = low` (8) and New York as market capital (10), then activates laws and amendments. Starting `nukes` values elsewhere: Russia 250 (`rus - russia.txt:8`), China 30 (`prc - china.txt:5`), Britain 25 (`gbr - great britain.txt:6`).

**Technology** comes from bundles in `common/scripted_effects/00_starting_tech.txt`. `00_streamlining.txt` applies `smd_low_tech_effect` to every country (line 22), then `smd_high_tech_effect` to specific countries (lines 33–54). Russia calls `smd_medium_tech_effect` (`rus - russia.txt:5`).

**GDP and population totals.** `00_streamlining.txt` calls `fake_population_effect` (line 23) and `fake_gdp_effect` (line 24). Neither effect is defined anywhere in `mod/`. No file under `common/history/` sets a treasury, debt or GDP figure directly.

**Relations** in `common/history/diplomacy/00_relations.txt` range from −1,000 to 100.

**Country definitions** set tier, cultures and capital. For example, GBR (`common/country_definitions/00_countries.txt:14`) has `tier = empire`, cultures `british scottish` and capital `STATE_HOME_COUNTIES`. PRC is defined in `CMP_countries.txt:832`.

## Where the numbers come from

No citation or external source appears in `common/history/countries/`, `diplomacy/`, `common/country_definitions/`, `country_formation/` or `map_data/`. The only sourcing comments in `common/history/` are the 19th-century population notes and labels in `pops/New folder/`.

## Dependencies

- **Out:** laws, amendments, institutions, interest groups, journal entries and scripted effects are referenced by key; states reference `map_data` provinces.
- **In:** every other subsystem starts from this state.

## Open questions about the mod

- What did `fake_gdp_effect` and `fake_population_effect` do, and does calling an undefined effect log an error at start?
- For the 218 tags declared more than once, which definition wins, and are the duplicates deliberate overrides?
- Are the Python scripts and CSV in `common/history/buildings/` one-off tools whose output is already applied?
- Is `map_data/` a whole replacement map, or edits to the base map?
