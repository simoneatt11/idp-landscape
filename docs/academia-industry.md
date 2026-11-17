# Academia ↔ industry

Almost every IDP company in this repo is a **single-lab spinout** or has PIs from one of about 20 labs on its scientific advisory board. The full mapping is in [`data/academic_groups.csv`](../data/academic_groups.csv), and the visual explorer draws it as a network.

## Connection patterns

| Pattern | Examples |
|---|---|
| **Founder-PI spinout** | Salvatella + Hnisz → Nuage · Soucek → Peptomyc · Brangwynne → Nereid · Hyman + Young → Dewpoint · Knowles + Weitz → Transition Bio · Pilong Li → 抟相医药 · Griesinger/Giese → MODAG |
| **SAB / scientific network** | Knowles, Vendruscolo, Linse → Wren |
| **Lab alumni founding new vehicles** | Gabi Heller (PhD with Vendruscolo, now UCL) → Bind Research |
| **Open tools that companies build on** | Holehouse lab (metapredict, ALBATROSS, STARLING), Lindorff-Larsen lab (CALVADOS), Baker lab (IDR binders), Tosatto lab (DisProt, MobiDB, PED, CAID) |
| **Non-profit / public research vehicles** | Bind Research (UK FRO, £25.8M), ARPA-H project at UC Berkeley IGI (up to $28.6M over 2 years) |
| **Investigator-initiated trials** | OMO-103 Phase 2 run by VHIO and sponsored by the Osteosarcoma Institute |

## Hubs

- **Cambridge, UK.** The Knowles and Vendruscolo labs and the Centre for Misfolding Diseases sit behind Transition Bio, Wren and indirectly Bind Research.
- **Barcelona.** IRB Barcelona and VHIO produced Nuage and Peptomyc.
- **Germany.** MPI-CBG Dresden (Dewpoint), MPI Göttingen and LMU (MODAG), MPI Molecular Genetics Berlin (Nuage).
- **Boston / Cambridge MA.** Whitehead/MIT (Dewpoint) and Harvard (Transition Bio).
- **US West Coast and Midwest.** UW IPD (designed binders), WashU (Holehouse, Pappu: sequence–ensemble theory), UC Berkeley (IGI, Bakar Labs → Aikium; Topos founders).
- **China.** Tsinghua (Pilong Li → 抟相医药). Other strong condensate and amyloid groups have not yet been mapped to companies (see TODO below).

## What academia provides that companies can't (yet)

1. **Ground truth.** NMR, SAXS and smFRET ensembles and curated disorder annotations (DisProt, PED).
2. **Open models.** STARLING, ALBATROSS and CALVADOS are free, and companies build proprietary layers on top of them.
3. **Benchmarks.** CAID is community-run. No equivalent exists yet for IDP–ligand binding.

## TODO (next scrape)

- [ ] Add Chinese condensate and amyloid labs (e.g. SUSTech/HKUST, SIOC) and check for company links
- [ ] Map EU funding (ERC, MSCA doctoral networks, EIC Pathfinder/Accelerator) to labs and companies
- [ ] Add SAB membership for Dewpoint, Peptone, Transition Bio and Topos from company websites
- [ ] Add tech-transfer offices and licence terms where public
