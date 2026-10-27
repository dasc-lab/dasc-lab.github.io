---
layout: papers
title: "Kalman-Bucy Filtering with Randomized Sensing: Fundamental Limits and Sensor Network Design for Field Estimation"
# Website listing date; the journal publication date has not been assigned.
date: 2026-10-26
image: /images/2026-kalman-bucy-randomized-sensing.gif
venue: "Automatica (accepted, to appear)"
authors:
  - xinyiwang*
  - devanshagrawal*
  - dimitrapanagou
pdf: https://arxiv.org/pdf/2511.03740
arxiv: https://arxiv.org/abs/2511.03740
code: https://github.com/Lawliet9666/multi-sensor-network-design
demo: https://lawliet9666.github.io/multi-sensor-network-design-app/
funding: [CAREER, CPS]
abstract: "Stability analysis of the Kalman filter under randomly lost measurements has been widely studied. We revisit this problem in a general continuous-time framework, where both the measurement matrix and noise covariance evolve as random processes, capturing variability in sensing locations. Within this setting, we derive a closed-form upper bound on the expected estimation covariance for continuous-time Kalman filtering. We then apply this framework to spatiotemporal field estimation, where the field is modeled as a Gaussian process observed by randomly located, noisy sensors. Using clarity, introduced in our earlier work as a rescaled form of the differential entropy of a random variable, we establish a lower bound on the expected spatially averaged clarity and show that its steady-state value converges to a grid-independent limit as the grid is refined. This result exposes fundamental performance limits through a composite sensing parameter that jointly captures the effects of the number of sensors, noise level, and measurement frequency. Simulations show close agreement between the continuous-time analytical solution and the discrete-time covariance, with the agreement improving as the sampling interval decreases. The analytical solution also avoids the recursive computations required in the discrete-time formulation. Most importantly, the derived limits provide principled and efficient guidelines for sensor network design prior to deployment."
---

\* Equal contribution.
