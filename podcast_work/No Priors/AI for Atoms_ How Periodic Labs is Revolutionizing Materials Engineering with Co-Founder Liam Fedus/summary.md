# [AI for Atoms: How Periodic Labs is Revolutionizing Materials Engineering with Co-Founder Liam Fedus](https://traffic.megaphone.fm/PDP2440813202.mp3)

**Podcast:** No Priors
**Date:** 2026-04-03
**Processed:** 2026-04-04T17:06:42Z
**Participants:** Elad Gil, Interjector, Liam Fedus, No Priors Announcer
**Episode URL:** https://traffic.megaphone.fm/PDP2440813202.mp3
**Transcript:** [View Transcript](./transcript.md)

---

# Periodic Labs & AI for the Physical World — No Priors Summary

---

## 1. Key Themes

### AI Is Finally Ready to Connect to the Physical World

Fedus argues that the missing link in AI's impact on science isn't intelligence — it's the closed-loop connection to physical reality. Language models alone, even powerful ones, were insufficient to drive real scientific acceleration.

> "The opinion that I and others held at Periodic was you're not going to see the same kind of acceleration in science and technology unless you start connecting these things to the physical world. Science ultimately isn't sitting in a room thinking really hard. You have to conduct experiments. You have to learn from them. You have to interface with reality." [00:05:26]

> "The creation of ChatGPT in late 2022 was an important technology, but it was still far too weak. We couldn't have done Periodic on technology of that era." [00:05:52]

### Scaling Laws Will Come to Physical Sciences — And That's the Real Unlock

Fedus draws a direct analogy between the early days of Google Brain (a few GPUs, small teams) and where physical sciences are today. The industrialization of ML via scaling laws is the template for what's coming to materials science.

> "The physical sciences, physical engineering will have a very similar property where we establish these scaling properties and bring that mindset. And so Periodic in this field is really thinking about how do we bring much larger scale sets of experiments to bear on this?" [00:18:57]

> "Scientists very much feel this where they're not used to working at that level of throughput and they just can't simply make sense of so much data." [00:19:25]

### Closed-Loop Experimental Systems Are the Core Infrastructure Advantage

Raw data pools are not enough. The real moat is a continuously active, self-correcting loop between AI models, simulation, and physical experiments — where each experiment informs the next.

> "It's not just like a pool of data. It's this interactive closed loop system that is so powerful. Once you have the experimental data, you can look through it, you can look for aberrations, you can look for patterns, you can look for consistency with simulation data, with literature, and then that helps drive the next set of experiments." [00:09:34]

---

## 2. Contrarian Perspectives

### Intelligence Is Not a Scalar — "Spikiness" Makes AGI Timelines Misleading

Most public discourse treats AGI as a single threshold to cross. Fedus argues intelligence in these systems is fundamentally uneven and domain-specific in non-intuitive ways, making blanket AGI predictions misleading.

> "One fallacy is thinking about intelligence as a scalar. We've consistently seen these systems have a very odd spikiness. It's actually possible to architect a system that is world class on some math domain, but then you could do some perturbations to the questions and actually degrade it substantially. So it's like a bad high school student." [00:22:10]

### Compute Costs Now Dwarf Physical Lab Infrastructure Costs

Most people assume building a physical-world AI company (labs, equipment, robotics) is the dominant capital expense. Fedus flips this: GPUs cost more than physical lab infrastructure, which changes how you think about the capital structure of science-AI companies.

> "GPUs are so extraordinarily expensive. What's interesting is just the compute costs relative to physical infrastructure is actually surprising where so much money is spent on the compute that the physical infrastructure sometimes is actually lower." [00:19:57]

### Self-Improving AI in Software Engineering Is Happening Now — But Domain Transfer Is Not Automatic

The common narrative is that AGI will generalize across domains once software engineering is cracked. Fedus pushes back: domain-specific closed loops are necessary, and winning in code does not transfer to biology or materials.

> "Rolling forward that software engineering self-improvement, I think you're going to have a system that can write complete repositories, identify bugs, refactor code, but it doesn't suddenly understand biology. There's a domain gap there in knowledge." [00:23:42]

### Literature-Reported Material Properties Are Unreliable as Training Data

A non-obvious point: scientific literature, the assumed gold standard for training science AI, is actually deeply noisy and spans orders of magnitude for the same property — making experimental ground truth data far more valuable than scraping papers.

> "One of the engineers on our team was looking at a reported material property and it was just sort of extracted values from literature. And it was really interesting to see the reported value spanned many orders of magnitude. And so you train an ML system on that and it's like, well, the best you can do is model distribution, but you're no closer to a ground truth." [00:09:08]

