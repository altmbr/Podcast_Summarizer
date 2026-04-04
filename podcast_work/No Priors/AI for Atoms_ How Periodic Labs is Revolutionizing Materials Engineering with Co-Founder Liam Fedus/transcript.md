[00:00:05] Elad Gil: Today on No Priors we're talking with Liam Fedus. Liam is one of the co-creators of ChatGPT, which I think almost everybody uses at this point. He was the VP of post-training at OpenAI and before that was at Google Brain, where he worked on a variety of really early AI innovations. Liam will be telling us a bit about Periodic Labs, his company which is focused on building an AI foundation lab for atoms. In other words, how do we impact the physical world, material sciences, chemistry, etc., using AI?

[00:00:32] Elad Gil: Very exciting topic and excited to be talking with him today. Liam, thank you so much for joining us today on No Priors. Liam Fedus, Yeah, thank you so much for having me. It's great to see you. Liam Fedus, Yeah. So maybe what we can do, I think you're doing incredibly interesting things in terms of alternative types of models, specifically for material sciences, for the physical world. Effectively, what you're building is an AI foundation lab for atoms, which I think is fascinating. Liam Fedus, That's right. Liam Fedus, But maybe we can start with this a little bit more of your background. You know, I think you were VP at OpenAI. You worked on one of the first trillion parameter models ever, etc.

[00:01:01] Elad Gil: Could you tell us a little bit more about just like what got you here?

[00:01:04] Liam Fedus: Liam Fedus, Yeah. So even further back, I was a physics major in undergrad, spent some time doing dark matter research. We had an apparatus that was directionally sensitive to dark matter's direction. So it was very interesting.

[00:01:21] Elad Gil: Liam Fedus, Why are there, sorry to interrupt, I'd love to come back to this, but why are there so many physicists in AI right now? So you look at Dario Amodi who runs Anthropic. Liam Fedus, Of course, yeah. Liam Fedus, You look at Adam Brown at Google, you look at a variety of people and they all kind of have these physics backgrounds.

[00:01:33] Liam Fedus: Liam Fedus, Yeah. My old manager, Joshua, also physics and now Anthropic. Liam Fedus, Yeah. Why do you think that is? Liam Fedus, I think it's a great way to think about the world. It's like very principled, very like hard nosed scientists, very careful. And I don't know.

[00:01:49] Liam Fedus: Liam Fedus, Yeah. I think it's just, it's such an incredible field. You have such high leverage in computer science, in AI. And so I think a lot of physicists were seeing that, particularly in like high energy physics. After the discovery of the Higgs, I think a lot of high energy physicists were sort of looking for what's next. Ultimately, it becomes bottlenecked on the new apparatus for pushing the next energy frontier. And I think a lot of physicists were looking at their skill set and looking at the progress elsewhere.

[00:02:19] Liam Fedus: Liam Fedus, Yeah. And saying like, hey, I think I could be a huge contributor elsewhere.

[00:02:22] Elad Gil: Liam Fedus, This has been fascinating to see like string theorists and people working on buckles and all sorts of effects, like kind of moving into AI. Liam Fedus, Absolutely. Liam Fedus, It almost feels like we're recreating them in Hen Project or something, except now what we're seeking is, you know, different forms of intelligence. So, Liam Fedus, Yeah, that's right. Liam Fedus, Sorry to interrupt. So, you know, you studied physics, you worked on dark matter.

[00:02:39] Liam Fedus: Liam Fedus, That's right. And then I was basically, and then in grad school in physics, I was always gravitating towards the machine learning problems. I was looking at particle reconstruction. Liam Fedus, And it's thinking effectively machine learning problems. But it felt if I really wanted to push frontier of machine learning, I should be in computer science. So ended up at Google Brain was overlapping with the first year residents there. Absolutely remarkable group of people remarkable period for Google Brain.

