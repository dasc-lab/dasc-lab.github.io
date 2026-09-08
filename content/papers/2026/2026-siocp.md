---
layout: papers
# specify the title of the paper
title:  "Staggered Integral Online Conformal Prediction for Safe Dynamics Adaptation with Multi-Step Coverage Guarantees"
# specify the date it was published
date: 2026-12-15
# list the authors. if a "/people/id" page exists for the person, it will be linked. If not, the author's name is printed exactly as you typed it.
authors:
    - dmrc
    - dimitrapanagou
# give the main figure location, relative to /static/
image: /images/2026-siocp.gif
# specify the conference or journal that it was published in
venue: "IEEE CDC 2026"
# link to publisher site (optional)
link: 
# link to arxiv (optional)
arxiv: https://arxiv.org/abs/2604.06058
# link to github (optional)
code: https://github.com/dcherenson/staggered-integral-ocp
# link to video (optional)
video: 
# link to pdf (optional)
pdf: https://arxiv.org/pdf/2604.06058
# abstract
abstract: "Safety-critical control of uncertain, adaptive systems often relies on conservative, worst-case uncertainty bounds that limit closed-loop performance. Online conformal prediction is a powerful data-driven method for quantifying uncertainty when truth values of predicted outputs are revealed online; however, for systems that adapt the dynamics without measurements of the state derivatives, standard online conformal prediction is insufficient to quantify the model uncertainty. We propose Staggered Integral Online Conformal Prediction (SI-OCP), an algorithm utilizing an integral score function to quantify the lumped effect of disturbance and learning error. This approach provides long-run coverage guarantees, resulting in long-run safety when synthesized with safety-critical controllers, including robust tube model predictive control. Finally, we validate the proposed approach through a numerical simulation of an all-layer deep neural network (DNN) adaptive quadcopter using robust tube MPC, highlighting the applicability of our method to complex learning parameterizations and control strategies."
# bib entry (optional). the |- is used to allow for multiline entry."
bib:
---
