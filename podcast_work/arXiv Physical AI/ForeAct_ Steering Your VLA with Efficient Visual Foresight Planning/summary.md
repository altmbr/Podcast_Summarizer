# ForeAct: Steering Your VLA with Efficient Visual Foresight Planning

**Podcast:** arXiv Physical AI Research
**Date:** 2026-04-02
**Processed:** 2026-04-02T09:05:00Z
**Participants:** Zhuoyang Zhang, Song Han, et al. (arXiv Physical AI)
**Source:** paper
**arXiv:** 2602.12322
**PDF:** https://arxiv.org/pdf/2602.12322

---

# ForeAct: Steering Your VLA with Efficient Visual Foresight Planning

**TL;DR for decision-makers:** MIT and NVIDIA researchers built a plug-in planning layer that shows robots *what the next step should look like* rather than just telling them in words. Dropped into a state-of-the-art VLA without any architectural changes, it lifted success rates from 46.5% to 87.4% across 11 real-world tasks. This is a meaningful unlock for complex, multi-step manipulation — the exact regime where current VLAs break down in production.

---

## 1. Key Themes

### Visual Instructions Outperform Language Instructions for Motor Control

The paper's core bet is that showing a robot the *next state* is fundamentally more efficient than describing it. The authors formalize this as a division of labor: let a world model handle "what should happen next" and let the VLA handle "how to physically do it." As they put it: *"By supplying imagined future observations, our method substantially reduces the difficulty for VLAs in grounding high-level language instructions into concrete actions. Consequently, the VLA model can focus solely on visuo-motor inference rather than high-level semantic reasoning."* (Abstract/Section 3.1). The +40.9% absolute improvement over the π₀ baseline is the empirical payoff of this division.

### A Plug-In Planning Layer That Requires Zero Architectural Surgery

Most planning-layer papers require retraining or restructuring the base policy. ForeAct sidesteps this entirely by treating the generated future image as just another camera input. *"State-of-the-art VLAs can integrate our planner seamlessly by simply augmenting their visual inputs, without any architectural modification."* (Abstract). This is strategically important: it means the technique is VLA-agnostic and can be dropped on top of whatever base model a team is already using — validated on both π₀ and π₀.5 (Table 2).

### Pretrained World Models Are Non-Negotiable for Generalization

The paper runs a clean ablation showing that a foresight generator trained only on in-house data fails completely on out-of-distribution tasks (fidelity score: 0.00, quality: 0.00), while the pretrained version scores 0.88 and 0.96 respectively on the same OOD tasks (Table 1). The pretraining covered *"over 1 million multi-task, cross-embodiment episodes curated from open-source datasets"* (Section 3.2). The message is unambiguous: generalization requires scale, and proprietary-data-only approaches will hit a hard ceiling.

### Visual Foresight Dramatically Reduces Data Requirements

The paper tests how performance scales with training data volume on a challenging cleaning task. *"With only 60% of the data, it attains a >90% success rate, and with just 20% of the data, it still achieves 79%, substantially outperforming the baseline."* (Section 4.6). The explanation is intuitive: when you show the robot a goal image, it doesn't need to see every possible object configuration to understand what "success" looks like. This directly attacks one of the biggest cost drivers in robotics deployment — teleoperation data collection.

### Sub-Second World Model Inference Makes Closed-Loop Planning Practical

Previous video-generation-based world model approaches were too slow for real-time control. ForeAct generates a 640×480 future observation in 0.33 seconds on an H100 GPU using 8 denoising steps. *"This demonstrates the practicality of our planner for real-world closed-loop control."* (Section 4.2). Notably, the paper also points out that *"although we have not yet incorporated acceleration techniques such as distillation or quantization, we believe further reductions in latency are possible"* — meaning 0.33s is likely not the floor.

---

## 2. Contrarian Perspectives

### General-Purpose Image Editing Models Are Useless for Robot Planning

