---
layout: papers
# specify the title of the paper
title:  "Robust Multi-Agent LLMs under Byzantine Faults"
# specify the date it was published
date: 2026-10-29
# list the authors. if a "/people/id" page exists for the person, it will be linked. If not, the author's name is printed exactly as you typed it.
authors:
    - haejoonl
    - Vincent-Daniel Yun
    - dimitrapanagou
    - Sai Praneeth Karimireddy
# give the main figure location, relative to /static/
image: /images/robust-llms.png
# specify the conference or journal that it was published in
venue: "EMNLP 2026 Oral"
# link to publisher site (optional)
link: 
# link to arxiv (optional)
arxiv: https://arxiv.org/pdf/2605.09076
# link to github (optional)
code: https://github.com/daniel-eai/Robust-Multi-Agent-LLMs-under-Byzantine-Faults
# link to video (optional)
video: 
# link to pdf (optional)
pdf: https://arxiv.org/pdf/2605.09076
# abstract
abstract: "Large language model (LLM) agents increasingly collaborate over peer-to-peer networks to improve their reliability. However, these same interactions can also introduce vulnerability to unreliable or Byzantine agents that can propagate incorrect information and degrade overall system performance. To address this, we propose Self-Anchored Consensus (SAC), a fully decentralized filter-and-refine protocol in which agents iteratively exchange responses, locally evaluate and filter unreliable messages, and refine their own outputs. We present (F+1)-robustness conditions on the communication graph that ensure honest agents preserve and propagate reliable information despite Byzantine influence. Experiments across diverse open- and closed-weight LLMs on mathematical and commonsense reasoning benchmarks show that SAC effectively suppresses Byzantine influence and consistently improves performance across diverse communication topologies, whereas prior methods degrade significantly under Byzantine attacks."
# bib entry (optional). the |- is used to allow for multiline entry."
bib:
---
