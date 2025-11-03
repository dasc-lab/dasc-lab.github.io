---
layout: papers
title:  "A Constructive Method for Designing Safe Multirate Controllers for Differentially-Flat Systems"
date:  2022-12-17
image: /images/2021-differentially-flat.png
venue: "IEEE L-CSS and ACC 2022"
authors:
    - devanshagrawal
    - hardikparwana
    - Ryan K Cosner
    - Ugo Rosolia
    - Aaron D Ames
    - dimitrapanagou
# give the main figure location, relative to /static/
# link to publisher site (optional)
link: https://doi.org/10.1109/LCSYS.2021.3136465
# link to arxiv (optional)
arxiv:
# link to github (optional)
code: https://github.com/dev10110/Multirate-Controllers-for-Differentially-Flat-Systems
# link to video (optional)
video:
# link to pdf (optional)
pdf: /pdfs/2021-differentially-flat.pdf
# abstract
abstract: "This paper introduces the notion of an Input
Constrained Control Barrier Function (ICCBF), as a method to
synthesize safety-critical controllers for nonlinear control-affine
systems with input constraints. The method identifies a subset
of the safe set of states, and constructs a controller to render the
subset forward invariant. The feedback controller is represented
as the solution to a quadratic program, which can be solved
efficiently for real-time implementation. Furthermore, we show
that ICCBFs are a generalization of Higher Order Control
Barrier Functions, and thus are applicable to systems of non-
uniform relative degree. Simulation results are presented for the
adaptive cruise control problem, and a spacecraft rendezvous
problem."
bib: |-
  @ARTICLE{9655322,
    author={Agrawal, Devansh R. and Parwana, Hardik and Cosner, Ryan K. and Rosolia, Ugo and Ames, Aaron D. and Panagou, Dimitra},
    journal={IEEE Control Systems Letters},
    title={A Constructive Method for Designing Safe Multirate Controllers for Differentially-Flat Systems},
    year={2022},
    volume={6},
    number={},
    pages={2138-2143},
    doi={10.1109/LCSYS.2021.3136465}
  }
---
