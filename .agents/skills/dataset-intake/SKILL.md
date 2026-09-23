---
name: dataset-intake
description: Pull a calibration dataset, record it in the registry, and write its transformation script so a figure built from it is reproducible. Use when a mechanic needs historical data.
---

# Dataset intake

Getting data into this project is mechanical work with one non-negotiable property: **someone else must be able to reproduce every number from the registry plus the script, without asking you anything.**

## Steps

1. Identify the series and its authoritative publisher — the statistical agency or central bank that produces it, not an aggregator that republishes it.

2. Add an entry to `data/registry.yaml` with, at minimum:

   ```yaml
   - id: fred-cpiaucsl
     title: Consumer Price Index for All Urban Consumers, All Items
     publisher: U.S. Bureau of Labor Statistics via FRED
     source_url: https://fred.stlouisfed.org/series/CPIAUCSL
     license_or_terms: <what the publisher's terms actually say>
     retrieval_date: <YYYY-MM-DD>
     coverage: 1947-01 to present, monthly, United States
     transformation_script: data/scripts/fred_cpiaucsl.py
     processed_path: data/processed/cpiaucsl.parquet
   ```

3. Write the transformation script under `data/scripts/`. It downloads the raw series, writes it to `data/raw/` (gitignored), and produces the processed file deterministically. Re-running it on the same inputs must produce a byte-identical output.

4. Record the vintage. Revised series change under you: note the release or vintage date, and say in the registry entry whether the model needs real-time data or is content with the latest revision.

5. Never commit `data/raw/`. The registry entry plus the script is the artifact.

## Hard limits

- Never hand-edit a processed file. If it is wrong, the script is wrong.
- Never silently fill gaps, interpolate, or splice two series into one. If a series has a break, say so in the registry entry and leave the handling to the specification.
- Units, seasonal adjustment and frequency go in the registry entry. A series whose units are not written down will eventually be used wrongly.

## Done when

`git clean -xdf && uv run python data/scripts/<script>.py` reproduces the processed file exactly, and the registry entry answers where it came from, when, under what terms, and what it measures.