A reasonable assumption is that powerful foundation models like GPT-4o or Gemini can be repurposed as world models. The paper directly tests this and finds it doesn't hold. GPT-Image, Gemini 2.5 Flash, and Qwen-Edit all fail: *"The first model slightly adjusts the arm, it produces an unnatural grasp of the carrot, while the other two models directly hallucinate a carrot on the plate instead of manipulating the existing one... state-of-the-art image-editing models lack an understanding of the underlying real-world physics and object dynamics."* (Section 4.2). For builders evaluating whether to leverage foundation model APIs for robot planning, this is a concrete warning. A robotics-specific pretrained generator is required.

### Unifying Planning and Control in a Single Model Is the Wrong Architecture

The dominant trend in the VLA community is to build ever-larger end-to-end models that handle both reasoning and action. ForeAct argues this is architecturally flawed for two compounding reasons: *"VLA models typically employ relatively small vision-language backbones (e.g., 3B parameters) to reduce latency, which limits their capacity for complex reasoning; and fine-tuning these models on robot data often leads to catastrophic forgetting, thereby compromising their general-purpose capabilities."* (Section 2). The alternative — a hierarchical system with a capable cloud-hosted planner and a lightweight edge-deployed VLA — is what ForeAct demonstrates, and the results support it.

### Spatial Text Prompts Are a Better Baseline Than Most Papers Admit

In an underreported ablation on the Pick_Tool task, the paper shows that simply replacing semantic instructions ("pick up the hammer") with spatial ones ("pick up the object on the bottom right") nearly doubled baseline performance — from 20.0% to 46.8% (Table 4). This is a quiet indictment of how VLA benchmarks are typically designed: many reported "language-conditioned" results may be bottlenecked not by motor capability but by semantic grounding. The paper's ForeAct still beats the spatial text baseline (93.4% vs. 46.8%), but the finding suggests the community may be misattributing failure modes.

---

## 3. Companies Identified

**Physical Intelligence (π.ai)**
The makers of π₀ and π₀.5, the base VLA models used throughout the paper as both a baseline and integration target. Their models are the primary platform ForeAct is validated on, which means this paper is simultaneously a critique of their baseline performance (46.5% on 11 tasks) and a demonstration that their architecture is extensible.
*"π₀: A 3.3B VLA model pretrained on over 10k hours of robot data."* (Section 4.3). *"Our method boosts the average success rate of the highly capable π₀.5 model from 70.3% to 88.2%."* (Table 2).

**NVIDIA**
Co-author institution; provided DGX compute for pretraining and co-developed the work. The deployment architecture uses an H100 for the cloud-hosted planner and an RTX 5090 for edge VLA inference. NVIDIA's involvement signals this is not purely academic — the cloud-edge deployment pattern maps directly onto their AI infrastructure stack.
*"Part of the work done during an internship at NVIDIA."* (Author affiliations). *"We thank NVIDIA for donating the DGX server."* (Acknowledgements).

**Galaxea Robotics**
The physical robot platform used for all real-world experiments is the Galaxea R1 Lite — a dual-arm mobile manipulator with 23 degrees of freedom. Their open-world dataset was also used for pretraining. This is a meaningful real-world validation signal for Galaxea's hardware.
*"We collect our real-world data on the Galaxea R1 Lite, a dual-arm mobile manipulator equipped with 23 degrees of freedom."* (Section 4.1).

**AgiBot**
Their AgiBot-World Colosseo dataset was a primary pretraining source.
*"We collect data from the AgiBot-World Colosseo, RoboMind, Galaxea Open-World, and Bridge datasets."* (Section 3.2).

**OpenAI**
GPT-Image-1 was tested as a candidate world model and failed the physics understanding test.
*"We evaluate several state-of-the-art image-editing models, including Gemini 2.5 Flash Image, GPT-Image, and Qwen-Edit."* (Section 4.2).

**Google DeepMind**
Gemini 2.5 Flash was tested as a candidate world model and failed; Gemini-3-pro-preview was used as an LLM judge for subtask evaluation.
*"State-of-the-art image-editing models lack an understanding of the underlying real-world physics and object dynamics."* (Section 4.2).

**Alibaba / Qwen Team**
Qwen3-VL-8B-Instruct is the VLM used for subtask planning and monitoring throughout the system. The paper evaluates multiple Qwen model sizes, finding that 8B is sufficient but 7B drops significantly.
*"In our visual foresight planner, we also employ Qwen-3-VL-8B-Instruct as the VLM for subtask planning and monitoring."* (Section 4.3).

