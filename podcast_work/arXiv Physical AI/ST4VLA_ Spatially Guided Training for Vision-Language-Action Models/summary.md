# ST4VLA: Spatially Guided Training for Vision-Language-Action Models

**Podcast:** arXiv Physical AI Research
**Date:** 2026-03-29
**Processed:** 2026-03-29T09:05:39Z
**Participants:** Ji-lu Ye, Jiangmiao Pang, et al. (arXiv Physical AI)
**Source:** paper
**arXiv:** 2602.10109
**PDF:** https://arxiv.org/pdf/2602.10109

---

# ST4VLA: Spatially Guided Training for Vision-Language-Action Models
## Investor & Operator Summary

---

## 1. Key Themes

### Spatial Understanding Is the Missing Link Between Language Models and Robot Control

The paper's central finding is that current VLA models fail not because they can't understand language, but because naive fine-tuning on robot action data actively destroys the spatial reasoning capabilities that foundation models already have. The authors show this quantitatively: "Vanilla VLA shows rapid spatial perception degradation, with RefCOCO-g performance dropping to near-random levels by 20k steps, indicating that action-only optimization disrupts spatial representations" (Section 3.1). This isn't a minor degradation — it's near-total collapse of spatial grounding. The implication is that every team fine-tuning a VLM into a robot policy using standard supervised approaches is likely destroying the very capabilities they paid to acquire from pretraining.

### A Two-Stage Training Recipe That Preserves What You Paid For

ST4VLA's core contribution is a structured pipeline: first pre-train the VLM specifically on spatial grounding tasks (point prediction, bounding box detection, trajectory forecasting), then use "spatial prompting" during action fine-tuning to keep those representations active. This isn't just an academic distinction — the authors demonstrate that the ordering and separation of objectives matters enormously. The gradient alignment metric (PSS) jumps from 0.25 to 0.42 when spatial prompting is used, meaning the two learning objectives stop fighting each other (Section 3.1). The practical result: "84.6/75.9 on Google Robot and 73.2 on WidowX" versus baselines of 66.1 and 54.7 respectively (Table 1) — improvements of 14-28% over vanilla approaches.

### Generalization, Not Just Benchmark Performance

The headline numbers on SimplerEnv are impressive, but the more important finding for deployment is the real-world generalization data. On a Franka robot doing pick-and-place with unseen objects, novel backgrounds, and paraphrased instructions, ST4VLA achieves 65% average success versus π₀'s 31% and GR00T N1.5's 48% (Table 4). On unseen object orientations specifically — a notoriously hard real-world problem — ST4VLA scores 63% versus GR00T's 47% and π₀'s 27%. "These findings demonstrate the model's robust visual and linguistic generalization in pick-and-place tasks" (Section 3.4). For operators, the signal here is not just that it's better, but that the gap widens under distribution shift — exactly the conditions that break deployed systems.

### Long-Horizon Manipulation Becomes Tractable

The dual-system architecture (a "System 2" VLM planner feeding a "System 1" DiT action expert) is what enables multi-step tasks. ST4VLA reaches 92% success on real-world long-horizon manipulation under distribution shifts including physical interference and mid-task replanning (Section 3.5, Figure 5). Tasks tested include desktop sorting, drawer organization, and sandwich assembly — not toy tasks. The authors note ST4VLA "jointly trains on multimodal inputs, task decomposition, subtask identification, numerical reasoning, and action supervision, for unified planning and action prediction" without requiring an external planner (Appendix D.4). This matters because external planners are a common deployment bottleneck.

### Scaling Laws Apply to Spatial Data, Not Just Action Data

The paper contains a critical finding buried in the ablations: spatial grounding data has a non-linear scaling relationship with manipulation performance. "Performance gains remain modest when spatial grounding data is below 1.0M pairs. However, once the data scale surpasses 2.0M pairs, we observe dramatically increasing returns. At 3.0M pairs, the model achieves substantial improvement, with average performance rising from 61.4 to 77.9 — a remarkable 26.9% relative gain" (Section C.4, Table 9). This is a data strategy insight, not just a modeling one. Teams investing in robot data collection should be asking whether they're collecting the right *type* of data, not just more of it.

---

## 2. Contrarian Perspectives

### More Action Data Alone Won't Solve Your Generalization Problem

