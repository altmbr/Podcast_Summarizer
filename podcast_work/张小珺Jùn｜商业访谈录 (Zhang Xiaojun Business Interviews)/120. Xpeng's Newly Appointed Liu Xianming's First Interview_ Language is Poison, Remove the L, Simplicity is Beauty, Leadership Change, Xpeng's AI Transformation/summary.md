# 120. Xpeng's Newly Appointed Liu Xianming's First Interview: Language is Poison, Remove the L, Simplicity is Beauty, Leadership Change, Xpeng's AI Transformation

**Podcast:** 张小珺Jùn｜商业访谈录 (Zhang Xiaojun Business Interviews)
**Date:** 2025-11-18
**Participants:** 张小珺, 刘鲜明
**Region:** Chinese
**Video ID:** 691c3670cbba038b421f74a4
**Video URL:** https://www.xiaoyuzhoufm.com/episode/691c3670cbba038b421f74a4
**Transcript:** [View Transcript](./transcript.md)

---

# Podcast Summary: Xpeng's Liu Xianming on AI Transformation and Autonomous Driving

## 1. Key Themes

### The Radical Simplification Philosophy: Removing Language as the Core AI Breakthrough

Liu Xianming describes the counterintuitive decision to remove language tokens from Xpeng's VLA (Vision-Language-Action) model, transitioning to what he calls "VLA 2.0." This wasn't just a technical adjustment but a fundamental reimagining of how autonomous driving AI should work.

"Language is离散的空间...但是我们说物理世界的模型...它输入是连续的视觉信号...它的输出也是个连续的空置空间...用语言区生成离散的空间化这样的一个Token，再去翻译出来这样连续控制量，显然就是一个低效的一个过程" [01:18:38] - Liu Xianming explaining why language tokens create inefficiency in physical AI systems.

The team discovered that while language models provide good initial representations, they become a bottleneck for scaling. "L不够高效，还成为中间的Bottleneck...L本身是离散化的，而且你要去解决...你的输入是连续器号，输出是连续空间是动作，那我中间为什么要差一个L呢" [01:07:35] Liu states, articulating the core insight that led to their breakthrough.

### Data as the Ultimate Competitive Moat in Physical AI

Liu consistently emphasizes that data—not algorithms or model architecture—is the fundamental advantage for OEMs in autonomous driving. The scale reached is significant: "我们大概现在训练一个模型大概是20、70万到30万小时数据" [01:01:23] - approximately 200,000-300,000 hours of training data per model.

What makes this particularly powerful is the closed-loop system: "我有一个模型上出现了一个问题，我可以自动化一个去找到我数据分布的这个新格爾的point...迅速地讓我的車隊明天就會收上來數據" [01:13:45] This ability to identify data gaps and rapidly collect targeted data the next day is something only OEMs with vehicle fleets can achieve, creating an insurmountable advantage over third-party suppliers.

### Organizational Transformation: From Internet Speed to AI Cadence

The transition from traditional automotive or internet company structures to AI-first organization requires fundamental changes. Liu describes the challenge: "做AI这个东西，你很难像传统的稳定开发一样定一个时间节点，想打战役一样去做这个事情...它更多是一个系统性的一个体系化的东西" [01:04:08]

The solution involves extreme organizational flattening: "我们变平化了...我一直变平到最一线单之内，我可以看他们的代码，看他们的实验结果" [01:27:26] This allows rapid iteration and decision-making that AI development requires, contrasting sharply with traditional hierarchical structures.

## 2. Contrarian Perspectives

### Rejecting Open-Source Foundation Models Despite Industry Consensus

While most companies leverage open-source language models as foundations, Liu argues this approach is "像一个毒药一样，你会越来越重来去依赖于它" [00:21:54] - like poison that creates increasing dependency. 

His reasoning challenges conventional wisdom: "即使我第一次去打标签，我还是要去做人工之前，然后再去做训练...这个会遇到一个跟Tesla一样的问题，就是你会有个维修灾难的问题" [01:03:54] The reliance on language supervision creates labeling bottlenecks and dimensionality disasters that fundamentally limit scaling potential.

Most remarkably, this decision was made mid-2024 when the entire industry was moving toward VLM architectures: "差L差不多今年的上半年到年中的时候吧...很快" [00:28:09] The speed of this decision and the willingness to abandon what appeared to be working demonstrates unusual conviction.

### Rules and Language Must Be Removed, Not Refined

Counter to incremental improvement philosophy, Liu advocates for complete removal of legacy systems: "所以从去年到今年，拆了激光雷达，拆了规矩规则，端端端也拆了，然后再后面拆域演，基本全拆了" [00:40:39] - systematically removing LiDAR, rules, end-to-end components, and language.

The team faced significant internal resistance: "这个事情就是去年的时候，其实我们内部有很多的被退回头的争论" [01:42:37] Yet Liu remained firm: "当你有了一个强大的模型之后，你会发现你很多你知情不敢想的事情都能做的" [00:28:26]