---

## 4. People Identified

**Song Han**
MIT / NVIDIA. Principal investigator and corresponding author. Han is one of the most prominent figures in efficient deep learning (TinyML, quantization, neural architecture search). His involvement signals this paper's emphasis on *deployable* efficiency, not just benchmark performance. The use of SANA's architecture and the focus on 0.33s inference are consistent with his lab's core thesis.
*"Song Han, MIT, NVIDIA."* (Author affiliations).

**Zhuoyang Zhang & Shang Yang**
MIT (Han Lab). Equal-contribution first authors and the primary builders of the system. Both are graduate researchers in Han's lab with backgrounds in efficient generative models and robotics.
*"Equal Contribution."* (Author footnote).

**Qinghao Hu**
MIT / NVIDIA (intern). Contributed to the NVIDIA-side implementation and cloud deployment pipeline.
*"Part of the work done during an internship at NVIDIA."* (Author footnote).

**Yao Lu**
NVIDIA. Senior collaborator on the project representing NVIDIA Research's embodied AI efforts.
Listed as NVIDIA affiliation in the author list.

---

## 5. Operating Insights

### The Cloud-Edge Split Is the Right Deployment Architecture for Complex VLAs Today

The paper's production deployment runs the world model and VLM planner on a cloud H100, while the VLA policy runs locally on an RTX 5090. This is a deliberate architectural choice, not a limitation. *"We design a hierarchical cloud-edge deployment pipeline... the cloud server performs high-level planning and distills the result into a dual-guidance packet (textual, visual). This packet is then returned to the edge host, where the local VLA policy performs rapid inference."* (Section 3.5). For teams building commercial deployments, this is a practical template: you don't need to cram planning intelligence onto the robot — push it to cloud and pull back a 640×480 goal image. The 0.33s round-trip latency is acceptable for manipulation tasks that operate at multi-second subtask granularity.

### Data Collection Strategy Should Shift Toward Subtask-Level Episodes, Not Full Task Rollouts

ForeAct is trained at the subtask granularity — each training example is a (current frame, future frame, subtask instruction) triplet, not a full task trajectory. This decomposition, combined with visual goal conditioning, is what drives the 79% success rate at 20% data volume. *"Within each subtask, we sample condition frames at 1-second intervals. For each condition frame, we choose a future frame that comes half a subtask's length later in time."* (Section 3.2). For CTOs budgeting teleoperation data collection: structuring collection around atomic subtasks rather than full demonstrations will yield better return on investment per hour of human operator time.

---

## 6. Overlooked Insights

### The Pretraining Data Exclusion Criteria Are a Quiet Signal About Camera Quality Standards

The paper excluded Open-X-Embodiment and DROID — two of the largest public robot datasets — explicitly because of *"relatively low camera resolution."* (Section 3.2). This is buried in a single sentence, but it has real implications. As the industry invests heavily in data collection infrastructure, this paper implicitly sets a minimum bar: sub-640×480 camera data may be actively harmful or useless for training world models. Teams running data collection pipelines with low-resolution cameras are accumulating an asset that may be excluded from the next generation of training runs. The industry shift toward higher-resolution perception hardware has a concrete technical justification here, not just a marketing one.

### The VLM Size Threshold Is Surprisingly Accessible

The appendix evaluation of VLM planner performance across model sizes (Figure 13) reveals that Qwen3-VL-8B achieves competitive subtask planning accuracy — nearly matching Qwen2.5-VL-32B — while Qwen2.5-VL-7B drops significantly. This is a practically useful finding that doesn't appear in the main results. *"Both Qwen2.5-VL-32B and Qwen3-VL-8B achieve competitive performance, effectively steering the robot through complex tasks. Conversely, the significant performance drop observed with the smaller Qwen2.5-VL-7B model validates the discriminative nature of our benchmark."* (Section A.4). For teams designing inference stacks: an 8B VLM appears to be the current minimum viable planner for complex manipulation tasks. This has direct implications for cloud compute cost modeling — you likely don't need a 70B+ model in the planning loop.