# [Sergey Levine - Building LLMs for the Physical World - [Invest Like the Best, EP.465]](https://colossus.com/episode/building-general-physical-intelligence)

**Podcast:** Invest like the best
**Date:** 2026-03-31
**Processed:** 2026-03-31T17:06:42Z
**Participants:** Patrick O'Shaughnessy, Sergey Levine, Show Disclaimer
**Episode URL:** https://colossus.com/episode/building-general-physical-intelligence
**Transcript:** [View Transcript](./transcript.md)

---

# Sergey Levine – Building LLMs for the Physical World
**Invest Like the Best, EP.465**

---

## 1. Key Themes

### Generality as the Winning Strategy in Robotics AI
The core thesis of Physical Intelligence is that solving the general problem of robotic intelligence is actually easier in the long run than building narrow, task-specific robots. This mirrors the lesson learned from LLMs, where general models outperformed domain-specific ones.

> "Part of the thesis of this company is that we believe that doing it at the full level of generality might actually in the long run be easier than trying to special case very specific narrow application domains. Again, in much the same way that for language models, it turned out to be easier in some ways to solve natural language tasks in their full generality than to narrowly target like machine translation or sentiment analysis." [00:04:07] — Sergey Levine

### The Data Flywheel Problem: Robots Must Become Useful Before They Can Become Great
Unlike LLMs which had the internet as a training corpus, robotic AI has no equivalent data reservoir. The critical insight is that the goal isn't to pre-define the size of the dataset needed — it's to get robots deployed and useful enough that they self-generate training data at scale.

> "My sense is that we actually don't need to know. What we need to do is get to the point where these systems are useful enough that they can go on to the world and gather more data themselves. Tesla doesn't worry about how much data their cars can collect. If anything, it's the other way around. That's a little too much data." [00:21:02] — Sergey Levine

### Common Sense is the Missing Link Between Physical Skills and General Intelligence
The deepest unsolved problem in robotics isn't dexterity — it's common sense: the ability to apply semantic knowledge from other domains to novel physical situations. Multimodal LLMs are now providing a path to inject this, but grounding that knowledge in physical context remains a hard technical challenge.

> "This has been like a huge mystery in robotic learning world. Where do you get that common sense? And this is what's changed in the last few years, because it turns out that multimodal language models are really good at pulling in knowledge and trying to articulate that knowledge... There is a path to get that common sense by essentially leveraging the knowledge that is contained in multimodal LLMs." [00:13:07] — Sergey Levine

---

## 2. Contrarian Perspectives

### The "Bitter Lesson" Is Still Not Universally Accepted — and That's the Core Debate
Most people assume the AI research community has aligned around end-to-end learning from data. Levine reveals it remains genuinely controversial — and he believes it is still the right path, precisely because programmed knowledge creates a ceiling on generalization.

> "I don't think there's still universal acceptance that end-to-end learning is the right way to go... The bitter lesson says that you should not program the machine to think the way you think it should think but you should let it learn from data and that is not a universally accepted idea." [00:41:56] — Sergey Levine

### Humanoid Robots Are Not the Inevitable Form Factor — and Betting on Them May Be a Distraction
While humanoids dominate investor and media attention, Levine argues the real prize is a foundation model that makes *any* physical form factor intelligent. The humanoid framing may actually limit our imagination.

> "I don't think we should be tackling intelligence in the context of one specific body... You could imagine that you're building a house with a robot that is a swarm of 1,000 quadcopters... The fundamentals of how you interact with objects, how things move in the world, how causality works — that's all conserved for all of these different systems." [00:09:37] — Sergey Levine

### The Hardest Robotic Tasks Will Be the Ones That Seem Easiest to Humans
Moravec's Paradox is still widely underappreciated. The tasks that will take longest to automate aren't complex manufacturing — they're intimate human-interaction tasks like elderly care and childcare. People systematically misprice these timelines.

> "I think changing a child's diaper will be really, really hard... Things that involve behaviors that interact with other people, where you have to help somebody — I think that's a lot harder than people appreciate. Elderly care, taking care of small children — I think those things are going to be hard and they're probably going to be harder than people think." [00:44:07] — Sergey Levine

### Robots Can Already Surpass Human Dexterity in Certain Tasks Right Now
Against the conventional narrative that robots are still clumsy compared to humans, Levine points out that robots can already perform certain physical tasks faster and more efficiently than people — by removing the cognitive processing pauses humans inherently require.

