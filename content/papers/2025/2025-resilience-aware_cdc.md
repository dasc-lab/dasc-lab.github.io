---
layout: papers
# specify the title of the paper
title:  "Distributed Resilience-Aware Control in Multi-Robot Networks"
# specify the date it was published
date: 2025-12-19
# list the authors. if a "/people/id" page exists for the person, it will be linked. If not, the author's name is printed exactly as you typed it.
authors:
    - haejoonl
    - dimitrapanagou
# give the main figure location, relative to /static/
image: /images/2025-resilience-aware-controller.gif
# specify the conference or journal that it was published in
venue: IEEE CDC 2025
# link to publisher site (optional)
link: 
# link to arxiv (optional)
arxiv: https://arxiv.org/abs/2504.03120
# link to github (optional)
code: https://github.com/joonlee16/Distributed-Resilience-Aware-Control
# link to video (optional)
video: 
# link to pdf (optional)
pdf: https://arxiv.org/pdf/2504.03120
# abstract
abstract: "Ensuring resilient consensus in multi-robot systems with misbehaving agents remains a challenge, as many existing network resilience properties are inherently combinatorial and globally defined. While previous works have proposed control laws to enhance or preserve resilience in multi-robot networks, they often assume a fixed topology with known resilience properties, or require global state knowledge. These assumptions may be impractical in physically-constrained environments, where safety and resilience requirements are conflicting, or when misbehaving agents corrupt the shared information. In this work, we propose a distributed control law that enables each robot to guarantee resilient consensus and safety during its navigation without fixed topologies using only locally available information. To this end, we establish a new sufficient condition for resilient consensus in time-varying networks based on the degree of non-misbehaving or normal agents. Using this condition, we design a Control Barrier Function (CBF)-based controller that guarantees resilient consensus and collision avoidance without requiring estimates of global state and/or control actions of all other robots. Finally, we validate our method through simulations."
bib:
---
