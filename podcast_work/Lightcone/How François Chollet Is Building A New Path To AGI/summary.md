# [How François Chollet Is Building A New Path To AGI](https://podcasters.spotify.com/pod/show/ycombinator/episodes/How-Franois-Chollet-Is-Building-A-New-Path-To-AGI-e3h1jve)

**Podcast:** Lightcone
**Date:** 2026-03-27
**Processed:** 2026-03-28T17:06:33Z
**Participants:** François Chollet, Host 1 (Y Combinator), Host 2 (Y Combinator), Host 3 (Y Combinator), Host 4 (Y Combinator)
**Episode URL:** https://podcasters.spotify.com/pod/show/ycombinator/episodes/How-Franois-Chollet-Is-Building-A-New-Path-To-AGI-e3h1jve
**Transcript:** [View Transcript](./transcript.md)

---

# Summary: How François Chollet Is Building A New Path To AGI

---

## 1. Key Themes

### The Verifiable Reward Signal Is the Master Key to AI Automation

The single most important unlock in recent AI progress is not raw intelligence — it's the ability to formally verify outputs. Chollet argues that any domain with verifiable rewards can now be fully automated with current technology, and that code was simply the first to fall.

> "Any problem where the solutions you propose can be formally verified and you can actually trust a reward signal... any domain like this can be fully automated with current technology, with the LLM-based stack. And code is sort of like the first domain to fall, but there will be many others in the future. I think mathematics is also primed to see a revolution in the next few years for the same reasons." [00:06:26]

### Deep Learning Is a Dead End for True AGI — Symbolic Learning Is the Path to Optimality

Chollet makes the case that gradient descent cannot find generalizable programs — it overfits. The entire industry is scaling a fundamentally suboptimal approach, and the right answer is symbolic models that compress data to their shortest possible explanation.

> "I personally don't think that machine learning or AI in 50 years is still going to be built on this stack... I think it's inevitable that the world of AI will trend over time towards optimality. And so I'm trying to sort of leapfrog directly to optimality." [00:04:39]

> "The minimum description length principle that the model of the data that is most likely to generalize is the shortest. And I think you cannot find a model like this if you're doing parametric learning. You need to try symbolic learning." [00:04:09]

### AGI Will Be Shockingly Simple in Retrospect

Chollet's most striking claim is that AGI, when achieved, will be a small, elegant codebase — not a massive scaled-up system — and that the fundamental insight could have been implemented decades ago.

> "I do believe that, you know, when you create AGI, retrospectively, it will turn out that it's a code base that's less than 10,000 lines of code. And that if you had known about it back in the 1980s, you could have done AGI back then using the computer resources available back then." [00:36:00]

---

## 2. Contrarian Perspectives

### The Models Haven't Gotten Smarter — They've Just Been Better Trained

Most people attribute recent AI breakthroughs to increased intelligence or capability. Chollet argues it's purely a training improvement — models have a better execution model of code but no higher fluid IQ.

> "It's not so much that the models have higher fluid intelligence than they did with the first using models. It's just that you have this new paradigm of post-training... The models don't have higher fluid intelligence per se. They don't have like a higher IQ, so to speak. It's just that they're way better trained." [00:22:18]

### Automation ≠ AGI — The Industry Is Solving the Wrong Problem

The dominant industry definition of AGI (automating economically valuable tasks) is not actually about intelligence at all, according to Chollet. We may fully automate the economy before ever achieving true general intelligence.

> "My definition of general intelligence — many people around the industry these days, they say AGI is going to be a system that can automate most economically valuable tasks. And to me, that definition is it's about automation. It's not about intelligence." [00:09:52]

### Human-Made Harnesses Are a Sign of AGI's Absence, Not Progress Toward It

When a company saturates an AI benchmark by engineering custom harnesses around the problem, the AI community celebrates it as progress. Chollet says this is actually proof that AGI is far away.

> "The fact that you need humans to engineer these harnesses is also a sign that we're short of AGI today. Because if we had AGI, AGI would just make its own harness. It would not need to be told how to solve a problem. It would just figure it out." [00:25:36]

### Scaling LLMs Is Counterproductive at the Macro Level

While every rational actor is pouring money into the LLM stack (because returns are real), Chollet argues this monoculture is actively harmful to long-term AI progress.

> "It's counterproductive to have everybody working on the same thing... I think AI research will have to trend towards not just efficiency, but in fact, optimality over time." [00:04:39]

### Low-Probability Moonshots Are Obligatory if No One Else Will Do Them

Chollet operates Endia with only a 10-15% chance of success — and argues this is sufficient justification to pursue it, specifically because no one else will.