[00:03:07] Liam Fedus: Liam Fedus, I mean, it was an era of when there's the creation of like distributed training strategies, mixture of experts, the transformer. It was a really rich period in that history. And it was a fun kind of like Cambrian era where people were really pushing the frontier with just like a handful of GPUs, really small collaborations. The field was a much, much earlier. And I think there was a lot of diversity and entropy in the research. And it was very fun. Liam Fedus, So it was kind of late 2010s or so, something like that.

[00:03:36] Liam Fedus: Liam Fedus, This was 2016, 2017. So Google Brain at that point was still really small and eventually was subsumed by DeepMind or combined with DeepMind. So it was at Google for many years, mostly just doing architecture work. So was really pushing sparsity that allows for more efficient serving of models at scale and just really pushing the scale of what we could do.

[00:04:00] Liam Fedus: Liam Fedus, Towards late 2022, really became excited about the creation of products. The technology was getting very compelling. And so I ended up at OpenAI with some other Googlers as well. And what did you work on specifically at OpenAI?

[00:04:15] Liam Fedus: Liam Fedus, Well, so the goal was we need to come up with some productionization of GPT-4. So OpenAI had GPT-4. It was pre-trained and there were some like LaVaroff post trains on it. And there's questions about like, how do we turn this incredibly powerful model into products? And we're all spitballing ideas like writing bot, coding bot, you know, very natural at the time. Some of our least interesting ideas were a meeting bot.

[00:04:42] Liam Fedus: So it would just sit in a Google Meet, take notes and then send out like to do's after. But John Schulman was very opinionated. He's like, we think we should keep it very general. Let's do a chatbot. And that became a large part of the effort for those few months.

[00:04:56] Elad Gil: That's like, oh yeah. So you worked on chat GPT. That's right. And obviously I felt like that was kind of the starting gun of this whole AI revolution, or at least in terms of people's awareness, like I'd started investing in the area beforehand. Right. But it seemed like almost as a secret up until chat GPT came out and then suddenly everybody realized that there's this powerful technology available. Yes. How did that lead you to materials and atoms and, you know, the physical world again? I know that was sort of your starting point in terms of academics. But what brought you back given how much is being transformed right now through language?

[00:05:26] Liam Fedus: I think just the inevitability of connecting these systems to the physical world. The opinion that I and others held as periodic was you're not going to see the same kind of acceleration in science and technology unless you start connecting these things to the physical world. Science ultimately isn't sitting in a room thinking really hard. You have to conduct experiments. You have to learn from them. You have to interface with reality.

[00:05:52] Liam Fedus: And the creation of chat GPT in late 2022 was an important technology, but it was still far too weak. We couldn't have done periodic on technology of that era.

[00:06:05] Liam Fedus: I think over the next few years past that, we saw ever improving models. We saw reasoning. I think like test time inference became really important. That led to more reliable error correction, more reliable tool use. And we see like the rise of coding agents and other agents. And I think those were foundational technologies necessary to then connect these systems to the physical world. It was just not possible with like the AI technology of 2022.

[00:06:34] Elad Gil: I guess the other thing that's missing from the physical world is data or at least data that's easily accessible. So you look at something like the big foundation models on the language side and they're basically trained on the internet as a major corpus. It's augmented in all sorts of ways with other data sources. How do you think about that for what you're doing where you're trying to model atoms in the physical world and how all that stuff kind of works?

[00:06:51] Liam Fedus: Yeah. So experiment. I mean, so we have simulation, physics simulations, and we have experiment. And, you know, I think exactly as you're pointing out, ML systems are good on the data you've trained them on, on the tasks you've trained them to do.

[00:07:06] Liam Fedus: I think sometimes there's like this mythology of AGI, ASI, RSI. And I think we see increasingly powerful systems, but they do become limited if they don't have access to the raw data to actually make informed decisions.

[00:07:22] Elad Gil: How much data do you need? And so I know that there's some data scale related research and other things in terms of how you kind of hill climb towards like a really good model. Yep. So how many experiments do you need to run or how many data points do you need? Or how do you think about the diversity of data points you need to generate? I'm a little bit curious, like what does that actually look like tangibly?