> "It turns out to be like pretty straightforward to go in and find all those pauses and remove them. You can speed things up further. So you can get to a task where a person demonstrates what it means to succeed and then you can have the robot practice the task and succeed in the same way but a lot more quickly, a lot more efficiently." [00:36:22] — Sergey Levine

### Simulation-Heavy vs. Real-Data-Heavy Approaches Are Diverging in Robotics — and No One Knows Which Wins
The field is split: humanoid locomotion succeeds with near-zero real-world data via simulation, while manipulation succeeds with almost no simulation and enormous real-world data. This divergence is unresolved and underappreciated by observers assuming one paradigm dominates.

> "It is surprising that in these two robotic domains the dominant approaches look so different. It may be that one will win out and there's a particular approach that can handle everything in the long run, or maybe there's some sort of synthesis of these ideas that's important. I don't know the answer." [00:31:59] — Sergey Levine

---

## 3. Companies Identified

**Physical Intelligence (PI)**
- Description: AI research company building foundation models for robotic control — a "brain" that can operate any physical robot for any task
- Why Mentioned: Core subject of the podcast; demonstrated ability to onboard novel robotic tasks (Robot Olympics challenges) with no task-specific development, using a general model and standard data pipeline
- > "We didn't like develop anything special for this. We literally used this as a test of our task onboarding process... It suggests the power of generality — that when you have this general system you can just onboard all these crazy tasks without really doing anything particularly sophisticated." [00:35:03] — Sergey Levine

**Tesla**
- Description: EV and autonomous driving company
- Why Mentioned: Used as the exemplar of a real-world data flywheel — a deployed product that generates its own training data at scale, the model Physical Intelligence wants to emulate for robotics
- > "Tesla doesn't worry about how much data their cars can collect. If anything, it's the other way around. That's a little too much data." [00:21:02] — Sergey Levine

**Boston Dynamics**
- Description: Pioneer robotics company, now owned by Hyundai, known for highly capable agile robots
- Why Mentioned: Levine cited the new Atlas as a personal favorite robot, while also honestly noting the longstanding gap between impressive demos and customer utility — a question he acknowledges applies to much of the robotics industry
- > "I do really like the Boston Dynamics robot, especially the new version of the Atlas." [00:53:59] — Sergey Levine

**OpenAI**
- Description: AI research and deployment company
- Why Mentioned: Praised for organizational culture that empowers individual researchers — ChatGPT cited as an example of a "pet project" becoming a world-changing product, held up as a cultural model for Physical Intelligence
- > "OpenAI has historically done a great job of this — of creating an atmosphere where individual researchers can experiment with things and be empowered to see those things through. ChatGPT was basically John Schulman's pet experiment for a while. It wasn't a concerted corporate strategy with lots of spreadsheets and pie charts." [00:103:07] — Sergey Levine

---

## 4. People Identified

**Benji Holson**
- Description: Former roboticist at Everyday Robots (Alphabet); thinker on practical robotics benchmarks
- Why Mentioned: Author of an influential blog post proposing a "Robot Olympics" focused on everyday human tasks that robots struggle with — used by Physical Intelligence as an actual stress test of their task onboarding pipeline
- > "There is a gentleman named Benji Holson who used to work at Everyday Robots, part of Alphabet before it dissolved. He spends a lot of time thinking about tasks that robots could do... He had things like opening a door, washing a frying pan with grease on it, using a plastic bag to pick up dog poop — things that people don't find particularly challenging but that no current robotic system can do." [00:34:04] — Sergey Levine

**John Schulman**
- Description: Co-founder of OpenAI, key researcher behind reinforcement learning from human feedback and ChatGPT
- Why Mentioned: Cited as the canonical example of an individual researcher whose "pet experiment" became transformative — used to make a broader point about research cultures that empower individual curiosity
- > "ChatGPT was basically John Schulman's pet experiment for a while. It wasn't a concerted corporate strategy with lots of spreadsheets and pie charts. It was a pet project." [00:103:07] — Sergey Levine

