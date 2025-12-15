# Why humans are AGI's biggest bottleneck (and what's coming in 2026) | Alexander Embiricos

**Podcast:** Lenny's
**Date:** 2025-12-14
**Video ID:** z1ISq9Ty4Cg
**Video URL:** https://www.youtube.com/watch?v=z1ISq9Ty4Cg

---

[00:00:00] Do you need work on Codex?
[00:00:01] SPEAKER_01: Codex is Open the Ice Coding Agent.
[00:00:03] SPEAKER_01: We think of Codex as just the beginning
[00:00:05] SPEAKER_01: of a software engineering teammate.
[00:00:06] SPEAKER_01: It's a bit like this really smart intern
[00:00:08] SPEAKER_01: that refuses to read Slack.
[00:00:10] SPEAKER_01: It doesn't check data dog, unless you ask it to.
[00:00:12] SPEAKER_01: I remember Carpote that he tweeted,
[00:00:14] SPEAKER_00: the gnarlyest bugs that he runs into,
[00:00:16] SPEAKER_00: that he just spends hours trying to figure out
[00:00:18] SPEAKER_00: nothing else assault he gives it to Codex.
[00:00:20] SPEAKER_00: Let's run for an hour and it solves it.
[00:00:21] SPEAKER_00: Starting to see glimpses of the future
[00:00:22] SPEAKER_01: where we're actually starting to have Codex
[00:00:24] SPEAKER_01: be on call for its own training.
[00:00:26] SPEAKER_01: Codex writes a lot of the code that helps like manage
[00:00:28] SPEAKER_01: its training run, the key infrastructure.
[00:00:30] SPEAKER_01: And so we have a Codex code review.
[00:00:32] SPEAKER_01: It's like catching a lot of mistakes.
[00:00:33] SPEAKER_01: It's actually caught some like pretty interesting
[00:00:34] SPEAKER_01: configuration mistakes.
[00:00:35] SPEAKER_01: One of the most mind-blowing examples of acceleration
[00:00:38] SPEAKER_01: to Sora and Red Hat, like a fully new app.
[00:00:40] SPEAKER_01: We built it in 18 days and then 10 days later.
[00:00:43] SPEAKER_01: So 28 days total we went to the public.
[00:00:45] SPEAKER_01: How do you think you win in this space?
[00:00:47] SPEAKER_01: One of our major goals with Codex is to get to productivity.
[00:00:50] SPEAKER_01: If we're gonna build a super assistant
[00:00:51] SPEAKER_01: it has to be able to do things.
[00:00:52] SPEAKER_01: One of the learnings over the past year
[00:00:53] SPEAKER_01: is that for models to do stuff
[00:00:55] SPEAKER_01: they are much more effective when they can use a computer.
[00:00:57] SPEAKER_01: It turns out the best way for models to use computers
[00:00:59] SPEAKER_01: is simply to write code.
[00:01:00] SPEAKER_01: And so we're kind of getting to this idea
[00:01:01] SPEAKER_01: where if you want to build any agent
[00:01:03] SPEAKER_01: maybe you should be building a coding agent.
[00:01:04] SPEAKER_01: When you think about progress on Codex
[00:01:07] SPEAKER_01: I imagine you have a bunch of e-vals
[00:01:08] SPEAKER_01: and there's all these public benchmarks.
[00:01:10] SPEAKER_01: A few of us are like constantly on Reddit.
[00:01:12] SPEAKER_01: You know there's praise up there
[00:01:13] SPEAKER_01: and there's a lot of complaints.
[00:01:14] SPEAKER_01: What we can do is we as a product team
[00:01:16] SPEAKER_01: just try to always think about how are we building a tool
[00:01:18] SPEAKER_01: so that it feels like we're maximally accelerating
[00:01:20] SPEAKER_01: people rather than building a tool
[00:01:21] SPEAKER_01: that makes it more unclear what you should do
[00:01:23] SPEAKER_01: is the human.
[00:01:24] SPEAKER_01: Being at OpenAI I can't not ask about
[00:01:26] SPEAKER_01: how far you think we are from AGI.
[00:01:28] SPEAKER_01: I can't under-appreciate limiting factor
[00:01:29] SPEAKER_01: as literally human typing speed
[00:01:31] SPEAKER_01: or human multitasking speed.
[00:01:35] Today my guest is Alexander Embirocos,
[00:01:37] SPEAKER_00: product lead for Codex.
[00:01:39] SPEAKER_00: OpenAI is incredibly popular and powerful coding agent.
[00:01:42] SPEAKER_00: In the words of Nick Turley, head of ChatGbT
[00:01:44] SPEAKER_00: and former podcast guest,
[00:01:46] SPEAKER_00: Alex is one of my all-time favorite humans I've ever worked with
[00:01:49] SPEAKER_00: and bringing him and his company into OpenAI
[00:01:51] SPEAKER_00: ended up being one of the best decisions we've ever made.
[00:01:54] SPEAKER_00: Similarly, Kevin Wheel, OpenAI's CPO
[00:01:57] SPEAKER_00: said Alex is simply the best.
[00:01:59] SPEAKER_00: In our conversation, we chat about what it's truly
[00:02:01] SPEAKER_00: like to build product at OpenAI.
[00:02:03] SPEAKER_00: How Codex allowed the Sora team to ship the Sora app,
[00:02:06] SPEAKER_00: which became the number one app in the app store
[00:02:08] SPEAKER_00: in under one month.
[00:02:09] SPEAKER_00: Also the 20x growth Codex is seeing right now
[00:02:12] SPEAKER_00: and what they did to make it so good at coding.
[00:02:15] SPEAKER_00: Why his team is now focused on making it easier
[00:02:17] SPEAKER_00: to review code, not just write code.
[00:02:19] SPEAKER_00: His AGI timelines, his thoughts on when AIA agents
[00:02:22] SPEAKER_00: will actually be really useful
[00:02:23] SPEAKER_00: and so much more, a huge thank you to Ed Bayes,
[00:02:26] SPEAKER_00: Nick Turley and Dennis Yang for suggesting topics
[00:02:29] SPEAKER_00: for this conversation.
[00:02:30] SPEAKER_00: If you enjoy this podcast, don't forget to subscribe
[00:02:32] SPEAKER_00: and follow it in your favorite podcasting app or YouTube.
[00:02:35] SPEAKER_00: And if you become an annual subscriber of my newsletter,
[00:02:37] SPEAKER_00: you get a year of free of 19 incredible products,
[00:02:41] SPEAKER_00: including a year of free of dev and lovable,
[00:02:43] SPEAKER_00: replant, bolt, NADAM linear superhuman
[00:02:45] SPEAKER_00: de-script, bus-proof, logam, or perplexity,
[00:02:47] SPEAKER_00: warp, granola, magic patterns,
[00:02:48] SPEAKER_00: raycast, type of your D, mob, and post-hog
[00:02:50] SPEAKER_00: and striped atlas.
[00:02:52] SPEAKER_00: Head on over to Lenny's newsletter.com
[00:02:53] SPEAKER_00: and click product pass.
[00:02:55] SPEAKER_00: With that, I bring you Alexander M. Birkos
[00:02:57] SPEAKER_00: after a short word from our sponsors.
[00:03:00] Here's a puzzle for you.
[00:03:01] SPEAKER_00: What do open AI, cursor, perplexity,
[00:03:03] SPEAKER_00: versatile, plat, and hundreds of other
[00:03:06] SPEAKER_00: winning companies have in common?
[00:03:08] SPEAKER_00: The answer is they're all powered by today's sponsor,
[00:03:10] SPEAKER_00: WorkOS.
[00:03:12] SPEAKER_00: If you're building software for enterprises,
[00:03:14] SPEAKER_00: you've probably felt the pain
[00:03:15] SPEAKER_00: of integrating single sign-on,
[00:03:16] SPEAKER_00: skim, R-back, audit logs, and other features
[00:03:20] SPEAKER_00: required by big customers.
[00:03:21] SPEAKER_00: WorkOS turns those deal blockers into drop-in APIs
[00:03:25] SPEAKER_00: with a modern developer platform built specifically
[00:03:27] SPEAKER_00: for B2B SaaS.
[00:03:29] SPEAKER_00: Whether you're a seed-stage startup
[00:03:30] SPEAKER_00: trying to land your first enterprise customer,
[00:03:32] SPEAKER_00: or a unicorn expanding globally,
[00:03:34] SPEAKER_00: WorkOS is the fastest path to becoming enterprise-ready
[00:03:37] SPEAKER_00: and unlocking growth.
[00:03:39] SPEAKER_00: They're essentially striped for enterprise features.
[00:03:42] SPEAKER_00: Visit workos.com to get started
[00:03:44] SPEAKER_00: or just hit up their slack support
[00:03:45] SPEAKER_00: where they have real engineers in there
[00:03:47] SPEAKER_00: who answer your questions super fast.
[00:03:49] SPEAKER_00: WorkOS allows you to build like the best
[00:03:51] SPEAKER_00: with delightful APIs, comprehensive docs,
[00:03:54] SPEAKER_00: and a smooth developer experience.
[00:03:56] SPEAKER_00: Go to workos.com to make your app enterprise-ready today.
[00:04:01] This episode is brought to you by Finn,
[00:04:03] SPEAKER_00: the number one AI agent for customer service.
[00:04:06] SPEAKER_00: If your customer support tickets are piling up,
[00:04:08] SPEAKER_00: then you need Finn.
[00:04:09] SPEAKER_00: Finn is the highest performing AI agent on the market
[00:04:12] SPEAKER_00: with a 65% average resolution rate.
[00:04:15] SPEAKER_00: Finn resolves even the most complex customer queries.
[00:04:18] SPEAKER_00: No other AI agent performs better.
[00:04:20] SPEAKER_00: In head to head bakeoffs with competitors,
[00:04:22] SPEAKER_00: Finn wins every time.
[00:04:23] SPEAKER_00: Yes, switching to a new tool can be scary,
[00:04:26] SPEAKER_00: but Finn works on any help desk with no migration needed,
[00:04:29] SPEAKER_00: which means you don't have to overhaul your current system
[00:04:32] SPEAKER_00: or deal with delays in service for your customers.
[00:04:34] SPEAKER_00: And Finn is trusted by over 6,000 customer service leaders
[00:04:37] SPEAKER_00: and top companies like Anthropic,
[00:04:39] SPEAKER_00: Shutterstock, Synthesia, Clay,
[00:04:41] SPEAKER_00: Vanta, Lovable, Monday.com, and more.
[00:04:43] SPEAKER_00: Because Finn is powered by the Finn AI engine,
[00:04:46] SPEAKER_00: which is a continuously improving system
[00:04:48] SPEAKER_00: that allows you to analyze, train, test, and deploy with ease,
[00:04:51] SPEAKER_00: Finn can continuously improve your results too.
[00:04:54] SPEAKER_00: So if you're ready to transform your customer service
[00:04:56] SPEAKER_00: and scale your support, give Finn a try
[00:04:58] SPEAKER_00: for only 99 cents per resolution,
[00:05:00] SPEAKER_00: plus Finn comes with a 90 day money back guarantee.
[00:05:03] SPEAKER_00: Find out how Finn can work for your team at fiand.ai slash Lenny.
[00:05:07] SPEAKER_00: That's Finn.ai slash Lenny.
[00:05:11] Alexander, thank you so much for being here and welcome
[00:05:16] SPEAKER_00: to the podcast.
[00:05:18] SPEAKER_00: Thank you so much.
[00:05:18] SPEAKER_00: I've been following for ages, and I'm excited to be here.
[00:05:21] SPEAKER_00: I'm even more excited.
[00:05:22] SPEAKER_00: I really appreciate that.
[00:05:24] I'm going to start with your time at OpenAI.
[00:05:27] SPEAKER_00: So you joined OpenAI about a year ago.
[00:05:29] SPEAKER_00: Before that, you had your own startup for about five years.
[00:05:33] SPEAKER_00: Before that, you're a product manager at Dropbox.
[00:05:36] SPEAKER_00: Imagine OpenAI is very different from every other place
[00:05:39] SPEAKER_00: you've worked.
[00:05:40] SPEAKER_00: Let me just ask you this.
[00:05:41] SPEAKER_00: What is most different about how OpenAI operates?
[00:05:45] SPEAKER_00: And what's something that you've learned there
[00:05:46] SPEAKER_00: that you think you're going to take with you wherever
[00:05:48] SPEAKER_00: you go assuming you ever leave?
[00:05:49] SPEAKER_00: By far, I would say the speed and ambition
[00:05:52] SPEAKER_01: of working in OpenAI are just dramatically
[00:05:55] SPEAKER_01: more than what I can imagine.
[00:05:57] SPEAKER_01: And I guess it's kind of an embarrassing thing
[00:05:59] SPEAKER_01: to say because everyone who's a startup founder
[00:06:01] SPEAKER_01: thinks like, oh, yeah, my startup moves super fast.
[00:06:03] SPEAKER_01: And the talent bar is super high and we're super ambitious.
[00:06:05] SPEAKER_01: But I have to say, working in OpenAI
[00:06:08] SPEAKER_01: just made me reimagine what that even means.
[00:06:11] SPEAKER_01: We hear this a lot about, it feels like every AI company
[00:06:14] SPEAKER_00: is just like, oh, my God, I can't believe how fast they're moving.
[00:06:17] SPEAKER_00: Is there an example of just like, wow,
[00:06:18] SPEAKER_00: that wouldn't have happened this quickly anywhere else?
[00:06:20] SPEAKER_00: The most obvious thing that comes to mind
[00:06:21] SPEAKER_01: is just the explosive growth of Codex itself.
[00:06:26] SPEAKER_01: I think it's awesome.
[00:06:26] SPEAKER_01: We bumped our external number.
[00:06:28] SPEAKER_01: But the 10xing of Codex's scale was just super fast
[00:06:33] SPEAKER_01: in a matter of months.
[00:06:34] SPEAKER_01: And it's well more since then.
[00:06:36] SPEAKER_01: And once you've lived through that,
[00:06:38] SPEAKER_01: or at least speaking for myself, having lived through that now,
[00:06:42] SPEAKER_01: I feel like any time I'm going to spend my time
[00:06:45] SPEAKER_01: on building tech product, there's that kind of that speed
[00:06:49] SPEAKER_01: and scale that I now need to meet.
[00:06:52] SPEAKER_01: If I think of what I was doing in my startup,
[00:06:54] SPEAKER_01: it moved way slower.
[00:06:56] SPEAKER_01: And there's always this balance with startups
[00:06:58] SPEAKER_01: of how much do you commit to an idea that you have
[00:07:01] SPEAKER_01: versus find out that it's not working and then pivot.
[00:07:06] SPEAKER_01: But I think one thing I've realized that OpenAI is the amount
[00:07:08] of impact that we can have, and in fact,
[00:07:10] SPEAKER_01: need to have to do a good job is so high
[00:07:12] SPEAKER_01: that it's, I have to be way more ruthless
[00:07:14] SPEAKER_01: without spending my time now.
[00:07:15] SPEAKER_01: Before we get to Codex, is there a way
[00:07:17] SPEAKER_00: that they've structured the org or, I don't know,
[00:07:20] SPEAKER_00: the way that OpenAI operates that allows the team
[00:07:22] SPEAKER_00: to move this quickly?
[00:07:23] SPEAKER_00: Because everyone wants to move super fast.
[00:07:25] SPEAKER_00: Imagine there's a structural approach
[00:07:28] SPEAKER_00: to allowing this to happen.
[00:07:29] SPEAKER_00: I mean, so one thing is just the technology
[00:07:31] SPEAKER_01: that we're building with has just transformed so many things
[00:07:35] SPEAKER_01: from both how we build, but also what kinds of things
[00:07:38] SPEAKER_01: we can enable for users.
[00:07:41] SPEAKER_01: And we spend most of our time talking about
[00:07:44] SPEAKER_01: the improvements in the foundation models,
[00:07:46] SPEAKER_01: but I believe that even if we had no more progress today
[00:07:49] SPEAKER_01: with models, which is absolutely not the case,
[00:07:51] SPEAKER_01: but even if we had no more progress,
[00:07:53] SPEAKER_01: we are way behind on product.
[00:07:55] SPEAKER_01: There's so much more product to build.
[00:07:57] SPEAKER_01: So I think just the moment is ripe, if that makes sense.
[00:08:01] SPEAKER_01: But I think there's a lot of counterintuitive things
[00:08:04] SPEAKER_01: that surprised me when I arrived
[00:08:05] SPEAKER_01: as far as how things are structured.
[00:08:07] One example that comes to mind is when I was working
[00:08:10] SPEAKER_01: on my startup, and before that one I was a Dropbox,
[00:08:12] SPEAKER_01: it was very important, especially as a PM,
[00:08:14] SPEAKER_01: to always rally the ship and make sure you're
[00:08:17] SPEAKER_01: pointed in the right direction, and then you can accelerate
[00:08:19] SPEAKER_01: in that direction.
[00:08:21] But here, I think, because we don't exactly know
[00:08:25] SPEAKER_01: what capabilities will even come up soon,
[00:08:27] SPEAKER_01: and we don't know what's going to work technically.
[00:08:30] SPEAKER_01: And then we also don't know what's going to land,
[00:08:32] SPEAKER_01: even if it works technically.
[00:08:33] SPEAKER_01: It's much more important for us to be very humble
[00:08:37] SPEAKER_01: and learn a lot more empirically and just try things quickly.
[00:08:40] SPEAKER_01: And the org is set up in that way to be incredibly bottomed up.
[00:08:45] SPEAKER_01: This is, again, one of those things,
[00:08:47] SPEAKER_01: as you were saying, everyone wants to move fast.
[00:08:48] SPEAKER_01: I think everyone likes to say that they're bottomed up,
[00:08:50] SPEAKER_01: or at least a lot of people do.
[00:08:52] SPEAKER_01: But OpenAI is truly, truly bottomed up,
[00:08:54] SPEAKER_01: and that's like been a learning experience for me.
[00:08:56] SPEAKER_01: That now, it'll be interesting if I ever work it,
[00:09:01] SPEAKER_01: I don't think it'll ever, it'll even make sense
[00:09:03] SPEAKER_01: to work at a non-AI company in the future.
[00:09:05] SPEAKER_01: I don't even know what that means.
[00:09:06] SPEAKER_01: But if I were to imagine it or go back in time,
[00:09:08] SPEAKER_01: I think I would run things totally.
[00:09:10] SPEAKER_01: What I'm hearing is this ready fire aim
[00:09:14] SPEAKER_00: is the approach more than ready aim fire.
[00:09:17] SPEAKER_00: And this is something, and as you process that,
[00:09:20] SPEAKER_00: because that may not come across well.
[00:09:21] SPEAKER_00: But I actually have heard this a lot of day-eye companies
[00:09:24] SPEAKER_00: because you don't know, and Nick Charlie shared,
[00:09:26] SPEAKER_00: they think the same sentiment.
[00:09:27] SPEAKER_00: Because you don't know how people will use it.
[00:09:29] SPEAKER_00: It doesn't make sense to spend a lot of time
[00:09:31] SPEAKER_00: making it perfect.
[00:09:32] SPEAKER_00: It's better to just get it out there in a primordial way,
[00:09:35] SPEAKER_00: see how people use it, and then go big on that use case.
[00:09:39] SPEAKER_01: Yeah, it's like, okay, to use this analogy a little bit,
[00:09:42] SPEAKER_01: I feel like there is an aim component,
[00:09:44] SPEAKER_01: but the aim component is much fuzzier.
[00:09:46] SPEAKER_01: You know, it's kind of like roughly,
[00:09:47] SPEAKER_01: what do we think can happen?
[00:09:49] SPEAKER_01: Someone, I've learned a ton from working here,
[00:09:52] SPEAKER_01: is a research lead,
[00:09:53] SPEAKER_01: and he likes to say that like, in OpenAI,
[00:09:56] we can have really good conversations
[00:09:58] SPEAKER_01: about something that's like a year plus from now.
[00:10:01] And there's a lot of ambiguity in what will happen,
[00:10:03] SPEAKER_01: but that's a right timeline.
[00:10:05] SPEAKER_01: And then we can have really good conversations
[00:10:06] SPEAKER_01: about what's happening in low months or weeks.
[00:10:10] SPEAKER_01: But there's kind of this awkward middle ground,
[00:10:12] SPEAKER_01: which was like, as you start approaching a year,
[00:10:14] SPEAKER_01: but you're not out of year,
[00:10:15] SPEAKER_01: where it's very difficult to reason about.
[00:10:18] SPEAKER_01: And so as far as aiming, I think we want to know,
[00:10:20] SPEAKER_01: like, okay, what are some of the futures
[00:10:22] SPEAKER_01: that we're trying to build towards,
[00:10:23] SPEAKER_01: and like a lot of the problems we're dealing with in AI,
[00:10:25] SPEAKER_01: like such as alignment or problems,
[00:10:26] SPEAKER_01: you need to be thinking out like, really far out
[00:10:28] SPEAKER_01: into the future.
[00:10:29] SPEAKER_01: So we're kind of aiming fuzzily there,
[00:10:31] SPEAKER_01: but when it comes down to the more tactically,
[00:10:33] SPEAKER_01: like, oh yeah, like what product will we build,
[00:10:35] SPEAKER_01: and therefore how will people use that product?
[00:10:38] SPEAKER_01: That's the place where we're much more like,
[00:10:39] SPEAKER_01: what's find out in parathy.
[00:10:41] That's a good way of putting it.
[00:10:42] SPEAKER_00: Something else that when people hear this,
[00:10:45] SPEAKER_00: they, people sometimes hear companies like yours,
[00:10:48] SPEAKER_00: saying, okay, we're gonna be bottoms up,
[00:10:49] SPEAKER_00: we're gonna drive bunch of stuff,
[00:10:50] SPEAKER_00: we're not gonna have exactly a plan of where
[00:10:52] SPEAKER_00: to go in the next few months.
[00:10:54] SPEAKER_00: The key is you all hire the best people in the world,
[00:10:57] SPEAKER_00: and so that feels like a really key ingredient
[00:10:59] SPEAKER_00: in order to be the successful at bottoms up work.
[00:11:02] SPEAKER_00: Just super rising, basically.
[00:11:05] SPEAKER_01: I was just like, again, surprised or even shocked
[00:11:08] SPEAKER_01: when I arrived at like the level of like individual,
[00:11:10] SPEAKER_01: like drive and like autonomy that everyone here has.
[00:11:15] SPEAKER_01: So I think like the way that opening eye runs, like many,
[00:11:18] SPEAKER_01: you can't like read this or be able to listen
[00:11:21] SPEAKER_01: to a podcast and be like, I am,
[00:11:22] SPEAKER_01: I'm just gonna deploy this to my company.
[00:11:25] SPEAKER_01: Maybe this is a hard thing to say,
[00:11:26] SPEAKER_01: but I think like, yeah, very few companies have the talent
[00:11:28] SPEAKER_01: caliber to be able to do that.
[00:11:30] SPEAKER_01: So it might need to be like adjusted
[00:11:33] SPEAKER_01: if you were gonna implement this.
[00:11:34] SPEAKER_01: Okay, so let's talk codex.
[00:11:36] SPEAKER_00: You lead work on codex.
[00:11:38] SPEAKER_00: How is codex going?
[00:11:39] SPEAKER_00: What number is kidney shares?
[00:11:40] SPEAKER_00: Are anything you can share there?
[00:11:41] SPEAKER_00: Also just, not everyone knows exactly what codex is.
[00:11:43] SPEAKER_00: Explain what codex is.
[00:11:45] Totally, yeah.
[00:11:46] SPEAKER_01: So I had the very lucky job of living in the future
[00:11:49] SPEAKER_01: and leaning front with ton codex.
[00:11:51] SPEAKER_01: And codex is open-air coding agent.
[00:11:54] SPEAKER_01: So super concretely, that means it's an IDE extension,
[00:11:58] SPEAKER_01: the VS code extension, that you can install
[00:12:01] SPEAKER_01: or a terminal tool that you can install.
[00:12:02] SPEAKER_01: And when you do so, you can then basically pair with codex
[00:12:06] SPEAKER_01: to answer questions about code, write code,
[00:12:09] SPEAKER_01: run tasks, execute code,
[00:12:10] SPEAKER_01: and do a bunch of the work in sort of that like thick,
[00:12:13] SPEAKER_01: middle section of the software development life cycle,
[00:12:16] SPEAKER_01: which is all about writing code
[00:12:18] SPEAKER_01: that you're gonna get into production.
[00:12:21] SPEAKER_01: More broadly, we think of codex as like,
[00:12:24] SPEAKER_01: it's what it kindly is, is just the beginning
[00:12:26] SPEAKER_01: of a software engineering teammate.
[00:12:29] SPEAKER_01: And so, when you use a big word like teammate,
[00:12:31] SPEAKER_01: like some of the things we're imagining are that,
[00:12:33] SPEAKER_01: it's not only able to write code,
[00:12:36] SPEAKER_01: but actually it participates like early on
[00:12:38] SPEAKER_01: and like the ideation and planning phases
[00:12:40] SPEAKER_01: of writing software and then further downstream
[00:12:42] SPEAKER_01: in terms of like validation, deploying,
[00:12:44] SPEAKER_01: and like maintaining code.
[00:12:46] To make that a little more fun,
[00:12:47] SPEAKER_01: like one thing I like to imagine is like,
[00:12:49] SPEAKER_01: if you think of what codex is today,
[00:12:50] SPEAKER_01: it's a bit like this like really smart intern
[00:12:52] SPEAKER_01: that like refuses to read Slack
[00:12:55] SPEAKER_01: and like doesn't check data dog or like century
[00:12:57] SPEAKER_01: unless you ask it to.
[00:12:59] SPEAKER_01: And so like no matter how smart it is,
[00:13:00] SPEAKER_01: like how much you're gonna trust it to write code
[00:13:02] SPEAKER_01: without you also working with it, right?
[00:13:03] SPEAKER_01: So that's how people use it mostly today is they pair with it.
[00:13:06] SPEAKER_01: But we wanna get to the point where, you know,
[00:13:08] SPEAKER_01: it can work like just like a new intern that you hire,
[00:13:11] SPEAKER_01: you don't only ask them to write code,
[00:13:13] SPEAKER_01: but you ask them to participate across the cycle.
[00:13:15] SPEAKER_01: And so you know that like, even if they don't get something
[00:13:17] SPEAKER_01: right the first try, they're eventually gonna be able
[00:13:18] SPEAKER_01: to iterate their way there.
[00:13:20] SPEAKER_01: I thought the point about not reading Slack
[00:13:22] SPEAKER_00: and did dog was it's just not distracted,
[00:13:24] SPEAKER_00: it's just constantly focused and it's always in flow.
[00:13:27] SPEAKER_00: But I get what you're saying there
[00:13:28] SPEAKER_00: is it doesn't have all the context on everything that's good on.
[00:13:31] SPEAKER_00: And like that's not only true when it's performing a task,
[00:13:33] SPEAKER_01: but again, if you think of like the best team in teammates,
[00:13:35] SPEAKER_01: like you don't tell them what to do, right?
[00:13:38] SPEAKER_01: Like maybe when you first hire them,
[00:13:39] SPEAKER_01: you have a couple meetings and you're like,
[00:13:41] SPEAKER_01: hey, like you kind of learn like, okay,
[00:13:43] SPEAKER_01: this is, these prompts work for this team,
[00:13:45] SPEAKER_01: these prompts don't, right?
[00:13:46] SPEAKER_01: This is how to communicate with this person.
[00:13:47] SPEAKER_01: The eventually you give them some starter tasks,
[00:13:49] SPEAKER_01: you delegate if you task.
[00:13:50] SPEAKER_01: But the eventually you just say like,
[00:13:51] SPEAKER_01: hey, great, okay, you're working with this set of people
[00:13:54] SPEAKER_01: in this area of the code base.
[00:13:56] SPEAKER_01: You know, feel free to work with other people
[00:13:57] SPEAKER_01: and other parts of the code base too, even.
[00:13:59] SPEAKER_01: And yeah, you tell me what you think makes sense to be done,
[00:14:02] right?
[00:14:03] SPEAKER_01: And so, you know, we think of this as like proactivity
[00:14:04] SPEAKER_01: in like one of our major goals with code access
[00:14:06] SPEAKER_01: to like get to proactivity.
[00:14:09] I think this is, this is like critically important
[00:14:13] SPEAKER_01: to like achieve the mission of opening.
[00:14:14] SPEAKER_01: I would just to deliver the benefits of AI to all humanity.
[00:14:17] SPEAKER_01: You know, I like to joke today that like AI products,
[00:14:19] SPEAKER_01: and it's a half joke.
[00:14:20] SPEAKER_01: They're actually like really hard to use
[00:14:23] because you have to like be very thoughtful
[00:14:25] SPEAKER_01: about when it could help you.
[00:14:28] SPEAKER_01: And if you're not prompting a model to help you,
[00:14:30] SPEAKER_01: it's probably not helping you at that time.
[00:14:33] SPEAKER_01: And if you think of how many times like the average user
[00:14:35] SPEAKER_01: is prompting the AI today, it's probably like tens of times.
[00:14:38] SPEAKER_01: But if you think of how many times people could actually get
[00:14:40] SPEAKER_01: benefit from a really intelligent entity,
[00:14:43] SPEAKER_01: it's thousands of times per day.
[00:14:45] SPEAKER_01: And so a lot, a large part of our goal with code access
[00:14:47] SPEAKER_01: to figure out like what is the shape of an actual teammate agent
[00:14:51] SPEAKER_01: that is sort of helpful by default?
[00:14:53] SPEAKER_01: When people think about cursor and even cloud code,
[00:14:57] SPEAKER_00: it's like a IDE that helps you code
[00:14:59] SPEAKER_00: and kind of autocomplete code
[00:15:00] SPEAKER_00: and maybe does that make it work.
[00:15:02] SPEAKER_00: But I'm hearing here is the vision is different,
[00:15:05] SPEAKER_00: which is it's a teammate.
[00:15:06] SPEAKER_00: It's like a remote teammate building code for you
[00:15:09] SPEAKER_00: that you talk to and ask to do things.
[00:15:11] SPEAKER_00: And it also does an IDE autocomplete and things like that.
[00:15:15] SPEAKER_00: Is that kind of a differentiator
[00:15:16] SPEAKER_00: in the way you think about codecs?
[00:15:18] SPEAKER_00: It's basically this idea that like we want the way,
[00:15:22] SPEAKER_01: like if you're a developer and you're trying to get something
[00:15:24] SPEAKER_01: gone, we want you to just feel like you have superpowers
[00:15:26] SPEAKER_01: and you're able to move much, much faster.
[00:15:28] SPEAKER_01: But we don't think that in order for you
[00:15:31] SPEAKER_01: to reap those benefits, you need to be sitting there
[00:15:34] SPEAKER_01: constantly thinking about like how can I invoke AI
[00:15:36] SPEAKER_01: at this point to do this thing?
[00:15:38] SPEAKER_01: We want you to be able to sort of like plug it in
[00:15:40] SPEAKER_01: to the way that you work and have it just start to do stuff
[00:15:42] SPEAKER_01: without you having to think about it.
[00:15:43] SPEAKER_01: We'll go.
[00:15:44] SPEAKER_00: Just as long as lines, but just how's it going?
[00:15:46] SPEAKER_00: Is there any stats any numbers you can share
[00:15:48] SPEAKER_00: about how codecs is doing?
[00:15:49] SPEAKER_00: Yeah, it's been codecs you've been growing
[00:15:50] SPEAKER_01: like absolutely explosively since the launch of GPT-5
[00:15:54] SPEAKER_01: back in August.
[00:15:55] SPEAKER_01: There's some definitely some interesting product insights
[00:15:57] SPEAKER_01: to talk about as to like how we unlock that growth
[00:15:59] SPEAKER_01: if you're interested.
[00:16:00] SPEAKER_01: But you know, the last that we showed there was like,
[00:16:03] SPEAKER_01: we were like well over 10x since August.
[00:16:06] SPEAKER_01: In fact, it's been like 20x since then.
[00:16:09] SPEAKER_01: Also, the codecs models are serving many
[00:16:11] SPEAKER_01: trillions of tokens a week now.
[00:16:14] SPEAKER_01: And it's basically like our most served coding model.
[00:16:17] SPEAKER_01: One of the really cool things that we've seen
[00:16:18] SPEAKER_01: is that the way that we decided to set up the codecs team
[00:16:22] SPEAKER_01: was to build a really tightly integrated product
[00:16:25] and research team that are iterating on the model
[00:16:28] SPEAKER_01: and the harness together.
[00:16:29] And it turns out that lets you just do a lot more
[00:16:31] SPEAKER_01: and try many more experiments as to how these things
[00:16:33] SPEAKER_01: will work together.
[00:16:35] SPEAKER_01: And so we were just training these models for use
[00:16:38] SPEAKER_01: in our first party harness that we were very opinionated
[00:16:40] SPEAKER_01: about.
[00:16:42] And then what we've started to see more recently
[00:16:44] SPEAKER_01: actually is that other major sort of API coding customers
[00:16:47] SPEAKER_01: are now starting to adopt these models as well.
[00:16:50] And so we've reached the point where actually the codecs model
[00:16:52] SPEAKER_01: is the most served coding model in the API as well.
[00:16:55] SPEAKER_01: You hinted at this what unlocked this growth.
[00:16:59] SPEAKER_00: I am extremely interested in hearing that.
[00:17:01] SPEAKER_00: It felt like before, I don't know,
[00:17:03] SPEAKER_00: maybe this was before you joined the team.
[00:17:05] SPEAKER_00: It just felt like Cloud Code was killing it.
[00:17:06] SPEAKER_00: Just everyone was sitting on top of Cloud Code.
[00:17:09] SPEAKER_00: It was by far the best way to code.
[00:17:11] SPEAKER_00: And then all of a sudden, Codex comes around.
[00:17:13] SPEAKER_00: I remember Carpati tweeted that he just
[00:17:16] SPEAKER_00: has never seen a model like this.
[00:17:18] SPEAKER_00: I think the tweet was the gnarlyest bugs that he runs into
[00:17:21] SPEAKER_00: that he just spends hours trying to figure out
[00:17:23] SPEAKER_00: nothing else has solved.
[00:17:25] SPEAKER_00: He gives it to Codex, lets it run for an hour
[00:17:27] SPEAKER_00: and it solves it.
[00:17:28] What did you guys do?
[00:17:30] SPEAKER_01: We have this strong sort of mission here at OpenAI
[00:17:33] SPEAKER_01: to basically to build the API.
[00:17:36] SPEAKER_01: And so we think a lot about how can we shape a product
[00:17:40] SPEAKER_01: so that it can scale.
[00:17:43] SPEAKER_01: Earlier I was mentioning like, hey, if you're an engineer,
[00:17:45] SPEAKER_01: you should be getting help from AI thousands of times
[00:17:47] SPEAKER_01: per day.
[00:17:48] SPEAKER_01: And so we thought a lot about the primitives for that
[00:17:51] SPEAKER_01: when we launched our first version of Codex, which
[00:17:54] SPEAKER_01: was Codex Cloud.
[00:17:56] And that was basically a product that had its own computer.
[00:17:58] SPEAKER_01: It lives in the Cloud.
[00:17:59] SPEAKER_01: You can delegate to it.
[00:18:00] SPEAKER_01: And the coolest part about that was you could run
[00:18:03] SPEAKER_01: many, many tasks in parallel.
[00:18:05] SPEAKER_01: But some of the challenges that we saw are that it's
[00:18:09] SPEAKER_01: a little bit harder to set that up, both in terms of environment
[00:18:13] SPEAKER_01: configuration, like giving the model the tools it needs
[00:18:16] SPEAKER_01: to about its changes and to learn how to prompt them that way.
[00:18:19] SPEAKER_01: And sort of my analogy for this is going back
[00:18:21] SPEAKER_01: to this teammate analogy.
[00:18:22] SPEAKER_01: It's like if you hire a teammate, but you're never
[00:18:25] SPEAKER_01: allowed to get on a call with them.
[00:18:27] SPEAKER_01: And you can only go back and forth asynchronously over time.
[00:18:30] Like that works for some teammates.
[00:18:32] SPEAKER_01: And eventually that's actually how you want to spend most
[00:18:34] SPEAKER_01: of your time.
[00:18:36] SPEAKER_01: But it's hard to initially adopt.
[00:18:39] SPEAKER_01: So we still have that vision of like that's
[00:18:41] SPEAKER_01: what we're trying to get you to a teammate that you delegate to
[00:18:43] SPEAKER_01: and then is proactive.
[00:18:44] SPEAKER_01: And we're seeing that growing.
[00:18:45] SPEAKER_01: But the key unlock is actually first you
[00:18:48] SPEAKER_01: need to land with users in a way that's
[00:18:50] SPEAKER_01: like much more intuitive and like trivial to get value from.
[00:18:54] SPEAKER_01: So the way that most people discover, like the vast majority
[00:18:57] SPEAKER_01: of users discover Codex today is either they download an IDE
[00:19:00] SPEAKER_01: extension or they run it in their CLI.
[00:19:03] SPEAKER_01: And the agent works there with you on your computer
[00:19:06] SPEAKER_01: interactively.
[00:19:07] SPEAKER_01: And it works within a sandbox, which is actually
[00:19:09] SPEAKER_01: like a really cool piece of tech to help that be safe and secure.
[00:19:13] SPEAKER_01: But it has access to all those dependencies.
[00:19:16] SPEAKER_01: So if the agent needs to do something,
[00:19:17] SPEAKER_01: like it needs to run a command, it
[00:19:18] SPEAKER_01: can do so within the sandbox.
[00:19:19] SPEAKER_01: We don't have to set up any environment.
[00:19:21] SPEAKER_01: And if it's a command that doesn't work in the sandbox,
[00:19:23] SPEAKER_01: it can just ask you.
[00:19:24] SPEAKER_01: And so you can get into this like really strong feedback loop
[00:19:27] SPEAKER_01: using the model.
[00:19:28] SPEAKER_01: And then over time, like our team's job
[00:19:30] SPEAKER_01: is to help turn that feedback loop into you, sort of,
[00:19:34] SPEAKER_01: as a byproduct of using the product,
[00:19:35] SPEAKER_01: configuring it so that you can then be delegating to it
[00:19:37] SPEAKER_01: down the line.
[00:19:38] SPEAKER_01: And again, Nougie, you're going to keep coming back to it.
[00:19:41] SPEAKER_01: But if you hire a teammate and you're asking to do work,
[00:19:43] SPEAKER_01: but you just give them a fresh computer from the store,
[00:19:47] SPEAKER_01: it's going to be hard for them to do their job, right?
[00:19:48] SPEAKER_01: But if as you work with them side by side,
[00:19:50] SPEAKER_01: you can be like, oh, you don't have a password for this service
[00:19:52] SPEAKER_01: we use.
[00:19:53] SPEAKER_01: Here's the password for the service.
[00:19:55] Yeah, don't worry.
[00:19:56] SPEAKER_01: Feel free to run this command.
[00:19:57] SPEAKER_01: Then it's much easier for them to then go off
[00:19:59] SPEAKER_01: and do work for hours without you.
[00:20:01] SPEAKER_01: So what I'm hearing is the initial version of Codex
[00:20:04] SPEAKER_00: was almost too far in the future.
[00:20:05] SPEAKER_00: It's like a remote in the cloud agent that's
[00:20:08] SPEAKER_00: coding for you asynchronously.
[00:20:10] SPEAKER_00: And what you did is, OK, let's actually
[00:20:12] SPEAKER_00: come back a little bit.
[00:20:13] SPEAKER_00: Let's integrate into the way engineers
[00:20:15] SPEAKER_00: already integrate into IDs and locally
[00:20:18] SPEAKER_00: and help them kind of on-ramp to this new world.
[00:20:21] SPEAKER_00: Totally.
[00:20:21] SPEAKER_00: And if this was quite interesting because we
[00:20:25] SPEAKER_01: dog food products a ton, an open AI.
[00:20:28] SPEAKER_01: So dog food as in we use our own product.
[00:20:31] SPEAKER_01: And so Codex has been accelerating open AI
[00:20:33] SPEAKER_01: over the course of the entire year.
[00:20:35] SPEAKER_01: And the cloud product was a massive accelerant
[00:20:37] SPEAKER_01: to the company as well.
[00:20:40] SPEAKER_01: It just turns out that this was one of those places
[00:20:43] SPEAKER_01: where the signal we got from dog fooding
[00:20:45] SPEAKER_01: is a little bit different from the signal you get
[00:20:47] SPEAKER_01: from the general market.
[00:20:48] SPEAKER_01: Because at OpenAI, we train reasoning models all day.
[00:20:51] SPEAKER_01: And so we're very used to this kind of prompting
[00:20:53] SPEAKER_01: and think upfront, run things massively in parallel.
[00:20:57] SPEAKER_01: And it takes some time and then come back to it later
[00:21:00] SPEAKER_01: asynchronously.
[00:21:02] SPEAKER_01: And so now when we build, we still get a ton of signal
[00:21:05] SPEAKER_01: from dog fooding internally.
[00:21:06] SPEAKER_01: But we're also very cognizant of the different ways
[00:21:11] SPEAKER_01: the different audiences use the product.
[00:21:12] SPEAKER_01: That's really funny.
[00:21:13] SPEAKER_00: It's like, live in the future, but maybe not too far
[00:21:16] SPEAKER_00: in the future.
[00:21:17] SPEAKER_00: And I could see everyone open AI is living very far
[00:21:19] SPEAKER_00: in the future.
[00:21:20] SPEAKER_00: And sometimes they won't work for everyone.
[00:21:23] SPEAKER_00: What about just intelligence training data?
[00:21:26] SPEAKER_00: I don't know.
[00:21:27] SPEAKER_00: Is there something else that helped codex accelerate?
[00:21:30] SPEAKER_00: Its ability to actually code.
[00:21:31] SPEAKER_00: Is it better, cleaner data?
[00:21:34] SPEAKER_00: Is it more just models advancing?
[00:21:35] SPEAKER_00: Is there anything else that really helped accelerate?
[00:21:38] SPEAKER_01: Yeah.
[00:21:38] SPEAKER_01: So there's like a few components here.
[00:21:41] SPEAKER_01: I guess you were mentioning models
[00:21:43] SPEAKER_01: and the models have improved a ton.
[00:21:44] SPEAKER_01: In fact, just last Wednesday, we shipped GPG501 codex
[00:21:48] SPEAKER_01: max, a very accurate lead name model.
[00:21:53] SPEAKER_01: That is awesome.
[00:21:54] SPEAKER_01: It is awesome both because it is for any given task
[00:21:58] SPEAKER_01: that you were using GPG501 codex for.
[00:22:01] It's roughly 30% faster at accomplishing a task.
[00:22:05] SPEAKER_01: But also it unlocks a ton of intelligence.
[00:22:07] SPEAKER_01: So if you use it at our higher reasoning levels,
[00:22:10] SPEAKER_01: it's just even smarter.
[00:22:12] SPEAKER_01: And that feedback or that tweet you were saying,
[00:22:14] SPEAKER_01: Carpati made about, hey, give this to your gnarliest bugs.
[00:22:18] SPEAKER_01: Obviously, there's a ton going on in the market right now.
[00:22:20] SPEAKER_01: And but codex max is definitely carrying that mantle
[00:22:23] SPEAKER_01: of tackling the hardest bugs.
[00:22:26] SPEAKER_01: So that is super cool.
[00:22:28] SPEAKER_01: But I will say it's like some of what,
[00:22:31] SPEAKER_01: how we're thinking about this is evolving a little bit
[00:22:33] SPEAKER_01: from being like, yeah, we're just going
[00:22:34] SPEAKER_01: to think about the model and let's just train the best model.
[00:22:36] SPEAKER_01: So really thinking about what is an agent actually overall?
[00:22:42] And I'm not going to try to define agent exactly,
[00:22:44] SPEAKER_01: but at least the stack that we think of it as having
[00:22:46] SPEAKER_01: is it's like you have this model, really
[00:22:48] as far as reasoning model, that knows
[00:22:50] how to do a specific kind of task really well.
[00:22:52] SPEAKER_01: So we can talk about how we make that possible.
[00:22:54] SPEAKER_01: But then actually, we need to serve that model
[00:22:57] through an API into a harness.
[00:23:00] SPEAKER_01: And both of those things also have a really big role here.
[00:23:02] SPEAKER_01: So for instance, one of the things that we're really proud of
[00:23:06] SPEAKER_01: is you can have GP5.1 Carpati's max work
[00:23:08] SPEAKER_01: for really long periods of time.
[00:23:10] SPEAKER_01: That's not like normal, but you can set it up to do that
[00:23:12] SPEAKER_01: or that might happen.
[00:23:13] SPEAKER_01: But now routinely we'll hear about people saying,
[00:23:15] SPEAKER_01: yeah, I ran overnight or I ran for 24 hours.
[00:23:18] SPEAKER_01: And so for a model to work continuously
[00:23:21] SPEAKER_01: for that amount of time, it's going to exceed its context
[00:23:23] SPEAKER_01: window.
[00:23:24] SPEAKER_01: And so we have a solution for that, which we call compaction.
[00:23:28] But compaction is actually a feature that
[00:23:29] SPEAKER_01: uses all three layers of that stack.
[00:23:32] SPEAKER_01: So you need to have a model that has a concept of compaction.
[00:23:36] SPEAKER_01: And those like, OK, as I started to approach this context
[00:23:38] SPEAKER_01: window, I might be asked to prepare to be running
[00:23:41] SPEAKER_01: a new context window.
[00:23:42] SPEAKER_01: And then at the API layer, you need an API that
[00:23:45] SPEAKER_01: understands this concept.
[00:23:46] SPEAKER_01: And as an endpoint, then you can hit to do this change.
[00:23:49] SPEAKER_01: And at the harness layer, you need a harness
[00:23:50] SPEAKER_01: that you can prepare the payload for this to be done.
[00:23:52] SPEAKER_01: And so shipping this compaction feature that now just
[00:23:55] SPEAKER_01: like made this behavior possible to anyone using Codex,
[00:23:58] SPEAKER_01: actually been working across all three things.
[00:24:00] SPEAKER_01: And I think that's increasingly going to be true.
[00:24:02] SPEAKER_01: Another maybe under appreciated version of this
[00:24:06] SPEAKER_01: is if you think about all the different coding products
[00:24:09] SPEAKER_01: out there, they all have very different tool harnesses
[00:24:11] SPEAKER_01: with very different opinions on how the model should work.
[00:24:14] And so if you want to train a model to be good at all
[00:24:16] SPEAKER_01: the different ways, it could work.
[00:24:19] SPEAKER_01: Maybe you have a strong opinion that it should work
[00:24:21] SPEAKER_01: using semantic search.
[00:24:22] SPEAKER_01: Maybe you have a strong opinion that it should call
[00:24:24] SPEAKER_01: the spoke tools.
[00:24:25] SPEAKER_01: Or maybe you have, in our case, a strong opinion
[00:24:27] SPEAKER_01: that it should just use the shell, work in the terminal.
[00:24:32] SPEAKER_01: You can move much faster if you're just optimizing for one
[00:24:34] SPEAKER_01: of those worlds.
[00:24:35] SPEAKER_01: And so the way that we built Codex is that it just uses the shell.
[00:24:39] SPEAKER_01: But in order to make that safer and secure,
[00:24:41] SPEAKER_01: we have a sandbox that the model is used to operating in.
[00:24:45] So I think one of the biggest accelerants
[00:24:47] SPEAKER_01: to go all the way back to your answer of Russian
[00:24:48] SPEAKER_01: is just like, we're building all three things in parallel
[00:24:51] SPEAKER_01: and kind of tuning each one and constantly experimenting
[00:24:55] SPEAKER_01: with how those things work with a tightly integrated
[00:24:58] SPEAKER_01: product and research team.
[00:24:59] SPEAKER_01: How do you think you win in this space?
[00:25:02] SPEAKER_00: Do you think it'll always be this kind of race
[00:25:05] SPEAKER_00: with other models constantly kind of leapfrogging each other?
[00:25:09] SPEAKER_00: Do you think there's a world where someone just
[00:25:10] SPEAKER_00: runs away with it and no one else can ever catch up?
[00:25:13] SPEAKER_00: Is there a path to just we win?
[00:25:15] Again, comes back to this idea of building a teammate.
[00:25:18] And not just a teammate that participates in team planning
[00:25:23] SPEAKER_01: and prioritization, not just a teammate that really tests
[00:25:26] SPEAKER_01: its code and helps you maintain and deploy it.
[00:25:29] SPEAKER_01: But even a teammate, if you think again,
[00:25:30] SPEAKER_01: an engineering teammate, they can also
[00:25:32] SPEAKER_01: like schedule a calendar invite or move stand up
[00:25:35] SPEAKER_01: or do whatever.
[00:25:36] SPEAKER_01: And so in my mind, if we just imagine
[00:25:41] SPEAKER_01: that every day or every week, some crazy new capabilities
[00:25:45] SPEAKER_01: just going to be deployed by a research lab,
[00:25:47] SPEAKER_01: it's just impossible for us as humans to keep up
[00:25:50] SPEAKER_01: and use all this technology.
[00:25:52] SPEAKER_01: And so I think we need to get to this world
[00:25:54] SPEAKER_01: where you kind of just have an AI teammate or super assistant
[00:25:59] SPEAKER_01: that you just talked to.
[00:26:00] SPEAKER_01: And it just knows how to be helpful on its own.
[00:26:04] And so you don't have to be reading the latest tips
[00:26:07] SPEAKER_01: for how to use it.
[00:26:07] SPEAKER_01: And you just plug it in and it just provides help.
[00:26:10] SPEAKER_01: And so that's kind of the shape of what I think we're building.
[00:26:13] SPEAKER_01: And I think that will be a very sticky winning product
[00:26:16] SPEAKER_01: if we can do so.
[00:26:17] SPEAKER_01: So the shape that I might have, at least I have,
[00:26:19] SPEAKER_01: is that we build maybe a fun topic
[00:26:22] SPEAKER_01: is like, is chat the right interface for AI?
[00:26:24] SPEAKER_01: Actually, chat is a very good interface
[00:26:27] when you don't know what you're supposed to use it for.
[00:26:29] SPEAKER_01: In the same way that if I think of like,
[00:26:31] SPEAKER_01: I'm like on a team's or in Slack with a teammate, chat
[00:26:34] SPEAKER_01: is pretty good.
[00:26:34] SPEAKER_01: I can ask for whatever I want.
[00:26:36] SPEAKER_01: It's kind of the nominator for everything.
[00:26:38] SPEAKER_01: So you can chat with the super assistant
[00:26:40] SPEAKER_01: about whatever topic you want, whether it be coding or not.
[00:26:43] SPEAKER_01: And then if you are like a functional expert
[00:26:46] SPEAKER_01: in a specific domain such as coding,
[00:26:48] SPEAKER_01: there's like a GUI that you can pull up to go really deep
[00:26:52] SPEAKER_01: and like look at the code and like work with the code.
[00:26:54] SPEAKER_01: So I think like what we need to build as opening I is basically
[00:26:59] SPEAKER_01: this idea of like, you have chat, chat, PT,
[00:27:01] SPEAKER_01: and not as a tool that's like ubiquitously available
[00:27:03] SPEAKER_01: to like everyone, you start using it even like outside of work,
[00:27:07] SPEAKER_01: right, to just help you.
[00:27:08] SPEAKER_01: You become very comfortable with the idea
[00:27:09] SPEAKER_01: of being accelerated with AI.
[00:27:11] SPEAKER_01: And so then you get to work and you just can naturally just,
[00:27:13] SPEAKER_01: yeah, I'm just gonna ask it for this.
[00:27:15] SPEAKER_01: And I don't need to know about all the connectors
[00:27:17] SPEAKER_01: or like all the different features.
[00:27:18] SPEAKER_01: I'm just gonna ask it for help.
[00:27:19] SPEAKER_01: And it'll surface to me the best way that it can help
[00:27:22] SPEAKER_01: at this point in time.
[00:27:23] SPEAKER_01: And maybe even chime in when I didn't ask it for help.
[00:27:26] So in my mind, if we can get to that,
[00:27:28] SPEAKER_01: I think that's, you know, that's how we really build
[00:27:30] SPEAKER_01: like the winning product.
[00:27:32] This is so interesting because with the,
[00:27:34] SPEAKER_00: my chat would nick Charlie, the head of chat, PT.
[00:27:36] SPEAKER_00: I think he shared that the original name for chat,
[00:27:38] SPEAKER_00: PT was super assistant or something like that.
[00:27:41] SPEAKER_00: Yeah.
[00:27:42] SPEAKER_00: And it's interesting that there's like that approach
[00:27:45] SPEAKER_00: to the super assistant and then there's this codex approach.
[00:27:47] SPEAKER_00: It's almost like the beta c version and the beta b version.
[00:27:51] And what I'm hearing is the idea here is,
[00:27:52] SPEAKER_00: okay, you start with coding and building.
[00:27:54] SPEAKER_00: And then it's doing all this other stuff
[00:27:55] SPEAKER_00: for you scheduling meetings.
[00:27:57] SPEAKER_00: I don't know, probably posting and Slack.
[00:28:00] SPEAKER_00: I don't know, shipping designs.
[00:28:01] SPEAKER_00: I don't know, is that, is the idea there?
[00:28:02] SPEAKER_00: This is like the business version of chat,
[00:28:05] SPEAKER_00: PT in a sense or is there, or is there something else there?
[00:28:08] SPEAKER_00: Yeah.
[00:28:09] SPEAKER_01: So we're getting to the like one year time horizon conversation.
[00:28:13] SPEAKER_01: A lot of this might happen sooner,
[00:28:14] SPEAKER_01: but in terms of fuzziness, I think that the one year.
[00:28:16] SPEAKER_01: So I'll give you like a contention
[00:28:19] SPEAKER_01: in like a plausible way we get there.
[00:28:20] SPEAKER_01: But as for how it happens, who knows?
[00:28:22] SPEAKER_01: So basically, if we're going to build a super assistant,
[00:28:25] SPEAKER_01: it has to be able to do things, right?
[00:28:27] SPEAKER_01: So like we're going to have a model
[00:28:28] SPEAKER_01: and it's going to be able to do stuff affecting your world.
[00:28:31] SPEAKER_01: And one of the learnings I think we've seen over the past year
[00:28:35] SPEAKER_01: or so is that for models to do stuff,
[00:28:37] SPEAKER_01: they're much more effective when they can use a computer.
[00:28:41] Right.
[00:28:42] SPEAKER_01: Okay.
[00:28:42] SPEAKER_01: So now we're like, okay, we need the super assistant
[00:28:44] SPEAKER_01: that can use a computer, right?
[00:28:45] SPEAKER_01: Or many computers.
[00:28:47] And now the question is, okay, well, how should it use the computer?
[00:28:50] Right.
[00:28:51] SPEAKER_01: And there's lots of ways to use a computer.
[00:28:52] SPEAKER_01: You know, you could try to hack the OS
[00:28:54] SPEAKER_01: and like use accessibility APIs, maybe a bit easier
[00:28:56] SPEAKER_01: as you could point and click.
[00:28:58] That's a little slow, you know, and unpredictable sometimes.
[00:29:01] SPEAKER_01: And another way, it turns out the best way
[00:29:04] SPEAKER_01: for models to use computers is simply to write code.
[00:29:07] Right.
[00:29:08] SPEAKER_01: And so we're kind of getting to this idea where like,
[00:29:09] SPEAKER_01: well, if you want to build any agent,
[00:29:11] SPEAKER_01: maybe you should be building a coding agent.
[00:29:13] SPEAKER_01: And maybe to the user, a non-technical user,
[00:29:16] SPEAKER_01: they won't even know they're using a coding agent.
[00:29:18] SPEAKER_01: The same way that no one thinks about,
[00:29:19] SPEAKER_01: are they using the internet or not?
[00:29:20] SPEAKER_01: And just they're more just like, is Wi-Fi on?
[00:29:22] Right.
[00:29:23] So I think that what we're doing with codex
[00:29:25] SPEAKER_01: is we're building a software engineering teammate.
[00:29:28] SPEAKER_01: And as part of that, we're kind of building an agent
[00:29:30] SPEAKER_01: that can use a computer by writing code.
[00:29:34] SPEAKER_01: And so we're already seeing like some pull for this.
[00:29:37] SPEAKER_01: It's like quite early.
[00:29:38] SPEAKER_01: We're starting to see people like we're using codex
[00:29:40] SPEAKER_01: for like coding adjacent product purposes.
[00:29:43] And so as that develops, I think we'll just naturally see
[00:29:46] SPEAKER_01: that like, oh, it turns out like we should just always have
[00:29:48] SPEAKER_01: the agent write code if there is a coding way
[00:29:50] SPEAKER_01: to solve a problem instead of even if you're doing
[00:29:53] SPEAKER_01: in financial analysis, right?
[00:29:54] SPEAKER_01: Like maybe write some code for that.
[00:29:55] SPEAKER_01: So basically, like, you were like,
[00:29:56] SPEAKER_01: hey, this is like the two ends of this product
[00:29:59] SPEAKER_01: for the super assistant, right, of ChatGPT.
[00:30:02] SPEAKER_01: In my mind, like just coding is a core competency
[00:30:04] SPEAKER_01: of any agent including ChatGPT.
[00:30:06] SPEAKER_01: And so like what really what we think we're building
[00:30:08] SPEAKER_01: is like that competency.
[00:30:10] SPEAKER_01: So here's like the really cool thing about agents
[00:30:12] SPEAKER_01: writing code is that you can import code, right?
[00:30:15] SPEAKER_01: Code is like composable, interoperable, right?
[00:30:19] SPEAKER_01: Because if we, you know, one very reductive view
[00:30:22] SPEAKER_01: we could have for an agent is it's just going to be given
[00:30:24] SPEAKER_01: a computer and it's just going to like point and click
[00:30:26] SPEAKER_01: and you know, go around.
[00:30:28] SPEAKER_01: But you know, that is the future.
[00:30:30] SPEAKER_01: And then how we get there is difficult to sort of chart
[00:30:34] SPEAKER_01: a path because a lot of the questions around building agents
[00:30:37] SPEAKER_01: aren't like can the agent do it.
[00:30:38] SPEAKER_01: But it's more about, well, how can we help the agent
[00:30:42] SPEAKER_01: understand the context that it's working in?
[00:30:43] SPEAKER_01: And like the team that's using it, you know,
[00:30:45] SPEAKER_01: probably has a way that they like to do things.
[00:30:47] SPEAKER_01: They have guidelines.
[00:30:48] SPEAKER_01: They probably want certain deterministic guarantees
[00:30:51] SPEAKER_01: about what the agent can or cannot do.
[00:30:53] Well, they want to know that the agent understands
[00:30:56] SPEAKER_01: sort of this detail, like an example would be,
[00:30:58] SPEAKER_01: you know, if we're looking at a crash reporting tool
[00:31:02] SPEAKER_01: hitting a connector for it,
[00:31:03] SPEAKER_01: every sub team is probably has a different meta prompt
[00:31:06] SPEAKER_01: for like how they want the crashes to be analyzed.
[00:31:10] Right.
[00:31:10] And so we start to get to this thing where like,
[00:31:12] SPEAKER_01: yeah, we have this agency in front of a computer,
[00:31:14] SPEAKER_01: but we need to make that configurable for the team
[00:31:16] SPEAKER_01: or for the user, right?
[00:31:18] SPEAKER_01: And let them like stuff that the agent does often.
[00:31:20] SPEAKER_01: And we probably just want to like build in
[00:31:22] SPEAKER_01: as a competency that this agent has that it can do.
[00:31:24] SPEAKER_01: So I think we end up with this generalizable thing
[00:31:28] SPEAKER_01: that you were saying of like an agent
[00:31:30] SPEAKER_01: that can just write its own scripts for whatever it wants to do.
[00:31:33] SPEAKER_01: But I think that the really key part here is can we make it
[00:31:37] SPEAKER_01: so that everything that the agent has to do often
[00:31:40] SPEAKER_01: or that it does well, we can just like remember and store
[00:31:44] SPEAKER_01: so that the agent doesn't have to write a script for that again, right?
[00:31:46] SPEAKER_01: Or maybe like if I just joined a team
[00:31:48] SPEAKER_01: and you are already on the same team as me,
[00:31:50] SPEAKER_01: I can just like use all those scripts
[00:31:52] SPEAKER_01: that the agent said written already.
[00:31:53] SPEAKER_01: Yeah, that's like, if this is our teammate,
[00:31:56] SPEAKER_00: we can share things that it's learned from working
[00:31:58] SPEAKER_00: with other people at the company.
[00:32:00] SPEAKER_00: Just makes sense as a metaphor.
[00:32:01] SPEAKER_00: Yeah.
[00:32:02] SPEAKER_00: So it's like you're in the Carpati camp of agents today
[00:32:05] SPEAKER_00: or not that great and mostly slop and maybe in the future,
[00:32:08] SPEAKER_00: they'll be awesome.
[00:32:09] SPEAKER_00: Does that resonate?
[00:32:10] SPEAKER_00: I think so I think coding agents are pretty great.
[00:32:12] SPEAKER_00: I think we're still trying to complete it.
[00:32:15] SPEAKER_01: Yeah.
[00:32:16] SPEAKER_01: And then I think like agent side outside of coding,
[00:32:19] SPEAKER_01: it's still like very early.
[00:32:21] SPEAKER_01: And you know, this is just my opinion,
[00:32:22] SPEAKER_01: but I think they're going to get a whole lot better
[00:32:24] SPEAKER_01: once they can use coding too in like in a composable way.
[00:32:28] This is kind of the fun part of like when you're building
[00:32:30] SPEAKER_01: for software engineers, like I,
[00:32:32] at my startup, we were building for software engineers too
[00:32:34] SPEAKER_01: for a lot of that journey.
[00:32:35] SPEAKER_01: And they're just such a fun audience to build for
[00:32:38] SPEAKER_01: because they also like building for themselves
[00:32:42] SPEAKER_01: and are often like even more creative than we are
[00:32:44] SPEAKER_01: in thinking about how to use the technology.
[00:32:46] SPEAKER_01: And so like by building for software engineers,
[00:32:48] SPEAKER_01: you get to just observe a ton of emerging behaviors
[00:32:50] SPEAKER_01: and like things that you should do
[00:32:52] SPEAKER_01: and build into the product.
[00:32:54] SPEAKER_00: I love how you say that because a lot of people
[00:32:55] SPEAKER_00: building for engineers get really annoyed
[00:32:57] SPEAKER_00: because then engineers have her.
[00:32:58] SPEAKER_00: So there's always complain about stuff.
[00:33:00] SPEAKER_00: They're like, yeah, the sex.
[00:33:01] SPEAKER_00: Why'd you build it this way?
[00:33:03] SPEAKER_00: I love that you enjoy it,
[00:33:04] SPEAKER_00: but I think it's probably because you're building
[00:33:05] SPEAKER_00: such an amazing tool for engineers
[00:33:07] SPEAKER_00: that can actually solve problems and just code for them.
[00:33:12] SPEAKER_00: Cut along the lines, you know,
[00:33:13] SPEAKER_00: there's always this talk of what will happen
[00:33:15] SPEAKER_00: to jobs, engineers coding,
[00:33:17] SPEAKER_00: you have to learn coding, all these things.
[00:33:19] SPEAKER_00: Clearly the way you're just scarring it is a teammate.
[00:33:21] SPEAKER_00: It's going to work with you and making more superhuman.
[00:33:23] SPEAKER_00: It's not going to replace you.
[00:33:24] SPEAKER_00: What's the way you just think about the impact
[00:33:26] SPEAKER_00: on the field of engineering having this super intelligent
[00:33:31] SPEAKER_00: engineering teammate?
[00:33:32] SPEAKER_00: I think there's two sides to it,
[00:33:34] SPEAKER_01: but the one we were just talking about
[00:33:36] SPEAKER_01: is this idea that maybe every agent should actually use code
[00:33:41] SPEAKER_01: and be a coding agent.
[00:33:42] SPEAKER_01: And in my mind, that's just like a small part
[00:33:44] SPEAKER_01: of this like broader idea that like,
[00:33:46] SPEAKER_01: hey, as we make code even more ubiquitous,
[00:33:47] SPEAKER_01: I mean, you could probably claim it's ubiquitous today,
[00:33:49] SPEAKER_01: even pre-AI, right?
[00:33:50] SPEAKER_01: And as we make code even more ubiquitous,
[00:33:52] SPEAKER_01: it's actually just going to be used for many more purposes.
[00:33:56] And so there's just going to be a ton more need
[00:33:58] SPEAKER_01: for people with this, like humans with this competency.
[00:34:01] SPEAKER_01: So that's my view.
[00:34:03] SPEAKER_01: I think this is like quite a complex topic.
[00:34:05] SPEAKER_01: So you know, it's something we talk about a lot
[00:34:08] SPEAKER_01: and we have to kind of see how it pans out.
[00:34:09] SPEAKER_01: But I think what we can do,
[00:34:11] what we can do basically as a product team building
[00:34:13] SPEAKER_01: in the space is just try to always think about
[00:34:15] SPEAKER_01: how are we building a tool so that it feels like
[00:34:17] SPEAKER_01: we're like maximally accelerating people,
[00:34:21] SPEAKER_01: you know, rather than building a tool
[00:34:22] SPEAKER_01: that makes it like more unclear what you should do
[00:34:25] SPEAKER_01: is the human, right?
[00:34:26] SPEAKER_01: Like I think like to, you know, give an example right now,
[00:34:30] SPEAKER_01: like nowadays when you work with a coding agent,
[00:34:34] SPEAKER_01: it writes a ton of code,
[00:34:35] SPEAKER_01: but it turns out writing code is actually one
[00:34:36] SPEAKER_01: of the most fun parts of software engineering
[00:34:38] SPEAKER_01: for many software engineers.
[00:34:40] SPEAKER_01: It's the new and end up reviewing AI code, right?
[00:34:43] SPEAKER_01: And that's often a less fun part of the job
[00:34:46] SPEAKER_01: for many software engineers, right?
[00:34:48] SPEAKER_01: And so I actually think like we see that like this,
[00:34:50] SPEAKER_01: this comes out plays out all the time
[00:34:52] SPEAKER_01: in like a ton of micro decisions.
[00:34:53] SPEAKER_01: And so we as a product team are always thinking about like,
[00:34:55] SPEAKER_01: okay, how do we make this more fun?
[00:34:56] SPEAKER_01: How do we make you feel more empowered?
[00:34:57] SPEAKER_01: Whereas it's not working and I would argue that like,
[00:35:00] SPEAKER_01: reviewing agent written code is like a place that
[00:35:02] SPEAKER_01: today is like less fun.
[00:35:03] SPEAKER_01: And so, you know, then I think, okay,
[00:35:05] SPEAKER_01: what can we do about that?
[00:35:06] SPEAKER_01: Well, we can ship a code review feature
[00:35:08] SPEAKER_01: that like helps you build confidence in the air written code.
[00:35:10] SPEAKER_01: Okay, cool.
[00:35:12] You know, another thing we could do
[00:35:12] is we can make it so that the agents like
[00:35:14] SPEAKER_01: better able to validate its work.
[00:35:16] And you know, it gets all the way down
[00:35:18] SPEAKER_01: into like micro decisions like if you're gonna have
[00:35:20] SPEAKER_01: the and agent capability to validate work.
[00:35:23] SPEAKER_01: And let's say you have like,
[00:35:24] SPEAKER_01: I'm thinking of codex web right now,
[00:35:25] SPEAKER_01: like you have a pain that sort of reflects the work
[00:35:28] SPEAKER_01: the agent did.
[00:35:29] SPEAKER_01: What do you see first?
[00:35:30] SPEAKER_01: Do you see the diff?
[00:35:30] SPEAKER_01: Or do you see the image preview of the code it wrote?
[00:35:33] Right?
[00:35:34] And you know, I think if you're thinking about this
[00:35:36] SPEAKER_01: from perspective like, how do I empower the human?
[00:35:37] SPEAKER_01: How do I make them feel like as accelerated as possible?
[00:35:39] SPEAKER_01: Like you obviously see the image first, right?
[00:35:42] SPEAKER_01: You shouldn't be reviewing the code unless first,
[00:35:44] SPEAKER_01: you know, you've seen the image
[00:35:45] SPEAKER_01: unless it maybe it's being like reviewed by an AI
[00:35:47] SPEAKER_01: and now it's time for you to take a look.
[00:35:49] When I had Michael Turell, the CEO of cursor on the podcast,
[00:35:51] SPEAKER_00: he had this kind of vision of us moving
[00:35:55] SPEAKER_00: to something beyond code.
[00:35:57] SPEAKER_00: And I've seen this rise of something
[00:35:58] SPEAKER_00: all spectraven development where you kind of just write
[00:36:00] SPEAKER_00: the spec and then the code, you know,
[00:36:03] SPEAKER_00: the AI writes code for you.
[00:36:04] SPEAKER_00: And so you kind of start working
[00:36:05] SPEAKER_00: at this higher abstraction level.
[00:36:07] SPEAKER_00: Is that something you see where we're going just like,
[00:36:10] SPEAKER_00: engineers not having to actually write code or look at code
[00:36:12] SPEAKER_00: and there's gonna be this higher level of abstraction
[00:36:14] SPEAKER_00: that we focus on?
[00:36:16] Yeah, I mean, I think,
[00:36:17] I think there's like constantly these levels of abstraction
[00:36:19] SPEAKER_01: and they're actually already played out today, right?
[00:36:22] Like today, like coding agents, mostly it's like prompt to patch,
[00:36:27] SPEAKER_01: right?
[00:36:28] SPEAKER_01: We're starting to see people doing like spectraven development
[00:36:31] SPEAKER_01: or like planned and driven development
[00:36:32] SPEAKER_01: that's actually one of the ways when people ask,
[00:36:34] SPEAKER_01: like, hey, how do you run codex on a really long task?
[00:36:36] SPEAKER_01: Well, it's like often collaborate with it first
[00:36:38] SPEAKER_01: to write like a planned on MD,
[00:36:39] SPEAKER_01: like a markdown file that's your plan.
[00:36:41] SPEAKER_01: And once you're happy with that,
[00:36:43] then you ask it to go off and do work.
[00:36:44] SPEAKER_01: And if that plan has verifiable steps,
[00:36:46] SPEAKER_01: it'll like work for much longer.
[00:36:48] SPEAKER_01: So we're totally seeing that.
[00:36:50] I think spectraven development is like an interesting
[00:36:52] SPEAKER_01: idea is not clear to me that it'll work out that way
[00:36:56] SPEAKER_01: because a lot of people don't write,
[00:36:57] SPEAKER_01: don't like writing specs either.
[00:36:59] SPEAKER_01: But it seems plausible that some people work that way.
[00:37:03] SPEAKER_01: You know, like a bit of a joke idea though,
[00:37:05] SPEAKER_01: is like if you think of like the way
[00:37:08] SPEAKER_01: that many teams work today,
[00:37:09] SPEAKER_01: they often don't necessarily have specs,
[00:37:12] SPEAKER_01: but the team is just really self-driven
[00:37:14] SPEAKER_01: and so stuff just gets done.
[00:37:15] SPEAKER_01: And so almost that is like,
[00:37:16] SPEAKER_01: I'm coming up with this on the spot,
[00:37:17] SPEAKER_01: so it's not a good name,
[00:37:18] SPEAKER_01: but like chatter driven development.
[00:37:21] Where it's just like, stuff is happening on social media
[00:37:23] SPEAKER_01: and like in your team communications tools.
[00:37:25] SPEAKER_01: And then as a result,
[00:37:26] SPEAKER_01: like code gets written and deployed.
[00:37:29] SPEAKER_01: Right, so yeah, I think I'm a little bit more oriented
[00:37:32] SPEAKER_01: in that way of,
[00:37:33] SPEAKER_01: you know, I don't even necessarily want to have to write a spec.
[00:37:36] SPEAKER_01: Like sometimes I want to,
[00:37:37] SPEAKER_01: only if I like writing specs, right?
[00:37:41] SPEAKER_01: Other times I might just want to say like,
[00:37:43] SPEAKER_01: hey, here's like the customer service channel
[00:37:45] SPEAKER_01: and like, tell me what's interesting to know.
[00:37:47] SPEAKER_01: But if it's a small bug, just fix it,
[00:37:49] SPEAKER_01: I don't have to write a spec for that, right?
[00:37:51] SPEAKER_01: I have this sort of hypothetical future
[00:37:56] SPEAKER_01: that I like to share sometimes with people as a provocation,
[00:37:58] SPEAKER_01: which is like in a world where we have like,
[00:38:00] SPEAKER_01: truly amazing agents, like what does it look like
[00:38:02] SPEAKER_01: to be a solo printer?
[00:38:05] And you know, one terrible idea for how it could look
[00:38:08] SPEAKER_01: is that it's actually, there's a mobile app.
[00:38:10] SPEAKER_01: And every idea that the agent has to do
[00:38:14] SPEAKER_01: is just like vertical video on your phone.
[00:38:17] SPEAKER_01: And then you can like swipe left
[00:38:19] SPEAKER_01: if you think it's a bad idea
[00:38:20] SPEAKER_01: and you can like swipe right if it's a good idea.
[00:38:22] SPEAKER_01: And like you can press and hold and like speak to your phone
[00:38:25] SPEAKER_01: if you want to get feedback on the idea before you swipe.
[00:38:28] You know, and then this world like basically what your job is
[00:38:30] SPEAKER_01: just like plug in this app into like every single like signal
[00:38:33] SPEAKER_01: system, you know, system of record.
[00:38:36] SPEAKER_01: And then you just sort of sit back and like swipe.
[00:38:38] I don't know.
[00:38:39] SPEAKER_01: And love this.
[00:38:40] SPEAKER_00: So there's like Tinder meets TikTok meets codex.
[00:38:42] SPEAKER_00: It's pretty terrible.
[00:38:44] SPEAKER_00: No, this is great.
[00:38:45] SPEAKER_00: So the idea here is this thing is this agent
[00:38:46] SPEAKER_00: is watching and right, listening to you,
[00:38:49] SPEAKER_00: paying attention to the market, your users.
[00:38:51] SPEAKER_00: And it's like, well, I hear something I should do.
[00:38:53] SPEAKER_00: It's like a proactive engineer,
[00:38:54] SPEAKER_00: just like here, we should build this feature fix this thing.
[00:38:56] SPEAKER_00: Exactly.
[00:38:57] SPEAKER_00: Exactly.
[00:38:58] SPEAKER_00: We're really gonna communicate with you
[00:38:59] SPEAKER_01: in like the lowest way for you to get the gym.
[00:39:02] SPEAKER_00: The modern way to communicate.
[00:39:05] SPEAKER_00: Yeah, swipe left to right and vertical feed.
[00:39:08] SPEAKER_00: And then the Sora video, okay,
[00:39:09] SPEAKER_00: so I see how the sulking X now.
[00:39:11] SPEAKER_00: Nice see.
[00:39:12] SPEAKER_01: Yeah, to be clear, we're not building that,
[00:39:13] SPEAKER_01: but like, you know, it's a fun idea.
[00:39:15] SPEAKER_01: I mean, you see, you know, like in this example though,
[00:39:17] SPEAKER_01: like one of the things that it's doing
[00:39:18] SPEAKER_01: is it's consuming external signals, right?
[00:39:21] SPEAKER_01: I think the other really interesting things,
[00:39:23] SPEAKER_01: like if we think about like what is the most successful,
[00:39:25] SPEAKER_01: like AI product to date,
[00:39:29] SPEAKER_01: I would argue, it's funny,
[00:39:31] SPEAKER_01: actually not to confuse things at all,
[00:39:33] SPEAKER_01: but like the first time we used the brand codex
[00:39:36] SPEAKER_01: at OpenAI was actually the model powering
[00:39:38] SPEAKER_01: GitHub Copilot.
[00:39:39] SPEAKER_01: This is like way back in the day years ago.
[00:39:41] SPEAKER_01: So we decided to reuse that brand recently,
[00:39:44] SPEAKER_01: because it's just so good, you know, codex, code execution.
[00:39:46] SPEAKER_01: But I think actually like auto completion in IDEs
[00:39:51] SPEAKER_01: is like one of the most successful AI products today.
[00:39:54] SPEAKER_01: And part of what's so magical about it
[00:39:56] SPEAKER_01: is that when the, it can surface like ideas
[00:40:00] SPEAKER_01: for helping you really rapidly, when it's right,
[00:40:04] SPEAKER_01: you're accelerated, when it's wrong,
[00:40:05] SPEAKER_01: it's not like that annoying, it can be annoying,
[00:40:08] SPEAKER_01: but it's not that annoying, right?
[00:40:09] SPEAKER_01: And so you can create this like next initiative system
[00:40:11] SPEAKER_01: that's like contextually responding
[00:40:13] SPEAKER_01: to like what you're attempting to do.
[00:40:16] And so in my mind, this is like a really interesting thing
[00:40:19] SPEAKER_01: for us as OpenAI as we're building.
[00:40:22] SPEAKER_01: So for instance, you know, when I think about launching a browser,
[00:40:25] SPEAKER_01: which we did with Atlas, right, like in my mind,
[00:40:29] one of the really interesting things we can then do
[00:40:31] SPEAKER_01: is we can then like contextually surface
[00:40:33] SPEAKER_01: like ways that we can help you
[00:40:34] SPEAKER_01: as you're going about your day, right?
[00:40:37] SPEAKER_01: And so we break out of this like, you know,
[00:40:39] SPEAKER_01: we're just looking at code or we're just in your terminal,
[00:40:42] SPEAKER_01: into this idea that like, hey,
[00:40:43] SPEAKER_01: like a real teammate is dealing with a lot more than just code,
[00:40:46] SPEAKER_01: right, they're dealing with a lot of things
[00:40:47] SPEAKER_01: that are web content.
[00:40:48] SPEAKER_01: So like, you know, how can we help you with that?
[00:40:51] Man, there's so much there.
[00:40:52] SPEAKER_00: And I love this.
[00:40:53] SPEAKER_00: So auto complete on web with the browser.
[00:40:55] SPEAKER_00: That's so interesting.
[00:40:56] SPEAKER_00: Just like here's all the things that we can help you with
[00:40:58] SPEAKER_00: as you're browsing and going about your day.
[00:41:01] SPEAKER_00: I want to talk about Atlas.
[00:41:02] SPEAKER_00: I'll come back to that.
[00:41:03] SPEAKER_00: Codex code execution did not know that.
[00:41:05] SPEAKER_00: That's really clever.
[00:41:07] SPEAKER_00: I get it now.
[00:41:08] SPEAKER_00: Okay.
[00:41:09] SPEAKER_00: And then this chatter, what is a chatter driven development?
[00:41:12] SPEAKER_00: I had a, no, this is a really good idea,
[00:41:14] SPEAKER_00: but it reminds me I had John G, Don G on the podcast,
[00:41:17] SPEAKER_00: CT of block.
[00:41:18] And they have this product called Goose,
[00:41:20] SPEAKER_00: which is their own internal agent thing.
[00:41:23] SPEAKER_00: And he talked about an engineer at block,
[00:41:26] SPEAKER_00: just has Goose watch him with like his screen
[00:41:31] SPEAKER_00: and listens to every meeting.
[00:41:32] SPEAKER_00: And proactively does work that he should probably want to do.
[00:41:37] SPEAKER_00: So ships a PR sends an email,
[00:41:38] SPEAKER_00: drafts a Slack message.
[00:41:40] SPEAKER_00: So he's doing exactly what you're describing
[00:41:43] SPEAKER_00: in kind of a very early way.
[00:41:45] SPEAKER_00: Yeah, that's super interesting.
[00:41:46] SPEAKER_01: And you know, I vet you the,
[00:41:48] SPEAKER_01: so if we go, if we want to ask them what the bottleneck
[00:41:51] SPEAKER_01: to that productivity is, did they share what it is?
[00:41:54] SPEAKER_01: Probably looking at it,
[00:41:55] SPEAKER_01: just making sure this is the right thing to do.
[00:41:57] SPEAKER_01: Yeah.
[00:41:58] Yeah.
[00:41:59] SPEAKER_01: So like we see this now,
[00:41:59] SPEAKER_01: like we have a Slack integration for Codex.
[00:42:01] SPEAKER_01: People love, you know, if there's like something
[00:42:03] SPEAKER_01: that you need to do quickly,
[00:42:04] SPEAKER_01: people will just like,
[00:42:05] SPEAKER_01: at mentioned Codex,
[00:42:06] SPEAKER_01: like why do you think this bug is happening, right?
[00:42:08] SPEAKER_01: Doesn't have to be an engineer,
[00:42:08] SPEAKER_01: even like maybe data scientists often hear
[00:42:11] SPEAKER_01: or using Codex ton to just like answer questions.
[00:42:13] SPEAKER_01: Like why do you think this metric moved?
[00:42:15] SPEAKER_01: What happened?
[00:42:16] SPEAKER_01: So questions, you know,
[00:42:17] SPEAKER_01: you get the answer right back in Slack.
[00:42:19] SPEAKER_01: It's amazing, super useful.
[00:42:21] SPEAKER_01: But as for when it's what writing code,
[00:42:23] then you have to go back and look at the code, right?
[00:42:25] SPEAKER_01: And so the real like,
[00:42:27] I think bottleneck right now is like validating
[00:42:30] SPEAKER_01: that the code worked and like writing code review.
[00:42:33] So in my mind,
[00:42:34] SPEAKER_01: if we wanted to get to something like, you know,
[00:42:36] SPEAKER_01: that a friend you were talking about,
[00:42:38] SPEAKER_01: I think we really need to figure out how to get people
[00:42:41] SPEAKER_01: to configure their coding agents
[00:42:43] SPEAKER_01: to be much more autonomous on those later stages of work.
[00:42:46] It makes sense.
[00:42:47] SPEAKER_00: Like you said, writing code,
[00:42:48] SPEAKER_00: I used to be an engineer as an engineer for 10 years.
[00:42:50] SPEAKER_00: Really fun to write code,
[00:42:51] SPEAKER_00: really fun to just get in the fly-o build architect test.
[00:42:54] SPEAKER_00: Not so fun to look at everyone else's code
[00:42:56] SPEAKER_00: and just have to go through and be on the hook
[00:42:58] SPEAKER_00: if it is doing something dumb that's gonna take down production.
[00:43:01] SPEAKER_00: And now that building has become easier,
[00:43:03] SPEAKER_00: what I've always heard from companies
[00:43:04] SPEAKER_00: that are really at the cutting edge of this
[00:43:06] SPEAKER_00: that bottleneck is now like figuring out what to build
[00:43:08] SPEAKER_00: and then it's at the end of like, okay,
[00:43:10] SPEAKER_00: we have all this 100 PRs to review.
[00:43:12] SPEAKER_00: Who's gonna go through all that?
[00:43:14] SPEAKER_00: Right, yeah.
[00:43:16] This episode is brought to you by Gira Product Discovery.
[00:43:20] SPEAKER_00: The hardest part of building products
[00:43:21] SPEAKER_00: isn't actually building products.
[00:43:23] SPEAKER_00: It's everything else.
[00:43:24] SPEAKER_00: It's proving that the work matters,
[00:43:26] SPEAKER_00: managing stakeholders, trying to plan ahead.
[00:43:29] SPEAKER_00: Most teams spend more time reacting than learning,
[00:43:31] SPEAKER_00: chasing updates, justifying roadmaps,
[00:43:33] SPEAKER_00: and constantly unlocking work to keep things moving.
[00:43:36] SPEAKER_00: Gira Product Discovery puts you back in control.
[00:43:39] SPEAKER_00: With Gira Product Discovery,
[00:43:41] SPEAKER_00: you can capture insights and prioritize
[00:43:43] SPEAKER_00: high impact ideas.
[00:43:44] SPEAKER_00: It's flexible so it adapts to the way your team works
[00:43:47] SPEAKER_00: and helps you build a roadmap
[00:43:48] SPEAKER_00: that drives alignment, not questions.
[00:43:51] SPEAKER_00: And because it's built on Gira,
[00:43:52] SPEAKER_00: you can track ideas from strategy to delivery,
[00:43:55] SPEAKER_00: all in one place.
[00:43:57] SPEAKER_00: Less chasing, more time to think, learn,
[00:43:59] SPEAKER_00: and build the right thing.
[00:44:00] SPEAKER_00: Get Gira Product Discovery for free at
[00:44:03] SPEAKER_00: at lasian.com slash Lenny.
[00:44:06] SPEAKER_00: That's at lasian.com slash Lenny.
[00:44:08] SPEAKER_00: What is the impact of Codex been on the way you operate
[00:44:12] SPEAKER_00: as a product person as a PM?
[00:44:14] SPEAKER_00: It's clear how engineering is impacted.
[00:44:17] SPEAKER_00: Code is written for you.
[00:44:19] SPEAKER_00: What is it done to the way you operate
[00:44:21] SPEAKER_00: and the way PMs operate at OpenA?
[00:44:23] SPEAKER_00: Yeah, I mean, I think mostly I just feel like
[00:44:26] SPEAKER_01: much more empowered.
[00:44:28] I've always been more technical leaning PM.
[00:44:32] SPEAKER_01: And especially when I'm working on products for engineers,
[00:44:34] SPEAKER_01: I feel like it's necessary to dog food the product.
[00:44:37] SPEAKER_01: But even beyond that, I just feel like I can do much,
[00:44:39] SPEAKER_01: much more as a PM.
[00:44:41] SPEAKER_01: And Scott Beltsky talks about this idea
[00:44:43] SPEAKER_01: of compressing the talent stack.
[00:44:45] SPEAKER_01: I'm not sure if I'm phrased that right.
[00:44:46] SPEAKER_01: But it's basically this idea that maybe the boundaries
[00:44:49] SPEAKER_01: between these roles are a little bit less needed
[00:44:52] SPEAKER_01: than before because people can just do much more.
[00:44:55] SPEAKER_01: And every time you, someone can do more,
[00:44:57] SPEAKER_01: you can like skip one communication boundary
[00:44:59] SPEAKER_01: and make the team that much more efficient.
[00:45:03] SPEAKER_01: So I think we see it in a bunch of functions now,
[00:45:08] SPEAKER_01: but I guess since you asked about product specifically,
[00:45:11] now answering questions, much much easier.
[00:45:14] SPEAKER_01: You can just ask Codex for thoughts on that.
[00:45:17] SPEAKER_01: A lot of PM type work understanding was changing.
[00:45:20] SPEAKER_01: Again, just ask Codex for how I'm put that.
[00:45:23] SPEAKER_01: Prototyping is often faster than writing specs.
[00:45:26] SPEAKER_01: This is something that a lot of people have talked about.
[00:45:29] I think something that, I don't think it's super surprising,
[00:45:32] SPEAKER_01: but something that's slightly surprising is like,
[00:45:33] SPEAKER_01: we're mostly building Codex to write code
[00:45:37] SPEAKER_01: that's going to be deployed to production.
[00:45:39] But actually, we see a lot of throwaway code written
[00:45:41] SPEAKER_01: with Codex now.
[00:45:42] SPEAKER_01: It's kind of going back to this idea of like,
[00:45:43] SPEAKER_01: ubiquitous code.
[00:45:45] SPEAKER_01: So you'll see someone wants to do an analysis.
[00:45:49] SPEAKER_01: Like if I want to understand something, it's like, okay,
[00:45:51] SPEAKER_01: this gave Codex a bunch data,
[00:45:52] SPEAKER_01: but then ask it to build like an interactive
[00:45:53] SPEAKER_01: like date if you were for this data, right?
[00:45:55] SPEAKER_01: You, that's just like too annoying to do in the past,
[00:45:57] SPEAKER_01: but now it's just like totally worth the time
[00:45:59] SPEAKER_01: of just getting an agent to go do something.
[00:46:02] SPEAKER_01: Similarly, I've seen like some pretty cool prototypes
[00:46:05] SPEAKER_01: on our design team about like, if you want to,
[00:46:08] SPEAKER_01: well, like a designer basically wanted to build an animation,
[00:46:11] SPEAKER_01: and this is the coin animation codex,
[00:46:13] SPEAKER_01: and it was like normally it'd be too annoying
[00:46:16] SPEAKER_01: to program this animation,
[00:46:17] SPEAKER_01: so they just vibe coded a animation editor,
[00:46:20] and then they use the animation editor
[00:46:21] SPEAKER_01: to build the animation,
[00:46:22] SPEAKER_01: which they then checked into the repo.
[00:46:24] Actually our designers are,
[00:46:25] SPEAKER_01: there's a ton of acceleration there,
[00:46:26] SPEAKER_01: and like speaking of compressing the town stack,
[00:46:28] SPEAKER_01: I think our designers are very PME.
[00:46:31] So, you know, they do a ton of product work,
[00:46:34] SPEAKER_01: and like they actually have like an entire like vibe coded
[00:46:37] SPEAKER_01: sort of side prototype of the Codex app,
[00:46:40] SPEAKER_01: and so a lot of how we talk about things is like,
[00:46:42] SPEAKER_01: we'll have like a really quick jam,
[00:46:43] SPEAKER_01: because there's like 10,000 things going on,
[00:46:45] SPEAKER_01: and then the design will like go think about how this should work,
[00:46:47] SPEAKER_01: but instead of like talking about it again,
[00:46:49] SPEAKER_01: I'll just like vibe code a prototype of that,
[00:46:50] SPEAKER_01: and they're like standalone prototype.
[00:46:52] SPEAKER_01: We'll play with it if we like it,
[00:46:53] SPEAKER_01: they'll vibe code that prototype into,
[00:46:56] SPEAKER_01: or vibe engineer that prototype
[00:46:58] SPEAKER_01: into an actual PR to land,
[00:47:00] SPEAKER_01: and then depending on their comfort with the code base,
[00:47:02] SPEAKER_01: like Codex CLI's and Rust is a little harder,
[00:47:04] SPEAKER_01: maybe they'll like land it themselves,
[00:47:06] SPEAKER_01: or they'll like get close,
[00:47:07] SPEAKER_01: and then an engineer can help them like land the PR.
[00:47:10] SPEAKER_01: You know, we recently shipped the Sora Android app,
[00:47:14] SPEAKER_01: and that was one of the most sort of mind-blowing examples
[00:47:18] SPEAKER_01: of acceleration actually,
[00:47:20] SPEAKER_01: because the usage of Codex internally
[00:47:22] SPEAKER_01: and opening as obviously really, really high,
[00:47:24] SPEAKER_01: but it's been growing over the course of the year,
[00:47:27] SPEAKER_01: both in terms of like, now it's basically like
[00:47:29] SPEAKER_01: all technical staff use it,
[00:47:31] SPEAKER_01: but even like the intensity and know how
[00:47:32] SPEAKER_01: of how to make the most of coding agencies gone up by a ton.
[00:47:35] And so the Sora Android app,
[00:47:36] SPEAKER_01: like a fully new app,
[00:47:38] SPEAKER_01: we built it in 18 days.
[00:47:41] SPEAKER_01: It went from like zero to launch to employees,
[00:47:44] SPEAKER_01: and then 10 days later,
[00:47:46] SPEAKER_01: so 28 days total we went to just like GA to the public.
[00:47:50] And that was done just like with the help of Codex.
[00:47:53] So pretty insane velocity.
[00:47:55] SPEAKER_01: I would say it was like a little bit,
[00:47:58] I don't wanna say easy mode,
[00:47:59] SPEAKER_01: but there is one thing that Codex is really good at,
[00:48:02] SPEAKER_01: if you're a company that's like building software
[00:48:04] SPEAKER_01: on multiple platforms,
[00:48:05] SPEAKER_01: so you've already figured out like some of the underlying
[00:48:07] SPEAKER_01: like APIs or systems,
[00:48:09] SPEAKER_01: asking Codex to like to port things over
[00:48:12] SPEAKER_01: is really effective,
[00:48:13] SPEAKER_01: because it has like something you can go look at.
[00:48:14] SPEAKER_01: And so the engineers on that team,
[00:48:17] SPEAKER_01: we're basically having Codex go look at the iOS app,
[00:48:20] SPEAKER_01: produce plans of work that needs to be done,
[00:48:22] SPEAKER_01: and then go implement those,
[00:48:23] SPEAKER_01: and it was kind of looking at iOS and Android at the same time.
[00:48:25] SPEAKER_01: And so you know, basically it was like two weeks
[00:48:27] SPEAKER_01: to launch the employees, four weeks total, insanely fast.
[00:48:31] SPEAKER_00: What makes that even more insane
[00:48:32] SPEAKER_00: is it became the number one app in the App Store.
[00:48:36] I don't, this just boggles the mind, okay.
[00:48:38] SPEAKER_00: So, yeah, so imagine,
[00:48:40] SPEAKER_00: do you remember what app in the App Store,
[00:48:42] SPEAKER_01: with like a handful of engineers?
[00:48:45] SPEAKER_01: I think it was like two or three possibly,
[00:48:50] SPEAKER_01: in a handful of weeks, yeah.
[00:48:52] This was absurd.
[00:48:55] So, yeah, so that's a really fun example of acceleration
[00:49:01] SPEAKER_01: and then like Atlas is the other one that I think
[00:49:03] SPEAKER_01: Ben did a podcast,
[00:49:04] SPEAKER_01: the entry on Atlas,
[00:49:08] SPEAKER_01: sharing a little bit of how we built there.
[00:49:10] SPEAKER_01: Many, Atlas is actually,
[00:49:12] SPEAKER_01: I mean, it's a browser, right?
[00:49:14] SPEAKER_01: And building a browser is really hard.
[00:49:17] SPEAKER_01: And so we had to build a lot of difficult systems
[00:49:22] SPEAKER_01: in order to do that.
[00:49:23] SPEAKER_01: And basically we got to the point where that team
[00:49:26] SPEAKER_01: has a ton of power users of Codex right now.
[00:49:29] SPEAKER_01: And you know, it got to the point where they were basically,
[00:49:32] SPEAKER_01: we were talking to them about it,
[00:49:33] SPEAKER_01: because a lot of those engineers
[00:49:34] SPEAKER_01: are people I used to work with before at my startup.
[00:49:37] SPEAKER_01: And so they'd say, you know,
[00:49:38] SPEAKER_01: before this would have taken us like two to three weeks
[00:49:41] SPEAKER_01: for two to three engineers.
[00:49:43] SPEAKER_01: And now it's like one engineer one week.
[00:49:47] SPEAKER_01: So massive acceleration there as well.
[00:49:48] SPEAKER_01: And what's quite cool is that,
[00:49:51] SPEAKER_01: you know, we shipped Atlas on Mac first,
[00:49:53] SPEAKER_01: but now we're working on the Windows version.
[00:49:55] SPEAKER_01: You know, so the team now is like ramping up on Windows
[00:49:57] SPEAKER_01: and they're helping us make Codex better on Windows 2,
[00:50:00] SPEAKER_01: which is admittedly earlier,
[00:50:02] SPEAKER_01: like just the model we shipped last week
[00:50:04] SPEAKER_01: is the first model that natively understands PowerShell.
[00:50:07] SPEAKER_01: So you know, PowerShell being the native like shell language
[00:50:11] SPEAKER_01: on Windows.
[00:50:12] SPEAKER_01: So yeah, it's been really awesome to see like the whole company
[00:50:16] SPEAKER_01: getting accelerated by Codex like from.
[00:50:19] And you know, most obviously also research
[00:50:22] SPEAKER_01: and like improving how quickly we train models
[00:50:24] SPEAKER_01: and how well we do it.
[00:50:25] SPEAKER_01: And then even like design as we talked about and marketing.
[00:50:28] SPEAKER_01: Like actually we're at this point now where my product marketer
[00:50:31] SPEAKER_01: is often also making string changes
[00:50:33] SPEAKER_01: just directly from Slack or like updating docs
[00:50:35] SPEAKER_01: directly from Slack.
[00:50:37] SPEAKER_00: These are amazing examples.
[00:50:39] SPEAKER_00: You guys are living at the bleeding edge of what is possible.
[00:50:42] SPEAKER_00: And this is how other companies are gonna work.
[00:50:45] SPEAKER_00: Just shipping again, what became the number one app in the App Store
[00:50:48] SPEAKER_00: and just beloved all over the,
[00:50:49] SPEAKER_00: just like took over the, I don't know, the world for at least a week.
[00:50:53] SPEAKER_00: Built, you said, a 28 days and like, you know, 10 days,
[00:50:57] SPEAKER_00: 18 days just to get like the core of it working.
[00:51:00] SPEAKER_00: Yeah, so like 18 days we had a thing
[00:51:02] SPEAKER_00: that employees were playing with.
[00:51:03] SPEAKER_00: And then 10 days later we were out.
[00:51:05] SPEAKER_00: And you said just a couple engineers.
[00:51:07] SPEAKER_00: Yeah, two or three.
[00:51:08] SPEAKER_00: Okay, and then Atlas, you said it was, took a week to build.
[00:51:11] SPEAKER_00: No, no, no, no.
[00:51:12] SPEAKER_01: So Atlas, not the whole week,
[00:51:13] SPEAKER_01: but Atlas was like a really meany project.
[00:51:16] SPEAKER_01: Yeah.
[00:51:17] SPEAKER_01: And so I was talking to one of the engineers on Atlas
[00:51:20] SPEAKER_01: about like, you know, just how, what they use Codex for.
[00:51:23] SPEAKER_01: And it's basically like, we use Codex for absolutely everything.
[00:51:24] SPEAKER_01: I was like, okay.
[00:51:25] SPEAKER_01: Well, like, you know, how would you measure the acceleration?
[00:51:29] SPEAKER_01: So basically the answer back was previously would have taken
[00:51:32] SPEAKER_01: two to three weeks for two to three engineers.
[00:51:34] SPEAKER_01: And now it's like one engineer one week.
[00:51:36] SPEAKER_01: Do you think this eventually moves to non-engineers
[00:51:38] SPEAKER_00: doing this sort of thing?
[00:51:39] SPEAKER_00: Like does it have to be an engineer building this thing?
[00:51:41] SPEAKER_00: Could sort of build been built by a, I don't know,
[00:51:43] SPEAKER_00: a PM or a designer?
[00:51:45] SPEAKER_01: I think we will very much get to the point where,
[00:51:47] SPEAKER_01: well, basically where the boundaries are a little bit blurred,
[00:51:50] right?
[00:51:51] SPEAKER_01: Like, I think we, you're going to want someone
[00:51:53] SPEAKER_01: who's like, understands the details of what they're building,
[00:51:55] SPEAKER_01: but what details those are will evolve.
[00:51:57] SPEAKER_01: Kind of like how now like, if you're writing Swift,
[00:52:00] SPEAKER_01: you don't have to speak assembly.
[00:52:02] SPEAKER_01: You know, there's a handful of people in the world
[00:52:04] SPEAKER_01: and it's really important that they exist
[00:52:05] SPEAKER_01: and like speak assembly, maybe more than a handful, right?
[00:52:09] SPEAKER_01: But that's like a specialized function
[00:52:10] SPEAKER_01: that like most companies don't need to have.
[00:52:14] So I think we're just going to naturally see like,
[00:52:16] SPEAKER_01: an increase in layers of abstraction.
[00:52:19] SPEAKER_01: And then the cool thing is now we're entering
[00:52:21] SPEAKER_01: like the language layer of abstraction,
[00:52:22] SPEAKER_01: like natural language.
[00:52:24] And the natural language itself is really flexible, right?
[00:52:27] Like you could have engineers talking about like a plan
[00:52:30] SPEAKER_01: and then you could have engineers talking about a spec
[00:52:31] SPEAKER_01: and then you could have engineers talking about just,
[00:52:33] SPEAKER_01: you know, a product or an idea.
[00:52:35] SPEAKER_01: So I think we can also like start moving up those layers
[00:52:37] SPEAKER_01: of abstraction as well.
[00:52:39] But you know, I do think this is going to be gradual.
[00:52:42] SPEAKER_01: I don't think it's going to go off to like all of a sudden
[00:52:44] SPEAKER_01: like nobody ever writes anything
[00:52:45] SPEAKER_01: and like, you know, any code and it's just specs.
[00:52:47] SPEAKER_01: I think it's going to be much more like, okay,
[00:52:49] SPEAKER_01: we've set up our coding agent to be really good
[00:52:51] SPEAKER_01: at like previewing the build or like running tests.
[00:52:54] SPEAKER_01: Maybe that's the first part, right?
[00:52:55] SPEAKER_01: That most people have set up and say, okay, now we've set it up
[00:52:58] SPEAKER_01: so that it can like execute the build
[00:53:00] SPEAKER_01: and it can like see the results of its own changes.
[00:53:02] SPEAKER_01: But you know, we haven't yet built a good integration harness
[00:53:04] SPEAKER_01: so that it can like, in the case of Atlas,
[00:53:06] SPEAKER_01: like, by the way, I don't know if they've done any of this
[00:53:08] SPEAKER_01: or not, I think they've done a lot of this.
[00:53:09] SPEAKER_01: But you know, maybe the next stage is like,
[00:53:12] SPEAKER_01: enable it to like load a few sample pages
[00:53:14] SPEAKER_01: to see how well those work, right?
[00:53:16] SPEAKER_01: So then, okay, now we're going to like set up to that.
[00:53:18] SPEAKER_01: And I think for some time at least we're going to have humans
[00:53:20] SPEAKER_01: kind of curating like which of these connectors
[00:53:23] SPEAKER_01: or systems or components that the agent needs
[00:53:25] SPEAKER_01: to be good at talking to.
[00:53:27] SPEAKER_01: And then, you know, in the future,
[00:53:29] SPEAKER_01: there will be an even greater unlock
[00:53:30] SPEAKER_01: where codex tells you how to set it up
[00:53:32] SPEAKER_01: or maybe sets itself up in a repo.
[00:53:34] SPEAKER_01: What a wild time to be alive.
[00:53:36] SPEAKER_00: Wow, I'm curious just the second order of effects
[00:53:38] SPEAKER_00: of this sort of thing, just how quickly it is to build stuff.
[00:53:41] SPEAKER_00: What does that do?
[00:53:42] SPEAKER_00: Does that mean distribution becomes much, much more important?
[00:53:44] SPEAKER_00: Does it mean ideas are just worth a lot more?
[00:53:48] SPEAKER_00: It's interesting to think about how quick,
[00:53:50] SPEAKER_00: how that changes.
[00:53:51] SPEAKER_00: I'm curious what you think.
[00:53:52] SPEAKER_01: I still don't think ideas are worth as much as maybe
[00:53:56] a lot of people think.
[00:53:58] I think still think execution is really hard, right?
[00:54:00] SPEAKER_01: Like you can build something fast
[00:54:01] SPEAKER_01: that you still need to execute well on it.
[00:54:03] SPEAKER_01: Still needs to make sense and be a coherent thing overall.
[00:54:06] SPEAKER_01: Yeah, and distribution is massive.
[00:54:08] SPEAKER_01: Yeah, just feels like everything else is now more important.
[00:54:11] SPEAKER_00: Everything that isn't the building piece,
[00:54:12] SPEAKER_00: which is coming up in the idea,
[00:54:14] SPEAKER_00: getting to market, profit, all that kind of stuff.
[00:54:18] SPEAKER_00: Yeah, I think we might have been in this
[00:54:20] SPEAKER_01: weird temporary phase where, you know, for a while,
[00:54:24] SPEAKER_01: like you could just, it was so hard to build product
[00:54:28] SPEAKER_01: that you mostly just had to be really good at building product
[00:54:31] SPEAKER_01: and it maybe didn't matter if you had an intimate understanding
[00:54:34] SPEAKER_01: of a specific customer.
[00:54:37] SPEAKER_01: But now I think we're getting to this point where actually,
[00:54:40] SPEAKER_01: like if I could only choose one thing to understand,
[00:54:42] SPEAKER_01: it would be like really meaningful understanding
[00:54:44] SPEAKER_01: of the problems that a certain customer has.
[00:54:48] If I could only go in with one core competency.
[00:54:52] SPEAKER_01: So I think that that's ultimately still
[00:54:54] SPEAKER_01: what's gonna matter most, right?
[00:54:55] SPEAKER_01: Like if you're starting a new company today
[00:54:57] SPEAKER_01: and you have like a really good understanding
[00:55:01] SPEAKER_01: and like network of customers that are currently
[00:55:03] SPEAKER_01: underserved by AI tools, I think you're like your set, right?
[00:55:06] Whereas if you're like good at building like, you know,
[00:55:09] SPEAKER_01: websites, but you don't have any specific customer to build for,
[00:55:12] SPEAKER_01: I think you're in for a much harder time.
[00:55:14] SPEAKER_00: Bullish on vertical AI startups is what I'm hearing.
[00:55:17] SPEAKER_00: Yeah, I could be like, there's like, you know,
[00:55:20] SPEAKER_00: there's like the general thing that can solve a lot of problems
[00:55:22] SPEAKER_00: and then there's like, we're gonna solve presentations
[00:55:24] SPEAKER_00: incredibly well and we're gonna understand the presentation
[00:55:26] SPEAKER_00: of a problem better than anyone and we're gonna
[00:55:28] SPEAKER_00: play into your workflows and in all these other things
[00:55:32] SPEAKER_00: that matter for a very specific problem.
[00:55:34] SPEAKER_00: Okay, incredible.
[00:55:36] SPEAKER_00: When you think about progress on codex,
[00:55:39] SPEAKER_00: I imagine you have a bunch of e-dails
[00:55:40] SPEAKER_00: and there's all these public benchmarks.
[00:55:42] SPEAKER_00: What's something you look at that tell you, okay,
[00:55:44] SPEAKER_00: we're making really good progress.
[00:55:46] SPEAKER_00: I imagine it's not gonna be the one thing,
[00:55:47] SPEAKER_00: but what do you focus on?
[00:55:48] SPEAKER_00: What's like something you're trying to push?
[00:55:49] SPEAKER_00: What's like a KPI or two?
[00:55:51] SPEAKER_01: One of the things that I'm constantly reminding myself of
[00:55:54] SPEAKER_01: is that a tool like codex sort of naturally
[00:55:57] SPEAKER_01: is a tool that you would become a power user of, right?
[00:56:00] SPEAKER_01: And so we can accidentally spend a lot of our time
[00:56:02] SPEAKER_01: thinking about features that are like very deep
[00:56:04] SPEAKER_01: in the user adoption journey.
[00:56:06] And so we can kind of end up over solving for that.
[00:56:10] SPEAKER_01: And so I think it's like just critically important
[00:56:11] SPEAKER_01: to like go look at like your like D7 retention, right?
[00:56:15] SPEAKER_01: Just go try the product, like sign up from scratch again.
[00:56:18] I have a few too many like chat to PT pro accounts
[00:56:20] SPEAKER_01: that I've just like, you know,
[00:56:22] where it's a maximally correctly dog food,
[00:56:24] SPEAKER_01: like sign up for my Gmail,
[00:56:25] SPEAKER_01: and they charge me like 200 bucks a month
[00:56:27] SPEAKER_01: and you need to expense those.
[00:56:28] SPEAKER_01: But you know, like I think just like the feeling
[00:56:33] SPEAKER_01: of being a user and the early retention stats
[00:56:35] SPEAKER_01: are still like super important for us
[00:56:37] SPEAKER_01: because you know, as much as this category is taking off,
[00:56:40] SPEAKER_01: I think we're still in the very everyday's
[00:56:42] SPEAKER_01: like people using them.
[00:56:44] Another thing that we do that might be,
[00:56:48] SPEAKER_01: I think we might be the most like user feedback slash
[00:56:52] SPEAKER_01: social media, PELF team out there in this space.
[00:56:55] SPEAKER_01: It's like a few of us are like constantly on Reddit
[00:56:58] SPEAKER_01: and Twitter and you know, there's a,
[00:57:01] SPEAKER_01: there's praise up there and there's a lot of complaints
[00:57:03] SPEAKER_01: but we take the complaints like very seriously
[00:57:05] SPEAKER_01: and look at them.
[00:57:06] SPEAKER_01: And I think that again, because you can use like coding
[00:57:09] SPEAKER_01: eating for so many different things,
[00:57:11] SPEAKER_01: it often is like kind of broken in many sort of ways
[00:57:14] SPEAKER_01: for like specific behaviors.
[00:57:16] SPEAKER_01: And so we actually monitor a lot just like what the vibes are
[00:57:19] SPEAKER_01: on social media pretty often, especially,
[00:57:22] I think for Twitter X, it's a little bit more hypey
[00:57:28] SPEAKER_01: and then Reddit is a little more negative but real actually.
[00:57:33] SPEAKER_01: So I've started increasingly paying attention to like
[00:57:36] SPEAKER_01: how people are talking about using Codex on Reddit actually.
[00:57:39] This is important for people to know
[00:57:40] SPEAKER_00: which the subreddits do you check most?
[00:57:42] SPEAKER_00: Is there like in our codex or?
[00:57:44] SPEAKER_00: I mean, the algorithm's pretty good at surf things stuff
[00:57:46] SPEAKER_01: but like our slash codex is there.
[00:57:48] SPEAKER_00: Okay, I'll take very interesting.
[00:57:51] SPEAKER_00: And then people tag on Twitter, you still see that
[00:57:53] SPEAKER_00: but maybe not as powerful as seeing it on Reddit.
[00:57:56] Well, yeah, and the interesting,
[00:57:57] SPEAKER_01: well the thing with Twitter is it's a little bit more one-to-one
[00:57:59] SPEAKER_01: even if it's like in public, whereas like with Reddit
[00:58:01] SPEAKER_01: there's like really good uprooting mechanics
[00:58:02] SPEAKER_01: and like maybe most people are still not pots unclear.
[00:58:06] So you get like good signal on what matters
[00:58:08] SPEAKER_01: and what other people think.
[00:58:09] SPEAKER_01: So interestingly, Atlas, I wanna talk about that briefly.
[00:58:13] SPEAKER_00: You guys launched Atlas.
[00:58:15] SPEAKER_00: I tweeted actually that I tried Atlas
[00:58:17] SPEAKER_00: and then I don't love the AI only search experience
[00:58:22] SPEAKER_00: as just like, I just want Google sometimes
[00:58:24] SPEAKER_00: or whatever, like just waiting for AI
[00:58:25] SPEAKER_00: to give me an answer.
[00:58:26] SPEAKER_00: I'm like, I don't want it.
[00:58:27] SPEAKER_00: And there was no way to switch.
[00:58:28] SPEAKER_00: So I just tweeted, I am, I'm switching back at on.
[00:58:30] SPEAKER_00: It's not great.
[00:58:31] SPEAKER_00: And I feel like I made some PMs that open AI sad
[00:58:33] SPEAKER_00: and I saw someone tweet, okay, we have this now,
[00:58:36] SPEAKER_00: which I imagine was always part of the plan.
[00:58:38] SPEAKER_00: It's probably an example of we just ship,
[00:58:39] SPEAKER_00: we got to ship stuff, see how people use it
[00:58:41] SPEAKER_00: and then we figured out.
[00:58:43] SPEAKER_00: So I guess one is that, I don't know, is there anything there?
[00:58:46] SPEAKER_00: And two, I'm just curious,
[00:58:46] SPEAKER_00: why are you guys building a web browser?
[00:58:48] SPEAKER_00: So I worked on Atlas for a bit.
[00:58:50] SPEAKER_01: I don't work on it now.
[00:58:52] SPEAKER_01: But, you know, like the,
[00:58:54] SPEAKER_01: a bit of the narrative here for me
[00:58:56] SPEAKER_01: to tell my sort of bit was like,
[00:58:57] SPEAKER_01: I was working on this like screen sharing,
[00:58:59] SPEAKER_01: like pair programming, start up, right?
[00:59:01] SPEAKER_01: And then we joined OpenAI.
[00:59:03] SPEAKER_01: And so the idea was really to build a contextual
[00:59:05] SPEAKER_01: desktop assistant.
[00:59:06] SPEAKER_01: And the reason I believe that's so important
[00:59:08] SPEAKER_01: is because I think that it's really annoying
[00:59:12] SPEAKER_01: to have to give all your context to an assistant
[00:59:13] SPEAKER_01: and then to figure out how it can help you, right?
[00:59:16] And so if it could just like understand
[00:59:18] SPEAKER_01: what you were trying to do,
[00:59:19] SPEAKER_01: then it could maximally accelerate you.
[00:59:21] And so I would, you know,
[00:59:23] SPEAKER_01: I still think of Codex actually
[00:59:25] SPEAKER_01: as like a contextual assistant
[00:59:27] SPEAKER_01: from a little bit of a different angle,
[00:59:28] SPEAKER_01: like starting with coding tasks.
[00:59:30] SPEAKER_01: But the, some of the,
[00:59:34] SPEAKER_01: some of the thinking at least for me personally,
[00:59:35] SPEAKER_01: I can't speak for the whole product,
[00:59:37] SPEAKER_01: but was that a lot of work is done in the web.
[00:59:41] SPEAKER_01: And if we could build a browser,
[00:59:43] SPEAKER_01: then we could be contextual for you.
[00:59:44] SPEAKER_01: But in a much more first class way,
[00:59:46] SPEAKER_01: we weren't hacking like other desktop software,
[00:59:48] SPEAKER_01: which have like very, very support
[00:59:50] SPEAKER_01: for like what content they're rendering
[00:59:52] SPEAKER_01: can the accessibility tree.
[00:59:54] SPEAKER_01: We wouldn't be relying on screenshots,
[00:59:55] SPEAKER_01: which are a little bit slower and unreliable.
[00:59:58] Instead we could like be in the rendering engine, right?
[01:00:01] SPEAKER_01: And like extract whatever we needed to to help you.
[01:00:05] SPEAKER_01: And also I like to think of like, you know,
[01:00:07] SPEAKER_01: in video games like, I don't know if you've played,
[01:00:09] SPEAKER_01: like I don't know, say Halo, right?
[01:00:11] SPEAKER_01: Like you walk up to an object.
[01:00:13] SPEAKER_01: I mean, this is true for many games.
[01:00:14] SPEAKER_01: You press, man, it's been a long time.
[01:00:15] SPEAKER_01: This is embarrassing.
[01:00:16] SPEAKER_01: Press X.
[01:00:19] SPEAKER_01: And it just the right thing, right?
[01:00:21] SPEAKER_01: And I was one of those guys who always read
[01:00:22] SPEAKER_01: the instruction manual for every video game that I bought.
[01:00:24] SPEAKER_01: Now, I remember the first time I read about a contextual
[01:00:26] SPEAKER_01: action and I just thought it was like this really cool idea.
[01:00:28] SPEAKER_01: And you know, the thing about a contextual action
[01:00:32] SPEAKER_01: is we need to know what you are attempting to do.
[01:00:35] SPEAKER_01: We have a little bit of context and then we can help.
[01:00:39] SPEAKER_01: And I think this is critically important
[01:00:41] SPEAKER_01: because imagine this world that we reach, right?
[01:00:43] SPEAKER_01: Where we have agents that are helping you
[01:00:45] SPEAKER_01: thousands of times per day.
[01:00:49] SPEAKER_01: Imagine if the only way we could tell you that we helped you
[01:00:51] SPEAKER_01: was if we could like push, notify you.
[01:00:54] So you get a thousand push notifications a day
[01:00:57] SPEAKER_01: of an AI saying like, hey, I did this thing.
[01:00:58] SPEAKER_01: Do you like it?
[01:00:59] SPEAKER_01: It'd be super annoying, right?
[01:01:01] SPEAKER_01: Whereas imagine going back to software engineering,
[01:01:03] SPEAKER_01: like I was looking at a dashboard
[01:01:05] SPEAKER_01: and I noticed some like key metric had like gone down.
[01:01:09] And you know, at that point in time,
[01:01:11] SPEAKER_01: and then I could like maybe go take a look
[01:01:13] SPEAKER_01: and then surface the fact that it has an opinion
[01:01:15] SPEAKER_01: on why this metric went down and maybe it fixed
[01:01:17] SPEAKER_01: right there, right when I'm looking at the dashboard, right?
[01:01:20] SPEAKER_01: That would be like, that would much more keep me in flow
[01:01:23] SPEAKER_01: and enable the agents take action on like many more things.
[01:01:26] SPEAKER_01: So in my mind, like, part of why I'm excited for us
[01:01:29] SPEAKER_01: to have a browser is that I think we have
[01:01:32] SPEAKER_01: then like much more context around like what we should help with.
[01:01:36] SPEAKER_01: Users have much more control over what they want us
[01:01:39] SPEAKER_01: to look at.
[01:01:40] SPEAKER_01: It's like, hey, if you want to open,
[01:01:41] SPEAKER_01: if you want us to like take action on something,
[01:01:42] SPEAKER_01: you can open it in your AI browser,
[01:01:43] SPEAKER_01: if you don't, then you can open it in your other browser, right?
[01:01:46] SPEAKER_01: So like really clear control and boundaries.
[01:01:48] SPEAKER_01: And then we have the ability to build you
[01:01:50] SPEAKER_01: exits like mixed initiatives so that we can surface
[01:01:53] SPEAKER_01: contextual actions to you like at the time that they're helpful
[01:01:56] SPEAKER_01: as opposed to just like randomly notifying you.
[01:01:58] SPEAKER_01: Hearing the vision for codecs being the super assistant,
[01:02:00] SPEAKER_00: it's not just there to code for you.
[01:02:02] SPEAKER_00: It's trying to do a lot for you as a teammate
[01:02:04] SPEAKER_00: as this kind of super teammate.
[01:02:06] SPEAKER_00: That makes you awesome at work.
[01:02:08] SPEAKER_00: So I get this.
[01:02:10] SPEAKER_00: Speaking of that, are there other non-engineering
[01:02:13] SPEAKER_00: common use cases for codecs?
[01:02:15] SPEAKER_00: Just ways that non-engineers, we talked about designers
[01:02:17] SPEAKER_00: for typing and building stuff.
[01:02:19] SPEAKER_00: Are there any kind of fun or unexpected ways
[01:02:21] SPEAKER_00: people are using codecs that aren't engineers?
[01:02:24] SPEAKER_00: I mean, there's a load of unexpected ways,
[01:02:26] SPEAKER_01: but I think like most of what we're seeing like
[01:02:30] SPEAKER_01: real attraction with people using things are still for now,
[01:02:32] SPEAKER_01: like very like I would say coding in JSON
[01:02:36] SPEAKER_01: or like sort of tech oriented places where there's like
[01:02:39] SPEAKER_01: a mature ecosystem or maybe you're doing data analysis
[01:02:43] SPEAKER_01: or something like that.
[01:02:44] SPEAKER_01: I personally am expecting that we're going to see
[01:02:47] SPEAKER_01: a lot more of that over time, but for now,
[01:02:50] SPEAKER_01: we're keeping the team very focused on just coding for now
[01:02:52] SPEAKER_01: because there's so much more work to do.
[01:02:54] SPEAKER_00: For people that are thinking about trying out codecs,
[01:02:56] SPEAKER_00: is there like, does it work for all kinds of code bases?
[01:03:00] SPEAKER_00: What code does it support if you're like,
[01:03:02] SPEAKER_00: I don't know it, SAP, can you add codecs and start building
[01:03:06] SPEAKER_00: things, what's kind of like the sweet spot
[01:03:08] SPEAKER_00: where does it start to not be amazing yet?
[01:03:11] SPEAKER_00: This is, I'm really glad you asked this question actually
[01:03:13] SPEAKER_01: because the best way to try codecs is to give it
[01:03:15] SPEAKER_01: your hardest tasks, which is a little different
[01:03:19] SPEAKER_01: than some of the other coding agents.
[01:03:20] SPEAKER_01: Like, some tools you might think,
[01:03:23] SPEAKER_01: okay, let me start easy or just like vibe code something
[01:03:26] SPEAKER_01: random and decide if I like the tool.
[01:03:29] SPEAKER_01: Whereas, we're really building codecs
[01:03:31] SPEAKER_01: to be the professional tool that you can give
[01:03:33] SPEAKER_01: your hardest problems to.
[01:03:36] And that writes high quality code in your enormous code base
[01:03:39] SPEAKER_01: that is in fact not perfect right now.
[01:03:42] So yeah, I think if you're going to try codecs,
[01:03:43] SPEAKER_01: you want to try it on a real task that you have
[01:03:47] and not necessarily dumb that task down to something
[01:03:49] SPEAKER_01: that's trivial, but actually a good one would be
[01:03:54] SPEAKER_01: you have a hard bug and you don't know what's causing
[01:03:56] SPEAKER_01: that bug and you ask codecs to help figure that out.
[01:03:58] SPEAKER_01: Or like, to implement that, you know, the fix.
[01:04:00] SPEAKER_01: And I love that answer.
[01:04:01] SPEAKER_01: Just give it to your hardest problem.
[01:04:03] SPEAKER_01: I will say like, you know, if you're like,
[01:04:04] SPEAKER_01: hey, okay, well, the hardest problem I have
[01:04:06] SPEAKER_01: is that I need to build like a new unicorn business.
[01:04:08] SPEAKER_01: Like, obviously, you know, it's not going to work.
[01:04:12] SPEAKER_01: Not yet.
[01:04:12] SPEAKER_01: So I think it's like, give it like the hardest problem
[01:04:16] SPEAKER_01: but something that is still like one question, right?
[01:04:20] SPEAKER_01: Or one task to start.
[01:04:22] SPEAKER_01: That's if you're testing and then over time,
[01:04:23] SPEAKER_01: you can learn how to use it for like bigger things.
[01:04:25] SPEAKER_01: Yeah, what language does it support?
[01:04:27] SPEAKER_01: Basically, the way we've trained codecs is like,
[01:04:29] SPEAKER_01: there's a distribution of languages that we support
[01:04:31] SPEAKER_01: and it's like fairly aligned with like the frequency
[01:04:34] SPEAKER_01: of these languages in the world.
[01:04:35] SPEAKER_01: So unless you're writing some like very esoteric language
[01:04:38] SPEAKER_01: or like some private language,
[01:04:39] SPEAKER_01: it should do fine in your language.
[01:04:41] If someone was just getting started,
[01:04:43] is there a tip you could share to help them be successful?
[01:04:45] SPEAKER_00: Like, if you could just whisper a little tip
[01:04:47] SPEAKER_00: into someone just setting up codecs for the first time
[01:04:50] SPEAKER_00: to help them have a really good time,
[01:04:52] SPEAKER_00: what's something you'd whisper?
[01:04:54] SPEAKER_01: I might say try a few things in parallel, right?
[01:04:57] SPEAKER_01: So you could try giving it a hard task.
[01:05:00] Maybe ask it to understand the codebase,
[01:05:03] SPEAKER_01: formulate a plan with it around an idea that you have
[01:05:06] SPEAKER_01: and kind of build your way up from there.
[01:05:07] SPEAKER_01: And like sort of the meta idea here is it's again,
[01:05:10] SPEAKER_01: it's like you're building trust with a new teammate, right?
[01:05:14] SPEAKER_01: And so like you wouldn't go to a new teammate
[01:05:15] SPEAKER_01: and just give them like, hey, do this thing.
[01:05:17] SPEAKER_01: Here's the real context.
[01:05:18] SPEAKER_01: You would start by like first making sure they understand
[01:05:21] SPEAKER_01: the codebase and then you would like maybe align
[01:05:23] SPEAKER_01: on a plan approach and then you would have them
[01:05:24] SPEAKER_01: go off and do bit by bit, right?
[01:05:26] And I think if you use codecs in that way,
[01:05:28] SPEAKER_01: you'll just sort of naturally start to understand
[01:05:29] SPEAKER_01: like the different ways of prompting it
[01:05:30] SPEAKER_01: because it is a super powerful like agent and model,
[01:05:34] SPEAKER_01: but it is a little bit different to prompt codecs
[01:05:37] SPEAKER_01: in other models.
[01:05:38] Just a couple more questions.
[01:05:39] SPEAKER_00: One, we'll touch on this a little bit.
[01:05:42] As AI does more and more coding,
[01:05:45] SPEAKER_00: there's always this question,
[01:05:46] SPEAKER_00: if should I learn to code and what should I spend time
[01:05:48] SPEAKER_00: doing this sort of thing?
[01:05:50] SPEAKER_00: For people that are trying to figure out
[01:05:52] SPEAKER_00: what to do with their career, especially if they're
[01:05:53] SPEAKER_00: in to software engineering computer science,
[01:05:56] SPEAKER_00: do you think there's specific elements of computer science
[01:05:59] SPEAKER_00: that are more and more important to lean into?
[01:06:02] SPEAKER_00: Maybe things they don't need to worry about.
[01:06:03] SPEAKER_00: Like what do you think people should be leaning
[01:06:05] SPEAKER_00: into skill-wise as this becomes more and more
[01:06:08] SPEAKER_00: but thing in our workplace?
[01:06:11] I think there's like a couple angles
[01:06:13] you could go at this from.
[01:06:16] SPEAKER_01: I think the, well, the easiest one to think of at least
[01:06:20] SPEAKER_01: is just like be a doer of things.
[01:06:24] SPEAKER_01: I think that with coding agents,
[01:06:27] SPEAKER_01: getting better and better over time,
[01:06:28] SPEAKER_01: it's just what you can do as even someone in college
[01:06:33] SPEAKER_01: or a new grad is just so much more than what that was before.
[01:06:36] SPEAKER_01: And so I think you just want to be taking advantage of that.
[01:06:39] SPEAKER_01: And it definitely when I'm looking at
[01:06:41] SPEAKER_01: high-end folks who are earlier career,
[01:06:42] SPEAKER_01: it's definitely something that I think about as how productive
[01:06:46] are they using the latest tools.
[01:06:48] They should be super productive.
[01:06:50] SPEAKER_01: And if you think of it in that way,
[01:06:51] SPEAKER_01: they actually have less of a handicap than before
[01:06:54] SPEAKER_01: versus a more senior career person
[01:06:56] SPEAKER_01: because the divide is actually getting smaller
[01:06:58] SPEAKER_01: because they've got these amazing coding agents now.
[01:07:01] SPEAKER_01: So that's one thing, which is like,
[01:07:02] SPEAKER_01: I guess the thing the advice is just like,
[01:07:05] learn about whatever you want
[01:07:06] SPEAKER_01: but just make sure you spend time doing things
[01:07:07] SPEAKER_01: not just like fulfilling homework assignments, I guess.
[01:07:11] SPEAKER_01: I think the other side of it though is that
[01:07:13] SPEAKER_01: it's still deeply worth understanding
[01:07:16] SPEAKER_01: like what makes a good overall software system.
[01:07:20] SPEAKER_01: So I still think that skills like really strong systems
[01:07:23] SPEAKER_01: engineering skills or even like really effective
[01:07:27] SPEAKER_01: like communication and collaboration with your team.
[01:07:29] SPEAKER_01: It goes like that I think are important
[01:07:31] SPEAKER_01: or I mean continue to matter for quite some time.
[01:07:34] SPEAKER_01: Like I don't think it's gonna be like
[01:07:36] SPEAKER_01: all of a sudden the AI coding agents
[01:07:39] SPEAKER_01: are just able to build like perfect systems without your help.
[01:07:42] SPEAKER_01: I think it's gonna look much more gradual where it's like,
[01:07:46] okay we have these AI coding agents,
[01:07:48] SPEAKER_01: they're able to validate their work.
[01:07:50] SPEAKER_01: It's still important and like for example,
[01:07:52] SPEAKER_01: like I'm thinking of an engineer who was working on Atlas
[01:07:54] SPEAKER_01: since we were talking about it.
[01:07:56] SPEAKER_01: He set up codex that I can like verify its own work
[01:07:58] SPEAKER_01: which is a little bit non trivial
[01:08:00] SPEAKER_01: because of the nature of the Alice project.
[01:08:01] SPEAKER_01: So the way that he did that was he actually prompted codex
[01:08:03] SPEAKER_01: like, hey, why can't you verify your work, fix it
[01:08:06] SPEAKER_01: and like did that on a loop, right?
[01:08:08] SPEAKER_01: And so you still like at various phases
[01:08:11] SPEAKER_01: are gonna want a human in the loop
[01:08:12] SPEAKER_01: to like help configure the coding agent to be effective.
[01:08:16] SPEAKER_01: And so I think like you still want to be able
[01:08:18] SPEAKER_01: to reason about that.
[01:08:19] SPEAKER_01: So maybe it's like less important
[01:08:20] SPEAKER_01: that you can like type really fast
[01:08:23] SPEAKER_01: and like you understand exactly how to write
[01:08:25] SPEAKER_01: not that anyone writes a four each loop or something, right?
[01:08:28] SPEAKER_01: But it is, or you know,
[01:08:30] SPEAKER_01: you don't need to not implement like a specific algorithm
[01:08:32] SPEAKER_01: but I think you need to be able to reason
[01:08:33] SPEAKER_01: about the different systems
[01:08:34] SPEAKER_01: and like what makes like effective.
[01:08:36] SPEAKER_01: A software engineering team effective.
[01:08:38] SPEAKER_01: So I think that's the other really important thing.
[01:08:40] SPEAKER_01: And then like maybe the last angle that you could take is,
[01:08:43] I think if you're on the frontier of knowledge
[01:08:46] SPEAKER_01: for a given thing, I still think that's like
[01:08:48] SPEAKER_01: deeply interesting to go down.
[01:08:49] SPEAKER_01: Partially because that knowledge is still gonna be like,
[01:08:55] you know, agents are gonna be as good of that.
[01:08:57] SPEAKER_01: But also partially because I think that like by trying
[01:08:59] SPEAKER_01: to advance the frontier of a specific thing
[01:09:00] SPEAKER_01: you'll actually like end up like being forced
[01:09:03] SPEAKER_01: to take advantage of coding agents
[01:09:05] SPEAKER_01: and like using them to accelerate your own workflow.
[01:09:09] What's an example that when you're when you talk about
[01:09:10] SPEAKER_00: being at the frontier or some codex writes a lot of the code
[01:09:13] SPEAKER_01: that helps like manage its training runs,
[01:09:15] SPEAKER_01: the key infrastructure, you know, we move pretty fast
[01:09:19] SPEAKER_01: and so we have a codex code review
[01:09:21] SPEAKER_01: is like catching a lot of mistakes.
[01:09:23] SPEAKER_01: It's actually caught some like pretty interesting
[01:09:24] SPEAKER_01: configuration mistakes.
[01:09:26] SPEAKER_01: And you know, we're starting to see glimpses of the future
[01:09:28] SPEAKER_01: where we're actually starting to have codex
[01:09:31] SPEAKER_01: even like the on call for its own training,
[01:09:34] SPEAKER_01: which is pretty interesting.
[01:09:36] SPEAKER_01: So there's lots there.
[01:09:38] SPEAKER_00: Wait, what does that mean to be on call for its own training?
[01:09:39] SPEAKER_00: So it's running its training and it's like,
[01:09:41] SPEAKER_00: oh, something broke, someone needs,
[01:09:43] SPEAKER_00: and it does it like alert people, it's like here
[01:09:45] SPEAKER_00: and we're gonna fix the problem and restart.
[01:09:47] SPEAKER_01: This is an early idea that we're like figuring out.
[01:09:49] SPEAKER_01: But the basic idea is that during a training run,
[01:09:52] SPEAKER_01: there's like a bunch of graphs that like today,
[01:09:53] SPEAKER_01: like humans are looking at it
[01:09:54] SPEAKER_01: and it's like really important to like look at those.
[01:09:57] We call this babysitting because it's very expensive
[01:10:00] SPEAKER_01: to train, I imagine, and very important to move fast.
[01:10:02] SPEAKER_01: Exactly.
[01:10:03] SPEAKER_01: And there's a lot of, there's a lot of systems underlying
[01:10:06] SPEAKER_01: the training run and so like a system could go down
[01:10:08] SPEAKER_01: or there could be an error somewhere that gets introduced.
[01:10:10] SPEAKER_01: And so we might need to like fix it or pause things
[01:10:13] SPEAKER_01: or I don't know, there's lots of actions we might need to take.
[01:10:15] SPEAKER_01: And so basically having codex like run on a loop
[01:10:18] SPEAKER_01: to like evaluate how those charts are moving over time,
[01:10:22] SPEAKER_01: this sort of this idea that we have to like how to enable us
[01:10:24] SPEAKER_01: to like train like way more efficiently.
[01:10:26] SPEAKER_01: I love that.
[01:10:27] SPEAKER_00: And this is very much along the lines of,
[01:10:28] SPEAKER_00: this is the future of agents.
[01:10:30] SPEAKER_00: It's codex isn't just for building code and red,
[01:10:32] SPEAKER_00: it's a lot more than that.
[01:10:34] SPEAKER_00: Yeah.
[01:10:36] SPEAKER_00: Okay, last question.
[01:10:37] SPEAKER_00: Being at OpenAI, I can't not ask about your AGI timeline
[01:10:42] SPEAKER_00: and how far you think we are from AGI.
[01:10:44] SPEAKER_00: I know this isn't what you were come,
[01:10:45] SPEAKER_00: but there's a lot of opinions, a lot of, I don't know,
[01:10:48] SPEAKER_00: timelines.
[01:10:50] SPEAKER_00: How far do you think we are from a humanly human version
[01:10:54] SPEAKER_00: of AI, whatever that means to you?
[01:10:56] SPEAKER_01: For me, I think that it's a little bit about like
[01:11:00] SPEAKER_01: when do we see the acceleration curves kind of go like this
[01:11:02] SPEAKER_01: or I don't know which way I'm mirrored here, right?
[01:11:04] SPEAKER_01: When do we see the hockey stick?
[01:11:06] SPEAKER_01: And I think that the current limiting factor,
[01:11:09] SPEAKER_01: I mean, there's many, but I think a current
[01:11:11] SPEAKER_01: underappreciated limiting factor is like literally human
[01:11:13] SPEAKER_01: typing speed or human multitasking speed
[01:11:16] SPEAKER_01: unlike writing prompts, right?
[01:11:19] And like, you know, you were talking about it's like,
[01:11:20] SPEAKER_01: you can have an agent like watch all the work you're doing,
[01:11:22] SPEAKER_01: but if you don't have the agent also validating its work,
[01:11:26] then you're still bottlenecked on like,
[01:11:27] SPEAKER_01: can you go review all that code, right?
[01:11:29] SPEAKER_01: So my view is that we need to unblock those productivity
[01:11:35] SPEAKER_01: loops from like humans having a prompt
[01:11:37] SPEAKER_01: and humans having to like manually validate all the work.
[01:11:39] SPEAKER_01: And so if we can like rebuild systems to let the agent
[01:11:42] SPEAKER_01: like be default useful, we'll start unlocking hockey sticks.
[01:11:47] Unfortunately, I don't think that's gonna be binary.
[01:11:49] SPEAKER_01: I think it's gonna be very dependent on what you're building,
[01:11:51] SPEAKER_01: right? So like, I would imagine that like next year,
[01:11:53] SPEAKER_01: if you're a startup and you're building a new,
[01:11:56] SPEAKER_01: new pieces like, you know, some new app or something,
[01:11:59] it'll be possible for you to set it up on a stack
[01:12:01] SPEAKER_01: where agents are like much more self-sufficient than not,
[01:12:04] right? But now let's say, I don't know,
[01:12:06] SPEAKER_01: you mentioned SAP, right?
[01:12:07] SPEAKER_01: Let's say you work in SAP.
[01:12:09] SPEAKER_01: Like they have many like complex systems and they're not
[01:12:11] SPEAKER_01: gonna be able to just like get the agent to be
[01:12:12] SPEAKER_01: self-sufficient overnight in those systems.
[01:12:15] SPEAKER_01: So they're gonna have to slowly like maybe replace systems
[01:12:17] SPEAKER_01: or update systems to allow the agent to like,
[01:12:20] SPEAKER_01: handle more of the work and to end.
[01:12:22] SPEAKER_01: And so basically my sort of long answer to your question,
[01:12:25] SPEAKER_01: maybe boring answer is that I think starting next year,
[01:12:28] SPEAKER_01: we're gonna see like early adopters,
[01:12:30] SPEAKER_01: like starting to like hockey stick their productivity.
[01:12:33] And then over the years that follow,
[01:12:34] SPEAKER_01: we're gonna see larger and larger companies like hockey stick
[01:12:37] SPEAKER_01: and that productivity.
[01:12:38] SPEAKER_01: And then somewhere in that fuzzy middle is like when
[01:12:41] SPEAKER_01: that hockey sticking will be like flowing back
[01:12:44] SPEAKER_01: into the AI labs and that's when we'll basically be
[01:12:47] SPEAKER_01: at the AGI tier.
[01:12:48] SPEAKER_01: I love this answer.
[01:12:49] SPEAKER_00: It's very practical and it's something that comes up
[01:12:51] SPEAKER_00: a lot in this podcast, just like the time to review
[01:12:54] SPEAKER_00: all the things AI is doing is really annoying
[01:12:56] SPEAKER_00: and a big bottleneck.
[01:12:57] SPEAKER_00: I love that you're working on this because it's one thing
[01:13:00] SPEAKER_00: to just make coding much more efficient
[01:13:02] SPEAKER_00: and do that for people.
[01:13:03] SPEAKER_00: It's another to take care of that final step of vocation.
[01:13:06] SPEAKER_00: This is actually great.
[01:13:07] SPEAKER_00: And that's so interesting that your sense is
[01:13:09] SPEAKER_00: that's the limiting factor.
[01:13:11] SPEAKER_00: It comes back to your earlier point of even if AI did not
[01:13:14] SPEAKER_00: advance anymore.
[01:13:15] SPEAKER_00: We have so much more potential to unlock
[01:13:18] SPEAKER_00: if we as we learn to use it more effectively.
[01:13:22] SPEAKER_00: So that is a really unique answer.
[01:13:23] SPEAKER_00: I haven't heard that first fact on what is the big unlock.
[01:13:26] SPEAKER_00: Human typing speeds were of you basically
[01:13:28] SPEAKER_00: what AI is doing for us.
[01:13:30] SPEAKER_00: So good.
[01:13:31] SPEAKER_00: Okay, Alexander, we covered a lot of ground.
[01:13:35] SPEAKER_00: Is there anything that we haven't covered?
[01:13:37] SPEAKER_00: Is there anything you wanted to share
[01:13:38] SPEAKER_00: maybe double down on before we get
[01:13:41] SPEAKER_00: to our very exciting lightning round?
[01:13:43] SPEAKER_00: I think one thing is that the codex team is growing.
[01:13:47] And as I was just saying, we're still somewhat limited
[01:13:49] SPEAKER_01: by human thinking speed and human typing speed.
[01:13:52] SPEAKER_01: We're working on it.
[01:13:53] SPEAKER_01: So if you're an engineer or a salesperson
[01:13:58] SPEAKER_01: or I am hiring for product person, please hit us up.
[01:14:02] SPEAKER_01: I'm not sure the best way to give contact info,
[01:14:04] SPEAKER_01: but I guess you can go to our jobs page
[01:14:06] SPEAKER_01: or do they have contact for you?
[01:14:08] SPEAKER_01: Actually, do you listen to some contact for you?
[01:14:10] SPEAKER_01: Before they send me like, hey, I want to apply to codex.
[01:14:13] SPEAKER_00: I do have a contact forum at Lenny.com.
[01:14:15] SPEAKER_00: I'm afraid of all the amazing people
[01:14:17] SPEAKER_00: that are picking me, but there you go.
[01:14:19] SPEAKER_00: We could try that.
[01:14:20] SPEAKER_00: Let's see how that works.
[01:14:20] SPEAKER_00: Yeah, maybe an easier way.
[01:14:22] SPEAKER_01: We can edit all that out.
[01:14:23] SPEAKER_01: Give up up to you.
[01:14:24] SPEAKER_01: But yeah, or I would just say you can drop us a DM.
[01:14:28] SPEAKER_01: For example, I'm Enbureko on Twitter and give me up.
[01:14:31] SPEAKER_01: Like you're sitting joining the team.
[01:14:33] SPEAKER_01: What a dream job for so many people.
[01:14:35] SPEAKER_00: What to sign.
[01:14:36] SPEAKER_00: They will, I don't know.
[01:14:38] SPEAKER_00: What's like a way to filter people a little bit
[01:14:39] SPEAKER_00: so they're not letting you're in bucks.
[01:14:42] SPEAKER_00: So specifically, if you want to join the codex team,
[01:14:45] SPEAKER_01: then you need to be a technical person who uses these tools.
[01:14:49] SPEAKER_01: And I think I would just ask yourself the question,
[01:14:51] hey, let's say I work to join OpenAI and work on codex
[01:14:55] SPEAKER_01: over the next six months and crush it.
[01:14:58] SPEAKER_01: What does the life of a software engineer look like then?
[01:15:01] SPEAKER_01: And I think if you haven't paid on that,
[01:15:02] SPEAKER_01: you should apply.
[01:15:03] SPEAKER_01: And if you don't have an opinion on that
[01:15:05] SPEAKER_01: and have to think about it first.
[01:15:08] SPEAKER_01: Depending on how long you have to think about it,
[01:15:09] SPEAKER_01: I guess that would be the filter, right?
[01:15:10] SPEAKER_01: I think there's a lot of people thinking about the space.
[01:15:13] SPEAKER_01: And so we're very interested in folks who sort of have already
[01:15:18] SPEAKER_01: been thinking about what the future should look like with agents.
[01:15:22] SPEAKER_01: And we don't have to agree on where we're going.
[01:15:24] SPEAKER_01: But I think we want people who are very passionate
[01:15:26] SPEAKER_01: about the topic, I guess.
[01:15:28] It's very rare to be working on a product
[01:15:30] SPEAKER_00: that has this much impact.
[01:15:31] SPEAKER_00: And as it's such a bleeding edge of where it's possible,
[01:15:35] SPEAKER_00: it's a medical role for the right person.
[01:15:37] SPEAKER_00: So it's awesome that you have an opening
[01:15:40] SPEAKER_00: and this audience is a really good fit,
[01:15:43] SPEAKER_00: potentially for that role.
[01:15:45] SPEAKER_00: So I hope we find someone that would be incredible.
[01:15:47] SPEAKER_00: With that, we've reached our very exciting lightning round.
[01:15:50] SPEAKER_00: I've got five questions for you, Alexander.
[01:15:53] SPEAKER_00: Are you rid?
[01:15:54] I don't know what these are, but I'm excited.
[01:15:56] SPEAKER_00: Let's do it.
[01:15:57] SPEAKER_00: They're the same questions asked everyone,
[01:15:59] SPEAKER_00: except for the last one.
[01:16:01] SPEAKER_00: So probably not a surprise.
[01:16:03] SPEAKER_00: I should probably make them more often a surprise.
[01:16:07] SPEAKER_00: OK, first question.
[01:16:08] SPEAKER_00: What are a couple of books that you recommend most
[01:16:09] SPEAKER_00: to other people to or three books that come to mind?
[01:16:12] SPEAKER_00: I have been reading a lot of science fiction recently.
[01:16:16] SPEAKER_01: And I'm sure this has been recommended before, but the culture.
[01:16:20] I think it's Ian Banks, who's the name of the author.
[01:16:23] SPEAKER_01: Part of why I love it is because it's basically relatively
[01:16:27] SPEAKER_01: recent writing about a future with AI.
[01:16:30] SPEAKER_01: But it's an optimistic future with AI.
[01:16:33] And I think a lot of sci-fi is fairly dystopian.
[01:16:37] SPEAKER_01: But this is like people, sort of the joke,
[01:16:39] SPEAKER_01: at least on the culture subreddit.
[01:16:42] SPEAKER_01: Is that, let me see if I can get this right.
[01:16:44] SPEAKER_01: It is a space communist utopia.
[01:16:48] SPEAKER_01: Or I think it's a gay space communist utopia.
[01:16:52] SPEAKER_01: And I just think it's really fun to think about,
[01:16:56] SPEAKER_01: like, to use the culture as a way to think about what kind
[01:16:58] SPEAKER_01: of world can we usher in, and what decisions
[01:17:00] SPEAKER_01: can we make today to help usher in that world?
[01:17:02] Wow.
[01:17:03] SPEAKER_00: I don't think anyone's recommended that.
[01:17:04] SPEAKER_00: I know you're reading.
[01:17:05] SPEAKER_00: You mentioned before, it's the recording Lord of the Rings
[01:17:07] SPEAKER_00: right now.
[01:17:09] SPEAKER_00: If you want another AI-ish sci-fi book,
[01:17:12] SPEAKER_00: have you read Fire Upon the Deep?
[01:17:15] SPEAKER_00: No, I haven't.
[01:17:15] SPEAKER_00: OK.
[01:17:16] SPEAKER_00: It's incredibly good.
[01:17:18] SPEAKER_00: It's like a sci-fi space opera, sort of epic tale,
[01:17:22] SPEAKER_00: with super intelligence.
[01:17:25] SPEAKER_00: Cool.
[01:17:25] SPEAKER_00: Yeah.
[01:17:25] SPEAKER_00: Someone, mostly not optimistic, but somewhat optimistic.
[01:17:30] SPEAKER_00: OK.
[01:17:30] SPEAKER_00: Next question.
[01:17:30] SPEAKER_00: Is there a favorite recent movie or TV show
[01:17:34] SPEAKER_00: that you've really enjoyed?
[01:17:36] Yeah.
[01:17:36] There's an anime called Jiu Jitsu Kaizen, which I really like.
[01:17:40] SPEAKER_01: Again, it's got a slightly dark topic of demons.
[01:17:45] But what I love about it is that the hero is really nice.
[01:17:48] SPEAKER_01: And I think there's this new wave of anime and cartoons
[01:17:51] SPEAKER_01: where the protagonists are really friendly and people
[01:17:57] SPEAKER_01: who care about the world, rather than being
[01:18:00] SPEAKER_01: like, if you look at some older anime that started the genre,
[01:18:03] SPEAKER_01: there's Evangelion or Akita.
[01:18:07] SPEAKER_01: And those characters, the protagonists are deeply flawed,
[01:18:11] SPEAKER_01: quite unhappy.
[01:18:14] SPEAKER_01: They didn't start the genre, but it
[01:18:15] SPEAKER_01: was like a trend for a while to poke fun at the idea
[01:18:18] SPEAKER_01: that in these cartoons, the protagonist was very young,
[01:18:22] SPEAKER_01: but being given a ridiculous amount of responsibility
[01:18:24] SPEAKER_01: to save the world.
[01:18:26] SPEAKER_01: And so there was kind of a wave of content that
[01:18:30] SPEAKER_01: was like critiquing this by making the character
[01:18:31] SPEAKER_01: like basically go through serious mental issues
[01:18:35] SPEAKER_01: in the middle of the show.
[01:18:36] SPEAKER_01: And I'm not saying this is better,
[01:18:38] SPEAKER_01: but at least it's quite fun to have
[01:18:39] SPEAKER_01: these really positive protagonists are just
[01:18:42] SPEAKER_01: trying to help everyone around them.
[01:18:43] SPEAKER_01: I love how much we're learning about your personality
[01:18:46] SPEAKER_00: hearing these recommendations.
[01:18:49] SPEAKER_00: Nice protagonists, optimistic futures.
[01:18:52] SPEAKER_00: I think if you don't believe it, you can't
[01:18:54] SPEAKER_01: have a little bit of an inter-existence.
[01:18:55] SPEAKER_01: So you need a balance.
[01:18:57] SPEAKER_01: This is your training data.
[01:18:59] Is there a product you recently discovered
[01:19:01] SPEAKER_00: that you really love to be an app, could be some clothing,
[01:19:05] SPEAKER_00: could be some kitchen gadget, tech gadget, a hat?
[01:19:09] Yeah, so I have been quite into combustion engines
[01:19:16] SPEAKER_01: and cars.
[01:19:17] SPEAKER_01: Actually, the reason I came to America initially
[01:19:19] SPEAKER_01: was because I wanted to work on US aircraft.
[01:19:23] SPEAKER_01: Now I work in software.
[01:19:24] SPEAKER_01: And so for the longest time, I've basically only had
[01:19:28] SPEAKER_01: quite old sports cars, old just because they were more
[01:19:31] SPEAKER_01: affordable.
[01:19:33] SPEAKER_01: And then recently, we got a Tesla instead.
[01:19:38] SPEAKER_01: And I have to say that I find the Tesla software
[01:19:41] SPEAKER_01: like quite inspiring.
[01:19:43] SPEAKER_01: In particular, it has the self-driving
[01:19:45] SPEAKER_01: feature.
[01:19:45] SPEAKER_01: And I've mentioned a few times today.
[01:19:49] SPEAKER_01: I think it's really interesting to think about how to build
[01:19:51] SPEAKER_01: an extended initiative software that makes you feel
[01:19:53] SPEAKER_01: maximally empowered as a human, maximally in control,
[01:19:56] SPEAKER_01: but yet you're getting a lot of help.
[01:19:58] And I think they did a really good job
[01:20:00] SPEAKER_01: with enabling the car to drive itself.
[01:20:03] SPEAKER_01: But all these different ways that you
[01:20:05] SPEAKER_01: can adjust what it's doing without turning off the self-driving.
[01:20:08] SPEAKER_01: So you can accelerate.
[01:20:10] SPEAKER_01: It'll listen to that.
[01:20:11] SPEAKER_01: You can turn a knob to change its speed.
[01:20:13] SPEAKER_01: You can steer slightly.
[01:20:16] I think it's actually a masterclass in building an agent
[01:20:19] SPEAKER_01: that still leaves the human in control.
[01:20:21] SPEAKER_01: This reminds me, Nick Tureley's whole mantra
[01:20:23] SPEAKER_00: was, are we maximally accelerated?
[01:20:26] SPEAKER_00: Yeah.
[01:20:26] SPEAKER_00: It's completely infiltrated, everything
[01:20:28] SPEAKER_00: out of putting eye, which makes sense.
[01:20:30] SPEAKER_00: That tracks two more questions.
[01:20:33] SPEAKER_00: Do you have a life motto that you often think about,
[01:20:36] SPEAKER_00: come back to in worker and life that's been helpful?
[01:20:39] SPEAKER_00: I don't know if I have a life motto,
[01:20:41] SPEAKER_01: but maybe I can tell you about the number one company
[01:20:44] SPEAKER_01: value from my startup, which is still something that sticks
[01:20:47] SPEAKER_01: with me, which is to be kind and candid.
[01:20:51] That tracks.
[01:20:53] Kind and candid.
[01:20:54] SPEAKER_00: Wow.
[01:20:54] SPEAKER_00: Yeah.
[01:20:55] SPEAKER_01: And we had to put it together because we,
[01:20:58] SPEAKER_01: as founders, realized that we often would be nice.
[01:21:04] And it wasn't actually the right thing to do.
[01:21:07] SPEAKER_01: We would like delay the difficult conversations
[01:21:09] SPEAKER_01: and we were not candid.
[01:21:11] SPEAKER_01: And so every time we would remind ourselves of this motto,
[01:21:13] SPEAKER_01: and then we would become more candid.
[01:21:14] SPEAKER_01: And then six months later, we would realize
[01:21:16] SPEAKER_01: that we were in fact not candid six months ago.
[01:21:18] SPEAKER_01: And we needed to be even more candid.
[01:21:20] SPEAKER_01: So then the question is like, OK, how should we be candid?
[01:21:23] SPEAKER_01: It was like, OK, well, let's think of being candid
[01:21:26] SPEAKER_01: as an act of kindness, but also think of that both
[01:21:28] SPEAKER_01: in terms of doing it and willing ourselves to do it,
[01:21:30] SPEAKER_01: but also in terms of how we frame its people.
[01:21:32] SPEAKER_01: That is a beautiful way of summarizing
[01:21:35] SPEAKER_00: how to lead well.
[01:21:36] SPEAKER_00: What's the look about challenge directly,
[01:21:40] SPEAKER_00: Bricarot deeply, radical candor?
[01:21:43] SPEAKER_00: Yeah, around you.
[01:21:44] SPEAKER_00: Yeah.
[01:21:44] SPEAKER_00: Like another way of thinking about radical candor.
[01:21:46] SPEAKER_00: OK, last question.
[01:21:47] SPEAKER_00: I was looking at your last name just like, hey,
[01:21:49] SPEAKER_00: what's the story here?
[01:21:51] SPEAKER_00: So your last name is Enbira Kos.
[01:21:53] SPEAKER_00: And I was talking at JGPT.
[01:21:55] SPEAKER_00: And it told me the most famous individuals
[01:21:57] SPEAKER_00: with the surname are the influential Greek poet
[01:22:00] SPEAKER_00: and psychoanalyst Andreas Enbira Kos
[01:22:04] SPEAKER_00: and his relative, the wealthy shipping magnate
[01:22:06] SPEAKER_00: and art collector George Enbira Kos.
[01:22:09] SPEAKER_00: So the question is, which of these two
[01:22:11] SPEAKER_00: do you most identify with?
[01:22:13] SPEAKER_00: The Greek poet and psychoanalyst
[01:22:15] SPEAKER_00: or the wealthy shipping magnate and art collector?
[01:22:18] SPEAKER_00: I think it's going to have to be the poet
[01:22:20] SPEAKER_01: because he loved the island that our families from.
[01:22:27] SPEAKER_00: Where you know those city people, they OK.
[01:22:28] SPEAKER_01: This is not news to you.
[01:22:30] SPEAKER_00: Well, I mean, it's an enormous family, but it's like Greek.
[01:22:33] SPEAKER_01: So these big families, everyone's your uncle.
[01:22:36] SPEAKER_01: You know what I mean?
[01:22:37] SPEAKER_01: My mother's Malaysian and also everyone is my uncle.
[01:22:39] SPEAKER_01: Or aunt in Malaysia too, if that makes sense.
[01:22:42] SPEAKER_01: But yeah, he loved this island that the family sort
[01:22:47] SPEAKER_01: of initiated from.
[01:22:48] SPEAKER_01: I believe I don't actually know where that's shipping
[01:22:51] SPEAKER_01: magnate lived.
[01:22:51] SPEAKER_01: I think it was New York or something.
[01:22:53] SPEAKER_01: But we all came from this island called Andros,
[01:22:56] SPEAKER_01: which is a really beautiful place.
[01:22:58] SPEAKER_01: And it's like there's more like livestock there
[01:23:00] SPEAKER_01: than humans, not too many tourists go there.
[01:23:04] But I think he, like, part of what I think is really cool
[01:23:07] SPEAKER_01: is like he published a lot.
[01:23:08] SPEAKER_01: And a lot of his writing is about the beauty of that island,
[01:23:11] SPEAKER_01: which I think is super cool.
[01:23:12] SPEAKER_01: Wow, that was an amazing answer.
[01:23:14] SPEAKER_00: To more questions, work in folks fine if they want to
[01:23:16] SPEAKER_00: follow you online and maybe reach out.
[01:23:18] SPEAKER_00: And then how can listeners be useful to you?
[01:23:20] SPEAKER_00: I'm one of those people who has social media only
[01:23:22] SPEAKER_01: for the purposes of having work.
[01:23:24] SPEAKER_01: My phone turns black and white at 9 p.m. at night.
[01:23:27] SPEAKER_01: But yeah, so Twitter or X at Enbureco.
[01:23:33] SPEAKER_01: And yeah, if you post in our slash code, X,
[01:23:35] SPEAKER_01: I'll probably see it.
[01:23:37] SPEAKER_01: So you can go there.
[01:23:40] SPEAKER_01: How can listeners be useful?
[01:23:42] SPEAKER_01: I would say please try codex.
[01:23:43] SPEAKER_01: Please share feedback.
[01:23:45] SPEAKER_01: Let us know what to improve.
[01:23:46] SPEAKER_01: We pay a ton of attention to feedback.
[01:23:48] SPEAKER_01: I think it's like honestly, like the growth has been amazing,
[01:23:51] SPEAKER_01: but it's still very early times.
[01:23:54] SPEAKER_01: So we still pay a lot of attention and hope to do so forever.
[01:23:57] SPEAKER_01: And also, I would say if you're interested in working
[01:24:01] on the future of coding agents and then agents generally
[01:24:04] SPEAKER_01: then please apply to our job site and or message me
[01:24:08] SPEAKER_01: in those social media places.
[01:24:10] Alexander, this was awesome.
[01:24:11] SPEAKER_00: I always love meeting people working on AI
[01:24:14] SPEAKER_00: because it always feels like there's
[01:24:16] SPEAKER_00: very, I don't know, sterile, scary, mysterious thing.
[01:24:20] SPEAKER_00: And then you meet the people building these tools.
[01:24:22] SPEAKER_00: And they're always just so awesome.
[01:24:24] SPEAKER_00: And you especially, just so nice.
[01:24:26] SPEAKER_00: And as you, like the examples you shared, optimism and kindness,
[01:24:32] SPEAKER_00: this is what we want to be.
[01:24:34] SPEAKER_00: These are the kinds of people we want to be building.
[01:24:35] SPEAKER_00: These tools that are going to drive the future.
[01:24:37] SPEAKER_00: So I'm really thankful that you did this.
[01:24:41] SPEAKER_00: Grateful to have met you and thank you so much for being here.
[01:24:45] SPEAKER_00: Yeah, thanks so much for having me.
[01:24:46] SPEAKER_00: This is fun.
[01:24:48] Thank you so much for listening.
[01:24:50] SPEAKER_00: If you found this valuable, you can subscribe to the show
[01:24:52] SPEAKER_00: on Apple Podcasts, Spotify, or your favorite podcast app.
[01:24:56] SPEAKER_00: Also, please consider giving us a rating or a leaving review
[01:24:59] SPEAKER_00: as that really helps other listeners find the podcast.
[01:25:02] SPEAKER_00: You can find all past episodes or learn more about the show
[01:25:05] SPEAKER_00: at Lenny'spodcast.com.
[01:25:08] SPEAKER_00: See you in the next episode.