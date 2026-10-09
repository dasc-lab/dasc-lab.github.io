---
layout: papers
# specify the title of the paper
title:  "Multi-Objective Kinodynamic Planning in Stochastic Environments"
# specify the date it was published
date: 2026-07-21
# list the authors. if a "/people/id" page exists for the person, it will be linked. If not, the author's name is printed exactly as you typed it.
authors:
    - marshallvielmetti
    - dmrc
    - dimitrapanagou
# give the main figure location, relative to /static/
image: /images/smo_sst.gif
# specify the conference or journal that it was published in
venue: "IEEE CDC 2026"
# link to project page (optional)
projectpage:
# link to publisher site (optional)
link:
# link to arxiv (optional)
arxiv: "https://arxiv.org/pdf/2607.19284"
# link to github (optional)
code: "https://github.com/MarshallVielmetti/Multi_Objective_Planning_Stochastic_Environments"
# link to video (optional)
video:
# link to pdf (optional)
pdf: "https://arxiv.org/pdf/2607.19284"
# abstract
abstract: This paper addresses kinodynamic planning for stochastic nonlinear systems subject to non-Gaussian disturbances in reactive stochastic hybrid environments. Conventional chance-constrained formulations require a prescribed risk threshold. We reformulate the problem as a multi-objective optimization in which risk and expected cost are jointly minimized. To efficiently approximate the Pareto front of solutions to the proposed problem, we introduce Stochastic Multi-Objective Stable Sparse RRT (SMO-SST), which extends the sparsification approach of Stable Sparse RRT (SST) to the proposed stochastic multi-objective problem.  We prove the proposed algorithm to be asymptotically near-optimal with respect to the risk-cost Pareto front, and provide explicit bounds on approximation error. In wall-clock-matched trials, the proposed algorithm outperformed non-pruning ablations, showcasing the efficacy of the proposed pruning mechanism. These results provide a principled framework for exploring risk-performance tradeoffs in nonlinear, non-Gaussian, reactive environments.
# bib entry (optional). the |- is used to allow for multiline entry.
bib:
---
