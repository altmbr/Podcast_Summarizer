# ABot-M0: VLA Foundation Model for Robotic Manipulation with Action Manifold Learning

**Podcast:** arXiv Physical AI Research
**Date:** 2026-04-04
**Processed:** 2026-04-04T09:03:55Z
**Participants:** Yandan Yang, Mu Xu, et al. (arXiv Physical AI)
**Source:** paper
**arXiv:** 2602.11236
**PDF:** https://arxiv.org/pdf/2602.11236

---

# ABot-M0: VLA Foundation Model for Robotic Manipulation with Action Manifold Learning

---

## 1. Key Themes

### The Data Problem Is Solvable Without Proprietary Pipelines

The paper's most commercially significant claim is that world-class manipulation performance can be achieved by systematically engineering public data — no proprietary collection required. From six open-source datasets, the team built UniACT-dataset: "over 6 million trajectories and 9,500 hours of data, covering diverse robot morphologies and task scenarios... currently the largest collection within the non-private domain" (Abstract, Section 2). After rigorous cleaning, approximately 16% of raw trajectories were discarded (Section 2.2). The result is a foundation that drove 98.6% average success on LIBERO and 80.5% zero-shot on LIBERO-Plus — outperforming π0.5, GR00T-N1.6, and OpenVLA-OFT (Section 6.2). For companies burning cash on proprietary data collection, this is a direct challenge to that capex assumption.

### Predicting Actions Directly Beats Predicting Noise

The paper's core architectural innovation challenges the diffusion orthodoxy that has dominated VLA design. The Action Manifold Hypothesis posits that "effective robot actions lie not in the full high-dimensional space but on a low-dimensional, smooth manifold governed by physical laws and task constraints" (Abstract). Rather than predicting noise (ε-prediction) or velocity (v-prediction) as GR00T, π0, and most diffusion-based policies do, ABot-M0 predicts the clean action directly. The practical payoff: when action chunk size is pushed to 30 (simulating long-horizon or high-DOF tasks), GR00T's performance "drops sharply by 23.6%, while ABot-M0 maintains an impressive 62.8% success rate" (Section 6.3.1). This matters enormously for humanoid and whole-body control, where action spaces explode in dimensionality.

### Sampling Strategy Is an Underrated Training Variable

Most robotics teams obsess over architecture and data volume, but the paper demonstrates that *how* you sample across heterogeneous datasets is a first-order determinant of generalization. Comparing three strategies — trajectory-uniform, task-uniform, and embodiment-uniform — the team found that task-uniform sampling "provides a more favorable trade-off between embodiment diversity and skill coverage" (Section 4.1). On the Libero Plus downstream benchmark, task-uniform outperforms trajectory-uniform by 1.1 percentage points (Table 2, Section 4.2). More importantly, trajectory-uniform sampling "suffers from severe scale dominance and embodiment concentration" — meaning the dominant dataset (AgiBot-G1) simply drowns out rare robot morphologies. For any team mixing datasets from multiple hardware platforms, this is an operational finding, not an academic one.

### 3D Spatial Awareness as a Modular Add-On, Not a Rearchitect

Standard VLMs are perceptually blind to geometry — they know "the cup is to the left of the box" but cannot reason about millimeter-level distance or reachability. ABot-M0 addresses this through a plug-and-play dual-stream architecture that injects 3D features from VGGT (single-view geometry) and Qwen-Image-Edit (synthetic multi-view) without touching the VLM backbone. The gains are task-dependent but measurable: on the camera viewpoint perturbation subset of LIBERO-Plus, two synthesized views yield "+14% points" improvement (Section 5.2). The module "can be toggled on/off or combined... based on task demands, offering flexible deployment without retraining the core VLM" (Section 5.2). This is a deployment architecture decision, not just a research one — teams can ship the base model and layer 3D perception on top for precision tasks.

### Cross-Embodiment Generalization Is an Engineering Problem, Not Just a Research One

