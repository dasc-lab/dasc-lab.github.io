---
title: "AFOSR: Networked Adversarially-Resilient Reconfigurable Operations in Obstacle Worlds"
# short name; papers with `funding: AFOSR` are listed on this page automatically
key: AFOSR
# one-line summary shown on the /projects/ list page
summary: "Safe planning and attack-tolerant control and estimation for multi-robot networks that must stay resilient to adversaries while operating in confined, obstacle-rich environments."
sponsor: "Air Force Office of Scientific Research (AFOSR), Complex Networks program, FA9550-23-1-0163"
dates: "2023 - 2026"
# external project website (optional)
link:
# image relative to /static/
image: /images/2025-strong_r-icra.gif
# order on the /projects/ page (lower = first)
weight: 3
# principal investigator(s), shown separately from the team
pi:
  - dimitrapanagou
# people on the project in addition to the first authors of tagged papers (optional)
people:
  - haejoonl
---

**NARRO²W SPACE: Networked Adversarially-Resilient Reconfigurable Operations in Obstacle Worlds for Safe Planning and Attack-tolerant Control and Estimation**, funded by the AFOSR Complex Networks program.

Teams of robots that coordinate over a wireless network are vulnerable to adversaries that inject malicious information, for example by sharing false mission parameters to steer the team off course. Resilient consensus algorithms can filter out such information, but only if the communication graph is sufficiently *robust* (in the sense of r- and (r, s)-robustness) relative to the number of adversaries. Most existing results assume a static or slowly varying network. Far less is known about how to maintain, or gracefully relax, graph robustness when robots move through narrow spaces where obstacles and communication range constrain which formations, and therefore which graphs, are feasible.

This project develops planning, control, and estimation methods that let multi-robot networks reconfigure in time and space while keeping a guaranteed level of resilience:

- **Resilient network structure:** characterizing robust communication topologies, including the sparsest graphs that achieve maximal robustness.
- **Adversarially-resilient control barrier functions:** encoding resilience requirements (r- and strong r-robustness) together with safety constraints such as collision and obstacle avoidance, so that robots preserve robust communication while moving safely.
- **Adaptive resilience:** adjusting resilience levels on the fly, and relaxing them in a principled way when needed, based on updated knowledge of the environment and the adversaries, while guaranteeing a minimum tolerance to attacks.
- **Resilient consensus and learning:** leader–follower consensus and distributed decision making that remain correct in time-varying graphs with Byzantine agents.

Algorithms are evaluated in simulation and in experiments with ground and aerial robots in the Ford Robotics Building and M-Air at the University of Michigan.
