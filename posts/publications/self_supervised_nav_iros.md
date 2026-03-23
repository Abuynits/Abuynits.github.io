---
title: "Online Hierarchical Policy Learning using Physics Priors for Robot Navigation in Unknown Environments"
authors: "W. Chen, Y. Liu, <b>A. Buynitsky</b>, and A.H. Qureshi"
venue: "International Conference on Intelligent Robots and Systems (IROS)"
year: 2025
thumbnail: "/assets/publications/self_supervised_nav_iros.png"
arxiv: "https://arxiv.org/abs/2510.01519"
website: ""
order: 3
bibtex: |
  @misc{chen2025onlinehierarchicalpolicylearning,
    title={Online Hierarchical Policy Learning using Physics Priors for Robot Navigation in Unknown Environments}, 
    author={Wei Han Chen and Yuchen Liu and Alexiy Buynitsky and Ahmed H. Qureshi},
    year={2025},
    eprint={2510.01519},
    archivePrefix={arXiv},
    primaryClass={cs.RO},
    url={https://arxiv.org/abs/2510.01519}, 
    }
---
Robot navigation in large, complex, and unknown indoor environments is a challenging problem. The existing approaches, such as traditional sampling-based methods, struggle with resolution control and scalability, while imitation learning-based methods require a large amount of demonstration data. Active Neural Time Fields (ANTFields) have recently emerged as a promising solution by using local observations to learn cost-to-go functions without relying on demonstrations. Despite their potential, these methods are hampered by challenges such as spectral bias and catastrophic forgetting, which diminish their effectiveness in complex scenarios. To address these issues, our approach decomposes the planning problem into a hierarchical structure. At the high level, a sparse graph captures the environment's global connectivity, while at the low level, a planner based on neural fields navigates local obstacles by solving the Eikonal PDE. This physics-informed strategy overcomes common pitfalls like spectral bias and neural field fitting difficulties, resulting in a smooth and precise representation of the cost landscape. We validate our framework in large-scale environments, demonstrating its enhanced adaptability and precision compared to previous methods, and highlighting its potential for online exploration, mapping, and real-world navigation. 
