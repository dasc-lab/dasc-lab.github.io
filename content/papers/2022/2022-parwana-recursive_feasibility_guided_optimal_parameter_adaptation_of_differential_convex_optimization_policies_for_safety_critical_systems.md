---
abstract: Quadratic Program(QP) based state-feedback controllers, whose inequality
  constraints bound the rate of change of control barrier (CBFs) and lyapunov function
  with a class-$\mathcal{K}$ function of their values, are sensitive to the parameters
  of these class-$\mathcal{K}$ functions. The construction of valid CBFs, however,
  is not straightforward, and for arbitrarily chosen parameters of the QP, the system
  trajectories may enter states at which the QP either eventually becomes infeasible,
  or may not achieve desired performance. In this work, we pose the control synthesis
  problem as a differential policy whose parameters are optimized for performance
  over a time horizon at high level, thus resulting in a bi-level optimization routine.
  In the absence of knowledge of the set of feasible parameters, we develop a Recursive
  Feasibility Guided Gradient Descent approach for updating the parameters of QP so
  that the new solution performs at least as well as previous solution. By considering
  the dynamical system as a directed graph over time, this work presents a novel way
  of optimizing performance of a QP controller over a time horizon for multiple CBFs
  by (1) using the gradient of its solution with respect to its parameters by employing
  sensitivity analysis, and (2) backpropagating these as well as system dynamics gradients
  to update parameters while maintaining feasibility of QPs.
authors:
- hardikparwana
- dimitrapanagou
bib: "@inproceedings{DBLP:conf/icra/ParwanaP22,\n  author       = {Hardik Parwana\
  \ and\n                  Dimitra Panagou},\n  title        = {Recursive Feasibility\
  \ Guided Optimal Parameter Adaptation of Differential\n                  Convex\
  \ Optimization Policies for Safety-Critical Systems},\n  booktitle    = {2022 International\
  \ Conference on Robotics and Automation, {ICRA} 2022,\n                  Philadelphia,\
  \ PA, USA, May 23-27, 2022},\n  pages        = {6807--6813},\n  publisher    = {{IEEE}},\n\
  \  year         = {2022},\n  url          = {https://doi.org/10.1109/ICRA46639.2022.9812398},\n\
  \  doi          = {10.1109/ICRA46639.2022.9812398},\n  timestamp    = {Wed, 20 Jul\
  \ 2022 18:22:50 +0200},\n  biburl       = {https://dblp.org/rec/conf/icra/ParwanaP22.bib},\n\
  \  bibsource    = {dblp computer science bibliography, https://dblp.org}\n}"
date: 2022-01-01
key: conf/icra/ParwanaP22
layout: papers
link: https://doi.org/10.1109/ICRA46639.2022.9812398
title: Recursive Feasibility Guided Optimal Parameter Adaptation of Differential Convex
  Optimization Policies for Safety-Critical Systems.
venue: ICRA
---
