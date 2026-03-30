# [134. 和谢晨聊“数据的综述”：AI和机器人数据的历史、版图、金字塔与Recipe](https://www.xiaoyuzhoufm.com/episode/69c953b4b977fb2c478df5c3?utm_source=rss)

**Podcast:** 张小珺Jùn｜商业访谈录
**Date:** 2026-03-30
**Processed:** 2026-03-30T17:11:31Z
**Participants:** Zhang Xiaojun, 张小珺
**Episode URL:** https://www.xiaoyuzhoufm.com/episode/69c953b4b977fb2c478df5c3?utm_source=rss
**Transcript:** [View Transcript](./transcript.md)

---

# Episode Summary: Data in AI & Robotics – An Industry Overview with Xie Chen (Steve)

**Podcast:** 张小珺Jùn｜商业访谈录
**Guest:** Xie Chen (Steve), Founder & CEO of Guanglun Intelligence (光轮智能)
**Host:** Zhang Xiaojun

---

## 1. Key Themes

### Data as the Foundational "Education System" for AI Intelligence

Xie Chen draws a compelling analogy between data and human education, arguing that data is not merely a resource but the entire learning infrastructure for AI. The evolution goes from static datasets (rote memorization), to factory-produced labeled data (mass education), to expert-driven feedback and evaluation (personalized mentorship).

> "I think data for intelligence is similar to how we humans acquire knowledge to continuously improve ourselves. Knowledge is a primary first-principles need for human intelligence. By the same logic, data is critically important for intelligence." [00:21:44]

He further argues we are now entering an era where the data provider must act as a "teacher who diagnoses and corrects" rather than a factory that fills orders:

> "In the current data... it's more of a targeted delivery. So Scale actually started calling itself a 'data foundry' at this point — somewhat like TSMC's wafer fab model. Essentially still a factory, but with more process, more know-how, more secret sauce." [00:09:21]

### Robotics Data is Structurally Harder Than LLM Data — By Orders of Magnitude

Xie Chen makes an emphatic distinction: while LLMs have "hit the wall" on pre-training data, robots are operating in a desert. He quantifies this gap starkly.

> "If 1 million deployed robots providing data is a starting point — and that starting point might not even be 100 points, maybe 60 — right now there aren't even 10,000 robots, whether in real or simulated or human data form, providing this type of data. So if you look at it from this angle, it might not even be 0.6 points." [01:03:20]

He identifies two structural gaps robotics faces that LLMs don't: (1) lack of sufficient pre-training data grounded in physical reality, and (2) no scalable evaluation mechanism comparable to self-driving's "shadow mode" or LLMs' user feedback loops:

> "For robotics, it doesn't currently have the foundation to provide shadow mode in the real world at scale. The only thing it can do is use simulation to scale evaluation and get more signals, feeding those signals back to the embodied brain so they can keep improving." [01:01:38]

### The Data Pyramid: Body-Agnostic Data Will Dominate, Breaking Tesla's Closed-Loop Logic

Xie Chen argues the "Tesla data flywheel" model — where scale of hardware deployment generates training data — fundamentally breaks down for robotics. The majority of useful training data will NOT come from physical robots.

> "I think the data architecture will conform to the data pyramid. The smallest data volume will be from real deployed robots... The middle portion will be simulation-generated data. And at the bottom will be internet and human first-person perspective data. These bottom two — simulation and human first-person data — don't require a hardware body to generate, and their scalability is far superior." [00:51:19]

He cites Optimus/XAI as inadvertent proof: "Tesla's robots are having their brain provided by XAI, not Tesla itself. By the same logic, it will definitely be a large model company doing the brain work... The data core will be body-agnostic data — that's squarely a large model company's game." [00:52:44]

---

## 2. Contrarian Perspectives

### The Most Valuable Training Data is "Fail-Then-Succeed" — Not Perfect Demonstrations

Counter to the intuition that clean, correct demonstrations are optimal training data, Xie Chen argues that recovery data (failure followed by correction) is MORE valuable — and commands a price premium.

> "The most effective data is actually the data of first failing then succeeding... I was reaching for a mushroom, I sliced it, but I didn't grip it tightly enough and it fell on the table. I picked it up again and placed it back on the pizza. This data — we call it negative samples or correction data — is often more effective." [00:33:50]

> "People might think a perfect pizza-making video would be the most expensive. But actually, it's not. If you dropped a few pieces of vegetables and picked them back up, that's worth more. It's similar to human learning — the experience of failing then succeeding is the most valuable." [02:00:01]

### Chinese Robot Body Companies Building Data Collection Centers Are Making a Strategic Error

Xie Chen suggests that many Chinese robot hardware companies are building their business model around selling robots as data collection hardware — but this is "the tail wagging the dog," with commercial incentives distorting their technical beliefs.

> "Their customers often use [the robots] to build data collection centers... so they need to believe in real-machine data to sell their hardware. It's essentially the rear end determining the head. They need to advocate for the real-machine approach in order to make their data-collection-based business model work." [01:24:00]

