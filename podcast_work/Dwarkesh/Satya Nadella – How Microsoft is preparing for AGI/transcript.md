# Satya Nadella – How Microsoft is preparing for AGI

**Podcast:** Dwarkesh
**Date:** 2025-11-12
**Video ID:** 8-boBsWcr5A
**Video URL:** https://www.youtube.com/watch?v=8-boBsWcr5A

---

[00:00:00] maybe after the industrial revolution this is the biggest thing.
[00:00:03] Satya Nadella: But at the same time, I'm a little grounded in the fact that this is still early innings.
[00:00:08] Satya Nadella: If you're a model company, you may have a winner's curse, you may have done all the hard work,
[00:00:12] Satya Nadella: done unbelievable innovation, except it's kind of like one copy away from that being commoditized.
[00:00:20] Satya Nadella: We didn't want to just be a host for one company and have just a massive book of business
[00:00:26] Satya Nadella: with one customer. That's not a business. You can't build an infrastructure that's optimized
[00:00:30] Satya Nadella: for one model. If you do that, you're one tweak away. Some MOE like breakthrough that happens
[00:00:35] Satya Nadella: when your entire network topology goes out of the window, then that's a scary thing.
[00:00:39] Satya Nadella: Our business which today is an end user tools business will become essentially an infrastructure
[00:00:45] Satya Nadella: business in support of agents doing work. The thing that you have to think through is not what
[00:00:49] Satya Nadella: you do in the next five years, but what do you do for the next 50?
[00:00:53] Satya Nadella: Today we are interviewing Satya Nadella, we being me and Delaan Patel, who is founder of Simeon Alessas.
[00:01:00] Dwarkesh Patel: Satya, welcome. Thank you. It's great. Thanks for coming over.
[00:01:03] Satya Nadella: I'm at Atlanta. Yeah, thank you for giving us the tour of the new facility. It's been really
[00:01:07] Dwarkesh Patel: cool to see. Absolutely. Satya and Scott Guthrie, Microsoft's EVP of Cloud and AI,
[00:01:13] Dwarkesh Patel: give us a tour of their brand new Fairwater 2 data center, the current most powerful in the world.
[00:01:18] Dwarkesh Patel: We're trying to 10X the training capacity every 18 to 24 months, and so this would be effectively a 10X
[00:01:25] Scott Guthrie: increase. 10X from what GPD-5 was trained with. And so to put a perspective, the number of
[00:01:29] Scott Guthrie: optics, the network optics in this building is almost as much as all of Azure across all our data
[00:01:36] Scott Guthrie: centers two and a half years ago. It's kind of what five million network connections.
[00:01:41] Scott Guthrie: You've got all this bandwidth between different sites and a region and between the two regions.
[00:01:45] Dwarkesh Patel: So is this like a big bet on scaling in the future that you anticipate in the future? There's
[00:01:49] Dwarkesh Patel: going to be some huge model that needs to require two whole different regions to train. The goal
[00:01:54] Satya Nadella: is to be able to kind of aggregate these flops for a large training job and then put these things
[00:02:00] Satya Nadella: together across sites. Right. And the reality is you'll use it for training and then you'll use it
[00:02:08] Satya Nadella: for data, you'll use it for inference in all sort of ways. It's not like it's going to be used
[00:02:12] Satya Nadella: only for one workload forever. Fairwater 4, which you're going to see under construction nearby.
[00:02:18] Scott Guthrie: Yeah, we'll also be on that one petabits network so that we can actually link the two at a very
[00:02:23] Scott Guthrie: high rate. And then basically we do the I-Wan connecting to Milwaukee where we have multiple
[00:02:28] Scott Guthrie: other fair waters being built. Literally you can see the model parallelism and the data parallel.
[00:02:34] Satya Nadella: It's kind of built for essentially the training jobs, the pods, the super pods across this campus
[00:02:44] Satya Nadella: and then with the van you can go to the Wisconsin data center and you literally run a training job
[00:02:52] Satya Nadella: with all of them getting aggregated. And what we're seeing right here is this is a cell with no
[00:02:56] Scott Guthrie: servers in it. No racks. How many racks are in a cell? We think about it. We don't necessarily
[00:03:02] Scott Guthrie: share that per se, but we do. So, we did I ask you. You'll see upstairs. You can start counting.
[00:03:09] Scott Guthrie: We'll let you start counting. That part also I can't do it.
[00:03:12] SPEAKER_02: The division is easy, right?
[00:03:18] Oh my god, it's got a lot of load. How are you looking at this? Like now I see where my money is going.
[00:03:23] SPEAKER_02: It's got like, I run a software company. Welcome to the software company.
[00:03:29] SPEAKER_02: How big is the design space once we've decided to use the GB200 and Enveiling? How many other
[00:03:34] Dwarkesh Patel: decisions are there to be made? It is coupling from the model architecture to what is the physical
[00:03:42] Satya Nadella: plan that's optimized. And it's also scary in that sense, which is, hey, there's going to be a new
[00:03:48] Satya Nadella: chip that will come out, which obviously I mean you take where are we in ultra? I mean that's
[00:03:52] Satya Nadella: going to have power density that's going to be so different, but with cooling requirements that
[00:03:56] Satya Nadella: are going to be so different, right? So you kind of don't want to just build all to one spec.
[00:04:03] Satya Nadella: So that goes back a little bit to I think the dialogue will have, which is you want to be scaling
[00:04:10] Satya Nadella: in time, as opposed to scale once and then be stuck with it then.
[00:04:14] Satya Nadella: When you look at all the past technological transitions, whether it be railroads or the internet or
[00:04:21] Dwarkesh Patel: replaceable parts and drush utilization, the cloud, all of these things, each revolution has gotten
[00:04:28] Dwarkesh Patel: much faster in the time it goes from technology discovered to ramp and pervasiveness through the
[00:04:32] Dwarkesh Patel: economy. Many folks who have been on the market share podcast believe this is sort of the final
[00:04:38] Dwarkesh Patel: technological revolution or transition and this time is very, very different. And at least so far
[00:04:44] Dwarkesh Patel: in the markets it's sort of in three years we've already skyrocketed to hyper scalers are doing
[00:04:49] Dwarkesh Patel: 500 billion dollars of cat-backs next year, which is a scale that's unmatched to prior
[00:04:54] Dwarkesh Patel: revolutions in terms of speed. And the end state seems to be quite different. How do you,
[00:05:00] Dwarkesh Patel: you're framing of this seems quite different than sort of the I would say the AI bro who is
[00:05:05] Dwarkesh Patel: quite, you know, AGI is coming and you know I'd like to understand that more.
[00:05:10] Dwarkesh Patel: I mean look I start with the excitement that I also feel for maybe after the industrial
[00:05:17] Satya Nadella: revolution this is the biggest thing. And so therefore I start with that premise.
[00:05:24] Satya Nadella: But at the same time I'm a little grounded in the fact that this is still early innings.
[00:05:29] Satya Nadella: We've built some very useful things we're seeing some great properties the scaling laws seem to be
[00:05:34] Satya Nadella: working and I'm optimistic that they'll continue to work, right. Some of it is you know it does
[00:05:42] Satya Nadella: require real science breakthroughs but it's also a lot of engineering and what have you.
[00:05:47] Satya Nadella: But that said I also sort of take the view that you know even what has been happening in the
[00:05:53] Satya Nadella: last 70 years of computing has also been a march that has helped us move. You know with as I said
[00:06:03] Satya Nadella: you know I like one of the things that Raj ready has as a metaphor for what AI is right he's
[00:06:09] Satya Nadella: is attuning a word winner of CMU and he's always and he had this even pre-AGI but he had this metaphor
[00:06:18] Satya Nadella: of AI should either be a guardian angel or a cognitive amplifier. I love that. It's a simple way
[00:06:24] Satya Nadella: to think about what this is ultimately what is it's human utility it is going to be a cognitive
[00:06:30] Satya Nadella: amplifier and a guardian angel and so if I sort of view it that way I view it as a tool but then
[00:06:37] Satya Nadella: you can also go very mystical about it and say well this is you know more than a tool it does all
[00:06:42] Satya Nadella: these things which only humans did so far but that has been the case with many technologies in the
[00:06:46] Satya Nadella: past only humans did a lot of things and then we add tools that did them. I guess we don't have to
[00:06:51] Dwarkesh Patel: get wrapped up in the definition here but maybe one way to think about is like maybe it takes five
[00:06:56] Dwarkesh Patel: years 10 years 20 years at some point eventually a machine is producing satya tokens right and the
[00:07:01] Dwarkesh Patel: Microsoft board things that satya tokens are worth a lot. How much how much are you wasting of
[00:07:05] Dwarkesh Patel: this of like economic value by interviewing such it's not for the API cost of satya tokens but so
[00:07:13] Dwarkesh Patel: you know whatever you want to call it is that are the satya tokens a tool or an agent whatever
[00:07:18] Dwarkesh Patel: right now if you have models that cost on the order of dollars or cents for million tokens
[00:07:22] Dwarkesh Patel: there's just an enormous room for expansion a margin expansion there where satya to a million
[00:07:29] Dwarkesh Patel: tokens of satya are like worth a lot and where does that margin go and what level of that margin
[00:07:36] Dwarkesh Patel: is Microsoft involved and is the question I have. So I think in some sense this goes back up and
[00:07:43] Satya Nadella: to essentially what's the economic growth picture going to really look like what's the fun going
[00:07:49] Satya Nadella: to look like what's productivity going to look like and that to me is where again if the industrial
[00:07:54] Satya Nadella: revolution created after whatever 70 years of diffusion is when you started seeing the economic growth
[00:08:00] Satya Nadella: right it took that's the other thing to remember is even if the tech is diffusing fast this time around
[00:08:09] Satya Nadella: for true economic growth to appear it has to sort of diffuse to a point where the work the work
[00:08:15] Satya Nadella: artifact and the work flow has to change and so that's kind of one place where I think the change
[00:08:20] Satya Nadella: management required for a corporation to truly change I think is something mission discount.
[00:08:25] Satya Nadella: So I think going forward do humans and the tokens they produce get higher leverage right whether
[00:08:33] Satya Nadella: it's the door cash or the Dylan tokens of the future I mean think about the amount of technology
[00:08:39] Satya Nadella: would you be able to run semi-analysis or this podcast without technology no chance right I mean
[00:08:45] Satya Nadella: scale that you have been able to achieve no chance so the question is what's that scale is it going
[00:08:50] Satya Nadella: to be 10x with something that comes through absolutely and therefore with your ramp to some revenue
[00:08:57] Satya Nadella: number or your ramp to some audience number or what happy and so that I think is what's going to
[00:09:02] Satya Nadella: happen right I mean the the point is that's whatever what took 70 years maybe 150 years for the
[00:09:09] Satya Nadella: industrial revolution may happen in 20 years 25 years that's a better way to like I would love to
[00:09:15] Satya Nadella: compress what happened in 200 years of the industrial revolution into 20 a period if you're lucky
[00:09:22] Dwarkesh Patel: so Microsoft historically has been perhaps you know the greatest software company the largest
[00:09:27] Dwarkesh Patel: software as a service company you know you've gone through a transition in the past where
[00:09:31] Dwarkesh Patel: you used to sell windows licenses and disks of windows or Microsoft and now you sell you know
[00:09:36] Dwarkesh Patel: subscriptions to 365 or as we go from sort of you know that transition to where your businesses today
[00:09:45] Dwarkesh Patel: there's also a transition going after that right software as a service incredibly low incremental cost
[00:09:51] Dwarkesh Patel: per user there's a lot of R&D there's a lot of customer acquisition cost this is why not Microsoft
[00:09:56] Dwarkesh Patel: but the SaaS companies have underformed massively in the markets because the cogs of AI is just so high
[00:10:02] Dwarkesh Patel: and that just completely breaks how these business models work how do you as a as perhaps the
[00:10:09] Dwarkesh Patel: greatest software company software as a service company transition Microsoft to this new age where
[00:10:15] Dwarkesh Patel: cogs matters a lot and the incremental cost per users is different right because right now you're
[00:10:20] Dwarkesh Patel: charging hey it's 20 bucks for co-pilot yeah so I think that this is a it's a great question because
[00:10:25] Satya Nadella: in some sense the business models themselves I think the levers are going to remain similar right
[00:10:30] Satya Nadella: which is if I look at the if if you look at the menu of models starting from like say consumer all
[00:10:37] Satya Nadella: the way right there will be some ad unit there will be some transaction there'll be some device
[00:10:43] Satya Nadella: gross margin for somebody who builds an AI device there will be subscriptions consumer and enterprise
[00:10:50] Satya Nadella: and then there'll be consumption right so I still think that that's kind of how those are all the
[00:10:55] Satya Nadella: meters to your point what is a subscription up to now people like subscriptions because they
[00:11:01] Satya Nadella: can budget for them right they are essentially entitlements to some consumption rights that come
[00:11:08] Satya Nadella: encapsulated in a subscription so that I think is what in some sense it becomes a pricing decision
[00:11:14] Satya Nadella: so how much consumption is in your entitled to is if you look at all the coding subscriptions
[00:11:21] Satya Nadella: that's kind of what they are right and they kind of have the pro tier the standard tier and what
[00:11:25] Satya Nadella: have you and so I think that's how the pricing will you know and the margin structures will get tiered
[00:11:33] Satya Nadella: the interesting thing is having at Microsoft the good news for us is we kind of are in that
[00:11:39] Satya Nadella: business all in all across all those meters in fact that as a portfolio level we pretty much have
[00:11:47] Satya Nadella: consumption subscriptions to all of the other consumer levers as well and then I think time will tell
[00:11:55] Satya Nadella: which of these models makes sense in what categories one thing on the SaaS sites since you brought up
[00:12:01] Satya Nadella: which I think a lot about is take Office 365 or Microsoft 365 I mean man having a low RPU is great
[00:12:09] Satya Nadella: because here's an interesting thing right during the transition from server to cloud one of the
[00:12:14] Satya Nadella: questions we used to ask ourselves is oh my god if all we did was just basically move the same
[00:12:20] Satya Nadella: users who were using let's call it our office licenses and our servers at that time office servers
[00:12:26] Satya Nadella: right to the cloud and we had cogs this is going to basically not only shrink our margins but it will
[00:12:33] Satya Nadella: be fundamentally a non profitable or in less profitable company except what happened was that
[00:12:38] Satya Nadella: move to the cloud expanded the market like crazy right I mean we sold a few servers in India didn't
[00:12:45] Satya Nadella: sell much whereas in the cloud suddenly everybody in India also could afford fractionally buying
[00:12:51] Satya Nadella: servers the IT cost them in fact the biggest thing I had not realized for example was the amount of
[00:12:57] Satya Nadella: money people were spending buying storage underneath SharePoint in fact EMCs biggest segment may have
[00:13:05] Satya Nadella: been storage servers for SharePoint all that sort of dropped in the cloud because nobody had to
[00:13:12] Satya Nadella: go buy in fact it is working capital basically it is cash flow out right and so it expanded the
[00:13:19] Satya Nadella: market massively so this AI thing will be that right so if you take coding what we built with
[00:13:28] Satya Nadella: GitHub and VS code in over one or a decade suddenly the coding assistant is that big in one year
[00:13:36] Satya Nadella: and so that I think is what's going to happen as well which is the market expands massively
[00:13:41] Satya Nadella: I guess there's a question of the market will expand will the parts of the revenue that
[00:13:46] Dwarkesh Patel: touch Microsoft expand so co-pilot is an example where if you look early this year I think I guess
[00:13:54] Dwarkesh Patel: according to Dylan's numbers the co-pilot revenue would get a co-pilot revenue was like 500
[00:13:59] Dwarkesh Patel: million or something like that and then there were like no close competitors whereas now you have
[00:14:05] Dwarkesh Patel: cloud code cursor and co-pilot with around similar revenue around a billion and then code x is
[00:14:10] Dwarkesh Patel: catching up around 700 800 million and so the question is across all the surfaces that Microsoft has
[00:14:15] Dwarkesh Patel: access to what is the advantage that Microsoft's equivalents of co-pilot have yeah by the way I love
[00:14:20] Satya Nadella: this chart you know I love this chart for so many reasons one is we're still on the top
[00:14:26] second is all these companies that are listed here are all companies that have been born in the
[00:14:32] Satya Nadella: last four five years yeah that to be is the best sign which is if you have new competitors new
[00:14:38] Satya Nadella: existential problems when you say man who's it now cloud's going to kill you cursor is going to
[00:14:43] Satya Nadella: kill you yeah it's not boring right so thank god like that means we are in the right direction
[00:14:48] Satya Nadella: but this is it right the fact that we went from nothing to this scale is the market expansion so
[00:14:55] Satya Nadella: this is like the cloud like stuff this fundamentally this category of coding and AI is probably going to
[00:15:01] Satya Nadella: be one of the biggest categories right it is a software factory category in fact it may be bigger
[00:15:06] Satya Nadella: than knowledge work yeah so I kind of want to keep myself open-minded about I mean we're going to
[00:15:11] Satya Nadella: have tough competition I think that's your point which I think is a great one but man like I'm glad
[00:15:17] Satya Nadella: we have we parlayed what we had into this and now we have to compete and so in the compete side
[00:15:26] Satya Nadella: even in the last quarter I think we just we did our quarterly announcement I think we grew from
[00:15:30] Satya Nadella: 20 to 26 million subs right so I feel good about our sub growth and where the direction or
[00:15:36] Satya Nadella: travel on that is but the more interesting thing that has happened is guess where all the
[00:15:42] Satya Nadella: repos of all these other guys who are generating lots and lots of code go to they're going to get up
[00:15:48] Satya Nadella: so it get hub is it an all-time high in terms of repo creation PRs everything so that in some
[00:15:56] Satya Nadella: sense we want to keep that open by the way that means we want to have that right because we don't
[00:16:00] Satya Nadella: want to conflate that with our own growth right interestingly enough we're getting one developer
[00:16:04] Satya Nadella: joining get up a second or something that is the stat I think and then 80% of them just fall
[00:16:10] Satya Nadella: into some get up copilot workflow just because there are and by the way many of these things will
[00:16:15] Satya Nadella: even use some of our coding code review agents which are by default on just because you can use it
[00:16:21] Satya Nadella: so we will have many many structural shots at this the thing that we're also going to do
[00:16:27] Satya Nadella: is what we did with get get the primitives of get up whether starting with get to issues to actions
[00:16:35] Satya Nadella: these are powerful lovely things because they kind of are all built around your repo so we want
[00:16:41] Satya Nadella: to extend that at last week at get up universe that's kind of what we did right so we said agent HQ
[00:16:48] was the conceptual thing that we said we're going to build out this is where for example you have
[00:16:52] Satya Nadella: a thing called mission control and you go to mission control and now I can fire off sometimes I
[00:16:58] Satya Nadella: describe it as the cable TV of all these AI agents because I'll have essentially packaged into one
[00:17:03] Satya Nadella: subscription codex, clad, you know cognition stuff anyone's agents, grok all of them will be there
[00:17:13] Satya Nadella: so I get one package and then I can literally go issue a task, steer them so they will all be working
[00:17:20] Satya Nadella: in their independent branches I can monitor them so I literally have because I think that's going
[00:17:26] Satya Nadella: to be one of the biggest places of innovation right because right now I want to be able to use
[00:17:31] Satya Nadella: multiple agents I want to be able to then digest the output of the multiple agents I want to be able
[00:17:35] Satya Nadella: to then keep a handle on my repo so it says come some kind of a heads up display that needs to be
[00:17:41] Satya Nadella: built and then for me to quickly steer and triage what the coding agents have generated that to
[00:17:47] Satya Nadella: me between VS code, GitHub and all of these new primitives we will build as mission control I think
[00:17:55] Satya Nadella: with a control plane observability I mean think about every one who is going to deploy all this
[00:18:00] Satya Nadella: will require a whole host of observability of what agent did what at what time to what code base
[00:18:06] Satya Nadella: so I feel that's the opportunity and at the end of the day your point is well taken which is
[00:18:11] Satya Nadella: we better be competitive and innovate and if we don't yes we will get toppled but I like the chart
[00:18:17] Satya Nadella: at least as long as we're on the top even with competition. The key point here is sort of that
[00:18:21] Dwarkesh Patel: GitHub will keep growing regardless of who's coding agent wins but that market only grows at you
[00:18:27] Dwarkesh Patel: know call it 10 15 20% which is way above GDP it's a great compounder but these AI coding agents
[00:18:33] Dwarkesh Patel: have grown from you know call it $500 million run rate at the end of last year which was basically
[00:18:37] Dwarkesh Patel: just GitHub Copilot to now the current run rate across you know GitHub Copilot, Cloud Code,
[00:18:43] Dwarkesh Patel: cursor, cognition, Windsor, Replet, Codex, OpenAI Codex that's that's that's run rating at $56
[00:18:50] Dwarkesh Patel: billion now for the Q4 of this year that's a 10x right and and when you look at hey what's the
[00:18:57] Dwarkesh Patel: tam of software agents is it is it the $2 trillion of wages you pay people or is it is it is it
[00:19:04] Dwarkesh Patel: something beyond that because every company in the world will now be able to you know develop
[00:19:09] Dwarkesh Patel: software more no question Microsoft takes a slice of that but you've gone from near 100% or
[00:19:16] Dwarkesh Patel: certainly way above 50% to you know sub 25% market share in just one year what is the sort of
[00:19:22] Dwarkesh Patel: confidence that people can get that Microsoft will be it goes back a little bit Dylan to sort of
[00:19:27] Satya Nadella: there's no birth right here that we should have any confidence other than to say hey we should
[00:19:32] Satya Nadella: go innovate and knowing the lucky break we have in some sense is that this category is going to
[00:19:39] Satya Nadella: be a lot bigger than anything we had high share it let's let me say it that way right in some
[00:19:44] Satya Nadella: sense you could say when we kind of had high share in VS Code we had high share in the repos for
[00:19:49] Satya Nadella: with GitHub and that was a good market but the point is even having a decent share in what is a
[00:19:56] Satya Nadella: much more expansive market right I mean you could say we had a high share in client server
[00:20:00] Satya Nadella: server computing we have much lower share than that in hyper scale but is it a much bigger business
[00:20:08] Satya Nadella: by orders of magnitude so at least there's existence proof that Microsoft has been okay
[00:20:13] Satya Nadella: even if our share position has not been as strong as it was as long as the markets we're competing
[00:20:20] Satya Nadella: in are creating more value and there are multiple winners so I think that's the stuff but I take
[00:20:26] Satya Nadella: your point that ultimately it all means you have to get competitive so I watch that every quarter
[00:20:32] Satya Nadella: and so that's why I think what I'm very optimistic that what we are going to do with GitHub HQ
[00:20:38] Satya Nadella: or Agent HQ turning GitHub into a place where all these agents come as I said we'll have multiple
[00:20:45] Satya Nadella: shots on goal on there right it need not be that hey some of these guys can succeed along with us
[00:20:51] Satya Nadella: and so it doesn't need to be just one winner and one subscription. I guess the reason to focus on
[00:20:57] Dwarkesh Patel: this question is that it's not just about GitHub but fundamentally about office and all the other
[00:21:02] Dwarkesh Patel: software that Microsoft offers which is that one vision you could have about how I perceive is that
[00:21:08] Dwarkesh Patel: look the models are going to keep being hobbled and you will need this direct visible
[00:21:15] Dwarkesh Patel: observability all the time and another vision is over time these models can now they're doing
[00:21:20] Dwarkesh Patel: tacitake two minutes in the future they'll be doing tacitake next time we did tacitake 10 30
[00:21:24] Dwarkesh Patel: minutes in the future maybe they're doing days worth of work autonomously and then the model
[00:21:29] Dwarkesh Patel: companies are charging thousands of dollars maybe for access to really a coworker which could
[00:21:35] Dwarkesh Patel: use any UI to communicate with their human and so forth and migrate between platforms so if
[00:21:42] Dwarkesh Patel: we're getting closer to that why aren't the model companies that are just getting more and more
[00:21:47] Dwarkesh Patel: profitable the ones that are taking all the margin why is the the place where this scaffolding
[00:21:52] Dwarkesh Patel: happens which becomes less and less relevant to say as become more capable going to be that
[00:21:55] Dwarkesh Patel: important and that goes to you know office as it exists now versus co-workers that are just
[00:22:00] Dwarkesh Patel: doing knowledge with the conversation. I mean I think that's a great example I mean this is where
[00:22:04] Satya Nadella: you know does all the value migrate just to the model and or does the you know does it get split
[00:22:12] Satya Nadella: between the scaffolding and the model and what have you I think that time will tell but my
[00:22:20] Satya Nadella: fundamental point also is the incentive structure gets clear right which is if you take
[00:22:25] Satya Nadella: let's take let's take information what take even coding now already in fact one of the
[00:22:31] Satya Nadella: favorite settings I have in GitHub co-pilot is called auto right which will just optimize in
[00:22:38] Satya Nadella: fact I buy a subscription the auto one will start picking and optimizing for what I am asking
[00:22:45] Satya Nadella: it to do and it could even be fully autonomous and it could sort of arbitrage the tokens available
[00:22:51] Satya Nadella: across multiple models to go get a test done so if that is the that mean that if you take that
[00:22:57] Satya Nadella: argument the commodity there will be models and especially with open source models you can pick a
[00:23:03] Satya Nadella: checkpoint and you can take a bunch of your data and you're seeing it right I think all of us
[00:23:08] Satya Nadella: will start you whether it's from cursor or from Microsoft you'll start seeing some in house models
[00:23:13] Satya Nadella: even which will and then you'll offer out most of your tasks to it so I think that one argument is
[00:23:20] Satya Nadella: if you win the scaffolding which today is dealing with all the hobbling problems or the
[00:23:28] Satya Nadella: the jaggedness of this intelligence problems which you kind of have to if you win that then you
[00:23:34] Satya Nadella: will vertically integrate yourself into the model just because you will have the liquidity of the
[00:23:39] Satya Nadella: data and what have you and there are enough and more checkpoints that are going to be available
[00:23:43] Satya Nadella: that's the other thing I show structurally I think there will always be an open source model
[00:23:49] Satya Nadella: that will be fairly capable in the world that you could then use as long as you have something
[00:23:56] Satya Nadella: that you can use that with which is data and a scaffolding right so I can make the argument that oh my
[00:24:02] Satya Nadella: god if you're a model company you may be you may have a winners curse you may have done all the hard
[00:24:07] Satya Nadella: work done unbelievable innovation except it's kind of like one copy away from that being commoditized
[00:24:17] Satya Nadella: and then the person who has the data for grounding and context engineering and the liquidity of
[00:24:24] Satya Nadella: data can then go take that checkpoint and train it so I think the argument can be made both ways
[00:24:30] Satya Nadella: unpacking sort of what she said there's two views of the world right one is that models there's
[00:24:34] Dwarkesh Patel: so many different models out there open source exists there will be differences between the models
[00:24:39] Dwarkesh Patel: that will drive some level of you know who wins and who doesn't but the scaffolding is what
[00:24:43] Dwarkesh Patel: enables you to win yeah the other view is that actually models are the key IP and yes we're in a
[00:24:50] Dwarkesh Patel: very everyone's in a tight race and there's some you know hey I can use inthropic or open AI and
[00:24:55] Dwarkesh Patel: you can see this in the revenue charts right like open AI's revenue started skyrocketing once they
[00:24:59] Dwarkesh Patel: finally had a code model similar capabilities to anthropic although in different ways there's
[00:25:05] a view that like the model companies are actually the ones that garner all the margin right because
[00:25:10] Dwarkesh Patel: you know if you look across this year at least on an anthropic their gross margins on inference went
[00:25:14] Dwarkesh Patel: from you know well below 40% to north of 60 right by the end of the year these the margins are
[00:25:21] Dwarkesh Patel: expanding their despite hey more Chinese open source models than ever yeah open AI's competitive hey
[00:25:25] Dwarkesh Patel: Google's competitive hey X-Grok is now competitive right all these all these companies are now competitive
[00:25:30] Dwarkesh Patel: and yet despite this the margins have expanded at the model layer significantly yeah how do you
[00:25:36] Dwarkesh Patel: think about the it's a great question I mean I think the one thing is perhaps a few years ago
[00:25:43] Satya Nadella: people were saying oh I can just wrap a model and build a successful company and that I think
[00:25:49] Satya Nadella: is probably gotten debunked just because the model capabilities and with tools used in particular
[00:25:56] but the interesting thing is there's no like when I look at office 36 well let's take even this
[00:26:00] Satya Nadella: little thing we built called excel agent it's interesting right excel agent is not a UI level
[00:26:06] Satya Nadella: wrapper it's actually a model that is in the middle tier in this case because we have all the
[00:26:14] Satya Nadella: IP from the the GPT family we are taking that and putting it into the core middle tier of the office
[00:26:22] Satya Nadella: system to both teach it what it means to natively understand excel everything in it so it's not just
[00:26:31] Satya Nadella: where I just have a pixel level understanding I have a not full understanding of all the native
[00:26:35] Satya Nadella: artifacts of excel both when I see it like because if you think about it if I'm going to give it
[00:26:41] Satya Nadella: some reasoning task right I need to even fix the reasoning mistakes I make and so that means I need
[00:26:46] Satya Nadella: to both not just see the pixels I need to be able to see oh I got that formula wrong and I need to
[00:26:51] Satya Nadella: understand that and then so to some degree that's all being done not at the UI wrapper level with
[00:26:56] Satya Nadella: some prompt but it's being done in the middle tier by teaching it all the tools of excel right so
[00:27:01] Satya Nadella: I'm giving it even essentially a markdown to teach it the skills of what it means to be a
[00:27:06] Satya Nadella: sophisticated excel user so it's a weird thing that it goes back a little bit to AI brain right which
[00:27:12] Satya Nadella: is you're building not just excel you are now business logic in its traditional sense you're
[00:27:19] Satya Nadella: taking the excel business logic in the traditional sense and wrapping essentially a cognitive layer
[00:27:24] Satya Nadella: to it using this model which knows how to use the tool so in some sense excel will come with an
[00:27:31] Satya Nadella: analyst bundled in and with all the tools used that's the type of stuff that'll get built by
[00:27:38] Satya Nadella: everybody so even for the model companies they allow to compete right so if they're price
[00:27:42] Satya Nadella: stuff high guess what if I'm a builder of a tool like this I'll substitute you I mean use you
[00:27:49] Satya Nadella: for a while and so as long as this competition there's always a winner take all thing right if there's
[00:27:54] Satya Nadella: won't be one model that is better than everybody else with massive distance yes that's a winner take all
[00:27:59] Satya Nadella: as long as there's going to be competition where there's multiple models just like hyper scale
[00:28:03] Satya Nadella: competition and there's an open source check there is enough room here to go build value on top of
[00:28:10] Satya Nadella: models but at Microsoft the way I look at it and say is we're going to be in the hyper scale business
[00:28:17] Satya Nadella: which will support multiple models we will have access to open AI models for you know seven more
[00:28:23] Satya Nadella: years which we will innovate on top off so royalty for essentially I think of ourselves as having
[00:28:29] Satya Nadella: a frontier class model that we can use and innovate on with full flexibility and we'll build our own
[00:28:35] Satya Nadella: models with M.A.I. and and so we will always have a model level and then we'll build these whether
[00:28:43] Satya Nadella: it's insecurity whether it's in knowledge work whether it's encoding or in science we will build
[00:28:48] Satya Nadella: our own application scaffolding which will be modeled forward right it won't be a wrapper on a model
[00:28:54] Satya Nadella: but the model will be wrapped into the application I have so many questions about the other things
[00:29:00] Dwarkesh Patel: you mentioned but before we move on to those topics I still wonder whether this is like not
[00:29:06] Dwarkesh Patel: forward looking on the capabilities where you're imagining models like the exist today where yeah I
[00:29:12] Dwarkesh Patel: can you have to like it takes a screenshot of your screen but it can't like look inside each cell
[00:29:16] Dwarkesh Patel: and what the formula is and I think the better mental modded here is like look a human just imagine
[00:29:20] Dwarkesh Patel: that these models actually will be able to actually use a computer as well as a human and a human
[00:29:25] Dwarkesh Patel: knowledge worker who is using Excel can look into the formulas can you know use alternative software
[00:29:31] Dwarkesh Patel: can migrate data between office 365 and another piece of software if the migration is necessary etc so
[00:29:37] Dwarkesh Patel: that's what I'm saying but what but if that's the case then the integration with Excel doesn't matter
[00:29:42] Dwarkesh Patel: that much no no I don't worry about the Excel integration after all Excel was built as a tool for
[00:29:48] Satya Nadella: analysts great so whoever is this AI that is an analyst should have tools that they can use
[00:29:56] Satya Nadella: the computer right the just the way a human can use a computer that's their tool the tool is the
[00:30:00] Satya Nadella: computer right all right so that so all I'm saying is I'm building an analyst as as essentially an
[00:30:06] Satya Nadella: AI agent which happens to come with an a priori knowledge of how to use all of these analytical tools
[00:30:14] Satya Nadella: but is it is it something a little maybe just just to make sure we're talking about the same thing
[00:30:18] Dwarkesh Patel: is it a thing that a huge like me using Excel as a podcast or another efficient Excel like a completely
[00:30:24] Dwarkesh Patel: autonomous so just imagine I work like so we should now maybe sort of lay out how I think the future
[00:30:30] Satya Nadella: of the company is right the future of the company would be the tools business which I have a
[00:30:35] Satya Nadella: computer I use Excel and in fact in the future I'll even have a co-pilot and that co-pilot will
[00:30:41] Satya Nadella: also have agents right that's still I am you know it's still me steering everything yeah and
[00:30:46] Satya Nadella: everything is coming back so that's kind of one world yeah then the second world is the company
[00:30:52] Satya Nadella: just literally provisions a computing resource for an AI agent yeah and that is working fully
[00:30:58] Satya Nadella: autonomously yeah that fully autonomous agent will have essentially embodied set of those same tools
[00:31:06] Satya Nadella: right uh that are available to it right so this AI tool that comes in also has not just a raw
[00:31:13] Satya Nadella: computer because it's going to be more token efficient to use tools to get stuff done in fact I
[00:31:19] Satya Nadella: kind of look at it and say our business which today is an end user tools business will become
[00:31:24] Satya Nadella: essentially an infrastructure business in support of agents doing work is another way to think
[00:31:29] Satya Nadella: about it right so if one of the things that you'll see us do and in in in fact like all the stuff
[00:31:35] Satya Nadella: we built underneath m365 still is going to be very relevant uh you need someplace to store it some
[00:31:43] Satya Nadella: place to do archival some place to do discovery some place to manage all of these activities
[00:31:49] Satya Nadella: even if you're an AI agent so that's so it's kind of a new infrastructure so just to make sure
[00:31:55] Dwarkesh Patel: I understand you're saying like look theoretically a future AI that has actual computer use which
[00:32:01] Dwarkesh Patel: all these companies are working on model companies are working right now could use even if it's not
[00:32:05] Dwarkesh Patel: partnered with Microsoft or under our umbrella could use Microsoft software but you're saying we're
[00:32:10] Dwarkesh Patel: going to give them if if you're working with our infrastructure we're going to give you like
[00:32:15] Dwarkesh Patel: lower level access that makes it more efficient for you to do the same things you could have
[00:32:18] Dwarkesh Patel: otherwise than anyways hundred percent I mean so the entire thing in in fact the way the you know
[00:32:23] Satya Nadella: like what happened is we had servers then there was virtualization and they were had many more
[00:32:29] Satya Nadella: servers so that's it another way to think about this which is hey don't think of the the tool as
[00:32:34] Satya Nadella: the end thing what is the entire substrate underneath that tool that humans use and that entire
[00:32:41] Satya Nadella: substrate is the bootstrapped for the AI agent as well because the AI agent needs a computer
[00:32:46] Satya Nadella: that's kind of one like you know so in fact one of the fascinating things we're seeing a significant
[00:32:51] Satya Nadella: amount of growth is all these guys who are doing these office artifacts and and what have you as
[00:32:56] Satya Nadella: autonomous agents and so on want to provision windows 365 right they really want to be able to
[00:33:02] Satya Nadella: provision a computer for these agents and so absolutely and that's why I think we're going to have
[00:33:08] Satya Nadella: essentially an end user computing infrastructure business which I think is going to just keep growing
[00:33:14] Satya Nadella: because guess what it's going to grow faster than the number of users so in fact that's kind of
[00:33:18] Satya Nadella: one of the other questions people asked me is hey what happens to the per user business at least
[00:33:22] Satya Nadella: the early signs maybe the way to think about the per user business is not just per user it's per agent
[00:33:28] Satya Nadella: and if you sort of say it's per user and per agent the key is what's the stuff to provision for every
[00:33:34] Satya Nadella: agent a computer a set of security things around it an identity around it and all those things are
[00:33:43] Satya Nadella: observability and so on are the management layers and that's I think all going to get baked into that
[00:33:48] Satya Nadella: the way to frame it at least the way I currently think about it and I'd like to hear your you know your
[00:33:52] Dwarkesh Patel: view is that these model companies are all building environments to yeah train their models to use
[00:33:58] Dwarkesh Patel: excel or amazon shopping or whatever whatever it is book flights but at the same time they're also
[00:34:05] Dwarkesh Patel: training these models to do migration from because that that is probably the most immediate
[00:34:11] Dwarkesh Patel: valuable thing right converting mainframe based systems to standard cloud systems converting
[00:34:17] Dwarkesh Patel: excel databases into real databases with SQL right or converting you know what is done in word
[00:34:25] Dwarkesh Patel: in excel to something that is more programmatic and more efficient in a classical sense that can
[00:34:30] Dwarkesh Patel: actually be done by humans as well it's just not cost effective for the software developer to do that
[00:34:35] Dwarkesh Patel: that seems to be what everyone is going to do with AI for the next you know a few years at least
[00:34:39] Dwarkesh Patel: to massively drive value how does Microsoft fit into that if the models can utilize the tools
[00:34:47] Dwarkesh Patel: themselves to migrate to something and yes Microsoft has you know a leadership position in databases
[00:34:52] Dwarkesh Patel: and in storage and in all these other categories but the use of say a office ecosystem is going to be
[00:35:01] Dwarkesh Patel: significant less just like potentially the use of a mainframe ecosystem could be potentially less
[00:35:05] Dwarkesh Patel: now mainframes have grown for the last two decades actually even though no one talks about them
[00:35:08] Dwarkesh Patel: anymore they've still grown yeah how does how does that for the end of the day this is not about
[00:35:14] Satya Nadella: sort of hey there is going to be a significant amount of time where there's going to be a hybrid world
[00:35:20] Satya Nadella: right because people are going to be using the tools that are going to be working with agents that
[00:35:23] Satya Nadella: have to use tools and by the way they have to communicate with each other what's the artifact I
[00:35:28] Satya Nadella: generate that then a human needs to see so like all of these things will be real considerations in
[00:35:33] Satya Nadella: any place so the outputs input so I don't think it'll just be about oh I migrated off right but the
[00:35:37] Satya Nadella: bottom line is I have to live in this hybrid world so let but that doesn't fully answer your
[00:35:42] Satya Nadella: question because there can be a real new efficient frontier where I mean it's just agents working
[00:35:47] Satya Nadella: with agents and completely optimizing and even when agents are working with agents what are the
[00:35:52] Satya Nadella: primitives that are needed do you need a storage system does that storage system need to have
[00:35:59] Satya Nadella: e-discovery does that e-discovery do you need to have observability do you need to have an
[00:36:03] Satya Nadella: identity system that is going to use multiple models with all having one identity system so these
[00:36:09] Satya Nadella: are all the core underlying rails we have today for what are the office systems or what have you
[00:36:16] Satya Nadella: and that's what I think we will have in the future as well think you talked about databases right I
[00:36:20] Satya Nadella: mean take you know man I would love all of excel to have a database back in right in fact I would
[00:36:25] Satya Nadella: love for all that to happen immediately and that database is a good database I mean databases in
[00:36:30] Satya Nadella: fact will be a big thing that will grow in fact if I think about all of the office artifacts
[00:36:37] Satya Nadella: being structured better the ability to do the joins between structure and unstructured better
[00:36:42] Satya Nadella: because of the agenting what that'll grow the underlying what is infrastructure business it
[00:36:47] Satya Nadella: happens the consumption of that is all being driven by agents you could say all that is just in time
[00:36:52] Satya Nadella: generated software by a model company that could also be true if we we will be one such model
[00:36:57] Satya Nadella: company too and so we will build in so the competition could be that we will build a model plus
[00:37:04] Satya Nadella: all the infrastructure and provision it and then there will be competition between a bunch of
[00:37:09] Satya Nadella: those folks who can do that I guess speaking of model companies you say okay we will also be one
[00:37:15] Dwarkesh Patel: of the not only will have the infrastructure we'll have the model itself right now Microsoft AI
[00:37:19] Dwarkesh Patel: is most recent model that was released two months ago is 36 in Chabot Arena and there's a
[00:37:24] Dwarkesh Patel: I mean you obviously have the IP rights to open AI so there's a question of first to the extent
[00:37:29] Dwarkesh Patel: you agree with that it seems to be behind why is that the case especially given the fact that you
[00:37:33] Dwarkesh Patel: could you theoretically have the right to just like fork open AI's monorepa or distill on their models
[00:37:41] Dwarkesh Patel: yeah especially if it's a big part of your strategy that we need to have a leading model company
[00:37:45] Dwarkesh Patel: yeah I mean so first of all we are absolutely going to use the open AI models to the maximum
[00:37:52] Satya Nadella: across all of our products right I mean that's I think the core thing that we're going to continue to
[00:37:57] Satya Nadella: do all the way for the next seven years and not just use it but then add value to it that's kind of
[00:38:04] Satya Nadella: where the analyst in this Excel agent and these are all things that we will do where we know we'll do
[00:38:10] Satya Nadella: our alphine tuning we'll do some mid-training runs on top of a GPT family where we have unique
[00:38:15] Satya Nadella: data assets and build capability the M.A.I model the way I think we're going to think about it is
[00:38:22] Satya Nadella: the the good news here in fact with the new agreement is even we can be very very clear that we
[00:38:27] Satya Nadella: are going to build a world class super intelligence team and go after it with high ambition but at the
[00:38:32] Satya Nadella: same time we're also going to use this time to be smart about how to use both these things so
[00:38:38] Satya Nadella: that means we will on one end be very product focused on on the other end be very research focused
[00:38:44] Satya Nadella: in other words because we have access to the GPT family the last thing I don't want to do is use
[00:38:50] Satya Nadella: my flops in a way that is just duplicative and doesn't add much value so I want to be able to take
[00:38:57] Satya Nadella: the flops that we use to generate a GPT family and maximize its value while my M.A.I flops are being
[00:39:05] Satya Nadella: used for let's take the image model that we launched which I think this launched is a number nine
[00:39:10] Satya Nadella: in the imagery now you know we're using it you know both for cost optimization it's on
[00:39:15] Satya Nadella: co-pilot it's in Bing and we're going to use that we have an audio model in co-pilot which
[00:39:20] Satya Nadella: has got personality and what have you we optimized it for our product so we will do those even on
[00:39:26] Satya Nadella: the LM arena we started on the text one I think it was it debuted at night 13 and by the way it
[00:39:31] Satya Nadella: was it was done only on whatever 15,000 H100s and so it was a very small model and so it was
[00:39:38] Satya Nadella: again to prove out the core capability the instruction following and everything else which you know
[00:39:44] Satya Nadella: we wanted to make sure we can match what was state of the art and so that shows us given scaling
[00:39:49] Satya Nadella: laws what we are capable of doing if it gave more flops to it right so the next thing we will do
[00:39:54] Satya Nadella: is an omnimodel where we will take sort of the work we have done in audio what we have done in
[00:39:59] Satya Nadella: image and what we have done in text that'll be the next pit stop on the M.A.I side so when I think
[00:40:04] Satya Nadella: about the M.A.I roadmap we're going to build a first class super intelligence team we're going to
[00:40:08] Satya Nadella: continue to drop and do on in the open some of these models they will either be in our products
[00:40:14] Satya Nadella: being used because they're going to be latency friendly cogs friendly or what have you or they'll
[00:40:19] Satya Nadella: have some special capability and we will do real research in order to be ready for some next 5, 6,
[00:40:25] Satya Nadella: 7, 8 breakthroughs that are all needed on this march towards super intelligence so I think that's
[00:40:31] Satya Nadella: and while exploiting the advantage we have of having the gpt family that we can work on top of as
[00:40:38] Satya Nadella: well. Savvy Row 4.7 years you no longer have access to open-air models what does one get
[00:40:45] Dwarkesh Patel: confidence or what does Microsoft do to make sure they are leading or have a leading AI lab right
[00:40:51] Dwarkesh Patel: today you know it's open-air is developed many of the breakthroughs whether it be scaling or
[00:40:55] Dwarkesh Patel: reasoning or Google has developed all the breakthroughs like transformers but it is also a big talent
[00:41:01] Dwarkesh Patel: game right you know you've seen meta spend you know north of $20 billion on talent right you've
[00:41:07] Dwarkesh Patel: seen an anthropic poached the entire blue shift reasoning team from Google last year you've seen
[00:41:12] Dwarkesh Patel: meta poached a large reasoning and post training team from Google more recently these these
[00:41:17] Dwarkesh Patel: sorts of talent wars are very capital intensive they're the ones that you know arguably you know
[00:41:22] Dwarkesh Patel: if you're spending $100 billion on infrastructure you should also spend you know x amount of money
[00:41:27] Dwarkesh Patel: on on the people using the infrastructure so that they're more efficiently making these new breakthroughs
[00:41:32] Dwarkesh Patel: what what confidence can one get that you know hey Microsoft will have a team that's world class
[00:41:36] Dwarkesh Patel: that can make these breakthroughs and you know once you decide to turn on the money faucet you know
[00:41:41] Dwarkesh Patel: you're being a bit capital efficient right now which is which is smart it seems to not waste money
[00:41:45] Dwarkesh Patel: doing duplicative work but once you decide you need to you know how how can one say oh yeah now you
[00:41:51] Dwarkesh Patel: can shoot up to where the top five model oh look I mean at the end of the day we're going to build a
[00:41:56] Satya Nadella: world class team and we already have a world class team that's beginning to be sort of assemble right
[00:42:01] Satya Nadella: with Mustafa coming in we have Karen we have Omar Subramaniam we did a lot of the post training at
[00:42:06] Satya Nadella: Gemini to five who is at Microsoft Nando who did a lot of the multimedia work at DeepMind is there
[00:42:12] Satya Nadella: and so we're going to build a world class team and in fact I think later this week even Mustafa
[00:42:17] Satya Nadella: published some you know a little more clarity on what our lab is going to go do I think the thing
[00:42:23] Satya Nadella: that I want the world to know perhaps is we are going to build the infrastructure that'll support
[00:42:31] Satya Nadella: multiple models you know we because from a hyperscale perspective we want to build the most
[00:42:38] Satya Nadella: scaled infrastructure fleet that's capable of supporting all the models the world needs whether
[00:42:44] Satya Nadella: it's from open source or obviously from open AI and others and so that's kind of one job
[00:42:48] Satya Nadella: second is in our own model capability we will absolutely use the open AI model in our products
[00:42:54] Satya Nadella: and we will start building our own models and we may like in in get up copilot and
[00:42:58] Satya Nadella: thropic is used so we will even have other frontier models that are going to be wrapped into our
[00:43:03] Satya Nadella: products as well so I think that that's kind of how at least each time at the end of the day the
[00:43:08] Satya Nadella: eval of the product as it meets a particular task or a job is what matters and we'll sort of back
[00:43:14] Satya Nadella: from there into the vertical integration needed knowing that as long as you're serving the market
[00:43:21] Satya Nadella: well with the product you can always cost optimize there's a question going forward so right now
[00:43:27] Dwarkesh Patel: we have models that have this distinction between training and inference and one could argue that
[00:43:32] Dwarkesh Patel: there's like a smaller and smaller difference between the different models going forward if you're
[00:43:37] Dwarkesh Patel: really expecting something like human level intelligence humans learn on the job you know if you
[00:43:42] Dwarkesh Patel: think about your last 30 years what makes saite token so valuable it's the last 30 years of wisdom
[00:43:46] Dwarkesh Patel: and experience you've gained in Microsoft and we will eventually have models if they get to human
[00:43:51] Dwarkesh Patel: level which will have this ability to continuously learn on the job and that will drive so much value
[00:43:56] Dwarkesh Patel: to the model company that is ahead at least in my view because you have copies of one model broadly
[00:44:01] Dwarkesh Patel: before through the economy learning how to do every single job and unlike humans they can amalgamate
[00:44:06] Dwarkesh Patel: their learnings to that model so there's this sort of continuous learning sort of exponential
[00:44:11] Dwarkesh Patel: feedback loop which almost looks like a sort of intelligence explosion if that happens and
[00:44:18] Dwarkesh Patel: Microsoft isn't the leading model company by that time doesn't then this you know you're saying well
[00:44:25] Dwarkesh Patel: we substitute one model for another etc matter less because it's just like this one model knows how
[00:44:29] Dwarkesh Patel: to do every single job in the economy the other long tail don't yeah no I think your point about if
[00:44:34] Satya Nadella: there's one model that is the only model that's most broadly deployed in the world and it sees
[00:44:39] Satya Nadella: all the data and it does continuous learning that's game set match and you know it's such sharp
[00:44:44] Satya Nadella: right I mean the the reality at least I see is the world even today for all the dominance of
[00:44:55] Satya Nadella: any one model it's not the case it's like take any take coding there's multiple models in fact
[00:45:02] Satya Nadella: every day it's less the case where there is not one model that is getting deployed broadly in
[00:45:08] Satya Nadella: fact there's multiple models that are getting deployed it's kind of like databases right it's
[00:45:12] Satya Nadella: always the thing is like hey can one database be the one that just is used everywhere except it's not
[00:45:18] Satya Nadella: there are multiple types of databases that are getting deployed for different use cases so I think
[00:45:24] Satya Nadella: that there is going to be some network effects of continual learning or data you know I'll call
[00:45:30] Satya Nadella: liquidity that any one model has is it going to happen in all domains I don't think so is it
[00:45:36] Satya Nadella: going to happen in all geos I don't think so is it going to happen in all segments I don't think so
[00:45:40] Satya Nadella: it'll happen all categories at the same time I don't think so so therefore I feel like the design
[00:45:44] Satya Nadella: space is so large that there's plenty of opportunity but your fundamental point is having a
[00:45:51] Satya Nadella: capability which is at the infrastructure layer model layer and at the scaffolding layer and then
[00:45:58] Satya Nadella: to be able to compose these things not just as a vertical stack but to be able to compose each
[00:46:03] Satya Nadella: thing for what its purpose is right you can build an infrastructure that's optimized for one model if
[00:46:08] Satya Nadella: you do that what if you go fall behind in fact all the infrastructure you built will be a waste
[00:46:14] Satya Nadella: right you kind of need to build an infrastructure that's capable of supporting multiple sort of
[00:46:19] Satya Nadella: families and lineages or models otherwise the capital you put in which is optimized for one
[00:46:24] Satya Nadella: model architecture that means you're one tweak away from some MOE like breakthrough that happens
[00:46:29] Satya Nadella: for somebody else in your entire network topology goes out of the window then that's a scary thing
[00:46:34] Satya Nadella: right so therefore you kind of want the infrastructure to support whatever may come in fact in your
[00:46:40] Satya Nadella: own model family and other model families and you got to be open if you're if you're serious about
[00:46:44] Satya Nadella: the hyper-skill business you've got to be serious about that right if you're a series about being
[00:46:49] Satya Nadella: a model company you've got to basically say hey what are the ways people can actually do
[00:46:54] Satya Nadella: things on top of the model so that I can have an ISV ecosystem unless I'm thinking I'll own
[00:46:59] Satya Nadella: every category that just can't be that then you won't have an API business and that by definition
[00:47:04] Satya Nadella: will mean you'll never be a platform company that's going to be successfully deployed everywhere
[00:47:08] Satya Nadella: right so therefore the industry structure is such that it will really force people to specialise
[00:47:18] Satya Nadella: and that in that specialization a company like Microsoft should compete in each layer by its
[00:47:26] Satya Nadella: merits but not think that this is all about all a road to gameset match where I just compose
[00:47:32] Satya Nadella: vertically all these layers that just doesn't happen so according to Dylan's numbers there's
[00:47:38] Dwarkesh Patel: going to be half a trillion in AI CapEx next year alone and labs are already spending billions of
[00:47:43] Dwarkesh Patel: dollars to snack top researcher talent but none of that matters if there's not enough high-quality
[00:47:48] Dwarkesh Patel: data to train on without the right data even the most advanced infrastructure and world-class talent
[00:47:54] Dwarkesh Patel: won't translate into end value for the user that's where libelbox comes in libelbox produces
[00:48:00] Dwarkesh Patel: high quality data at massive scale powering any capability that you want your model to have
[00:48:06] Dwarkesh Patel: it doesn't matter whether you need a coding agent that needs detailed feedback on multi-hour
[00:48:10] Dwarkesh Patel: trajectories or robotics model that needs thousands of samples on everyday tasks or a voice
[00:48:15] Dwarkesh Patel: agent that can also perform real-world actions for the user like booking them a flight to be clear
[00:48:20] Dwarkesh Patel: this isn't just off-the-shelf data libelbox can design and launch a custom production scale
[00:48:27] Dwarkesh Patel: data pipeline in 48 hours and they can get you tens of thousands of targeted examples in weeks
[00:48:33] Dwarkesh Patel: reach out to at libelbox.com slash thru our cache all right back to satya
[00:48:40] Dwarkesh Patel: so last year microsoft was on path to be the largest infrastructure provider by far you were
[00:48:47] Dwarkesh Patel: the earliest in 23 so you went out there you acquired all the resources in terms of leasing data
[00:48:51] Dwarkesh Patel: center starting construction securing power everything you guys were on pace to beat amazon in
[00:48:56] Dwarkesh Patel: 26 or 27 but certainly by 28 you're going to beat them since then you you know in let's call
[00:49:04] Dwarkesh Patel: the second half last year microsoft did this big pause right where they let go of a bunch of
[00:49:09] Dwarkesh Patel: leasing sites that they were going to take which then google met amazon in some cases oracle
[00:49:16] Dwarkesh Patel: took these sites we're sitting in one of the largest data centers in the world so obviously it's
[00:49:19] Dwarkesh Patel: not everything you guys are expanding like crazy but there are sites that you just stop working
[00:49:24] Dwarkesh Patel: why why did you do this right yeah i mean the fundamental thing we this goes back a little bit
[00:49:31] Satya Nadella: to what is the hyperscale business all about right which is one of the key decisions we made
[00:49:37] Satya Nadella: was that if you're going to build out Azure to be fantastic for all sort of stages of AI
[00:49:46] Satya Nadella: from training to mid-training to data gen to inference we just need fungibility off the fleet
[00:49:54] Satya Nadella: and and so that entire thing caused us not to basically go build a whole lot of capacity with a
[00:50:04] Satya Nadella: particular set of generations because the other thing that you got to realize is having actually
[00:50:10] Satya Nadella: for now up to now 10x to every 18 months in our training capacity for the various open AI models
[00:50:17] Satya Nadella: we realize that the key is to stay on that path but the more important thing is to actually have a
[00:50:25] Satya Nadella: balance to not just train but to be able to serve these models all around the world because at the
[00:50:30] Satya Nadella: end of the day the rate of monetization is what then will allow us to even keep funding and then
[00:50:36] Satya Nadella: the infrastructure was going to need us to support as i said multiple models and what have you so
[00:50:41] Satya Nadella: once we said that that's the case since then we just course corrected to where the path we're on
[00:50:47] Satya Nadella: right if i look at the path we're on is we are doing lot more starts now we're also buying up
[00:50:53] Satya Nadella: as managed capacity as we can but that is to build whether it's to lease or even GPUs as a service
[00:50:59] Satya Nadella: but we are building it for where we see the demand and the serving needs and our training needs
[00:51:05] Satya Nadella: and we didn't want to just be a host star for one company and have just a massive book of business
[00:51:13] Satya Nadella: with one customer that that's not a business right that is sort of you know you should be
[00:51:17] Satya Nadella: working integrated with that company yeah and so given the the thing that open AI was going to be
[00:51:23] Satya Nadella: a successful independent company which is fantastic right i think it's makes sense right and even
[00:51:27] Satya Nadella: metame use third party capacity but ultimately they're all going to be first party for anyone who has
[00:51:34] Satya Nadella: large scale they'll be you know they'll be a hyper-scaler on their own and so to me was to build out
[00:51:41] Satya Nadella: a hyper-scale fleet and our own research compute and that's what the adjustment was um you know
[00:51:47] Satya Nadella: and and so i feel very very good oh by the way the other thing is i didn't want to get stuck
[00:51:53] Satya Nadella: with massive scale of one generation i mean we just saw the the gb 200s i mean the gb 300s are coming
[00:51:59] Satya Nadella: right and by the time i get to where rubin where rubin ultra guess what the data center is going to
[00:52:05] Satya Nadella: look very different because the power per rack power per row is going to be so different uh the
[00:52:11] Satya Nadella: cooling requirements are going to be so different and that that means i don't want to just go build
[00:52:15] Satya Nadella: out like a whole number of gigawatts that are only for a one generation one family and so i think
[00:52:22] Satya Nadella: the pacing matters and the fungibility and the location matters uh the workload diversity matters
[00:52:30] Satya Nadella: customer diversity matters and that's what we're building towards the other thing that we've learned a lot
[00:52:34] Satya Nadella: is um every AI workload does require not only the AI accelerator but it requires a whole lot of
[00:52:41] Satya Nadella: other things right and in fact a lot of the margin structure for us will be in those other things
[00:52:46] Satya Nadella: and so therefore we want to build out azure as being fantastic for the long tail of the work loads
[00:52:53] Satya Nadella: because that's the hyperscale business while knowing that we've got to be super competitive starting
[00:52:58] Satya Nadella: with the bare metal for the highest end training and but that can't crowd out the rest of the business
[00:53:05] Satya Nadella: right because we're not in the business of just doing five contracts with five customers
[00:53:10] Satya Nadella: being their bare metal service that's not a a Microsoft business that maybe a business for someone
[00:53:15] Satya Nadella: else and that's a good thing what we have said is we are in the hyperscale business which is at the
[00:53:20] Satya Nadella: end of the day a long tail business uh for AI workloads and in order to do that we will have some
[00:53:27] Satya Nadella: leading bare metal as a service capabilities for a set of models including our own uh and that
[00:53:34] Satya Nadella: I think is the balance you see the another sort of question that comes around this whole fungibility
[00:53:38] Dwarkesh Patel: topic is okay it's not where you want it right you would rather have it in a good population center
[00:53:43] Dwarkesh Patel: like at Lanta's here we're here um there there's there's also the question of like well how much does
[00:53:48] Dwarkesh Patel: that matter if as the horizon of AI task grows well actually you know 30 seconds for a reasoning
[00:53:55] Dwarkesh Patel: prompt or you know 30 minutes for a deep research or you know it's going to be hours for software
[00:54:00] Dwarkesh Patel: agents at some point um and days and so on and so forth the time to human interaction what does it
[00:54:05] Dwarkesh Patel: matter if it's if it's a great great question location a b or c that's exactly so in fact that's
[00:54:11] Satya Nadella: one of the other reasons why we want to think about like hey what is an Azure region look like
[00:54:15] Satya Nadella: and what is the in fact the networking between Azure region so this is where uh I think as the
[00:54:19] Satya Nadella: model capabilities evolve and I think the usage of these tokens whether it's synchronously or
[00:54:25] Satya Nadella: asynchronously evolves and in fact you don't want to be out of position right then on top of that
[00:54:30] Satya Nadella: by the way what are the data residency draws right where do I like I mean the entire EU thing
[00:54:37] Satya Nadella: for us where we literally had to create an EU data boundary uh basically meant that you can't just
[00:54:42] Satya Nadella: round trip a call to wherever even if it's asynchronous and so therefore you need to have maybe
[00:54:47] Satya Nadella: regional things that are high density and then the power costs and so on but you're 100% right
[00:54:53] Satya Nadella: in bringing up that the topology as we build out uh will have to evolve one for tokens per dollar
[00:55:02] Satya Nadella: what uh what are the economics overlay that with what is the usage pattern uh usage pattern in terms
[00:55:10] Satya Nadella: of synchronously synchronous but also what is the compute storage because the latencies may matter
[00:55:15] Satya Nadella: for certain things uh the storage better be there if I have a cosmos db close to this for session
[00:55:20] Satya Nadella: data or even for an autonomous thing then that also has to be somewhere close to it and so on so
[00:55:26] Satya Nadella: I think that all of those considerations is what would shape uh the hyperscale business
[00:55:32] Dwarkesh Patel: you know prior to the pause you were you were you know versus you know what we had forecasted
[00:55:36] Dwarkesh Patel: for you by 28 you're gonna be like 12 13 you get a lot to know right you know nine and a half or
[00:55:42] Dwarkesh Patel: so right but you know something that's even more relevant right and it's it's you know I just
[00:55:46] Dwarkesh Patel: want you to like more is crunkly state that this is the business you don't want to be in but like
[00:55:49] Dwarkesh Patel: Oracle is going from like one fifths your size to bigger than you by end of 2027 and while it's
[00:55:56] Dwarkesh Patel: not a Microsoft level quality of return on invested capital right they're still making 35%
[00:56:02] Dwarkesh Patel: gross margins right the sort of the question is like does it is it isn't is it is it is it is it
[00:56:06] Dwarkesh Patel: you know hey it's not Microsoft's business to maybe do this what but you've created a hyperscaler now
[00:56:12] Dwarkesh Patel: yeah refusing this business by giving away the right of uh first refusal what's i i'm not
[00:56:16] Dwarkesh Patel: first of all i don't i don't want to take away any uh uh thing from the success Oracle has had
[00:56:21] Satya Nadella: in building their business and i wish them well and so the thing that i think i've answered for you
[00:56:26] Satya Nadella: is it didn't make sense for us uh to go be a host uh for one model company uh with limited time horizon
[00:56:36] Satya Nadella: RPO let's yeah let's just put it that way right the thing that you have to think through is not what
[00:56:40] Satya Nadella: you do in the next five years but what do you do for the next 50 uh because that's kind of what i
[00:56:47] Satya Nadella: we made our set of decisions uh i feel very good about our open AI partnership and what we're doing
[00:56:53] Satya Nadella: we have a decent book a book of business we wish them a lot of success in fact we are buyers
[00:56:58] Satya Nadella: we want a more of a capacity we wish them success but you know at this point i think the industrial
[00:57:04] Satya Nadella: logic for what we are trying to do is pretty clear which is it's not about like chasing uh first
[00:57:09] Satya Nadella: well i track by the way your uh things whether it's the AWS or the google and ours which i think is
[00:57:14] Satya Nadella: super useful uh but doesn't mean i gotta chase those yeah i have to chase them for not just
[00:57:22] Satya Nadella: uh the gross margin that they may represent in a period of time you know does might what what is
[00:57:27] Satya Nadella: this book of business that Microsoft uniquely can go clear which makes sense for us to clear and
[00:57:33] Satya Nadella: that's what we'll do i guess i have a question even stepping back from this of okay i take your
[00:57:38] Dwarkesh Patel: point to that it's a better business to be an all else equal to have a long tale of customers
[00:57:43] Dwarkesh Patel: you can have higher margin from rather than serving bare metal to a few labs but then there's a
[00:57:49] Dwarkesh Patel: question of okay which way is the industry evolving and so if we believe we're on the path to
[00:57:53] Dwarkesh Patel: smarter and smarter a i's then why isn't the shape of the industry that the opening eyes and
[00:57:59] Dwarkesh Patel: then throttics and deep minds are the platform which the long tail of enterprises are actually
[00:58:06] Dwarkesh Patel: doing business with where they need bare metal but like they are the platform what is the long
[00:58:10] Dwarkesh Patel: tail that is directly using azure um because you know you we want to use the general point of
[00:58:16] Dwarkesh Patel: work going to be available on azure right so any workload that says hey i want to use um
[00:58:22] Satya Nadella: you know some open source model and an open AI model like i mean if you go to azure foundry today
[00:58:27] Satya Nadella: you have all these models that you can provision by pt use get a cosmos db get a sequel db get some
[00:58:33] Satya Nadella: storage get some compute that's what a real workload looks like a real workload is not just a
[00:58:37] Satya Nadella: i called it an api call to a model a real workload needs all of these things to go build an app
[00:58:45] Satya Nadella: or instantiate an application in fact the model companies need that right to build anything is
[00:58:50] Satya Nadella: just not like i have a token factory i have to have all of these things that's the hyper scale
[00:58:55] Satya Nadella: business and it's not a we any one model but all these models and so if you want groc plus let's
[00:59:02] Satya Nadella: say open AI plus an open source model come to azure foundry provision them build your application
[00:59:08] Satya Nadella: here is a database that's kind of what the business is there is a separate business called just
[00:59:14] Satya Nadella: selling raw bare metal services to model companies and that's the argument about how much of that
[00:59:19] Satya Nadella: business you want to be in and not be in and what is that it's a very different segment of the
[00:59:24] Satya Nadella: business which we are in and we also have limits to how much of it is going to crowd out the
[00:59:29] Satya Nadella: rest of it but that's kind of at least the way i look at it so there's sort of two questions
[00:59:35] Dwarkesh Patel: here like why couldn't you just do both is one and then the other one is given you know our
[00:59:41] Dwarkesh Patel: our estimates on what your capacity is in 2028 is three and a half gigawatts lower sure you could
[00:59:46] Dwarkesh Patel: have dedicated that to open AI training and inference capacity but you could have also dedicated that
[00:59:52] Dwarkesh Patel: to hey this three and a half gigawatts is actually just running azure is running microsoft 365 that's
[00:59:58] Dwarkesh Patel: running get hub co-pilot it doesn't actually i could have built it and not given it to open AI or
[01:00:02] Dwarkesh Patel: i mean i want to build it in a different location i mean i want to build it in ua i mean i want to build
[01:00:07] Satya Nadella: it in india i mean i want to build it in europe right so one of the other things is as i said like
[01:00:11] Satya Nadella: where we have real capacity constraints right now are given the regulatory needs and the data
[01:00:15] Satya Nadella: sovereignty needs we got to build all over the world it's first of all state side capacity is super
[01:00:20] Satya Nadella: important and we're going to build everything but one of the things is when i look out to 2030
[01:00:25] Satya Nadella: i haven't sort of a global view of what is microsoft shape of business by first party and third
[01:00:30] Satya Nadella: party third party segmented by the frontiac labs and how much they want versus the inference
[01:00:37] Satya Nadella: capacity we want to build for multiple models and our own research compute needs right so that's
[01:00:43] Satya Nadella: all what's going into my calculus versus saying hey i think you're rightfully pointing out the pause
[01:00:50] Satya Nadella: but the pause was not done because we said oh my god we don't want to build that we realize that
[01:00:57] Satya Nadella: oh we want to build what we want to build slightly differently by both workload type as well as
[01:01:04] Satya Nadella: geotype and timing as well like we'll keep ramping up our gigawatts and the question is
[01:01:10] Satya Nadella: at what pace and in what location and in what sort of how do i write even the Moore's law on it
[01:01:16] Satya Nadella: right which is do i really want to over build three and a half in twenty seven or do i want to
[01:01:21] Satya Nadella: spread that in twenty seven twenty eight knowing even one of the biggest learnings we had even
[01:01:26] Satya Nadella: within videos their pace increased in terms of their model my i mean their migrations so that was a
[01:01:32] Satya Nadella: big factor i didn't want to go get stock for four years five years of depreciation on one
[01:01:37] Satya Nadella: generation and i wanted to just basically buy like in fact jensen's advice to me was two things one
[01:01:43] Satya Nadella: is hey get on the speed of light execution that's why i think even the execution in the
[01:01:47] Satya Nadella: zeat lanter data center i mean like it 90 days right well between when we get it and to hand
[01:01:51] Satya Nadella: off to a real workload that's sort of real speed of light execution on their front and so i want
[01:01:57] Satya Nadella: to get good at that and then that way then i'm building this each generation scaling
[01:02:03] Satya Nadella: and then every five years then you have a much more balanced so it becomes really literally like a flow
[01:02:11] Satya Nadella: for a large scale industrial operation like this where you suddenly are not a lot
[01:02:14] Satya Nadella: sided where you built up a lot in one time and then you take a massive hiatus because you're stuck
[01:02:19] Satya Nadella: with all this to your point in one location which may be great for training may not be great for
[01:02:24] Satya Nadella: infants because i can't serve even if it's like it's all asynchronous but european won't let me
[01:02:29] Satya Nadella: run trip to you texas so that's all of the things how do i rationalize this statement with what you've
[01:02:34] Dwarkesh Patel: done over the last few weeks you've announced deals with iris energy with nebius and lamda labs
[01:02:41] Dwarkesh Patel: and there's a few more coming as well you're you're going out there and securing capacity that you're
[01:02:46] Dwarkesh Patel: renting from the neoclouds rather than having built it yourself what was the what was it's fine
[01:02:52] Dwarkesh Patel: for us because we now have you know when you have line a site to demand which can be served
[01:02:57] Satya Nadella: where people are building it it's great in fact we'll even have i would say you know we will
[01:03:02] Satya Nadella: take leases we will take built a suite we'll take even GPUs of service where we don't have capacity
[01:03:09] Satya Nadella: but we need capacity and someone else has that and by the way i would even sort of welcome every
[01:03:14] Satya Nadella: neocloud to just be part of our marketplace because again guess what if they go bring their capacity
[01:03:21] Satya Nadella: into our marketplace that customer who comes through azure will use the neocloud which is a great
[01:03:25] Satya Nadella: win for them and will use compute storage databases all the rest from azure so i'm not at all
[01:03:32] Satya Nadella: thinking of this as just you know hey i should just go gobble up all of that myself
[01:03:38] Dwarkesh Patel: so you mentioned the how the you know you're depreciating this asset that's five six years and
[01:03:44] Dwarkesh Patel: this is the majority of the you know 75% of the tco data center and jensen is taking a 75% margin on
[01:03:52] Dwarkesh Patel: that so what all the hyper scalers are trying to do is develop their own accelerator so that they can
[01:03:57] Dwarkesh Patel: reduce this overwhelming cost for equipment to increase the margins yeah and then like you know
[01:04:05] Dwarkesh Patel: when you look at where they are right google's way ahead of everyone else right they've been doing
[01:04:08] Dwarkesh Patel: it for the longest they're going to make something like five to seven million chips right of their
[01:04:12] Dwarkesh Patel: own tp is you look at amazon they're trying to make three to five million but when we look at what
[01:04:17] Dwarkesh Patel: you know Microsoft is is ordering of their own chips it's it's it's way below that number
[01:04:22] Dwarkesh Patel: you've had a program for just as long what's going on with your
[01:04:25] Dwarkesh Patel: in some of the questions so so the couple of things one is the thing that is the biggest
[01:04:31] Satya Nadella: competitor for any new accelerator is kind of even the previous generation of Nvidia right i mean
[01:04:36] Satya Nadella: in a fleet what i'm going to look at is the overall t-seer so the bar i have even for our own and
[01:04:41] Satya Nadella: which by the way you know i was just looking at the data for my 200 which looks great
[01:04:47] Satya Nadella: except that one of the things that we learned even on the compute side right which is we add a
[01:04:52] Satya Nadella: lot of intel then we introduce AMD and then we introduce cobalt and so that's kind of how we
[01:04:57] Satya Nadella: scale that and so we have good sort of existence proof of at least in core compute on how to build
[01:05:03] Satya Nadella: your own silicon and then manage a fleet where all three are at play in some balance
[01:05:08] Satya Nadella: because by the way even google's buying Nvidia and so is amazon and it makes sense because
[01:05:12] Satya Nadella: Nvidia is innovating and it's the general purpose thing all models run on it
[01:05:18] Satya Nadella: and customer demand is there because if you build your own vertical thing you better have your own
[01:05:23] Satya Nadella: model which is you know either going to use it for training or inference and you have to generate
[01:05:28] Satya Nadella: your own demand for it or subsidize the demand for it so therefore you want to make sure
[01:05:33] Satya Nadella: you scale it appropriately so the way we are going to go do it is have a closed loop between our
[01:05:40] Satya Nadella: own ma i models and our silicon because i feel like that's the that's what gives you the birth
[01:05:46] Satya Nadella: right to really do your own silicon right where you literally have designed the micro architecture
[01:05:54] Satya Nadella: with what you're doing and then you keep pace with your own models and in our case the good news
[01:06:00] Satya Nadella: here is open AI has a program which we have access to and so therefore to think that Microsoft
[01:06:06] Satya Nadella: is not going to have something that's still level of access to you have to that all of it you just
[01:06:10] Satya Nadella: get the if you follow that so the only it you don't have as a consumer hardware that's it oh
[01:06:15] Dwarkesh Patel: okay yeah interesting yeah and by the way we gave them a bunch of ip as well to bootstrap them right so
[01:06:25] Satya Nadella: this is one of the reasons why they had a mass because we built all these super computers together
[01:06:30] Satya Nadella: we built it for them and they benefited from it rightfully so and and now as they innovate even
[01:06:37] Satya Nadella: at the system level we get access to all of it and we first want to instantiate what they build
[01:06:45] Satya Nadella: for them but then we'll extend it and so to think that we don't have and sorry if anything the way
[01:06:50] Satya Nadella: I think about to your question is Microsoft wants to be a fantastic alcoholic speeder light
[01:06:58] Satya Nadella: execution partner for Nvidia because quite frankly that fleet is life itself i'm not worried about
[01:07:05] Satya Nadella: I mean obviously Jensen is doing super well with his margins but the tco has many dimensions to it
[01:07:10] Satya Nadella: and I want to be greater that tco on top of that I want to be able to sort of really work with the
[01:07:17] Satya Nadella: open AI lineage and the mai lineage and the system design knowing that we have the ip writes on both
[01:07:25] Satya Nadella: ends speaking of rights one thing you know you you had to interview a couple days ago
[01:07:30] Dwarkesh Patel: where you said that we have rights to the the new agreement you made with open AI you have
[01:07:36] Dwarkesh Patel: right it's the exclusivity to the stateless API calls that open AI makes and we were sort of confused
[01:07:44] Dwarkesh Patel: about if there's any state whatsoever I mean you were just mentioning a second ago that all these
[01:07:48] Dwarkesh Patel: complicated workloads that are coming up are going to require memory and databases and storage and
[01:07:52] Dwarkesh Patel: so forth and is that now not stateless of chat GPT storing stuff on such a reason by so the the
[01:07:59] Satya Nadella: thing the business the strategic decision we made and also accommodating for the flexibility open AI
[01:08:05] Satya Nadella: needed you know to be able to procure compute for essentially think of open AI having a
[01:08:11] Satya Nadella: past business and a SaaS business SaaS business is chat GPT that past business is their API yeah
[01:08:18] Satya Nadella: that API is Azure exclusive the SaaS business they can run it anywhere and they can
[01:08:25] Satya Nadella: partner with anyone they want to to build SaaS products that so if they want a partner and
[01:08:30] Satya Nadella: thus partner wants to use a stateless API then Azure is the place where they can get the stateless
[01:08:36] Satya Nadella: API it seems like there's a way for them to make you you know build the product together and
[01:08:41] Dwarkesh Patel: and it's a state no real that they'll have to come to Azure okay so if it is any partner and so
[01:08:46] Satya Nadella: so fundamentally you know so again this is done in the spirit of what is it that we valued as part
[01:08:52] Satya Nadella: of our partnership and we made sure while at the same time we have a good partner to open AI given
[01:08:58] Satya Nadella: all the flexibility they need so for example Salesforce wants to integrate open AI it's not
[01:09:01] Dwarkesh Patel: through an API they actually work together train a model together deploy it on let's say
[01:09:06] Dwarkesh Patel: Amazon now is that is that allowed or or do they have to for any custom agreement like that they
[01:09:12] Satya Nadella: will have to come run it they've there are some few exceptions to us government and so on that we
[01:09:17] Satya Nadella: made but other than that they'll have to come to Azure so as I'd explain as agents get more
[01:09:22] Dwarkesh Patel: capable you're going to need more more observability into what they're doing you're going to need to
[01:09:26] Dwarkesh Patel: catch them when they're making mistakes you're going to need high level summaries of what they're
[01:09:30] Dwarkesh Patel: doing and you're going to need a picture of how everything that they're doing fits together this is
[01:09:34] Dwarkesh Patel: exactly what code rabbit provides you just make a normal pull request and code rabbit automatically
[01:09:40] Dwarkesh Patel: reviews the PR it generates a summary of changes you can understand exactly what the PR's author
[01:09:44] Dwarkesh Patel: was intending and it uses the context from a full code base to provide line by line feedback on how
[01:09:50] Dwarkesh Patel: things could be improved this is helpful whether you're reviewing a PR from a coworker or an agent
[01:09:56] Dwarkesh Patel: in either case code rabbit will write up its thoughts and flag any issues so that your teammate
[01:10:01] Dwarkesh Patel: or your agent can go fix them I've noticed that when I'm coding with the agents code rabbit catches
[01:10:07] Dwarkesh Patel: a lot of mistakes that the models make by default for example the models have a bad habit of
[01:10:13] Dwarkesh Patel: using old versions of libraries so in one session I wash code rabbit cash a call to an old model
[01:10:20] Dwarkesh Patel: figure out what the new version was and then suggest that improvement go to code rabbit dot AI
[01:10:27] Dwarkesh Patel: slash the work cash to learn more stepping back a question I have is you know when we're walking
[01:10:32] Dwarkesh Patel: back and forth the the factory one of the things you're talking about is you know Microsoft you can
[01:10:38] Dwarkesh Patel: think of it as a software business but now it's really becoming an industrial business there's all
[01:10:42] Dwarkesh Patel: this catbacks there's all this construction and if you just look over the last two two years you're
[01:10:48] Dwarkesh Patel: sort of catbacks is like tripled and maybe you extrapolate that forward it just actually just
[01:10:53] Dwarkesh Patel: becomes a huge industrial explosion other hyper scalars are taking loans right meta is meta is done
[01:10:59] Dwarkesh Patel: a 20 billion dollar loan at Louisiana they've taken they've done a corporate loan it seems clear
[01:11:03] Dwarkesh Patel: everyone's free cash flow is going to zero which is which is I'm sure Amy is like going to beat you
[01:11:08] Dwarkesh Patel: up for even if you've even tried to do that but like a what what's happening I mean I think I think
[01:11:14] Satya Nadella: the structural change is what you're referencing which I think is massive right which is I
[01:11:21] Satya Nadella: describe it as we are now a capital intensive business and a knowledge intensive business and in
[01:11:27] Satya Nadella: fact we have to use our knowledge to increase the ROIC on the capital spend right because that's kind
[01:11:32] Satya Nadella: you know look at the hardware guys have done a great job of marketing the Moore's law which I think
[01:11:37] Satya Nadella: is unbelievable and it's great but if you even look I think some of the stats are even did in my
[01:11:42] Satya Nadella: earnings call which is for a given GPT family right the improvement software improvements of
[01:11:49] Satya Nadella: really throughput in terms of tokens for dollar per watt that we're able to get you know quarter
[01:11:55] Satya Nadella: over quarter year over year is massive right so it's 5 x 10 x maybe 40 x in some of these cases
[01:12:01] Satya Nadella: right just because how you can optimize that's sort of knowledge intense intensity coming to
[01:12:08] Satya Nadella: bring out capital efficiency so that at some level the that's what we have to master what does
[01:12:15] Satya Nadella: it mean like somebody people ask me what was the difference between you know a classic old time
[01:12:20] Satya Nadella: holster and a hyperscaler it will suffer so yes it is capital intensive but as long as you have
[01:12:28] Satya Nadella: systems know how software capability to optimize by workload by fleet that's why I think when
[01:12:34] Satya Nadella: we say fungibility there's so much software and it's just not about the fleet right it's kind
[01:12:40] Satya Nadella: of the ability to evict a workload you know and then schedule another workload can I like manage
[01:12:46] Satya Nadella: the that algorithm of scheduling around that is the type of stuff that we have to be world class at
[01:12:53] Satya Nadella: and so yes so I think we'll still remain a software company but yes this is a different business
[01:12:59] Satya Nadella: and we're going to manage look at the end of the day the cash flow that Microsoft has
[01:13:04] Satya Nadella: allows us to have both these arms firing and you know wealth it seems like in the short term you
[01:13:13] Dwarkesh Patel: have more sort of credence on things taking a while being more jagged but in the maybe in the long
[01:13:19] Dwarkesh Patel: term you think like the people who say talk about agi and as I are correct like Sam Sam will be
[01:13:23] Dwarkesh Patel: right but eventually and I have a broader question about what makes sense for a hyperscaler to do
[01:13:30] Dwarkesh Patel: given that you have to invest massively in this thing which depreciates over five years
[01:13:35] Dwarkesh Patel: so if you have 2040 timelines for the kind of thing that somebody like Sam
[01:13:40] Dwarkesh Patel: anticipates in three years you know what is a reasonable thing for you to do in that world
[01:13:46] Dwarkesh Patel: there needs to be an allocation to while call it research compute that needs to be done
[01:13:54] Satya Nadella: like you did R&D right so that's the best way to even account for it quite frankly
[01:13:59] Satya Nadella: we should think of it as just R&D expense and you should say hey what's the research compute
[01:14:03] Satya Nadella: and how do you want to scale it yeah and let's even say it's an order of magnitude scale
[01:14:11] Satya Nadella: in some period pick your thing is it two years is it 16 months what have you right so that's sort
[01:14:17] Satya Nadella: of one piece which is kind of that's kind of table stakes that's R&D expenses and the rest
[01:14:23] Satya Nadella: is all demand driven right I mean ultimately you can you love to build ahead of demand but you better
[01:14:27] Satya Nadella: have a demand plan that doesn't go completely off kilter do you buy so these alabs are not
[01:14:34] Dwarkesh Patel: projecting revenues of a hundred billion and twenty seven twenty eight and the projecting you
[01:14:40] Dwarkesh Patel: know revenue keeps growing at this rate of like three acts two as a year in the marketplace right
[01:14:45] Satya Nadella: there's all kinds of incentives right now and and rightfully so right I mean what do you expect
[01:14:51] Satya Nadella: an independent lab that is sort of trying to raise money to do right they have to put some numbers
[01:14:56] Satya Nadella: out there such that they can actually go raise money so that they can pay their bills for compute
[01:15:01] Satya Nadella: and what have you and it's and it's good thing I mean someone's going to take some risk and put it
[01:15:06] Satya Nadella: in there and they've shown traction it's not like it's all risk without seeing the fact that they've
[01:15:12] Satya Nadella: been performing whether it's opening eye whether it's anthropic so I feel great about what they've
[01:15:16] Satya Nadella: done and we have massive book of business with these traps so therefore that's all good but overall
[01:15:23] Satya Nadella: ultimately there's two simple things one is you got to allocate for R&D you brought up even talent
[01:15:29] Satya Nadella: you got a like the talent for AI is at a premium you got to spend there you got to spend on compute
[01:15:35] Satya Nadella: so in some sense researcher to GPU ratios have to be high that is sort of what it takes to be a leading
[01:15:43] Satya Nadella: R&D company in this world and that's something that needs to scale and you have to have a balance
[01:15:50] Satya Nadella: sheet that allows you to scale that long before it's conventional wisdom and so on so that's
[01:15:54] Satya Nadella: kind of one thing but the other is all about sort of knowing how to forecast as we look across the
[01:16:02] Dwarkesh Patel: world right America has dominated many tech stacks right the US owns Windows right through Microsoft
[01:16:09] Dwarkesh Patel: which is to deploy even in China right that's the main operating system of course there's the Linux
[01:16:13] Dwarkesh Patel: which is open source but you know Windows is deployed everywhere in China on personal computers
[01:16:18] Dwarkesh Patel: you look at you look at word it's deployed everywhere you look at all these various technologies
[01:16:22] Dwarkesh Patel: it's deployed everywhere the thing that is quite unique and Microsoft and other companies have grown
[01:16:27] Dwarkesh Patel: elsewhere right they've built they're building data centers in Europe and in India and and
[01:16:31] Dwarkesh Patel: and all these other you know in Southeast Asia and in Latin America right all of these different
[01:16:36] Dwarkesh Patel: places you're building capacity but this seems quite different right you know today the political
[01:16:43] Dwarkesh Patel: aspect of technology of compute you know you know the the US administration didn't care about the
[01:16:49] Dwarkesh Patel: dot com bubble right it seems like the US administration as well as every other administration around
[01:16:54] Dwarkesh Patel: the world cares a lot about AI and the question is you know we're in a sort of a bipolar world at
[01:16:59] Dwarkesh Patel: least with US and China but Europe and India and all these other countries are are saying no
[01:17:05] Dwarkesh Patel: actually we're going to have sovereign AI as well how does Microsoft navigate you know the difference
[01:17:10] Dwarkesh Patel: of the 90s where it's like there's one country in the world that matters right it's American we do
[01:17:14] Dwarkesh Patel: we are companies sell everywhere and therefore Microsoft benefits massively to a world where it is
[01:17:18] Dwarkesh Patel: bipolar where hey Microsoft can't just necessarily have the right to win all of Europe or India or
[01:17:24] Dwarkesh Patel: you know Singapore there's actually sovereign AI efforts what what is your thought process here and
[01:17:29] Dwarkesh Patel: how do you think about this it's I think a super you know critical piece which is I think that the
[01:17:37] Satya Nadella: key key priority for the US tech sector and the US government is to ensure that we not only
[01:17:45] Satya Nadella: do leading innovative work but we also collectively build trust around the world on our tech stack
[01:17:55] right because I always say the United States is just an unbelievable place it's just unique in
[01:18:00] Satya Nadella: history right it's 4% of the world's population 25% of the GDP and 50% of the market cap and I
[01:18:07] Satya Nadella: think you should think about those ratios and really and reflect on it that 50% happens because
[01:18:13] Satya Nadella: quite frankly though trust the world has in the United States whether it's its capital markets or
[01:18:19] Satya Nadella: whether it's its technology and its stewardship of what matters at any given time in terms of leading
[01:18:27] Satya Nadella: sector so if that is broken then that's not a good day for the United States and so if we start
[01:18:35] Satya Nadella: with that which I think the you know President Trump gets the White House David Sacks everyone
[01:18:41] Satya Nadella: really I think gets it and so therefore I applaud anything that the United States government
[01:18:49] Satya Nadella: and the tech sector jointly does to quite frankly for example put our own capital at risk collectively
[01:18:57] Satya Nadella: as an industry in every part of the world right so I would like in fact the USG to take credit
[01:19:02] Satya Nadella: for foreign direct investment by American companies all over the world right it's kind of like
[01:19:08] Satya Nadella: least talked about but the best marketing that the United States should be doing is it's not just
[01:19:14] Satya Nadella: about all the foreign direct investment coming into the United States but the most leading sector
[01:19:19] Satya Nadella: which is these AI factories are all being created all over the world by whom by America
[01:19:25] Satya Nadella: and American companies and so you start there and then you even build other agreements around it
[01:19:31] Satya Nadella: which are around their continuity their legitimate sovereignty concerns around whether it's data
[01:19:37] Satya Nadella: residency whether it's even what happens for them to have real agency and guarantees on privacy
[01:19:48] Satya Nadella: and so on and so that in fact our European commitments I think are worth reading right so we made a
[01:19:53] Satya Nadella: series of commitments to Europe on how we will really govern our hyper scale investment there
[01:20:01] Satya Nadella: such that really European Union and the European countries have sovereignty they're also
[01:20:06] Satya Nadella: building sovereign clouds in in France and in Germany we have something called sovereign
[01:20:11] Satya Nadella: services on Azure which literally give people key management services along with confidential
[01:20:18] Satya Nadella: computing including confidential computing in GPUs which we've done great innovative work with
[01:20:24] Satya Nadella: Nvidia and so I think I feel very way good about being able to build both technically and through
[01:20:32] Satya Nadella: policy this trust in the American tech stack and how do you see this shaking out as you know you do
[01:20:39] Dwarkesh Patel: have this network effect with conventional learning and things on the model level maybe you have
[01:20:43] Dwarkesh Patel: equivalent things at the hyper scale level as well and do you expect that the country will say
[01:20:49] Dwarkesh Patel: look it's clearly one model or a couple models are the best and so we're going to use them but we're
[01:20:53] Dwarkesh Patel: going to have some laws around while the weights have to be hosted in our country or do you expect
[01:20:57] Dwarkesh Patel: that there will be this push to have it has to be a model trained in our country maybe an analogy
[01:21:03] Dwarkesh Patel: here is like people would you know the semiconductors are very important to the economy and people would
[01:21:07] Dwarkesh Patel: like to have their sort of sovereign semiconductors but like TSMC is just better and so semiconductors
[01:21:12] Dwarkesh Patel: are so important to the economy that you will just go to Taiwan and buy the semiconductors you have to
[01:21:17] Dwarkesh Patel: will it be like that with AI or is there ultimately I think what matters is the use of AI
[01:21:24] Satya Nadella: in their economy to create economic value right I mean that's the the diffusion theory which is
[01:21:30] Satya Nadella: ultimately it's not the leading sector but it's the ability to use the leading technology to
[01:21:36] Satya Nadella: create your own comparative advantage right so that I think will fundamentally be the core driver
[01:21:42] Satya Nadella: but that said they will want continuity of that right so in some sense that's one of the reasons
[01:21:46] Satya Nadella: why I believe there's always going to be a check a little bit to sort of some of your points
[01:21:52] Satya Nadella: hey can thus one model have all the runaway deployment that's why open source is always going to be
[01:21:58] Satya Nadella: there they will be by definition multiple models that will be one way like it's kind of you know
[01:22:05] Satya Nadella: that's one way for people to sort of demand continuity and not have concentration risk is
[01:22:09] Satya Nadella: another way to say it is right and so you say hey I'll want multiple models and then I want
[01:22:14] Satya Nadella: an open source so I feel as long as that's there every country will feel like okay I don't have
[01:22:21] Satya Nadella: to worry about deploying the best model and broadly diffusing because I can always take what is
[01:22:27] Satya Nadella: my data and my liquidity and move it to another model whether it's open source or from another
[01:22:34] Satya Nadella: country or what have you concentration risk and sovereignty right which is really agency those
[01:22:41] Satya Nadella: are the two things I think that'll drive the market structure the thing about this is that this
[01:22:45] Dwarkesh Patel: doesn't exist for semiconductors right you know all refrigerators cars have chips made in time
[01:22:50] Dwarkesh Patel: it don't exist until now until now everybody's not like even then right America you know if Taiwan
[01:22:56] Dwarkesh Patel: has cut off there isn't there are no more cars or no more refrigerators TSMC Arizona is not
[01:23:00] Dwarkesh Patel: replacing any real fraction of the production like there it is there the sovereignty is a bit of like
[01:23:06] Dwarkesh Patel: a scam if you all right I mean it's it's worthwhile having it it's important to have it but it's not a
[01:23:11] Dwarkesh Patel: real it's not real sovereignty right and we're a global economy we don't we I think it's kind of
[01:23:16] Satya Nadella: like Dylan saying hey at this point we've not learned anything about sort of uh what resilience
[01:23:22] Satya Nadella: means and what one needs to do right so it's kind of any nation state including the United States
[01:23:31] Satya Nadella: at this point will do what it takes to be more self-sufficient on some of these critical supply chains
[01:23:39] Satya Nadella: so I as a multinational company have to think about that as a first-class requirement right if I
[01:23:46] Satya Nadella: don't then I'm not respecting what is in the sort of policy interests of that country long term
[01:23:55] Satya Nadella: right and I'm not saying they won't make practical decisions in the short term right absolutely I
[01:24:00] Satya Nadella: mean the globalization can't just be rebound right I mean all these capital investments cannot be made
[01:24:05] Satya Nadella: in in a way at the pace at which but at the same time you have to kind of like if I just think
[01:24:10] Satya Nadella: about it right if somebody showed up in Washington and said hey you know what we're not going to
[01:24:14] Satya Nadella: build any semiconductor plans they're going to be kicked out of the United States and and the same
[01:24:20] Satya Nadella: thing is going to be the true in every other country too and so therefore I think we have to
[01:24:25] Satya Nadella: as companies respect what the lessons learned are you know whether it's you know you could say
[01:24:32] Satya Nadella: the pandemic woke us up or whatever but and nevertheless people are saying look globalization
[01:24:36] Satya Nadella: was fantastic uh it helped the supply chains be globalized and be super efficient but there's such
[01:24:42] Satya Nadella: a thing called resilience and we are happy you know we want resilience and so therefore that
[01:24:47] Satya Nadella: feature will get built at what pace I think is the point you're making it can't be like you can't
[01:24:53] Satya Nadella: snap your fingers and say all the TSMC plans now are all in Arizona and with all of the capability
[01:24:59] Satya Nadella: they're not going to be but is there a plan there will be a plan and should we respect that absolutely
[01:25:04] Satya Nadella: and so I I feel that's the world I want to meet the world where it is and what it wants to do
[01:25:12] Satya Nadella: going forward as opposed to say hey we have a point of view that doesn't respect you. So just to
[01:25:18] Dwarkesh Patel: make sure I understand the idea here is each country will want some kind of data residency,
[01:25:25] Dwarkesh Patel: privacy, et cetera and Microsoft is especially privileged here because you have relationships with
[01:25:29] Dwarkesh Patel: these countries you have expertise in setting up these kinds of sovereign data centers and
[01:25:35] Dwarkesh Patel: therefore Microsoft is uniquely fit for world with more sovereignty requirements.
[01:25:41] Dwarkesh Patel: Yeah I mean I don't want to sort of describe it as somehow we're uniquely privileged. I would just
[01:25:47] Satya Nadella: say I think of that as a business required that we have been doing all the hard work all these
[01:25:52] Satya Nadella: decades and we plan to and so my answer to Dylan's previous question was I take these you know
[01:25:59] Satya Nadella: whether it's in the United States quite frankly when you know when the White House and the USG
[01:26:05] Satya Nadella: says hey we want you to allocate more of your I don't know way for starts to
[01:26:13] Satya Nadella: fabs in the US we take that seriously or whether it is data center and the EU boundary we take that
[01:26:19] Satya Nadella: seriously. So to me respecting what I think our legitimate reasons why countries care about sovereignty
[01:26:27] Satya Nadella: and building for it as a software and a physical plant is what I would say we are going to do.
[01:26:34] And as we go to like the bipolar world right US China there is there is a lot around
[01:26:41] Dwarkesh Patel: you know American tech does not you know it's not just you versus Amazon or you versus you know
[01:26:46] Dwarkesh Patel: Anthropic or you versus Google. Yeah there is a whole host of competitive competition. How does
[01:26:52] Dwarkesh Patel: how does America rebuild the trust? What do you do to rebuild the trust to say actually no American
[01:26:57] Dwarkesh Patel: companies will be the main provider for you and how do you think about competition with up and
[01:27:02] Dwarkesh Patel: coming Chinese companies whether it be you know by dance and alibaba or deep seek in moonshot.
[01:27:07] Dwarkesh Patel: And so just to add to the question one concern is look we're talking about how we
[01:27:10] Dwarkesh Patel: are is becoming this sort of industrial cat-backed race where you're just rapidly having to build
[01:27:15] Dwarkesh Patel: quickly across all those supply chain. When you hear that at least I've built till now you just
[01:27:20] Dwarkesh Patel: think about China right this is like their competitive advantage and especially if we're not
[01:27:24] Dwarkesh Patel: going to moonshot to ASI next year but we it's going to be this decades of buildouts and
[01:27:31] Dwarkesh Patel: infrastructure and so forth. How do you deal with Chinese competition are they privileged in
[01:27:36] Dwarkesh Patel: that world? Yeah so it's a great question. I mean in fact you just made the point of why I think
[01:27:41] Satya Nadella: trust in American tech is probably the most important feature. It's not even the model capability
[01:27:50] maybe it is like can I trust you the company can I trust you your country and its institutions
[01:27:59] Satya Nadella: to be a long-term supplier may be the thing that wins the world. It's a good note to end on.
[01:28:06] Dwarkesh Patel: So I think thank you for doing this. Thank you so much. Thank you. It's such a pleasure.
[01:28:10] Dwarkesh Patel: Yeah it's awesome. It's like man you two guys are like quite the team.
[01:28:17] Hey everybody I hope you enjoyed that episode. If you did the most helpful thing you can do is
[01:28:21] Dwarkesh Patel: just share it with other people who you think might enjoy it. It's also helpful if you leave a
[01:28:26] Dwarkesh Patel: rating or a comment on whatever platform you're listening on. If you're interested in sponsoring
[01:28:31] Dwarkesh Patel: the podcast you can reach out at twerkesh.com slash advertise. Otherwise I'll see you on the next one.