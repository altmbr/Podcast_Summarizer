# OmniRetarget: Interaction-Preserving Data Generation for Humanoid Whole-Body Loco-Manipulation and Scene Interaction

**Podcast:** arXiv Physical AI Research
**Date:** 2026-03-26
**Processed:** 2026-03-26T09:04:16Z
**Participants:** Lujie Yang, Guanya Shi, et al. (arXiv Physical AI)
**Source:** paper
**arXiv:** 2509.26633
**PDF:** https://arxiv.org/pdf/2509.26633

---

# OmniRetarget: Interaction-Preserving Data Generation for Humanoid Whole-Body Loco-Manipulation

**TL;DR:** Amazon's robotics research arm has cracked one of the most frustrating bottlenecks in humanoid robot training — getting clean motion data that actually reflects how robots need to interact with objects and environments. The result: a robot that can carry a chair, use it as a step stool to climb a platform, jump off, and roll to absorb impact — all in one 30-second sequence, trained with minimal engineering overhead and deployed zero-shot to hardware.

---

## 1. Key Themes

### The Data Bottleneck Is the Core Problem in Humanoid RL — and OmniRetarget Directly Attacks It

The paper's central argument is that humanoid reinforcement learning has been held back not by RL algorithms, but by garbage-in-garbage-out data pipelines. Existing motion retargeting methods produce reference trajectories with artifacts — feet sliding, limbs penetrating objects, hands floating through boxes — that force engineers to compensate with increasingly complex reward functions. OmniRetarget's thesis: fix the data, and RL becomes trivially simple.

> "With suboptimal reference motions, practitioners are forced to either manually clean the data or re-introduce extensive reward engineering, such as ad-hoc regularizers for contact, slipping, and air time, to compensate for artifacts." (Section II-B)

The quantitative payoff is stark: OmniRetarget achieves **94.73% success rate on terrain interaction tasks** versus 52.63% for PHC, 78.94% for GMR, and 51.75% for VideoMimic — all using identical RL hyperparameters. (Table II, Section V-B)

### Interaction Preservation Is the Missing Ingredient Every Other Pipeline Ignores

Prior methods treat retargeting as a pure pose-matching problem: make the robot's joints look like the human's joints. OmniRetarget adds a fundamentally different constraint: preserve the *spatial relationships* between the robot, the objects it's manipulating, and the terrain it's traversing. This is the difference between a robot that looks like it's picking up a box and one that actually grips it correctly.

The technical mechanism is an **interaction mesh** — a volumetric structure built via Delaunay tetrahedralization that encodes the geometry of how body parts relate to objects and surfaces. Minimizing the deformation of this mesh across the human-to-robot translation preserves grasps, contact sequences, and terrain interactions that keypoint-matching approaches simply discard.

> "More importantly, common retargeting methods neglect the rich human-object and human-environment interactions essential for expressive locomotion and loco-manipulation." (Abstract)

> "Contact preservation is directly proportional to the success rate." (Section V-B)

### One Demonstration Becomes a Dataset: Scalable Augmentation Without Additional Human Labor

A single human motion capture recording can be automatically augmented into hundreds of kinematically-valid training trajectories covering different object positions, object shapes, platform heights, and even different robot embodiments (Unitree G1, H1, Booster T1). This directly attacks the teleoperation scaling problem that plagues humanoid data collection.

> "While existing methods require separate demonstrations for each variation—making data collection costly and limiting coverage—OmniRetarget addresses this bottleneck directly." (Section I)

Critically, augmented data generalizes to hardware: "Training and evaluating on the full augmented dataset achieves a **79.1% success rate**, comparable to 82.2% when evaluating on nominal motions only, showing that kinematics augmentation substantially enlarges coverage without significant performance degradation." (Section V-A)

### Minimal RL Formulation Becomes Sufficient When Reference Quality Is High

The paper demonstrates that the complexity of RL reward engineering is a *symptom* of bad reference data, not an inherent property of hard tasks. With clean references, the entire system trains with just **5 reward terms** and **4 domain randomization parameters**, with zero hyperparameter tuning beyond copying settings from a prior work (BeyondMimic).

