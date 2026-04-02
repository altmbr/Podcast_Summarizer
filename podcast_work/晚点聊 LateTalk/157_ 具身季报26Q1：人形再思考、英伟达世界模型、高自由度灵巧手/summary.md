# [157: 具身季报26Q1：人形再思考、英伟达世界模型、高自由度灵巧手](https://podcast.latepost.com/157)

**Podcast:** 晚点聊 LateTalk
**Date:** 2026-04-02
**Processed:** 2026-04-02T17:12:04Z
**Participants:** Manchi, 晚点团队
**Episode URL:** https://podcast.latepost.com/157
**Transcript:** [View Transcript](./transcript.md)

---

# Embodied Intelligence Q1 2026 Quarterly Review

**Podcast:** 晚点聊 LateTalk | **Episode 157**
**Participants:** Manchi (host), Chen Zhe (guest investor/researcher, recently returned from GTC in the US)

---

## 1. Key Themes

### Humanoid Robots Are Crossing a Reliability Threshold That Changes Everything

The Unitree spring festival performance wasn't just a PR stunt — it represented a genuine technical milestone. The key wasn't one robot doing impressive moves, but 20+ robots doing complex synchronized actions with high consistency. "It's not just carefully tuning one robot, but ensuring that on over 20 mass-produced machines, consistent responses can be achieved — and each machine faces different environmental disturbances." [00:12:08] This consistency, enabled by reinforcement learning rather than traditional control algorithms, represents a qualitative leap. The prior era of Boston Dynamics' parkour was "carefully edited with many failures" and even single robots had low success rates on long sequences. [00:13:34] This threshold crossing is now enabling adjacent markets — a humanoid robot rental company (擎天租) has already emerged to serve the performance market. [00:28:09]

### World Models Are Emerging as the Next Architecture Paradigm Beyond VLA

The field is undergoing a shift from Vision-Language-Action (VLA) models to World Action Models (WAM), with NVIDIA's Dream Zero and Dream Dojo as the flagship examples. VLA's fundamental limitation: "It's establishing a kind of mapping — when you see this image and this text description, I should produce this joint sequence... it's a form of behavior cloning with descriptions." [00:21:04] This is why VLA generalizes poorly — change the blue cup to red, or move it from left to right, and it fails. World models predict physical consequences of actions through video generation, enabling causal reasoning. "Video represents intelligence that is more reactive, more real-time, more interactive with the environment." [00:19:09] However, this path is compute-intensive and heavily favors large incumbents with video generation capabilities.

### Dexterous Hands With Tactile Feedback Are the Next Major Research Frontier

A consensus is emerging among leading researchers globally: "Basically all the researchers I've been in contact with, their consensus revolves around dexterous hands." [00:05:38] The reason is structural — current VLA and world models are "completely without tactile signals" [01:04:39], yet tactile feedback is essential for manipulation. Experiments blocking fingertip nerve endings show humans can't complete seemingly simple tasks without touch. The Sharpard (founded by ex-Unitree team: Li Yifan, Sun Kai, Shao Shaoxin) 22-DOF hand with tactile feedback demonstrated this at CES with an autonomous windmill assembly demo. The opportunity is analogous to Unitree's G1 creating a research standard: "Today if you do humanoid research and don't use the G1, it's very hard for others to reproduce your work." [01:09:05] The same standard-setting opportunity exists for dexterous hands.

---

## 2. Contrarian Perspectives

### Humanoid Form Factor May Actually Be More Cost-Efficient Than Wheeled Robots for Many Industrial Tasks

Most people assume wheels are the pragmatic, cost-effective alternative to bipedal locomotion. The reality is more nuanced. A humanoid robot needs only 40x60cm of floor space — "about the area of two MacBook laptops placed together" [00:36:57]. Boston Dynamics' wheeled "Stretch" robot weighs approximately 1 ton to safely handle 20-25kg boxes due to center-of-mass requirements, while a full-size humanoid weighs 70-80kg doing the same task — a 10x weight difference. "If you need more or the same number of motors, and higher quality ones because the base is heavier, all costs increase rapidly." [00:38:52] A four-wheel-steer mobile robot actually needs 8 motors just for movement, plus additional actuators for height adjustment — comparable complexity to humanoid.

### Tesla's Tendon-Driven Hand for Optimus May Be Fundamentally Flawed, Not Visionary