[00:07:43] Liam Fedus: Um, so there is some generalization from the existing models. So we don't need to reproduce a system that can understand and write English or write code. So we're kind of like leveraging.

[00:07:56] Elad Gil: And are you using open source for that or close source models or some?

[00:07:59] Liam Fedus: We use a combination. Uh-huh. Yeah. So for example, like periodic spend zero effort on improving coding models. Um, we're incredibly impressed by codex, cloud code. And so that's been a huge accelerator for the company. Um, but focus our machine learning efforts where, um, you know, the existing frontiers is not sufficiently good for us.

[00:08:17] Liam Fedus: I think going back to the data question, we're leveraging, call it order tens of trillions of tokens that went into open source models. And that's given this like very like foundational understanding. But once we start moving into specific, um, discovery areas, chemical spaces, um, we can see, um, a very high level of sample efficiency.

[00:08:42] Liam Fedus: So the system isn't starting as like a randomly initialized neural net. It has a strong prior on the world. And where does that prior come from? What data do you think that informs that? Just general? Just, just like, you know, papers, the internet, as you're pointing out. Yeah. Um, however, that's insufficient. Um, one of the engineers on our team was looking at a reported material, um, property and it was just sort of extracted values from literature.

[00:09:08] Liam Fedus: And it was really interesting to see the reported value spanned many orders of magnitude. And so you train an ML system on that and it's like, well, the best you can do is model distribution, but you're no closer to like a ground truth. And that's where experimental data comes in where you now have a grounding in this. Um, but really important. It's not just like a pool of data. It's this interactive closed loop system that is so powerful.

[00:09:34] Liam Fedus: Um, once you have the experimental data, you can look through it, you can look for aberrations, you can look for patterns, you can look for consistency with, um, simulation data, with literature, and then that helps drive the next set of experiments. So it's not just a pool of data. It's this very active loop.

[00:09:52] Elad Gil: I see. And then, um, how do you think about diversity of data? So I look at something like, um, alpha fold or some of the protein folding, uh, related, um, models, which are amazing, right? If you think about it, I used to work as a biologist and we would, you know, a crystal structure would take years if it happened at all. Cause you wouldn't necessarily certain if you could crystallize the specific protein and a certain reagent conditions in a way that would be performant for actual extra, uh, you know, crystal axillography and everything, or NMR or whatever approach you took for structure.

[00:10:18] Elad Gil: And then sort of alpha fold comes out and you can just arbitrarily model anything on the protein world, which was, you know, amazing as a breakthrough. Um, but it was a very specific data set that already existed that had lots and lots and lots of structures over decades, over decades of work. How hard do you have to bootstrap that for every single materials domain or do you choose specific ones that you think can then generalize?

[00:10:48] Liam Fedus: Um, but I think you can think of, um, different levels of generalization and for systems that are strongly governed by quantum mechanical effects. There is some generalization there. Um, but like if you produce a system that has modeled, um, quantum mechanical objects really accurately, it's not really helping much on like, you know, fluid dynamics or, you know, like another kind of like level of abstraction.

[00:11:14] Liam Fedus: And so the generalization we're seeing is quite good. Um, but there's almost like a first principles you can.

[00:11:20] Elad Gil: Oh, that's interesting. So you could do like, here are the basic steps of chemical synthesis. Here's quantum mechanics. Here's different aspects of how atoms interact in general or Vanderwall forces or things like that. Absolutely. Oh, so interesting. Yeah, that's cool. And then from a architecture perspective, is there anything unique that you're doing or interesting? Or can you talk a little bit about how you're actually constructing some of these models on top?

[00:11:39] Liam Fedus: Yeah. So, uh, language models are incredibly powerful. It's a very natural interface. Uh, and so we continue to use these. Um, but we think about them almost as like an orchestration layer. So that's sort of a, a co-pilot assistant, but also like a system that can direct, um, experiments. And it's almost, it's orchestrating other specialized models as well.

