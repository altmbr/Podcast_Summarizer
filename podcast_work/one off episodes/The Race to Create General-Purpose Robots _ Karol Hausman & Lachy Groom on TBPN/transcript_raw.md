# The Race to Create General-Purpose Robots | Karol Hausman & Lachy Groom on TBPN

**Podcast:** One-off Episodes
**Date:** 2025-04-26
**Video ID:** RdxAYNIYxAc
**Video URL:** https://www.youtube.com/watch?v=RdxAYNIYxAc

---

[00:00:00] Welcome to the studio. How are you doing?
[00:00:02] SPEAKER_00: We are. We got both of you. That's fantastic. What's happening?
[00:00:08] SPEAKER_00: Welcome to the show. You can ask him about how it was. Yes. Yes. Maybe that's a great way to start.
[00:00:14] SPEAKER_00: We are huge fans. We were just singing big techs praises saying that we would do anything to support big technology.
[00:00:20] SPEAKER_00: And yet you left big tech. Why did you leave and what are you building now?
[00:00:27] We are building physical intelligence. We want to build a model that can control any robot to do any task.
[00:00:35] This is something I did exploring big tech before. It's just much more fun to do it in a startup way and we're fun.
[00:00:42] SPEAKER_01: Also a little quicker. A little quicker. A little faster paste. Yeah. We need to be crazy.
[00:00:47] SPEAKER_01: Anything's become clear in the last few weeks. We need the robots now.
[00:00:50] SPEAKER_02: Yes. You can't really wait 20 years. Big tech was fully responsible. We probably would have to wait.
[00:00:57] SPEAKER_02: Something like that. Yeah. For sure. Can you walk me through the most recent announcement?
[00:01:02] SPEAKER_00: I saw the video. Fantastic. How would you break it down in terms of what the milestone represents?
[00:01:09] Yes. The biggest challenge in robotics so far hasn't really been agility or dexterity. What robots can do.
[00:01:17] SPEAKER_01: Generalization. Similar to what we've seen in language before.
[00:01:22] SPEAKER_01: Where it was really hard to do tasks. We asked to do something and see if it can work.
[00:01:30] SPEAKER_01: And what we tried to do for the past six months or so is to get to the next level of generalization for
[00:01:36] SPEAKER_01: these models for robots. So the challenge we set for ourselves is to take a robot to a completely new home.
[00:01:43] SPEAKER_01: It's never seen before and ask you to do a complex long horizon task like clean a bedroom or clean a
[00:01:48] SPEAKER_01: kitchen. And there is so many details that go into cleaning a kitchen that you need to understand when
[00:01:55] SPEAKER_01: you're in a new home. And you only start appreciating it when you try to do it with a robot where
[00:02:00] you know everything is different. Like the countertop looks very differently. You don't know where the
[00:02:04] SPEAKER_01: drawers are. You don't know how to open them. You don't know where the objects are. You don't know
[00:02:08] SPEAKER_01: I don't even when I try to wash dishes in my house. I'm always I can't versus where's the spot?
[00:02:14] SPEAKER_02: I don't know where the soap is. Where do I put this? So mess. So you can't generalize. Yeah.
[00:02:21] Challenge really hard. And on top of like knowing all of those things, then you also need to connect
[00:02:26] SPEAKER_01: to motion. You actually need to get the robot to do the right thing. And it turns out that with
[00:02:33] SPEAKER_01: with pi 05, which we which were just released yesterday, we we can do that. And it doesn't work
[00:02:39] SPEAKER_01: all go time. It's not that I can just give it to you and it will work in your kitchen every single
[00:02:44] SPEAKER_01: time. But it works quite often quite well. So we bring it to a new home and it can do those
[00:02:51] SPEAKER_01: things, maybe like 50% of the time, sometimes 80% of the time. I didn't increase from zero percent of
[00:02:57] SPEAKER_01: the time. But yeah, yeah, we've seen before where the previous state of the art was basically
[00:03:02] SPEAKER_01: if you want to show a robotic demo, you need to collect data in that specific environment or
[00:03:06] SPEAKER_01: those specific tasks. And that's where you show it. But now the person I'm bringing somewhere else
[00:03:12] SPEAKER_01: and it kind of works and understands what it means to do. Do you think that consumers will generally
[00:03:17] SPEAKER_02: be more patient around reliability with robotics? Because if I, you know, let's say I have some type
[00:03:23] SPEAKER_02: of robot in my home and I say, hey, do the dishes, right? And 50% of the time it does it perfectly.
[00:03:28] SPEAKER_02: And like, you know, the other 50% of the time I have to kind of interject. Whereas if I'm like
[00:03:32] SPEAKER_02: booking a flight and only 50% of the time it like books the flight, it's like, well, I'm just
[00:03:37] SPEAKER_02: going to do it myself, right? Because like it's only going to take me a minute. Whereas like the
[00:03:40] SPEAKER_02: dishes could take 20 minutes, right? So how do you think about kind of the sort of threshold of
[00:03:46] SPEAKER_02: reliability in order to like really deliver value for consumers? Yeah, I think that like we don't
[00:03:52] SPEAKER_03: think right now about delivering value for consumers. And it's kind of why we structured the
[00:03:56] SPEAKER_03: company the way we did. We're a research lab. We're trying to solve this problem of physical
[00:04:00] SPEAKER_03: intelligence. We really like these consumer oriented tasks. And I think people tend to as well,
[00:04:05] SPEAKER_03: like when they think about laundry being folded for them, I think there'll be a point at which
[00:04:09] SPEAKER_03: it gets good enough that we can deploy it to consumers, but it's not going to be like 50%.
[00:04:13] SPEAKER_03: It's going to be closer to 98, 99%, and there I think we can harp on self driving cars where there
[00:04:20] SPEAKER_03: will be a period of of interventions, right? Like if it doesn't work, it's not that it just will stop
[00:04:25] SPEAKER_03: and do nothing for a while. We can have a human tele operator intervene and finish the toss.
[00:04:30] SPEAKER_03: But I think the other cool thing about the home and consumer use case is there's so much that could
[00:04:34] SPEAKER_03: also just happen overnight. There's like while you're sleeping, your laundry is folded, your meals
[00:04:40] SPEAKER_03: are cooked for like the you know, they're prepped for the week ahead, your house is tidied.
[00:04:45] SPEAKER_03: So consumers still a little far away, but making a lot of progress.
[00:04:49] SPEAKER_03: Can you talk about the just the path in terms of the underlying technology to go from
[00:04:56] SPEAKER_00: a Rumba, we're pulling up the video here on the stream of what you've actually built,
[00:05:02] SPEAKER_00: what were the foundational turning points in terms of the like the different models and
[00:05:07] SPEAKER_00: different breakthroughs? I imagine the transformer was really important, but there's probably a ton
[00:05:14] SPEAKER_00: of other developments that excited you. Now is the time like we're ready to go.
[00:05:20] Yeah, there's been a lot of things that we are building on top of, things like transformers,
[00:05:26] SPEAKER_01: things like vision language models, the concept of pre-training and post-training. A lot of those
[00:05:31] SPEAKER_01: things transfer to the robotics world, but they're they're not as well understood. We are still in
[00:05:37] SPEAKER_01: the process of figuring out what that recipe should be like. We kind of have to rediscover
[00:05:43] SPEAKER_01: some of the steps that language people had to do initially and see how we can map them onto
[00:05:48] SPEAKER_01: the robotics world. We don't have the privilege of having open internet full of data. We need to
[00:05:54] SPEAKER_03: collect the data ourselves, which on one hand is a big challenge, like the data isn't there. You
[00:06:00] SPEAKER_01: can't eat right nearly as fast. On the other hand, it also gives you more freedom in figuring out
[00:06:05] SPEAKER_01: what kind of data is the most important and what data to collect. For this particular
[00:06:10] SPEAKER_01: Pi-05 advancement, what we have to do is one, collect very diverse data set, large diverse data
[00:06:18] SPEAKER_01: set that involves not only model manipulators in homes, but also static robots in the office or
[00:06:25] SPEAKER_01: data of the internet. It turns out if you collect very diverse data across many different tasks
[00:06:30] SPEAKER_01: from many different form factors, they all contribute to each other and they contribute to a
[00:06:35] SPEAKER_01: better understanding for them all what actually is happening and how to utilize all of the data to
[00:06:40] SPEAKER_01: figure out what to do. That was a really, really big component. Then there's also a lot of
[00:06:46] SPEAKER_01: architectural things, a lot of details that we need to get right to make sure that we take full
[00:06:51] SPEAKER_01: advantage of that data. Interestingly, most of the data is actually not the model manipulators in
[00:06:57] SPEAKER_01: many different homes. It's a very, very small percentage of it. It gives us also a lot of code
[00:07:02] SPEAKER_01: that we can leverage the data from the internet or from other platforms where it's easier to collect it
[00:07:08] to get to that kind of generalization. Can you talk a little bit about simulation,
[00:07:14] SPEAKER_00: like data generation through simulation? I imagine it's very easy to procedurally generate
[00:07:18] SPEAKER_00: like a million different floor plans or a trillion different floor plans to try and navigate those
[00:07:23] SPEAKER_00: in two-dimensional space. But at the same time, when you get into the manipulating of a sheet,
[00:07:30] SPEAKER_00: all of a sudden that's a physics calculation, it's probably harder to simulate. It's not like
[00:07:35] SPEAKER_00: with self-driving cars. There's Grand Theft Auto. You can train on. Maybe there's a game where
[00:07:40] SPEAKER_00: you clean up your house, but I certainly haven't played it. How effective has simulation been in
[00:07:45] SPEAKER_00: generating data and is it useful? Is that a viable path here? Yeah, it's been so far really,
[00:07:51] SPEAKER_01: really useful for locomotion, for robots walking around. The reason for this is that for that kind
[00:07:59] SPEAKER_01: of problem, the main difficulty is modeling your own body. How do you place your foot? How do you
[00:08:05] SPEAKER_01: walk? That you can do once when you model your robot really, really well. Then it works. It works
[00:08:11] SPEAKER_01: across many different terrains. You can easily randomize that and figure out the gate that is robust.
[00:08:18] It hasn't worked nearly as well for manipulating objects or working with your hands. I think the reason
[00:08:24] SPEAKER_01: for that is then the difficulty isn't about how do you move your hands. It's more about the world
[00:08:31] SPEAKER_01: that you're manipulating. That is much harder to simulate. You don't just do it once. Every object
[00:08:36] SPEAKER_01: you interact with is different and you have to model each one of those. It's really hard to figure
[00:08:42] SPEAKER_01: out all the different physical parameters to make it good. This is the data that is the most
[00:08:49] SPEAKER_01: important, the data of physical interactions. This is the data that is not on the internet.
[00:08:54] SPEAKER_01: This is the data that is not even describing language. This is something that comes really
[00:08:57] SPEAKER_01: natural to you. You just know how to do it. You don't even sometimes know how to describe it in words.
[00:09:03] I think it's kind of like a really bad combination where it's the hardest thing to do for Sim
[00:09:10] SPEAKER_01: and is the data that we need to Sim the most for. What we discovered so far is that
[00:09:17] basically looking at the past successes of machine learning of AI, it seems that the best
[00:09:24] SPEAKER_01: successes are where you take real world data and large diversity of that data and learn directly
[00:09:30] SPEAKER_01: on that. You don't try to find some kind of proxy or some kind of simulated environment that reflects
[00:09:35] SPEAKER_01: what you actually want to do. You just go after the problem head on and that's what we're doing here.
[00:09:40] SPEAKER_01: So we're collecting a ton of data ourselves in the real world. We can collect very diverse
[00:09:45] SPEAKER_01: data this way. It's also very easy to collect it across many different scenes, many different
[00:09:49] SPEAKER_01: objects. We don't need to create them in Sim. We can just buy them and bring them in and start
[00:09:55] SPEAKER_01: interacting with them. That so far has been actually easier than we had initially thought.
[00:10:02] Yeah, I mean, you say you're collecting a lot of data, but I imagine there's only so many
[00:10:06] SPEAKER_00: of those robots in that demo video that you can manufacture. There's only so many houses that are
[00:10:10] SPEAKER_00: like, yeah, come try your 50% robot in my house. Is that a key? Is that scaling as you'd like?
[00:10:18] SPEAKER_00: Or is this more like you're going to build a physical demonstration unit and then be manipulating
[00:10:28] SPEAKER_00: it in a warehouse or is the plan to be more like let's roll this out and just have beta testers kind
[00:10:35] SPEAKER_00: of dog food for us? All of the above. Basically where we find there's benefits to scale at this stage,
[00:10:42] SPEAKER_03: we'll scale it. We'll figure out a way and whether that's producing more robots, giving them to people,
[00:10:46] SPEAKER_03: whether it's scaling up our operations team and the folks that tele-operate these robots ourselves,
[00:10:53] SPEAKER_03: whether it's going on commercially deploying these into environments where they're doing
[00:10:57] SPEAKER_03: economically useful or viable costs. The training data set collection, we'll do it. We also think
[00:11:03] SPEAKER_03: there's so much though to do on just the algorithmic development that can make the data far more
[00:11:08] SPEAKER_03: useful, that can reduce the necessities of scale, but we're structured such that we can go into every
[00:11:15] SPEAKER_03: avenue. You guys both mentioned there is one of the big questions before Pio 5, where it kind of
[00:11:22] SPEAKER_01: was unclear, do we have to visit million homes? We have to visit hundreds of thousands and at some
[00:11:27] SPEAKER_01: point it becomes kind of not feasible or really really hard and maybe we need to find a different path.
[00:11:33] But so far we've been quite surprised by how few different environments you need to see to be
[00:11:38] SPEAKER_01: able to generalize to anyone. It's awesome. We actually got really reassured that this path could
[00:11:44] SPEAKER_01: really work. Would you guys like to see way more early stage robotics companies? It feels like
[00:11:51] SPEAKER_02: there's the optimists, the 1x, you've got figure making noise, but it feels like we just covered
[00:12:00] SPEAKER_02: this. I think Monday, the Chinese humanoid marathon, I'm sure you guys all of that. They've got a
[00:12:06] SPEAKER_02: lot of people working on this problem. It seems like there's a tendency in venture to think that
[00:12:13] SPEAKER_02: okay, there's a bunch of heavily funded players now. I shouldn't go build in that space, but at the
[00:12:18] SPEAKER_02: same time when you look at some of these tabs, maybe we should have 10 times the amount of early stage
[00:12:24] SPEAKER_02: robotics companies getting started. It's extremely early. We work with, I'd say probably most of the
[00:12:30] SPEAKER_03: EuroBotics companies starting in the US and end abroad. If you're starting the robotics company,
[00:12:36] SPEAKER_03: reach out to us. We'd love to work with you. You can build the body, we'll build the brain, but yeah,
[00:12:41] SPEAKER_03: we need to see a lot more robotics companies, particularly in the US. That's awesome.
[00:12:46] I want to talk, did you ever interact with the Google ARM farm?
[00:12:50] SPEAKER_00: Yes, yeah. One of my co-founders actually started on the project.
[00:12:55] SPEAKER_01: I have a feeling. Do you have your own version of an ARM farm, or can you describe for people that
[00:13:01] SPEAKER_00: might not know what was the genesis of the ARM farm, what was the purpose, what was the takeaway,
[00:13:07] SPEAKER_00: and does every robotics company in ARM farm, or is it just you, and what will that look like in
[00:13:14] SPEAKER_00: the context of what you're building specifically? Yeah, so back then, that was a few years ago.
[00:13:21] SPEAKER_01: The idea was that robots to acquire those kind of skills to manipulate the world around them.
[00:13:26] SPEAKER_01: You can't really pre-scribe it. You can just code it all up. The world is too diverse. You can
[00:13:32] SPEAKER_01: have a lot of if statements describing what you should do in every single situation. They need to
[00:13:37] SPEAKER_01: learn it the same way as we do. The idea of the ARM farm was to set up many different stations where
[00:13:45] SPEAKER_01: you have static robots, static robotic arms where they just practice and they learn from experience.
[00:13:51] SPEAKER_01: In that particular case, they were trying to learn how to grasp objects. They just had a bin in front
[00:13:56] SPEAKER_01: of them with lots of different objects that were very diverse. The arm was just going down and trying
[00:14:00] SPEAKER_01: to figure out how to grasp it. Over a long period of time, the gutter did not experience to actually
[00:14:06] SPEAKER_01: learn from it and become really, really good at grasping objects. Remarkably,
[00:14:10] SPEAKER_01: it would be good. Way better than any pre-scribed systems that people design by hand.
[00:14:18] On one hand, it was a big success because of that. It was clear that this learning approach
[00:14:25] SPEAKER_01: is something that can truly work and understand the nature of grasping and truly nail that skill.
[00:14:30] SPEAKER_01: On the other hand, it was also disappointing in that it took really long time. It needed a lot
[00:14:35] SPEAKER_01: of data and especially a lot of data at the beginning was the arm wandering around and not knowing
[00:14:41] SPEAKER_01: what to do. It seemed like a lot of that time was wasted with the arm figuring out the simplest
[00:14:46] SPEAKER_01: things. One thing with PIO5 that we are really excited about is that we are now at the stage where
[00:14:54] SPEAKER_01: the robots get the sense of what they should be doing in that environment. They are no longer
[00:15:02] SPEAKER_01: in the space where you just arrive in a new home and you start moving your arms around,
[00:15:08] SPEAKER_01: not knowing what to do and hoping that you do something that is useful and then you learn from that.
[00:15:14] SPEAKER_01: You start at a point where you kind of know more or less what you can do. It works some of the
[00:15:19] SPEAKER_01: time. You just now need to get it to work every time and really, really well.
[00:15:24] Can you talk about the path or the importance of end-to-end learning in the context of robotics?
[00:15:33] SPEAKER_00: My understanding is that teleoperation is great and as long as it is economical, we should do it
[00:15:41] SPEAKER_00: and then having a deterministic code, like control system that is written in C++, that is also great
[00:15:48] SPEAKER_00: as long as it works. It is sometimes more debuggable. But the reason that we want to get to end-to-end
[00:15:54] SPEAKER_00: AI systems is that then you are on the scaling law, then you are just data bound and the more you
[00:15:59] SPEAKER_00: can manufacture, the more you can produce the actual robots, you are on this flywheel and you are now
[00:16:05] SPEAKER_00: bound by actual productive, you know, getting the cars on the roads, getting the robots into the world,
[00:16:13] SPEAKER_00: that will naturally create a flywheel. That is what everyone is hoping for in self-driving.
[00:16:18] SPEAKER_00: But what does that path look like now and how ridiculous is it to claim that end-to-end robotics
[00:16:25] SPEAKER_00: will be here by the end of the year or something like that?
[00:16:29] SPEAKER_01: So end-to-end robotics is already here. Everything we've shown so far is fully entilent
[00:16:34] SPEAKER_01: where you take camera input in and view other sensors and output actions directly.
[00:16:39] SPEAKER_01: Wow. I think there is another reason to do end-to-end learning, which is this is
[00:16:46] SPEAKER_01: something the only thing that has a chance of working. If there was a way to just pre-program your
[00:16:51] SPEAKER_01: robot and write a really good C++ code to do all kinds of different things like folding laundry,
[00:16:58] SPEAKER_01: we would have done it a long time ago. It's not for the lack of trying. Many people have tried it
[00:17:02] SPEAKER_01: for a very, very long time. The world is too complex. There are too many things that you will never
[00:17:08] SPEAKER_01: see. You will never predict and you can't really write that code. I think the only way to get there
[00:17:16] SPEAKER_01: is for AI to figure it out from experience. This is similar to what we've seen in language or
[00:17:23] SPEAKER_01: in vision where people have tried to write chatbots with writing different instructions and prescribing
[00:17:30] SPEAKER_01: logical steps of how you should proceed. But it turns out that the intelligence you need is much
[00:17:34] SPEAKER_01: more messy. You give it a lot of text and you let it figure out all the different patterns and
[00:17:39] SPEAKER_01: analogies. There is many, many more of them than the ones that we can express in code or in language.
[00:17:45] SPEAKER_01: I think something very, very analogous is going to happen here. That's what we start seeing.
[00:17:50] SPEAKER_01: The demonstrations that we've shown so far here at physical intelligence are of tasks that were not
[00:17:55] SPEAKER_01: possible before. It's like folding laundry. There is no program that I've ever seen that could do
[00:18:02] SPEAKER_01: that. The same with arriving in a new home and making the bed. There's just too many variables there
[00:18:08] SPEAKER_01: to do it any other way. Can you talk about some of the experiences that you both have had in your
[00:18:15] SPEAKER_00: careers, Google and Stripe in some ways big companies that maybe move slower than a small startup,
[00:18:21] SPEAKER_00: but at the same time, both of those organizations, I feel like the time from, hey, we're starting the
[00:18:26] SPEAKER_00: company too. We have a product that it wasn't a research organization for years.
[00:18:32] SPEAKER_00: What have you learned from those organizations? What are you taking into this experience?
[00:18:35] SPEAKER_00: Right. It really taught me everything I need to know about building a robotics research lab.
[00:18:41] SPEAKER_03: Just lessons, school or. I'd never worked in a research environment. I don't have
[00:18:48] SPEAKER_03: priors. I don't know what a research environment actually looks like. I just know our research
[00:18:52] SPEAKER_03: environment looks like I feel like we, whatever it looks like, maybe it operates exactly like
[00:18:58] SPEAKER_03: startups, like maybe grad programs or exactly like startups, but we feel like every other company I've
[00:19:03] SPEAKER_03: worked with that moves extremely quickly and has a clear set of goals and direction and just has
[00:19:08] SPEAKER_03: a bunch of people that work behind it and work extremely hard to solve whatever it is that we're
[00:19:12] SPEAKER_03: setting our minds towards and there's so much I learned from Stripe that informed that, but a lot
[00:19:19] SPEAKER_03: of it's just the obvious stuff, right? It's like higher exceptional people set a really high bar for
[00:19:25] SPEAKER_03: it. Don't compromise set a very clear set of goals for everyone, really aligned people. Actually,
[00:19:29] SPEAKER_03: I think that's one thing I really took from Stripe is you want an extremely aligned set of people.
[00:19:34] SPEAKER_03: I've never seen more alignment than I've seen in Pi. We talk about the alignment tax. When we're
[00:19:39] SPEAKER_03: bringing someone on, how much work is there to align them around our mission, our way of seeing the
[00:19:43] SPEAKER_03: world and almost everyone that joins, there's like basically nothing. Most of the people that work here
[00:19:49] SPEAKER_03: have dedicated their lives towards robotics or robotic learning or AI in some form or another,
[00:19:54] SPEAKER_03: hardware, whatever it might be. That just allows us to move so much quicker. It's like we need to
[00:19:58] SPEAKER_03: communicate a fraction of what the average company needs to communicate to someone. We don't really
[00:20:02] SPEAKER_03: need to inspire people or motivate them because they're so inspired and so self-motivated. I think
[00:20:08] SPEAKER_03: that's probably one of the things that's worked best for us today. How have you seen your customers
[00:20:14] SPEAKER_02: react to all the news and chaos around the tariffs? I think a lot of these companies are not in full
[00:20:21] SPEAKER_02: commercial production yet. It's not like, hey, we're no longer making money, but how are they
[00:20:26] SPEAKER_02: thinking kind of like long-term just given how much of the supply chain is based in Asia? Are there
[00:20:33] SPEAKER_02: opportunities for new US subcontractors and manufacturing companies to sort of service this new
[00:20:41] SPEAKER_02: industry? Yeah, the good thing is, I mean, good and bad. It's also subscale right now.
[00:20:47] SPEAKER_03: Most of the money is being spent on R&D rather than scale production. It's not as if there's
[00:20:52] SPEAKER_03: 100,000 robots that everyone's buying and it's now just twice as expensive. I think the good thing is
[00:20:58] SPEAKER_03: that given its subscale, there's a lot of time to build out US supply chains and it's putting a
[00:21:02] SPEAKER_03: lot of focus on figuring out can we get US actuators? Can we start to create companies that are developing
[00:21:09] SPEAKER_03: those? All the other critical supply elements in the supply chain. It's actually just getting
[00:21:14] SPEAKER_03: people into gear and maybe it's the right time for it. Can you talk a little bit about
[00:21:19] SPEAKER_00: what you're excited about on the data center side? Is there a moment where you're like really pulling
[00:21:25] SPEAKER_00: for Stargate to come together and we need the 100 gigawatt data center to crunch all of the data
[00:21:33] SPEAKER_00: that you've collected in a GPT-5 class training run? Or is that something that's so far out that
[00:21:42] SPEAKER_00: you'll always be able to just tag along on the residual capability from the large language model
[00:21:49] SPEAKER_00: labs? Yeah, we are not there yet in terms of having a full scaling law the same way as we've
[00:21:57] SPEAKER_01: seen for LLAM companies where you can just translate compute to progress. We're searching
[00:22:06] SPEAKER_01: really, really heavily for that. We are trying to figure out what is the recipe that could scale
[00:22:12] SPEAKER_01: like this but we are not there yet. We do at the same time generate a ton of data. I think that's
[00:22:18] SPEAKER_01: one thing that I realized since starting the company is that robots generate a ton of data and
[00:22:24] SPEAKER_01: you don't need that many to generate data that is close to the levels that LLAM companies use for
[00:22:30] SPEAKER_01: their models and there is no ceiling to it. The data robots can collapse. It's not like the internet.
[00:22:39] So I think over time it's quite likely that places are going to switch a little bit where most of
[00:22:46] SPEAKER_01: the models including LLAMs and BLM are going to be using real-world data collected through robots
[00:22:52] SPEAKER_01: because that's the data that has no ceiling and it's very active as opposed to just pass
[00:22:57] SPEAKER_01: observations of what people wrote on the internet. I think at that point probably the question
[00:23:03] SPEAKER_01: about data centers and compute is going to be a big one but for our models we are not there yet.
[00:23:09] SPEAKER_01: We are not bottleneck by, if only we had 100 times more compute everything would have worked so
[00:23:15] SPEAKER_01: much better. How do you guys think about demos long term? We joked on the show recently after
[00:23:22] SPEAKER_02: seeing the Chinese humanoid marathon. I want to see humanoid doing big wave surfing,
[00:23:28] SPEAKER_02: lift jumping. What point is that worth even doing or exploring just because of the amount of
[00:23:34] SPEAKER_02: attention that it would bring to the industry? What do you think we should demo? I think I'd like to see
[00:23:40] SPEAKER_02: one of your robot surf jaws. I want to see a robot do the 900 on a half pipe Tony Hawk style.
[00:23:48] SPEAKER_00: That was a really foundational moment in my childhood and American skateboarding.
[00:23:52] SPEAKER_00: Like really life or death stuff. Exactly. It's got to be high stakes. What about with hands?
[00:23:58] SPEAKER_03: What about manipulation? Juggling for sure. Rubik's cube for sure.
[00:24:02] SPEAKER_00: Juggling Rubik's cubes. You can do that. I can do the Rubik's cube. Jority can juggle.
[00:24:06] SPEAKER_00: We need to learn each other's skills so we can do both at the same time.
[00:24:11] SPEAKER_00: But yeah I mean these stunts when they're done right they can draw a bunch of attention.
[00:24:14] SPEAKER_00: Although you guys have plenty of attention I don't know if that's really what's
[00:24:17] SPEAKER_00: you. Yeah but it's an interesting thing where it's like you have the intention of the entire
[00:24:21] SPEAKER_02: industry but then at some point you need to basically inspire the next you know for many thousand
[00:24:27] SPEAKER_02: robotics companies. I would love to know about obviously with any AI project there's always the
[00:24:33] SPEAKER_00: public perception of like job displacement dystopia AI doom etc but when I look at the demo that
[00:24:39] SPEAKER_00: you just posted I'm like that thing is going to be fighting on my team in the singularity like this
[00:24:44] SPEAKER_00: is a friendly robot that will be defending me but how do you think about the like tuning the
[00:24:50] SPEAKER_00: language interaction so that it do you see a world where yes it's doing my laundry or making my
[00:24:58] SPEAKER_00: bed but if I happen to just also ask it I tell me about the news I can just have a chat with it.
[00:25:04] SPEAKER_00: Is that something that's even in your mind in terms of like human computer interaction?
[00:25:10] It's not a big focus of ours right now really we're so focused on on manipulation and economically
[00:25:16] SPEAKER_03: valuable tasks and more so than that the fundamental building blocks that we think gets us from
[00:25:21] SPEAKER_03: here at a physical intelligence. I think it's inevitable that everyone has robots in their homes
[00:25:25] SPEAKER_03: their workplaces just like in their lives and I think they'll want robots that are more useful
[00:25:30] SPEAKER_03: than just doing things whether it's companionship or like it's the best Amazon Alexa that can actually
[00:25:35] SPEAKER_03: then go like cook the recipe that you ask it for it's a place we focus around the interaction but
[00:25:41] SPEAKER_03: right now it's more understanding the intent of cleaning my kitchen and then breaking that down
[00:25:46] SPEAKER_03: in its tasks but it's pretty straightforward to go from do the thing to tell me about the thing
[00:25:52] SPEAKER_03: let's have a conversation about the thing and so it's on the horizon but not the greatest priority.
[00:25:57] SPEAKER_03: And one thing that says with the models we've been releasing they're actually built on top of
[00:26:02] SPEAKER_01: vision language models so the models that are truly what they call multi-model where you can
[00:26:08] SPEAKER_01: talk to it you can ask it what they see in the image and every now and then you can ask it to
[00:26:12] SPEAKER_01: perform actions too. That's cool. And what we what we start to realize is that all of these
[00:26:17] SPEAKER_01: different data sources contribute to each other they give you just like a bigger picture of what the
[00:26:22] SPEAKER_01: world is like and better understanding and it just turns out that robot actions is just like yet
[00:26:28] SPEAKER_01: another language that these models can speak and they just need to learn it and see
[00:26:32] SPEAKER_01: nothing examples of it. So the model that we have already is the model that you can talk to and
[00:26:37] SPEAKER_01: it works just as well as open source BLMs but on top of that it can also have that understanding
[00:26:45] SPEAKER_01: be very embodied and it and you know it understands what it's seasoned front of it and it's
[00:26:50] SPEAKER_01: so much deeper understanding what it knows how to how to move its arm to actually accomplish a task.
[00:26:55] We were kind of joking before the show about the obvious comparison between robotics and self-driving
[00:27:01] SPEAKER_00: cars but can you explain to me like I'm a five-year-old or like a venture capitalist like
[00:27:06] SPEAKER_00: why is that a bad analogy why don't you love that that analogy. I feel like it's it's not that
[00:27:12] SPEAKER_03: you don't love it it's just that it it can put you down a bunch of wrong directions. So there's
[00:27:18] SPEAKER_03: a lot of parallels but I mean even like the Waymo Tesla thing right like Tesla has this incredible
[00:27:26] SPEAKER_03: advantage with how much data they're collecting and passively yet Waymo is so much better
[00:27:31] so far and it has so many fewer cars on the roads there's useful things about it but there's also
[00:27:36] SPEAKER_03: aspects that that don't transfer in the analogy and it I think the like the reason why we were joking
[00:27:42] SPEAKER_03: about it is it's the number one question yeah we don't talk to many five-year-olds but investors and
[00:27:47] SPEAKER_03: VCs ask us and so we have to go down this rabbit hall where we're breaking down all the assumptions
[00:27:52] SPEAKER_03: and correcting some of them and validating some of them. I mean is that so should VCs if they're
[00:27:59] SPEAKER_00: looking at the robotics market just throw out that analogy entirely or they are set of robotics
[00:28:05] SPEAKER_00: companies that are in the Waymo category and there's a set of robotics companies that are in the
[00:28:08] SPEAKER_00: Tesla category and those are reasonable like an ontology to map to. Yeah no it's a there's a lot
[00:28:16] SPEAKER_03: of very useful stuff in the analogy. I think I think one thing that's interesting is that
[00:28:25] SPEAKER_03: there are all these self-driving companies that have died over the past 15 years and one thing that
[00:28:32] SPEAKER_03: we actually like to remind people is that this is not coming tomorrow. He logged on to Twitter
[00:28:37] SPEAKER_03: and you'll see all of these crazy robotic stamos most of them tell you operated or most of them being
[00:28:42] SPEAKER_03: like robots doing backflips which is a much easier problem than actually a robot folding laundry
[00:28:48] SPEAKER_03: and the thing we really try and remind everyone that looks at investing in us or is thinking about
[00:28:52] SPEAKER_03: investing in us is this is not a problem we're going to sell tomorrow. There's fundamental research
[00:28:56] SPEAKER_03: breakthroughs that that we need to make and much like self-driving how to it's what like a 15-year
[00:29:02] SPEAKER_03: arc at this point there is a very high likelihood that robotics is the same way. Like we we think our
[00:29:08] SPEAKER_03: greatest competition and science itself it's not like this company or that company it's just
[00:29:12] SPEAKER_03: maybe we can't pull it off in our lifetimes we think we'll be able to it's looking more and more
[00:29:16] SPEAKER_03: likely but it's it's not a tomorrow thing. I have one last question I know you enjoy food and cooking
[00:29:22] SPEAKER_00: what is the final eval the Mount Rushmore the Mount Everest of cooking that you expect will be the
[00:29:29] SPEAKER_00: last the last dish that a robot will be able to cook what's the hardest dish for a robot to cook
[00:29:35] SPEAKER_00: than Don Angie was on you oh yeah yeah okay so very difficult so so when when when when they cook
[00:29:41] SPEAKER_00: that when you guys achieved it's game over that's amazing uh there was actually a
[00:29:47] SPEAKER_00: nice AGI aGI benchmark someone shared a screenshot and it was a very old definition of AGI it's
[00:29:54] SPEAKER_00: said it'll be able to describe a sheep tell you three things that are larger than a lobster and all
[00:29:58] SPEAKER_00: of an AGI is here by that definition but one of the one of the things that it can't do is bake you a
[00:30:02] SPEAKER_00: cake uh and and we just thought it was funny that like that was the that was the last thing that the
[00:30:07] SPEAKER_00: the computer can't do um but maybe soon maybe future uh but thank you so much for coming on the show
[00:30:12] SPEAKER_00: great this is a fantastic conversation thanks for making the time guys. Best of luck to you and
[00:30:16] SPEAKER_00: and thank you so much for for building this this is really important technology. Yeah we're excited
[00:30:19] SPEAKER_00: put it put a robot in the studio yeah when you're ready set it over it's a mess I have clothes
[00:30:23] SPEAKER_02: all over here that need to be folded uh so we'd love to have one awesome to you guys. See you