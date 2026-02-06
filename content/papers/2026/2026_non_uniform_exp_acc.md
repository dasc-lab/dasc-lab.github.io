---
layout: papers
# specify the title of the paper
title:  "Multi-Robot Allocation for Information Gathering in Non-Uniform Spatiotemporal Environments"
# specify the date it was published
date: 2026-05-26
# list the authors. if a "/people/id" page exists for the person, it will be linked. If not, the author's name is printed exactly as you typed it.
authors:
    - kalebbennaveed
    - haejoonl
    - dimitrapanagou
# give the main figure location, relative to /static/
image: /images/2026_NST.png
# specify the conference or journal that it was published in
venue: "IEEE ACC 2026"
# link to publisher site (optional)
link: 
# link to arxiv (optional)
arxiv: https://arxiv.org/abs/2510.22883
# link to github (optional)
# code: https://github.com/joonlee16/partial_resilient_leader_follower_consensus
# link to video (optional)
video: 
# link to pdf (optional)
pdf: https://arxiv.org/pdf/2509.22883
# abstract
abstract: "Autonomous robots are increasingly deployed to estimate spatiotemporal fields (e.g., wind, temperature, gas concentration) that vary across space and time. We consider environments divided into non-overlapping regions with distinct spatial and temporal dynamics, termed non-uniform spatiotemporal environments. Gaussian Processes (GPs) can be used to estimate these fields. The GP model depends on a kernel that encodes how the field co-varies in space and time, with its spatial and temporal lengthscales defining the correlation. Hence, when these lengthscales are incorrect or do not correspond to the actual field, the estimates of uncertainty can be highly inaccurate. Existing GP methods often assume one global lengthscale or update only periodically; some allow spatial variation but ignore temporal changes. To address these limitations, we propose a two-phase framework for multi-robot field estimation. Phase 1 uses a variogram-driven planner to learn region-specific spatial lengthscales. Phase 2 employs an allocation strategy that reassigns robots based on the current uncertainty, and updates sampling as temporal lengthscales are refined. For encoding uncertainty, we utilize clarity, an information metric from our earlier work. We evaluate the proposed method across diverse environments and provide convergence analysis for spatial lengthscale estimation, along with dynamic regret bounds quantifying the gap to the oracle's allocation sequence"
bib:
---
