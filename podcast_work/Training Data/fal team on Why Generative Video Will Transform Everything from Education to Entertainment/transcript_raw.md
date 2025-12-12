# fal team on Why Generative Video Will Transform Everything from Education to Entertainment

**Podcast:** Training Data
**Date:** 2025-12-10
**Video ID:** s_IIjGamN3Y
**Video URL:** https://www.youtube.com/watch?v=s_IIjGamN3Y

---

[00:00:00] We recently had our first-general media conference
[00:00:03] SPEAKER_03: and Jeffrey Katzenberg former CEO of DreamWorks was there
[00:00:07] SPEAKER_03: and he met a comparison.
[00:00:09] SPEAKER_03: He said, this is exactly playing out how animation.
[00:00:13] SPEAKER_03: When it first came out, people revolted against it.
[00:00:17] SPEAKER_03: It was all hand-drawn before that
[00:00:19] SPEAKER_03: and computer graphics.
[00:00:20] SPEAKER_03: It was new and there was a lot of rebellion
[00:00:24] SPEAKER_03: against computer-driven animation.
[00:00:26] SPEAKER_03: And something very similar is happening with AI right now.
[00:00:29] SPEAKER_03: But there's no way of stopping technology.
[00:00:33] SPEAKER_03: It's just going to happen.
[00:00:34] SPEAKER_03: You're either going to be part of it or not.
[00:00:36] SPEAKER_03: MUSIC
[00:00:53] In this episode, we sit down with a team from Fall,
[00:00:56] SPEAKER_02: the developer platform and infrastructure
[00:00:58] SPEAKER_02: powering generative video at scale.
[00:01:00] Follows a place that developers can go to access more than 600
[00:01:03] SPEAKER_02: generative media models simultaneously
[00:01:05] SPEAKER_02: from OpenAI, Sora, and Google Vio
[00:01:07] SPEAKER_02: to open-weight models like Kling.
[00:01:10] We'll discuss why video models present fundamentally
[00:01:12] SPEAKER_02: different optimization challenges than LLMs,
[00:01:15] SPEAKER_02: why the open source ecosystem for video
[00:01:17] SPEAKER_02: has a thriving long tail in ways that text models never did,
[00:01:20] SPEAKER_02: and why the top video models have a half-life of just 30 days.
[00:01:24] SPEAKER_02: The team also shares insights from the demand
[00:01:26] SPEAKER_02: side of the video model equation.
[00:01:28] SPEAKER_02: We discuss what's happening in the app layer
[00:01:29] SPEAKER_02: from AI native studios to personalized education,
[00:01:32] SPEAKER_02: what's happening in Hollywood, and more.
[00:01:34] SPEAKER_02: Enjoy the show.
[00:01:35] SPEAKER_02: BORCHI GORKUM BATOEN, thank you so much for joining us today.
[00:01:41] I want to start with the problem space
[00:01:42] SPEAKER_02: that you decided to tackle.
[00:01:44] SPEAKER_02: So Fall is a developer API and platform
[00:01:46] SPEAKER_02: for generative video and image models.
[00:01:49] SPEAKER_02: Video is massive, obviously.
[00:01:51] SPEAKER_02: It is more than 80% of the internet span with.
[00:01:54] SPEAKER_02: And it follows that generative video is going to be similarly
[00:01:56] SPEAKER_02: massive, but there's not that many companies
[00:01:58] SPEAKER_02: that are focused on this problem.
[00:02:00] SPEAKER_02: Why do you think that is?
[00:02:01] SPEAKER_02: Yeah, in a way, a generative image and that video
[00:02:04] SPEAKER_03: was an overlooked market in this current phase of AI.
[00:02:10] SPEAKER_03: In my opinion, for two reasons.
[00:02:12] SPEAKER_03: Number one, there wasn't a very clear industry use case
[00:02:18] SPEAKER_03: that people were going after.
[00:02:20] SPEAKER_03: There wasn't vibe coding that automates
[00:02:23] SPEAKER_03: software engineering or there wasn't search,
[00:02:28] SPEAKER_03: which seems a lot of market is going after or customer support,
[00:02:32] SPEAKER_03: anything like that.
[00:02:33] SPEAKER_03: Also number two, the investment on the research side
[00:02:38] SPEAKER_03: wasn't as big three years ago and then that ramped up
[00:02:42] SPEAKER_03: a little bit slower than an alarms,
[00:02:43] SPEAKER_03: but still considerably since then.
[00:02:46] SPEAKER_03: And now the models are much more capable,
[00:02:49] SPEAKER_03: much more useful and real industry use cases,
[00:02:53] SPEAKER_03: compared to what it was three years ago.
[00:02:55] SPEAKER_03: It felt like a toy use case.
[00:02:58] SPEAKER_03: This was just going to be for fun on the side.
[00:03:01] SPEAKER_03: And it's going to be a small market at the end.
[00:03:03] SPEAKER_03: And now we can see that it's going to be a massive market
[00:03:06] SPEAKER_03: with very unique use cases and customers
[00:03:09] SPEAKER_03: compared to the alarm market.
[00:03:11] Like if you actually go back to like,
[00:03:14] SPEAKER_00: as we were experiencing it, I think that was an interesting time.
[00:03:18] SPEAKER_00: We were working on some like Python,
[00:03:22] SPEAKER_00: computing infrastructure and then these models,
[00:03:24] SPEAKER_00: like Delhi two had just come out.
[00:03:26] SPEAKER_00: And then soon after that,
[00:03:28] SPEAKER_00: Chad Chippit had come out and then Lama had come out.
[00:03:31] SPEAKER_00: And we were just like, we were initially,
[00:03:35] SPEAKER_00: we didn't know that image and video market
[00:03:39] SPEAKER_00: was going to get that big.
[00:03:41] SPEAKER_00: We were actually just curious about like running image models
[00:03:45] SPEAKER_00: much faster.
[00:03:46] SPEAKER_00: That was like our initial entry point.
[00:03:48] SPEAKER_00: And then we saw like the initial growth.
[00:03:51] SPEAKER_00: We had a few customers and they were growing really fast.
[00:03:54] SPEAKER_00: We were like, what the heck is going on?
[00:03:56] SPEAKER_00: And then a few customers later,
[00:03:59] SPEAKER_00: we actually thought, hey, we should double down here.
[00:04:02] SPEAKER_00: And around that time, also the other thing that was happening
[00:04:06] SPEAKER_00: was people were over indexed on language models.
[00:04:09] SPEAKER_00: This like story of AGI was being told
[00:04:12] SPEAKER_00: and that attracted all the dollars,
[00:04:14] SPEAKER_00: that attracted all the talent.
[00:04:16] SPEAKER_00: So everyone was just like working on that
[00:04:18] SPEAKER_00: where we thought like we had something niche,
[00:04:21] SPEAKER_00: like growing fast, you know, don't tell anyone.
[00:04:24] SPEAKER_00: And then we just like started focusing on that.
[00:04:27] SPEAKER_00: And soon after like as we got more familiar with the models,
[00:04:31] SPEAKER_00: we thought the, I remember,
[00:04:34] SPEAKER_00: I think we changed our website copy
[00:04:36] SPEAKER_00: to say generative media, generative media platform.
[00:04:39] SPEAKER_00: And then it was only like two or three months after that,
[00:04:42] SPEAKER_00: Sora was announced.
[00:04:44] SPEAKER_00: So we were definitely like ahead.
[00:04:47] SPEAKER_00: But we really saw the whole like future kind of coming
[00:04:50] SPEAKER_00: with like better image models, video models, et cetera.
[00:04:52] SPEAKER_00: So yeah, we made this early bit.
[00:04:55] SPEAKER_00: I mean, you guys have front row seat
[00:04:56] SPEAKER_02: to the sorts of new experiences people are building.
[00:04:59] SPEAKER_02: I think it the market's only going to expand
[00:05:01] SPEAKER_02: from the media market that we know today.
[00:05:03] Yeah, absolutely.
[00:05:03] I think like Al-Quaara Carpati tweet, you know,
[00:05:07] SPEAKER_00: no good podcasts without it.
[00:05:09] SPEAKER_00: He did want to like recently where he was talking about
[00:05:13] SPEAKER_00: like why he's excited about the, you know, media models.
[00:05:16] SPEAKER_00: And one of the things he said was that like he also mentioned
[00:05:18] SPEAKER_00: that right, you know, people are visual.
[00:05:20] SPEAKER_00: And we're gonna, we have more, so much more video
[00:05:22] SPEAKER_00: than text like wall of text.
[00:05:24] SPEAKER_00: And he was saying like, he wasn't making a point
[00:05:28] SPEAKER_00: around like education.
[00:05:30] SPEAKER_00: And a lot of the like content you consume
[00:05:32] SPEAKER_00: just to like like learn things.
[00:05:34] SPEAKER_00: I think right now the model quality is just like,
[00:05:37] SPEAKER_00: like relatively it's just so much like,
[00:05:41] SPEAKER_00: it's so much worse than what it can be,
[00:05:43] SPEAKER_00: where like you could actually like have,
[00:05:45] SPEAKER_00: you know, I do a lot of learning on chat GPT,
[00:05:47] SPEAKER_00: but it's like through text.
[00:05:49] SPEAKER_00: But if it actually rendered a video
[00:05:51] SPEAKER_00: where it could compress like a concept, right,
[00:05:53] SPEAKER_00: instead of you know, 10,000 characters,
[00:05:56] SPEAKER_00: if it could do it in like 15 seconds,
[00:05:59] SPEAKER_00: it'd be so much better.
[00:06:00] SPEAKER_00: I think like there's sort of like the quality bar
[00:06:05] SPEAKER_00: where if like it's gonna go up.
[00:06:07] SPEAKER_00: And if you have, once we have that,
[00:06:09] SPEAKER_00: we're gonna have even more penetration.
[00:06:11] SPEAKER_00: So it's a, it's really a function of the quality right now
[00:06:15] SPEAKER_00: and we're just like in the very early beginnings.
[00:06:17] SPEAKER_00: Totally.
[00:06:18] SPEAKER_03: Education markets almost untouched right now
[00:06:21] SPEAKER_03: with video generation.
[00:06:22] SPEAKER_03: And there's so much potential there.
[00:06:24] SPEAKER_03: And it's just waiting the quality, the predictability
[00:06:26] SPEAKER_03: to get there.
[00:06:27] SPEAKER_03: And I think it's gonna have a lot of potential.
[00:06:30] SPEAKER_03: Totally.
[00:06:31] SPEAKER_02: I mean, you guys sent me that generative video Bible.
[00:06:34] SPEAKER_02: I think it's a much better way to learn some of the lessons
[00:06:37] SPEAKER_02: from the Bible.
[00:06:38] SPEAKER_02: And it's, you know, if you're capturing consumer's attention
[00:06:41] SPEAKER_02: right where they are.
[00:06:42] SPEAKER_02: Exactly.
[00:06:43] SPEAKER_02: I think it's, I agree with you, we're just at the beginning.
[00:06:47] So falls in infrastructure company.
[00:06:49] SPEAKER_02: And so we're gonna structure today's interview.
[00:06:51] SPEAKER_02: I love infrastructure companies
[00:06:52] SPEAKER_02: in terms of the technical layer cake.
[00:06:55] SPEAKER_02: So we're gonna start from the core inference engine,
[00:06:57] SPEAKER_02: compilers, kernels that you built.
[00:06:59] SPEAKER_02: We're gonna go up to the model layer
[00:07:00] SPEAKER_02: and then the workflows and then end with some observations
[00:07:03] SPEAKER_02: on the markets and what people are building.
[00:07:05] SPEAKER_02: Sounds good.
[00:07:06] SPEAKER_03: Sounds exciting.
[00:07:07] SPEAKER_02: Okay, let's do it.
[00:07:08] The inference engine.
[00:07:10] SPEAKER_02: That's one.
[00:07:10] SPEAKER_02: How old are you?
[00:07:13] 22.
[00:07:14] You're 22 years old.
[00:07:15] SPEAKER_02: Okay, say it on your background.
[00:07:16] SPEAKER_02: I think it's super badass and makes complete sense
[00:07:19] SPEAKER_02: why this company is so hardcore.
[00:07:21] SPEAKER_02: I started working on compilers when I was 14.
[00:07:24] SPEAKER_01: So in a way, I have a lot of experience on that.
[00:07:27] SPEAKER_01: You know, it's not just that.
[00:07:29] SPEAKER_01: But like I started working on open source projects.
[00:07:32] SPEAKER_01: So my first contributions were tooling around the Python language.
[00:07:35] SPEAKER_01: And then I started to slowly contribute back to the Python language,
[00:07:39] SPEAKER_01: core compiler, core parser, and core interpreter itself
[00:07:42] SPEAKER_01: and became like one of the core maintainers of it.
[00:07:45] SPEAKER_01: I think at the time I was like the youngest core maintainer
[00:07:48] SPEAKER_01: of the language.
[00:07:49] SPEAKER_01: And this kind of gave me like a unique appreciation
[00:07:51] SPEAKER_01: of compilers and how flexible they are.
[00:07:54] SPEAKER_01: So when we first started like working on
[00:07:57] SPEAKER_01: serving these image models at fault,
[00:07:59] SPEAKER_01: the main idea was, okay, there is like these
[00:08:01] SPEAKER_01: like three different image models,
[00:08:03] SPEAKER_01: three different architectures.
[00:08:05] SPEAKER_01: But this surely gonna explode.
[00:08:07] SPEAKER_01: There's upscalers.
[00:08:08] SPEAKER_01: There's gonna be video models.
[00:08:09] SPEAKER_01: We were predicting that and we didn't want to go optimize
[00:08:12] SPEAKER_01: a single model, put our eggs into a single basket
[00:08:16] SPEAKER_01: and then go became invalidated when the next model comes.
[00:08:19] SPEAKER_01: So we started building this inference engine,
[00:08:21] SPEAKER_01: which is tracing compiler that traces the execution.
[00:08:24] SPEAKER_01: And essentially tries to find common patterns
[00:08:26] SPEAKER_01: that are fitting within the templated kernels that we do.
[00:08:30] SPEAKER_01: So our our bread and butter is like spending.
[00:08:32] SPEAKER_01: We have a 10% performance team
[00:08:34] SPEAKER_01: that's spending all their efforts into writing kernels
[00:08:37] SPEAKER_01: that are like 95% there, but like generalized with templates.
[00:08:40] SPEAKER_01: So we traced the execution of a model
[00:08:42] SPEAKER_01: and find common patterns that could like replace
[00:08:45] SPEAKER_01: these templated semi generic kernels
[00:08:47] SPEAKER_01: to like specialized kernels at runtime
[00:08:49] SPEAKER_01: and optimize the performance of these models.
[00:08:51] SPEAKER_01: And we found this technique to yield like
[00:08:53] SPEAKER_01: pretty much superior results from anything
[00:08:55] SPEAKER_01: that's out there in the market.
[00:08:56] SPEAKER_01: And this led us to claim like number one spot on performance
[00:09:00] SPEAKER_01: on all the benchmarks.
[00:09:01] SPEAKER_01: And another big thing about this is we specialize
[00:09:05] SPEAKER_01: in doing like this sort of kernel level
[00:09:07] SPEAKER_01: mathematically correct sound abstractions
[00:09:10] SPEAKER_01: that led us like you know, maintain the same quality
[00:09:12] SPEAKER_01: of these models, which is a very high bar
[00:09:14] SPEAKER_01: when you're in this media industry
[00:09:15] SPEAKER_01: and when you really care about the output that you're getting.
[00:09:19] SPEAKER_02: What's different between optimizing
[00:09:20] SPEAKER_02: a diffusion model versus another aggressive element?
[00:09:23] SPEAKER_02: In autoregressive elements like your bottleneck
[00:09:25] SPEAKER_01: is half as you can move all those like giant weights
[00:09:28] SPEAKER_01: from memory to S-Crem because you have like a 600 billion
[00:09:31] SPEAKER_01: or a parameter model and you're trying to predict the next
[00:09:34] SPEAKER_01: token you're doing the attention for like all the tokens
[00:09:36] SPEAKER_01: like a couple tokens before that.
[00:09:38] SPEAKER_01: In diffusion models, you're trying to denoise like thousands,
[00:09:42] SPEAKER_01: tens of thousands of tokens for a video
[00:09:43] SPEAKER_01: at the same time doing attention of it.
[00:09:45] SPEAKER_01: So you're essentially saturating all the compute bandwidth
[00:09:48] SPEAKER_01: of these GPUs.
[00:09:50] SPEAKER_01: You're not necessarily bound on memory bandwidth
[00:09:52] SPEAKER_01: but like the computational operations
[00:09:54] SPEAKER_01: that you do are like fully saturated.
[00:09:55] SPEAKER_01: So you're trying to find better ways to execute around the GPU.
[00:09:59] SPEAKER_01: This could be like writing more efficient kernels
[00:10:01] SPEAKER_01: or this could be overlapping of softmax
[00:10:03] SPEAKER_01: with gams that you do.
[00:10:04] SPEAKER_01: Like it's essentially like you're trying to use all of the power
[00:10:08] SPEAKER_01: of the GPU leverage than a way that like you know
[00:10:10] SPEAKER_01: that gets you all the capabilities.
[00:10:12] SPEAKER_01: So it's a different binding constraint
[00:10:13] SPEAKER_02: it's on the compute versus the memory.
[00:10:15] SPEAKER_02: And what's the intuition for why LLMs are relatively memory
[00:10:19] SPEAKER_02: constrained and why video models are by comparison
[00:10:22] SPEAKER_02: relatively compute constrained but not as large
[00:10:24] SPEAKER_02: in terms of just sheer number of parameters?
[00:10:26] SPEAKER_02: I think it's scaling issue right?
[00:10:28] SPEAKER_01: Like in terms of like if you scale these video
[00:10:29] SPEAKER_01: I'm also 600 billion parameters
[00:10:31] SPEAKER_01: with the same dense architecture,
[00:10:32] SPEAKER_01: you're gonna have to do attention with all those full
[00:10:35] SPEAKER_01: like 100 like the say single video is 100,000 tokens.
[00:10:38] SPEAKER_01: And you do this attention step or like you do this
[00:10:41] SPEAKER_01: like denoising step 50 times.
[00:10:43] SPEAKER_01: And every 50 times you do like attention
[00:10:44] SPEAKER_01: over all these like 100,000 tokens.
[00:10:46] SPEAKER_01: It's insanely insanely expensive.
[00:10:48] SPEAKER_01: So I think the constraint there is like just
[00:10:49] SPEAKER_01: how fast you can do the inference.
[00:10:51] SPEAKER_01: And the same applies to LLMs at like larger batch sizes
[00:10:54] SPEAKER_01: but like at like the traffic patterns that people do
[00:10:57] SPEAKER_01: like you know the batch size are not that much.
[00:10:59] SPEAKER_01: And you're mainly constrained by memory bandwidth
[00:11:00] SPEAKER_01: so people do optimizations like speculative decoding
[00:11:03] SPEAKER_01: and other factors to like reduce that a lot.
[00:11:05] SPEAKER_01: Yeah.
[00:11:06] What exactly goes into being at the top of the leaderboard
[00:11:09] SPEAKER_02: in terms of performance?
[00:11:10] SPEAKER_02: Cause I would imagine there's other teams
[00:11:11] SPEAKER_02: that are also very smart people and you know
[00:11:13] SPEAKER_02: this is my Olympics.
[00:11:15] SPEAKER_02: And so what exactly goes into I imagine people
[00:11:18] SPEAKER_02: have like very similar ideas on the techniques
[00:11:20] SPEAKER_02: and different optimizations they can do.
[00:11:22] SPEAKER_02: I don't think anyone cares about it as much as us.
[00:11:25] SPEAKER_01: We are literally obsessed with giants in media.
[00:11:27] SPEAKER_01: We are literally obsessed with these models.
[00:11:29] SPEAKER_01: We have a team that's like just focusing on this.
[00:11:31] SPEAKER_01: Like so far like it seems like
[00:11:33] SPEAKER_01: and from an media to other inference players
[00:11:35] SPEAKER_01: everyone is like super obsessed with language models.
[00:11:37] SPEAKER_01: Everyone is trying to get like one more tokens per second
[00:11:40] SPEAKER_01: on like deep seek benchmarks, whatever.
[00:11:42] SPEAKER_01: And like we are like on a different lane.
[00:11:44] SPEAKER_01: We have like competitors but like no one close to us
[00:11:46] SPEAKER_01: because I think the SM was one of the best teams.
[00:11:48] SPEAKER_01: We found out like the best way to optimize these general
[00:11:51] SPEAKER_01: models and we just focus on this.
[00:11:52] SPEAKER_01: This is like a purely focusing right?
[00:11:54] SPEAKER_01: Like at the end of the day you're constrained by the hardware.
[00:11:56] SPEAKER_01: There's nothing unique about it.
[00:11:58] SPEAKER_01: But like we're just like three months ahead, six months ahead.
[00:12:00] SPEAKER_01: Like when we benchmark torch like the latest version of torch
[00:12:04] SPEAKER_01: again it's like you know our inference engine
[00:12:06] SPEAKER_01: from a year ago we're clearly under performing
[00:12:09] SPEAKER_01: because like torch caught up.
[00:12:10] SPEAKER_01: The same thing is gonna happen with other players.
[00:12:12] SPEAKER_01: You're gonna always like the lead that you can maintain
[00:12:15] SPEAKER_01: is three months, six months ahead at most.
[00:12:17] SPEAKER_01: The thing that matters is just focus.
[00:12:19] SPEAKER_01: If you focus on it, if you purely put all your energy into it
[00:12:21] SPEAKER_01: I think that's like there's it's very hard to get out
[00:12:24] SPEAKER_01: competed by others.
[00:12:25] SPEAKER_01: Because models are slightly changing each month, each release.
[00:12:29] SPEAKER_03: So it's still the same general architecture
[00:12:32] SPEAKER_03: but there are slight differences where we can go in
[00:12:35] SPEAKER_03: and optimize where that's different
[00:12:36] SPEAKER_03: and no one else is paying that much attention to it.
[00:12:39] SPEAKER_03: Also hardware is changing as well.
[00:12:42] SPEAKER_03: So we were able to adapt to be 200s earlier than anyone else
[00:12:46] SPEAKER_03: and we were able to run video models much faster
[00:12:49] SPEAKER_03: basically throughout the year
[00:12:50] SPEAKER_03: because of that obsession with running video models
[00:12:53] SPEAKER_03: with the latest hardware.
[00:12:55] SPEAKER_02: Yeah, got it.
[00:12:56] SPEAKER_02: What are the hardest technical problems
[00:12:58] SPEAKER_02: that you think you're solving?
[00:12:59] SPEAKER_02: So one thing people don't appreciate it as much
[00:13:02] SPEAKER_03: is we are running 600 different models at the same time.
[00:13:06] SPEAKER_03: We have to be running them.
[00:13:07] SPEAKER_03: We have to be so good at running them
[00:13:09] SPEAKER_03: that we should be running a single one of them better than
[00:13:13] SPEAKER_03: as if someone else is running a single model
[00:13:15] SPEAKER_03: because when a foundational lab is running models
[00:13:18] SPEAKER_03: maybe they have a single version of the model
[00:13:20] SPEAKER_03: maybe they have like a couple other different versions
[00:13:23] SPEAKER_03: and that's what all they care about.
[00:13:25] SPEAKER_03: We have to be better than them at running those models
[00:13:28] SPEAKER_03: and we have to be doing all 600 at the same time.
[00:13:31] SPEAKER_03: So on top of the inference optimizations
[00:13:34] SPEAKER_03: that happens in the GPU,
[00:13:36] SPEAKER_03: a lot of optimizations on the infrastructure level needs
[00:13:39] SPEAKER_03: to happen.
[00:13:40] SPEAKER_03: We need to manage the GPU cluster in a way
[00:13:42] SPEAKER_03: that's efficient to load and load these models
[00:13:45] SPEAKER_03: at the right times.
[00:13:46] SPEAKER_03: We need to route traffic to the right GPUs
[00:13:48] SPEAKER_03: who have the warm cache of these models.
[00:13:51] SPEAKER_03: We need to be smart about choosing the right kind of machines
[00:13:54] SPEAKER_03: which kind of chips are running what kind of models
[00:13:57] SPEAKER_03: and the customer traffic is changing all the time
[00:14:01] SPEAKER_03: and we need to adapt towards that.
[00:14:03] SPEAKER_03: So on top of the inference engine,
[00:14:05] SPEAKER_03: the overall infrastructure is also really, really hard
[00:14:08] SPEAKER_03: beast to manage and so far we've done an incredible job at that.
[00:14:12] SPEAKER_03: Would you add anything to the...
[00:14:14] SPEAKER_03: I think that's a pretty fair,
[00:14:16] SPEAKER_01: fair, exponential for what we do.
[00:14:18] SPEAKER_01: Like I call this distributed super-comparing.
[00:14:21] SPEAKER_01: I don't know why people don't like that name, but like...
[00:14:23] SPEAKER_01: I like it.
[00:14:25] SPEAKER_01: But the idea is we are at 28...
[00:14:28] SPEAKER_01: This was a month ago,
[00:14:30] SPEAKER_01: now we are probably at 35 different data centers
[00:14:32] SPEAKER_01: and you have these heterogeneous groups of compute
[00:14:36] SPEAKER_01: that split across with their own different specs,
[00:14:39] SPEAKER_01: different networking, whatever.
[00:14:41] SPEAKER_01: And you're trying to schedule workloads
[00:14:42] SPEAKER_01: as if it's a homogeneous cluster
[00:14:44] SPEAKER_01: that you got from a hyper-schedder.
[00:14:45] SPEAKER_01: It doesn't work like that.
[00:14:46] SPEAKER_01: So if we build, we spend the last three years
[00:14:48] SPEAKER_01: building that traction over it
[00:14:50] SPEAKER_01: from our own orchestrator to building our own CDM.
[00:14:52] SPEAKER_01: Like we go back to like, you know,
[00:14:54] SPEAKER_01: fundamentals of web and we build our own CDM service,
[00:14:57] SPEAKER_01: deploying racks to call us,
[00:14:58] SPEAKER_01: like, you know, just like routing traffic.
[00:15:01] SPEAKER_01: So we build all these technologies
[00:15:02] SPEAKER_01: to essentially make sure that we can tap into capacity
[00:15:04] SPEAKER_01: wherever it is as scheduler workloads,
[00:15:06] SPEAKER_01: which is like very different than like a traditional
[00:15:09] SPEAKER_01: enterprise L and usage pattern, you know.
[00:15:11] SPEAKER_01: Like the use case that we have
[00:15:13] SPEAKER_01: are like so much more spread across, so much more, you know,
[00:15:16] SPEAKER_01: like more consumer facing
[00:15:19] SPEAKER_01: and like when you consider that,
[00:15:20] SPEAKER_01: like there is so much investment going into
[00:15:22] SPEAKER_01: making sure we can tap into the
[00:15:23] SPEAKER_01: like scarce capacity of GPUs.
[00:15:25] SPEAKER_01: Yeah, you mentioned hyperscalers.
[00:15:27] SPEAKER_02: And you know, I hear distributed computers
[00:15:29] SPEAKER_02: and I hear managing giant clusters
[00:15:31] SPEAKER_02: and I naturally think that somewhere where hyperscalers
[00:15:33] SPEAKER_02: should have the incumbent advantage.
[00:15:35] SPEAKER_02: Why do you think that you've been able to
[00:15:37] SPEAKER_02: so far execute them on the core engine?
[00:15:40] I, there's two things about the core unit, right?
[00:15:42] SPEAKER_01: There's the inference part where none of
[00:15:44] SPEAKER_01: hyperscalers have any expertise.
[00:15:46] SPEAKER_01: This is a net new field.
[00:15:48] SPEAKER_01: I think this has been only happening
[00:15:50] SPEAKER_01: for the past three years in front of the news action.
[00:15:51] SPEAKER_01: So it's like a brand new lane that we have been
[00:15:54] SPEAKER_01: outcompeting anyone in our field.
[00:15:55] SPEAKER_01: I think like that's like a pretty much answer of its own.
[00:15:58] SPEAKER_01: And the second one is infrastructure.
[00:16:00] SPEAKER_01: I think right now hyperscalers are very busy
[00:16:03] SPEAKER_01: with their traditional pattern of,
[00:16:06] SPEAKER_01: oh, we have this data center capacity.
[00:16:07] SPEAKER_01: We'll just deploy GPUs and we don't care about the rest.
[00:16:10] SPEAKER_01: This has been changing recently, you know,
[00:16:11] SPEAKER_01: even like Microsoft is going buying from new clots.
[00:16:14] SPEAKER_01: This is like there's like an interesting pattern happening
[00:16:16] SPEAKER_01: because the GPUs and the demand
[00:16:18] SPEAKER_01: and the growth of GPUs doesn't fit to the patterns
[00:16:20] SPEAKER_01: of these hyperscalers, the growth patterns they expect.
[00:16:23] SPEAKER_01: So I think at this age, not even hyperscalers
[00:16:26] SPEAKER_01: have that big of an advantage of scale
[00:16:28] SPEAKER_01: because like they're going buying GPUs from new clots.
[00:16:30] SPEAKER_01: Like the tables have turned a bit.
[00:16:33] SPEAKER_01: Yeah, it almost helps to also be like slightly earlier,
[00:16:37] SPEAKER_00: like in the company journey, right?
[00:16:39] SPEAKER_00: Like if you're a public company, you also have to kind of
[00:16:43] SPEAKER_00: abide by like what the market's expecting of you.
[00:16:47] SPEAKER_00: So like the other thing is that there's a huge price
[00:16:50] SPEAKER_00: discrepancy with hyperscalers and new clouts, right?
[00:16:54] SPEAKER_00: So like it's maybe sometimes 2X, 3X,
[00:16:59] SPEAKER_00: more expensive to use things through hyperscalers.
[00:17:02] SPEAKER_00: What's driving that?
[00:17:05] SPEAKER_00: Well, I think one is like market pressure, right?
[00:17:09] SPEAKER_00: And also like there's added kind of operational expenses
[00:17:14] SPEAKER_00: that hyperscalers have for like having, you know,
[00:17:17] SPEAKER_00: better, they just have a better service, right?
[00:17:19] SPEAKER_00: Better uptime and better SLA's and all of these things add up.
[00:17:22] SPEAKER_00: And then on top of that, there's kind of an established
[00:17:26] SPEAKER_00: like cloud margin, right?
[00:17:27] SPEAKER_00: And you know, the market expects the cloud margin
[00:17:30] SPEAKER_00: to be a certain level.
[00:17:32] SPEAKER_00: Whereas like if you have a three year old NeoCloud,
[00:17:34] SPEAKER_00: you know, you're a private company,
[00:17:37] SPEAKER_00: maybe you don't have as much pressure.
[00:17:39] SPEAKER_00: And there's like assuming infinite demand
[00:17:41] SPEAKER_00: and limited capacity, you can actually, you know,
[00:17:44] SPEAKER_00: hyperscalers can keep their prices high.
[00:17:47] SPEAKER_00: And, you know, they will fill out the capacity
[00:17:50] SPEAKER_00: and also like get slightly better economics,
[00:17:53] SPEAKER_00: whereas like NeoCloud's compete over the whole,
[00:17:56] SPEAKER_00: whole like infinite demand and that pushes the prices down.
[00:18:00] SPEAKER_02: Perfect price competition.
[00:18:02] SPEAKER_02: What does it take to run image versus video models?
[00:18:04] SPEAKER_02: Well, like you guys started the company round,
[00:18:06] SPEAKER_02: a stable, stable fusion moment.
[00:18:08] SPEAKER_02: It was the field was mostly image at the time.
[00:18:10] SPEAKER_02: How does running video models compare to image?
[00:18:12] SPEAKER_02: Let's actually do text image video.
[00:18:15] SPEAKER_03: Okay.
[00:18:16] SPEAKER_03: Even let's compare all three of them.
[00:18:18] SPEAKER_03: And so for, for let's say a SOTA LLM,
[00:18:22] SPEAKER_03: like we don't, let's say deep seek or something like that,
[00:18:25] SPEAKER_03: where we know the numbers,
[00:18:26] SPEAKER_03: running a single prompt like 200 tokens.
[00:18:30] SPEAKER_03: And let's say it takes one X of, of, of Terraflops.
[00:18:35] SPEAKER_03: I think it's tens of Terraflops,
[00:18:36] SPEAKER_03: but let's call that unit one.
[00:18:39] SPEAKER_03: One image is around 100 X of that.
[00:18:43] SPEAKER_03: And if you are doing a five second video, 24 FPS,
[00:18:47] SPEAKER_03: that is around 120 frames.
[00:18:50] SPEAKER_03: So 100 X from one image.
[00:18:52] SPEAKER_03: So you are already 100 X of,
[00:18:58] SPEAKER_03: of 100 X.
[00:18:59] SPEAKER_03: So you are at a thousand X for a standard,
[00:19:04] SPEAKER_03: low standard definition video.
[00:19:06] SPEAKER_03: And if you wanna do 4K, that's another 10 X.
[00:19:10] SPEAKER_03: So 10,000 X compared to a single 200 token LLM input.
[00:19:17] SPEAKER_03: So it is a lot more compute intensive
[00:19:19] SPEAKER_03: in terms of amount of flops you are doing.
[00:19:22] SPEAKER_03: Yeah.
[00:19:23] SPEAKER_01: In, in, in general, like when we started with image,
[00:19:26] SPEAKER_01: the infrastructure was relatively easier to do
[00:19:28] SPEAKER_01: because it's like, it takes three seconds,
[00:19:31] SPEAKER_01: or it took 15 seconds back in the days.
[00:19:33] SPEAKER_01: It takes 15 seconds to generate an image.
[00:19:34] SPEAKER_01: You don't need to necessarily shave like that.
[00:19:36] SPEAKER_01: 50 MS, 100 MS you have overall on the system.
[00:19:39] SPEAKER_01: And then when we went to video,
[00:19:40] SPEAKER_01: it's like even easier because it takes like 20 seconds,
[00:19:42] SPEAKER_01: 30 seconds to generate the video.
[00:19:44] The way that has been happening
[00:19:45] SPEAKER_01: in the past like couple months is real time video,
[00:19:48] SPEAKER_01: where you need to stream 24 FPS videos
[00:19:51] SPEAKER_01: over the, over like a network link from these GPUs.
[00:19:54] SPEAKER_01: That's where we actually spend like some of our time.
[00:19:57] SPEAKER_01: We started this progress with like,
[00:19:59] SPEAKER_01: speech to speech models a year ago.
[00:20:01] SPEAKER_01: We started optimizing them,
[00:20:02] SPEAKER_01: very, very able to like reduce the latency of our system
[00:20:05] SPEAKER_01: with like globally distributed GPU fleet.
[00:20:07] SPEAKER_01: When you send a request,
[00:20:08] SPEAKER_01: we route to the closest GPU,
[00:20:09] SPEAKER_01: minimize our own overhead,
[00:20:11] SPEAKER_01: and then do stuff like, you know,
[00:20:12] SPEAKER_01: we pick the best run or whatever stuff like that.
[00:20:15] SPEAKER_01: So we are now applying those same optimizations with it
[00:20:18] SPEAKER_01: to real time video.
[00:20:19] SPEAKER_01: And we actually see like really good interesting demander
[00:20:22] SPEAKER_01: where people want to experience these stuff like,
[00:20:24] SPEAKER_01: as they type, as they prompt.
[00:20:26] SPEAKER_01: And that's where like some of the infrastructure,
[00:20:27] SPEAKER_01: technical challenges differ from traditionally
[00:20:30] SPEAKER_01: running image and video models
[00:20:31] SPEAKER_01: because image and video are similar as, you know,
[00:20:34] SPEAKER_01: like just more compute excellence.
[00:20:35] SPEAKER_01: So, but like you actually need to care about infrastructure stuff.
[00:20:38] SPEAKER_01: Maybe you go from like less than a second generation time
[00:20:41] SPEAKER_01: for some of these models.
[00:20:43] SPEAKER_00: Yeah.
[00:20:44] SPEAKER_00: Another interesting thing is like image, image models,
[00:20:47] SPEAKER_00: especially you were able to run them on a single GPU.
[00:20:52] SPEAKER_00: Like the parameter counts is actually much smaller.
[00:20:55] SPEAKER_00: So that actually makes it like a little bit easier for us
[00:20:58] SPEAKER_00: as opposed to elements.
[00:20:59] SPEAKER_00: And then with video parameter count is going up.
[00:21:02] SPEAKER_00: Right now I think we're around like for the open source ones,
[00:21:06] SPEAKER_00: I don't know, 30 billion parameter.
[00:21:08] SPEAKER_00: Whereas, you know, we hear rumors about, you know,
[00:21:11] SPEAKER_00: GPT-4 being like in the trillions, GPT-5, maybe more.
[00:21:15] SPEAKER_00: So that's another, that's like, you know,
[00:21:19] SPEAKER_00: on the flip side, it's a little bit easier.
[00:21:22] SPEAKER_00: But it doesn't mean video models are not gonna grow, right?
[00:21:26] SPEAKER_00: There's, you know, rumors around numbers for Vio,
[00:21:29] SPEAKER_00: numbers are out.
[00:21:30] SPEAKER_00: So, so are so like there's also a increase in parameter count.
[00:21:34] SPEAKER_00: So that you're gonna have to kind of, you know,
[00:21:38] SPEAKER_00: use more distributed computing.
[00:21:39] SPEAKER_00: But if you're just, you know, eight nodes,
[00:21:41] SPEAKER_00: that's a, or one node or eight nodes,
[00:21:43] SPEAKER_00: you kind of have a slight advantage.
[00:21:45] SPEAKER_00: Yeah, totally.
[00:21:47] Okay, let's pop one layer of the stack to the models.
[00:21:49] SPEAKER_02: Let's do it.
[00:21:50] SPEAKER_00: So one thing I think people don't fully appreciate
[00:21:52] SPEAKER_02: at the media space and you mentioned this,
[00:21:54] SPEAKER_02: you alluded to this before, is that there are,
[00:21:56] SPEAKER_02: there's a very, very long tail of models
[00:21:58] SPEAKER_02: that are actually used in practice.
[00:22:00] SPEAKER_02: And so it's helping you give people a sense of
[00:22:02] SPEAKER_02: on your platform, how many models are people actively using,
[00:22:05] SPEAKER_02: how's it distributed?
[00:22:06] SPEAKER_02: And like, why do you think there's such a long tail
[00:22:08] SPEAKER_02: of models being used compared to the alarm space?
[00:22:11] This is actually one of the things I would say three years
[00:22:14] SPEAKER_03: ago, people got it wrong.
[00:22:15] SPEAKER_03: I mean, jury's still out, but people right after the chat GPT,
[00:22:20] SPEAKER_03: people start talking about omnimodels.
[00:22:22] SPEAKER_03: There's gonna be these giant models
[00:22:24] SPEAKER_03: that they're gonna be able to generate video, audio,
[00:22:27] SPEAKER_03: image and code text, every type of token.
[00:22:32] SPEAKER_03: This might still happen, I think,
[00:22:34] SPEAKER_03: but it's more clear that you are better off
[00:22:38] SPEAKER_03: if you optimize for a certain type of output.
[00:22:41] SPEAKER_03: Even this is true for code generation,
[00:22:44] SPEAKER_03: definitely true for image or video output.
[00:22:47] SPEAKER_03: So that's one thing when we were pitching three years ago,
[00:22:51] SPEAKER_03: everyone, like, that's one feedback we got,
[00:22:53] SPEAKER_03: or there's gonna be omnimodels and there's gonna be
[00:22:56] SPEAKER_03: a single way of running these.
[00:22:57] SPEAKER_03: It's gonna be hard to create an edge on the modality,
[00:23:03] SPEAKER_03: but turns out it's not true,
[00:23:06] SPEAKER_03: and it actually makes sense to have a technical edge
[00:23:10] SPEAKER_03: on the modality.
[00:23:12] SPEAKER_03: And this is one of the reasons why there's also
[00:23:15] SPEAKER_03: a variety of models because still the best upscaling model
[00:23:18] SPEAKER_03: is just doing upscaling and the best image editing model.
[00:23:22] SPEAKER_03: Even the best text to image model
[00:23:24] SPEAKER_03: is different from the image editing model.
[00:23:25] SPEAKER_03: So all these special tasks require their own model.
[00:23:30] SPEAKER_03: It might be the similar model family or similar architecture,
[00:23:36] SPEAKER_03: but at the end of the day, it has its own weights
[00:23:38] SPEAKER_03: that needs to be deployed independently
[00:23:41] SPEAKER_03: and that creates the variety in the ecosystem.
[00:23:44] I think there's also the,
[00:23:45] SPEAKER_01: this also applies to language models
[00:23:47] SPEAKER_01: where even in the same modality,
[00:23:49] SPEAKER_01: there is different families of models
[00:23:51] SPEAKER_01: with different tastes, different characteristics.
[00:23:53] SPEAKER_01: There's different personas
[00:23:55] SPEAKER_01: and this happens with language models still.
[00:23:56] SPEAKER_01: The code that Cloud writes is very different
[00:23:59] SPEAKER_01: than the code GPT-5 does, right?
[00:24:01] SPEAKER_01: And we see this happening,
[00:24:02] SPEAKER_01: but the good thing about here is there's
[00:24:04] SPEAKER_01: these three four different personas
[00:24:07] SPEAKER_01: on top of different categories upscaling everything,
[00:24:10] SPEAKER_01: video, text-to-video, whatever stuff like that.
[00:24:12] SPEAKER_01: So it gets close to 50 models that are active
[00:24:16] SPEAKER_01: at any point in time,
[00:24:17] SPEAKER_01: and then you have a very long tail of models
[00:24:19] SPEAKER_01: that people still choose
[00:24:21] SPEAKER_01: because they might like the person of that better.
[00:24:23] SPEAKER_01: Yeah, totally.
[00:24:25] SPEAKER_02: Speaking of model personalities,
[00:24:27] SPEAKER_02: whether some of the most popular models on your platform,
[00:24:30] SPEAKER_02: what do you think are the personalities of them?
[00:24:32] SPEAKER_02: So one thing that's been through since the beginning,
[00:24:35] SPEAKER_03: the popular models change all the time.
[00:24:37] SPEAKER_03: So there's always new releases from different labs
[00:24:41] SPEAKER_03: that take over the other
[00:24:43] SPEAKER_03: and it's always a moving target.
[00:24:45] SPEAKER_03: But that being said,
[00:24:46] SPEAKER_03: there's two types of models usually preferred by our customers.
[00:24:51] SPEAKER_03: It's usually there's a one big expensive model
[00:24:54] SPEAKER_03: that has the best quality on video generation.
[00:24:57] SPEAKER_03: This could be VO,
[00:24:59] SPEAKER_03: this could be cling, this could be Sora,
[00:25:02] SPEAKER_03: and then there's usually a workhorse model
[00:25:04] SPEAKER_03: which is cheaper, smaller, but good enough,
[00:25:08] SPEAKER_03: and people usually use that at higher volumes.
[00:25:11] SPEAKER_03: I would say this has been true for the past almost two years
[00:25:14] SPEAKER_03: that there's an expensive high quality model.
[00:25:18] SPEAKER_03: That keeps changing.
[00:25:20] SPEAKER_03: There's a cheaper, good enough model
[00:25:22] SPEAKER_03: that keeps changing,
[00:25:23] SPEAKER_03: but overall, this has been constant.
[00:25:26] SPEAKER_03: And is the workhorse model for prototyping
[00:25:28] SPEAKER_02: and then you run it through the big expensive model
[00:25:30] SPEAKER_02: for the final product?
[00:25:31] SPEAKER_02: Or what do people use the workhorse?
[00:25:33] SPEAKER_02: It's for higher volume use cases
[00:25:36] SPEAKER_03: and depending on the application you are building,
[00:25:39] SPEAKER_03: you might encourage different, like,
[00:25:43] SPEAKER_03: lots of variations of the same output maybe,
[00:25:45] SPEAKER_03: but it's very application-specific, I would say.
[00:25:48] SPEAKER_00: There's also another dimension, I think,
[00:25:50] SPEAKER_00: that's kind of happening in real time right now,
[00:25:52] SPEAKER_00: which is based on the different use case.
[00:25:55] SPEAKER_00: You want to use the model for.
[00:25:57] SPEAKER_00: So when OpenAI released GPT image editing,
[00:26:03] SPEAKER_00: that model had just like superior text generation
[00:26:08] SPEAKER_00: and editing capabilities,
[00:26:09] SPEAKER_00: and for things that require a lot of text,
[00:26:13] SPEAKER_00: people started going and choosing that model
[00:26:17] SPEAKER_00: versus the other models.
[00:26:18] SPEAKER_00: So it also tends to correlate with
[00:26:21] SPEAKER_00: like different capabilities models are bringing
[00:26:24] SPEAKER_00: and also like what they're good at, right?
[00:26:27] SPEAKER_00: So like, Kling, for example,
[00:26:30] SPEAKER_00: people really like it for visual effects types of workflows
[00:26:35] SPEAKER_00: because they had that kind of data in their dataset
[00:26:40] SPEAKER_00: as opposed to some other models.
[00:26:44] SPEAKER_00: For example, C-dance is very good at
[00:26:46] SPEAKER_00: like detailed textures and artistic diversity,
[00:26:50] SPEAKER_00: things like that.
[00:26:51] SPEAKER_00: So it's really a matter of also
[00:26:54] SPEAKER_00: like this sort of use case dimension
[00:26:57] SPEAKER_00: that models excel at.
[00:26:59] SPEAKER_00: An interesting metric that we saw on Q2 and Q3
[00:27:02] SPEAKER_01: was how life of a top five model was 30 days.
[00:27:06] SPEAKER_01: Wow.
[00:27:07] SPEAKER_01: It's very, very interesting to me,
[00:27:08] SPEAKER_01: where these models are continuously shifting
[00:27:11] SPEAKER_01: like the top five of the models
[00:27:13] SPEAKER_01: are continuously shifting.
[00:27:15] Tough depreciation schedule for the model for everybody.
[00:27:18] SPEAKER_02: Hopefully they are building on top of the work
[00:27:20] SPEAKER_03: that they already done.
[00:27:21] SPEAKER_03: So it's, you know,
[00:27:23] SPEAKER_03: additive to the end, but yeah.
[00:27:26] SPEAKER_03: Yeah, I'm teasing.
[00:27:27] SPEAKER_02: And the model probably isn't a more turbulent state
[00:27:30] SPEAKER_02: right now than what the end state will probably be.
[00:27:34] SPEAKER_02: What do you guys think is the most underrated model?
[00:27:36] SPEAKER_02: Like what's your personal favorite?
[00:27:38] SPEAKER_02: I usually like Kling models for video.
[00:27:42] SPEAKER_03: But this kind of has been changing
[00:27:46] SPEAKER_03: because they don't have sound.
[00:27:48] SPEAKER_03: For sound, we have Yo3 and Sora.
[00:27:51] SPEAKER_03: They are the only ones.
[00:27:53] SPEAKER_03: A lot of people are working on it.
[00:27:55] SPEAKER_03: So we'd love to have more variety there as well.
[00:27:58] SPEAKER_03: In which models I like Revs model.
[00:28:00] SPEAKER_01: And like Flux still holds like a very nostalgic,
[00:28:04] SPEAKER_01: even though it's been a year, well, for me,
[00:28:06] SPEAKER_01: you know, like I still go back to Flux.
[00:28:08] SPEAKER_01: There's like variations of Flux models now
[00:28:10] SPEAKER_01: that I like.
[00:28:11] I'll go with mid-journey, which is not on file.
[00:28:14] SPEAKER_00: It's not available on API.
[00:28:17] SPEAKER_00: I just like how they navigated the space.
[00:28:20] SPEAKER_00: I think is very interesting.
[00:28:22] SPEAKER_00: Like they kind of brought this like photorealism,
[00:28:25] SPEAKER_00: which was, you know, that was like a very big deal
[00:28:29] SPEAKER_00: at the time, you know, no model could do it.
[00:28:31] SPEAKER_00: And then now they are more like this artsy model, right?
[00:28:35] SPEAKER_00: Like it's no, photorealism is kind of cracked
[00:28:37] SPEAKER_00: and like no one cares about it.
[00:28:39] SPEAKER_00: So now they have this like niche, very artistic
[00:28:41] SPEAKER_00: like visuals, which is very cool.
[00:28:44] SPEAKER_02: Yeah.
[00:28:44] SPEAKER_02: I'd love to chat about the marketplace dynamics
[00:28:47] SPEAKER_02: a little bit.
[00:28:48] SPEAKER_02: So I understand your business as a little bit
[00:28:49] SPEAKER_02: of a marketplace where you aggregate developers
[00:28:51] SPEAKER_02: on one side of the market, that's the demand side.
[00:28:54] SPEAKER_02: And you aggregate model vendors
[00:28:55] SPEAKER_02: on the other side of the market, that's the supply side.
[00:28:58] SPEAKER_02: And the model vendors are both, you know, proprietary APIs,
[00:29:02] SPEAKER_02: model labs that view you as a distribution partner.
[00:29:05] SPEAKER_02: And then also open models that you host and run yourselves.
[00:29:10] SPEAKER_02: And so maybe talk a little bit about
[00:29:13] SPEAKER_02: for the closed model providers.
[00:29:15] SPEAKER_02: You have partnerships with OpenAI, Sora,
[00:29:17] SPEAKER_02: with DeepMind on Vio.
[00:29:20] SPEAKER_02: What's in it for them?
[00:29:21] SPEAKER_02: Why did they choose to partner with you?
[00:29:23] We were one of the first platforms that accumulated
[00:29:28] SPEAKER_03: the developer love and, you know, following from that,
[00:29:31] SPEAKER_03: these developers work at big companies.
[00:29:33] SPEAKER_03: So they started working with us.
[00:29:36] SPEAKER_03: And we really built the platform for simplicity
[00:29:40] SPEAKER_03: and being able to get going really fast.
[00:29:44] SPEAKER_03: And because the thing Bhatuan mentioned,
[00:29:47] SPEAKER_03: the half-life of these models is really short.
[00:29:52] SPEAKER_03: People usually work with many different models
[00:29:54] SPEAKER_03: at the same time.
[00:29:56] SPEAKER_03: So we were able to claim that we have this big developer base
[00:30:00] SPEAKER_03: that love the platform and not tied into any single model
[00:30:04] SPEAKER_03: and here for the platform.
[00:30:06] SPEAKER_03: And model research labs see this
[00:30:09] SPEAKER_03: and they use the platform for as a distribution channel
[00:30:13] SPEAKER_03: and tap into the developer ecosystem that we built.
[00:30:18] SPEAKER_03: On the other side, this helps us with the next model provider
[00:30:22] SPEAKER_03: because they see all the developers.
[00:30:25] SPEAKER_03: They wanna be on the platform as well,
[00:30:27] SPEAKER_03: which attracts more developers on the platform
[00:30:30] SPEAKER_03: and creates a very nice positive flywheel for us.
[00:30:32] SPEAKER_03: Yeah, very much as a marketplace business.
[00:30:34] SPEAKER_02: And for developers, it's a single choke point
[00:30:36] SPEAKER_02: to be able to access multiple model vendors.
[00:30:39] SPEAKER_02: And see your point on like the model space is changing
[00:30:42] SPEAKER_02: so quickly, I think they really do value that choice.
[00:30:44] SPEAKER_02: Yeah, we call it marketplace plus plus
[00:30:46] SPEAKER_03: because we get to provide infrastructure
[00:30:48] SPEAKER_03: to the research labs as well, also to the developers.
[00:30:52] SPEAKER_03: So there's additional benefits
[00:30:54] SPEAKER_03: that ties into the flywheel effect that we are creating.
[00:30:59] SPEAKER_03: So marketplace plus other services next to it.
[00:31:02] How do you position yourselves to get,
[00:31:04] SPEAKER_02: in some cases, day zero launch access,
[00:31:06] SPEAKER_02: sometimes exclusive launch access to models like
[00:31:10] SPEAKER_02: Kling and Minimax.
[00:31:11] SPEAKER_02: How have you done that?
[00:31:12] Yeah, throughout the last two years,
[00:31:14] SPEAKER_03: you were able to build a very robust marketing machine as well.
[00:31:17] SPEAKER_03: And this is our connection point
[00:31:20] SPEAKER_03: with the developers who are on the platform.
[00:31:22] SPEAKER_03: Every time we release something,
[00:31:24] SPEAKER_03: this creates another opportunity for us to introduce
[00:31:28] SPEAKER_03: a new capability, introduce a new model.
[00:31:30] SPEAKER_03: And model developers also see that
[00:31:33] SPEAKER_03: and we usually do call marketing together
[00:31:36] SPEAKER_03: and part of that call marketing,
[00:31:37] SPEAKER_03: we get exclusive release access for a certain period of time,
[00:31:42] SPEAKER_03: sometimes forever.
[00:31:44] SPEAKER_03: We have a couple competitors that are on the smaller side.
[00:31:49] SPEAKER_03: So model developers want to work with the biggest platform
[00:31:52] SPEAKER_03: out there and increasingly that platform is ours.
[00:31:56] SPEAKER_03: And we get to have these exclusive benefits
[00:31:59] SPEAKER_03: with the model providers.
[00:32:01] That's awesome.
[00:32:02] SPEAKER_02: What do you think it is that the open source model ecosystem
[00:32:04] SPEAKER_02: has been so vibrant for video models?
[00:32:08] SPEAKER_02: It almost feels like the tech models
[00:32:09] SPEAKER_02: are just consistently a generation behind,
[00:32:11] SPEAKER_02: whereas in video,
[00:32:14] SPEAKER_02: there's so much that's happening in the open source realm.
[00:32:17] SPEAKER_02: Video and also image editing as well.
[00:32:20] SPEAKER_03: What do you think that is?
[00:32:21] SPEAKER_03: It started with stability.
[00:32:23] SPEAKER_03: They first open source stable diffusion
[00:32:25] SPEAKER_03: and got insane adoption.
[00:32:27] SPEAKER_03: And almost the same team then started Black Forest Labs
[00:32:31] SPEAKER_03: and they knew the power of open source.
[00:32:34] SPEAKER_03: How it helps them create the ecosystem.
[00:32:37] SPEAKER_03: And with image and medium models,
[00:32:38] SPEAKER_03: the ecosystem actually matters.
[00:32:40] SPEAKER_03: When the developers are training loras,
[00:32:42] SPEAKER_03: they are building adapters,
[00:32:43] SPEAKER_03: they are building on top of your model.
[00:32:45] SPEAKER_03: It really brings free marketing,
[00:32:48] SPEAKER_03: but also creates stickiness.
[00:32:49] SPEAKER_03: So the develop,
[00:32:51] SPEAKER_03: there are still people who are using stable diffusion models
[00:32:54] SPEAKER_03: because they like that ecosystem,
[00:32:56] SPEAKER_03: because it was so open.
[00:32:58] SPEAKER_03: So the Flex team saw this
[00:33:01] SPEAKER_03: from their experience at stability
[00:33:02] SPEAKER_03: and they had a very smart strategy of having
[00:33:05] SPEAKER_03: at least some models that are open source,
[00:33:08] SPEAKER_03: some that are close source.
[00:33:09] SPEAKER_03: And a lot of video model providers that came after
[00:33:13] SPEAKER_03: is following the same playbook
[00:33:16] SPEAKER_03: because you can have a very robust ecosystem.
[00:33:19] SPEAKER_03: It gives you a lot of advantages in terms of marketing,
[00:33:22] SPEAKER_03: in terms of dual upper love.
[00:33:24] SPEAKER_03: And I think it's going to keep going like this.
[00:33:26] SPEAKER_03: Yeah, Thomas.
[00:33:27] SPEAKER_02: I want to add on to that.
[00:33:28] SPEAKER_02: The domain is also very interesting.
[00:33:30] SPEAKER_00: I think in the visual domain,
[00:33:32] SPEAKER_00: ecosystem actually matters more.
[00:33:35] SPEAKER_00: I think when Lambo 2 first came out,
[00:33:38] SPEAKER_00: there was many fine tunes out there.
[00:33:41] SPEAKER_00: But if you actually downloaded it and start using one,
[00:33:44] SPEAKER_00: you can't, I mean,
[00:33:45] SPEAKER_00: You can't tell it's a fine tune.
[00:33:47] SPEAKER_00: You can't tell the difference.
[00:33:49] SPEAKER_00: You can't really, if you're using a,
[00:33:52] SPEAKER_00: I don't know, a control net,
[00:33:54] SPEAKER_00: concept doesn't even exist.
[00:33:55] SPEAKER_00: Language models are a lot more generalized.
[00:34:00] SPEAKER_00: So you can't really understand the difference
[00:34:04] SPEAKER_00: if you were to actually fine tune it.
[00:34:07] SPEAKER_00: So it kind of just ends up being very monolithic.
[00:34:11] SPEAKER_00: As opposed to in the visual realm,
[00:34:13] SPEAKER_00: it's just like any small adjustment you make to the model,
[00:34:18] SPEAKER_00: it can actually have huge implications.
[00:34:23] SPEAKER_00: And so it's just very fertile ground for a lot of customization.
[00:34:31] SPEAKER_00: Yeah.
[00:34:32] SPEAKER_02: Speaking of mid-journey, David Holtz,
[00:34:34] SPEAKER_02: one of his close that I like is curating the aesthetic space with mid-journey.
[00:34:40] SPEAKER_02: Yeah.
[00:34:40] SPEAKER_02: I very much think you just have this combinatorial explosion of styles
[00:34:44] SPEAKER_02: aesthetically.
[00:34:45] SPEAKER_02: And I think that's the reason why it's some of the,
[00:34:48] SPEAKER_02: I think it's all the models on your platform are fine tunes of other models.
[00:34:52] SPEAKER_02: Yes.
[00:34:53] SPEAKER_00: And like the thing is like even if you add a lot of diversity of aesthetics,
[00:34:58] SPEAKER_00: like if you actually train on everything,
[00:35:01] SPEAKER_00: like if you have trained on too many,
[00:35:03] SPEAKER_00: you may not be able to like actually get the exact,
[00:35:06] SPEAKER_00: like like there's so many times you want the exact aesthetics.
[00:35:09] SPEAKER_00: Yeah.
[00:35:10] SPEAKER_00: And then you still, you may still have to like fine tune the model
[00:35:13] SPEAKER_00: to get exactly the output you want.
[00:35:15] SPEAKER_00: Whereas like with L&M's,
[00:35:16] SPEAKER_00: that's not really like how you operate.
[00:35:18] SPEAKER_00: You don't exactly want a particular outcome.
[00:35:20] SPEAKER_00: It's like a different, it's a different problem.
[00:35:23] SPEAKER_00: So this is a lot more, you know,
[00:35:26] SPEAKER_00: it's very subjective.
[00:35:28] SPEAKER_00: So like you kind of have to do these like post-training things on top of the models.
[00:35:32] SPEAKER_00: Sora is another like good example.
[00:35:34] SPEAKER_00: Like Sora too is very fine tuned on like social looking stuff, right?
[00:35:40] SPEAKER_00: And so, you know, you could, you could probably,
[00:35:43] SPEAKER_00: you know, you can have tens of different styles
[00:35:46] SPEAKER_00: and you still want to probably push the model towards that direction
[00:35:50] SPEAKER_00: with post-training.
[00:35:52] Yeah, absolutely.
[00:35:52] It all depends on the use case too.
[00:35:54] SPEAKER_03: Like a customer support chatbot does not need personality.
[00:35:58] SPEAKER_03: Like you want it to be as vanilla as possible.
[00:36:01] SPEAKER_03: But you are talking about filmmakers, marketing teams.
[00:36:05] SPEAKER_03: They all want to add the personality of their style or their brand.
[00:36:10] SPEAKER_03: So they want to have greater control over the outputs.
[00:36:15] SPEAKER_03: Whereas maybe in L&M's, that's not necessarily true all the time.
[00:36:19] SPEAKER_03: If you have an agent, if you are in code generation,
[00:36:21] SPEAKER_03: there's no equivalent of style and personality.
[00:36:24] SPEAKER_03: Yeah.
[00:36:25] SPEAKER_03: Okay, that's a good segue for us to go.
[00:36:27] SPEAKER_02: One more layer of the stack.
[00:36:28] SPEAKER_02: Let's go to workflows.
[00:36:30] SPEAKER_02: What's the, what is the average developer workflow inside fall look like today?
[00:36:35] They are using many different models, first of all.
[00:36:38] SPEAKER_03: Okay.
[00:36:38] SPEAKER_03: So you looked at this up recently.
[00:36:42] SPEAKER_03: Our top 100 customers, they are using 14 different models at the same time.
[00:36:47] SPEAKER_03: These are sometimes chain to each other.
[00:36:49] SPEAKER_03: So one takes the image model, one upscaler, one in which the video model
[00:36:54] SPEAKER_03: all part of a same workflow or like a many more complicated combination of this part of a same workflow
[00:37:02] SPEAKER_03: or different models used in different use cases.
[00:37:05] SPEAKER_03: I think that's the most interesting part, the variety of the models people use on the platform.
[00:37:11] SPEAKER_03: We do have a no code workflow builder as well.
[00:37:15] SPEAKER_03: We built this in collaboration with Shopify.
[00:37:18] SPEAKER_03: And this is usually very good for their PMs, their marketing teams,
[00:37:24] SPEAKER_03: the non-technical members of the team who are playing with these models.
[00:37:29] SPEAKER_03: It's really good for trying different things,
[00:37:32] SPEAKER_03: really good for comparing different models,
[00:37:34] SPEAKER_03: but eventually this makes it into the product as well.
[00:37:37] SPEAKER_03: You can reach to this workflow through an API.
[00:37:40] SPEAKER_03: It's been very popular recently.
[00:37:43] SPEAKER_03: And more and more people in a typical software engineering organization
[00:37:47] SPEAKER_03: is now interested in image and video models.
[00:37:50] SPEAKER_03: So the users of this platform has been increasing.
[00:37:54] SPEAKER_02: Okay, so the average workflow is not just text to prompt.
[00:37:57] SPEAKER_02: Is that not?
[00:37:57] SPEAKER_02: Create a five minute commercial that does it.
[00:37:59] SPEAKER_02: If I wanted to create a five minute commercial, what would the workflow be?
[00:38:03] SPEAKER_02: Yeah, so for this reason, people actually prefer opens,
[00:38:07] SPEAKER_03: like that's one of the reasons why people prefer open source models
[00:38:11] SPEAKER_03: because they get to have more control over the model.
[00:38:15] SPEAKER_03: And they can add things here and there to steer the model towards the outputs they want.
[00:38:20] SPEAKER_03: Yeah.
[00:38:21] SPEAKER_03: When we go talk to studios or more professional marketing teams,
[00:38:27] SPEAKER_03: they all love working with the open source models
[00:38:29] SPEAKER_03: because of the pieces they can replace and control they can add into it.
[00:38:35] SPEAKER_03: And then these workflows are usually like the ones
[00:38:38] SPEAKER_03: if you've seen any like big, confu i workflows with many different nodes.
[00:38:42] SPEAKER_03: It resembles those where each different piece of the model can be replaced
[00:38:47] SPEAKER_03: to create more control for the creator.
[00:38:50] Got it.
[00:38:51] SPEAKER_02: Yeah.
[00:38:51] SPEAKER_02: And I think like what we have like our workflow tool,
[00:38:54] SPEAKER_00: it's not the final form of like there's almost like another layer of abstraction,
[00:39:00] SPEAKER_00: maybe on top in terms of workflow.
[00:39:02] SPEAKER_00: And like as we talked to like these studios,
[00:39:04] SPEAKER_00: we actually figure out like there's so many ways of just like
[00:39:08] SPEAKER_00: there's so many ways of using Photoshop.
[00:39:10] SPEAKER_00: Like there's no single workflow.
[00:39:12] SPEAKER_00: In fact like there's probably like based on your role,
[00:39:17] SPEAKER_00: like you're a marketing person or you're a animator or whatever,
[00:39:21] SPEAKER_00: like you have different workflows, right?
[00:39:23] SPEAKER_00: And so I think that is also emerging.
[00:39:26] SPEAKER_00: Like as more and more like professionals are actually starting to use these tools.
[00:39:30] SPEAKER_00: Like you see the emergence of like very particular workflows, right?
[00:39:35] SPEAKER_00: One of our favorite creators is PJ A's.
[00:39:38] SPEAKER_00: He actually like shares his workflows online.
[00:39:43] SPEAKER_00: And every time like he posts things, you know, every month,
[00:39:47] SPEAKER_00: he actually has like a different kind of workflow.
[00:39:49] SPEAKER_00: It's really driven by like the new models, like based on new model,
[00:39:54] SPEAKER_00: he may have a completely new workflow next time.
[00:39:57] SPEAKER_00: I think I think once like we sort of reach some sort of,
[00:40:01] SPEAKER_00: I guess like some sort of productivity and you know,
[00:40:05] SPEAKER_00: some professionals actually adopting these tools,
[00:40:08] SPEAKER_00: there will probably be more sort of standardized like best practices around
[00:40:13] SPEAKER_00: around using these abstractions.
[00:40:15] SPEAKER_00: But like you know, it's not, I don't think anyone knows like the final, final format.
[00:40:20] SPEAKER_00: And it's like every day we see new things and we try to like update our product
[00:40:25] SPEAKER_00: to make sure like it it caters those people.
[00:40:27] SPEAKER_00: Totally. One of the workflows I'm seeing somewhat commonly is,
[00:40:30] SPEAKER_02: you know, you have an idea for high level what you want and you type that in and then
[00:40:36] SPEAKER_02: and the aesthetics that you want and you iterate on the aesthetics from an image model.
[00:40:39] SPEAKER_02: And then use that image model with the aesthetics you want to then generate a series of images
[00:40:44] SPEAKER_02: which then form the storyboard. So to speak.
[00:40:46] SPEAKER_02: And then it's cat cascades down exactly.
[00:40:49] SPEAKER_03: And then the video model is kind of interpolate in between them.
[00:40:52] SPEAKER_02: And it's funny because that's actually how, you know, that's how, you know,
[00:40:55] SPEAKER_02: Pixar and all these companies work in terms of storyboards.
[00:40:58] SPEAKER_02: And so I think it was a costing in the beginning.
[00:41:01] SPEAKER_00: Yeah.
[00:41:01] SPEAKER_00: Like that's why they had to do it like that.
[00:41:03] SPEAKER_00: But like it actually also makes sense, right?
[00:41:05] SPEAKER_00: Like it makes sense in so many ways to do it, to do it like that.
[00:41:09] SPEAKER_00: And yeah, they call that stuff pre-production and then, you know, post or production.
[00:41:15] SPEAKER_00: Right. So pre-production is all the tooling around storyboarding, etc.
[00:41:19] SPEAKER_00: Like that's not everyone does like even today.
[00:41:22] SPEAKER_00: Even though it was like a very cost-costing.
[00:41:24] SPEAKER_00: Now it's more of a speed thing.
[00:41:27] And AI makes the workflow, you know, very interesting where you have everything laid out.
[00:41:32] SPEAKER_03: And let's say a new model, new text image model comes out.
[00:41:36] SPEAKER_03: They built it in such a way that, okay, you can press a button.
[00:41:40] SPEAKER_03: And now all the different combinations are going to be generated with this other model.
[00:41:44] SPEAKER_03: And then you can like generate all the videos again.
[00:41:47] SPEAKER_03: We've seen those insane workflows.
[00:41:51] SPEAKER_03: You want to update one thing and the whole thing is going to cost like a thousand
[00:41:54] SPEAKER_03: dollars to be run it again.
[00:41:56] SPEAKER_03: But these individuals like they spend a ton of money on,
[00:42:00] SPEAKER_03: on creator platforms.
[00:42:01] SPEAKER_03: I've seen bills like half a million dollars just spent by a single individual.
[00:42:06] SPEAKER_03: And maybe even more when it's in some small production studio stuff like that.
[00:42:11] SPEAKER_03: So it's pretty incredible.
[00:42:14] SPEAKER_03: Totally.
[00:42:15] SPEAKER_02: Wonderful.
[00:42:16] SPEAKER_02: Okay, speaking of studios who are building on your platform.
[00:42:19] SPEAKER_02: Let's go.
[00:42:20] SPEAKER_02: Our final layer of the stack.
[00:42:22] SPEAKER_02: Let's talk about customers and markets and then what the future might hold.
[00:42:27] SPEAKER_02: Maybe what are the coolest things that people are building on your platform today?
[00:42:30] SPEAKER_02: And are they what we would think of as traditional media businesses?
[00:42:33] SPEAKER_02: Or are they net new businesses?
[00:42:36] It's all over the place.
[00:42:37] SPEAKER_00: Like what's so exciting about this space is that it just goes across like all of the,
[00:42:44] SPEAKER_00: you know, markets you can possibly imagine.
[00:42:46] SPEAKER_00: Like I'll give you some more, I guess long tail stuff first because it's super fun and interesting.
[00:42:54] SPEAKER_00: There's a security company that's building on top of all.
[00:42:57] SPEAKER_00: And they basically have these like trainings.
[00:43:00] SPEAKER_00: And the trainings are generated on the fly.
[00:43:03] SPEAKER_00: And the content is all dynamic.
[00:43:05] SPEAKER_00: Obviously they have some scripts I'm guessing to kind of fit like the curriculum.
[00:43:09] SPEAKER_00: But like the content you get, you know, per person is all dynamic.
[00:43:15] SPEAKER_00: This is Brian Long's company.
[00:43:17] SPEAKER_02: Yeah, this is adaptive security.
[00:43:18] SPEAKER_00: Yeah.
[00:43:19] SPEAKER_02: Yeah, they do, they do some really cool stuff.
[00:43:22] SPEAKER_00: I think that's one of the like most unique use cases.
[00:43:26] SPEAKER_00: You can see how that translates into like rest of education.
[00:43:29] SPEAKER_00: I think that market is like kind of picking up.
[00:43:32] SPEAKER_00: Another one, I think like, you know, this is more common use case, I guess, is
[00:43:39] SPEAKER_00: like AI native studios.
[00:43:40] SPEAKER_00: You mentioned like the Bible app.
[00:43:42] SPEAKER_00: Yeah.
[00:43:43] SPEAKER_00: That was one of my favorites.
[00:43:45] SPEAKER_00: It's called Faith.
[00:43:46] SPEAKER_00: It's one of the like highest ranked apps on the app store.
[00:43:50] SPEAKER_00: And yeah, they have like stories for each of the stories from the Bible.
[00:43:54] SPEAKER_00: And they're like really well produced.
[00:43:57] SPEAKER_00: And you know, this is sort of category of AI native studios,
[00:44:02] SPEAKER_00: either in the form of, you know, applications or like they're doing like, you know, feature,
[00:44:09] SPEAKER_00: feature films and, and you know, series and things like that.
[00:44:11] SPEAKER_00: That's a huge category.
[00:44:14] SPEAKER_00: So I would call this like maybe new media or like AI native media and entertainment.
[00:44:20] SPEAKER_00: There is also a lot of like design and productivity, like out of our public customers,
[00:44:27] SPEAKER_00: like canvas, one of those.
[00:44:29] SPEAKER_00: Adobe is one of those.
[00:44:30] SPEAKER_00: So they're integrating kind of like in this, you know, in this older tooling,
[00:44:35] SPEAKER_00: they're integrating new new models.
[00:44:38] SPEAKER_00: Ads is a big one.
[00:44:41] SPEAKER_00: So and ads kind of come in many flavors.
[00:44:45] SPEAKER_00: Basically, there's like the UGC style ads, like the stuff you see, like as a person,
[00:44:50] SPEAKER_00: you know, demoing a product.
[00:44:51] SPEAKER_00: That's like a very big category.
[00:44:53] SPEAKER_00: So AI generate versions of those.
[00:44:55] SPEAKER_00: There's also kind of like older styles of ads, right?
[00:44:59] SPEAKER_00: More professional looking higher, higher production.
[00:45:02] SPEAKER_00: Maybe you saw the Coca-Cola ad that came out recently.
[00:45:05] SPEAKER_00: That's a controversy.
[00:45:06] SPEAKER_00: Yeah, so that's like a kind of a higher production,
[00:45:10] SPEAKER_00: you know, style of ads.
[00:45:13] SPEAKER_00: But you know, what we're excited about is also like programmatic ads, right?
[00:45:17] SPEAKER_00: So where you can do personalized, you know, to the degree of like, like, literally individuals,
[00:45:24] SPEAKER_00: you know, yourself being the ad or in the movies, whatever.
[00:45:26] SPEAKER_00: So like, that's also a big like growing use case.
[00:45:30] SPEAKER_00: Yeah.
[00:45:31] I'm also excited for the education use case.
[00:45:33] SPEAKER_02: I think that, you know, ads is, you know, the backbone of the of commerce and the internet.
[00:45:38] SPEAKER_02: And so like, like super compelling business case.
[00:45:41] SPEAKER_02: But education is a market that's like so important.
[00:45:44] SPEAKER_02: It has never really had that many compelling business cases behind it.
[00:45:48] SPEAKER_02: And part of the challenge with education, I mean, the challenge has been the bottleneck
[00:45:51] SPEAKER_02: to creating high quality content at scale.
[00:45:53] SPEAKER_02: That's actually ideal for the learner.
[00:45:56] SPEAKER_02: And so I'm personally most excited about education.
[00:45:58] SPEAKER_02: Yeah.
[00:45:59] SPEAKER_02: Same.
[00:45:59] SPEAKER_02: Like I really love the education use cases.
[00:46:02] SPEAKER_00: And I actually think that like chat GPT or like just, you know,
[00:46:06] SPEAKER_00: LLM's in general, I think they are already solving it in a way.
[00:46:11] SPEAKER_00: But it's not the right form factor.
[00:46:12] SPEAKER_00: Like if you actually want to fully realize, like the sort of power that these models are bringing,
[00:46:20] SPEAKER_00: you actually need to go into the visual space.
[00:46:22] SPEAKER_00: Because then, you know, it's so much more compact.
[00:46:24] SPEAKER_00: It's more approachable.
[00:46:26] SPEAKER_00: And yeah, I think once we actually crack,
[00:46:29] SPEAKER_00: like visual learning, like sort of these video models,
[00:46:33] SPEAKER_00: that's when it's going to really just like impact people.
[00:46:37] SPEAKER_00: Do you think that the advent of generative media is going to increase the value of existing
[00:46:43] SPEAKER_02: IP?
[00:46:43] SPEAKER_02: So like Mario Brothers, Nintendo, Disney, Pikachu, all these things?
[00:46:48] SPEAKER_02: Or do you think it's going to lead to the democratization of the creation of IP?
[00:46:52] SPEAKER_02: I love this question.
[00:46:53] SPEAKER_02: Because it felt like, I would say six months ago, it felt like
[00:46:58] SPEAKER_03: this was all happening too fast for Hollywood, the IP holders, to adapt and be part of it.
[00:47:05] SPEAKER_03: And from our viewpoint, we thought, all right, these, these INADIV studios,
[00:47:11] SPEAKER_03: they're just going to take over.
[00:47:12] SPEAKER_03: And Hollywood is just going to be too slow.
[00:47:14] SPEAKER_03: And this is just go past them.
[00:47:17] SPEAKER_03: And they're going to be left behind.
[00:47:19] SPEAKER_03: But this summer, something changed.
[00:47:22] SPEAKER_03: And we've been talking to a lot of usual suspects from the Hollywood.
[00:47:26] SPEAKER_03: We recently had our first generative media conference.
[00:47:29] SPEAKER_03: And Jeffrey Katzenberg, former CEO of Dreamworks, was there.
[00:47:34] SPEAKER_03: And he met a comparison.
[00:47:36] SPEAKER_03: He said, this is exactly playing out how animation.
[00:47:40] SPEAKER_03: When it first came out, people revolted against it.
[00:47:43] SPEAKER_03: It was all hand-drawn before that.
[00:47:45] SPEAKER_03: And computer graphics, it was new.
[00:47:48] SPEAKER_03: And there was a lot of rebellion against computer driven animation.
[00:47:54] SPEAKER_03: And something very similar is happening with AI right now.
[00:47:58] SPEAKER_03: But there's no way of stopping technology.
[00:48:01] SPEAKER_03: It's just going to happen.
[00:48:02] SPEAKER_03: You're either going to be part of it or not.
[00:48:05] SPEAKER_03: So we are seeing a lot of existing IP holders are now taking this very seriously.
[00:48:10] SPEAKER_03: And at least for the medium term, I think they are pretty well positioned.
[00:48:14] SPEAKER_03: Because they have the technical people who are actually really interested behind the scenes
[00:48:19] SPEAKER_03: in this technology.
[00:48:21] SPEAKER_03: They also have the IP.
[00:48:22] SPEAKER_03: But they also have storytelling and filmmaking know how.
[00:48:27] SPEAKER_03: You still need quite large budgets.
[00:48:29] SPEAKER_03: Maybe things are going to get cheaper.
[00:48:31] SPEAKER_03: But in the medium term, filmmaking is still going to be expensive.
[00:48:35] SPEAKER_03: Yes, AI is going to make it maybe a little bit cheaper.
[00:48:37] SPEAKER_03: But we need these deeply technical people who know filmmaking,
[00:48:42] SPEAKER_03: who has the IP, who know storytelling to actually in the beginning be part of this.
[00:48:47] SPEAKER_03: And I think they are going to play a big role in the next coming years in the AI ecosystem.
[00:48:53] When there's infinite content generation, it almost puts a value on the things that are finite.
[00:48:58] SPEAKER_02: And I think for those of us who grew up with power rangers or
[00:49:03] SPEAKER_02: new pets or whatever there is, just this nostalgia element and this finite supply of IP that really resonates with us.
[00:49:09] SPEAKER_02: The opposite is true too.
[00:49:10] SPEAKER_03: There's a lot of new, like we had little toys of these Italian men of characters.
[00:49:16] SPEAKER_03: These are characters with no IP.
[00:49:18] SPEAKER_03: No one owns them.
[00:49:19] SPEAKER_03: They are completely AI generated from the internet community.
[00:49:23] SPEAKER_03: And once you have cheap generation of content, very different permutations of it,
[00:49:30] SPEAKER_03: things that people like catch us on and it becomes part of the zeitgeist.
[00:49:36] SPEAKER_03: Totally.
[00:49:37] SPEAKER_03: The opposite, there's signs of opposite nature as well.
[00:49:39] SPEAKER_03: Yeah, both are true.
[00:49:41] SPEAKER_02: How do you relate a question?
[00:49:42] SPEAKER_02: How do we prevent the infinite slop machine state of the world?
[00:49:47] SPEAKER_02: The version where we're just connected to this machine that knows how to personalize stuff for us.
[00:49:51] SPEAKER_02: And we're just hooked up to the infinite slop machine.
[00:49:56] SPEAKER_02: And there's a version where there's human creativity and artistry and things like that involved.
[00:50:02] SPEAKER_02: How do you think the world plays out?
[00:50:04] SPEAKER_02: I think humans eventually converge on all the things that are more meaningful in general.
[00:50:14] SPEAKER_00: I don't know.
[00:50:16] No matter how much slop we feel the world with, I think taste prevails.
[00:50:23] SPEAKER_00: And people are drawn to experiences that are personal and human.
[00:50:29] SPEAKER_00: I just think that that's going to happen.
[00:50:31] SPEAKER_00: One interesting example of this was when meta-announced vibes
[00:50:38] SPEAKER_00: and then open AI and Sora 2.
[00:50:40] SPEAKER_00: The reception was very different.
[00:50:43] SPEAKER_00: And one of the reasons in my mind was vibes was positioned as this
[00:50:49] SPEAKER_00: slop machine kind of thing where they didn't have the product out at the time.
[00:50:59] SPEAKER_00: You have no relation to the characters, etc.
[00:51:02] SPEAKER_00: It was this detached thing.
[00:51:05] SPEAKER_00: Whereas Sora really made it about friends,
[00:51:08] SPEAKER_00: like Cameo and they were very...
[00:51:11] SPEAKER_00: And now you can cameo your pets.
[00:51:12] SPEAKER_00: There you go.
[00:51:14] SPEAKER_00: It's huge.
[00:51:15] SPEAKER_00: So yeah, I think this connection to friends and pets and things like that that actually made.
[00:51:23] SPEAKER_00: And Sora was also like, they were being very personal about it.
[00:51:25] SPEAKER_00: They were very adamant about like, hey, we want to make this about friends.
[00:51:30] SPEAKER_00: We want to make this about these connections as opposed to the infinite slop machine.
[00:51:36] SPEAKER_00: So I think that perception was also a good signal.
[00:51:41] SPEAKER_00: There's ways to make this technology work in a good way.
[00:51:48] Absolutely.
[00:51:49] I'm going to get your perspective on timelines.
[00:51:52] SPEAKER_02: What's feasible today and what's feasible to come?
[00:51:55] SPEAKER_02: I guess, do you think that we'll see Hollywood grade feature film-length films entirely generated
[00:52:03] SPEAKER_02: by AI and if so, on what time?
[00:52:05] SPEAKER_02: What does entire generate by AI means?
[00:52:07] SPEAKER_01: Is it like no human involvement or like...
[00:52:09] SPEAKER_01: No human filming.
[00:52:11] SPEAKER_02: So human involvement.
[00:52:12] SPEAKER_02: Anything is okay.
[00:52:12] SPEAKER_02: Anything.
[00:52:13] SPEAKER_03: Yes, absolutely human editing.
[00:52:15] SPEAKER_02: But no human filming.
[00:52:16] SPEAKER_02: I think less than a year will have like, you know, advanced video models
[00:52:19] SPEAKER_01: with combined with the storyboarding that people have been doing.
[00:52:22] SPEAKER_01: You'll have feature grade short films, like less than 20 minutes.
[00:52:27] SPEAKER_01: I think that's a fair estimation.
[00:52:29] SPEAKER_01: Like even today, I think you can like do really great films.
[00:52:32] SPEAKER_01: It's just like not enough investment of time is going into these.
[00:52:36] SPEAKER_01: But like the enough investment of time and the model quality, I think you'll be there.
[00:52:39] SPEAKER_01: I think we're ready there.
[00:52:40] SPEAKER_02: Okay.
[00:52:41] SPEAKER_02: And you think it's photorealistic.
[00:52:43] SPEAKER_02: You think it's anime.
[00:52:44] SPEAKER_02: You think what categories do you think are more likely to happen sooner?
[00:52:48] I think photorealistic is like what everyone is like targeting.
[00:52:51] SPEAKER_01: But like anime would be a cool one, right?
[00:52:54] SPEAKER_01: Like it's like, you don't see that many anime specialized models.
[00:52:56] SPEAKER_01: Why not?
[00:52:57] SPEAKER_01: I think there needs to be a market for that.
[00:53:01] SPEAKER_01: Clearly.
[00:53:02] I think it's going to be animation or anime or cartoon.
[00:53:06] SPEAKER_03: Like not photorealistic.
[00:53:08] SPEAKER_03: Like as far away from photorealistic as possible, maybe even as fantasy as possible.
[00:53:14] SPEAKER_03: Because filming photorealism is cheap and doable already.
[00:53:19] SPEAKER_03: Like that's not what costs money when people are making movies.
[00:53:23] SPEAKER_03: It's the non-photorealistic stuff that's actually expensive.
[00:53:27] SPEAKER_03: And even if you look at animated movies,
[00:53:31] SPEAKER_03: some of my favorite movies are animated.
[00:53:34] SPEAKER_03: The Toy Story series, how to train your dragon, Shrek, Retotwee.
[00:53:39] SPEAKER_03: And people like these things, not because it reminds them photorealism.
[00:53:45] SPEAKER_03: It's the storytelling that matters.
[00:53:47] SPEAKER_03: And this created a new medium.
[00:53:49] SPEAKER_03: I think AI is going to be similar to animation and how that brought a whole
[00:53:54] SPEAKER_03: different angle to filmmaking.
[00:53:57] SPEAKER_03: I think feature films are hard.
[00:53:59] SPEAKER_00: Because with photorealism,
[00:54:02] SPEAKER_00: like you typically, I mean, people usually like the movies that they're like favorite actors
[00:54:07] SPEAKER_00: are in, whatever actors actresses.
[00:54:09] SPEAKER_00: And that's, you know, so it's like one step removed from.
[00:54:13] SPEAKER_00: That's the thing that costs money to get the actors.
[00:54:15] SPEAKER_03: Yeah, exactly.
[00:54:16] SPEAKER_03: So that's the, you know, we first need to build a connection to this AI,
[00:54:20] SPEAKER_00: you know, AI generated character before we can turn into a film.
[00:54:25] SPEAKER_00: But, but I think like, yeah, I think I think it's
[00:54:29] SPEAKER_00: among like different kinds of content, like shorts, you know,
[00:54:33] SPEAKER_00: I think Italian Brain Rod is an amazing example, right?
[00:54:37] SPEAKER_00: It was first like these characters and then it became a Roblox game.
[00:54:41] SPEAKER_00: And making, I don't even know, like, you know, a lot of revenue.
[00:54:44] SPEAKER_00: So, so yeah, I think I think like AI native stuff is a shorter
[00:54:49] SPEAKER_00: form content is probably going to be very, very big.
[00:54:53] SPEAKER_00: We saw this with VFX where like the VFX effects,
[00:54:56] SPEAKER_01: like one of the most expensive parts of like producing these videos or films is like
[00:55:02] SPEAKER_01: got like AI fight very, very quickly because it's very easy for AI to do like explosions,
[00:55:07] SPEAKER_01: right? Like or a building collapse.
[00:55:08] SPEAKER_01: It's like almost perfect now.
[00:55:10] SPEAKER_01: And I think it's just going to continue along on that dimension.
[00:55:13] SPEAKER_01: Hmm.
[00:55:13] SPEAKER_01: And maybe facial expressions are going to be hard.
[00:55:16] SPEAKER_03: Yes.
[00:55:17] SPEAKER_03: And very hard.
[00:55:18] SPEAKER_03: You don't have to do facial expressions.
[00:55:20] SPEAKER_03: That's going to be okay.
[00:55:21] SPEAKER_03: But now they can do gymnastics.
[00:55:23] SPEAKER_02: Yeah, gymnastics are important.
[00:55:25] SPEAKER_03: Good thing we have a lot of footage of Olympics.
[00:55:30] SPEAKER_02: What about you mentioned Roblox?
[00:55:33] SPEAKER_02: At what point do you think we'll have interactive video games that are generated in real time?
[00:55:37] Yes, I think so.
[00:55:39] SPEAKER_00: I'm very excited about it actually.
[00:55:41] SPEAKER_00: Like I think I think like in one world,
[00:55:44] SPEAKER_00: I think the sort of next reasonable step for text to video.
[00:55:49] SPEAKER_00: Like if you think text to video is the continuation of text to image,
[00:55:53] SPEAKER_00: I would say like a text to game is the continuation of text to video.
[00:55:59] SPEAKER_00: Because you know, with a game, you would, you know, you would essentially making the video interactive.
[00:56:05] SPEAKER_00: Right? That's that's kind of what that means.
[00:56:06] SPEAKER_00: And I actually think that there is a world where there's like hyper,
[00:56:11] SPEAKER_00: you know, hyper casual games exist.
[00:56:14] SPEAKER_00: But this is like another level of hyper casual where it's actually discardable.
[00:56:19] SPEAKER_00: I think I think we're not too far away from that.
[00:56:21] SPEAKER_00: I actually feel like pretty, pretty bullish on having like these, you know,
[00:56:27] SPEAKER_00: one time playable games like very short games.
[00:56:30] SPEAKER_00: Yeah.
[00:56:31] SPEAKER_00: I think that's probably going to happen.
[00:56:33] SPEAKER_00: I think that's a good use case for world models other than many other great use cases.
[00:56:39] SPEAKER_00: But I think it's going to happen.
[00:56:41] Whether at AAA quality games, well, well, these models at least, you know,
[00:56:44] SPEAKER_02: assist and change the development pipeline of those games or.
[00:56:48] SPEAKER_02: Yeah. I think they're already impacting like at least an alarm's are impacting like conversations.
[00:56:53] SPEAKER_00: There's like, you know, dynamic conversations, things like that.
[00:56:56] SPEAKER_00: I think pre-production stuff is impacted already.
[00:57:02] SPEAKER_00: I think like kind of side quests like IP stuff is impacted, right?
[00:57:07] SPEAKER_00: Like where you have the assets and you can make a mini game.
[00:57:10] SPEAKER_00: I think people are using it actually.
[00:57:11] SPEAKER_00: Not very public, but like that is already happening.
[00:57:14] SPEAKER_00: I think like using for AAA production or like generating that with a model that's like,
[00:57:21] SPEAKER_00: I don't know, at least like three, four years ahead for me.
[00:57:25] SPEAKER_00: And yeah, it's, I mean, that would be insane if we can actually do that.
[00:57:30] SPEAKER_00: But, but you know, along the way there, just like the,
[00:57:34] SPEAKER_00: just like the, you know, video space, I think along the way to the AAA,
[00:57:38] SPEAKER_00: there's like many other things.
[00:57:40] SPEAKER_00: I think those are going to be very big.
[00:57:42] SPEAKER_00: Yeah.
[00:57:43] SPEAKER_02: The video model space has just exploded in terms of options, quality, etc.
[00:57:50] As you look ahead towards what's needed to get us to the promised land for everything
[00:57:54] SPEAKER_02: that generative media can be, do you think that there's, you know, future R&D breakthroughs
[00:57:59] SPEAKER_02: that are needed on the horizon, like fundamental R&D breakthroughs?
[00:58:02] SPEAKER_02: Or do you think we're very much in the engineering scale-up
[00:58:05] SPEAKER_02: uh, leg of the race?
[00:58:07] SPEAKER_02: I think the architecture needs to like slightly change, at least like if you think about like
[00:58:11] SPEAKER_01: scaling these models by 10x, 100x, I think the architecture is a big
[00:58:15] SPEAKER_01: bottleneck right now in terms of the inference efficiency where I like the more compression of
[00:58:19] SPEAKER_01: the video space, then that's definitely needed.
[00:58:21] SPEAKER_01: Like we solve this with image, image most used to be like much less compressed.
[00:58:25] SPEAKER_01: And then later like or like you were operating at the pixel space and I'm
[00:58:29] SPEAKER_01: introduced later space and then like even inside that latent space, you took like 64 pixels and
[00:58:33] SPEAKER_01: made them a single pixel. Uh, and now like with video, we are compressing on a time dimension
[00:58:38] SPEAKER_01: where we're seeing like four x ratios. Why not like 24x or whatever? Like you, you need to like
[00:58:43] SPEAKER_01: increase that like compression and like I think that's going to be a big driver of
[00:58:48] SPEAKER_01: improming both inference efficiency as well as training efficient.
[00:58:51] SPEAKER_01: But like I think like any model like I think at this age that we are operating any model you take
[00:58:56] SPEAKER_01: on the generating media side, we're far from being like scaled up engineering-wise. Like I think
[00:59:01] SPEAKER_01: there's not enough investment being put into it or like it just started happening in the within
[00:59:06] SPEAKER_01: the past six months. Like Google showed this with like their models and how quickly they were able to
[00:59:10] SPEAKER_01: catch up. They didn't need to innovate that much. It's just like they have the resources they can
[00:59:14] SPEAKER_01: put more more effort into it. But at the same time smaller labs are able to demonstrate this because
[00:59:20] SPEAKER_01: like there's so much like unique and novel stuff that you can do at the data level to train these
[00:59:24] SPEAKER_01: models. So I think that's also like helping contributing and there's the factor of like outside,
[00:59:29] SPEAKER_01: like you know mid-tier labs that raise like 100 to a billion dollars that's also trying to come
[00:59:34] SPEAKER_01: up with models through listening to open source or like contributing to ecosystem. Yeah.
[00:59:38] SPEAKER_01: That's what's so exciting about this space. There's so much more work to do like so far. The research
[00:59:44] SPEAKER_03: community did the simplest thing possible. They captioned images and trained a model on text
[00:59:50] SPEAKER_03: to prompt. And now like we are doing video image editing that requires a lot more data engineering
[00:59:57] SPEAKER_03: to create the data sets. But luckily seemingly we have a lot of abundant free video data. We are
[01:00:03] SPEAKER_03: going to run out of compute before we run out of video data. So that means there's a lot more work
[01:00:09] SPEAKER_03: to do and a lot more room for improvement. I mean earlier on like GERKAMS math also indicates that
[01:00:15] SPEAKER_00: like if you want to get to 4k video real time that is like I mean that that means like I don't know
[01:00:22] SPEAKER_00: 100x maybe more in compute or architecture. Something has to give to get us there.
[01:00:33] SPEAKER_00: And yeah like right now a lot of models are like not that usable like for professionals especially
[01:00:41] SPEAKER_00: right or even for like consumer right like if you're sitting there like for the best models you
[01:00:47] SPEAKER_00: still have to wait like 40 seconds. I don't know. Sometimes you have to wait two minutes,
[01:00:52] SPEAKER_00: three minutes. Like that's not really acceptable in a world where like we want everything
[01:00:57] SPEAKER_00: on demand. So yeah I think I think something needs to change. And probably pace of like hardware
[01:01:06] SPEAKER_00: getting faster. It's not enough. I think if that's the case you know it'll take much longer.
[01:01:11] SPEAKER_00: It'll have longer timelines. So I think architecture needs to get better.
[01:01:14] SPEAKER_00: Awesome. Thank you guys. You made a very high conviction that on
[01:01:20] SPEAKER_02: Generative Media as a theme I think way before it was obvious. I think we're just at the start
[01:01:26] SPEAKER_02: of I think what's going to be an explosion of Generative Media. And it's been really
[01:01:31] SPEAKER_02: cool to hear about everything you've built from the kernel optimizations and the compiler all the
[01:01:36] SPEAKER_02: way up to the workflows and what you're seeing from customers with new and old media like. And so
[01:01:42] SPEAKER_02: thank you for joining us on the show today. Thank you. Thank you so much. Thanks a lot of fun.