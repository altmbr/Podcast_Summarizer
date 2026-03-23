# Being-0: A Humanoid Robotic Agent with Vision-Language Models and Modular Skills

**Podcast:** Beijing Academy of Artificial Intelligence (BAAI) Research
**Date:** 2026-03-23
**Processed:** 2026-03-23T09:03:43Z
**Participants:** Haoqi Yuan, Zongqing Lu, et al. (Beijing Academy of Artificial Intelligence (BAAI))
**Source:** paper
**arXiv:** 2503.12533
**PDF:** https://arxiv.org/pdf/2503.12533

---

# Being-0: A Humanoid Robotic Agent with Vision-Language Models and Modular Skills

---

## 1. Key Themes

### The "Connector" Is the Real Innovation — Not the Foundation Model

The paper's central contribution is not using GPT-4o to control a robot (that's been tried before, and it fails). The real contribution is a lightweight, task-specific VLM called the **Connector** that sits between GPT-4o and the physical skill library. Without it, the system achieves 0% completion on three of five long-horizon tasks. With it, average completion jumps to 84.4%.

> "In the Fetch-bottle task, the baseline system (w/o Connector) achieves a score of 0.00, whereas the system with the Connector attains a remarkable score of 0.90. Similarly, tasks such as Deliver-basket and Prepare-coffee show substantial improvements, with performance increasing from 0.00 to 0.80 and 0.00 to 0.75, respectively." (Section 5.2, Table 1)

The practical implication: GPT-4o alone cannot navigate a humanoid robot through a real environment. It lacks the spatial grounding and inference speed. The Connector handles real-time embodied decisions at ~1 second per inference on onboard hardware, while GPT-4o handles only high-level planning from the cloud.

---

### 4.2× Speed Increase from Offloading Navigation Intelligence Onboard

One of the most deployment-relevant findings: running a large FM in the cloud as the sole navigation decision-maker produces a robot that moves at 2.3 cm/s and fails 100% of navigation trials. Adding the onboard Connector brings speed to 9.6 cm/s with a 5/5 success rate — a 4.2× improvement — while maintaining cloud FM for abstract reasoning.

> "Being-0 demonstrates notable advantages in efficiency... Being-0 with the Connector achieves a 4.2× increase in moving speed compared to the configuration without the Connector, along with a perfect success rate of 5/5. In contrast, the agent without the Connector consistently fails to reach the distant target." (Section 5.3, Table 4)

This is a direct argument for a hybrid cloud/edge architecture. The cloud FM is reserved for infrequent, high-level decisions; the onboard VLM handles the continuous, low-latency loop.

---

### Active Vision Is a Non-Negotiable Hardware Requirement

No fixed camera angle works for both navigation and manipulation. A downward-tilted camera (high pitch) enables grasping but blinds the robot during navigation. An upward-tilted camera enables navigation but results in 0/5 grasp success. Only the active, motorized neck camera achieves 5/5 across all task types.

> "No fixed camera configuration achieves high success rates for both navigation and manipulation tasks. In comparison, Being-0 with an active camera consistently achieves perfect success rates across all tasks." (Section 5.3, Table 3)

For teams designing humanoid hardware or selecting platforms, this is a concrete system-level requirement, not a nice-to-have. Fixed-camera humanoid designs will hit a ceiling at the navigation-to-manipulation transition.

---

### Skill Libraries Can Be Scaled at Low Cost with Teleoperation

The manipulation skill library is built using Apple Vision Pro teleoperation with 50–200 demonstration trajectories per skill, requiring under one hour of teleoperation per new capability. This is a deployable data flywheel — not a research artifact.

> "This approach ensures scalability of the skill library, as a new skill can be acquired with 50∼150 trajectories, requiring less than 1 hour of teleoperation." (Section 3.1)

The same framework extends to dexterous hands with tactile sensors (demonstrated on a chess-playing task at 0.90 success rate), suggesting the architecture doesn't hit a wall as manipulation complexity increases.

---

### Navigation Termination Pose Is a Hidden Failure Mode

The paper identifies and quantifies a problem that most teams deploying nav+manipulation systems underestimate: even when navigation succeeds, the robot's final standing position often makes the subsequent manipulation skill impossible to execute. The Connector's pose adjustment module, which approaches targets on an arc rather than head-on, doubles or quadruples grasp success rates post-navigation.

