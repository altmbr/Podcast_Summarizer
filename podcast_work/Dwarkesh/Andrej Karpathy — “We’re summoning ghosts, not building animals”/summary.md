# [Andrej Karpathy — “We’re summoning ghosts, not building animals”](https://www.youtube.com/watch?v=lXUZvyajciY)

**Podcast:** Dwarkesh
**Date:** 2025-10-17
**Region:** Western
**Video ID:** lXUZvyajciY
**Video URL:** https://www.youtube.com/watch?v=lXUZvyajciY
**Transcript:** [View Transcript](./transcript.md)

---

# [Summary: Andrej Karpathy Podcast](https://www.youtube.com/watch?v=lXUZvyajciY)

## 1. Key Themes

### The Decade (Not Year) of Agents - Why Progress Will Be Gradual

Karpathy pushes back against claims of an imminent "year of agents," arguing we're in for a decade-long journey. The fundamental issue is that current AI agents simply don't work well enough to replace human employees.

**Quote:** "When would you prefer to have an agent like cloud or codecs do that work? Currently, of course, they can't. What would it take for them to be able to do that? Why don't you do it today? The reason you don't do it today is because they just don't work. They don't have enough intelligence. They're not multimodal enough... They're just cognitively lacking and it's just not working."

This reflects a pragmatic engineer's perspective: multiple missing pieces (continual learning, true multimodality, better reasoning) need to be solved, and each represents substantial research challenges that won't be overcome in months.

### We're Building "Ghosts," Not Animals - The Fundamental Difference in AI Development

Karpathy introduces a provocative framework: evolution created animals through a completely different optimization process than we use for AI, making biological analogies misleading.

**Quote:** "We're not actually building animals. We're building ghosts, or spirits, or whatever people want to call it. Because we're not doing training by evolution, we're doing training by basically imitation of humans, and the data that they've put on the internet. And so you end up with these, like, sort of ethereal spirit entities because they're fully digital, and they're kind of like mimicking humans, and it's a different kind of intelligence."

He argues that evolution encodes tremendous hardware (neural circuitry) in DNA that allows zebras to run minutes after birth—this isn't reinforcement learning, it's baked-in functionality. Current AI follows a fundamentally different path: mimicking human internet output rather than evolving embodied intelligence.

### The Problem with Current Reinforcement Learning - "Sucking Supervision Through a Straw"

Karpathy offers a scathing critique of current RL approaches, coining the memorable phrase about how inefficient the learning signal is.

**Quote:** "You're sucking supervision through straw because you've done all this work that could be a minute to roll out. And you're like sucking the bits of supervision of the final reward through straw... you're broadcasting that across the entire trajectory and using that to up weight or down with that trajectory. It's too crazy. A human would never do this."

The core problem: when you try 100 different solution paths and only learn from the final binary outcome, you're noisily attributing success/failure to every single token along the way, even though many steps in successful attempts were actually wrong turns. Humans do something far more sophisticated—they review their work, identify what specifically worked or didn't, and extract nuanced lessons. Current AI systems lack any equivalent process.

### Memory vs. Intelligence - The Overfitting Problem in LLMs

A non-obvious insight: current models are *too good* at memorization, and this actually holds back their intelligence.

**Quote:** "I actually think that humans actually, they do kind of like have a lot more of an element compared to all of them of seeing the forest for the trees, and we're not actually that good at memorization, which is actually a feature. Because we're not that good at memorization, we actually are kind of like forced to find patterns, like in a more general sense."

Karpathy advocates for a "cognitive core" stripped of factual memory—a model that maintains only the algorithms for thought, problem-solving strategies, and meta-learning capabilities, while looking up facts externally. Current trillion-parameter models waste capacity memorizing training documents when they should be learning generalizable reasoning patterns.

## 2. Contrarian Perspectives

### Most "AI Progress" Hype is Just Fundraising Theater

Karpathy directly challenges the industry narrative around coding agents and imminent automation.

