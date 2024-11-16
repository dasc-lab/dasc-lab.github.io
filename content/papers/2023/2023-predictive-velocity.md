---
layout: papers
title:  "Predictive Velocity Trajectory Control for a Persistently Operating Solar-Powered Autonomous Surface Vessel"
date: 2023-07-03
image: /images/soc_v_time.png
venue: "IEEE ACC 2023"
authors:
    - kavinmgovindarajan
    - Ben Haydon
    - Christopher Vermillion
code: https://github.com/kmgovind/speed-controller
abstract: "The Gulf Stream represents a major potential
resource for renewable energy but is presently only sparsely
characterized via radar, buoys, gliders, and intermittently op-
erating human-operated research vessels. Dramatically greater
resolution is possible through the use of persistently operating
autonomous surface vessels (ASVs), which can be powered
by wind, wave, or solar resources. Optimizing the control of
these ASVs, taking into account the device and environmental
properties, is crucial to obtaining good data. An ASV’s path and
velocity profile along that path both significantly influence the
amount of a mission domain that can be covered and, ultimately,
the scientific quality of the mission. While our previous work
focused on optimizing the path of a solar-powered ASV with
fixed speed, the present work represents the complement:
optimizing the speed for a given path, accounting for the ASV
dynamics, flow resource, and solar resource. We perform this
optimization through a model predictive controller that maxi-
mizes the projected distance traversed, with a terminal incentive
that captures the estimated additional long-duration range that
is achievable from a given terminal battery state of charge.
We present simulation results based on the SeaTrac SP-48
ASV, Mid-Atlantic Bight/South-Atlantic Bight Regional Ocean
Model, and European Centre for Medium-Range Weather
Forecasts solar model. Our results show improved performance
relative to simpler heuristic controllers that aim to maintain
constant speed or constant state of charge. However, we also
show that the design of the MPC terminal incentive and design
of the heuristic comparison controller can significantly impact
the achieved performance; by examining underlying simulation
results for different designs, we are able to identify likely causes
of performance discrepancies."
pdf: /pdfs/2023-persistent-velocity.pdf
---
