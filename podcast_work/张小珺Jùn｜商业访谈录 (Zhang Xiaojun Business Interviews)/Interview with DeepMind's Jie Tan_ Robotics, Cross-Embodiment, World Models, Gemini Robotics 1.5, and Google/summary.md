# Interview with DeepMind's Jie Tan: Robotics, Cross-Embodiment, World Models, Gemini Robotics 1.5, and Google

**Podcast:** 张小珺Jùn｜商业访谈录 (Zhang Xiaojun Business Interviews)
**Date:** 2025-11-28
**Participants:** Jie Tan, Zhang Xiaojun
**Region:** Chinese
**Video ID:** 692965c0ba2292550f3551f7
**Video URL:** https://www.xiaoyuzhoufm.com/episode/692965c0ba2292550f3551f7
**Transcript:** [View Transcript](./transcript.md)

---

# Podcast Summary: Google DeepMind Robotics Senior Research Scientist Tan Jie

## 1. Key Themes

### The Evolution of Robotics Through Deep Reinforcement Learning and Foundation Models

The podcast reveals two fundamental paradigm shifts in robotics over the past decade. The first breakthrough came through deep reinforcement learning applied to locomotion, which Tan Jie pioneered with his 2018 paper on sim-to-real learning for quadruped robots. "I think the first paradigm shift in the past ten years was using reinforcement learning to solve walking and locomotion problems," Tan explains [00:08:07]. This approach, utilizing techniques like PPO (Proximal Policy Optimization), enabled robots to perform complex movements like backflips and running that were previously only achievable through expensive manual engineering. The second paradigm shift involves foundation models, which have given robots common sense and language understanding. "When you have foundation models, first, robots can understand human language. So you can directly use natural language dialogue to make them do things," Tan notes [00:12:00]. This allows anyone to command robots without programming expertise, fundamentally democratizing human-robot interaction.

### Data as the Fundamental Bottleneck in Robotics

Unlike language models that can leverage internet-scale data freely available online, robotics faces an acute data scarcity problem that represents the primary constraint on progress. "For language models, data is free - there's already so much text data online... But for robotics, obtaining data in the real world through embodied interaction is extremely difficult," Tan emphasizes [00:24:00]. This challenge has spawned an entire industry of "data factories" that collect robotic manipulation data through teleoperation, but the cost remains prohibitive. Tan describes a data pyramid where different types of data play different roles: internet video at the base provides massive scale but low relevance; ego-centric human videos offer more utility; simulation data bridges the gap; and robot-specific data at the top provides the highest quality but smallest quantity [00:47:00]. The fundamental research question is determining the optimal mix and how to leverage more scalable data sources to reduce dependence on expensive real robot data collection.

### The Intensifying Competition and Cultural Shift in Silicon Valley AI Research

The podcast reveals a dramatic transformation in research culture at major tech companies, with Google DeepMind moving from a loose confederation of individual researchers to highly coordinated team efforts. "When I joined, there were maybe ten people. Now there are about 150-180 people on the robotics team," Tan shares [01:24:00]. More significantly, the work culture has intensified dramatically: "I would say we work 70-80 hours per week now, which might be even more intense than 996" [01:30:00]. This shift reflects the high stakes of AI competition, where companies believe falling behind means losing top talent to competitors. Meta's aggressive recruitment has particularly disrupted the ecosystem by dramatically raising compensation for AI talent, creating both retention challenges and opportunities. However, Tan emphasizes that for the most talented researchers, compensation isn't the primary motivator: "For people with a sense of mission, what they really care about is whether they can be in the driver's seat when this major transformation happens in robotics" [01:36:00].

## 2. Contrarian Perspectives

### Simulation Data Will Outpace Real-World Data Collection

