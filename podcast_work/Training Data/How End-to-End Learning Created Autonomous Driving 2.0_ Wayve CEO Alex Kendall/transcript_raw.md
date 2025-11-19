# How End-to-End Learning Created Autonomous Driving 2.0: Wayve CEO Alex Kendall

**Podcast:** Training Data
**Date:** 2025-11-18
**Video ID:** 8x_O8BeGNTw
**Video URL:** https://www.youtube.com/watch?v=8x_O8BeGNTw

---

[00:00:00] If you're building a vertically integrated robotic solution,
[00:00:02] SPEAKER_02: maybe you can go deep, but our ambition is to be the
[00:00:05] SPEAKER_02: embodied AI foundation model for all of the best
[00:00:08] SPEAKER_02: fleets and manufacturers around the world.
[00:00:10] SPEAKER_02: And to do that, unless we want to overload the company by building
[00:00:15] SPEAKER_02: a separate neural network for each application,
[00:00:17] SPEAKER_02: we need to be out of generalize.
[00:00:18] SPEAKER_02: We need to be able to amortize our cost over one large
[00:00:21] SPEAKER_02: intelligence and to be able to very quickly adapt to each
[00:00:24] SPEAKER_02: different application that our customers care about.
[00:00:27] SPEAKER_02: That's what we're trying to push.
[00:00:28] SPEAKER_02: [♪ OUTRO MUSIC PLAYING [♪ OUTRO MUSIC [♪
[00:00:42] [♪ OUTRO MUSIC PLAYING [♪
[00:00:45] SPEAKER_00: Today we're talking with Alex Kendall, CEO of Wave,
[00:00:48] SPEAKER_00: about the shift from software 1.0 to 2.0,
[00:00:51] SPEAKER_00: or from classical machine learning to end-to-end neural
[00:00:53] SPEAKER_00: networks in autonomous driving.
[00:00:55] SPEAKER_00: Wave sells an autonomous driving stack to auto OEMs,
[00:00:58] SPEAKER_00: similar to Tesla FSD, but for non-test-law automobiles.
[00:01:01] SPEAKER_00: Major car manufacturers globally like Nissan are choosing
[00:01:04] SPEAKER_00: Wave to power their AV stacks.
[00:01:06] SPEAKER_00: Alex started Wave back in 2017 when most self-driving software
[00:01:09] SPEAKER_00: stacks were massive hand-coded C++ code
[00:01:11] SPEAKER_00: bases covering every possible edge case like navigating
[00:01:14] SPEAKER_00: around double parked cars.
[00:01:16] Alex bet the farm from the beginning on an end-to-end
[00:01:18] SPEAKER_00: neural net approach to self-driving and on the use of synthetic
[00:01:21] SPEAKER_00: data and world models as the ultimate path to generalization
[00:01:24] SPEAKER_00: and scaling.
[00:01:25] SPEAKER_00: Today, the architecture is reshaping AV and all of
[00:01:27] SPEAKER_00: physical AI including robotics.
[00:01:29] SPEAKER_00: Enjoy the show.
[00:01:30] SPEAKER_00: [♪ OUTRO MUSIC PLAYING [♪
[00:01:32] Alex, thanks for joining us on the show.
[00:01:34] SPEAKER_01: Hey, Pat, hi, Sonja.
[00:01:35] SPEAKER_01: One of the things that is very special about your company
[00:01:38] SPEAKER_01: is that it sort of typifies AV 2.0,
[00:01:42] SPEAKER_01: meaning a new architectural approach that I think is kind of
[00:01:46] SPEAKER_01: demonstrated to be superior to the AV 1.0 approach
[00:01:50] SPEAKER_01: that people toiled with for so many years.
[00:01:53] SPEAKER_01: Can we just start by defining what was AV 1.0?
[00:01:56] SPEAKER_01: What is AV 2.0?
[00:01:58] For sure.
[00:01:59] SPEAKER_02: When we started the company in 2017,
[00:02:01] SPEAKER_02: the opening pitch in our C-deck was all about
[00:02:05] SPEAKER_02: the classical robotics approach at the time was
[00:02:08] SPEAKER_02: to take a perception, planning, mapping, control,
[00:02:10] SPEAKER_02: essentially break down the autonomy problem
[00:02:12] SPEAKER_02: into a bunch of different components
[00:02:14] SPEAKER_02: and largely hand engineer them.
[00:02:16] SPEAKER_02: And our pitch was that, okay, we think that the future of
[00:02:19] SPEAKER_02: robotics is not going to be a system that's
[00:02:21] SPEAKER_02: hand engineer to drive with a lot of infrastructure
[00:02:24] SPEAKER_02: like high-definition maps.
[00:02:25] SPEAKER_02: But instead, we thought that the future of robots
[00:02:29] SPEAKER_02: would be intelligent machines that have the onboard
[00:02:30] SPEAKER_02: intelligence to make their own decisions.
[00:02:33] SPEAKER_02: And of course, the best way we know how to build an AI
[00:02:35] SPEAKER_02: system is within to end-earned learning.
[00:02:37] SPEAKER_02: So for the last 10 years, we've been promoting an approach,
[00:02:40] SPEAKER_02: next generation approach, AV 2.0 that replaces that stack
[00:02:43] SPEAKER_02: with one end-to-end neural network.
[00:02:46] SPEAKER_02: Now, of course, that may seem more obvious today,
[00:02:50] SPEAKER_02: but it has been contrarian for many, many years.
[00:02:54] SPEAKER_02: But I think today it's maybe unfair to make that basic
[00:02:57] SPEAKER_02: distinction because, of course, anyone who's worth a
[00:03:00] SPEAKER_02: grain of salt will use deep learning in various parts of the
[00:03:03] SPEAKER_02: stack. But what you see in more incumbent solutions to
[00:03:07] SPEAKER_02: autonomous driving is, of course, deep learning for
[00:03:09] SPEAKER_02: perception and maybe for each different component,
[00:03:11] SPEAKER_02: but still a lot of hand interface, there's still a
[00:03:13] SPEAKER_02: lot of infrastructure on high-deficient maps,
[00:03:15] SPEAKER_02: and perhaps reliance on a lot of hardware.
[00:03:19] SPEAKER_02: So our solution is still somewhat
[00:03:24] SPEAKER_02: moved on, but today, rather than just being an end-to-end network,
[00:03:26] SPEAKER_02: today, of course, we start to talk about foundation models.
[00:03:28] SPEAKER_02: We start to talk about more of a general purpose
[00:03:31] SPEAKER_02: intelligence, one that can understand not just how to drive
[00:03:34] SPEAKER_02: that car, but many cars with different sensor
[00:03:37] SPEAKER_02: architectures with different use cases.
[00:03:38] SPEAKER_02: And so really, it all boils down to how do we build the
[00:03:42] SPEAKER_02: most intelligent robot that can scale without
[00:03:46] SPEAKER_02: needing owner of infrastructure?
[00:03:49] So where there's sensor inputs, motion output,
[00:03:54] gigantic neural net in the middle.
[00:03:56] SPEAKER_01: That's right. At a very, very simple level, but some of the
[00:04:01] SPEAKER_02: interesting things you see that are maybe different from the
[00:04:03] SPEAKER_02: story we've all heard with large language models
[00:04:05] SPEAKER_02: is with autonomous driving, of course, there are some
[00:04:08] SPEAKER_02: interesting new factors. One is, of course, safety.
[00:04:12] SPEAKER_02: The system we need to make sure is safe by design.
[00:04:15] SPEAKER_02: And what that means is that we can't just pump more data in
[00:04:18] SPEAKER_02: and hope that hallucinations go away.
[00:04:21] SPEAKER_02: But we need to design an architecture that is still
[00:04:24] SPEAKER_02: into end-to-end data driven, but is both functionally safe,
[00:04:28] SPEAKER_02: and we can build a robust behavioral safety case.
[00:04:32] SPEAKER_02: So that introduces some interesting architectural
[00:04:36] SPEAKER_02: challenges. And then, of course, we also need to run real-time
[00:04:39] SPEAKER_02: onboard a robot, onboard a vehicle.
[00:04:41] SPEAKER_02: And so dealing with the onboard compute and onboard sensor
[00:04:44] SPEAKER_02: limitations, make it an interesting challenge.
[00:04:48] SPEAKER_02: Yes, it's the same narrative we're seeing playing out in
[00:04:50] SPEAKER_02: robotics that we've seen play out and all these other AI
[00:04:53] SPEAKER_02: fields like language or game playing agents.
[00:04:55] SPEAKER_02: It's that an end-to-end data-learn solution is out
[00:04:58] SPEAKER_02: competing anything we can hand code.
[00:05:00] SPEAKER_02: And what we're excited to be pioneering is that exact same
[00:05:03] SPEAKER_02: narrative here in robotics and autonomous vehicles.
[00:05:05] SPEAKER_02: And when you guys started this in 2017 and it was a very
[00:05:08] SPEAKER_01: contrarian approach, when people from the industry
[00:05:13] SPEAKER_01: said, well, that'll never work but cuts.
[00:05:15] SPEAKER_01: How did they finish that sentence?
[00:05:18] I could count hundreds of those things.
[00:05:22] SPEAKER_02: Yeah, typical arguments were, look, it's not safe.
[00:05:26] SPEAKER_02: It's not interpretable.
[00:05:29] SPEAKER_02: You can't understand what it's doing or even simply,
[00:05:33] SPEAKER_02: it doesn't make sense.
[00:05:34] SPEAKER_02: We haven't heard of this AI thing.
[00:05:37] SPEAKER_02: And look, I think five, 10 years ago, it was probably
[00:05:40] SPEAKER_02: reasonable to say, end-to-end-end learning wasn't interpretable.
[00:05:44] SPEAKER_02: But I don't think that's true today.
[00:05:45] SPEAKER_02: I think today we have a lot of really great tools for
[00:05:48] SPEAKER_02: understanding and responding to insights about the way
[00:05:52] SPEAKER_02: these deep learning systems reason.
[00:05:55] SPEAKER_02: But moreover, I think if you have the ambition to build
[00:05:58] SPEAKER_02: any intelligent machine, I think it's naive to think
[00:06:01] SPEAKER_02: you can build a complex intelligent machine and actually make it
[00:06:05] SPEAKER_02: you know, let's say, strictly interpretable to the point
[00:06:08] SPEAKER_02: where you can point to a single line of code or a single thing
[00:06:11] SPEAKER_02: that causally made the outcome occur.
[00:06:14] SPEAKER_02: The beauty of intelligent machines is that they are
[00:06:16] SPEAKER_02: so wonderfully complex.
[00:06:19] SPEAKER_02: And there, I think the way that we're going to not just design them,
[00:06:23] SPEAKER_02: but understand them is through a data-driven structure.
[00:06:27] Can you say more about the before and after of the
[00:06:29] SPEAKER_00: AV1.0 stack and the millions, billions of lines of code that
[00:06:34] SPEAKER_00: goes into those systems versus the two that are systems today?
[00:06:40] SPEAKER_00: And how quickly is that changing?
[00:06:42] SPEAKER_00: Because my sense is that deep learning, large neural nets,
[00:06:46] SPEAKER_00: hitting the physical economy is a much more recent phenomenon
[00:06:49] SPEAKER_00: than people might appreciate.
[00:06:51] SPEAKER_00: Well, especially when you think about path to distribution
[00:06:54] SPEAKER_02: and deploying these systems, I mean, the automotive industry has just gone
[00:06:57] SPEAKER_02: through a seismic shift and bringing out software to fine vehicles
[00:07:00] SPEAKER_02: and the right hardware on these cars to be able to make them drive.
[00:07:04] SPEAKER_02: Maybe one common point of debate is, is it camera only or camera radar
[00:07:10] SPEAKER_02: as a sensor approach to autonomy?
[00:07:13] SPEAKER_02: Just to be clear on our position, Wave, we want to build an AI that can
[00:07:18] SPEAKER_02: understand all kinds of different sensor architectures.
[00:07:19] SPEAKER_02: There's going to be sometimes where camera only solution makes sense,
[00:07:22] SPEAKER_02: sometimes where camera radar, light, and we train our
[00:07:26] SPEAKER_02: our embodied AI model on all of those permutations from very diverse data sources.
[00:07:31] SPEAKER_02: And the car we just drove in is a camera only stack.
[00:07:34] SPEAKER_02: We've got other cars that we work on with partners that have radar and
[00:07:37] SPEAKER_02: lighter and of course there's different trade-offs that you take there.
[00:07:41] SPEAKER_02: But more generally, we're seeing mass-produced cars from the best manufacturers
[00:07:45] SPEAKER_02: around the world have a GPU, but onboard have surround camera,
[00:07:48] SPEAKER_02: surround radar and sometimes a front lighter.
[00:07:51] SPEAKER_02: And what's beautiful about that is there's now the opportunity to see this AI come out
[00:07:54] SPEAKER_02: and benefit people around the world.
[00:07:56] SPEAKER_02: I think that kind of software-defined infrastructure is happening
[00:08:00] SPEAKER_02: and automotive has perhaps not yet happened to the same degree in other
[00:08:04] SPEAKER_02: robotics verticals, but I'm sure the markets are going to move that way as well.
[00:08:08] SPEAKER_02: And in general, having the right level of compute and infrastructure in a scalable way and
[00:08:14] SPEAKER_02: opening up these platforms to AI I think is what's really making this possible.
[00:08:18] SPEAKER_02: And that's gone through a tipping point in the last couple of years.
[00:08:21] And you know, your perspective of AV2.0 has flipped from contrarian to I'd say consensus.
[00:08:28] SPEAKER_00: Maybe in the last two or three years, do you think it was FSD12 that did it?
[00:08:33] SPEAKER_00: When did that mindset start to shift?
[00:08:36] I miss the contrarian day, but even today I still, I was in a conversation this morning where
[00:08:43] SPEAKER_02: I still see a lot of folks still say, yes, we need into an AI.
[00:08:48] SPEAKER_02: They've brought the big tech narrative around the future of AI,
[00:08:51] SPEAKER_02: but they say things like we need into an AI with hard constraints or with safety guarantees.
[00:08:57] SPEAKER_02: And still, there's still can be some belief that some hybrid approach is the way to go,
[00:09:05] SPEAKER_02: where you want to try and take a rules-based stack and an end-to-end lens stack,
[00:09:09] SPEAKER_02: but often these approaches can get the worst of both worlds or just ag costs and complexity.
[00:09:15] SPEAKER_02: I still think there is a distribution in the market of those that are leaning and moving
[00:09:18] SPEAKER_02: fast and those that are perhaps have some catching up to do.
[00:09:24] SPEAKER_02: But of course, crediting the breakthrough that all of us that have been working in deep learning
[00:09:30] SPEAKER_02: that really made this world-changing and mainstream, of course, we've got to credit the
[00:09:33] SPEAKER_02: large language model breakthroughs. I think they've inspired the world and opened up the markets
[00:09:38] SPEAKER_02: mind to be curious about the technology. But also what we've been doing at Wave,
[00:09:45] SPEAKER_02: a year ago, we were just driving in Central London. Central London, I think, is a great
[00:09:49] SPEAKER_02: proving ground because it's this unstructured, incredibly complex and dynamic city
[00:09:55] SPEAKER_02: that our AI has learned to navigate around very smoothly, safely and reliably.
[00:10:01] SPEAKER_02: But in the last year, we've taken it to highways, to Europe, Japan, North America,
[00:10:05] SPEAKER_02: our cars were in New York City last week driving around there. And so bringing a global,
[00:10:10] SPEAKER_02: being able to take it to different manufacturers' vehicles and show a product-like experience.
[00:10:17] SPEAKER_02: This growth is, I think, also really opened up a lot of inspiration around the world.
[00:10:23] Why is it that you're able to launch in hundreds of cities worldwide?
[00:10:27] And some of the AV-1.0 companies need to actually go out and build an HD map.
[00:10:32] SPEAKER_00: Just say we're on the difference in how technical differences are actually leading to
[00:10:39] differences in how the machine is able to learn and how you're able to roll out.
[00:10:42] SPEAKER_00: Autonomous driving is all about generalization. Generalization means being able to
[00:10:47] reason about or understand something you've never seen before. Every time you go for a drive,
[00:10:52] SPEAKER_02: you're going to see something new for the first time. What did we see today? We saw a road worker
[00:10:58] SPEAKER_02: rolling out some carpet thing in front of the road, but on a pedestrian crossing, but not
[00:11:03] SPEAKER_02: wanting to step out. And we had to reason about, could we pass them without yielding, for example.
[00:11:08] SPEAKER_02: There's just an example from earlier today, but you could think about all the new things you see
[00:11:13] SPEAKER_02: on the roads every time you drive. You're never going to see every experience in your training data.
[00:11:18] SPEAKER_02: So that means that you have to be able to reason and generalize to things you haven't seen before
[00:11:22] SPEAKER_02: to be safe, to be useful around the world. And that's what has motivated our entire approach.
[00:11:29] SPEAKER_02: So whether it's us, a manufacturer giving us one of their vehicles and within a couple of months,
[00:11:33] SPEAKER_02: us being able to drive it on the road, a couple of weeks ago, in September this year, we
[00:11:41] SPEAKER_02: unveiled a vehicle to media with Nissan in Tokyo. Just four months earlier, was the first time we'd
[00:11:48] SPEAKER_02: even driven in Tokyo and got hands on this vehicle. Four months later, we were having media
[00:11:52] SPEAKER_02: driving the car, experience it, and that was a new country and a new vehicle for us.
[00:11:58] SPEAKER_02: So what that showed is that our AI was able to generalize. It's trained on very diverse data
[00:12:02] SPEAKER_02: from around the world. It's trained on diverse sensor sets, vehicles. And so it was able to understand
[00:12:07] SPEAKER_02: that that vehicle is a new sensor distribution and of course the complexity of driving around
[00:12:11] SPEAKER_02: in central Tokyo. So I think that's a really great demonstration of generalization. And if we think
[00:12:17] SPEAKER_02: about, you know, if you're building a vertically integrated robotic solution, maybe you can go deep,
[00:12:21] SPEAKER_02: but our ambition is to be the embodied AI foundation model for all of the best fleets and
[00:12:27] SPEAKER_02: manufacturers around the world. And to do that, unless we want to overload the company by building
[00:12:33] SPEAKER_02: a separate neural network for each application, we need to be able to generalize. We need to
[00:12:36] SPEAKER_02: about it, amortize our cost over one large intelligence and about a very quickly adapt to each
[00:12:42] SPEAKER_02: different application that our customers care about. That's what we're trying to push.
[00:12:46] SPEAKER_02: You mentioned reasoning in there in terms of how the model is reasoning through, you know,
[00:12:51] SPEAKER_00: there's construction work for what do I do now? In the LLM world, obviously reasoning is its own
[00:12:57] separate track of lots of scaling and Princeton computer techniques. Are you deliberately training
[00:13:03] SPEAKER_00: your models to reason? Is it an emergent property, emergent behavior of the models, like say more about
[00:13:07] SPEAKER_00: even that reasoning? We are. And I think reasoning in the physical world can be really well expressed as
[00:13:14] SPEAKER_02: a world model. In 2018, we put our very first world model approach on the road. It was a very small
[00:13:23] SPEAKER_02: 100,000 parameter neural network that could simulate a 30 by three pixel image of a road in front of us.
[00:13:31] SPEAKER_02: But we were able to use it as an internal simulator to train a model-based reinforcement learning algorithm.
[00:13:36] SPEAKER_02: There's a fun blog post, if you want to see the history on that. But fast forward to today,
[00:13:42] SPEAKER_02: and we've developed a Gaia. It's a full generative world model that's able to simulate
[00:13:48] SPEAKER_02: multiple camera and sensors in very rich and diverse environments. You can control it and prompt
[00:13:53] SPEAKER_02: the different agents or seen in it. And that's an example of reasoning where we can train in the
[00:13:59] SPEAKER_02: ability to simulate how the world works and what's going to happen next. What happens when you
[00:14:04] bring this kind of representation on the road is you get some really nice emergent behavior. Like
[00:14:09] SPEAKER_02: today, when we saw we were driving around unprotected turns that were included, you saw the car
[00:14:13] SPEAKER_02: nudge forward until it could see for itself and then completed the turn. Or when it's foggy and
[00:14:19] SPEAKER_02: London, you see the car slow down and drive to what it can reason about. And by training it with
[00:14:25] SPEAKER_02: that level of understanding, it gives that level of emergent behavior that helps it really understand
[00:14:32] SPEAKER_02: particularly complex multi-agent scenarios. I think that's key for getting
[00:14:37] SPEAKER_02: safe and smooth autonomous driving. So the world models are really key to teaching the model how
[00:14:42] SPEAKER_00: the reason through their new scenarios. 100%. You mentioned earlier the diversity of your data.
[00:14:47] SPEAKER_01: Say, word about world data comes from. It's becoming like an enormous amount of data because,
[00:14:53] SPEAKER_02: of course, unlike the language domain or image domain when we're dealing with
[00:14:59] SPEAKER_02: a typical self-driving car that has a dozen multiple megapixel cameras, radar, maybe a
[00:15:06] SPEAKER_02: lighter, you know, you're dealing with when you aggregate that up, it's very quickly tens or
[00:15:11] SPEAKER_02: hundreds of petabytes of data. So it's an enormous amount of data you have to train on. But it's
[00:15:17] SPEAKER_02: the diversity that's really key. And we've solved for diversity in two ways. The first one is by
[00:15:21] SPEAKER_02: becoming a trusted partner across the industry and aggregating data across many different sources
[00:15:27] SPEAKER_02: from dash cams to fleets to manufacturers to robot operators. The second one is being able to
[00:15:33] SPEAKER_02: filter and really understand the data. Here we've really worked hard to develop different
[00:15:41] SPEAKER_02: unsupervised learning techniques to be able to cluster and find unusual anomaly experiences.
[00:15:48] SPEAKER_02: And of course, find the scenarios that our system is performing poorly at and then drive the
[00:15:53] SPEAKER_02: learning curriculum on those. But yeah, today we learn from a diverse set of vehicles,
[00:16:00] SPEAKER_02: diverse set of sensor architectures of countries. And that's really one of the key things that
[00:16:04] SPEAKER_02: drives the level of generalization. Does the increased growth of world models and
[00:16:10] SPEAKER_00: similar data, does that mean that you just don't need as many actual on-road miles?
[00:16:16] I think there's two sides to that question, right? On the one side, yes,
[00:16:21] SPEAKER_02: learning efficiency really matters. But second, you can't only rely on learning efficiency.
[00:16:27] SPEAKER_02: At the limit, if we take our current approach and just scale it up, I'm sure it'll produce
[00:16:31] SPEAKER_02: generic level 5 driving. At the limit, if you have unlimited training data, this is really just
[00:16:37] SPEAKER_02: a lookup data table with some prior experience. But that's not economically or technically feasible.
[00:16:43] SPEAKER_02: And so the question is, how can you train this to be the most efficient data efficient system?
[00:16:48] SPEAKER_02: Because I think efficiency will lead to not just improved cost, but faster time to market and more
[00:16:53] SPEAKER_02: intelligence. So efficiency comes from a number of different factors. There's most importantly,
[00:17:01] SPEAKER_02: how the data curriculum you put in place. But then the learning algorithms, how do you magnify
[00:17:06] SPEAKER_02: the learning you have? And I think world models are a really great opportunity for that. They generate
[00:17:10] SPEAKER_02: synthetic data and synthetic understanding that doesn't replace real world data, but it
[00:17:14] SPEAKER_02: recombines it and magnifies it in new ways. It lets you pull in interesting insights. And I think
[00:17:20] SPEAKER_02: these kind of approaches can really, really improve data efficiency. But across the board, I think
[00:17:26] SPEAKER_02: working under resource constraints as a forced out team to develop so many innovations,
[00:17:32] SPEAKER_02: I'd also call out just the workflow. Because in traditional robotics, when you're
[00:17:38] SPEAKER_02: tuning parameters or algorithms or designing geometric maps and things like this,
[00:17:43] SPEAKER_02: there's very well established cultures and workflows. But our team, when we have 50 model
[00:17:48] SPEAKER_02: developers working on one main production model, or when we have an end-to-end net that we need to
[00:17:55] SPEAKER_02: understand and interest back to, or even the way that we deploy these systems to simulation or to
[00:17:58] SPEAKER_02: the road and feedback, we've developed the entire culture from the ground up way that's been developed
[00:18:04] SPEAKER_02: for embodied AI for end-to-end deep learning for driving. The data infrastructure, the simulation,
[00:18:09] SPEAKER_02: the safety licensing before we put systems on the road, this is not being a hedge or a
[00:18:15] SPEAKER_02: side-bet for us, but this is the entire essence of our culture. And I think doing this under
[00:18:21] SPEAKER_02: resource constraints and doing this with full mission-driven conviction has led to a bunch of
[00:18:26] SPEAKER_02: interesting innovations that look getting to where we are today, everything is about iteration speed.
[00:18:31] SPEAKER_02: Speaking of your culture, I'm picturing a bunch of AI research types, machine learning
[00:18:39] SPEAKER_01: engineers, that sort of thing. How does the culture of your organization differ from similar
[00:18:46] SPEAKER_01: applied lab type environments, given the customer base that you serve, given that you're going
[00:18:51] SPEAKER_01: after the automotive industry specifically with all of its quirks around supply chain and all of
[00:18:57] SPEAKER_01: its requirements around safety? And so how does that influence the culture of your business?
[00:19:03] Hugely. In fact, for the first few years of wave, we were really a group of passionate
[00:19:10] SPEAKER_02: embodied AI researchers, but in the last couple of years, I'm really, really proud of how our
[00:19:16] SPEAKER_02: team has built out deep expertise in understanding the automotive industry, but also the ability to
[00:19:22] SPEAKER_02: reliably deliver to our partners there. And that's a different culture. It's a culture of really
[00:19:28] SPEAKER_02: growing to respect because when you're building millions of cars, the level of reliability and
[00:19:34] SPEAKER_02: MTT if you need there is extraordinary. What have you all learned from them? I mean, I'm sure
[00:19:41] SPEAKER_01: part of your job is to teach them about what's going on in the world of AI. What have you learned
[00:19:45] SPEAKER_01: from them? I think some of the main things I'll call out have been efficiency and reliability,
[00:19:52] SPEAKER_02: the difference between technology and a product will be some of the main themes. I mean, the
[00:19:57] SPEAKER_02: the level of reliability required, but also the level of quality that is seen to really robustly
[00:20:06] SPEAKER_02: prove these systems out before deployment and the pride that these companies take in that has
[00:20:11] SPEAKER_02: been exceptional. Another thing has been perhaps the sense of brand differentiation and the desire for
[00:20:18] SPEAKER_02: do you want your car to drive? How can your driving personality really match the brand's preferences?
[00:20:26] SPEAKER_02: How can you provide that experience that really gives brand differentiation? And the great
[00:20:31] SPEAKER_02: news is that I think we've been able to riff and brainstorm off these and come up with some really
[00:20:35] SPEAKER_02: neat technical ideas down that vein. But ultimately, safe, high quality and personalizable AI
[00:20:47] SPEAKER_02: has been some great feedback we've got from the industry. Can you talk about your path to market
[00:20:52] SPEAKER_00: in partnering with the other OEMs? How do you decide to do that? And then how do you think
[00:20:56] SPEAKER_00: the market landscape will play out for how autonomy rules out? Of course, great questions
[00:21:01] SPEAKER_02: on you because since the beginning of Wave, we've been focused on the pitch I gave around
[00:21:07] SPEAKER_02: into and deep learning, being an approach autonomy. But we've tried a number of different
[00:21:11] SPEAKER_02: go-to-market approaches over the years. But in the last couple of years, I've been hugely energized
[00:21:17] SPEAKER_02: about working and partnering with the biggest and best consumer automotive manufacturers around
[00:21:24] SPEAKER_02: the world. Why is that? Well, I mentioned how they've begun to introduce software-defined vehicles,
[00:21:29] SPEAKER_02: so they have the infrastructure to work with autonomy. There's the market belief that this is
[00:21:34] SPEAKER_02: a technology that can really thrive. And also, it's the chance to get to scale far beyond what we're
[00:21:40] SPEAKER_02: seeing with the city by city robot taxis we're seeing right now. But moreover, these are OEMs that
[00:21:48] SPEAKER_02: invest in the right infrastructure to go from not just driver assistance, but to
[00:21:53] SPEAKER_02: eyes off autonomy where you can actually take liability for the drive and give the user a safe
[00:21:59] SPEAKER_02: and give them time back from their driving experience. So that's awesome. I think when you think
[00:22:04] SPEAKER_02: about the market, there are 90 million cars built each year. And so some manufacturers that are
[00:22:11] SPEAKER_02: building the autonomy systems themselves like Tesla built a couple of million, but the vast majority
[00:22:15] SPEAKER_02: of the market, I think there's an opportunity partner to work with some of these innovative
[00:22:19] SPEAKER_02: platforms and to bring our AI to market to make these autonomous products possible. And it will
[00:22:24] SPEAKER_02: only grow from there. These manufacturers don't want to stop a driver assistance. We're working
[00:22:28] SPEAKER_02: together to build eyes off and driverless robot taxi products. But the key thing is that by avoiding
[00:22:34] SPEAKER_02: retrofitting our own hardware on these vehicles, by putting them in natively as a software integration,
[00:22:40] SPEAKER_02: we can move fast at scale, we can build low-cost vehicles that can be homologated all around the
[00:22:44] SPEAKER_02: world. And this is going to be the path to see tens and hundreds of thousands of robot
[00:22:49] SPEAKER_02: taxis rolled out around the world at an affordable price. And of course, this is all possible because
[00:22:55] SPEAKER_02: of the level of generalization that this AI enables. Tesla FSD is just such a game-changing product.
[00:23:02] SPEAKER_00: And you know, my friends have it. It's just they can't imagine driving any other way. And so
[00:23:06] SPEAKER_00: it's really cool that you're going to empower the 88 million other vehicle sold every year to
[00:23:12] SPEAKER_00: be able to sell that experience as well. 100%. It's one of those things that a lot of people
[00:23:17] SPEAKER_02: jump in our car and come for a drive with some being skeptical about autonomy. But without
[00:23:22] SPEAKER_02: exception, they step out with a smile on their face. It's a magical experience. And yeah, I can't
[00:23:28] SPEAKER_02: wait for people to try it around the world and make autonomy. Not just a robot taxi tourism
[00:23:33] SPEAKER_02: experience, but bring this experience to people in, yeah, eventually every city.
[00:23:39] What do you make of the sensor fusion, confusion, debate? You know, the one that plays it on
[00:23:44] SPEAKER_00: Twitter every year or so of Tesla gets confused if there's both camera and and light are coming in.
[00:23:51] SPEAKER_00: Sorry, radar. I think it's the wrong debate to be having. It's not the frontier question.
[00:23:56] SPEAKER_02: The industry is really, he's outside of Tesla. It's really coalesced around a common architecture
[00:24:02] SPEAKER_02: of a surround camera, surround radar, and a front-facing light-air stack. Now, this costs under
[00:24:07] SPEAKER_02: $2,000. So it's automotive grade components, not the retrofit robot taxi components you see today.
[00:24:13] SPEAKER_02: But having a front-air GPU, automotive grade GPU on the car and that kind of sensor architecture
[00:24:20] SPEAKER_02: is a really great platform to build L3L4 autonomy, eyes off or driverless. It gives you the necessary
[00:24:26] SPEAKER_02: redundancy. It lets you deal with edge cases that cameras alone, I agree they can get you to
[00:24:31] SPEAKER_02: human level, but we want to go beyond human level. And so I think this kind of architecture is
[00:24:36] SPEAKER_02: affordable, scalable. It's got the supply chain for mass manufacturer and it can eliminate, I think,
[00:24:45] SPEAKER_02: eliminate all accidents and really drive superhuman levels of performance.
[00:24:50] SPEAKER_02: So that's what we're seeing. Many manufacturers bring out on their vehicles and we're integrating
[00:24:55] SPEAKER_02: our AI. Of course, for a driver assistance system, camera only can work for a human level driverless
[00:25:01] SPEAKER_02: system or of course, I should clarify, 90 something you can look at different stats, but 95%
[00:25:08] SPEAKER_02: or above accidents unfortunately are caused by human error. So not only can you be human level,
[00:25:13] SPEAKER_02: but you can eliminate a lot of human attention and accidents caused by that. But there are still
[00:25:19] SPEAKER_02: accidents that to be able to solve would require perception capabilities that could be on vision.
[00:25:25] SPEAKER_02: And if we want to tackle that long tail, there are many ways to solve it. One of the ways would be
[00:25:29] SPEAKER_02: to bring in some other sensing modalities like radar and light hours. So we're excited to be working
[00:25:34] SPEAKER_02: with those kind of platforms, but crucially, natively integrated into the OEMs vehicles themselves.
[00:25:41] SPEAKER_02: Is it the same neural net that can drive on one OEM's car and another's car? How does that even work?
[00:25:47] SPEAKER_00: Because I imagine each vehicle has slightly different position cameras, things like that.
[00:25:52] It comes from the same family. So we train a very large scale, we regularly train very large
[00:25:57] SPEAKER_02: scale models. Of course, we iterate them on the month to month, but that's one model that's common
[00:26:04] SPEAKER_02: to all of the fleets that we work with. But as you optimize to a specific sensor set or a specific
[00:26:10] SPEAKER_02: embedded target, of course, you can start to specialise the model. But the beauty is that 99%
[00:26:16] SPEAKER_02: plus of the cost and the time and the effort is training their base model. And then we can build
[00:26:20] SPEAKER_02: very efficient personalization to the specific customer. And so this lets this scale, but gives us
[00:26:27] SPEAKER_02: the ability to squeeze it to very efficient real-time platforms and make it adapted to a specific
[00:26:35] SPEAKER_02: use case. Are you going to let Pat personalize a super aggressive driver model?
[00:26:39] SPEAKER_00: And they need to. What driving style would you like Pat?
[00:26:42] SPEAKER_02: But yeah, pretty aggressive.
[00:26:45] Safe, very safe. We can do that. We find, it's really funny when you build distributions around
[00:26:52] SPEAKER_02: driving behaviour. Yeah, you can really tell from the human training data we have, you can really
[00:26:58] SPEAKER_02: tell when it goes from being helpfully assertive, let's say, to unhelpfully aggressive. And we can
[00:27:04] SPEAKER_02: draw a clean line there. What about you, Sonia? How was the drive we just had?
[00:27:08] SPEAKER_02: Fantastic. It was comfortable. It was safe. It felt very human actually. The way it was kind of
[00:27:14] SPEAKER_00: nudging up when it couldn't see on the tour, and it was very human.
[00:27:17] SPEAKER_00: Yeah, well, it's as complex as we can get in Silicon Valley, but come to Tokyo or London or
[00:27:24] SPEAKER_02: was in the weekend in downtown San Francisco. And yeah, you really need the ability to predict and
[00:27:31] SPEAKER_02: reason about other folks around you to be able to drive in a human-like way. And what we find is
[00:27:36] SPEAKER_02: that if you're not able to smoothly go around double parked vehicles or deal with other dynamic
[00:27:43] SPEAKER_02: obstacles or even the prevailing road traffic might not be aligned to the specific lane, but maybe
[00:27:47] SPEAKER_02: there's a human-like way of driving. Then what's awesome about the intelligence that we've built is
[00:27:54] SPEAKER_02: it's able to reason about these things and keep the traffic flowing, keep interacting with road
[00:27:58] SPEAKER_02: users in a very human-like way. I think this is going to be key for societies to accept and love
[00:28:02] SPEAKER_02: for robot taxis. I can't wait to make that a reality. Are there any specific corner cases that you
[00:28:07] SPEAKER_01: across have a hard time with today? There are loads and it's really hard to generically talk about
[00:28:15] SPEAKER_02: one because they're so rare. It's very hard to say, Alex, always these types because it's always
[00:28:23] SPEAKER_02: a corner case is a couple of edge cases coming together in a corner and it's always confounding
[00:28:27] SPEAKER_02: factors when you get something really obscure. But we're driving, we've driven in over 500 cities
[00:28:33] SPEAKER_02: this year and so when you're driving at that level of scale, of course you see things that you've
[00:28:37] SPEAKER_02: never seen before. Road signs are written in a new language. Actually, maybe one way to break it down
[00:28:42] SPEAKER_02: is often we talk about driving broken down into safety, utility and flow, safety being, of course,
[00:28:48] SPEAKER_02: safety critical behavior, flow being the style of driving, is it smooth, is it enjoyable,
[00:28:53] SPEAKER_02: and then utility being the navigation and road semantics. Safety and flow we've found
[00:28:58] SPEAKER_02: generalize exceptionally well throughout the world. We get almost uniform metrics in every country
[00:29:02] SPEAKER_02: we operate in in terms of safety and flow or comfort of the drive. But utility has been the
[00:29:09] SPEAKER_02: really interesting one. As we've gone global, how do you navigate, how do you deal with road signs,
[00:29:13] SPEAKER_02: how do you read different languages, how do you deal with different driving cultures,
[00:29:17] SPEAKER_02: and so that's the one that's been interesting. But we published some results about this when we
[00:29:24] SPEAKER_02: went from the UK to the US. We needed hundreds of hours of data to be able to drive within
[00:29:31] SPEAKER_02: 10% of our frontier performance. But then when we went to Europe and to Germany, of course,
[00:29:38] SPEAKER_02: we'd already learn to drive on the right side of the road, coming to the US would learn to do
[00:29:42] SPEAKER_02: right turns of red lights. We then came into Germany. We had to learn to still drive on the right
[00:29:46] SPEAKER_02: side of the road, but of course you can't turn right at a red light there. But then on the auto
[00:29:50] SPEAKER_02: you'd like this unique to drive. We drive today up to 140. So pretty fast there. But
[00:29:57] SPEAKER_02: yeah, it gets more efficient each time with exponentially less data in each new market because
[00:30:02] SPEAKER_02: you've seen some of those things before. Yeah. You mentioned at the beginning that large
[00:30:06] SPEAKER_00: language models were part of what flipped your approach from from contrarian to consensus.
[00:30:12] SPEAKER_00: Are you integrating large language models at all into your models? And I know some of the robotics
[00:30:17] SPEAKER_00: companies they're getting started now are starting from this VLA VLM base. Is that part of your
[00:30:21] SPEAKER_00: architecture? 100% in 2021 we started working on language for driving. I remember my team
[00:30:28] SPEAKER_02: counted to me at the time and said, hey, we should start a project on language. I said, no, no,
[00:30:32] SPEAKER_02: no guys, start up sort of that focus, keep keep focus. But they actually gave some pretty
[00:30:36] SPEAKER_02: compelling arguments. So we started to play around with these things and a year or so later we
[00:30:41] SPEAKER_02: released a lingo, which is the first vision language action model in autonomous driving.
[00:30:48] SPEAKER_02: And what was special about this model was it could not only drive a car, see the world driver
[00:30:53] SPEAKER_02: car, but also converse and language. And it'll let you talk to it and ask questions, what are
[00:30:57] SPEAKER_02: you finding this risky? What's going to happen next? Or even a comment at your drive? And what's
[00:31:03] SPEAKER_02: interesting about this is that so there's a few benefits. One is bringing language into pre-training.
[00:31:07] SPEAKER_02: Of course, just improves the representations. Power gives you know more interesting information
[00:31:13] SPEAKER_02: to learn from than than just imagery alone. But then second, aligning the representation with
[00:31:18] SPEAKER_02: language opens up a ton of interesting product features. It enables a you know, you to create a
[00:31:24] SPEAKER_02: chauffeur experience where you could actually talk to your driver. You know, no longer do you need a
[00:31:28] SPEAKER_02: PhD in robotics to understand the system, but actually you can just talk to us and like ask
[00:31:33] SPEAKER_02: it to drive Pat if you want to race around the commute super fast, then you can you can demand that.
[00:31:40] SPEAKER_02: But then third, it gives you a really nice introspection tool where you can start to actually
[00:31:44] SPEAKER_02: you know, you could imagine regulators or our engineering team conversal the system in language
[00:31:48] SPEAKER_02: to really diagnose why it's doing what it's doing or get it to explain its reasoning. So I think
[00:31:53] SPEAKER_02: these these are really clear benefits, which which we're really excited to be pushing.
[00:31:56] SPEAKER_02: That's super cool. And you're running it on the embedded compute.
[00:32:00] We are. So we've put out demos that run offboard. Onboard's challenging with what's in the
[00:32:05] SPEAKER_02: automotive market today, but some of the next generation compute, for example, the Nvidia
[00:32:09] SPEAKER_02: Thor that our next year in development vehicle is going to be with will be large enough to run it
[00:32:13] SPEAKER_02: on board. That's going to be cool. Very cool. You you've talked about how autonomous driving sort of
[00:32:19] SPEAKER_01: provides a path to more generalized in body day. I can you paint that picture for us? How you go
[00:32:24] SPEAKER_01: from autonomous driving to humanoid robots or whatever other things you might want to
[00:32:31] SPEAKER_01: in by the AI? I think we're going to be in the future looking at a ton of interesting use cases
[00:32:37] SPEAKER_02: for robotics. What we're seeing is that mobility is becoming possible, I think, much before
[00:32:44] SPEAKER_02: manipulation. Manipulation is challenging in terms of access to data, global supply chains
[00:32:51] SPEAKER_02: for hardware and actually even the hardware designs themselves. I think tactile sensing is still
[00:32:57] SPEAKER_02: a really hard challenge. But inevitably, it'll be a massive transformative thing. But maybe,
[00:33:04] SPEAKER_02: maybe is it the maturity of where self-driving was in 2015? But today, our system is rapidly
[00:33:09] SPEAKER_02: becoming a general purpose navigation agent, giving it an arbitrary sense of view and a goal
[00:33:14] SPEAKER_02: condition that's able to produce a safe trajectory. So I think we're going to see a rapid
[00:33:20] SPEAKER_02: advancement from not just consumer automotive, robot taxis, talking about trucking and other
[00:33:25] SPEAKER_02: applications. But this AI will enable manufacturers and fleets who want to build robots in any kind
[00:33:31] SPEAKER_02: of mobility application. And of course, we'll we're really excited to be working with
[00:33:37] SPEAKER_02: frontier developers and applications over time as you as you go out across that robotic stack.
[00:33:42] SPEAKER_02: And I expect we'll see more maturity in the coming years from manufacturing and manipulation
[00:33:47] SPEAKER_02: use cases as well. But in the end, I think the benefits of having a large foundation model that
[00:33:54] SPEAKER_02: certainly in automotive, we can, I think we have access to the largest robot and data supply chain.
[00:34:01] SPEAKER_02: And so we're really lucky in that regard to about a push for the intelligence there. But
[00:34:05] SPEAKER_02: generalizing the intelligence and new applications, I think there'll be benefits from the model being
[00:34:09] SPEAKER_02: able to experience multiple different verticals and it'll only make it more more general purpose.
[00:34:13] SPEAKER_02: Any applications you're excited about?
[00:34:16] SPEAKER_02: I mean, I'm psyched to have humanoid robots walking around.
[00:34:19] SPEAKER_01: Yeah, me too. I think they're going to be neat, whichever form factor, I think humanoid will play a big
[00:34:26] SPEAKER_02: part. I think other forms of locomotion as well. And then manipulation, there's some really
[00:34:31] SPEAKER_02: interesting challenges in those space. But I think the same story is going to play out.
[00:34:36] SPEAKER_02: You know, a working on a narrow application, you know, like when self-driving,
[00:34:42] SPEAKER_02: when to Phoenix, Arizona and put in a ton of infrastructure and expensive hardware to make it
[00:34:46] SPEAKER_02: a work is going to, I think, a limited runway. But working on general purpose, lean,
[00:34:51] SPEAKER_02: low-cost hardware stacks that really focus on making the system most intelligent and robust.
[00:34:58] SPEAKER_02: I think this is the recipe for scale. So yeah, let's watch that space.
[00:35:02] SPEAKER_02: Yeah.
[00:35:03] Do you think there are major research breakthroughs needed to reach kind of physical AGI,
[00:35:08] SPEAKER_00: so to speak? And if so, what do you think is the most promising direction?
[00:35:13] SPEAKER_00: Absolutely, I do. I think there's so much more ground to scale up the current approaches,
[00:35:18] SPEAKER_02: and we'll do that. But I think we'll get compounding returns from, I usually talk about four
[00:35:26] SPEAKER_02: factors that drive performance. There's of course data and compute. But then also the algorithmic
[00:35:32] SPEAKER_02: capabilities and the embodiment, the what is the hardware and capability on the robots. And I think
[00:35:37] SPEAKER_02: we need to push all four. And on the algorithmic side, there are so many opportunities for growth.
[00:35:42] SPEAKER_02: I think a key one is measurement. How do you actually measure and quantify these systems? How do
[00:35:49] SPEAKER_02: you respond quickly? Find regressions? Be able to really have a simulator that closes the
[00:35:57] SPEAKER_02: the real-world gap at scale and can run efficiently. I mean, there's no secret that these
[00:36:02] SPEAKER_02: generative world models are very compute-intensive. But having a good measurement system will just
[00:36:08] SPEAKER_02: drive efficiency and iteration speed. So that's a key one. People often talk about being a chicken
[00:36:13] SPEAKER_02: and egg. If you have a perfect simulator, you've solved self-driving and vice versa. And I
[00:36:16] SPEAKER_02: really believe that. I think AlphaGo showed that when you have a perfect simulator, you can just
[00:36:22] SPEAKER_02: solve problems through Monte Carlo tree search. And so I think that's going to be the case in robotics as
[00:36:28] SPEAKER_02: well. So one is measurement. Another pillar is building more generality into the model. How can
[00:36:36] SPEAKER_02: you build out more modalities and align those different modalities in their reasoning? I think this
[00:36:42] SPEAKER_02: is going to open up new use cases, particularly when it comes to human-robot interaction and
[00:36:47] SPEAKER_02: navigation. I was going back to the utility problem before. Some of these things I'm super excited
[00:36:54] SPEAKER_02: about. And then the last one is just engineering efficiency. I mean, training these systems and the
[00:37:00] SPEAKER_02: data requirements is extraordinary. And so I wouldn't understate, I think the most sexy part of this
[00:37:06] SPEAKER_02: problem is the efficient infrastructure to train and serve these models. And getting that right,
[00:37:15] SPEAKER_02: yeah, I think it's a real competitive advantage or disadvantage. We started by talking about
[00:37:20] SPEAKER_01: AV2.0. Someday, I imagine we might be talking about AV3.0. What could AV3.0 look like? If you go 5, 10,
[00:37:29] SPEAKER_01: 15 years in the future, are there any other big leaps in this industry that you think we'll see?
[00:37:34] You said that with such deadpan. AV, so the whole premise of AV2.0 was all about
[00:37:43] SPEAKER_02: putting the intelligence on the car and not needing infrastructure and a ton of,
[00:37:48] SPEAKER_02: you know, ton of overcooked hardware, but really making the system intelligent.
[00:37:52] And so I think we're seeing that emerge now with this system that can generalize the world with all
[00:37:57] SPEAKER_02: of the on board scalable intelligence and compute. If I were to speculate where AV3.0.0. We haven't
[00:38:05] SPEAKER_02: thought about it lately but one idea could be taking the intelligence outside the car. So
[00:38:11] SPEAKER_02: I mean, when you start to have majority prevailing autonomous vehicles, you could imagine a ton
[00:38:17] SPEAKER_02: of new things you could do when they start to communicate, when they start to interact with each other.
[00:38:22] SPEAKER_02: Why do we need traffic lights in the future if they can coordinate? Why do we need all these
[00:38:27] SPEAKER_02: senses if you can actually just communicate with the AV in front of you to be able to see
[00:38:31] SPEAKER_02: around corners.
[00:38:32] SPEAKER_02: I mean, of course I'm speculating here.
[00:38:34] SPEAKER_02: It opens up tons of interesting cyber security questions, communication, latency questions,
[00:38:39] SPEAKER_02: things like that.
[00:38:40] SPEAKER_02: But I don't know, I'm all up for embodied AI and if we can build a safer and more accessible
[00:38:47] SPEAKER_02: system by taking the intelligence, not only in the car, but beyond maybe that's a path,
[00:38:53] SPEAKER_02: let's see.
[00:38:54] SPEAKER_01: That's really interesting.
[00:38:55] SPEAKER_01: If AV 3.0 is the point at which it's sort of a mesh network and you know, at that point
[00:39:00] SPEAKER_01: maybe humans aren't allowed to drive because they can't communicate with the mesh network
[00:39:04] SPEAKER_01: the same way that the robots can and or maybe there are special places that humans go to
[00:39:08] SPEAKER_01: drive just for recreational purposes, but always try to take it.
[00:39:12] SPEAKER_01: You know, it's all autonomous.
[00:39:14] Yeah, interesting.
[00:39:15] SPEAKER_01: How do you hire and how do you attract people with how hot the AI market is these days?
[00:39:19] SPEAKER_00: I love that question because you know, the end of the day our team is our product, our
[00:39:24] SPEAKER_02: team are the most important thing to making this possible and we talk a lot about it
[00:39:29] SPEAKER_02: wave about being a place where you can do the best work of your career and what that
[00:39:33] SPEAKER_02: means for me in embodied AI is having a set of colleagues around you that inspire and
[00:39:39] SPEAKER_02: excite world class and what they do, having the right resources, the right culture, I'm
[00:39:43] SPEAKER_02: going to block you, but I think uniquely at wave, we are able to bring together really
[00:39:49] SPEAKER_02: a frontier AI environment with a near-term product opportunity and automotive.
[00:39:55] SPEAKER_02: So if you want to work on intelligent machines and see your system brought out with the scale
[00:40:00] SPEAKER_02: of impact of chat GPT in robotics, I think that's this is a place where we can do it.
[00:40:06] SPEAKER_02: The other thing is that we've gone global.
[00:40:08] SPEAKER_02: I mean, we have teams in London, Stuttgart, Tel Aviv, Vancouver, Tokyo, Silicon Valley,
[00:40:16] SPEAKER_02: and wherever there's an almost some of the major AI and automotive hubs and we're really
[00:40:24] SPEAKER_02: looking to build a global culture that can bring this product to the world, work with
[00:40:28] SPEAKER_02: customers around the world and most importantly collaborate with the very best people.
[00:40:35] SPEAKER_02: Yeah, so anyone who's interested in pioneering a body day, I'm pushing the frontiers and actually
[00:40:40] SPEAKER_02: turning it into a game-changing product, come chat, we'd love to speak.
[00:40:45] Wonderful.
[00:40:46] Alex, you've believed in the future for N2N neural nets and self-driving and in the physical
[00:40:52] SPEAKER_00: economy for longer than just about anybody and it must be incredibly fulfilling to see
[00:40:58] SPEAKER_00: that vision start to come to life.
[00:41:00] SPEAKER_00: Congratulations and thank you for joining us.
[00:41:02] SPEAKER_00: Thank you, Sonya.
[00:41:03] SPEAKER_02: Thank you, Pat.