This philosophy directly contradicts the "safety through redundancy" approach many companies take. Liu's bet is that simplicity and scale trump complexity and rules.

### Third-Party Autonomous Driving Suppliers Cannot Win Long-Term

Liu makes a stark prediction against companies like Huawei or Momenta that supply autonomous driving systems: "对於第三方來說，它是很難規模化的拿到你想要的數據的" [01:13:27]

His argument: "當你想要去收集靠著KS數據的話，首先你要知道什麼靠著K的數據...如果沒有零到一的把這套規則的體系...你根本不知道什麼靠著KS" [00:51:12] Without deployed vehicles and baseline systems, suppliers cannot identify corner cases or collect targeted data effectively.

This challenges the prevailing industry structure where many OEMs rely on third-party solutions, suggesting massive consolidation ahead.

## 3. Companies Identified

### **Cruise**
**Description**: General Motors' autonomous vehicle subsidiary where Liu worked from 2020-2024.

**Why mentioned**: Cruise represented the state-of-the-art in robotaxi development and Liu's formative experience in scaling autonomous systems.

**Key Quotes**: 
- "Cruise应该是当时做的做增加式企业里面Infra团队算是最大规模的一个...有700人的Infra团队" [00:07:28] - Illustrating Cruise's massive infrastructure investment as a startup.
- "那个时候开始去做一件事情叫做Contentance of the Limit性持续学习的一种机器...所有人躺在下午一的海滩上，等着KruzCoin这个精闭风吹吻掉下来，就是数据迭代来解决一切的问题" [00:08:43] - The vision of continuous learning machines that would improve autonomously through data.

### **Facebook/Meta AI Research**
**Description**: Meta's AI research division where Liu worked 2016-2018.

**Why mentioned**: Formative experience in large-scale AI infrastructure and research methodology.

**Key Quotes**:
- "当时Facebook最大的开零级决象，大概用了整个Facebook超过16%的计算资源来做一件事，然后那个事情就是...给我海利这个国家他在地震之前和地震之后人口分布和建筑分布的这个数据" [00:05:45] - Demonstrating the scale of impact-driven AI work.
- "Facebook非常累...每天早上从早公司到晚，然后晚上写课的写到11点12点" [00:12:15] - Countering the stereotype of easy big tech jobs.

### **Waymo**
**Description**: Google's autonomous vehicle company, mentioned as the leading competitor during Liu's time at Cruise.

**Why mentioned**: The benchmark and primary competitor that drove technical decisions.

**Key Quote**: "当时去的时候Cruise的技术站比我想了还要懒了还要查...Cruise所面临的挑战和差距当时还是比想象的要高很多...靠传统这种打法能不能追得上回梦" [00:07:07] - Illustrating the competitive gap that motivated aggressive innovation.

## 4. People Identified

### **He Xiaopeng (何小鹏, Xpeng CEO)**
**Description**: Founder and CEO of Xpeng Motors, technical background, former UC Web founder.

**Why mentioned**: Exemplifies rare founder willingness to bet on long-term AI despite uncertainty.

**Key Quotes**:
- "来小朋友就是那个时候大师兄跟我展示肺骨帮工室约了一个小时...出来就跟H2说了什么还准备奥帆了就直接来了" [00:14:29] - The decisive one-hour conversation that led to Liu joining.
- "我们最开始的时候还是挺贵的...跟男人说我要做这个事...没有任何弹幕，然后也没有任何的结果，然后你打算说这么多GPU 这么多钱，你怎么办，打算说好，就完了" [00:35:18] - He Xiaopeng's willingness to invest in unproven AI research.
- "大师兄是一个非常谈成的一个人，而且就是一个技术宅男" [00:15:38] - Describing He's technical depth and judgment.

### **Andrej Karpathy**
**Description**: Former Tesla AI director, now at OpenAI; pioneer of end-to-end autonomous driving.

**Why mentioned**: Intellectual predecessor whose work on end-to-end learning influenced Xpeng's direction.

**Key Quote**: "这个最早该进体会Andry and Patry...如果我能有一个模型的你纯粹的神经网络我能数据解带去解决很多问题就可以了" [00:15:33] - Crediting Karpathy's vision of pure neural network approaches.

### **Yann LeCun**
**Description**: Chief AI Scientist at Meta, Turing Award winner, Liu's former colleague at Facebook.

**Why mentioned**: Example of academic research informing practical systems, and recent relevant work on vision-language models.

**Key Quote**: "最近有一个很有意思类似的DPC楼下...它其实告诉你一个新的一个方法就是我们没有必要去把一个图像对起到文字的Token的Space里面" [01:00:00] - Recent research validating Xpeng's approach to removing language bottlenecks.

## 5. Operating Insights

### Extreme Organizational Flattening Enables AI Speed

Liu implemented radical organizational changes: "我们变平化了...我一直变平到最一线单之内，我可以看他们的代码，看他们的实验结果，去做的需要问题" [01:27:26]

