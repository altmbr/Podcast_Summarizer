# How End-to-End Learning Created Autonomous Driving 2.0: Wayve CEO Alex Kendall

**Podcast:** Training Data
**Date:** 2025-11-18
**Video ID:** 8x_O8BeGNTw
**Video URL:** https://www.youtube.com/watch?v=8x_O8BeGNTw

---

[00:00:00] If you're building a vertically integrated robotic solution,
[00:00:02] Alex Kendall: maybe you can go deep, but our ambition is to be the
[00:00:05] Alex Kendall: embodied AI foundation model for all of the best
[00:00:08] Alex Kendall: fleets and manufacturers around the world.
[00:00:10] Alex Kendall: And to do that, unless we want to overload the company by building
[00:00:15] Alex Kendall: a separate neural network for each application,
[00:00:17] Alex Kendall: we need to be out of generalize.
[00:00:18] Alex Kendall: We need to be able to amortize our cost over one large
[00:00:21] Alex Kendall: intelligence and to be able to very quickly adapt to each
[00:00:24] Alex Kendall: different application that our customers care about.
[00:00:27] Alex Kendall: That's what we're trying to push.
[00:00:28] Alex Kendall: [♪ OUTRO MUSIC PLAYING [♪ OUTRO MUSIC [♪
[00:00:42] [♪ OUTRO MUSIC PLAYING [♪
[00:00:45] Pat Grady: Today we're talking with Alex Kendall, CEO of Wave,
[00:00:48] Pat Grady: about the shift from software 1.0 to 2.0,
[00:00:51] Pat Grady: or from classical machine learning to end-to-end neural
[00:00:53] Pat Grady: networks in autonomous driving.
[00:00:55] Pat Grady: Wave sells an autonomous driving stack to auto OEMs,
[00:00:58] Pat Grady: similar to Tesla FSD, but for non-test-law automobiles.
[00:01:01] Pat Grady: Major car manufacturers globally like Nissan are choosing
[00:01:04] Pat Grady: Wave to power their AV stacks.
[00:01:06] Pat Grady: Alex started Wave back in 2017 when most self-driving software
[00:01:09] Pat Grady: stacks were massive hand-coded C++ code
[00:01:11] Pat Grady: bases covering every possible edge case like navigating
[00:01:14] Pat Grady: around double parked cars.
[00:01:16] Alex bet the farm from the beginning on an end-to-end
[00:01:18] Pat Grady: neural net approach to self-driving and on the use of synthetic
[00:01:21] Pat Grady: data and world models as the ultimate path to generalization
[00:01:24] Pat Grady: and scaling.
[00:01:25] Pat Grady: Today, the architecture is reshaping AV and all of
[00:01:27] Pat Grady: physical AI including robotics.
[00:01:29] Pat Grady: Enjoy the show.
[00:01:30] Pat Grady: [♪ OUTRO MUSIC PLAYING [♪
[00:01:32] Alex, thanks for joining us on the show.
[00:01:34] Sonya Huang: Hey, Pat, hi, Sonja.
[00:01:35] Sonya Huang: One of the things that is very special about your company
[00:01:38] Sonya Huang: is that it sort of typifies AV 2.0,
[00:01:42] Sonya Huang: meaning a new architectural approach that I think is kind of
[00:01:46] Sonya Huang: demonstrated to be superior to the AV 1.0 approach
[00:01:50] Sonya Huang: that people toiled with for so many years.
[00:01:53] Sonya Huang: Can we just start by defining what was AV 1.0?
[00:01:56] Sonya Huang: What is AV 2.0?
[00:01:58] For sure.
[00:01:59] Alex Kendall: When we started the company in 2017,
[00:02:01] Alex Kendall: the opening pitch in our C-deck was all about
[00:02:05] Alex Kendall: the classical robotics approach at the time was
[00:02:08] Alex Kendall: to take a perception, planning, mapping, control,
[00:02:10] Alex Kendall: essentially break down the autonomy problem
[00:02:12] Alex Kendall: into a bunch of different components
[00:02:14] Alex Kendall: and largely hand engineer them.
[00:02:16] Alex Kendall: And our pitch was that, okay, we think that the future of
[00:02:19] Alex Kendall: robotics is not going to be a system that's
[00:02:21] Alex Kendall: hand engineer to drive with a lot of infrastructure
[00:02:24] Alex Kendall: like high-definition maps.
[00:02:25] Alex Kendall: But instead, we thought that the future of robots
[00:02:29] Alex Kendall: would be intelligent machines that have the onboard
[00:02:30] Alex Kendall: intelligence to make their own decisions.
[00:02:33] Alex Kendall: And of course, the best way we know how to build an AI
[00:02:35] Alex Kendall: system is within to end-earned learning.
[00:02:37] Alex Kendall: So for the last 10 years, we've been promoting an approach,
[00:02:40] Alex Kendall: next generation approach, AV 2.0 that replaces that stack
[00:02:43] Alex Kendall: with one end-to-end neural network.
[00:02:46] Alex Kendall: Now, of course, that may seem more obvious today,
[00:02:50] Alex Kendall: but it has been contrarian for many, many years.
[00:02:54] Alex Kendall: But I think today it's maybe unfair to make that basic
[00:02:57] Alex Kendall: distinction because, of course, anyone who's worth a
[00:03:00] Alex Kendall: grain of salt will use deep learning in various parts of the
[00:03:03] Alex Kendall: stack. But what you see in more incumbent solutions to
[00:03:07] Alex Kendall: autonomous driving is, of course, deep learning for
[00:03:09] Alex Kendall: perception and maybe for each different component,
[00:03:11] Alex Kendall: but still a lot of hand interface, there's still a
[00:03:13] Alex Kendall: lot of infrastructure on high-deficient maps,
[00:03:15] Alex Kendall: and perhaps reliance on a lot of hardware.
[00:03:19] Alex Kendall: So our solution is still somewhat
[00:03:24] Alex Kendall: moved on, but today, rather than just being an end-to-end network,
[00:03:26] Alex Kendall: today, of course, we start to talk about foundation models.
[00:03:28] Alex Kendall: We start to talk about more of a general purpose
[00:03:31] Alex Kendall: intelligence, one that can understand not just how to drive
[00:03:34] Alex Kendall: that car, but many cars with different sensor
[00:03:37] Alex Kendall: architectures with different use cases.
[00:03:38] Alex Kendall: And so really, it all boils down to how do we build the
[00:03:42] Alex Kendall: most intelligent robot that can scale without
[00:03:46] Alex Kendall: needing owner of infrastructure?
[00:03:49] So where there's sensor inputs, motion output,
[00:03:54] gigantic neural net in the middle.
[00:03:56] Sonya Huang: That's right. At a very, very simple level, but some of the
[00:04:01] Alex Kendall: interesting things you see that are maybe different from the
[00:04:03] Alex Kendall: story we've all heard with large language models
[00:04:05] Alex Kendall: is with autonomous driving, of course, there are some
[00:04:08] Alex Kendall: interesting new factors. One is, of course, safety.
[00:04:12] Alex Kendall: The system we need to make sure is safe by design.
[00:04:15] Alex Kendall: And what that means is that we can't just pump more data in
[00:04:18] Alex Kendall: and hope that hallucinations go away.
[00:04:21] Alex Kendall: But we need to design an architecture that is still
[00:04:24] Alex Kendall: into end-to-end data driven, but is both functionally safe,
[00:04:28] Alex Kendall: and we can build a robust behavioral safety case.
[00:04:32] Alex Kendall: So that introduces some interesting architectural
[00:04:36] Alex Kendall: challenges. And then, of course, we also need to run real-time
[00:04:39] Alex Kendall: onboard a robot, onboard a vehicle.
[00:04:41] Alex Kendall: And so dealing with the onboard compute and onboard sensor
[00:04:44] Alex Kendall: limitations, make it an interesting challenge.
[00:04:48] Alex Kendall: Yes, it's the same narrative we're seeing playing out in
[00:04:50] Alex Kendall: robotics that we've seen play out and all these other AI
[00:04:53] Alex Kendall: fields like language or game playing agents.
[00:04:55] Alex Kendall: It's that an end-to-end data-learn solution is out
[00:04:58] Alex Kendall: competing anything we can hand code.
[00:05:00] Alex Kendall: And what we're excited to be pioneering is that exact same
[00:05:03] Alex Kendall: narrative here in robotics and autonomous vehicles.
[00:05:05] Alex Kendall: And when you guys started this in 2017 and it was a very
[00:05:08] Sonya Huang: contrarian approach, when people from the industry
[00:05:13] Sonya Huang: said, well, that'll never work but cuts.
[00:05:15] Sonya Huang: How did they finish that sentence?
[00:05:18] I could count hundreds of those things.
[00:05:22] Alex Kendall: Yeah, typical arguments were, look, it's not safe.
[00:05:26] Alex Kendall: It's not interpretable.
[00:05:29] Alex Kendall: You can't understand what it's doing or even simply,
[00:05:33] Alex Kendall: it doesn't make sense.
[00:05:34] Alex Kendall: We haven't heard of this AI thing.
[00:05:37] Alex Kendall: And look, I think five, 10 years ago, it was probably
[00:05:40] Alex Kendall: reasonable to say, end-to-end-end learning wasn't interpretable.
[00:05:44] Alex Kendall: But I don't think that's true today.
[00:05:45] Alex Kendall: I think today we have a lot of really great tools for
[00:05:48] Alex Kendall: understanding and responding to insights about the way
[00:05:52] Alex Kendall: these deep learning systems reason.
[00:05:55] Alex Kendall: But moreover, I think if you have the ambition to build
[00:05:58] Alex Kendall: any intelligent machine, I think it's naive to think
[00:06:01] Alex Kendall: you can build a complex intelligent machine and actually make it
[00:06:05] Alex Kendall: you know, let's say, strictly interpretable to the point
[00:06:08] Alex Kendall: where you can point to a single line of code or a single thing
[00:06:11] Alex Kendall: that causally made the outcome occur.
[00:06:14] Alex Kendall: The beauty of intelligent machines is that they are
[00:06:16] Alex Kendall: so wonderfully complex.
[00:06:19] Alex Kendall: And there, I think the way that we're going to not just design them,
[00:06:23] Alex Kendall: but understand them is through a data-driven structure.
[00:06:27] Can you say more about the before and after of the
[00:06:29] Pat Grady: AV1.0 stack and the millions, billions of lines of code that
[00:06:34] Pat Grady: goes into those systems versus the two that are systems today?
[00:06:40] Pat Grady: And how quickly is that changing?
[00:06:42] Pat Grady: Because my sense is that deep learning, large neural nets,
[00:06:46] Pat Grady: hitting the physical economy is a much more recent phenomenon
[00:06:49] Pat Grady: than people might appreciate.
[00:06:51] Pat Grady: Well, especially when you think about path to distribution
[00:06:54] Alex Kendall: and deploying these systems, I mean, the automotive industry has just gone
[00:06:57] Alex Kendall: through a seismic shift and bringing out software to fine vehicles
[00:07:00] Alex Kendall: and the right hardware on these cars to be able to make them drive.
[00:07:04] Alex Kendall: Maybe one common point of debate is, is it camera only or camera radar
[00:07:10] Alex Kendall: as a sensor approach to autonomy?
[00:07:13] Alex Kendall: Just to be clear on our position, Wave, we want to build an AI that can
[00:07:18] Alex Kendall: understand all kinds of different sensor architectures.
[00:07:19] Alex Kendall: There's going to be sometimes where camera only solution makes sense,
[00:07:22] Alex Kendall: sometimes where camera radar, light, and we train our
[00:07:26] Alex Kendall: our embodied AI model on all of those permutations from very diverse data sources.
[00:07:31] Alex Kendall: And the car we just drove in is a camera only stack.
[00:07:34] Alex Kendall: We've got other cars that we work on with partners that have radar and
[00:07:37] Alex Kendall: lighter and of course there's different trade-offs that you take there.
[00:07:41] Alex Kendall: But more generally, we're seeing mass-produced cars from the best manufacturers
[00:07:45] Alex Kendall: around the world have a GPU, but onboard have surround camera,
[00:07:48] Alex Kendall: surround radar and sometimes a front lighter.
[00:07:51] Alex Kendall: And what's beautiful about that is there's now the opportunity to see this AI come out
[00:07:54] Alex Kendall: and benefit people around the world.
[00:07:56] Alex Kendall: I think that kind of software-defined infrastructure is happening
[00:08:00] Alex Kendall: and automotive has perhaps not yet happened to the same degree in other
[00:08:04] Alex Kendall: robotics verticals, but I'm sure the markets are going to move that way as well.
[00:08:08] Alex Kendall: And in general, having the right level of compute and infrastructure in a scalable way and
[00:08:14] Alex Kendall: opening up these platforms to AI I think is what's really making this possible.
[00:08:18] Alex Kendall: And that's gone through a tipping point in the last couple of years.
[00:08:21] And you know, your perspective of AV2.0 has flipped from contrarian to I'd say consensus.
[00:08:28] Pat Grady: Maybe in the last two or three years, do you think it was FSD12 that did it?
[00:08:33] Pat Grady: When did that mindset start to shift?
[00:08:36] I miss the contrarian day, but even today I still, I was in a conversation this morning where
[00:08:43] Alex Kendall: I still see a lot of folks still say, yes, we need into an AI.
[00:08:48] Alex Kendall: They've brought the big tech narrative around the future of AI,
[00:08:51] Alex Kendall: but they say things like we need into an AI with hard constraints or with safety guarantees.
[00:08:57] Alex Kendall: And still, there's still can be some belief that some hybrid approach is the way to go,
[00:09:05] Alex Kendall: where you want to try and take a rules-based stack and an end-to-end lens stack,
[00:09:09] Alex Kendall: but often these approaches can get the worst of both worlds or just ag costs and complexity.
[00:09:15] Alex Kendall: I still think there is a distribution in the market of those that are leaning and moving
[00:09:18] Alex Kendall: fast and those that are perhaps have some catching up to do.
[00:09:24] Alex Kendall: But of course, crediting the breakthrough that all of us that have been working in deep learning
[00:09:30] Alex Kendall: that really made this world-changing and mainstream, of course, we've got to credit the
[00:09:33] Alex Kendall: large language model breakthroughs. I think they've inspired the world and opened up the markets
[00:09:38] Alex Kendall: mind to be curious about the technology. But also what we've been doing at Wave,
[00:09:45] Alex Kendall: a year ago, we were just driving in Central London. Central London, I think, is a great
[00:09:49] Alex Kendall: proving ground because it's this unstructured, incredibly complex and dynamic city
[00:09:55] Alex Kendall: that our AI has learned to navigate around very smoothly, safely and reliably.
[00:10:01] Alex Kendall: But in the last year, we've taken it to highways, to Europe, Japan, North America,
[00:10:05] Alex Kendall: our cars were in New York City last week driving around there. And so bringing a global,
[00:10:10] Alex Kendall: being able to take it to different manufacturers' vehicles and show a product-like experience.
[00:10:17] Alex Kendall: This growth is, I think, also really opened up a lot of inspiration around the world.
[00:10:23] Why is it that you're able to launch in hundreds of cities worldwide?
[00:10:27] And some of the AV-1.0 companies need to actually go out and build an HD map.
[00:10:32] Pat Grady: Just say we're on the difference in how technical differences are actually leading to
[00:10:39] differences in how the machine is able to learn and how you're able to roll out.
[00:10:42] Pat Grady: Autonomous driving is all about generalization. Generalization means being able to
[00:10:47] reason about or understand something you've never seen before. Every time you go for a drive,
[00:10:52] Alex Kendall: you're going to see something new for the first time. What did we see today? We saw a road worker
[00:10:58] Alex Kendall: rolling out some carpet thing in front of the road, but on a pedestrian crossing, but not
[00:11:03] Alex Kendall: wanting to step out. And we had to reason about, could we pass them without yielding, for example.
[00:11:08] Alex Kendall: There's just an example from earlier today, but you could think about all the new things you see
[00:11:13] Alex Kendall: on the roads every time you drive. You're never going to see every experience in your training data.
[00:11:18] Alex Kendall: So that means that you have to be able to reason and generalize to things you haven't seen before
[00:11:22] Alex Kendall: to be safe, to be useful around the world. And that's what has motivated our entire approach.
[00:11:29] Alex Kendall: So whether it's us, a manufacturer giving us one of their vehicles and within a couple of months,
[00:11:33] Alex Kendall: us being able to drive it on the road, a couple of weeks ago, in September this year, we
[00:11:41] Alex Kendall: unveiled a vehicle to media with Nissan in Tokyo. Just four months earlier, was the first time we'd
[00:11:48] Alex Kendall: even driven in Tokyo and got hands on this vehicle. Four months later, we were having media
[00:11:52] Alex Kendall: driving the car, experience it, and that was a new country and a new vehicle for us.
[00:11:58] Alex Kendall: So what that showed is that our AI was able to generalize. It's trained on very diverse data
[00:12:02] Alex Kendall: from around the world. It's trained on diverse sensor sets, vehicles. And so it was able to understand
[00:12:07] Alex Kendall: that that vehicle is a new sensor distribution and of course the complexity of driving around
[00:12:11] Alex Kendall: in central Tokyo. So I think that's a really great demonstration of generalization. And if we think
[00:12:17] Alex Kendall: about, you know, if you're building a vertically integrated robotic solution, maybe you can go deep,
[00:12:21] Alex Kendall: but our ambition is to be the embodied AI foundation model for all of the best fleets and
[00:12:27] Alex Kendall: manufacturers around the world. And to do that, unless we want to overload the company by building
[00:12:33] Alex Kendall: a separate neural network for each application, we need to be able to generalize. We need to
[00:12:36] Alex Kendall: about it, amortize our cost over one large intelligence and about a very quickly adapt to each
[00:12:42] Alex Kendall: different application that our customers care about. That's what we're trying to push.
[00:12:46] Alex Kendall: You mentioned reasoning in there in terms of how the model is reasoning through, you know,
[00:12:51] Pat Grady: there's construction work for what do I do now? In the LLM world, obviously reasoning is its own
[00:12:57] separate track of lots of scaling and Princeton computer techniques. Are you deliberately training
[00:13:03] Pat Grady: your models to reason? Is it an emergent property, emergent behavior of the models, like say more about
[00:13:07] Pat Grady: even that reasoning? We are. And I think reasoning in the physical world can be really well expressed as
[00:13:14] Alex Kendall: a world model. In 2018, we put our very first world model approach on the road. It was a very small
[00:13:23] Alex Kendall: 100,000 parameter neural network that could simulate a 30 by three pixel image of a road in front of us.
[00:13:31] Alex Kendall: But we were able to use it as an internal simulator to train a model-based reinforcement learning algorithm.
[00:13:36] Alex Kendall: There's a fun blog post, if you want to see the history on that. But fast forward to today,
[00:13:42] Alex Kendall: and we've developed a Gaia. It's a full generative world model that's able to simulate
[00:13:48] Alex Kendall: multiple camera and sensors in very rich and diverse environments. You can control it and prompt
[00:13:53] Alex Kendall: the different agents or seen in it. And that's an example of reasoning where we can train in the
[00:13:59] Alex Kendall: ability to simulate how the world works and what's going to happen next. What happens when you
[00:14:04] bring this kind of representation on the road is you get some really nice emergent behavior. Like
[00:14:09] Alex Kendall: today, when we saw we were driving around unprotected turns that were included, you saw the car
[00:14:13] Alex Kendall: nudge forward until it could see for itself and then completed the turn. Or when it's foggy and
[00:14:19] Alex Kendall: London, you see the car slow down and drive to what it can reason about. And by training it with
[00:14:25] Alex Kendall: that level of understanding, it gives that level of emergent behavior that helps it really understand
[00:14:32] Alex Kendall: particularly complex multi-agent scenarios. I think that's key for getting
[00:14:37] Alex Kendall: safe and smooth autonomous driving. So the world models are really key to teaching the model how
[00:14:42] Pat Grady: the reason through their new scenarios. 100%. You mentioned earlier the diversity of your data.
[00:14:47] Sonya Huang: Say, word about world data comes from. It's becoming like an enormous amount of data because,
[00:14:53] Alex Kendall: of course, unlike the language domain or image domain when we're dealing with
[00:14:59] Alex Kendall: a typical self-driving car that has a dozen multiple megapixel cameras, radar, maybe a
[00:15:06] Alex Kendall: lighter, you know, you're dealing with when you aggregate that up, it's very quickly tens or
[00:15:11] Alex Kendall: hundreds of petabytes of data. So it's an enormous amount of data you have to train on. But it's
[00:15:17] Alex Kendall: the diversity that's really key. And we've solved for diversity in two ways. The first one is by
[00:15:21] Alex Kendall: becoming a trusted partner across the industry and aggregating data across many different sources
[00:15:27] Alex Kendall: from dash cams to fleets to manufacturers to robot operators. The second one is being able to
[00:15:33] Alex Kendall: filter and really understand the data. Here we've really worked hard to develop different
[00:15:41] Alex Kendall: unsupervised learning techniques to be able to cluster and find unusual anomaly experiences.
[00:15:48] Alex Kendall: And of course, find the scenarios that our system is performing poorly at and then drive the
[00:15:53] Alex Kendall: learning curriculum on those. But yeah, today we learn from a diverse set of vehicles,
[00:16:00] Alex Kendall: diverse set of sensor architectures of countries. And that's really one of the key things that
[00:16:04] Alex Kendall: drives the level of generalization. Does the increased growth of world models and
[00:16:10] Pat Grady: similar data, does that mean that you just don't need as many actual on-road miles?
[00:16:16] I think there's two sides to that question, right? On the one side, yes,
[00:16:21] Alex Kendall: learning efficiency really matters. But second, you can't only rely on learning efficiency.
[00:16:27] Alex Kendall: At the limit, if we take our current approach and just scale it up, I'm sure it'll produce
[00:16:31] Alex Kendall: generic level 5 driving. At the limit, if you have unlimited training data, this is really just
[00:16:37] Alex Kendall: a lookup data table with some prior experience. But that's not economically or technically feasible.
[00:16:43] Alex Kendall: And so the question is, how can you train this to be the most efficient data efficient system?
[00:16:48] Alex Kendall: Because I think efficiency will lead to not just improved cost, but faster time to market and more
[00:16:53] Alex Kendall: intelligence. So efficiency comes from a number of different factors. There's most importantly,
[00:17:01] Alex Kendall: how the data curriculum you put in place. But then the learning algorithms, how do you magnify
[00:17:06] Alex Kendall: the learning you have? And I think world models are a really great opportunity for that. They generate
[00:17:10] Alex Kendall: synthetic data and synthetic understanding that doesn't replace real world data, but it
[00:17:14] Alex Kendall: recombines it and magnifies it in new ways. It lets you pull in interesting insights. And I think
[00:17:20] Alex Kendall: these kind of approaches can really, really improve data efficiency. But across the board, I think
[00:17:26] Alex Kendall: working under resource constraints as a forced out team to develop so many innovations,
[00:17:32] Alex Kendall: I'd also call out just the workflow. Because in traditional robotics, when you're
[00:17:38] Alex Kendall: tuning parameters or algorithms or designing geometric maps and things like this,
[00:17:43] Alex Kendall: there's very well established cultures and workflows. But our team, when we have 50 model
[00:17:48] Alex Kendall: developers working on one main production model, or when we have an end-to-end net that we need to
[00:17:55] Alex Kendall: understand and interest back to, or even the way that we deploy these systems to simulation or to
[00:17:58] Alex Kendall: the road and feedback, we've developed the entire culture from the ground up way that's been developed
[00:18:04] Alex Kendall: for embodied AI for end-to-end deep learning for driving. The data infrastructure, the simulation,
[00:18:09] Alex Kendall: the safety licensing before we put systems on the road, this is not being a hedge or a
[00:18:15] Alex Kendall: side-bet for us, but this is the entire essence of our culture. And I think doing this under
[00:18:21] Alex Kendall: resource constraints and doing this with full mission-driven conviction has led to a bunch of
[00:18:26] Alex Kendall: interesting innovations that look getting to where we are today, everything is about iteration speed.
[00:18:31] Alex Kendall: Speaking of your culture, I'm picturing a bunch of AI research types, machine learning
[00:18:39] Sonya Huang: engineers, that sort of thing. How does the culture of your organization differ from similar
[00:18:46] Sonya Huang: applied lab type environments, given the customer base that you serve, given that you're going
[00:18:51] Sonya Huang: after the automotive industry specifically with all of its quirks around supply chain and all of
[00:18:57] Sonya Huang: its requirements around safety? And so how does that influence the culture of your business?
[00:19:03] Hugely. In fact, for the first few years of wave, we were really a group of passionate
[00:19:10] Alex Kendall: embodied AI researchers, but in the last couple of years, I'm really, really proud of how our
[00:19:16] Alex Kendall: team has built out deep expertise in understanding the automotive industry, but also the ability to
[00:19:22] Alex Kendall: reliably deliver to our partners there. And that's a different culture. It's a culture of really
[00:19:28] Alex Kendall: growing to respect because when you're building millions of cars, the level of reliability and
[00:19:34] Alex Kendall: MTT if you need there is extraordinary. What have you all learned from them? I mean, I'm sure
[00:19:41] Sonya Huang: part of your job is to teach them about what's going on in the world of AI. What have you learned
[00:19:45] Sonya Huang: from them? I think some of the main things I'll call out have been efficiency and reliability,
[00:19:52] Alex Kendall: the difference between technology and a product will be some of the main themes. I mean, the
[00:19:57] Alex Kendall: the level of reliability required, but also the level of quality that is seen to really robustly
[00:20:06] Alex Kendall: prove these systems out before deployment and the pride that these companies take in that has
[00:20:11] Alex Kendall: been exceptional. Another thing has been perhaps the sense of brand differentiation and the desire for
[00:20:18] Alex Kendall: do you want your car to drive? How can your driving personality really match the brand's preferences?
[00:20:26] Alex Kendall: How can you provide that experience that really gives brand differentiation? And the great
[00:20:31] Alex Kendall: news is that I think we've been able to riff and brainstorm off these and come up with some really
[00:20:35] Alex Kendall: neat technical ideas down that vein. But ultimately, safe, high quality and personalizable AI
[00:20:47] Alex Kendall: has been some great feedback we've got from the industry. Can you talk about your path to market
[00:20:52] Pat Grady: in partnering with the other OEMs? How do you decide to do that? And then how do you think
[00:20:56] Pat Grady: the market landscape will play out for how autonomy rules out? Of course, great questions
[00:21:01] Alex Kendall: on you because since the beginning of Wave, we've been focused on the pitch I gave around
[00:21:07] Alex Kendall: into and deep learning, being an approach autonomy. But we've tried a number of different
[00:21:11] Alex Kendall: go-to-market approaches over the years. But in the last couple of years, I've been hugely energized
[00:21:17] Alex Kendall: about working and partnering with the biggest and best consumer automotive manufacturers around
[00:21:24] Alex Kendall: the world. Why is that? Well, I mentioned how they've begun to introduce software-defined vehicles,
[00:21:29] Alex Kendall: so they have the infrastructure to work with autonomy. There's the market belief that this is
[00:21:34] Alex Kendall: a technology that can really thrive. And also, it's the chance to get to scale far beyond what we're
[00:21:40] Alex Kendall: seeing with the city by city robot taxis we're seeing right now. But moreover, these are OEMs that
[00:21:48] Alex Kendall: invest in the right infrastructure to go from not just driver assistance, but to
[00:21:53] Alex Kendall: eyes off autonomy where you can actually take liability for the drive and give the user a safe
[00:21:59] Alex Kendall: and give them time back from their driving experience. So that's awesome. I think when you think
[00:22:04] Alex Kendall: about the market, there are 90 million cars built each year. And so some manufacturers that are
[00:22:11] Alex Kendall: building the autonomy systems themselves like Tesla built a couple of million, but the vast majority
[00:22:15] Alex Kendall: of the market, I think there's an opportunity partner to work with some of these innovative
[00:22:19] Alex Kendall: platforms and to bring our AI to market to make these autonomous products possible. And it will
[00:22:24] Alex Kendall: only grow from there. These manufacturers don't want to stop a driver assistance. We're working
[00:22:28] Alex Kendall: together to build eyes off and driverless robot taxi products. But the key thing is that by avoiding
[00:22:34] Alex Kendall: retrofitting our own hardware on these vehicles, by putting them in natively as a software integration,
[00:22:40] Alex Kendall: we can move fast at scale, we can build low-cost vehicles that can be homologated all around the
[00:22:44] Alex Kendall: world. And this is going to be the path to see tens and hundreds of thousands of robot
[00:22:49] Alex Kendall: taxis rolled out around the world at an affordable price. And of course, this is all possible because
[00:22:55] Alex Kendall: of the level of generalization that this AI enables. Tesla FSD is just such a game-changing product.
[00:23:02] Pat Grady: And you know, my friends have it. It's just they can't imagine driving any other way. And so
[00:23:06] Pat Grady: it's really cool that you're going to empower the 88 million other vehicle sold every year to
[00:23:12] Pat Grady: be able to sell that experience as well. 100%. It's one of those things that a lot of people
[00:23:17] Alex Kendall: jump in our car and come for a drive with some being skeptical about autonomy. But without
[00:23:22] Alex Kendall: exception, they step out with a smile on their face. It's a magical experience. And yeah, I can't
[00:23:28] Alex Kendall: wait for people to try it around the world and make autonomy. Not just a robot taxi tourism
[00:23:33] Alex Kendall: experience, but bring this experience to people in, yeah, eventually every city.
[00:23:39] What do you make of the sensor fusion, confusion, debate? You know, the one that plays it on
[00:23:44] Pat Grady: Twitter every year or so of Tesla gets confused if there's both camera and and light are coming in.
[00:23:51] Pat Grady: Sorry, radar. I think it's the wrong debate to be having. It's not the frontier question.
[00:23:56] Alex Kendall: The industry is really, he's outside of Tesla. It's really coalesced around a common architecture
[00:24:02] Alex Kendall: of a surround camera, surround radar, and a front-facing light-air stack. Now, this costs under
[00:24:07] Alex Kendall: $2,000. So it's automotive grade components, not the retrofit robot taxi components you see today.
[00:24:13] Alex Kendall: But having a front-air GPU, automotive grade GPU on the car and that kind of sensor architecture
[00:24:20] Alex Kendall: is a really great platform to build L3L4 autonomy, eyes off or driverless. It gives you the necessary
[00:24:26] Alex Kendall: redundancy. It lets you deal with edge cases that cameras alone, I agree they can get you to
[00:24:31] Alex Kendall: human level, but we want to go beyond human level. And so I think this kind of architecture is
[00:24:36] Alex Kendall: affordable, scalable. It's got the supply chain for mass manufacturer and it can eliminate, I think,
[00:24:45] Alex Kendall: eliminate all accidents and really drive superhuman levels of performance.
[00:24:50] Alex Kendall: So that's what we're seeing. Many manufacturers bring out on their vehicles and we're integrating
[00:24:55] Alex Kendall: our AI. Of course, for a driver assistance system, camera only can work for a human level driverless
[00:25:01] Alex Kendall: system or of course, I should clarify, 90 something you can look at different stats, but 95%
[00:25:08] Alex Kendall: or above accidents unfortunately are caused by human error. So not only can you be human level,
[00:25:13] Alex Kendall: but you can eliminate a lot of human attention and accidents caused by that. But there are still
[00:25:19] Alex Kendall: accidents that to be able to solve would require perception capabilities that could be on vision.
[00:25:25] Alex Kendall: And if we want to tackle that long tail, there are many ways to solve it. One of the ways would be
[00:25:29] Alex Kendall: to bring in some other sensing modalities like radar and light hours. So we're excited to be working
[00:25:34] Alex Kendall: with those kind of platforms, but crucially, natively integrated into the OEMs vehicles themselves.
[00:25:41] Alex Kendall: Is it the same neural net that can drive on one OEM's car and another's car? How does that even work?
[00:25:47] Pat Grady: Because I imagine each vehicle has slightly different position cameras, things like that.
[00:25:52] It comes from the same family. So we train a very large scale, we regularly train very large
[00:25:57] Alex Kendall: scale models. Of course, we iterate them on the month to month, but that's one model that's common
[00:26:04] Alex Kendall: to all of the fleets that we work with. But as you optimize to a specific sensor set or a specific
[00:26:10] Alex Kendall: embedded target, of course, you can start to specialise the model. But the beauty is that 99%
[00:26:16] Alex Kendall: plus of the cost and the time and the effort is training their base model. And then we can build
[00:26:20] Alex Kendall: very efficient personalization to the specific customer. And so this lets this scale, but gives us
[00:26:27] Alex Kendall: the ability to squeeze it to very efficient real-time platforms and make it adapted to a specific
[00:26:35] Alex Kendall: use case. Are you going to let Pat personalize a super aggressive driver model?
[00:26:39] Pat Grady: And they need to. What driving style would you like Pat?
[00:26:42] Alex Kendall: But yeah, pretty aggressive.
[00:26:45] Safe, very safe. We can do that. We find, it's really funny when you build distributions around
[00:26:52] Alex Kendall: driving behaviour. Yeah, you can really tell from the human training data we have, you can really
[00:26:58] Alex Kendall: tell when it goes from being helpfully assertive, let's say, to unhelpfully aggressive. And we can
[00:27:04] Alex Kendall: draw a clean line there. What about you, Sonia? How was the drive we just had?
[00:27:08] Alex Kendall: Fantastic. It was comfortable. It was safe. It felt very human actually. The way it was kind of
[00:27:14] Pat Grady: nudging up when it couldn't see on the tour, and it was very human.
[00:27:17] Pat Grady: Yeah, well, it's as complex as we can get in Silicon Valley, but come to Tokyo or London or
[00:27:24] Alex Kendall: was in the weekend in downtown San Francisco. And yeah, you really need the ability to predict and
[00:27:31] Alex Kendall: reason about other folks around you to be able to drive in a human-like way. And what we find is
[00:27:36] Alex Kendall: that if you're not able to smoothly go around double parked vehicles or deal with other dynamic
[00:27:43] Alex Kendall: obstacles or even the prevailing road traffic might not be aligned to the specific lane, but maybe
[00:27:47] Alex Kendall: there's a human-like way of driving. Then what's awesome about the intelligence that we've built is
[00:27:54] Alex Kendall: it's able to reason about these things and keep the traffic flowing, keep interacting with road
[00:27:58] Alex Kendall: users in a very human-like way. I think this is going to be key for societies to accept and love
[00:28:02] Alex Kendall: for robot taxis. I can't wait to make that a reality. Are there any specific corner cases that you
[00:28:07] Sonya Huang: across have a hard time with today? There are loads and it's really hard to generically talk about
[00:28:15] Alex Kendall: one because they're so rare. It's very hard to say, Alex, always these types because it's always
[00:28:23] Alex Kendall: a corner case is a couple of edge cases coming together in a corner and it's always confounding
[00:28:27] Alex Kendall: factors when you get something really obscure. But we're driving, we've driven in over 500 cities
[00:28:33] Alex Kendall: this year and so when you're driving at that level of scale, of course you see things that you've
[00:28:37] Alex Kendall: never seen before. Road signs are written in a new language. Actually, maybe one way to break it down
[00:28:42] Alex Kendall: is often we talk about driving broken down into safety, utility and flow, safety being, of course,
[00:28:48] Alex Kendall: safety critical behavior, flow being the style of driving, is it smooth, is it enjoyable,
[00:28:53] Alex Kendall: and then utility being the navigation and road semantics. Safety and flow we've found
[00:28:58] Alex Kendall: generalize exceptionally well throughout the world. We get almost uniform metrics in every country
[00:29:02] Alex Kendall: we operate in in terms of safety and flow or comfort of the drive. But utility has been the
[00:29:09] Alex Kendall: really interesting one. As we've gone global, how do you navigate, how do you deal with road signs,
[00:29:13] Alex Kendall: how do you read different languages, how do you deal with different driving cultures,
[00:29:17] Alex Kendall: and so that's the one that's been interesting. But we published some results about this when we
[00:29:24] Alex Kendall: went from the UK to the US. We needed hundreds of hours of data to be able to drive within
[00:29:31] Alex Kendall: 10% of our frontier performance. But then when we went to Europe and to Germany, of course,
[00:29:38] Alex Kendall: we'd already learn to drive on the right side of the road, coming to the US would learn to do
[00:29:42] Alex Kendall: right turns of red lights. We then came into Germany. We had to learn to still drive on the right
[00:29:46] Alex Kendall: side of the road, but of course you can't turn right at a red light there. But then on the auto
[00:29:50] Alex Kendall: you'd like this unique to drive. We drive today up to 140. So pretty fast there. But
[00:29:57] Alex Kendall: yeah, it gets more efficient each time with exponentially less data in each new market because
[00:30:02] Alex Kendall: you've seen some of those things before. Yeah. You mentioned at the beginning that large
[00:30:06] Pat Grady: language models were part of what flipped your approach from from contrarian to consensus.
[00:30:12] Pat Grady: Are you integrating large language models at all into your models? And I know some of the robotics
[00:30:17] Pat Grady: companies they're getting started now are starting from this VLA VLM base. Is that part of your
[00:30:21] Pat Grady: architecture? 100% in 2021 we started working on language for driving. I remember my team
[00:30:28] Alex Kendall: counted to me at the time and said, hey, we should start a project on language. I said, no, no,
[00:30:32] Alex Kendall: no guys, start up sort of that focus, keep keep focus. But they actually gave some pretty
[00:30:36] Alex Kendall: compelling arguments. So we started to play around with these things and a year or so later we
[00:30:41] Alex Kendall: released a lingo, which is the first vision language action model in autonomous driving.
[00:30:48] Alex Kendall: And what was special about this model was it could not only drive a car, see the world driver
[00:30:53] Alex Kendall: car, but also converse and language. And it'll let you talk to it and ask questions, what are
[00:30:57] Alex Kendall: you finding this risky? What's going to happen next? Or even a comment at your drive? And what's
[00:31:03] Alex Kendall: interesting about this is that so there's a few benefits. One is bringing language into pre-training.
[00:31:07] Alex Kendall: Of course, just improves the representations. Power gives you know more interesting information
[00:31:13] Alex Kendall: to learn from than than just imagery alone. But then second, aligning the representation with
[00:31:18] Alex Kendall: language opens up a ton of interesting product features. It enables a you know, you to create a
[00:31:24] Alex Kendall: chauffeur experience where you could actually talk to your driver. You know, no longer do you need a
[00:31:28] Alex Kendall: PhD in robotics to understand the system, but actually you can just talk to us and like ask
[00:31:33] Alex Kendall: it to drive Pat if you want to race around the commute super fast, then you can you can demand that.
[00:31:40] Alex Kendall: But then third, it gives you a really nice introspection tool where you can start to actually
[00:31:44] Alex Kendall: you know, you could imagine regulators or our engineering team conversal the system in language
[00:31:48] Alex Kendall: to really diagnose why it's doing what it's doing or get it to explain its reasoning. So I think
[00:31:53] Alex Kendall: these these are really clear benefits, which which we're really excited to be pushing.
[00:31:56] Alex Kendall: That's super cool. And you're running it on the embedded compute.
[00:32:00] We are. So we've put out demos that run offboard. Onboard's challenging with what's in the
[00:32:05] Alex Kendall: automotive market today, but some of the next generation compute, for example, the Nvidia
[00:32:09] Alex Kendall: Thor that our next year in development vehicle is going to be with will be large enough to run it
[00:32:13] Alex Kendall: on board. That's going to be cool. Very cool. You you've talked about how autonomous driving sort of
[00:32:19] Sonya Huang: provides a path to more generalized in body day. I can you paint that picture for us? How you go
[00:32:24] Sonya Huang: from autonomous driving to humanoid robots or whatever other things you might want to
[00:32:31] Sonya Huang: in by the AI? I think we're going to be in the future looking at a ton of interesting use cases
[00:32:37] Alex Kendall: for robotics. What we're seeing is that mobility is becoming possible, I think, much before
[00:32:44] Alex Kendall: manipulation. Manipulation is challenging in terms of access to data, global supply chains
[00:32:51] Alex Kendall: for hardware and actually even the hardware designs themselves. I think tactile sensing is still
[00:32:57] Alex Kendall: a really hard challenge. But inevitably, it'll be a massive transformative thing. But maybe,
[00:33:04] Alex Kendall: maybe is it the maturity of where self-driving was in 2015? But today, our system is rapidly
[00:33:09] Alex Kendall: becoming a general purpose navigation agent, giving it an arbitrary sense of view and a goal
[00:33:14] Alex Kendall: condition that's able to produce a safe trajectory. So I think we're going to see a rapid
[00:33:20] Alex Kendall: advancement from not just consumer automotive, robot taxis, talking about trucking and other
[00:33:25] Alex Kendall: applications. But this AI will enable manufacturers and fleets who want to build robots in any kind
[00:33:31] Alex Kendall: of mobility application. And of course, we'll we're really excited to be working with
[00:33:37] Alex Kendall: frontier developers and applications over time as you as you go out across that robotic stack.
[00:33:42] Alex Kendall: And I expect we'll see more maturity in the coming years from manufacturing and manipulation
[00:33:47] Alex Kendall: use cases as well. But in the end, I think the benefits of having a large foundation model that
[00:33:54] Alex Kendall: certainly in automotive, we can, I think we have access to the largest robot and data supply chain.
[00:34:01] Alex Kendall: And so we're really lucky in that regard to about a push for the intelligence there. But
[00:34:05] Alex Kendall: generalizing the intelligence and new applications, I think there'll be benefits from the model being
[00:34:09] Alex Kendall: able to experience multiple different verticals and it'll only make it more more general purpose.
[00:34:13] Alex Kendall: Any applications you're excited about?
[00:34:16] Alex Kendall: I mean, I'm psyched to have humanoid robots walking around.
[00:34:19] Sonya Huang: Yeah, me too. I think they're going to be neat, whichever form factor, I think humanoid will play a big
[00:34:26] Alex Kendall: part. I think other forms of locomotion as well. And then manipulation, there's some really
[00:34:31] Alex Kendall: interesting challenges in those space. But I think the same story is going to play out.
[00:34:36] Alex Kendall: You know, a working on a narrow application, you know, like when self-driving,
[00:34:42] Alex Kendall: when to Phoenix, Arizona and put in a ton of infrastructure and expensive hardware to make it
[00:34:46] Alex Kendall: a work is going to, I think, a limited runway. But working on general purpose, lean,
[00:34:51] Alex Kendall: low-cost hardware stacks that really focus on making the system most intelligent and robust.
[00:34:58] Alex Kendall: I think this is the recipe for scale. So yeah, let's watch that space.
[00:35:02] Alex Kendall: Yeah.
[00:35:03] Do you think there are major research breakthroughs needed to reach kind of physical AGI,
[00:35:08] Pat Grady: so to speak? And if so, what do you think is the most promising direction?
[00:35:13] Pat Grady: Absolutely, I do. I think there's so much more ground to scale up the current approaches,
[00:35:18] Alex Kendall: and we'll do that. But I think we'll get compounding returns from, I usually talk about four
[00:35:26] Alex Kendall: factors that drive performance. There's of course data and compute. But then also the algorithmic
[00:35:32] Alex Kendall: capabilities and the embodiment, the what is the hardware and capability on the robots. And I think
[00:35:37] Alex Kendall: we need to push all four. And on the algorithmic side, there are so many opportunities for growth.
[00:35:42] Alex Kendall: I think a key one is measurement. How do you actually measure and quantify these systems? How do
[00:35:49] Alex Kendall: you respond quickly? Find regressions? Be able to really have a simulator that closes the
[00:35:57] Alex Kendall: the real-world gap at scale and can run efficiently. I mean, there's no secret that these
[00:36:02] Alex Kendall: generative world models are very compute-intensive. But having a good measurement system will just
[00:36:08] Alex Kendall: drive efficiency and iteration speed. So that's a key one. People often talk about being a chicken
[00:36:13] Alex Kendall: and egg. If you have a perfect simulator, you've solved self-driving and vice versa. And I
[00:36:16] Alex Kendall: really believe that. I think AlphaGo showed that when you have a perfect simulator, you can just
[00:36:22] Alex Kendall: solve problems through Monte Carlo tree search. And so I think that's going to be the case in robotics as
[00:36:28] Alex Kendall: well. So one is measurement. Another pillar is building more generality into the model. How can
[00:36:36] Alex Kendall: you build out more modalities and align those different modalities in their reasoning? I think this
[00:36:42] Alex Kendall: is going to open up new use cases, particularly when it comes to human-robot interaction and
[00:36:47] Alex Kendall: navigation. I was going back to the utility problem before. Some of these things I'm super excited
[00:36:54] Alex Kendall: about. And then the last one is just engineering efficiency. I mean, training these systems and the
[00:37:00] Alex Kendall: data requirements is extraordinary. And so I wouldn't understate, I think the most sexy part of this
[00:37:06] Alex Kendall: problem is the efficient infrastructure to train and serve these models. And getting that right,
[00:37:15] Alex Kendall: yeah, I think it's a real competitive advantage or disadvantage. We started by talking about
[00:37:20] Sonya Huang: AV2.0. Someday, I imagine we might be talking about AV3.0. What could AV3.0 look like? If you go 5, 10,
[00:37:29] Sonya Huang: 15 years in the future, are there any other big leaps in this industry that you think we'll see?
[00:37:34] You said that with such deadpan. AV, so the whole premise of AV2.0 was all about
[00:37:43] Alex Kendall: putting the intelligence on the car and not needing infrastructure and a ton of,
[00:37:48] Alex Kendall: you know, ton of overcooked hardware, but really making the system intelligent.
[00:37:52] And so I think we're seeing that emerge now with this system that can generalize the world with all
[00:37:57] Alex Kendall: of the on board scalable intelligence and compute. If I were to speculate where AV3.0.0. We haven't
[00:38:05] Alex Kendall: thought about it lately but one idea could be taking the intelligence outside the car. So
[00:38:11] Alex Kendall: I mean, when you start to have majority prevailing autonomous vehicles, you could imagine a ton
[00:38:17] Alex Kendall: of new things you could do when they start to communicate, when they start to interact with each other.
[00:38:22] Alex Kendall: Why do we need traffic lights in the future if they can coordinate? Why do we need all these
[00:38:27] Alex Kendall: senses if you can actually just communicate with the AV in front of you to be able to see
[00:38:31] Alex Kendall: around corners.
[00:38:32] Alex Kendall: I mean, of course I'm speculating here.
[00:38:34] Alex Kendall: It opens up tons of interesting cyber security questions, communication, latency questions,
[00:38:39] Alex Kendall: things like that.
[00:38:40] Alex Kendall: But I don't know, I'm all up for embodied AI and if we can build a safer and more accessible
[00:38:47] Alex Kendall: system by taking the intelligence, not only in the car, but beyond maybe that's a path,
[00:38:53] Alex Kendall: let's see.
[00:38:54] Sonya Huang: That's really interesting.
[00:38:55] Sonya Huang: If AV 3.0 is the point at which it's sort of a mesh network and you know, at that point
[00:39:00] Sonya Huang: maybe humans aren't allowed to drive because they can't communicate with the mesh network
[00:39:04] Sonya Huang: the same way that the robots can and or maybe there are special places that humans go to
[00:39:08] Sonya Huang: drive just for recreational purposes, but always try to take it.
[00:39:12] Sonya Huang: You know, it's all autonomous.
[00:39:14] Yeah, interesting.
[00:39:15] Sonya Huang: How do you hire and how do you attract people with how hot the AI market is these days?
[00:39:19] Pat Grady: I love that question because you know, the end of the day our team is our product, our
[00:39:24] Alex Kendall: team are the most important thing to making this possible and we talk a lot about it
[00:39:29] Alex Kendall: wave about being a place where you can do the best work of your career and what that
[00:39:33] Alex Kendall: means for me in embodied AI is having a set of colleagues around you that inspire and
[00:39:39] Alex Kendall: excite world class and what they do, having the right resources, the right culture, I'm
[00:39:43] Alex Kendall: going to block you, but I think uniquely at wave, we are able to bring together really
[00:39:49] Alex Kendall: a frontier AI environment with a near-term product opportunity and automotive.
[00:39:55] Alex Kendall: So if you want to work on intelligent machines and see your system brought out with the scale
[00:40:00] Alex Kendall: of impact of chat GPT in robotics, I think that's this is a place where we can do it.
[00:40:06] Alex Kendall: The other thing is that we've gone global.
[00:40:08] Alex Kendall: I mean, we have teams in London, Stuttgart, Tel Aviv, Vancouver, Tokyo, Silicon Valley,
[00:40:16] Alex Kendall: and wherever there's an almost some of the major AI and automotive hubs and we're really
[00:40:24] Alex Kendall: looking to build a global culture that can bring this product to the world, work with
[00:40:28] Alex Kendall: customers around the world and most importantly collaborate with the very best people.
[00:40:35] Alex Kendall: Yeah, so anyone who's interested in pioneering a body day, I'm pushing the frontiers and actually
[00:40:40] Alex Kendall: turning it into a game-changing product, come chat, we'd love to speak.
[00:40:45] Wonderful.
[00:40:46] Alex, you've believed in the future for N2N neural nets and self-driving and in the physical
[00:40:52] Pat Grady: economy for longer than just about anybody and it must be incredibly fulfilling to see
[00:40:58] Pat Grady: that vision start to come to life.
[00:41:00] Pat Grady: Congratulations and thank you for joining us.
[00:41:02] Pat Grady: Thank you, Sonya.
[00:41:03] Alex Kendall: Thank you, Pat.