The prevailing strategy in robot learning is to collect more teleoperation data and scale. This paper directly challenges that. The extended training curves show "Vanilla VLA and Vanilla Co-training baselines continue to show marginal improvements early on, they ultimately converge to substantially lower plateaus compared to our method. These results conclusively show that explicitly injecting spatial priors does not simply act as a warm-up for faster learning; it fundamentally alters the optimization landscape, allowing the policy to generalize to a higher performance ceiling that standard multimodal co-training fails to reach" (Appendix B.1, Figure 6). The ceiling is different, not just the convergence speed. Companies spending millions on teleoperation data collection who are not also curating spatial grounding data may be hitting a hard ceiling they don't yet understand.

### Co-Training Spatial and Action Data Simultaneously Makes Things Worse, Not Better

Intuition says: if spatial understanding helps robots, just train on both spatial and action data together. ST4VLA shows this is wrong without careful design. "Naive co-training of action data with spatial data yields a PSS of only 0.25, indicating significant misalignment between the gradient subspaces" (Section 3.1). Vanilla co-training does improve over action-only training (61.1 vs. 54.7 on WidowX), but it oscillates unstably and never reaches the performance of properly staged training. The gradient conflict between spatial and action objectives is real and measurable. This is a direct challenge to any team thinking they can simply add spatial data to their existing training mix without restructuring the pipeline.

### You Don't Need a Bigger Backbone — You Need Better Training

The paper tests ST4VLA's framework on Florence-2, a "considerably weaker VLM" than the Qwen2.5-VL backbone used for the main results. Even with Florence-2, "ST4VLA still surpasses GR00T N1.5 (67.9% vs. 61.9%), while the Vanilla Co-training baseline collapses on difficult tasks (e.g., 3.1% for Block Stacking)" (Section C.3, Table 8). GR00T N1.5 is built on a substantially more capable backbone and was trained on far more data. The implication: teams chasing larger foundation models are potentially misallocating resources if their training recipe is architecturally flawed. The training methodology contributes more to the performance gap than backbone capacity.

---

## 3. Companies Identified

**Physical Intelligence (π₀, π₀.5)**
Physical Intelligence's π₀ and π₀-FAST models are used as primary baselines throughout the paper. On SimplerEnv, ST4VLA achieves 84.6% on Google Robot Visual Matching versus π₀'s 58.8%. On real-world pick-and-place, ST4VLA scores 65% average versus π₀'s 31%. On long-horizon tasks, ST4VLA consistently surpasses π₀. The paper also cites π₀.5 with Knowledge Insulation (KI) on LIBERO (94.3% average), where ST4VLA edges ahead at 95.9%. Physical Intelligence is the most directly benchmarked commercial competitor, and the gap in generalization-heavy settings is substantial.
> "ST4VLA outperforms all baselines across real-world test settings. Even under highly challenging conditions, such as interference from visually similar distractors, novel object instances, and paraphrased instructions, ST4VLA achieves strong results." (Section 3.4)

**NVIDIA (GR00T N1.5)**
NVIDIA's GR00T N1.5 generalist humanoid foundation model is a consistent point of comparison. On real-world pick-and-place, GR00T achieves 48% average versus ST4VLA's 65%. On the simulated 200-task benchmark, ST4VLA outperforms GR00T across all four generalization tracks. Notably, when ST4VLA is tested with the weaker Florence-2 backbone, it still beats GR00T N1.5.
> "With a much weaker Florence-2 backbone, ST4VLA still surpasses GR00T N1.5 (67.9% vs. 61.9%), while the Vanilla Co-training baseline collapses on difficult tasks." (Section C.3)

**Google DeepMind (RT-1, RT-2, RT-1-X)**
Google's RT-series models appear in benchmark comparisons throughout the paper. RT-2-X, which uses web-scale co-training, achieves only 46.3% on Google Robot Visual Matching versus ST4VLA's 84.6%. These are older models, but their inclusion contextualizes the trajectory of improvement and validates that the SimplerEnv benchmark is a meaningful reference point.
> "RT-2-X... 46.3 [Average VM]" vs. ST4VLA's 84.6 (Table 2)