The paper frames the "one-brain, many-forms" goal as a practical engineering challenge solvable today with systematic data standardization. Key to this is a unified action representation: "all tasks are standardized into delta actions with end-effector (EEF) position... all orientation representations (e.g., Euler angles, rotation matrices, quaternions) are transformed into rotation vectors" (Section 2.3). A pad-to-dual-arm strategy allows single-arm and dual-arm tasks to share the same policy network: "for single-arm trajectories, the action dimensions corresponding to the unused arm are filled with zeros" (Section 2.3). The result spans 20+ embodiments in a single trained model.

---

## 2. Contrarian Perspectives

### Proprietary Data Moats in Robotics Are Weaker Than Assumed

The conventional wisdom — especially among investors — is that robotics AI companies with large proprietary datasets have durable competitive advantages. This paper directly challenges that narrative. The authors explicitly set out to answer: "given the high cost and hardware dependence of robotic data collection, can we integrate global open-source datasets, currently isolated in silos, into a unified foundation for training VLA models?" (Section 1). Their answer is yes — and they back it with state-of-the-art numbers across four benchmarks. The conclusion is unambiguous: "high-performance embodied intelligence is achievable without proprietary data or custom hardware when public resources are systematically engineered" (Section 7.2). Companies betting their moat on data exclusivity should pay attention.

### Noise Prediction in Diffusion-Based Policies Is Architecturally Mismatched to Robotics

Most leading VLA systems — GR00T, π0, π0.5, Diffusion Policy — are built on diffusion backbones that predict noise or velocity. The paper argues this is fundamentally inefficient for robot action learning: "noise or velocity are inherently high-dimensional and off-manifold... Forcing a network with finite capacity to directly regress these unstructured, high-dimensional targets is inefficient" (Section 3.1). This isn't just a theoretical point — the ablation shows it has real consequences at scale. As the authors note, "The challenge escalates significantly as the embodiment complexity grows from a single robotic arm to a full-body humanoid with two dexterous hands, which results in a substantially expanded action space and increased degrees of freedom" (Section 3.1). Companies building toward humanoid or high-DOF manipulation on diffusion-based architectures may be accumulating technical debt.

### Chain-of-Thought Reasoning Does Not Fix Perceptual Deficits in VLMs

A popular approach to improving robot spatial reasoning is adding chain-of-thought (CoT) prompting or reasoning steps on top of existing VLMs. The paper explicitly dismisses this: "such methods operate at the reasoning level without enriching the underlying perceptual representation" (Section 1). Instead, the solution is to inject geometric priors directly into the feature representation via 3D modules. The ablation validates this — VGGT-based 3D injection improves LIBERO long-horizon tasks from 90.8% to 95.6% (Table 9, Section 6.3.3), a gain that reasoning-layer interventions cannot replicate. For teams investing in CoT-based VLA approaches (CoT-VLA is a direct competitor cited in Table 3), this is a substantive architectural critique.

---

## 3. Companies Identified

**Alibaba (AMAP CV Lab)**
- Description: Chinese technology conglomerate; AMAP is Alibaba's mapping and navigation division
- Why relevant: ABot-M0 is developed by the AMAP CV Lab under Alibaba, with the corresponding author at alibaba-inc.com (Section 8). This is a significant corporate robotics AI investment from a company not traditionally associated with physical AI
- Quote: "Corresponding author: xumu.xm@alibaba-inc.com" (Section 8)

**Physical Intelligence (π0, π0.5)**
- Description: Leading robotics AI startup focused on generalist robot policies
- Why relevant: π0.5 is a primary benchmark competitor, directly outperformed by ABot-M0 on RoboTwin 2.0 (80.42% vs. 42.98% clean) and LIBERO (98.6% vs. 96.9%). ABot-M0 explicitly positions itself as exceeding π0 without proprietary data
- Quote: "outperforming strong baselines such as π0.5, UniVLA, and OpenVLA-OFT" (Section 1); "ABot-M0 outperforms strong VLA models like π0.5 and X-VLA in both the clean and randomized multi-task settings on RoboTwin2.0" (Section 6.2.4)

