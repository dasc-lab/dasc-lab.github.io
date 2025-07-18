---
layout: papers
title:  "How to Adapt Control Barrier Functions? A Learning-Based Approach with Applications to a VTOL Quadplane"
date: 2025-12-19
image: /images/2025-vtol-cdc.gif
venue: "IEEE CDC 2025"
authors:
    - taekyungkim
    - Randal W. Beard
    - dimitrapanagou
projectpage: https://www.taekyung.me/how-to-adapt-cbf
arxiv: https://arxiv.org/abs/2504.03038
code: https://github.com/tkkim-robot/online_adaptive_cbf
abstract: "In this paper, we present a novel theoretical framework for online adaptation of Control Barrier Function (CBF) parameters, i.e., of the class K functions included in the CBF condition, under input constraints. We introduce the concept of locally validated CBF parameters, which are adapted online to guarantee finite-horizon safety, based on conditions derived from Nagumo's theorem and tangent cone analysis. To identify these parameters online, we integrate a learning-based approach with an uncertainty-aware verification process that account for both epistemic and aleatoric uncertainties inherent in neural network predictions. Our method is demonstrated on a VTOL quadplane model during challenging transition and landing maneuvers, showcasing enhanced performance while maintaining safety."
---
