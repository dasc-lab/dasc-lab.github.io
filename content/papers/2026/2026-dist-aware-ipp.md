---
layout: papers
title: Disturbance-Aware Informative Planning in Spatiotemporal Environments
date: 2026-11-13
authors:
  - kalebbennaveed
  - haejoonl
  - Anouck Girard
  - dimitrapanagou
venue: "Under Review, 2026"
image: /images/2026-dist-aware-ipp.gif
listPreviewAlt: A robot samples wind, then follows a monitoring route around obstacles.
arxiv: https://arxiv.org/abs/2611.18505
pdf: https://arxiv.org/pdf/2611.18505
projectpage: https://kalebbennaveed.github.io/dist-aware-ipp/
code: https://github.com/kalebbennaveed/voi-diffusion-ipp
demo: https://kalebbennaveed.github.io/dist-aware-ipp/drone/
slides: https://kalebbennaveed.github.io/dis-aware-ipp/slides/
abstract: >-
  A robot monitoring a changing environment must revisit locations as its measurements become stale.
  Wind can slow the robot or push it off course. The planner first identifies routes to locations
  that need fresh measurements and samples wind where its uncertainty matters for those routes.
  It then uses the learned wind field to predict how much information the robot can collect along
  each trajectory. In four simulations, targeted sampling cut the time spent learning disturbances
  by 25.0–52.3% compared with sampling across the whole environment.
---
