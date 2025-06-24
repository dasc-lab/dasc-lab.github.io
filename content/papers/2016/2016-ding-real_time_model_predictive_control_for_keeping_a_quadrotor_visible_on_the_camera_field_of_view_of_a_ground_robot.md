---
abstract: This paper considers a cooperative control design for an aerial/ground robot
  system, and addresses the problem of maintaining visibility of a quadrotor within
  the camera field-of-view of a ground robot in the presence of external disturbances.
  The quadrotor needs to be tracked by the ground robot with a monocular camera, and
  hence its motion should facilitate the ground vision-based tracking process by remaining
  in the effective camera sensing area. We design a model predictive controller (MPC)
  strategy where the visibility constraints of the camera and the control input constraints
  of the quadrotor are encoded into the cost function via barrier functions, and we
  adopt a fast MPC solver that is able to solve the optimization problem in real time.
  We also propose a method to enhance the robustness of the algorithm by suitably
  defining a restart method for the MPC solver. The applicability of the proposed
  algorithm is demonstrated through simulations and experimental results on real setups.
authors:
- Wei Ding
- Madan Ravi Ganesh
- Robert N. Severinghaus
- Jason J. Corso
- dimitrapanagou
bib: "@inproceedings{DBLP:conf/amcc/DingGSCP16,\n  author       = {Wei Ding and\n\
  \                  Madan Ravi Ganesh and\n                  Robert N. Severinghaus\
  \ and\n                  Jason J. Corso and\n                  Dimitra Panagou},\n\
  \  title        = {Real-time model predictive control for keeping a quadrotor visible\n\
  \                  on the camera field-of-view of a ground robot},\n  booktitle\
  \    = {2016 American Control Conference, {ACC} 2016, Boston, MA, USA, July\n  \
  \                6-8, 2016},\n  pages        = {2259--2264},\n  publisher    = {{IEEE}},\n\
  \  year         = {2016},\n  url          = {https://doi.org/10.1109/ACC.2016.7525254},\n\
  \  doi          = {10.1109/ACC.2016.7525254},\n  timestamp    = {Sat, 30 Sep 2023\
  \ 09:34:15 +0200},\n  biburl       = {https://dblp.org/rec/conf/amcc/DingGSCP16.bib},\n\
  \  bibsource    = {dblp computer science bibliography, https://dblp.org}\n}"
date: 2016-01-01
key: conf/amcc/DingGSCP16
layout: papers
link: https://doi.org/10.1109/ACC.2016.7525254
title: Real-time model predictive control for keeping a quadrotor visible on the camera
  field-of-view of a ground robot.
venue: ACC
---
