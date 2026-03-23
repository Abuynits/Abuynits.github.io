---
title: "Camera Control at the Edge with Language Models for Scene Understanding"
authors: "<b>A. Buynitsky</b>, S. Ehsani, and P.K. Mishra"
venue: "International Conference on Control, Automation and Robotics (ICCAR)"
year: 2025
thumbnail: "/assets/publications/edge_camera_iccar.png"
arxiv: https://arxiv.org/abs/2505.06402
website: ""
order: 6
bibtex: |
    @inproceedings{Buynitsky_2025,
    title={Camera Control at the Edge with Language Models for Scene Understanding},
    url={http://dx.doi.org/10.1109/ICCAR64901.2025.11073044},
    DOI={10.1109/iccar64901.2025.11073044},
    booktitle={2025 11th International Conference on Control, Automation and Robotics (ICCAR)},
    publisher={IEEE},
    author={Buynitsky, Alexiy and Ehsani, Sina and Pallakonda, Bhanu and Mishra, Pragyana},
    year={2025},
    month=apr, pages={524–530} }
---
In this paper, we present Optimized Prompt-based Unified System (OPUS), a framework that utilizes a Large Language Model (LLM) to control Pan-Tilt-Zoom (PTZ) cameras, providing contextual understanding of natural environments. To achieve this goal, the OPUS system improves cost-effectiveness by generating keywords from a high-level camera control API and transferring knowledge from larger closed-source language models to smaller ones through Supervised Fine-Tuning (SFT) on synthetic data. This enables efficient edge deployment while maintaining performance comparable to larger models like GPT-4. OPUS enhances environmental awareness by converting data from multiple cameras into textual descriptions for language models, eliminating the need for specialized sensory tokens. In benchmark testing, our approach significantly outperformed both traditional language model techniques and more complex prompting methods, achieving a 35% improvement over advanced techniques and a 20% higher task accuracy compared to closed-source models like Gemini Pro. The system demonstrates OPUS's capability to simplify PTZ camera operations through an intuitive natural language interface. This approach eliminates the need for explicit programming and provides a conversational method for interacting with camera systems, representing a significant advancement in how users can control and utilize PTZ camera technology. 
