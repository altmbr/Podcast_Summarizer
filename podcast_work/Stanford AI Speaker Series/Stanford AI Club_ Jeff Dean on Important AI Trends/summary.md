# [Stanford AI Club: Jeff Dean on Important AI Trends](https://www.youtube.com/watch?v=AnTw_t21ayE)

**Podcast:** Stanford AI Speaker Series
**Date:** 2025-11-23
**Participants:** Jeff Dean
**Region:** Western
**Video ID:** AnTw_t21ayE
**Video URL:** https://www.youtube.com/watch?v=AnTw_t21ayE
**Transcript:** [View Transcript](./transcript.md)

---

# Podcast Summary: Jeff Dean on 15 Years of AI Advances at Google

## 1. Key Themes

### The Compounding Power of Algorithmic and Scale Improvements

Jeff Dean demonstrates throughout the talk that the most dramatic advances in AI haven't come from scale alone, but from the interaction between better algorithms and more compute. He shows this pattern repeatedly: transformers delivered "much higher accuracy from the paper with 10 to 100x less compute" [[00:18:45]](https://www.youtube.com/watch?v=AnTw_t21ayE&t=18m35s), sparse models showed "an 8x improvement in training reduction in training cost compute for the same accuracy" [[00:22:47]](https://www.youtube.com/watch?v=AnTw_t21ayE&t=22m37s), and vision transformers achieved "four to 20 times less compute, you could get to the best results" [[00:21:29]](https://www.youtube.com/watch?v=AnTw_t21ayE&t=21m19s). This isn't just about efficiency—it's about unlocking new capabilities by freeing up compute budget to train fundamentally larger and more capable models. As Dean notes about the transformer breakthrough, you could get results "with 10 times fewer parameters in a transformer based model" [[00:18:56]](https://www.youtube.com/watch?v=AnTw_t21ayE&t=18m46s), which then enables building even larger models with the saved resources.

### The Hardware-Software Co-Evolution That Enabled Modern AI