> "For grasping tasks, such as Grasp-bottle and Grasp-coffee, Being-0 with adjustment significantly outperforms the ablation baseline, achieving success rate gains of over 0.4... Without adjustment, the robot may stop too far from the object or position the object behind the grasping hand, causing the subsequent grasping skill to fail." (Section 5.3, Table 2)

---

## 2. Contrarian Perspectives

### End-to-End VLA Models Are Not the Right Architecture for Humanoid Long-Horizon Tasks — Yet

The dominant industry trend is toward monolithic Vision-Language-Action (VLA) models (RT-2, OpenVLA, π₀) that handle perception, planning, and action in a single model. Being-0 argues the opposite: modular hierarchies outperform end-to-end approaches for full-sized humanoids in complex environments, because no large-scale humanoid-specific dataset exists to train a capable VLA.

> "While these methods have shown promise for robot arms with grippers, the lack of large-scale datasets for humanoid robots — particularly those with dexterous hands and active cameras — remains a significant barrier to developing FMs for humanoid robots." (Section 6, Related Work)

The evidence is operational: Being-0 achieves 84.4% average completion on multi-step real-world tasks on a full-sized humanoid today, using modular architecture and a few hundred teleoperation trajectories per skill — a bar that no published end-to-end VLA has cleared on comparable humanoid hardware.

---

### Whole-Body Control Policies Are Premature for Task Diversity

The current academic consensus is moving toward unified whole-body control policies that simultaneously manage locomotion and manipulation with a single neural network. Being-0 explicitly rejects this approach for practical deployment.

> "For most tasks, we observe that the lower body and upper body serve distinct functionalities: the lower body is primarily used for navigation, while the upper body is used for manipulation... This observation motivates us to develop separate skills for stable lower-body locomotion and upper-body manipulation." (Section 3.1)

The practical argument: whole-body policies have not yet demonstrated "a wide range of manipulation skills due to the complexity of achieving precise manipulation, stable locomotion, and sim-to-real deployment with one policy" (Section 3.1). Separating these domains allows each to be optimized independently and new skills to be added incrementally, without retraining the entire system.

---

### GPT-4o Is Actively Harmful as a Low-Level Robot Controller

The prevailing assumption in many robotics-AI integrations is that more capable frontier models are always better. Being-0 provides direct empirical evidence to the contrary for embodied, real-time control.

> "Existing FMs, including GPT-4o, struggle with accurate 3D scene understanding, often failing to estimate the direction and depth of navigation targets correctly, which can lead to incorrect skill plans... GPT-4o alone frequently makes errors in planning locomotion directions, leading to inefficient or incorrect navigation paths." (Sections 1 and 5.3)

The implication for teams building humanoid software stacks: frontier LLMs should be treated as strategic planners, not reactive controllers. Investing in a fast, domain-specialized intermediate model — even a small fine-tuned VLM — yields larger performance gains than upgrading the FM.

---

## 3. Companies Identified

**Unitree Robotics**
- Description: Chinese humanoid and quadruped robot manufacturer
- Why relevant: Being-0 is deployed and tested on the Unitree H1-2 full-sized humanoid robot as the primary hardware platform. All real-world experiments use this hardware.
- Quote: "We conduct experiments on a Unitree H1-2 humanoid robot equipped with two Inspire hands for manipulation, two Dynamixel motors for neck movement, and a ZED-mini camera mounted on the neck for active vision." (Section 5.1)

---

**Inspire Robotics**
- Description: Manufacturer of multi-fingered dexterous robotic hands
- Why relevant: Being-0 uses Inspire dexterous hands as the end-effector hardware, enabling the complex manipulation skills (grasping, coffee machine operation, chess piece manipulation) demonstrated in the paper
- Quote: "We conduct experiments on a Unitree H1-2 humanoid robot equipped with two Inspire hands for manipulation." (Section 5.1)

---

**NVIDIA**
- Description: GPU and edge computing hardware manufacturer
- Why relevant: The onboard computation platform enabling real-time Connector inference is the NVIDIA Jetson AGX. This is the hardware constraint that shapes the entire edge/cloud deployment split.
- Quote: "The NVIDIA Jetson AGX onboard device is used to deploy the Connector and all modular skills." (Section 5.1)

---

**Apple**
- Description: Consumer technology company
- Why relevant: Apple Vision Pro is used as the teleoperation interface for collecting all manipulation training data. This makes it a core data collection tool in the Being-0 pipeline, directly affecting the quality and diversity of the skill library.
- Quote: "To collect high-quality, human-like manipulation data for the humanoid equipped with two dexterous hands and active vision, we use Apple VisionPro for teleoperation." (Section 3.1)

