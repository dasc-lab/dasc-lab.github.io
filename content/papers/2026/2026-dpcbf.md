---
layout: papers
title:  "Beyond Collision Cones: Dynamic Obstacle Avoidance for Nonholonomic Robots via Dynamic Parabolic Control Barrier Functions"
date:   2026-01-31
image: /images/2026-dpcbf.gif
venue: "IEEE ICRA 2026"
authors:
    - hunkukpark*
    - taekyungkim*
    - dimitrapanagou
projectpage: https://www.taekyung.me/dpcbf
arxiv: https://arxiv.org/abs/2510.01402
code: https://github.com/tkkim-robot/safe_control/tree/main/dynamic_env
video: https://youtu.be/57qgoe7YJao
abstract: "Control Barrier Functions (CBFs) are a powerful tool for ensuring the safety of autonomous systems, yet applying them to nonholonomic robots in cluttered, dynamic environments remains an open challenge. State-of-the-art methods often rely on collision-cone or velocity-obstacle constraints which, by only considering the angle of the relative velocity, are inherently conservative and can render the CBF-based quadratic program infeasible, particularly in dense scenarios. To address this issue, we propose a Dynamic Parabolic Control Barrier Function (DPCBF) that defines the safe set using a parabolic boundary. The parabola's vertex and curvature dynamically adapt based on both the distance to an obstacle and the magnitude of the relative velocity, creating a less restrictive safety constraint. We prove that the proposed DPCBF is valid for a kinematic bicycle model subject to input constraints. Extensive comparative simulations demonstrate that our DPCBF-based controller significantly enhances navigation success rates and QP feasibility compared to baseline methods. Our approach successfully navigates through dense environments with up to 100 dynamic obstacles, scenarios where collision cone-based methods fail due to infeasibility."
---
