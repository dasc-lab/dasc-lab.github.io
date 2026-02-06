---
layout: papers
title:  "Adaptive Ergodic Search with Energy-Aware Scheduling for Persistent Multi-Robot Missions"
date:   2025-09-08
image: /images/mEclares.gif
venue: "Autonomous Robots, Springer Nature"
authors:
    - kalebbennaveed
    - devanshagrawal
    - rahulhkumar
    - dimitrapanagou
arxiv: https://arxiv.org/abs/2505.11663
code: https://github.com/kalebbennaveed/mEclares-main
video: https://www.youtube.com/watch?v=dmaZDvxJgF8
abstract: "Autonomous robots are increasingly deployed for long-term information-gathering tasks, which pose two key challenges: planning informative trajectories in environments that evolve across space and time, and ensuring persistent operation under energy constraints. This paper presents a unified framework, mEclares, that addresses both challenges through adaptive ergodic search and energy-aware scheduling in multi-robot systems. Our contributions are two-fold: (1) we model real-world variability using stochastic spatiotemporal environments, where the underlying information evolves unpredictably due to process uncertainty. To guide exploration, we construct a target information spatial distribution (TISD) based on clarity, a metric that captures the decay of information in the absence of observations and highlights regions of high uncertainty; and (2) we introduce Robustmesch (Rmesch), an online scheduling method that enables persistent operation by coordinating rechargeable robots sharing a single mobile charging station. Unlike prior work, our approach avoids reliance on preplanned schedules, static or dedicated charging stations, and simplified robot dynamics. Instead, the scheduler supports general nonlinear models, accounts for uncertainty in the estimated position of the charging station, and handles central node failures. The proposed framework is validated through real-world hardware experiments, and feasibility guarantees are provided under specific assumptions."
---
