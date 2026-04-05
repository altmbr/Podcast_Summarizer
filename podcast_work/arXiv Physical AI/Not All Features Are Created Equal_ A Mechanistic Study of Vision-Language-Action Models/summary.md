# Not All Features Are Created Equal: A Mechanistic Study of Vision-Language-Action Models

**Podcast:** arXiv Physical AI Research
**Date:** 2026-04-05
**Processed:** 2026-04-05T09:04:08Z
**Participants:** Bryce Grant, Xijia Zhao, Peng Wang
**Source:** paper
**arXiv:** 2603.19233
**PDF:** https://arxiv.org/pdf/2603.19233

---

# Not All Features Are Created Equal: A Mechanistic Study of Vision-Language-Action Models

**Relevance Score for Physical AI Investors/Operators: High**
This paper opens the black box of VLA models — the dominant architecture class for generalist robot policies — and finds that what's inside is both more structured and more brittle than the field assumes. Six models, 394,000+ rollout episodes, four benchmarks. The findings directly affect how you build, debug, evaluate, and invest in robot learning systems.

---

## 1. Key Themes

### Vision Dominates Language — Even When Language Appears to Work

The most striking finding: VLA models are, at their core, visual-motor replay systems. When researchers injected baseline visual activations into episodes with blank language prompts on π₀.₅, task success recovered to 73–77% and action cosine similarity hit 0.999 — nearly identical to the baseline with correct prompts. The model ran coherent manipulation sequences with *no language input at all*.

This isn't a π₀.₅ quirk. Table 6 confirms visual pathway dominance "Y" across all six architectures tested, including ACT (which has no language pathway), SmolVLA, GR00T, OpenVLA-OFT, and X-VLA.

> "The visual pathway dominates action generation across all architectures: injecting baseline activations into null-prompt episodes recovers near-identical behavior." — Abstract

The practical implication: when your VLA-powered robot fails, the language instruction is rarely the culprit. The visual scene is doing the heavy lifting.

### Language Sensitivity Is a Property of the Task, Not the Model

Across every architecture tested, the same pattern emerges: if the visual scene uniquely identifies the task (one object, one goal), language is ignored. If the scene is ambiguous (multiple objects, multiple possible goals), language becomes critical.

On X-VLA's `libero_goal` benchmark (where multiple goals share a scene), feeding a wrong prompt drops success from 94% to 10%. On `libero_object` (single object, unambiguous), performance holds at 60–100% *regardless of what prompt is given*. This pattern replicates on OFT, GR00T, and SmolVLA.

> "Language sensitivity depends on task structure, not model design: when visual context uniquely specifies the task, language is ignored; when multiple goals share a scene, language becomes essential." — Abstract

For operators: your language-conditioning evaluation needs to test *ambiguous scenes*, not easy pick-and-place. Benchmark numbers on single-object tasks tell you almost nothing about whether the model actually follows instructions.

### Motor Programs Are Spatially Bound, Not Abstractly Represented

Cross-task injection — replacing one task's neural activations with another's — causes 100% task failure across all six models. But the robots don't freeze. They reach toward *where the source task's objects would have been*, executing what the authors call "spatially grounded motor programs."

On X-VLA, 99.8% of injected episodes aligned more closely with the source trajectory than the destination. On π₀.₅, 99.6%. The robot is executing the wrong task's movements *at the right scene coordinates for the wrong task*.

> "The robot reaches toward where source objects would have been, executing what we term spatially grounded motor programs: action sequences bound to specific scene coordinates rather than abstract task representations." — Section 4.3

This explains why VLAs trained on LIBERO collapse under position perturbations (cited prior work shows 97% → 0% under 0.2-unit shifts). The motor program is literally a coordinate-indexed lookup, not a relational plan.

### Multi-Pathway Architectures Have Consistent Functional Specialization

For the three architectures with distinct internal pathways (π₀.₅ with PaliGemma + Expert, SmolVLA with VLM + Expert, GR00T with DiT + Eagle + VL-SA), a consistent division of labor emerges:

- **Expert/action pathways**: encode motor programs — the "how." Injecting wrong expert activations produces active misdirection (robot reaches to wrong locations, continues for 231–337 steps).
- **VLM pathways**: encode goal semantics — the "what." Injecting wrong VLM activations produces passive stalling (robot runs to the 520-step timeout).

Expert pathway injection causes 2× greater behavioral displacement than VLM pathway injection across SmolVLA's 732 MetaWorld cross-task pairs (15.8% vs. 9.0% source-like behavior).

> "Expert pathways cause 2× greater behavioral displacement than VLM pathways... expert pathways encode motor programs while VLM pathways encode goal semantics." — Section 4.5

### SAE-Based Interpretability Works for Robots — With One Critical Caveat

