# No Priors Ep. 141 | With Sunday Robotics Co-Founders Tony Zhao and Cheng Chi

**Podcast:** No Priors
**Date:** 2025-11-20
**Video ID:** 4-VzXoZqAH0
**Video URL:** https://www.youtube.com/watch?v=4-VzXoZqAH0

---

[00:00:00] Nobody wants to do their dishes, nobody wants to do their laundry, people will love to
[00:00:09] Tony Zhao: spend more time with their family, with their loved ones.
[00:00:13] Tony Zhao: So what we believe in is that if the robot is cheap, safe and capable, everyone will
[00:00:18] Tony Zhao: want our robot.
[00:00:20] Tony Zhao: And we see a future where we have more than 1 billion of these robots in people's homes
[00:00:25] Tony Zhao: within the decades.
[00:00:26] Tony Zhao: Thanks, memo.
[00:00:35] Hi listeners, welcome back to No Pires.
[00:00:37] Unknown Host: Today we're here with Tony's Ow and Chang-Chi, co-founders of Sunday and Makers of Memo,
[00:00:42] Unknown Host: the first general home robot.
[00:00:44] Unknown Host: We'll talk about AI and robotics, data collection, building a full stack robotics company, and
[00:00:50] Unknown Guest: a world beyond toil.
[00:00:51] Unknown Guest: Welcome.
[00:00:52] Chang, Tony, thanks for being here.
[00:00:53] Unknown Guest: Thanks for having me.
[00:00:55] Tony Zhao: Okay, first I want to ask, where are we here?
[00:00:58] Unknown Guest: Because classical robotics has not been an area of great optimism over time or massive
[00:01:04] Unknown Guest: velocity of work.
[00:01:06] Unknown Guest: And now people are talking about a foundation model for robotics or a Chad GPD moment.
[00:01:11] Unknown Guest: Can you just contextualize the state of AI robotics and why we should be excited?
[00:01:15] Unknown Guest: I will say I think we're kind of in between the GPD moment and the Chad GPD moment.
[00:01:21] Tony Zhao: In the context of LMS, what it means is that it seems like we have a recipe that can
[00:01:28] Tony Zhao: be scout, but we haven't scaled up yet.
[00:01:31] Tony Zhao: And we haven't scaled up so much so that we can have a great consumer product out of
[00:01:35] Tony Zhao: it.
[00:01:36] Tony Zhao: So this is where I mean like GPD, which is like a technology and Chad GPD, which is
[00:01:40] Tony Zhao: a product.
[00:01:41] Tony Zhao: Yeah, I'm so we're seeing across academia.
[00:01:44] Cheng Chi: There's consensus around what's the method from manipulation, but everybody's talking
[00:01:49] Cheng Chi: about scaling up.
[00:01:50] Cheng Chi: It's like we know there's sign of life for the algorithms people are picking, but people
[00:01:55] Cheng Chi: don't know if we have more data like what happened to GPD 2, GB 3 will happen.
[00:02:01] Cheng Chi: And but we see a clear trend that no, there's no reason to believe that robotics doesn't
[00:02:05] Cheng Chi: follow the trajectory of other AI fields that know scaling up is going to improve performance.
[00:02:12] Unknown Guest: Maybe even if you took a step back, like what was the process for deploying a robot into
[00:02:17] Unknown Guest: the world like 10 years ago, like pre set of generalizable AI algorithms.
[00:02:22] Unknown Guest: Why was it so slow as a field?
[00:02:24] Unknown Guest: Yeah, so previously, you know, classical robotics have this sense plan act modular approach,
[00:02:31] Cheng Chi: where there's a human designing interface between each of the modules.
[00:02:34] Cheng Chi: And those army to be designed for each specific task and each specific environment.
[00:02:38] Cheng Chi: Yeah, academia that means for every task, that means a paper.
[00:02:42] Cheng Chi: So a paper is you design a task, design environment, and you design interfaces.
[00:02:47] Cheng Chi: And then you produce engine work for that specific task.
[00:02:50] Cheng Chi: But once you move on to the next task, you throw out your code, all your work and you
[00:02:53] Cheng Chi: start over again.
[00:02:54] Cheng Chi: And that's also kind of what happened to industry.
[00:02:57] Cheng Chi: So for each application, people build a very specific software and hardware system around
[00:03:01] Cheng Chi: it, but it's not really generalizable.
[00:03:03] Cheng Chi: And therefore, it's just feel like we're just running loops.
[00:03:06] Cheng Chi: We build a one system and then we build a next one, but there's like no synergy between
[00:03:11] Cheng Chi: them.
[00:03:12] Cheng Chi: So the progress has been somewhat slow.
[00:03:13] Cheng Chi: I feel like that's a good segue into some of the amazing research work that you guys
[00:03:17] Unknown Guest: have contributed over the last five years to the field.
[00:03:21] Unknown Guest: Should we start with diffusion policy?
[00:03:22] Unknown Guest: What was the impact of that?
[00:03:23] Unknown Guest: Yeah, so the field of policy is like specific algorithm for a paradigm called imitation
[00:03:28] Cheng Chi: learning.
[00:03:29] Cheng Chi: That's really like the most intuitive way of, you know, how to use machine learning for
[00:03:33] Cheng Chi: robotics.
[00:03:34] Cheng Chi: So you collect pair data of action observation of what the robot should do.
[00:03:38] Cheng Chi: You use that to train a model with supervised learning and then the robot do the same thing.
[00:03:42] Cheng Chi: The problem is that in the field is known to be very finicky.
[00:03:46] Cheng Chi: So when it comes to researchers, when I start into the field, people are like the researchers
[00:03:51] Cheng Chi: themselves, the specific researcher need to collect data so that there's exactly one way
[00:03:56] Cheng Chi: to do everything.
[00:03:58] Cheng Chi: Otherwise the robot either like use a model training with average or the robot behaves
[00:04:01] Cheng Chi: some weird way.
[00:04:03] Cheng Chi: The fusion model really allows us to capture multiple modes of behavior for the same observation
[00:04:10] Cheng Chi: in a way that still preserve training stability and that really kind of unlocked more scalable
[00:04:15] Cheng Chi: training and more scalable data function.
[00:04:17] Cheng Chi: So it doesn't have to be you personally wearing, you know, a teleopset in order to make a robot
[00:04:22] Unknown Guest: learn.
[00:04:23] Unknown Guest: Yeah, so like we can have multiple people sometimes even and train people collecting data
[00:04:27] Cheng Chi: and the result will still be great.
[00:04:29] Cheng Chi: Where do Aloha and act plan to this?
[00:04:32] Unknown Guest: Yeah, so these two papers are actually like super close each other.
[00:04:35] Tony Zhao: They're like one month or two months away.
[00:04:37] Tony Zhao: That's actually how me and Trinno each other.
[00:04:39] Tony Zhao: It was about looking at each other's paper like and we met on Twitter, I think, when
[00:04:44] Tony Zhao: Trinns back in Columbia.
[00:04:45] Tony Zhao: Before Aloha, I think the typical way people collect data is with a like polyoption setup
[00:04:53] Tony Zhao: with we are hasent and it turns out to be very unintuitive to do and it's hard to collect
[00:04:58] Tony Zhao: data that is actually dexterous.
[00:05:00] Tony Zhao: Well, Aloha brings this a very simple and reproducible setup.
[00:05:03] Tony Zhao: So it's very intuitive.
[00:05:04] Tony Zhao: Sorry, in terms of just for most people who haven't worn a teleopset up, is it the lag?
[00:05:09] Unknown Guest: Is it like just, you know, how should I compare it to like playing a video game or something?
[00:05:13] Unknown Guest: Yeah, I think Aloha make it feel more like playing a video game.
[00:05:17] Tony Zhao: Normally it feels kind of disconnected that you're just like moving in the free air and
[00:05:21] Tony Zhao: Aroha is moving with some delays, but Aloha reduces that delay by a lot and that contribute
[00:05:27] Tony Zhao: to the smoothness and how fast human can react.
[00:05:31] Tony Zhao: Like once we got those really dexterous data, what allows us to do is to investigate
[00:05:37] Tony Zhao: on algorithms that are actually solving things that are difficult.
[00:05:42] Tony Zhao: In this case is through the introducing of trans, using transformers in the case of robotics.
[00:05:48] Tony Zhao: And there was a long period of time that I think robotics was stuck with a failure MLP's
[00:05:54] Tony Zhao: and covenants and as you make it deeper, it works worse.
[00:05:58] Tony Zhao: But it turns out that once you have very strong and dexterous data sets, like just through
[00:06:04] Tony Zhao: a transformer edit and it works quite well.
[00:06:06] Tony Zhao: Actually, like just in terms of progress of the industry over time, transformers are
[00:06:11] Unknown Guest: going to make sense without a certain level of data collection, capability, okay.
[00:06:14] Unknown Guest: And also, also, the system around it, for example, action chunking, which is to predict
[00:06:18] Tony Zhao: a trajectory as opposed to projecting single-sampus fractions.
[00:06:22] Tony Zhao: All these things kind of combined to make dexterous tasks by manual tasks more scalable.
[00:06:28] Why is chunking important here if I think about like just the analogy to LMS and like
[00:06:34] Unknown Guest: text sequence prediction?
[00:06:35] Unknown Guest: I think it just kind of throws the amount off if you're trying to force it to react every
[00:06:41] Tony Zhao: millisecond.
[00:06:42] Tony Zhao: That's not how human act.
[00:06:45] We perceive and we can actually move quite a bit without looking at things again.
[00:06:51] Tony Zhao: That turns out to make things the motion a lot more consistent and or performance to
[00:06:55] Tony Zhao: be a lot better.
[00:06:57] And you discovered that actually transformers are potentially did apply through a lot of
[00:07:01] Unknown Guest: products.
[00:07:02] Unknown Guest: Cheng, you felt then that data collection was still a problem.
[00:07:05] Unknown Guest: So enter Oomi.
[00:07:06] Unknown Guest: Yeah.
[00:07:07] Cheng Chi: So after a low-ha and a digital policy, I was super excited about imitation learning.
[00:07:12] Cheng Chi: But at the time, most of us start still doing catalymperation and that just feel super
[00:07:17] Cheng Chi: limiting.
[00:07:18] Cheng Chi: The problem is that you know, the interest set up at a time like a patty op set up.
[00:07:23] Cheng Chi: It takes a piece of student couple of hours to set up in the lab.
[00:07:27] Cheng Chi: It pretty much restrict data collection to a lab.
[00:07:29] Cheng Chi: But in order for the robot to actually work as a product, it needs to be worked in the
[00:07:33] Cheng Chi: wild in on scene environments that requires the data to be also collected in the wild.
[00:07:39] Cheng Chi: And at the time I was thinking, okay, is there a way we can collect robotic data without
[00:07:43] Cheng Chi: actually using a robot?
[00:07:45] Cheng Chi: Like fourth means to think, okay, what's the actual most essential part of a robotic
[00:07:49] Cheng Chi: data?
[00:07:50] Cheng Chi: And after the field of policy and act, actually the paradigm is kind of simple.
[00:07:54] Cheng Chi: You just need paired observation and action data.
[00:07:57] Cheng Chi: In our case, observation is the video clip.
[00:07:59] Cheng Chi: The action is the movement of your hand plus how the finger moves.
[00:08:04] Cheng Chi: I realized that all of these information you can get from a GoPro.
[00:08:07] Cheng Chi: You can track the movement of GoPro in space and you can track the motion of the grip
[00:08:14] Cheng Chi: and also finger through images as well.
[00:08:17] Cheng Chi: And that's why I built this Umi Gryppur and 30 printed.
[00:08:21] Cheng Chi: At the time, the product had three peachy students.
[00:08:23] Cheng Chi: We just took the Gryppur everywhere.
[00:08:25] Cheng Chi: I think there's two weeks before the paper deadline.
[00:08:29] Cheng Chi: Every time it goes to a restaurant, before the weather comes in, we just collect some
[00:08:32] Cheng Chi: data.
[00:08:33] Cheng Chi: And very quickly, we got, I think, 1,500 video clips of this like, express or cop serving
[00:08:40] Cheng Chi: task.
[00:08:41] Cheng Chi: And that turns out to be one of the biggest data sets in your robotics and just simply
[00:08:45] Cheng Chi: by three people.
[00:08:46] Cheng Chi: And that's like how that's where the power kind of shines.
[00:08:49] Cheng Chi: And then with that amount of data allows to train the first end to end model that can
[00:08:55] Cheng Chi: actually generalize to unseen environments.
[00:08:57] Cheng Chi: So we can push the robot around in Stanford.
[00:08:59] Cheng Chi: Actually Tony was there as well.
[00:09:01] Cheng Chi: Push the robot around the Stanford campus and then anywhere the robot can serve you to
[00:09:06] Cheng Chi: drink.
[00:09:07] Tony Zhao: Yeah, I think that is the moment I was like, hey, maybe we should start the company.
[00:09:11] Tony Zhao: This is actually working so well.
[00:09:13] Tony Zhao: I remember like just falling in town and the times that doesn't work well.
[00:09:17] Tony Zhao: I think the only exception I saw was when it's under direct sunlight.
[00:09:21] Tony Zhao: Yeah.
[00:09:22] Tony Zhao: And I think the reasoning was like over that whole like two, three weeks of data, that
[00:09:26] Tony Zhao: two weeks is already.
[00:09:27] Cheng Chi: So there's no sunlight data.
[00:09:29] Cheng Chi: So like it fails.
[00:09:30] Cheng Chi: That also demonstrated importance of distribution matching.
[00:09:33] Cheng Chi: So in order for robot to work in a sunny environment, it must have seen sunny environments
[00:09:38] Cheng Chi: training training data.
[00:09:39] Cheng Chi: Yeah, it's really interesting because I remember when I first met you guys, it was like
[00:09:42] Unknown Guest: you spent like, I don't know, $200,000 across all of your academic research.
[00:09:48] Unknown Guest: And yet the scale of data collection as translated to model capability is leading.
[00:09:54] Unknown Guest: Right.
[00:09:55] Unknown Guest: So it's very interesting that we look at where we are, maybe going back to Tony's point
[00:10:00] Unknown Guest: of scaling and massive capital deployment.
[00:10:04] Unknown Guest: But that entire paradigm actually wasn't relevant before people realized like you should
[00:10:09] Unknown Guest: train on all of the internet data.
[00:10:11] Unknown Guest: And we just don't have that in robotics.
[00:10:13] Unknown Guest: So the entire field is just blocked on having any scale of data that's relevant.
[00:10:16] Unknown Guest: Yeah.
[00:10:17] Tony Zhao: I think DCs are so like assuming the base about like what is even the right way to scale.
[00:10:22] Tony Zhao: They're like role models, they're assimilations, there is teleoperation.
[00:10:26] Tony Zhao: They're like all these new ideas.
[00:10:28] Tony Zhao: And I think this is the sort of area that we really want to innovate that we want to differentiate.
[00:10:34] Tony Zhao: We want to find out something that is both high quality and scalable.
[00:10:38] Tony Zhao: And then you guys, you decide to start a company pushing this cart around Stanford.
[00:10:42] Unknown Guest: Tell me about that decision and congratulations on the launch and sort of the direction in
[00:10:47] Unknown Guest: team you've got.
[00:10:48] Unknown Guest: Yeah.
[00:10:49] Tony Zhao: It's a very interesting journey.
[00:10:51] Tony Zhao: I remember in the beginning of society, two of us in terms of apartment on his desk,
[00:10:56] Tony Zhao: we were like clamped a robot there and tried to do some tasks.
[00:10:59] Tony Zhao: And I soon become like, I think an eight person team who was the end of 2024.
[00:11:06] Tony Zhao: And now we're around like 30 to 40 people.
[00:11:08] Tony Zhao: We're not the best at everything, right?
[00:11:10] Tony Zhao: But certainly a company allows us to find people who really love working with and then
[00:11:14] Tony Zhao: bring all the expertise together from the kind of engineering supply chain, like software
[00:11:19] Tony Zhao: engineering, like controls, and to build a system together that is not like a demo, but
[00:11:25] Tony Zhao: a real product.
[00:11:27] Tony Zhao: To build this amazing team, what are people actually signing up for?
[00:11:29] Unknown Guest: What's the mission of Sunday?
[00:11:31] Tony Zhao: Yes, it is to play a home robot in Erwa's home.
[00:11:34] Tony Zhao: I think there are a lot of AIs trying to make you more efficient during the work, but
[00:11:39] Tony Zhao: there is not enough AIs that actually helps you with all these mundane things that are
[00:11:43] Tony Zhao: not creative that really has nothing to do with what's making us more intrinsically
[00:11:48] Tony Zhao: human.
[00:11:49] Tony Zhao: What's ideal for people to spend more time on is actually with their hobbies, with their
[00:11:53] Tony Zhao: passions, as opposed to spending more time doing chores.
[00:11:57] Unknown Guest: So if you guys are going from these amazing research breakthroughs to we're actually going
[00:12:03] Unknown Guest: to ship a home robot, and that's a product you have to talk about, cost and capability
[00:12:08] Unknown Guest: and robustness, like what's the design philosophy?
[00:12:11] Unknown Guest: As these AIs models become more capable and as hardware costs continue to go down, the
[00:12:18] home robots, all kinds of robots will be everywhere.
[00:12:22] Tony Zhao: So if you start from the most surface level, which is design of the robots, when we
[00:12:26] Tony Zhao: design it, we think about what should the robot look like if it is ubiquitous?
[00:12:32] Tony Zhao: You need to see it every single day.
[00:12:35] Tony Zhao: What should it look like?
[00:12:37] And what we end up with is that we really think the robot should have a face.
[00:12:41] Tony Zhao: It should have a cute face, and it should be very friendly.
[00:12:45] Tony Zhao: So instead of like a terminator doing your dishes, we want the robot to feel like it's
[00:12:49] Tony Zhao: out of a cartoon movie.
[00:12:51] Tony Zhao: And then the huge decision is like how many arms do the robot have?
[00:12:56] Tony Zhao: Should they have like four arms?
[00:12:57] Tony Zhao: Should they have like one arms?
[00:12:58] Tony Zhao: Should they have legs?
[00:12:59] Tony Zhao: Should they have like five fingers, two fingers, two fingers?
[00:13:02] Tony Zhao: It's a huge space.
[00:13:03] Tony Zhao: Why is it the obvious answer?
[00:13:05] Unknown Guest: It should just be like a full human.
[00:13:07] Tony Zhao: I think the core motivation for us is how can we build a useful robot as soon as possible?
[00:13:14] Tony Zhao: So whenever we see something that we can accelerate it with simplification, we'll go simplify
[00:13:19] Tony Zhao: that.
[00:13:20] Tony Zhao: So one example of that is the hand that we designed, which has three fingers.
[00:13:25] Tony Zhao: We kind of combine the three of the fingers that we have together.
[00:13:29] Tony Zhao: And the reasoning there is just that most of the time when we use those fingers, we use
[00:13:33] Tony Zhao: it together.
[00:13:34] Let it be like grasping a handle, let it be opening the dishwasher.
[00:13:37] Tony Zhao: So it really doesn't make sense to add the cost, like multiply by three X to have separate
[00:13:44] Tony Zhao: it into three, and we can do one with most of the benefits.
[00:13:48] Tony Zhao: So this is how we think about the whole robot as well.
[00:13:51] Tony Zhao: It's kind of with the constraint that we're building a general-purpose robot that can eventually
[00:13:55] Tony Zhao: do all your chores and will simplify everything we possibly can so that the robot can be as
[00:14:00] Tony Zhao: low cost and as easy to repair as possible.
[00:14:03] Tony Zhao: Yeah, just want to add a little bit more to the I-Freeter and the mechanical design.
[00:14:08] Cheng Chi: Traditionally, most robots are designed for industrial use cases.
[00:14:11] Cheng Chi: And the robot are very fast.
[00:14:13] Cheng Chi: They are very stiff and never precise.
[00:14:15] Cheng Chi: The reasons because all the industrial robots are blind.
[00:14:18] Cheng Chi: So they're blindy flowing a trajectory that's programmed by someone.
[00:14:21] Cheng Chi: It's not a reaction to perception.
[00:14:23] Unknown Guest: Correct.
[00:14:24] Cheng Chi: But because of the brakes we have in AI, like now robots have eyes.
[00:14:28] Cheng Chi: So it can actually correct this own mechanical and hardware inaccuracies.
[00:14:33] Cheng Chi: So that kind of opened up a new different space of design.
[00:14:37] Intuitively, it should be like, I can't tell you exactly what the distance is that you're
[00:14:41] Unknown Guest: on a millimeter scale, but I'm going to get to the cup because I can stop.
[00:14:45] Yeah, exactly.
[00:14:45] So that allows us to use these low cost actuators that's cheap, that's compliant, but they're
[00:14:52] Cheng Chi: in precise.
[00:14:53] Cheng Chi: But because of the AI's algorithms and systems we build, it allows us to build robots as mechanically
[00:14:59] Cheng Chi: inherently safe and compliant.
[00:15:00] Cheng Chi: While simultaneously, we'll be able to achieve the sufficient accuracy we need for the home
[00:15:04] Cheng Chi: tasks.
[00:15:05] Where are we in that timeline?
[00:15:06] Unknown Guest: You said we're between GPT and chat GPT.
[00:15:10] Unknown Guest: And so like when do consumers get chat GPT and when will you guys ship something?
[00:15:14] Unknown Guest: Yeah, it's actually really exciting time because we have so many prototypes internally.
[00:15:19] Tony Zhao: What we will do next year, 2026 is actually start doing beta programs.
[00:15:24] Tony Zhao: We'll have these robots, all kinds of different ones, into people's home and see how they react
[00:15:29] Tony Zhao: to it.
[00:15:30] Tony Zhao: That will be when we learn the most about like how people like people want to talk to
[00:15:34] Tony Zhao: a robot.
[00:15:35] Tony Zhao: If you go want to have the robots, maybe teach their kids some new knowledge about the
[00:15:42] Tony Zhao: world.
[00:15:43] Tony Zhao: And this will inform us what the eventual product should look like.
[00:15:47] Tony Zhao: Internally, we just have an extremely high standard of what is the minimal consumer
[00:15:53] Tony Zhao: product we want to ship.
[00:15:54] Tony Zhao: It needs to be extremely safe.
[00:15:55] Tony Zhao: It needs to be extremely capable and low cost.
[00:15:58] Tony Zhao: Do you feel like you know something now that you didn't when you started the company?
[00:16:02] Unknown Guest: Absolutely.
[00:16:03] Tony Zhao: So I think at the beginning of the story, as we see light at the end of the tunnel of
[00:16:09] Tony Zhao: their two axes, their sexuality, their externalization, we add more data, things works better.
[00:16:14] Tony Zhao: And what this company about is the cross product of these two.
[00:16:18] Tony Zhao: How can we scale and have both the Xerity and generalization?
[00:16:23] Tony Zhao: And this is something we're able to show in our generalization demo, which is like we
[00:16:26] Tony Zhao: can pick up these like very precise like forks, like actual metallic forks, only ceramic
[00:16:32] Tony Zhao: plates with very high success rates.
[00:16:35] Tony Zhao: And honestly, this is not something that like we thought that would work so easily just
[00:16:41] Tony Zhao: by having so much more data.
[00:16:42] Tony Zhao: Yeah, so actually just want to expand a little bit.
[00:16:45] Cheng Chi: You know, it's actually the process was long and painful.
[00:16:49] Cheng Chi: So, yeah, there's so many issues like just scaling up a system.
[00:16:54] Cheng Chi: Robotics is very, very hard.
[00:16:56] Cheng Chi: There are mechanical issues like reliability issues.
[00:16:59] Cheng Chi: There's like data, you know, quality issues that come out of it.
[00:17:03] Cheng Chi: In the beginning, I actually thought it's going to be much easier than this.
[00:17:07] Cheng Chi: But really, it just takes time and effort to grind out all the little details for this
[00:17:11] Cheng Chi: to work.
[00:17:12] Cheng Chi: I also actually compared to Teddy Albus much harder to get this system scaled up.
[00:17:16] Cheng Chi: But once the scaled up is very powerful, very repeatable.
[00:17:18] Cheng Chi: So it is both harder than you thought it would be to get to here and you are further
[00:17:22] Unknown Guest: than you thought you would be.
[00:17:24] Unknown Guest: And I remember in the beginning, we're having this like funny conversation of where
[00:17:29] Tony Zhao: like if we built this, someone can just like take our glove and they'll build the same
[00:17:34] Tony Zhao: thing.
[00:17:34] Tony Zhao: Like, well, we'll do it half.
[00:17:36] Tony Zhao: Are we worried about that?
[00:17:37] Tony Zhao: And at the beginning, actually, we are a little bit worried because we thought like,
[00:17:40] Tony Zhao: you know, they can probably just replicate it.
[00:17:43] Tony Zhao: But as we go along the path, it turns out things are so much harder than we thought.
[00:17:47] Tony Zhao: It will have so many the small, small, yeah.
[00:17:50] Cheng Chi: Yes.
[00:17:51] Cheng Chi: And when you say scaling up a robotic system, you mean the data collection to training pipeline
[00:17:56] Unknown Guest: and the hard work itself.
[00:17:57] Unknown Guest: Yeah.
[00:17:57] Unknown Guest: So I actually like for the, yeah, for this to work at all, you know, the declaration system,
[00:18:02] Cheng Chi: yeah, need the robotic and control system to be able to deliver the hand to where we want
[00:18:05] Cheng Chi: to go.
[00:18:06] Cheng Chi: Yeah.
[00:18:06] Cheng Chi: And you also need the data filtering pipeline and data cleaning pipeline and the training
[00:18:11] Cheng Chi: pipeline.
[00:18:12] Cheng Chi: And all these things need to be iterated together.
[00:18:14] Cheng Chi: So actually gone to several loop of these is kind of hard to imagine without having a
[00:18:18] Cheng Chi: full stack team in the house.
[00:18:20] Cheng Chi: How does it kind of even be done?
[00:18:21] Cheng Chi: Yeah.
[00:18:22] Tony Zhao: The glove we're using right now is we call it like V5.
[00:18:26] Tony Zhao: And for V0 to V5, each version has like around 20 iterations.
[00:18:30] Tony Zhao: Okay.
[00:18:31] Unknown Guest: And so 100.
[00:18:33] Unknown Guest: Yes.
[00:18:34] Tony Zhao: And also like just when you make these as scale right now, we have more than 500 people
[00:18:39] Tony Zhao: using these golfs in the wild.
[00:18:41] Tony Zhao: Like all the things that could go wrong will go wrong.
[00:18:45] Tony Zhao: For example, they did they did.
[00:18:46] Tony Zhao: Yes.
[00:18:47] Tony Zhao: For example, like how things are assembled.
[00:18:50] Tony Zhao: If you don't specify exactly how it should be done, people will assemble it in creative
[00:18:55] Tony Zhao: ways.
[00:18:56] Tony Zhao: And the creativity doesn't help us here because I really want the data collection device
[00:19:00] Tony Zhao: to be extremely present.
[00:19:02] Tony Zhao: So you guys can't obviously know everything that's happening in every company in academia
[00:19:07] Unknown Guest: industry.
[00:19:08] Unknown Guest: But from what you know, how would you compare the scale of training data that you have today
[00:19:14] Unknown Guest: relative to the industry?
[00:19:16] At this point, we are almost 10 million trajectories being collected in the wild.
[00:19:23] Tony Zhao: And those trajectories are not just like, oh, pick up a cup.
[00:19:26] Tony Zhao: These long trajectories with like walking with navigation and then like doing this long
[00:19:32] Tony Zhao: horizon tasks.
[00:19:33] Tony Zhao: Tony, as you mentioned, like it's an open question actually what the right way to scale
[00:19:39] Unknown Guest: data up is.
[00:19:40] Unknown Guest: And so there are strong theories around teleop around like pure RL around video and world
[00:19:46] Unknown Guest: models.
[00:19:47] Unknown Guest: Like how did you think about all of these?
[00:19:50] Yeah.
[00:19:51] Cheng Chi: So from our perspective, actually it's kind of civil surprising.
[00:19:53] Cheng Chi: So in the beginning, we worried that the data from glove or only like data has higher
[00:19:58] Cheng Chi: quantity, but lower quality compared to teleop.
[00:20:01] Cheng Chi: Because of teleop, you're using exactly the same hardware software stack between training
[00:20:04] Cheng Chi: and testing is perfectly distribution match.
[00:20:07] Cheng Chi: But what we realized is actually, you know, this glove form factor encouraged people to do
[00:20:12] Cheng Chi: more text version, more natural movement.
[00:20:14] Cheng Chi: And those actually result in a more intelligent behavior on the modeling side.
[00:20:20] Cheng Chi: But in terms of data quality, we don't really see a difference in terms of how much like
[00:20:25] Cheng Chi: there's a gap between teleop and glove data.
[00:20:28] Cheng Chi: After we did the 20 engineering life service life.
[00:20:33] Tony Zhao: Yeah.
[00:20:34] Tony Zhao: Yeah.
[00:20:35] Tony Zhao: Like apparently there is a mismatch, right?
[00:20:37] Tony Zhao: That's in the camera frame, there's a human is out of the robots.
[00:20:41] Tony Zhao: And there are just a lot of things that we need to do to kind of convert a human data one
[00:20:47] Tony Zhao: to one to like as if it is robot data and have the model not being able to tell you
[00:20:51] Tony Zhao: the difference.
[00:20:52] Tony Zhao: Yeah.
[00:20:53] Cheng Chi: And that kind of relies on again, the whole the full cycle iteration between hardware and
[00:20:57] Cheng Chi: software.
[00:20:58] Cheng Chi: What about RL?
[00:20:59] We see a lot of great promise for RL in local motion.
[00:21:03] Cheng Chi: And you know, we think that will continue to be true for local motion.
[00:21:06] Cheng Chi: So what we see really felt like RL is a method is very powerful.
[00:21:10] Cheng Chi: But it is much less sample efficient compared to imitation learning.
[00:21:14] Cheng Chi: And we see that to work great in environments where it's easy to simulate.
[00:21:18] Cheng Chi: For the case of local motion, you only need to worry about rigid body dynamics and
[00:21:23] Cheng Chi: rigid body contact between the robot and the ground.
[00:21:26] Cheng Chi: And you know, because you engineer a robot, you know, everything.
[00:21:29] Cheng Chi: But for manipulation, it's kind of hard for us to imagine like have does actually the
[00:21:34] Cheng Chi: same amount of diversity and the distribution of real object in terms of matching both
[00:21:41] Cheng Chi: appearance and physical properties.
[00:21:45] Cheng Chi: And we think that it's going to be challenging compared to a global collection and tell
[00:21:49] Tony Zhao: you.
[00:21:50] Tony Zhao: Yeah.
[00:21:51] Tony Zhao: I think it's really about which method can get us there faster.
[00:21:54] Tony Zhao: There might be different methods that will eventually get there.
[00:21:57] Tony Zhao: For example, like, you know, simulation world model, right?
[00:22:01] Tony Zhao: And like it's almost a technology to say that if I have a perfect world simulator, anything
[00:22:07] can be done there.
[00:22:08] Tony Zhao: Like as long as you can do in a real world, you can do it in a simulation.
[00:22:12] Tony Zhao: And you can like, you know, cure cancer in a simulator, right?
[00:22:15] Tony Zhao: But what it turns out for robotics is that some, some things are harder than others.
[00:22:21] Tony Zhao: And it really depends on the problem itself.
[00:22:24] Tony Zhao: So in the case of local motion, as we mentioned, all we need to model in a simulator are
[00:22:28] Tony Zhao: point contacts with a somewhat flat ground.
[00:22:32] Tony Zhao: Like feet.
[00:22:33] Tony Zhao: Yes.
[00:22:35] Tony Zhao: But sort of the behavior we want out of it is actually very difficult to model.
[00:22:39] Tony Zhao: Like it's all these are reactive behaviors that when you feel like you're, um, you're
[00:22:43] Tony Zhao: like is hitting something, you should like retract and, you know, step again.
[00:22:47] Tony Zhao: Uh, these are very, very hard to describe or try to learn from demonstrations directly.
[00:22:52] Tony Zhao: But in the case of manipulation, I think the difficulty is flipped.
[00:22:58] Tony Zhao: That it's a lot easier to capture the behavior itself.
[00:23:03] Tony Zhao: And it's a lot harder to simulate the world.
[00:23:06] Tony Zhao: For example, if you were to grasp a transparent cup with some orange juice in it, it's ridiculously
[00:23:14] Tony Zhao: hard to simulate how like your hand deforms around the cup and how all those replines, how
[00:23:21] Tony Zhao: those like the color of the juice results in like the rendering and what the policy
[00:23:28] Tony Zhao: end up seeing, simulating that is very expensive and difficult.
[00:23:32] Tony Zhao: But all we need to learn is just to like guess your hand to be in front of the cup and
[00:23:37] Tony Zhao: then close with the appropriate amount of force.
[00:23:40] Tony Zhao: And that's actually very easy to learn.
[00:23:42] Tony Zhao: That's why like we see so many success of imitation learning in the case of robotics.
[00:23:48] Tony Zhao: Mediflation is because the behavior itself is actually not as hard as simulating the
[00:23:55] Tony Zhao: world.
[00:23:56] Tony Zhao: And that's why we see faster progress there.
[00:23:58] Is there anything that you have changed your point of view on in data over the last
[00:24:02] Unknown Guest: year?
[00:24:03] Unknown Guest: Like it's one thing I wouldn't say changed, but just data quality really matters.
[00:24:09] Cheng Chi: I think we know I always knew data quality matters.
[00:24:12] Cheng Chi: But once you scale it up, like it really matters.
[00:24:16] Cheng Chi: And then because you know, just like the diversity of behavior that you experience in a
[00:24:21] Cheng Chi: world is very hard to control.
[00:24:23] Cheng Chi: And the hardware failure is a harder control.
[00:24:25] Cheng Chi: You need to constantly monitor them.
[00:24:26] Cheng Chi: Just mean to spend a lot of huge amount of engineering effort just to make sure that
[00:24:31] Cheng Chi: and know the data is clean.
[00:24:32] Tony Zhao: Yeah.
[00:24:33] Tony Zhao: And also building all those automatic processes.
[00:24:35] Tony Zhao: We have our own way of calibrating the glove before we ship it out.
[00:24:39] Tony Zhao: And we have this whole software system to catch if a something is broken on the glove.
[00:24:44] Tony Zhao: And we can detect it automatically.
[00:24:46] Tony Zhao: Is like the importance of data quality kind of translates to all these repeatable processes.
[00:24:52] Tony Zhao: And we don't need a human to be staring at the data to know that something is wrong.
[00:24:56] Unknown Guest: When you describe the beta for next year, a lot of it sounded like, you know, we just
[00:25:01] Unknown Guest: want to understand behavior, like how people actually want to use it.
[00:25:04] Unknown Guest: We can make some design decisions for the actual product.
[00:25:08] Unknown Guest: What technical challenges do you still say?
[00:25:11] So to me, I think there's like two kind.
[00:25:14] Cheng Chi: The number one is really figuring out the training recipe at scale.
[00:25:18] Cheng Chi: We as a field just entered the realm of scaling and we just got amount of data that we need.
[00:25:23] Cheng Chi: And think now is a perfect time to start to research and figure out what exactly the
[00:25:27] Cheng Chi: recipe we need to actually get robust behaviors.
[00:25:31] Cheng Chi: And I think we're in a unique position because the amount of data and the entire pipeline
[00:25:35] Cheng Chi: we built around data.
[00:25:37] Cheng Chi: The second point, I think it's just really hard.
[00:25:39] Cheng Chi: We're still pushing the envelope, performance envelope of hardware.
[00:25:43] Cheng Chi: It's not really clear actually what is needed, what is necessary for the hardware to be
[00:25:48] Cheng Chi: reliable because like whenever the mechanical team build a hardware, the learning team will
[00:25:53] try to try harder to push it against the boundary and then it'll break at some point.
[00:25:58] Cheng Chi: But I think what's interesting in this company is that everybody is under the same roof.
[00:26:03] Cheng Chi: So immediately after something breaks, it goes straight back into mechanical design and
[00:26:07] Cheng Chi: we have each other iteration, like I said, for the hand parts very quickly.
[00:26:12] Cheng Chi: hardware is hard, but it is important.
[00:26:15] Cheng Chi: And I think it's a hard but right thing to do.
[00:26:18] Cheng Chi: And I think we as a field should avoid doing the hard things just because they're hard.
[00:26:22] Cheng Chi: Yeah, I'll just echo a checkpoint about like first the research.
[00:26:26] Tony Zhao: I think when there is data scarcity, it is really easy to come up with like cute fancy
[00:26:33] Tony Zhao: research ideas that doesn't end up scaling very well.
[00:26:38] Tony Zhao: And this is why when we build a company, we actually focus on the infrastructure and
[00:26:42] Tony Zhao: the scalable data pipeline operations before we start to really dive into research, which
[00:26:46] Tony Zhao: we only started to do like three months ago.
[00:26:48] Tony Zhao: I think we really want to avoid doing research that doesn't scale and want to focus on things
[00:26:53] Tony Zhao: that contribute to the final product.
[00:26:55] Tony Zhao: The second point is I think robotics is so intrinsically a system that right now we don't
[00:27:05] Tony Zhao: like there's not a existing general purpose home robot out there.
[00:27:10] Tony Zhao: And we don't really know what the interface of different system is like what is even
[00:27:14] Tony Zhao: good.
[00:27:15] Tony Zhao: And in that case, if you're working with the partner, it's actually really hard for
[00:27:20] Tony Zhao: them to understand your standard of good because your standard of good is changing all
[00:27:24] Tony Zhao: the time.
[00:27:25] Tony Zhao: This is why we are like building everything in house in a more full stack approach that
[00:27:29] Tony Zhao: we build our own data collection device that is co-designed with the robot.
[00:27:33] Tony Zhao: We build our own operation team to be like, how can we most efficiently get the most
[00:27:38] Tony Zhao: high quality data out?
[00:27:40] Tony Zhao: And of course our own AI training team that's the best use of these data.
[00:27:45] Tony Zhao: I think these are the things that are really not easy.
[00:27:49] Tony Zhao: It makes our company a lot harder to build that right now is suddenly like so many teams
[00:27:54] Tony Zhao: and they need to orchestrate together.
[00:27:57] Tony Zhao: But we believe it is the right thing to do.
[00:27:59] Tony Zhao: OK, I'm going to ask you a few questions that are uncomfortable guesses now.
[00:28:03] Unknown Guest: But when will people be able to buy robots commercially from home?
[00:28:06] Unknown Guest: Like there's something we're really excited about because we have so many of prototype robots
[00:28:11] Tony Zhao: in our office and really want to get it out there.
[00:28:14] Tony Zhao: So the next step of our plan is to have a better group program, 2026.
[00:28:19] Tony Zhao: And what it means is that for people who sign up that we selected, they will have a real
[00:28:24] Tony Zhao: robot in their home and it will start doing chores for you.
[00:28:28] Tony Zhao: And it's going to be a really interesting learning lesson for us because we will see like
[00:28:32] Tony Zhao: how can we interact with the robots, we'll see like what kind of things people just really
[00:28:37] Tony Zhao: want to do.
[00:28:39] Tony Zhao: I think this will be before we actually ship it to the masses because we just have an
[00:28:45] Tony Zhao: incredibly high standard of what we are willing to ship as a for a consumer experience standpoint.
[00:28:51] Tony Zhao: We want the robot to be highly reliable, want it to be capable, want it to be cheap.
[00:28:55] Tony Zhao: I think it really depends on the results of the beta program that will decide when is
[00:29:00] Tony Zhao: the good time to ship it.
[00:29:01] Tony Zhao: Is it 2027?
[00:29:02] Tony Zhao: Is it 28?
[00:29:04] Tony Zhao: And all of those are possible.
[00:29:06] Tony Zhao: But it's not a decade away.
[00:29:08] Tony Zhao: No, it's definitely not a decade away.
[00:29:10] How much do you think it could cost?
[00:29:11] Tony Zhao: Right now, the prototype robots we have in in house, I think the cost ranges from like
[00:29:17] Tony Zhao: $6,000 to something like $20,000.
[00:29:22] Tony Zhao: And this is actually pretty interesting that the big difference here is not like, oh,
[00:29:26] Tony Zhao: we find a better actuator.
[00:29:27] Tony Zhao: They're usually the same actuators.
[00:29:28] Tony Zhao: They're like very low cost.
[00:29:30] Tony Zhao: But actually, it's the clotting of the robots.
[00:29:32] Tony Zhao: When you're trying to make them at low scale, it's just really expensive.
[00:29:36] Tony Zhao: Like the clottings are like a few thousand dollars to make.
[00:29:40] Tony Zhao: But this is a type of things that as we scale up, it becomes like dirt cheap because instead
[00:29:45] Tony Zhao: of like the CNC instead of hand painting them, it'll become injection molding.
[00:29:49] Tony Zhao: What we see is that as we get the scale to a few thousand units, we can drastically reduce
[00:29:56] Tony Zhao: the material cost, likely under 10k.
[00:30:00] Tony Zhao: And what it implies is that when we sell the robots, the price will be somewhere around
[00:30:06] Tony Zhao: it.
[00:30:07] Okay.
[00:30:08] Unknown Guest: So you fast forward two, three years out.
[00:30:11] Unknown Guest: If you look like five years and beyond the home robots are ubiquitous.
[00:30:14] Unknown Guest: Like, what does life look like?
[00:30:16] Unknown Guest: How does it change for the average person?
[00:30:19] Tony Zhao: This is a different answer for everyone.
[00:30:21] Tony Zhao: For me, like I just really hate dishes.
[00:30:25] Tony Zhao: Like in my sink, there's always like four or five dishes.
[00:30:27] Tony Zhao: There are like somewhat very out there that kind of stinks a little bit.
[00:30:31] Tony Zhao: And after a long day of work, it really doesn't feel good to come up like see a home like
[00:30:35] Tony Zhao: that.
[00:30:37] Tony Zhao: So I think the world will live in is.
[00:30:39] Tony Zhao: It was going to be cleaner.
[00:30:42] Tony Zhao: It's going to be cleaner.
[00:30:43] Tony Zhao: And I was just thinking about it as like the marginal cost of labor in homes goes to zero.
[00:30:47] Tony Zhao: The last thing I want to make sure we do is like talk about demos, right?
[00:30:51] Unknown Guest: There's a lot of robotics launch videos today.
[00:30:54] Unknown Guest: It's been years since you saw an optimist serving drinks at a bar.
[00:30:59] Why are those not available?
[00:31:01] Unknown Guest: And what is actually hard?
[00:31:02] Unknown Guest: I think the way I'll put it is make zero assumptions.
[00:31:07] Tony Zhao: No price.
[00:31:08] Tony Zhao: As a nice if you see a robot handing one drink to one person first asked the question of
[00:31:15] Tony Zhao: is that autonomous or is that highly operated?
[00:31:18] Tony Zhao: This is the first thing.
[00:31:19] Tony Zhao: So we look at the tweet and see what they say about it.
[00:31:22] Tony Zhao: And then is that the show giving another slightly different color cop to the same person
[00:31:28] Tony Zhao: or not.
[00:31:29] Tony Zhao: If they didn't show it, it means that the robot can literally only pick up that single
[00:31:34] Tony Zhao: cop and give it to that same person.
[00:31:37] Tony Zhao: When we look at demos, we tend to put our human instinct into it that like, oh, if
[00:31:42] Tony Zhao: you can hand a cop to that person, it must be able to hand a different cop to another
[00:31:45] Tony Zhao: person.
[00:31:46] Tony Zhao: Maybe you can also do an addition, maybe you can do a laundry.
[00:31:48] Tony Zhao: There are a lot of like visual thinking that we can have about it, which is what's
[00:31:51] Tony Zhao: great about robotics that there are a lot of imaginations.
[00:31:54] Tony Zhao: But I think when we look at demos, only index on things that is strong.
[00:32:00] And that's likely the full scope of that task.
[00:32:04] Tony Zhao: I think another aspect is at least me as a review researcher, I appreciate the number
[00:32:10] Cheng Chi: of interactions that happens in demos.
[00:32:13] Cheng Chi: Usually the more interactions you have, like every interaction, there's a chance of failure.
[00:32:17] Cheng Chi: So the longer the sequence is, the harder it actually is.
[00:32:20] Cheng Chi: So that's something we really emphasize here.
[00:32:23] Cheng Chi: And that's actually somewhat uniquely easy for us because the glove way of data collection
[00:32:29] Cheng Chi: is so intuitive after people.
[00:32:31] Cheng Chi: Yeah.
[00:32:32] Cheng Chi: It's really about like generalization and reliability.
[00:32:34] Tony Zhao: So can you explain the demos that you guys are showing?
[00:32:36] Unknown Guest: Yeah, of course.
[00:32:38] Tony Zhao: So we're showing like basically three categories of demos.
[00:32:41] Tony Zhao: The first one, as you saw, is we have this whole like messy cable.
[00:32:45] Tony Zhao: And what the robot does is clean up the whole table and dump the food into the food waste
[00:32:50] Tony Zhao: bin and load the dishes with dishwasher and then operate at dishwasher.
[00:32:53] Tony Zhao: What makes this demo really hard is that it is a mix of really fine grained manipulation
[00:33:00] Tony Zhao: with these super long horizon full range tasks as in like indigo up and it also need
[00:33:06] Tony Zhao: to go down very much.
[00:33:08] Tony Zhao: It's a mobile manipulation highest, exactly.
[00:33:11] Tony Zhao: The reason that we can show this is just how nimble and easy for us to collect these
[00:33:17] Tony Zhao: data sets to make horizon text for them possible.
[00:33:20] Tony Zhao: And it's also about the force as well.
[00:33:22] Tony Zhao: So you might have seen like we're trying to pick up two wine glasses with one hand.
[00:33:29] Tony Zhao: And I struggle with this.
[00:33:30] Unknown Guest: It's actually really hard.
[00:33:32] Tony Zhao: And because it's like transparent objects, we need to also load it very precisely into
[00:33:36] Tony Zhao: the into dishwasher.
[00:33:38] Tony Zhao: A lot of it is about how much force you apply.
[00:33:41] Tony Zhao: Because if you are trying to grasp two and one hand, if you squeeze a little harder,
[00:33:45] Tony Zhao: you're going to break one of the glass.
[00:33:47] Tony Zhao: And when you load it into a dishwasher, if you're pushing it in the wrong direction and
[00:33:51] Tony Zhao: it hits something, it's going to shout out.
[00:33:52] Tony Zhao: We did a lot of glasses when we were like you're spending with it.
[00:33:56] Tony Zhao: So these are the tasks that are like really high stake that is not just about recovering
[00:34:02] Tony Zhao: from mistakes, but about not making those mistakes in the first place.
[00:34:06] Tony Zhao: And this is what's generally the case in a lot of the home tasks that you're just not
[00:34:10] Tony Zhao: allowed to make any mistakes.
[00:34:12] Tony Zhao: And then we get into the gyrosation demos, which we basically show our robot.
[00:34:17] Tony Zhao: We book like six EMB and B's and we get it there zero shots and see if can do like part
[00:34:24] Tony Zhao: of the task.
[00:34:25] Tony Zhao: So two tasks we use one is like around table and clock all the utensils into the caddy.
[00:34:29] Tony Zhao: The other is to grab a plate and I load it into the dishwasher.
[00:34:33] Tony Zhao: What makes these these demos very interesting is that we don't need any data when we enter
[00:34:39] Tony Zhao: that home.
[00:34:40] Tony Zhao: It is pure gyrosation.
[00:34:42] Tony Zhao: And this is as close to getting like a real product as you can get because when someone
[00:34:49] Tony Zhao: buy a home robot, we really don't want them to like clock the huge it at themselves.
[00:34:53] Tony Zhao: Just to like unbox it.
[00:34:55] Tony Zhao: Also in addition to the gyrosation, those two tasks are also really precise.
[00:34:59] Tony Zhao: We're using the exact silver verse in the home and you need like basically like a few millimeter
[00:35:06] Tony Zhao: of precision. We're to grasp it properly. Those fours are also hard to perceive because they're
[00:35:10] Tony Zhao: reflective. Like the lights looks weird on it. We have a transparent table home.
[00:35:16] Tony Zhao: I think that the table looks like nothing and the robot still like reacts very well to it.
[00:35:20] Tony Zhao: And again, the reason that we can do it is because we have all these like more than 500 people
[00:35:24] Tony Zhao: and we've seen so many glass tables in that dataset. So the robot is able to do it.
[00:35:29] Tony Zhao: I think the last bit of the task that we did is kind of pushing what's possible in terms of
[00:35:36] Tony Zhao: dexterity. The two tasks we chose one is a espresso, operating espresso machine. The other is like
[00:35:43] Tony Zhao: folding socks. We'll make these hard is that they require very fine-grinned force.
[00:35:50] Tony Zhao: That is hard to get if you're doing with tally operation. Because these days,
[00:35:56] Tony Zhao: there's not a good tally operation system that can let you feel how much force the robot is feeling.
[00:36:03] Tony Zhao: So basically when you're tally operating, your hand is numb. And sometimes you are applying like
[00:36:08] Tony Zhao: a huge amount of force on the robot, but you don't know it. And that can result in like very low
[00:36:13] Tony Zhao: data quality that robot is also doing in that aggressive way that we really want to avoid for our
[00:36:18] system. The Saga is a very good example that when you're trying to fold it, your two fingers can
[00:36:23] Tony Zhao: clutch. And that forms a, or we call it a force closure. You have a closed loop for the force.
[00:36:29] Tony Zhao: And if you roll a stiff, you can apply infinite amount of force at it and doesn't look like anything.
[00:36:35] Tony Zhao: But for us, because we're using the glove to collect the data, the human who is collecting
[00:36:39] Tony Zhao: the country's naturally feel it is very intuitive. I think we're the first to do the sock folding
[00:36:48] Tony Zhao: and using end-to-end to do like espresso machine out of the whole industry.
[00:36:53] Tony Zhao: One of the things that you will also need to scale as you guys, you know,
[00:36:58] Unknown Guest: scale up the company is the team. What are you hiring for? What are you looking for?
[00:37:03] Unknown Guest: One thing I'm really looking forward to is.
[00:37:06] Cheng Chi: Thanks, Big Stuff.
[00:37:07] Unknown Guest: So it's full-stock roboticists and people who aspire to become full-stock roboticists.
[00:37:15] Cheng Chi: Really, when you learn in this company, it's just that robotics is such a multi-disciplinary field.
[00:37:21] Cheng Chi: You need to know mechanical, a little mechanical, a little electrical, a little code,
[00:37:25] Cheng Chi: little data to actually fully optimize the system. And we have a couple examples of training,
[00:37:31] Cheng Chi: full-stock self-engineered to become roboticist. Training and engineers to become roboticists.
[00:37:36] Cheng Chi: And so if you want to learn about robotics, you can learn the whole thing, not just to
[00:37:41] Cheng Chi: be boxing into your small little cubicle. Let us know.
[00:37:45] And you told me that you didn't write code until you got to college or something.
[00:37:51] Unknown Guest: I was super enthusiastic about robotics. I was mostly doing a mechanical and for design before that.
[00:37:58] Cheng Chi: And then I realized, okay, the bottleneck is actually how the robot will move.
[00:38:01] Cheng Chi: And there's something called programming. And then the more I get into it, the deeper it gets.
[00:38:08] Cheng Chi: And then toward the end of college, I realized, okay, there's a thing called machine learning.
[00:38:12] Cheng Chi: And you can bring your own hundred-three models. I think this thing just goes on and on.
[00:38:15] Cheng Chi: I think it's very natural for me to graduate X-Bamma skill set because I'm always looking forward
[00:38:20] Cheng Chi: to building a robot.
[00:38:21] Cheng Chi: Well, I hope you discover the next field because you're no longer doing dishes.
[00:38:24] Unknown Guest: It's tough. It's a very fun place to work.
[00:38:27] Tony Zhao: Whatever you can imagine about robotics and consumer products and machine learning,
[00:38:33] Tony Zhao: you can find it here because we're just fundamentally such a full-stack company.
[00:38:37] Tony Zhao: We're not just about a software. We're not just about a hardware, but we're about the whole
[00:38:41] Tony Zhao: experience, the whole product. And making sure that product is general and scalable in the future.
[00:38:47] Tony Zhao: Awesome. Congratulations.
[00:38:48] Unknown Guest: It's really exciting.
[00:38:55] Find us on Twitter at No Pryor's Pod.
[00:39:00] Unknown Host: Subscribe to our YouTube channel if you want to see our faces.
[00:39:03] Unknown Host: Follow the show on Apple Podcasts, Spotify, or wherever you listen.
[00:39:07] Unknown Host: That way you get a new episode every week.
[00:39:09] Unknown Host: And sign up for emails or find transcripts for every episode at no-pryor's.com.