[00:12:02] Liam Fedus: So we do construct neural nets that, um, are specially designed for atomic systems where there's like some symmetry awareness. Um, and those have much lower latency and they've been like fine tuned for that. And so basically you kind of think of this like orchestrating layer that can ingest literature. It can go through our experimental data. It can go through different, uh, modalities, but they can also use specialized neural nets as tools, as reward functions.

[00:12:31] Liam Fedus: So it's like an overall system.

[00:12:33] Elad Gil: Okay. Yeah. That makes a lot of sense. Yeah. I've seen a lot of people architect those sorts of approaches, even for things like customer support or other areas. Like it seems like it's the common architecture that's emerging as you're doing these different use cases. That's right. Yeah.

[00:12:45] Liam Fedus: Yeah. But transformers have been very powerful. Yeah.

[00:12:47] Elad Gil: Yeah. And that's really cool. So if I look at the language world, one of the things that was pretty unique about it, and it's the reason I think these companies like open AI and tropic and others are growing so fast is it just plugged into a very big domain of human existence, which is all language. And all language means enterprise software and enterprise interactions. And it means consumer behavior is basically how we interact with the world. Yes. It seems like there's a little bit more of a leap for other areas.

[00:13:12] Elad Gil: So for example, in robotics, there's really interesting things, different types of robots that exist in the world, but the footprint of that is quite limited relative to language. And the same seems to be true for material sciences. So how do you think about where you're going to commercialize this first or who you're going to work with or other specific domains of products that you're working on first?

[00:13:28] Liam Fedus: So we've begun working very closely with scientists. We've treated periodic as our customer zero and seeing how can we transform how this field of science is done. But there's huge opportunities across all of these industries, all these enterprises that are interfacing with the physical world. People who are bottlenecked by materials engineering, process engineering.

[00:13:53] Liam Fedus: And again, those are kind of the same natural interfaces where engineers are asking questions about their data. They're trying to find aberrations. They're trying to debug machinery. They're trying to get to a better formulation. It's actually a quite universal thing as well. And so we've kind of created our little testing ground internally. And now we're sufficiently excited about the tech we've been building and to see this acceleration for advanced manufacturing more broadly.

[00:14:22] Elad Gil: And is your model going to be developing materials for other third parties? Is it developing your own materials that you then sell in the market? Because it almost reminds me a little bit of a biotech model where in biotech you can either partner with a big pharma and then effectively help them create a drug and take a royalty on it, or you can build your own drugs. How do you think about that in the context of what you're doing?

[00:14:41] Liam Fedus: We're thinking about ourselves as an intelligence layer for these companies. So you can think about system of record, control plane for different experiments and getting to solutions. But like you're saying, there is a very interesting aspect of some breakthroughs here could have really high value. And it might be more akin to a discovery model like we've seen in biotech and elsewhere. But starting thinking about art just as a software business. Have you ever had the The Diamond Age? That's very fast.

[00:15:11] Liam Fedus: Yeah.

[00:15:12] Elad Gil: Have you had the Diamond Age? No, I haven't. It's the Neil Stephenson book. It's basically this book about, it was written in the 90s. Okay. And there's two key concepts in it. One key concept is there's effectively an AI tutor that's unleashed on the world and it kind of teaches huge numbers of young girls all sorts of skills. And it's this very interesting thing about AI education. And then in parallel- Why young girls in particular?

[00:15:34] Elad Gil: Basically, this AI research scientist creates a primer for his daughter and the Chinese steal it and clone it and distribute it across the country. And because he built it for young girls, it's suddenly every young girl in China has it. Right, right. So that's the reason. Got it. Okay, yeah. It's this very China theft of IP kind of thing. Yes, right. And then the other part of the book is about matter pipes into everybody's homes and they all have 3D printers. And you download blueprints and it just creates whatever you need in the physical world.

