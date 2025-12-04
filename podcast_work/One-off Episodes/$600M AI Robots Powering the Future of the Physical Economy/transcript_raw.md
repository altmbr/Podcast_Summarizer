# $600M AI Robots Powering the Future of the Physical Economy

**Podcast:** One-off Episodes
**Date:** 2025-09-25
**Video ID:** aY5694DIQnA
**Video URL:** https://www.youtube.com/watch?v=aY5694DIQnA

---

[00:00:00] Imagine this. You walk into a laundromat and a robot has been folding laundry nonstop for 24 hours.
[00:00:06] SPEAKER_00: That's what Jason and his team is working towards.
[00:00:08] SPEAKER_00: Fully autonomous, single-task, commercial-grade robots.
[00:00:12] SPEAKER_00: Which is just a fancier way of saying the robot does one thing very well without needing human
[00:00:17] SPEAKER_00: intervention. And they just raised $120 million in order to get there.
[00:00:21] SPEAKER_00: Now go is to power the future of the physical economy. Getting these robots to be very robust and
[00:00:26] SPEAKER_01: can sustain a long duration of actually doing a task.
[00:00:30] SPEAKER_01: This is a technical barrier that hasn't been really solved before our work.
[00:00:35] SPEAKER_01: Very important to have a good taste from what are the right problems that you should have your robots solve.
[00:00:42] SPEAKER_01: At the present moment, the bottleneck for useful robots is AI and software.
[00:00:47] SPEAKER_01: These humanoid right now, they are not actually very useful.
[00:00:50] SPEAKER_01: And the cost and the hardware readiness is a big factor.
[00:00:53] SPEAKER_01: The best way to succeed is to build research on the product at the same time.
[00:01:01] Quick thing before we get started. We have a lofty goal this year of hitting a thousand subscribers
[00:01:06] SPEAKER_00: in order to help more people build really great companies.
[00:01:09] SPEAKER_00: So if you enjoy the content, learn something new.
[00:01:12] SPEAKER_00: The best way to support us is by subscribing.
[00:01:15] SPEAKER_00: Okay, let's get into it.
[00:01:17] SPEAKER_00: Today's guest is Jason Ma, one of the brightest minds in robotics.
[00:01:21] SPEAKER_00: He's the lead author of multiple award-winning papers,
[00:01:25] SPEAKER_00: recognized internationally for his research.
[00:01:27] SPEAKER_00: He had offers to return to Google DeepMind and Video, Meta,
[00:01:31] but turned them all down to start dyno robotics.
[00:01:34] SPEAKER_00: And now, instead of chasing sci-fi humanoids,
[00:01:38] SPEAKER_00: robots that look and move like humans, he's building robots that actually work,
[00:01:43] SPEAKER_00: folding towels, stacking, packing in the real world.
[00:01:47] SPEAKER_00: So Jason, thank you for joining me at Founders in Motion today.
[00:01:52] Thank you, Thia. Thanks for inviting.
[00:01:54] SPEAKER_01: Really happy to be here and nice catching up with you after so long.
[00:01:58] SPEAKER_01: Yeah, this is an interesting change of scenery for us.
[00:02:01] SPEAKER_00: Jason, in very plain English, what is dyno robotics building?
[00:02:07] SPEAKER_00: A dyno, we're building general purpose robots that power the future of physical economy.
[00:02:13] SPEAKER_01: So the way I think about it is that we're developing AI-powered robots that can do any task
[00:02:19] SPEAKER_01: in any business or home scenario.
[00:02:21] SPEAKER_01: And to start out, we have deployed our robots using AI in many different scenarios,
[00:02:28] SPEAKER_01: such as restaurants, gyms, fitness centers, etc.
[00:02:31] SPEAKER_01: And our mission is to make this robot and our AI model as general as possible,
[00:02:36] SPEAKER_01: so you can basically do any task that you want it to do.
[00:02:40] So when it comes to robotics, there are kind of typically two approaches that people usually go for.
[00:02:46] SPEAKER_00: So the general purpose, every day, kind of companion supportive robot,
[00:02:50] SPEAKER_00: or the very fancy humanoid move and feel like humans.
[00:02:56] SPEAKER_00: So why did you decide to start with everyday tasks like folding towels instead of going after
[00:03:02] SPEAKER_00: kind of the overarching humanoid dream?
[00:03:05] Yeah, so our eventual goal is to develop a robot that can do any task right.
[00:03:10] SPEAKER_01: So to that, and perhaps at some point, we'll venture into humanoid robots?
[00:03:16] But it is our belief from our past experience and also research that
[00:03:20] SPEAKER_01: humanoid robots as hardware is not currently mature, and it's way too expensive.
[00:03:27] SPEAKER_01: But I think at the present moment, the bottleneck for useful robots is AI and software.
[00:03:34] SPEAKER_01: So we decided as a company to first focus on off-the-shelf hardware.
[00:03:38] SPEAKER_01: So basically, these are robots that you can buy off-the-shelf,
[00:03:43] SPEAKER_01: couple thousand dollars, and then we developed the AI on top of it, so you can be already useful.
[00:03:48] So you might have seen some of our demos, our robots can already fold napkins, fold clothes,
[00:03:53] SPEAKER_01: do packaging at very, very high success rate and robustness.
[00:03:57] SPEAKER_01: And I think that's a stepping stone towards developing like the more human-like
[00:04:03] form factory, if you will, because if you look at these humanoid right now, they are not actually
[00:04:07] SPEAKER_01: very useful, and you could only see them behind a screen instead of actually seeing the robots
[00:04:12] SPEAKER_01: in front of you. And the cost and the hardware readiness is a big factor.
[00:04:18] Yeah, that's super fair. And so folding laundry seems like a very simple task for humans.
[00:04:26] SPEAKER_00: Why is it actually so hard for a robot to do?
[00:04:29] SPEAKER_00: First, I think folding laundry is also a very challenging for humans.
[00:04:33] SPEAKER_01: For one, it's very mundane and tedious. I don't like doing my laundry and
[00:04:42] I think for cloth garments, they're coming all different shapes, types, shirts, jeans,
[00:04:48] SPEAKER_01: long sleeves, jackets. And what's really hard about robots? Why is this hard for a robot?
[00:04:54] SPEAKER_01: It exists for a couple of reasons. So one, just taking a step back, right?
[00:04:59] SPEAKER_01: Traditionally, you have robots as automation tool. You see robots in factory.
[00:05:05] SPEAKER_01: And what happens is you pre-program robots the exact sequence of motions, right?
[00:05:11] SPEAKER_01: So for instance, you want a robot to package into a box of things you want to deliver.
[00:05:17] SPEAKER_01: It's a pre-program sequence of motion. But that's actually very difficult to do for something
[00:05:23] SPEAKER_01: like folding laundry because your clothes is like deformable, right? The shapes are always
[00:05:30] SPEAKER_01: different. They're not in perfect rigid shapes and states. So it's really hard to pre-program
[00:05:35] SPEAKER_01: a sequence of motion to fold cloth for you. And what that means is you really need to develop
[00:05:41] SPEAKER_01: using generic AI tools, right? Just like a language model or chat GBT can really do anything
[00:05:48] SPEAKER_01: based on your language command. You want to develop AI models that can control robots to do very
[00:05:53] SPEAKER_01: fluid and dynamic motions, just like how human arms are very fluid and dynamic and do many
[00:05:59] SPEAKER_01: different motions to fold cloth. So that is why this task traditionally has been very difficult
[00:06:06] SPEAKER_01: for the preceding paradigm for robotics, where you pre-program the motions. And now it's actually
[00:06:13] more amenable for the new wave of robotics, which is learning robot actions through like data,
[00:06:19] right? You learn from data, yeah. Yeah. And if we take a moment to dive a little bit deeper into
[00:06:25] SPEAKER_00: the technology behind all of this, I guess at a high level, how do you think about training
[00:06:33] SPEAKER_00: these generative models to help robots recognize different outcomes in the real world?
[00:06:40] SPEAKER_00: Or a different in the real world? Yeah. So the way we train it is very much like how humans
[00:06:48] SPEAKER_01: interact with the physical world, right? So for us, we have our eyes that perceive the world
[00:06:55] SPEAKER_01: through vision through perception. And then we use our brain to turn these sensory image inputs
[00:07:02] SPEAKER_01: to our eyes into actions that are the arms and our legs perform, right? So very much for training
[00:07:09] SPEAKER_01: these robots, it's like we have cameras on the robots that perceive the physical world. And then
[00:07:13] SPEAKER_01: we train neural network to output actions. Like actions that command their robots joints and
[00:07:21] SPEAKER_01: different motors on the robots. So the way to do this is you collect input, output pairs of images
[00:07:27] SPEAKER_01: in and robot joins out, right? So you can basically control the robot to fold clothes many, many times
[00:07:35] SPEAKER_01: to collect data. And then that data gets fed into a model which then can control the robot
[00:07:41] SPEAKER_01: autonomously. So you're essentially kind of building your own general purpose data models and
[00:07:47] SPEAKER_00: data sets in order to train these folding laundry robots. Yeah, basically. Yeah, but you see the
[00:07:55] SPEAKER_01: paradigm here is fairly general, right? There's not a really specific laundry folding. So if you have
[00:08:02] SPEAKER_01: data that you collected for us a packaging for cooking a meal for cleaning your bedroom, then the
[00:08:09] SPEAKER_01: robot using the same algorithm can train models that can do these tasks. And what's really interesting
[00:08:15] SPEAKER_01: is they can actually just combine all the different data sets for different tasks into one model.
[00:08:21] SPEAKER_01: Then that model becomes very powerful, right? Just much like language models today. It's not just
[00:08:28] SPEAKER_01: one model that has one particular language task, but one model that can chat with you,
[00:08:33] SPEAKER_01: write code for you and do many other things. So that's like the vision that we're also trying to
[00:08:38] SPEAKER_01: do for robotics. But there's of course a lot of nuance, which we can get into later as well. Yeah.
[00:08:44] Yeah, super cool. I think I read on your research somewhere that there's a high adapt
[00:08:48] SPEAKER_00: adaptability from use cases from one to another. So the next use case should be trained at a lighter
[00:08:55] weight and then continuously forward. So you ran this super cool 24 hour nap contest nearly 800 folded
[00:09:03] SPEAKER_00: with 99% success rate for someone who's not technical. Why was that such a breakthrough?
[00:09:10] SPEAKER_00: The reason why that result was very difficult and very impressive in the research community,
[00:09:17] SPEAKER_01: robotics community is that we have seen you're probably have seen a lot of demos recently of robots
[00:09:23] SPEAKER_01: doing cool stuff. But typically what happens is that those demos are very brittle. It took many,
[00:09:28] SPEAKER_01: many shots to get even one video that works very well. So basically robots are now at a place you
[00:09:34] SPEAKER_01: can shoot fancy videos, but actually getting these robots to be very robust and can sustain a
[00:09:41] SPEAKER_01: long duration of like actually doing a task. This is a technical barrier that hasn't been really
[00:09:47] SPEAKER_01: sought before our work, especially for these highly dexterous, you know, complex manipulation tasks
[00:09:54] SPEAKER_01: such as for the laundry or for the inakins, right? And so that is why this result was very different
[00:10:00] SPEAKER_01: in that it's okay. It's a result where we across a span of a week, we shot many 24 hour video of
[00:10:07] SPEAKER_01: the robot just continuously folding napkins nonstop for 24 hours, hundreds of napkins folded without
[00:10:14] SPEAKER_01: much failure at all. And that was very different than prior works where yes, you can get a robot to
[00:10:21] SPEAKER_01: do a laundry folding demo, but the success rate is often like about 70% or 80% success rate. So that
[00:10:29] SPEAKER_01: means if you try to fold 10 t-shirts, it might only succeed eight times. So that's good enough for a
[00:10:34] SPEAKER_01: demo, but it's not good enough for actual real world deployment, right? Because you know, if you
[00:10:39] imagine your robot only succeed eight out of 10 times, so it will be a very frustratingly bad robot.
[00:10:44] SPEAKER_01: Right? So at Dynah, we are very much focused on not just putting off fancy demos, but actually
[00:10:50] SPEAKER_01: developing the AI technology to power like what actually can work in the physical world. Yeah.
[00:10:57] Yeah. And for anyone that is a little bit confused, it's okay, because I've printed all these terms
[00:11:02] SPEAKER_00: in case Jason ever mentioned them, but the exterior's manipulation is basically just teaching robots
[00:11:08] SPEAKER_00: to use their hands as flexibility as we do. So folding, gripping, managing weight, twisting,
[00:11:15] SPEAKER_00: without breaking things. And okay, while you were training the robot to get to this very high level
[00:11:23] SPEAKER_00: of success rate, what's like one funny or surprising failure that the robot had before it finally
[00:11:29] SPEAKER_00: nailed the test? For the napkin example in particular, what was very, very difficult is like actually,
[00:11:36] SPEAKER_01: so what happens at a real restaurant is like they'll ship you a stack of they'll give you a stack
[00:11:42] SPEAKER_01: of napkins for which you have to fold the napkins one by one. So the robot initially would make the
[00:11:48] SPEAKER_01: mistake of like pulling out many, many napkins from the stack. Right. And then now you have a whole
[00:11:56] SPEAKER_01: big mess on the table where tons of napkins are at the center of the table and then where you're
[00:12:03] SPEAKER_01: only supposed to fold one. So that was a very tricky scenario that the robot got into early on.
[00:12:08] SPEAKER_01: But you know, we were able to basically train the robot to handle those scenarios. So when
[00:12:14] SPEAKER_01: every grabs multiple napkins, then it would put the actual ends back onto the stack. But then that
[00:12:21] creates a pretty messy stack on the side. So the robot then had to figure out how to deal with that
[00:12:26] SPEAKER_01: situation. But eventually our robot was able to get around all these tricky scenarios and become
[00:12:31] SPEAKER_01: very, very good. But just from this example, you probably realized, you know, real world physical AI,
[00:12:38] SPEAKER_01: like embodied AI, you know, basically teaching robots to do things is actually very complex. If you
[00:12:44] SPEAKER_01: handle one scenario well, there might be other scenarios that you didn't expect that a robot has to
[00:12:50] SPEAKER_01: handle that concept. So it's kind of like, you know, walk and roll, you know, like just because
[00:12:55] SPEAKER_01: you handle one scenario doesn't really mean other hand scenarios handled very well, which is why
[00:13:00] SPEAKER_01: physical AI is often very, very challenging. And as our model got really, really good, another
[00:13:06] SPEAKER_01: video cases it pulls napkin too fast. So the napkin just slid off the table. But besides those scenarios,
[00:13:13] SPEAKER_01: yeah, the robot was pretty much like 100% infoting a napkin that's present in front of it.
[00:13:20] SPEAKER_01: There's so many different edge cases in the human world to deal with. And embody AI here is just
[00:13:27] AI inside of physical body. So like a robot arm that can see decide and act in the world. I wouldn't
[00:13:33] SPEAKER_00: say I'm technical, but like I need a little bit of technical stuff. So like, this is really fun
[00:13:38] SPEAKER_00: for like the nerd in me. So I also wanted to talk about that approach a little bit. So Dina one is
[00:13:46] SPEAKER_00: both the arm, so the body, the actual physical arm and the AI, the brain of it. So why is it so
[00:13:55] SPEAKER_00: important to kind of build them in conjunction almost rather than just like building like a general
[00:14:04] SPEAKER_00: purpose AI brain that can be applied for any different type of physical embodiment?
[00:14:10] SPEAKER_00: The way we think about this is that physical AI is extremely hard, especially if you're interested
[00:14:16] SPEAKER_01: in pushing real world performance, right? So if you think about like pushing real world performance,
[00:14:23] SPEAKER_01: then it's a matter of both the software and hardware. Like if your hardware like always breaks,
[00:14:30] SPEAKER_01: your robots are just not good enough, then you can't actually run a model AI model on the robot
[00:14:38] SPEAKER_01: for 24 hours, right? So previously when we when I was doing research in the lab, we often
[00:14:42] SPEAKER_01: ran to the issue that the robots would break after a couple hours or like you have to maintain it or
[00:14:48] SPEAKER_01: the robot would start overheating after like five or six hours. So it's just even physically not
[00:14:54] SPEAKER_01: possible to run for 24 hours. So from that simple thought exercise is probably more clear that
[00:15:01] SPEAKER_01: in order to get to any real world performance, you have to do a software hardware
[00:15:06] co-design co-ederation. But as I thought, you know, in Diner 1, the arms themselves were something
[00:15:13] SPEAKER_01: that we bought off the shelf, but we had to do a lot of things on top of it to make it more
[00:15:17] SPEAKER_01: durable, more, you know, just has higher endurance. So we could even try
[00:15:23] SPEAKER_01: running a model for 24 hours. And during the early days of the research, it's certainly the case that
[00:15:29] the model would do something like more violent, but maybe it would hit the table very hard. So that
[00:15:34] SPEAKER_01: makes it even more important that the hardware is good enough. But what I find interesting is that
[00:15:41] SPEAKER_01: traditionally robotics would have a lot of safety features or safety layer like your program
[00:15:47] SPEAKER_01: the robot to be safer. But in the AI age, what we found is that the robots are the models are more
[00:15:52] SPEAKER_01: intelligent. It actually just does more, you know, dexterous, smooth behavior. So it's much less
[00:16:00] SPEAKER_01: likely to even do the unsafe behavior in the first place. So that made hardware
[00:16:07] SPEAKER_01: reliability also just a much simpler problem than before. One point that you mentioned, I thought
[00:16:11] SPEAKER_00: super interesting, is that like even though you bought the hardware off the shelf, it still went
[00:16:16] SPEAKER_00: through a lot of iteration to ensure that it could even operate in 21st for 24 hours,
[00:16:24] SPEAKER_00: which kind of double ends the point of like maybe hardware is the bottleneck for humanoids and
[00:16:33] SPEAKER_00: that kind of more advanced application of robotics. Why did the team choose kind of an application
[00:16:38] SPEAKER_00: like folding laundry, folding napkins as the first test case use case to play with?
[00:16:45] SPEAKER_00: One is that like if you want to use a more AI like data driven approach to train robots,
[00:16:52] SPEAKER_01: then it's very important that you have a lot of data, right? Yeah. And folding clothes, folding
[00:16:57] SPEAKER_01: napkins is a scenario where you couldn't really like break the object that you are like teaching
[00:17:04] SPEAKER_01: a robot with. Right? Like, you know, clothes is like napkins are soft. So like you couldn't really
[00:17:11] SPEAKER_01: like mess it up, but yeah. There were other applications we looked into, for instance, like loading
[00:17:17] SPEAKER_01: dishes, right? There the safety risks are a lot higher. If the robot messes up a single time,
[00:17:24] SPEAKER_01: like it drops a dish, then the dish break. To advance model capability, we start out with some tasks
[00:17:30] SPEAKER_01: that has the feature where like you can just have the robots practice try many many times. And like
[00:17:36] SPEAKER_01: closed folding laundry was like the perfect scenario because once you fold it very nicely, you can
[00:17:41] SPEAKER_01: just like disturb it. So the cloth gets like crumpled again. So you can have the robot practice again,
[00:17:47] SPEAKER_01: if you will. Right? So that was from a technology perspective, very appealing, but from the business
[00:17:54] SPEAKER_01: side, it's also the case that there's a huge demand actually. Like we don't even think about
[00:17:58] SPEAKER_01: folding napkins in restaurants, but if you go to like, I don't know, like cheesecake factory,
[00:18:03] SPEAKER_01: apple vies of the world, there are just so many like napkins that need to be folded in the back
[00:18:09] office all the time. So it's almost like a full-time employees job. Like their whole job is to do that.
[00:18:15] SPEAKER_01: So we thought there's a huge need to like do this kind of tasks to get started. Yeah.
[00:18:21] SPEAKER_01: Yeah. I mean, I think folding napkins is a universal experience across all restaurants.
[00:18:27] SPEAKER_00: And also even folding laundry is such a pain too. I am also not a big fan of it. You've
[00:18:32] SPEAKER_00: moved from control tests to doing some kind of pilots in the real world. So when you move from like
[00:18:40] SPEAKER_00: a lab setting to say a local laundromat, what new challenges pop up? We didn't realize is that
[00:18:47] SPEAKER_01: in the office, first of all, like we have air conditioning so the room was like kind of cool,
[00:18:52] SPEAKER_01: but like in a lot of these real world scenarios, you know, you do not have control of the
[00:18:58] SPEAKER_01: temperature. So like overheating becomes more severe. You also don't have good control of the
[00:19:04] SPEAKER_01: network. Lundromats don't necessarily have the best Wi-Fi. So if you think about like running models
[00:19:10] SPEAKER_01: over cloud, then Wi-Fi becomes a bottleneck where if you're doing some data collection on site,
[00:19:16] SPEAKER_01: then uploading data also becomes a loss slower. And there is the operation challenge. Like how can
[00:19:23] SPEAKER_01: we trust to put a robot in a real customer site and not worry about something goes catastrophically
[00:19:29] SPEAKER_01: wrong? Right? For instance, like the robots for the napkin that back office, but you don't want it to
[00:19:33] SPEAKER_01: catch on fire by accident. And that's the hard part of robotics. It's not just like getting AI
[00:19:39] SPEAKER_01: to work. You also have to like make sure the deployment flywheel goes smoothly. For a business owner,
[00:19:45] SPEAKER_00: like how does the math work? How are you kind of thinking of pricing these robots and when do
[00:19:51] SPEAKER_00: they actually pay for themselves? A lot of these businesses are quite price sensitive or like they're
[00:19:56] SPEAKER_01: operating, you know, it's a spectrum, but let's say like, you know, restaurants are perhaps low-margin
[00:20:02] SPEAKER_01: businesses. So we realized that you order for the economics to make sense at all. Like your robots
[00:20:09] SPEAKER_01: have to be somewhat cheap, right? So this is also why like when you were mentioning humanos,
[00:20:15] SPEAKER_01: we don't think it's ready because any humanos you can buy or you, first of all, you can't buy them
[00:20:20] SPEAKER_01: any, but the ones you could buy are also in the order of like tens of thousand, 20,000, if not more,
[00:20:27] SPEAKER_01: right? But our robots are like a couple grand each. We do like a robotics service business model,
[00:20:32] SPEAKER_01: so we don't like actually sell the hardware. We just rent the hardware out to different customers,
[00:20:37] SPEAKER_01: several grand a month to rent our robot. So it's actually like a part, if not cheaper than like
[00:20:45] SPEAKER_01: typical labor cost in the United States. When you think about the next application for Dina,
[00:20:52] SPEAKER_00: where what is the team kind of actively testing with right now? Now, go is to power the future of
[00:20:58] SPEAKER_01: the physical economy. So basically, any task that we think is extremely mundane, dull,
[00:21:04] SPEAKER_01: dirty, dangerous for humans to do, we're looking into it. Looking into many different markets,
[00:21:10] SPEAKER_01: so of course hospitality, right? Like hotel restaurants were discovering use cases, then
[00:21:15] SPEAKER_01: the laundromats of the world, the logistic warehouses of the world, the most important thing
[00:21:21] SPEAKER_01: just like develop a general recipe. So we could actually just deploy our models to any scenario
[00:21:28] SPEAKER_01: that we want. Moving into a bit more about your founder journey. So you could have gone back to
[00:21:34] SPEAKER_00: DeepMind and video or meta. And if you only knew the eye popping number that they gave Jason,
[00:21:41] SPEAKER_00: but I don't think I can say. But instead, you chose the riskier founder path. What made you take
[00:21:49] SPEAKER_00: that leap? The best way to make impacting robotics is at a startup. Modeling is like extremely
[00:21:54] SPEAKER_01: complex problems. Not just a software problem. So you wanted to have the freedom, the velocity to do
[00:22:01] SPEAKER_01: other things required to get robots to work. And I firmly believe that getting robots to work
[00:22:06] SPEAKER_01: requires you to actually deploy the robots in realistic, real scenarios. Right? And I think that's
[00:22:13] SPEAKER_01: just not possible to do at a big corporate lab where robotics is like a research problem to them,
[00:22:21] SPEAKER_01: but not necessarily something they want to solve right away. Like all the companies you mentioned,
[00:22:26] SPEAKER_01: their core businesses are not robotics. And their core AI is not in robotics at the moment.
[00:22:31] SPEAKER_01: Right? You know, they're developing big language model, why not to power their platforms
[00:22:38] SPEAKER_01: by competing with, you know, let's say open AI and through the world. So robotics is more like
[00:22:42] SPEAKER_01: a research problem for them. But I felt that it's possible to actually get robots to work in the
[00:22:48] SPEAKER_01: real world with the right team, the right mindset. And you know, there's enough funding that's
[00:22:54] SPEAKER_01: willing to fund this kind of startup now. So I thought it would make a lot of sense to
[00:23:00] SPEAKER_01: start dying at. So you've always been kind of on the more research side. So moving into
[00:23:05] SPEAKER_00: startup and more of the business realm of things, what's one lesson that you've learned that
[00:23:10] SPEAKER_00: really surprised you? For robotics in particular, it's very important to have a good taste
[00:23:17] SPEAKER_01: for what are the right problems that you should have your robots solve. There are so many robotics
[00:23:21] SPEAKER_01: companies in the past that perhaps pick the problem that's too hard or like the too costly. So it's
[00:23:28] SPEAKER_01: actually very, very hard to penetrate the market and succeed as a business. And that's also,
[00:23:33] and hardware is also just in the expensive. So there's been a history of, you know, like,
[00:23:39] SPEAKER_01: you know, like venture capital don't really like find a hardware company for that reason.
[00:23:42] SPEAKER_01: In research, the most important thing in my opinion is also research taste. How do you pick a good
[00:23:47] SPEAKER_01: research problem to work on? What happened in the past is a lot of robotics company went really
[00:23:52] SPEAKER_01: deep in a vertical. So all their solutions, their software hardware style becomes very specialized
[00:23:58] SPEAKER_01: in that domain. So you cannot just go from one domain to the other. So that's the kind of thing
[00:24:03] SPEAKER_01: we don't want to do at Dina. What is like your two sentence pitch for why Dina is different from
[00:24:09] SPEAKER_00: other robotic companies? At Dina, we do both the research and also the product. And I think the
[00:24:14] SPEAKER_01: best way to succeed is to build research and product product at the same time. Right? So you can
[00:24:21] SPEAKER_01: think of let's say like, you know, a chat GVT, right? It's a product that you can use, right? But
[00:24:25] SPEAKER_01: there's also a lot of research that goes behind it to make it well. And I think the feedback
[00:24:29] SPEAKER_01: move from product to research and from research to product is what makes, you know, the existing AI
[00:24:36] SPEAKER_01: products in the market like so good and so sticky. So you're looking to robotics. There are
[00:24:42] SPEAKER_01: companies just purely trying to take some existing technologies and turning into a product. But I think
[00:24:47] SPEAKER_01: right now, the existing technology just as it is is not ready to get to general purpose like
[00:24:53] SPEAKER_01: manipulation, right? Like using arms hands to do things. But at the same time, if you're only focused
[00:24:59] SPEAKER_01: on research, then I think sometimes you're focusing on problems or like tasks that
[00:25:07] may not really be representative of the real world tasks. Because there's always a gap between
[00:25:11] SPEAKER_01: research and actually deployment. So as a researcher, you know, certainly in my research papers and all
[00:25:16] SPEAKER_01: that, all the tasks I were solving are like toy versions of the real world tasks. But at Dina,
[00:25:23] SPEAKER_01: we go straight to like the real version of the task. So we know that if our research is good enough
[00:25:27] SPEAKER_01: to solve those tasks, we can immediately turn them into product. That feedback move makes our
[00:25:32] SPEAKER_01: technology and business much more solid. Research is always theoretical. Like the name of it is
[00:25:37] SPEAKER_00: about being very theoretical. So iterating it within deployment and within testing is very
[00:25:43] SPEAKER_00: important to make it actionable. Throughout this journey, what has been the most valuable lesson
[00:25:49] SPEAKER_00: that you've learned, something that you really wish someone had told you earlier?
[00:25:53] SPEAKER_00: Building a startup is actually quite hard. Yeah, yeah. I think it's being here. I think it's
[00:26:00] SPEAKER_01: definitely harder than why I did my research for PhD. Because in PhD, I was really just
[00:26:07] SPEAKER_01: mining my own business, my own research. So like there's not that much else have to worry about
[00:26:12] SPEAKER_01: besides the existing research. For a company like Dina, we were really trying to develop like
[00:26:19] SPEAKER_01: full stack robotics, right? Going from hardware, software, AI, everything. Then there's always
[00:26:25] SPEAKER_01: many things moving at the same time. Not only just excel at what I already do, which is AI research,
[00:26:30] SPEAKER_01: but also coordinate collaborate with many different teams. And to make sure we're always being
[00:26:35] SPEAKER_01: able to prioritize the most important things in a company to allocate resources at CoDNA.
[00:26:40] SPEAKER_01: And I think that's definitely like a shifting gear compared to previously,
[00:26:45] while I was just doing my research. Shifting gears from like an independent contributor to like
[00:26:50] SPEAKER_00: a leader is always very hard. Okay, so Jason, the way that we like to end these things is we like
[00:26:59] SPEAKER_00: to play a quick game. So since you're on the frontier of robotics, I want our predictions.
[00:27:06] So in 10 years, who will be doing these jobs, robots are humans, flipping fast food burgers, robots,
[00:27:15] delivering packages to your door, robots or humus. I think you get the truth where you should be
[00:27:23] SPEAKER_01: able to choose. Teaching kids in classroom. Humans. Walking your dog. Humans. Or robots. I have
[00:27:34] SPEAKER_01: seen videos of robot dogs walking like real dogs. Performing surgery in a hospital.
[00:27:40] Humans. Surgery is where like safety is so important. And I think the precision required,
[00:27:46] SPEAKER_01: you know, there's a lot of research papers on surgical robots, but I feel that this is one area I
[00:27:53] SPEAKER_01: would be like very careful. So I would still trust a human surgeon that robots. Or maybe, you know,
[00:28:00] SPEAKER_01: maybe Dina will solve it one day. We don't know. We'll see. Yeah. We don't know. I mean, I'd also think
[00:28:06] SPEAKER_00: it's like depending on the application, right? Thank you so much for coming on the show. I really
[00:28:10] SPEAKER_00: enjoy the conversation, learning a lot more about robotics. Yeah, thank you for hosting and having me.
[00:28:15] That's a wrap. If you liked this episode, please hit the subscribe button. It helps us bring on
[00:28:19] SPEAKER_00: more awesome guests, level of production and drop new series you'll want to watch. See you in two
[00:28:25] SPEAKER_00: weeks. The robot's very meticulous. You'll fix all the like, it's going to try to bring the
[00:28:37] SPEAKER_01: sleeve out before it goes to the photo-instage. And sometimes it's very delicate. So the robot has to
[00:28:45] SPEAKER_01: try a couple times. Let's see if it recovers from that. Go robot.
[00:28:57] Yeah. Oh, there we go. Right. So it's going to stretch it out. So some of our people and police
[00:29:09] use their Facebook. So that's why here's a Facebook shirt. See you'll see. Yeah.
[00:29:23] SPEAKER_01: I think Fodilandry's hard. If I were to Fodilandry, it's not as good. Like this square, let me.