---

**OpenAI**
- Description: AI research company, developer of GPT-4o
- Why relevant: GPT-4o serves as the Foundation Model (high-level planner) in Being-0. The paper also explicitly documents GPT-4o's failure modes in embodied contexts — limited 3D spatial understanding and insufficient inference speed — which has competitive implications for OpenAI's robotics ambitions.
- Quote: "Existing FMs, such as GPT-4o, suffer from limitations in inference efficiency and embodied scene understanding, making humanoid agents less reactive and robust during the alternating phases of navigation and manipulation in long-horizon tasks." (Section 1)

---

**Stereolabs (ZED)**
- Description: Manufacturer of stereoscopic depth cameras
- Why relevant: The ZED-mini camera is the active vision system mounted on the robot's motorized neck, providing the binocular RGB input that powers both navigation and manipulation. The active camera is shown to be essential for task success.
- Quote: "A ZED-mini camera mounted on the neck for active vision." (Section 5.1)

---

**Dynamixel (ROBOTIS)**
- Description: Manufacturer of smart servo actuators
- Why relevant: Dynamixel motors drive the robot's active neck, enabling the pan/tilt movements that the ablation study proves are essential for bridging navigation and manipulation performance.
- Quote: "Two Dynamixel motors for neck movement." (Section 5.1)

---

## 4. People Identified

**Haoqi Yuan**
- Lab/Institution: Peking University / Beijing Academy of Artificial Intelligence (BAAI)
- Why notable: Lead author of Being-0. Also co-author of related work on cross-embodiment dexterous grasping (Yuan et al., 2024) and RL-GPT (Liu et al., 2024b), indicating a sustained research focus on connecting foundation models with physical manipulation. A researcher to watch in the humanoid agent space.
- Quote: Correspondence and lead authorship on Being-0; cited for prior work on "Cross-embodiment dexterous grasping with reinforcement learning" (References)

---

**Zongqing Lu**
- Lab/Institution: Peking University / BeingBeyond
- Why notable: Corresponding author and likely lab PI. Affiliated with BeingBeyond, suggesting direct commercialization intent behind this research. Overseeing a portfolio of humanoid manipulation research (Yuan et al., Zhou et al., Huang et al. all cite this group).
- Quote: "Correspondence to: Zongqing Lu <zongqing.lu@pku.edu.cn>." (Author affiliations)

---

**Börje F. Karlsson**
- Lab/Institution: Beijing Academy of Artificial Intelligence (BAAI)
- Why notable: Senior BAAI researcher on the team, bridging the academic research with BAAI's institutional mandate to advance Chinese AI infrastructure. BAAI's involvement signals state-level interest in humanoid agent development.
- Quote: Listed as co-author from BAAI affiliation (Author list)

---

**Xuxin Cheng (referenced, not author)**
- Lab/Institution: Referenced work from UC Berkeley / CMU groups
- Why notable: The paper heavily relies on Cheng et al.'s Open-Television teleoperation framework (Cheng et al., 2024b) for data collection, and cites the expressive whole-body control work (Cheng et al., 2024a). Cheng's teleoperation infrastructure is effectively a dependency of Being-0's data pipeline.
- Quote: "To collect high-quality, human-like manipulation data for the humanoid equipped with two dexterous hands and active vision, we use Apple VisionPro for teleoperation, following recent work Cheng et al. (2024b)." (Section 3.1)

---

## 5. Operating Insights

### The Edge/Cloud Split Is the Deployment Architecture Decision That Determines System Viability

Being-0's architecture makes a concrete, tested claim about how to deploy humanoid AI systems: only the high-level FM runs on the cloud; everything else — the Connector VLM, locomotion policy, and all manipulation skills — runs on an NVIDIA Jetson AGX onboard. This isn't a theoretical architecture preference; it's the configuration that produces the 4.2× speed improvement and enables real-time task execution.

> "With all components, except the FM, deployable on low-cost onboard computation devices, Being-0 achieves efficient, real-time performance on a full-sized humanoid robot." (Abstract)

For CTOs and heads of engineering: any humanoid system that routes low-level control decisions through cloud inference will face latency and reliability problems in real environments. The design principle is to push everything time-critical to the edge and use cloud FM only for infrequent, high-level replanning. The Jetson AGX (~$1,500 MSRP) is sufficient for the Connector and all skill policies — this constrains the VLM size and informs hardware BOM planning.