[00:16:03] Elad Gil: And some people start evolving different nanobots to do different things. It's this very advanced kind of AI plus materials kind of future world. Yes. What is your vision or conception of what our world looks like in 10 years, assuming periodic is successful?

[00:16:16] Liam Fedus: Well, I mean, I think as you're pointing out, you're going from systems that aren't just writing essays, not just writing software, but to literally generating matter. And I think it has pretty profound implications to semiconductors, aerospace, energy. And I think it's incredibly important for can we increase the pace of just like the physical development of the world? I mean, we see how quickly the digital realm is changing.

[00:16:44] Liam Fedus: Software engineering now looks wildly different than even six months ago. But I think we see like similar opportunities in the physical world. Of course, like atoms are hard. And so you will have some limits of physics. But just because atoms are hard doesn't mean there's not an order of magnitude or two to speed up. Just making sense of huge amounts of data and getting to solutions more quickly. Yeah.

[00:17:12] Liam Fedus: So I think what we're trying to do is give humanity this agency for atomic rearrangement synthesis. And we think it's going to just be a huge accelerator. So, I mean, if our physical world could keep up at some fraction to our digital world, I think life will just feel dramatically different.

[00:17:31] Elad Gil: Yeah, it's kind of the revolution that could really come. Yeah, it kind of reminds me of almost the materials equivalent of the agricultural revolution.

[00:17:36] Interjector: Yeah.

[00:17:37] Elad Gil: We suddenly had a massive spike in productivity. Exactly. And it seems like there's been all sorts of bottlenecks that have constrained us until now that you folks are trying to address.

[00:17:44] Liam Fedus: That's right.

[00:17:44] Elad Gil: Yeah. What aspect of the work that you're doing are you most excited about?

[00:17:49] Liam Fedus: Collaboration between these groups of people. I mean, it's like this is just irreducibly a multidisciplinary problem. We have physicists and chemists working really closely with some of the top AI researchers in the world, working closely with some of the best engineers in the world. And this multidisciplinary close collaboration is just absolutely incredible because seeing firsthand how a field can fundamentally change.

[00:18:15] Liam Fedus: People who have been doing research for, in some cases, decades in a field and now seeing like, oh, under these systems, under intelligent systems, it could look this very different way. And I mean, I use like an analog to machine learning a lot. Going back to the early Google brain days where the frontier is pushed forward by a few GPUs and a few people.

[00:18:38] Liam Fedus: Now you look at this era where it's really like industrialized and there's dozens, hundreds of researchers working together with hundreds of thousands, millions of GPUs dictated and driven by scaling laws. Everything is about scaling. It's given that predictability. It's allowed us to put huge amounts of capital into this field.

[00:18:57] Liam Fedus: And I think the physical sciences, physical engineering will have a very similar property where we establish these scaling properties and bring that mindset. And so periodic in this field is really thinking about how do we bring much larger scale sets of experiments to bear on this? And intelligent systems have enabled us. Automation has enabled us. And you really need both.

[00:19:25] Liam Fedus: An improvement to automation where you can soon become, create bottlenecks in intelligence. And I mean, the scientists very much feel this where they're not used to working at that level of throughput and they just can't simply make sense of so much data. So interesting.

[00:19:41] Elad Gil: Yeah. So I guess in terms of scale here, one of the real benefits, one of the things that's really benefited the frontier labs on the LLM side is just scale of capital and therefore scale of GPU and scale of data. Of course. Is this similarly a capital intensive area in your mind?

[00:19:57] Liam Fedus: Yeah, we will require more capital. GPUs are so extraordinarily expensive. What's interesting is just the compute costs relative to physical infrastructure is actually surprising where so much money is spent on the compute that the physical infrastructure sometimes is actually lower, but has very large lead times. And there's intrinsic difficulty of having these well calibrated, well functioning physical systems.

[00:20:24] Liam Fedus: But from a capital perspective, it's primarily a compute cost.