> "Since OmniRetarget produces such artifact-free, interaction-preserving references, we can follow this minimal formulation directly, achieving faithful tracking of dynamic interactions and zero-shot sim-to-real transfer without any hyperparameter tuning." (Section IV)

Compare this to prior SOTA methods that require "random force injection, motor PD, action delay" and extensive contact/air-time reward terms. (Section IV)

### Zero-Shot Sim-to-Real on Agile, Long-Horizon Tasks Sets a New Capability Bar

The flagship demonstration — a 30-second sequence of chair-carrying, platform-climbing, jumping, and parkour-style rolling — represents a genuine capability milestone for humanoid hardware. The wall-flip result is equally notable: **5/5 success rate** on hardware, reaching peak angular velocity of 15 rad/s, completing the flip in ~0.5 seconds.

> "This 30-second, complex, multi-stage task highlights OmniRetarget's ability to produce precise and versatile reference motions, pushing the boundaries of what is possible for humanoids learning agile, human-like behaviors." (Section V-A)

---

## 2. Contrarian Perspectives

### More Reward Engineering Is a Sign of Failure, Not Sophistication

The conventional wisdom in humanoid RL is that complex, multi-term reward functions with carefully tuned coefficients are a marker of engineering rigor — you're teaching the robot exactly what good behavior looks like. This paper argues the opposite: reward complexity is a patch on broken data pipelines.

> "Prior works rely on many ad-hoc regularizers (e.g., foot flight and contact time) to compensate for artifacts in noisy references, but tuning these terms is tedious and fragile." (Section IV)

The evidence: policies trained on OmniRetarget data with 5 reward terms outperform policies trained on competitor pipelines with far more elaborate reward structures. VideoMimic — which uses a sophisticated soft-penalty optimization with many tunable λ parameters — achieves only **3.85% success rate on object manipulation tasks** versus OmniRetarget's **82.20%**. (Table II) The implication for teams building humanoid systems: if you're spending weeks tuning reward coefficients, audit your reference data first.

### Teleoperation Does Not Scale — Offline Retargeting Is the Real Path to Large-Scale Humanoid Data

Many leading humanoid companies (including those building whole-body teleoperation systems) are betting that teleoperation is the primary data flywheel. This paper argues that teleoperation hits fundamental walls that offline retargeting does not.

> "Teleoperation is difficult to scale: it's labor-intensive, prone to operator fatigue, and limited by the embodiment gap between human and robot kinematics. The lack of rich haptic feedback and difficulty stabilizing extreme motions (e.g., deep squats) further constrain its applicability." (Section II-C)

The augmentation results make the scaling math concrete: a *single* human demonstration, retargeted and augmented, produces a dataset covering diverse object shapes, positions, and terrain configurations — all kinematically valid and hardware-deployable. No operator hours required per variation.

### Soft Constraints Are Architecturally Broken for Interaction-Rich Tasks

VideoMimic's approach — using soft penalties on collision and contact rather than hard constraints — is representative of a broader design philosophy in the field: let the optimizer trade off competing objectives with tunable weights. OmniRetarget's results suggest this approach has a structural flaw for tasks involving physical contact.

> "Although this could be partially attributed to the tuning of its soft penalties, OmniRetarget demonstrates that a hard-constraint formulation avoids such sensitivities altogether." (Section V-B)

The specific failure mode: VideoMimic's collision avoidance cost *conflicts* with its keypoint matching cost, causing the optimizer to find compromises that satisfy neither well. Hard constraints eliminate this tension by making collision avoidance non-negotiable, forcing the optimizer to find solutions that are physically valid by construction.

---

## 3. Companies Identified

**Amazon (Amazon FAR — Frontier AI & Robotics)**
Lead institution for the paper. All co-leads are Amazon FAR team members, and multiple interns from MIT, UC Berkeley, Stanford, and CMU contributed. This positions Amazon as a serious player in humanoid whole-body control research infrastructure, not just logistics automation. The open-source release of code, datasets, and trained policies is a strategic move to establish platform influence.
> "All code, retargeted datasets, and trained policies will be publicly released." (Abstract)

