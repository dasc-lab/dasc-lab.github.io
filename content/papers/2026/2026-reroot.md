---
layout: papers
# specify the title of the paper
title:  "Autonomy Architectures for Safe Planning in Unknown Environments Under Budget Constraints"
# specify the date it was published
date: 2026-05-26
# list the authors. if a "/people/id" page exists for the person, it will be linked. If not, the author's name is printed exactly as you typed it.
authors:
    - dmrc
    - devanshagrawal
    - dimitrapanagou
# give the main figure location, relative to /static/
image: /images/2026-reroot_field.gif
# specify the conference or journal that it was published in
venue: "IEEE ACC 2026"
# link to publisher site (optional)
link: 
# link to arxiv (optional)
arxiv: https://arxiv.org/abs/2504.03001
# link to github (optional)
code: https://github.com/dcherenson/budget-constrained-planning
# link to video (optional)
video: 
# link to pdf (optional)
pdf: https://arxiv.org/pdf/2504.03001
# abstract
abstract: "Mission planning can often be formulated as a constrained control problem under multiple path constraints (i.e., safety constraints) and budget constraints (i.e., resource expenditure constraints). In a priori unknown environments, verifying that an offline solution will satisfy the constraints for all time can be difficult, if not impossible. We present ReRoot, a novel sampling-based framework that enforces safety and budget constraints for nonlinear systems in unknown environments. The main idea is that ReRoot grows multiple reverse RRT* trees online, starting from renewal sets, i.e., sets where the budget constraints are renewed. The dynamically feasible backup trajectories guarantee safety and reduce resource expenditure, which provides a principled backup policy when integrated into the gatekeeper safety verification architecture. We demonstrate our approach in simulation with a fixed-wing UAV in a GNSS-denied environment with a budget constraint on localization error that can be renewed at visual landmarks."
# bib entry (optional). the |- is used to allow for multiline entry."
bib:
---
