# Population and society — upstream map

Upstream `bamcat/vic3-unipolar` at `9f3854f`. Paths relative to `mod/`. Facts about the mod only; see [README](README.md) for method.

## Files

| Directory | Contents |
| --- | --- |
| `common/pop_types/` | 16 files, one per pop type: academics, aristocrats, bureaucrats, capitalists, clergymen, clerks, engineers, farmers, laborers, machinists, officers, peasants, professionals, shopkeepers, slaves, soldiers. Plus `pop_types.md` |
| `common/social_classes/` | `00_default.txt` (`upper_class`, `middle_class` at line 11, `lower_class` at line 27), `01_british_indian_caste_system.txt`, `readme.md` |
| `common/cultures/` | `00_cultures.txt`, `00_additional_cultures.txt`, `CMP_more_cultures.txt` |
| `common/religion/` | `cmp_religion.txt` only |
| `common/character_templates/` | 29 files, mostly one per country |
| `common/character_traits/` | 5 trait files plus `character_traits.md` |
| `common/history/pops/` | Starting pop sizes: 17 regional files (`00_west_europe.txt` … `15_russia.txt`, including both `15_new_states.txt` and `15_russia.txt`), `100_pops_example.txt`, and a subfolder `New folder/` (see below) |
| `common/history/population/` | 270 per-country files setting starting wealth and literacy through effects, e.g. `effect_starting_pop_literacy_middling` in `prc - china.txt` |

## Counts

| Definition | Count |
| --- | ---: |
| Pop types | 16 (the same 16 names as the base game) |
| Cultures | 348 (316 + 9 + 23) |
| Religions in `cmp_religion.txt` | 8, all `REPLACE_OR_CREATE:`: taoism, confucianism, wiccan, satanism, pagan, atheism, jedi, sith |
| Character traits | 120 (condition 17, personality 25, skill 53, special personality 20, special skill 5) |
| Character-template files | 29 |

## As scripted

**Pop types** set wages, quality of life, literacy and political engagement:

- `common/pop_types/laborers.txt`: `wage_weight = 9` (line 9), political engagement base 0.1 plus literacy factor 0.7.
- `common/pop_types/capitalists.txt`: `wage_weight = 40`, `literacy_target = 0.35` (lines 5–7).
- `common/pop_types/peasants.txt:10`: `consumption_mult = 0.05`.

Qualification formulas for engineers, professionals, clerks and machinists carry comments saying literacy has been redefined as college education, e.g. `common/pop_types/engineers.txt:50–52`:

> Rescaled to the mod's college-educated literacy: the old gate of 0.20 meant a developed nation at exactly 20% produced NO engineers, and manufacturing is 33% engineers.

**Two sets of starting pops.** `common/history/pops/New folder/` holds second versions of five regional files: `01_south_europe`, `02_east_europe`, `04_subsaharan_africa`, `06_central_america` and `07_south_america`. They differ from the top-level files of the same name; for example, the top-level `01_south_europe.txt` has 237 `size` lines and the `New folder/` copy has 199.

## Where the numbers come from

- Pop-type constants: no source. The comments above explain the formula, not where its numbers came from.
- Top-level starting pop sizes (`common/history/pops/*.txt`): no source comments.
- `common/history/pops/New folder/` is the only place in the mapped directories with source comments, and they describe 1830s figures. For example, line 204 of `New folder/01_south_europe.txt` mentions the census of 1833, and line 1 of `New folder/07_south_america.txt` discusses estimates of Brazil's population in the 1830s.

## Dependencies

- **Out:** social classes list allowed professions; character templates reference cultures, religions, ideologies and interest groups.
- **In:** political engagement feeds the politics subsystem; buy packages in [economy](economy-production.md) define what each wealth tier consumes.

## Open questions about the mod

- Does the game load `common/history/pops/New folder/`? If so, are those five regions' pops created twice?
- How do `common/history/pops/` (sizes by state) and `common/history/population/` (wealth and literacy by country) combine?
- Which of `15_new_states.txt` and `15_russia.txt` is current, or are both meant to load?
- Where is the base religion list that `cmp_religion.txt` extends?
