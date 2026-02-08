---
layout: papers
title:  "Safe Model Predictive Diffusion with Shielding"
date:   2026-01-31
image: /images/2026-safe_mpd.gif
venue: "IEEE ICRA 2026"
authors:
    - taekyungkim
    - Keyvan Majd
    - Hideki Okamoto
    - Bardh Hoxha
    - dimitrapanagou
    - Georgios Fainekos
projectpage: https://www.taekyung.me/safe-mpd
arxiv: https://arxiv.org/abs/2512.06261
code: https://github.com/cps-atlas/safe-mpd
video: https://youtu.be/DQBeybU7EYI
abstract: "Generating safe, kinodynamically feasible, and optimal trajectories for complex robotic systems is a central challenge in robotics. This paper presents Safe Model Predictive Diffusion (Safe MPD), a training-free diffusion planner that unifies a model-based diffusion framework with a safety shield to generate trajectories that are both kinodynamically feasible and safe by construction. By enforcing feasibility and safety on all samples during the denoising process, our method avoids the common pitfalls of post-processing corrections, such as computational intractability and loss of feasibility. We validate our approach on challenging non-convex planning problems, including kinematic and acceleration-controlled tractor-trailer systems. The results show that it substantially outperforms existing safety strategies in success rate and safety, while achieving sub-second computation times. "
---