**Alibaba (Qwen2.5-VL)**
Qwen2.5-VL-3B-Instruct is the VLM backbone that ST4VLA is built on. The paper demonstrates that a 3B parameter model with the right training recipe outperforms much larger models from Physical Intelligence and NVIDIA. This is a meaningful validation of Alibaba's open-source VLM investment for physical AI applications.
> "We propose a new dual-system, end-to-end VLA framework based on Qwen2.5-VL." (Section 2.1)

**Microsoft (Magma, Florence-2)**
Microsoft's Magma model (which also uses spatial pre-training) is compared directly. ST4VLA outperforms Magma on all benchmarks (84.6% vs. 52.9% on Google Robot VM). Florence-2 is used as an ablation backbone to show the training method's backbone-agnosticism.
> "Similar to ours, Magma also adopts spatial pre-training, though it does not explicitly leverage spatial prompting to guide action generation." (Section 4)

**Figure AI (Helix)**
Referenced in the introduction as a hierarchical robotic system that uses foundation models for embodied tasks. Cited as an example of the broader class of approaches that ST4VLA positions itself against — systems that rely on rule-based task decomposition rather than end-to-end spatial grounding.
> "Figure AI. Helix, 2024." (References)

**Shanghai AI Laboratory**
The primary institutional backer and research home of this work, with infrastructure for real-robot deployment including Franka Research 3 robots and ARX LIFT2 dual-arm platforms. The acknowledgment section references the broader InternVLA-M1 framework, signaling this is part of a larger coordinated research program.
> "This research is supported by Shanghai Artificial Intelligence Laboratory." (Acknowledgments)

---

## 4. People Identified

**Jiangmiao Pang — Shanghai AI Laboratory**
Corresponding author and apparent project lead. Pang leads the broader InternVLA-M1 initiative at Shanghai AI Lab, which this paper is a component of. His lab is producing a coherent, multi-paper research program on generalist robot policies with real deployment infrastructure. Investors evaluating Chinese Physical AI research ecosystems should track this group closely.
> "Corresponding author... This paper systematically analyzes the impact of spatial training on Vision-Language-Action (VLA) models and extends the manipulation of spatial data for generalist purposes within the InternVLA-M1 framework." (Acknowledgments)

**Jinhui Ye — HKUST / Shanghai AI Laboratory**
First author, also affiliated with HKUST. Has prior work on long-form video understanding, suggesting cross-domain expertise in temporal reasoning that likely informed the long-horizon manipulation design. The dual institutional affiliation indicates this is a significant cross-institutional collaboration.
> "Jinhui Ye, Fangjing Wang, Ning Gao, Junqiu Yu... Equal contribution." (Author list)

**Fangjing Wang, Ning Gao, Junqiu Yu — Equal Contributors**
Three equal first authors spanning Southern University of Science and Technology and Fudan University. Their equal contribution designation reflects genuine co-development of the core technical components — spatial grounding pre-training, gradient analysis methodology, and real-world evaluation infrastructure.

**Yanwei Fu — Fudan University**
Senior co-author from Fudan. Fu's presence alongside Zheng (SUSTech) and Pang (Shanghai AI Lab) reflects the multi-institution structure of Chinese Physical AI research that is increasingly competing with US and European labs.

**Chelsea Finn, Sergey Levine (cited prominently)**
Not authors of this paper, but their work on π₀ (Finn) and OXE/Octo (Levine) forms the baseline infrastructure that ST4VLA is evaluated against. The fact that a 3B-parameter model with a structured training recipe consistently beats these groups' systems is a meaningful signal about where the field is heading.

---

## 5. Operating Insights

### Restructure Your Data Pipeline Before Scaling Your Action Data Budget

The single most actionable finding in this paper is that spatial grounding data is a force multiplier on action data, but only when injected at the right stage. The scaling law result (Table 9) shows near-zero marginal returns below 1M spatial grounding pairs, then dramatically increasing returns above 2M. Any team planning a data collection campaign should be allocating budget to web-scale and robot-specific spatial grounding data (point prediction, bounding box annotation, trajectory labeling) before adding more teleoperation episodes. The paper provides a concrete template: combine datasets like RefCOCO, LLaVA-OneVision, RoboRefIt, and task-specific affordance data in a unified QA format, then run spatial pre-training before touching action data. The cost of spatial grounding data is substantially lower than teleoperation at scale.
> "Our experimental results reveal a nonlinear relationship between spatial data scale and model performance... At 3.0M pairs, the model achieves substantial improvement, with average performance rising from 61.4 to 77.9 — a remarkable 26.9% relative gain." (Section C.4)