He adds that even real-machine data labs use fake props: "If you visit their collection centers, you'll see they're also using simulation. They're using fake bananas, fake apples — not real ones. The scene variation is minimal." [01:25:31]

### Simulation Will Replace Tesla-Style Data Flywheels, Not Just Accelerate Them

The conventional view is that simulation is an "accelerator" complementing real-world data. Xie Chen argues it is a *prerequisite* for robotics — without it, general intelligence in embodied AI simply cannot emerge.

> "Simulation is a necessary condition for robots. Without it, this definitely can't be done... If there's no simulation and human data at the bottom of the embodied intelligence pyramid, general intelligence in embodied AI simply cannot emerge." [01:43:05]

### Scaling AI Capability Increases Data Hunger, Not Decreases It

Against the common narrative that better AI will need less data, Xie Chen argues the opposite — more capable AI demands more and harder data.

> "The smarter a person is, the more they love learning. The amount of books they read daily doesn't decrease — it increases... My current view is that the stronger the intelligence, the greater its hunger for knowledge and data." [02:33:11]

### Physical Simulation and Video/World Models Are Complementary, Not Competing

Widely assumed to be substitutes, Xie Chen argues they are deeply symbiotic — world models need physics-grounded simulation data to improve, while simulation needs world models to scale generalization.

> "I don't think simulation and world models have a relationship where one replaces the other. They're more of a symbiotic relationship... They should together achieve a larger goal: providing better learning capability for intelligence." [01:31:34]

---

## 3. Companies Identified

**Scale AI**
Description: US data labeling and AI data infrastructure company
Why mentioned: Identified as the company that industrialized AI data production — first for autonomous driving, then for LLM post-training/RLHF. Called a pivotal company that "led the industrialization of AI data twice."
> "Scale truly industrialized AI data... processing it factory-style, ensuring quality, efficiency, and delivery timelines. And I think around 2021-2022, they entered the GPT-2 era and began serving LLM post-training and evaluation data." [01:14:53]

**Surge / Mercor (Scale AI successors)**
Description: Companies providing expert-driven post-training and evaluation data for frontier LLMs
Why mentioned: Represent the new paradigm of data provision — expert humans (engineers, mathematicians, lawyers, doctors) at $100+/hr actively evaluating and generating data, not just labeling it.
> "Companies like Mercor and Surge... they find highly qualified people to provide more evaluation to their model clients' algorithms, give feedback through this evaluation, and stimulate more targeted data needs to help the algorithm improve." [00:26:58]

**Unitree (宇树)**
Description: Chinese humanoid/quadruped robot hardware company
Why mentioned: Singled out as strategically clear about its role as a body/hardware company — not competing with brain companies, focused on stable, mass-producible hardware.
> "Unitree's differentiation is the clearest. It's firmly committed to building its hardware body well. I don't think Unitree will compete with brain companies. They're a very pragmatic company that knows where they have advantages and where they don't want to develop. Knowing your boundary is key." [02:22:36]

**Zhiyuan (智元)**
Description: Chinese humanoid robot company
Why mentioned: Praised for commercial execution and strategic clarity from day one — building the full vertical stack and focusing on supply-driven market creation.
> "Zhiyuan's commercialization is going very well. From day one they thought clearly: to do this systematically, they needed to fully integrate the upstream and downstream. I think their mass production capability is very strong." [02:24:01]

**Figure**
Description: US humanoid robot company
Why mentioned: Identified as the closest thing to a "Tesla of robotics" — building its own hardware, scaling production, deploying, and developing its own brain.
> "Figure is hoping to become the Tesla of embodied intelligence. It has its own hardware, is scaling mass production, deploying, and also building its own brain." [01:41:30]

**Meta (Ray-Ban AI glasses)**
Description: Meta's consumer AI glasses product
Why mentioned: Cited as the ideal model for human first-person data collection — a device people want to wear for its own merits (stylish, has AI assistant), which incidentally captures data.
> "Meta's Ray-Ban glasses have a very clever point: first, it's a very cool, good-looking pair of glasses. Second, it has an AI assistant you can converse with. I think this type of wearable — one that people already have rather than something you need to get people to buy — is the most useful long-term." [01:54:51]

**NVIDIA**
Description: GPU/accelerated computing platform company
Why mentioned: Identified as an early believer in simulation for robotics (Omniverse), and now increasingly aggressive in physical AI. Also used as personal career context.
> "NVIDIA is making very aggressive moves [in robotics]. Jim's team, Minyu's team — they're sufficiently strong teams with sufficient resources. NVIDIA takes physical AI extremely seriously." [02:28:07]

---

## 4. People Identified