> "We have maybe a 10 or 15% chance of success, but that is enough that it's worth trying... if we don't do it, no one else will do it. Right. So it's worth trying. Even if we don't succeed, it's worth trying." [00:05:35]

---

## 3. Companies Identified

**Endia (NDI)**
- Description: A new AGI research lab founded by François Chollet, focused on symbolic program synthesis as an alternative to deep learning.
- Why mentioned: Building from first principles toward optimal AI, with a unique approach that no other major lab is pursuing.
> "We are trying to build this new branch of machine learning that will be much closer to optimal, unlike deep learning." [00:01:08]

**Confluence Lab (YC Winter 2026 batch)**
- Description: A YC-backed startup that built an agent harness approach to AI benchmarks.
- Why mentioned: Saturated ARC AGI V2 at 97% accuracy within just a couple months of working on it, demonstrating extraordinary speed of execution and the power of the harness-based RL loop.
> "I actually worked with a company in the winter 26 batch not too long ago called Confluence Lab, which actually ended up saturating the V2 results with 97%. And I think their task cost was a lot more efficient, too." [00:24:27] — Host 2 (Y Combinator)

**Poetic**
- Description: A company that built an agent harness approach targeting ARC V2.
- Why mentioned: Reached the top of the ARC V2 benchmark by structuring problem domains into formally verifiable environments — a meaningful demonstration of the new RL paradigm.
> "We actually had the founders of Poetic that came and spoke about the approach... the hardness is basically structuring a problem domain into something that can be formally verified. And they did that basically for ARK V2, which when they released it, they were at the top of the benchmark." [00:23:57] — Host 2 (Y Combinator)

---

## 4. People Identified

**François Chollet**
- Description: Creator of Keras, founder of the ARC Prize, and founder of Endia (NDI). One of the world's foremost AI researchers.
- Why mentioned: Built Keras in 2015 which became the dominant deep learning framework; designed the ARC-AGI benchmark series which has proven to be the most predictive benchmark for real AI capability jumps; now building a fundamentally new branch of ML.
> "I was trained deep learning model for natural language processing, in fact, in 2014. And from that work, I actually started developing this open source library, which I released, in fact, exactly 11 years ago, March 2015. So that was Keras." [00:12:55]

---

## 5. Operating Insights

### Build Compounding Stacks, Not Disconnected Experiments

Chollet's lab-building advice is directly applicable to any research or product organization: avoid constant pivots that throw away prior learnings. The goal is architectural leverage — each layer builds on the last.

> "You don't want to be in a situation where you're constantly trying something new. It's not reusing any learnings, any findings from the previous approaches. You want a compounding stack. You want to build reusable foundations and then the next layer and then the next layer." [00:43:24]

### Hire Your Power Users — They Are Always the Best People

When building an open source project or developer tool, your most enthusiastic community members are your best recruiting pipeline. Chollet flagged this as something Google made difficult and he regretted not doing more of.

> "Find the most enthusiastic users from your community and just hire them on your team. Amazing. Yeah. And these are always the best people, right?" [00:55:07]

### Documentation Should Teach the Domain, Not Just the Tool

For developer tools or technical products, docs that teach users the underlying domain — not just the product — dramatically expand your addressable audience and lower onboarding friction.

> "The docs should be not just telling you about how to use this thing. They should actually be teaching you about the domain in the first place. Because the folks who land on your website, they're not going to be already deep learning experts." [00:54:12]

---

## 6. Overlooked Insights

### Genetic Algorithms at Scale May Be a Wide-Open Opportunity

Chollet briefly but meaningfully flags genetic algorithms as a dramatically underinvested approach with enormous potential — particularly for automating scientific discovery. This was mentioned almost in passing, but the implication is significant: an entire paradigm with scaling potential has been essentially abandoned, and anyone willing to revisit it with modern compute could achieve breakthrough results.

> "Genetic algorithms, for instance. If you try to scale up genetic algorithms, I mean, I'm sure you can do incredible things with that. You could, in fact, probably do new science because that's based on search and search is the best fit for automating the scientific method... I think this is an approach that has a tremendous amount of potential. But not too many people are looking into scaling it up deeply." [00:46:37]

### Reading 1970s–80s AI Research Papers Is a Legitimate Alpha-Generating Strategy

Host 2 floated this idea and Chollet immediately validated it — the field has collapsed into monoculture, and the unexplored ideas from earlier eras represent a genuine whitespace. For investors or researchers looking for non-consensus bets in AI, going back to pre-neural-network-dominance literature is a concrete, actionable edge that almost no one is pursuing.

> "Earlier in the history of the AI research timeline, people were exploring more things and very different things. You've had this sort of like collapse of everything into one approach. It's actually kind of a bad idea." [00:48:41]