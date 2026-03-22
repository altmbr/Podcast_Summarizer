# [Andrej Karpathy on Code Agents, AutoResearch, and the Loopy Era of AI](https://traffic.megaphone.fm/PDP8703207384.mp3)

**Podcast:** No Priors
**Date:** 2026-03-20
**Processed:** 2026-03-22T16:02:06Z
**Participants:** Andrej Karpathy, Sarah Guo
**Episode URL:** https://traffic.megaphone.fm/PDP8703207384.mp3
**YouTube:** [Watch on YouTube](https://youtube.com/watch?v=kwSVtQ7dziU)
**Transcript:** [View Transcript](./transcript.md)

---

# Andrej Karpathy on Code Agents, AutoResearch, and the Loopy Era of AI

---

## 1. Key Themes

### The Agentic Workflow Inflection Point: December 2024 Was the Threshold

Something fundamentally shifted in how elite engineers work in December 2024. Karpathy describes going from writing code himself 80% of the time to essentially never typing a line of code again — a complete inversion of his workflow in a matter of weeks. This isn't incremental improvement; it's a phase transition.

> "I kind of went from 80-20 of like, you know, to like 20-80 of writing code by myself versus just delegating to agents. And I don't even think it's 20-80 by now. I think it's a lot more than that. I don't think I've typed like a line of code, probably since December, basically." — Andrej Karpathy [00:01:27](https://youtube.com/watch?v=kwSVtQ7dziU&t=87)

The new skill is "macro actions" — not writing individual functions but orchestrating multiple parallel agents across multiple repos simultaneously, much like a conductor.

> "You can move in much larger macro actions. It's not just like here's a line of code. Here's a new function. It's like here's a new functionality and delegate it to agent one. Here's a new functionality that's not going to interfere with the other one. Give it agent two." — Andrej Karpathy [00:04:01](https://youtube.com/watch?v=kwSVtQ7dziU&t=241)

---

### Auto-Research as Recursive Self-Improvement: The Most Important Project in AI

Karpathy's auto-research experiment — removing himself entirely from the optimization loop and letting agents run experiments on NanoGPT — found improvements he missed after two decades of experience. He views this as a microcosm of what frontier labs are racing to build at scale.

> "It came back with tunings that I didn't see. And, yeah, I did forget, like, the weight decay on the value embeddings. And my atom betas were not sufficiently tuned... I shouldn't be a bottleneck. I shouldn't be running these hyperprimers or shop optimizations." — Andrej Karpathy [00:18:58](https://youtube.com/watch?v=kwSVtQ7dziU&t=1138)

The deeper insight is that every research organization can be described as a set of Markdown files, and those files themselves can be optimized — creating a meta-layer of recursive improvement.

> "So, basically, every research organization is described by program MD. A research organization is a set of Markdown files that describe all the roles and how the whole thing connects... once you have code, then you can imagine tuning the code." — Andrej Karpathy [00:21:38](https://youtube.com/watch?v=kwSVtQ7dziU&t=1298)

---

### Digital Before Physical: The Investment Sequencing Framework

Karpathy offers a clear, sequenced framework for where AI impact flows: first digital (bits are infinitely cheap to copy and manipulate), then the interface layer between digital and physical (sensors and actuators), and only then the full physical/robotics world. This has direct implications for where to invest now versus later.

> "I kind of feel like digital space is going to like change a huge amount and then the physical space will lag behind... right now is digital is like my main interest. Then interfaces would be like after that. And then maybe like some of the physical things, their time will come and they'll be huge when they do." — Andrej Karpathy [00:57:40](https://youtube.com/watch?v=kwSVtQ7dziU&t=3460)

Robotics specifically will lag because atoms are hard — but the market opportunity when it arrives may be even larger than digital.

> "The physical world, I almost feel like the total addressable market in terms of the amount of work is massive, possibly even much larger, maybe what can happen in digital space. So I actually think it's like a much bigger opportunity as well, but I do feel like it's a huge amount of work and the atoms are just like a million times harder." — Andrej Karpathy [00:57:10](https://youtube.com/watch?v=kwSVtQ7dziU&t=3430)

---

## 2. Contrarian Perspectives

### The "Smarter Code = Smarter Everything" Thesis Is Wrong

The prevailing narrative from major research groups is that gains in verifiable domains like code automatically generalize to broader intelligence. Karpathy directly disputes this, using a simple and devastating example: frontier models still tell the same bad joke they told four years ago.

> "If you give them an agentic task, they will just go for hours and move mountains for you. And then you ask for, like, a joke, and it has a stupid joke, a crappy joke from five years ago... shouldn't you expect models as they get better to also have, like, better jokes or more diversity of them? Or it's just, it's not being optimized, and it's stuck." — Andrej Karpathy [00:26:55](https://youtube.com/watch?v=kwSVtQ7dziU&t=1615)

This "jaggedness" suggests the intelligence is narrow and rail-dependent, not genuinely general — a major caveat for anyone betting on AGI timelines based solely on coding benchmark progress.

---

### Apps Shouldn't Exist — APIs and Agents Should Replace the Entire App Layer

Most of the software industry is building apps for human UX. Karpathy's view is that this entire category of software is architecturally obsolete. The right model is exposed APIs consumed directly by agents, not bespoke apps for humans.

> "In a certain sense, it does point to this, like, maybe there's, like, an overproduction of lots of custom-bespoke apps that shouldn't exist because agents kind of, like, crumble them up. And everything should be a lot more just, like, exposed API endpoints. And agents are the glue of the intelligence that actually, like, tool calls all the parts." — Andrej Karpathy [00:13:35](https://youtube.com/watch?v=kwSVtQ7dziU&t=815)

This is a direct threat to large swaths of the SaaS industry and implies the customer for software is no longer the human.

> "The industry just has to reconfigure in so many ways that it's, like, the customer is not the human anymore. It's, like, agents who are acting on behalf of humans." — Andrej Karpathy [00:14:04](https://youtube.com/watch?v=kwSVtQ7dziU&t=844)

---

### Staying Outside Frontier Labs May Actually Compromise Your Judgment on AI Safety

The conventional wisdom is that independence from big labs preserves intellectual freedom and safety credibility. Karpathy flips this: staying outside the frontier labs causes your judgment about AI development to *drift*, making you less equipped to have meaningful influence on the most consequential decisions.

> "If you're outside of that frontier lab, your judgment fundamentally will start to drift because you're not part of the, you know, what's coming down the line... I won't actually have an understanding of how these systems actually work under the hood. That's an opaque system." — Andrej Karpathy [00:47:14](https://youtube.com/watch?v=kwSVtQ7dziU&t=2834)

His proposed solution — cycling in and out of frontier labs — is itself contrarian versus the typical career path of staying permanently inside or outside.

---

### Flops, Not Dollars, May Become the True Reserve Currency

As compute becomes the binding constraint and money alone can't acquire it, Karpathy floats a provocative inversion of economic value.

> "It's almost like dollars, the thing everyone cares about, but is flop the thing that actually everyone cares about in the future? Like, is there going to be like a flippening almost of like what's the thing that you care about? Like right now, for example, it's really hard to get compute, even if you have money. So actually, it almost seems like the flop is like dominant in a certain sense." — Andrej Karpathy [00:37:25](https://youtube.com/watch?v=kwSVtQ7dziU&t=2245)

---

### Centralization of AI Is the Real Systemic Risk — And It's Getting Worse

While the public debate focuses on AI safety in terms of model behavior, Karpathy identifies *structural centralization* among frontier labs as a more fundamental risk, with explicitly few people controlling decisions of civilizational importance.

> "I almost feel like it's been like even further centralizing recently because I think a lot of the frontrunners are like not necessarily like the top tier... I want there to be ensembles of people in a room when they, to be all well-informed and to make all those decisions... I don't want it to be like a closed doors with two people or three people. I feel like that's like not a good, not a good future." — Andrej Karpathy [00:53:54](https://youtube.com/watch?v=kwSVtQ7dziU&t=3234)

---

## 3. Companies Identified

**Periodic**
A materials science company doing "auto-research" — applying autonomous agent loops to scientific experimentation with physical lab equipment as sensors.
Why mentioned: Cited as a real-world example of the digital-to-physical interface thesis, where expensive lab equipment serves as sensors feeding an AI research loop.
> "A friend of mine, Liam is running, is a CEO of Periodic. I visited them last week... they're trying to do auto research for material science. And so in that case, it's like the sensors to the intelligence are actually like pretty expensive lab equipment." — Andrej Karpathy [00:58:39](https://youtube.com/watch?v=kwSVtQ7dziU&t=3519)

---

**Anthropic (Claude)**
Frontier AI lab, maker of Claude.
Why mentioned: Karpathy singles out Claude specifically for having a better-calibrated personality and sycophancy dial than competitors — a non-obvious product differentiator that actually affects user behavior and trust.
> "I think they dialed the sycophantasy fairly well, where when Claude gives me praise, I do feel like I slightly deserve it... I kind of feel like I'm trying to like earn its praise, which is really weird. And so I do think the personality matters a lot." — Andrej Karpathy [00:08:34](https://youtube.com/watch?v=kwSVtQ7dziU&t=514)

---

**OpenClaw / Open-Claw (Peter Steinberg's project)**
An agentic harness / claw-type system built by Peter Steinberg, featuring sophisticated memory, a crafted AI persona (SoulMD document), WhatsApp integration, and persistent looping.
Why mentioned: Identified as innovating simultaneously across five dimensions — memory systems, personality design, loop persistence, tool integration, and single-portal UX — setting the standard for what agentic products should look like.
> "Peter has done a really amazing job... I think he innovated simultaneously in like five different ways and put it all together... the SoulMD document, like he actually really crafted a personality that is kind of compelling and interesting." — Andrej Karpathy [00:07:50](https://youtube.com/watch?v=kwSVtQ7dziU&t=470)

---

## 4. People Identified

**Peter Steinberg**
Builder of OpenClaw, an advanced agentic harness system.
Why mentioned: Karpathy uses him as the archetype of mastery in the new agentic paradigm — running multiple parallel Codex agents tiling a monitor, each taking 20-minute tasks across separate repos. Also credited with five simultaneous innovations in agent design.
> "Peter is famous. He has a funny photo where he's in front of a monitor with lots of... codex agents tiling the monitor. And they all take about 20 minutes if you prompt them correctly... he's just going between them and giving them work." — Andrej Karpathy [00:04:01](https://youtube.com/watch?v=kwSVtQ7dziU&t=241)

---

**Liam (CEO of Periodic)**
CEO of Periodic, a materials science auto-research company.
Why mentioned: Running one of the most advanced real-world implementations of the physical-digital interface thesis — using autonomous agent loops with expensive lab equipment to do materials science research.
> "A friend of mine, Liam is running, is a CEO of Periodic. I visited them last week... they're trying to do auto research for material science." — Andrej Karpathy [00:58:39](https://youtube.com/watch?v=kwSVtQ7dziU&t=3519)

---

## 5. Operating Insights

### Token Throughput as a KPI: Maximize Subscription Utilization Like GPU Utilization

Karpathy reframes the productivity metric for the agentic era: just as he felt anxious as a PhD student when GPUs sat idle, he now feels anxious when subscription token quota goes unused. For operators and teams, this implies a new metric — token throughput per person per day — and that idle time waiting for agents is itself an opportunity to spawn more parallel tasks.

> "I feel nervous when I have subscription left over. That just means I haven't maximized my token throughput... it's not my thought. It's about tokens. So what is your token throughput and what token throughput do you command?" — Andrej Karpathy [00:05:30](https://youtube.com/watch?v=kwSVtQ7dziU&t=330)

---

### Personality Design in AI Products Is Underrated and Competitively Differentiated

Most teams are focused on capability benchmarks. Karpathy's observation is that personality calibration — specifically how an AI agent expresses enthusiasm, gives praise, and engages with the work — is a major driver of user engagement and is currently poorly executed by most tools. This is an underexploited product lever.

> "I think a lot of the current agents, they don't get this correctly... Codex is very dry. It doesn't seem to care about what you're creating... The personality matters a lot. And I think a lot of the other tools maybe don't appreciate it as much." — Andrej Karpathy [00:08:16](https://youtube.com/watch?v=kwSVtQ7dziU&t=496)

---

### Auto-Research Requires Objective Metrics First — Identify What Is Verifiable Before Automating

For operators trying to implement autonomous agent loops in their own workflows, the critical filter is whether the task has an objective, easy-to-evaluate metric. Without it, the loop cannot close. Karpathy offers CUDA kernel optimization as a perfect example (correct behavior + speed = verifiable), versus anything "soft" which degrades rapidly.

> "This is extremely well suited to anything that has objective metrics that are easy to evaluate... if you can't evaluate it, then you can't auto-research it, right? So that's, like, caveat number one." — Andrej Karpathy [00:24:07](https://youtube.com/watch?v=kwSVtQ7dziU&t=1447)

---

### Documentation Should Be Written for Agents, Not Humans

For anyone shipping libraries, tools, or internal systems: the immediate operational change is to replace HTML/human docs with Markdown docs structured for agent comprehension. If the agent understands it, the agent can explain it to any human at their level — making human-written tutorials obsolete.

> "If I have a library, for example, of code or something like that, it used to be that you have documentation for other people... but like you shouldn't do that anymore. Like you should have, instead of HTML documents for humans, you have markdown documents for agents because if agents get it, then they can just explain all the different parts of it." — Andrej Karpathy [00:04:33](https://youtube.com/watch?v=kwSVtQ7dziU&t=273)

---

## 6. Overlooked Insights

### The Blockchain-Like Architecture for Decentralized AI Research Is a Real, Investable Structure

Karpathy briefly describes a system architecture for untrusted, distributed AI improvement that structurally resembles a blockchain — but almost no one in the conversation picks up on the full implication. The key insight: AI model improvement has the exact same "hard to generate, cheap to verify" property as proof-of-work, making it structurally amenable to decentralized compute contribution at internet scale. This could enable a "Folding@Home for LLMs" that potentially outcompetes frontier labs through sheer distributed scale.

> "It almost actually, like, looks a little bit like a blockchain, a little bit, because instead of blocks, you have commits. And these commits can build on each other and they contain, like, changes to the code as you're improving it. And the proof of work is basically doing tons of experimentation to find the commits that work... a swarm of agents on the internet could collaborate to improve LLMs and could potentially even like run circles around Frontier Labs." — Andrej Karpathy [00:34:11](https://youtube.com/watch?v=kwSVtQ7dziU&t=2051)

This is a nascent but structurally sound idea for a decentralized AI research network — one that no major project has yet fully built, and which represents a potential category-defining company.

---

### Information Markets for Physical World Data Will Be the Next Commodity Exchange

In a single paragraph that flew by without follow-up, Karpathy describes a world where agents are the *buyers* of real-world sensor data — paying humans to capture photos or videos from specific locations in service of prediction markets and autonomous decision-making. This is essentially a new kind of commodity exchange, with information as the commodity and agents as the primary market participants.

> "If Iran was just happening now, like how come there isn't a process where like taking a photo or video from somewhere in Tehran should cost, like 10 bucks, like someone should be able to pay for that... There's not going to be a human looking at it. It's going to be like agents who are trying to guess the betting games and stock markets." — Andrej Karpathy [00:59:02](https://youtube.com/watch?v=kwSVtQ7dziU&t=3542)

No company has yet built a programmatic, agent-native marketplace for real-world sensor data with micropayment rails. This is the missing infrastructure layer between the digital intelligence explosion and the physical world — and it's an earlier-stage opportunity than robotics with a potentially faster path to value.