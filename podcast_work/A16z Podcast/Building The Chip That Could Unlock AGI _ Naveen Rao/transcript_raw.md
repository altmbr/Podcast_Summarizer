# Building The Chip That Could Unlock AGI | Naveen Rao

**Podcast:** A16z Podcast
**Date:** 2025-12-08
**Video ID:** wZ4DT20OHXE
**Video URL:** https://www.youtube.com/watch?v=wZ4DT20OHXE

---

[00:00:00] I think AI is the next evolution of humanity.
[00:00:03] SPEAKER_01: I think it takes us to a new level.
[00:00:04] SPEAKER_01: It allows us to collaborate and understand the world
[00:00:06] SPEAKER_01: in much deeper ways.
[00:00:08] SPEAKER_01: The V-Row, she's expert in AI.
[00:00:10] SPEAKER_00: The V-Row probably won with smartest guys in this domain.
[00:00:12] SPEAKER_01: He sees things well before anybody else sees them.
[00:00:15] SPEAKER_01: You had a lot of success doing Nirvana, Mosaic, and Databricks.
[00:00:17] SPEAKER_00: Why start a new chip company now?
[00:00:19] SPEAKER_00: First of all, it's not a chip company per se.
[00:00:21] SPEAKER_01: Most of what we're doing is really kind of looking
[00:00:23] SPEAKER_01: at first principles of how learning worked in a physical system.
[00:00:27] SPEAKER_01: Nvidia, TSMC, Google, are these potential allies
[00:00:31] SPEAKER_00: for unconventional or these competitors?
[00:00:32] SPEAKER_00: I think TSMC is absolutely going to be a partner.
[00:00:35] SPEAKER_01: Google kind of has everything internally.
[00:00:36] SPEAKER_01: And Nvidia, of course, they built the platform
[00:00:39] SPEAKER_01: to everyone's programs on today.
[00:00:40] SPEAKER_01: So are we going to be odds with Nvidia going for?
[00:00:43] SPEAKER_01: I don't know.
[00:00:43] SPEAKER_01: We'll see what the world looks like,
[00:00:44] SPEAKER_01: but there could be a world where we collaborate.
[00:00:46] SPEAKER_01: Has anyone called you crazy yet for doing this?
[00:00:48] SPEAKER_00: Oh, yeah, plenty of people.
[00:00:50] Our guest today is Naveen Rao, co-founder and CEO
[00:01:00] SPEAKER_00: of Unconventional AI, which is an AI chip startup.
[00:01:03] SPEAKER_00: Prior to that, Naveen was at Databricks as head of AI.
[00:01:06] SPEAKER_00: And co-founder, two successful companies, Mosaic
[00:01:09] SPEAKER_00: in the Cloud Computing World and Nirvana
[00:01:12] SPEAKER_00: doing AI chip accelerators before was cool.
[00:01:15] SPEAKER_00: We're here reporting from NURPS.
[00:01:18] SPEAKER_00: And yeah, great to have you on the podcast, Naveen.
[00:01:21] SPEAKER_00: Welcome.
[00:01:22] SPEAKER_00: Thanks, thanks for having me.
[00:01:23] SPEAKER_00: So you were kind of at the Vanguard,
[00:01:25] SPEAKER_00: thinking about what the proper hardware is
[00:01:28] SPEAKER_00: for running AI workloads.
[00:01:29] SPEAKER_00: Absolutely.
[00:01:30] SPEAKER_01: I mean, it's like we have a hammer, everything's an AL,
[00:01:33] SPEAKER_01: I suppose, but the early part of my career was really about,
[00:01:36] how do I take certain algorithms and capabilities
[00:01:40] SPEAKER_01: and shrink them, make them faster,
[00:01:41] SPEAKER_01: put them in a form factors that make those use cases
[00:01:44] SPEAKER_01: to afford wireless technology or video compression.
[00:01:51] SPEAKER_01: You couldn't do video compression real time
[00:01:53] SPEAKER_01: on a laptop back then.
[00:01:54] SPEAKER_01: It was just there wasn't enough computing power.
[00:01:56] SPEAKER_01: So you actually needed to build hardware
[00:01:58] SPEAKER_01: to those kinds of things.
[00:01:59] SPEAKER_01: So my career was, early part of my career was all about that.
[00:02:02] SPEAKER_01: And then I went back to academia,
[00:02:05] SPEAKER_01: did a PhD in neuroscience.
[00:02:06] SPEAKER_01: And so you still kind of look at it like,
[00:02:07] SPEAKER_01: hey, can I make something better, it's more efficient?
[00:02:10] SPEAKER_00: And so you sold Nirvana to Intel.
[00:02:13] SPEAKER_00: And then founded Mosaic, which is a cloud company.
[00:02:17] SPEAKER_00: It's interesting to sort of cross domains like that,
[00:02:19] SPEAKER_00: I think, to be able to look at hardware and software.
[00:02:22] SPEAKER_00: I would sort of argue Mosaic was really a software company.
[00:02:25] SPEAKER_00: How did you make that decision and why do you
[00:02:28] SPEAKER_00: think you have these diverse interests?
[00:02:30] Well, I think I was, I guess you would call it OG,
[00:02:33] SPEAKER_01: kind of full stack.
[00:02:34] SPEAKER_01: Now, full stack engineer means something different
[00:02:36] SPEAKER_01: than it did back then.
[00:02:37] SPEAKER_01: I think back then, and then someone who understands
[00:02:40] SPEAKER_01: potentially devices like Silicon,
[00:02:42] SPEAKER_01: how to do logic design, computer architecture,
[00:02:47] SPEAKER_01: low level software, maybe OS level software
[00:02:50] SPEAKER_01: and then application.
[00:02:51] SPEAKER_01: That was a full stack engineer.
[00:02:53] SPEAKER_01: I was actually touched all those topics.
[00:02:56] SPEAKER_01: So to me, it was very natural to kind of think
[00:02:57] SPEAKER_01: across these boundaries.
[00:02:59] SPEAKER_01: To me, software and hardware is not really a natural boundary.
[00:03:03] SPEAKER_01: It's just where we decide to draw the line and say,
[00:03:05] SPEAKER_01: OK, this is something I make configurable or I don't.
[00:03:08] SPEAKER_01: And it's like, where is the world
[00:03:11] SPEAKER_01: going to consume something?
[00:03:12] SPEAKER_01: Where is the problem?
[00:03:14] SPEAKER_01: You then write size and figure out the solution to go and hit it.
[00:03:18] SPEAKER_00: Now, full stack means I know JavaScript and Python.
[00:03:21] SPEAKER_00: That's right.
[00:03:22] SPEAKER_00: So you've had a lot of success doing
[00:03:23] SPEAKER_00: both of those things in a data bricks.
[00:03:25] SPEAKER_00: Why start a new chip company?
[00:03:27] SPEAKER_00: No.
[00:03:28] It is kind of crazy.
[00:03:29] SPEAKER_01: It's one of these things like, I actually
[00:03:31] SPEAKER_01: was first off there.
[00:03:32] SPEAKER_01: It's not a chip company per se.
[00:03:33] SPEAKER_01: Most of what we're doing is at the beginning is theory.
[00:03:37] SPEAKER_01: And really looking at first principles
[00:03:40] SPEAKER_01: of how learning works in a physical system.
[00:03:45] SPEAKER_01: And the reason you can do this is just purely out of passion.
[00:03:49] SPEAKER_01: I think we can change how a computer is built.
[00:03:52] SPEAKER_01: We've been building largely the same kind of computer for 80 years.
[00:03:56] SPEAKER_01: We went digital back in the 1940s.
[00:03:58] SPEAKER_01: And in undergrad, in the 1990s, when I
[00:04:03] SPEAKER_01: weren't about the dynamics of the brain,
[00:04:06] SPEAKER_01: like the brain's 20 watts of energy and the kind of computations
[00:04:09] SPEAKER_01: that can happen inside of brain and neural systems,
[00:04:11] SPEAKER_01: I was just blown away then.
[00:04:14] SPEAKER_01: I'm still blown away by it.
[00:04:15] SPEAKER_01: And I think we haven't really scratched the surface
[00:04:18] SPEAKER_01: of how we can get close to that.
[00:04:21] SPEAKER_01: Biology is exquisitely efficient.
[00:04:23] SPEAKER_01: It's very fast.
[00:04:24] SPEAKER_01: It writes sizes itself to the application at hand.
[00:04:29] SPEAKER_01: When you're showing out, you don't use much energy.
[00:04:32] SPEAKER_01: But you're still aware of other threats and things like this.
[00:04:34] SPEAKER_01: And then once a threat happens, everything turns on.
[00:04:37] SPEAKER_01: It's very dynamic.
[00:04:39] SPEAKER_01: And we really haven't built systems like this.
[00:04:40] SPEAKER_01: And I've been in the industry long enough to know
[00:04:44] SPEAKER_01: that we have to have an incentive to build things.
[00:04:47] SPEAKER_01: You can't just say, I want to build this cool thing.
[00:04:49] SPEAKER_01: Therefore, I go build it.
[00:04:50] SPEAKER_01: Maybe in academia, you can do that.
[00:04:52] SPEAKER_01: But in the real world, I can't.
[00:04:54] SPEAKER_01: And now it's exciting because those concepts are super relevant.
[00:04:59] SPEAKER_01: We're at a point in time where computing
[00:05:02] SPEAKER_01: is bound by energy at the level level,
[00:05:06] SPEAKER_01: which just was never true in all of humanity.
[00:05:09] SPEAKER_01: And so for those of us who aren't experts,
[00:05:13] SPEAKER_00: can you describe the difference between digital
[00:05:15] SPEAKER_00: and analog computing systems?
[00:05:17] SPEAKER_00: And why do you think the architecture is evolved
[00:05:22] SPEAKER_00: the way it has more digital focus over and over decades?
[00:05:26] Yeah, I mean, very simply,
[00:05:28] SPEAKER_01: digital computers implement numerics.
[00:05:32] SPEAKER_01: And numerics with some sort of estimation, right?
[00:05:34] SPEAKER_01: I mean, in a digital computer, a number
[00:05:37] SPEAKER_01: is represented by a fixed number of bits.
[00:05:39] SPEAKER_01: And that has some precision error and things like this.
[00:05:43] SPEAKER_01: It's just a way to implement the system.
[00:05:45] SPEAKER_01: If you make it enough bits, like 64 bits,
[00:05:47] SPEAKER_01: you can largely say that maybe the error is small.
[00:05:50] SPEAKER_01: You don't have to think about it.
[00:05:52] SPEAKER_01: And so when the digital computer is capable of simulating
[00:05:56] SPEAKER_01: anything that you can express as numbers and arithmetic.
[00:05:59] SPEAKER_01: So it became a very general machine.
[00:06:01] SPEAKER_01: I can literally simulate any physical process,
[00:06:04] SPEAKER_01: all the physics we try to do computational physics, right?
[00:06:07] SPEAKER_01: I have that equation.
[00:06:08] SPEAKER_01: I can then write numeric solvers that sort of deal
[00:06:11] SPEAKER_01: with those imprecisions in the number of bits.
[00:06:16] SPEAKER_01: And so this became obviously computer science,
[00:06:19] SPEAKER_01: this entire field now.
[00:06:20] SPEAKER_01: And we went that direction actually very early on
[00:06:23] SPEAKER_01: because we couldn't scale up computation.
[00:06:27] SPEAKER_01: It was actually kind of an interesting conversation
[00:06:29] SPEAKER_01: if you look from back then, not that it was there, of course.
[00:06:31] SPEAKER_01: But if you look at the papers and things,
[00:06:33] SPEAKER_01: they actually looked very similar to today
[00:06:34] SPEAKER_01: in terms of scaling up GPUs.
[00:06:37] SPEAKER_01: Analog computers were actually some of the first computers.
[00:06:40] SPEAKER_01: And they worked really well.
[00:06:42] SPEAKER_01: They were very efficient, but they couldn't be scaled up
[00:06:45] SPEAKER_01: because of manufacturing variability.
[00:06:47] SPEAKER_01: So someone said, oh, OK, you know what?
[00:06:49] SPEAKER_01: I can actually say they can make a vacuum tube
[00:06:52] SPEAKER_01: with a high or low, very reliably.
[00:06:55] SPEAKER_01: We can't characterize it in between very well,
[00:06:57] SPEAKER_01: but I can say it's higher low.
[00:06:59] SPEAKER_01: And so that was kind of where we went to digital abstraction.
[00:07:01] SPEAKER_01: And then we could scale up.
[00:07:03] SPEAKER_01: ENIAC, which was built in 1945 at 18,000 vacuum tubes.
[00:07:07] SPEAKER_01: So 18,000 kind of somewhere, how many GPUs
[00:07:09] SPEAKER_01: people use now are for hard-skilled trading.
[00:07:11] SPEAKER_01: So scaling things up is always a hard problem.
[00:07:14] SPEAKER_01: And once you figure out how to do it,
[00:07:15] SPEAKER_01: it makes a paradigm happen.
[00:07:17] SPEAKER_01: And I think that's why we went to digital.
[00:07:19] SPEAKER_01: But analog still is inherently more efficient,
[00:07:22] SPEAKER_01: because it's actually analogous computing
[00:07:25] SPEAKER_01: is the way to think about it.
[00:07:26] SPEAKER_01: Can I build a physical system that is similar to the quantity
[00:07:29] SPEAKER_01: I'm trying to express or compute over?
[00:07:32] SPEAKER_01: You're effectively using the physics of the underlying
[00:07:36] SPEAKER_01: medium to do the computation.
[00:07:38] SPEAKER_01: And so in digital computers, we have transistors.
[00:07:41] SPEAKER_00: Just to make it sort of concrete, what kind of substrate
[00:07:43] SPEAKER_00: are you talking about for analog computers?
[00:07:46] Yeah, analog computers can be lots of different things.
[00:07:48] SPEAKER_01: There's wind tunnels, our great example of an analog
[00:07:52] SPEAKER_01: computer in the sets where I have a race car, a track,
[00:07:56] SPEAKER_01: or an airplane.
[00:07:57] SPEAKER_01: And I want to understand how the wind moves around it.
[00:08:01] SPEAKER_01: And you can, in theory, solve those things computationally.
[00:08:05] SPEAKER_01: The problem is you're always going to be off.
[00:08:07] SPEAKER_01: It's very hard to know what the real system is going to look like.
[00:08:09] SPEAKER_01: And doing things with computational fluid dynamics
[00:08:12] SPEAKER_01: accurately is pretty hard.
[00:08:14] SPEAKER_01: So people still build wind tunnels.
[00:08:15] SPEAKER_01: That's actually modeling them.
[00:08:16] SPEAKER_01: That's an analog computer.
[00:08:19] SPEAKER_01: I think we still have lots of reasons
[00:08:21] SPEAKER_01: to build these analogous type computers.
[00:08:22] SPEAKER_01: Now, in the situation we're talking about,
[00:08:25] SPEAKER_01: we can actually build circuits in silicon
[00:08:28] SPEAKER_01: to recapitulate behaviors of neural networks.
[00:08:33] SPEAKER_01: So what we're doing today is more specified
[00:08:36] SPEAKER_01: than what we're doing any years ago in a sense
[00:08:38] SPEAKER_01: is that then we were trying to automate generic calculation,
[00:08:41] SPEAKER_01: which was used to calculate artillery trajectories.
[00:08:44] SPEAKER_01: It was used to calculate finances.
[00:08:46] SPEAKER_01: Maybe some physics problems like going into space,
[00:08:49] SPEAKER_01: things like that.
[00:08:50] SPEAKER_01: Those require determinism and specificity
[00:08:54] SPEAKER_01: around these numbers and these computations.
[00:08:57] SPEAKER_01: Intelligence is a different beast.
[00:08:59] SPEAKER_01: You can build it out of numbers,
[00:09:00] SPEAKER_01: but is it naturally built out of numbers?
[00:09:03] SPEAKER_01: I don't know.
[00:09:03] SPEAKER_01: The neural network is actually a stochastic machine.
[00:09:06] SPEAKER_01: And so why are we using the substrate
[00:09:09] SPEAKER_01: that is highly precise in the termistic for something
[00:09:13] SPEAKER_01: that's actually stochastic and distributed in nature?
[00:09:16] SPEAKER_01: So we believe we can find the right isomorphism
[00:09:19] SPEAKER_01: in electrical circuits that can subserv intelligence.
[00:09:22] SPEAKER_01: That's a pretty wild idea, isn't it?
[00:09:26] SPEAKER_00: Maybe on packet, one level deeper.
[00:09:29] SPEAKER_00: Because I totally agree with you.
[00:09:32] SPEAKER_00: It's like computers for decades
[00:09:35] SPEAKER_00: have been sort of the complement to human intelligence.
[00:09:37] SPEAKER_00: It's like, hey, my brain isn't really great
[00:09:39] SPEAKER_00: at computing an orbital trajectory.
[00:09:41] SPEAKER_00: And I don't want to burn up on reentry.
[00:09:44] SPEAKER_00: So a computer can help us with this incredible degree
[00:09:46] SPEAKER_00: of precision.
[00:09:48] SPEAKER_00: We're now kind of going the opposite direction, right?
[00:09:50] SPEAKER_00: We're actually trying to encode more sort of fuzziness
[00:09:54] SPEAKER_00: into computer systems.
[00:09:56] SPEAKER_00: So yeah, so maybe just a little bit deeper
[00:09:57] SPEAKER_00: on this idea of an analog.
[00:09:58] SPEAKER_00: And why intelligence is a good fit for analog systems?
[00:10:03] SPEAKER_00: Well, I mean, the best examples
[00:10:05] SPEAKER_01: we have of intelligent systems in nature of brains.
[00:10:08] SPEAKER_01: And it's often been said, human brains
[00:10:12] SPEAKER_01: are not 20 watts of energy.
[00:10:13] SPEAKER_01: That's true.
[00:10:14] SPEAKER_01: But if you look at mammalian brains generally,
[00:10:17] SPEAKER_01: that's extremely efficient, like a squirrel or a cat.
[00:10:19] SPEAKER_01: It's like a tentable lot.
[00:10:20] SPEAKER_01: And so there's something there that we're still missing.
[00:10:23] SPEAKER_01: And not to say that we understand all of it,
[00:10:26] SPEAKER_01: but part of what I think we're missing is,
[00:10:29] SPEAKER_01: we have lots of abstractions in a computer
[00:10:31] SPEAKER_01: that are quite lossy.
[00:10:33] SPEAKER_01: In a brain, the neural network dynamics
[00:10:36] SPEAKER_01: are implemented physically.
[00:10:38] SPEAKER_01: So there is no abstraction.
[00:10:39] SPEAKER_01: Intelligence is the physics.
[00:10:41] SPEAKER_01: There are one in the same.
[00:10:42] SPEAKER_01: There's no OS and some sort of API and this and that.
[00:10:46] SPEAKER_00: So there's some visual stimulus, for instance,
[00:10:48] SPEAKER_00: that directly activates an actual neural network
[00:10:51] SPEAKER_00: and produces some somatic response, that sort of thing.
[00:10:54] SPEAKER_00: Exactly.
[00:10:55] SPEAKER_01: And those things are mediated by chemical diffusion
[00:10:58] SPEAKER_01: and just the physical properties of the near
[00:11:02] SPEAKER_01: on the physics itself.
[00:11:03] SPEAKER_01: So I think absolutely it's possible to build something
[00:11:07] SPEAKER_01: that's much more efficient by using physics.
[00:11:10] SPEAKER_01: In an analogous way, that is 100% true.
[00:11:13] SPEAKER_01: Can we do it and build a product out of it?
[00:11:17] SPEAKER_01: Is really the question we're asking you're unconventional?
[00:11:20] And as part of the idea that now is the right time
[00:11:22] SPEAKER_00: because AI is both a huge and a unique workload.
[00:11:26] SPEAKER_00: Yeah, absolutely.
[00:11:27] SPEAKER_01: It's interesting.
[00:11:28] SPEAKER_01: So just maybe some stats here.
[00:11:30] SPEAKER_01: The US is about 50% of the world's data center capacity.
[00:11:34] SPEAKER_01: And today we put about 4% of the energy grid,
[00:11:37] SPEAKER_01: of the US energy grid into those data centers.
[00:11:40] SPEAKER_01: And this past year, 2025 was the first time we started
[00:11:43] SPEAKER_01: to see news articles about brownouts in the Southwest
[00:11:46] SPEAKER_01: during the summer.
[00:11:47] SPEAKER_01: And just imagine what happens when this goes to 8%,
[00:11:51] SPEAKER_01: 10% of the energy grid.
[00:11:52] SPEAKER_01: It's not going to be a good place that we're in.
[00:11:55] SPEAKER_01: So can we build more power?
[00:11:57] SPEAKER_01: Absolutely.
[00:11:57] SPEAKER_01: We should.
[00:11:58] SPEAKER_01: Building power generation is very hard, expensive.
[00:12:01] SPEAKER_01: And it's infrastructure.
[00:12:02] SPEAKER_01: Like it takes time.
[00:12:04] SPEAKER_01: You can't bring online so many gigabytes per year.
[00:12:09] SPEAKER_01: So something only were four per year.
[00:12:12] SPEAKER_01: By some estimates, we need 400 gigawatts additional capacity
[00:12:16] SPEAKER_01: over the next 10 years to power the demand for AI.
[00:12:19] SPEAKER_01: Well, so a huge shortfall.
[00:12:20] SPEAKER_01: And so we really just need to rethink this.
[00:12:23] The 15-year-old sci-fi nerd in me says, wow,
[00:12:27] SPEAKER_00: we're mobilizing species scale resources
[00:12:30] SPEAKER_00: to invent the future.
[00:12:32] SPEAKER_00: We are.
[00:12:33] SPEAKER_00: Then there's the practical.
[00:12:34] SPEAKER_00: It's like even if we add 400 gigawatts of production capacity
[00:12:38] SPEAKER_00: our 1970s era transmission grid is probably
[00:12:42] SPEAKER_00: going to melt under the load.
[00:12:43] SPEAKER_00: So yeah, so there's very serious infrastructure hurdles
[00:12:46] SPEAKER_00: to this, I think.
[00:12:47] SPEAKER_00: It's hard to get a lot of humans to act together.
[00:12:49] SPEAKER_00: It's just a reality.
[00:12:51] That's what has to happen to me to solve these problems.
[00:12:54] What trade-offs do you think this entails?
[00:12:56] SPEAKER_00: Sort of the path you're pursuing
[00:12:57] SPEAKER_00: versus the mainstream digital path, no?
[00:13:00] Yeah, I actually don't see it as it's digital or analog.
[00:13:03] SPEAKER_01: It doesn't work like that.
[00:13:04] SPEAKER_01: I think there are certain types of workloads
[00:13:06] SPEAKER_01: that are amenable to these analog approaches,
[00:13:09] SPEAKER_01: especially the ones that can be expressed
[00:13:11] SPEAKER_01: as dynamical system, dynamics mean time.
[00:13:15] SPEAKER_01: They have time associated with them.
[00:13:16] SPEAKER_01: In the real world, every physical process has time.
[00:13:19] SPEAKER_01: And in the computing world, like a numeric computing world,
[00:13:22] SPEAKER_01: we actually don't have that concept.
[00:13:24] SPEAKER_01: You simulate time with numbers.
[00:13:26] Actually, simulating time is very useful
[00:13:28] SPEAKER_01: in certain problems.
[00:13:30] SPEAKER_01: So I think we should still build those things.
[00:13:32] SPEAKER_01: And we should still have those capabilities
[00:13:34] SPEAKER_01: for the problems that we need to solve that way.
[00:13:37] SPEAKER_01: But for these problems where, like you said, it's a bit fuzzier.
[00:13:41] SPEAKER_01: I'm trying to retrieve and summarize
[00:13:42] SPEAKER_01: across multiple inputs.
[00:13:44] SPEAKER_01: That's actually what brains do really well.
[00:13:47] SPEAKER_01: They can take in tons of data and sort of
[00:13:50] SPEAKER_01: formulate a model of how those things interact.
[00:13:54] SPEAKER_01: And sometimes this model is going to be actually
[00:13:55] SPEAKER_01: extremely accurate.
[00:13:56] SPEAKER_01: Like, look at it, athlete.
[00:14:00] SPEAKER_01: Alexander O'Connor, Al Capitan.
[00:14:04] SPEAKER_01: He's just thinking about the precision that's required.
[00:14:06] SPEAKER_01: It still scares me every time I see it.
[00:14:09] SPEAKER_01: And if he slips, like just, at least off
[00:14:11] SPEAKER_01: kind of millimeter in some places, he dies.
[00:14:14] SPEAKER_01: And that's true for like every top level athlete.
[00:14:17] SPEAKER_01: There are someone who's the only Steph Curry,
[00:14:21] SPEAKER_00: the story is he set up a special tracking system
[00:14:23] SPEAKER_00: so he can make sure the ball was sitting
[00:14:24] SPEAKER_00: in the middle of the rim, not just going through.
[00:14:28] SPEAKER_00: So the level of precision, these guys
[00:14:29] SPEAKER_00: hit with a neural network that's noisy is actually quite high.
[00:14:33] SPEAKER_01: So neural systems can actually do a lot of precision
[00:14:37] SPEAKER_01: under certain circumstances.
[00:14:38] SPEAKER_01: But what's interesting about these situations
[00:14:40] SPEAKER_01: is Steph Curry, when he shoots a ball,
[00:14:43] SPEAKER_01: is never going to shoot under ideal circumstances in a game.
[00:14:46] SPEAKER_00: Always it's a unique input.
[00:14:48] SPEAKER_01: There's a lot of different input varieties coming at you,
[00:14:51] SPEAKER_01: like where the players are precisely where you're standing.
[00:14:55] SPEAKER_01: Maybe your shoes are different.
[00:14:56] SPEAKER_01: Maybe the surface is a little different.
[00:14:57] SPEAKER_01: Like maybe the ball is tackier or your hands are sweaty.
[00:15:00] SPEAKER_01: Like there's so many inputs.
[00:15:02] SPEAKER_01: And we kind of put them all together and integrate them.
[00:15:04] SPEAKER_01: It's still a very accurate behavior.
[00:15:06] SPEAKER_01: So brains are exceptionally good at this.
[00:15:08] SPEAKER_01: And that's the set of problems that is actually
[00:15:11] SPEAKER_01: very useful to solve.
[00:15:13] SPEAKER_01: And now we're approaching those problems.
[00:15:15] SPEAKER_01: But it doesn't mean we don't still
[00:15:16] SPEAKER_01: use computational substrates to do actual computation.
[00:15:21] SPEAKER_01: This is kind of an intelligent substrate.
[00:15:23] And so what types of AI models or data modalities
[00:15:26] SPEAKER_00: do you expect your part of our own B-Well suit for?
[00:15:31] Yeah, so we're obviously starting
[00:15:33] SPEAKER_01: with the state of the art today, like transformers, diffusion
[00:15:36] SPEAKER_01: models, they work.
[00:15:38] SPEAKER_01: They do really good stuff.
[00:15:39] SPEAKER_01: So we shouldn't throw that out.
[00:15:41] SPEAKER_01: And diffusion models and flow models
[00:15:43] SPEAKER_01: are actually energy-based models are actually
[00:15:45] SPEAKER_01: pretty interesting because they inherently
[00:15:47] SPEAKER_01: have dynamics as part of them.
[00:15:49] SPEAKER_01: They're literally written as an ordinary differential equation.
[00:15:52] SPEAKER_01: So that makes it so set, hey, can I map those dynamics
[00:15:57] SPEAKER_01: onto the dynamics of a physical system in some way
[00:15:59] SPEAKER_01: that's either fixed or has some principle way of evolving?
[00:16:04] SPEAKER_01: And then can I basically use that physical system
[00:16:07] SPEAKER_01: to implement that thing and do it very
[00:16:09] SPEAKER_01: efficiently with the physics?
[00:16:10] SPEAKER_01: So that's kind of the nature of what we're doing.
[00:16:12] SPEAKER_01: And we will be releasing some open source and things
[00:16:15] SPEAKER_01: around this to let people play around.
[00:16:17] SPEAKER_01: But transformers are really, they're
[00:16:21] SPEAKER_01: big innovation because they made the constructs of a GPU
[00:16:25] SPEAKER_01: work extremely well.
[00:16:27] SPEAKER_01: And it doesn't mean it's wrong, but I don't think there's
[00:16:30] SPEAKER_01: nothing natural.
[00:16:31] SPEAKER_01: There's no natural law about the parameter of a transformer.
[00:16:35] SPEAKER_01: Transformers parameter is a function
[00:16:36] SPEAKER_01: of the nonlinearities and the way a whole thing is set up
[00:16:39] SPEAKER_01: with attention.
[00:16:40] SPEAKER_01: There's going to be some kind of mapping
[00:16:42] SPEAKER_01: between transformer parameter spaces
[00:16:44] SPEAKER_01: and these other parameter spaces.
[00:16:45] SPEAKER_01: And transformers are, I think, have kind of use
[00:16:50] SPEAKER_01: of parameters to accomplish what they do.
[00:16:52] SPEAKER_01: I have to ask just since you mentioned energy-based models
[00:16:56] SPEAKER_00: and Jan McEun has been writing quite a lot about this,
[00:17:01] SPEAKER_00: do you think pursuing these sorts of paths
[00:17:04] SPEAKER_00: that you're talking about gets us closer on the path to AGI,
[00:17:08] SPEAKER_00: whatever AGI means?
[00:17:10] Honestly, I do.
[00:17:12] SPEAKER_01: The reason I feel that way, and again, this is hand-wavy.
[00:17:14] SPEAKER_01: I'm going to be really honest.
[00:17:15] SPEAKER_01: That's why I'm putting quotes around the GGI.
[00:17:17] SPEAKER_00: The discussion is necessarily hand-wavy.
[00:17:20] SPEAKER_01: It's got to be, because we just don't know.
[00:17:21] SPEAKER_01: But my intuition says that anything
[00:17:25] SPEAKER_01: where the basis is dynamic, which has time and causality
[00:17:29] SPEAKER_01: as part of it will be a better basis than something
[00:17:31] SPEAKER_01: it's not.
[00:17:32] SPEAKER_01: So we've largely tried to remove that.
[00:17:34] SPEAKER_01: And a lot of times you can write math down.
[00:17:37] SPEAKER_01: It's reversible in time and things like that.
[00:17:39] SPEAKER_01: But physical world tends not to be.
[00:17:41] SPEAKER_01: At least the way we perceive it.
[00:17:42] SPEAKER_01: And so can we build out of elements of the physical world
[00:17:45] SPEAKER_01: that are, do you have time evolution?
[00:17:48] SPEAKER_01: I think that's the right basis to build something
[00:17:50] SPEAKER_01: that understands causation.
[00:17:53] SPEAKER_01: So I do think we'll have something that is better
[00:17:55] SPEAKER_01: and we'll give us something closer
[00:17:57] SPEAKER_01: to what we really think is intelligence.
[00:18:00] SPEAKER_01: Because yes, we have intelligence in these machines.
[00:18:03] SPEAKER_01: I don't think there are anywhere close to AGI
[00:18:04] SPEAKER_01: because they still make stupid errors.
[00:18:06] SPEAKER_01: They're very useful tools.
[00:18:08] SPEAKER_01: But they're not working with a person, right?
[00:18:10] SPEAKER_01: I think most people at that.
[00:18:12] SPEAKER_01: That's actually really interesting.
[00:18:13] SPEAKER_00: So the thing that's missing in AI behavior,
[00:18:19] SPEAKER_00: which I think a lot of us see that there's something missing
[00:18:22] SPEAKER_00: but can't quite put a name to it,
[00:18:24] SPEAKER_00: it sounds like your arguing part of that
[00:18:25] SPEAKER_00: is sort of a real sense of causality.
[00:18:28] SPEAKER_00: And that training and more dynamic regime
[00:18:33] SPEAKER_00: may impart this kind of like a parent understanding
[00:18:35] SPEAKER_00: of causality better than what we have now.
[00:18:37] SPEAKER_00: Yeah, and again, hand away.
[00:18:38] SPEAKER_00: But yes, I mean, look, you have kids, little kids,
[00:18:42] SPEAKER_01: and you see them.
[00:18:43] SPEAKER_01: Children kind of innately understand causality in some ways.
[00:18:46] SPEAKER_01: Like, you know, this happened and that happened.
[00:18:48] SPEAKER_01: And yes, I know you can say like,
[00:18:50] SPEAKER_01: it's reinforcement-orinating or whatever.
[00:18:52] SPEAKER_01: It's some part of it.
[00:18:53] SPEAKER_01: But there's something innate that we understand causality.
[00:18:56] SPEAKER_01: In fact, that's how we move our limbs and all of that.
[00:18:58] SPEAKER_01: I know if I send a certain command to my arm,
[00:19:00] SPEAKER_01: it'll do something.
[00:19:02] SPEAKER_01: So I think there's something innate about the way our brains
[00:19:04] SPEAKER_01: are wired.
[00:19:05] SPEAKER_01: It builds out of primitives that are,
[00:19:07] SPEAKER_01: that do understand causation.
[00:19:09] SPEAKER_01: Put unconventional in the context of the broader industry
[00:19:12] SPEAKER_00: for me like Nvidia, TSMC, Google,
[00:19:17] SPEAKER_00: are these potential allies for unconventional
[00:19:20] SPEAKER_00: or these competitors, how do you think about it?
[00:19:22] SPEAKER_00: Yeah, I mean, a couple of things that we set out to do
[00:19:25] SPEAKER_01: when we built where we were starting this company was,
[00:19:28] SPEAKER_01: see if we can find a paradigm that's analogous
[00:19:30] SPEAKER_01: to intelligence within five years.
[00:19:32] SPEAKER_01: And then at the five year mark,
[00:19:34] SPEAKER_01: we should be able to build something that's scalable
[00:19:36] SPEAKER_01: from a manufacturing standpoint.
[00:19:37] SPEAKER_01: So you know, you can think about building a computer
[00:19:40] SPEAKER_01: out of many different things.
[00:19:42] SPEAKER_01: But if it's not scalable from a manufacturing standpoint,
[00:19:44] SPEAKER_01: we can't intercept this global energy problem.
[00:19:48] SPEAKER_01: So we need to have somebody say,
[00:19:49] SPEAKER_01: okay, go build 10 million of these things, right?
[00:19:52] SPEAKER_01: So I think TSMC is absolutely gonna be a partner
[00:19:55] SPEAKER_01: forward, you know, met with them recently.
[00:19:57] SPEAKER_01: And you know, we wanna work closely with them
[00:19:59] SPEAKER_01: to make sure we get what we need,
[00:20:01] SPEAKER_01: get faster on time, to prototype and all of that.
[00:20:04] SPEAKER_01: Google and video, Microsoft, all these guys are,
[00:20:08] SPEAKER_01: you know, at the forefront of where the application spaces,
[00:20:11] SPEAKER_01: obviously Google kind of has everything internally.
[00:20:14] SPEAKER_01: And I think they're working on sort of lower risk,
[00:20:19] SPEAKER_01: but you know, continual improvements
[00:20:21] SPEAKER_01: for their hardware with TPUs, you mean?
[00:20:23] SPEAKER_01: With TPUs, yeah, from what I can see,
[00:20:25] SPEAKER_01: you know, just publicly is, it makes total sense, right?
[00:20:28] SPEAKER_01: They have a business to run and they're trying
[00:20:29] SPEAKER_01: to make the margins better.
[00:20:31] SPEAKER_01: And you know, how can I do that with all the tools
[00:20:33] SPEAKER_01: I have at, you know, in front of me?
[00:20:36] SPEAKER_01: And video, of course, you know,
[00:20:37] SPEAKER_01: they've built the platform that everyone programs on today.
[00:20:41] SPEAKER_01: So, is it, are we gonna be at odds with Nvidia going for?
[00:20:45] SPEAKER_01: I don't know, we'll see what the world looks like,
[00:20:47] SPEAKER_01: but I mean, we are trying to build a better substrate
[00:20:51] SPEAKER_01: than Matrix multiply.
[00:20:53] SPEAKER_01: There could be a world where we collaborate
[00:20:55] SPEAKER_01: on such solutions.
[00:20:57] SPEAKER_01: And, you know, we're open to all of these things.
[00:21:00] Look, where do you, where do you personally get the motivation
[00:21:03] SPEAKER_00: to get up in the morning and build this company?
[00:21:05] SPEAKER_00: I mean, you've had a lot of success in your career,
[00:21:06] SPEAKER_00: the C-Earn startup.
[00:21:08] SPEAKER_00: What, you know, what's exciting about this to you?
[00:21:12] I don't know, it's, it's a weird thing.
[00:21:14] SPEAKER_01: Like if you have a work in hardware, it's hard.
[00:21:17] SPEAKER_01: I've had the, been fortunate to work in hardware and software.
[00:21:20] SPEAKER_01: And, you know, I love writing a bunch of software
[00:21:23] SPEAKER_01: and then hitting compile and seeing it work.
[00:21:24] SPEAKER_01: That's, that's a good dopamine hit.
[00:21:26] SPEAKER_01: But man, when you work on these hardware
[00:21:28] SPEAKER_01: and you turn that thing on, that's a big dopamine hit.
[00:21:31] SPEAKER_01: That's like, this is like celebration jumping,
[00:21:34] SPEAKER_01: you know, jumping up in the air high five.
[00:21:35] SPEAKER_01: I think it's a different thing.
[00:21:36] SPEAKER_01: And I don't know, you sort of live for these moments, you know?
[00:21:40] SPEAKER_01: Like when I was at Intel, like,
[00:21:42] SPEAKER_01: I was one of the only execs would go to the lab
[00:21:44] SPEAKER_01: and force ship would come back and I'm like,
[00:21:45] SPEAKER_01: I want to see what happens.
[00:21:47] SPEAKER_01: Let's see what happens.
[00:21:48] SPEAKER_01: Sometimes you turn on, sometimes you turn on,
[00:21:49] SPEAKER_01: it's like, you see the little puff of spokes come out.
[00:21:52] SPEAKER_01: She likes, oh.
[00:21:54] SPEAKER_01: That's not good.
[00:21:55] SPEAKER_01: But you want to be there, it's going to be part of the moment.
[00:21:56] SPEAKER_01: But I think that's part of it.
[00:21:59] SPEAKER_01: I think for me, personally, like, we have this opportunity now
[00:22:03] SPEAKER_01: that we can really change the world of computing
[00:22:07] SPEAKER_01: and make AI ubiquitous.
[00:22:08] SPEAKER_01: I'm the opposite of an AI Doomer.
[00:22:11] SPEAKER_01: I think AI is the next evolution of humanity.
[00:22:14] SPEAKER_01: I think it takes us to a new level
[00:22:16] SPEAKER_01: that allows us to collaborate, understand each other
[00:22:18] SPEAKER_01: and understand the world and touch deep away.
[00:22:20] SPEAKER_01: Totally agree.
[00:22:21] SPEAKER_01: So every technology has negatives,
[00:22:23] SPEAKER_01: but the positive is to be so far away.
[00:22:25] SPEAKER_01: And the only way we're going to get to ubiquity
[00:22:28] SPEAKER_01: is we have to change the computer.
[00:22:30] SPEAKER_01: The current paradigm is good as it is
[00:22:33] SPEAKER_01: and as far as it's taken us is not going to take us to that level.
[00:22:36] I think that's such a great way to say it.
[00:22:38] SPEAKER_00: AI actually can't help us understand each other better,
[00:22:41] SPEAKER_00: help us understand ourselves better,
[00:22:42] SPEAKER_00: understand the natural world better.
[00:22:44] SPEAKER_00: I don't think it's at all what some of the Doomers think
[00:22:47] SPEAKER_00: of replacing human experience.
[00:22:50] SPEAKER_00: That's a short term thing.
[00:22:52] SPEAKER_00: I mean, there will be bumps on the way, right?
[00:22:54] SPEAKER_01: Technology does that.
[00:22:55] SPEAKER_01: That's what happens when you've seen too many sci-fi movies.
[00:22:58] SPEAKER_00: That's right.
[00:22:59] SPEAKER_00: But let's start track.
[00:23:00] SPEAKER_00: Yeah, yeah, totally.
[00:23:02] SPEAKER_00: Totally, it's great.
[00:23:03] SPEAKER_00: This is a really big swing, right?
[00:23:07] SPEAKER_00: Like this is a very ambitious company.
[00:23:09] SPEAKER_00: What gives you confidence that it's going to work
[00:23:12] SPEAKER_00: or has a reasonable shot of working?
[00:23:15] SPEAKER_01: There's a number of data points.
[00:23:16] SPEAKER_01: Of course, like I said, the brains are existence proof.
[00:23:19] SPEAKER_01: But there's also 40 plus years of academic research
[00:23:23] SPEAKER_01: which is showing a lot of promise here.
[00:23:25] SPEAKER_01: People have built different devices.
[00:23:27] SPEAKER_01: I'll be at nine and latest technology
[00:23:30] SPEAKER_01: with professional engineering teams,
[00:23:31] SPEAKER_01: but they have built proofs of concept
[00:23:32] SPEAKER_01: that actually show some of these things work.
[00:23:35] SPEAKER_01: We've also, from a theory standpoint,
[00:23:37] SPEAKER_01: both from neuroscience and just pure
[00:23:40] SPEAKER_01: to amypless systems and math theory,
[00:23:43] SPEAKER_01: do start to understand how these systems can work.
[00:23:45] SPEAKER_01: So I think we now have pieces at different parts
[00:23:48] SPEAKER_01: of the stack that show, hey, if I can combine these things
[00:23:51] SPEAKER_01: the right way, I can build this.
[00:23:53] SPEAKER_01: And that's what great engineering is all about
[00:23:56] SPEAKER_01: is like exploiting this thing that someone else built
[00:24:00] SPEAKER_01: for something else, exploiting that thing.
[00:24:02] SPEAKER_01: And engineers are kind of like the opposite of theories.
[00:24:07] SPEAKER_01: It's like, well, all right, that thing is a quite fit.
[00:24:09] SPEAKER_01: She's standing down and saying, right?
[00:24:11] SPEAKER_01: So it's like, we got to do a little bit of that right now
[00:24:12] SPEAKER_01: and then we can build something and put it all together.
[00:24:14] SPEAKER_01: That's awesome.
[00:24:15] SPEAKER_00: Has anyone called you crazy yet for doing this?
[00:24:18] SPEAKER_00: Oh, yeah, playing at people.
[00:24:19] SPEAKER_00: Is it like everybody?
[00:24:20] SPEAKER_00: Well, I'm used to this at this point.
[00:24:22] SPEAKER_01: My family would call crazy.
[00:24:24] SPEAKER_01: I was called crazy going back to grad school years ago
[00:24:27] SPEAKER_01: and I had a very good career in tech.
[00:24:30] SPEAKER_01: So it's fine.
[00:24:31] SPEAKER_01: I think that's, you need crazy people to go out and explore.
[00:24:34] SPEAKER_01: Maybe think about humanity out of Africa, all that.
[00:24:37] SPEAKER_01: The crazy people went out and we would be lost
[00:24:39] SPEAKER_01: without crazy.
[00:24:40] SPEAKER_01: We need some crazy in there.
[00:24:41] SPEAKER_01: So it's okay. I'm fine with that.
[00:24:43] SPEAKER_01: And so what kind of people are you looking to bring
[00:24:47] SPEAKER_00: on to the team of a very ambitious goal?
[00:24:50] SPEAKER_00: Who should be interested in joining you?
[00:24:52] SPEAKER_00: Yeah, I mean, I think some of the traditional,
[00:24:55] SPEAKER_01: traditional, I say traditional, you know,
[00:24:57] SPEAKER_01: over the last five years, this field of AI systems
[00:25:00] SPEAKER_01: has of all a people who are really good at taking algorithms
[00:25:03] SPEAKER_01: and mapping them very effectively to physical substrates.
[00:25:07] SPEAKER_01: Those folks who understand energy-based models,
[00:25:10] SPEAKER_01: full models, gradient descent in different ways.
[00:25:13] SPEAKER_01: You know, this kind of thing is what we need there.
[00:25:17] SPEAKER_01: We need theorists who can think about different ways
[00:25:21] SPEAKER_01: of building coupled systems, how I can characterize
[00:25:24] SPEAKER_01: the richness of dynamical systems
[00:25:25] SPEAKER_01: and relating that to neural networks.
[00:25:27] SPEAKER_01: So there is a theory aspect of this.
[00:25:30] SPEAKER_01: Then there's folks who are like,
[00:25:31] SPEAKER_01: at the system architecture level, it's like,
[00:25:32] SPEAKER_01: all right, here's what the theory says.
[00:25:34] SPEAKER_01: This is what I can really build.
[00:25:36] SPEAKER_01: How do I bridge that gap?
[00:25:37] SPEAKER_01: And then there's the people actually physically building
[00:25:39] SPEAKER_01: the stuff like analog circuit people,
[00:25:41] SPEAKER_01: actually digital circuit people too.
[00:25:43] SPEAKER_01: We're gonna have a mixed signal here.
[00:25:45] SPEAKER_01: So that's the whole stack.
[00:25:47] SPEAKER_01: The stack is it's hard because these are all things
[00:25:50] SPEAKER_01: that no one's really pushed to that level.
[00:25:53] SPEAKER_01: When we build this chip, our first prototype,
[00:25:55] SPEAKER_01: it's gonna be probably one larger,
[00:25:57] SPEAKER_01: maybe the largest analog chip people have ever built,
[00:26:00] SPEAKER_01: which is kind of weird.
[00:26:01] SPEAKER_01: For something, do something things
[00:26:02] SPEAKER_01: don't usually work the way you think they see.
[00:26:04] SPEAKER_00: You can get in on that Ceribris Jensen game
[00:26:06] SPEAKER_00: where they're each pulling the biggest possible way
[00:26:08] SPEAKER_00: for out of an oven.
[00:26:10] SPEAKER_00: You sound like that.
[00:26:11] SPEAKER_00: Yeah, exactly, right.
[00:26:12] SPEAKER_00: Put a few vacuum tubes on top for effect.
[00:26:15] SPEAKER_00: Yeah, I need blinking lights.
[00:26:16] SPEAKER_00: Yeah, exactly.
[00:26:18] SPEAKER_01: We're not gonna have cool heat sinks.
[00:26:19] SPEAKER_01: It's gonna be super cool.
[00:26:20] SPEAKER_01: It's gonna be cool.
[00:26:21] SPEAKER_01: You don't need biggie, I say that.
[00:26:23] SPEAKER_01: So I hope they make something that looks interesting here.
[00:26:26] SPEAKER_00: This is a funny time for top AI people, right?
[00:26:31] SPEAKER_00: Where you have sort of the option.
[00:26:33] SPEAKER_00: If you wanna start a company,
[00:26:34] SPEAKER_00: there's a lot of venture capitalists
[00:26:35] SPEAKER_00: who probably would fund you.
[00:26:37] SPEAKER_00: If you want to get a cushy job at a big company,
[00:26:39] SPEAKER_00: you can get a very cushy job
[00:26:41] SPEAKER_00: and kind of do some interesting things.
[00:26:44] SPEAKER_00: Or people can join a startup like unconventional
[00:26:47] SPEAKER_00: that has a lot of the nice aspects
[00:26:50] SPEAKER_00: that people look for in sort of AI careers
[00:26:52] SPEAKER_00: and are taking like super sort of big swings.
[00:26:56] SPEAKER_00: I'm just sort of curious, you've been on all sides of this.
[00:26:58] SPEAKER_00: Do you have any advice for younger people
[00:27:01] SPEAKER_00: starting out in their careers
[00:27:02] SPEAKER_00: or how do you think about this?
[00:27:03] SPEAKER_00: I think you get such a breath of working in startup
[00:27:06] SPEAKER_01: that as a beginner in your career,
[00:27:08] SPEAKER_01: that will pay dividends later on.
[00:27:10] SPEAKER_01: Because like I said, the reason I can think across the stack
[00:27:12] SPEAKER_01: is because I did all those things very early in my career.
[00:27:15] SPEAKER_01: I built hardware, I built software, I built applications.
[00:27:18] SPEAKER_01: And in big companies, it's not aimed at fault,
[00:27:22] SPEAKER_01: it's just the way it is.
[00:27:23] SPEAKER_01: Like you get hired to do a thing
[00:27:25] SPEAKER_01: and you do that thing over and over again,
[00:27:27] SPEAKER_01: you're really good at doing that thing.
[00:27:28] SPEAKER_01: And that's fine, you need people
[00:27:30] SPEAKER_01: who are really good at doing specific things.
[00:27:32] SPEAKER_01: But if you want to be prepared for change in the future,
[00:27:37] SPEAKER_01: being really good at one thing
[00:27:38] SPEAKER_01: is probably less valuable and being very good at,
[00:27:41] SPEAKER_01: but slightly good at a lot of things.
[00:27:43] SPEAKER_00: Yeah, that's interesting.
[00:27:44] SPEAKER_00: Is it fair to say unconventional sort of a practical research lab?
[00:27:47] SPEAKER_00: Is that kind of the culture you're going for?
[00:27:48] SPEAKER_00: Absolutely, yeah.
[00:27:49] SPEAKER_01: I mean, first few years, it really is open-ended.
[00:27:51] SPEAKER_01: I don't want to close doors.
[00:27:53] SPEAKER_01: Like I am really specific about this.
[00:27:54] SPEAKER_01: Like I always try to bring the conversation back
[00:27:56] SPEAKER_01: because those people are like,
[00:27:57] SPEAKER_01: oh, that's going to be hard to manufacture.
[00:27:58] SPEAKER_01: They'll say, stop.
[00:28:00] SPEAKER_01: Don't think about that.
[00:28:00] SPEAKER_01: Will it work?
[00:28:02] SPEAKER_01: First come up with existence, proofs.
[00:28:05] SPEAKER_01: Then we go back and try to engineer it
[00:28:06] SPEAKER_01: and all the trade-offs they're in.
[00:28:08] SPEAKER_01: But if you make those trade-offs up upfront,
[00:28:10] SPEAKER_01: you don't go into a good place.
[00:28:12] SPEAKER_01: So yes, we're really thinking wide open,
[00:28:15] SPEAKER_01: but with an eye on the future,
[00:28:16] SPEAKER_01: who we are building a product.
[00:28:18] SPEAKER_01: And to your point, it takes not only people
[00:28:21] SPEAKER_00: to first skill sets, but people with high agency
[00:28:24] SPEAKER_00: to try new things and learn new things
[00:28:26] SPEAKER_00: and integrate across the stack.
[00:28:28] SPEAKER_00: Yeah, I mean, I think what I've done really well
[00:28:31] SPEAKER_01: across the company's eyes, built has been
[00:28:33] SPEAKER_01: going after hard problems,
[00:28:35] SPEAKER_01: which kind of ends itself with smart people
[00:28:37] SPEAKER_01: wanting to come in and try solve them.
[00:28:39] SPEAKER_01: They see a challenge.
[00:28:40] SPEAKER_01: Like here's the amount of risk of climate.
[00:28:42] SPEAKER_01: But then giving them agency,
[00:28:44] SPEAKER_01: and I sort of look at it like,
[00:28:45] SPEAKER_01: what decisions can I make as a leader
[00:28:47] SPEAKER_01: to increase agency of the org overall?
[00:28:50] SPEAKER_01: Like me making top-stown decision,
[00:28:53] SPEAKER_01: maybe a global, globally better for the company
[00:28:56] SPEAKER_01: in the short term.
[00:28:58] SPEAKER_01: But I think wrong term, we will do better
[00:29:01] SPEAKER_01: if more people have agency and can try more things out.
[00:29:03] SPEAKER_01: So personally, I like to find ways to get out of the way
[00:29:06] SPEAKER_01: when I see people who are very passionate
[00:29:08] SPEAKER_01: about trying something.
[00:29:09] SPEAKER_01: He's like, okay, what you really want to do this?
[00:29:12] SPEAKER_01: That makes sense. Go for it.
[00:29:14] SPEAKER_01: And then you own it.
[00:29:14] SPEAKER_01: You own both the good and the bad, right?
[00:29:16] SPEAKER_01: And that's agency to me.
[00:29:17] SPEAKER_01: It's like, you got it.
[00:29:18] SPEAKER_01: You guys are like, okay, I fucked up.
[00:29:19] SPEAKER_01: Now this wasn't real.
[00:29:21] SPEAKER_01: That's okay too.
[00:29:21] SPEAKER_01: But give people the room to do that.
[00:29:24] SPEAKER_00: Anything else you want to say before we wrap up?
[00:29:26] SPEAKER_01: I mean, I think this is like an opportunity
[00:29:28] SPEAKER_01: to do something that is generationally will be felt.
[00:29:34] SPEAKER_01: To me, that's what gets me up in the morning is,
[00:29:38] SPEAKER_01: you know, you can go work on a product
[00:29:39] SPEAKER_01: and make a tweak and people will use it.
[00:29:41] SPEAKER_01: That's great.
[00:29:42] SPEAKER_01: But like in five years, many times people forget those things.
[00:29:45] SPEAKER_01: But if we are successful here,
[00:29:48] SPEAKER_01: the world will not forget this for a very long time.
[00:29:50] SPEAKER_01: Right? This will be written in history books.
[00:29:51] SPEAKER_01: And so I feel like those opportunities are rare.
[00:29:54] So, I'm going to go to the next one.
[00:29:56] I'm going to go to the next one.
[00:29:58] I'm going to go to the next one.
[00:30:00] I'm going to go to the next one.
[00:30:02] I'm going to go to the next one.
[00:30:04] I'm going to go to the next one.
[00:30:06] I'm going to go to the next one.
[00:30:08] I'm going to go to the next one.
[00:30:10] I'm going to go to the next one.
[00:30:12] I'm going to go to the next one.
[00:30:14] I'm going to go to the next one.
[00:30:16] I'm going to go to the next one.
[00:30:18] I'm going to go to the next one.
[00:30:20] I'm going to go to the next one.