# Open-World Task and Motion Planning via Vision-Language Model Generated Constraints

**Podcast:** MIT Research
**Date:** 2026-03-25
**Processed:** 2026-03-25T09:04:05Z
**Participants:** Nishanth Kumar, Caelan Reed Garrett, et al. (MIT)
**Source:** paper
**arXiv:** 2411.08253
**PDF:** https://arxiv.org/pdf/2411.08253

---

# OWL-TAMP: VLM-Generated Constraints for Open-World Robot Planning

**Paper:** *Open-World Task and Motion Planning via Vision-Language Model Generated Constraints*
**Authors:** Kumar, Shen, Ramos, Fox, Lozano-Pérez, Kaelbling, Garrett (MIT CSAIL / NVIDIA Research)

---

## 1. Key Themes

### VLMs Are Good at "What," TAMP Is Good at "How" — OWL-TAMP Bridges Both

The core insight is a clean division of labor: VLMs handle natural language interpretation and commonsense reasoning; TAMP handles geometric feasibility, collision avoidance, and kinematic constraints. Neither alone solves real manipulation problems. The paper proves this empirically — pure VLM approaches (Code as Policies) achieved **0% success** on 7 of 10 tasks, while pure TAMP with direct language translation achieved only **32% overall success**. OWL-TAMP achieved **92% overall success across all 10 tasks** (Table 1, Section 6.1).

### The "Constraint Contract" Is the Architectural Innovation

Rather than having a VLM generate full plans or raw actions, OWL-TAMP has VLMs generate *constraints* in two forms: (1) discrete plan sketches that specify action ordering, and (2) continuous constraints written as Python code that restrict where objects can be placed or how actions must be parameterized. As the authors describe: *"Our key insight is that we can leverage the commonsense and language-grounding capabilities of VLMs to guide TAMP systems through dynamically generated constraints."* (Section 1). This constraint-as-interface design means the VLM never needs to solve geometry — it just narrows the search space.

### Zero-Shot Generalization Without Demonstration Data or Fine-Tuning

OWL-TAMP handles tasks entirely outside its pre-defined symbolic vocabulary — concepts like "near," "upright," "fits inside," "not vegan" — without any task-specific training or demonstrations. This is a direct contrast to VLA approaches like π₀ or GROOT N1, which require fine-tuning on domain-specific data. The paper explicitly states: *"our approach combines VLMs with generic, domain-independent TAMP systems to solve tasks with no requirement for additional demonstrations or learning in simulation."* (Section 2). The system was deployed on 19 different real-world tasks with **no changes to the system across tasks** (Section 6.2).

### Backtracking Is Non-Negotiable for Complex Manipulation

One of the clearest ablation results: removing backtracking ("No backtrack") drops overall success from 92% to 60% (Table 1). Tasks requiring obstacle removal — where a robot must first move an obstructing object before grasping a target — fail entirely without it. This validates that geometry-aware search, not just LLM-guided action sequencing, is essential for deployment in cluttered real environments.

### Soundness (False Positive Rate) Is as Important as Success Rate

OWL-TAMP produced **only one false positive across all tasks** — a case where the system declared success incorrectly. Competing approaches like "Direct Translation" and "No Continuous Constraints" had dramatically higher false positive rates, meaning they declared tasks complete when they weren't (Figure 4, Section 6.1). For deployed systems, a robot that thinks it succeeded when it didn't is arguably worse than one that correctly identifies failure.

---

## 2. Contrarian Perspectives

### Scaling VLA Training Data Is Not the Only Path to Open-World Manipulation

The dominant narrative in robotics AI is that more robot demonstration data → better generalization. OWL-TAMP directly challenges this. The system handles tasks like *"throw away anything not vegan in the purple bin"* or *"weigh the shortest object and put it in the bin"* — requiring real-world commonsense and physical measurement — without a single robot demonstration. The paper notes that VLA approaches *"require finetuning on some task and environment-specific data when adapting to novel setups and embodiments"* (Section 2), while OWL-TAMP uses *"pretrained VLMs without finetuning to generate constraints that expand TAMP's capabilities without task-specific demonstration or exploration data"* (Section 2). For operators deploying robots across diverse, unpredictable environments, this is a fundamentally different scaling strategy.

