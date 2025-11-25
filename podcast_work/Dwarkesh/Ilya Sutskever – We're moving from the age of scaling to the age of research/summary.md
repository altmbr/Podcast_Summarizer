# [Ilya Sutskever – We're moving from the age of scaling to the age of research](https://www.youtube.com/watch?v=aR20FWCCjAs)

**Podcast:** Dwarkesh
**Date:** 2025-11-25
**Participants:** Dwarkesh Patel, Ilya Sutskever
**Region:** Western
**Video ID:** aR20FWCCjAs
**Video URL:** https://www.youtube.com/watch?v=aR20FWCCjAs
**Transcript:** [View Transcript](./transcript.md)

---

# Dwarkesh Patel & Ilya Sutskever Podcast Summary

## 1. Key Themes

### The Era Transition: From Scaling to Research Redux

The field is transitioning from the "age of scaling" (2020-2025) back to an "age of research." During the scaling era, compute was the primary bottleneck and pre-training provided a clear recipe: more data + more compute = better results. Now, with massive compute available but diminishing returns from pure scaling, the bottleneck has shifted back to fundamental research insights. "From 2020, from 2020, it was the age of research. Now, from 2020 to 2025, it was the age of scaling... But now the scale is so big. Like, is the belief really that, oh, it's so big, but if you had a 100x more, everything would be so different. Like, it would be different for sure. But like, is the belief that if you just 100x the scale, everything would be transformed? I don't think that's true. So, in respect to the age of research again, just with the computers." [[00:21:22]](https://www.youtube.com/watch?v=aR20FWCCjAs&t=21m12s)

Ilya notes that "scaling sucked out all the air in the room" [[00:36:47]](https://www.youtube.com/watch?v=aR20FWCCjAs&t=36m37s) and created a situation where "there are more companies than ideas, but quite a bit" [[00:37:04]](https://www.youtube.com/watch?v=aR20FWCCjAs&t=36m54s). The breakthrough insights like AlexNet (2 GPUs), the Transformer (8-64 GPUs), and even reasoning approaches didn't require maximal compute to prove their viability - they required the right ideas.

### The Generalization Mystery: The Core Unsolved Problem

The most fundamental puzzle in current AI is the dramatic disconnect between evaluation performance and real-world reliability. Models achieve superhuman scores on difficult benchmarks yet make elementary mistakes that humans would never make. "How to reconcile the fact that they are doing so well on eVALs... They are doing so well. But the economic impact seems to be dramatically behind... And it's almost like it's very difficult to make sense of how can the model on the one hand do these amazing things. And on the other hand, like repeat itself twice in some situation" [[00:01:44]](https://www.youtube.com/watch?v=aR20FWCCjAs&t=1m34s)

Ilya proposes a provocative explanation: companies inadvertently train RL environments inspired by their evaluation benchmarks, essentially "reward hacking" at the human researcher level. "What would be a rail training that could help on this task? Right? I think that is something that happens. And I think it could explain a lot of what's going on. If you combine this with generalization of the models actually being inadequate, that has the potential to explain a lot of what we are seeing." [[00:04:28]](https://www.youtube.com/watch?v=aR20FWCCjAs&t=4m18s)

The analogy he offers is powerful: imagine two students approaching competitive programming. One practices 10,000 hours specifically for competitions, memorizing all proof techniques and algorithms. The other practices 100 hours but has broader capabilities. "Which one do you think is going to do better in their career later on? The second." [[00:06:48]](https://www.youtube.com/watch?v=aR20FWCCjAs&t=6m38s) Current models are like the first student - hyper-optimized for specific benchmarks but lacking robust generalization.

### Super Intelligence as Super Learning, Not Omniscience

Rather than conceptualizing AGI as a finished system that can perform every job, Ilya proposes thinking about it as a learning system that can learn any job. "I would produce like a super intelligent 15-year-old that's very eager to go and you say, okay, I'm going to, they don't know very much at all, the great student, very eager. You go and be a programmer, you go and be a doctor, go and learn." [[00:50:20]](https://www.youtube.com/watch?v=aR20FWCCjAs&t=50m10s)

This reframes the entire paradigm. The term "AGI" itself may be misleading - it emerged as a reaction to "narrow AI" but overshot the target. "A human being is not an AGI. Because a human being, yes, there is definitely a foundation of skills, a human being, a human being lacks a huge amount of knowledge. Instead, we rely on continued learning." [[00:49:45]](https://www.youtube.com/watch?v=aR20FWCCjAs&t=49m35s) The deployment model would involve these learning systems being deployed into various roles, continuously learning on the job, similar to how humans join organizations and become productive over time.

## 2. Contrarian Perspectives

### Emotions as Hard-Coded Value Functions Are AI's Missing Piece

Ilya describes a neurological case study that challenges conventional thinking about intelligence: a person who lost emotional processing through brain damage could still solve puzzles and appeared cognitively intact, but became completely dysfunctional at decision-making. "He would take him hours to decide on which socks to wear, and he would make very bad financial decisions." [[00:12:11]](https://www.youtube.com/watch?v=aR20FWCCjAs&t=12m1s)

This suggests emotions aren't just irrational noise to be eliminated but rather evolution's solution to grounding decision-making - a built-in value function that evolution managed to hard-code despite it requiring recognition of high-level, abstract concepts. "It is too narrow. It's only good for negotiation, conflict, certain social skills, strategizing that kind of stuff." [[01:31:23]](https://www.youtube.com/watch?v=aR20FWCCjAs&t=1h31m13s) The mystery is how evolution encoded these sophisticated social desires into the genome when "it's a high level concept that's represented in the brain" [[00:12:27]](https://www.youtube.com/watch?v=aR20FWCCjAs&t=12m17s) rather than a simple sensory signal like smell.

### Pre-Training's Success Comes From Its Data, Not Its Generalization

Ilya challenges the implicit assumption that pre-training is fundamentally better at generalization than RL. Instead, its power may come from two simpler factors: (a) the sheer quantity and diversity of data, and (b) not having to choose what data to include. "The main strength of pre-training is that there is a so much of it. And b, you don't have to think hard about what data to put into pre-training." [[00:08:29]](https://www.youtube.com/watch?v=aR20FWCCjAs&t=8m19s)

With RL, companies must deliberately choose environments and reward signals, introducing "such a huge variety of a rail environments you could produce" [[00:04:05]](https://www.youtube.com/watch?v=aR20FWCCjAs&t=3m55s) and creating countless opportunities to optimize for the wrong thing. Pre-training's advantage isn't superior learning - it's that it captures "the whole world as projected by people onto text" [[00:08:48]](https://www.youtube.com/watch?v=aR20FWCCjAs&t=8m38s) without requiring researchers to make these choices.

### SSI Has Sufficient Compute Because Others Waste Theirs

When challenged about SSI's apparent compute disadvantage compared to frontier labs, Ilya provides a contrarian economic analysis. While other companies raise vastly more money, "a lot of what their a lot of their compute goes for inference... you need to have a big staff of engineers, of salespeople, a lot of the research needs to be dedicated for producing all kinds of product related features. So then when you look at what's actually left for research, the difference becomes a lot smaller." [[00:41:10]](https://www.youtube.com/watch?v=aR20FWCCjAs&t=41m0s)

Moreover, he argues that maximal compute isn't necessary to prove research ideas: "if you want to build the absolutely best system, then it helps to have much more compute. And especially if everyone is within the same paradigm, then compute becomes one of the big differentiators." [[00:39:28]](https://www.youtube.com/watch?v=aR20FWCCjAs&t=39m18s) But for discovering fundamentally new approaches, SSI's compute is sufficient to demonstrate viability.

### The Straight Shot to Superintelligence Might Be Better

While the conventional wisdom is that gradual deployment helps society adapt and makes AI safer through iterative feedback (as with airplane safety improving through crash investigations), Ilya argues there's value in the "straight shot" approach. The primary benefit: "you are, so one of the challenges that people face when they're in the market is that they have to participate in the rat race. And the rat race is quite difficult in that it exposes you to do to difficult trade-offs which you need to make." [[00:44:15]](https://www.youtube.com/watch?v=aR20FWCCjAs&t=44m5s)

However, he acknowledges the counterpoint: "it is useful for the world to see powerful AI because that's the only way you can communicate it... you see an AI doing this and AI doing that. It is incomparable." [[00:45:01]](https://www.youtube.com/watch?v=aR20FWCCjAs&t=44m51s) The resolution might be that "even in the stretch of scenario, you would still do a gradual release of it... It's just a question of what is the first thing that you get out of the door." [[00:46:54]](https://www.youtube.com/watch?v=aR20FWCCjAs&t=46m44s)

### Intelligence Explosion Will Be Dampened by Practical Constraints

Contrary to the standard recursive self-improvement narrative where a million copies of top researchers rapidly bootstrap superintelligence, Ilya expresses skepticism: "I don't know. I think I think they'll definitely be a there'll be diminution returns because you want you want people who think differently rather than the same... if they were literal copies of me, I'm not sure how much more incremental value you'd get." [[01:29:06]](https://www.youtube.com/watch?v=aR20FWCCjAs&t=1h28m56s)

He also challenges the winner-takes-all dynamic: "my strong intuition is that it's not how it's going to go" [[01:28:24]](https://www.youtube.com/watch?v=aR20FWCCjAs&t=1h28m14s) even if one company achieves human-like learning first. Instead, "competition loves specialization and you see it in the market, you see it in evolution as well. So you're going to have lots of different niches and you're going to have lots of different companies who are occupying different niches." [[00:26:52]](https://www.youtube.com/watch?v=aR20FWCCjAs&t=26m42s)

## 3. Companies Identified

**SSI (Safe Superintelligence Inc.)**
- Ilya Sutskever's current company focused on building aligned superintelligence
- Raised $3 billion at $32 billion valuation
- Described as "squarely age of research company" that has "made quite good progress over the past year" [[01:19:05]](https://www.youtube.com/watch?v=aR20FWCCjAs&t=1h18m55s)
- Different technical approach focused on understanding reliable generalization
- Strategy is to potentially go straight to superintelligence rather than incremental product releases, though this may change

**Google/DeepMind**
- Mentioned as potentially finding "a way to get more out of pre-training" based on Twitter discussions [[00:21:02]](https://www.youtube.com/watch?v=aR20FWCCjAs&t=20m52s)
- Gemini team specifically noted for recent progress

**OpenAI** 
- Discussed in context of spending "on the order of $56 billion a year" on experiments [[00:42:04]](https://www.youtube.com/watch?v=aR20FWCCjAs&t=41m54s)
- Collaborating with Anthropic on AI safety initiatives
- Ilya's former company, where he co-authored GPT-3 and other major advances

**Anthropic**
- Mentioned as beginning to collaborate with OpenAI on safety work [[00:59:11]](https://www.youtube.com/watch?v=aR20FWCCjAs&t=59m1s)
- Part of the frontier lab ecosystem

**Meta**
- Attempted to acquire SSI during fundraising
- Hired Ilya's former co-founder, who "was the only person from SSI to join meta" [[01:20:13]](https://www.youtube.com/watch?v=aR20FWCCjAs&t=1h20m3s)

## 4. People Identified

**Ilya Sutskever**
- Co-founder of SSI and former chief scientist at OpenAI  
- Co-author of foundational work including AlexNet and GPT-3
- Described his research taste: "an aesthetic of how AI should be by thinking about how people are, but thinking correctly... looking for almost beauty, beauty, simplicity, ugliness. There's no room for ugliness. It's just beauty, simplicity, elegance, correct inspiration from the brain." [[01:33:14]](https://www.youtube.com/watch?v=aR20FWCCjAs&t=1h33m4s)
- Predicted 3+ years ago that competitor companies would begin collaborating on AI safety, which is now happening [[00:59:18]](https://www.youtube.com/watch?v=aR20FWCCjAs&t=59m8s)

**Yann LeCun**
- Referenced for making the point that "children learn to drive after 16 hours, after 10 hours of practice" [[00:27:24]](https://www.youtube.com/watch?v=aR20FWCCjAs&t=27m14s)
- Used to illustrate debates about sample efficiency

## 5. Operating Insights

### The Power of Language in Shaping Research Direction

Ilya identifies how specific terms fundamentally shaped the field's thinking. The word "scaling" was "just one word, but it's such a powerful word because it informs people what to do" [[00:19:45]](https://www.youtube.com/watch?v=aR20FWCCjAs&t=19m35s). Similarly, "AGI" exists not as an essential descriptor but as a reaction to "narrow AI" - and in doing so, it may have led the field astray by suggesting a finished omniscient system rather than a learning system.

This insight suggests that as leaders, we should be extremely thoughtful about the terminology we introduce, as it will shape how entire organizations and fields conceptualize their work. The right framing can unlock progress; the wrong one can lead to years of misdirected effort.

### Front-Load Verification Difficulty Into Research Direction Selection

When discussing how to identify promising research directions with limited compute, the implicit framework is: choose directions where modest-scale experiments can definitively prove or disprove the core hypothesis. "If you are doing something different, do you really need the absolute maximal scale to prove it? I don't think it's true at all. I think that in our case, we have sufficient compute to prove to convince ourselves and anyone else that what we're doing is correct." [[00:41:51]](https://www.youtube.com/watch?v=aR20FWCCjAs&t=41m41s)

This is the opposite of "we'll try it and scale it up if it works" - it's designing the research question so that the answer becomes clear at achievable scale.

### Hire for Diversity of Thought in AI Research Teams

When asked about the value of having many copies of the same researcher, Ilya emphasized: "I think they'll definitely be a there'll be diminution returns because you want you want people who think differently rather than the same... if they were literal copies of me, I'm not sure how much more incremental value you'd get." [[01:29:06]](https://www.youtube.com/watch?v=aR20FWCCjAs&t=1h28m56s)

This contradicts the common Silicon Valley bias toward cultural fit and similar backgrounds. For research specifically, the operating insight is to deliberately seek out researchers with different "prejudices" and approaches, as diversity of perspective is more valuable than raw talent replication.

### Use Top-Down Beliefs to Sustain You Through Contradictory Data

Ilya describes how aesthetic intuition guides him through the inevitable experimental failures: "if you just trust the data all the time, well, sometimes you can be doing a correct thing, but there's a bug... How can you tell that there is a bug? How do you know if you should keep debugging or you conclude it's the wrong direction? Well, is the top-down? Well, how should you can say the things have to be this way? Something like this has to work. Therefore, we gotta keep going." [[01:35:03]](https://www.youtube.com/watch?v=aR20FWCCjAs&t=1h34m53s)

This suggests maintaining strong theoretical frameworks and first-principles reasoning as tools to distinguish between "this approach is wrong" and "this implementation has a bug." The best researchers have enough conviction in their top-down models to persist through apparent empirical failures.

## 6. Overlooked Insights

### The Sigmoid Learning Curve of RL Reveals Something Fundamental

Ilya briefly mentions that RL learning curves look like sigmoids - learning very little for a long time, then rapidly learning, then asymptoting - which is totally different from the power law of pre-training. [[00:33:02]](https://www.youtube.com/watch?v=aR20FWCCjAs&t=32m52s) This passing observation may actually be profound: it suggests RL and pre-training are operating under fundamentally different learning dynamics, not just different applications of the same underlying mechanism.

If RL's difficulty comes from needing to find a hypothesis that's exponentially distant from your current distribution (as suggested by information theory), while pre-training benefits from having everything in its massive dataset from the start, this explains why RL is so brittle and sample-inefficient. The shape of the learning curve itself is diagnostic of the learning mechanism - and we should perhaps be paying much more attention to this signal when evaluating new training approaches.

### Human Social Desires Are Evolution's Unsolved Alignment Success

The most overlooked but potentially crucial insight: evolution somehow managed to hard-code high-level, abstract social goals (caring about status, reputation, others' perceptions) into humans despite these being "high level concept[s] that's represented in the brain" [[00:12:27]](https://www.youtube.com/watch?v=aR20FWCCjAs&t=12m17s) rather than simple sensory signals. "It's pretty easy to understand how evolution would endow us with the desire for food that smells good. Because smell is a chemical... But evolution also has endowed us with all these social desires... I feel strongly that they're baked in. And I don't know how evolution did it." [[00:12:06]](https://www.youtube.com/watch?v=aR20FWCCjAs&t=11m56s)

This is profound because if we understood evolution's solution to aligning the cortex with the brainstem's values, where the brainstem cannot possibly understand the high-level abstractions the cortex operates on, we might have solved the alignment problem. The fact that even people with "all kinds of strange mental conditions and deficiencies and emotional problems tend to care about this also" [[00:16:47]](https://www.youtube.com/watch?v=aR20FWCCjAs&t=16m37s) suggests this alignment mechanism is remarkably robust. 

Ilya tried to explain it with spatial encoding but found counterexamples (people with half their brain removed still maintain these desires) [[00:16:17]](https://www.youtube.com/watch?v=aR20FWCCjAs&t=16m7s). This mystery deserves far more attention from the AI safety community - the answer may already exist in neuroscience, we just haven't recognized its significance.