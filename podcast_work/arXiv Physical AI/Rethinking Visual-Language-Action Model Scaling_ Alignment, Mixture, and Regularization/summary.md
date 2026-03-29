# Rethinking Visual-Language-Action Model Scaling: Alignment, Mixture, and Regularization

**Podcast:** arXiv Physical AI Research
**Date:** 2026-03-29
**Processed:** 2026-03-29T09:03:34Z
**Participants:** Ye Wang, Qin Jin, et al. (arXiv Physical AI)
**Source:** paper
**arXiv:** 2602.09722
**PDF:** https://arxiv.org/pdf/2602.09722

---

# Rethinking VLA Scaling: What Actually Works When You Mix Robot Data

**Paper:** Wang et al. (2026), "Rethinking Visual-Language-Action Model Scaling: Alignment, Mixture, and Regularization" — BeingBeyond / Renmin University of China / Peking University

---

## 1. Key Themes

### More Data Does Not Mean Better Robots — And the Paper Proves It Systematically

The central finding is a direct refutation of the "scale data = scale performance" assumption borrowed from LLMs. When the authors incrementally added heterogeneous robot datasets on top of their OXE-only baseline, performance went *down*, not up. Starting from a 54.7% average success rate on RoboCasa with OXE-only data (D1), adding real-world EEF data from additional embodiments dropped performance to 48.8% (D2), and further additions only partially recovered it — ending nearly 5% below the OXE-only baseline. As the paper states: "In contrast to language-model scaling behavior, enlarging the robotic pre-training corpus does NOT yield monotonic gains" (Section V-B). This is not a marginal finding — it is the paper's headline result, and it has direct implications for any company currently budgeting to acquire more robot data.

### End-Effector Relative Coordinates Are the One Reliable Default

Across both simulation benchmarks and real-robot trials, representing actions relative to the robot's own end-effector (EEF-Relative) consistently outperformed world-frame representations. On LIBERO with a frozen VLM backbone, EEF-Relative achieved the highest average of 75.1% — the largest improvement over training from scratch at +8.2%. On RoboCasa, it was the only representation to show consistent gains across all task categories, including a +7.0% improvement on manipulation tasks. Critically, in real-robot testing, Delta-based representations (both World-Delta and EEF-Delta) produced zero performance: "all Delta actions exhibit jittering in place on the real robot, rendering them unable to execute tasks and resulting in a 0% success rate" (Section V-A). The EEF-Relative frame is invariant to camera placement and robot base position — a property that matters enormously when you are deploying across multiple facilities or robot configurations.

### Common Training Tricks Don't Scale — Simpler Pipelines Win

The paper ran controlled ablations on two widely used training practices: sensory dropout (randomly zeroing proprioceptive state or camera views during training) and multi-stage curriculum learning (freezing the VLM backbone first, then unfreezing). Neither consistently helped. Disabling visual dropout entirely scored *higher* (85.6%) than the baseline with dropout (84.5%). And the multi-stage curriculum was outperformed by simple end-to-end fine-tuning from the start: "Directly fine-tuning the full model end-to-end ('Stage 2 Only') attains the best average success 85.8%, outperforming the multi-stage schedule" (Section V-C). The implication is that engineering complexity layered on top of pretraining may be solving problems that don't exist at scale.

### The Evaluation Protocol Problem Is Real and Largely Ignored

The paper introduces a "Grouped Blind Ensemble" protocol as a formal contribution — operators run trials without knowing which model variant is being tested, and outcome scoring is separated from policy execution. This is not a minor methodological footnote. It reflects a real problem: most robotics benchmarks in industry and academia are run by operators who know which system they are evaluating, introducing systematic bias. As the authors note, "real-world testing can be influenced by experimenter bias, including operator familiarity with a policy and small adjustments during execution" (Section I). For investors evaluating robotics companies, this is a flag: many reported real-world success rates in the field are likely inflated.

### State-of-the-Art Performance Is Achievable Without Task-Specific Engineering

Despite the cautionary findings, the authors' base model — trained on their best data configuration with EEF-Relative actions — achieves 97.9% average success on LIBERO and 50.0% on RoboCasa under a matched 50-shot fine-tuning protocol. This exceeds or matches π₀, π₀.₅, and NVIDIA GR00T-N1 on RoboCasa. The model uses a ~2.7B parameter Mixture-of-Transformers (MoT) architecture initialized from InternVL-3.5-2B. The takeaway: getting the fundamentals right (action representation, data curation) matters more than architectural novelty.

---

## 2. Contrarian Perspectives

### Data Diversity Is a Liability, Not an Asset — If Embodiments Are Too Different

The conventional wisdom in robotics AI is that broader data diversity enables better generalization. This paper directly challenges that. Adding proprietary Agibot data, RoboMind data, and simulation trajectories on top of OXE consistently degraded performance. The authors describe the mechanism as "destructive interference": "naively pooling structurally disparate robot datasets induces destructive interference rather than improved transfer" (Section V-B). This runs counter to the strategy of companies building massive heterogeneous data collection pipelines. The evidence suggests that curated, structurally similar data beats diverse-but-incompatible data. The practical implication: a smaller, well-aligned dataset may outperform a larger, messier one — and the industry's race to collect more data across more embodiments may be misallocating capital.

