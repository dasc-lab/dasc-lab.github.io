---
layout: papers
title:  "Learning to Refine Input Constrained Control Barrier Functions via Uncertainty-Aware Online Parameter Adaptation"
date:   2025-05-19
image: /images/2025-online-adaptive-iccbf.png
venue: "IEEE ICRA 2025"
authors:
    - taekyungkim
    - Robin Inho Kee
    - dimitrapanagou
projectpage: https://www.taekyung.me/online-adaptive-cbf
arxiv: https://arxiv.org/abs/2409.14616
code: https://github.com/tkkim-robot/online_adaptive_cbf
video: https://youtu.be/255IUS1f6Lo
abstract: "Control Barrier Functions (CBFs) have become powerful tools for ensuring safety in nonlinear systems. However, finding valid CBFs that guarantee persistent safety and feasibility remains an open challenge, especially in systems with input constraints. Traditional approaches often rely on manually tuning the parameters of the class K functions of the CBF conditions a priori. The performance of CBF-based controllers is highly sensitive to these fixed parameters, potentially leading to overly conservative behavior or safety violations. To overcome these issues, this paper introduces a learning-based optimal control framework for online adaptation of Input Constrained CBF (ICCBF) parameters in discrete-time nonlinear systems. Our method employs a probabilistic ensemble neural network to predict the performance and risk metrics, as defined in this work, for candidate parameters, accounting for both epistemic and aleatoric uncertainties. We propose a two-step verification process using Jensen-Renyi Divergence and distributionally-robust Conditional Value at Risk to identify valid parameters. This enables dynamic refinement of ICCBF parameters based on current state and nearby environments, optimizing performance while ensuring safety within the verified parameter set. Experimental results demonstrate that our method outperforms both fixed-parameter and existing adaptive methods in robot navigation scenarios across safety and performance metrics."
---