[00:20:28] Elad Gil: Yeah, it's really interesting. If you look up the cost of a Stanford postdoc, for example, relative to a machine learning engineer, it's like such a big difference. Absolutely. And you really, you know, my takeaway is that many people working in science, particularly in an academic setting, are very undercompensated relative to sort of their societal value. Absolutely.

[00:20:47] Elad Gil: And so I always like it when companies kind of help bring people into the fold in terms of both human impact, but also, you know, that ability to do things at real scale and, you know, really do things a different way. So it must be very exciting for the people on your team.

[00:21:02] Liam Fedus: Yeah. I mean, some of the scientists who've joined us are among the best in the world and it's been absolutely incredible working with them.

[00:21:08] Elad Gil: Yeah. I mean, it sounds like you've built such an amazing interdisciplinary team. Are there specific roles you're actively looking for right now or key things that you really want to hire up? Absolutely.

[00:21:17] Liam Fedus: So on our site, we have decomposed the world into bits and atoms. You know, it's a loose taxonomy. But on bits side, we're really thinking about mid-training, pre-training roles from the AI side, always more infrastructure roles. And on atom side, like control engineering, system engineering. But also now thinking, too, about, you know, spanning that with like product engineering. So, yeah. Across the world. Yeah, it's exciting.

[00:21:43] Elad Gil: Yeah, it's really cool. So I think one of the things that everybody is really thinking deeply about or is excited about right now is AGI, ASI, sort of these advanced systems that are as good as humans or better than humans at different things. Right. Or are very generalizable in terms of their abilities to do a broad swath of things. How do you think about that, but in the context of what's happening over the overall foundation model curve? Because obviously you were very integral in terms of the development of some of these systems. And then how do you think about that applied specifically to some of the areas you're working in?

[00:22:10] Liam Fedus: I think one fallacy is thinking about intelligence as a scalar. We've consistently seen these systems have a very odd spikiness. And it's actually possible to architect a system that is world class on some math domain. But then you could do some perturbations to the questions and actually degrade it substantially. So it's like a bad high school student. And so there's this like odd spikiness to these systems.

[00:22:37] Liam Fedus: So basically you can make a system that's like a genius at one thing and not very good at a bunch of other stuff. And I guess the point I was making is those fields can actually be quite adjacent. So like sometimes a generalization can be non-intuitive. But one way I think about recursive self-improvement is really kind of akin to neural architecture search from roughly 10 years ago. And I think there's a very clear path for software engineering.

[00:23:03] Liam Fedus: So these systems have become so incredibly impressive on this domain as a result of huge amounts of data, really cheap verifiable environments. Like you can check Unitesco from failing to passing with just a few CPUs. It's basically instantaneous. There's no domain expertise gap between an AI researcher or software engineer. And obviously this will become and is becoming a larger contributor to the next generation of the system.

[00:23:30] Elad Gil: When do you think it just flips into we just everything is machine self-improvement versus human directed or needs a lot of human intervention? So do you think that's two years away? Do you think that's five years away? Do you think that's 10 years away?

[00:23:42] Liam Fedus: Well, I guess like building on what I was saying is I think there's a domain caveat to that. So rolling forward that software engineering self-improvement, I think you're going to have a system that can write complete repositories, identify bugs, refactor code, but it doesn't suddenly understand biology. Sure. Right. It's just like there's a domain gap there in knowledge. Yeah.

[00:24:06] Liam Fedus: But even beyond that, there's sets of strategies done in software engineering that differ from scientific or engineering strategies. So you're not operating under, it's not like decision making under uncertainty to the same degree. It's like very verifiable. And that's driven so much of our work. So in that domain, I think it's happening now-ish. And I think we'll see the same thing too for AI research. Uh-huh.

[00:24:36] Liam Fedus: That's a slower outer loop because now the experiment isn't just checking some unit tests passing, but it's checking what was the scaling property? Did this model converge? What's the generalization of the system? That requires GPUs. That requires many hours of experiments. But I think that will also will-

[00:24:55] Elad Gil: And those are all evals that people use today as they're looking at existing models. And so they do have that utility function, that feedback loop that can be just driven by self-learning.

