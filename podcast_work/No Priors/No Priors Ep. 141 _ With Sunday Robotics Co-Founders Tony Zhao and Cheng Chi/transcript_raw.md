# No Priors Ep. 141 | With Sunday Robotics Co-Founders Tony Zhao and Cheng Chi

**Podcast:** No Priors
**Date:** 2025-11-20
**Video ID:** 4-VzXoZqAH0
**Video URL:** https://www.youtube.com/watch?v=4-VzXoZqAH0

---

[00:00:00] Nobody wants to do their dishes, nobody wants to do their laundry, people will love to
[00:00:09] SPEAKER_03: spend more time with their family, with their loved ones.
[00:00:13] SPEAKER_03: So what we believe in is that if the robot is cheap, safe and capable, everyone will
[00:00:18] SPEAKER_03: want our robot.
[00:00:20] SPEAKER_03: And we see a future where we have more than 1 billion of these robots in people's homes
[00:00:25] SPEAKER_03: within the decades.
[00:00:26] SPEAKER_03: Thanks, memo.
[00:00:35] Hi listeners, welcome back to No Pires.
[00:00:37] SPEAKER_00: Today we're here with Tony's Ow and Chang-Chi, co-founders of Sunday and Makers of Memo,
[00:00:42] SPEAKER_00: the first general home robot.
[00:00:44] SPEAKER_00: We'll talk about AI and robotics, data collection, building a full stack robotics company, and
[00:00:50] SPEAKER_01: a world beyond toil.
[00:00:51] SPEAKER_01: Welcome.
[00:00:52] Chang, Tony, thanks for being here.
[00:00:53] SPEAKER_01: Thanks for having me.
[00:00:55] SPEAKER_03: Okay, first I want to ask, where are we here?
[00:00:58] SPEAKER_01: Because classical robotics has not been an area of great optimism over time or massive
[00:01:04] SPEAKER_01: velocity of work.
[00:01:06] SPEAKER_01: And now people are talking about a foundation model for robotics or a Chad GPD moment.
[00:01:11] SPEAKER_01: Can you just contextualize the state of AI robotics and why we should be excited?
[00:01:15] SPEAKER_01: I will say I think we're kind of in between the GPD moment and the Chad GPD moment.
[00:01:21] SPEAKER_03: In the context of LMS, what it means is that it seems like we have a recipe that can
[00:01:28] SPEAKER_03: be scout, but we haven't scaled up yet.
[00:01:31] SPEAKER_03: And we haven't scaled up so much so that we can have a great consumer product out of
[00:01:35] SPEAKER_03: it.
[00:01:36] SPEAKER_03: So this is where I mean like GPD, which is like a technology and Chad GPD, which is
[00:01:40] SPEAKER_03: a product.
[00:01:41] SPEAKER_03: Yeah, I'm so we're seeing across academia.
[00:01:44] SPEAKER_02: There's consensus around what's the method from manipulation, but everybody's talking
[00:01:49] SPEAKER_02: about scaling up.
[00:01:50] SPEAKER_02: It's like we know there's sign of life for the algorithms people are picking, but people
[00:01:55] SPEAKER_02: don't know if we have more data like what happened to GPD 2, GB 3 will happen.
[00:02:01] SPEAKER_02: And but we see a clear trend that no, there's no reason to believe that robotics doesn't
[00:02:05] SPEAKER_02: follow the trajectory of other AI fields that know scaling up is going to improve performance.
[00:02:12] SPEAKER_01: Maybe even if you took a step back, like what was the process for deploying a robot into
[00:02:17] SPEAKER_01: the world like 10 years ago, like pre set of generalizable AI algorithms.
[00:02:22] SPEAKER_01: Why was it so slow as a field?
[00:02:24] SPEAKER_01: Yeah, so previously, you know, classical robotics have this sense plan act modular approach,
[00:02:31] SPEAKER_02: where there's a human designing interface between each of the modules.
[00:02:34] SPEAKER_02: And those army to be designed for each specific task and each specific environment.
[00:02:38] SPEAKER_02: Yeah, academia that means for every task, that means a paper.
[00:02:42] SPEAKER_02: So a paper is you design a task, design environment, and you design interfaces.
[00:02:47] SPEAKER_02: And then you produce engine work for that specific task.
[00:02:50] SPEAKER_02: But once you move on to the next task, you throw out your code, all your work and you
[00:02:53] SPEAKER_02: start over again.
[00:02:54] SPEAKER_02: And that's also kind of what happened to industry.
[00:02:57] SPEAKER_02: So for each application, people build a very specific software and hardware system around
[00:03:01] SPEAKER_02: it, but it's not really generalizable.
[00:03:03] SPEAKER_02: And therefore, it's just feel like we're just running loops.
[00:03:06] SPEAKER_02: We build a one system and then we build a next one, but there's like no synergy between
[00:03:11] SPEAKER_02: them.
[00:03:12] SPEAKER_02: So the progress has been somewhat slow.
[00:03:13] SPEAKER_02: I feel like that's a good segue into some of the amazing research work that you guys
[00:03:17] SPEAKER_01: have contributed over the last five years to the field.
[00:03:21] SPEAKER_01: Should we start with diffusion policy?
[00:03:22] SPEAKER_01: What was the impact of that?
[00:03:23] SPEAKER_01: Yeah, so the field of policy is like specific algorithm for a paradigm called imitation
[00:03:28] SPEAKER_02: learning.
[00:03:29] SPEAKER_02: That's really like the most intuitive way of, you know, how to use machine learning for
[00:03:33] SPEAKER_02: robotics.
[00:03:34] SPEAKER_02: So you collect pair data of action observation of what the robot should do.
[00:03:38] SPEAKER_02: You use that to train a model with supervised learning and then the robot do the same thing.
[00:03:42] SPEAKER_02: The problem is that in the field is known to be very finicky.
[00:03:46] SPEAKER_02: So when it comes to researchers, when I start into the field, people are like the researchers
[00:03:51] SPEAKER_02: themselves, the specific researcher need to collect data so that there's exactly one way
[00:03:56] SPEAKER_02: to do everything.
[00:03:58] SPEAKER_02: Otherwise the robot either like use a model training with average or the robot behaves
[00:04:01] SPEAKER_02: some weird way.
[00:04:03] SPEAKER_02: The fusion model really allows us to capture multiple modes of behavior for the same observation
[00:04:10] SPEAKER_02: in a way that still preserve training stability and that really kind of unlocked more scalable
[00:04:15] SPEAKER_02: training and more scalable data function.
[00:04:17] SPEAKER_02: So it doesn't have to be you personally wearing, you know, a teleopset in order to make a robot
[00:04:22] SPEAKER_01: learn.
[00:04:23] SPEAKER_01: Yeah, so like we can have multiple people sometimes even and train people collecting data
[00:04:27] SPEAKER_02: and the result will still be great.
[00:04:29] SPEAKER_02: Where do Aloha and act plan to this?
[00:04:32] SPEAKER_01: Yeah, so these two papers are actually like super close each other.
[00:04:35] SPEAKER_03: They're like one month or two months away.
[00:04:37] SPEAKER_03: That's actually how me and Trinno each other.
[00:04:39] SPEAKER_03: It was about looking at each other's paper like and we met on Twitter, I think, when
[00:04:44] SPEAKER_03: Trinns back in Columbia.
[00:04:45] SPEAKER_03: Before Aloha, I think the typical way people collect data is with a like polyoption setup
[00:04:53] SPEAKER_03: with we are hasent and it turns out to be very unintuitive to do and it's hard to collect
[00:04:58] SPEAKER_03: data that is actually dexterous.
[00:05:00] SPEAKER_03: Well, Aloha brings this a very simple and reproducible setup.
[00:05:03] SPEAKER_03: So it's very intuitive.
[00:05:04] SPEAKER_03: Sorry, in terms of just for most people who haven't worn a teleopset up, is it the lag?
[00:05:09] SPEAKER_01: Is it like just, you know, how should I compare it to like playing a video game or something?
[00:05:13] SPEAKER_01: Yeah, I think Aloha make it feel more like playing a video game.
[00:05:17] SPEAKER_03: Normally it feels kind of disconnected that you're just like moving in the free air and
[00:05:21] SPEAKER_03: Aroha is moving with some delays, but Aloha reduces that delay by a lot and that contribute
[00:05:27] SPEAKER_03: to the smoothness and how fast human can react.
[00:05:31] SPEAKER_03: Like once we got those really dexterous data, what allows us to do is to investigate
[00:05:37] SPEAKER_03: on algorithms that are actually solving things that are difficult.
[00:05:42] SPEAKER_03: In this case is through the introducing of trans, using transformers in the case of robotics.
[00:05:48] SPEAKER_03: And there was a long period of time that I think robotics was stuck with a failure MLP's
[00:05:54] SPEAKER_03: and covenants and as you make it deeper, it works worse.
[00:05:58] SPEAKER_03: But it turns out that once you have very strong and dexterous data sets, like just through
[00:06:04] SPEAKER_03: a transformer edit and it works quite well.
[00:06:06] SPEAKER_03: Actually, like just in terms of progress of the industry over time, transformers are
[00:06:11] SPEAKER_01: going to make sense without a certain level of data collection, capability, okay.
[00:06:14] SPEAKER_01: And also, also, the system around it, for example, action chunking, which is to predict
[00:06:18] SPEAKER_03: a trajectory as opposed to projecting single-sampus fractions.
[00:06:22] SPEAKER_03: All these things kind of combined to make dexterous tasks by manual tasks more scalable.
[00:06:28] Why is chunking important here if I think about like just the analogy to LMS and like
[00:06:34] SPEAKER_01: text sequence prediction?
[00:06:35] SPEAKER_01: I think it just kind of throws the amount off if you're trying to force it to react every
[00:06:41] SPEAKER_03: millisecond.
[00:06:42] SPEAKER_03: That's not how human act.
[00:06:45] We perceive and we can actually move quite a bit without looking at things again.
[00:06:51] SPEAKER_03: That turns out to make things the motion a lot more consistent and or performance to
[00:06:55] SPEAKER_03: be a lot better.
[00:06:57] And you discovered that actually transformers are potentially did apply through a lot of
[00:07:01] SPEAKER_01: products.
[00:07:02] SPEAKER_01: Cheng, you felt then that data collection was still a problem.
[00:07:05] SPEAKER_01: So enter Oomi.
[00:07:06] SPEAKER_01: Yeah.
[00:07:07] SPEAKER_02: So after a low-ha and a digital policy, I was super excited about imitation learning.
[00:07:12] SPEAKER_02: But at the time, most of us start still doing catalymperation and that just feel super
[00:07:17] SPEAKER_02: limiting.
[00:07:18] SPEAKER_02: The problem is that you know, the interest set up at a time like a patty op set up.
[00:07:23] SPEAKER_02: It takes a piece of student couple of hours to set up in the lab.
[00:07:27] SPEAKER_02: It pretty much restrict data collection to a lab.
[00:07:29] SPEAKER_02: But in order for the robot to actually work as a product, it needs to be worked in the
[00:07:33] SPEAKER_02: wild in on scene environments that requires the data to be also collected in the wild.
[00:07:39] SPEAKER_02: And at the time I was thinking, okay, is there a way we can collect robotic data without
[00:07:43] SPEAKER_02: actually using a robot?
[00:07:45] SPEAKER_02: Like fourth means to think, okay, what's the actual most essential part of a robotic
[00:07:49] SPEAKER_02: data?
[00:07:50] SPEAKER_02: And after the field of policy and act, actually the paradigm is kind of simple.
[00:07:54] SPEAKER_02: You just need paired observation and action data.
[00:07:57] SPEAKER_02: In our case, observation is the video clip.
[00:07:59] SPEAKER_02: The action is the movement of your hand plus how the finger moves.
[00:08:04] SPEAKER_02: I realized that all of these information you can get from a GoPro.
[00:08:07] SPEAKER_02: You can track the movement of GoPro in space and you can track the motion of the grip
[00:08:14] SPEAKER_02: and also finger through images as well.
[00:08:17] SPEAKER_02: And that's why I built this Umi Gryppur and 30 printed.
[00:08:21] SPEAKER_02: At the time, the product had three peachy students.
[00:08:23] SPEAKER_02: We just took the Gryppur everywhere.
[00:08:25] SPEAKER_02: I think there's two weeks before the paper deadline.
[00:08:29] SPEAKER_02: Every time it goes to a restaurant, before the weather comes in, we just collect some
[00:08:32] SPEAKER_02: data.
[00:08:33] SPEAKER_02: And very quickly, we got, I think, 1,500 video clips of this like, express or cop serving
[00:08:40] SPEAKER_02: task.
[00:08:41] SPEAKER_02: And that turns out to be one of the biggest data sets in your robotics and just simply
[00:08:45] SPEAKER_02: by three people.
[00:08:46] SPEAKER_02: And that's like how that's where the power kind of shines.
[00:08:49] SPEAKER_02: And then with that amount of data allows to train the first end to end model that can
[00:08:55] SPEAKER_02: actually generalize to unseen environments.
[00:08:57] SPEAKER_02: So we can push the robot around in Stanford.
[00:08:59] SPEAKER_02: Actually Tony was there as well.
[00:09:01] SPEAKER_02: Push the robot around the Stanford campus and then anywhere the robot can serve you to
[00:09:06] SPEAKER_02: drink.
[00:09:07] SPEAKER_03: Yeah, I think that is the moment I was like, hey, maybe we should start the company.
[00:09:11] SPEAKER_03: This is actually working so well.
[00:09:13] SPEAKER_03: I remember like just falling in town and the times that doesn't work well.
[00:09:17] SPEAKER_03: I think the only exception I saw was when it's under direct sunlight.
[00:09:21] SPEAKER_03: Yeah.
[00:09:22] SPEAKER_03: And I think the reasoning was like over that whole like two, three weeks of data, that
[00:09:26] SPEAKER_03: two weeks is already.
[00:09:27] SPEAKER_02: So there's no sunlight data.
[00:09:29] SPEAKER_02: So like it fails.
[00:09:30] SPEAKER_02: That also demonstrated importance of distribution matching.
[00:09:33] SPEAKER_02: So in order for robot to work in a sunny environment, it must have seen sunny environments
[00:09:38] SPEAKER_02: training training data.
[00:09:39] SPEAKER_02: Yeah, it's really interesting because I remember when I first met you guys, it was like
[00:09:42] SPEAKER_01: you spent like, I don't know, $200,000 across all of your academic research.
[00:09:48] SPEAKER_01: And yet the scale of data collection as translated to model capability is leading.
[00:09:54] SPEAKER_01: Right.
[00:09:55] SPEAKER_01: So it's very interesting that we look at where we are, maybe going back to Tony's point
[00:10:00] SPEAKER_01: of scaling and massive capital deployment.
[00:10:04] SPEAKER_01: But that entire paradigm actually wasn't relevant before people realized like you should
[00:10:09] SPEAKER_01: train on all of the internet data.
[00:10:11] SPEAKER_01: And we just don't have that in robotics.
[00:10:13] SPEAKER_01: So the entire field is just blocked on having any scale of data that's relevant.
[00:10:16] SPEAKER_01: Yeah.
[00:10:17] SPEAKER_03: I think DCs are so like assuming the base about like what is even the right way to scale.
[00:10:22] SPEAKER_03: They're like role models, they're assimilations, there is teleoperation.
[00:10:26] SPEAKER_03: They're like all these new ideas.
[00:10:28] SPEAKER_03: And I think this is the sort of area that we really want to innovate that we want to differentiate.
[00:10:34] SPEAKER_03: We want to find out something that is both high quality and scalable.
[00:10:38] SPEAKER_03: And then you guys, you decide to start a company pushing this cart around Stanford.
[00:10:42] SPEAKER_01: Tell me about that decision and congratulations on the launch and sort of the direction in
[00:10:47] SPEAKER_01: team you've got.
[00:10:48] SPEAKER_01: Yeah.
[00:10:49] SPEAKER_03: It's a very interesting journey.
[00:10:51] SPEAKER_03: I remember in the beginning of society, two of us in terms of apartment on his desk,
[00:10:56] SPEAKER_03: we were like clamped a robot there and tried to do some tasks.
[00:10:59] SPEAKER_03: And I soon become like, I think an eight person team who was the end of 2024.
[00:11:06] SPEAKER_03: And now we're around like 30 to 40 people.
[00:11:08] SPEAKER_03: We're not the best at everything, right?
[00:11:10] SPEAKER_03: But certainly a company allows us to find people who really love working with and then
[00:11:14] SPEAKER_03: bring all the expertise together from the kind of engineering supply chain, like software
[00:11:19] SPEAKER_03: engineering, like controls, and to build a system together that is not like a demo, but
[00:11:25] SPEAKER_03: a real product.
[00:11:27] SPEAKER_03: To build this amazing team, what are people actually signing up for?
[00:11:29] SPEAKER_01: What's the mission of Sunday?
[00:11:31] SPEAKER_03: Yes, it is to play a home robot in Erwa's home.
[00:11:34] SPEAKER_03: I think there are a lot of AIs trying to make you more efficient during the work, but
[00:11:39] SPEAKER_03: there is not enough AIs that actually helps you with all these mundane things that are
[00:11:43] SPEAKER_03: not creative that really has nothing to do with what's making us more intrinsically
[00:11:48] SPEAKER_03: human.
[00:11:49] SPEAKER_03: What's ideal for people to spend more time on is actually with their hobbies, with their
[00:11:53] SPEAKER_03: passions, as opposed to spending more time doing chores.
[00:11:57] SPEAKER_01: So if you guys are going from these amazing research breakthroughs to we're actually going
[00:12:03] SPEAKER_01: to ship a home robot, and that's a product you have to talk about, cost and capability
[00:12:08] SPEAKER_01: and robustness, like what's the design philosophy?
[00:12:11] SPEAKER_01: As these AIs models become more capable and as hardware costs continue to go down, the
[00:12:18] home robots, all kinds of robots will be everywhere.
[00:12:22] SPEAKER_03: So if you start from the most surface level, which is design of the robots, when we
[00:12:26] SPEAKER_03: design it, we think about what should the robot look like if it is ubiquitous?
[00:12:32] SPEAKER_03: You need to see it every single day.
[00:12:35] SPEAKER_03: What should it look like?
[00:12:37] And what we end up with is that we really think the robot should have a face.
[00:12:41] SPEAKER_03: It should have a cute face, and it should be very friendly.
[00:12:45] SPEAKER_03: So instead of like a terminator doing your dishes, we want the robot to feel like it's
[00:12:49] SPEAKER_03: out of a cartoon movie.
[00:12:51] SPEAKER_03: And then the huge decision is like how many arms do the robot have?
[00:12:56] SPEAKER_03: Should they have like four arms?
[00:12:57] SPEAKER_03: Should they have like one arms?
[00:12:58] SPEAKER_03: Should they have legs?
[00:12:59] SPEAKER_03: Should they have like five fingers, two fingers, two fingers?
[00:13:02] SPEAKER_03: It's a huge space.
[00:13:03] SPEAKER_03: Why is it the obvious answer?
[00:13:05] SPEAKER_01: It should just be like a full human.
[00:13:07] SPEAKER_03: I think the core motivation for us is how can we build a useful robot as soon as possible?
[00:13:14] SPEAKER_03: So whenever we see something that we can accelerate it with simplification, we'll go simplify
[00:13:19] SPEAKER_03: that.
[00:13:20] SPEAKER_03: So one example of that is the hand that we designed, which has three fingers.
[00:13:25] SPEAKER_03: We kind of combine the three of the fingers that we have together.
[00:13:29] SPEAKER_03: And the reasoning there is just that most of the time when we use those fingers, we use
[00:13:33] SPEAKER_03: it together.
[00:13:34] Let it be like grasping a handle, let it be opening the dishwasher.
[00:13:37] SPEAKER_03: So it really doesn't make sense to add the cost, like multiply by three X to have separate
[00:13:44] SPEAKER_03: it into three, and we can do one with most of the benefits.
[00:13:48] SPEAKER_03: So this is how we think about the whole robot as well.
[00:13:51] SPEAKER_03: It's kind of with the constraint that we're building a general-purpose robot that can eventually
[00:13:55] SPEAKER_03: do all your chores and will simplify everything we possibly can so that the robot can be as
[00:14:00] SPEAKER_03: low cost and as easy to repair as possible.
[00:14:03] SPEAKER_03: Yeah, just want to add a little bit more to the I-Freeter and the mechanical design.
[00:14:08] SPEAKER_02: Traditionally, most robots are designed for industrial use cases.
[00:14:11] SPEAKER_02: And the robot are very fast.
[00:14:13] SPEAKER_02: They are very stiff and never precise.
[00:14:15] SPEAKER_02: The reasons because all the industrial robots are blind.
[00:14:18] SPEAKER_02: So they're blindy flowing a trajectory that's programmed by someone.
[00:14:21] SPEAKER_02: It's not a reaction to perception.
[00:14:23] SPEAKER_01: Correct.
[00:14:24] SPEAKER_02: But because of the brakes we have in AI, like now robots have eyes.
[00:14:28] SPEAKER_02: So it can actually correct this own mechanical and hardware inaccuracies.
[00:14:33] SPEAKER_02: So that kind of opened up a new different space of design.
[00:14:37] Intuitively, it should be like, I can't tell you exactly what the distance is that you're
[00:14:41] SPEAKER_01: on a millimeter scale, but I'm going to get to the cup because I can stop.
[00:14:45] Yeah, exactly.
[00:14:45] So that allows us to use these low cost actuators that's cheap, that's compliant, but they're
[00:14:52] SPEAKER_02: in precise.
[00:14:53] SPEAKER_02: But because of the AI's algorithms and systems we build, it allows us to build robots as mechanically
[00:14:59] SPEAKER_02: inherently safe and compliant.
[00:15:00] SPEAKER_02: While simultaneously, we'll be able to achieve the sufficient accuracy we need for the home
[00:15:04] SPEAKER_02: tasks.
[00:15:05] Where are we in that timeline?
[00:15:06] SPEAKER_01: You said we're between GPT and chat GPT.
[00:15:10] SPEAKER_01: And so like when do consumers get chat GPT and when will you guys ship something?
[00:15:14] SPEAKER_01: Yeah, it's actually really exciting time because we have so many prototypes internally.
[00:15:19] SPEAKER_03: What we will do next year, 2026 is actually start doing beta programs.
[00:15:24] SPEAKER_03: We'll have these robots, all kinds of different ones, into people's home and see how they react
[00:15:29] SPEAKER_03: to it.
[00:15:30] SPEAKER_03: That will be when we learn the most about like how people like people want to talk to
[00:15:34] SPEAKER_03: a robot.
[00:15:35] SPEAKER_03: If you go want to have the robots, maybe teach their kids some new knowledge about the
[00:15:42] SPEAKER_03: world.
[00:15:43] SPEAKER_03: And this will inform us what the eventual product should look like.
[00:15:47] SPEAKER_03: Internally, we just have an extremely high standard of what is the minimal consumer
[00:15:53] SPEAKER_03: product we want to ship.
[00:15:54] SPEAKER_03: It needs to be extremely safe.
[00:15:55] SPEAKER_03: It needs to be extremely capable and low cost.
[00:15:58] SPEAKER_03: Do you feel like you know something now that you didn't when you started the company?
[00:16:02] SPEAKER_01: Absolutely.
[00:16:03] SPEAKER_03: So I think at the beginning of the story, as we see light at the end of the tunnel of
[00:16:09] SPEAKER_03: their two axes, their sexuality, their externalization, we add more data, things works better.
[00:16:14] SPEAKER_03: And what this company about is the cross product of these two.
[00:16:18] SPEAKER_03: How can we scale and have both the Xerity and generalization?
[00:16:23] SPEAKER_03: And this is something we're able to show in our generalization demo, which is like we
[00:16:26] SPEAKER_03: can pick up these like very precise like forks, like actual metallic forks, only ceramic
[00:16:32] SPEAKER_03: plates with very high success rates.
[00:16:35] SPEAKER_03: And honestly, this is not something that like we thought that would work so easily just
[00:16:41] SPEAKER_03: by having so much more data.
[00:16:42] SPEAKER_03: Yeah, so actually just want to expand a little bit.
[00:16:45] SPEAKER_02: You know, it's actually the process was long and painful.
[00:16:49] SPEAKER_02: So, yeah, there's so many issues like just scaling up a system.
[00:16:54] SPEAKER_02: Robotics is very, very hard.
[00:16:56] SPEAKER_02: There are mechanical issues like reliability issues.
[00:16:59] SPEAKER_02: There's like data, you know, quality issues that come out of it.
[00:17:03] SPEAKER_02: In the beginning, I actually thought it's going to be much easier than this.
[00:17:07] SPEAKER_02: But really, it just takes time and effort to grind out all the little details for this
[00:17:11] SPEAKER_02: to work.
[00:17:12] SPEAKER_02: I also actually compared to Teddy Albus much harder to get this system scaled up.
[00:17:16] SPEAKER_02: But once the scaled up is very powerful, very repeatable.
[00:17:18] SPEAKER_02: So it is both harder than you thought it would be to get to here and you are further
[00:17:22] SPEAKER_01: than you thought you would be.
[00:17:24] SPEAKER_01: And I remember in the beginning, we're having this like funny conversation of where
[00:17:29] SPEAKER_03: like if we built this, someone can just like take our glove and they'll build the same
[00:17:34] SPEAKER_03: thing.
[00:17:34] SPEAKER_03: Like, well, we'll do it half.
[00:17:36] SPEAKER_03: Are we worried about that?
[00:17:37] SPEAKER_03: And at the beginning, actually, we are a little bit worried because we thought like,
[00:17:40] SPEAKER_03: you know, they can probably just replicate it.
[00:17:43] SPEAKER_03: But as we go along the path, it turns out things are so much harder than we thought.
[00:17:47] SPEAKER_03: It will have so many the small, small, yeah.
[00:17:50] SPEAKER_02: Yes.
[00:17:51] SPEAKER_02: And when you say scaling up a robotic system, you mean the data collection to training pipeline
[00:17:56] SPEAKER_01: and the hard work itself.
[00:17:57] SPEAKER_01: Yeah.
[00:17:57] SPEAKER_01: So I actually like for the, yeah, for this to work at all, you know, the declaration system,
[00:18:02] SPEAKER_02: yeah, need the robotic and control system to be able to deliver the hand to where we want
[00:18:05] SPEAKER_02: to go.
[00:18:06] SPEAKER_02: Yeah.
[00:18:06] SPEAKER_02: And you also need the data filtering pipeline and data cleaning pipeline and the training
[00:18:11] SPEAKER_02: pipeline.
[00:18:12] SPEAKER_02: And all these things need to be iterated together.
[00:18:14] SPEAKER_02: So actually gone to several loop of these is kind of hard to imagine without having a
[00:18:18] SPEAKER_02: full stack team in the house.
[00:18:20] SPEAKER_02: How does it kind of even be done?
[00:18:21] SPEAKER_02: Yeah.
[00:18:22] SPEAKER_03: The glove we're using right now is we call it like V5.
[00:18:26] SPEAKER_03: And for V0 to V5, each version has like around 20 iterations.
[00:18:30] SPEAKER_03: Okay.
[00:18:31] SPEAKER_01: And so 100.
[00:18:33] SPEAKER_01: Yes.
[00:18:34] SPEAKER_03: And also like just when you make these as scale right now, we have more than 500 people
[00:18:39] SPEAKER_03: using these golfs in the wild.
[00:18:41] SPEAKER_03: Like all the things that could go wrong will go wrong.
[00:18:45] SPEAKER_03: For example, they did they did.
[00:18:46] SPEAKER_03: Yes.
[00:18:47] SPEAKER_03: For example, like how things are assembled.
[00:18:50] SPEAKER_03: If you don't specify exactly how it should be done, people will assemble it in creative
[00:18:55] SPEAKER_03: ways.
[00:18:56] SPEAKER_03: And the creativity doesn't help us here because I really want the data collection device
[00:19:00] SPEAKER_03: to be extremely present.
[00:19:02] SPEAKER_03: So you guys can't obviously know everything that's happening in every company in academia
[00:19:07] SPEAKER_01: industry.
[00:19:08] SPEAKER_01: But from what you know, how would you compare the scale of training data that you have today
[00:19:14] SPEAKER_01: relative to the industry?
[00:19:16] At this point, we are almost 10 million trajectories being collected in the wild.
[00:19:23] SPEAKER_03: And those trajectories are not just like, oh, pick up a cup.
[00:19:26] SPEAKER_03: These long trajectories with like walking with navigation and then like doing this long
[00:19:32] SPEAKER_03: horizon tasks.
[00:19:33] SPEAKER_03: Tony, as you mentioned, like it's an open question actually what the right way to scale
[00:19:39] SPEAKER_01: data up is.
[00:19:40] SPEAKER_01: And so there are strong theories around teleop around like pure RL around video and world
[00:19:46] SPEAKER_01: models.
[00:19:47] SPEAKER_01: Like how did you think about all of these?
[00:19:50] Yeah.
[00:19:51] SPEAKER_02: So from our perspective, actually it's kind of civil surprising.
[00:19:53] SPEAKER_02: So in the beginning, we worried that the data from glove or only like data has higher
[00:19:58] SPEAKER_02: quantity, but lower quality compared to teleop.
[00:20:01] SPEAKER_02: Because of teleop, you're using exactly the same hardware software stack between training
[00:20:04] SPEAKER_02: and testing is perfectly distribution match.
[00:20:07] SPEAKER_02: But what we realized is actually, you know, this glove form factor encouraged people to do
[00:20:12] SPEAKER_02: more text version, more natural movement.
[00:20:14] SPEAKER_02: And those actually result in a more intelligent behavior on the modeling side.
[00:20:20] SPEAKER_02: But in terms of data quality, we don't really see a difference in terms of how much like
[00:20:25] SPEAKER_02: there's a gap between teleop and glove data.
[00:20:28] SPEAKER_02: After we did the 20 engineering life service life.
[00:20:33] SPEAKER_03: Yeah.
[00:20:34] SPEAKER_03: Yeah.
[00:20:35] SPEAKER_03: Like apparently there is a mismatch, right?
[00:20:37] SPEAKER_03: That's in the camera frame, there's a human is out of the robots.
[00:20:41] SPEAKER_03: And there are just a lot of things that we need to do to kind of convert a human data one
[00:20:47] SPEAKER_03: to one to like as if it is robot data and have the model not being able to tell you
[00:20:51] SPEAKER_03: the difference.
[00:20:52] SPEAKER_03: Yeah.
[00:20:53] SPEAKER_02: And that kind of relies on again, the whole the full cycle iteration between hardware and
[00:20:57] SPEAKER_02: software.
[00:20:58] SPEAKER_02: What about RL?
[00:20:59] We see a lot of great promise for RL in local motion.
[00:21:03] SPEAKER_02: And you know, we think that will continue to be true for local motion.
[00:21:06] SPEAKER_02: So what we see really felt like RL is a method is very powerful.
[00:21:10] SPEAKER_02: But it is much less sample efficient compared to imitation learning.
[00:21:14] SPEAKER_02: And we see that to work great in environments where it's easy to simulate.
[00:21:18] SPEAKER_02: For the case of local motion, you only need to worry about rigid body dynamics and
[00:21:23] SPEAKER_02: rigid body contact between the robot and the ground.
[00:21:26] SPEAKER_02: And you know, because you engineer a robot, you know, everything.
[00:21:29] SPEAKER_02: But for manipulation, it's kind of hard for us to imagine like have does actually the
[00:21:34] SPEAKER_02: same amount of diversity and the distribution of real object in terms of matching both
[00:21:41] SPEAKER_02: appearance and physical properties.
[00:21:45] SPEAKER_02: And we think that it's going to be challenging compared to a global collection and tell
[00:21:49] SPEAKER_03: you.
[00:21:50] SPEAKER_03: Yeah.
[00:21:51] SPEAKER_03: I think it's really about which method can get us there faster.
[00:21:54] SPEAKER_03: There might be different methods that will eventually get there.
[00:21:57] SPEAKER_03: For example, like, you know, simulation world model, right?
[00:22:01] SPEAKER_03: And like it's almost a technology to say that if I have a perfect world simulator, anything
[00:22:07] can be done there.
[00:22:08] SPEAKER_03: Like as long as you can do in a real world, you can do it in a simulation.
[00:22:12] SPEAKER_03: And you can like, you know, cure cancer in a simulator, right?
[00:22:15] SPEAKER_03: But what it turns out for robotics is that some, some things are harder than others.
[00:22:21] SPEAKER_03: And it really depends on the problem itself.
[00:22:24] SPEAKER_03: So in the case of local motion, as we mentioned, all we need to model in a simulator are
[00:22:28] SPEAKER_03: point contacts with a somewhat flat ground.
[00:22:32] SPEAKER_03: Like feet.
[00:22:33] SPEAKER_03: Yes.
[00:22:35] SPEAKER_03: But sort of the behavior we want out of it is actually very difficult to model.
[00:22:39] SPEAKER_03: Like it's all these are reactive behaviors that when you feel like you're, um, you're
[00:22:43] SPEAKER_03: like is hitting something, you should like retract and, you know, step again.
[00:22:47] SPEAKER_03: Uh, these are very, very hard to describe or try to learn from demonstrations directly.
[00:22:52] SPEAKER_03: But in the case of manipulation, I think the difficulty is flipped.
[00:22:58] SPEAKER_03: That it's a lot easier to capture the behavior itself.
[00:23:03] SPEAKER_03: And it's a lot harder to simulate the world.
[00:23:06] SPEAKER_03: For example, if you were to grasp a transparent cup with some orange juice in it, it's ridiculously
[00:23:14] SPEAKER_03: hard to simulate how like your hand deforms around the cup and how all those replines, how
[00:23:21] SPEAKER_03: those like the color of the juice results in like the rendering and what the policy
[00:23:28] SPEAKER_03: end up seeing, simulating that is very expensive and difficult.
[00:23:32] SPEAKER_03: But all we need to learn is just to like guess your hand to be in front of the cup and
[00:23:37] SPEAKER_03: then close with the appropriate amount of force.
[00:23:40] SPEAKER_03: And that's actually very easy to learn.
[00:23:42] SPEAKER_03: That's why like we see so many success of imitation learning in the case of robotics.
[00:23:48] SPEAKER_03: Mediflation is because the behavior itself is actually not as hard as simulating the
[00:23:55] SPEAKER_03: world.
[00:23:56] SPEAKER_03: And that's why we see faster progress there.
[00:23:58] Is there anything that you have changed your point of view on in data over the last
[00:24:02] SPEAKER_01: year?
[00:24:03] SPEAKER_01: Like it's one thing I wouldn't say changed, but just data quality really matters.
[00:24:09] SPEAKER_02: I think we know I always knew data quality matters.
[00:24:12] SPEAKER_02: But once you scale it up, like it really matters.
[00:24:16] SPEAKER_02: And then because you know, just like the diversity of behavior that you experience in a
[00:24:21] SPEAKER_02: world is very hard to control.
[00:24:23] SPEAKER_02: And the hardware failure is a harder control.
[00:24:25] SPEAKER_02: You need to constantly monitor them.
[00:24:26] SPEAKER_02: Just mean to spend a lot of huge amount of engineering effort just to make sure that
[00:24:31] SPEAKER_02: and know the data is clean.
[00:24:32] SPEAKER_03: Yeah.
[00:24:33] SPEAKER_03: And also building all those automatic processes.
[00:24:35] SPEAKER_03: We have our own way of calibrating the glove before we ship it out.
[00:24:39] SPEAKER_03: And we have this whole software system to catch if a something is broken on the glove.
[00:24:44] SPEAKER_03: And we can detect it automatically.
[00:24:46] SPEAKER_03: Is like the importance of data quality kind of translates to all these repeatable processes.
[00:24:52] SPEAKER_03: And we don't need a human to be staring at the data to know that something is wrong.
[00:24:56] SPEAKER_01: When you describe the beta for next year, a lot of it sounded like, you know, we just
[00:25:01] SPEAKER_01: want to understand behavior, like how people actually want to use it.
[00:25:04] SPEAKER_01: We can make some design decisions for the actual product.
[00:25:08] SPEAKER_01: What technical challenges do you still say?
[00:25:11] So to me, I think there's like two kind.
[00:25:14] SPEAKER_02: The number one is really figuring out the training recipe at scale.
[00:25:18] SPEAKER_02: We as a field just entered the realm of scaling and we just got amount of data that we need.
[00:25:23] SPEAKER_02: And think now is a perfect time to start to research and figure out what exactly the
[00:25:27] SPEAKER_02: recipe we need to actually get robust behaviors.
[00:25:31] SPEAKER_02: And I think we're in a unique position because the amount of data and the entire pipeline
[00:25:35] SPEAKER_02: we built around data.
[00:25:37] SPEAKER_02: The second point, I think it's just really hard.
[00:25:39] SPEAKER_02: We're still pushing the envelope, performance envelope of hardware.
[00:25:43] SPEAKER_02: It's not really clear actually what is needed, what is necessary for the hardware to be
[00:25:48] SPEAKER_02: reliable because like whenever the mechanical team build a hardware, the learning team will
[00:25:53] try to try harder to push it against the boundary and then it'll break at some point.
[00:25:58] SPEAKER_02: But I think what's interesting in this company is that everybody is under the same roof.
[00:26:03] SPEAKER_02: So immediately after something breaks, it goes straight back into mechanical design and
[00:26:07] SPEAKER_02: we have each other iteration, like I said, for the hand parts very quickly.
[00:26:12] SPEAKER_02: hardware is hard, but it is important.
[00:26:15] SPEAKER_02: And I think it's a hard but right thing to do.
[00:26:18] SPEAKER_02: And I think we as a field should avoid doing the hard things just because they're hard.
[00:26:22] SPEAKER_02: Yeah, I'll just echo a checkpoint about like first the research.
[00:26:26] SPEAKER_03: I think when there is data scarcity, it is really easy to come up with like cute fancy
[00:26:33] SPEAKER_03: research ideas that doesn't end up scaling very well.
[00:26:38] SPEAKER_03: And this is why when we build a company, we actually focus on the infrastructure and
[00:26:42] SPEAKER_03: the scalable data pipeline operations before we start to really dive into research, which
[00:26:46] SPEAKER_03: we only started to do like three months ago.
[00:26:48] SPEAKER_03: I think we really want to avoid doing research that doesn't scale and want to focus on things
[00:26:53] SPEAKER_03: that contribute to the final product.
[00:26:55] SPEAKER_03: The second point is I think robotics is so intrinsically a system that right now we don't
[00:27:05] SPEAKER_03: like there's not a existing general purpose home robot out there.
[00:27:10] SPEAKER_03: And we don't really know what the interface of different system is like what is even
[00:27:14] SPEAKER_03: good.
[00:27:15] SPEAKER_03: And in that case, if you're working with the partner, it's actually really hard for
[00:27:20] SPEAKER_03: them to understand your standard of good because your standard of good is changing all
[00:27:24] SPEAKER_03: the time.
[00:27:25] SPEAKER_03: This is why we are like building everything in house in a more full stack approach that
[00:27:29] SPEAKER_03: we build our own data collection device that is co-designed with the robot.
[00:27:33] SPEAKER_03: We build our own operation team to be like, how can we most efficiently get the most
[00:27:38] SPEAKER_03: high quality data out?
[00:27:40] SPEAKER_03: And of course our own AI training team that's the best use of these data.
[00:27:45] SPEAKER_03: I think these are the things that are really not easy.
[00:27:49] SPEAKER_03: It makes our company a lot harder to build that right now is suddenly like so many teams
[00:27:54] SPEAKER_03: and they need to orchestrate together.
[00:27:57] SPEAKER_03: But we believe it is the right thing to do.
[00:27:59] SPEAKER_03: OK, I'm going to ask you a few questions that are uncomfortable guesses now.
[00:28:03] SPEAKER_01: But when will people be able to buy robots commercially from home?
[00:28:06] SPEAKER_01: Like there's something we're really excited about because we have so many of prototype robots
[00:28:11] SPEAKER_03: in our office and really want to get it out there.
[00:28:14] SPEAKER_03: So the next step of our plan is to have a better group program, 2026.
[00:28:19] SPEAKER_03: And what it means is that for people who sign up that we selected, they will have a real
[00:28:24] SPEAKER_03: robot in their home and it will start doing chores for you.
[00:28:28] SPEAKER_03: And it's going to be a really interesting learning lesson for us because we will see like
[00:28:32] SPEAKER_03: how can we interact with the robots, we'll see like what kind of things people just really
[00:28:37] SPEAKER_03: want to do.
[00:28:39] SPEAKER_03: I think this will be before we actually ship it to the masses because we just have an
[00:28:45] SPEAKER_03: incredibly high standard of what we are willing to ship as a for a consumer experience standpoint.
[00:28:51] SPEAKER_03: We want the robot to be highly reliable, want it to be capable, want it to be cheap.
[00:28:55] SPEAKER_03: I think it really depends on the results of the beta program that will decide when is
[00:29:00] SPEAKER_03: the good time to ship it.
[00:29:01] SPEAKER_03: Is it 2027?
[00:29:02] SPEAKER_03: Is it 28?
[00:29:04] SPEAKER_03: And all of those are possible.
[00:29:06] SPEAKER_03: But it's not a decade away.
[00:29:08] SPEAKER_03: No, it's definitely not a decade away.
[00:29:10] How much do you think it could cost?
[00:29:11] SPEAKER_03: Right now, the prototype robots we have in in house, I think the cost ranges from like
[00:29:17] SPEAKER_03: $6,000 to something like $20,000.
[00:29:22] SPEAKER_03: And this is actually pretty interesting that the big difference here is not like, oh,
[00:29:26] SPEAKER_03: we find a better actuator.
[00:29:27] SPEAKER_03: They're usually the same actuators.
[00:29:28] SPEAKER_03: They're like very low cost.
[00:29:30] SPEAKER_03: But actually, it's the clotting of the robots.
[00:29:32] SPEAKER_03: When you're trying to make them at low scale, it's just really expensive.
[00:29:36] SPEAKER_03: Like the clottings are like a few thousand dollars to make.
[00:29:40] SPEAKER_03: But this is a type of things that as we scale up, it becomes like dirt cheap because instead
[00:29:45] SPEAKER_03: of like the CNC instead of hand painting them, it'll become injection molding.
[00:29:49] SPEAKER_03: What we see is that as we get the scale to a few thousand units, we can drastically reduce
[00:29:56] SPEAKER_03: the material cost, likely under 10k.
[00:30:00] SPEAKER_03: And what it implies is that when we sell the robots, the price will be somewhere around
[00:30:06] SPEAKER_03: it.
[00:30:07] Okay.
[00:30:08] SPEAKER_01: So you fast forward two, three years out.
[00:30:11] SPEAKER_01: If you look like five years and beyond the home robots are ubiquitous.
[00:30:14] SPEAKER_01: Like, what does life look like?
[00:30:16] SPEAKER_01: How does it change for the average person?
[00:30:19] SPEAKER_03: This is a different answer for everyone.
[00:30:21] SPEAKER_03: For me, like I just really hate dishes.
[00:30:25] SPEAKER_03: Like in my sink, there's always like four or five dishes.
[00:30:27] SPEAKER_03: There are like somewhat very out there that kind of stinks a little bit.
[00:30:31] SPEAKER_03: And after a long day of work, it really doesn't feel good to come up like see a home like
[00:30:35] SPEAKER_03: that.
[00:30:37] SPEAKER_03: So I think the world will live in is.
[00:30:39] SPEAKER_03: It was going to be cleaner.
[00:30:42] SPEAKER_03: It's going to be cleaner.
[00:30:43] SPEAKER_03: And I was just thinking about it as like the marginal cost of labor in homes goes to zero.
[00:30:47] SPEAKER_03: The last thing I want to make sure we do is like talk about demos, right?
[00:30:51] SPEAKER_01: There's a lot of robotics launch videos today.
[00:30:54] SPEAKER_01: It's been years since you saw an optimist serving drinks at a bar.
[00:30:59] Why are those not available?
[00:31:01] SPEAKER_01: And what is actually hard?
[00:31:02] SPEAKER_01: I think the way I'll put it is make zero assumptions.
[00:31:07] SPEAKER_03: No price.
[00:31:08] SPEAKER_03: As a nice if you see a robot handing one drink to one person first asked the question of
[00:31:15] SPEAKER_03: is that autonomous or is that highly operated?
[00:31:18] SPEAKER_03: This is the first thing.
[00:31:19] SPEAKER_03: So we look at the tweet and see what they say about it.
[00:31:22] SPEAKER_03: And then is that the show giving another slightly different color cop to the same person
[00:31:28] SPEAKER_03: or not.
[00:31:29] SPEAKER_03: If they didn't show it, it means that the robot can literally only pick up that single
[00:31:34] SPEAKER_03: cop and give it to that same person.
[00:31:37] SPEAKER_03: When we look at demos, we tend to put our human instinct into it that like, oh, if
[00:31:42] SPEAKER_03: you can hand a cop to that person, it must be able to hand a different cop to another
[00:31:45] SPEAKER_03: person.
[00:31:46] SPEAKER_03: Maybe you can also do an addition, maybe you can do a laundry.
[00:31:48] SPEAKER_03: There are a lot of like visual thinking that we can have about it, which is what's
[00:31:51] SPEAKER_03: great about robotics that there are a lot of imaginations.
[00:31:54] SPEAKER_03: But I think when we look at demos, only index on things that is strong.
[00:32:00] And that's likely the full scope of that task.
[00:32:04] SPEAKER_03: I think another aspect is at least me as a review researcher, I appreciate the number
[00:32:10] SPEAKER_02: of interactions that happens in demos.
[00:32:13] SPEAKER_02: Usually the more interactions you have, like every interaction, there's a chance of failure.
[00:32:17] SPEAKER_02: So the longer the sequence is, the harder it actually is.
[00:32:20] SPEAKER_02: So that's something we really emphasize here.
[00:32:23] SPEAKER_02: And that's actually somewhat uniquely easy for us because the glove way of data collection
[00:32:29] SPEAKER_02: is so intuitive after people.
[00:32:31] SPEAKER_02: Yeah.
[00:32:32] SPEAKER_02: It's really about like generalization and reliability.
[00:32:34] SPEAKER_03: So can you explain the demos that you guys are showing?
[00:32:36] SPEAKER_01: Yeah, of course.
[00:32:38] SPEAKER_03: So we're showing like basically three categories of demos.
[00:32:41] SPEAKER_03: The first one, as you saw, is we have this whole like messy cable.
[00:32:45] SPEAKER_03: And what the robot does is clean up the whole table and dump the food into the food waste
[00:32:50] SPEAKER_03: bin and load the dishes with dishwasher and then operate at dishwasher.
[00:32:53] SPEAKER_03: What makes this demo really hard is that it is a mix of really fine grained manipulation
[00:33:00] SPEAKER_03: with these super long horizon full range tasks as in like indigo up and it also need
[00:33:06] SPEAKER_03: to go down very much.
[00:33:08] SPEAKER_03: It's a mobile manipulation highest, exactly.
[00:33:11] SPEAKER_03: The reason that we can show this is just how nimble and easy for us to collect these
[00:33:17] SPEAKER_03: data sets to make horizon text for them possible.
[00:33:20] SPEAKER_03: And it's also about the force as well.
[00:33:22] SPEAKER_03: So you might have seen like we're trying to pick up two wine glasses with one hand.
[00:33:29] SPEAKER_03: And I struggle with this.
[00:33:30] SPEAKER_01: It's actually really hard.
[00:33:32] SPEAKER_03: And because it's like transparent objects, we need to also load it very precisely into
[00:33:36] SPEAKER_03: the into dishwasher.
[00:33:38] SPEAKER_03: A lot of it is about how much force you apply.
[00:33:41] SPEAKER_03: Because if you are trying to grasp two and one hand, if you squeeze a little harder,
[00:33:45] SPEAKER_03: you're going to break one of the glass.
[00:33:47] SPEAKER_03: And when you load it into a dishwasher, if you're pushing it in the wrong direction and
[00:33:51] SPEAKER_03: it hits something, it's going to shout out.
[00:33:52] SPEAKER_03: We did a lot of glasses when we were like you're spending with it.
[00:33:56] SPEAKER_03: So these are the tasks that are like really high stake that is not just about recovering
[00:34:02] SPEAKER_03: from mistakes, but about not making those mistakes in the first place.
[00:34:06] SPEAKER_03: And this is what's generally the case in a lot of the home tasks that you're just not
[00:34:10] SPEAKER_03: allowed to make any mistakes.
[00:34:12] SPEAKER_03: And then we get into the gyrosation demos, which we basically show our robot.
[00:34:17] SPEAKER_03: We book like six EMB and B's and we get it there zero shots and see if can do like part
[00:34:24] SPEAKER_03: of the task.
[00:34:25] SPEAKER_03: So two tasks we use one is like around table and clock all the utensils into the caddy.
[00:34:29] SPEAKER_03: The other is to grab a plate and I load it into the dishwasher.
[00:34:33] SPEAKER_03: What makes these these demos very interesting is that we don't need any data when we enter
[00:34:39] SPEAKER_03: that home.
[00:34:40] SPEAKER_03: It is pure gyrosation.
[00:34:42] SPEAKER_03: And this is as close to getting like a real product as you can get because when someone
[00:34:49] SPEAKER_03: buy a home robot, we really don't want them to like clock the huge it at themselves.
[00:34:53] SPEAKER_03: Just to like unbox it.
[00:34:55] SPEAKER_03: Also in addition to the gyrosation, those two tasks are also really precise.
[00:34:59] SPEAKER_03: We're using the exact silver verse in the home and you need like basically like a few millimeter
[00:35:06] SPEAKER_03: of precision. We're to grasp it properly. Those fours are also hard to perceive because they're
[00:35:10] SPEAKER_03: reflective. Like the lights looks weird on it. We have a transparent table home.
[00:35:16] SPEAKER_03: I think that the table looks like nothing and the robot still like reacts very well to it.
[00:35:20] SPEAKER_03: And again, the reason that we can do it is because we have all these like more than 500 people
[00:35:24] SPEAKER_03: and we've seen so many glass tables in that dataset. So the robot is able to do it.
[00:35:29] SPEAKER_03: I think the last bit of the task that we did is kind of pushing what's possible in terms of
[00:35:36] SPEAKER_03: dexterity. The two tasks we chose one is a espresso, operating espresso machine. The other is like
[00:35:43] SPEAKER_03: folding socks. We'll make these hard is that they require very fine-grinned force.
[00:35:50] SPEAKER_03: That is hard to get if you're doing with tally operation. Because these days,
[00:35:56] SPEAKER_03: there's not a good tally operation system that can let you feel how much force the robot is feeling.
[00:36:03] SPEAKER_03: So basically when you're tally operating, your hand is numb. And sometimes you are applying like
[00:36:08] SPEAKER_03: a huge amount of force on the robot, but you don't know it. And that can result in like very low
[00:36:13] SPEAKER_03: data quality that robot is also doing in that aggressive way that we really want to avoid for our
[00:36:18] system. The Saga is a very good example that when you're trying to fold it, your two fingers can
[00:36:23] SPEAKER_03: clutch. And that forms a, or we call it a force closure. You have a closed loop for the force.
[00:36:29] SPEAKER_03: And if you roll a stiff, you can apply infinite amount of force at it and doesn't look like anything.
[00:36:35] SPEAKER_03: But for us, because we're using the glove to collect the data, the human who is collecting
[00:36:39] SPEAKER_03: the country's naturally feel it is very intuitive. I think we're the first to do the sock folding
[00:36:48] SPEAKER_03: and using end-to-end to do like espresso machine out of the whole industry.
[00:36:53] SPEAKER_03: One of the things that you will also need to scale as you guys, you know,
[00:36:58] SPEAKER_01: scale up the company is the team. What are you hiring for? What are you looking for?
[00:37:03] SPEAKER_01: One thing I'm really looking forward to is.
[00:37:06] SPEAKER_02: Thanks, Big Stuff.
[00:37:07] SPEAKER_01: So it's full-stock roboticists and people who aspire to become full-stock roboticists.
[00:37:15] SPEAKER_02: Really, when you learn in this company, it's just that robotics is such a multi-disciplinary field.
[00:37:21] SPEAKER_02: You need to know mechanical, a little mechanical, a little electrical, a little code,
[00:37:25] SPEAKER_02: little data to actually fully optimize the system. And we have a couple examples of training,
[00:37:31] SPEAKER_02: full-stock self-engineered to become roboticist. Training and engineers to become roboticists.
[00:37:36] SPEAKER_02: And so if you want to learn about robotics, you can learn the whole thing, not just to
[00:37:41] SPEAKER_02: be boxing into your small little cubicle. Let us know.
[00:37:45] And you told me that you didn't write code until you got to college or something.
[00:37:51] SPEAKER_01: I was super enthusiastic about robotics. I was mostly doing a mechanical and for design before that.
[00:37:58] SPEAKER_02: And then I realized, okay, the bottleneck is actually how the robot will move.
[00:38:01] SPEAKER_02: And there's something called programming. And then the more I get into it, the deeper it gets.
[00:38:08] SPEAKER_02: And then toward the end of college, I realized, okay, there's a thing called machine learning.
[00:38:12] SPEAKER_02: And you can bring your own hundred-three models. I think this thing just goes on and on.
[00:38:15] SPEAKER_02: I think it's very natural for me to graduate X-Bamma skill set because I'm always looking forward
[00:38:20] SPEAKER_02: to building a robot.
[00:38:21] SPEAKER_02: Well, I hope you discover the next field because you're no longer doing dishes.
[00:38:24] SPEAKER_01: It's tough. It's a very fun place to work.
[00:38:27] SPEAKER_03: Whatever you can imagine about robotics and consumer products and machine learning,
[00:38:33] SPEAKER_03: you can find it here because we're just fundamentally such a full-stack company.
[00:38:37] SPEAKER_03: We're not just about a software. We're not just about a hardware, but we're about the whole
[00:38:41] SPEAKER_03: experience, the whole product. And making sure that product is general and scalable in the future.
[00:38:47] SPEAKER_03: Awesome. Congratulations.
[00:38:48] SPEAKER_01: It's really exciting.
[00:38:55] Find us on Twitter at No Pryor's Pod.
[00:39:00] SPEAKER_00: Subscribe to our YouTube channel if you want to see our faces.
[00:39:03] SPEAKER_00: Follow the show on Apple Podcasts, Spotify, or wherever you listen.
[00:39:07] SPEAKER_00: That way you get a new episode every week.
[00:39:09] SPEAKER_00: And sign up for emails or find transcripts for every episode at no-pryor's.com.