---

## 3. Companies Identified

### Periodic Labs
AI foundation lab for atoms; applies AI and closed-loop experimentation to materials science, chemistry, and physical engineering. Founded by Liam Fedus (co-creator of ChatGPT, former VP of Post-Training at OpenAI). The company treats itself as "customer zero," building tools for scientists before expanding to advanced manufacturing.
> "We've begun working very closely with scientists. We've treated Periodic as our customer zero and seeing how can we transform how this field of science is done." [00:13:28]

### Codex / Claude Code (Anthropic)
AI coding tools. Highlighted as so capable that Periodic offloads all coding infrastructure work to them rather than building internally — a significant operating insight about AI-native companies.
> "Periodic spend zero effort on improving coding models. We're incredibly impressed by Codex, Claude Code. And so that's been a huge accelerator for the company." [00:07:59]

---

## 4. People Identified

### John Schulman
Co-founder of OpenAI. Mentioned for his decisive product instinct that shaped ChatGPT's direction away from narrow bots toward a general-purpose interface.
> "John Schulman was very opinionated. He's like, we think we should keep it very general. Let's do a chatbot. And that became a large part of the effort for those few months." [00:04:42]

### Liam Fedus
Co-creator of ChatGPT, former VP of Post-Training at OpenAI, former Google Brain researcher (worked on mixture of experts, trillion-parameter models), now co-founder of Periodic Labs. Physics undergraduate, dark matter researcher — exemplifies the physicist-to-AI pipeline.
> "Even further back, I was a physics major in undergrad, spent some time doing dark matter research. We had an apparatus that was directionally sensitive to dark matter's direction." [00:01:04]

---

## 5. Operating Insights

### Use Frontier AI Tools to Completely Eliminate Entire Internal Functions

Rather than building capabilities in-house across the board, Periodic made a deliberate choice to outsource coding entirely to existing frontier tools and focus ML investment only where those tools fall short. This is a powerful operating principle for any AI-native company: identify where the frontier is already good enough, and redirect all internal resources to genuinely differentiated problems.

> "Periodic spend zero effort on improving coding models. We're incredibly impressed by Codex, Claude Code. And so that's been a huge accelerator for the company. But we focus our machine learning efforts where the existing frontier is not sufficiently good for us." [00:07:59]

### Architect AI as an Orchestration Layer, Not a Monolith

Rather than a single giant model, Periodic uses language models as an orchestration and reasoning layer that directs specialized, symmetry-aware neural nets tuned for atomic systems. This architecture — general LLM on top, specialized models as tools — appears to be the emerging standard for high-complexity scientific and enterprise applications.

> "We think about them almost as like an orchestration layer... but they can also use specialized neural nets as tools, as reward functions. So it's like an overall system." [00:11:39]

---

## 6. Overlooked Insights

### Robotics Is the Hidden Dependency That Will Determine Who Wins in Physical-World AI

Fedus briefly mentions that general-purpose dexterous robotics (when it crosses a reliability threshold) will be a "massive accelerator" not just for Periodic's throughput, but for spinning up entirely new labs. This is undersold in the conversation: whoever builds or owns reliable lab robotics will effectively control the data generation rate for physical-world AI — making companies like Physical Intelligence (Pi) or similar stealth robotics players a crucial upstream dependency for the entire physical sciences AI ecosystem.

> "If you had a dexterous humanoid who could wander into an unstructured lab and make sense and follow instructions reliably, that would be a huge accelerator... with improvements in robotics, it's just going to accelerate this." [00:26:17]

> "As these more general robotic systems come to be and hit this reliability threshold, it's going to be a massive accelerator for spinning up new labs as well." [00:27:59]

### Physics Talent Arbitrage Is a Real and Underexploited Hiring Strategy

Fedus and Gil briefly touch on the massive compensation gap between academic scientists (Stanford postdocs) and ML engineers — and how physicists are systematically undervalued by academia but are among the most capable builders in AI. The non-obvious implication: companies that aggressively recruit physicists and domain scientists from academia — before the market corrects — are accessing top-tier talent at a significant discount. Periodic appears to be explicitly doing this.

> "If you look up the cost of a Stanford postdoc, for example, relative to a machine learning engineer, it's like such a big difference... many people working in science, particularly in an academic setting, are very undercompensated relative to their societal value." [00:20:28]

> "Some of the scientists who've joined us are among the best in the world and it's been absolutely incredible working with them." [00:21:02]