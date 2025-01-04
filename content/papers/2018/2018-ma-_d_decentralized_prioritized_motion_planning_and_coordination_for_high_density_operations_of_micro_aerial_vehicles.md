---
abstract: This paper presents a decentralized motion planning method for multiple
  aerial vehicles moving among 3-D polygonal obstacles resembling an urbanlike environment.
  The algorithm combines a prioritized  $A^\star$  algorithm for high-level planning,
  along with a coordination method based on barrier functions for low-level trajectory
  generation and vehicle control. To this end, we extend the barrier functions method
  developed in our earlier work so that it treats 2-D and 3-D polygonal obstacles,
  and generates collision-free trajectories for the multiagent system. We furthermore
  augment the low-level trajectory generation and control with a prioritized  $A^\star$  path
  planning algorithm, in order to compute waypoints and paths that force the agents
  of lower priority to avoid the paths of the agents of higher priority, reducing
  thus congestion. This feature enhances further the performance of the barrier-based
  coordination, and results in shorter paths and time to the goal destinations. We
  finally extend the proposed control design to the agents of constrained double-integrator
  dynamics, compared with the single-integrator case in our earlier work. We assume
  that the obstacles are known to the agents, and that each agent knows the state
  of other agents lying in its sensing area. Simulation results in 2-D and 3-D polygonal
  environments, as well as experimental results with micro aerial vehicles (quadrotors)
  in an indoor lab environment demonstrate the efficacy of the proposed approach.
authors:
- Xiaobai Ma
- Ziyuan Jiao
- Zhenkai Wang
- dimitrapanagou
bib: "@article{DBLP:journals/tcst/MaJWP18,\n  author       = {Xiaobai Ma and\n   \
  \               Ziyuan Jiao and\n                  Zhenkai Wang and\n          \
  \        Dimitra Panagou},\n  title        = {3-D Decentralized Prioritized Motion\
  \ Planning and Coordination for\n                  High-Density Operations of Micro\
  \ Aerial Vehicles},\n  journal      = {{IEEE} Trans. Control. Syst. Technol.},\n\
  \  volume       = {26},\n  number       = {3},\n  pages        = {939--953},\n \
  \ year         = {2018},\n  url          = {https://doi.org/10.1109/TCST.2017.2699165},\n\
  \  doi          = {10.1109/TCST.2017.2699165},\n  timestamp    = {Mon, 08 Jun 2020\
  \ 22:20:35 +0200},\n  biburl       = {https://dblp.org/rec/journals/tcst/MaJWP18.bib},\n\
  \  bibsource    = {dblp computer science bibliography, https://dblp.org}\n}"
date: 2018-01-01
key: journals/tcst/MaJWP18
layout: papers
link: https://doi.org/10.1109/TCST.2017.2699165
title: 3-D Decentralized Prioritized Motion Planning and Coordination for High-Density
  Operations of Micro Aerial Vehicles.
venue: IEEE Trans. Control. Syst. Technol.
---
