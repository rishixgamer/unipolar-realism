# Economy and production — upstream map

Upstream `bamcat/vic3-unipolar` at `9f3854f`. Paths relative to `mod/`. Facts about the mod only; see [README](README.md) for method.

## Files

| Directory | Contents |
| --- | --- |
| `common/goods/` | `00_goods.txt`, every good. A commented-out `fresh_water` good sits at lines 807–816 |
| `common/buildings/` | 14 category files `01_industry.txt` … `15_smd_monuments.txt` (no `12_`), plus `buildings.md` (a notes file) |
| `common/building_groups/` | `00_building_groups.txt` |
| `common/production_methods/`, `common/production_method_groups/` | One file per building category, mirroring `buildings/`, plus `.md` notes files |
| `common/company_types/` | 22 files: 19 `00_companies_<region or tag>.txt` (including `_cots`, `_ip2`, `_ip3`, `_ip4`, `_mp1`, `_soi`), `99_basic_companies.txt`, `100_smd_companies.txt`, `101_smd_companies.txt`; plus `companies.md` |
| `common/buy_packages/` | `00_buy_packages.txt`, consumption baskets `wealth_1` (line 1) to `wealth_99` (line 1584) |
| `common/pop_needs/` | `00_pop_needs.txt` |
| `common/prestige_goods/` | `00_prestige_goods.txt`, `00_smd_prestige_goods.txt`, plus a `.md` notes file |
| `common/state_traits/` | `00_generic_traits.txt` and 12 regional files (`01_scandinavia_traits.txt` … `12_oceania_traits.txt`) |
| `common/terrain_manipulators/` | Only `provinces/allowed_provinces.txt` |

## Counts

| Definition | Count |
| --- | ---: |
| Goods | 73 (50 `REPLACE_OR_CREATE:`, 23 new) |
| Buildings (`building_`) | 127 |
| Building groups (`bg_`) | 72 |
| Production methods (`pm_`) | 543 |
| Production method groups (`pmg_`) | 212 |
| Company types (`company_`) | 271 |
| Pop needs (`popneed_`) | 15 |
| Buy packages (`wealth_`) | 99 |
| Prestige goods (all column-0 blocks) | 59 |

## As scripted

**Goods.** Each good sets `cost`, `category`, `prestige_factor`, `traded_quantity` and related fields. Examples: `common/goods/00_goods.txt:11` gives the first good `cost = 170`; `:568` gives gold a cost of 500. Line 586 is a comment `# NEW GOODS FROM SMD`, after which 21 goods are defined without `REPLACE_OR_CREATE:`: computers, microchips, plastic, professional_services, spacecraft, warplanes, video_games, missiles, rotorcraft, telecommunications, intellectual_property, credit, pharmaceuticals, real_estate, retail_services, food_services, advertising, securities, storage, appliances, luxury_services. `traded_quantity` lines carry a trailing number comment, e.g. `traded_quantity = 5 # 250` at `:15`.

**Local (non-traded) goods.** Nine goods set `local = yes`: the base-game overrides services, transportation and electricity, and the new goods telecommunications, real_estate, retail_services, food_services, storage and luxury_services.

**Service buildings.** `common/buildings/14_services.txt` adds `building_bank` (:50), `building_food_service` (:70), `building_retail_services` (:90), `building_advertising_agency` (:110), `building_warehouse` (:130), `building_pharmaceutical_services` (:149), `building_software_industry` (:169, unlocked by `empiricism` at :176) and `building_nuclear_silo` (:193). The silo's `potential` requires the owner to have the variable `nuclear_capable` (:213), and private construction is disabled with `can_build_private = { always = no }`.

**Consumption.** `common/buy_packages/00_buy_packages.txt` assigns each wealth tier a `political_strength` (0.03 for `wealth_1`, line 2) and a table of pop-need weights. Comments record the author's running totals, e.g. `# Sum = 164` at line 3.

**State traits.** Traits apply modifiers to states, e.g. `common/state_traits/00_generic_traits.txt:7` sets a growth-speed multiplier of −0.9.

## Where the numbers come from

No citation or external source appears in any file in these directories (case-insensitive search for `source`, `wikipedia`, `IMF`, `World Bank`, `OECD`, `citation`). The numeric comments that do appear (`# 250`, `# Sum = 164`) are the author's arithmetic.

## Dependencies

- **Out:** technologies (`unlocking_technologies`), laws and interest groups (`common/buildings/01_industry.txt`, `06_urban_center.txt` and `11_private_infrastructure.txt` test `has_law` and interest-group types), the `nuclear_capable` variable set in `common/history/countries/`.
- **In:** starting buildings in `common/history/buildings/`; military unit upkeep draws on goods such as microchips, computers and spacecraft (see [military](military.md)).

## Open questions about the mod

- What do the trailing numbers on `traded_quantity` lines mean, and does anything read them?
- What rule decides which new goods are `local = yes`?
- What do the company-file suffixes `cots`, `ip2`–`ip4`, `mp1` and `soi` refer to?
- Is the commented-out `fresh_water` good referenced anywhere while disabled?
