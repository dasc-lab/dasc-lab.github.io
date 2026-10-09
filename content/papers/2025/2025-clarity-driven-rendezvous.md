---
layout: papers
title:  "Clarity-Driven Ergodic Control for Persistent Tip-and-Cue Missions with Synchronized Rendezvous"
date:   2025-12-12
image: /images/clarity-rendezvous-conops.png
venue: "IEEE CDC 2025"
authors:
    - David Li
    - kavinmgovindarajan
    - Christopher Vermillion
projectpage:
link: https://ieeexplore.ieee.org/abstract/document/11313015
arxiv:
code: https://github.com/corelab-umich/OptimalRendezvous
pdf: /pdfs/2025-clarity-driven-rendezvous.pdf
video: 
abstract: "This paper presents a persistent control methodology for a sustainably powered host/agent network that executes tip-and-cue oceanographic observing operations within a spatiotemporally evolving environment. Specifically, a renewably powered host vessel simultaneously serves as a recharging platform for an autonomous aerial vehicle (AAV), while also performing broad surveillance of an evolving mission domain. When the AAV is on board the host vessel, the mission trajectory (termed the ``nominal'' trajectory) is selected based on a clarity-driven ergodic planner. When a location of interest (termed a ``tip'' location) is detected by the host vessel, the AAV is dispatched to provide detailed observation of that location. This necessitates a replanning operation (of the ``rendezvous'' trajectory) wherein a rendezvous point is selected to maximize the mutual long-horizon benefit to the host and agent. Because the mutually beneficial rendezvous point will, in general, deviate from the original ergodic trajectory, another replanning operation (of the nominal trajectory) is completed on rendezvous. In this paper, we demonstrate the efficacy of the combination of the ergodic trajectory planner and rendezvous planner for a solar-powered host vessel (the SeaTrac SP-48 ASV) and a quadrotor (Agilicious) agent vehicle. In particular, the combined control system is shown to significantly outperform a line-transect strategy and an ergodic controller wherein the rendezvous point is constrained to lie on the nominal mission trajectory."
---
