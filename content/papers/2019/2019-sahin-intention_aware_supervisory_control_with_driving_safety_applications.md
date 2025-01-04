---
abstract: This paper proposes a guardian architecture, consisting of an estimation
  and a supervisor module providing a set of inputs that guarantees safety, in driving
  scenarios. The main idea is to offline compute a library of robust controlled invariant
  sets (RCIS), for each possible driver intention model of the other vehicles, together
  with an intention-agnostic albeit conservative RCIS. At runtime, when the intention
  estimation module determines which driver model the other vehicles are following,
  the appropriate RCIS is chosen to provide the safe and less conservative input set
  for supervision. We show that the composition of the intention estimation module
  with the proposed intention-aware supervisor module is safe. Moreover, we show how
  to compute intention-agnostic and intention-specific RCIS by growing an analytically
  found simple invariant safe set. The results are demonstrated on a case study on
  how to safely interact with a human-driven car on a highway scenario, using data
  collected from a driving simulator.
authors:
- Yunus Emre Sahin
- Zexiang Liu
- Kwesi J. Rutledge
- dimitrapanagou
- Sze Zheng Yong
- Necmiye Ozay
bib: "@inproceedings{DBLP:conf/ccta/SahinLRPYO19,\n  author       = {Yunus Emre Sahin\
  \ and\n                  Zexiang Liu and\n                  Kwesi J. Rutledge and\n\
  \                  Dimitra Panagou and\n                  Sze Zheng Yong and\n \
  \                 Necmiye Ozay},\n  title        = {Intention-Aware Supervisory\
  \ Control with Driving Safety Applications},\n  booktitle    = {2019 {IEEE} Conference\
  \ on Control Technology and Applications, {CCTA}\n                  2019, Hong Kong,\
  \ SAR, China, August 19-21, 2019},\n  pages        = {1--8},\n  publisher    = {{IEEE}},\n\
  \  year         = {2019},\n  url          = {https://doi.org/10.1109/CCTA.2019.8920426},\n\
  \  doi          = {10.1109/CCTA.2019.8920426},\n  timestamp    = {Wed, 07 Dec 2022\
  \ 23:10:43 +0100},\n  biburl       = {https://dblp.org/rec/conf/ccta/SahinLRPYO19.bib},\n\
  \  bibsource    = {dblp computer science bibliography, https://dblp.org}\n}"
date: 2019-01-01
key: conf/ccta/SahinLRPYO19
layout: papers
link: https://doi.org/10.1109/CCTA.2019.8920426
title: Intention-Aware Supervisory Control with Driving Safety Applications.
venue: CCTA
---