The development of specialized AI hardware was driven by an existential calculation that revealed a critical inflection point. Dean recalls: "if we wanted to run this high quality model on CPUs, which is what we had in the data centers at that time, we would need to double the number of computers Google had in order just to roll out this improved speech recognition feature" [[00:13:19]](https://www.youtube.com/watch?v=AnTw_t21ayE&t=13m9s). This wasn't just an optimization—it was a requirement for deployment. The TPU design capitalized on two key insights: neural nets are "very tolerant of very low precision computations" and they are "just different compositions of essentially dense linear algebra operations" [[00:13:49]](https://www.youtube.com/watch?v=AnTw_t21ayE&t=13m39s). The result was hardware that was "15 to 30 times faster than CPUs and GPUs at the time and 30 to 80 times more energy efficient" [[00:14:39]](https://www.youtube.com/watch?v=AnTw_t21ayE&t=14m29s). The latest Ironwood system represents "about 3,600 times the peak performance per pod, compared to the first one" and is "about 30 times as energy efficient" [[00:16:20]](https://www.youtube.com/watch?v=AnTw_t21ayE&t=16m10s) as TPU v2.

### Multi-Modal Reasoning as Native Architecture Rather Than Retrofit

The Gemini approach treats multi-modality as a foundational design principle rather than an afterthought. Dean emphasizes they "wanted it to be multi-model from the start to take all kinds of different modalities as input and also produce lots of modalities as output" [[00:32:57]](https://www.youtube.com/watch?v=AnTw_t21ayE&t=32m47s). The most striking demonstration is the model's ability to "actually reasons in intermediate imagery" [[00:38:45]](https://www.youtube.com/watch?v=AnTw_t21ayE&t=38m35s) when solving problems like predicting which bucket a ball lands in—generating step-by-step visual reasoning rather than just producing text. This represents a fundamental shift in how models process information, moving beyond text-based reasoning chains to native visual thinking that mirrors human cognitive processes.

## 2. Contrarian Perspectives

### Mathematically Wrong Training Methods That Work Better

Dean reveals that the distributed training approach in Google's DistBelief system was "completely mathematically wrong because at the same time, all the other mathematical model replicas were also computing gradients and asynchronously adding them into this shared set of parameter state. So that made a lot of people kind of nervous because it's not actually what you're really supposed to do, but it turned out to work" [[00:07:01]](https://www.youtube.com/watch?v=AnTw_t21ayE&t=6m51s). This challenges the academic preference for theoretically sound approaches and suggests that practical engineering that accepts mathematical impurity can unlock scale advantages that overwhelm the theoretical downsides. The system ran "200 replicas of the model all turning away synchronously and updating parameters. And a team to work reasonably well" [[00:07:16]](https://www.youtube.com/watch?v=AnTw_t21ayE&t=7m6s).

### The Undergraduate's Failed Thesis Was Actually Right

Dean's contrarian insight comes from his own early failure: "So it turns out I was completely wrong. You needed like a million times as much processing power to make really good neural nets, not 32 times" [[00:04:52]](https://www.youtube.com/watch?v=AnTw_t21ayE&t=4m42s). Most people would have concluded neural networks were a dead end. Instead, Dean kept the idea "always kind of had a little clinging in the back of my mind. This could be an important instruction" [[00:05:08]](https://www.youtube.com/watch?v=AnTw_t21ayE&t=4m58s). The contrarian insight is that being directionally correct but quantitatively wrong by orders of magnitude isn't actually being wrong—it's being early. This patience across decades to wait for Moore's Law and architectural improvements to catch up to an insight represents a fundamentally different investment timeframe than most researchers or companies pursue.

### Smaller Models Can Match Larger Ones Through Knowledge Transfer

The distillation work challenges the conventional wisdom that you need to deploy large models to get large model performance. Dean shows that "if you use these soft targets in a distillation process, then 3% of the training data, you can get 57% accuracy" [[00:29:05]](https://www.youtube.com/watch?v=AnTw_t21ayE&t=28m55s) compared to 44% without distillation and 58.9% with the full dataset. This means "you can train a really, really large model. And then you can use distillation to take a much smaller model and use the distillation targets to give you a really high quality small model that approximates quite closely the performance of a large model" [[00:29:26]](https://www.youtube.com/watch?v=AnTw_t21ayE&t=29m16s). The contrarian implication: the race to deploy ever-larger models may be misguided when you can train large and deploy small.

### Sparsity Over Density: Activating Less is More Efficient

Dean pushed for sparse models based on the contrarian view that "in a normal neural network, you have the idea model activated for every example or every token you're trying to predict. And that just seems very wasteful. It'd be much better to have a very, very large model and then have different parts of it be good at different kinds of things" [[00:22:12]](https://www.youtube.com/watch?v=AnTw_t21ayE&t=22m2s). Instead of the conventional wisdom to make dense models more efficient, the insight was to make models larger but activate "maybe one to one to five percent of the total parameters in the model are used on any given prediction" [[00:22:28]](https://www.youtube.com/watch?v=AnTw_t21ayE&t=22m18s). This approach, now used in "most of the models you hear about today, like Gemini models" [[00:23:17]](https://www.youtube.com/watch?v=AnTw_t21ayE&t=23m7s), contradicts the intuition that smaller, fully-activated models would be more efficient.

## 3. Companies Identified

### Google

**Description:** Technology company pioneering AI research and deployment at massive scale

**Why Mentioned:** Featured as the primary organization driving multiple foundational AI breakthroughs, from infrastructure (MapReduce, Bigtable, Spanner) to frameworks (TensorFlow) to models (Gemini). Dean highlights Google's unique capability to deploy AI at scale: "if we wanted to run this high quality model on CPUs, which is what we had in the data centers at that time, we would need to double the number of computers Google had" [[00:13:19]](https://www.youtube.com/watch?v=AnTw_t21ayE&t=13m9s). This constraint drove the creation of custom AI hardware that became industry-defining.

**Quote:** "We built some of the most foundational infrastructure that I was modern Internet, including MapReduce, Bigtable, and Spanner" [[00:00:12]](https://www.youtube.com/watch?v=AnTw_t21ayE&t=2s) and "our goal with the Gemini effort is really train the world's best multi-models use them all across Google and make them available to external people as well" [[00:32:42]](https://www.youtube.com/watch?v=AnTw_t21ayE&t=32m32s)

### DeepMind

**Description:** Google's AI research laboratory (acquired division)

**Why Mentioned:** Referenced as part of Google's AI organization structure where Dean serves as Chief Scientist

**Quote:** "Jeff now serves as the chief scientist of Google D.Mine in Google Research, where he leads the team" [[00:00:28]](https://www.youtube.com/watch?v=AnTw_t21ayE&t=18s)

## 4. People Identified

### Andrew Ng

**Description:** AI researcher, Stanford professor, and early deep learning pioneer

**Why Mentioned:** The chance encounter with Andrew Ng catalyzed the creation of Google Brain. Dean describes: "So in 2012, I bumped in actually to Andrew In in a microkitchen at Google. And I'm like, oh, hi, Andrew, how are you? He's like, what are you doing here? And he's like, oh, well, I'm starting to spend a day week at Google. And I haven't really figured out what I'm doing yet here. But my students at Stanford are starting to get good results with neural nets on various kinds of speech problems. I'm like, oh, that's cool. We should train really big neural networks" [[00:05:20]](https://www.youtube.com/watch?v=AnTw_t21ayE&t=5m10s). This casual conversation led to one of the most important AI research projects in history.

**Quote:** "So that was kind of the genesis of the Google Brain project was how do we scale large training of neural networks using lots and lots of computation" [[00:05:54]](https://www.youtube.com/watch?v=AnTw_t21ayE&t=5m44s)

### Ilya Sutskever

**Description:** Co-creator of sequence-to-sequence learning and LSTM applications at Google

**Why Mentioned:** Led the breakthrough work on sequence-to-sequence models that became foundational for translation and many other applications

**Quote:** "Then my colleagues, Ilya, Oriola and Quack worked on using LSTM. So these kind of recurrent long shorter memory models to work on a particularly nice problem that's traction where you have one sequence. And you're going to use that to predict a different sequence" [[00:11:21]](https://www.youtube.com/watch?v=AnTw_t21ayE&t=11m11s)

### Oriol Vinyals

**Description:** Research scientist at Google working on sequence models and distillation

**Why Mentioned:** Collaborator on both the sequence-to-sequence work and the distillation paper that showed how to transfer knowledge from large to small models

**Quote:** "Another important technique turns out to be a technique I worked on with Jeff Hinton and Oriol Vinyol's called distillation" [[00:27:29]](https://www.youtube.com/watch?v=AnTw_t21ayE&t=27m19s)

### Geoffrey Hinton

**Description:** Deep learning pioneer and Turing Award winner

**Why Mentioned:** Co-author on the distillation paper that enabled training smaller models to match larger model performance

**Quote:** "Another important technique turns out to be a technique I worked on with Jeff Hinton and Oriol Vinyol's called distillation" [[00:27:29]](https://www.youtube.com/watch?v=AnTw_t21ayE&t=27m19s)

### John Hennessy and David Patterson

**Description:** Computer architecture pioneers and Turing Award winners

**Why Mentioned:** Co-authors with Dean on examining the societal implications of AI across multiple domains

**Quote:** "Actually John Hennessy and Dave Patterson and I and a few other who authors worked on a paper last year that kind of touched on all those different areas and look and interview domain experts in all those areas" [[00:41:23]](https://www.youtube.com/watch?v=AnTw_t21ayE&t=41m13s)

## 5. Operating Insights

### Build Abstractions That Hide Complexity But Enable Scale

The Pathways system exemplifies how to manage massive-scale distributed systems. Dean explains it "orchestrates all this computation. So you don't use a ML researcher. Don't have to think about, okay, which network links that I use. It sort of chooses the best thing at the best time and it uses deals with failures of what happens if one of these chips goes down or one of these pods goes down" [[00:24:55]](https://www.youtube.com/watch?v=AnTw_t21ayE&t=24m45s). The key insight is creating "a layer underneath jacks that is Pathways runtime system. And so we can then make a single Python process look like it jacks programming environment that instead of having four devices has 10,000 devices" [[00:25:14]](https://www.youtube.com/watch?v=AnTw_t21ayE&t=25m4s). This abstraction layer lets researchers think in terms of their algorithms while the system handles the distribution complexity.

### Use Diverse RL Signals Based on Domain Verifiability

Dean outlines a sophisticated approach to post-training that adapts the reinforcement learning source to the problem domain: "RL from machine feedback is you can use machine feedback from another model, often called a reward model, where you prompt the reward model to judge, you know, do you like answer A or B better and use that as an RL signal. And that then probably one of the most important things is RL and verifiable domains like math or coding" [[00:30:59]](https://www.youtube.com/watch?v=AnTw_t21ayE&t=30m49s). For coding specifically: "you give reward for code that compiles. And then even more reward for code that compiles and passes the unit tests" [[00:31:38]](https://www.youtube.com/watch?v=AnTw_t21ayE&t=31m28s). The operating principle is to use the highest-quality signal available for each domain rather than one-size-fits-all approaches.

### Demonstrate Desired Behavior in Prompts to Elicit Better Responses

The chain-of-thought prompting insight reveals a fundamental operating principle about how to extract maximum capability from models. Dean explains: "if you just tell the model, here's the example problem and it just is told to give the answer, like, you know, the answer is nine, then it doesn't do as well as if you give the model sort of some guidance that it's supposed to show its work and demonstrate that in the first problem. And then it will actually go ahead and admit it's, you know, show its work for the actual problem, we're trying to get it to solve" [[00:25:47]](https://www.youtube.com/watch?v=AnTw_t21ayE&t=25m37s). The meta-insight: "because the model gets to do more computation for every token it emits in some sense it's able to use more compute in order to arrive at the answer" [[00:26:29]](https://www.youtube.com/watch?v=AnTw_t21ayE&t=26m19s).

## 6. Overlooked Insights

### The Self-Supervised Learning Paradigm Creates Near-Infinite Training Data

Dean briefly mentions that "there's lots and lots of text in the world. Self supervised learning on this text can give you almost infinite numbers of training examples where the right answer is known because you have some word that you've removed from the view of the model" [[00:19:33]](https://www.youtube.com/watch?v=AnTw_t21ayE&t=19m23s). This seemingly simple observation represents a profound shift in machine learning economics. Traditional supervised learning requires expensive human labeling that scales linearly with desired capability. Self-supervised learning inverts this: the data labels itself, creating a training corpus limited only by available text/data in the world. This architectural choice—making the model predict missing pieces rather than requiring external labels—essentially removed the data bottleneck from AI development and enabled the scale we see today. The implications extend beyond language to any domain where you can create self-supervised objectives.

### Multi-Metro Training Infrastructure Signals Compute Scale Exhaustion

Dean briefly mentions that "you can even run computations where you're using multiple metro areas and a long distance high speed length to communicate between multiple metro areas" [[00:24:36]](https://www.youtube.com/watch?v=AnTw_t21ayE&t=24m26s). This is presented as a capability of Pathways, but it reveals something more significant: Google has exhausted the compute available in single data centers and even single campuses for their largest training runs. This suggests we're approaching fundamental limits on how much compute can be co-located, which has profound implications for training efficiency (since cross-metro communication is orders of magnitude slower than in-rack communication). The fact that they're engineering around this constraint indicates the frontier models are now so large that geographic distribution is necessary, which likely creates a significant moat—most organizations cannot coordinate training across multiple metro areas with high-speed dedicated links.