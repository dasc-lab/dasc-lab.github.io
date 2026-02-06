---
layout: papers
# specify the title of the paper
title:  "R3R: Decentralized Multi-Agent Collision Avoidance with Infinite-Horizon Safety"
# specify the date it was published
date: 2026-01-21
# list the authors. if a "/people/id" page exists for the person, it will be linked. If not, the author's name is printed exactly as you typed it.
authors:
    - marshallvielmetti
    - devanshagrawal
    - dimitrapanagou
# give the main figure location, relative to /static/
image: /images/2026_r3r_decentralized.png
# specify the conference or journal that it was published in
venue: "IEEE ACC 2026"
# link to publisher site (optional)
link: 
# link to arxiv (optional)
arxiv: https://arxiv.org/abs/2510.06436
# link to github (optional)
code: https://github.com/MarshallVielmetti/r3r_decentralized_gatekeeper
# link to video (optional)
video: 
# link to pdf (optional)
pdf: https://arxiv.org/pdf/2510.06436
# abstract
abstract: "Existing decentralized methods for multi-agent motion planning lack formal, infinite-horizon safety guarantees, especially for communication-constrained systems. We present R3R, to our knowledge the first decentralized and asynchronous framework for multi-agent motion planning under distancebased communication constraints with infinite-horizon safety guarantees for systems of nonlinear agents. R3R’s novelty lies in combining our gatekeeper safety framework with a geometric constraint called R-Boundedness, which together establish a formal link between an agent’s communication radius and its ability to plan safely. We constrain trajectories to within a fixed planning radius that is a function of the agent’s communication radius, which enables trajectories to be shown provably safe for all time, using only local information. Our algorithm is fully asynchronous, and ensures the forward invariance of these guarantees even in time-varying networks where agents asynchronously join, leave, and replan. We validate our approach in simulations of up to 128 Dubins vehicles, demonstrating 100% safety in dense, obstacle rich scenarios. Our results demonstrate that R3R’s performance scales with agent density rather than problem size, providing a practical solution for scalable and provably safe multi-agent systems."
bib:
---
