# Scripted content — upstream map

Journal entries, events, decisions and the hooks that fire them. Upstream `bamcat/vic3-unipolar` at `9f3854f`. Paths relative to `mod/`. Facts about the mod only; see [README](README.md) for method.

## Files

| Directory | `.txt` files | Organisation |
| --- | ---: | --- |
| `events/` | 96 | Episode files at the root (e.g. `covid_19.txt`), plus subfolders `arab_spring/`, `drugs/`, `formables/`, `israel_palestine_conflict/`, `law_enactment_smd/`, `tech_events/`, `terrorism_and_such/`, `usa/`, `yugoslavia/` |
| `common/journal_entries/` | 209 | By two-digit filename prefix: `00_` 79, `01_` 11, `02_` 16, `03_` 6, `04_` 15, `05_` 21, `06_` 17, `50_` 32, `99_` 12 |
| `common/journal_entry_groups/` | 1 | |
| `common/decisions/` | 32 | Includes `00_EU.txt`, `00_NATO.txt`, `00_olympics.txt`, `00_covid_pandemic_decisions.txt` |
| `common/scripted_buttons/` | 9 | Includes EU, UN and IMF buttons |
| `common/scripted_progress_bars/` | 16 | One set per storyline |
| `common/scripted_guis/` | 5 | Includes central bank and international organisations |
| `common/objectives/`, `objective_subgoals/`, `objective_subgoal_categories/` | 2, 3, 1 | `objective_the_west`, `objective_the_east`, `objective_rising_powers` (`common/objectives/01_player_objectives.txt:1, 22, 43`) |
| `common/on_actions/` | 14 | `00_code_on_actions.txt`, monthly, half-yearly and yearly pulse files, and storyline hook files (nuclear, Great Polarization, Rise of the Right, Afghan civil war, guerrilla war, term limits, law enactment) |

The 32 `50_` journal-entry files cover 1990s-and-later storylines, from `50_2008_financial_crisis.txt` to `50_yugoslav_wars.txt`. The `00_`–`06_` range also contains files named for 19th-century episodes, e.g. `00_italian_unification.txt`, `00_scramble_for_africa.txt`, `04_sepoy_mutiny.txt`, `05_balkan_wars.txt`, `06_the_carlist_wars.txt`.

## Counts

| Definition | Count |
| --- | ---: |
| Journal entries (`je_`) | 135 |
| Decisions (all column-0 blocks) | 30 |

## As scripted

**Hooks.** `common/on_actions/00_code_on_actions.txt` defines `on_game_started` (line 6), `on_game_started_after_lobby` (13), `on_monthly_pulse` (129) and `on_monthly_pulse_country` (480), among others. `common/on_actions/00_on_actions_monthly.txt` sets `chance_to_happen` values such as 50 (line 15).

**A worked journal entry.** `je_israel_palestine_peacetime` in `common/journal_entries/50_israel_palestine_je.txt`:

- `should_be_involved` at line 28;
- initial global variables such as `ip_peacetime_negotiations = 10` (line 42);
- a monthly update at line 101;
- an `invalid` block at 162 and a `complete` block at 198, which needs thresholds of 60 and 40 (lines 209–210).

Its progress bar in `common/scripted_progress_bars/50_israel_palestine.txt` starts at 35 on a 0–100 scale (lines 9–11).

**Fixed dates versus simulated state.** Some content keys on the calendar, e.g. `events/covid_19.txt:31` tests `game_date >= 2020.1.1`. Across `events/`, `common/journal_entries/`, `common/on_actions/` and `common/decisions/`, there are 139 `game_date` comparisons against a year: 111 compare with 1992 or later and 28 with earlier years. The earlier ones include `game_date >= 1886.6.1` (`common/on_actions/00_code_on_actions.txt:698`) and `game_date >= 1910.08.27 #historical date` (line 925), which is before the mod's 1992 start date. Other content depends only on simulated state, e.g. the journal entry above.

## Where the numbers come from

No citation or external source appears in these directories. Thresholds, probabilities and dates carry no stated origin.

## Dependencies

- **Out:** laws (the law-enactment events), public-service expenses (`common/on_actions/smd_on_actions.txt`), wars and relations, country tags (pervasive `c:TAG` scoping), international-organisation membership.
- **In:** starting journal entries are attached in `common/history/countries/` and `common/history/global/00_global.txt`.

## Open questions about the mod

- Are the 19th-century journal entries and pre-1992 date triggers reachable from a 1992 start, or dead code?
- What does the `00_`–`99_` filename prefix scheme record?
- Where did storyline thresholds and probabilities come from?
