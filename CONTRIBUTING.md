# Contributing

Corrections and additions are welcome. Every claim must have a source.

## Add or correct a company
1. Add the source to `data/sources.csv` with the next free ID (`S68`, …).
2. Add or edit the row in `data/companies.csv`:
   - `id`: lowercase slug, unique
   - `region`: `Europe` | `USA` | `China`
   - `relevance`: `core` | `adjacent` | `watchlist`
   - `approach` / `approach_secondary`: IDs from `data/approaches.csv` (separate several with `;`)
   - `stage`: `research` `discovery` `preclinical` `phase-1` `phase-2` `phase-3` `approved` `discontinued` `closed`
   - `funding_total_usd_m`: number only, or empty
   - `confidence`: `high` | `medium` | `low` (see METHODOLOGY.md)
   - `sources`: source IDs separated by `;`
   - `last_verified`: today's date
3. If there is a dated milestone, add it to `data/events.csv`.
4. Run `python3 scripts/build.py`. It validates everything and regenerates `site/data.js` and the README table.
5. Open a PR, or commit directly if you are a maintainer.

## Style
- Separate lists inside a cell with `;`.
- Use `verify` in a text field when something is plausible but unconfirmed.
- No promotional language. Describe what the company does, not its marketing claims, and label company-reported benchmarks as such.