### LLMs Cannot Directly Plan Long-Horizon Manipulation — The Evidence Is Categorical

Many robotics companies are betting on foundation models to plan multi-step tasks end-to-end. The paper's Code as Policies (CaP) baseline — representing this approach — achieves **0% success on 7 of 10 tasks** and **0% overall** in its direct-execution form (Table 1). Even the sampling-augmented variant (CaP-sample, with a 2,500-sample budget) achieves only **14% overall success**. The paper cites Kambhampati (2024): *"Can large language models reason and plan?"* (Section 2, Reference 32) — the answer, in this context, is clearly no for tasks requiring continuous geometric reasoning. The failure mode is fundamental: *"they struggle to reason about continuous parameter values and geometry (e.g., synthesizing collision-free grasps and placements) without task-specific fine-tuning."* (Section 1).

### Approximately 50% of OWL-TAMP's Runtime Is Spent Querying Foundation Models — This Is the Real Bottleneck

The community often treats inference latency as a solved problem for deployed systems. Table 3 shows that across tasks, roughly 40–85% of wall clock time is consumed by VLM queries, not robot execution or planning. The paper explicitly acknowledges: *"the overall runtime of our method could be significantly reduced by reducing the time taken for foundation model querying."* (Appendix A.4). For real-time or high-throughput applications, the foundation model API call — not motion planning or kinematics — is the critical path. This has direct implications for on-device vs. cloud inference architecture decisions.

---

## 3. Companies Identified

**NVIDIA Research**
Co-affiliation for multiple authors (Kumar, Shen, Ramos, Fox, Garrett). NVIDIA is directly invested in this research direction. Relevant to their broader Isaac robotics platform and foundation model strategy for physical AI. The paper notes: *"Work conducted partially during an internship at NVIDIA Research."* (Author affiliations). NVIDIA's GR00T N1 is cited as a VLA approach that requires fine-tuning, positioning OWL-TAMP as a complementary or alternative architecture.

**OpenAI**
GPT-4o is the VLM used across all experiments: *"We use GPT-4o as the VLM across all methods."* (Section 6). This makes OpenAI's model a critical dependency in the entire system. API latency and cost are directly reflected in the 40–85% of wall clock time spent on VLM queries. Any degradation or pricing change in GPT-4o has direct operational consequences for this architecture.

**Boston Dynamics AI Institute**
Listed in the acknowledgements as a funding source: *"from the Boston Dynamics Artificial Intelligence Institute."* (Acknowledgements). Their investment in this research signals interest in integrating structured planning with foundation models for legged/manipulation robotics.

**Kinova Robotics**
The real-world hardware platform used: *"we deployed OWL-TAMP on a dual-arm robot (Kinova Gen3 arms with a pan-tilt head camera)"* (Section 6.2). Kinova's Gen3 arms are the testbed validating sim-to-real transfer across 19 tasks.

---

## 4. People Identified

**Nishanth Kumar** — MIT CSAIL / NVIDIA Research
PhD student and primary author. His prior work on bilevel planning (SeSaME, predicate invention) is the direct predecessor to OWL-TAMP. Has published multiple papers on combining learned models with TAMP (References 34, 35, 43). Contact: njk@csail.mit.edu. One of the most productive young researchers at the intersection of symbolic planning and learning.

**Caelan Reed Garrett** — NVIDIA Research (formerly MIT CSAIL)
Senior author and co-architect of PDDLStream, one of the most widely used TAMP frameworks. Contact: cgarrett@nvidia.com. Garrett's PDDLStream is the off-the-shelf TAMP system used in real-world deployment: *"we used PDDLStream and its 'Adaptive' solver to implement the TAMP framework and algorithm within OWL-TAMP"* (Appendix A.5). He is arguably the most influential researcher on production-viable TAMP systems.

**Tomás Lozano-Pérez & Leslie Pack Kaelbling** — MIT CSAIL
Co-directors of the Learning and Intelligent Systems group at MIT. Two of the foundational figures in robot task and motion planning globally. Their group has produced a decade of work that underpins every major TAMP system in use today (PDDLStream, STRIPStream, SeSaME). Their involvement signals this is not a one-off paper but a sustained research direction toward open-world capable robots.