---

### Navigation-to-Manipulation Handoff Requires Explicit State Management — Plan for It From Day One

The paper identifies and solves a failure mode that is almost certainly present in any system combining mobile navigation with stationary manipulation: the robot arrives at the correct location but in the wrong body pose to execute the next skill. This isn't a fringe edge case — without the pose adjustment module, grasp success rates drop from 4/5 to 1/5 for precision tasks like placing a cup on a coffee machine (0/5 without adjustment).

> "For Place-coffee (m), which requires placing the cup on a coffee machine with a very small available area, Being-0 with adjustment performs significantly better [3/5 vs. 0/5]." (Section 5.3, Table 2)

For engineering teams: the handoff between navigation and manipulation must be treated as a distinct system state with its own success criteria — not just "did the robot arrive?" but "did the robot arrive in a pose that makes the next skill executable?" This requires the navigation policy to know about downstream manipulation constraints, which in Being-0 is handled by the Connector predicting optimal alignment direction during the final approach. Budget engineering time for this; it is not automatically solved by improving either navigation or manipulation in isolation.

---

### New Skills Can Be Added in Under an Hour — Exploit This for Rapid Customer-Specific Customization

The ACT-based manipulation skill acquisition pipeline requires 50–200 human teleoperation demonstrations per skill and less than one hour of data collection. This is a commercially significant number: it means a deployment team can add a customer-specific skill (e.g., "operate this specific machine," "handle this specific product") in a single working session.

> "This approach ensures scalability of the skill library, as a new skill can be acquired with 50∼150 trajectories, requiring less than 1 hour of teleoperation." (Section 3.1)

The skill library in Being-0 spans grasping, bimanual tasks, coffee machine operation, basket handling, and fine manipulation (chess pieces) — all acquired through the same pipeline. For operators building humanoid deployment businesses, this is the unit economics lever: the marginal cost of a new skill is measured in hours of operator time, not months of engineering.

---

## 6. Overlooked Insights

### The Training Dataset Is Tiny by AI Standards — And That's a Warning About Generalization

The Connector VLM is trained on 3,177 images collected from a single office environment, with bounding box annotations across only 19 spatial categories and yes/no labels across 18 object categories. The system works impressively within that environment, but the dataset scope is narrow enough that generalization to different building layouts, lighting conditions, or object categories is an open question — not a solved one.

> "Our dataset consists of two major types of tasks: Visual Understanding (VLU) tasks and Action Planning (AP) tasks. We collected a total of 3,177 images, with 2,483 images dedicated to visual understanding tasks and 694 images for action planning tasks." (Appendix B.2.1, Table 11)

The robustness results show a 20% drop in navigation success when moving to "in-room with obstacles" (1.0 → 0.80) and a further drop for cross-room navigation (0.83), both tested in the same building. The manipulation skills show 20–37% degradation on unseen objects. For investors evaluating Being-0 or comparable systems: the gap between a working lab demo and a generalizable deployable product is not primarily in the agent architecture — it's in the scale and diversity of the training data for the Connector. Any company claiming to have solved this should be asked about their data collection scope and cross-environment validation methodology.

---

### The System Has No Complex Locomotion — Stairs, Ramps, and Uneven Floors Are Out of Scope

Being-0 is explicitly limited to flat-ground operation, and the authors acknowledge this openly. The locomotion policy handles forward/backward/lateral movement and turning, but excludes crouching, stair climbing, seated operation, and height-varying manipulation. For a paper about a "full-sized humanoid," this is a significant operational constraint that limits near-term deployment venues to flat, open office or warehouse environments.

> "The current system does not incorporate complex locomotion skills such as crouching, sitting, or jumping. These skills could extend the humanoid's functionality beyond flat-ground settings, enabling tasks like climbing stairs, working from seated positions, or manipulating objects at varying heights." (Section 7, Conclusion and Limitations)

This is a direct signal for investors: the current competitive moat in humanoid agents is being built on flat-ground, structured indoor environments. Any deployment scenario involving stairs, ramps, uneven surfaces, or outdoor terrain requires a different locomotion stack — and the modular architecture of Being-0 would require a new locomotion skill tier, not just a software update. Teams betting on humanoids for manufacturing or warehousing should map their target environments against these constraints explicitly before committing to a platform.