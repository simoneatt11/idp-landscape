# Bottlenecks

The bottlenecks below are drawn from the sources in this repo and from company and investor commentary. Each one notes who is trying to solve it.

## Scientific

| Bottleneck | Why it matters | Who is working on it |
|---|---|---|
| **No stable pocket** | Docking, crystallography and fragment screening assume one structure | Ensemble-based design (Peptone, Topos), designed binders (Baker lab, Aikium) |
| **Proving target engagement** | Binding to an ensemble is weak and transient (often µM), and cellular readouts are indirect | HDX-MS (Peptone), NMR (Salvatella, Griesinger labs), condensate phenotyping (Transition Bio, DropScan) |
| **Unclear mechanism of action for condensate drugs** | Is the drug acting on the condensate or on its client protein? Reviewers and investors keep asking | Dewpoint's β-catenin IND is the first real clinical test |
| **Ground-truth data scarcity** | The PDB is biased toward folded proteins, PED holds few ensembles, and AI models are trained on simulations | Bind Research (open datasets), PED/DisProt curation, ARPA-H IGI project |
| **Self-reported AI benchmarks** | Company claims such as "beats AlphaFold" are hard to compare | CAID (disorder prediction), but there is **no community benchmark yet for ensembles or IDP–ligand binding** |
| **In-vitro to in-vivo translation** | Droplet behaviour in a test tube is not the same as behaviour in a cell | Cellular condensate assays and in-cell NMR (academic) |

## Clinical & translational

- **Few clinical datapoints, and one major failure.** Masofaniten's 2024 futility result is the main reference for direct IDP small molecules ([S27](../data/sources.csv)). OMO-103 (Phase 2) and DPTX3186 (entering Phase 1/2) are the next readouts to watch.
- **Neurodegeneration trial cost.** Aggregation programs (Wren, MODAG/Teva) need large, long trials, so they tend to be partnered early.
- **Biologics delivery.** Mini-proteins and designed binders must get into cells. OMO-103's cell penetration is unusual.

## Financial & market

- **The hype cycle has cooled.** Condensate funding peaked in 2020–2022 ([S56](../data/sources.csv)). Since then Faze closed (2022), Dewpoint cut about 70% of its staff (2025) and Nereid has disclosed no programs.
- **Platform vs asset.** Investors now want a lead asset with human-relevant biology rather than a "platform for undruggables". Peptone's Evotec deal and Dewpoint's narrowed pipeline both reflect that shift.
- **Small rounds outside the USA.** European seeds (Nuage at €12M) and Chinese Pre-A rounds (tens of millions RMB) are an order of magnitude smaller than US Series A/B rounds of 2020–22.

## Ecosystem

- **Talent.** The work needs people who combine polymer physics, NMR/HDX-MS, ML and medicinal chemistry, and those profiles mostly come from about 20 labs (see [academia-industry.md](academia-industry.md)).
- **Transparency in China.** English names, pipelines and amounts are often undisclosed, which makes tracking hard.

## Readouts to watch (signals to track)

1. DPTX3186 Phase 1/2 first patient and early data (Dewpoint)
2. OMO-103 Phase 2 osteosarcoma data (Peptomyc)
3. Start and results of the anle138b Phase 2 (Teva/MODAG)
4. First disclosed development candidates from Peptone, Nuage, Transition Bio and Topos
5. A public IDP–ligand or ensemble benchmark (a natural task for Bind Research or CAID)
6. Chinese IND filings from phase-separation companies (抟相医药)
