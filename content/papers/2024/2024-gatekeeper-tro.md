---
layout: papers
title:  "gatekeeper: Online Safety Verification and Control for Nonlinear Systems in Dynamic Environments"
date:   2024-09-04
image: /images/2023-gatekeeper-iros.png
venue: "IEEE T-RO 2024"
authors:
    - devanshagrawal
    - Ruichang Chen
    - dimitrapanagou
link: https://ieeexplore.ieee.org/document/10665919
arxiv: https://arxiv.org/abs/2211.14361
code: https://github.com/dev10110/gatekeeper
abstract: "This paper presents the gatekeeper algorithm, a real-time and computationally-lightweight method to ensure that nonlinear systems can operate safely in dynamic environments despite limited perception. gatekeeper integrates with existing path planners and feedback controllers by introducing an additional verification step that ensures that proposed trajectories can be executed safely, despite nonlinear dynamics subject to bounded disturbances, input constraints and partial knowledge of the environment. Our key contribution is that (A) we propose an algorithm to recursively construct committed trajectories, and (B) we prove that tracking the committed trajectory ensures the system is safe for all time into the future. The method is demonstrated on a complicated firefighting mission in a dynamic environment, and compares against the state-of-the-art techniques for similar problems."
bib: |-
  @inproceedings{agrawal2024gatekeeper,
    title={gatekeeper: Online safety verification and control for nonlinear systems in dynamic environments},
    author={Agrawal, Devansh and Chen, Ruichang and Panagou, Dimitra},
    booktitle={{IEEE Transactions on Robotics},
    year={2024},
    volume={40},
    number={},
    pages={4358-4375},
    organization={IEEE}
  }
---