Sparse autoencoders, the interpretability tool that cracked open LLMs, can be applied to VLA models and recover meaningful structure: 82+ distinct manipulation concepts (motion verbs, object types, spatial relations), identifiable via contrastive selection. But there's a hard constraint that doesn't exist in language models: **you must process activations per action-token, not as a pooled mean**.

Mean-pooling across action tokens — the natural default from LLM practice — destroys task performance catastrophically. On π₀.₅ LIBERO-10, mean-pooled SAE reconstruction produces 0.4% success versus 69.9% for per-token processing, despite achieving 95–98% explained variance.

> "Mean-pooling activations across token positions destroys action-critical information, causing catastrophic task failure despite high reconstruction quality." — Section 1

The exception is X-VLA (Florence-2 backbone), where mean-pooling actually *improves* rollout fidelity — suggesting this is architecture-dependent and not a universal rule.

---

## 2. Contrarian Perspectives

### Bigger VLM Backbones Don't Make Better Language Followers

The conventional assumption: scale your VLM backbone, improve language grounding, get better instruction-following robots. This paper systematically undermines that story. OpenVLA-OFT uses a 7B Llama-2 backbone — the largest model tested — and shows the same suite-dependent language blindness as the 450M SmolVLA and the 1B X-VLA.

π₀.₅'s PaliGemma backbone encodes language prompts internally with 99.3% classification accuracy at layer 17 (a linear classifier can perfectly distinguish prompt categories from the activations) — yet behavioral ANOVA across 3,396 episodes shows *no statistically significant difference* in task outcomes across any prompt variation (p=0.247, η²=0.012).

> "Despite behavioral invariance on π₀.₅, linear classifiers trained on layer 17 activations predict prompt category with 99.3% accuracy: prompts are encoded but not used." — Section 4.4

The implication that cuts against industry consensus: improving VLM benchmark scores (as measured by standard NLP benchmarks) does not predict better language following in manipulation. A separately cited paper (VLM4VLA) makes this explicit — "VLM benchmark performance does not predict VLA task success; language understanding and visuomotor competence are decoupled."

### Representation Width Does Not Predict Robustness

A natural assumption in scaling: wider representations (higher-dimensional activations) should be more robust to perturbation. The causal ablation results directly contradict this.

SmolVLA uses a 480-dimensional expert pathway and shows the *highest* causal sensitivity — 28% zero-effect rate, meaning 72% of ablations have measurable impact. OpenVLA-OFT uses a 4096-dimensional backbone (8.5× wider) and shows 92% zero-effect rate, meaning it's far more resilient. X-VLA at 1024 dimensions approaches OFT's resilience (82% zero-effect) despite matching π₀.₅'s hidden size.

> "Causal sensitivity does not follow representation width: X-VLA approaches OFT despite sharing π₀.₅'s 1024-dim hidden size." — Figure 4 caption

Architecture and training regime, not sheer width, determine whether individual features are load-bearing. This matters for anyone trying to prune, compress, or fine-tune VLAs in deployment.

### Fine-Tuning Creates Coordinate-Specific Motor Programs, Not Abstract Skills

The conventional story of transfer learning in robotics: a pretrained VLM provides rich semantic understanding; fine-tuning layers task-specific skills on top of that foundation. The spatial binding analysis tells a different story.

Fine-tuning concentrates representational changes in the *final third* of the network (layers L20–L31 in the 32-layer OFT backbone), where cosine similarity to the base model drops to 0.917–0.938. Early and mid layers remain near-identical to the untuned backbone (similarity >0.999 through L15). The coordinate-specific action sequences revealed by cross-task injection are encoded precisely in the layers that change most during fine-tuning.

> "The concentration of divergence in the final third of the backbone shows that fine-tuning reshapes late-layer representations to encode action-relevant motor programs while preserving early/mid-layer visual and linguistic features." — Section E.4

Translation: you're not fine-tuning a flexible reasoner onto a new task. You're overwriting the last few layers with hardcoded workspace coordinates. That's why 0.2-unit position shifts kill performance.

---

## 3. Companies Identified

**Physical Intelligence (π₀.₅, π₀, π₀.₆*)**
*Physical AI startup, developer of π₀ model family*
The primary architecture studied in depth. π₀.₅'s dual-pathway design (PaliGemma + Expert) is the paper's most thoroughly analyzed system, with 65,000+ episodes and 36 SAEs trained. The finding that PaliGemma encodes prompts with 99.3% accuracy but doesn't use them behaviorally is a direct challenge to claims about language-conditioned generalization. Also cited: π₀.₆*, their RL-from-experience follow-up.
> "Injecting only layer 0 achieves comparable results (0.997); task-relevant information is already encoded in the first transformer layer." — Section 4.2