### Multi-Stage Training Curricula Are Engineering Overhead, Not Performance Gains

A significant fraction of robotics ML infrastructure is built around curriculum learning — the idea that you should warm up models gradually, freeze components, then progressively unfreeze. This paper finds that "the two-stage alignment curriculum is similarly non-essential. Directly fine-tuning the full model end-to-end ('Stage 2 Only') attains the best average success 85.8%, outperforming the multi-stage schedule" (Section V-C). Similarly, "disabling visual dropout (p_view = 0) increases success to 85.6% versus the balanced baseline (84.5%), whereas heavy proprioceptive masking reduces performance." Companies investing in complex training pipelines with elaborate regularization schedules should audit whether those design choices are actually delivering returns.

### World-Frame Action Representations Actively Hurt Cross-Embodiment Transfer

Many robotics systems express robot actions in world coordinates — a natural choice when cameras are calibrated and workspaces are bounded. This paper shows that pretraining on world-frame actions produces *negative* transfer: "pre-training yields negative transfer for world-frame variants (-0.9%, -0.5%) but consistent gains for EEF-frame variants (+2.6%, +2.4%). This inversion indicates that world coordinates can overfit single-environment regularities, whereas EEF coordinates generalize better across varying cameras and robot bases in large-scale data" (Section V-A). For companies deploying robots across multiple sites with varying camera setups, this finding argues for a fundamental change in how action data is collected, labeled, and stored.

---

## 3. Companies Identified

**BeingBeyond**
- Description: Chinese robotics/embodied AI company, co-author institution
- Why relevant: Primary institutional sponsor of the research; has a dedicated research site (research.beingbeyond.com) hosting the paper's project page. Appears to be building generalist VLA infrastructure at scale.
- Quote: "Project website: https://research.beingbeyond.com/rethink_vla" (Abstract)

**Agibot (AgiBot World)**
- Description: Chinese robotics company producing large-scale manipulation datasets, including gripper-based and dexterous-hand trajectories
- Why relevant: Their dataset (AgiBot World Colosseo) is one of the largest components of the training corpus — 249M raw frames for gripper alone — but required aggressive downsampling (step size 7) to prevent it from dominating training. Adding their data contributed to negative transfer. Their dataset scale does not translate into proportional model gains.
- Quote: "We further incorporate large-scale proprietary datasets from Agibot, which cover both gripper-based and dexterous-hand EEF control" (Section IV-A); step size 7 for Agibot Gripper (Table VII)

**Physical Intelligence (π₀, π₀.₅)**
- Description: US robotics AI startup building generalist robot policies
- Why relevant: Used as a direct performance benchmark. The paper's base model matches or exceeds π₀ (94.4% LIBERO avg) and π₀.₅ (96.9% LIBERO avg), with the authors achieving 97.9% LIBERO and outperforming both on RoboCasa (50.0% vs. π₀'s 42.4% and π₀.₅'s 41.4%).
- Quote: "our base model is competitive without task-specific tuning or specialized optimizations, reaching 97.9% average success on LIBERO and 50.0% on RoboCasa benchmarks" (Section V-D)

**NVIDIA (GR00T-N1)**
- Description: NVIDIA's open foundation model for generalist humanoid robots
- Why relevant: Directly benchmarked and outperformed on both LIBERO (93.9% vs. 97.9%) and RoboCasa (36.0% vs. 50.0%).
- Quote: Table VI shows GR00T-N1 at 36.0% RoboCasa average versus the authors' 50.0%

**Open X-Embodiment Collaboration (OXE)**
- Description: Multi-institution open robot dataset spanning diverse embodiments and tasks
- Why relevant: The OXE-only pretraining configuration (D1) consistently outperformed all larger, more diverse mixtures. OXE's high-quality subsets (DROID, Bridge, Fractal) formed the strongest foundation. The paper validates OXE's quality but also shows that simply adding more data on top of it is counterproductive.
- Quote: "D1 provides the strongest pre-training transfer on LIBERO, reaching 77.3% average success in the Frozen VLM setting (+10.4% over training from scratch). However, simply increasing data diversity degrades performance." (Section V-B)

**InternVL / Shanghai AI Lab (InternVL-3.5-2B)**
- Description: Open-source vision-language model used as the semantic backbone
- Why relevant: The VLM backbone underpinning the entire architecture. Demonstrates that a 2B parameter open VLM is sufficient for competitive generalist robot control when paired with the right action representation and training recipe.
- Quote: "the semantic expert ℰ_sem is initialized from InternVL-3.5-2B with hidden size 2048" (Section IV-B)

**Hugging Face / LeRobot (SO-100)**
- Description: Low-cost teleoperation platform dataset included in the training corpus
- Why relevant: Included as a real joint-space data source. Signals that low-cost community data (5M frames, step size 1 — no downsampling) is treated as high-quality signal, not noise.
- Quote: "step sizes 4-8 for InternData Sim subsets, while keeping dense sampling for smaller but diverse datasets (e.g., step size 1 for SO-100 and most OXE subsets)" (Section IV-A)