**Unitree Robotics**
The Unitree G1 humanoid is the primary hardware platform for all sim-to-real validation in this paper. The G1's joint limits, collision model, and kinematic structure are directly integrated into OmniRetarget's constraint formulation. The paper also benchmarks against Unitree's publicly released LAFAN1 retargeting dataset.
> "Policies trained on our data reproduce a diverse range of expressive behaviors on a Unitree G1 humanoid, including natural box-carrying motions...dynamically climbing a 0.9m-high platform (70% of the robot's height), and crawling over slopes." (Section V-A)
> "We retarget motions from the LAFAN1 MoCap dataset and benchmark them against the publicly available Unitree LAFAN1 retargeted dataset, which is widely considered a high-quality data source for RL-based locomotion training." (Section V-B)

**Boston Dynamics**
Referenced explicitly as the inspiration for the flagship demonstration — the paper directly cites the Atlas tool-use demo as the benchmark of complex multi-stage manipulation the authors are targeting.
> "We present a long-horizon, dynamic sequence inspired by the Boston Dynamics Atlas tool-use demo." (Section V-A, citing [53])

**Booster Robotics**
The Booster T1 humanoid is listed alongside Unitree G1 and H1 as a supported robot embodiment in OmniRetarget's cross-embodiment retargeting capability. This is a notable signal that the framework is being validated against multiple commercial humanoid platforms.
> "Our interaction-mesh-based kinematic pipeline is highly general. It adapts to different robot embodiments, including the Unitree G1, H1, and Booster T1." (Section III-A)

**Reallusion (ActorCore)**
The wall-flip motion data was sourced from ActorCore's 3D motion library, demonstrating that commercial MoCap asset libraries can feed directly into OmniRetarget's pipeline — a practical data sourcing path for teams without in-house MoCap infrastructure.
> "The motion is acquired from https://actorcore.reallusion.com/3d-motion?asset=parkour-tic-tac-backflip." (Section V-A, footnote 1)

---

## 4. People Identified

**Lujie Yang** — MIT / Amazon FAR (intern), Equal co-first author. Yang also first-authored a prior paper on physics-driven data generation for contact-rich manipulation via trajectory optimization (reference [15]), suggesting deep expertise in the data generation pipeline problem. Likely a key architect of the constrained optimization formulation.

**Xiaoyu Huang** — UC Berkeley / Amazon FAR (intern), Equal co-first author. Based at UC Berkeley's robotics program, contributing to a line of work connecting motion imitation and physical humanoid deployment.

**Zhen Wu** — Amazon FAR (intern), Equal co-first author. Co-authored prior work on human-object interaction synthesis (reference [6] with C.K. Liu), bringing graphics-side interaction modeling expertise into the robotics pipeline.

**Angjoo Kanazawa** — UC Berkeley / Amazon FAR team co-lead. Kanazawa is a highly cited researcher in human body reconstruction from video and 3D human pose estimation. Her involvement connects computer vision-derived motion data (e.g., VideoMimic, which also involves her group) to the retargeting pipeline. Her presence on both VideoMimic and OmniRetarget is notable — she is actively pushing the boundary of video-to-robot motion transfer.

**Pieter Abbeel** — UC Berkeley / Amazon FAR team co-lead. One of the most influential figures in robot learning, Abbeel's involvement signals institutional commitment and likely accelerates adoption. His lab's prior work on DeepMimic (reference [4] with Peng) is a direct ancestor of this line of research.
> "DeepMimic shows that using human references yields natural, human-like behaviors with agile, dynamic motions." (Section II-B, citing [4])

**C. Karen Liu** — Stanford University / Amazon FAR team co-lead. Liu is a leading researcher in physics-based character animation and human motion synthesis. Her group produced the OMOMO dataset used in this paper, and her work on human-object interaction (reference [6]) directly informs OmniRetarget's interaction modeling approach. She is a central node connecting the computer graphics and robotics communities on this problem.

