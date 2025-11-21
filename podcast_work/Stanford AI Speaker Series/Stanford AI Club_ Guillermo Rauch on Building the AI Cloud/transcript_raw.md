# Stanford AI Club: Guillermo Rauch on Building the AI Cloud

**Podcast:** Stanford AI Speaker Series
**Date:** 2025-11-21
**Video ID:** Uac2ZCpuU2Y
**Video URL:** https://www.youtube.com/watch?v=Uac2ZCpuU2Y

---

[00:00:00] These are just like cutting-edge thoughts.
[00:00:02] SPEAKER_00: We produce this presentation with B0, of course.
[00:00:06] SPEAKER_00: And kind of wanted to give you guys kind of a dump
[00:00:09] SPEAKER_00: of where my head is at, some of the stuff
[00:00:12] SPEAKER_00: of working on a Purcell.
[00:00:13] SPEAKER_00: And some things that could be useful for you guys
[00:00:16] SPEAKER_00: as you get through college and beyond.
[00:00:19] SPEAKER_00: Obviously, I have to say, I'm really interested always
[00:00:23] SPEAKER_00: in feedback from you guys who have Purcell, Misha, et cetera.
[00:00:26] SPEAKER_00: I Purcell, one of our key priorities
[00:00:29] SPEAKER_00: and things that we work on every day
[00:00:31] SPEAKER_00: is enabling innovators and startups.
[00:00:32] SPEAKER_00: So keep that in mind.
[00:00:35] SPEAKER_00: Also, happy to announce that Stanford is now on Purcell.
[00:00:39] SPEAKER_00: So I tweeted about this yesterday.
[00:00:42] SPEAKER_00: We're hosting FTL, Stanford.edu,
[00:00:44] SPEAKER_00: with a lot more departments coming.
[00:00:46] SPEAKER_00: So I'm really excited to be here today
[00:00:48] SPEAKER_00: because I tweeted that this session's smartest university
[00:00:52] SPEAKER_00: as well last week.
[00:00:55] SPEAKER_00: And so, very cool stuff.
[00:00:57] SPEAKER_00: So I think a lot of you guys know about us.
[00:01:00] SPEAKER_00: But we've hit some pretty awesome milestones recently.
[00:01:04] SPEAKER_00: So next year has doubled the number of downloads year
[00:01:07] SPEAKER_00: over year.
[00:01:08] SPEAKER_00: We're just talking about how the future of developer experience
[00:01:11] SPEAKER_00: is agents holding developer tools.
[00:01:14] SPEAKER_00: Not the developers holding developer tools directly.
[00:01:16] SPEAKER_00: I think it's the important mindset shift that's happening.
[00:01:20] SPEAKER_00: That actually resulted in a re-exceleration
[00:01:23] SPEAKER_00: of the next year's adoption.
[00:01:24] SPEAKER_00: So GitHub just also mentioned the other day
[00:01:27] SPEAKER_00: that TypeScript is the number one language again.
[00:01:30] SPEAKER_00: We're so back.
[00:01:31] SPEAKER_00: Python was the number one language last year.
[00:01:33] SPEAKER_00: The hypothesized this is a byproduct of Python.
[00:01:37] There are so many tools out there, like VZero,
[00:01:41] SPEAKER_00: where you prompt and you end up with a bunch of TypeScript code
[00:01:46] SPEAKER_00: that is placed at Purcell itself,
[00:01:48] SPEAKER_00: Hose and Deliver's websites, which is recently
[00:01:50] SPEAKER_00: passed a trillion requests per month.
[00:01:52] SPEAKER_00: And we started over 10 million customers.
[00:01:57] I wanted to give you guys some context
[00:01:58] SPEAKER_00: on how I'm thinking about the future by telling you
[00:02:01] SPEAKER_00: a little bit about the beginning of Purcell.
[00:02:04] SPEAKER_00: So Purcell was started out because I
[00:02:05] SPEAKER_00: wanted to make creating for the web and experience
[00:02:08] SPEAKER_00: that's basically the instantaneous feeling
[00:02:12] SPEAKER_00: of bringing a new idea to life.
[00:02:15] SPEAKER_00: And I think recently, in going back to the idea of startups,
[00:02:20] SPEAKER_00: on Purcell, you should be able to not only test out
[00:02:23] SPEAKER_00: your hypothesis, your ideas to a prototype,
[00:02:25] SPEAKER_00: but actually bring entire businesses alive.
[00:02:27] SPEAKER_00: Purcell is the tool that I wished I had had when Purcell got
[00:02:31] SPEAKER_00: started.
[00:02:33] SPEAKER_00: Also, if you're looking to make a dent in the world
[00:02:37] SPEAKER_00: or a startup here, I think you have to look at 10 years
[00:02:40] SPEAKER_00: into the future.
[00:02:40] SPEAKER_00: So yeah, fun enough.
[00:02:42] SPEAKER_00: Yesterday was the 10th year anniversary
[00:02:45] SPEAKER_00: of Purcell incorporating.
[00:02:48] SPEAKER_00: And for us, it's always day zero.
[00:02:51] SPEAKER_00: When we started this company, LLM's were not a thing.
[00:02:56] SPEAKER_00: The AISDK was not a thing.
[00:02:59] SPEAKER_00: Not even next day, I was a thing.
[00:03:00] SPEAKER_00: So keep that in mind as you continue to iterate
[00:03:04] SPEAKER_00: and come up with new ideas.
[00:03:06] SPEAKER_00: Our latest new idea and our focus for the foreseeable future
[00:03:11] SPEAKER_00: will be in building what we call the AI cloud.
[00:03:14] SPEAKER_00: When Purcell was started, the main problem
[00:03:17] SPEAKER_00: at age that I was scratching is I saw a huge amount
[00:03:21] SPEAKER_00: of potential in cloud computing, but it was broadly inaccessible.
[00:03:26] So if you had an idea and you wanted
[00:03:28] SPEAKER_00: to deploy it to the cloud, especially
[00:03:31] SPEAKER_00: for you guys as a student, just the friction in prototyping it,
[00:03:36] SPEAKER_00: bringing it to life, and then potentially scaling it
[00:03:39] SPEAKER_00: was so significant that perhaps a lot of ideas
[00:03:41] SPEAKER_00: were just not how they existed to begin with.
[00:03:44] We see a similar opportunity with AI
[00:03:46] SPEAKER_00: because if you have an idea for the next big assistant agent
[00:03:51] SPEAKER_00: or AI application, there's significant friction
[00:03:54] SPEAKER_00: and bringing that to reality.
[00:03:57] SPEAKER_00: And so there's three fundamental shifts behind this
[00:03:59] SPEAKER_00: that we've noticed.
[00:04:02] Number one is a disruption of the very thing
[00:04:05] SPEAKER_00: that we're looking at now.
[00:04:06] SPEAKER_00: And the very thing that we created when we started Purcell,
[00:04:09] SPEAKER_00: which is this concept of going from pages to agents.
[00:04:12] So one interesting irony of the pipe coding
[00:04:15] SPEAKER_00: and pipe coding tool site zero, where a lot of things
[00:04:18] SPEAKER_00: that are being created with platform site,
[00:04:22] SPEAKER_00: lovable and replete and things like that,
[00:04:24] SPEAKER_00: is that they're actually outputting pages,
[00:04:26] SPEAKER_00: which is of course a silvator very relevant.
[00:04:30] SPEAKER_00: But there is a future ahead of us
[00:04:31] SPEAKER_00: where consuming information that has been statically defined
[00:04:36] SPEAKER_00: by an engineer or semi-statically defined by an engineer
[00:04:38] SPEAKER_00: is not a noticeable element.
[00:04:41] SPEAKER_00: I personally believe pages will be due to be really important,
[00:04:44] SPEAKER_00: but a lot of the ways that we interact with computers
[00:04:48] SPEAKER_00: and the future will happen through agents.
[00:04:51] SPEAKER_00: For Purcell specifically, one of the things
[00:04:53] SPEAKER_00: that we're investing is if you look at how the cloud works
[00:04:57] SPEAKER_00: until now, obviously Purcell has moved
[00:04:59] SPEAKER_00: the needle here significantly, but most of what the cloud gives
[00:05:02] SPEAKER_00: you is a bunch of problems.
[00:05:04] SPEAKER_00: And this is true actually for a lot of existing systems
[00:05:06] SPEAKER_00: at scale.
[00:05:07] SPEAKER_00: If you're running a cluster in some kind of cloud today,
[00:05:12] SPEAKER_00: you have to constantly be paying attention
[00:05:14] SPEAKER_00: to a lot of negative feedback the system gives you,
[00:05:16] SPEAKER_00: whether it's errors, alerts, misconfigurations, et cetera.
[00:05:21] SPEAKER_00: So our goal is to switch to a world of complete autonomy,
[00:05:26] SPEAKER_00: where the cloud offers you solutions or other problems.
[00:05:30] SPEAKER_00: And the other one that's very close to my heart
[00:05:31] SPEAKER_00: because next year it's gotten as big as it has
[00:05:34] SPEAKER_00: because it's open source.
[00:05:35] SPEAKER_00: So if anybody can pick it up, if anybody can deploy it,
[00:05:39] SPEAKER_00: the third big shift that we are both investing in,
[00:05:42] SPEAKER_00: and I think we're going to be seeing over the next 10 years
[00:05:44] SPEAKER_00: is this switch from close to open.
[00:05:48] SPEAKER_00: In terms of pages to pages, I think this one
[00:05:50] SPEAKER_00: is one of the most interesting ones.
[00:05:51] SPEAKER_00: We're just riffing on an idea of what
[00:05:54] SPEAKER_00: would it look like if ChatGbD was behind every page render
[00:05:59] SPEAKER_00: that happens on the internet?
[00:06:01] SPEAKER_00: Today, the way that this page is going
[00:06:04] SPEAKER_00: to create it is engineers go out and define a bunch of react
[00:06:09] SPEAKER_00: render functions.
[00:06:10] SPEAKER_00: They bring in a lot of data.
[00:06:11] SPEAKER_00: It's kind of like deterministic, right?
[00:06:15] A lot of what I think people actually
[00:06:18] SPEAKER_00: need in order to solve problems is not
[00:06:20] SPEAKER_00: to consume UI and interact with the UI directly.
[00:06:24] A lot will happen in the foreground,
[00:06:26] SPEAKER_00: and a lot will happen through conversational interfaces
[00:06:31] SPEAKER_00: instead of generic UIs.
[00:06:34] I have this mental model that I've been working for a while.
[00:06:37] SPEAKER_00: I actually recently shared this with Andy Jassy at AWS,
[00:06:43] SPEAKER_00: and we kind of riffed on.
[00:06:45] SPEAKER_00: When AWS first came out, a lot of what the cloud was looking
[00:06:53] SPEAKER_00: to solve was you go to Amazon.com,
[00:06:57] SPEAKER_00: you want to respond to 100 milliseconds.
[00:07:00] SPEAKER_00: 100 milliseconds of latency has an impacting conversion,
[00:07:03] SPEAKER_00: speed is king, right?
[00:07:06] SPEAKER_00: And as we evolved towards this AI cloud,
[00:07:09] SPEAKER_00: I think we're going to see a shift towards,
[00:07:12] SPEAKER_00: well, it's not so important anymore
[00:07:14] SPEAKER_00: than computation happens instantaneously.
[00:07:17] SPEAKER_00: What actually matters more is that you get the right response.
[00:07:21] SPEAKER_00: We see this all the time when, for example,
[00:07:23] SPEAKER_00: you use ChatGbD and you say, GPT-5 Pro mode.
[00:07:27] You don't care so much that you get an answer instantaneously.
[00:07:31] As long as you get some feedback over time,
[00:07:33] SPEAKER_00: so you get a stream of token,
[00:07:35] SPEAKER_00: so you get a stream of reasoning traces, et cetera,
[00:07:38] SPEAKER_00: as long as you get the right answer of that right solution
[00:07:40] SPEAKER_00: that you were after, you're happy.
[00:07:42] Obviously, for cell-created, the framework for pages
[00:07:45] SPEAKER_00: in UI, as I mentioned, that we've been calling
[00:07:47] SPEAKER_00: this sort of the traditional cloud foundation slide
[00:07:49] SPEAKER_00: is going to continue to be super relevant.
[00:07:52] SPEAKER_00: But now we're working on the framework
[00:07:54] SPEAKER_00: for defining AI applications and agents.
[00:07:57] Another thing that I've been particularly excited about,
[00:08:00] SPEAKER_00: and we're seeing this benefit of growth in,
[00:08:02] SPEAKER_00: is I call it the metaphor of a CDN, right?
[00:08:05] SPEAKER_00: CDNs came and solved a lot of problems
[00:08:08] SPEAKER_00: for the traditional web because it was unreliable,
[00:08:12] SPEAKER_00: because it needed to be secured,
[00:08:15] SPEAKER_00: because it needed to fail over.
[00:08:17] We're kind of seeing the same thing with token providers.
[00:08:21] SPEAKER_00: There's frequent outages, people run out of capacity,
[00:08:25] SPEAKER_00: you get rate limited, you actually
[00:08:27] SPEAKER_00: might need to do some kind of intelligent routing
[00:08:29] SPEAKER_00: based on the prompt, you might want to do some intelligent
[00:08:32] SPEAKER_00: caching.
[00:08:33] SPEAKER_00: So we've been working on what we call this CDN of tokens,
[00:08:37] SPEAKER_00: with the Vercel AI gateway, or you might have used something
[00:08:40] SPEAKER_00: like OpenRider.
[00:08:42] SPEAKER_00: Another big shift that we're seeing is we humans
[00:08:46] SPEAKER_00: used to be responsible for all of the code that run in the cloud.
[00:08:51] Increasingly, it's agents that are responsible for it,
[00:08:54] SPEAKER_00: and it's on two domains.
[00:08:55] SPEAKER_00: Obviously, you're using agents when
[00:08:57] SPEAKER_00: you build your applications, but also a lot of code
[00:09:00] SPEAKER_00: is being written and executed,
[00:09:03] SPEAKER_00: ephemerally, work on the man, meaning code
[00:09:06] SPEAKER_00: that we've never seen before gets executed.
[00:09:08] SPEAKER_00: So the metaphor here is that we're building the EC2 of AI,
[00:09:14] which is the Vercel sandbox.
[00:09:16] SPEAKER_00: So every single day when you push code of Vercel,
[00:09:19] SPEAKER_00: we create it when we call it micro VM,
[00:09:22] SPEAKER_00: or a ephemeral virtual machine that takes in your code,
[00:09:25] SPEAKER_00: and then you can build it and optimize it for production.
[00:09:29] SPEAKER_00: You can think of us having reused that infrastructure
[00:09:32] SPEAKER_00: that we've built for the build process,
[00:09:35] SPEAKER_00: and now we're giving it to agents,
[00:09:36] SPEAKER_00: so that agents can basically write and execute
[00:09:39] SPEAKER_00: any kind of code in a secure fashion.
[00:09:43] SPEAKER_00: And the other one that I mentioned
[00:09:43] SPEAKER_00: that I think is really interesting is,
[00:09:46] SPEAKER_00: so much of the computation that was triggered by the web
[00:09:50] SPEAKER_00: was very quick, mostly CPU bound and instantaneous.
[00:09:55] And what we're seeing now is this shift
[00:09:57] SPEAKER_00: towards compute that runs in the background.
[00:09:59] SPEAKER_00: So from the foreground to the background,
[00:10:01] SPEAKER_00: we created a technological fluid compute
[00:10:04] SPEAKER_00: that is optimizing for packing lots of requests
[00:10:08] SPEAKER_00: within the same serverless function instance.
[00:10:11] SPEAKER_00: It actually addresses a lot of the problems
[00:10:14] SPEAKER_00: of the old serverless pair, and especially with Lambda had.
[00:10:18] SPEAKER_00: So to give you a concrete example,
[00:10:20] SPEAKER_00: if you have an LLAM that is thinking for 30 minutes,
[00:10:24] SPEAKER_00: the way that old serverless compute
[00:10:26] SPEAKER_00: primitive is charged to you is 30 minutes of wall time.
[00:10:30] Now, we multiply that by, you have 1,000 users.
[00:10:33] You get 1,000 instances of 30 minutes of wall time
[00:10:36] SPEAKER_00: that you get charged for.
[00:10:37] SPEAKER_00: So we had to innovate and we created something called fluid.
[00:10:41] SPEAKER_00: It optimizes for packing compute more densely
[00:10:44] SPEAKER_00: or requests more densely within the same unit of compute.
[00:10:47] SPEAKER_00: And the other really interesting thing,
[00:10:49] SPEAKER_00: we created a new pricing multiple active CPU.
[00:10:52] SPEAKER_00: We only charge for the computation that actually happens.
[00:10:56] SPEAKER_00: And this active CPU model extends to both sandbox
[00:11:00] SPEAKER_00: and the compute that runs when you make an API call.
[00:11:03] SPEAKER_00: This is quite interesting because it
[00:11:05] SPEAKER_00: means that when you give this micro VMs
[00:11:08] SPEAKER_00: for computers to an agent, they can kind of like just
[00:11:13] SPEAKER_00: kind of go nuts in terms of how long they use it.
[00:11:16] SPEAKER_00: And you as a developer are not worried about the building
[00:11:19] SPEAKER_00: of it for so long.
[00:11:22] The other one that I'm kind of obsessed with is this idea
[00:11:24] SPEAKER_00: that almost every compute platform at scale
[00:11:27] SPEAKER_00: has been predicated on the existence of a human operator
[00:11:32] SPEAKER_00: that shoulders the burden of dealing mostly with problems.
[00:11:36] SPEAKER_00: So and make it even give you an idea
[00:11:39] SPEAKER_00: or an inspiration of how this will shake out
[00:11:42] SPEAKER_00: even companies at scale, right?
[00:11:44] SPEAKER_00: A lot of companies in the cloud infrastructure space,
[00:11:48] SPEAKER_00: even public ones are, for example, predicated
[00:11:51] SPEAKER_00: on the idea of observability.
[00:11:53] SPEAKER_00: There's a huge market of observability
[00:11:55] SPEAKER_00: that basically all it gives you is mostly bad news
[00:11:59] SPEAKER_00: of the kind of, here's a chart of how your latency has
[00:12:03] SPEAKER_00: gotten worse.
[00:12:04] SPEAKER_00: Here's a chart of errors over time.
[00:12:09] For some reason, they actually shipped something
[00:12:11] SPEAKER_00: that we call anomaly alerts with AI investigations,
[00:12:14] SPEAKER_00: which is sort of our answer to this.
[00:12:16] Whenever something bad happens at runtime,
[00:12:19] SPEAKER_00: whether it's the US East to one meltdown
[00:12:21] SPEAKER_00: that happened the other day,
[00:12:22] SPEAKER_00: it should result in actionable solutions.
[00:12:25] SPEAKER_00: So it'll take the form of for requests
[00:12:28] SPEAKER_00: where the agents suggest that you make a change to your code.
[00:12:32] SPEAKER_00: You might take the form of recommendations
[00:12:35] SPEAKER_00: or automated actions in the case of security, for example.
[00:12:38] SPEAKER_00: So every single day, we get massive attacks,
[00:12:42] most of which we can definitely say,
[00:12:44] SPEAKER_00: this is traffic that is not denied.
[00:12:47] SPEAKER_00: We block it, it's a botnet, it's a ddy-setank, et cetera.
[00:12:50] SPEAKER_00: But there's a lot of great area in the cloud
[00:12:53] SPEAKER_00: where you might get an anomaly of traffic,
[00:12:56] SPEAKER_00: and we have to give you the option to decide,
[00:12:59] SPEAKER_00: OK, block it, allow it, throw it away, challenge it, et cetera.
[00:13:05] And then the big one I mentioned, maybe the one that's
[00:13:08] SPEAKER_00: most close to my heart in the mission of Excel
[00:13:10] SPEAKER_00: is they shipped from close to open.
[00:13:14] SPEAKER_00: So what you look at here is the plot of downloads
[00:13:17] SPEAKER_00: of the different SDKs to write AI applications.
[00:13:22] SPEAKER_00: And I'm pretty inspired by the fact
[00:13:24] SPEAKER_00: that right now the fastest growing SDK
[00:13:28] SPEAKER_00: for creating this agents or apps for sales AI SDK,
[00:13:32] SPEAKER_00: which is this provider agnostic and runtime agnostic
[00:13:36] SPEAKER_00: and gateway agnostic way of accessing tokens.
[00:13:39] SPEAKER_00: Our goal with this module is to provide an API that's not
[00:13:43] SPEAKER_00: lossy, meaning if open AI or a traffic
[00:13:45] SPEAKER_00: come out with a new API or a new way of doing caching
[00:13:48] SPEAKER_00: or whatever, as the SDK can perfectly model it.
[00:13:51] SPEAKER_00: But at the same time, it gives back to the world
[00:13:54] SPEAKER_00: the flexibility to switch between models.
[00:13:57] SPEAKER_00: And it looks like we're in track to actually surpass opening
[00:14:00] SPEAKER_00: and I probably sometimes be here or early next year.
[00:14:03] SPEAKER_00: So if this module becomes the prevalent way
[00:14:06] SPEAKER_00: that TypeScript JavaScript in soon by the engineers to AI,
[00:14:10] SPEAKER_00: we'll be able to allow for that portability
[00:14:13] SPEAKER_00: and hopefully the emergence of more open solutions.
[00:14:17] SPEAKER_00: We also announced the next JS eBounce the other day.
[00:14:22] SPEAKER_00: So I'm really excited about this.
[00:14:24] SPEAKER_00: We will be extending this effort to a lot
[00:14:26] SPEAKER_00: of our open source projects.
[00:14:29] SPEAKER_00: Actually, if any of you guys are interested in this research
[00:14:34] SPEAKER_00: direction or contribution, let me know.
[00:14:37] SPEAKER_00: So we started out with defining really hard problems
[00:14:40] SPEAKER_00: that we encounter in next JS.
[00:14:43] SPEAKER_00: One thing that elements traditional struggle is keeping up
[00:14:46] SPEAKER_00: with API version changes or variance in APIs.
[00:14:51] SPEAKER_00: So app writer comes out or next JS 16 comes out
[00:14:55] SPEAKER_00: and there's a new directive or there's a new API.
[00:14:58] SPEAKER_00: Can the agent successfully discover what
[00:15:02] SPEAKER_00: is the next JS version being used, what
[00:15:04] SPEAKER_00: is the right API to use in this case, et cetera.
[00:15:07] SPEAKER_00: There's a little bit of a shared responsibility
[00:15:09] SPEAKER_00: and model.
[00:15:09] SPEAKER_00: Of course, we have to make the DX as good as possible
[00:15:12] SPEAKER_00: for the agent.
[00:15:14] SPEAKER_00: But we're ranking both agents and models in this case.
[00:15:19] SPEAKER_00: You can look at this success rate
[00:15:20] SPEAKER_00: of the best model available cloud is only 42%.
[00:15:24] SPEAKER_00: So what we want to do with this is the underlying platform
[00:15:29] that is used for writing and disevaluations.
[00:15:31] SPEAKER_00: We believe will be the future of testing systems.
[00:15:34] SPEAKER_00: So traditionally what next has done in order
[00:15:37] SPEAKER_00: to grow, in order to be a reliable and successful piece
[00:15:40] SPEAKER_00: of software is with write code in the form of compiler
[00:15:43] SPEAKER_00: and runtime.
[00:15:44] SPEAKER_00: Then we write unit tests and integration tests
[00:15:47] SPEAKER_00: and end-to-end tests.
[00:15:48] SPEAKER_00: And then we evangelize on X and other forums.
[00:15:52] SPEAKER_00: I think the evangelism to humans
[00:15:54] SPEAKER_00: will give way to evangelism to agents.
[00:15:57] SPEAKER_00: So this is our way of saying, hey, agents,
[00:16:00] SPEAKER_00: like here's the exams that you need to take
[00:16:02] SPEAKER_00: in order to be a proficient next-genese agent
[00:16:05] SPEAKER_00: or next-genese engineer.
[00:16:07] SPEAKER_00: As I mentioned, the underlying platform
[00:16:08] SPEAKER_00: is both the testing and evaluation system
[00:16:11] SPEAKER_00: and the execution layer, which actually
[00:16:14] SPEAKER_00: uses our sandbox for running the agents
[00:16:16] SPEAKER_00: and you just started getting away for accessing the models.
[00:16:19] SPEAKER_00: We will be extending into spelled,
[00:16:21] SPEAKER_00: nogged, AISDK, Turbo repo, and a bunch of other projects.
[00:16:26] SPEAKER_00: And we hopefully, we hope that this becomes a broader effort,
[00:16:30] SPEAKER_00: much like GitHub for storing code.
[00:16:33] SPEAKER_00: We can sort of spearhead the GitHub of model performance
[00:16:38] SPEAKER_00: evaluations.
[00:16:39] SPEAKER_00: So combining the fact that we'll make the AI access
[00:16:45] SPEAKER_00: more model and nogged stick and the fact that we'll
[00:16:49] SPEAKER_00: have more of this objective measurement function
[00:16:52] SPEAKER_00: of what agent is best for each task,
[00:16:55] SPEAKER_00: we hope to basically contribute to the proliferation
[00:17:00] SPEAKER_00: of open solutions.
[00:17:02] SPEAKER_00: These are some of the top of mind things.
[00:17:05] SPEAKER_00: I wanted to give you guys some context
[00:17:06] SPEAKER_00: of how we're thinking about the future
[00:17:09] SPEAKER_00: and I know that there's a bunch of questions.
[00:17:11] SPEAKER_00: But regardless of this repeated questions,
[00:17:13] SPEAKER_00: I feel free to ask anything that comes to mind
[00:17:16] SPEAKER_00: and make this a conversation as possible.
[00:17:20] SPEAKER_00: Thank you.