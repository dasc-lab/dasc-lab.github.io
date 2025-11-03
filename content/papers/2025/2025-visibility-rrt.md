---
layout: papers
title:  "Visibility-Aware RRT* for Safety-Critical Navigation of Perception-Limited Robots in Unknown Environments"
date:   2025-03-17
image: /images/2025-visibility-rrt.png
venue: "IEEE Robotics and Automation Letter 2025"
authors:
    - taekyungkim
    - dimitrapanagou
projectpage: https://www.taekyung.me/visibility-rrt
arxiv: https://arxiv.org/abs/2406.07728
code: https://github.com/tkkim-robot/visibility-rrt
video: https://youtu.be/sYK1A0wceFs
abstract: "Safe autonomous navigation in unknown environments remains a critical challenge for robots with limited sensing capabilities. While safety-critical control techniques, such as Control Barrier Functions (CBFs), have been proposed to ensure safety, their effectiveness relies on the assumption that the robot has complete knowledge of its surroundings. In reality, robots often operate with restricted field-of-view and finite sensing range, which can lead to collisions with unknown obstacles if the planning algorithm is agnostic to these limitations. To address this issue, we introduce the visibility-aware RRT* algorithm that combines sampling-based planning with CBFs to generate safe and efficient global reference paths in partially unknown environments. The algorithm incorporates a collision avoidance CBF and a novel visibility CBF, which guarantees that the robot remains within locally collision-free regions, enabling timely detection and avoidance of unknown obstacles. We conduct extensive experiments interfacing the path planners with two different safety-critical controllers, wherein our method outperforms all other compared baselines across both safety and efficiency aspects."
---