### Spatial Prompting Is a Near-Zero-Cost Intervention With Outsized Returns

The spatial prompting mechanism — appending a simple natural language instruction like "Figure out how to execute it, then locate the key object needed" to each task instruction — is architecturally trivial but empirically powerful. The ablation shows this single prompt, versus a semantically empty random padding baseline, accounts for the difference between 58.5% and 77.9% average success rate (Table 10). Critically, the unified prompt outperforms more specific prompts that demand explicit coordinate outputs (box: 76.6%, point: 74.9%, trace: 73.9%). This means teams can implement this today without modifying their action prediction heads or output formats. Any team running VLA inference should be testing whether a spatial attention prompt in the instruction improves their real-world success rates.
> "The Random Padding baseline significantly underperforms the Unified Prompting (58.5% vs. 77.9%). This confirms that the performance gains in ST4VLA stem from the model explicitly attending to spatial semantics, rather than merely from the computational overhead of processing extra tokens." (Section C.5)

### Gradient Conflict Between Perception and Action Objectives Is Measurable and Solvable

The PSS metric introduced in this paper (Section 3.1, Appendix A) gives engineering teams a concrete diagnostic tool for a problem that currently manifests as unexplained performance degradation during co-training. If you are jointly training on VQA/grounding data and robot action data and seeing unstable loss curves or spatial capability degradation, you now have a method to quantify whether your objectives are in conflict. The fix — staged training with gradient attenuation (a factor of 0.5 on gradients flowing back from the action expert to the VLM) — is lightweight. The querying transformer connecting VLM to action expert is only 8.7 MB, meaning this architectural separation adds negligible inference cost.
> "Motivated by prior studies showing that direct gradient flow between action and VLM modules may distort multimodal knowledge, we introduce a gradient decay factor within the querying transformer. This attenuates the gradients propagated from the Action Expert back to the VLM (e.g., by a factor of 0.5), thereby preserving the Planner's semantic reasoning ability while still enabling effective joint optimization." (Section 2.1)

---

## 6. Overlooked Insights

### The Loss Weight Ratio Has a Physically Interpretable Optimum — And Getting It Wrong Costs 35+ Points

Buried in Appendix C.2 is a finding that deserves front-page placement: the ratio of spatial grounding loss to action loss during co-training is not a standard hyperparameter to sweep — it has a principled optimum. At 1:1 (equal weighting), manipulation performance collapses to 47.2% despite strong spatial grounding. At 1:20, performance also degrades to 68.3%. The sweet spot is 1:10, which the authors hypothesize "corresponds approximately to the proportion between the action chunk length and the average next-token prediction length in the multimodal data" (Section C.2, Table 7). This is a transferable heuristic: if your action chunk size is 16 tokens and your average spatial QA answer is ~1-2 tokens, weight action loss roughly 8-16x higher than spatial loss. Teams doing naive co-training with equal loss weights are likely leaving 20-35 percentage points of performance on the table.

### The 244K Simulation Demonstrations Pipeline Is Itself a Deployable Asset

The paper evaluates on a 200-task, 3,000+ object pick-and-place benchmark generated in Isaac-Sim via the GenManip framework — but the underlying synthetic data engine is the more important artifact. The paper states the model was post-trained on "244K pick-and-place demonstrations simulations generated in Isaac-Sim" (Section 3.3) using a scalable synthetic data engine described in Appendix F.3. For teams struggling with the cost and logistics of real-world data collection, this pipeline — which automatically rewrites instructions via GPT-4o-mini, randomizes object layouts, and validates executability — is a production-ready alternative to physical teleoperation for initial policy training. The paper shows that combining this simulation data with only 1K real trajectories (6 hours of teleoperation across 23 objects) is sufficient to achieve 65% average success in real-world generalization tests. The real-data requirement is far lower than most teams assume when spatial priors are properly established first.
> "We collected 1K pick-and-place trajectories involving 23 objects and 5 containers, which are used for post-training. Unlike the 200 simulated tasks, the post-training leverages both large-scale simulation data and real-world trajectories." (Section 3.4)