# Xiaomi-Robotics-0: An Open-Sourced Vision-Language-Action Model with Real-Time Execution

**Podcast:** arXiv Physical AI Research
**Date:** 2026-04-02
**Processed:** 2026-04-02T09:03:28Z
**Participants:** Ruisi Cai, Quan Zhou, et al. (arXiv Physical AI)
**Source:** paper
**arXiv:** 2602.12684
**PDF:** https://arxiv.org/pdf/2602.12684

---

# Xiaomi-Robotics-0: Real-Time VLA Execution on Consumer Hardware

## Why This Paper Matters in 10 Seconds

Xiaomi just open-sourced a state-of-the-art robot brain that runs on a $1,500 GPU, beats Physical Intelligence's π0.5 on throughput for dexterous bimanual tasks, and doesn't forget how to see and reason while learning to act. For anyone building or funding deployable robot systems, this is a meaningful capability threshold being crossed — and given away for free.

---

## 1. Key Themes

### State-of-the-Art Performance Achieved on a Consumer GPU

The headline result isn't just benchmark scores — it's that those scores are achieved at **80ms inference latency on an NVIDIA GeForce RTX 4090**. This is a $1,500-2,000 consumer card, not a data center GPU cluster. The paper reports: *"Deployed on an NVIDIA GeForce RTX 4090 GPU, the model achieves an inference latency of t_inf = 80ms"* (Section 2.3). On simulation benchmarks, the model hits 98.7% average success on LIBERO, 4.80 average task length on CALVIN ABCD→D (vs. previous best of 4.67), and 85.5% on SimplerEnv Visual Matching — all state-of-the-art at time of publication (Tables 1, 2, 5). The practical implication: the compute cost to run a frontier-class VLA policy is now within reach of small teams, startups, and even individual developers.

### Solving the "Jerky Robot" Problem with a New Training Trick

One of the most frustrating deployment realities for VLA models is that inference takes time, so the robot either freezes mid-task (synchronous) or moves erratically when stitching together action chunks (asynchronous). Prior solutions like Training RTC (from Physical Intelligence) helped with continuity but introduced a new failure mode: the model learns to lazily copy previous actions rather than actually perceive the environment. The paper describes this explicitly: *"policy learning may take a shortcut by simply copying the action prefix instead of attending to the visual and language inputs, leading to less reactive policies and degraded performance"* (Section 2.2.2). Xiaomi's fix — a Λ-shape attention mask that allows smooth transitions at chunk boundaries but forces later-timestep predictions to attend to vision and language, not just prior actions — is a clean architectural solution to a real deployment problem. The result in towel folding was concrete: Training RTC *"often gets stuck when it inadvertently grasps multiple layers of the towel... Rather than re-grasping to correct this, the policy falls into a repetitive loop"* (Section 3.2.3), while Xiaomi-Robotics-0 recovered correctly.

### Catastrophic Forgetting Is Now a Solved Problem (With the Right Recipe)

Training robots on manipulation data typically destroys the model's ability to reason about the visual world in general — a phenomenon called catastrophic forgetting. Xiaomi's two-stage pre-training approach (jointly training VLM on robot trajectories + vision-language data, then freezing the VLM while training the diffusion action head) nearly eliminates this degradation. As shown in Table 3, π0 scores near **zero** on every vision-language benchmark after training. Xiaomi-Robotics-0 tracks its base VLM (Qwen3-VL-4B) within a few percentage points across 10 benchmarks, and actually **surpasses** it on the ERQA embodied reasoning benchmark: *"Xiaomi-Robotics-0 slightly surpasses Qwen3-VL-4B-Instruct on the ERQA benchmark (40.8 vs. 40.0)"* (Section 3.3). For anyone building robots that need to understand natural language instructions, adapt to novel scenarios, or interface with human operators — this matters enormously.

### 738 Hours of In-House Bimanual Data as a Competitive Moat

