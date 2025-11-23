# 6 Months Later, How Our AI SDRs Actually Work as AI Runs GTM with SaaStr's CEO and Chief AI Officer

**Podcast:** SaaStr
**Date:** 2025-11-23
**Video ID:** 6YrzIuvhi5k
**Video URL:** https://www.youtube.com/watch?v=6YrzIuvhi5k

---

[00:00:00] Welcome to the official Saster Podcast where you can hear some of the best Saster speakers.
[00:00:06] Jason Lemkin: This is one of the cloud meets.
[00:00:08] Up today on the Saster Podcast, don't fire anyone good to replace them with AI if you haven't learned anything.
[00:00:14] Jason Lemkin: If someone's failed, if they can't close anything or if your AI SGR is instead a single appointment,
[00:00:19] Jason Lemkin: I mean your human SGR maybe just replace that page with your SGR can't do anything, you know, you can't do worse than zero.
[00:00:27] But we'll track it.
[00:00:29] Jason Lemkin: Many of you, if you're early stage folks watching this, you'll think that's expensive and if you don't believe in the vendor, it will seem very expensive.
[00:00:37] Jason Lemkin: It will speak as if you'll get quoted by a sales rep a lot of money and it will feel risky to you if the deployment doesn't work.
[00:00:45] You know, that's why we're not trying to be walking billboards, but we do share the vendors that we use.
[00:00:51] Jason Lemkin: Others are good too, but if you get the right people, it's going to work, but it can't feel risky.
[00:00:56] Jason Lemkin: It's tough to start at $500 a month today, but you got to take a little risk of life.
[00:01:07] Hey everybody at Saster Connect Data, automate, busy work, and empower teams like nobody's business with the one platform that grows with you.
[00:01:14] Jason Lemkin: Every step of the way.
[00:01:15] Jason Lemkin: Learn how Salesforce works for startups at Salesforce.com slash SMB.
[00:01:20] Jason Lemkin: That's Salesforce.com slash SMB.
[00:01:26] Hey Saster, imagine having agents for every support task.
[00:01:30] Amelia Ibarra: One that triage is tickets, another that catches duplicates, one that spots churn risk.
[00:01:34] Amelia Ibarra: That'd be pretty amazing, right?
[00:01:36] Amelia Ibarra: Happy Fox just made it real with Autofilet.
[00:01:38] Amelia Ibarra: These pre-built AI agents deploying about 60 seconds and run for as low as two cents per successful action.
[00:01:45] Amelia Ibarra: All of it sits inside the Happy Fox Omnichannel AI First Support Stack.
[00:01:50] Amelia Ibarra: Chatbot, Co-Pilot, and Autofilet working as one.
[00:01:53] Amelia Ibarra: Check them out at HappyFox.com slash Saster.
[00:02:01] All right, hello everyone, welcome.
[00:02:05] Welcome to everyone in to chat and listening for your agents that are also listening and you'll be reading the recap later.
[00:02:14] Amelia Ibarra: We thought it would be fun to do a deep dive into where we're at today in our AI journey.
[00:02:22] It's kind of crazy to think before Saster and you all this last of May.
[00:02:28] Amelia Ibarra: We really only had one agent that we had sort of just deployed.
[00:02:34] Amelia Ibarra: And now we have about 20 or so core agents, which we've gone through, but I'll go through a little bit as well for context.
[00:02:41] Amelia Ibarra: So it's crazy to see, you know, just kind of from May till November, you know, post annual now that we're fully in all the platforms.
[00:02:49] Amelia Ibarra: We've added a lot more use cases across go to market, which you'll see just to give an update of where we're at.
[00:02:56] Amelia Ibarra: What's working?
[00:02:58] Amelia Ibarra: New on says on what has it worked?
[00:03:01] Amelia Ibarra: And there's some maybe unexpected learnings there that will also go through, but hopefully it's helpful for folks just to listen and hear and see where we're at share our learnings and our findings.
[00:03:13] Amelia Ibarra: Hopefully this helps you as well.
[00:03:16] Amelia Ibarra: But if you have any questions, as we go along, put them into the chat.
[00:03:20] Amelia Ibarra: We'll try and do a bunch of questions at the end.
[00:03:22] Amelia Ibarra: I'll answer your guys as any deep dive questions to.
[00:03:26] Amelia Ibarra: So with that.
[00:03:29] Amelia Ibarra: Let's try and keep it new.
[00:03:31] Amelia Ibarra: Let's go through it.
[00:03:34] So what do I mean by six months of AI running our GTM now it's not on full autopilot.
[00:03:41] Amelia Ibarra: So it is not just that the AI is running a month with our GTM on its own.
[00:03:46] Amelia Ibarra: It does require a lot of oversight and time and management, which you'll see here today.
[00:03:52] Amelia Ibarra: How we do that, how we think about it.
[00:03:55] And also how we are thinking about doing that going forward just because right now it does take literally the majority I would say of both mine and Jason's time to run all these agents and use them successfully right.
[00:04:08] Amelia Ibarra: We could run more agents and they would fail if we didn't put in as much time, but since we do devote a lot of time to them.
[00:04:14] They've become quite time consuming.
[00:04:17] Amelia Ibarra: I don't think 20 is the right amount for everybody.
[00:04:22] Amelia Ibarra: So if you haven't seen the disaster.ai slash agents, you can see all the agents we use.
[00:04:28] Amelia Ibarra: There's a mix of ones we've coded that Jason talked about previously and then there's ones that we are using third party tools for.
[00:04:37] Amelia Ibarra: So that's all listed there.
[00:04:39] Amelia Ibarra: You'll see most of those here today too will go through the metrics of them just like in full disclosure.
[00:04:45] Amelia Ibarra: That's great shots of all of our metric.
[00:04:48] Amelia Ibarra: And then also we're going to go through how we think about them in our day to day.
[00:04:52] Amelia Ibarra: So Jason, anything want to add there?
[00:04:55] No, I think that's great. I think I think I think we'll really go through all of it.
[00:04:58] Jason Lemkin: I think most importantly we'll give you an update on how all our a I s d r slash b d r is a work outbound inbound the actual data.
[00:05:06] Which I think will be super helpful and really put this together, which is great.
[00:05:11] And then so why 20 right so I'll kick this off to say 20 is not the right amount for most people.
[00:05:20] Amelia Ibarra: I think even like a few is maybe the right amount for most people or even right now feel like I have maybe let's say one agent kind of fully deployed.
[00:05:31] Amelia Ibarra: It's scary me to go from one to 20.
[00:05:34] Amelia Ibarra: I don't think you should take this as like the gold standard of everyone needs to be on 20 apps or you're behind now.
[00:05:40] Amelia Ibarra: I think you need to be we've talked about before I do think you need to be on some version of this stack in gtm to not fall behind.
[00:05:48] And I'll show you why.
[00:05:50] But I don't think 20 is the right number for everyone.
[00:05:52] I feel like between myself and Jason we're fairly technical right some of the stuff we've got it we've been thinking about for a long time.
[00:05:58] Amelia Ibarra: Some of the stuff you'll see that we've deployed across our go to market or is where we had gaps and we had a need to fill them right so.
[00:06:06] That's why we have 20.
[00:06:08] I just put a fun image of yes this is a real image of myself that then reared added a digital clone to.
[00:06:15] Amelia Ibarra: But I think there is a lot of talk and I want to get your thoughts quick Jason on us before we move on you know how much can AI.
[00:06:25] Amelia Ibarra: I want to get a lot of things to do.
[00:06:27] Amelia Ibarra: I want to get a lot of things to do.
[00:06:29] Amelia Ibarra: I want to get a lot of things to do.
[00:06:31] Amelia Ibarra: I want to get a lot of things to do.
[00:06:33] Amelia Ibarra: I want to get a lot of things to do.
[00:06:35] Amelia Ibarra: I want to get a lot of things to do.
[00:06:37] Amelia Ibarra: I want to get a lot of things to do.
[00:06:39] Amelia Ibarra: I want to get a lot of things to do.
[00:06:41] Amelia Ibarra: I want to get a lot of things to do.
[00:06:43] Amelia Ibarra: I want to get a lot of things to do.
[00:06:45] Amelia Ibarra: I want to get a lot of things to do.
[00:06:47] Amelia Ibarra: I want to get a lot of things to do.
[00:06:49] Amelia Ibarra: I want to get a lot of things to do.
[00:06:51] Amelia Ibarra: I want to get a lot of things to do.
[00:06:53] Amelia Ibarra: Customers Customers Customers Customers Customers Customers Customers Customers Customers Customers Customers Customers Customers Customers Customers Customers Customers Customers Customers Customers Customers Customers Customers Customers Customers Customers Customers Customers Customers Customers Customers Customers Customers Customers Customers Customers Customers Customers Customers Customers Customers Customers Customers Customers Customers Customers Customers Customers Customers Customers Customers Customers Customers Customers Customers Customers Customers Customers Customers Customers Customers Customers Customers Customers Customers Customers Customers Customers Customers Customers Customers Customers Customers Customers Customers Customers Customers Customers Customers Customers Customers Customers Customers Customers Customers Customers Customers Customers Customers Customers Customers Customers Customers Customers Customers Customers Customers Customers Customers Customers Customers Customers Customers Customers Customers Customers Customers Customers Customers Customers Custom
[00:07:23] Amelia Ibarra: we have all across the org.
[00:07:25] Amelia Ibarra: But I think this concept now,
[00:07:27] Amelia Ibarra: it's cloning the best parts of your best players, right?
[00:07:31] Amelia Ibarra: Maybe your org isn't as small internally as Saster is.
[00:07:35] And you've got more folks,
[00:07:36] Amelia Ibarra: but I think there is now, I think it's clear path
[00:07:38] Amelia Ibarra: to where I'm seeing in these platforms.
[00:07:40] Amelia Ibarra: You can clone all your best A players, right?
[00:07:42] Amelia Ibarra: Take all of the best A players on your team
[00:07:45] Amelia Ibarra: across marketing sales, CS sales, rev-offs,
[00:07:48] Amelia Ibarra: and make the best year with A.I.
[00:07:50] Amelia Ibarra: I truly believe that's possible,
[00:07:51] Amelia Ibarra: and you'll see it from our results.
[00:07:54] But yeah, what do you,
[00:07:55] Amelia Ibarra: and you've also there, Jason?
[00:07:57] Jason Lemkin: I think that's a really great insight.
[00:07:58] Jason Lemkin: Thinking about what we have learned
[00:07:59] Jason Lemkin: since we've had some success.
[00:08:02] Jason Lemkin: A lot of folks want agents,
[00:08:05] Jason Lemkin: specifically A.I.
[00:08:06] Jason Lemkin: I said SGRs, A.I. B.D.R.s,
[00:08:08] Jason Lemkin: A.I. marketing agents, others.
[00:08:10] Jason Lemkin: They want them to do magical work for them.
[00:08:12] Jason Lemkin: They want to spend 20 grand, 50 grand,
[00:08:14] Jason Lemkin: 100 grand, and all of a sudden get leads.
[00:08:16] Jason Lemkin: That is, I didn't fully realize that at children's now,
[00:08:19] Jason Lemkin: children said, that's the wrong way to think about it.
[00:08:21] Jason Lemkin: What your agents can do, and it is so powerful,
[00:08:24] Jason Lemkin: is they can take your best practices
[00:08:26] Jason Lemkin: and scale them out almost infinitely.
[00:08:28] Jason Lemkin: Figure out what works, figure out what campaigns work,
[00:08:30] Jason Lemkin: what messaging, whatever works is already working.
[00:08:33] Jason Lemkin: You have to have something that's working.
[00:08:35] Jason Lemkin: An agent can't today figure out,
[00:08:36] Jason Lemkin: make something that isn't working at work.
[00:08:38] Jason Lemkin: But if you know what's working,
[00:08:40] Jason Lemkin: and then this is important,
[00:08:41] Jason Lemkin: you train the agent with it,
[00:08:43] Jason Lemkin: then you get 24, seven infinite firepower
[00:08:46] Jason Lemkin: backing up your best practices,
[00:08:48] Jason Lemkin: and your best practices will change,
[00:08:49] Jason Lemkin: and you'll run A.B. tests, and A.B.C.D.E.F. tests,
[00:08:52] Jason Lemkin: and multivariant tests.
[00:08:53] Jason Lemkin: But you've got to understand what is working in GDM
[00:08:56] Jason Lemkin: before your agent can scale it up.
[00:08:58] Jason Lemkin: And I think that is a fundamental mistake
[00:09:01] Jason Lemkin: that confuses folks, it's not about buying a tool,
[00:09:03] Jason Lemkin: but once you have something that works,
[00:09:05] Jason Lemkin: which we have, and Amelia will show you the data,
[00:09:08] then you can scale in a way you can't with humans.
[00:09:11] Yeah, I would say that's my biggest learning six month
[00:09:14] Amelia Ibarra: and we took things that were already,
[00:09:17] Amelia Ibarra: or some processes were broken, right?
[00:09:18] Amelia Ibarra: Like our Roblox process was pretty broken before we did this.
[00:09:22] But we figured out how to fix it,
[00:09:24] Amelia Ibarra: and then we basically put that on acid
[00:09:26] Amelia Ibarra: with the AI in the agents.
[00:09:28] Amelia Ibarra: So I do think it's an interesting nuance
[00:09:31] Amelia Ibarra: of how to approach it as people are in different states.
[00:09:35] Amelia Ibarra: Okay, this is just a quick fun one
[00:09:36] Amelia Ibarra: before you go into our data.
[00:09:38] Amelia Ibarra: This is from Jason's co-host Rory Hitski.
[00:09:41] Amelia Ibarra: This is their state of GTMAI.
[00:09:46] It's actually fairly short but concise,
[00:09:48] Amelia Ibarra: so I like it, you can just go to those that you can download it.
[00:09:51] It's set a lot of interesting things
[00:09:52] Amelia Ibarra: that I used to kind of anchor how I wanted to present
[00:09:55] Amelia Ibarra: a lot of our data since we have a lot, right?
[00:09:57] Amelia Ibarra: So I think we're in this right now,
[00:10:00] Amelia Ibarra: sort of paradoxical world in November of 2025,
[00:10:05] Amelia Ibarra: where a lot of folks have adopted at least one sort of AI or agent,
[00:10:09] Amelia Ibarra: but maybe to Jason's point that he just made,
[00:10:11] Amelia Ibarra: a lot of them aren't seeing the impact
[00:10:12] Amelia Ibarra: because either they're expecting too much
[00:10:14] Amelia Ibarra: or they're not putting in the time.
[00:10:16] So I think that's kind of where I see the paradox line.
[00:10:20] Amelia Ibarra: In this report, you'll see,
[00:10:22] if you're at all right it up to,
[00:10:23] Amelia Ibarra: I'm just some of my learnings, but you'll see a cross go to market
[00:10:28] Amelia Ibarra: which chives into this most deeply the adoption has been in marketing.
[00:10:33] Amelia Ibarra: But if you read the whole report,
[00:10:35] Amelia Ibarra: it's on kind of what I consider base level adoption, right?
[00:10:39] Amelia Ibarra: Like they're using cloud to create content.
[00:10:41] Amelia Ibarra: Yes, so are we, but you'll see our more kind of like sophisticated 2.0 stack
[00:10:45] Amelia Ibarra: at the end of this sales dev same thing,
[00:10:47] Amelia Ibarra: they're using it for sales messaging.
[00:10:50] Like the kind of middle ground is using it for starting to do things like revops
[00:10:56] Amelia Ibarra: or more intelligent emails.
[00:10:58] Amelia Ibarra: Again, consider that kind of baseline.
[00:11:03] Amelia Ibarra: I feel like you can again,
[00:11:04] Amelia Ibarra: if you take the best people, give them an agent,
[00:11:07] Amelia Ibarra: they get used to and they know how to train it.
[00:11:08] Amelia Ibarra: I do think you can get them to blow by that fairly quickly.
[00:11:12] Amelia Ibarra: So I think across the board,
[00:11:13] Amelia Ibarra: even what they said in sales and CS is a lot of votes are still early, right?
[00:11:17] Amelia Ibarra: So a lot of still early adopters there across the board,
[00:11:22] Amelia Ibarra: but some bits of their I'll try and tie into what we're going to show.
[00:11:26] I think just a quick one to tie into that data,
[00:11:28] Amelia Ibarra: plus what Jason was saying as well.
[00:11:32] Here are my quick biggest learnings and then literally all the next lines
[00:11:35] Amelia Ibarra: or the data that will run through.
[00:11:38] Amelia Ibarra: I think again, in a lot of really days and as you add more platform,
[00:11:42] Amelia Ibarra: I think the expectation that it gets easier with each platform you add is false.
[00:11:47] Amelia Ibarra: So I wouldn't expect to have that expectation.
[00:11:50] Amelia Ibarra: I do think a lot of the platforms, whether you use what like one specialized one
[00:11:55] Amelia Ibarra: for each function the way we are,
[00:11:57] Amelia Ibarra: or you end up on one platform that does kind of like a little bit of everything pretty good.
[00:12:01] Amelia Ibarra: Maybe in that case,
[00:12:02] Amelia Ibarra: it gets a little bit easier as time goes on, but it's never set in for again.
[00:12:05] Amelia Ibarra: Like the biggest thing is that our agents will ebb and flow oddly,
[00:12:10] Amelia Ibarra: depending on how much time the humans put in.
[00:12:12] Amelia Ibarra: It's the war time I put in with our agent.
[00:12:15] Amelia Ibarra: Wow, shocker, the better the output is.
[00:12:17] Amelia Ibarra: And sometimes that ends in flows, right?
[00:12:19] Amelia Ibarra: Like we get busy, we have saster London coming up.
[00:12:22] Amelia Ibarra: So I can't always spend the amount of time I would like to with the agents.
[00:12:26] Amelia Ibarra: Right? And so that obviously does translate to the results.
[00:12:30] Amelia Ibarra: And so I think that's one of the biggest things.
[00:12:32] Amelia Ibarra: I think Jason was fine on like a media ROI and headcount is a hugely false expectation
[00:12:38] Amelia Ibarra: I hope nobody have on this call.
[00:12:40] Amelia Ibarra: But if you had it, maybe going into this can kind of course correct
[00:12:45] Amelia Ibarra: where you're going to see left.
[00:12:47] Amelia Ibarra: And there are happen cases in our data.
[00:12:49] Amelia Ibarra: You'll be where we did get immediate left.
[00:12:51] Amelia Ibarra: But again, it took our processes,
[00:12:54] Amelia Ibarra: like it took us recreating some of our best processes that we're already working to get an immediate
[00:12:58] Amelia Ibarra: lift in these six months.
[00:13:01] Amelia Ibarra: You know, and then I think in the expectation on needing to staff like an AI expert,
[00:13:05] Amelia Ibarra: I've talked to a bunch of CMOs and CROs now, as well as founders that are either at SAS or
[00:13:11] Amelia Ibarra: participating in SAS or where, you know, they say, hey, Amelia, what's your advice on my biggest
[00:13:15] Amelia Ibarra: problem right now is we're starting to on board all these tools, but I don't have anybody to run it.
[00:13:21] Amelia Ibarra: I don't have a chief AI officer like I am now to help us figure all this out.
[00:13:26] Amelia Ibarra: What do I do?
[00:13:27] Amelia Ibarra: And most folks, I will say that that have figured this out and started to deploy AI more across the
[00:13:34] Amelia Ibarra: DGM org.
[00:13:35] Amelia Ibarra: Have told me that their best success has been, again, taking your A player, take somebody that is
[00:13:42] Amelia Ibarra: the best person on your sales off steam, your rev off steam, your best marketer,
[00:13:47] Amelia Ibarra: your best SDR, your best AE.
[00:13:50] Sit down with that figure out what tools you want to use together.
[00:13:52] Amelia Ibarra: Don't just deploy it to them from, you know, the castle.
[00:13:56] Amelia Ibarra: And then go through that process with them together because it's very important to that you
[00:14:01] Amelia Ibarra: need to do the AI yourself with harder to figure out how it works.
[00:14:04] Amelia Ibarra: You know, you can't expect the even your best SDR to know how to instantly use this.
[00:14:09] Amelia Ibarra: You got to help the mountain help some figure it out a little bit.
[00:14:12] Amelia Ibarra: But everyone I talk to you that says they go this route of using the best A tier players
[00:14:17] Amelia Ibarra: and injecting AI and figuring it out with them have now they have now changed their job roles.
[00:14:22] Amelia Ibarra: Like in the way that my job role has changed into an out chief AI officer, they're saying the
[00:14:26] Amelia Ibarra: same thing. This is like the best path I've seen work for people across and these are you know,
[00:14:32] Amelia Ibarra: founders and CMOs at different stages, different off some of them are even AI native companies.
[00:14:37] Amelia Ibarra: And they need to figure out AI too. They're just taking all their best people,
[00:14:41] Amelia Ibarra: figuring out and these are the founders figuring out AI with them in the trenches.
[00:14:45] Amelia Ibarra: And then you become this S tier team together with AI that can do this again, great outputs that
[00:14:51] Amelia Ibarra: you'll see like ours with everything AI. I think this like somebody else asked me yesterday,
[00:14:58] Amelia Ibarra: hey, I, you know, I'm rolling out a few platforms. Some of the some of them are ones that's
[00:15:03] Amelia Ibarra: after you. So do you like recommend anybody to any other anybody or like an agency that cannot
[00:15:09] Amelia Ibarra: be deployed all this. I'm like, that's the wrong way to go about it. One, you've got to figure it
[00:15:13] Amelia Ibarra: out yourself to, you know, no, I don't care who where anybody went in life or school or whatever.
[00:15:20] Amelia Ibarra: No single person on planet Earth will know how to do this better. There's no agency that
[00:15:24] Amelia Ibarra: are you now set to do? There's no, maybe there's a few like asked your people at orgs that you can
[00:15:30] Amelia Ibarra: try and steal. But outside of that, I would it, you know, by this naked oil of, oh, we're at
[00:15:36] Amelia Ibarra: an AI native agency and we know how to do GGM across the entire org. I'm like, they probably
[00:15:41] Amelia Ibarra: haven't done it themselves. I know maybe that's the little disheartening that you have to figure
[00:15:46] Amelia Ibarra: out yourself, but that is the best path forward in the meantime until other sketch up.
[00:15:52] And then I would say to don't get to hung up on this data governance thing. A lot of folks,
[00:15:56] Amelia Ibarra: I talked to now, especially at bigger org.
[00:16:01] Give very concerned. Okay, if I add so many agents, I'm going to need governance as a layer.
[00:16:05] Amelia Ibarra: I'm going to need to clean up all my data and cleaning up all my data or getting all the process
[00:16:09] Amelia Ibarra: we've got to take two years before I can even think about implementing. I think too much data,
[00:16:14] Amelia Ibarra: too much data. And if you have things that are working, again, I would focus there first.
[00:16:19] Amelia Ibarra: So I wouldn't try and tackle, you know, fight off more than you can chew, which is it didn't work
[00:16:24] Amelia Ibarra: pre AI and it stuck work with AI. And then I think the last one because the other one we'll get into
[00:16:31] Amelia Ibarra: per department is I hear this panic a lot from folks now. I don't know if it's because of
[00:16:38] Amelia Ibarra: how much content we post about AI or because of all the tweets, all the LinkedIn messages,
[00:16:45] Amelia Ibarra: that they have to keep adding. Oh, I got to catch it. I got it. Saster has 20. I got it. It's a 20.
[00:16:51] You don't like actually we have 20. I'm only adding one more tool for the rest of the year.
[00:16:56] Amelia Ibarra: Absolutely. I'm adding more use cases to our current agent. I'm adding a 2.0 agent to agent for us.
[00:17:02] Amelia Ibarra: I'm adding a 2.0 thing to qualify. Like I'm going deeper on our current tools. I'm adding one more
[00:17:07] Amelia Ibarra: because I think it's cool. And that's probably it for the foresee it like Q1. I don't really know
[00:17:13] Amelia Ibarra: I'm going to add yet. Actually, that's like if our agents can just go a little deeper. I may not add
[00:17:18] Amelia Ibarra: anything. You know, I might add, you know, just deeper use cases are current.
[00:17:26] Okay, let's start with how bound. I'll try and have to spend all the time here.
[00:17:31] Amelia Ibarra: We I know Albound is near and dear to a lot of our hearts and we talk about it a lot.
[00:17:37] Amelia Ibarra: But I'll start here and she's not yet. You're in put too.
[00:17:41] So for Albound six months and now we have sent now almost 20,000 messages. Actually, it would be
[00:17:47] Amelia Ibarra: 20,000 again. If the human me had a little bit more time to spend with my agent, it'd be over 20,000.
[00:17:54] Amelia Ibarra: But still 20,000 is like a lot. Overall our Albound with the AI is almost a 7% overall response
[00:18:06] Amelia Ibarra: rate, which is kind of double just overall averages across anything you'll see from
[00:18:12] all any tool that does sequences and outreach of 4% positive response rate, which is higher than
[00:18:18] Amelia Ibarra: most. Now keep that in mind. This is like higher than most folks in the platform.
[00:18:24] But interestingly, two, now that it's been six months, 10% of ticket revenue for SASTRA AI in London,
[00:18:32] Amelia Ibarra: only on this agent. So this is an interesting thing where I have seen our Albound agent.
[00:18:40] Amelia Ibarra: It has different goals. We've explained this previously, but I'll just give you guys some
[00:18:43] Amelia Ibarra: context. It has different goals. And so it has like different agents in one platform. Because the
[00:18:49] Amelia Ibarra: training is different on all those agents. I have an agent basically for lab sponsors. I got what
[00:18:54] Amelia Ibarra: for current sponsors. I've got one for people who previously attended SASTRA. Now I now I have one
[00:18:59] Amelia Ibarra: for people who are opening our emails, but maybe not taking any actions with us. And then I have
[00:19:04] Amelia Ibarra: one purely for cold outbound. So all of those agents are trained into in a slightly different way.
[00:19:09] Amelia Ibarra: Because those audiences are different, right? The messaging is different. The collateral of
[00:19:14] Amelia Ibarra: what we want the agent to do. And also the goal for the what we want the agent to do is very different
[00:19:19] Amelia Ibarra: across those five. And so we've got about five core ones just within artists that are set up
[00:19:25] Amelia Ibarra: differently. And this is I think is surprisingly because at the start I was like, okay, you know,
[00:19:31] Amelia Ibarra: it's an Albound tool. They were a sponsor of SASTRA. This last May, I'm going to use it for sponsorships.
[00:19:37] But then I quickly saw, okay, like it's not bad at booking meetings. It's fine at booking meetings.
[00:19:42] Amelia Ibarra: And that's great. And then you know, you have to ensure that intent. And it's a great way to do
[00:19:49] Amelia Ibarra: follow ups again to like current or past or lab customers. It's a great way to do that.
[00:19:54] Amelia Ibarra: Using yeah, I again, at scale in a more consistent way that sometimes we can't physically do.
[00:20:00] But then you know, there was just this interesting learning of because tickets for London and
[00:20:06] Amelia Ibarra: then now for annual or you know, less than a thousand dollars depending on which event you go to.
[00:20:10] Amelia Ibarra: The AI got pretty good at selling the tickets itself. Like it got pretty good. Like at first I was
[00:20:18] Amelia Ibarra: nervous. Now six months in. I'm like, let it go. Let it run free. Like it's gotten pretty good
[00:20:26] Amelia Ibarra: now with all the time we put in that it is empowered to sell tickets to people. Again, it's a lower ASP.
[00:20:33] Amelia Ibarra: So maybe that's the most interesting learning. And it is still booking meetings for us on like the higher
[00:20:37] Amelia Ibarra: ASP things. But yeah, these people know us. And it's just, it's giving us this scale and personalization
[00:20:44] Amelia Ibarra: in a way we couldn't free, you know, pre six months ago. Like every event after we have is after event.
[00:20:51] Amelia Ibarra: I struggled to, you know, send, I'm like, okay, we should send out hyper personalized follow ups to
[00:20:56] Amelia Ibarra: everyone. To all the sponsors, all the attendees, all the speakers, everybody think about London.
[00:21:01] Amelia Ibarra: That's 2000 people. Annual, that's 10,000 people. Like we could never do it. Right. Like we had to
[00:21:06] Amelia Ibarra: literally cherry pick the people who got like an actual human customized email. Then who with the
[00:21:13] Amelia Ibarra: sales seems like a somewhat customized email to you. And then who just got like a template of
[00:21:17] Amelia Ibarra: the email because we didn't have time to do the rest, right? We just can't send that hyper personalized
[00:21:23] Amelia Ibarra: organization of scale before this. Now, you know, we've sent 20,000 post one to know easily send
[00:21:29] Amelia Ibarra: a highly customized email to all 25 hundred people that come. That's crazy. If you think, just stop
[00:21:34] Amelia Ibarra: and think about that for a second, it's doing all this for us. And this also was something that
[00:21:41] Amelia Ibarra: took not just me, it took you to do for members of the sales team. Like everything that we did is
[00:21:47] Amelia Ibarra: now consolidated into this in a way where the output is obviously fairly for us,
[00:21:52] Amelia Ibarra: positively, right? We've seen some good gains here, but it's not without time, right? So are,
[00:22:01] how do you think about using Arzum specifically for Albound? And you'll see here, that's why I put the
[00:22:06] Amelia Ibarra: data like the positive response rates do vary, right? And so this is varied on agent. This is showing
[00:22:12] Amelia Ibarra: just the ones a website one. You'll see a couple of these are attendee ones, but different years.
[00:22:17] Amelia Ibarra: And so they have slightly different trainings, slightly different things that they're referencing here.
[00:22:23] But these are ones where, you know, these positive response rates do vary depending on how maybe
[00:22:28] Amelia Ibarra: recent they interacted with us. Again, that was probably true pre-AI and it's not true now. But
[00:22:33] Amelia Ibarra: because our Albound emails sent for rep, but this was a crazy sad, I just looked into the last
[00:22:39] thing. Our Albound emails per rep across the board. So across the things I just mentioned,
[00:22:44] Amelia Ibarra: for us, you know, tickets, sponsorships, speakers, whatever. On the average band six months ago,
[00:22:50] Amelia Ibarra: with anywhere between 75, you know, let's say at the low end to 285 at the high and depending on
[00:22:56] Amelia Ibarra: the person, some people are faster than others. Now our AI is blowing that scale out of the water.
[00:23:03] Amelia Ibarra: It does 3000 on its own per month in one, this is just one platform. I'm another one at
[00:23:08] Amelia Ibarra: so that I've actually two more, two more that's doing outbound. This is just one platform that's
[00:23:14] Amelia Ibarra: giving us this leverage. And so I think again, what's working for us is using this to do hyper,
[00:23:22] Amelia Ibarra: specialized, personalized, you know, messaging at scale has been working. There is a,
[00:23:31] Amelia Ibarra: which I fully believe it. I've talked to Jasper, Succio, part of the, there is a two to three
[00:23:35] Amelia Ibarra: week warm-up period with artists and so that they can get your deliverability as close to perfect
[00:23:41] Amelia Ibarra: as possible. You want to do this. You don't want to skip this step. There's a reason I make everybody do
[00:23:45] Amelia Ibarra: it. At first, I was kind of, I'll be honest, like, previous webinars, like, you're like, it's kind of
[00:23:49] Amelia Ibarra: annoying to take two weeks or anytime I need to add new domains, it takes another year, like,
[00:23:54] Amelia Ibarra: I'm a little frustrated. But then you wait and then you see why because you're like, okay,
[00:24:00] you're not only do your email in this hit the inbox, they don't go to promotions. I can't
[00:24:06] Amelia Ibarra: even solve that in Marquetto. So many of our newsletters end up in promotions because actually
[00:24:11] Amelia Ibarra: go to the inbox. And so again, just another point of like differentiation there of things that
[00:24:17] Amelia Ibarra: could do that we can do six months ago. And at the start, we had a review. I was nervous. I
[00:24:23] Amelia Ibarra: wanted to review all the emails myself. But now I just spot check, right? I spot check it.
[00:24:31] But I do mainly let the AI in orders and draft a response. I don't let it send it fully yet,
[00:24:37] Amelia Ibarra: even six months in. I think it's still, and some of my other agents I do empower to do full responses
[00:24:44] Amelia Ibarra: without me looking. But this one in particular, because of where Saster is and maybe if you have
[00:24:50] Amelia Ibarra: multiple products, you might be the same way. Sometimes people ask malls, I've got it questions.
[00:24:54] Amelia Ibarra: And so I think that's where the AI is pretty good. You know, let's just say in this scenario,
[00:24:58] Amelia Ibarra: it's to book a meeting and a person said, yeah, I want a book meeting. I'm like,
[00:25:02] Amelia Ibarra: cool, here's the calendar or the AI can do that. But if someone starts to ask about speaking
[00:25:05] Amelia Ibarra: and sponsorship, that's a common question we get. It's multi-freted. It's not as good. And I think
[00:25:11] Amelia Ibarra: because there's just some human nuance and, okay, do I feel like they're trying to ask me about
[00:25:15] Amelia Ibarra: speaking or free tickets because they want to, they actually want to sponsor or do they just not
[00:25:19] Amelia Ibarra: free tickets and they're kind of wasting my AI's. And so there's still a little bit of that,
[00:25:25] Amelia Ibarra: you know, we do constantly monitor the human attention and responses, specifically
[00:25:34] in this platform that we're using. So again, I do think it, I think the unexpected learning is
[00:25:41] for art is in a particular, and probably any other outbound tool used for AI, for
[00:25:45] Amelia Ibarra: outbound, it relates heavily on human consistency for training and iteration and quality of
[00:25:52] Amelia Ibarra: contacts. Like it's not 100% of not 100, okay, 90% of the contacts we've reached out to with
[00:26:02] Amelia Ibarra: our artisan agents or contacts we had. They're not contacts on going at my new loose show or
[00:26:08] Amelia Ibarra: Apollo or clay or artisan has a way you can do it natively in a platform. I just, you know,
[00:26:14] Amelia Ibarra: I trust our contacts more. And so putting in all that data does require time and requires
[00:26:20] Amelia Ibarra: consistency on our end. So when I've had more time, you know, the sequences and everything works
[00:26:26] Amelia Ibarra: better when I've had less time, it still works on autopilot, but I see a drop off in the amount of
[00:26:31] Amelia Ibarra: responses we get. And that's because I just can't keep up with the AI. Six months in, I have to
[00:26:36] Amelia Ibarra: try and give it fresh contacts. It used to be, I would do it once a week, now I do it
[00:26:43] Amelia Ibarra: twice a week if I can ideally because it's gotten better. Jay right, Lenguipan Power
[00:26:48] Amelia Ibarra: Agency's gotten better. And so ideally twice a week would be better. So that's I think the,
[00:26:54] Amelia Ibarra: again, unexpected learning there. Anything you want to add on outbound, Jason?
[00:27:02] No, I think I think that's a lot here is it's interesting. I think there's a, this is plenty,
[00:27:10] Jason Lemkin: I think the question, I mean, the conclusion obviously is that moving from the two human
[00:27:17] Jason Lemkin: SGRs we had the way we were doing it to AI, there was no no downside in net, right?
[00:27:25] Actually, not necessarily better. It looks like net the open rates response rates were roughly
[00:27:30] Jason Lemkin: similar in the end, but we have 10 times the scale if I to summarize it, right? Correct.
[00:27:34] Jason Lemkin: Yep. I guess the one question that I might have on the audience is that's great. But what about
[00:27:40] Jason Lemkin: like super high value prospects? The ones you would want to reach out to personally, how do you,
[00:27:46] Jason Lemkin: how did we address that? How do you measure that? How do you think about that versus this is a broad
[00:27:51] Jason Lemkin: swath of a lot of potential prospects? Yeah, it's a great version. Yeah, for super high value folks,
[00:27:59] I still put our AIs into draft mode across our agents, right? So there's different use cases where
[00:28:06] Amelia Ibarra: I want to hit different folks, different parties with a message that is maybe hyper personalized,
[00:28:12] Amelia Ibarra: or somebody who's actually met me and would know that, you know, my Amelia get sassard.com is one
[00:28:18] Amelia Ibarra: of my art is an email, the not ameliancestrink.com. And so for those folks, like no matter what platform I
[00:28:27] Amelia Ibarra: use, artism, just some of them, some other platforms to others, I pretty much put the agent
[00:28:32] Amelia Ibarra: to draft out and I see what it says, right? But that still saves me time. Like having a draft that
[00:28:38] Amelia Ibarra: next email, either next email or first email of, you know, whatever I'm trying to action with them
[00:28:43] Amelia Ibarra: as like the end goal is helpful versus me writing everything you've scratched. That's the
[00:28:49] helpful. I think I still spend probably the most time making sure the contact to the right people.
[00:28:55] I think where there's a gap right now is for a lot of these folks, especially our high value ones,
[00:29:02] Amelia Ibarra: I always have to find new people that see see which was manual like that. No AI can do this yet.
[00:29:07] Amelia Ibarra: Trust me, I've looked like. No AI can do this yet. We're like because we have so many CEOs and
[00:29:12] Amelia Ibarra: powers on our database, and maybe you sell to a lot of C suite executives too. The biggest issue I have
[00:29:17] Amelia Ibarra: right now in the AI is not that it's not working or that we have high value contacts that it can't
[00:29:22] Amelia Ibarra: draft an email to pretty good and apparently customize. It's that don't want to send it just to
[00:29:28] Amelia Ibarra: see you. If I'm an email, the CEO of Databricks, like I want to copy his press team, his chief of staff,
[00:29:34] Amelia Ibarra: his CM, if it's for something speaking, probably the CMO too for visibility. I don't want to just
[00:29:40] Amelia Ibarra: send it to Ollie, like even though I have his email and he knowsaster, and there's no way to really
[00:29:45] Amelia Ibarra: do that in the, like there's no good way right now in any AI to find those additional contacts.
[00:29:51] Amelia Ibarra: And also include them in the sequence. Like right now across all across the board, all of our
[00:29:58] Amelia Ibarra: platforms are one to one. Right. So I think that's something where we're six months in. I do think
[00:30:03] Amelia Ibarra: that will get better and the platform tool let you do that more through down the road. But that
[00:30:08] Amelia Ibarra: part takes a lot of time right now. That's kind of like one of my biggest main points.
[00:30:15] Okay. Let's look at the end bound because I want to try and go through all of good market,
[00:30:19] but I'm already getting off of it.
[00:30:24] All right. This is the end bound. So there's some interesting numbers here on the right. My
[00:30:31] Amelia Ibarra: zoom is a little bit in the way. We actually have not had this for six months. We've only had it since
[00:30:36] Amelia Ibarra: August. So August, September, October, a couple of weeks in November, three and a half months.
[00:30:42] Amelia Ibarra: We have not had this one as long because I added out on first and then I tackled it down.
[00:30:47] Amelia Ibarra: Again, you got to steer step your use cases here on AI. I wouldn't try and do everything in
[00:30:52] Amelia Ibarra: GGM all at once. Do one, get it working, and have another one if you want. So then I added in
[00:30:58] Amelia Ibarra: bound. We've had, you could see, it's had a lot of sense, almost 700,000 sessions with people,
[00:31:05] Amelia Ibarra: which we can never do physically. And it's had a thousand conversations. So like sessions versus
[00:31:12] Amelia Ibarra: conversation on this realm is that the sessions are either I think accounts at where it can answer
[00:31:18] Amelia Ibarra: itself. Whereas a conversation is something where the AI agent is actually conversing with the
[00:31:24] Amelia Ibarra: person more fully. It's looking, you know, it's looking at it's trading, it's answering it a bit more.
[00:31:29] Amelia Ibarra: I think that's the new ones, but don't think about work for it, but it's still a lot of sessions
[00:31:33] Amelia Ibarra: with conversations. And then while I took this screenshot, it was nine new on meeting bucks,
[00:31:38] Amelia Ibarra: and then this morning was close to 100. So we've had a lot of interactions with end bound. Now
[00:31:45] Amelia Ibarra: that's always going to be true. Right. This is in now. But this is the data I wanted to share.
[00:31:50] Amelia Ibarra: Because I will say I wasn't as hesitant as adding an outbound agent. There's alternatives to
[00:31:56] Amelia Ibarra: artisan. If you don't like that one, I like that one because they get it's highly
[00:31:59] Amelia Ibarra: specialized on outbound. So I like that one because everything it does is to get the like
[00:32:05] Amelia Ibarra: similar results to what we're saying. Like that's literally its whole manifest too. So I like to
[00:32:10] Amelia Ibarra: go specialize. I know other people like to try and find one platform that can do like multiple
[00:32:15] Amelia Ibarra: ages and try and consolidate for a lot of reason. But I like to go specialize because I do feel
[00:32:20] Amelia Ibarra: like the specialized ones for now still work a lot better because they go deeper. But anyway,
[00:32:25] so then when I added inbound, we've only had this, let's say three months, the end bound agent
[00:32:34] Amelia Ibarra: has been responsible for already a million dollars of revenue. Now you could say, okay,
[00:32:39] Amelia Ibarra: some of that revenue would have closed in me. Right. It's inbound people are reaching out to
[00:32:44] Amelia Ibarra: soundstory in those caseboards. You could live for sponsorships. You could say, okay, you know,
[00:32:48] Amelia Ibarra: one that would end the old day six months ago that would have been routed to a rep. Somebody would
[00:32:52] Amelia Ibarra: have responded eventually, you got in the meeting on the books. And then, you know, hopefully,
[00:32:58] Amelia Ibarra: I don't know. I mean, my data to show our win rates are better now with a uninbound
[00:33:03] Amelia Ibarra: than six months ago. But assuming it was similar, I shouldn't still barely. Let's say, you know,
[00:33:08] Amelia Ibarra: 750 of that would have still closed. The onus here is that it closes not only does it close a lot
[00:33:16] Amelia Ibarra: faster is what we're saying in our data. It's also closing closing at a higher rate than
[00:33:22] Amelia Ibarra: previous to six months ago. So even though it isn't inbound and you could say, okay, there's
[00:33:27] Amelia Ibarra: obviously inherent demand because they're coming inbound. This has given context to both the
[00:33:36] Amelia Ibarra: prospect and our sales team in a way that it's giving us speed. So our amount agent right now is
[00:33:43] Amelia Ibarra: definitely picking up speed. Oh, crazy sad. I just saw two like 70% of our October close one came
[00:33:50] Amelia Ibarra: from the AI. So you could see right there was a little bit of a lag in August, the time,
[00:33:56] Amelia Ibarra: and the most of that melody came last one. But then we have like another 2.5 and pie that is
[00:34:02] Amelia Ibarra: literally attributed to meetings and deals that came from the qualified agent. And
[00:34:08] Amelia Ibarra: that's magical in a couple ways. Now I know some people like to describe it as, okay,
[00:34:12] Amelia Ibarra: it's just a meetings booker. I could do the same thing with just a meetings booker. That's like
[00:34:18] Amelia Ibarra: round robbing and by show that on the website with a little AI. Maybe that's good enough. And maybe
[00:34:22] Amelia Ibarra: that is good enough for you. But I'll say the difference here of why I've become a fan of qualified
[00:34:30] Amelia Ibarra: for what we use on this tool is that it gives you so much context more than a meetings booker,
[00:34:36] Amelia Ibarra: right? Like even if you have an AI meetings booker that's during round robbing for inbound,
[00:34:42] our agent is having conversations with people like it's, okay, wow, you know, let me
[00:34:48] Amelia Ibarra: let me book the meeting. But first, okay, it puts the meeting instantly. It used to be six months
[00:34:52] Amelia Ibarra: ago. You had to fill out a contact form to talk disaster. Then I would write, it would go to me,
[00:34:58] Amelia Ibarra: I would rob robbing it. So there's a delay, like if it's overnight or on the East Coast or a time,
[00:35:04] Amelia Ibarra: I'm not awake. There's a delay for me to round rob it it. Then I send the round robbing to the rep.
[00:35:08] Amelia Ibarra: Then the rep has to respond to that person. And so that process is anywhere from within the same
[00:35:14] Amelia Ibarra: hour to a day later. That's highly inconsistent six months ago. Now our agent is empowered to book
[00:35:21] Amelia Ibarra: meetings on its own and have a conversation. So it's sending, it's not only booking the meeting
[00:35:26] Amelia Ibarra: instantly where this used to take up to a day at the worst gate scenario. The meeting is instant.
[00:35:32] Amelia Ibarra: But it's having a conversation with this person. So that when I give it to the sales team,
[00:35:36] Amelia Ibarra: it literally means they have to go through, like, what do they say to the agent? Do they say anything?
[00:35:40] Amelia Ibarra: Interesting. The agent can also show you other people who open on the website. You could say,
[00:35:45] Amelia Ibarra: oh, hey, cool. Like this person actually booked the meeting with me, but I saw their CEO was on the
[00:35:50] Amelia Ibarra: site or I saw a lot of contacts from the same company around the site. Let me see. And also what they
[00:35:54] Amelia Ibarra: were looking at, it'll show you directly. Okay. This is what they were reading on the website.
[00:35:59] This is what they were probably interested in. And so that context just gives us a lot more, like
[00:36:06] Amelia Ibarra: highly free, qualified contextualized meeting. We don't really have to do discovery anymore because
[00:36:11] Amelia Ibarra: the AI has already done it. The AI already knows what websites you are on. It already knows who was on
[00:36:16] Amelia Ibarra: the site. Who was there? How many times you visited the site? And because we have ours on multiple
[00:36:22] Amelia Ibarra: domains, it can also say, hey, they were also looking at XYZ thing on saster.com. Again, we don't do
[00:36:30] Amelia Ibarra: discovery anymore. We're like, okay, our agent already did it and already has the data. We just
[00:36:35] Amelia Ibarra: used that to do like a theory of what we think. We saw you were looking at XYZ thing. Is that actually
[00:36:40] Amelia Ibarra: what you want to talk about today? Part of sales is still learning what their goals are. But we have,
[00:36:47] Amelia Ibarra: it's so nice now again, we have that baseline with folks. They appreciate it, right? That you're not
[00:36:52] Amelia Ibarra: doing, you're not wasting 10 of their minutes on discovery. You already know what they're about. You
[00:36:56] Amelia Ibarra: know what they've been doing. Or sometimes they're like, oh, I didn't know our CEO was on the site
[00:37:00] Amelia Ibarra: looking at speaking. That's good to know. Maybe I should look at a sponsorship package on it. We're
[00:37:05] speaking. The conversations of qualities anecdotally a lot better. I don't have data around that,
[00:37:10] Amelia Ibarra: but maybe we will now bust. It's just like that. It can do that. So that's an interesting context on
[00:37:20] Amelia Ibarra: selling something that is more of a higher ASP right coast for us. Okay, tickets are like
[00:37:24] Amelia Ibarra: sub $1,000 sponsorships. The most popular one is, let's say, between the 50 to 100K range,
[00:37:31] Amelia Ibarra: there are more captive ones on that. But this is helping us with something that's at a higher
[00:37:35] Amelia Ibarra: price point. Close one a lot faster and we're seeing a lot more of. I will say two interesting things
[00:37:43] Amelia Ibarra: with our move on to the next one. And then anything you want to hit Jason on this one, but
[00:37:49] I say a lot of folks who use qualified that limit their agent, right? Like they limit it to talk to
[00:37:55] Amelia Ibarra: support or talk to sales and there's two buttons and that's kind of it. And then when I talk to
[00:38:01] Amelia Ibarra: other people's qualifies, I've seen it sometimes not as good. I mean, on it, this is not as good.
[00:38:06] Amelia Ibarra: And that's not a fall on the technology. That's a fall on the training. Again, if you take
[00:38:10] Amelia Ibarra: something that is a tier and make it even better, like we have like I've empowered our
[00:38:16] Amelia Ibarra: qualified agent to adjust all of our website. So across saster.com, which is, you know, 20 million
[00:38:22] Amelia Ibarra: words. Saster AI London, Saster Annual. Are you two channel things I upload to it? I'm like,
[00:38:29] Amelia Ibarra: these meetings, I upload these meetings, I upload some of my sponsors meeting. All I upload calls
[00:38:33] Amelia Ibarra: to it. I really kind of know like what we're saying on calls because they can adjust all that.
[00:38:38] Amelia Ibarra: It does so much more than I think most agents do on qualified. And so ours in particular to
[00:38:45] Amelia Ibarra: is I think pretty good, but it's also pretty good because we've empowered it to be that way.
[00:38:50] Amelia Ibarra: There's a level of trust I have with my Amelia AI now that we've also, you know, I talked a little
[00:38:55] bit about the outbound piece of that's booking meeting for sponsors, but it was also selling a lot
[00:39:00] Amelia Ibarra: of tickets. The inbound agent previously, right? You would fill out a form on the website
[00:39:06] for sponsorships. And then if you wanted to buy a ticket, there was kind of nothing.
[00:39:10] Amelia Ibarra: There was like, you could email events at sastering.com six months ago. It wasn't great. And it's
[00:39:17] you know, the number one question our chat gets now. Really, it's you tickets versus sponsorship is,
[00:39:22] Amelia Ibarra: can I have a discount? And so quickly, oh, I think a weekend when I saw the data with qualified,
[00:39:29] Amelia Ibarra: we empowered the agent to sell tickets directly. So what it does now, and if you ask
[00:39:34] Amelia Ibarra: it that question or if you propped it for that question, that you're looking at, you're like
[00:39:37] Amelia Ibarra: seeking a discount, the agent's goal is to not only give you that discount, it will remind you.
[00:39:43] Amelia Ibarra: Because the agent was on our website, it will know if you come back. And if you don't have for
[00:39:46] Amelia Ibarra: a couple days, it will actually even like, Hey, Jason, I give you the code. We have this nice
[00:39:51] Amelia Ibarra: conversation as Amelia AI, you didn't use it. And then it reached out to the code, Hey,
[00:39:55] Amelia Ibarra: are you still interested in people then use that code? Like, again, I can't do that in scale,
[00:40:01] Amelia Ibarra: just me. And it's something we didn't have prior to this. So between our two agents,
[00:40:08] it's now 20% of our ticket revenue for the upcoming London event. We'll see where we net out
[00:40:13] Amelia Ibarra: for London and then where we net out for annual because it will have a lot more time.
[00:40:18] But I think our AI just totally crushes it on this kind of stuff.
[00:40:21] Amelia Ibarra: If you can empower it, if you can get it to work in the same way, man does a crush it.
[00:40:28] Amelia Ibarra: So I love our Amelia AI. I actually want to go film with qualified, I think it's called TABUS,
[00:40:38] to make our AI into a full blown seller and supporter where it's going to have my video and voice.
[00:40:46] Amelia Ibarra: And so that will hopefully roll out by London and you all can play with it there in person too.
[00:40:53] But I'm just letting it do more.
[00:40:59] It's good. Yeah, I want to keep moving because this data is so good. We've set it before, but when we
[00:41:02] Jason Lemkin: look, you know, we're a hundred and days in here, we're 125 days into using Repplet, we're six or seven,
[00:41:09] Jason Lemkin: seven or eight months into using Delphi. If your hands off with your agent, not only will it not
[00:41:15] Jason Lemkin: perform, not only will you not train it properly or iterate, you won't realize all the things
[00:41:21] Jason Lemkin: that can do. It can do so. All of our agents when you get good at it, if you just are really hands on
[00:41:26] Jason Lemkin: with your agent, you work with it every day, you watch results, you're as quantitative and data-driven
[00:41:30] Jason Lemkin: as Amelia is here. If you get there, there is a pot of gold after that because you will find your
[00:41:36] Jason Lemkin: agent can do so much more than you thought it could. That is the magic. But you've got to push on,
[00:41:41] Jason Lemkin: you've got to get really good at what you think it does and then open your eyes for other
[00:41:45] Jason Lemkin: use cases. All these AIs get so powerful, they know all your data, they ingest everything out of you,
[00:41:51] Jason Lemkin: and the underlying LLMs are so powerful, they can't help but do more.
[00:41:58] Yeah, you'll see, I'm reading some comments in the chat too, where you're going.
[00:42:04] Amelia Ibarra: My flash art theory is I like to go deep now with specialized tools where I can just keep adding
[00:42:13] Amelia Ibarra: use cases and add agents within certain tools. I don't use it all in one tool, but I feel like the
[00:42:20] Amelia Ibarra: results are worth it. That's why it's worth. Sometimes I have to put stuff in artisan and qualified
[00:42:26] Amelia Ibarra: separately. Is it a little annoying? Of course, it's a little bit annoying. It's time consuming.
[00:42:31] Amelia Ibarra: Am I going to do it because the response rates I think will be better in the long run for
[00:42:35] Amelia Ibarra: inbound versus outbound? Yeah, so I'm still going to do that for the foreseeable future.
[00:42:40] It's going to be a little bit annoying and painful. That's true of anything. Outbound is always
[00:42:45] Amelia Ibarra: a little bit annoying and painful. The AI would have been a magically wave its wand and
[00:42:50] Amelia Ibarra: the linda via it. It's less painful and I have more scale, but I'm just still outbound.
[00:42:57] Amelia Ibarra: You've been doing it before, AI. You're probably not going to like doing it now.
[00:43:02] A quick one here because I do think I don't know if I'll have to do a part two.
[00:43:10] AI and GTM, there's this middle ground and I do want to spend some time on this because I feel like
[00:43:17] Amelia Ibarra: most people have a misconception about the next product which is Asian forest. I do feel like
[00:43:25] Amelia Ibarra: when I talk to people about it, they're always shocked. They're like, what do you mean?
[00:43:30] Amelia Ibarra: Either they've never seen it. I put more screen shot. Or I'm not sure how to use it
[00:43:38] because I don't know. I think because it's from an existing company versus an
[00:43:45] Amelia Ibarra: company versus a startup. I don't know. But anyways, I guess reaction.
[00:43:50] Amelia Ibarra: But I'm like, yeah, part of our course deck now is Asian forest. I'll explain.
[00:43:55] Asian forest, I've gotten to know their team very well. They're all fantastic humans. Let me say,
[00:44:01] Amelia Ibarra: they are the nicest people on the planet. They're like some of the best people. I now love also,
[00:44:05] Amelia Ibarra: you know, I love the qualified team. I've gotten to know the Asperer and Ardism. Part of this is
[00:44:10] Amelia Ibarra: I do trust the human that are on the backside. I think that's if you're going to pick an AI vendor,
[00:44:16] Amelia Ibarra: I do think that's part of it. You should trust the humans. You should want to work with their
[00:44:21] Amelia Ibarra: human counterparts. I call Replic team Replic team humans. Replic humans. We went there
[00:44:26] Amelia Ibarra: those week. I was like, oh, we're going to go see Replic humans. I'm like, but I like those guys
[00:44:30] Amelia Ibarra: and I trust them. Same thing with any vendor you pick. We have this middle ground where I've
[00:44:36] Amelia Ibarra: gotten to know their team law. I think publicly, they're number one. They're number one use case
[00:44:42] Amelia Ibarra: for agent force is support. I'm building a 2.0 agent that lives somewhere between support and
[00:44:49] Amelia Ibarra: personalization. Our first agent that we deployed, and this was recently, so this was just
[00:44:55] right at Dreamforce, which is like a month ago. It's only been live a month. This is our newest
[00:44:59] Amelia Ibarra: agent right? I had Ardism and I had to qualify and then I had a bunch of other stuff you'll see
[00:45:03] Amelia Ibarra: marketing that I added agent force. We had a gap where it wasn't inbound in the way that qualified
[00:45:12] Amelia Ibarra: is. It wasn't outbound in the way that Ardism mostly is. I had this gap where, embarrassingly,
[00:45:20] post-saster annual, I was like, we literally just from this saster annual, I'm about 1,000 people
[00:45:26] Amelia Ibarra: ourselves team we never followed up with. These are people who literally filled out that forum I
[00:45:31] Amelia Ibarra: was talking about earlier. So they wanted an information about saster annual. I routed it to a rep
[00:45:36] Amelia Ibarra: and then the rep did nothing. I found 1,000 of these people, which is all gone. Like, I can't kill.
[00:45:41] Amelia Ibarra: I'm not going to go, I should email those people an apology, one by one, and email them, but
[00:45:48] Amelia Ibarra: that, again, that would take me too much time. I need the scale. And so I thought, okay,
[00:45:52] Amelia Ibarra: this is probably the best first use case for an agent force agent because these people
[00:45:58] Amelia Ibarra: raised their hand, meaning they're already in our sales force because that's how our forum
[00:46:02] Amelia Ibarra: seems to work. And I already have info about them in sales force, whereas Ardism does a lot of
[00:46:07] Amelia Ibarra: personalization based on what they're posting. This, the magic, I would say, the agent force is
[00:46:13] Amelia Ibarra: that it knows everything your sales force knows, which sometimes they say that to people and they're
[00:46:18] Amelia Ibarra: surprised. I'm like, what? That's the beauty of it. Like, it has all your sales force data. You
[00:46:26] Amelia Ibarra: like, look at what and then you want to do. And then you can use that to them since the context of
[00:46:33] Amelia Ibarra: the email. So I'll show you what I mean. Next, but this is our first use case. We had a thousand
[00:46:37] Amelia Ibarra: leave. Nobody wanted to follow up with. Though it's now sending out rage to mainly those people,
[00:46:45] Amelia Ibarra: like it's still working, again, it's newer. So it's still working that list of a thousand. I also
[00:46:51] Amelia Ibarra: capped it, right, whereas like, Ardism's doing 300,000 a month, it's doing 300,000 a month on
[00:46:56] Amelia Ibarra: month six, like, agent force is very much on, I would say month one at the end of month one,
[00:47:02] Amelia Ibarra: going to month two. So I've capped it. So it's still evenly and those thousand people that we
[00:47:06] Amelia Ibarra: ghosted. But then I also started adding people where if I have a conversation with them
[00:47:12] for a deal cycle, it starts to email them a follow up because sometimes I'm really bad at fun.
[00:47:17] Between those two use cases, what we've seen in this is early days is a higher response rate so far
[00:47:25] Amelia Ibarra: and a huge open rate, like I can't go open rate is 72% is freaking hot. You can't get that in
[00:47:32] Amelia Ibarra: market. You can't get that with a human that doesn't send that email, the open rate is zero
[00:47:37] Amelia Ibarra: and equal zero for an email that was never sent. And even though it's early days, I'm fairly
[00:47:43] Amelia Ibarra: bullish on this one because the early data is pretty good. So I have liked it for that.
[00:47:51] Amelia Ibarra: I think it's a good use case that more folks are getting into. Okay, first, you know,
[00:47:57] Amelia Ibarra: again, support is their number one kind of like agents normal, most people do pull it.
[00:48:01] Amelia Ibarra: Find whatever but are qualified to support it. So like I close my phone that did sales and you'll
[00:48:07] Amelia Ibarra: see I put two sample emails here. This was like a follow up email to again somebody we ghosted.
[00:48:12] And for this agent because it's early days, I haven't empowered it yet to do bookings itself.
[00:48:16] Amelia Ibarra: So that's why it's asking for a meeting versus like just showing a direct booker. And Kyle
[00:48:21] Amelia Ibarra: responded literally right away and said, you know, no thanks, but all attend. Again, never would have
[00:48:28] Amelia Ibarra: happened six months ago because our sales team, nothing against that they just decided not to follow
[00:48:35] Amelia Ibarra: up with these thousand people. And yeah, you could say maybe I started with the use case that is
[00:48:41] Amelia Ibarra: low hanging fruit. Sure, but why also why wouldn't you already have somebody use the other
[00:48:47] agents that we use that I wanted one that was near dear to me because I was like, I end
[00:48:52] Amelia Ibarra: down to just somebody and they never followed up. I salty. Maybe because they I have data and
[00:49:00] Amelia Ibarra: you know them being in our sales force and what their company has done with us. But I think it's
[00:49:04] Amelia Ibarra: something like a nice note like, you know, so I don't know. That's where I went into it. The other
[00:49:10] Amelia Ibarra: thing I'll say about agent force, which was the learning is there's two slides there. So if
[00:49:15] Amelia Ibarra: we're flipping it head on the deck because somebody asked us earlier, actually about the setup of it,
[00:49:20] it is within the UX sales force, right? My biggest learning was like, I will admit, I am not the
[00:49:28] Amelia Ibarra: greatest sales force user on planet Earth. I was not the greatest user six months ago. I've
[00:49:34] Amelia Ibarra: definitely become a better user now in this process, but I wouldn't by no means like, you know,
[00:49:40] Amelia Ibarra: I'm not even sort of not even certified like I know that a lot of people, I'm not Mercado
[00:49:46] Amelia Ibarra: certified either. So I but I would say like in my rankings of tools in our stack six months
[00:49:53] Amelia Ibarra: ago, I would say I was a lot better at Mercado than sales force and I pushed a lot of things for
[00:49:58] Amelia Ibarra: Mercado to sales force just because that's what I was trained on in the early days of the market or
[00:50:03] Amelia Ibarra: versus sales force, which was a sales tool. Only back in the day, they just wouldn't give you
[00:50:08] Amelia Ibarra: access. And so I didn't know all the like nooks and crannies. I learned a lot of them in this
[00:50:13] Amelia Ibarra: process. And so I think that's I think there's a misconception on it's super technical and nobody
[00:50:20] Amelia Ibarra: can get it to work. That's like the number one thing I hear. But honestly, one, I had help with all
[00:50:27] Amelia Ibarra: these platforms, artisan help to sell set of art isn't qualified help to set up qualified.
[00:50:32] Amelia Ibarra: So those first help just set up Asian for it. Like all of these they, it wasn't just me like we did
[00:50:36] Amelia Ibarra: a lot of the trading and tuning. Let's be new outwards, but they helped us with this out of that's
[00:50:41] Amelia Ibarra: not vendor agnostic right now. And I think it's true of any good vendor in AI right now. They do have
[00:50:46] Amelia Ibarra: to help you and they should want to help you get some trustable. They want you to have the same
[00:50:51] Amelia Ibarra: numbers on results. We have I think the Smith's conception of you know, I can't use Asia for if
[00:50:57] Amelia Ibarra: you've been all in Salesforce because it's probably too technical or it's going to be doomed to fail
[00:51:01] Amelia Ibarra: or I probably can't get you know, I'll need either a third party agency or like a Salesforce admin
[00:51:07] Amelia Ibarra: so come do this for me. I'm not a Salesforce admin. I figured this out with their help.
[00:51:12] So again, I think it's for many tours. You'll need their help at the start for sure. Like now I
[00:51:18] Amelia Ibarra: need less help. Now I get help this works. But you'll see too like a lot of things even though they
[00:51:23] Amelia Ibarra: don't look the same are kind of the same concepts. So once you learn one tool because I learned
[00:51:30] Amelia Ibarra: art is in first like this is for reference the art is in setup where this is only two three shots
[00:51:35] Amelia Ibarra: of a very long page. And it's great. But you're seeing like I'm putting in what is this one for
[00:51:41] Amelia Ibarra: this one's for London tickets. I can tell because of what I put in my proof points. And then there's
[00:51:48] Amelia Ibarra: coaching right here that I put in. Then there's other things you have to put into the setup.
[00:51:53] This is not just similar to that where I'm putting in instructions on the prompts builder.
[00:51:58] Amelia Ibarra: Stimilar to are actually copied my 12th agent first. I said copied all the instructions I put
[00:52:05] Amelia Ibarra: into art is in I just put them in date and for us and rewrote them for this use case of email
[00:52:10] Amelia Ibarra: people who haven't been reached out to. And then it worked. So like some of the training you do is
[00:52:16] Amelia Ibarra: again, maybe not going to look physically the same. But some of the same concepts I think are
[00:52:20] Amelia Ibarra: core across any AI tool you use where again between the ones I've shared so far art is in qualified
[00:52:28] Amelia Ibarra: now Phil's first slash agent for us like this logic that I had to learn six months ago. Okay,
[00:52:33] Amelia Ibarra: this is how you tune an agent. This is how you train it. This is how you consistently update it.
[00:52:38] Amelia Ibarra: Does have this kind of universityality to it, which I know seems a little funky. But once you kind of
[00:52:44] Amelia Ibarra: learn how to do it in one, it is easier to do the others. I don't think I could have gotten
[00:52:48] Amelia Ibarra: successful on having all these agents of now learning how to buy good and replicate how to not
[00:52:53] Amelia Ibarra: take in the time to learn the foundations of one of them and go really deep so that I can
[00:52:58] Amelia Ibarra: basically speed through the other ones and say, okay, I kind of know a version of this.
[00:53:03] Amelia Ibarra: I kind of the concepts. You just start to learn how to talk to AI and talk to the agents and the models
[00:53:10] Amelia Ibarra: with your data in a way that again, no one can do you like it's just something you've got to go
[00:53:15] Amelia Ibarra: through yourself of. Okay, I've learned now how to talk to Reppley. I've learned how to talk to
[00:53:19] Amelia Ibarra: you for the agent. I know how to talk to qualified. I know how to talk to Repplet. Like again,
[00:53:24] Amelia Ibarra: certain universities are there actually six months in where if you kind of if you learn one,
[00:53:30] Amelia Ibarra: you can figure out the others because they're not as similar to one another.
[00:53:36] Okay, I have there's a lot of questions. There's eight minutes, but I haven't really gone
[00:53:39] Amelia Ibarra: all to all these. What do you record? Jason try keep going. Actually, I just do questions on
[00:53:43] Amelia Ibarra: do part you. You're on mute. Sorry, let's do questions. I think they asked you are outbound
[00:53:50] Jason Lemkin: and not so important. Let's take questions and then let's break this up into a part two on
[00:53:54] Jason Lemkin: the rest of GTM and AI agents. Okay, okay, I can do part two next week as it will not be long.
[00:54:02] Amelia Ibarra: I can do part two, but I haven't even touched on rev options. Yes, and like we're getting so
[00:54:06] Amelia Ibarra: there's a lot there. Let me go back to the question. Oh, so people like keep going. Do you want to
[00:54:12] Amelia Ibarra: be here for us? I'm going to go back to question. We're going back to a few key questions,
[00:54:24] Amelia Ibarra: and then I'll do a quick overview of the part two. So I'll meet you guys in the middle of that.
[00:54:29] You know, that just start. Let me go back to the start.
[00:54:34] Amelia Ibarra: Someone has asked what are the tools you are using with success? Yeah, they're in this deck, and then
[00:54:44] Amelia Ibarra: I don't sorry, a lot of you asked for a link to the deck. So I'm going to put that in now.
[00:54:51] It wouldn't let me do it while I was talking. I have to refer.
[00:55:04] Hold on. I said to Jason, play.
[00:55:10] Oh, I do think this is important because if we're going to do part two, you guys can also tell me
[00:55:14] Amelia Ibarra: what you want to see in the next one. Okay, here it is. Let me get you guys a link.
[00:55:24] Amelia Ibarra: I think it's not everything you'd be told by something. Let's see how to do.
[00:55:34] You're selling. Like finding this link in a very roundabout way, but I've got it too.
[00:55:42] And also you guys can keep asking questions. I will all stay on. I can go over. So if you guys want
[00:55:48] Amelia Ibarra: to stay on, then get your question answered or if you want to watch the replay later, that is good.
[00:55:54] Amelia Ibarra: 5D. So copy the address. Okay, slides. There we go. Okay, there's one. First,
[00:56:04] make your question. I thought somebody else was asking what's our tools and stack as they join
[00:56:09] Amelia Ibarra: lights. So at the beginning of this presentation, but if you also go to faster.ai slash agents,
[00:56:16] Amelia Ibarra: we talked a lot about these tools. So this has all the tools. You can see I really didn't make
[00:56:21] Amelia Ibarra: a part. I only made it through the. The ones I went through today, but we haven't seen here.
[00:56:29] Amelia Ibarra: So you can go to saster.ai slash agent. There's a little bit more on all of them here.
[00:56:34] Amelia Ibarra: And then I'd like this deck where you can we'll draw it on saster.com too. So that you can also see it
[00:56:39] Amelia Ibarra: there. There's a few good questions here. I think gone the earlier part of the session that was about
[00:56:47] Amelia Ibarra: inbound and outbound.
[00:56:56] Nation. Some folks were asking what is our cost for each of these tools. I think it's
[00:57:01] Amelia Ibarra: done how you should budget for it. It's a good question. I want to get your thoughts on this as
[00:57:07] Amelia Ibarra: well, Jason mainly on the budget side. I would say for costs one, it depends on what you're going to
[00:57:14] Amelia Ibarra: use it for. And I'll give it a quick hand at it. I learned about you, a stitching million dollar ARR
[00:57:21] Amelia Ibarra: CMO this week. And he was like, Oh, I have 10 betas going. I don't know why to have 10 betas.
[00:57:30] Right now, I'm in a bake off with three Jim for an outbound AISCR tools like two for inbound,
[00:57:37] Amelia Ibarra: a couple more for all in one tool. I was like, maybe don't do that. Making my advice is to
[00:57:47] stop all that. I was like, why? I just want to see which one works the best before I spend money.
[00:57:53] Amelia Ibarra: I'm like, I think you got to make a bet here, dude. Like I think in trying to save money,
[00:57:58] Amelia Ibarra: you're actually spending a lot more time than you really would just appoint these that getting
[00:58:03] Amelia Ibarra: the outputs of AI by doing these 10 different betas. I was like, just pick one. And if you feel like
[00:58:09] Amelia Ibarra: the cost is prohibitive, work with the vendor on the cost, see what they can do for you.
[00:58:15] Amelia Ibarra: If not, go to their competitor if you need to. But I was like, don't do 10 trials because you think
[00:58:20] Amelia Ibarra: it's going to magically save you money in the end on AI. There's like the craziest thing I've
[00:58:24] Amelia Ibarra: never heard. I think it to be it is to, first of all, one, I don't think you, I mean, it would be
[00:58:32] Jason Lemkin: nice to have a bake off, but unless you're going to invest the effort to truly train all of them,
[00:58:36] Jason Lemkin: it'd be hard to do a bake off than more than two vendors. You should do a bake off for a variety of
[00:58:40] Jason Lemkin: reasons. There's different flavors, different UI, UX, different limitations, they all have limitations.
[00:58:47] Jason Lemkin: They all have limitations. So I would bake, but I wouldn't do 10 because you won't put the energy
[00:58:51] Jason Lemkin: into training them. The bake off will fail with 10. I would do two, just like in the old days.
[00:58:56] Jason Lemkin: The one thing I would say, Mule, you could add to it is what's the pricing they asked? You can talk
[00:59:00] Jason Lemkin: to the vendors. Here's the tough part, basically all the vendors that we're describing for this,
[00:59:06] Jason Lemkin: for GTM sales, type motions, or marketing, BDR, whatever you want to call it. They all require
[00:59:13] Jason Lemkin: training, they all have a thorough amount of data, and really they're mostly optimized kind of
[00:59:18] Jason Lemkin: around 100k price point. Now sometimes it's 60 or 70k annual and 30k to pay you for the onboarding
[00:59:26] Jason Lemkin: training. Some of the vendors absorb some of the onboarding costs, some don't.
[00:59:33] There are lower end versions, but it is all in the tens of thousands of dollars a year or more,
[00:59:38] Jason Lemkin: and probably more like 20, 30, 40,000. Artisan that we happen to use is launching the low end
[00:59:44] Jason Lemkin: version, right? I think everybody will. And we will be on top of that. And we will test out more
[00:59:52] Jason Lemkin: of these cheaper versions and see how that more automated training works. I'm not skeptical with
[00:59:57] Jason Lemkin: where LLMs and AI's are going today. I think I can guarantee you that the low end cheap versions,
[01:00:02] Jason Lemkin: just, and this is true in support, which is for the long. The low end cheap versions aren't as good.
[01:00:08] And it's not that the software isn't as good. I just did a deep dive with G2 on the CEO of Zendesk,
[01:00:12] Jason Lemkin: and we talked about it. At Zendesk in support, the low end agents work. They just don't
[01:00:16] Jason Lemkin: ingest as much data. They might ingest your wiki in a little bit of information. And so the low end
[01:00:21] Jason Lemkin: Zendesk AI engine is still good, but it may be only as 20% of the power of the enterprise version.
[01:00:26] Jason Lemkin: And I suspect that's what's going to happen. Instead of training this on every bit of data we have
[01:00:31] Jason Lemkin: for a decade, every interaction, every customer action, it's just going to simplify what it trains.
[01:00:36] Jason Lemkin: Maybe Amelia feels it differently. And so it won't be, quote, as good, but it may be plenty good.
[01:00:41] Jason Lemkin: It may be plenty good for $299 a month or 10 grand or what. We don't know. We're going to be objective.
[01:00:47] Jason Lemkin: And I think if we do nothing else, we're going to pilot some low end versions of these and we'll
[01:00:52] Jason Lemkin: compare and contrast for you. But I am not aware of in right now, as this is recorded, I'm not
[01:00:57] Jason Lemkin: aware of any cheap AISDR and BDR tool that works because of the training, gestion, and data.
[01:01:03] Jason Lemkin: But I wouldn't rule it out for 2026, but I would budget 50 to 80 grand or more. And if you can't
[01:01:10] Jason Lemkin: afford that, don't expect much. Just don't expect.
[01:01:16] No, it's a good point. I think the bake-off thing was interesting because that was something
[01:01:21] Amelia Ibarra: I was just kind of shocked when I found this. I was like, well, I know you're trying to say money,
[01:01:25] Amelia Ibarra: but I don't think this is the way to do it. It's just too many. It's just too many and too much.
[01:01:32] Amelia Ibarra: You're either going to say that they all suck or you're going to kind of pick one and it's
[01:01:37] Amelia Ibarra: going to take you too long to actually implement it. And you're supposed to see a moment,
[01:01:41] Amelia Ibarra: like you're CEO is going to get frustrated with you. There's a lot of problems in doing too many
[01:01:45] Amelia Ibarra: bake-offs for all these AI tools in the vein of saving money. There's other reasons
[01:01:51] Amelia Ibarra: you should do it to Jason's point, but I think in the vein of saving money, I'd like for
[01:01:53] Amelia Ibarra: for not the way to save money. The other thing I'll say about budget, I think the
[01:01:58] Amelia Ibarra: HunterK range is right. Some are right below it, some are maybe right above it.
[01:02:03] Depends on what you use it for. I think it does fluctuate based on uses.
[01:02:08] But the other thing I'll say about budget that I've come to learn from folks to and then like trials.
[01:02:15] Amelia Ibarra: Yeah, a lot of these are going to be rolling out self-serverions where it's more of a paid
[01:02:20] Amelia Ibarra: to go or you can try it for a few months and see how it goes and see if you get some of the same
[01:02:25] Amelia Ibarra: results we do. But I would say to the thing that you should budget that is maybe more
[01:02:31] Amelia Ibarra: important than the direct cost is going to be time. We also were able to reallocate budget,
[01:02:39] Amelia Ibarra: right? There are certain things you could do where this was not new budget. I had for all these
[01:02:44] Amelia Ibarra: tools that I went to Jason and said, hey, can't come through for Asian parts qualified.
[01:02:50] But also around the time of Arvinton May, a few people left disaster after. I was like, okay,
[01:02:56] Amelia Ibarra: instead of replacing that headcount, which was already budgeted, I will replace it with the tool.
[01:03:03] And so that's another way to do it. I'm not saying to fire someone and then hire
[01:03:06] Amelia Ibarra: this tool instead. But if something happens to you. We replace two human, the budget from two
[01:03:10] Jason Lemkin: permanents to support our agents. We didn't fire anybody. I really think natural attrition is
[01:03:16] Jason Lemkin: going to create your budget more than, if you're going to fire someone because they don't perform
[01:03:20] Jason Lemkin: just fire someone. You don't fire anyone good to replace them with AI if you haven't learned
[01:03:23] Jason Lemkin: anything. If someone's failed, if they can't close anything or if you're AISGRs and set a single
[01:03:28] Jason Lemkin: appointment, I mean, you're human SGR, maybe just replace that budget with it. You know,
[01:03:32] Jason Lemkin: if you're SGR can't do anything, you know, you can't do worse than zero.
[01:03:38] But we'll track it. Many of you, if you're early stage folks watching this, you'll think that's
[01:03:43] Jason Lemkin: expensive. And if you don't believe in the vendor, it will seem very expensive. It will
[01:03:47] Jason Lemkin: because you'll get quoted by a sales rep a lot of money. And it will feel risky to you if the
[01:03:53] Jason Lemkin: deployment doesn't work. That's why we're not trying to be walking billboards, but we do share
[01:04:00] Jason Lemkin: the vendors that we use. Others are good too. But if you get the right people, it's going to work.
[01:04:05] Jason Lemkin: But it can feel risky. It's tough to start at 500 bucks a month today. But you got to take a
[01:04:12] Jason Lemkin: little risk in life. There's another question for, I think, related to outbound for what is
[01:04:20] Amelia Ibarra: question given. Let me ask, can I have one more thing? I'm pretty interesting. All of the vendors
[01:04:26] have too much demand, including sales. They have too much demand. And so you're going to hear
[01:04:33] Jason Lemkin: that manifested with some of them where they might not take your business. And the main reason,
[01:04:40] Jason Lemkin: Amelia, you could maybe share other anecdotes you learned. I've seen it just a few ways she's
[01:04:43] Jason Lemkin: seen it more often because she interacts more with them. If you don't have enough data,
[01:04:47] Jason Lemkin: if they don't think you have a rich enough data source to train these agents, they might just,
[01:04:51] Jason Lemkin: even if you have the money, they may not take your business. We've sent a lot of business to our,
[01:04:56] Jason Lemkin: the vendors we use directly or just by doing this, we generate millions, generated millions of
[01:05:01] Jason Lemkin: revenue, top of the revenue for all these guys just by sharing what we use. That's the nature
[01:05:06] Jason Lemkin: of the beast, but they turned away a lot of business. We've sent to them a lot of business.
[01:05:11] So don't get flustered, but just be aware, not only is it not durchy, but if you're not an appropriate
[01:05:17] Jason Lemkin: candidate, it's a, it's bad that they have too much business and that it's like everything
[01:05:21] Jason Lemkin: in AI folks are overwhelmed with demand. But also if they tell you they can't support you, ask why
[01:05:27] Jason Lemkin: and listen and they're probably right. Yep. I agree. I think the biggest other thing I've seen is like
[01:05:35] Amelia Ibarra: either through this webinar content we post, right? Folks will then reach out to these vendors or
[01:05:41] Amelia Ibarra: they'll ask me and I'll say, hey, I'll just make a look and enter to you to the team because now I know
[01:05:45] Amelia Ibarra: them. And you know, I'll be like, hey, did that ever work out? Did this person that I referred you
[01:05:51] Amelia Ibarra: actually signed something to some of them don't? So it's, they do have a lot of demand, which shouldn't
[01:05:58] Amelia Ibarra: turn you off, but also they're going to go through with you and the way they did with us,
[01:06:03] Amelia Ibarra: it's not unique to this because it's on another question in the chat.
[01:06:08] Are we getting special upgrades from some of our vendors, how one pricing
[01:06:12] Amelia Ibarra: that are public? Okay, now those three vendors I just focus on today have become
[01:06:19] Amelia Ibarra: sponsors of Staster. Sure. If art isn't hadn't, art isn't actually sponsored Staster before
[01:06:25] Amelia Ibarra: I became a customer. So if they hadn't sponsored, maybe I would be on it if from my ISDR tool
[01:06:30] Amelia Ibarra: talking about it. But because they were a sponsor, I did the classic thing. If I just went to the
[01:06:35] Amelia Ibarra: founder, Jeff, where I said, hey, I want to use this post-eannual, can you help me get like the best
[01:06:41] Amelia Ibarra: person on your team to help me set it up because I didn't know as much at the time. And can you help
[01:06:46] Amelia Ibarra: me figure out like, yeah, what is your pricing? How does all this work? And so we were, I just went to
[01:06:50] Amelia Ibarra: the CEO, but again, if you know the CEO of a company, you're going to do that anyway that hasn't
[01:06:55] Amelia Ibarra: changed in my life. And then I put it in the chat, there are a few features specifically,
[01:07:02] like beyond pricing, we're in a lot of beta features, I would say with all of these vendors
[01:07:06] Amelia Ibarra: across the board. So we spent the most of the time today on sales, but also in market day,
[01:07:11] Amelia Ibarra: most of the things you'll see next week as I'll come back and do in part two, we're in beta features.
[01:07:17] And I think that's partially because one, this is not like a hubris thing, but a lot of
[01:07:23] Amelia Ibarra: vendors have told us because we have so many agents, we're a lot faster now. I'd adopt
[01:07:27] Amelia Ibarra: them than just maybe a typical SaaS company, slash office rent company. I think too, because we
[01:07:33] Amelia Ibarra: spend so much time with them, I think of more use cases, right? I'm like, okay, I started using it
[01:07:38] Amelia Ibarra: for one thing, I wanted to just put it in the end. And I'm like, wait, can it, I'm like, maybe
[01:07:42] Amelia Ibarra: can it do this or that? Or maybe can it do X, Y, Z thing? And so I just see, you know, the founders
[01:07:51] Amelia Ibarra: are, yes, where I put it, it is. I'm like, okay, can the agent maybe do this by
[01:07:55] Amelia Ibarra: have the source cases like the next use case? And sometimes the answer is, yeah, usually the answer,
[01:08:00] Amelia Ibarra: I would say is, yeah, that's already on the right map, but we can give you access. Like, we can
[01:08:04] Amelia Ibarra: have you guys test it, break it. And so we do get access to things, but also because we want to,
[01:08:09] Amelia Ibarra: I want to test these things. I have no capability with the AI, where I want all those data features.
[01:08:14] Amelia Ibarra: So I can be like, okay, if I break it or hallucinate, I understand the risk there of
[01:08:19] chestings on it, that's not fully released. But I will say that's my disclosure, but we do
[01:08:24] Amelia Ibarra: have some features on each of those tools that are not publicly available yet. But some of them
[01:08:30] are like either just launching in the new year or soon. But I don't think that's unique,
[01:08:35] Amelia Ibarra: maybe that's unique to Saster, but I also think it's there's a lot there for, there's a, like,
[01:08:39] Amelia Ibarra: I personally have a lot to do some of those things and they have a lot to test some of those things.
[01:08:43] Amelia Ibarra: Yeah, but let me just, I think it's a good question because we have to have a lot of success.
[01:08:48] Jason Lemkin: Some folks think it's because we have so much data. We thought in the beginning, it turns out
[01:08:51] Jason Lemkin: to not to be true. You just need enough data for these tools to work. I don't need 10 years of
[01:08:55] Jason Lemkin: data six months is enough. You need a volume of actionable data. You don't need to know who came
[01:09:00] Jason Lemkin: to Saster and you'll first meet up in 2012. That data really doesn't help, okay? So it's not so much
[01:09:05] Jason Lemkin: data. Do we get special treatment? I think we do. We get the best people at these vendors helping us,
[01:09:11] Jason Lemkin: the best FDE is the best onboarding folks. And so I want to tell you a counter story,
[01:09:16] Jason Lemkin: just to help you qualify vendors. There's another vendor on this list that we thought about using.
[01:09:23] Great founders like them. We were routed to a very mediocre sales slash onboarding person who
[01:09:29] Jason Lemkin: really didn't want our business. I told us we couldn't use certain features and was a pain to
[01:09:35] Jason Lemkin: work with. And so we passed them by and we never used them. Do that yourself. Talk to these vendors.
[01:09:41] Jason Lemkin: If you have a bad experience, don't use that one. And don't also in the age of AI is where I'm
[01:09:47] getting frustrated. Don't get bamboozled by a sales rep that doesn't know the product or isn't
[01:09:52] Jason Lemkin: technical. Ask to talk to an FDE or a solution architect or an onboarding specialist. Don't waste
[01:09:59] Jason Lemkin: your time with an idiot sales rep. The bet there is the I will tell you some of the very best AI
[01:10:04] Jason Lemkin: companies across the globe. Not just anyone's we're talking about the best ones I know have really
[01:10:08] Jason Lemkin: mediocre sales teams that do not understand the products they're selling. They just don't understand
[01:10:14] Jason Lemkin: how AI coding tools work and how AI support tools are trained or how any of these tools are trained.
[01:10:20] Jason Lemkin: Don't stand for that in the age of AI because a rep will tell you something's just wrong or they
[01:10:25] Jason Lemkin: won't understand a bypass that and say listen if you want my real money, I want to talk to the
[01:10:29] Jason Lemkin: person that's going to be onboarding me and own it. And if some blocker that last worked at
[01:10:35] Jason Lemkin: you know a dated B2B company five years ago and doesn't know AI won't let you talk to that person
[01:10:41] Jason Lemkin: find another vendor you deserve it. You deserve it. Assume the sales rep unless they're technical
[01:10:46] Jason Lemkin: or know their CRAP or have done a deployment. If they hesitate on an answer talk to somebody else.
[01:10:54] And so we just didn't deploy one of these agents since probably as good as the ones on this list
[01:10:58] Jason Lemkin: it's probably just as good because we had the idiot sales guy. He lost all this PR
[01:11:04] Jason Lemkin: revenue promotion friends and just ran the deal into the ground and you deserve to talk to an
[01:11:12] Jason Lemkin: expert an FDE or whatever it is before you sign before you sign and we did with Harry and Rory we
[01:11:19] Jason Lemkin: had Mark Benioff on about a month and a half ago and we talked about what's the number one thing
[01:11:23] Jason Lemkin: you wanted it sells for us. He not only do they want does he want to have thousands more
[01:11:27] Jason Lemkin: forward to put engineers on agent force and AI. He said he wished obviously it's not practical
[01:11:31] Jason Lemkin: at 44 billion in ARR. He wished every company could deploy their agent and have value before
[01:11:36] Jason Lemkin: they sign their contract. Okay, and it's not practical for sales reps it's not even practical for
[01:11:41] Jason Lemkin: the folks the startups on this list. But you should demand as close to that as you can. You should
[01:11:47] Jason Lemkin: demand that you at least talk to an expert who in 20 minutes can tell you exactly how successful
[01:11:52] Jason Lemkin: your tool will be. They'll go that he can just look here she can just look at your sales force data
[01:11:55] Jason Lemkin: look at your upspot data look at your marketo day whatever data pop up a little bit and say yeah
[01:11:59] Jason Lemkin: listen I did this with 20 other customers and clients this will work or no won't work you deserve
[01:12:04] Jason Lemkin: that you deserve that you have to pay 20 grand for it for the training it's going to be your best 20
[01:12:10] Jason Lemkin: grand that you're going to pay this year. Yeah, the other thing I'll say
[01:12:15] to add on to it and then we can answer a few more questions when you put to next week.
[01:12:21] Some are related to cough like I like I said we we replaced headcounts Ben so I reallocate
[01:12:29] Amelia Ibarra: actions I request a reallocated headcounts Ben into some of these tools that will start to
[01:12:35] Amelia Ibarra: happen at your org as people naturally lead for no matter what the reason you can start to say okay
[01:12:40] Amelia Ibarra: can it is it a role where I can start to your mark that budget and move it into a bucket that would
[01:12:45] Amelia Ibarra: then be an AI tool that again mutts a you to replace your entire SDR team with AI and get these three
[01:12:53] Amelia Ibarra: agents that we have you can we thought of it we still have humans here too like I'm saying the
[01:12:58] Amelia Ibarra: magic of this is getting the best A tier players on your team that are still there
[01:13:04] to become S tier with AI so I think there's some of that and I think a lot of folks I talked
[01:13:10] Amelia Ibarra: to Jim more common you probably do two days that just say they're not going to add headcount
[01:13:15] Amelia Ibarra: so that they can empower their teams either Q4 or 235 or Q1 or 26 with these tools like they're
[01:13:22] Amelia Ibarra: just again reallocating budget that they would have to say okay instead of growing the sales team
[01:13:27] Amelia Ibarra: from five to 10 humans next year we're going to keep it at five but we reallocate some of that
[01:13:31] Amelia Ibarra: spends the tool so that those five people can be S tier I think that's a good way to think about
[01:13:37] Amelia Ibarra: the other thing I'll say we're not immune from people roasting our AI and so I think we haven't
[01:13:45] Amelia Ibarra: kind of plays into costs if you decide to roast an AI in the beta because maybe it's not very good
[01:13:51] Amelia Ibarra: I don't know all listen I don't know all the tools I know a lot of them I've seen a lot of them now
[01:13:56] Amelia Ibarra: can't say I know them all there's so many of them I do try if we can't use it for myself I do try
[01:14:02] Amelia Ibarra: it at least learn all the tools and their capabilities so that what folks ask me for recommendations
[01:14:07] Amelia Ibarra: like and make at least an informed answer so I don't know all the tools but I will say there are
[01:14:12] Amelia Ibarra: instances where people roast our AI and they've roasted all of our inherent vendor because they
[01:14:17] Amelia Ibarra: roast our AI I think to some degree that's a little bit okay and your team should be maybe a
[01:14:24] Amelia Ibarra: little bit skeptical and maybe the outlets and the outputs are never going to be perfect but
[01:14:29] Amelia Ibarra: the outputs with the human are never perfect either so maybe if there's one file takeaway before
[01:14:36] Amelia Ibarra: we answer the last questions if it wasn't working pre-AI it probably still won't work now
[01:14:42] if it was working or is working kind of good and AI can get you that leverage then as we've seen
[01:14:47] Amelia Ibarra: in our results then it's even better but you know if you hit it out down pre-AI you're still going
[01:14:52] Amelia Ibarra: to get out there it's you hated if you didn't have the best support or you still won't have the
[01:14:59] Amelia Ibarra: best support documentation for your AI to adjust and your support is still probably going to be
[01:15:03] Amelia Ibarra: to be to your birth is after there are times where our agent can't answer a question and it's a
[01:15:09] Amelia Ibarra: support question and I'm like that's my failing that's and they should I know people roast the AI
[01:15:15] Amelia Ibarra: in those times when yeah it's happened I put it somewhere on the side I think less than 10%
[01:15:20] Amelia Ibarra: of the time or I think 3% of the time well yeah we'll touch on it next week less than 3% of the time
[01:15:27] but when they do roasted I'm like you know what it's not even a failing on the AI's fault it's
[01:15:31] Amelia Ibarra: actually a failing on my fault like it's something they're asking the AI that I didn't train it on
[01:15:36] Amelia Ibarra: I didn't do it on even though it has 20 million words there are certain
[01:15:41] use cases and scenarios where you've asked certain questions that are 20 million words you
[01:15:45] Amelia Ibarra: not have the answer to and they were not going to have the answer to pre AI and they don't have
[01:15:49] Amelia Ibarra: the answer to now last couple questions I'm going to wrap and we'll come back to report to you next week
[01:15:58] there's a few specific questions that are fairly technical but I think they're good ones
[01:16:02] Amelia Ibarra: just so that you guys are thinking through this as well so the first one's on art is in so come
[01:16:09] Amelia Ibarra: back to here which we use for outbound there's two questions on it one someone has done have I
[01:16:16] Amelia Ibarra: played around with the lead-gen context that it has related question of have I seen art is
[01:16:22] Amelia Ibarra: an engaging with duplicate context and a smarter way than maybe a human would
[01:16:29] is there anything built in to prevent bombarding inevitable dupes so on the first part have I
[01:16:35] Amelia Ibarra: experimented with their lead-gen context yes I commented on the chat I just started so like
[01:16:42] Amelia Ibarra: to this point if we're six months in I have 99% of the contacts are ours I just started using it to
[01:16:48] Amelia Ibarra: see how I want to learn it what does we how it does on completely cold outbound contacts but that's
[01:16:55] Amelia Ibarra: a new experiment I'm running so it's really for me to say yet if the data was it's a contact data
[01:17:00] Amelia Ibarra: was good enough for us to keep outing but again I don't think you with the beauty of art is
[01:17:06] Amelia Ibarra: and it's like you know you just a training like the sub eight we can call it sub agents you can call
[01:17:10] Amelia Ibarra: it sub campaigns whatever separately the it's too early for me to see on you know outside contacts but
[01:17:20] Amelia Ibarra: I do want to assess it because there's other things we use when for instance I need to find a new
[01:17:26] Amelia Ibarra: email for a contact that existed in our ecosystem which I think is a lot of people but it's not
[01:17:30] Amelia Ibarra: there anymore we have a lot of contact we've got 12 years of saturated old data makes six year
[01:17:36] Amelia Ibarra: opus now so we are not all at the same job they may still be in Zaz and they still maybe get a
[01:17:42] Amelia Ibarra: company I want to reach out to and that's why contact management to get their new contact a lot
[01:17:48] Amelia Ibarra: of people we have gmail's I will say we've been very careful since the start to get gmail's
[01:17:54] Amelia Ibarra: so you're not going to change your gmail so I have those but for contacts that move on which I
[01:17:59] Amelia Ibarra: think is the common occurrence for those folks that's where I'm testing it so it'll be interesting to
[01:18:03] Amelia Ibarra: see how that pans out now on the question on dupes a lot of it I will say I don't get dupes within
[01:18:10] Amelia Ibarra: a single agent so artisan has artisan will dedupe your list across you know multiple campaigns
[01:18:15] Amelia Ibarra: multiple agents qualified does the same thing sales were so it's the same thing where there's a gap
[01:18:22] Amelia Ibarra: because I have three I have to be super careful in saying okay this bucket of contacts going to
[01:18:30] Amelia Ibarra: artisan this bucket going to qualify that bucket going to sales force and then inevitably all
[01:18:37] Amelia Ibarra: contacts yeah all contact throughout the sales force because we use mercenaries with sales force
[01:18:41] Amelia Ibarra: and so they're kind of all already in sales force anyway and so I don't really see a lot of
[01:18:47] Amelia Ibarra: per one vendor so if you only use one vendor you won't have the issue I do but my insurance I
[01:18:52] Amelia Ibarra: have to be super careful in manual oversight to make sure those contacts are not getting hit by
[01:18:58] Amelia Ibarra: three different gents because those three agents ads of right now mostly do not talk to them
[01:19:04] they're getting there though like I know artisan just pushed artisan just push an update where
[01:19:08] Amelia Ibarra: you could turn on a toggle and you can pick what sales force campaigns do on it to exclude
[01:19:14] so that's great so it's starting to solve for this problem if they know some of their customers
[01:19:19] Amelia Ibarra: like us have multiple agents that don't all live there qualified already syncs natively to sales
[01:19:25] Amelia Ibarra: force so it kind of has that algal by default so again because the backbone of all these three
[01:19:31] Amelia Ibarra: is that sales force is the common denominator it works but I do think it's a it's an interesting
[01:19:38] Amelia Ibarra: new one there like you may not have a problem if you just go deep on one but I thought that problem
[01:19:42] Amelia Ibarra: now we're trying to get data across of different agencies sometimes right now a little bit manual
[01:19:49] Amelia Ibarra: pushing it to a few different places that can be inevitable but again because we're getting
[01:19:54] good results I think it's worth it for the interim last question and then anything you want to
[01:20:06] Amelia Ibarra: hit Jason in the end let's do it somebody asked me about how to trigger all these
[01:20:12] Amelia Ibarra: which I think is a good question it's fairly technical right let me stay here so they're all
[01:20:20] again the underlying foundations and training are all a little bit the same but you know
[01:20:27] Amelia Ibarra: particular to the vendor that you use and so the way you can trigger in or just go to
[01:20:33] Amelia Ibarra: for your work the way you can trigger in or then as you can upload a list let's see this thing
[01:20:39] Amelia Ibarra: you can do you could just export that that's what I do honestly I just export or again I don't
[01:20:44] Amelia Ibarra: want the contacts to be a matter to agent I export the contact I upload them that's the way I do it
[01:20:50] Amelia Ibarra: that's the reason to do it now you can't there's other ways you can do it you can like I said now
[01:20:54] Amelia Ibarra: you can kind of like cherry pit from certain sales force campaigns or contacts that you have
[01:21:00] Amelia Ibarra: you can do just like a search like an intent search on there and do it that way I use CSD it's
[01:21:06] Amelia Ibarra: the easiest trigger also because I don't I've seen this I don't know if this is like a again a platform
[01:21:12] Amelia Ibarra: thing or a methane but I've played different sizes in order to have really different campaigns
[01:21:17] Amelia Ibarra: and different audiences but I see 800 to a thousand as the sweet spot so the other reason why I do
[01:21:22] Amelia Ibarra: CSB is I want to keep it in that band because it seems to perform better for whatever reason
[01:21:28] Amelia Ibarra: I keep it in that band triggering on qualified is more so automatic so also the user can just
[01:21:35] Amelia Ibarra: talk to the agent if you guys go on sasterlin right now you could talk to my Amelia AI that was
[01:21:40] something we're in the early days I used to I still somewhat do it but I use to monitor or qualify
[01:21:46] Amelia Ibarra: like a hawk and me like what are people saying to Amelia AI is she giving the right response is she
[01:21:52] Amelia Ibarra: saying the right thing now I've obviously built some like trust and comfortability with it and I let
[01:21:56] Amelia Ibarra: it run and it will tell me if it needs to be it'll break its hand and say someone's interacting and
[01:22:02] Amelia Ibarra: needs your help and then I'll jump in but now she doesn't say that and I just let it go full autopilot
[01:22:08] so that's how that's triggered I'll talk next week if I're to you how I trigger some of the email
[01:22:12] Amelia Ibarra: that it's doing I made the earlier case if I if I if our agent gives you a code it sends you an
[01:22:17] Amelia Ibarra: email fall up in a few days I'll show that more so next week on the marketing side because there's
[01:22:22] Amelia Ibarra: different ways you can think about using that use case that's relevant for you and then in
[01:22:27] Amelia Ibarra: agent course the trigger is I'm a screen job for it so to be questioned but the trigger is faced
[01:22:34] Amelia Ibarra: on either the you can do it on a gam lead level contact level or like a campaign level it's I will
[01:22:43] Amelia Ibarra: say that portion of it I think I think they just pushed it I think you know as we were rolling
[01:22:50] Amelia Ibarra: this out we did it very manually just to make sure it wasn't like spamming a thousand people all at
[01:22:55] Amelia Ibarra: one but then since then I've been able to say okay I've got like a list of contacts already
[01:23:00] Amelia Ibarra: in filled course I could put them into a campaign and then I just I then I could just have the
[01:23:05] Amelia Ibarra: entire campaign go live on the agent and it'll parse it out the way I think that should write
[01:23:10] Amelia Ibarra: okay you've got a thousand people I'm liking it them all at once I'm gonna see what time zone they're
[01:23:15] Amelia Ibarra: all at the times you want me to email those folks and I'll just start to queue them up you can do it
[01:23:21] either way it's actually gotten easier so I commend them on that easier on how to in our use case for
[01:23:26] Amelia Ibarra: this fails this sales motion that we use it for it's gotten easier to trigger this particular flow
[01:23:37] and you also have a wrap on sorry we have to do part two guys
[01:23:40] Amelia Ibarra: okay good okay cool yeah you guys can keep you can I'm just like is it earlier just a million
[01:23:53] Amelia Ibarra: spring we try and answer any additional question I'm not only to not often but I will add you
[01:23:58] Amelia Ibarra: in a week when I check it and then the we will do part two next week's also and then as a follow-up
[01:24:04] Amelia Ibarra: to everyone so we can cover the rest of gtm and then I'll do a much shorter version of this at
[01:24:10] Amelia Ibarra: saster AI in London if there's anything you want to see in particular for part two I've already
[01:24:16] Amelia Ibarra: gotten some good ideas from this just let me know I will put into part two and then we'll see you next
[01:24:21] Amelia Ibarra: thanks
[01:24:29] you didn't create a startup to run a small business let Salesforce help you connect data automate
[01:24:35] Jason Lemkin: busy work and empower employees on the only platform you will ever need no matter how big you
[01:24:39] Jason Lemkin: get with smarter AI and built in collaboration tools like SAC which we use and you use the sky
[01:24:45] Jason Lemkin: is the limit learn how Salesforce works for startups at Salesforce.com slash SMB that's Salesforce.com
[01:24:52] Jason Lemkin: slash SMB
[01:24:57] hey saster imagine having agents for every support tab one that triage is tickets
[01:25:02] Amelia Ibarra: another that catches duplicates one that spots children's that'd be pretty amazing right
[01:25:06] Amelia Ibarra: happy fox just made it real with autopilot these prebuilt AI agents deploying about 60 seconds
[01:25:12] Amelia Ibarra: and run for as low as 2 cents per successful action all that sits inside the happy fox omni
[01:25:17] Amelia Ibarra: channel AI first support stack chatbot co-pilot and autopilot working as one check them out at
[01:25:24] Amelia Ibarra: happyfox.com slash saster