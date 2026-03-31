# Coordinated Humanoid Manipulation with Choice Policies

**Podcast:** arXiv Physical AI Research
**Date:** 2026-03-31
**Processed:** 2026-03-31T09:04:19Z
**Participants:** Haozhi Qi, Jitendra Malik, et al. (arXiv Physical AI)
**Source:** paper
**arXiv:** 2512.25072
**PDF:** https://arxiv.org/pdf/2512.25072

---

# Coordinated Humanoid Manipulation with Choice Policies
### UC Berkeley | Qi, Wang, Lin, Yi, Ma, Sreenath, Malik | 2025

---

## 1. Key Themes

### Choice Policy Beats Diffusion Policy Without the Inference Tax

The central contribution is a new imitation learning architecture that generates K candidate action sequences in a single forward pass and uses a learned scorer to pick the best one. This "winner-takes-all" approach directly attacks the core trade-off haunting humanoid policy deployment: diffusion models are expressive but too slow; standard behavior cloning is fast but averages over multimodal data into garbage actions.

The results are stark. On dishwasher loading, the critical insertion sub-task (the hardest step) succeeded at:
- Diffusion Policy: 5/10 with hand-eye coordination
- Behavior Cloning: 5/10 with hand-eye coordination
- **Choice Policy: 7/10 with hand-eye coordination**

And for out-of-distribution position shifts, Choice Policy scored 4/10 on insertion while Diffusion Policy scored 0/10 and Behavior Cloning scored 2/10 (Table II). On the loco-manipulation wiping task, Diffusion Policy "could not be deployed because of slow inference and training instability" (Section V-B) — a telling real-world failure that benchmarks don't capture.

### Modular Teleoperation as a Data Flywheel

The paper's teleoperation system decomposes full humanoid control into four functional modules: arm end-effector tracking, hand grasps, head/eye tracking, and locomotion. The key insight is that modularity doesn't constrain the final policy — the learned policy is a unified neural network — but it dramatically lowers the cost and quality floor of data collection.

The practical payoff: "users typically required less than 10 minutes of practice before they could smoothly perform complex, long-horizon tasks" (Section III). The system runs on a 44-DoF robot (Fourier GR-1) and a 55-DoF robot (Robotera Star-1), collecting 100 demonstrations for dishwasher loading and 50 for whiteboard wiping — tiny datasets by foundation model standards, yet sufficient for real task execution.

### Head Orientation Is a Load-Bearing Component, Not an Afterthought

This is the most underappreciated finding in the paper. Without active hand-eye coordination, insertion success rates across ALL policy types collapsed to 1–2/10. With it, they jumped to 5–7/10. The paper states bluntly: "without adaptive head motion, all methods still succeed in pickup but struggle in later stages... success rates drop to nearly zero" during insertion (Section V-A). The fixed-head viewpoint causes occlusion that is physically irrecoverable regardless of how good your policy is. Head control is an infrastructure requirement, not a nice-to-have.

### Emergent Sub-Skill Specialization Without Explicit Decomposition

An unexpected finding from ablation visualizations: the K=5 proposal heads spontaneously specialized. "Choice ID 2 is consistently selected during the reaching and handover phases, while Choice ID 0 dominates the grasping stage... the network naturally decomposes the long-horizon task into distinct modes, where each head learns to represent a specific portion of the behavior" (Section V-A). This self-organized specialization emerged from a simple winner-takes-all training objective, with no explicit sub-task labeling or hierarchical architecture.

### Scoring Mechanism Is the Critical Differentiator

The ablation study (Table III) cleanly isolates what drives performance. Using the same K proposals but with random selection scored 3/10 on insertion. Averaging proposals scored 0/10. The best single fixed head scored 0/10 on insertion. The learned scorer brought that to 7/10. As the paper states: "these results confirm that the scoring mechanism is critical, as it allows the policy to adaptively select the most suitable proposal at each step" (Section V-A).

---

## 2. Contrarian Perspectives

### More Demonstrations Won't Solve Your Deployment Problem — Better Teleoperation Will

The prevailing industry logic is that scaling data collection (more hours, more operators, more variation) is the path to robust manipulation. This paper argues the opposite lever matters more: the quality and modularity of how data is collected in the first place. The system collects only 100 demonstrations for dishwasher loading and achieves real-world success — not because the dataset is large, but because the teleoperation interface produces clean, consistent, high-quality trajectories.