**Fei-Fei Li (李飞飞)**
Description: Stanford AI professor, creator of ImageNet, founder of World Labs
Why mentioned: Credited as the foundational figure who "truly defined AI data." Also highlighted for her Behavior benchmark (used to evaluate embodied AI), which remains the hardest evaluation suite in the industry with top scores only at 26% success.
> "Fei-Fei Li truly defined the AI data field. Her contribution is extremely high." [01:14:24]
> "Behavior — made by Fei-Fei Li's team based on simulation, designed for embodied intelligence evaluation — contains difficult long-horizon tasks. The highest success rate is currently 26%. There's still a ways to go." [01:06:24]

**Zhu Yuke (朱一可, referenced as Fei-Fei's student)**
Description: Researcher, credited with articulating the Data Pyramid concept for embodied AI
Why mentioned: Identified as the originator of the "Data Pyramid" framework that is now shaping how the entire industry thinks about robotics training data.
> "The data pyramid concept was proposed by Professor Zhu Yuke, a student of Fei-Fei's. He essentially analyzed that the most data for embodied intelligence won't come from the body itself... [it will rely on] simulation and internet/human data." [01:43:29]

**Tan Jie (谭杰, referenced as "Tangjie")**
Description: Robotics/AI researcher or practitioner (likely from a major lab)
Why mentioned: Xie Chen expresses strong agreement with Tan Jie's view that simulation's challenge is "sim-to-real transfer," not generalization — generalization should be solved by generating massive simulation data volume.
> "Tan Jie's point I remember well: sim-to-real is a sim-to-real problem, not a generalization problem. Generalization should be solved by generating extremely large amounts of simulation data." [01:27:03]

---

## 5. Operating Insights

### Evaluation Infrastructure as the Bottleneck — Build It First

Xie Chen's experience reveals that the companies making the fastest model progress are those who invested in scalable *evaluation* before worrying about more training data. For operators building AI products, this suggests the first investment should be evaluation/measurement infrastructure.

> "The core issue [for all our recent new clients who previously rejected simulation] is: they cannot scale their evaluation anymore. That's their core problem. They believe their algorithms are already good enough, but they can't measure it at scale." [01:18:56]

### The "Shadow Mode" Framework Should Be Replicated in Every AI Product

Xie Chen articulates that autonomous driving succeeded partly because of free, always-on evaluation via shadow mode (comparing model outputs to human driver behavior in real time). This is a generalizable operating principle for AI product development.

> "Self-driving's evaluation is essentially free. They deploy the algorithm in shadow mode — the algorithm runs alongside but doesn't execute. Its output is compared to the human driver's actions. When there's a discrepancy, that becomes feedback... an extremely cheap signal." [01:00:13]

### Data Companies Should Be Evaluation-Led, Not Delivery-Led

Traditional data companies respond to client requests. Xie Chen argues the winning model is for data providers to proactively evaluate the client's model, identify weaknesses, then stimulate targeted data production — forming a feedback loop where the data company essentially becomes the model's "teacher."

> "The data company and the large model company will increasingly form a symbiotic relationship. The large model company needs the data company to provide effective evaluation and data. The data company needs the large model company's model to provide better data validation feedback to iterate their production pipeline." [00:53:42]

---

## 6. Overlooked Insights

### The "RL Environment" (RL-inf) for Digital Agents is the Exact Analog to Simulation for Physical Robots — and Both Markets Are Nascent

Xie Chen briefly mentions "RL-inf" (reinforcement learning environments for digital agents) as a critical emerging data product for LLM agents — virtual browsers, virtual coding environments, virtual shopping sites. This is mentioned almost in passing but represents a structurally parallel opportunity to simulation for robotics: a largely unbuit infrastructure layer that every frontier AI lab will need.

> "For large model agents, there's a very critical data product called RL-inf — serving reinforcement learning environments. This environment is essentially a virtual environment: a virtual website, virtual JD.com, virtual shopping site, virtual coding environment — helping them continuously fine-tune themselves through reinforcement learning in this environment, trial and error, and self-improvement." [01:04:28]

The insight: **whoever builds the dominant RL environment infrastructure for digital agents** is building the "simulation layer" for software AI, just as Guanglun is building it for physical AI. This company likely doesn't exist yet at scale, and the market is not being talked about with the same intensity as robotics simulation.

### Mass-Market Consumer Wearables (Like Ray-Ban Meta) Are Secretly the Most Important Infrastructure Play for Robotics Data

Xie Chen briefly mentions this but neither he nor the host dwell on it: consumer wearables that people *want to wear* are the only scalable path to first-person human data collection. This implies that Meta — not any robotics company — may be accumulating the most strategically valuable training data asset for embodied AI through their glasses product, possibly without fully realizing or disclosing it.

> "Ideally, people genuinely want to wear these glasses — not wear them for the sake of data collection. That might be the point that human data truly needs to reach... If a consumer hardware company launches a hit product and everyone is wearing it, that's the real inflection point." [01:55:57]

The implication: **any investor evaluating robotics data moats should be tracking consumer wearable adoption metrics**, particularly Ray-Ban Meta glasses, as a leading indicator of the most valuable body-agnostic training data accumulation. This is a non-obvious cross-sector connection the broader market is not pricing in.