The model is trained on approximately 200M timesteps of robot trajectory data (Section 2.1). Of this, Xiaomi contributed 338 hours of Lego Disassembly and 400 hours of Towel Folding teleoperation data — **738 hours of in-house bimanual dexterous manipulation data** on top of open datasets like DROID and MolmoAct. This is not a model fine-tuned on someone else's data. Xiaomi built a serious data collection operation, and the tasks chosen (Lego disassembly requiring millimeter-precise grasps under contact forces, towel folding requiring deformable object dynamics) are exactly the kind of high-contact, high-dexterity tasks that separate real-world capable systems from benchmark-optimized ones.

### Open-Source Release Creates Immediate Industry Pressure

Unlike many frontier robot learning papers, this one ships code and model weights: *"We release the pre-trained and post-trained checkpoints, along with the inference code to facilitate future research"* (Section 5, Abstract). This means any team can fine-tune from Xiaomi's pre-trained checkpoint rather than starting from scratch — dramatically lowering the barrier for new entrants and compressing the time-to-capable-robot for companies that don't have the resources to run 200M-timestep pre-training runs.

---

## 2. Contrarian Perspectives

### Bigger Models Are Not the Answer to Real-Time Execution — Better Training Recipes Are

The dominant assumption in robot foundation models is that inference speed is primarily a hardware or model-size problem: you either need better accelerators, quantization, or a smaller model. Xiaomi challenges this directly. Their 4.7B parameter model achieves 80ms latency not by aggressive compression, but through a carefully designed asynchronous execution training protocol that teaches the model to *operate correctly* under latency rather than trying to eliminate the latency. The paper positions this as the central contribution: *"The key to our method lies in a carefully designed training recipe and deployment strategy"* (Abstract). The implication for product teams: before buying more compute or shrinking your model, ask whether your training procedure is actually preparing the model for the asynchronous reality of real robot deployment.

### Preserving Vision-Language Capabilities Is Not Optional — It's Architecturally Necessary

Most VLA papers treat the vision-language understanding of the underlying model as a nice-to-have that degrades gracefully. The Xiaomi data suggests this is wrong — and the degradation is catastrophic, not graceful. Table 3 shows that π0.5 (Physical Intelligence's latest model, which *does* incorporate VL data during training) still scores **0.0 on ERQA, POPE, and TextVQA**, and near-zero on MME. π0 scores near zero across the board. A model that has forgotten how to reason visually cannot be expected to generalize to novel environments, follow complex language instructions, or recover from unexpected states. Xiaomi's co-training approach (VL data mixed 1:6 with robot trajectory data throughout pre-training, Section 2.2.1) is the mechanism that preserves this capability — and the results suggest it should be considered a baseline requirement, not an optimization.

### Throughput, Not Success Rate, Is the Metric That Determines Commercial Viability

The paper introduces a framing that most academic robot learning work ignores entirely: **throughput** (tasks completed per unit time), not just success rate. In Lego Disassembly, the synchronous Xiaomi variant and π0.5 achieve comparable success rates, but Xiaomi-Robotics-0's asynchronous execution delivers meaningfully higher throughput. For Towel Folding, all synchronous methods plateau at 1 piece/minute, while Xiaomi-Robotics-0 achieves **1.2 pieces/minute** — a 20% throughput improvement that compounds across an entire operational day (Section 3.2.3, Figure 6c). In any commercial deployment — warehouse, laundry, assembly — this difference is the difference between a profitable and unprofitable operation. The field's fixation on success rate as the primary metric is actively misleading for deployment decisions.

---

## 3. Companies Identified

**Xiaomi**
- Description: Chinese consumer electronics giant (smartphones, smart home), now building humanoid robots (CyberOne) and robot software
- Why relevant: This is Xiaomi's first major open-source robot foundation model release, signaling serious investment in Physical AI as a strategic priority. The open-source release is notable — Xiaomi appears to be competing for developer mindshare and talent, not just product differentiation.
- Quote: *"To facilitate future research, code and model checkpoints are open-sourced at https://xiaomi-robotics-0.github.io"* (Abstract)

**Physical Intelligence (π)**
- Description: Robot foundation model startup backed by Bezos, Google, Tiger Global; creators of π0 and π0.5
- Why relevant: Directly benchmarked against. Xiaomi's model outperforms π0.5 on throughput for both real-robot tasks, and π0.5 scores near-zero on nearly all vision-language benchmarks. The Training RTC technique (from Physical Intelligence's Black et al. 2025b) is used as a baseline and shown to produce "repetitive loop" failure modes that Xiaomi's approach addresses.
- Quote: *"In terms of throughput, Xiaomi-Robotics-0 achieves the highest throughput among all methods, surpassing the training RTC variant which is also deployed asynchronously"* (Section 3.2.3)