The paper explicitly attributes this to design: "on-demand activation is critical for collecting large-scale, precise demonstrations" and "simplifying hand movements into precision and power grasps... yields smoother and more reliable grasps" (Section III). The implication is that companies investing heavily in raw data volume without fixing teleoperation interface quality may be building on a flawed foundation.

### Diffusion Policy Is Not Production-Ready for Full Humanoids

Diffusion policies are widely treated as the state-of-the-art for expressive imitation learning, with major labs and companies (Physical Intelligence, etc.) building on them. This paper directly challenges their viability for full-body humanoid deployment. On the loco-manipulation task, the paper reports that diffusion policy "could not be deployed because of slow inference and training instability" (Section V-B).

This isn't a benchmark critique — it's a field deployment failure. A policy that can't run in real-time on a walking robot isn't a policy. The paper's Choice Policy runs in a single forward pass, making it compatible with the control loop requirements of a real bipedal system. The paper does acknowledge that optimizations exist, citing pi_0 as an example of trading responsiveness for smoothness, but frames these as workarounds rather than solutions (Section I).

### Behavioral Diversity in Demonstrations Is an Asset, Not Noise to Filter

Most data cleaning pipelines in robotics treat variation between operators as noise — something to normalize out or filter. Choice Policy inverts this: operator-to-operator variation is precisely what enables the policy to learn multimodal behaviors. The winner-takes-all training objective preserves this diversity by forcing different proposal heads to specialize on different behavioral modes.

"In teleoperation data, humans rarely repeat identical trajectories; therefore, multiple different actions may be valid for the same state. Naively minimizing MSE with a deterministic policy usually causes the model to average across these actions, often producing unrealistic or suboptimal behaviors" (Section IV-A). Companies homogenizing their demonstration data to reduce variance may be inadvertently eliminating the diversity that makes policies robust.

---

## 3. Companies Identified

**Fourier Intelligence (Fourier GR-1)**
Primary hardware platform for the main dishwasher loading experiments. The GR-1 is a full-sized 44-DoF humanoid with 32 actuated body motors plus two 6-motor Psyonic Ability Hands. Relevant because it serves as the validation platform for the core claims of the paper, including hand-eye coordination and Choice Policy performance. "We use the Fourier GR-1 and Robotera Star-1 as examples to demonstrate the generality of our method" (Section III).

**Robotera (Star-1)**
Secondary hardware platform demonstrating method generality. The Star-1 is a 55-DoF humanoid with dexterous XHands (12 actuated DoF each). Relevant as evidence that the teleoperation framework and policy architecture transfer across different hardware configurations, which matters for anyone evaluating platform-agnostic tooling.

**Psyonic**
Manufacturer of the Ability Hands mounted on the GR-1. Each hand has 6 motors. Relevant because dexterous hand hardware is a key bottleneck in manipulation tasks — the paper's simplification of hand control to power/precision grasps is partly a workaround for the difficulty of controlling high-DoF hands in real time. "Each Ability Hand has 6 motors" (Section III).

**Physical Intelligence (π₀)**
Referenced as a prior approach to fast diffusion inference. The paper characterizes their approach as involving "a trade-off between fast responsiveness and smooth motion" (Section I), positioning Choice Policy as a cleaner solution. Directly relevant as a competitive framing.

**Meta (via FAIR researchers)**
Jitendra Malik is a senior author and longtime FAIR/Berkeley figure. The paper's use of DINOv3 as a frozen visual encoder (Section IV-B) also connects to Meta's vision foundation model research lineage.

**NVIDIA (IsaacGym)**
Used as the simulation environment for training the RL locomotion policy: "The low-level controller is trained in IsaacGym" (Section VI-A). Relevant for anyone evaluating sim-to-real pipelines for humanoid locomotion.

---

## 4. People Identified

**Haozhi Qi**
UC Berkeley (equal first author). Focuses on dexterous manipulation and learning from demonstrations. Notable for bridging policy learning with real-world deployment constraints. Co-leads the core Choice Policy contribution.

**Yen-Jen Wang**
UC Berkeley (equal first author). Works on humanoid locomotion and whole-body control. Brings the locomotion integration expertise that makes the loco-manipulation experiments credible, not just simulated. Co-leads the teleoperation system design.