**NVIDIA (GR00T N1, N1.6)**
- Description: GPU and AI infrastructure company; GR00T is their humanoid robot foundation model
- Why relevant: GR00T N1 and N1.6 are direct architectural comparisons throughout. ABot-M0 outperforms GR00T-N1.6 on RoboCasa GR1 (58.3% vs. 47.6%) and uses the same 0.16B action expert size for fair ablation comparison. The noise-prediction paradigm of GR00T is the primary target of the Action Manifold Hypothesis critique
- Quote: "ABot-M0 achieves a 58.3% success rate, comprehensively outperforming prior noise prediction-based experts like GR00T-N1.6... thereby setting a new SOTA" (Section 6.2.3)

**AgiBot**
- Description: Chinese humanoid robotics company
- Why relevant: AgiBot-Beta dataset (1M+ trajectories) is a primary training data source. The paper's sampling strategy explicitly compensates for AgiBot-Beta's single-embodiment bias: "we deliberately reduce its sampling ratio during training to mitigate embodiment bias" (Section 2.2)
- Quote: "AgiBot-Beta and Galaxea contribute high-quality visual observations and temporally coherent action sequences" (Section 2.2)

**Hugging Face (LeRobot)**
- Description: Open-source AI platform
- Why relevant: LeRobot v2 format is adopted as the universal data standard for the UniACT-dataset pipeline. "we convert all trajectories into the LeRobot v2 format as a common standard" (Section 2.2). This makes HuggingFace's data tooling a critical infrastructure dependency for open-source robotics pipelines
- Quote: "The raw data originates from heterogeneous sources—including LeRobot v2, LeRobot v3, RLDS... we convert all trajectories into the LeRobot v2 format as a common standard" (Section 2.2)

**Galaxea**
- Description: Chinese robotics company focused on dual-arm manipulation
- Why relevant: Galaxea dataset (100K trajectories) contributes high-quality dual-arm data to UniACT-dataset, cited for "Long-Horizon Subtask Annotation" and "Rich Sensor Data" (Table 1)
- Quote: "AgiBot-Beta and Galaxea contribute high-quality visual observations and temporally coherent action sequences" (Section 2.2)

---

## 4. People Identified

**Yandan Yang**
- Lab/Institution: AMAP CV Lab, Alibaba
- Why notable: Lead contributor on data collection, analysis, standardization, and writing. Primary architect of the UniACT-dataset curation methodology
- Quote: Listed first in author contributions across Data Collection & Analysis, Data Standardization, Writing (Section 8)

**Shuang Zeng**
- Lab/Institution: AMAP CV Lab, Alibaba
- Why notable: Lead contributor on model architecture, training, evaluation, and writing — making her the primary technical architect of the ABot-M0 model itself
- Quote: Listed in Model Architecture, Training, Evaluation, and Writing (Section 8)

**Tong Lin**
- Lab/Institution: AMAP CV Lab, Alibaba
- Why notable: Co-lead on data pipeline, data standardization, training, and evaluation — bridging data engineering and model training
- Quote: Listed in Data Standardization, Data Pipeline, Training, Evaluation, Writing (Section 8)

**Xinyuan Chang**
- Lab/Institution: AMAP CV Lab, Alibaba
- Why notable: Project lead alongside Feng Xiong; also contributed to data standardization and writing. Organizational authority behind the project
- Quote: "Project Lead: Xinyuan Chang, Feng Xiong" (Section 8)

**Mu Xu**
- Lab/Institution: Alibaba
- Why notable: Corresponding author and advisor; the senior research leader accountable for the work. Alibaba's physical AI research strategy runs through this person
- Quote: "Corresponding author: xumu.xm@alibaba-inc.com... Advisor: Mu Xu" (Section 8)

**Tianhong Li and Kaiming He (cited)**
- Lab/Institution: MIT / Meta AI (referenced via JiT paper)
- Why notable: Their JiT work on direct action prediction is the primary intellectual inspiration for Action Manifold Learning. The paper acknowledges: "Inspired by JiT compilation, we propose the 'Action Manifold Hypothesis'" (Section 1). Kaiming He's influence on the core architectural innovation is significant
- Quote: "Inspired by JiT [25] compilation, we propose the 'Action Manifold Hypothesis'" (Section 1)

