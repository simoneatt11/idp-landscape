# IDP Landscape: startups drugging intrinsically disordered proteins

This is a living, sourced map of the companies, academic groups and tools working on **intrinsically disordered proteins (IDPs)** and the biomolecular condensates they form. It covers **Europe, the USA and China**.

About 30–40% of the human proteome is disordered or contains long disordered regions. That includes many "undruggable" oncology and neurodegeneration targets: MYC, the androgen receptor N-terminal domain, p53 TAD, α-synuclein, tau and TDP-43. Over the past decade a small group of startups has tried to make these proteins druggable, and the field has now produced its first clinical results, its first failures and a new wave of AI-native companies.

**Who it is for:**

| You are… | Start with |
|---|---|
| **Following the field** | [Visual explorer](site/index.html) → [timeline](data/events.csv) |
| **An investor** | [Company table](#company-landscape) → [bottlenecks](docs/bottlenecks.md) → [market reading](docs/market-overview.md) |
| **An academic** | [Academia ↔ industry](docs/academia-industry.md) → [tools & databases](data/tools.csv) |
| **A job seeker** | [Company table](#company-landscape) (status column) → [approaches](docs/approaches.md) to see which skills each company uses |

> **Status:** first scrape, done on 2026-11-17. Every row carries a `confidence` level and source IDs. Treat `low` rows as leads to verify, not as facts. See [METHODOLOGY.md](METHODOLOGY.md).

---

## Repository map

```
data/                 ← single source of truth (edit these)
  companies.csv         companies & non-profits, one row each
  academic_groups.csv   PIs/labs and their company links
  approaches.csv        taxonomy of technical approaches
  tools.csv             databases, predictors, generative models
  events.csv            dated timeline (funding, deals, clinic, setbacks)
  sources.csv           every source, referenced by ID (S01…)
docs/
  approaches.md         the technologies, explained
  bottlenecks.md        what is blocking the field
  academia-industry.md  how labs connect to startups
  market-overview.md    regional reading: Europe / USA / China
site/
  index.html            interactive explorer (open locally or via GitHub Pages)
  data.js               generated from data/ – do not edit
scripts/build.py        validates data and regenerates site/data.js + the table below
METHODOLOGY.md          inclusion rules, confidence scale, update routine
CONTRIBUTING.md         how to add or correct an entry
```

## Company landscape

<!-- AUTO:COMPANIES START -->
_18 organisations tracked (Europe 8, USA 7, China 3) · 20 academic groups · 12 tools/databases · 67 sources · generated 2026-11-17_

| Company | Region | Approach | Stage | Lead / targets | Funding (USD) | Status | Confidence |
|---|---|---|---|---|---|---|---|
| Bind Research | Europe | AI & physics ensemble modelling | research | disordered proteins (platform) | $32.5M | active | high |
| MODAG | Europe | Aggregation / oligomer inhibition | phase-1 | anle138b (licensed to Teva) | n/d | active | medium |
| Nuage Therapeutics | Europe | Direct small-molecule binding to IDPs | preclinical | Androgen receptor (IDP TF);other IDP-driven TFs | $15.4M | active | medium |
| [Peptomyc](https://www.peptomyc.com) | Europe | Peptides; mini-proteins & designed binders | phase-2 | OMO-103 (Omomyc) | n/d | active | high |
| [Peptone](https://peptone.io) | Europe | Direct small-molecule binding to IDPs | discovery | IDP transcription factors and kinases (undisclosed) | $40M | active | high |
| [Transition Bio](https://transitionbio.com) | Europe | Condensate modulation | preclinical | YTHDC1 inhibitor | $63M | active | medium |
| Wren Therapeutics | Europe | Aggregation / oligomer inhibition | preclinical | alpha-synuclein oligomers | n/d | active | medium |
| AmbAgon Therapeutics | Europe | Molecular glues / complex stabilizers | discovery | 14-3-3 protein-protein interactions (disordered phospho-motifs) | $85M | active | low |
| Aikium | USA | Peptides; mini-proteins & designed binders | discovery | disordered regions (platform) | $2M | active | medium |
| [Dewpoint Therapeutics](https://dewpointx.com) | USA | Condensate modulation | phase-1 | DPTX3186 | $287M | active (restructured) | high |
| ESSA Pharma | USA | Direct small-molecule binding to IDPs | discontinued | masofaniten (EPI-7386) | n/d | program discontinued | high |
| Faze Medicines | USA | Condensate modulation | closed |  | $81M | closed | high |
| Nereid Therapeutics | USA | Condensate modulation | preclinical | undisclosed | $50M | active (quiet) | medium |
| Topos Bio | USA | AI & physics ensemble modelling | discovery | IDPs (undisclosed) | $10.5M | active | high |
| Kronos Bio | USA | Direct small-molecule binding to IDPs | discontinued | istisociclib (KB-0742) | n/d | wound down | medium |
| 奕拓医药 (English name TBC) | China | Condensate modulation | preclinical | undruggable oncology targets via LLPS | n/d | active | medium |
| 抟相医药 (English name TBC) | China | Condensate modulation | preclinical | undisclosed | n/d | active | medium |
| Tushen Zhihe (途深智合) | China | AI & physics ensemble modelling | discovery | GPCRs;protein disordered regions;antibodies;cyclic peptides | n/d | active | low |
<!-- AUTO:COMPANIES END -->

`n/d` means not disclosed or not yet compiled. Funding is the publicly reported total in USD millions; EUR and GBP amounts are converted approximately. The CSV has more detail: investors, partners, founders, academic origin and the latest event.

## Key takeaways (Nov 2026)

1. **There is clinical signal, but it is mixed.** The only direct-IDP small molecule to reach Phase 2, ESSA's masofaniten (AR-NTD), was stopped for futility in Oct 2024. Peptomyc's MYC mini-protein OMO-103 is in Phase 2. Dewpoint's condensate modulator DPTX3186 has an open IND and Fast Track designation (2025).
2. **Condensate companies have consolidated.** Faze closed in 2022, Dewpoint cut about 70% of its staff in 2025, and Nereid has been quiet since 2020. The survivors have narrowed their focus to one or two assets backed by pharma partnerships.
3. **AI is the new entry point.** Generative ensemble models (STARLING, Topos-1), de novo binders to disordered regions (Baker lab, 2025) and proteome-scale simulations (CALVADOS, ALBATROSS) are lowering the cost of modelling IDPs. Topos Bio ($10.5M seed, 2026) and the non-profit Bind Research (£25.8M, 2025) are built around that bet.
4. **Europe leads on academic spinouts.** Cambridge, Barcelona, Dresden and Göttingen account for most of the companies, and most of them grew out of a single lab.
5. **China is early but growing.** Phase-separation startups such as 抟相医药 (Pilong Li, Tsinghua) and 奕拓医药 (backed by Hillhouse and an AstraZeneca–CICC fund) are preclinical. Chinese AI protein-design firms are beginning to list disordered regions as targets.

## Updating

```bash
# 1. edit data/*.csv (add a source row first, then reference its ID)
# 2. validate and regenerate
python3 scripts/build.py
# 3. commit
```

CI runs `python3 scripts/build.py --check` on every push. See [CONTRIBUTING.md](CONTRIBUTING.md).

## Disclaimer

This is compiled from public sources and is not investment advice. Funding figures from data aggregators are marked as such and may be wrong. Corrections are welcome through an issue or PR.
