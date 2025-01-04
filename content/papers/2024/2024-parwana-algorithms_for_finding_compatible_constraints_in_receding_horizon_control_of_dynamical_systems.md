---
abstract: This paper addresses synthesizing receding-horizon controllers for nonlinear,
  control-affine dynamical systems under multiple incompatible hard and soft constraints.
  Handling incompatibility of constraints has mostly been addressed in literature
  by relaxing the soft constraints via slack variables. However, this may lead to
  trajectories that are far from the optimal solution and may compromise satisfaction
  of the hard constraints over time. In that regard, permanently dropping incompatible
  soft constraints may be beneficial for the satisfaction over time of the hard constraints
  (under the assumption that hard constraints are compatible with each other at initial
  time). To this end, motivated by approximate methods on the maximal feasible subset
  (maxFS) selection problem, we propose heuristics that depend on the Lagrange multipliers
  of the constraints. The main observation for using heuristics based on the Lagrange
  multipliers instead of slack variables (which is the standard approach in the related
  literature of finding maxFS) is that when the optimization is feasible, the Lagrange
  multiplier of a given constraint is non-zero, in contrast to the slack variable
  which is zero. This observation is particularly useful in the case of a dynamical
  nonlinear system where its control input is computed recursively as the optimization
  of a cost functional subject to the system dynamics and constraints, in the sense
  that the Lagrange multipliers of the constraints over a prediction horizon can indicate
  the constraints to be dropped so that the resulting constraints are compatible.
  The method is evaluated empirically in a case study with a robot navigating under
  multiple time and state constraints, and compared to a greedy method based on the
  Lagrange multiplier.
authors:
- Hardik Parwana
- Ruiyang Wang
- dimitrapanagou
bib: "@inproceedings{DBLP:conf/amcc/ParwanaWP24,\n  author       = {Hardik Parwana\
  \ and\n                  Ruiyang Wang and\n                  Dimitra Panagou},\n\
  \  title        = {Algorithms for Finding Compatible Constraints in Receding-Horizon\n\
  \                  Control of Dynamical Systems},\n  booktitle    = {American Control\
  \ Conference, {ACC} 2024, Toronto, ON, Canada, July\n                  10-12, 2024},\n\
  \  pages        = {2074--2081},\n  publisher    = {{IEEE}},\n  year         = {2024},\n\
  \  url          = {https://doi.org/10.23919/ACC60939.2024.10644243},\n  doi    \
  \      = {10.23919/ACC60939.2024.10644243},\n  timestamp    = {Sat, 21 Sep 2024\
  \ 12:19:37 +0200},\n  biburl       = {https://dblp.org/rec/conf/amcc/ParwanaWP24.bib},\n\
  \  bibsource    = {dblp computer science bibliography, https://dblp.org}\n}"
date: 2024-01-01
key: conf/amcc/ParwanaWP24
layout: papers
link: https://doi.org/10.23919/ACC60939.2024.10644243
title: Algorithms for Finding Compatible Constraints in Receding-Horizon Control of
  Dynamical Systems.
venue: ACC
---
