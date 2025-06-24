---
layout: papers
# specify the title of the paper
title:  "Conformal Prediction in the Loop: Risk-Aware Control Barrier Functions for Stochastic Systems with Data-Driven State Estimators"
# specify the date it was published
date: 2025-05-20
# list the authors. if a "/people/id" page exists for the person, it will be linked. If not, the author's name is printed exactly as you typed it.
authors:
    - junhuizhang
    - Bardh Hoxha
    - Georgios Fainekos
    - dimitrapanagou
# give the main figure location, relative to /static/
image: /images/2025-conformal-prediction.png
# specify the conference or journal that it was published in
venue: "IEEE Control Systems Letters 2025"
# link to project page (optional)
projectpage:
# link to publisher site (optional)
link:
# link to arxiv (optional)
arxiv:
# link to github (optional)
paper: https://ieeexplore.ieee.org/abstract/document/11007767
code:
# link to video (optional)
video:
# link to pdf (optional)
pdf:
# abstract
abstract: "This paper proposes a sampled-data, measurementrobust, risk-aware control barrier function (RA-CBF) framework for stochastic systems with measurement uncertainty. In this framework, what is available for control design are measurements of the system states, which are subject to unknown noise. First, in order to estimate the system states from these measurements, an offline-trained neural network is employed as a state estimator. Next, to quantify the performance of the state estimator, the state space is discretized, and calibration datasets are sampled from the grid points. Conformal prediction is then implemented, providing the estimation error bound with user-defined probability. In addition, we leverage the estimation error bound into sampleddata robust RA-CBF design, such that the probability that the state of the system enters the unsafe set during a finite time horizon is bounded by a desired threshold. Various case studies demonstrate the effectiveness of the proposed method."
---
