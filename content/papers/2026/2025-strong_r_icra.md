---
layout: papers
# specify the title of the paper
title:  "Partial Resilient Leader-Follower Consensus in Time-Varying Graphs"
# specify the date it was published
date: 2026-05-26
# list the authors. if a "/people/id" page exists for the person, it will be linked. If not, the author's name is printed exactly as you typed it.
authors:
    - haejoonl
    - dimitrapanagou
# give the main figure location, relative to /static/
image: /images/partial.png
# specify the conference or journal that it was published in
venue: "IEEE ACC 2026"
# link to publisher site (optional)
link: 
# link to arxiv (optional)
arxiv: https://arxiv.org/pdf/2510.01144
# link to github (optional)
code: https://github.com/joonlee16/partial_resilient_leader_follower_consensus
# link to video (optional)
video: 
# link to pdf (optional)
pdf: https://arxiv.org/pdf/2510.01144
# abstract
abstract: "This work studies resilient leader-follower consensus with a bounded number of adversaries. Existing approaches typically require robustness conditions of the entire network to guarantee resilient consensus. However, the behavior of such systems when these conditions are not fully met remains unexplored. To address this gap, we introduce the notion of partial leader-follower consensus, in which a subset of non-adversarial followers successfully tracks the leader’s reference state despite insufficient robustness. We propose a novel distributed algorithm - the Bootstrap Percolation and Mean Subsequence Reduced (BP-MSR) algorithm --- and establish sufficient conditions for individual followers to achieve consensus via the BP-MSR algorithm in arbitrary time-varying graphs. We validate our findings through simulations, demonstrating that our method guarantees partial leader-follower consensus, even when standard resilient consensus algorithms fail.
# bib entry (optional). the |- is used to allow for multiline entry."
bib:
---