**Dieter Fox** — NVIDIA Research / University of Washington
Senior research scientist at NVIDIA and professor at UW. Co-author on GR00T N1 (Reference 42) as well as this paper — his presence on both VLA and TAMP-hybrid work suggests NVIDIA is deliberately hedging across architectures for physical AI.

**Fabio Ramos** — NVIDIA Research
Co-author from NVIDIA Research. His background in probabilistic robotics and Bayesian methods complements the constraint sampling approach central to OWL-TAMP.

---

## 5. Operating Insights

### Build the VLM-TAMP Interface Around Constraints, Not Plans

The paper's most deployable insight is architectural: don't ask a foundation model to generate executable robot plans — ask it to generate *constraints* that a deterministic planner can satisfy. This separation of concerns means when the VLM generates a bad constraint (the primary failure mode), the TAMP system can detect infeasibility and request a new one, rather than silently executing a wrong plan. For CTOs designing robot software stacks, this suggests a pattern: foundation model as constraint generator, classical system as constraint satisfier and verifier. The paper formalizes this: *"Our main contribution is to propose a clear contract — in the form of constraints — for combining VLMs with generic domain-independent TAMP systems to enable zero-shot generalization."* (Section 1). This pattern is stack-agnostic and can be dropped into existing TAMP pipelines (both SeSaME and PDDLStream are demonstrated).

### False Positive Rate, Not Just Success Rate, Should Be a Primary Deployment KPI

The soundness metric — how often does the robot correctly identify when it has *not* succeeded — is buried in Section 6.1 and Appendix A.4 but has outsized operational importance. Approaches without continuous constraint generation declared success on tasks they objectively failed, at rates up to 80–90% false positives (Table 4). In deployed logistics, manufacturing, or service robotics, a robot that incorrectly reports task completion triggers downstream failures (inventory errors, missed handoffs, customer complaints) that are often more expensive than the robot simply stopping and requesting help. OWL-TAMP's near-zero false positive rate comes directly from the VLM-generated continuous constraints acting as verifiable success criteria — a design pattern worth replicating regardless of the planning architecture used.

---

## 6. Overlooked Insights

### The Primary Failure Mode Is Infeasible Constraints, Not Wrong Plans — and It's Unrecoverable in Current Form

The paper's most important limitation is stated clearly but easy to miss: *"Our system relies entirely on the VLM to generate constraints that are both syntactically and semantically correct. While the TAMP system is capable of backtracking internally, our current implementation cannot recover from errors in the generated constraints themselves."* (Section 8). In BerryCook, the VLM generated a constraint requiring *"the strawberry to be inside the bowl and pan simultaneously"* — physically impossible, causing guaranteed planning failure. This is distinct from a wrong plan (which backtracking handles) — it's a wrong *model of correctness*. For teams building on this architecture, the implication is that constraint validation and constraint repair need to be first-class components of the system, not afterthoughts. There is no current mechanism to detect that a generated Python constraint function is semantically wrong vs. simply hard to satisfy. A constraint debugger or constraint-level retry loop is the missing piece that would push OWL-TAMP from research prototype to production system.

### The Helper Function Library Is a Hidden Infrastructure Dependency That Determines What the VLM Can Express

The continuous constraints generated by the VLM are only as expressive as the primitive helper functions provided to it. The paper lists 15 geometric helper functions (Appendix A.6) — `modify_pose_bounds_to_be_near_object`, `modify_pose_bounds_to_be_inside_object`, etc. — that the VLM composes to construct constraints. This codebook is manually engineered and domain-specific. Tasks requiring constraints outside this vocabulary (e.g., force-based constraints, temporal ordering within a motion, deformable object placement) cannot be expressed regardless of VLM capability. For companies deploying this architecture, the quality and coverage of this helper function library is a direct determinant of system capability — and its expansion is a significant engineering effort that is invisible in the headline results. The paper acknowledges: *"our assumption of a set of primitive parameterized robot controllers... and a library of primitive helper functions — common in planning and foundation model-based code-generation works — which OWL-TAMP uses to generate plans and continuous constraints"* (Section 8). The helper library is, in effect, the domain knowledge that used to live in hand-engineered TAMP predicates — it has moved, not disappeared.