While the robotics community debates whether to focus on simulation versus real-world data collection, Tan takes a definitive stance that simulation—particularly video generation models—will become the dominant approach. "I have a somewhat contrarian judgment... In the next two to three years, traditional physics-based simulation will gradually be replaced by generative model simulation," he predicts [00:54:00]. This contradicts the current trend where many Chinese companies are investing heavily in teleoperation systems and data collection infrastructure. Tan's reasoning centers on scalability: "If I want 500 different home scenarios, with generative models you just need 500 different prompts... But with traditional simulation, you need designers to manually build each scene" [00:54:00]. He acknowledges video generation models still have issues with physics violations and hallucinations, but believes the fundamental scalability advantage will drive their eventual dominance. The key insight is that compute can substitute for precision—generating massive quantities of imperfect simulation data may ultimately prove more effective than collecting smaller amounts of perfect real-world data.

### The Telephony Hardware Advantage May Not Matter Without Foundation Models

Contrary to the common narrative that China's hardware superiority in robotics will drive its competitive advantage, Tan suggests this advantage is largely meaningless without access to cutting-edge foundation models. "If you're doing a robotics foundation model, you're still heavily dependent on existing large models," he explains [00:50:00]. The implication challenges the thesis of many Chinese robotics startups: even with superior hardware and faster iteration on physical robots, they face fundamental limitations if building on open-source models rather than frontier foundation models like Gemini. Tan's team found that "visual generalization comes for free" when using Google's vision encoders pre-trained on internet-scale data [01:21:00], a capability that would require extensive research to replicate from scratch. This suggests the real competitive moat in robotics may not be hardware or even robot-specific data, but rather access to the best foundation models—an uncomfortable reality for robotics companies without such resources.

### End-to-End Unified Models Will Win Over Hierarchical Architectures

While Gemini Robotics 1.5 currently uses a two-model architecture separating slow reasoning (ER) from fast execution (VLA), Tan believes this is merely a transitional phase dictated by compute constraints. "I think it should be a transitional approach... When compute is no longer a major constraint, I think a unified model would be optimal," he states [00:59:00]. He draws on his own experience trying to combine traditional control theory with reinforcement learning for locomotion—an approach that seemed pragmatic but was ultimately superseded by pure end-to-end learning. "Sometimes for short-term results you might take shortcuts and use hierarchical models, but at least from my past experience, directly investing in the end-to-end unified large model you believe in will ultimately win" [01:05:00]. This perspective contradicts much current research that advocates for specialized modules and hierarchical planning, suggesting researchers should invest directly in the ultimate architecture rather than incremental improvements to hybrid approaches.

## 3. Companies Identified

### Boston Dynamics
**Description:** Pioneering robotics company known for advanced legged robots like Spot and Atlas  
**Why mentioned:** Referenced as the previous gold standard in robotics capabilities that academia didn't understand  
**Quote:** "Ten years ago, people thought the best robots were Boston Dynamics' robots. They had dogs called Spot and humanoids called Atlas. They could do parkour, very impressive. But the entire academic community didn't know how they did it. Later we learned they used MPC (Model Predictive Control)" [00:09:00]

### Tesla
**Description:** Electric vehicle and AI company developing both autonomous driving and humanoid robots  
**Why mentioned:** Exemplifies the alternative approach of incremental development versus leap-to-L4 autonomy, and as a major player in humanoid robotics  
**Quote:** "I think we can compare Waymo and Tesla's very different strategies. They both want to solve autonomous driving. Waymo aims for L4 from the start—no human driver anywhere, even removing the steering wheel. But Tesla said we're not in a hurry, we can progress from L2 to L2.5 gradually, getting the data flywheel spinning" [01:16:00]

### Waymo
**Description:** Alphabet's autonomous driving subsidiary  
**Why mentioned:** Contrasted with Tesla's approach as taking the direct path to full autonomy  
**Quote:** "Waymo is very great in that they actually removed the driver from the seat—I'm also a Tesla user, I think FSD is very impressive and I use it often, but this zero-to-one breakthrough of having the courage to remove the driver, I think that's a qualitative breakthrough" [01:17:00]

### Physical Intelligence (Pi)
**Description:** Robotics AI startup (implied from context about foundation models)  
**Why mentioned:** As example of company building robotics foundation models outside large tech companies  
**Quote:** Referenced in discussion of whether robotics models should be viewed as independent discipline or extension of foundation models [00:13:00]