This isn't just about hierarchy—it's about information flow: "大家就在办公室里面隨時去討論問題，有了新的想法周快速的做出捲測" [01:27:32] The ability to go from idea to experiment rapidly requires removing all organizational friction.

Contrast with traditional management: "很难想像就是我這一個團隊的一個大團隊的力的會直接寫辦法直接地板子，這是很難想像的一件事情" [01:27:57] - In most organizations, leaders several levels up would never write code or directly review experiments.

### Infrastructure Investment Must Precede Model Scaling

Liu's first priority upon joining wasn't models but infrastructure: "第一步就是InfoStraucer，肯定是我的稳定性InfoStraucer Skulling Up，这是有一段时间的主要的关注点" [01:03:17]

The reasoning: "当你有几个几十个Pytovice这Data要去读的时候瞬间读进来，在模型训练里面也是做不到的...训练一个模型你几千块GPU你训练一个模型五分钟让它不崩掉，这个事情也是一个Pyco" [01:03:08] Without stable infrastructure that can handle petabyte-scale data and thousand-GPU training runs, model improvements are impossible.

### Technical Breakthroughs Come from Removing, Not Adding

The pattern Liu describes repeatedly: identify bottlenecks, then remove rather than optimize: "简单的东西一定是好多东西一定是简单的...世界上好东西都一定是简单的" [00:28:37]

Specific example: "拆了激光雷达，拆了规矩规则，端端端也拆了，然后再后面拆域演" [00:40:39] - Progressively removing LiDAR, rules, end-to-end modules, and language.

The counterintuitive result: "拆掉它发现我们第一个反应是拆掉它之后会担心它不work，比如说在红驴灯然后再软软区，但是发现根本就没出现，就非常自然地就过去了" [01:01:38] - Removing language tokens didn't cause the feared regressions; the model simply adapted.

### Data Collection Systems Are More Valuable Than Algorithms

Liu emphasizes: "我来小彭的核心左计是数据，数据就是一座情况" [01:13:08] But it's not just data volume—it's the collection and targeting system.

The process: "我可以自动化一个去找到我数据分布的这个新格爾的point，就哪些地方是我数据比较缺失的地方，迅速地让我的车队明天就会收上来数据" [00:51:38] This closed-loop system—identify gaps algorithmically, deploy fleet to collect specific scenarios, retrain—is the actual moat.

Without this: "如果没有零到一的把这套规则的体系...你发现你收拾很多数据都是无效的数据" [00:51:10] Most collected data is useless without a system to identify what's valuable.

## 6. Overlooked Insights

### The Scaling-to-Deployment Gap as the Real Technical Challenge

While Liu discusses removing language tokens and architectural decisions extensively, a subtler insight emerges around [00:52:06]: "怎麼計劃安全下顯的問題...我可以通過雲端的Telopps或者是雲端的階管這樣的安全遠方式來去做，但是其實本身來說就是你怎麼去降低你系統出錯的概率從而去降低雲端阶管的平次，降低成本達到一顆商的状态"

This reveals the critical insight: The real challenge isn't achieving good performance—it's achieving **economic** L4 through minimizing remote operator intervention. The technical problem is actually a cost problem. Companies can achieve high safety through human teleoperation backup, but that doesn't scale economically. The breakthrough is reducing system errors enough that remote intervention becomes rare enough to be commercially viable.

This is why Liu mentions: "明年我觉得至少先把这个事情本身先做好，再量起来，先去规模化法的吹起来" [00:53:01] The 2025 goal isn't just technical capability but proving economic scalability through reduced intervention rates.

### Shadow Mode as the Critical Zero-to-One Enabler

A brief but crucial comment at [00:51:05]: "有一些Shadow的这个影子模式在比如说有些用户接管的数据，如果这些数据你连一个基本系都没有大好啊，你发现你收拾很多数据都是无效的数据"

This reveals why the 0-to-1 rule-based system wasn't wasted effort—it created the shadow mode capability that makes data collection valuable. Without a baseline system running in shadow mode to identify where it would have failed, you cannot systematically collect the right corner cases.

This explains the sequencing: rules → end-to-end → VLA → world model. Each stage enables better data collection for the next. It's not that the previous approach was wrong; it was necessary infrastructure for scaling the next approach.

This insight fundamentally changes how to think about technical transitions: the "obsolete" system is actually the data collection instrument for its replacement. Companies trying to skip directly to end-to-end without this infrastructure will struggle with data quality regardless of model architecture.

---

**Key Timestamps Reference:**
- Liu's background and joining Xpeng: [00:00:00-00:16:00]
- Technical architecture evolution: [00:16:00-00:30:00]
- VLA 2.0 and removing language: [00:28:00-00:42:00]
- World model discussion: [00:42:00-00:54:00]
- Data and corner cases: [00:50:00-00:57:00]
- Leadership and organization: [00:56:00-01:12:00]
- Cultural adaptation: [01:12:00-01:30:00]
- Future outlook: [01:30:00-01:48:15]