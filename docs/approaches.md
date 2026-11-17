# Approaches & technologies

IDPs have no single stable 3D structure. Each one exists as a **conformational ensemble**, a fast-changing population of shapes. Classical structure-based drug design needs a stable pocket, so it breaks down on these proteins. The companies in this repo fall into seven strategies, defined in [`data/approaches.csv`](../data/approaches.csv).

| # | Approach | Idea | Companies (examples) | Main risk |
|---|---|---|---|---|
| 1 | **Direct small-molecule binding** | Bind transient pockets or shift the ensemble toward an inactive state | Peptone, Nuage, ESSA (stopped), Topos Bio, 奕拓医药 | Weak, dynamic binding that is hard to prove in cells |
| 2 | **Condensate modulation** | Dissolve, harden or reshape the liquid-like droplets that IDRs drive (transcriptional hubs, stress granules) | Dewpoint, Transition Bio, Nereid, 抟相医药, Faze (closed) | Unclear whether a drug acts on the condensate or on its client protein |
| 3 | **Aggregation / oligomer inhibition** | Block nucleation or oligomerisation of α-synuclein, tau or Aβ | Wren, MODAG (anle138b → Teva) | Long, costly neuro trials and weak engagement biomarkers |
| 4 | **Peptides, mini-proteins, designed binders** | A biologic that wraps around the disordered segment | Peptomyc (OMO-103 vs MYC), Aikium (SeqR), Baker-lab IDR binders | Intracellular delivery and developability |
| 5 | **Molecular glues / stabilisers** | Lock a disordered motif onto its folded partner | AmbAgon (14-3-3) | Selectivity across many partners |
| 6 | **AI & physics ensemble modelling** | Predict ensembles and binding from sequence | Topos Bio, Peptone, Bind Research, 途深智合 | Little ground-truth data and self-reported benchmarks |
| 7 | **Biophysics & measurement platforms** | HDX-MS, NMR, microfluidics, smFRET, SAXS at scale | Peptone (HDX-MS), Transition Bio and Wren (microfluidics/kinetics) | Throughput and cost |

## 1. Direct small-molecule binding

- **Clinical benchmark:** masofaniten (EPI-7386, ESSA Pharma) targeted the androgen receptor N-terminal domain, which is a disordered transactivation domain. It was the first drug of its class in the clinic. In Oct 2024 the Phase 2 combination with enzalutamide was stopped for futility, and ESSA ended all masofaniten studies ([S27](../data/sources.csv), [S28](../data/sources.csv)). The drug was well tolerated, so the problem was efficacy, not safety. That keeps open the question of whether the target was engaged strongly enough.
- **New generation:** Peptone pairs HDX-MS experiments with modelling and, through its May 2025 Evotec deal, targets transcription factors and kinases. Nuage builds on the Salvatella/Hnisz finding that AR condensation creates druggable features (NSMB 2023, [S09](../data/sources.csv)).

## 2. Condensate modulation

IDRs drive liquid–liquid phase separation (LLPS). Condensates concentrate transcription factors, RNA-binding proteins and signalling complexes. The commercial thesis, launched by Dewpoint in 2018, is that changing a condensate can switch off a pathway that has no classical pocket.

- **Most advanced:** Dewpoint's **DPTX3186** is a β-catenin condensate modulator for Wnt-driven gastric cancer. It has had an open IND since Oct 2025 and Fast Track designation since Nov 2025 ([S16](../data/sources.csv), [S17](../data/sources.csv)).
- **Screening tools:** DropScan (Pilong Li, Tsinghua) is a computer-vision screen of condensate phenotypes ([S48](../data/sources.csv)). Transition Bio uses microfluidic platforms that originated in the Knowles and Weitz labs.

## 3. Aggregation and oligomer inhibition

α-synuclein, tau, Aβ and TDP-43 are all IDPs. This is the oldest commercial segment, dominated by large neuroscience companies. The startups in this repo work on the **mechanism of oligomer formation**:
- Wren uses chemical kinetics (primary and secondary nucleation) and has an Eisai collaboration.
- MODAG's anle138b, an oligomer modulator, is licensed to Teva for MSA and Parkinson's disease.

## 4. Peptides, mini-proteins and designed binders

- **OMO-103 (Peptomyc):** a cell-penetrating mini-protein that blocks MYC. It completed Phase 1 and entered Phase 2 in osteosarcoma in 2025 ([S29](../data/sources.csv)–[S31](../data/sources.csv)).
- **De novo design (2025):** the Baker lab published two methods. *logos* assembles binders from 1,000 prebuilt parts and produced tight binders for 39 of 43 targets (*Science*). An RFdiffusion approach co-samples the target and binder conformations, with K_d in the low nM range (*Nature*) ([S39](../data/sources.csv), [S40](../data/sources.csv), [S67](../data/sources.csv)). This is the clearest academic route to a new generation of IDR-binder startups.
- **Aikium:** combines SeqR scaffolds, ultra-large mRNA display and ML (Yotta-ML²).

## 5. AI & physics ensemble modelling

| Tool | Type | What it gives |
|---|---|---|
| AlphaFold pLDDT | structure predictor | Flags disordered regions; it does **not** give an ensemble |
| metapredict | predictor | Fast per-residue disorder scores |
| ALBATROSS | deep learning | Ensemble dimensions (Rg, Re, scaling exponent) from sequence |
| STARLING | latent diffusion | Full coarse-grained ensembles in seconds (*Nature* 2026) |
| CALVADOS | coarse-grained force field | Proteome-wide IDR and condensate simulations |
| Topos-1 / Topos-Bind | commercial foundation models | Ensembles and small-molecule binding (benchmarks reported by the company) |

Benchmarking: CAID round 3 (2025) found that most top predictors now use protein language models ([S43](../data/sources.csv)). The open problem is no longer predicting **whether** a region is disordered. It is predicting **which ensemble it adopts and how a ligand changes that ensemble**.