**Peter Abbeel**
- Description: Professor at UC Berkeley, pioneer of robot learning and imitation learning
- Why Mentioned: Levine's postdoc mentor who gave him his first entry into robotics — described as someone who "bet on potential over accomplishments," a value Levine now pays forward
- > "When I started my postdoc with Peter Abbeel at Berkeley, I had zero robotics experience... I felt like that was a bet on my potential more so than my actual accomplishments." [00:105:21] — Sergey Levine

**Jeff Dean**
- Description: Former Google SVP of Research and AI, co-creator of TensorFlow, legendary infrastructure leader
- Why Mentioned: Provided the organizational leverage for Levine's "arm farm" experiment at Google — emblematic of how great research institutions empower individual researchers with extraordinary resources
- > "I found out from somebody that they had a warehouse full of robots. Jeff Dean was like, 'Yeah, let's do it. What do you need?' I just remember feeling like wow — I had never in my life thought that I'd have that leverage." [00:104:20] — Sergey Levine

---

## 5. Operating Insights

### Mid-Level Semantic Coaching Can Substitute for Expensive Teleoperation Data
When a robot fails at a task, the instinct is to collect more expensive human-demonstration data. Physical Intelligence discovered that simply labeling the robot's own experience with high-level semantic commands can improve generalization — a dramatically cheaper and more scalable feedback loop.

> "What we tried kind of on a whim is to see, okay, what if we don't add more teleoperation data? What if we just add more data labeled with the semantic command? So basically, just take whatever the robot experienced and just label it with some semantic commands, but don't add any more low-level actions. And that actually helps." [00:26:30] — Sergey Levine

### The "Task Onboarding Process" as an Internal Operational Benchmark
Rather than building special systems for high-profile demos, Physical Intelligence uses public challenge lists (like Holson's Robot Olympics) as live tests of their internal task ingestion pipeline. This creates a forcing function for operational rigor and exposes fragility in the system before it becomes a product problem.

> "We figured, okay, a good way to test this is to say here's a big list of tasks, let's just go through this process that we've developed and see if it works. It's almost like a test of our internal operations and model training system." [00:34:33] — Sergey Levine

### The Most Important Research Management Decision Is Knowing When to Pivot vs. Persist
Levine identifies the hardest call in running a research organization: when to keep pushing on a problem versus when to turn and explore new directions. Leaders who get this instinct right compound disproportionately.

> "If you get it wrong and don't stick with something for long enough, you might be about to get to the answer and you stop short of it — that's terrible. Or you could get stuck hammering against something that's never going to give way for years. Deciding when to turn a little bit and look this way versus when should you keep hammering — that's often the most important decision. And some people have an instinct for getting that right." [00:49:28] — Sergey Levine

---

## 6. Overlooked Insights

### Physical Analogies in Human Cognition May Be the Deepest Moat That Embodied AI Can Build
Levine briefly raised and then moved past what is potentially a profound insight: that humans use physical metaphors not just for everyday communication but to make breakthrough scientific inferences — from "momentum" in business to "spin" in quantum mechanics. If a robotic foundation model truly internalizes physical causality at a deep level, it may develop a form of reasoning that LLMs — trained only on text — structurally cannot replicate. This is not just a robotics advantage; it could be the basis for a fundamentally superior reasoning architecture.

> "You can say that company has a lot of momentum — that's a physical analogy... You can use it in everyday speech and you can use it when advancing fundamental theoretical physics. That's kind of remarkable. I don't know if LLMs can do that. Maybe they can. But I think that really understanding physical interactions, causal structures — there is something special about that." [00:45:25] — Sergey Levine

### The 90/10 Split Between Teleoperation and Autonomous Data Collection Is a Hidden Fork in the Entire Industry's Business Model
Levine casually mentioned that the ratio of human-demonstrated data to autonomous robot-collected data is deeply uncertain — and that this ratio will completely reshape how companies need to prepare, what hardware infrastructure matters, and what the labor/cost model of robotic deployment looks like. This is not just a technical question; it determines which business models are viable and which investments become stranded assets.

> "Here is a particular uncertainty about the tech: will the robots rely more on demonstrations or on reinforcement learning from autonomous data?... How somebody should prepare for the technology will be pretty different if they're expecting that they need lots of teleoperation... versus a tiny number of demonstrations and huge amounts of autonomous experience. Is it a 90-10 or 10-90? That's something we're hopefully going to learn about over the next few years, but it does change the correct approach pretty dramatically." [00:51:50] — Sergey Levine