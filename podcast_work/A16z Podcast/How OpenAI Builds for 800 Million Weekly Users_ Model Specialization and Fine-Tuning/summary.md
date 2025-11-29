# [How OpenAI Builds for 800 Million Weekly Users: Model Specialization and Fine-Tuning](https://www.youtube.com/watch?v=3x0jhpEj_6o)

**Podcast:** A16z Podcast
**Date:** 2025-11-28
**Participants:** Sherwin Wu, Erik Torenberg
**Region:** Western
**Video ID:** 3x0jhpEj_6o
**Video URL:** https://www.youtube.com/watch?v=3x0jhpEj_6o
**Transcript:** [View Transcript](./transcript.md)

---

# A16z Podcast Summary: Sherwin Wu on OpenAI's Developer Platform

### 1. Key Themes

### The Unexpected Proliferation of Specialized Models

The AI industry has dramatically shifted from expecting a single dominant model to embracing model specialization. As Sherwin Wu explains: "even within opening the thinking was that there would be like one model that rules them all...it's like definitely completely changed. It's like becoming increasing and clearer that there will be room for a bunch of specialized models. There will likely be a proliferation of other types of models." [[00:18:11]](https://www.youtube.com/watch?v=3x0jhpEj_6o&t=18m1s) This shift has major implications for the ecosystem, creating more opportunities for customization and vertical solutions rather than a winner-take-all dynamic.

### Models as Anti-Disintermediation Technology

Unlike traditional software layers, AI models resist abstraction in a unique way. Erik Torenberg observes: "the models are so hard to abstract away. Like they're just, they're just unruly, right? If you try to like have traditional software drive them, they just don't kind of manage very well...you kind of have to expose it to the user directly." [[00:12:43]](https://www.youtube.com/watch?v=3x0jhpEj_6o&t=12m33s) Sherwin confirms this, noting surprisingly high retention on the API: "the stickiness of the model itself has been surprising" because developers end up "building a product around the model" through deep iteration. [[00:15:10]](https://www.youtube.com/watch?v=3x0jhpEj_6o&t=15m0s) This creates natural defensibility that traditional APIs lack.

### The Evolution from Prompt Engineering to Context Engineering

The industry's understanding of how to work with models has fundamentally evolved. Sherwin notes: "the prevailing view this is back in 2022...prompt engineering is just not going to be a thing...the model would just be good enough." [[00:25:08]](https://www.youtube.com/watch?v=3x0jhpEj_6o&t=24m58s) Instead, the paradigm has shifted: "the name of the game now is...the context engineering site where it's like what are the tools you give it. What is like the data that it pulls in when does it pull on the right data?" [[00:25:44]](https://www.youtube.com/watch?v=3x0jhpEj_6o&t=25m34s) This reflects a maturation from simple instruction-following to sophisticated orchestration of intelligence.

---

### 2. Contrarian Perspectives

### Procedural Work Dominates More Than Silicon Valley Realizes

Sherwin challenges the tech industry's bias toward unstructured knowledge work: "there's another type of work, which is actually what we realize is like maybe even more prevalent in industry than software...work tends to be very procedural, very like SOP-oriented. Like customer support is a good example of this...And this pattern actually generalizes to do some different work...extensive like marketing, extensive like sales, extensive like a bunch, way more than it has any right to." [[00:48:12]](https://www.youtube.com/watch?v=3x0jhpEj_6o&t=48m2s) This insight explains why deterministic agent builders with nodes are seeing massive adoption despite seeming "not AGI forward" - they address real enterprise needs that Silicon Valley engineers undervalue.

### Usage-Based Pricing as a One-Way Ratchet

Sherwin shares a contrarian view from Ben Kotb (Roxette founder): "pricing is kind of like a one way ratchet. And like basically once you get a taste of usage based pricing, you're never gonna go back to like the per deployment pricing...it's getting, it gets closer and closer to like your true utility." [[00:34:29]](https://www.youtube.com/watch?v=3x0jhpEj_6o&t=34m19s) Despite the massive technical complexity of implementing usage-based billing at scale (800M users), it's becoming the irreversible standard because it aligns with actual value delivery, especially as costs remain high.

### Open Source Models Don't Cannibalize APIs

Despite fears of cannibalization, Sherwin reports: "we have not seen cannibalization at all...The customers tend to be like slightly different. The use cases are very different. And by the way, it turns out inference is super hard." [[00:39:12]](https://www.youtube.com/watch?v=3x0jhpEj_6o&t=39m2s) This challenges the conventional wisdom that open-sourcing models destroys API business. The reality is that "even if we just literally open source to GPT-5 or something, it would be really, really hard to inference it at the level that we are able to get it to do." [[00:40:00]](https://www.youtube.com/watch?v=3x0jhpEj_6o&t=39m50s)

---

### 3. Companies Identified

**Cursor**: A coding tool that exemplifies sophisticated multi-model usage and the anti-disintermediation thesis.

*Why mentioned*: Erik Torenberg describes using multiple OpenAI models within Cursor for different purposes: "my go to model at GPT-5...I use like Max mode with GPT-5 for planning...the tab complete model that's in cursor...the new model they just dropped is for like some basic...composed once good." [[00:16:19]](https://www.youtube.com/watch?v=3x0jhpEj_6o&t=16m9s) This demonstrates how successful products expose rather than hide model capabilities.

**Perplexity**: AI search company staffed by former Quora engineers.

*Why mentioned*: As an example of the exceptional talent concentration at early Quora: "a bunch of the perplexity team was there. Dennis was on the feed team with me." [[00:05:42]](https://www.youtube.com/watch?v=3x0jhpEj_6o&t=5m32s)

**Scale AI**: AI data infrastructure company founded by Alexandr Wang.

*Why mentioned*: Another example of Quora's legendary founding team diaspora: "Alexander the scale...He was there between high school and college." [[00:05:52]](https://www.youtube.com/watch?v=3x0jhpEj_6o&t=5m42s)

**Los Alamos National Labs**: Government research facility.

*Why mentioned*: As an example of OpenAI's government deployments: "we actually do have a local deployments Atlas Alamos National Labs...in a like, you know, classified a supercomputer with our with our model running there." [[00:01:26]](https://www.youtube.com/watch?v=3x0jhpEj_6o&t=1m16s)

---

### 4. People Identified

**Ben Kotb (Roxette founder)**: Pricing infrastructure expert.

*Why mentioned*: For his influential perspective on usage-based pricing evolution: "So there's a, we required this company called Roxette a while ago a founder of his name is Vencott...He's one of the best...his take is that pricing is kind of like a one way ratchet." [[00:34:06]](https://www.youtube.com/watch?v=3x0jhpEj_6o&t=33m56s) Erik specifically calls him out as someone they're "huge fans" of.

**Dennis (Perplexity team member)**: Former Quora feed engineer, now at Perplexity.

*Why mentioned*: As part of the exceptional early Quora engineering team that influenced the AI industry. [[00:05:45]](https://www.youtube.com/watch?v=3x0jhpEj_6o&t=5m35s)

**Johnny Ho and Jerry Ma**: Former Quora engineers.

*Why mentioned*: Part of the legendary 50-100 person Quora team that "was really solid. I still think that even while I was there, I was I still like him amazed at the quality of the talent." [[00:05:32]](https://www.youtube.com/watch?v=3x0jhpEj_6o&t=5m22s)

---

### 5. Operating Insights

### Fine-Tuning Unlocks Data Moats Through Reinforcement Learning

The shift from supervised fine-tuning (SFT) to reinforcement fine-tuning (RFT) fundamentally changes what's possible: "way back kind of back in like 2223 are fine tuning offering was I'd say like too limited...it was just like an asset like a supervised fine tuning...it's honestly just like instruction following plus plus...The big unlock that has happened recently is with the reinforcement fine tuning model...it allows you to leverage your data way more." [[00:21:57]](https://www.youtube.com/watch?v=3x0jhpEj_6o&t=21m47s) Companies have "giant treasure troves of data that they are sitting on" and RFT enables them to "create the world's best model using your data set" for specific verticals. [[00:23:40]](https://www.youtube.com/watch?v=3x0jhpEj_6o&t=23m30s)

### Data-for-Discount Exchanges Create Win-Win Dynamics

OpenAI is piloting innovative pricing where customers can "get discounted inference and potentially free training to if you're willing to share the data." [[00:24:29]](https://www.youtube.com/watch?v=3x0jhpEj_6o&t=24m19s) This creates a virtuous cycle: customers get economic benefits, OpenAI gets valuable training data, and the ecosystem benefits from better models. This is a clever operating approach to the classic data acquisition challenge.

### Separate Infrastructure for Different Modalities is Key to Success

On managing both language and image models (an "anti pattern" most companies fail at): "I think all like the world simulation team, like the team up builds Sora...It's just extremely solid...they're they're they're run very separately. They're kind of like thinking about their own particular roadmap...even like the inference stacks are are slightly different." [[00:43:23]](https://www.youtube.com/watch?v=3x0jhpEj_6o&t=43m13s) The key is complete separation with world-class teams rather than attempting to converge infrastructure.

---

### 6. Overlooked Insights

### The Token Laundering Economy

Erik Torenberg makes a brief but profound observation: "It is so remarkable how much of this entire economy is basically just token laundering. That's right. I think I can do to get like like English or like a natural language in and then like, you know, the intelligence out." [[00:30:55]](https://www.youtube.com/watch?v=3x0jhpEj_6o&t=30m45s) This insight captures the entire AI application layer's fundamental business model - companies are essentially intermediaries that translate natural language into structured intelligence outputs. The entire value chain is about finding novel ways to launder tokens through different interfaces and workflows, which explains both the opportunities and competitive dynamics in AI applications.

### Constrained Response Catalogs in Regulated AI

A barely-mentioned but hugely significant pattern: "some regulated industries actually can't let any generated content go to a user...what they do is...either pass in like a conversation tree...here are the viable things you can say choose which one to say. So language reasoning has happened by the model, but nothing generated comes out." [[00:49:12]](https://www.youtube.com/watch?v=3x0jhpEj_6o&t=49m2s) This represents a massive design pattern for AI in healthcare, finance, and other regulated industries - using AI for logic and routing while constraining outputs to pre-approved content. This approach solves compliance while maintaining intelligence benefits, potentially unlocking billions in regulated markets that seemed off-limits to generative AI.