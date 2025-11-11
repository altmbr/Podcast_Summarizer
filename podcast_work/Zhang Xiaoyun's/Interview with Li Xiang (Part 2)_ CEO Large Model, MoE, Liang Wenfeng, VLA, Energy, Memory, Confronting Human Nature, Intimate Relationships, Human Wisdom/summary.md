# [Interview with Li Xiang (Part 2): CEO Large Model, MoE, Liang Wenfeng, VLA, Energy, Memory, Confronting Human Nature, Intimate Relationships, Human Wisdom](https://www.youtube.com/watch?v=RxXVq7-sJzM)

**Podcast:** Zhang Xiaoyun's
**Date:** October 31, 2025
**Participants:** Li Xiang
**Region:** Chinese
**Video ID:** RxXVq7-sJzM
**Video URL:** https://www.youtube.com/watch?v=RxXVq7-sJzM
**Transcript:** [View Transcript](./transcript.md)

---

# [Summary: Li Xiang (理想汽车 CEO) Interview - AI Strategy & VLA Development](https://www.youtube.com/watch?v=RxXVq7-sJzM)

## 1. Key Themes

### Theme 1: VLA (Vision-Language-Action) as the True Path to Autonomous Driving
Li Xiang reveals that Ideal is developing VLA (Vision-Language-Action) models, which he describes as creating a "driver AI brain" rather than just an autonomous driving system. This represents a fundamental architecture shift from end-to-end models launched just a year ago.

