---
layout: papers
title:  "Fusion of Indirect Methods and Iterative Learning for Persistent Velocity Trajectory Optimization of a Sustainably Powered Autonomous Surface Vessel"
date:   2025-06-30
image: /images/2025-fusedindirectmethods-soc_constraint_subplot.png
venue: "IEEE Conference on Control Technology and Applications (CCTA) 2025"
authors:
    - kavinmgovindarajan
    - devanshagrawal
    - dimitrapanagou
    - Christopher Vermillion
projectpage:
arxiv: https://arxiv.org/abs/2503.10884
code: https://github.com/kmgovind/persistent-speed-control
video: 
abstract: "In this paper, we present the methodology and results for a real-time velocity trajectory optimization for a solar-powered autonomous surface vessel (ASV), where we combine indirect optimal control techniques with iterative learning. The ASV exhibits cyclic operation due to the nature of the solar profile, but weather patterns create inevitable disturbances in this profile. The nature of the problem results in a formulation where the satisfaction of pointwise-in-time state of charge constraints does not generally guarantee persistent feasibility, and the goal is to maximize information gathered over a very long (ultimately persistent) time duration. To address these challenges, we first use barrier functions to tighten pointwise-in-time state of charge constraints by the minimal amount necessary to achieve persistent feasibility. We then use indirect methods to derive a simple switching control law, where the optimal velocity is shown to be an undetermined constant value during each constraint-inactive time segment. To identify this optimal constant velocity (which can vary from one segment to the next), we employ an iterative learning approach. The result is a simple closed-form control law that does not require a solar forecast. We present simulation-based validation results, based on a model of the SeaTrac SP-48 ASV and solar data from the North Carolina coast. These simulation results show that the proposed methodology, which amounts to a closed-form controller and simple iterative learning update law, performs nearly as well as a model predictive control approach that requires an accurate future solar forecast and significantly greater computational capability."
---