---

## 4. People Identified

**Sipeng Zheng**
- Lab/Institution: BeingBeyond / Peking University
- Why notable: Co-corresponding author; appears to be leading the VLA research program at BeingBeyond. Also co-author on the related "Being-H0.5" paper on cross-embodiment generalization.
- Quote: Corresponding author designation; also cited in reference [29]: "Being-h0.5: scaling human-centric robot learning for cross-embodiment generalization"

**Zongqing Lu**
- Lab/Institution: Peking University / BeingBeyond
- Why notable: Senior academic PI on the project; prominent in Chinese embodied AI research. Co-corresponding author.
- Quote: Listed as corresponding author; affiliated with both Peking University and BeingBeyond

**Qin Jin**
- Lab/Institution: Renmin University of China
- Why notable: Co-corresponding author from RUC; bridges the academic research side of the collaboration.
- Quote: Listed as corresponding author, Renmin University of China

**Ye Wang, Hao Luo, Wanpeng Zhang**
- Lab/Institution: BeingBeyond / Peking University / Renmin University of China
- Why notable: Equal-contribution first authors who executed the controlled empirical study. Hao Luo is also a co-author on Being-H0.5, suggesting continuity of this research program.
- Quote: "Equal contribution" designation; Hao Luo cited in reference [29] for Being-H0.5

---

## 5. Operating Insights

### If You Are Buying or Collecting Data, Quality of Structural Alignment Beats Volume

The single most actionable finding: adding 130M+ additional frames of real and simulated robot data made models *worse*, not better, on downstream tasks. The authors explain this as structural incompatibility — different kinematic structures, control conventions, and action spaces create gradient interference during training. If you are a robotics company evaluating data vendors or planning a data collection program, the question is not "how many hours?" but "how structurally compatible is this data with your target deployment embodiment?" OXE's curated subsets (DROID, Bridge, Fractal) outperformed everything else combined. Budget accordingly.

### Standardize on EEF-Relative Action Representation Across Your Entire Data Pipeline — Now

The EEF-Relative action representation is the only one that produced consistent gains across simulation and real hardware, and it is the only one that avoided catastrophic failure modes (Delta representations produced 0% real-world success). This has infrastructure implications: if your data pipeline stores actions in world-frame coordinates (a common default), you are systematically encoding a representation that hurts cross-embodiment transfer. Retrofitting this is expensive. The paper is clear: "EEF-Relative achieves the highest average success rate of 75.1% with the largest improvement of +8.2%... confirming that the end-effector space is the most effective choice for preserving and transferring physical priors" (Section V-A). Make this a data schema standard before your dataset grows further.

### Adopt Blind Evaluation Protocols Before Your Next Internal Benchmark

The paper introduces the Grouped Blind Ensemble protocol specifically because "operators execute tasks without knowing which model variant is being tested." This is not just academic rigor — it directly affects how companies make model selection decisions. If your engineering team is evaluating policy variants and operators know which system they're running, your success rate numbers are likely systematically biased toward variants the team is more familiar with. The protocol is simple to implement (anonymized model IDs, randomized trial queues, separated outcome judgment) and has no cost. Any company making go/no-go deployment decisions based on internal real-robot evals should implement this immediately.

---

## 6. Overlooked Insights

### The Frozen VLM Regime Reveals Pretraining Quality More Reliably Than Fine-Tuning

A buried but important methodological finding: when the VLM backbone is frozen during fine-tuning, performance differences between pretraining strategies become *larger and more consistent* — not smaller. EEF-Relative with a frozen VLM achieves 75.1% on LIBERO vs. 84.5% with an unfrozen VLM, but the relative ranking of action representations is more stable in the frozen regime. The authors note: "The benefits of pre-training become even more pronounced when the VLM backbone is frozen. In this regime... the performance relies heavily on the high-quality representations initialized from pre-training" (Section V-A). This matters for deployment: companies that fine-tune with a frozen backbone (common for compute efficiency) are more exposed to pretraining quality issues. The frozen-VLM condition is essentially a stress test for pretraining — and it should be a standard part of any VLA evaluation suite, not an afterthought.

### 658M Raw Frames Collapsed to 182M Effective Frames — The Gap Is Where Strategy Lives

The paper's data table (Appendix A, Table VII) reveals that the raw corpus is 658M frames, but after balancing, only 182M are used effectively. The Agibot Gripper dataset alone contributes 249M raw frames but is downsampled to 35.6M (step size 7). Meanwhile, smaller datasets like SO-100 (5M frames) are kept at step size 1 — full density. This means the research team's data *curation and sampling strategy* is doing more work than the raw data volume. Any company treating raw frame count as a proxy for training data quality is misreading the signal. The effective data ratio (raw/effective) is itself a design variable with performance consequences, and this paper shows it can swing results by 5-10 percentage points across benchmarks. This is the kind of detail that separates teams that understand scaling from teams that are just scaling.