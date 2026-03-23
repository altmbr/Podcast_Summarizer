# [155: 贾鹏创立至简后的首次访谈：从英伟达到理想，具身智能的六边形战士](https://podcast.latepost.com/155)

**Podcast:** 晚点聊 LateTalk
**Date:** 2026-03-22
**Processed:** 2026-03-23T17:08:22Z
**Participants:** Manchi, 晚点团队
**Episode URL:** https://podcast.latepost.com/155
**Transcript:** [View Transcript](./transcript.md)

---

# Episode Summary: Jia Peng's First Interview After Founding Zhijian (至简)

**Podcast:** 晚点聊 LateTalk | **Episode:** 155
**Participants:** Jia Peng (贾鹏), CEO of Zhijian (至简); Host Manchi

---

## 1. Key Themes

### The Tesla Playbook as the North Star for Embodied AI

The central thesis of this episode is that the winning formula for autonomous driving—Tesla's data-flywheel approach—is the blueprint for embodied robotics. Jia Peng left NVIDIA in 2020 precisely because NVIDIA's approach lacked direct user data loops, then confirmed the thesis at Li Auto, and is now applying it to Zhijian.

> "Tesla's biggest inspiration for us is this: your commercialization and your data are always one and the same. Your commercialization process is actually pursuing scale effects, and those scale effects bring you real-world, real-user scenario data. That is the most precious thing." [01:28:18]

> "When I was chatting with Tesla's V14 team, I found their thinking was exactly the same as mine. I was both thrilled and slightly disappointed—thrilled because it validated our direction, and slightly disappointed because they were actually behind us. They had only just started incorporating language reasoning into System II thinking, but we had already shipped that in 2024." [01:52:24]

---

### Hardware Is the Bottleneck Nobody Wants to Admit

Jia Peng repeatedly returns to hardware reliability and consistency as the single most underappreciated problem in embodied AI. While the industry narrative is "hardware is solved, what's missing is data and algorithms," he directly contradicts this.

> "Everyone thinks the hardware for embodied AI is basically there—what's missing is data and algorithms. But I feel hardware hasn't reached that stage yet. The 'breakthrough' problem is actually hardware first." [02:18:33]

> "The return/failure rate I've observed is basically 100%. I haven't seen a single one that can sustain continuous work for a long time without breaking. This is something I've personally observed. The industry is far more optimistic than reality warrants." [01:36:11]

> "After coming from the automotive world, you look at embodied AI and realize nobody is deeply addressing manufacturing consistency, process standardization, or reliability testing at the level automotive has for 100 years." [01:38:40]

---

### The Unification Paradigm: One Model to Rule All Modalities

Jia Peng argues that the winning technical architecture is a single unified model that integrates world modeling, language reasoning, visual CoT, and action generation—rather than separate specialist models or dual-system designs.

> "We already shipped a fully unified VLA in 2024—one where world model capability and VLA are combined into a single model. It can simultaneously generate text CoT and predict what the next frames will look like. This is something we believe is the industry's first true productionized unified model." [01:26:20]

> "The dual-system approach has a fundamental problem: two models running at different frequencies. Who does the output listen to? And joint training is extremely awkward. So we asked: can the model itself decide when to use CoT and when not to? That's what we built." [01:23:23]

---

## 2. Contrarian Perspectives

### Synthetic Data Cannot Solve the Core Embodied AI Problem

While Jensen Huang and companies like Hillbot champion synthetic data as the primary training source, Jia Peng draws on 10 years of autonomous driving production experience to argue the opposite.

> "People who have truly done autonomous driving at scale all share one consensus: synthetic data is useful, but it is not the main force. Even for autonomous driving—a simpler environment than embodied AI—synthetic data was never used as the primary source. You cannot rely on it to solve 90% of the problem." [01:32:46]

> "Synthetic data is good for one thing: if you have a very rare edge case, you can expand it 1-to-100. But if you expect it to solve the fundamental training distribution? Not feasible right now." [01:33:16]

> "For locomotion and testing/validation pipelines, synthetic data works fine. But as the primary data source for manipulation tasks? I see no hope currently." [01:34:15]

---

### The Embodied AI Market Won't Consolidate Like Automotive—It Will Be Fragmented

While most industry observers assume a winner-take-all outcome similar to smartphones or EVs, Jia Peng argues embodied AI will be a multi-domain, fragmented market.

> "Autonomous driving ended up with a few oligarchs controlling 80-90% of the market. But embodied AI, I believe, won't get there. Humanoid will be the largest segment, but there will be many verticals where non-humanoid form factors are more efficient. Each vertical may have a few winners, and there may be dozens of verticals." [01:16:29]

---

### Choosing Industry #2 or #3 Suppliers—Not Leaders—Is the Right Strategic Partner

