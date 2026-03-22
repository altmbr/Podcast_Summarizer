# Sparse Autoencoders Reveal Interpretable and Steerable Features in VLA Models

**Podcast:** MIT Research
**Date:** 2026-03-19
**Processed:** 2026-03-22T00:07:25Z
**Participants:** Aiden Swann, Mac Schwager, et al. (MIT)
**Source:** paper
**arXiv:** 2603.19183
**PDF:** https://arxiv.org/pdf/2603.19183

---

# Sparse Autoencoders Reveal Interpretable and Steerable Features in VLA Models
**Stanford University | Swann, McGranahan, Buurmeijer, Kennedy, Schwager | arXiv:2603.19183**

---

## 1. Key Themes

### VLA Models Are Mostly Memorizing, Not Learning

The headline finding is uncomfortable: the vast majority of what VLA models "learn" during fine-tuning is rote memorization of specific training episodes, not transferable manipulation skills. Using Sparse Autoencoders (SAEs) to decompose internal model representations, the authors find that on LIBERO, **98.43% of features** in the primary π0.5 model are classified as memorized, not general. Even on the far more diverse DROID dataset, **94.92% of features** remain memorized at the key analysis layer (PG5).

> "We observe significant episode-level memorization in all cases... fine-tuning on diverse datasets such as DROID leads to comparatively more general features [but] the absolute portion of memorized features remains high." (Section 4.2)

This provides the first mechanistic (not just behavioral) explanation for why VLAs pass benchmarks but fail under perturbation — a finding corroborated by LIBERO-PRO, which showed models with >90% benchmark success rate "collapse to near-zero under systematic perturbations." (Section 1)

### General Motion Primitives Do Exist and Can Be Surgically Activated

Despite the memorization dominance, a meaningful subset of features corresponds to genuine, transferable motion primitives: grasp onset, pre-grasp alignment, object transport, task completion, and gripper aperture. Critically, these features are *causal*, not merely correlational. When the researchers inject these feature vectors directly into the model's computation stream during inference, the robot behavior changes predictably and consistently with the feature's meaning — across different tasks and scenes.

> "Steering a pre-grasp alignment feature causes the policy to hover above objects instead of continuing to grasp... steering a transport feature causes the robot to completely skip relevant object grasps and move directly to the goal location." (Section 4.4)

This is the first demonstration that individual directions in a VLA's internal representation space map cleanly onto discrete robot behaviors that can be externally triggered.

### Dataset Scale and Diversity Is the Primary Lever for Generalization

The paper establishes a clear, measurable relationship between training data diversity and the ratio of general-to-memorized features — and for the first time, this can be quantified *without running a single robot rollout*.

> "Moving from LIBERO-GOAL to full LIBERO and then to DROID, we observe a steady increase in the share of general features." (Section 4.2)

DROID has 1,545 unique task instructions vs. 130 in LIBERO. The DROID-trained model shows ~10x more general features at the model-wide average level (10.81% vs. 2.63%). This gives teams a concrete proxy metric for evaluating data collection strategies before deploying hardware.

### Fine-Tuning Actively Destroys Generalization — And Can Be Monitored

The paper tracks feature generality across training checkpoints and finds that fine-tuning degrades the ratio of general features monotonically from the very first steps — even though the π0.5 base model was pre-trained on "over 10,000 hours of cross-embodiment robot data."

> "Although the π0.5 base is trained on over 10,000 hours of cross-embodiment robot data, catastrophic forgetting appears to begin once fine-tuning begins." (Section 4.5)

Knowledge Insulation (KI) — a technique that stops gradients from corrupting the VLM backbone's representations — reverses this decline. The median generality classifier score for KI models (0.206) exceeds all standard fine-tuning checkpoints (0.179–0.190). This means teams can now use SAE feature metrics as a lightweight training-time signal, without needing costly real-world evaluations.

### ~80% of Extracted SAE Features Are Human-Interpretable

Across six model/layer combinations, the authors find a 79.17% interpretability rate on a random sample of 120 features. This validates that the SAE approach — well-established in LLM interpretability — transfers meaningfully to the embodied control domain.

> "We find that the vast majority of the SAE features produced by our primary model show strong interpretability... Total: 95 interpretable out of 120 sampled = 79.17%." (Table 1, Section 4.1)

---

## 2. Contrarian Perspectives

### Benchmark Performance Is a Misleading Signal for Deployment Readiness

The conventional wisdom is that higher task success rates on benchmarks like LIBERO indicate a more capable and generalizable policy. This paper argues the opposite: a model can achieve high benchmark scores primarily through memorization of scene layouts and action sequences, with almost no transferable understanding.

> "Models that exceed 90% success rate under the original protocol can collapse to near-zero under systematic perturbations, implying that these policies may rely on rote memorization of action sequences and environment layouts rather than generalizing to new perceptual inputs." (Section 1, citing LIBERO-PRO)

