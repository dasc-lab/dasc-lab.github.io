---
abstract: This paper presents a methodology for constructing Control Barrier Functions
  (CBFs) that proactively consider the future safety of a system along a nominal trajectory,
  and effect corrective action before the trajectory leaves a designated safe set.
  Specifically, this paper presents a systematic approach for propagating a nominal
  trajectory on a receding horizon, and then encoding the future safety of this trajectory
  into a CBF. If the propagated trajectory is unsafe, then a controller satisfying
  the CBF condition will modify the nominal trajectory before the trajectory becomes
  unsafe. Compared to existing CBF techniques, this strategy is proactive rather than
  reactive and thus potentially results in smaller modifications to the nominal trajectory.
  The proposed strategy is shown to be provably safe, and then is demonstrated in
  simulated scenarios where it would otherwise be difficult to construct a traditional
  CBF. In simulation, the predictive CBF results in less modification to the nominal
  trajectory and smaller control inputs than a traditional CBF, and faster computations
  than a nonlinear model predictive control approach.
authors:
- Joseph Breeden
- dimitrapanagou
bib: "@inproceedings{DBLP:conf/cdc/BreedenP22,\n  author       = {Joseph Breeden and\n\
  \                  Dimitra Panagou},\n  title        = {Predictive Control Barrier\
  \ Functions for Online Safety Critical Control},\n  booktitle    = {61st {IEEE}\
  \ Conference on Decision and Control, {CDC} 2022, Cancun,\n                  Mexico,\
  \ December 6-9, 2022},\n  pages        = {924--931},\n  publisher    = {{IEEE}},\n\
  \  year         = {2022},\n  url          = {https://doi.org/10.1109/CDC51059.2022.9992926},\n\
  \  doi          = {10.1109/CDC51059.2022.9992926},\n  timestamp    = {Wed, 18 Jan\
  \ 2023 15:37:50 +0100},\n  biburl       = {https://dblp.org/rec/conf/cdc/BreedenP22.bib},\n\
  \  bibsource    = {dblp computer science bibliography, https://dblp.org}\n}"
date: 2022-01-01
key: conf/cdc/BreedenP22
layout: papers
link: https://doi.org/10.1109/CDC51059.2022.9992926
title: Predictive Control Barrier Functions for Online Safety Critical Control.
venue: CDC
---