When building Li Auto's ADAS from scratch in 100 days, Jia Peng deliberately chose suppliers who were not market leaders, because existential stakes aligned incentives perfectly.

> "You cannot choose the industry leader. You must choose the #2 or #3 player. If this project fails, they die too. That's how you get true commitment. That's how everyone forms a single fighting unit." [01:37:47]

> "Horizon Robotics, Hesai, SenseTime—all these partners actually sent their best people to work with us side by side. They closed themselves in with us. This is what organizational capability looks like." [01:37:18]

---

### Humanoid Is Strategically Useful for Supply Chain, Not Near-Term Products

Jia Peng believes the obsession with humanoid form factor in the near term is misguided from a product standpoint, but understands its strategic value for forcing supply chain development.

> "Having players like Tesla and Unitree out front pushing humanoid is actually good for everyone—they're forcing the supply chain to develop. For us, we can pick up integrated joints and other components they've developed. But from a product and model-capability perspective right now, we've deliberately simplified our hardware to match what models can actually control." [02:00:53]

---

## 3. Companies Identified

**Zhijian (至简 / Simpliciti)**
Early-stage embodied AI startup founded mid-2025 by Jia Peng, Wang Kai, and Wang Jiajia, all ex-Li Auto. Building a full-stack (hardware + software + algorithms + data) embodied AI system with unified VLA architecture. Distinguishes itself by applying autonomous driving production discipline to robotics.
> "We are a hexagonal warrior. Technology, strategy, product, brand, organization, and commercialization all have to be strong." [00:33:17]

**Tesla**
Referenced repeatedly as the definitive role model for data flywheel, shadow mode testing, standardized hardware pre-installation, and lean 200-person teams producing world-class AI.
> "Tesla's team is the highest-efficiency AI team I've seen. A team of only about 200 people produced the world's best autonomous driving system and the best product. That's what I want to build toward." [02:17:05]

**Unitree (宇树)**
Singled out as the standout hardware company that has cracked manufacturing consistency through rigorous process engineering and vertical integration—demonstrated at Spring Festival events.
> "Unitree gave me great hope at this year's Spring Festival. They are clearly the hardware leader. Every unit performed consistently. No errors. That level of consistency takes genuine commitment to manufacturing process." [01:36:42]

**Li Auto (理想汽车)**
Used as the operational benchmark for how a "behind" team can leapfrog through project-based organization, aligned leadership cognition, and a balance of execution and research.
> "From a completely backward state, in just a few short years, we reached the first tier alongside Huawei and Xpeng. That was a genuinely satisfying comeback story." [01:50:28]

**Horizon Robotics (地平线)**
Notable for being the first chip partner Li Auto chose for mass production, and for deeply absorbing Li Auto's organizational culture including switching to Feishu and adopting LSA methodology.
> "Horizon even adopted our strategic analysis methodology—something we called LSA—and their entire organization began to look very similar to Li Auto's." [01:39:15]

**NVIDIA**
Contextualized as a company that plants 10-year seeds (CUDA took 10 years to become mainstream, automotive chips similarly), demonstrates the power of ecosystem thinking over product delivery.
> "Jensen Huang basically thinks in terms of the next step, or even the step after that. CUDA took 10 years before people really used it. Same with automotive chips. He's always thinking 10 years out." [01:19:18]

---

## 4. People Identified

**Jia Peng (贾鹏)**
CEO of Zhijian. Former NVIDIA China autonomous driving team employee #1, then VP-level ADAS leader at Li Auto (2020–2025). Rare "full-stack" technologist across hardware, chip architecture, software, and algorithms.
> "Whether you talk to me about hardware, chips, software, or algorithms—I can hold my own in any of those conversations. NVIDIA turned me into someone who had to touch everything." [01:14:55]

**Jensen Huang (黄仁勋)**
Described as someone with extraordinary energy, 10-year vision horizon, and the ability to personally evangelize vision to engineers at all levels—key to sustaining low-revenue bets.
> "Jensen told me once that he compares his forehead temperature to his wife's—his is always one degree higher. He said, 'My brain is running at full speed every day.' He wakes up at 4-5am and immediately starts reading papers or emails." [01:16:25]

> "He would personally respond to our weekly 'top 5' emails asking pointed questions: 'Why isn't China doing mass production yet? Is it our chip? Our software?' He was genuinely anxious about the market." [01:17:52]

**Li Xiang (李想)**
Founder of Li Auto. Identified as having unusually clear mental models around data supremacy and product primacy—despite not being a technical founder.
> "Li Xiang said two things that really moved me. First: technology must always serve the product. Second: data is everything. For a non-technical founder to say that, I found it remarkable—and very similar to how Elon thinks." [01:23:40]