The mechanistic evidence here — 98.43% memorized features in a high-performing LIBERO model — gives this claim its teeth. Most robotics companies are optimizing for benchmark numbers. This paper suggests they may be measuring the wrong thing.

### More Fine-Tuning Steps Make Your Robot Policy Worse, Not Better

The standard practice in deploying VLAs is to fine-tune extensively on task-specific data to maximize performance. This paper's training checkpoint analysis suggests that additional fine-tuning steps consistently reduce the proportion of generalizable features, and that this degradation begins immediately.

> "As we increase the number of fine-tuning steps, generality decreases... Episode coverage decreases while relative run length increases with training steps." (Section 4.5, Figure 6)

This is a direct challenge to the "more compute = better model" assumption. The implication is that fine-tuning schedules need active generality monitoring, not just loss curves and success rates.

### The Safety Problem for Robots Is Semantic, Not Just Geometric

The paper makes an explicit argument that the safety paradigm for robotics needs to expand beyond collision avoidance and force limits to include semantic and task-level understanding. Current robots can "safely" avoid collisions while still catastrophically misunderstanding what they're supposed to do.

> "'Safety' should no longer be just geometric or control-theoretic, but also semantic, situational, and task-dependent. For example, a home robot must avoid contact with hot surfaces and handle sharp or fragile objects appropriately." (Section 1)

Most robotics safety work is focused on physical constraints. This paper's interpretability tooling is positioned as the foundation for semantic safety monitoring — knowing *why* a robot is doing what it's doing, not just whether it will hit something.

---

## 3. Companies Identified

**Physical Intelligence (π)**, Developer of π0 and π0.5 VLA models; primary model studied in this paper. The π0.5 model's internal representations are the main subject of analysis, and both LIBERO and DROID fine-tuned variants are used. The Knowledge Insulation technique (developed internally at Physical Intelligence) is validated by this paper's feature metrics.
> "We use two fine-tuned variants open-sourced by Pi: π0.5-LIBERO and π0.5-DROID, both fine-tuned on the respective datasets with a technique known as knowledge insulation." (Section A.1.1)

**Google DeepMind**, Originating organization behind RT-2 (cited as the primary example of the VLA model class) and PaliGemma (the VLM backbone inside π0.5). The SigLIP image encoder used in π0.5 is also a Google product. The interpretability findings about PaliGemma layers directly affect how DeepMind-derived architectures are understood.
> "RT-2: Vision-language-action models transfer web knowledge to robotic control." (Reference [1], Section 1)

**Stanford University / Open-Source VLA Community**, The paper's open-source Dr. VLA codebase provides the field with tools for SAE training, feature evaluation, and policy steering. Researchers on OpenVLA (an open-source VLA built on Llama 2) are co-authors and collaborators.
> "We offer Dr. VLA, an open-source and user-friendly software package for SAE training, feature evaluation, and policy steering in VLAs." (Abstract)

**Meta AI (Llama)**, OpenVLA uses a Llama 2 7B backbone (32 transformer layers, d=4096). The paper's analysis of OpenVLA shows even lower generalization than π0.5 (99.55% memorized features), likely due to the smaller fine-tuning dataset used.
> "OpenVLA is an open-source VLA built on a Llama 2 7B backbone... We use the publicly available checkpoint fine-tuned on the LIBERO Spatial suite." (Section A.1.1)

---

## 4. People Identified

**Aiden Swann**, Stanford Mechanical Engineering / Aeronautics & Astronautics. Lead author; primary correspondence. NSF GRFP Fellow. Driving the application of LLM mechanistic interpretability techniques to embodied AI.
> "We propose a technique to extract interpretable, general, and steerable features from VLA models using Sparse Autoencoders." (Abstract)

**Monroe Kennedy III**, Stanford, Departments of Mechanical Engineering and Computer Science. Senior faculty advisor on the project. A key figure in Stanford's Physical AI research agenda connecting control theory and learned robot policies.
> Affiliation listed as corresponding senior author. (Author list)

**Mac Schwager**, Stanford Aeronautics & Astronautics. Senior faculty advisor. Known for multi-robot systems and learning-based control; this paper extends his lab's work into the interpretability of large-scale VLA policies.
> Affiliation listed as senior author. (Author list)

**Hugo Buurmeijer**, Stanford Aeronautics & Astronautics. Co-author on this paper and also co-author of the companion paper "Observing and Controlling Features in Vision-Language-Action Models" (Buurmeijer et al. 2026), which uses linear probes for VLA intervention. A key emerging researcher at the intersection of control theory and VLA interpretability.
> "Buurmeijer et al. span both observation and intervention of VLAs using linear probes... they propose leveraging SAEs to discover features without explicit labels as a direction of future work." (Section 2.2, Reference [24])

**Lachlain McGranahan**, Stanford Aeronautics & Astronautics. Co-lead author (co-correspondence). Instrumental in the feature classification methodology and steering experiments.
> Correspondence listed alongside Aiden Swann. (Author list)

