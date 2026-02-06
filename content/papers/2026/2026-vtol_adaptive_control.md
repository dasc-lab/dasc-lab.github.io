---
layout: papers
# specify the title of the paper
title:  "Adaptive Control Allocation for Underactuated Time-Scale Separated Non-Affine Systems"
# specify the date it was published
date: 2026-05-26
# list the authors. if a "/people/id" page exists for the person, it will be linked. If not, the author's name is printed exactly as you typed it.
authors:
    - dmrc
    - dimitrapanagou
# give the main figure location, relative to /static/
image: /images/2026-vtol_adaptive_control.gif
# specify the conference or journal that it was published in
venue: "IEEE ACC 2026"
# link to publisher site (optional)
link: 
# link to arxiv (optional)
arxiv: https://arxiv.org/abs/2510.07507
# link to github (optional)
code: https://github.com/dcherenson/adaptive-control-underactuated
# link to video (optional)
video: 
# link to pdf (optional)
pdf: https://arxiv.org/pdf/2510.07507
# abstract
abstract: "Many robotic systems are underactuated, meaning not all degrees of freedom can be directly controlled due to lack of actuators, input constraints, or state-dependent actuation. This property, compounded by modeling uncertainties and disturbances, complicates the control design process for trajectory tracking. In this work, we propose an adaptive control architecture for uncertain, nonlinear, underactuated systems with input constraints. Leveraging time-scale separation, we construct a reduced-order model where fast dynamics provide virtual inputs to the slower subsystem and use dynamic control allocation to select the optimal control inputs given the non-affine dynamics. To handle uncertainty, we introduce a state predictor-based adaptive law, and through singular perturbation theory and Lyapunov analysis, we prove stability and bounded tracking of reference trajectories. The proposed method is validated on a VTOL quadplane with nonlinear, state-dependent actuation, demonstrating its utility as a unified controller across various flight regimes, including cruise, landing transition, and hover."
# bib entry (optional). the |- is used to allow for multiline entry."
bib:
---
