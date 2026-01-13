---
layout: papers
# specify the title of the paper
title:  "Reformulations of Quadratic Programs for Lipschitz Continuity"
# specify the date it was published
date: 2025-11-06
# list the authors. if a "/people/id" page exists for the person, it will be linked. If not, the author's name is printed exactly as you typed it.
authors:
    - devanshagrawal
    - haejoonl
    - dimitrapanagou
# give the main figure location, relative to /static/
image: /images/reformulations.gif
# specify the conference or journal that it was published in
venue: "IEEE L-CSS 2025"
# link to publisher site (optional)
link: 
# link to arxiv (optional)
arxiv: https://arxiv.org/abs/2508.18530
# link to github (optional)
code: https://github.com/joonlee16/Lipschitz-controllers
# link to video (optional)
video: 
# link to pdf (optional)
pdf: https://arxiv.org/pdf/2508.18530
# abstract
abstract: "Optimization-based controllers often lack regularity guarantees, such as Lipschitz continuity, when multiple constraints are present. When used to control a dynamical system, these conditions are essential to ensure the existence and uniqueness of the system's trajectory. Here we propose a general method to convert a \acf{QP} into a \acf{SOCP}, which is shown to be Lipschitz continuous. Key features of our approach are that (i)~the regularity of the resulting formulation does not depend on the structural properties of the constraints, such as the linear independence of their gradients; and (ii)~it admits a closed-form solution under some assumptions, which is not available for general \acp{QP} with multiple constraints, enabling faster computation. We support our method with rigorous analysis and examples. "
bib:
---
