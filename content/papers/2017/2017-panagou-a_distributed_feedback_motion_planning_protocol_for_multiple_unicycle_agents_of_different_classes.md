---
abstract: This paper presents a novel feedback method for the motion planning and
  coordination of multiple agents that belong to two classes, namely class-A and class-B.
  All agents are modeled via unicycle kinematics. Agents of class-B do not share information
  with agents of class-A and do not participate in ensuring safety, modeling thus
  agents with failed sensing/communication systems, agents of higher priority, or
  moving obstacles with known upper bounded velocity. The method is built upon a family
  of 2-D analytic vector fields, which under mild assumptions are proved to be safe
  feedback motion plans with a unique stable singular point. The conditions which
  ensure collision free and almost global convergence for a single agent and the analytical
  form of the vector fields are then utilized in the design the proposed distributed,
  semi-cooperative multi-agent coordination protocol. Semi-cooperative coordination
  has been defined in prior work as the ad hoc prioritization and conflict resolution
  among agents of the same class; more specifically, participation in conflict resolution
  and collision avoidance for each agent is determined on-the-fly based on whether
  the agent's motion results in decreasing its distance with respect to its neighbor
  agents; based on this condition, the agent decides to either ignore its neighbors,
  or adjust its velocity and avoid the neighbor agent with respect to which the rate
  of decrease of the pairwise inter agent distance is maximal. The proposed coordination
  protocol builds upon this logic and addresses the case of multiple agents of distinct
  classes (class-A and class-B) in conflict. Guarantees on the safety of the multi-agent
  system and the almost global convergence of the agents to their destinations are
  proved. The efficacy of the proposed methodology is demonstrated via simulation
  results in static and dynamic environments.
authors:
- dimitrapanagou
bib: "@article{DBLP:journals/tac/Panagou17,\n  author       = {Dimitra Panagou},\n\
  \  title        = {A Distributed Feedback Motion Planning Protocol for Multiple\
  \ Unicycle\n                  Agents of Different Classes},\n  journal      = {{IEEE}\
  \ Trans. Autom. Control.},\n  volume       = {62},\n  number       = {3},\n  pages\
  \        = {1178--1193},\n  year         = {2017},\n  url          = {https://doi.org/10.1109/TAC.2016.2576020},\n\
  \  doi          = {10.1109/TAC.2016.2576020},\n  timestamp    = {Wed, 20 May 2020\
  \ 21:27:50 +0200},\n  biburl       = {https://dblp.org/rec/journals/tac/Panagou17.bib},\n\
  \  bibsource    = {dblp computer science bibliography, https://dblp.org}\n}"
date: 2017-01-01
key: journals/tac/Panagou17
layout: papers
link: https://doi.org/10.1109/TAC.2016.2576020
title: A Distributed Feedback Motion Planning Protocol for Multiple Unicycle Agents
  of Different Classes.
venue: IEEE Trans. Autom. Control.
---
