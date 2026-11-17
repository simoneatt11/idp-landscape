# Methodology

## Scope
- **Topic:** organisations whose main thesis is drugging, modelling or measuring **intrinsically disordered proteins/regions (IDPs/IDRs)** or **IDR-driven biomolecular condensates**.
- **Geography:** Europe, USA and China. Canadian companies with US operations (e.g. ESSA) are filed under `USA`.
- **Relevance levels**
  - `core`: IDPs or condensates are the stated thesis.
  - `adjacent`: IDP biology is part of the thesis but not all of it (e.g. 14-3-3 glues, general AI protein design that lists disordered regions).
  - `watchlist`: plausible players with nothing verified yet. These are kept out of `companies.csv` and listed here and in the docs.
- **Excluded for now:** big pharma internal programs, large neuro-aggregation companies whose work is mainly antibodies (they could be added as `adjacent`), and pure CROs.

## Confidence scale
| Level | Meaning |
|---|---|
| `high` | Core facts are confirmed by a primary source (company or institutional release, peer-reviewed paper) or by two independent news outlets |
| `medium` | Confirmed by trade press or aggregators, or sources disagree on one field (this is noted in `notes`) |
| `low` | Comes from a single aggregator or from background knowledge. Verify before citing |

Fields that could not be confirmed are left empty or marked `verify`. Values are never guessed.

## First scrape (2026-11-17)
- English web searches covering company launches, funding, clinical updates and the academic tools literature.
- Chinese-language searches (无序蛋白, 相分离, 生物分子凝聚体, together with 融资/药物) to find Chinese startups.
- Sources are logged in `data/sources.csv` and referenced by ID from every row.

## Watchlist (not yet in dataset)
XtalPi, DP Technology, Insilico (AI drug discovery with no verified IDP program) · AC Immune and ProMIS Neurosciences (misfolded/disordered neuro targets; candidates for `adjacent`) · Fluidic Analytics (Knowles spinout instrument maker; status unknown) · Fog Pharma (stapled peptides against undruggable PPIs).

## Update routine (suggested: quarterly)
1. For every `active` company, check the website news page plus one news search. Update `last_event`, `last_event_date` and `last_verified`.
2. Search for new entrants with the query set: `"intrinsically disordered" startup`, `condensate biotech launch`, `IDP seed round`, `无序蛋白 融资`, `相分离 药物 融资`.
3. Check ClinicalTrials.gov for OMO-103, DPTX3186 and anle138b/TEV-56286.
4. Run `python3 scripts/build.py` and commit with a message like `update: 2027-Q1 refresh`.
