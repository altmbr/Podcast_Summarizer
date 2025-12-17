# Building AI Systems That Scale | Office Hours w/ Calvin French-Owen

**Podcast:** Theory Ventures Office Hours
**Date:** 2025-12-16
**Video ID:** zTsEmtlSeaU
**Video URL:** https://www.youtube.com/watch?v=zTsEmtlSeaU

---

[00:00:00] Welcome everybody.
[00:00:06] Tomasz Tunguz: My name is Tomasz Trincoz.
[00:00:07] Tomasz Tunguz: I'm the founder and general partner at Theory Ventures.
[00:00:10] Tomasz Tunguz: We're an early stage venture firm based in the Ferry Building in San Francisco.
[00:00:14] Tomasz Tunguz: We invest in AI companies and web three companies.
[00:00:16] Tomasz Tunguz: We've been around for about three years and are very fortunate to be investors in our
[00:00:21] Tomasz Tunguz: host company Omni here.
[00:00:23] Tomasz Tunguz: The BI company has been around for three or four years and growing very, very quickly.
[00:00:28] Tomasz Tunguz: We host these sessions that are called Office Hours where we gather luminaries from the
[00:00:32] Tomasz Tunguz: software world to talk about their lessons learned and share with our community.
[00:00:37] Tomasz Tunguz: And tonight I'm thrilled to welcome Calvin.
[00:00:41] Tomasz Tunguz: Calvin's an MIT grad.
[00:00:42] Tomasz Tunguz: He founded a company called Segment, which Trulio bought for more than three billion.
[00:00:48] Tomasz Tunguz: And then was one of the team members on OpenAI's Codex and wrote a brilliant blog post about
[00:00:54] Tomasz Tunguz: it.
[00:00:56] Tomasz Tunguz: You know, as we're all using AI differently and starting to figure out how we do manage
[00:01:00] Tomasz Tunguz: 100 agents simultaneously and how we develop software within this world.
[00:01:04] Tomasz Tunguz: Thought it'd be brilliant to hear about some of your adventures and some of your learning.
[00:01:07] Tomasz Tunguz: But maybe we can just start with, so you'd sold Segment and then you decided to join OpenAI.
[00:01:14] Tomasz Tunguz: What catalyzed that decision?
[00:01:16] Yeah.
[00:01:17] Calvin French-Owen: So at the time, I had kind of been like taking a few years off, like figuring out what I wanted
[00:01:25] Calvin French-Owen: to do next.
[00:01:26] Calvin French-Owen: And I was pretty convinced that I was going to start another startup.
[00:01:28] Calvin French-Owen: Just because I had so much fun building the first time around and we had some survivorship
[00:01:33] Calvin French-Owen: bias, I think.
[00:01:35] Calvin French-Owen: But it felt like a good reason to give it another shot.
[00:01:39] Calvin French-Owen: And so this was back in March, April of 2024.
[00:01:48] Calvin French-Owen: And I was thinking, okay, I want to start a startup.
[00:01:50] Calvin French-Owen: I feel like I should be close to AI.
[00:01:52] Calvin French-Owen: The models seem plenty capable.
[00:01:54] Calvin French-Owen: Why don't I generate some sort of equivalent of deep research or something like that?
[00:02:00] And so I was doing actually what a bunch of people I think are doing now where you kind
[00:02:04] Calvin French-Owen: of put together these different agents and they have different roles.
[00:02:07] Calvin French-Owen: So there's a team lead and then there's an engineer and a designer and a researcher.
[00:02:13] Calvin French-Owen: I think I was using Foro at the time and it was just pure meeting slop.
[00:02:18] It's like, I don't know.
[00:02:19] It sounded like for board meetings for these different companies, you get these lawyer
[00:02:24] Calvin French-Owen: minutes.
[00:02:25] Calvin French-Owen: And the lawyer minutes are like, oh, Mr. Frencho and proposed an idea and everyone approved
[00:02:31] Calvin French-Owen: it.
[00:02:32] Calvin French-Owen: It's like, okay, it's like the most vague stuff.
[00:02:35] It kind of sounded like that.
[00:02:36] Calvin French-Owen: I was like, okay, I'm not getting good results from the public models.
[00:02:40] Calvin French-Owen: And around the same time, this guy, Peter Wheelender, who leads new products over at OpenAI,
[00:02:45] Calvin French-Owen: I was saying, hey, there's a new team who's spinning up.
[00:02:48] Calvin French-Owen: They're really focused on a lot of internal tooling for researchers.
[00:02:52] If you want to kind of see where research is going and understand how it's done, it's
[00:02:56] Calvin French-Owen: probably a good fit for building some new products.
[00:02:58] Calvin French-Owen: And I was like, okay, that actually sounds kind of interesting.
[00:03:01] Calvin French-Owen: If I don't like it, I can always leave and I'm kind of back to where I started.
[00:03:05] Calvin French-Owen: And so that was kind of the spark that started everything.
[00:03:08] Calvin French-Owen: And so was that research team responsible for Codex?
[00:03:12] Calvin French-Owen: In a way.
[00:03:13] Calvin French-Owen: In a way.
[00:03:14] Calvin French-Owen: Yeah, so originally we were building internal tools just to help researchers.
[00:03:18] Calvin French-Owen: You can imagine that if you're a researcher, like a lot of what you're doing is kind of
[00:03:21] Calvin French-Owen: the experimentation loop where you're trying to understand what other people have done,
[00:03:25] Calvin French-Owen: you're reading papers, you're like adding data sets, you're kind of doing these trading
[00:03:28] Calvin French-Owen: runs and you kind of like run this in a loop and see what works.
[00:03:32] Calvin French-Owen: And so initially we were just building an internal tool to help with that.
[00:03:36] Calvin French-Owen: And you can imagine a place like opening I where there's like a crazy amount of stuff
[00:03:39] Calvin French-Owen: going on internally.
[00:03:40] Calvin French-Owen: There's like all these Slack channels that people are posting in.
[00:03:44] Calvin French-Owen: There's all these updates that are going into the repo and stuff is changing constantly.
[00:03:48] Calvin French-Owen: So people have a lot of questions.
[00:03:49] Calvin French-Owen: And so it was kind of designed to help answer those questions.
[00:03:53] Calvin French-Owen: Around the time that the reasoning models came out, one member of our team, this guy Andrew,
[00:03:59] Calvin French-Owen: had basically hooked up the reasoning model to like start invoking commands via terminal
[00:04:03] Calvin French-Owen: on his laptop.
[00:04:04] Calvin French-Owen: And he's like, oh, actually, this works really well.
[00:04:07] Calvin French-Owen: And so kind of one thing led to another and we started prototyping and eventually that
[00:04:11] Calvin French-Owen: became CodeX.
[00:04:12] Calvin French-Owen: Wow.
[00:04:13] Wow.
[00:04:14] Tomasz Tunguz: And so I mean, now CodeX is, it's a brilliant piece of infrastructure, right?
[00:04:17] Tomasz Tunguz: And you have like cloud code and a bunch of other coding agents.
[00:04:22] Tomasz Tunguz: When you were, like at what point during the development of CodeX did the team switch
[00:04:26] Tomasz Tunguz: from primarily writing code by hand to what I assume is primarily writing code through
[00:04:31] Tomasz Tunguz: CodeX?
[00:04:32] Tomasz Tunguz: Did that happen?
[00:04:33] Calvin French-Owen: But it did, but pretty late in the cycle.
[00:04:35] Calvin French-Owen: Okay.
[00:04:36] Calvin French-Owen: And frankly, it was because we were kind of building the machine as it was going.
[00:04:40] Calvin French-Owen: Yeah.
[00:04:41] Calvin French-Owen: So there were many kind of like internal versions of CodeX that were floating around OpenAI.
[00:04:47] Calvin French-Owen: It's a very bottoms up place.
[00:04:48] Calvin French-Owen: And so kind of if you have a good idea, you kind of get carte blanche to go just pursue
[00:04:53] Calvin French-Owen: it and build something.
[00:04:55] Calvin French-Owen: And so there are a few teams who have these different internal versions.
[00:04:57] Calvin French-Owen: And those are actually getting like a decent amount of usage.
[00:05:01] But at least when I was there, we weren't yet able to use either Cloud Code or cursor or
[00:05:09] Calvin French-Owen: kind of any of these other tools.
[00:05:10] Calvin French-Owen: And so we were like, okay, we got to build the first version.
[00:05:14] And frankly, I think OpenAI was like trying to get to this game and we were feeling like
[00:05:18] Calvin French-Owen: a little bit late to it.
[00:05:19] Calvin French-Owen: So like cursor was out in the market.
[00:05:21] Calvin French-Owen: Quad Code was out in the market.
[00:05:22] Calvin French-Owen: It's like, okay, we got to launch something.
[00:05:24] Calvin French-Owen: And so basically the whole sprint to launch CodeX took about seven weeks and then like no
[00:05:29] Calvin French-Owen: code written to like launch product.
[00:05:31] Tomasz Tunguz: So it was wild.
[00:05:32] Calvin French-Owen: That's wild.
[00:05:33] Tomasz Tunguz: And was it AI-sacitor where you just cramped people and just jade-ing on people?
[00:05:36] Tomasz Tunguz: Or it was definitely AI-sacitor.
[00:05:37] Tomasz Tunguz: I mean, everyone there is using internal models.
[00:05:41] Calvin French-Owen: I think as time went on, we started being able to use CodeX to write itself, which was
[00:05:45] Calvin French-Owen: actually really cool.
[00:05:46] Calvin French-Owen: But for the most part of it, it was kind of us figuring out how to architect the system
[00:05:51] Calvin French-Owen: and build it in a kind of queenerm way.
[00:05:54] Calvin French-Owen: Yeah.
[00:05:55] Tomasz Tunguz: That's fascinating.
[00:05:56] Tomasz Tunguz: Okay.
[00:05:57] Tomasz Tunguz: And so are there, if you were to start a company today, but you started a very successful
[00:06:02] Tomasz Tunguz: company in the past and you're starting a company today, how big is the difference
[00:06:08] Tomasz Tunguz: between the engineering team?
[00:06:11] I'd say light and day.
[00:06:12] Calvin French-Owen: It's night and day.
[00:06:13] Calvin French-Owen: Yeah, what people can do.
[00:06:14] Calvin French-Owen: Yeah.
[00:06:15] Tomasz Tunguz: I mean, it's also for reference.
[00:06:17] Calvin French-Owen: So segment originally was a product that helped you integrate all these different tools,
[00:06:21] Calvin French-Owen: right?
[00:06:22] Calvin French-Owen: So it's like a single API.
[00:06:23] Calvin French-Owen: It's end data to Google Analytics.
[00:06:25] Calvin French-Owen: And it's the same data as it's going to Cuspereio.
[00:06:28] Calvin French-Owen: Same data as going to Zendesk.
[00:06:30] Calvin French-Owen: Sales force, kind of like this wrapper and adapter layer.
[00:06:34] Calvin French-Owen: And now when I kind of think about that business, I'm like, wow, like the value of writing code
[00:06:38] Calvin French-Owen: is kind of dropping to like zero, you know?
[00:06:40] Calvin French-Owen: Yeah.
[00:06:41] Calvin French-Owen: And so a lot more thinking around like the specs for how it should work and like running
[00:06:45] Calvin French-Owen: these data pipelines at scale.
[00:06:46] Calvin French-Owen: And like all these other things that kind of surround maybe what used to be the core
[00:06:50] Calvin French-Owen: value of that product.
[00:06:53] Calvin French-Owen: And so I don't know, I think you just start like kind of a different looking product in
[00:06:56] Calvin French-Owen: some ways.
[00:06:58] Calvin French-Owen: I think now engineering teams can just produce a lot more code a lot more quickly.
[00:07:04] Calvin French-Owen: And so we're starting to see bottlenecks around like code review.
[00:07:06] Calvin French-Owen: Or like, are we building the right things?
[00:07:09] Calvin French-Owen: How do we deploy it?
[00:07:10] Calvin French-Owen: How do we scale it in a way?
[00:07:12] So there are certain start of business models that you don't think would exist.
[00:07:16] Tomasz Tunguz: Can exist in this era because of the commoditization of code?
[00:07:19] Tomasz Tunguz: I think so.
[00:07:20] Calvin French-Owen: Yeah.
[00:07:21] At least from my perspective, I think writing code, especially sort of like tricky-ish pieces
[00:07:27] Calvin French-Owen: of code to write, like the value there is going down instead of being replaced by running
[00:07:33] Calvin French-Owen: code.
[00:07:34] Calvin French-Owen: Yeah.
[00:07:35] Tomasz Tunguz: Yeah.
[00:07:36] Tomasz Tunguz: And so, okay, so let's say we, you and I start together a company, right?
[00:07:38] Tomasz Tunguz: You'll be the CEO and CTO, right?
[00:07:41] Tomasz Tunguz: And I'll be your VPN.
[00:07:43] Tomasz Tunguz: What advice would you give me for the kinds of people that I would need to recruit?
[00:07:47] Yeah.
[00:07:48] Calvin French-Owen: I think in some ways the kinds of people you want are still the same as ever.
[00:07:52] Calvin French-Owen: Yeah.
[00:07:53] Calvin French-Owen: Or it's like you probably want good generalists who can do many different things well.
[00:07:58] Calvin French-Owen: You want people who are driven and motivated and can be self-starters.
[00:08:01] Calvin French-Owen: I think all of that still stays the same.
[00:08:03] Calvin French-Owen: Yeah.
[00:08:04] Tomasz Tunguz: I think what's shifting about software engineering right now is we're kind of going
[00:08:08] from being people who are focused a lot on the craft of exactly every single line of code
[00:08:14] Calvin French-Owen: that's getting written to more of like managers or PMs in a weird way.
[00:08:21] And I think it like doesn't excuse you from being a good architect and applying good design
[00:08:25] Calvin French-Owen: principles and like looking carefully at whatever you're generated because at the end of the
[00:08:29] Calvin French-Owen: day you're still on the hook as the author of the code.
[00:08:33] Calvin French-Owen: But I do think it's like a slightly different discipline where you don't need to be thinking
[00:08:36] Calvin French-Owen: as carefully about like all of the error cases for example or like how exactly the code looks.
[00:08:41] Calvin French-Owen: So do you change would I change my interviewing process as a result of this or do I still
[00:08:45] Tomasz Tunguz: go through a technical interview.
[00:08:47] Tomasz Tunguz: I think you'd want to change it.
[00:08:48] Tomasz Tunguz: You'd want to how would you change it?
[00:08:51] Calvin French-Owen: I mean this is a good question.
[00:08:55] I'd open it we're still running like very traditional interviews outside.
[00:08:59] Calvin French-Owen: But in general I think you still want to focus on fundamentals like at least for me when
[00:09:03] Calvin French-Owen: I'm bivocoding stuff in a language or like framework that I don't know.
[00:09:07] Calvin French-Owen: There's also our way worse.
[00:09:09] Calvin French-Owen: Even if I know a bunch of the fundamentals about like how it should it might work.
[00:09:13] Calvin French-Owen: There's kind of no replacement yet at least what I found from like knowing an ecosystem or
[00:09:17] Calvin French-Owen: like infrasdac well.
[00:09:21] I think you still yeah still screen for fundamentals.
[00:09:23] Calvin French-Owen: I think I've heard of firms actually just like giving people coding tools to use and saying
[00:09:29] Calvin French-Owen: like go build this thing.
[00:09:31] Calvin French-Owen: I'm going to pause.
[00:09:32] Tomasz Tunguz: So what we've heard is go here's an impossible task that you cannot complete without AI.
[00:09:37] Tomasz Tunguz: Build an email client in an hour and then let's see how far you can get as a proxy
[00:09:41] Tomasz Tunguz: force of sophistication with AI.
[00:09:43] Tomasz Tunguz: Do you think that's a valid?
[00:09:44] Tomasz Tunguz: Do you think that could work?
[00:09:46] I think it can work.
[00:09:47] Calvin French-Owen: I mean I don't know.
[00:09:49] Calvin French-Owen: I'm kind of a systems architecturally guys.
[00:09:51] Calvin French-Owen: I would like lean a lot more heavily on the architecture reviews.
[00:09:54] Calvin French-Owen: Probably screen for writing specs too.
[00:09:57] Calvin French-Owen: Like I find myself writing a lot more specs these days.
[00:09:59] Calvin French-Owen: Okay so let's talk about that.
[00:10:00] Tomasz Tunguz: So you used to have you know there's a PR product-minute classic development cycle that I learned
[00:10:04] Tomasz Tunguz: at Google was product manager comes up with a PRD, goes to the engineering manager, they
[00:10:08] Tomasz Tunguz: created requirements document together and then that is then proculated through the organization
[00:10:15] Tomasz Tunguz: execution.
[00:10:16] Tomasz Tunguz: This depth, how does that process change do you think in this era?
[00:10:21] Calvin French-Owen: I think it's become more important and maybe more iterative.
[00:10:24] Calvin French-Owen: Yeah.
[00:10:25] Calvin French-Owen: Like for the longest time in segment we didn't have specs you know it's like oh kind of
[00:10:28] Calvin French-Owen: like someone's like I got an idea for a thing it's like let me go write the thing you
[00:10:31] Calvin French-Owen: know.
[00:10:32] Calvin French-Owen: And I think it it look it is a valid way of learning to like build a first version and
[00:10:36] Calvin French-Owen: then learn from it and then build an x version.
[00:10:39] Calvin French-Owen: I think now we have these super capable agents that are able to produce code at like a
[00:10:43] Calvin French-Owen: crazy rate and so being able to steer them effectively and help provide the right plan
[00:10:48] Calvin French-Owen: for them I think actually goes a really long ways and it makes your time more leveraged.
[00:10:52] Yeah.
[00:10:53] Tomasz Tunguz: Okay so if you were to take five years ago planning versus acting right that's the model
[00:10:57] Tomasz Tunguz: that we're now calling it.
[00:10:58] Tomasz Tunguz: We're actually time on planning versus acting.
[00:11:01] Tomasz Tunguz: Compare and contrast that five years ago to the ideal today.
[00:11:04] Tomasz Tunguz: Yeah I mean I feel like five years ago is like oh you do like planning in a week for
[00:11:08] Calvin French-Owen: the quarter or something it's like 10.
[00:11:10] Calvin French-Owen: And now it's probably like I don't know 80% planning and then like 20% execution.
[00:11:17] Calvin French-Owen: So you spend a lot of time going through the specification of the.
[00:11:19] Tomasz Tunguz: So why are you thinking this system?
[00:11:21] Tomasz Tunguz: You're building a new feature.
[00:11:23] Calvin French-Owen: Yeah so greater this differs a lot whether you're in like a new code base or not.
[00:11:29] Calvin French-Owen: When I was at opening I like a lot of what I was doing is like okay what do I have to do today
[00:11:32] Calvin French-Owen: like what are the top three things that I want to kick off bugs for like in the morning
[00:11:36] Calvin French-Owen: before my commute let me like provide descriptions for those and then when I get in I can review
[00:11:40] Calvin French-Owen: the code like that's a pretty different mode of working in what I'm doing now.
[00:11:45] Calvin French-Owen: Most of what I'm doing now is kind of trying to put these like new green field systems together.
[00:11:48] Calvin French-Owen: So it's a lot of like writing reading docs like trying to understand especially like Cloudflare
[00:11:53] Calvin French-Owen: and for how it's put together.
[00:11:56] Like architecture specs for how I want the different services to work and trying to find like
[00:12:02] Calvin French-Owen: scaffolds of like tests and the right like initial I don't know kernel of how the code should look
[00:12:08] Calvin French-Owen: such that I think it will stay good for a while.
[00:12:11] Calvin French-Owen: So it's all architecture.
[00:12:13] Tomasz Tunguz: It's a lot more architecture.
[00:12:15] Calvin French-Owen: Yeah.
[00:12:16] Calvin French-Owen: That's fascinating.
[00:12:18] Tomasz Tunguz: But you still need to understand the underlying systems.
[00:12:20] Tomasz Tunguz: You're not blindly creating a specification.
[00:12:23] Tomasz Tunguz: Right.
[00:12:24] Tomasz Tunguz: Yes.
[00:12:25] Tomasz Tunguz: Yes.
[00:12:26] Calvin French-Owen: Yeah.
[00:12:27] Calvin French-Owen: And at least for myself I think the best plans are ones where I've actually written everything.
[00:12:30] Calvin French-Owen: Yeah.
[00:12:31] Calvin French-Owen: Like I think sometimes I'll use AI to generate plans.
[00:12:35] Calvin French-Owen: I don't know it doesn't end up being token efficient in a way that works for me.
[00:12:39] Calvin French-Owen: You know.
[00:12:40] Calvin French-Owen: Because you still need to review.
[00:12:41] Calvin French-Owen: Yeah.
[00:12:42] Tomasz Tunguz: Kind of read them and I'm like yeah okay this sounds good but like if you ask me two
[00:12:46] Calvin French-Owen: seconds later to picture how the system works in my head I don't think I could do it for
[00:12:49] Calvin French-Owen: you.
[00:12:50] Calvin French-Owen: First of I've written the plan and communicated it I think it comes across a little better.
[00:12:55] Calvin French-Owen: And then okay so once you've written the plan what is your goal to I mean there was the
[00:13:00] Tomasz Tunguz: in the recent open AI announcement one person said the record for the longest running agent
[00:13:05] Tomasz Tunguz: was seven hours.
[00:13:06] Tomasz Tunguz: Yeah.
[00:13:07] Tomasz Tunguz: For seven and a half hours.
[00:13:08] Tomasz Tunguz: So is your goal to do that?
[00:13:10] No.
[00:13:11] Tomasz Tunguz: No I don't think so.
[00:13:12] Calvin French-Owen: No.
[00:13:13] Like so for me I think the thing that I'm optimizing for right now is kind of feedback loops.
[00:13:19] Calvin French-Owen: It's like how quickly do I get something working that then I can like verify is a good
[00:13:23] Calvin French-Owen: thing that's working then I can go on to the next thing.
[00:13:27] Calvin French-Owen: So if it runs for seven hours and it like went off the rails somewhere and I have a bunch
[00:13:31] Calvin French-Owen: of code review like that actually doesn't help me that much.
[00:13:34] Calvin French-Owen: And granted like there are certain tasks where probably it does like I could imagine like
[00:13:38] Calvin French-Owen: oh you're hunting a memory bug somewhere and like the scope of it is very well constrained.
[00:13:42] Yeah let that agent go for seven hours and like it finds the bug like great you know.
[00:13:47] Tomasz Tunguz: Yeah.
[00:13:48] Okay but so you get to minimum viable loop.
[00:13:50] Tomasz Tunguz: Yeah.
[00:13:51] Tomasz Tunguz: Where you have this feedback loop where the system is working as designed.
[00:13:54] Tomasz Tunguz: Exactly.
[00:13:55] Tomasz Tunguz: And then you add more complexity and add more complexity.
[00:13:57] Tomasz Tunguz: And do you think at all or how do you think about that loop definition because once you
[00:14:01] Tomasz Tunguz: have that loop really well defined then you can kind of let the agent go and spin and
[00:14:06] Tomasz Tunguz: it'll raise its hand when it needs your help.
[00:14:07] Tomasz Tunguz: Like what makes for an ideal loop?
[00:14:10] Yeah.
[00:14:11] Tomasz Tunguz: Yeah.
[00:14:12] I think it's like both a good spec is input.
[00:14:15] Calvin French-Owen: Yeah.
[00:14:16] Calvin French-Owen: And then good ability to kind of just like run and execute and then some way of verifying
[00:14:19] Calvin French-Owen: the changes.
[00:14:20] Calvin French-Owen: And ideally the changes are able to be verified in a way that's as fast as possible.
[00:14:24] Calvin French-Owen: Yeah.
[00:14:25] Unknown Guest: I remember when I was at OpenAI like our entire backend kind of like booted as a single
[00:14:30] Calvin French-Owen: service and it would take like minutes to boot up.
[00:14:35] So a colleague of mine was joking he was like oh we're left with like the crappiest parts
[00:14:38] Calvin French-Owen: of the job right now.
[00:14:39] Calvin French-Owen: Like we are just like QAing the AI code.
[00:14:42] Calvin French-Owen: And so like if you can speed that up I think that helps a lot.
[00:14:46] Tomasz Tunguz: Any questions from the audience so far on any topics you've covered?
[00:14:49] Calvin French-Owen: Yeah so the question if I could paraphrase it is as you scale up your systems how do
[00:14:55] Calvin French-Owen: you ensure that the agent can continue running this loop in a really quick way or tight cadence
[00:15:02] Calvin French-Owen: as the system becomes more complex.
[00:15:04] Calvin French-Owen: Is that right?
[00:15:07] I think it's hard and actually I think this is where the point about architecture comes
[00:15:10] Calvin French-Owen: back in.
[00:15:11] Calvin French-Owen: Like I think if you do it right and sort of like package your systems up into small
[00:15:16] Calvin French-Owen: simple parts.
[00:15:18] Calvin French-Owen: Coding agents are actually quite good at like getting their footing and understanding
[00:15:22] Calvin French-Owen: like where they should go.
[00:15:25] Calvin French-Owen: I was actually just telling you like in some ways I think it's actually harder to do
[00:15:28] Calvin French-Owen: in a green field project where there is no code like the agent's just going to go off
[00:15:32] Calvin French-Owen: in a random direction.
[00:15:33] Calvin French-Owen: When you think about like median JavaScript that has been trading on and the entire world
[00:15:37] Calvin French-Owen: of JavaScript it's like probably not that good.
[00:15:40] Calvin French-Owen: Versus if you have a lot of like queer patterns in the code base and you're like oh like
[00:15:44] Calvin French-Owen: I want you to make it exactly like this.
[00:15:47] So just like throughout a very concrete example I've been using a lot of cloud player
[00:15:50] Calvin French-Owen: workers recently.
[00:15:51] Calvin French-Owen: And kind of the way that a cloud player worker works is like you write a little JavaScript
[00:15:54] Calvin French-Owen: function and you have a little config file and you can deploy it somewhere.
[00:15:59] Calvin French-Owen: For these workers you can bind them to individual databases.
[00:16:03] Calvin French-Owen: And so what I think is the right pattern for an agent to work with is like you have a
[00:16:08] Calvin French-Owen: bunch of these little workers around that are bound to databases and the workers combine
[00:16:13] Calvin French-Owen: to each other and you almost have like a little microservice architecture where like it's
[00:16:17] Calvin French-Owen: actually pretty clearly to find how data flows between them because they're all like in
[00:16:20] Calvin French-Owen: the same repo.
[00:16:23] And so what I found is that like kind of forcing this architecture where each service is
[00:16:28] Calvin French-Owen: like a few hundred lines and you documented how the service is fit together and there's
[00:16:32] Calvin French-Owen: a very clear request flow.
[00:16:33] Calvin French-Owen: The agent's actually quite good at managing that level of complexity where it wouldn't
[00:16:38] Calvin French-Owen: if you just kind of like let it run wild and it like duplicates functions everywhere.
[00:16:42] Calvin French-Owen: It like never refactors.
[00:16:44] Calvin French-Owen: I think that's the rough case.
[00:16:46] Calvin French-Owen: Yeah, so the question is is maintaining a doc or state around the spec important?
[00:16:51] Calvin French-Owen: It's money for myself.
[00:16:53] Calvin French-Owen: I kind of keep two sets of markdown files in my repo.
[00:16:57] Calvin French-Owen: One is plans and I view those as very much like throw away things.
[00:17:00] Calvin French-Owen: It's like I asked the agent to implement them once.
[00:17:04] Calvin French-Owen: The other is docs and for those I will sometimes ask it to update depending.
[00:17:10] Calvin French-Owen: For neither one will it actually really look at it unless I tell it to.
[00:17:15] And so in some ways the docs are more for my understanding.
[00:17:17] Calvin French-Owen: The plans are for its understanding and then the code is kind of the source of truth
[00:17:21] Calvin French-Owen: that it's using.
[00:17:23] Yeah, so there's a question on switching to more plan heavy versus more implementation
[00:17:31] Calvin French-Owen: heavy and how does that change kind of your implementation.
[00:17:36] Calvin French-Owen: Honestly while I was at OpenAID and see as much of this because we were kind of just
[00:17:39] Calvin French-Owen: building things as they go.
[00:17:41] Calvin French-Owen: So I feel like I'm not, I don't have the direct experience but from talking with friends.
[00:17:45] Calvin French-Owen: Like I definitely think there's a lot more time spent as a group on specs.
[00:17:52] Calvin French-Owen: And ideally the spec is like implemented or chunked in a way where each person is able
[00:17:55] Calvin French-Owen: to own some aspect of it.
[00:17:58] Calvin French-Owen: And then just the implementing goes much faster than it used to.
[00:18:02] So do you think, I mean, so you ran a large engineering organization
[00:18:05] Tomasz Tunguz: do you think the way that you evaluate the team's execution changes or is it just that
[00:18:10] Tomasz Tunguz: your expectations for sprint productivity increases?
[00:18:17] Tomasz Tunguz: Like you can capture more within a two-week sprint.
[00:18:19] Tomasz Tunguz: I think probably both.
[00:18:21] Calvin French-Owen: Both both.
[00:18:22] Calvin French-Owen: Yeah, yeah.
[00:18:23] Calvin French-Owen: I mean, OpenAID, that place moves at like a crazy clip.
[00:18:25] Calvin French-Owen: I think it definitely reset my expectations for how quickly an engineering team can move.
[00:18:30] Calvin French-Owen: Yeah.
[00:18:32] I think you can't exactly go now by like number of PRs merged or like lines of code added
[00:18:42] Calvin French-Owen: because the agents are really good at adding lines of code probably when they shouldn't.
[00:18:45] Calvin French-Owen: Right.
[00:18:46] Calvin French-Owen: To the point on simplicity.
[00:18:48] Calvin French-Owen: And so yeah, I think I would think of it more from like end outcomes.
[00:18:52] Calvin French-Owen: It's like, oh, did we deliver the feature?
[00:18:54] Calvin French-Owen: I mean, one thing I'd love for engineering teams that worked with is like having a weekly
[00:18:57] Calvin French-Owen: demos or like biweekly demos.
[00:18:59] Calvin French-Owen: Basically, it's always anchored on like a customer outcome.
[00:19:02] Calvin French-Owen: Yeah, that's smart.
[00:19:03] Tomasz Tunguz: Yeah.
[00:19:04] That's really cool.
[00:19:05] Tomasz Tunguz: Okay, so your expectation, so how much, I mean like roughly, how much faster do you expect
[00:19:09] Tomasz Tunguz: a modern engineering organization to move relative to say 10 years ago?
[00:19:13] Tomasz Tunguz: Yeah, probably like, I don't know.
[00:19:16] Double speed maybe?
[00:19:17] Calvin French-Owen: Yeah, yeah, yeah.
[00:19:18] Calvin French-Owen: Yeah, yeah.
[00:19:19] Calvin French-Owen: Something like there.
[00:19:20] Calvin French-Owen: And maybe like it's, I don't know, 50 to 100%.
[00:19:23] Calvin French-Owen: Yeah.
[00:19:24] Calvin French-Owen: Someone made this comment.
[00:19:25] Calvin French-Owen: I think it was on Twitter or something.
[00:19:26] Calvin French-Owen: I feel like I write like 100% more code than ever before and I throw away 60% of it.
[00:19:32] Calvin French-Owen: And yet I'm still more productive than I've ever been.
[00:19:34] Calvin French-Owen: It's like that really captures my experience of coding agents.
[00:19:37] Calvin French-Owen: It's like they're going to write a lot.
[00:19:38] Calvin French-Owen: They're going to go off the rails.
[00:19:40] You should think critically about what's there.
[00:19:44] Calvin French-Owen: I write prototypes all the time that I throw away.
[00:19:46] Calvin French-Owen: And I think that's fine.
[00:19:48] Calvin French-Owen: Okay, this still gets you closer to like knowing what the system should look like.
[00:19:50] Calvin French-Owen: Yeah, so we have an internship program at theory and we hired one of our interns in
[00:19:56] Tomasz Tunguz: January.
[00:19:56] Tomasz Tunguz: We took him out to lunch and this is one like lovable and bold.
[00:20:00] Tomasz Tunguz: And so we asked him like, hey, how many apps have you vibed coded?
[00:20:07] Tomasz Tunguz: And he said between 500 to 1000.
[00:20:10] And it blew our minds.
[00:20:12] Tomasz Tunguz: And we asked him like, pan, or how, like, why are you building so many apps?
[00:20:17] Tomasz Tunguz: And he's a student and he said, every time I need to learn a concept in school, we vibed
[00:20:22] code and app.
[00:20:23] Tomasz Tunguz: Really?
[00:20:24] Tomasz Tunguz: And it lives for a day.
[00:20:25] Tomasz Tunguz: We were studying acoustics and so we'll develop a three-dimensional model for how sound waves
[00:20:29] Tomasz Tunguz: travel around different shapes.
[00:20:31] Tomasz Tunguz: And that'll help us learn.
[00:20:32] Tomasz Tunguz: And so this is like that blew my mind.
[00:20:35] Tomasz Tunguz: And then you had this evolution of like best of end, right?
[00:20:37] Tomasz Tunguz: So you give one agent or three different agents, three slightly different prompts to produce.
[00:20:43] Tomasz Tunguz: And then you have an LLM as an evaluator to figure out, okay, which of the code you
[00:20:46] Tomasz Tunguz: throw away.
[00:20:47] Tomasz Tunguz: And that whole workflow, like throwing away two thirds of the code seems so counterintuitive
[00:20:54] Tomasz Tunguz: to a soft printing where you've been taught to be a craft person, right?
[00:20:58] Tomasz Tunguz: This is, I've chiseled this from the clay.
[00:21:00] Tomasz Tunguz: But then you use mid-journey and you realize, okay, actually I'll just throw away all these
[00:21:04] Tomasz Tunguz: images that I don't know.
[00:21:05] Tomasz Tunguz: I'll just pick the one.
[00:21:06] Calvin French-Owen: I think there's something to that even with craftspeople.
[00:21:08] Calvin French-Owen: It's like the quote about painters, right?
[00:21:12] Calvin French-Owen: It's like when the art critics get together, they ask like, oh, where can you find the best
[00:21:14] Calvin French-Owen: art?
[00:21:15] Calvin French-Owen: It's like when the painters get together, it's like, where can you find the cheap turpentine?
[00:21:18] Calvin French-Owen: It's like, you kind of just do things a lot.
[00:21:21] Calvin French-Owen: And I think if you're able to roll the dice more times.
[00:21:24] Calvin French-Owen: At least for myself, it's very instructed to see four different approaches of something.
[00:21:27] Calvin French-Owen: If they're all kind of similar, it's like, okay, there's probably a right way to do this.
[00:21:31] Calvin French-Owen: If they differ wildly, that's actually really interesting.
[00:21:34] Calvin French-Owen: Yeah, that's interesting.
[00:21:35] Calvin French-Owen: That's cool.
[00:21:36] Calvin French-Owen: Do you think?
[00:21:37] Tomasz Tunguz: Okay, so let's take a look at the back.
[00:21:39] Tomasz Tunguz: One thing that you said at the beginning of the conversation was that the role of the
[00:21:43] Tomasz Tunguz: engineering leader has changed.
[00:21:46] Tomasz Tunguz: And one of the things that we've been wondering is, you have, you know, EPD is the way
[00:21:50] Tomasz Tunguz: that these organizations are structured.
[00:21:52] Tomasz Tunguz: Engineering, product and design, all of a sudden, the engineer can do all of it, right?
[00:21:59] The product manager from his or her perspective, I can do all of it.
[00:22:03] Tomasz Tunguz: And the designer says, actually, I can also do all of it, right?
[00:22:06] Tomasz Tunguz: Yeah.
[00:22:07] Tomasz Tunguz: Right?
[00:22:08] Tomasz Tunguz: The designer will come up with a design and figmen and then vibe coded into an existence.
[00:22:11] Tomasz Tunguz: The product manager, again, will probably vibe code and then use the e-vows to drive accuracy
[00:22:15] Tomasz Tunguz: within the underlying system.
[00:22:17] Tomasz Tunguz: And then the engineering, the engineer will go and vibe coded design and then have an
[00:22:21] Tomasz Tunguz: implementation.
[00:22:23] And so do you think EPD, does it fuse?
[00:22:26] I don't think so.
[00:22:27] Calvin French-Owen: I know.
[00:22:28] Calvin French-Owen: I know there's still specialization.
[00:22:29] Calvin French-Owen: I mean, it's funny.
[00:22:30] Calvin French-Owen: Alex, who is the PM on the codex team?
[00:22:31] Calvin French-Owen: Yeah.
[00:22:32] Tomasz Tunguz: He would be using codex to fix issues in small bugs and things.
[00:22:37] Calvin French-Owen: And that was amazing.
[00:22:38] Calvin French-Owen: It'd like freedom up.
[00:22:39] Calvin French-Owen: It's like, oh, I hear a thing from a customer.
[00:22:40] Calvin French-Owen: I'd have fixed it five minutes later.
[00:22:41] Calvin French-Owen: That's great.
[00:22:45] Calvin French-Owen: I don't think he's the person who you'd want making the architecture decisions.
[00:22:50] Calvin French-Owen: But he was the person who was capturing the voice of the customer and prioritizing what
[00:22:53] Calvin French-Owen: should go next.
[00:22:54] Calvin French-Owen: And similarly, for the designers on the project, at least when I'm vibe coding stuff, I know
[00:22:58] Calvin French-Owen: it's not as good as a designer doing it.
[00:23:01] Calvin French-Owen: Right.
[00:23:02] Tomasz Tunguz: So the specialization still matters.
[00:23:03] Tomasz Tunguz: I think the specialization still matters.
[00:23:04] Calvin French-Owen: I think it is cool that you unlock new capabilities for these roles where it's like, oh, I could
[00:23:09] Calvin French-Owen: have been blocked before, but for small stuff, I can just put it out there.
[00:23:13] Calvin French-Owen: Yeah.
[00:23:14] Tomasz Tunguz: Cool.
[00:23:14] Tomasz Tunguz: Product manager with eVal.
[00:23:15] Tomasz Tunguz: So one of the things that we've been struggling or I've been struggling with at least is like,
[00:23:19] Tomasz Tunguz: how to set up the eVal's in the right way.
[00:23:22] Tomasz Tunguz: Right.
[00:23:23] Tomasz Tunguz: Let's say I have an authentic tool calling system, find a list of startups, figure out
[00:23:26] Tomasz Tunguz: whether or not they're in the CRM, evaluate all of those companies, and then add them to
[00:23:31] Tomasz Tunguz: the CRM if they don't exist.
[00:23:33] Tomasz Tunguz: What you really want to your point before was creating feedback loops along the way.
[00:23:37] Tomasz Tunguz: Have you, what do your recommendations or best practices on how to set those up?
[00:23:41] Tomasz Tunguz: Are you sending stuff into a database or are you using an off-the-shelf eVal's tool?
[00:23:48] Calvin French-Owen: We did not do a lot of great eVal work, I would say.
[00:23:52] Tomasz Tunguz: Yeah.
[00:23:53] eVal's eating your vegetables in some ways.
[00:23:55] Calvin French-Owen: It's like, okay, you got to look through a big Asian log, understand what went wrong
[00:23:59] Calvin French-Owen: or didn't.
[00:24:02] Calvin French-Owen: I will say they're uniquely powerful.
[00:24:05] Calvin French-Owen: If you have someone with good taste, who cares a lot, driving them.
[00:24:08] Calvin French-Owen: Interesting.
[00:24:09] Calvin French-Owen: I don't know how the other big labs are structured, but I do think a lot of the work at OpenAI
[00:24:14] Calvin French-Owen: was like, someone with taste figuring out, hey, here's where the agent went wrong.
[00:24:19] Calvin French-Owen: I'm going to train this behavior in the opposite way, and just paying very close attention.
[00:24:25] Calvin French-Owen: I think there's a question of how long that work stays good, because you fix the model
[00:24:31] Calvin French-Owen: or provide new instructions and saturates the eVal.
[00:24:37] Calvin French-Owen: I guess it's not, oftentimes it felt very one-off.
[00:24:40] Calvin French-Owen: It's like, oh, we have a bunch of spreadsheet rows, and they link to various trajectories,
[00:24:44] Calvin French-Owen: and you can see what's going on and that kind of thing.
[00:24:46] Calvin French-Owen: So it's brittle.
[00:24:47] Tomasz Tunguz: From your perspective, it's fine-tuning.
[00:24:49] Tomasz Tunguz: It's kind of a one-off thing as a temporary solution while you're waiting for the model
[00:24:53] Tomasz Tunguz: or the underlying characteristics of the system to improve.
[00:24:56] Yeah.
[00:24:57] Calvin French-Owen: I think you, maybe brittle, I don't know if that's the right word or not, but you have to
[00:25:02] just keep increasing which eVal is your measuring.
[00:25:06] Calvin French-Owen: I have friends who every time a new model comes out, they test it against their own eVal
[00:25:09] Calvin French-Owen: suite, which is a bunch of hard questions, usually they're in customer support or something.
[00:25:13] Calvin French-Owen: I think it's useful for them to just vibe check the model.
[00:25:19] Calvin French-Owen: It's not clear to me what they're actually able to do with that, and then what happens
[00:25:25] Calvin French-Owen: when the model actually saturates them.
[00:25:27] It's like, they got to go just get new eVal's.
[00:25:30] Yeah, it's treadmill.
[00:25:32] Tomasz Tunguz: Any questions on any of those topics?
[00:25:34] Tomasz Tunguz: Yeah.
[00:25:35] Calvin French-Owen: If you didn't have eVal's, basically, how do you evaluate a system that's running?
[00:25:42] Calvin French-Owen: Don't get me wrong.
[00:25:43] Calvin French-Owen: I think eVal's have their place, especially if you're doing your own model training or
[00:25:46] Calvin French-Owen: selection because they help you catch your aggressions.
[00:25:51] Calvin French-Owen: Most of the time it's like, oh, here's exactly where things went off.
[00:25:56] I guess all I would say is often I think that someone who's watching exactly what an agent
[00:26:02] Calvin French-Owen: did and has a small subset of that data, and maybe this is what you call the
[00:26:05] Calvin French-Owen: user's like a manual eVal.
[00:26:07] Calvin French-Owen: And then looking at where it went wrong, I think we'll usually be able to provide the
[00:26:11] Calvin French-Owen: right level of intervention more than having a big automated setup.
[00:26:16] Calvin French-Owen: And so it kind of all comes down to, you find the person with taste, you're able to identify
[00:26:21] Calvin French-Owen: spots where the agent went wrong, maybe automatically, and then you have them just look at it.
[00:26:26] Calvin French-Owen: I think that is an underrated thing that happens all the time in labs and is actually quite
[00:26:30] Calvin French-Owen: useful.
[00:26:31] Calvin French-Owen: Yeah, I mean, a lot of it was like vibes, right?
[00:26:41] Calvin French-Owen: It's like, oh, okay, you notice that something went right or went wrong.
[00:26:47] Calvin French-Owen: And I think actually this kind of goes back to like a holograms point where you should
[00:26:50] Calvin French-Owen: build a startup where you build something for yourself.
[00:26:52] Calvin French-Owen: If you're able to tell every single time something went wrong and log it or just flag it somehow,
[00:26:58] Calvin French-Owen: you'll pretty quickly discover what's going wrong.
[00:27:00] Calvin French-Owen: So a very interesting, like early codex checkpoint, it would kind of like put these Python imports
[00:27:07] Calvin French-Owen: all over the place and in line.
[00:27:10] Calvin French-Owen: And it's like, no, you want to put that at the top of the file.
[00:27:12] Calvin French-Owen: It's like very easy once you have that to add some scoring criteria for it.
[00:27:17] Calvin French-Owen: But until we just saw it and we're using it, it was like, this is a thing that we don't
[00:27:22] Calvin French-Owen: like.
[00:27:23] Calvin French-Owen: And over time, you get to more and more nuanced cases like that.
[00:27:26] Yeah.
[00:27:27] Calvin French-Owen: The question is like, what point do you intervene if the model is doing something bad?
[00:27:30] Calvin French-Owen: Do you do a fine tune?
[00:27:31] Calvin French-Owen: Do you update the context?
[00:27:33] Calvin French-Owen: Do you change the prompts?
[00:27:36] Here I actually don't have great answers.
[00:27:38] Calvin French-Owen: Like, in general, the open AI way is always just train.
[00:27:41] Calvin French-Owen: And so actually, if you like, look at the system instructions for open AI models, like they're
[00:27:45] Calvin French-Owen: pretty terseed because the model has just been trained to do everything.
[00:27:50] I think it probably depends a little bit on your level of complexity and how much resources
[00:27:58] Calvin French-Owen: you have.
[00:27:59] Calvin French-Owen: I would just always start with prompt.
[00:28:01] Calvin French-Owen: Start with the prompt in the context and see how far that can get you.
[00:28:05] Calvin French-Owen: And then if you're kind of limited there or you find yourself just like adding a crazy
[00:28:09] Calvin French-Owen: amount of tokens that then's hurting the model intelligence, then maybe think about
[00:28:12] Calvin French-Owen: a fine tune.
[00:28:13] Calvin French-Owen: And then...
[00:28:14] Calvin French-Owen: Well, I feel like you're better to answer this question because you're a VBSPY guy.
[00:28:43] Calvin French-Owen: We use a lot of DSPY internally with GEPA.
[00:28:48] Tomasz Tunguz: And that works and we do it naively.
[00:28:51] Tomasz Tunguz: So we just say, go and implement this library and then it actually works very, very well.
[00:28:55] Tomasz Tunguz: So yeah, I think that's brilliant framework for it.
[00:29:00] Tomasz Tunguz: You do internally.
[00:29:01] Tomasz Tunguz: Yeah.
[00:29:02] Tomasz Tunguz: So yeah, that's the way that we improve the prompts.
[00:29:04] Tomasz Tunguz: It works.
[00:29:05] Tomasz Tunguz: I would say it works surprisingly well.
[00:29:08] Tomasz Tunguz: And it's pretty computationally efficient.
[00:29:10] Tomasz Tunguz: You're able to run it on like a local, at least we are, local machine.
[00:29:14] Tomasz Tunguz: And you don't need that many examples.
[00:29:16] Tomasz Tunguz: And in fact, the AI agent will actually dynamically generate examples for you.
[00:29:20] Tomasz Tunguz: And even one of the things that we found about AI models is they're really great at creating
[00:29:24] Tomasz Tunguz: ontologies.
[00:29:25] Tomasz Tunguz: And so for the axes for GEPA or GEPA, you'll actually create those axes pretty well.
[00:29:30] Tomasz Tunguz: You do have to modify it from time to time.
[00:29:31] Tomasz Tunguz: So if you're creating a piece of content, there's voice, length, sentence structure, those
[00:29:35] Tomasz Tunguz: kinds of things.
[00:29:37] Tomasz Tunguz: You might have to add one or two different scoring parameters and maybe modify the weights,
[00:29:42] Tomasz Tunguz: but otherwise the bootstrapping is quite effective.
[00:29:50] How much better do you think the models will get by the end of the year?
[00:29:54] Tomasz Tunguz: By the end of the year?
[00:29:55] Tomasz Tunguz: Yeah.
[00:29:56] Tomasz Tunguz: Do you think we'll start, we'll continue to see meaningful improvements?
[00:29:59] Tomasz Tunguz: We do think we're close to a plateau.
[00:30:03] And I know, I mean, this is just your personal opinion.
[00:30:05] Tomasz Tunguz: Yeah, yeah, personal opinion.
[00:30:10] Let's see.
[00:30:12] I think we'll continue to see meaningful improvements in some areas.
[00:30:18] And I think there are ones that tend to be easier to train against.
[00:30:21] Calvin French-Owen: So I don't know, areas where the models do badly because they don't know about some recent
[00:30:27] Calvin French-Owen: version of libraries.
[00:30:28] Calvin French-Owen: It's like, OK, we'll kind of upgrade our prior for the model and then add some info and
[00:30:33] Calvin French-Owen: give it a ability to look for most recent versions, that kind of thing.
[00:30:36] Calvin French-Owen: Or maybe Rust is like, we're supported then Python.
[00:30:42] Calvin French-Owen: We'll see a lot more uplift there.
[00:30:46] Calvin French-Owen: I think some of these longer tasks around architecture and how to put systems together.
[00:30:54] Calvin French-Owen: They're harder to train.
[00:30:56] Tomasz Tunguz: What makes them harder to train?
[00:30:57] Tomasz Tunguz: Can you feed it a bunch of design patterns from one of the classic textbooks and say,
[00:31:01] Tomasz Tunguz: implemented this way?
[00:31:03] Calvin French-Owen: Like microservices, right?
[00:31:04] Tomasz Tunguz: Here's the best class microservices architecture.
[00:31:08] Tomasz Tunguz: You can.
[00:31:09] Calvin French-Owen: I think what's tricky about it is, well, in some ways to me, it's sort of like magic that
[00:31:14] Calvin French-Owen: the coding agents work at all.
[00:31:15] Calvin French-Owen: Like when you think about what they're doing, it's like, basically you have a team of like
[00:31:19] Calvin French-Owen: super engineers with laptops.
[00:31:23] You put them in a room that's totally white, unmarked.
[00:31:27] Calvin French-Owen: And then you like, slip them a prompt under the door, which is like, yo, go implement
[00:31:30] Calvin French-Owen: this feature, you have a copy of the repo.
[00:31:32] Calvin French-Owen: They don't know anything about your business, right?
[00:31:34] Calvin French-Owen: Like, it's crazy that it works at all.
[00:31:36] Calvin French-Owen: Right.
[00:31:37] Calvin French-Owen: And so I think that's where the architecture patterns get tricky because the thing that works
[00:31:41] Calvin French-Owen: for like a two person startup, maybe is not the thing that like a giant enterprise needs.
[00:31:47] Calvin French-Owen: And so I think it's hard to have like a one size fits all pattern for them.
[00:31:50] Calvin French-Owen: Yeah.
[00:31:51] Calvin French-Owen: Maybe you can do it.
[00:31:52] Calvin French-Owen: I think also the thing that gets tricky is like applying the appropriate reward signal
[00:31:58] Calvin French-Owen: to some of these spuzzier areas.
[00:32:00] Calvin French-Owen: It's very clear.
[00:32:01] Calvin French-Owen: It's like, oh, the test pass or they didn't pass or like the style pass or not.
[00:32:04] Calvin French-Owen: But architecture, there is no quantitative heuristic.
[00:32:08] Tomasz Tunguz: There's often like trade-offs, right?
[00:32:09] Tomasz Tunguz: And it's like, which trade-off do you accept as a business?
[00:32:11] Calvin French-Owen: Right.
[00:32:12] Calvin French-Owen: Yeah.
[00:32:13] Calvin French-Owen: That makes sense.
[00:32:14] Calvin French-Owen: That makes a lot of sense.
[00:32:15] So I didn't realize how these systems are architected.
[00:32:18] Tomasz Tunguz: I didn't realize what codex is or cloud code is actually doing.
[00:32:22] Tomasz Tunguz: And so I took the, I didn't have internet connection on a plane.
[00:32:27] Tomasz Tunguz: And I had access to the, I had downloaded the open source Gemini CLI.
[00:32:31] Tomasz Tunguz: Now.
[00:32:32] And I ran a little model to create a clone of it using a local model.
[00:32:37] And I didn't realize, I mean, you ask it a question.
[00:32:40] Tomasz Tunguz: It asks the model once.
[00:32:42] Tomasz Tunguz: It saves the answer in a little bit of the context.
[00:32:44] Tomasz Tunguz: And then it errates, it just keeps asking the model the same question, ask the model the
[00:32:47] Tomasz Tunguz: same question, ask the model the next question.
[00:32:50] Tomasz Tunguz: And it updates it.
[00:32:51] Tomasz Tunguz: And at some point, there's some like scoring mechanism that says you have enough information,
[00:32:54] Tomasz Tunguz: like go back to the user.
[00:32:55] Tomasz Tunguz: Yeah.
[00:32:56] Tomasz Tunguz: And all this stuff works.
[00:32:57] Tomasz Tunguz: Yes.
[00:32:58] Tomasz Tunguz: I mean, I had no idea that it was, and that from that very simple behavior, you get this unbelievably
[00:33:06] Tomasz Tunguz: complex output.
[00:33:07] Tomasz Tunguz: It kind of reminds me of like the funnomen automaton.
[00:33:10] Tomasz Tunguz: Yeah.
[00:33:11] Tomasz Tunguz: It's very, very simple rules for robots that all of a sudden get this hugely complex behavior.
[00:33:15] Tomasz Tunguz: It's wild.
[00:33:16] Yeah.
[00:33:17] Calvin French-Owen: I remember there was one all hands where someone like asked the chief scientist, they were like,
[00:33:23] Calvin French-Owen: oh, like how does the model know when it's done?
[00:33:25] Calvin French-Owen: And it's just like when it's trained to say it's done.
[00:33:29] Calvin French-Owen: And it's like, that's right.
[00:33:32] Calvin French-Owen: And also crazy that it works.
[00:33:33] Calvin French-Owen: Yeah.
[00:33:34] Calvin French-Owen: That's wild that it works.
[00:33:35] Tomasz Tunguz: And then you start to realize, okay, you need like memory management, you need to manage
[00:33:37] Tomasz Tunguz: context across these things.
[00:33:39] Tomasz Tunguz: And that's a brand new area where there are not a lot of best practices yet.
[00:33:44] Tomasz Tunguz: How do you compress, how do you, like, log code, you have to compact and like the management
[00:33:47] Tomasz Tunguz: of the compact, what fraction of the context window are you managing through different state
[00:33:51] Tomasz Tunguz: in order to drive accuracy?
[00:33:52] Tomasz Tunguz: Yeah.
[00:33:53] Calvin French-Owen: I think there's a lot of fertile ground there, for what it's worth.
[00:33:55] Calvin French-Owen: Yeah.
[00:33:56] Calvin French-Owen: I mean, I'm not a big fan of like compaction.
[00:33:58] Calvin French-Owen: It's like, okay, you like took this giant wall of context and like maybe you pulled out
[00:34:02] Calvin French-Owen: the good parts, maybe not.
[00:34:05] Calvin French-Owen: But it is very hard to figure out like, okay, the agent went down this wrong route loop.
[00:34:10] Calvin French-Owen: But like, it should mark kind of like a tombstone there for that.
[00:34:13] Calvin French-Owen: Like, oh, I want to explore these areas.
[00:34:15] Calvin French-Owen: Here actually the like top three relevant things.
[00:34:18] Calvin French-Owen: Like I've xxploring a bunch of different files.
[00:34:20] Calvin French-Owen: How do you not pollute the context?
[00:34:21] Calvin French-Owen: If it's like, it went, did something and you tell it, don't do that.
[00:34:24] Calvin French-Owen: Can it like prune it?
[00:34:26] Calvin French-Owen: I think we're still in like pretty wild west there.
[00:34:28] Calvin French-Owen: Yeah.
[00:34:29] One last question for me around like state management.
[00:34:31] Tomasz Tunguz: You create these like super long to do lists.
[00:34:34] Tomasz Tunguz: Are you using the internal to do list when you're coding with these systems?
[00:34:38] Tomasz Tunguz: Are you actually writing progressive state into the systems as they go?
[00:34:44] For me, it's more the internal to do list.
[00:34:46] Calvin French-Owen: It's the internal to do list.
[00:34:47] Calvin French-Owen: Yeah, yeah.
[00:34:48] Calvin French-Owen: Or at least I find they work well enough.
[00:34:49] Calvin French-Owen: And again, it like depends on what you're doing, I think.
[00:34:53] Calvin French-Owen: I do think for bigger features I'm trying to implement, I'll like try and chunk them
[00:34:56] Calvin French-Owen: into milestones.
[00:34:57] Calvin French-Owen: And like some of this is me like chunking them where it's like, oh, there's a spec for
[00:34:59] Calvin French-Owen: this.
[00:35:00] Calvin French-Owen: And then sometimes it's the model where I'm asking like, oh, okay, can you like chunk this
[00:35:03] Calvin French-Owen: into various parts?
[00:35:05] Calvin French-Owen: I think either can work.
[00:35:07] Calvin French-Owen: But yeah, my universal advice for everyone here is just like play around with all the
[00:35:11] Calvin French-Owen: different tools because they change all the time.
[00:35:14] Calvin French-Owen: And you'll probably develop like almost a model smell for like which models are good at
[00:35:17] Calvin French-Owen: which things.
[00:35:18] Calvin French-Owen: So what do you think which models are good at?
[00:35:20] Tomasz Tunguz: What?
[00:35:21] Tomasz Tunguz: You sense?
[00:35:22] Tomasz Tunguz: Yeah, I think in general, I think the inthropic models tend to be very good at tool use.
[00:35:30] And like they clearly they figured out something that doesn't show in the benchmarks.
[00:35:34] Calvin French-Owen: And so for anything where it's like, oh, you want to invoke a terminal command or like,
[00:35:37] Calvin French-Owen: I mean, you can customize quad code to the moon in terms of MCP servers and like all these
[00:35:42] Calvin French-Owen: different things.
[00:35:43] Calvin French-Owen: Like, I think quad code works very well there.
[00:35:46] Calvin French-Owen: And I think codex is like a very exceptional job in terms of just like pure like, oh, I
[00:35:49] Calvin French-Owen: want to like surgically like make these changes, especially if they're, I mean, especially
[00:35:55] Calvin French-Owen: Python stuff, but TypeScript too.
[00:35:59] Calvin French-Owen: And then I think actually, I don't know how many people here have tried the new cursor
[00:36:02] Calvin French-Owen: model.
[00:36:03] Calvin French-Owen: It is exceptionally fast.
[00:36:04] Calvin French-Owen: Oh, it's also unbelievably fast.
[00:36:06] Calvin French-Owen: Yeah.
[00:36:07] Calvin French-Owen: I think the intelligence ceiling might not be as high as some of the others, but like,
[00:36:11] Calvin French-Owen: if you're just like, oh, I want to make this change across like 10 different files,
[00:36:14] Calvin French-Owen: it's pretty good.
[00:36:15] Calvin French-Owen: That's really good.
[00:36:16] Calvin French-Owen: Yeah.
[00:36:17] Calvin French-Owen: And for that case, I like value the speed more.
[00:36:18] Calvin French-Owen: And it's addictive to watch all the tokens come through with that speed.
[00:36:21] Tomasz Tunguz: It's so change.
[00:36:22] Calvin French-Owen: Yeah.
[00:36:23] Calvin French-Owen: So honestly, I switch between kind of all three.
[00:36:25] Calvin French-Owen: You do.
[00:36:26] Calvin French-Owen: Yeah.
[00:36:27] Calvin French-Owen: Like, if I need to know like current version of library, I'll probably like, hit up quad
[00:36:29] Calvin French-Owen: code.
[00:36:30] Calvin French-Owen: I like kind of use codex for most of my mainly drive daily driver.
[00:36:33] Calvin French-Owen: So any final question?
[00:36:37] Calvin French-Owen: The question is, how do you generate or incorporate testing?
[00:36:39] Calvin French-Owen: Often I'll let the AI generate the tests.
[00:36:41] Calvin French-Owen: I think for things where I care a lot about the behavior, I'll actually kind of spec out
[00:36:45] Calvin French-Owen: the tests as well.
[00:36:47] Calvin French-Owen: I think I've also been experimenting with to do driven development, where I kind of create
[00:36:51] Calvin French-Owen: the scaffold and architecture for it.
[00:36:53] Calvin French-Owen: And then I say, oh, go implement these to do's, which actually the codex extension has
[00:36:57] Calvin French-Owen: a pretty awesome way of integrating with cursor via code, where it's just like, oh, implement
[00:37:02] Calvin French-Owen: with codex and just click if it sees it to do.
[00:37:05] Calvin French-Owen: But anyway, I think there's a lot of different ways to do it.
[00:37:09] Calvin French-Owen: There, I actually feel better in an established code base, because you could say mirror testing
[00:37:13] Calvin French-Owen: patterns from these other places, and the model will do a better job.
[00:37:16] Calvin French-Owen: Yeah.
[00:37:17] Calvin French-Owen: So what are the bottlenecks?
[00:37:20] I think there are a couple of big bottlenecks.
[00:37:21] Calvin French-Owen: When it comes to coding, code review is definitely one, invalidation.
[00:37:26] Like suddenly we've all got these crazy agents who can generate lots of code everywhere.
[00:37:32] Calvin French-Owen: Who's going to check that it's the right thing?
[00:37:35] Calvin French-Owen: I think it's kind of poor form to just create a giant PR and then send it to a coworker
[00:37:40] Calvin French-Owen: if you didn't review it.
[00:37:43] Calvin French-Owen: So I think there's a lot of room for improvement there.
[00:37:46] Calvin French-Owen: Actually, I've started using codex as like an auto review all my PRs feature.
[00:37:50] Calvin French-Owen: I think like cursor and traffic due to, that's awesome.
[00:37:53] Calvin French-Owen: At least for even just like being a sanded check.
[00:37:57] Calvin French-Owen: I think the other thing that tends to be a bottleneck is like context about kind of more specialized
[00:38:01] Calvin French-Owen: things.
[00:38:02] Calvin French-Owen: I mean, I know a lot of people are working on kind of like automated SRE type ideas,
[00:38:06] Calvin French-Owen: where it's like, oh, we like saw this issue in DataDog.
[00:38:09] Calvin French-Owen: Like, now we want to be able to pull that into the code base to be able to fix some sort
[00:38:12] Calvin French-Owen: of performance issue or like turning issues from linear into like automated pull requests.
[00:38:19] Calvin French-Owen: I think you're going to see a lot more of that kind of thing.
[00:38:22] Calvin French-Owen: I think we still have to, the workflows for figuring out how humans interact with that
[00:38:27] Calvin French-Owen: are still very nascent.
[00:38:29] Calvin French-Owen: And then I guess the other thing is like jumping between context like as a human in a bunch
[00:38:35] Calvin French-Owen: of different use cases, right?
[00:38:36] Calvin French-Owen: Because it's like, okay, maybe now instead of like doing one task at a time you're managing
[00:38:40] Calvin French-Owen: like five or six, it depends a lot on what you're doing.
[00:38:44] Calvin French-Owen: But I think jumping between those and remembering what you're doing is tough.
[00:38:48] Yeah, so the question is like, do we have to go to AGI if we have like really good coding
[00:38:54] Calvin French-Owen: agents?
[00:38:55] Calvin French-Owen: Is that right?
[00:38:56] Calvin French-Owen: Yeah, so again, this is just my personal take.
[00:38:58] Calvin French-Owen: Like, I'm not going to have open AI and don't speak for the company.
[00:39:02] Calvin French-Owen: I think there's still a lot of things that have to happen outside of just code for AI to
[00:39:08] Calvin French-Owen: really be like AGI or useful like broadly in terms of the economy.
[00:39:13] Calvin French-Owen: I mean, Anthropic tried this, right?
[00:39:15] Calvin French-Owen: Like, I don't know if you all read there like, Benning Machine blog post, but basically
[00:39:19] Calvin French-Owen: they had Quad try and like run an internal store at Anthropic where Benning or employees could
[00:39:24] Calvin French-Owen: go to the Benning Machine and like say like, oh, I want these things.
[00:39:27] Calvin French-Owen: And it was kind of a crazy experiment and it like didn't work at all compared to what
[00:39:32] Calvin French-Owen: you'd expect a human to do, you know?
[00:39:33] Calvin French-Owen: Like, people would be getting things for free all the time.
[00:39:36] Calvin French-Owen: They'd be like, haggling down.
[00:39:37] Calvin French-Owen: Like, it basically ran through its bank account already.
[00:39:40] Calvin French-Owen: And when I think about like, oh, would I like actually have an agent like go and run
[00:39:44] Calvin French-Owen: my life, like actually respond to all my email and like book flights for me and like manage
[00:39:49] Calvin French-Owen: a bunch of these things, it's like probably not yet.
[00:39:53] And I think there's a lot of areas of that that just require like a lot more training if
[00:39:57] Calvin French-Owen: that makes sense.
[00:39:59] Calvin French-Owen: Where, I don't know, it has to know like who your connection is to people.
[00:40:04] Calvin French-Owen: It has to be able to like respond differently in different situations.
[00:40:07] Calvin French-Owen: It has to be able to like guard against prompt injections.
[00:40:10] Calvin French-Owen: Like if someone says like, oh, transfer this money from this bank account.
[00:40:14] Calvin French-Owen: Like, is that coming from your banker or is that coming from like random person on the
[00:40:18] Calvin French-Owen: internet?
[00:40:19] Calvin French-Owen: And so I think there's a bunch of things that have to be figured out there.
[00:40:22] Calvin French-Owen: Coding is definitely like the highest value and easiest to train for because it's a very
[00:40:26] Calvin French-Owen: binary outcome.
[00:40:27] Calvin French-Owen: And so I think that's why you see such big gains there.
[00:40:29] Calvin French-Owen: And to expect you see like similar gains starting to take off in other areas which follow
[00:40:35] Calvin French-Owen: that pattern.
[00:40:36] Calvin French-Owen: Yeah.
[00:40:37] So if I could paraphrase the question is how do you think about junior engineers in
[00:40:43] Calvin French-Owen: like this current hiring climate?
[00:40:45] Calvin French-Owen: Or just like how do you think about how it changes the talent for regulation process
[00:40:51] or not just software?
[00:40:54] One is I do think it's going to be more difficult for a junior person to enter kind of
[00:40:59] Calvin French-Owen: just like median junior person.
[00:41:02] Calvin French-Owen: Because I do think like especially on the engineering side companies will probably need
[00:41:06] Calvin French-Owen: fewer.
[00:41:07] Calvin French-Owen: Is it my personal guess?
[00:41:09] Calvin French-Owen: I don't know if that's actually going to happen or not.
[00:41:12] We're seeing it in startups.
[00:41:13] Tomasz Tunguz: Are you?
[00:41:14] Calvin French-Owen: The organization's used to look like pyramids and now they look like rockets.
[00:41:16] Tomasz Tunguz: Yeah, I am.
[00:41:18] Calvin French-Owen: Intuitively that feels right to me.
[00:41:21] On the flip side, I do think young people who are entering the workforce like, I don't
[00:41:27] Calvin French-Owen: know.
[00:41:28] Calvin French-Owen: At least the young people that I have met are like so high powered.
[00:41:32] Calvin French-Owen: Like they just pour energy into everything and I'm like, oh man, I want to work with more
[00:41:35] Calvin French-Owen: of these people.
[00:41:37] Calvin French-Owen: And so I think, especially when I look back on like where I was when I was 21, like I
[00:41:42] Calvin French-Owen: made a bunch of bad choices and like didn't have that wisdom and made poor architecture
[00:41:47] Calvin French-Owen: decisions.
[00:41:48] Calvin French-Owen: But I kind of just made up with it with like endless energy more so than I have today
[00:41:53] Calvin French-Owen: and like probably more mental horsepower and like sharpness of wit.
[00:41:57] Calvin French-Owen: And so I think there is still a place for those people.
[00:42:00] Calvin French-Owen: Like it's not like I don't think we'll stop hiring new grads.
[00:42:03] Calvin French-Owen: You know, I think that would be the wrong conclusion to draw.
[00:42:07] I do think the labor is going to shift in like a pretty big way as you see like more
[00:42:13] Calvin French-Owen: of these entry level positions or like kind of more manual tasks get automated.
[00:42:19] I honestly don't know what that looks like.
[00:42:21] Calvin French-Owen: I feel like in Silicon Valley we like think about this a lot and you go talk to people
[00:42:25] Calvin French-Owen: in the broader world and they have no idea.
[00:42:28] Calvin French-Owen: And yeah, I'm not sure how it's going to diffuse.
[00:42:31] Calvin French-Owen: You talked all the economists and they're like, oh, like GDP is going to continue growing
[00:42:35] Calvin French-Owen: at like a similar rate.
[00:42:36] Calvin French-Owen: Like nothing's going to change.
[00:42:38] Calvin French-Owen: It will like very slow the diffuse and I kind of trust the economists on this one.
[00:42:42] Calvin French-Owen: But at the same time, the capabilities are accelerating on a crazy rate.
[00:42:46] Calvin French-Owen: Yeah, yeah.
[00:42:47] Calvin French-Owen: So what would I change in terms of how I'm hiring?
[00:42:51] In general, I think you can get a lot more done with a lot fewer people.
[00:42:55] I think there are definitely times like in the past 10, 15 years of startups where it's
[00:43:00] Calvin French-Owen: kind of like, oh, you got to like hire as many people as possible.
[00:43:04] Calvin French-Owen: And I think if people are looking at that and figuring out like, what can I automate
[00:43:07] Calvin French-Owen: instead?
[00:43:08] Calvin French-Owen: Like, are there ways to hire AI?
[00:43:11] Calvin French-Owen: I think there's still going to be a large class of problems for a while where you still
[00:43:15] Calvin French-Owen: want a human there.
[00:43:18] Calvin French-Owen: Whether it's judgment, whether it's like relationships with other people, whether it's,
[00:43:21] Calvin French-Owen: I don't know.
[00:43:23] Humans are like so flexible and so smart and like so, I don't know, able to do many different
[00:43:29] Calvin French-Owen: tasks well in a way that I think LMS are still quite a ways away from.
[00:43:33] Calvin French-Owen: Awesome.
[00:43:34] One more question.
[00:43:35] Yep.
[00:43:36] Tomasz Tunguz: So the question is referencing a paper which came out of MIT around AI adoption enterprise
[00:43:43] Calvin French-Owen: and finding that it wasn't working basically, right?
[00:43:46] Calvin French-Owen: Yeah.
[00:43:47] So the paper found that it was actually change management that was the problem.
[00:43:57] Tomasz Tunguz: It wasn't the underlying technology.
[00:43:58] Tomasz Tunguz: And so if we think about like this forward deployed engineer wave, a big part of it of
[00:44:05] Tomasz Tunguz: the value of forward deployed engineers is that change management.
[00:44:08] Tomasz Tunguz: Leadership says board says CEO says Calvin, you need to deploy AI inside of your
[00:44:13] Tomasz Tunguz: organization.
[00:44:14] Tomasz Tunguz: You know, I as a leader, I don't really know a lot about AI.
[00:44:17] Tomasz Tunguz: I need to find an expert.
[00:44:19] Tomasz Tunguz: And then I need to look at all of my underlying workflows, figure out which of those can
[00:44:24] Tomasz Tunguz: be automated with AI and then find a team to help me implement that.
[00:44:28] Tomasz Tunguz: That's hard.
[00:44:29] Tomasz Tunguz: I mean, you're talking about retraining entire workforces all at once on these new workflows.
[00:44:33] Tomasz Tunguz: That's why we see a lot of failure and why the FD motion is so popular these days.
[00:44:39] Tomasz Tunguz: Yeah.
[00:44:40] Calvin French-Owen: So it's crazy or what's hard to, well, at least from what I've heard for friends selling
[00:44:44] Calvin French-Owen: to enterprise startups or enterprise companies, is they are receiving like wild pressure from
[00:44:50] Calvin French-Owen: their board and their investors to double down in AI.
[00:44:55] Calvin French-Owen: And it's so new and there's so many people selling them things that it's hard to know what's
[00:45:00] Calvin French-Owen: real and like how to put it into practice.
[00:45:02] Calvin French-Owen: Yeah.
[00:45:03] Calvin French-Owen: The change management, absolutely.
[00:45:04] Tomasz Tunguz: Well, Calvin, thank you so much for your time.
[00:45:05] Tomasz Tunguz: It was great to hear about your journey through CodeX, all the different techniques that
[00:45:09] Tomasz Tunguz: we can use in order to implement software better and then how to build engineering organizations.
[00:45:13] Tomasz Tunguz: Big round of applause to Calvin.
[00:45:14] Tomasz Tunguz: Thank you.
[00:45:15] Tomasz Tunguz: Thank you very much.
[00:45:16] Tomasz Tunguz: Thanks so much.