Elon Musk frames the tendon approach as "first principles" biomimicry. But a researcher's counter-argument is compelling: "You're already using motors, not muscles. From where does the first principles analogy come?" [00:47:07] Human tendons can self-repair through rest and training; mechanical tendons wear irreversibly. Human muscles have extraordinary power and torque density that motors cannot match by volume. The practical consequence: assembling a high-DOF tendon hand "means inserting 40+ different tendons into the wrist and palm space" [00:46:38], and any tendon damage requires surgical-level disassembly. This is reportedly causing significant production challenges for Gen 3 Optimus, potentially delaying what was once a Q1 target to at least June, with mass production potentially slipping to 2027.

### The Research/Science Market That Investors Dismissed Is Actually Unitree's Greatest Competitive Moat

Investors including prominent VC Zhu Xiaohu publicly dismissed the science education market as unsustainable. But this "bad strategic direction" created an unassailable moat: "Unitree has truly completed the design, production, and mass manufacturing process of millions of motors" through its quadruped robots. [00:22:49] The result: 20 months after G1 launched, no competitor has meaningfully challenged its position. New entrants can prototype competing hardware easily, but replicating production reliability at thousands of units requires the same years of iteration Unitree went through. Meanwhile, the research ecosystem lock-in means "all the latest humanoid robot research is conducted based on their hardware." [00:27:09]

### Figure AI's Hollywood-Quality Marketing May Be Concealing Genuinely World-Class Technical Capability

Figure is widely derided in China's robotics community as all hype. The reality appears more complex. Their Helix AI framework implements a three-layer architecture (low/medium/high frequency unified whole-body control) and internal sources suggest performance "is very leading in the market." [00:52:29] Founder Brett Adcock's serial-exit background (Archer Aviation, sold prior company) creates legitimate skepticism, but "in the past one to two years, Figure has attracted very many excellent hardware and software talents, and has indeed delivered very solid results." [00:51:59] The real risk isn't fraud — it's whether Brett's history of optimizing for exits means the company is positioned for acquisition rather than the long-term industrial buildout humanoids require.

### Chinese Companies Are Actually Leading in Embodied AI, Not Just "Catching Up"

The conventional wisdom is that China trails the US in frontier AI. In embodied intelligence, the evidence suggests the opposite. "In embodied intelligence-related complex hardware products, whether robot bodies or dexterous hands, I believe Chinese companies are leading the world." [01:14:16] The US hardware supply chain atrophy means "it's hard to imagine American companies doing this at a few hundred thousand RMB cost." [00:53:27] The critical variable is whether world models — which favor compute-rich US incumbents — become the dominant paradigm, which could shift this balance.

---

## 3. Companies Identified

**Unitree Robotics (宇树机器人)**
Humanoid and quadruped robot manufacturer, preparing for IPO. The defining humanoid robotics company globally for the research market.
"Unitree's success is similar to DJI's success — both are founders who truly love and are committed to their direction... not just doing it because of the huge commercial opportunity." [00:23:47]
Revenue mix: humanoid grew from <2% (2023) → 27% (2024) → 51% (first 3 quarters of 2025). Gross margin on humanoids: ~63%. Targeting 1-2万 units in 2026 vs. 5,500 in 2025. [00:27:39]

**Sharpard (沙氏/夏帕)**
Dexterous hand company founded by ex-Unitree co-founders Li Yifan, Sun Kai, and Shao Shaoxin. Makes a 22-DOF tactile-enabled dexterous hand ($50K/unit).
"Sharpard's demo at CES — an autonomous windmill assembly — showed everyone the current SOTA level of dexterous hands globally." [00:05:27]
Formally launched at ICRA 2025 in Atlanta. Positioned to potentially become the "G1 of dexterous hands" — the default research platform. [01:08:35]

**Figure AI**
US-based humanoid robotics company, highest-funded and highest-valued in the US market.
"Their Helix AI [three-layer architecture] — from the demonstrated results and feedback I've heard from people inside, their capability is very leading in the market." [00:52:29]
Deserves an "Oscar for best visual effects" for marketing, but technical substance appears real. Founder Brett Adcock previously built and exited Archer Aviation (eVTOL). [00:49:35]

**Boston Dynamics**
Pioneer humanoid robotics company (founded 1992), now majority-owned by Hyundai.
New electric Atlas uses only 2 types of actuators, 360-degree rotation at all joints, interchangeable left/right limbs — designed for US manufacturing conditions where skilled technicians are scarce. Partnered with Google DeepMind for AI.
"Boston Dynamics, as the pioneer of humanoid robot research, has had very deep long-term research on difficult scenarios and landing value." [00:08:18]