---

## 5. Operating Insights

### Use SAE Feature Metrics as a Cheap Proxy for Deployment Readiness — No Robot Required

The most immediately actionable finding for engineering teams is that generality of a fine-tuned VLA policy can be estimated from internal activations alone, without running any rollouts in simulation or on hardware. The four metrics — episode coverage, onset count, activation magnitude, relative run length — can be computed on your training data after fine-tuning.

> "Because SAEs do not require any rollouts, simulated or otherwise, they can be applied in a lightweight fashion during training. For example, the presence of episode-specific features can be used to diagnose the brittleness of common VLA fine-tuning procedures." (Section 5)

For teams spending significant engineering time on hardware evaluation loops to check generalization, this is a potential order-of-magnitude speedup. A shift toward more general features (higher episode coverage, lower relative run length) is a training-time signal that the model is learning transferable skills rather than memorizing your demos.

### Knowledge Insulation Should Be a Default, Not an Optional Add-On

The paper validates that Knowledge Insulation — which preserves the VLM backbone's pre-trained representations during robot fine-tuning — measurably shifts the internal feature distribution toward generality. The effect is visible in both the feature metrics (Figure 6) and the classifier output distribution (median generality score 0.206 for KI vs. 0.179–0.190 for standard fine-tuning).

> "Knowledge Insulation appears to reverse this decline [in generality]... The KI model shifts the distribution towards generality with higher median than AE-finetuned models at comparable training steps." (Section 4.5)

Any team fine-tuning π0.5 or similar VLMs on task-specific robot data without KI or an equivalent representation-preserving technique is likely accelerating memorization with each training step. This is not a subtle effect — it shows up at the mechanistic level within the first 10k fine-tuning steps.

### Build Runtime Monitors Around General vs. Memorized Feature Activation

The paper identifies a practical path to deployment-time safety monitoring: detect when a policy is executing based on memorized scene features vs. general manipulation primitives. A policy relying on memorized features in a novel environment is likely to fail or behave unpredictably.

> "At test time, these features can be used within a runtime monitor, which alerts users when a policy is leveraging a memorized trajectory rather than utilizing general features." (Section 5)

This is directly implementable today using the open-source Dr. VLA codebase. For teams deploying in variable environments (warehouses, homes, unstructured industrial settings), this monitoring layer could function as a confidence gate — flagging when the robot is "outside" the memorized regime before a failure occurs, rather than after.

---

## 6. Overlooked Insights

### The Interpretable Features Emerge from Robot Fine-Tuning, Not from Pretrained Vision Encoders

A critical but easily missed control experiment: the authors train SAEs on the frozen pretrained SigLIP encoder (Google's vision model, which has never seen robotics data) and compare its features to those from the fine-tuned VLA. The pretrained encoder produces dense, unstructured activations with no event-locked temporal patterns. The general manipulation primitives — grasp onset, transport, pre-grasp alignment — only appear *after* robotic fine-tuning.

> "The pretrained SigLIP model produces a qualitatively different and much denser activation pattern, lacking the event-locked structure characteristic of the general features we identify in later layers. This suggests that the interpretable features reported in our main results are not inherited from the pretrained visual representations but instead emerge during robotic fine-tuning." (Section A.4.2)

The implication: the VLM backbone is not "bringing" manipulation knowledge from internet pre-training. Robot-specific manipulation primitives are learned from robot data. This matters for architectural decisions — teams debating how much to rely on frozen vision backbones vs. end-to-end fine-tuning should note that the general features this paper identifies as most useful for generalization are precisely the ones created by fine-tuning, not inherited from the base model.

### The Generality Classifier Systematically Undercounts General Features — Especially for Specialized Skills

The automated classifier used to categorize features has a known failure mode: features that activate exactly once per episode (mean onset count ≈ 1.0) across a semantically coherent but proportionally small task category get misclassified as memorized. The paper identifies a "lid grasping" feature in DROID that activates correctly across 86% of lid-related episodes and 336 additional episodes — but because lid tasks are only 6.7% of the total DROID dataset, its episode coverage (0.226) falls below the classifier's decision boundary.

> "F1381 fires in 116 of the 135 episodes whose task instructions contain the word 'lid' (86% recall within that subset)... However, because lid-related episodes constitute only 6.7% of the DROID dataset, the episode coverage of 0.226 falls below the classifier's decision boundary." (Section A.5.1)

This has a direct strategic implication: the already-alarming memorization statistics (94–99% memorized features) are likely *overestimates* of true memorization. Specialized skill features — exactly the kind needed for long-tail task coverage in real deployments — are being miscounted as memorized. Teams building task-specific capabilities (e.g., a robot that must handle a specific object category reliably) should not interpret low episode coverage as evidence of poor generalization. The evaluation methodology needs dataset-diversity-aware normalization that the field has not yet standardized.