### Meta
**Description:** Social media and technology conglomerate investing heavily in AI  
**Why mentioned:** For dramatically raising AI talent compensation and disrupting the Silicon Valley talent market  
**Quote:** "Meta has done several things. First, it drove up the price of AI talent, extremely high... This is very real" [01:34:00]

### Aloha (Implied: Stanford/Google Project)
**Description:** Research project for bimanual robot manipulation  
**Why mentioned:** As example demonstrating that vision alone could achieve surprisingly complex manipulation without tactile feedback  
**Quote:** "There's a paper from Stanford called Aloha... That was the first time I saw that through vision alone, completely through vision, you could teleoperate an Aloha robot to do very complex things, including taking a tissue from a tissue box" [01:09:00]

## 4. People Identified

### Karen Liu
**Description:** Tan Jie's PhD advisor, professor of computer graphics now at Stanford  
**Why mentioned:** For being open-minded and supporting Tan's pivot from graphics to robotics  
**Quote:** "My advisor is called Karen Liu. I did my PhD at Georgia Tech. Later she went to Stanford. She's now at Stanford. She was very supportive and open-minded. She said, 'Then just do it.' So my last project was completely using reinforcement learning methods on a small humanoid robot" [00:04:00]

### Sergey Levine (Implied from Berkeley reference)
**Description:** Berkeley professor and prominent robotics researcher  
**Why mentioned:** As another example of computer graphics researchers transitioning to robotics  
**Quote:** "There's a very famous Berkeley professor called Sergey Levine. He used to do computer graphics. We often presented papers one after another at SIGGRAPH conferences. But we both coincidentally switched to robotics, which shows these two fields are actually very related" [00:06:00]

### Elon Musk
**Description:** CEO of Tesla and other companies, technology visionary  
**Why mentioned:** As example of visionary leader whose conviction attracts resources and talent despite ambitious goals  
**Quote:** "I think if you look at examples from this world's development, regardless of right or wrong, or whether both paths might work, what will happen? There may be a big figure, maybe Elon Musk, maybe Steve Jobs—a visionary person who instills a concept" [00:20:00]

## 5. Operating Insights

### The Data Quality Challenge Requires Cultural Bridge-Building

One of the most practical challenges in scaling robotics is the lack of standardized data quality metrics, which creates friction between data collection vendors and model developers. "If we take their data and use it, and the results aren't good, we can say they didn't collect it well. They'll definitely say you didn't train the model well. So there's a process of argument here. The reason is that data quality doesn't have a good definition," Tan explains [01:01:00]. The operational insight is that teams need to invest heavily in defining clear data quality specifications upfront, including metrics for smoothness, coverage, task completion, and edge case handling. Without this, data collection partnerships become exercises in mutual blame rather than productive collaboration. This suggests robotics companies should dedicate senior technical staff to working directly with data vendors to establish and validate quality standards before scaling collection efforts.

### Accelerating Research Iteration Requires Fighting Organizational Antibodies

Tan reveals that a significant portion of his role involves actively combating "big company disease" to maintain research velocity. "I have another responsibility called research iteration speed. I need to ensure that what everyone wants to do can be done quickly. But this means you have to fight against big company disease," he shares [01:31:00]. Specifically, he describes procurement processes that previously took over 30 business days and compliance reviews that delayed access to datasets by weeks. The solution required working with legal and operations teams to create special fast-track processes for the robotics team, with executive support making this possible. The broader insight is that in fast-moving AI fields, research leaders must allocate significant time to operational infrastructure and process optimization, not just technical direction. Teams that fail to address these "plumbing" issues will fall behind regardless of their technical capabilities.

### Cross-Embodiment Transfer Requires Architecture Innovation, Not Just Data Mixing

The breakthrough in getting robots to learn from each other's data wasn't simply combining datasets but developing a specific technique called "motion transfer." When asked about the details, Tan describes it as a "secret sauce" but emphasizes: "It's not enough to just put data together. At the same time, you need to make considerable changes to the model architecture and training recipe" [00:40:00]. The operational takeaway is that cross-embodiment learning is fundamentally a research problem, not an engineering one. Teams pursuing this approach should expect to invest in novel architecture designs specifically optimized for this goal rather than assuming existing VLA architectures will naturally generalize across robot morphologies. The fact that three or four different team's compatible innovations combined to enable the result suggests this requires sustained, focused research investment rather than straightforward scaling of data collection.