**Quote:** "I kind of feel like the industry, it's over, it's making too big of a jump, and it's trying to pretend like this is amazing, and it's not. It's slop. And I think they're not coming at it from a perspective of like let's build animals. I come from a perspective of like let's build useful things. So I have a hard hat on and I'm just observing that like we're not going to do evolution because I don't know how to do that."

He notes that when building NanoChat (a complete chatbot implementation), coding agents provided minimal help because they're trained on typical patterns and fail on novel, architecturally unique code. They kept trying to insert standard boilerplate (like DDP containers) he deliberately avoided, showing they can't adapt to genuinely new approaches.

### Humans Don't Actually Use Reinforcement Learning for Intelligence

Counter to common wisdom in AI research, Karpathy argues humans primarily don't learn cognitively through RL.

**Quote:** "A lot of the reinforcement learning in my perspective would be things that are a lot more like motor-like, like simple kind of like task throwing hoop or stuff like that. But I don't think that humans use reinforcement learning for a lot of intelligence tasks, like problem solving and so on."

This challenges the Sutton-style view that a single learning algorithm will unlock AGI. Karpathy suggests human intelligence development is actually more about maturation of pre-encoded circuitry plus sophisticated review/reflection processes, not trial-and-error with reward signals.

### Small Models (Billion Parameters) Can Match Current Frontier Intelligence

Going against scaling maximalism, Karpathy predicts the "cognitive core" could be dramatically smaller than current models.

**Quote:** "I almost feel like we can get cognitive cores that are very good at even like a billion, billion parameters. It should be already like, like if you talk to a billion parameter model, I think in 20 years, you can actually have a very productive conversation, it thinks, and it's a lot more like a human."

His reasoning: current trillion-parameter models mostly store memorized facts from terrible internet data. Strip away the memory, keep only the reasoning algorithms, train on curated cognitive processes, and distill—you need far less. He observes we've already gone from trillion-parameter to 20B models with better performance in two years.

### The Internet as Training Data is "Total Garbage"

Challenging assumptions about pre-training data quality:

**Quote:** "When you're actually looking at a preaching data set in the Frontier Lab and you look at a random internet document, it's total garbage. Like, I don't even know how this works at all. It's some like stock ticker symbols. It's a huge amount of slop and garbage from like all the corners of the internet. It's not like your Wall Street Journal article. That's extremely rare."

Most people envision training data as high-quality articles. Reality: most tokens are noise, forcing models to be enormous just to compress the mess. Better data curation could enable much smaller, more capable models.

### Model Collapse is Fundamental and Humans Experience It Too

On synthetic data and model-generated training:

**Quote:** "I actually think that there's no fundamental solutions to this possibly. I also think humans collapse over time... children have completely, they haven't overfitted and they will say stuff that will shock you... But we're collapsed. We end up revisiting the same thoughts. We end up saying more and more of the same stuff and the learning rates go down and the collapse continues to get worse."

This biological analogy for model collapse suggests it may not be fully solvable—it's a fundamental feature of learning systems, not just an engineering bug.

## 3. Companies Identified

### OpenAI (Context: Early Agent Research)

**Description:** Frontier AI lab where Karpathy worked on early agent development

**Quote:** "My project at OpenAI, for example, was within the scope of the universe project on an agent that was using keyboard and mouse to operate web pages. And I really wanted to have something that, like, interacts with, you know, the actual digital world that can do knowledge work... This was extremely early, way too early."

The insight: OpenAI (and the field) tried to build full agents too early, before having the pre-trained representations (LLMs) necessary to ground them. The "Universe" project failed because pure RL from pixels was too sample-inefficient.

### Anthropic - Claude and Computer Use

**Description:** AI safety company building frontier models with agentic capabilities

**Quote:** "We have some very early agents that are actually extremely impressive and that I use daily, cloud and codecs and so on, but I still feel like there's so much work to be done."

Karpathy singles out Claude as something he actually uses, suggesting it represents the current state-of-art in practical a