**NVIDIA (GR00T N1.5)**
*Semiconductor and AI infrastructure company, robotics foundation model*
GR00T's triple-pathway architecture (DiT + Eagle LM + VL-SA) is confirmed to exhibit the same expert/VLM specialization as π₀.₅ and SmolVLA. DiT layers are most ablation-sensitive (40–80% success drop per zeroing); VL-SA layers are most resilient. 164,700+ episodes analyzed — the largest single-model dataset in the study.
> "DiT layers are most ablation-sensitive (40–80% success drop); Eagle LM layers show moderate sensitivity; VL-SA layers are the most resilient." — Section 4.5

**Hugging Face (SmolVLA)**
*Open-source AI platform, developer of SmolVLA*
SmolVLA's 450M interleaved VLM-expert architecture is validated for pathway specialization — expert layers cause 2× greater behavioral displacement than VLM layers. Also the most causally sensitive architecture tested (28% zero-effect rate), meaning individual features are most load-bearing. Evaluated on both LIBERO and MetaWorld.
> "Expert injection causes ~2× greater behavioral displacement than VLM layers (15.8% vs. 9.0% source-like behavior across 732 MetaWorld pairs)." — Section 4.3

**Stanford / UC Berkeley / Toyota Research Institute (OpenVLA, OpenVLA-OFT)**
*Academic/industry collaboration, open-source VLA*
OpenVLA-OFT (7B, continuous L1 regression) is the most resilient architecture to concept ablation (92% zero-effect rate) but the weakest at null injection recovery (14% vs. π₀.₅'s 73%). The discrete tokenization finding — that base OpenVLA with 256-bin tokenization produces 0% task success under SAE intervention at all but the final layer — is a critical negative result with broad implications.
> "Action representation, not model scale, determines SAE applicability." — Appendix C.1

**X-VLA / Zheng et al. (Microsoft Research Asia / affiliated)**
*Cross-embodiment VLA based on Florence-2*
X-VLA's Florence-2 soft-prompted backbone produces the most extreme visual pathway dependence: zeroing *any single one* of its 24 layers causes 0% task success on both LIBERO and SimplerEnv. It's also the only architecture where mean-pooled SAEs outperform per-token SAEs in rollout fidelity — a Florence-2-specific property with significant implications for how to apply interpretability tools.
> "Every single layer is critical: zeroing any one of the 24 layers causes 0% task success on both LIBERO and SimplerEnv-WidowX." — Section 4.2

**Stanford / Berkeley / CMU (ACT / ALOHA)**
*Academic manipulation platform, CVAE-based policy*
Serves as the language-free control. Cross-task injection between TransferCube and Insertion tasks produces outputs identical to the uninjected baseline (cosine similarity = 1.0, bit-identical action arrays). Confirms that visual pathway dominance and cross-task failure hold even without any language component — ruling out VLM-specific artifacts as the cause.
> "Visual pathway dominance and cross-task failure thus hold even for vision-only policies, which rules out VLM-specific artifacts." — Appendix C.2

---

## 4. People Identified

**Bryce Grant**
*Case Western Reserve University, AISM Lab*
Co-first author. Led the activation injection and cross-task displacement analysis. The 394,000-episode experimental infrastructure is a significant engineering achievement for an academic group.
> Contact: bag100@case.edu; Lab: https://cwru-aism.github.io/vla-interp-page/

**Xijia Zhao**
*Case Western Reserve University, AISM Lab*
Co-first author (equal contribution). Led SAE training and causal ablation analysis across 424 trained SAEs. The per-token vs. mean-pooled finding is the most immediately actionable technical contribution for practitioners building interpretability tooling.
> Contact: xxz1277@case.edu

**Peng Wang**
*Case Western Reserve University, AISM Lab — Corresponding Author*
PI. The lab's focus on mechanistic interpretability for physical AI is an emerging niche with few serious academic competitors. Their Action Atlas platform (action-atlas.com) represents an unusual commitment to practitioner-accessible tooling.
> Contact: pxw206@case.edu

**Chelsea Finn / Sergey Levine (Stanford / UC Berkeley)**
*Not authors, but central figures whose work is validated/challenged*
Physical Intelligence's π₀/π₀.₅ architecture (Finn, Levine, et al.) is the most-studied model in the paper. The finding that π₀.₅ ignores language instructions despite encoding them challenges the implicit claims of language-conditioned generalization in the Physical Intelligence papers.
> Referenced as Black et al. (2024) and Physical Intelligence (2025) throughout.

**Björck et al. / NVIDIA Research (GR00T)**
*NVIDIA Research team*
GR00T N1.5's triple-pathway architecture generates the paper's largest dataset (164,700+ episodes). The confirmed pathway specialization in a humanoid-targeted architecture is directly relevant to anyone building on or competing with NVIDIA's robotics foundation model stack.
> Referenced as Bjorck et al. (2025) throughout.

**Häon, Stocking, Chuang, Tomlin (UC Berkeley / BAIR)**
*Prior work on VLA mechanistic interpretability*
The closest prior work — SAE steering on π₀ and OpenVLA. This paper extends their single-architecture studies to cross-architecture validation at 100× the episode scale.
> "We extend these single-architecture studies to cross-architecture validation across six models." — Section 2

---

## 5. Operating Insights

### Runtime Failure Diagnosis via Pathway Monitoring Is Now Tractable

The pathway specialization finding has a direct operational application: you can distinguish *motor errors* from *goal misidentification* at inference time by monitoring which pathway's activations are anomalous, without any rollout.

When expert activations are wrong, the robot actively misdirects — reaching to incorrect positions, executing full trajectories toward wrong targets (231–337 step episodes). When VLM activations are wrong, the robot passively stalls (runs to the timeout limit). These are observably different failure modes, and they map cleanly to separable activation subspaces confirmed by subspace injection.

> "Probing expert vs. VLM activations distinguishes motor errors from goal misidentification... monitoring pathway-specific activation norms distinguishes motor errors from goal errors." — Section 4.5

For a CTO deploying a multi-pathway VLA (π₀.₅, SmolVLA, GR00T): build a lightweight probe on expert vs. VLM activations as a real-time failure detector. The paper shows that linear probes achieve AUC=0.93 for success prediction on π₀.₅ expert activations — this is a deployable monitor, not just a research tool.

### Benchmark Evaluation Is Systematically Misleading About Language Grounding

If you're evaluating a VLA for a use case involving ambiguous multi-object scenes or compositional instructions, standard LIBERO-Object or pick-and-place benchmarks will overstate language following by a wide margin. The paper demonstrates that `libero_object` results (single object, visually unambiguous) are near-completely language-immune across all architectures — meaning a model that "achieves 97% on LIBERO" may be doing so with zero language comprehension.

The correct evaluation protocol for language-conditioned deployment: test on `libero_goal`-style benchmarks where multiple plausible goals share a visual scene, or the MetaWorld hard/very-hard difficulty levels where SmolVLA shows a 21pp sensitivity gap under null prompts.

> "SmolVLA mirrors this on MetaWorld: easy tasks are language-insensitive while harder tasks show greater sensitivity. The common factor is whether visual context alone identifies the target, not model design." — Section 4.4

For procurement or investment due diligence: ask vendors to show performance under wrong-object-name prompts on goal-ambiguous scenes, not just standard benchmark accuracy. The difference between 94% (correct prompt) and 10% (wrong prompt) on `libero_goal` is the actual measure of language grounding.

---

## 6. Overlooked Insights

### Discrete Action Tokenization Kills SAE Applicability — With a Direct Fix

Buried in Appendix C.1: the researchers initially tried to apply SAEs to base OpenVLA, which uses discrete 256-bin tokenization. Despite achieving excellent SAE reconstruction quality (R²=0.87–0.96), hooking the SAE into the forward pass produced 0% task success at all but the final layer. The reason: argmax binning means even small reconstruction errors shift the selected action bin, and errors compound across the 7-token autoregressive sequence.

Switching to OpenVLA-OFT (continuous L1 regression) restores full SAE applicability at 99.2% success.

> "Action representation, not model scale, determines SAE applicability." — Appendix C.1

This has a direct implication for anyone building interpretability tooling, fine-tuning pipelines, or activation-based monitors for VLAs: **check the action head architecture first**. Discrete tokenization (RT-2 style) makes mechanistic intervention essentially impossible without architectural changes. This also means that FAST (DCT-compressed tokenization) and other discrete action representations may have the same fundamental barrier to interpretability and activation steering.

### The First Forward Pass Is the Entire Policy — Everything After Is Execution

Appendix G.6 contains a striking finding with major implications for intervention timing: ablating features only at step 0 (the very first forward pass) causes complete task failure. Ablating at step 1 has no effect. Steps 200+ have no effect.

> "The first forward pass commits the robot to a trajectory... step 0 is uniquely critical for task success." — Appendix G.6, Table 17

This means the entire motor program is committed at trajectory initiation. GR00T's temporal ablation analysis (Table 15) confirms this across 160 conditions: early-window DiT ablation (-50.3pp) is nearly as severe as full-episode ablation (-50.8pp), while mid- and late-window ablation causes only -12pp.

For deployment engineers: your error recovery window is essentially zero. If the first perception-to-action cycle produces a wrong trajectory commitment (wrong object, wrong approach vector), subsequent corrections via prompt changes or environmental feedback will not redirect the policy. This is a fundamental architectural limitation of behavior-cloned VLAs that motivates closed-loop RL fine-tuning or explicit replanning triggers at the system level — not just better models.