---

## 5. Operating Insights

### Data Cleaning Is Not Optional Infrastructure — It Is Model Performance

Teams that treat data preprocessing as a secondary concern are leaving significant performance on the table. ABot-M0's pipeline discarded 16% of raw trajectories and identified specific failure modes that silently degrade models: non-English instructions, frame-instruction mismatches, wrist camera frames with insufficient field of view, and trajectories with ambiguous rotation representations. The paper warns explicitly: "neglecting proper text alignment will cause the trained model to effectively degenerate into a vision-action (VA) model lacking proper language grounding" (Section 2.2). For CTOs evaluating data pipelines, the minimum viable quality bar includes: validated language instructions in consistent language, temporal alignment between frames and instructions, filtered visual anomalies, and verified action dimension semantics. The paper's full pipeline is being open-sourced, making this immediately actionable.

### Sampling Strategy Across Mixed Datasets Requires Active Design, Not Naive Mixing

When training on multiple datasets — which every serious robotics AI team is now doing — naive trajectory-level uniform sampling causes the largest dataset to dominate, starving rare embodiments and skills. The paper's recommendation is task-uniform sampling, which "provides a more favorable trade-off between embodiment diversity and skill coverage" and achieves "the lowest MAE on OXE, AgiBot-Beta, and RoboCoin" (Section 4.2). Practically: if your training mix includes one dataset 5-10x larger than others (common when using OXE), you need explicit reweighting. The authors use "a dual-weighted sampling strategy based on task category and robot morphology... Rare tasks are oversampled with probability inversely proportional to their data ratio" (Section 3.2). This is an engineering decision teams should make deliberately before large training runs, not after.

### Plan for High-DOF Action Spaces Now — Architecture Choices Have Compounding Consequences

The RoboCasa GR1 evaluation required predicting "a 29 action space encompassing both dual arms, hands, and the waist... to test the robustness of the new AML paradigm for predicting 464 high-dimensional actions" (Section 6.2.3). Diffusion-based noise-prediction architectures degrade significantly as action dimensionality grows — demonstrated by GR00T's 23.6% performance collapse at chunk size 30 vs. ABot-M0's 8.2% drop under the same conditions (Section 6.3.1, Table 7). For teams building toward humanoid whole-body control, choosing an action-prediction architecture over a noise-prediction one is a decision worth making at the start of a program, not during a painful retrofit.

---

## 6. Overlooked Insights

### VLM Pre-Training on Robotics Data Makes Action Query Modules Redundant

A subtle but high-leverage finding buried in the VLM feature interaction ablation: once a VLM has been pre-trained on robotics data, adding action query mechanisms (a common architectural pattern) actually *hurts* performance. "Using raw VLM features directly outperforms feature concatenation with action queries" and "concatenating features and queries as the conditioning input resulted in the lowest performance" (Section 5.1, Table 8). The explanation is that robotics pre-training already aligns the VLM's internal space with the action domain, and adding query interfaces "may introduce redundant or conflicting signals" that disrupt policy learning. The implication: architectural complexity designed to bridge the VLM-to-action gap is only necessary if the VLM hasn't been robotics-pretrained. Teams using off-the-shelf VLMs without robotics pre-training and teams using robotics-pretrained VLMs need fundamentally different adapter architectures.

### 50 Paired Samples Is Sufficient to Fine-Tune a Multi-View Synthesis Module for New Deployment Environments

The paper reports that Qwen-Image-Edit was fine-tuned for 3D multi-view synthesis "using only 50 paired samples per dataset" on Bridge and LIBERO data (Section 5.2). Despite this minimal fine-tuning, two synthesized views yielded a 14-percentage-point improvement on the camera viewpoint perturbation subset of LIBERO-Plus. This has a direct deployment implication: operators deploying robots in new physical environments with different camera configurations can adapt the 3D perception module with minimal labeled data collection — approximately 50 examples — rather than the thousands typically assumed necessary for domain adaptation. This dramatically lowers the cost of deploying ABot-M0 variants into new facilities or robot configurations.