### Talent Retention in AI Requires Mission Alignment Over Compensation Matching

Despite Meta offering compensation packages reportedly reaching $1 million annually, Tan successfully retains team members by focusing on mission alignment rather than matching offers. "For people with a sense of mission, what they really care about isn't actually money. What they really care about is—they believe the robotics industry will soon have a qualitative transformation, a major change. If this transformation happens, will it be Meta or Google? They want to be in the driver's seat when this transformation happens," he explains [01:36:00]. The operational insight is that for top AI researchers, the critical question is resource availability and organizational commitment to the mission, not marginal compensation differences. Leaders can successfully compete for talent by credibly demonstrating their organization provides the best platform for breakthrough work—through compute access, data resources, team quality, and leadership attention. This suggests robotics companies should invest heavily in showcasing their technical infrastructure and organizational momentum rather than purely competing on compensation.

### Managing Research Teams Requires Balancing Top-Down Direction with Bottom-Up Innovation

Tan describes a dual-track approach where major releases like Gemini Robotics operate top-down while maintaining space for bottom-up research exploration. "Gemini Robotics is more top-down... But besides Gemini Robotics, we also have many other research projects that are bottom-up. Because our researchers are all very strong, they're very sensitive to trends in this era. They think of various new methods and want to experiment," he explains [01:28:00]. The motion transfer breakthrough exemplified this hybrid model: the *what* (solving cross-embodiment data utilization) came from top-down problem identification, while the *how* emerged from multiple small teams trying different approaches that proved compatible. The operational framework is to set clear strategic objectives centrally while funding multiple small teams to explore different technical approaches, then integrate successful innovations into flagship products. This requires resisting the temptation to over-coordinate research efforts or mandate specific technical approaches.

## 6. Overlooked Insights

### The Profound Implications of White PhD Students Wanting to "Be a Cow and Horse"

In a remarkable cultural moment that Tan recounts with bemusement, a white American PhD candidate recently told him: "I really hope your team can hire more Chinese people... He said he also learned a phrase called 'niu ma' (cow and horse)... He said he particularly likes being a 'cow and horse' himself. He also wants to be one" [01:41:00]. While Tan questioned whether this person misunderstood the self-deprecating connotation of this Chinese internet slang, the anecdote reveals something profound about cultural perceptions of work ethic in AI. The fact that Chinese researchers' intensity and productivity has become so legendary that non-Chinese researchers actively seek to emulate it (even adopting the language) suggests we're witnessing a fundamental shift in Silicon Valley's cultural dynamics. This represents more than just Chinese researchers succeeding individually—it indicates Chinese work culture is becoming aspirational among top AI talent globally, potentially reshaping norms around intensity and commitment in the field.

### Video Generation Models Have Already Enabled Interactive World Models

While much discussion focuses on when "world models" will arrive for robotics, Tan points out that Google's Genie already demonstrates this capability: "Genie is more like a world model, because when you play games, you can use a keyboard to control it. You can turn left or right and see completely different worlds. So when you have input while playing that can change the next frame, that feels like a world model" [00:57:00]. This observation is hugely significant because it suggests the infrastructure for robot simulation via generative models already exists—it's not a far-future capability requiring fundamental breakthroughs. The implication is that robotics teams should be actively experimenting with using interactive video generation for data synthesis *now* rather than treating it as a future possibility. The gap between current video generation demos and practical robot training simulation may be much smaller than commonly assumed, suggesting near-term opportunities for teams willing to invest in this direction.

---

**Note:** This summary focuses on extracting investment-relevant insights, operational learnings, and non-obvious observations from a leading robotics AI researcher's perspective, with particular attention to the competitive dynamics between approaches, the critical role of foundation models, and the cultural transformation occurring in Silicon Valley AI labs.