**Jitendra Malik**
UC Berkeley (co-advisor). One of the most cited researchers in computer vision and embodied AI. His presence signals this work sits at the intersection of perception and physical AI — not just control theory. His lab has produced foundational work in visual representation and robot learning.

**Koushil Sreenath**
UC Berkeley (co-advisor). Leads the Hybrid Robotics Lab, known for RL-based locomotion and dynamic control of legged robots. His involvement ensures the locomotion components are grounded in rigorous control theory, not just empirical hacks.

**Toru Lin and Brent Yi**
UC Berkeley contributors. Both are part of Berkeley's broader Physical AI research ecosystem, connected to prior work on dexterous manipulation (HATO, Simple Dexterous Manipulation).

---

## 5. Operating Insights

### Head Control Is a System Architecture Decision, Not a Sensor Choice

For any team building or deploying manipulation systems on humanoids, the data here is unambiguous: without active head/camera orientation tracking toward the active hand, long-horizon task performance collapses. Insertion success goes from ~70% to ~10–20% across all policy types (Table I). This means head actuation and head control policy need to be first-class citizens in your system architecture — not bolted on after the arms work. If your humanoid platform has a fixed or passively-controlled head, this paper is evidence that you have a structural ceiling on manipulation task success rates, regardless of how good your arm policy gets.

### Winner-Takes-All Training Is a Drop-in Upgrade for Existing BC Pipelines

The Choice Policy is architecturally simple — two MLPs on top of a shared feature encoder. The PyTorch pseudocode fits in ~15 lines (Figure 3). If you're already running behavior cloning with action chunking, this is a low-cost architectural modification that the paper shows materially improves performance on multimodal tasks, with zero inference overhead relative to standard BC. The 50-demo dataset for whiteboard wiping and 100-demo dataset for dishwasher loading suggest this isn't a data-hungry approach. CTOs evaluating policy architectures should treat this as a strong candidate for a default upgrade over vanilla BC, particularly for tasks with multiple valid execution strategies.

### Modularity in Data Collection Should Decouple from Policy Architecture

The paper makes a design choice that has broader implications: decompose teleoperation into sub-skills to make data collection tractable, but train a single end-to-end policy on the resulting data. "Although upper-body teleoperation is decomposed into modules, the final policy is a unified neural network that integrates all signals in a fully data-driven manner" (Section III). This resolves a false dilemma teams often face — whether to build modular policies (interpretable but brittle at interfaces) or monolithic policies (expressive but hard to collect data for). The answer here is: modular data collection infrastructure, unified learned policy.

---

## 6. Overlooked Insights

### Position Generalization Is a Harder Barrier Than Visual Generalization

The OOD evaluation (Table II) contains a finding that deserves more attention than it gets in the paper's framing. Color generalization (unseen plate color) degraded performance modestly — insertion went from 7/10 to 5/10 for Choice Policy, a manageable drop. But position generalization (plate placed slightly outside training range) was catastrophic — insertion dropped from 7/10 to 4/10 for Choice Policy, and to 0/10 for Diffusion Policy. The paper notes this briefly: "position shifts prove to be more challenging. All methods degrade significantly in the latter case" (Section V-A).

This has direct implications for deployment: visual domain randomization (color, texture, lighting) — the standard robustness investment — may be providing false confidence. Spatial distribution shift is the harder problem. Teams specifying training data collection should be systematically varying object positions and robot starting poses, not just visual appearances. The 10-trial sample sizes limit statistical confidence, but the directional signal is strong enough to warrant attention.

### 50 Demonstrations for Loco-Manipulation Is Both Impressive and a Warning Sign

The whiteboard wiping task uses only 50 demonstrations for a task requiring perception, grasping, locomotion, and whole-body adjustment. That's a remarkably small dataset, and the fact that any policy works at all is a signal about the quality of the teleoperation interface. However, the performance ceiling (Choice Policy: 2/5 on wiping, 2/5 on walking) reveals that 50 demonstrations is insufficient for reliable deployment. The paper frames this as a demonstration of system flexibility, but operators should read it as a calibration point: 50 demos gets you proof-of-concept on a novel task, not deployment-ready performance. The implicit question — how many demos are needed for, say, 80% end-to-end success on a 4-stage loco-manipulation task — remains unanswered, and is a critical unknown for anyone planning data collection budgets.