**Supporting Evidence:**
- "VLA is essentially a driver large model - it can work like a human driver... It went through three stages: first, rule-based algorithms like insect intelligence; second, end-to-end like mammal intelligence; third, VLA with full human-like understanding of the physical world" [[00:37:42]](https://www.youtube.com/watch?v=RxXVq7-sJzM&t=37m32s)
- "End-to-end only handles what it has learned through imitation. But VLA can handle complex situations it has never seen, like construction zones, because it has language understanding and reasoning ability" [[01:02:57]](https://www.youtube.com/watch?v=RxXVq7-sJzM&t=1h2m47s)
- "We're training a 32B parameter cloud model and distilling it to 3.2B (8-expert MoE) for edge deployment. Training includes: 1) Pre-training with V+L+VL combined data, 2) Post-training (learning to drive like driving school), 3) Reinforcement learning with human feedback and pure RL" [[00:43:41]](https://www.youtube.com/watch?v=RxXVq7-sJzM&t=43m31s)

### Theme 2: DeepSeek's Impact - Accelerating Ideal's Timeline by 9 Months
DeepSeek's open-source models fundamentally accelerated Ideal's AI roadmap, saving approximately 1 billion RMB and enabling them to skip 9 months of language model development.

**Supporting Evidence:**
- "DeepSeek's appearance accelerated our VLA development by 9 months. We originally planned to have a good language model by September 2025, but now we can stand on the shoulders of giants" [[00:57:43]](https://www.youtube.com/watch?v=RxXVq7-sJzM&t=57m33s)
- "DeepSeek taught us human best practices: First do research (not development), then R&D, then capability demonstration, then business value. Research equals capability in AI" [[00:54:42]](https://www.youtube.com/watch?v=RxXVq7-sJzM&t=54m32s)
- "Because DeepSeek helped us so much, we decided to open-source our automotive OS. This was decided within days during our 2024 year-end review, purely out of gratitude" [[00:24:18]](https://www.youtube.com/watch?v=RxXVq7-sJzM&t=24m8s)

### Theme 3: From Automotive Company to "AI Terminal Company" - Vision for 2030
Li Xiang redefined Ideal's identity from an automotive company to a "leading AI terminal company" by 2030, with specific criteria for what constitutes an AI-era terminal.

**Supporting Evidence:**
- "By 2030, we hope to become a leading AI terminal company globally. An AI-era terminal must have four characteristics: 1) 360-degree physical world perception, 2) Cognitive decision-making, 3) Action capability (controlling machines or software), 4) Reflection and feedback capability" [[01:43:44]](https://www.youtube.com/watch?v=RxXVq7-sJzM&t=1h43m34s)
- "Just like Apple wasn't just a phone company - it went from computers to iPods to iPhones. When you reach certain scale (like 500B RMB revenue), you must consider new AI terminals in users' work and life scenarios" [[01:46:41]](https://www.youtube.com/watch?v=RxXVq7-sJzM&t=1h46m31s)
- "The vehicle could become a trillion-dollar revenue product in the AI era - potentially exceeding all Chinese smartphone companies combined. But it requires full autonomous driving (L4) capability" [[02:00:32]](https://www.youtube.com/watch?v=RxXVq7-sJzM&t=2h0m22s)

## 2. Contrarian Perspectives

### 1. Against "General-Purpose Agents" - Specialized Agents Will Win
While the industry chases AGI, Li Xiang believes specialized professional agents (not general-purpose ones) will create real production value.

**Supporting Evidence:**
- "I don't believe in general-purpose agents within 5 years. Instead, we'll have an 'Agent OS' where different professional fields build their own specialized agents. A general agent is like asking one person to be an expert doctor, lawyer, and driver - impossible" [[00:54:04]](https://www.youtube.com/watch?v=RxXVq7-sJzM&t=53m54s)
- "The key distinction: information tools (like ChatGPT) provide reference; assistance tools make existing products better; **production tools actually replace your 8-hour workday**. Only production tools deserve to be called true agents" [[00:08:09]](https://www.youtube.com/watch?v=RxXVq7-sJzM&t=7m59s)
- "Two products have touched production tool territory: Cursor (for developers) and OpenAI's Deep Research. Our colleagues pay for these themselves, not using company money - that's the test" [[00:10:29]](https://www.youtube.com/watch?v=RxXVq7-sJzM&t=10m19s)

### 2. Tools Matter More Than Model Intelligence for Deployment
Contrary to the "model solves everything" mentality, Li Xiang argues tools and deterministic solutions are essential, even in the AI era.

**Supporting Evidence:**
- "You can be 10x smarter than me, but if you dig with bare hands while I use a shovel, I'm still more efficient. Better brains and better tools don't conflict - they complement each other" [[00:11:57]](https://www.youtube.com/watch?v=RxXVq7-sJzM&t=11m47s)
- "Example: Vision-language models are terrible at positional judgment. For complex toll booth scenarios (10+ lanes), the model gets confused. But a simple rule-based algorithm solved it in under a week. Why not use rules for deterministic problems? It means lower energy consumption and higher accuracy" [[01:16:23]](https://www.youtube.com/watch?v=RxXVq7-sJzM&t=1h16m13s)
- "Manus (AI product) is moving toward production tools because it calls APIs and tools - browsing SEC filings, analyst reports - not just RAG search. Professional work requires going to source information" [[00:12:20]](https://www.youtube.com/watch?v=RxXVq7-sJzM&t=12m10s)

### 3. World Model = Training Ground, Not Part of the Agent
Li Xiang defines "world model" differently from most: it's a complete physics simulation of traffic (like a realistic game engine), separate from the VLA driving model.

**Supporting Evidence:**
- "Our traffic world model has three stages: 1) Examination environment (testing VLA), 2) Data generation for training, 3) Future L4 autonomous fleet operations system. It's reconstruction + generation, indistinguishable from real traffic" [[01:11:00]](https://www.youtube.com/watch?v=RxXVq7-sJzM&t=1h10m50s)
- "Cost reduction: Validation cost per 10,000km dropped from 170,000-180,000 RMB (human drivers) to 4,000 RMB (compute costs in world model). Plus we can test exact scenarios - same vehicles, positions, speeds - impossible in physical world" [[01:08:44]](https://www.youtube.com/watch?v=RxXVq7-sJzM&t=1h8m34s)
- "There are two definitions in academia: Some call the 'what happens next' prediction (diffusion-based future trajectory) a world model. We consider that part of the driver's capability. Our world model is the complete traffic environment itself" [[01:11:46]](https://www.youtube.com/watch?v=RxXVq7-sJzM&t=1h11m36s)

## 3. Companies Identified

### DeepSeek (深度求索)
**Description:** Chinese AI startup that released open-source models (V3 and R1) matching/exceeding international capabilities at significantly lower costs.

**Quotes:**
- "DeepSeek demonstrated the best human practices: Research first (not R&D). Research equals capability. It used MoE architecture (6x71B model), extremely efficient training and inference, saving 9 months and ~1B RMB for us" [[00:54:42]](https://www.youtube.com/watch?v=RxXVq7-sJzM&t=54m32s)
- "When chatting with Liang Wenfeng (DeepSeek founder), two key insights: 1) Let young people do research because experience can be a barrier, 2) Use Chinese education exam feedback systems as RL training methodology - complete answer processes with clear feedback" [[02:00:55]](https://www.youtube.com/watch?v=RxXVq7-sJzM&t=2h0m45s)

### Cursor
**Description:** AI-powered code editor that developers willingly pay for themselves.

**Quotes:**
- "Cursor and OpenAI's Deep Research are the only two products our colleagues consider production tools - they pay with their own money, not company funds" [[00:10:29]](https://www.youtube.com/watch?v=RxXVq7-sJzM&t=10m19s)

### Manus (AI Product)
**Description:** AI agent product that actively uses tools (browsing websites, reading documents) rather than just searching.

**Quotes:**
- "Manus took the biggest step toward production tools - it uses tools like browsing SEC filings, Tesla investor relations sites, and analyst reports directly, not just RAG search. That's how professional workers actually operate" [[00:12:20]](https://www.youtube.com/watch?v=RxXVq7-sJzM&t=12m10s)

## 4. Operating Insights

### Insight 1: The "Research → R&D → Demonstration → Business Value" Framework
Li Xiang learned from DeepSeek that skipping research leads to wasted R&D. True capability building requires research first.

**Supporting Evidence:**
- "DeepSeek taught us: First research (understand the problem deeply), then R&D, then capability demonstration, then business value. We often jump straight to R&D without research, which is why things fail" [[00:54:42]](https://www.youtube.com/watch?v=RxXVq7-sJzM&t=54m32s)
- "Our autonomous driving and model teams publish papers extensively - other companies cite our research. Research makes R&D much more efficient. If you don't research first, you can't even pick the right direction" [[00:55:04]](https://www.youtube.com/watch?v=RxXVq7-sJzM&t=54m54s)

### Insight 2: Three-Person Core Creates "Stronger Brain + Stronger Heart"
Organizations should be built around 3-7 person cores (not 2, not 8+) to create optimal decision-making and energy.

**Supporting Evidence:**
- "Three people form critical support: one person is too autocratic, two people create deadlock, but three create a stronger collective brain through debate while maintaining unified external action. We had me, Qinzhi, and Fanwei initially" [[01:51:58]](https://www.youtube.com/watch?v=RxXVq7-sJzM&t=1h51m48s)
- "When Ma Donghui stepped up after Xie Yan left, Litui and I became his support system - 'you will never fall, we'll hold you up.' Later added Xie Yanzong and Zuo Liaojun to form five-person core" [[01:53:33]](https://www.youtube.com/watch?v=RxXVq7-sJzM&t=1h53m23s)
- "3-7 people is optimal range. Less than 3 lacks diversity; more than 7 becomes unwieldy for energy alignment" [[01:54:29]](https://www.youtube.com/watch?v=RxXVq7-sJzM&t=1h54m19s)

### Insight 3: Work = Social Value, Family = Intimacy Value - Both Essential
Li Xiang reframes work relationships as intimate relationships because they fundamentally shape your social value and identity.

**Supporting Evidence:**
- "Colleagues ARE intimate relationships. Why? Your work determines social value - what company, what role directly affects how society perceives you, including school admissions for your kids. Work is 8+ hours daily, more than family time" [[02:23:37]](https://www.youtube.com/watch?v=RxXVq7-sJzM&t=2h23m27s)
- "Two separate values: Work provides social value (serving customers, creating products). Family provides intimacy value (happiness through quality companionship). Better work enables better life; better life creates energy for better work" [[02:24:37]](https://www.youtube.com/watch?v=RxXVq7-sJzM&t=2h24m27s)

### Insight 4: "I Need Them" Before "They Need Me" - Foundation of Intimate Relationships
Reversing the dependency mindset creates genuine partnership and energy flow.

**Supporting Evidence:**
- "Most important realization: In intimate relationships, emphasize 'I need them' before 'they need me.' I need my spouse, I need my children, I need Litui and Ma Donghui - they make me better. This creates proactive engagement" [[02:21:27]](https://www.youtube.com/watch?v=RxXVq7-sJzM&t=2h21m17s)
- "When you truly need people, you become proactive - you don't wait for things to happen or become terrible. You actively engage because their growth is your energy source" [[02:23:01]](https://www.youtube.com/watch?v=RxXVq7-sJzM&t=2h22m51s)

### Insight 5: Super-Alignment Team (100+ People) - As Model Capability Grows, Professional Behavior Becomes Critical
As AI models become more capable, they need proportionally stronger alignment - like hiring professional drivers vs race car drivers.

**Supporting Evidence:**
- "We established a super-alignment team of 100+ people last year (when we hit 10M km milestone). Not about collision avoidance (that's capability) - about value alignment: following traffic rules, human driving habits, comfort" [[01:13:13]](https://www.youtube.com/watch?v=RxXVq7-sJzM&t=1h13m3s)
- "Model capability vs professionalism: I can't hire a race car driver as my daily driver - I need a professional driver. Capability alone isn't enough; professional behavior (safety, comfort, compliance) is equally important" [[01:13:43]](https://www.youtube.com/watch?v=RxXVq7-sJzM&t=1h13m33s)

## 5. Overlooked Insights

### Insight 1: The "Scale → User Needs → Technology/Product → Organization" Strategic Loop
Li Xiang uses a unique strategic framework where scale is central, surrounded by three dynamic variables that must change in concert.

**Supporting Evidence:**
- "In our strategy sessions, we put scale (revenue) at the center - that's the certainty. Around it are three dynamic variables: user needs, technology/product, and organization. These three influence each other, but I don't change organization just because technology changed - only when user needs shift" [[00:13:56]](https://www.youtube.com/watch?v=RxXVq7-sJzM&t=13m46s)
- "Example: If we want 100M+ annual sales (reaching BBA scale), we need to cover more user segments beyond families - hence family sedans and larger MPVs. Organization must then evolve to support broader product portfolio" [[01:27:19]](https://www.youtube.com/watch?v=RxXVq7-sJzM&t=1h27m9s)

**Why This Matters:** Most companies either ignore scale constraints or reorganize reactively to every tech trend. Li Xiang's framework shows disciplined strategic thinking - technology possibilities don't drive org changes; user need shifts validated by technology maturity do.

### Insight 2: Validation Cost Collapsed 40x Through World Model - But Nobody Talks About Economics
The most dramatic AI impact at Ideal isn't the technology itself, but the economics: per 10,000km validation costs dropped from 180,000 to 4,000 RMB (45x reduction).

**Supporting Evidence:**
- "Using world model simulation, our validation cost per 10,000km went from 170,000-180,000 RMB (human drivers, vehicles, etc.) to about 4,000 RMB this year - mostly compute costs. And effectiveness is far superior because we can reproduce exact scenarios" [[01:08:44]](https://www.youtube.com/watch?v=RxXVq7-sJzM&t=1h8m34s)
- "Example of why it's better: If a problem involves our vehicle + multiple traffic participants + specific road conditions, it's nearly impossible to reproduce that exact combination on real roads. But in world model, we replay it precisely to validate fixes" [[01:09:36]](https://www.youtube.com/watch?v=RxXVq7-sJzM&t=1h9m26s)

**Why This Matters:** While everyone debates model architecture, the real competitive moat is economic - Ideal can iterate 45x faster at 1/45th the cost. This validation infrastructure becomes insurmountable advantage as complexity grows. This is the "unsexy" infrastructure work that creates durable leads.

---

**Note:** Timestamps are preserved as [HH:MM:SS] for reference. All quotes translated from Chinese to English as requested.