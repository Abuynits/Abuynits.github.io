---
title: "TacO: Benchmarking Tactile Sensors for Object Manipulation"
authors: "Anya Zorin, Zilin Si, Myungsun Park, Junsung Park, <b>Alexiy Buynitsky</b>, Sachin Bhadang, Taejun Park, Sohee John Yoon, Yong-Lae Park, Oliver Kroemer, Zeynep Temel, Michael T. Tolley, Sha Yi, Xiaolong Wang"
venue: "preprint"
year: 2026
thumbnail: "/assets/publications/tactile.png"
arxiv: "https://arxiv.org/abs/2605.21976"
website: "https://anyazorin.com/projects/taco"
video: ""
order: 1
bibtex: |
    @misc{taco2026,
    title   = {TacO: Benchmarking Tactile Sensors for Object Manipulation},
    author  = {Anya Zorin, Zilin Si, Myungsun Park, Junsung Park, Alexiy Buynitsky, Sachin Bhadang, Taejun Park, Sohee John Yoon, Yong-Lae Park, Oliver Kroemer, Zeynep Temel, Michael T. Tolley, Sha Yi, Xiaolong Wang},
    year    = {2026},
    }
---
While vision-based learning from demonstrations has achieved remarkable success in enabling robots to perform manipulation tasks and high-level semantic reasoning, it remains insufficient for complex, contact-rich manipulation. These fine-grained, low-level tasks are still bottlenecked by the inherent limitations of visual feedback, which cannot capture the dynamics essential for precise physical interactions. Despite broad agreement that tactile sensing improves manipulation, there is no empirical guidance on which tactile sensors are best suited for which manipulation tasks. In this paper, we provide a systematic, task-driven evaluation of tactile sensors for robot manipulation and propose a framework for selecting and evaluating sensors based on manipulation policy performance. Separate manipulation policies are trained for tactile sensors of four distinct modalities: visual, acoustic, magnetic, and resistive, across three tasks: pick-and-place with unknown mass, object reorientation, and plug insertion. For each task, an analysis of how sensor properties such as spatial resolution, shear sensing, and tactile representation, and the inherent material friction affect task performances is done. Rather than tactile sensing being universally beneficial in the same way, our results show that the usefulness of tactile information depends strongly on sensor modality, material properties, and the specific manipulation tasks. All of the tactile sensors, code, data, and hardware setup for sensor characterization will be publicly available on the project website.