[00:25:04] Liam Fedus: That's right. That's right. But again, like the connection of these things to the physical world is going to be so critical because both of the systems are being trained in a closed loop against that domain. So it's a closed loop for doing software engineering, a closed loop for doing AI research. And that's the premise of periodic. Like we need to have these closed loops of actually doing science, of actually doing engineering.

[00:25:28] Liam Fedus: And these two domains are how I think the rest of the world will go with some delay. And this is again like the foundational technology that we're thinking about.

[00:25:39] Elad Gil: Do you think you need sufficiently good robotic systems in order to have that closed loop for what you're doing? In other words, do you need something like Pi or skills or something else to work in order for periodic to hit that escape velocity in terms of a closed loop system?

[00:25:56] Liam Fedus: No, but it's a huge accelerator. The goal for periodic is to generate high quantity, high quality data, diverse data, and automation is assistance to that. So right now we employ people as well, and we have autonomous parts that are just very reliable.

[00:26:17] Liam Fedus: If you had a dexterous humanoid who could wander into an unstructured lab and make sense and follow instructions reliably, that would be a huge accelerator. Right now, the automation of physical systems requires a very careful design, and it's slow. But I think with improvements in robotics, it's just going to accelerate this.

[00:26:40] Liam Fedus: But already the reliability of these sort of like hybrid systems is sufficient to produce huge amounts of reliable data, but it's just going to accelerate us forever.

[00:26:50] Elad Gil: Yeah, one of the reasons I ask is I used to run this company, Color, and we built our own liquid handling robotic systems, right? We buy liquid handling robots, but then we have to adjust them dramatically. We had cameras that would use ML to monitor the system and sort of make adjustments. We had to 3D print parts to decrease vibrations on the platform because we were dealing with such small volumes of liquid. Right.

[00:27:14] Elad Gil: And so there's enormous amounts of customization versus just having – and the firmware for it was awful, and writing against that was painful –

[00:27:20] Interjector: Yep.

[00:27:20] Elad Gil: Versus just having like a robotic system that would work like a modern system in all the ways that you'd conceive that. Right. And that's the reason that I was asking is if you really want to do high-throughput experiments, you need these underlying systems to be able to do all the liquid handling and to do all the titration of stuff and all the rest of it.

[00:27:34] Liam Fedus: Yeah, that's right. I mean, I think it's – look, right now we're using almost like more like off-the-shelf robotics. It's like very simple, very commoditized, not doing like a huge amount of innovation on that front. But again, like as these more general robotic systems come to be like hit this reliability threshold, it's going to be a massive accelerator for spinning up new labs as well.

[00:27:59] Elad Gil: Yeah. You've seen such a wide range of different things happen in the AI world since – Indeed. You know, you're working at Google, I guess at this point about a decade ago. And so you were there during the birth of the Transformer model. You were there for the birth of ChatGPT. What are you most excited about outside of periodic over the next few years in terms of what's happening with AI? I mean, of course, robotics.

[00:28:21] Liam Fedus: Again, I'm like – I'm just so excited about the interface of AI systems with the physical world. And we're approaching one angle of that, which is science engineering. And we need that data in order to make those advances. But simply just agency and control of the physical world via robotics is going to be transformative. So I'm very excited about these interface layers. I think that's going to be such a massive opportunity.

[00:28:51] Liam Fedus: Because, I mean, you know, how many software engineers are there in the world versus people who like the physical world? And there's just labor shortages everywhere. So, yeah, I think it's going to be a very interesting decade. Oh, amazing. Well, thank you so much for joining us today. Yeah, well, thank you so much. It was really good chatting today.

[00:29:07] No Priors Announcer: Find us on Twitter at NoPriorsPod. Subscribe to our YouTube channel if you want to see our faces. Follow the show on Apple Podcasts, Spotify, or wherever you listen. That way you get a new episode every week. And sign up for emails or find transcripts for every episode at no-priors.com.