**Physical Intelligence (π / Pi)**
US-based robotics model company, widely considered the global frontier leader in embodied AI models.
"Looking at the entire Q1 from Pi, it still represents the most leading work globally in terms of cross-embodiment and dynamic environment adaptability." [00:59:18]
Notable Q1 work: long-sequence memory via text-based state reflection (similar to OpenAI's approach), online RL for complex scene execution. Uses open-source Polygamma as base model.

**Galaxy General Robotics (银河通用)**
Chinese humanoid robotics company (collaboration with Tsinghua).
"The first time to let everyone see that humanoid robots can perform well in what we consider a high-speed, real-time feedback system." [00:07:21]
Their tennis-playing demo was so impressive that robotics VC Andre Kampassian initially called it CG-generated on X. Uses external cameras (not onboard) for ball tracking — but "as long as this thing can be done, humans will definitely find ways to optimize it with less compute." [00:32:05]

**NVIDIA**
Released Dream Zero (world action model) and Dream Dojo (video-based physics simulator) and EgoSkill dataset framework (20,000+ hours of egocentric human data).
"The core understanding is using video generation methods rather than text generation methods." [00:06:53]
Despite massive resources, uses Alibaba's open-source Wan 2.1/2.2 as the video backbone for world models — suggesting the field is still too early for custom video backbone training. [01:36:02]

**Rode AI**
US world-model-focused robotics startup; announced $450M funding at GTC 2025.
"They've directly collected a lot of EgoCentric data — they have their own data, doing continual training." [01:39:55]
Appeared "after being underwater for a year" and immediately closed a landmark round, signaling institutional conviction in the world model paradigm.

**Ditu (地瓜) / Horizon Robotics (地平线)**
Ditu is a Horizon Robotics spinout focused on compute for mass-market commercial robots (cleaning robots, drones, etc.).
"The largest player is Ditu, which is a company incubated by Horizon." [01:46:48]
NVIDIA has essentially zero market share in mass-production consumer robots — this entire segment is open for Chinese chip companies. [01:46:19]

**Sunday (三内)**
US robotics company known for innovative data collection hardware — a three-finger gripper (vs. two-finger) with tactile feedback, designed for teleoperation data collection where the same gripper is used on both the data-collection device and the robot.
"Sunday has further expanded the two-finger Yumi to three fingers... through adding this one finger's degree of freedom, a large number of actions that are difficult for grippers can now be done with Sunday's three-finger gripper." [01:33:10]
Co-founder Chi Chen previously developed the UMI framework at Stanford.

---

## 4. People Identified

**Wang Xingxing (王兴星) — Founder, Unitree Robotics**
"Wang Xingxing is a very honest, very focused person. He just wanted to make quadruped robots, and wanted to make them well." [01:11:20]
Built the company to profitability from day one out of necessity — "if he wasn't profitable, I wouldn't have seen him by 2019." Publicly stated he didn't want to make humanoid robots as late as 2021-22, but pivoted when market demanded it. Created H1 in 3.5 person-months by "making a dog stand up." His frugality: R&D spend was only ~90M RMB for first 3 quarters of 2025 — far below peers. Planning to invest 2B RMB of IPO proceeds into brain/AI research.

**Li Yifan (李一帆) — Co-founder, Sharpard**
Former Unitree co-founder (along with Sun Kai and Shao Shaoxin) who left to found Sharpard.
"I briefly chatted with Li Yifan... he said what he thinks is most important is still the AI capability. I completely understand — their goal is still to build a general-purpose robotics company." [01:09:34]
Notable for creating a potentially category-defining dexterous hand while remaining focused on the larger vision of general robotics rather than getting distracted by the hand as an end product.

**Brett Adcock — Founder, Figure AI**
Serial entrepreneur: sold first company, founded Archer Aviation (eVTOL, IPO'd ~2021), left Archer, founded Figure AI.
"Brett's characteristic is being able to continuously find the next entrepreneurial hot spot, and also being able to attract investors who recognize his vision." [00:50:03]
"Whether Brett is this kind of founder [who will see it through], the market today has a lot of controversy." [00:51:29] History suggests optimization for exits over long-term company building.

**Chi Chen (池晨) — Co-founder, Sunday**
Stanford researcher who originally developed the UMI (Universal Manipulation Interface) framework, later improved by Generalist and then built into Sunday's three-finger gripper system.
"Chi Chen when he was at Stanford was working on the Yumi solution — Yumi itself was work he participated in." [01:33:02]
"I've known Tony [co-founder] and Chi Chen for quite some time. I truly admire such entrepreneurs because they can truly push out innovations that don't exist in the world, yet in retrospect feel completely reasonable." [01:32:40]

**Zhu Xiaohu (朱孝虎) — VC (referenced)**
Prominent Chinese VC who publicly expressed skepticism that Unitree's science/education market was sustainable. Mentioned as representative of the mainstream investor view that ultimately proved to be short-sighted. [00:20:20]

---

## 5. Operating Insights

### The "G1 Standard" Playbook: Own the Research Market Before the Commercial Market Exists

Unitree's path offers a repeatable template: build the best hardware for the research/science market, achieve ecosystem lock-in as the default platform, then benefit as any downstream commercial application built on your hardware succeeds regardless of who wins the AI race. "As long as this can continue long-term, I believe his ecological position is very hard to replace — even if better companies appear, even if those companies release excellent closed-source embodied models, I think Unitree will benefit along with them." [00:27:09] For founders: defining and dominating a niche (even a "small" ~1B RMB market) with genuine product-market fit creates a moat that larger, better-funded competitors won't bother attacking.

### Frugality as Survival Strategy in Hardware: The "Live Long Enough" Principle

Unitree's R&D spend (~90M RMB for 9 months of 2025) is "far smaller than many robot companies." [00:25:12] This wasn't a mistake — it was existential. Wang Xingxing survived 7+ years (founding 2016) of investor skepticism by staying profitable on modest revenue. "If he wasn't this kind of person, he wouldn't have survived to today, wouldn't have survived until the embodied intelligence wave arrived." [00:25:12] For hardware companies: the ability to generate cash from early markets (even "suboptimal" ones like science education) is the prerequisite for being alive when the large market emerges. Do not optimize for growth at the expense of unit economics in hardware.

### Data Pyramid Thinking: Match Data Quality to Training Need

The hierarchy matters for building embodied AI systems efficiently: teleoperation data (most expensive, highest quality) → UMI/Yumi-style capture → EgoCentric video with data gloves → EgoCentric video without gloves → internet video. "The data at the top of the pyramid is more expensive, fewer in quantity, but higher in quality." [01:31:11] Practical implication for teams: don't default to internet video (cheap but massive domain gap) or pure teleoperation (expensive, hard to scale). EgoCentric data with simple rigs offers a high-value middle tier that is underexploited. EgoSkill data "importance has been rapidly rising over the past six months." [01:29:43]

---

## 6. Overlooked Insights

### The Chip Market Follows an Inevitable Consolidation Pattern That Will Crown 1-2 Winners

This was mentioned briefly as context for algorithm discussion but carries enormous investment implications. "Historically, a complex chip basically only has two players — 80/20 split, first place with ~80%, second with ~20%." [01:48:45] The current chip landscape for humanoid robots is extraordinarily fragmented: NVIDIA (research/training), Horizon/Ditu (consumer robots), Qualcomm (automotive), Huawei (high-end auto), plus Tesla's custom chip, plus potential entries from Xiaomi, Xpeng, Li Auto. "Humanoid robots will very likely go through a very fierce elimination race." [01:49:11] The analog is precise: Tesla's explicit strategy of using the *same chip* for both its autonomous vehicles and Optimus robots confirms that automotive-grade chips are the natural precursor to robot chips. "Chinese companies that can mass-produce their own chips in the intelligent vehicle era — including Xpeng, Huawei, Li Auto, Xiaomi — will also be very powerful compute solutions in the embodied intelligence era." [01:48:17] This is an under-discussed but high-conviction investment theme: the 1-2 companies that win the automotive compute platform race are also likely to win the humanoid compute race — and the window to identify those winners is now, while the market is still fragmented.

### The Humanoid Robot Competition Circuit Could Become the F1 of Technology Development

Briefly mentioned almost as an afterthought, but historically significant: "All the well-known humanoid robot companies in China are sparing no effort to prepare for this competition [Beijing Yizhuang humanoid robot competition]." [02:00:52] Last year it was dismissed as a novelty. The guest's analogy is precise and underappreciated: "Just like F1 races in the automotive industry, this will accelerate many frontier technologies and solutions." [02:01:21] F1 genuinely does trickle down — regenerative braking, carbon fiber construction, advanced telemetry all entered consumer cars via motorsport. A humanoid robot competition that incentivizes extreme reliability, speed, and coordination under competitive pressure could compress the R&D cycle significantly. Investors and researchers should monitor these competition results as leading indicators of which companies' fundamental architectures are actually robust.