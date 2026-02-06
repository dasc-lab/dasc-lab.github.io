---
layout: papers
# specify the title of the paper
title:  "Provably Safe Stein Variational Clarity-Aware Informative Planning"
# specify the date it was published
date: 2026-06-17
# list the authors. if a "/people/id" page exists for the person, it will be linked. If not, the author's name is printed exactly as you typed it.
authors:
    - kalebbennaveed
    - Utkrisht Sahai
    - Anouck Girard
    - dimitrapanagou
# give the main figure location, relative to /static/
image: /images/2026_clarity_stein.png
# specify the conference or journal that it was published in
venue: "2026 L4DC"
# link to publisher site (optional)
link: 
# link to arxiv (optional)
arxiv: https://arxiv.org/abs/2511.09836
# link to github (optional)
# code: https://github.com/joonlee16/partial_resilient_leader_follower_consensus
# link to video (optional)
video: 
# link to pdf (optional)
pdf: https://arxiv.org/2511.09836
# abstract
abstract: "Autonomous robots are increasingly deployed for information-gathering tasks in environments that vary across space and time. Planning informative and safe trajectories in such settings is challenging because information decays when regions are not revisited. Most existing planners model information as static or uniformly decaying, ignoring environments where the decay rate varies spatially; those that model non-uniform decay often overlook how it evolves along the robot's motion, and almost all treat safety as a soft penalty. In this paper, we address these challenges. We model uncertainty in the environment using clarity, a normalized representation of differential entropy from our earlier work that captures how information improves through new measurements and decays over time when regions are not revisited. Building on this, we present Stein Variational Clarity-Aware Informative Planning, a framework that embeds clarity dynamics within trajectory optimization and enforces safety through a low-level filtering mechanism based on our earlier gatekeeper framework for safety verification. The planner performs Bayesian inference-based learning via Stein variational inference, refining a distribution over informative trajectories while filtering each nominal Stein informative trajectory to ensure safety. Hardware experiments and simulations across environments with varying decay rates and obstacles demonstrate consistent safety and reduced information deficits."
# bib entry (optional). the |- is used to allow for multiline entry."
bib:
---