**Wang Kai (王凯)**
Co-founder of Zhijian, former CTO of Li Auto's intelligent systems. Handles management, fundraising, and overseas strategy. Currently based in Europe scouting industrial customers.
> "Wang Kai has managed very large teams, has done VC work, and has touched chips, software, and hardware. His management leverage is something I simply don't have. I can hand off fundraising and he handles it beautifully." [01:58:18]

**Wang Jiajia (王佳佳)**
Co-founder of Zhijian, former delivery lead for Li Auto's ADAS. Handled software delivery and execution across all major Li Auto ADAS milestones (NOM, map-free, VLA).
> "Jiajia and I have worked together for five years. From the Orin chip delivery, to HD map, to map-free, to VLA—we've done every major project together. The chemistry is deeply established." [01:58:23]

---

## 5. Operating Insights

### Build a "Shadow Mode" Dual-Chip Architecture from Day One

Jia Peng argues this is not just a hardware choice—it is the core of your iteration infrastructure. One chip runs stable production; the other runs your new model in shadow mode. This gives you free, continuous, real-world A/B testing at scale.

> "We insist on dual-chip as standard configuration precisely for this reason: I can run my stable model on chip one, and deploy my new model on chip two in shadow mode—testing against real-world ground truth without affecting the user, and without any extra cost to the user." [01:31:17]

---

### "All Fall Into the Pit Together"—Cognitive Alignment Must Precede Execution

The single most important operating principle from Li Auto: ensure leadership has 100% aligned mental models before any major technical pivot. Dissent from outside the decision damages team cohesion catastrophically.

> "Li Xiang said: if you're going to fall into the pit, fall in together. Never let someone stand outside and say 'I told you so.' Because when everyone falls in together, everyone climbs out together. If someone is outside, the team is finished." [01:47:59]

> "The most important thing: the people at the top must have aligned cognition. If they disagree on Waymo vs. Tesla vs. NVIDIA approaches, the project is dead." [01:31:01]

---

### Use Closed Sprints With Named Battles to Compress Time

Li Auto compressed 100 days of work into the equivalent of 300 by running named "battle" projects with cross-functional elite teams in hotel lockdowns, parallel execution, and intense time compression analogous to the "Full Regiment on One Gun" military doctrine.

> "The question was: how do we take several minutes and compress it to 8 seconds? That's what the whole regiment had to do in unison. We applied exactly that logic—if your time utilization is high enough, your 100 days becomes 300." [01:35:51]

---

### Maintain a Permanent "Research Reserve" Even During Intense Delivery Periods

Li Auto deliberately kept a small team doing forward-looking research even during the most intense shipping cycles. This is what enabled the rapid pivot to map-free and end-to-end when the moment came.

> "Li Auto established one excellent habit: no matter how intense the fighting, always keep a portion of the team doing research—looking for better options. That's why when it was time to pivot to map-free and end-to-end, we could immediately switch the whole organization and ship." [01:33:56]

---

## 6. Overlooked Insights

### The Wearable Data Glove Is a Silent Make-or-Break Infrastructure Bet

Jia Peng briefly mentions that Zhijian's own custom wearable data collection glove is iterating slowly due to electromagnetic interference causing data corruption—and that early versions had 30% data usability. This is actually a fundamental constraint on the entire company's data flywheel, yet it received almost no attention in the conversation.

> "The wearable glove involves significant electromagnetic interference issues—the position data would suddenly jump. In early versions, maybe 30% of data was usable. Now we're at 90%, but this iteration has been painful and slow. It needs more time." [02:08:16]

This is significant because the entire embodied AI data strategy—including the industry-wide thesis that teleoperation/wearable devices can substitute for real deployment data—depends on this hardware working at near-100% fidelity. A 10% data corruption rate at scale poisons model training. Any investor or competitor who builds their data strategy around wearable teleoperation without solving this EMI problem is building on a flawed foundation.

---

### The Evaluation Problem Is the Silent Killer Nobody Is Solving

Jia Peng makes a passing but crucial observation: the industry is so focused on data collection and model training that almost nobody is building rigorous model evaluation infrastructure—the "tail end" of the iteration loop. Without this, you can't know if your model actually got better.

> "The industry has largely overlooked the evaluation question. After all these data iterations, how do you know your model actually improved? I push my team hard on this—it's one of two critical points I emphasize constantly. Tesla's shadow mode is the gold standard for this, and we are building an equivalent." [01:29:49]

This is non-obvious because it is invisible—it doesn't show up in demos, papers, or fundraising pitches. But it is the difference between teams that actually compound improvement and those that spin their wheels. The companies that crack rigorous, automated, real-world model evaluation first will have a structural compounding advantage that is essentially invisible to outside observers until the capability gap becomes unmistakable.