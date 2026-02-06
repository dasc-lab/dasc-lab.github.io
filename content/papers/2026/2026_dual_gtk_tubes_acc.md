---
layout: papers
# specify the title of the paper
title:  "A Formal gatekeeper Framework for Safe Dual Control with Active Exploration"
# specify the date it was published
date: 2026-05-26
# list the authors. if a "/people/id" page exists for the person, it will be linked. If not, the author's name is printed exactly as you typed it.
authors:
    - kalebbennaveed
    - devanshagrawal
    - dimitrapanagou
# give the main figure location, relative to /static/
image: /images/2026_dual_gatekeeper_acc.png
# specify the conference or journal that it was published in
venue: "IEEE ACC 2026"
# link to publisher site (optional)
link: 
# link to arxiv (optional)
arxiv: https://arxiv.org/abs/2510.06351
# link to github (optional)
# code: https://github.com/joonlee16/partial_resilient_leader_follower_consensus
# link to video (optional)
video: 
# link to pdf (optional)
pdf: https://arxiv.org/2510.06351
# abstract
abstract: "Planning safe trajectories under model uncertainty is a fundamental challenge. Robust planning ensures safety by considering worst-case realizations, yet ignores uncertainty reduction and leads to overly conservative behavior. Actively reducing uncertainty on-the-fly during a nominal mission defines the dual control problem. Most approaches address this by adding a weighted exploration term to the cost, tuned to trade off the nominal objective and uncertainty reduction, but without formal consideration of when exploration is beneficial. Moreover, safety is enforced in some methods but not in others. We propose a framework that integrates robust planning with active exploration under formal guarantees as follows: The key innovation and contribution is that exploration is pursued only when it provides a verifiable improvement without compromising safety. To achieve this, we utilize our earlier work on gatekeeper as an architecture for safety verification, and extend it so that it generates both safe and informative trajectories that reduce uncertainty and the cost of the mission, or keep it within a user-defined budget. The methodology is evaluated via simulation case studies on the online dual control of a quadrotor under parametric uncertainty."
# bib entry (optional). the |- is used to allow for multiline entry."
bib:
---