**NVIDIA**
- Description: GPU manufacturer; GR00T N1 humanoid robot foundation model team
- Why relevant: Two touchpoints. First, the RTX 4090 consumer GPU is the deployment hardware, making NVIDIA's consumer product line relevant infrastructure for robot AI. Second, GR00T-N1 is a direct benchmark comparison (achieving 93.9% on LIBERO vs. Xiaomi's 98.7%).
- Quote: *"Deployed on an NVIDIA GeForce RTX 4090 GPU, the model achieves an inference latency of t_inf = 80ms"* (Section 2.3); GR00T-N1 results in Table 1

**Alibaba / Qwen Team**
- Description: The underlying VLM backbone (Qwen3-VL-4B-Instruct) is from Alibaba's Qwen team
- Why relevant: Xiaomi builds on Alibaba's open-source VLM — the choice of base model matters because Xiaomi's pre-training specifically preserves Qwen3-VL's capabilities. This creates an implicit dependency and suggests that improvements to the Qwen3-VL base will directly benefit Xiaomi-Robotics-0 downstream fine-tuners.
- Quote: *"Xiaomi-Robotics-0 adopts a mixture-of-transformers (MoT) model architecture. It consists of a pre-trained vision-language model (VLM) (i.e., Qwen3-VL-4B-Instruct)"* (Section 2.2)

**Stanford / DROID Dataset Team**
- Description: Academic consortium that produced the DROID large-scale in-the-wild robot manipulation dataset
- Why relevant: DROID is one of the primary open-source datasets used in pre-training, alongside MolmoAct. The quality and diversity of open robot datasets directly gates what pre-trained checkpoints like this one can achieve.
- Quote: *"Our robot trajectory data are sourced from multiple open-sourced robot datasets (e.g., DROID and MolmoAct) as well as in-house data collected by ourselves"* (Section 2.1)

---

## 4. People Identified

**Kevin Black** — UC Berkeley / Physical Intelligence
- Why notable: Lead author on both the Real-Time Chunking (RTC) paper and the Training RTC paper that Xiaomi directly builds on and critiques. Also lead author of π0 and co-author of π0.5. Black is arguably the most cited individual in the asynchronous VLA execution literature, and his work is the technical foil against which Xiaomi defines its contribution.
- Quote: Referenced as [4] (RTC) and [5] (Training RTC) throughout Section 2.2.2 and Section 4; π0 [3] and π0.5 [19] are primary baselines throughout

**Sergey Levine** — UC Berkeley
- Why notable: Appears as co-author on both RTC papers and as a foundational figure in the broader robot learning ecosystem referenced throughout. His lab's work (DROID, Octo, RTC) forms much of the technical infrastructure this paper builds on.
- Quote: Co-author on Black et al. [2025a] and [2025b], cited extensively in Sections 2.2.2 and 4

**Chelsea Finn** — Stanford / Physical Intelligence
- Why notable: Co-author on π0, π0.5, and OpenVLA — three of the four primary VLA baselines benchmarked in this paper. Her presence across multiple competing systems makes her a central node in the VLA competitive landscape.
- Quote: Co-author on π0 [3], π0.5 [19], and OpenVLA [24], all appearing in Tables 1-5

**Haozhi Qi et al. (Choice Policies team)** — UC Berkeley
- Why notable: The Choice Policies paper [51] is directly incorporated into Xiaomi's pre-training architecture for handling multimodal trajectory distributions. This is a non-obvious architectural decision that distinguishes Xiaomi's approach from simpler action prediction methods.
- Quote: *"To account for the multi-modality in trajectories, we adopt Choice Policies for action prediction"* (Section 2.2.1)

---

## 5. Operating Insights

### The 80ms Latency Threshold on a $1,500 GPU Is a Deployment Unlock