**Guanya Shi** — CMU / Amazon FAR team co-lead. Shi is the lead on ASAP (reference [13]), the sim-to-real alignment work for agile humanoid skills, and OmniH2O (reference [8]), the universal teleoperation and learning system. His portfolio suggests he is building a complete stack from data generation through sim-to-real transfer for humanoid whole-body control.
> "OmniH2O: Universal and dexterous human-to-humanoid whole-body teleoperation and learning." (Reference [8])

**Carmelo Sferrazza** — Amazon FAR team co-lead. Co-lead on this work; background connects to learning-based control for physical systems.

**Rocky Duan** — Amazon FAR team co-lead. Appears to be leading the Amazon FAR humanoid program alongside the academic co-leads.

---

## 5. Operating Insights

### Fix Your Reference Data Before Touching Your Reward Function

If your team is spending engineering cycles tuning reward coefficients for humanoid locomotion or manipulation tasks, OmniRetarget's results suggest you may be solving the wrong problem. The paper demonstrates that identical RL hyperparameters produce radically different outcomes (3.85% vs. 82.20% success) purely as a function of reference data quality. Before adding another reward term, audit whether your retargeting pipeline produces foot skating, penetration artifacts, or interaction breakdowns — these are the root causes of training instability.

> "A central observation from prior works is that the quality of retargeted motions strongly influences the performance of downstream RL." (Section V-B)

For CTOs: the implication is that your data engineering team may be more valuable than your reward engineering team for humanoid skill development.

### Build Augmentation Into Your Data Pipeline From Day One

The paper's augmentation results reveal a practical multiplier: one human demonstration, properly retargeted, can cover the full distribution of object placements, sizes, and terrain configurations needed for robust deployment. The alternative — collecting separate demonstrations for each variation, or relying on domain randomization alone — is demonstrably worse.

> "In comparison, relying solely on domain randomization—which perturbs object shapes and poses only during training—performs poorly under our RL formulation, as the policies struggle to explore far beyond the nominal reference." (Section V-A)

For engineering teams: the lesson is to architect your MoCap or motion data collection with augmentation in mind. You don't need exhaustive coverage at collection time if your retargeting pipeline can generate kinematically valid variations automatically. One clean demonstration of box-lifting is worth far more if you can systematically generate 50 variants covering different box positions, sizes, and approach angles.

---

## 6. Overlooked Insights

### The Proprioceptive-Only Observation Space Is a Deployment Signal, Not Just an Ablation

The paper trains policies that are **completely blind to object and scene information** — no cameras, no object pose estimation, no explicit terrain sensing. The robot navigates a 30-second multi-stage task relying only on joint positions/velocities, pelvis state, and reference trajectory tracking. This is buried in the methods section but has major deployment implications.

> "To show that high-quality reference motions provide a sufficient prior for complex tasks, we design a minimal proprioceptive observation space, as listed below, where the agent is blind to explicit scene and object information and must follow the reference trajectory precisely." (Section IV, Observations)

For operators: this means the trained policies do not require perception pipelines to execute. The robot is essentially running open-loop relative to scene state — it tracks the reference and uses proprioception to stay on it. This dramatically simplifies deployment (no calibrated cameras, no real-time object pose estimation) but also limits adaptability to unexpected object positions. The 79.1% success rate on augmented data suggests the coverage from augmentation partially compensates for the lack of perception — but this is a fundamental architectural choice teams need to understand before adopting the approach.

### The IMU Requirement for the Wall-Flip Reveals a Hardware Readiness Gap Across the Industry

The wall-flip motion requires an IMU capable of measuring angular rates above 15 rad/s. This is noted in a footnote but represents a non-trivial hardware constraint: many commercial humanoid platforms ship with IMUs that saturate well below this threshold. The paper demonstrates a policy that works, but deployment on hardware that can't sense its own motion state during the flip would fail silently.

> "An IMU capable of measuring angular rates above 15 rad/s is required for this motion." (Section V-A, footnote 1)

For investors and operators evaluating humanoid platforms: this is a concrete example of how sensor specifications — not just actuator performance or control algorithms — gate what skills are achievable. As the field pushes toward more agile, dynamic behaviors, the IMU specification becomes a meaningful differentiator in hardware selection. Teams planning to deploy parkour-class behaviors should audit their sensor stack before assuming that a published policy will transfer to their hardware.