---
layout: papers
# specify the title of the paper
title:  "Fully Byzantine-Resilient Distributed Multi-Agent Q-Learning"
# specify the date it was published
date: 2026-12-15
# list the authors. if a "/people/id" page exists for the person, it will be linked. If not, the author's name is printed exactly as you typed it.
authors:
    - haejoonl
    - dimitrapanagou
# give the main figure location, relative to /static/
image: /images/fully_resilient_q.png
# specify the conference or journal that it was published in
venue: "IEEE CDC 2026"
# link to publisher site (optional)
link: 
# link to arxiv (optional)
arxiv: https://arxiv.org/pdf/2604.02791
# link to github (optional)
code: 
# link to video (optional)
video: 
# link to pdf (optional)
pdf: https://arxiv.org/pdf/2604.02791
# abstract
abstract: "We study Byzantine-resilient distributed multi-agent reinforcement learning (MARL), where agents must collaboratively learn optimal value functions over a compromised communication network. Existing resilient MARL approaches typically guarantee almost sure convergence only to near-optimal value functions, or require restrictive assumptions to ensure convergence to optimal solution. As a result, agents may fail to learn the optimal policies under these methods. To address this, we propose a novel distributed Q-learning algorithm, under which all agents’ value functions converge almost surely to the optimal value functions despite Byzantine edge attacks. The key idea is a redundancy-based filtering mechanism that leverages two-hop neighbor information to validate incoming messages, while preserving bidirectional information flow. We then introduce a new topological condition for the convergence of our algorithm, present a systematic method to construct such networks, and prove that this condition can be verified in polynomial time. We validate our results through simulations, showing that our method converges to the optimal solutions, whereas prior methods fail under Byzantine edge attacks."
bib:
---