The combination of 80ms inference latency and consumer-grade GPU deployment changes the economics of robot AI at the unit level. Previously, running a frontier VLA model required either (a) expensive compute infrastructure per robot, or (b) accepting frozen/jerky motion from synchronous execution. Xiaomi demonstrates that with the right training protocol, a 4.7B parameter model can run smoothly on an RTX 4090 at 30Hz action execution. For anyone designing robot compute stacks today: *"Deployed on an NVIDIA GeForce RTX 4090 GPU, the model achieves an inference latency of t_inf = 80ms"* (Section 2.3). This should recalibrate your hardware budget assumptions and competitive analysis for any company selling or deploying robot compute.

### Fine-Tune From This Checkpoint, Don't Pre-Train From Scratch

The open release of pre-trained checkpoints trained on 200M timesteps of cross-embodiment data, combined with preserved vision-language capabilities, means any team with a specific robot platform and task can now start from a genuinely strong initialization rather than fine-tuning from a general-purpose LLM or training from scratch. The paper explicitly frames this as the intent: *"We hope these resources serve as a practical foundation for advancing vision-language-action (VLA) models"* (Section 1). For a robotics startup with limited compute budget, the build-vs-borrow calculus just shifted significantly. The pre-training alone required 40k steps at batch size 32,768 across a dataset of ~200M timesteps (Section 3.2.2) — this is not a run most teams can replicate.

### Measure Throughput, Not Just Success Rate, Before Committing to a Policy Architecture

The paper's real-world evaluation framework — continuous 30-minute rollouts measuring pieces/minute, not just per-trial success rates — reveals capability gaps that benchmark success rates hide entirely. π0.5 and the synchronous Xiaomi variant have similar success rates to Xiaomi-Robotics-0 on Lego Disassembly, but lower throughput. On Towel Folding, the throughput gap (1.0 vs. 1.2 pcs/min) is invisible in success rate metrics. *"For Towel Folding, π0.5, Xiaomi-Robotics-0 (Sync), and Xiaomi-Robotics-0 (Training RTC) achieve comparable throughputs of 1 pcs/min. Xiaomi-Robotics-0 outperforms these three methods, achieving a throughput of 1.2 pcs/min"* (Section 3.2.3). If you're evaluating a policy for production deployment, run continuous timed rollouts, not episodic trials.

---

## 6. Overlooked Insights

### The Λ-Mask Failure Mode Reveals a Systemic Risk in Action-Prefix Conditioning

The Training RTC failure on towel folding — where the model gets stuck in a repetitive loop rather than correcting a grasp error — is more than a benchmark result. It reveals a fundamental risk in any architecture that conditions future action generation on committed past actions: the model can learn to ignore sensory input and just replay previous actions. This is a degenerate solution that passes offline training metrics (since consecutive actions are indeed temporally correlated in training data) but fails catastrophically under distribution shift. The paper's description is worth quoting in full: *"The Training RTC variant often gets stuck when it inadvertently grasps multiple layers of the towel during the flinging motion, preventing the motion from flattening the towel. Rather than re-grasping to correct this, the policy falls into a repetitive loop, repeatedly executing the flinging motion. This observation suggests that the action-prefixing mechanism introduces a shortcut in policy learning"* (Section 3.2.3). Any team using action-prefix conditioning (a common technique) should audit whether their training data and evaluation protocol can detect this failure mode before deployment.

### 738 Hours of Proprietary Bimanual Data May Be the Real Competitive Asset

The paper buries a data point that deserves more attention: Xiaomi collected **738 total hours** of teleoperated bimanual manipulation data (338 hours for Lego Disassembly, 400 hours for Towel Folding) as in-house data on top of public datasets (Section 2.1). For context, the DROID dataset — one of the largest public robot manipulation datasets — contains roughly 350 hours of data. Xiaomi's in-house collection for just two tasks is approximately twice the size of a major public benchmark. This data is not being open-sourced (only the model weights are). The model checkpoint encodes the benefits of this data, but the raw trajectories — and the teleoperation infrastructure, tooling, and operator workflows that produced them — represent a moat that is invisible from the paper's abstract. For investors evaluating robotics data strategies: proprietary high-contact, high-dexterity manipulation data at this scale is rare and expensive to replicate.