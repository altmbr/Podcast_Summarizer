# Fully autonomous robots are much closer than you think – Sergey Levine

**Podcast:** One-off Episodes
**Date:** 2025-09-12
**Video ID:** 48pxVdmkMIE
**Video URL:** https://www.youtube.com/watch?v=48pxVdmkMIE

---

[00:00:00] Today, I'm chatting with Sergey Levin,
[00:00:01] SPEAKER_04: who is a co-founder of Physical Intelligence,
[00:00:04] SPEAKER_04: which is a robotics foundation's model company,
[00:00:06] SPEAKER_04: and also a professor at UC Berkeley.
[00:00:08] SPEAKER_04: And just generally, one of the world's leading researchers
[00:00:11] SPEAKER_04: in robotics, RL, and AI.
[00:00:14] SPEAKER_04: Sergey, thank you for coming on the podcast.
[00:00:16] SPEAKER_04: Thank you.
[00:00:17] SPEAKER_04: And thank you for the kind introduction.
[00:00:18] SPEAKER_04: Let's talk about robotics.
[00:00:20] SPEAKER_04: So before I pepper you with questions,
[00:00:22] SPEAKER_04: I'm wondering if you can give the audience a summary
[00:00:24] SPEAKER_04: of where Physical Intelligence says that right now.
[00:00:26] SPEAKER_04: You guys started a year ago.
[00:00:28] SPEAKER_04: Yeah.
[00:00:29] SPEAKER_04: Is the progress look like?
[00:00:29] SPEAKER_04: What are you guys working on?
[00:00:31] Yeah.
[00:00:31] So Physical Intelligence aims to build robotic foundation
[00:00:35] SPEAKER_00: models.
[00:00:35] SPEAKER_00: And that basically means general purpose models
[00:00:38] SPEAKER_00: that could in principle control any robot
[00:00:40] SPEAKER_00: to perform any task.
[00:00:42] SPEAKER_00: We care about this because we see this
[00:00:44] SPEAKER_00: as a very fundamental aspect of the AI problem.
[00:00:48] SPEAKER_00: Like the robot is essentially encompassing all AI
[00:00:51] SPEAKER_00: technologies.
[00:00:52] SPEAKER_00: If you can get a robot that's truly general,
[00:00:53] SPEAKER_00: then you can do hopefully a large chunk of what people can do.
[00:00:58] SPEAKER_00: And where we're at right now is, I think we've kind of
[00:01:00] SPEAKER_00: gotten to the point where we've built out a lot of the basics.
[00:01:06] SPEAKER_00: And I think those basics actually are pretty cool.
[00:01:08] SPEAKER_00: They work pretty well.
[00:01:09] SPEAKER_00: We can get a robot that will fold laundry
[00:01:11] SPEAKER_00: and that will go into a new home and try to clean up the kitchen.
[00:01:14] SPEAKER_00: But in my mind, what we're doing at Physical Intelligence
[00:01:17] SPEAKER_00: right now is really the very, very early beginnings.
[00:01:19] SPEAKER_00: Just like putting in place the basic building blocks on top
[00:01:22] SPEAKER_00: of which we can then tackle all these really tough problems.
[00:01:25] SPEAKER_00: And what's the year by year vision?
[00:01:26] SPEAKER_04: So one year in, no, I got a chance to watch some of the robots.
[00:01:31] SPEAKER_04: And they can do pretty dexterous tasks,
[00:01:33] SPEAKER_04: like folding a box, using grippers.
[00:01:35] SPEAKER_04: And it's like, I don't know.
[00:01:36] SPEAKER_04: It's like pretty hard to fold the box, even with my hands.
[00:01:39] SPEAKER_04: If you had to go year by year until we get to the full robotics
[00:01:42] SPEAKER_04: explosion, what is happening every single year?
[00:01:44] SPEAKER_04: What is a thing that needs to be unlocked, et cetera?
[00:01:47] SPEAKER_04: So there are a few things that we need to get right.
[00:01:50] SPEAKER_00: I mean, Dexterity obviously is one of them.
[00:01:51] SPEAKER_00: And in the beginning, we really
[00:01:53] SPEAKER_00: wanted to make sure that we understand
[00:01:56] SPEAKER_00: whether the methods that we're developing
[00:01:58] SPEAKER_00: have the ability to tackle the kind of intricate tasks
[00:02:01] SPEAKER_00: that people can do.
[00:02:01] SPEAKER_00: As you mentioned, folding a box, folding
[00:02:04] SPEAKER_00: different articles of laundry, cleaning up a table,
[00:02:07] SPEAKER_00: making a coffee, that sort of thing.
[00:02:09] SPEAKER_00: And that's good, that works.
[00:02:11] SPEAKER_00: I think that the results have been able to show
[00:02:12] SPEAKER_00: our pretty cool.
[00:02:13] SPEAKER_00: But again, the end goal of this is not to fold a nice t-shirt.
[00:02:16] SPEAKER_00: The end goal is to just confirm our initial hypothesis
[00:02:19] SPEAKER_00: that the basics are kind of solid.
[00:02:21] SPEAKER_00: But from there, there are a number of really major challenges.
[00:02:24] SPEAKER_00: And I think that sometimes when results get up
[00:02:28] SPEAKER_00: extracted to the level of a three-minute video,
[00:02:30] SPEAKER_00: someone can look at this video and say,
[00:02:31] SPEAKER_00: oh, that's cool, that's what they're doing.
[00:02:34] But it's not.
[00:02:35] SPEAKER_00: It's a very simple and basic version
[00:02:38] SPEAKER_00: of what I think is to come.
[00:02:39] SPEAKER_00: What you really want from a robot is not to tell it,
[00:02:42] SPEAKER_00: hey, please fold my t-shirt.
[00:02:43] SPEAKER_00: What you want from a robot is to tell it, hey, robot,
[00:02:46] SPEAKER_00: you're now doing all sorts of home tasks for me.
[00:02:50] SPEAKER_00: I like to have dinner made at 6 p.m.
[00:02:52] SPEAKER_00: I wake up and go to work at 7 a.m.
[00:02:54] SPEAKER_00: I'd like to do my laundry on Saturday,
[00:02:57] SPEAKER_00: so make sure that that's ready, this and this and this.
[00:03:00] SPEAKER_00: And by the way, check in with me every Monday
[00:03:02] SPEAKER_00: to see what I want you to pick up when you do the shopping.
[00:03:06] SPEAKER_00: That's the prompt.
[00:03:08] SPEAKER_00: And then the robot should go and do this for six months, a year.
[00:03:12] SPEAKER_00: That's the duration of the task.
[00:03:14] SPEAKER_00: So it's ultimately, if this stuff is successful,
[00:03:18] SPEAKER_00: it should be a lot bigger.
[00:03:20] And it should have that ability to learn continuously.
[00:03:23] SPEAKER_00: It should have the understanding of the physical world,
[00:03:26] SPEAKER_00: the common sense, the ability to go in and pull in more
[00:03:28] SPEAKER_00: information if it needs it.
[00:03:29] SPEAKER_00: Like if I ask you, hey, tonight, can you make me this type
[00:03:33] SPEAKER_00: of salad?
[00:03:34] SPEAKER_00: It's like, you should figure out what that entails.
[00:03:36] SPEAKER_00: Look it up, go and buy the ingredients.
[00:03:37] SPEAKER_00: So there's a lot that goes into this.
[00:03:39] SPEAKER_00: It requires common sense.
[00:03:41] SPEAKER_00: It requires understanding that there's
[00:03:43] SPEAKER_00: certain edge case that you need to handle intelligently,
[00:03:44] SPEAKER_00: case where you need to think harder.
[00:03:46] SPEAKER_00: It requires the ability to improve continuously.
[00:03:49] SPEAKER_00: It requires understanding safety, being reliable
[00:03:52] SPEAKER_00: at the right time, being able to fix your mistakes
[00:03:54] SPEAKER_00: when you do make those mistakes.
[00:03:56] SPEAKER_00: So there's a lot more that goes into this.
[00:03:59] SPEAKER_00: But the principles there are, you need to leverage
[00:04:01] SPEAKER_00: per knowledge, and you need to have the right representation.
[00:04:05] SPEAKER_00: So this grand vision, what year, if you had a media
[00:04:08] SPEAKER_04: nest of it?
[00:04:09] SPEAKER_04: Yeah.
[00:04:09] SPEAKER_04: Or 25% tile, 50%, 75%.
[00:04:12] SPEAKER_04: I think it's something where it's not
[00:04:15] SPEAKER_00: going to be a case where we develop everything
[00:04:18] SPEAKER_00: in the laboratory and then it's done.
[00:04:19] SPEAKER_00: And then come 2030, something, you get a robot in a box.
[00:04:23] SPEAKER_00: I think it'll be the same as what we've
[00:04:25] SPEAKER_00: seen with AI assistants that once we reach some basic level
[00:04:29] SPEAKER_00: of competence where the robot is delivering something useful,
[00:04:32] SPEAKER_00: it'll go out there in the world.
[00:04:33] SPEAKER_00: The cool thing is that once it's out there in the world,
[00:04:35] SPEAKER_00: they can collect experience and leverage
[00:04:37] SPEAKER_00: that experience to get better.
[00:04:39] SPEAKER_00: So to me, what I tend to think about a lot in terms of timelines
[00:04:43] SPEAKER_00: is not the date when it will be done,
[00:04:45] SPEAKER_00: but the date when it will, when the flywheel starts, basically.
[00:04:48] SPEAKER_00: OK, so when does the flywheel start?
[00:04:50] SPEAKER_00: I think that could be very soon.
[00:04:52] SPEAKER_00: And I think there's some decisions to be made.
[00:04:54] SPEAKER_00: The trade off there is the more narrow you
[00:04:57] SPEAKER_00: scope the thing, the earlier you can get it
[00:04:59] SPEAKER_00: out into the real world.
[00:05:02] SPEAKER_00: But soon as in, this is something we're already exploring.
[00:05:04] SPEAKER_00: We're already trying to figure out what are the real things
[00:05:06] SPEAKER_00: this thing could do that could allow
[00:05:08] SPEAKER_00: to start spinning the flywheel.
[00:05:09] SPEAKER_00: But I think in terms of stuff that you would actually care about,
[00:05:11] SPEAKER_00: that you would want to see.
[00:05:13] SPEAKER_00: So I don't know, but I think that single digit years
[00:05:15] SPEAKER_00: is very realistic.
[00:05:17] SPEAKER_00: I'm really hoping it'll be more like one or two
[00:05:19] SPEAKER_00: before something is actually out there,
[00:05:20] SPEAKER_00: but it's hard to say.
[00:05:22] And something being out there means what?
[00:05:24] SPEAKER_04: What is out there?
[00:05:25] SPEAKER_04: It means that there is a robot that does a thing
[00:05:27] SPEAKER_00: that you actually care about that you want done.
[00:05:30] SPEAKER_00: And it does so competently enough to actually do it
[00:05:34] SPEAKER_00: for real, for real people that want it done.
[00:05:36] SPEAKER_00: We already have LLMs, which are broadly deployed.
[00:05:39] SPEAKER_04: And that hasn't resulted in some sort of flywheel.
[00:05:42] SPEAKER_04: That's right.
[00:05:43] At least not some obvious flywheel for the model companies
[00:05:46] SPEAKER_04: where the cloud is like learning how to do every single job
[00:05:49] SPEAKER_04: in the economy or GPD is learning how to do every single
[00:05:51] SPEAKER_04: job in the economy.
[00:05:52] SPEAKER_04: So why doesn't that flywheel work for LLMs?
[00:05:55] SPEAKER_04: Well, I think it's actually very close to working.
[00:05:59] SPEAKER_00: And I am like 100% certain that many organizations
[00:06:04] SPEAKER_00: are working on exactly this.
[00:06:06] SPEAKER_00: In fact, arguably there is already a flywheel in the sense
[00:06:08] SPEAKER_00: that not an automated flywheel, but a human
[00:06:12] SPEAKER_00: loop flywheel where everybody who's deploying LLMs,
[00:06:14] SPEAKER_00: of course, going to look at what it's doing.
[00:06:16] SPEAKER_00: And it's going to use that to then modify its behavior.
[00:06:20] It's complex because it comes back to this question
[00:06:24] SPEAKER_00: of representations and figuring out the right way
[00:06:28] SPEAKER_00: to derive supervision signals and ground those supervision
[00:06:31] SPEAKER_00: signals in the behavior of the system
[00:06:33] SPEAKER_00: so that it actually improves on what you want.
[00:06:35] SPEAKER_00: And I don't think that's like a profoundly impossible problem.
[00:06:38] SPEAKER_00: It's just something where the details get pretty gnarly
[00:06:41] SPEAKER_00: and challenges with algorithms and stability
[00:06:43] SPEAKER_00: become pretty complex.
[00:06:44] SPEAKER_00: So it's just something that's taken a while
[00:06:46] SPEAKER_00: for the community collectively to get their hands around.
[00:06:49] SPEAKER_00: Do you think it'll be easier for robotics
[00:06:51] SPEAKER_04: or just that the state of this kind of techniques
[00:06:55] SPEAKER_04: to label data that you collect out in the world
[00:06:59] SPEAKER_04: and use it as a ward will just the whole wave will rise
[00:07:04] SPEAKER_04: and robotics will rise as real.
[00:07:05] SPEAKER_04: So there's some reason the robotics will be
[00:07:07] SPEAKER_04: a little bit more from this.
[00:07:09] SPEAKER_00: Yeah, I don't think there's a profound reason
[00:07:10] SPEAKER_00: why robotics is that different.
[00:07:11] SPEAKER_00: But there are a few small differences
[00:07:13] SPEAKER_00: that I think make things a little bit more manageable.
[00:07:16] SPEAKER_00: So especially if you have a robot that's doing something
[00:07:19] SPEAKER_00: in cooperation with people, whether it's a person
[00:07:21] SPEAKER_00: that's supervising it or directing it,
[00:07:23] SPEAKER_00: like there are very natural sources of supervision
[00:07:25] SPEAKER_00: and there's a big incentive for the person
[00:07:27] SPEAKER_00: to provide the assistance that will make things succeed.
[00:07:30] SPEAKER_00: There are a lot of dynamics where you can make mistakes
[00:07:34] SPEAKER_00: and recover from those mistakes
[00:07:35] SPEAKER_00: and then reflect back on what happened
[00:07:36] SPEAKER_00: and avoid that mistake in the future.
[00:07:38] SPEAKER_00: And I think that when you're doing physical things
[00:07:40] SPEAKER_00: in the real world, that kind of stuff just happens more often
[00:07:43] SPEAKER_00: than it does if you're an AI assistant answering a question.
[00:07:46] SPEAKER_00: Like if you answer a question, you just answered it wrong.
[00:07:48] SPEAKER_00: It's like, well, it's not like you can just go back
[00:07:50] SPEAKER_00: and tweak a few things.
[00:07:52] SPEAKER_00: The person you told, the answer to,
[00:07:53] SPEAKER_00: might not even know that it's wrong.
[00:07:55] SPEAKER_00: Whereas if you're folding the t-shirt
[00:07:56] SPEAKER_00: and you messed up a little bit,
[00:07:57] SPEAKER_00: it's pretty obvious.
[00:07:58] SPEAKER_00: You can reflect on that, figure out what happened
[00:07:59] SPEAKER_00: and do it better next time.
[00:08:01] SPEAKER_04: Yeah, so in one year we have robots
[00:08:03] SPEAKER_04: which are doing some useful things.
[00:08:06] SPEAKER_04: Maybe if you have some relatively simple loopy process
[00:08:11] SPEAKER_04: they can do it for you.
[00:08:12] SPEAKER_04: You just gotta keep folding like thousands of boxes or something.
[00:08:15] SPEAKER_04: But then there's some flywheel, dot, dot, dot.
[00:08:18] SPEAKER_04: There's some machine which will just run my house for me
[00:08:23] SPEAKER_04: as well as a human housekeeper would.
[00:08:26] SPEAKER_04: What is the gap between this thing
[00:08:28] SPEAKER_04: which will be deployed in a year that starts to flywheel
[00:08:30] SPEAKER_04: and this thing which is like a fully autonomous housekeeper?
[00:08:33] SPEAKER_04: Well, I think it's actually not that different
[00:08:35] SPEAKER_00: than what we've seen with LMS in some ways
[00:08:37] SPEAKER_00: that it's a matter of scope.
[00:08:39] SPEAKER_00: If you think about coding assistance, right?
[00:08:41] SPEAKER_00: Like initially the best tools for coding,
[00:08:44] SPEAKER_00: they could do like a little bit of completion.
[00:08:46] SPEAKER_00: You give them a function signature
[00:08:48] SPEAKER_00: and they'll like try their best to type out
[00:08:50] SPEAKER_00: like the whole function
[00:08:51] SPEAKER_00: and they'll maybe like get half of it right.
[00:08:53] SPEAKER_00: And as that stuff progresses,
[00:08:55] SPEAKER_00: then you're willing to give these things
[00:08:56] SPEAKER_00: a lot more agency so that like the very best coding
[00:08:59] SPEAKER_00: assistance now, like if you're doing something
[00:09:01] SPEAKER_00: relatively formulaic, maybe it can like put together
[00:09:03] SPEAKER_00: most of a PR for you for something fairly accessible.
[00:09:08] SPEAKER_00: So I think it'll be the same thing.
[00:09:10] SPEAKER_00: That will see an increase in the scope
[00:09:12] SPEAKER_00: that we're willing to give to the robots
[00:09:14] SPEAKER_00: as they get better and better.
[00:09:15] SPEAKER_00: Where initially the scope might be like
[00:09:17] SPEAKER_00: there is a particular thing you do
[00:09:18] SPEAKER_00: like you're making the coffee or something.
[00:09:21] SPEAKER_00: Whereas as they get more capable
[00:09:23] SPEAKER_00: as their ability to have common sense
[00:09:25] SPEAKER_00: and a broad repertoire of tasks increases,
[00:09:27] SPEAKER_00: then we'll give them greater scope.
[00:09:28] SPEAKER_00: Now you're running the whole coffee shop.
[00:09:30] I get that there's a spectrum
[00:09:31] SPEAKER_04: and I get that there won't be a specific moment
[00:09:33] SPEAKER_04: that feels like we've achieved it.
[00:09:35] SPEAKER_04: But if you're gonna give a year in which like that,
[00:09:37] SPEAKER_04: you're meeting an estimate of when that happens.
[00:09:39] SPEAKER_04: I mean, my sense there too is that this is
[00:09:41] SPEAKER_00: probably a single digit thing rather than
[00:09:43] SPEAKER_00: a double digit thing, but the reason it's so hard
[00:09:45] SPEAKER_00: to really pin down is because as with all research,
[00:09:48] SPEAKER_00: it does depend on figuring out a few question marks.
[00:09:51] SPEAKER_00: And I think my answer in terms of the nature
[00:09:53] SPEAKER_00: of those question marks is I don't think these are things
[00:09:55] SPEAKER_00: that require profoundly deeply different ideas
[00:10:00] SPEAKER_00: but it does require the right synthesis
[00:10:02] SPEAKER_00: of the kinds of things that we already know.
[00:10:05] SPEAKER_00: And sometimes synthesis to be clear is just as difficult
[00:10:09] SPEAKER_00: as coming up with like profoundly new stuff, right?
[00:10:12] SPEAKER_00: So I think it's intellectually a very deep
[00:10:15] SPEAKER_00: and profound problem and figuring that out
[00:10:18] SPEAKER_00: is gonna be like very exciting.
[00:10:20] SPEAKER_00: But I think we kind of like know roughly the puzzle pieces
[00:10:25] SPEAKER_00: and it's something that we need to work on.
[00:10:27] SPEAKER_00: And I think if we work on it and we're a bit lucky
[00:10:30] SPEAKER_00: and everything kind of goes as planned,
[00:10:32] SPEAKER_00: I think single digit is the reason.
[00:10:33] SPEAKER_00: I mean, I'm just gonna do binary search
[00:10:35] SPEAKER_04: until I get a year.
[00:10:37] SPEAKER_04: Okay, so it's less than 10 years, so more than five years?
[00:10:40] SPEAKER_04: You're median estimate.
[00:10:41] SPEAKER_04: I know it's like a different.
[00:10:41] SPEAKER_04: I think five is a good median.
[00:10:43] SPEAKER_00: Okay, five years.
[00:10:45] SPEAKER_04: So if you can fully autonomously run a house,
[00:10:48] SPEAKER_04: then I think you've like, you can fully autonomously
[00:10:51] SPEAKER_04: do most blue collar work.
[00:10:53] SPEAKER_04: So your estimate is in five years
[00:10:55] SPEAKER_04: it should be able to do most like blue collar work
[00:10:57] SPEAKER_04: in the economy.
[00:10:59] SPEAKER_00: So I think there's a nuance here.
[00:11:01] SPEAKER_00: And the nuance is it becomes more obvious
[00:11:04] SPEAKER_00: if we consider the analogy to the coding assistance.
[00:11:07] SPEAKER_00: It's not like the nature of coding assistance today
[00:11:11] SPEAKER_00: is that there's a switch that flips
[00:11:13] SPEAKER_00: and suddenly instead of writing software,
[00:11:16] SPEAKER_00: suddenly all software engineers get fired
[00:11:18] SPEAKER_00: and everyone's using all M's for everything.
[00:11:21] And that actually makes a lot of sense
[00:11:24] SPEAKER_00: that the biggest gain in productivity comes from experts,
[00:11:28] SPEAKER_00: which is software engineers,
[00:11:29] SPEAKER_00: whose productivity is now augmented
[00:11:32] SPEAKER_00: by these really powerful tools.
[00:11:34] SPEAKER_00: I mean, separate from the question of
[00:11:36] SPEAKER_04: whether people will get fired or not,
[00:11:38] SPEAKER_04: a different question is like,
[00:11:39] SPEAKER_04: what will the economic impact be in five years?
[00:11:42] SPEAKER_04: The reason I'm curious about this is with LLMs,
[00:11:45] SPEAKER_04: the relationship between the revenues for these models
[00:11:48] SPEAKER_04: to their inherent, their seeming capability
[00:11:51] SPEAKER_04: has been sort of mysterious in a sense that like,
[00:11:54] SPEAKER_04: you have something which feels like AGI,
[00:11:56] SPEAKER_04: you can have a conversation with it really like,
[00:11:58] SPEAKER_04: it passes the scoring test, it really feels like
[00:12:01] SPEAKER_04: it can do all this knowledge work,
[00:12:03] SPEAKER_04: it's obviously doing a bunch of coding, et cetera.
[00:12:05] SPEAKER_04: But then the revenues for these AGI companies
[00:12:07] SPEAKER_04: are like, cumulatively on the order of like,
[00:12:08] SPEAKER_04: $20, $30 billion per year.
[00:12:11] SPEAKER_04: And that's so much less than all knowledge work,
[00:12:15] SPEAKER_04: which is $30, $40 trillion.
[00:12:18] SPEAKER_04: So in five years, are we in a similar situation
[00:12:20] SPEAKER_04: that LLMs are now, or is it more like,
[00:12:23] SPEAKER_04: we have robots deployed everywhere
[00:12:25] SPEAKER_04: and they're actually like doing a whole bunch
[00:12:26] SPEAKER_04: of real work, et cetera.
[00:12:28] It's a very subtle question.
[00:12:31] I think what it probably will come down to
[00:12:32] SPEAKER_00: is this question of scope, right?
[00:12:34] SPEAKER_00: Like the reason that LLMs are doing all software engineering
[00:12:38] SPEAKER_00: is because they're good within a certain scope,
[00:12:41] SPEAKER_00: but there's limits to that.
[00:12:42] SPEAKER_00: Those limits are increasing to be clear every year.
[00:12:44] SPEAKER_00: And I think that there's no reason
[00:12:46] SPEAKER_00: that we wouldn't see the same kind of thing with robots
[00:12:49] SPEAKER_00: that the scope will have to start out small
[00:12:53] SPEAKER_00: because there will be certain things
[00:12:55] SPEAKER_00: that these systems can do very well
[00:12:56] SPEAKER_00: and certain other things where more human oversight
[00:13:00] SPEAKER_00: is really important.
[00:13:01] SPEAKER_00: And the scope will grow and what that will translate into
[00:13:05] SPEAKER_00: is increased productivity.
[00:13:07] SPEAKER_00: And some of that productivity will come from
[00:13:10] SPEAKER_00: like the robots themselves being valuable
[00:13:12] SPEAKER_00: and some of it will come from the people
[00:13:14] SPEAKER_00: using the robots are now more productive
[00:13:16] SPEAKER_00: than there's any other activity.
[00:13:17] SPEAKER_04: Just like wearing gloves increases productivity
[00:13:20] SPEAKER_04: or like, I don't know, but then it's like,
[00:13:22] SPEAKER_04: you want to understand something
[00:13:23] SPEAKER_04: which increases work to be 100 fold
[00:13:25] SPEAKER_04: versus like wearing glasses or something
[00:13:29] SPEAKER_04: which has a small increase.
[00:13:31] SPEAKER_04: So robots already increase productivity for workers, right?
[00:13:35] SPEAKER_04: Where LLMs are right now in terms of
[00:13:38] SPEAKER_04: the share of knowledge work they can do,
[00:13:39] SPEAKER_04: which is, I guess probably like one 1,000th
[00:13:43] SPEAKER_04: of the knowledge work that happens in the economy,
[00:13:45] SPEAKER_04: LLMs are doing, at least in terms of revenue.
[00:13:49] SPEAKER_04: Are you saying that fraction will be possible
[00:13:51] SPEAKER_04: for robots but for physical work in five years?
[00:13:55] SPEAKER_04: That's a very hard question to answer.
[00:13:58] SPEAKER_00: I think I'm probably not prepared to tell you
[00:14:02] SPEAKER_00: what percentage of all labor work can be done by robots
[00:14:04] SPEAKER_00: because I don't think right now off the cuff,
[00:14:05] SPEAKER_00: I have a sufficient understanding of what's involved
[00:14:09] SPEAKER_00: in that big of a cross section of all physical labor.
[00:14:14] SPEAKER_00: I think what I can tell you is this
[00:14:16] SPEAKER_00: that I think it's much easier to get effective systems
[00:14:20] SPEAKER_00: rolled out gradually in a human in the loop setup.
[00:14:24] SPEAKER_00: And again, I think that's exactly what we've seen
[00:14:26] SPEAKER_00: with coding systems and I think we'll see the same thing
[00:14:29] SPEAKER_00: with automation where basically robot plus human
[00:14:33] SPEAKER_00: is much better than just human or just robot.
[00:14:36] SPEAKER_00: And that just like makes total sense.
[00:14:38] SPEAKER_00: It also makes it much easier to get all the technology
[00:14:41] SPEAKER_00: boot strength because when it's robot plus human,
[00:14:44] SPEAKER_00: now there's a lot more potential for the robot
[00:14:46] SPEAKER_00: to actually learn on the job but acquire new skills.
[00:14:49] SPEAKER_00: Because the human can label what's happening?
[00:14:51] SPEAKER_04: Also because the human can help the human can give hints.
[00:14:54] SPEAKER_00: Let me tell you this story.
[00:14:58] SPEAKER_00: When we were working on the PiO5 project,
[00:15:00] SPEAKER_00: this was the paper that we released last April.
[00:15:04] SPEAKER_00: We initially control our robots with teleoperation
[00:15:07] SPEAKER_00: in a variety of different settings.
[00:15:08] SPEAKER_00: And then at some point we actually realized
[00:15:11] SPEAKER_00: that we can actually make significant headway
[00:15:14] SPEAKER_00: once the model was good enough by supervising it
[00:15:17] SPEAKER_00: not just with low level actions,
[00:15:18] SPEAKER_00: but actually literally instructing it through language.
[00:15:21] SPEAKER_00: Now you need a certain level of competence
[00:15:23] SPEAKER_00: before you can do that.
[00:15:23] SPEAKER_00: But once you have that level of competence,
[00:15:24] SPEAKER_00: just standing there and telling the robot, okay, now,
[00:15:26] SPEAKER_00: now pick up the cup, put the cup in the sink,
[00:15:29] SPEAKER_00: put the addition of the sink just with words.
[00:15:32] SPEAKER_00: Already actually gives the robot information
[00:15:35] SPEAKER_00: that it can use to get better.
[00:15:37] SPEAKER_04: Now imagine what this implies
[00:15:38] SPEAKER_00: for the human plus robot dynamic.
[00:15:40] SPEAKER_00: Like now basically learning is not,
[00:15:44] SPEAKER_00: for these systems is not just learning from real action.
[00:15:46] SPEAKER_00: It's also learning from words,
[00:15:48] SPEAKER_00: eventually be learning from observing what people do,
[00:15:51] SPEAKER_00: from the kind of natural feedback
[00:15:52] SPEAKER_00: that you receive when you're doing a job together
[00:15:54] SPEAKER_00: with somebody else.
[00:15:56] SPEAKER_00: And this kind of, this is also the kind of stuff
[00:15:59] SPEAKER_00: where the prior knowledge that comes from these big models
[00:16:02] SPEAKER_00: is tremendously valuable
[00:16:03] SPEAKER_00: because that lets you understand
[00:16:04] SPEAKER_00: that then interaction dynamic.
[00:16:05] SPEAKER_00: So I think that there's a lot of potential
[00:16:08] SPEAKER_00: for these kind of human plus robot deployments
[00:16:11] SPEAKER_00: to make the model better.
[00:16:13] Interesting.
[00:16:14] SPEAKER_04: So I got to go to the level box and see the robot set up
[00:16:17] SPEAKER_04: and try operating some of the robots myself.
[00:16:19] SPEAKER_02: So the thing is like these triggers
[00:16:21] SPEAKER_02: be very mindful of pressing them
[00:16:23] SPEAKER_02: and don't do some like very fast movements.
[00:16:25] SPEAKER_02: Yeah, keep it like that.
[00:16:26] SPEAKER_02: Kind of slow.
[00:16:27] SPEAKER_02: Very deep, keep moving it.
[00:16:28] SPEAKER_02: Oh, sorry, okay.
[00:16:30] SPEAKER_02: That's what I, and don't move it very fast
[00:16:32] SPEAKER_02: because he can get hurt actually.
[00:16:34] SPEAKER_02: Okay, so operating ended up being a bit harder
[00:16:37] SPEAKER_02: than I anticipated.
[00:16:38] SPEAKER_04: But I did get to see the level box team
[00:16:41] SPEAKER_04: rip through a bunch of tasks.
[00:16:44] I also got to see the output data
[00:16:47] SPEAKER_04: that labs actually have to use to train their robots
[00:16:50] SPEAKER_04: and ask Manu, Libobox CEO,
[00:16:52] SPEAKER_04: about how all this is packaged together.
[00:16:54] SPEAKER_04: So what you're looking at is actually the final output
[00:16:57] SPEAKER_01: that is then delivered to the labs
[00:16:59] SPEAKER_01: which then they used to train the models.
[00:17:01] SPEAKER_01: And so you can see on the left
[00:17:03] SPEAKER_01: the visualization of the movements of the robot
[00:17:06] SPEAKER_01: including its 3D model and so forth.
[00:17:08] SPEAKER_01: And on the right you see all the camera streams
[00:17:10] SPEAKER_01: synchronized with the configuration.
[00:17:13] SPEAKER_01: Libobox can get you millions of episodes of robotics data
[00:17:17] SPEAKER_04: for every single robotics platform
[00:17:18] SPEAKER_04: and sub-task that you want to train on.
[00:17:20] SPEAKER_04: And if you reach out through
[00:17:21] SPEAKER_04: labobox.com, slash the work hash,
[00:17:23] SPEAKER_04: Manu will be very happy with me.
[00:17:24] SPEAKER_04: Yeah.
[00:17:26] In terms of robotics progress,
[00:17:28] SPEAKER_04: why won't it be like self-driving cars
[00:17:30] SPEAKER_04: where we, you know, it's been more than 10 years
[00:17:33] SPEAKER_04: since Google launched it.
[00:17:36] SPEAKER_04: It was in 2009 that they launched
[00:17:37] SPEAKER_04: the self-driving car initiative.
[00:17:39] SPEAKER_04: And then I remember when I was a teenager
[00:17:40] SPEAKER_04: like watching demos where we would go buy
[00:17:43] SPEAKER_04: a Taco Bell and drive back.
[00:17:46] SPEAKER_04: And only now do we have them actually deployed.
[00:17:49] SPEAKER_04: And even then, you know, they make mistakes, et cetera.
[00:17:52] SPEAKER_04: And so maybe there'll be many more years
[00:17:54] SPEAKER_04: before most of the cars are self-driving.
[00:17:58] SPEAKER_04: So why won robotics?
[00:18:00] SPEAKER_04: You know, you're saying five years to this
[00:18:01] SPEAKER_04: like quite robust thing,
[00:18:03] SPEAKER_04: but actually it'll just feel like 20 years
[00:18:05] SPEAKER_04: or just like once we get the cool demo in five years
[00:18:09] SPEAKER_04: then it'll be another 10 years before like,
[00:18:11] SPEAKER_04: we have the Waymo and the Tesla FSD working.
[00:18:14] SPEAKER_04: Yeah, that's a really good question.
[00:18:15] SPEAKER_00: So one of the big things that is different now
[00:18:18] SPEAKER_00: than it was in 2009 actually has to do with
[00:18:23] the technology for machine learning systems
[00:18:25] SPEAKER_00: that understand the world around them.
[00:18:28] SPEAKER_00: Principally, Fortonomous Driving,
[00:18:29] SPEAKER_00: this is a perception for robots
[00:18:31] SPEAKER_00: that can mean a few other things as well.
[00:18:33] SPEAKER_00: And perception certainly was not in a good place in 2009.
[00:18:38] SPEAKER_00: The trouble with perception is that it's one of those things
[00:18:40] SPEAKER_00: where you can nail a really good demo
[00:18:42] SPEAKER_00: with a somewhat engineered system,
[00:18:44] SPEAKER_00: but hit a brick wall when you try to generalize it.
[00:18:47] SPEAKER_00: Now at this point in 2025,
[00:18:49] SPEAKER_00: we have much better technology
[00:18:51] SPEAKER_00: for generalizable and robust perception systems
[00:18:54] SPEAKER_00: and more generally generalizable and robust systems
[00:18:57] for understanding the world around us.
[00:18:59] SPEAKER_00: Like when you say that the system is scalable
[00:19:01] SPEAKER_00: and machine learning scalable
[00:19:02] SPEAKER_00: really means generalizable.
[00:19:04] SPEAKER_00: So that gives us a much better starting point today.
[00:19:07] SPEAKER_00: So that's not an argument about robotics being easier
[00:19:09] SPEAKER_00: than autonomous driving.
[00:19:10] SPEAKER_00: It's just an argument for 2025 being a better year than 2009.
[00:19:14] SPEAKER_00: But there's also other things about robotics
[00:19:17] SPEAKER_00: that are a bit different than driving.
[00:19:18] SPEAKER_00: Like in some ways, robotic manipulation
[00:19:19] SPEAKER_00: is a much, much harder problem.
[00:19:21] SPEAKER_00: But in other ways, it's a problem space
[00:19:24] SPEAKER_00: where it's easier to get rolling
[00:19:27] SPEAKER_00: to start that flywheel with a more limited scope.
[00:19:30] SPEAKER_00: So to give you an example,
[00:19:33] if you're learning how to drive,
[00:19:35] you would probably be pretty crazy to learn how to drive
[00:19:37] SPEAKER_00: on your own without somebody helping you.
[00:19:39] SPEAKER_00: Like you would not trust your teenage child
[00:19:43] SPEAKER_00: to learn to drive just on their own,
[00:19:44] SPEAKER_00: just drop them in the car and say, like, go for it.
[00:19:46] SPEAKER_00: And that's like a 16-year-old
[00:19:49] SPEAKER_00: who's had a significant amount of time
[00:19:51] SPEAKER_00: to learn about the world.
[00:19:52] SPEAKER_00: He would never even dream of putting a five-year-old
[00:19:54] SPEAKER_00: in a car and telling him to get started.
[00:19:56] SPEAKER_00: But if you want somebody to clean the dishes,
[00:19:59] SPEAKER_00: like dishes can break too,
[00:20:00] SPEAKER_00: but you would probably be okay with a child
[00:20:03] SPEAKER_00: trying to do the dishes without somebody constantly,
[00:20:06] SPEAKER_00: like, you know, sitting next to them with a break, so to speak.
[00:20:11] SPEAKER_00: So for a lot of tasks that we want to do
[00:20:14] SPEAKER_00: with robotic manipulation,
[00:20:15] SPEAKER_00: there's potential to make mistakes and correct those mistakes.
[00:20:18] SPEAKER_00: And when you make a mistake and correct it,
[00:20:20] SPEAKER_00: well, first you've achieved the task
[00:20:22] SPEAKER_00: because you've corrected,
[00:20:22] SPEAKER_00: but you've also gained knowledge
[00:20:24] SPEAKER_00: that allows you to avoid that mistake in the future.
[00:20:27] SPEAKER_00: With driving because of the dynamics of how it's set up,
[00:20:29] SPEAKER_00: it's very hard to make a mistake,
[00:20:31] SPEAKER_00: correct it, and then learn from it
[00:20:32] SPEAKER_00: because the mistakes themselves
[00:20:33] SPEAKER_00: have significant ramifications.
[00:20:36] SPEAKER_00: Now, not all manipulation tasks are like that.
[00:20:38] SPEAKER_00: There are truly some very safety critical stuff.
[00:20:42] SPEAKER_00: And this is where the next thing comes in,
[00:20:43] SPEAKER_00: which is common sense.
[00:20:45] SPEAKER_00: Common sense, meaning the ability to make inferences
[00:20:48] SPEAKER_00: about what might happen that are reasonable guesses,
[00:20:52] SPEAKER_00: but that do not require you to experience that mistake
[00:20:55] SPEAKER_00: and learn from it in advance.
[00:20:57] SPEAKER_00: That's tremendously important.
[00:20:58] SPEAKER_00: And that's something that we basically had no idea
[00:21:00] SPEAKER_00: how to do about five years ago.
[00:21:03] SPEAKER_00: But now, we can actually use LMS and VLMS,
[00:21:07] SPEAKER_00: ask them questions,
[00:21:08] SPEAKER_00: and they will make reasonable guesses.
[00:21:10] SPEAKER_00: Like they will not give you expert behavior,
[00:21:11] SPEAKER_00: but you can say,
[00:21:12] SPEAKER_00: hey, there's a sign that's a slippery floor.
[00:21:14] SPEAKER_00: Like, what's gonna happen when I walk over that?
[00:21:16] It's kind of pretty obvious, right?
[00:21:18] SPEAKER_00: And no autonomous car in 2009 would have been able
[00:21:20] SPEAKER_00: to answer that question.
[00:21:21] SPEAKER_00: So common sense,
[00:21:23] SPEAKER_00: plus the ability to make mistakes and correct those mistakes.
[00:21:25] SPEAKER_00: Like that's sounding like an awful lot,
[00:21:28] SPEAKER_00: like what a person does when they're trying to learn something.
[00:21:30] SPEAKER_00: All of that doesn't make robotic manipulation easy necessarily,
[00:21:35] SPEAKER_00: but it allows us to get started with a smaller scope
[00:21:37] SPEAKER_00: and then grow from there.
[00:21:38] SPEAKER_00: So for years, using, I mean, not since 2009,
[00:21:42] SPEAKER_04: but we've had lots of video data, language data,
[00:21:46] SPEAKER_04: and transformers for five, seven, eight years.
[00:21:50] SPEAKER_04: And lots of companies have tried to build
[00:21:53] SPEAKER_04: transformer based robots with lots of training data,
[00:21:58] SPEAKER_04: including Google, Meta, et cetera.
[00:21:59] SPEAKER_04: And what is the reason that they've been hitting roadblocks?
[00:22:03] SPEAKER_04: What has changed now?
[00:22:05] Yeah, that's a really good question.
[00:22:07] So I'll start out with maybe a slight modification to your comment
[00:22:11] SPEAKER_00: is I think they've made a lot of progress.
[00:22:14] SPEAKER_00: And in some ways, a lot of the work that we're doing now
[00:22:16] SPEAKER_00: at physical intelligence is built on the backs of lots of other great work
[00:22:21] SPEAKER_00: that was done, for example, at Google,
[00:22:23] SPEAKER_00: like many of us were actually at Google before.
[00:22:25] SPEAKER_00: Right. We're involved in some of that work,
[00:22:26] SPEAKER_00: some of it is work that we're drawing on that others did.
[00:22:28] SPEAKER_00: So there's definitely been a lot of progress there.
[00:22:31] SPEAKER_00: But to make robotic foundation models really work,
[00:22:35] SPEAKER_00: it's not just a laboratory science kind of experiment.
[00:22:40] SPEAKER_00: It's also requires kind of industrial scale building effort.
[00:22:48] SPEAKER_00: Like it's more like the Apollo program
[00:22:50] SPEAKER_00: than it is like a science experiment.
[00:22:53] SPEAKER_00: And the excellent research that was done
[00:22:57] SPEAKER_00: in the past industrial research labs,
[00:22:59] SPEAKER_00: and I know I was involved in much of that,
[00:23:02] was very much framed as a fundamental research effort.
[00:23:05] SPEAKER_00: And that's good.
[00:23:06] SPEAKER_00: The fundamental research is really important,
[00:23:07] SPEAKER_00: but it's not enough by itself.
[00:23:08] SPEAKER_00: You need the fundamental research,
[00:23:10] SPEAKER_00: and you also need the impetus to make it real.
[00:23:14] SPEAKER_00: And make it real means like actually put the robots out there,
[00:23:17] SPEAKER_00: get data that is represented, the kind of tasks
[00:23:19] SPEAKER_00: that they want they need to do in the real world,
[00:23:21] SPEAKER_00: get that data at scale, build out the systems,
[00:23:23] SPEAKER_00: get all that stuff right.
[00:23:24] SPEAKER_00: And that requires a degree of focus,
[00:23:27] SPEAKER_00: a singular focus on really nailing
[00:23:30] SPEAKER_00: the robotic foundation model for its own sake,
[00:23:33] SPEAKER_00: not just as a way to do more science,
[00:23:36] SPEAKER_00: not just as a way to publish a paper,
[00:23:38] SPEAKER_00: and not just as a way to kind of like,
[00:23:41] SPEAKER_00: have a research lab.
[00:23:43] SPEAKER_00: What is preventing you now from continuing,
[00:23:45] SPEAKER_04: stealing that data even more?
[00:23:49] SPEAKER_04: If data is a big bottleneck,
[00:23:50] SPEAKER_04: why can't you just increase the size of your office
[00:23:54] SPEAKER_04: and 100x have 100x more operators
[00:23:57] SPEAKER_04: where operating these robots until like the more data?
[00:24:01] SPEAKER_04: Yeah, why not ramp it up immediately 100x more?
[00:24:03] SPEAKER_04: Yeah, that's a really good question.
[00:24:05] SPEAKER_00: So the challenge here is in understanding
[00:24:09] SPEAKER_00: which axes of scale contributes to
[00:24:11] SPEAKER_00: which axis of capability?
[00:24:14] So if we wanted to expand capability horizontally,
[00:24:16] SPEAKER_00: meaning like the robot knows how to do 10 things now
[00:24:18] SPEAKER_00: and I'd like it to do 100 things later,
[00:24:21] that can be addressed by just directly horizontally scaling
[00:24:24] SPEAKER_00: what we already have.
[00:24:25] SPEAKER_00: But we want to get robots to a level of capability
[00:24:29] SPEAKER_00: where they can do practical useful things in the real world
[00:24:32] SPEAKER_00: and that requires expanding along other axes too.
[00:24:35] SPEAKER_00: It requires, for example, getting to very high robustness.
[00:24:37] SPEAKER_00: It requires getting them to perform tasks
[00:24:40] SPEAKER_00: very efficiently quickly.
[00:24:41] SPEAKER_00: It requires them to recognize edge cases
[00:24:44] SPEAKER_00: and respond intelligently.
[00:24:46] SPEAKER_00: And those things I think can also be addressed with scaling,
[00:24:49] SPEAKER_00: but we have to identify the right axes for that,
[00:24:51] SPEAKER_00: which means figure out what kind of data to collect,
[00:24:53] SPEAKER_00: what settings to collect it in,
[00:24:54] SPEAKER_00: what kind of methods consume that data,
[00:24:57] SPEAKER_00: how those methods work.
[00:24:59] SPEAKER_00: So answering those questions more thoroughly
[00:25:02] SPEAKER_00: will give us greater clarity on the axes,
[00:25:06] SPEAKER_00: on those dependent variables,
[00:25:08] SPEAKER_00: on the things that we need to scale.
[00:25:09] SPEAKER_00: And we don't fully know right now what that will look like.
[00:25:13] SPEAKER_00: I think we'll figure it out pretty soon
[00:25:15] SPEAKER_00: and something will work out actively.
[00:25:16] SPEAKER_00: But we want to really get that right
[00:25:19] SPEAKER_00: so that when we do scale it up,
[00:25:21] SPEAKER_00: it'll directly translate into capabilities
[00:25:23] SPEAKER_00: that are very relevant to practical use.
[00:25:25] SPEAKER_00: Just to give an order of magnitude,
[00:25:27] SPEAKER_04: how does the amount of data you have collected
[00:25:29] SPEAKER_04: compared to internet scale pre-training data?
[00:25:32] SPEAKER_04: And I know it's hard to do like a token by token count,
[00:25:34] SPEAKER_04: because yeah, how does video information
[00:25:36] SPEAKER_04: compare to internet information, et cetera.
[00:25:38] SPEAKER_04: But like using your regional estimates,
[00:25:41] SPEAKER_04: what fraction of?
[00:25:42] SPEAKER_04: That's right.
[00:25:43] SPEAKER_00: It's very hard to do because robotic experience consists
[00:25:46] SPEAKER_00: of time steps that are very corollary with each other.
[00:25:49] SPEAKER_00: So like the raw, like, bite representation
[00:25:52] SPEAKER_00: is enormous, but probably the information
[00:25:54] SPEAKER_00: density is comparatively low.
[00:25:56] SPEAKER_00: Maybe a better comparison is to the data
[00:25:59] SPEAKER_00: sets that are used for multi-modal training.
[00:26:02] SPEAKER_00: And there, I believe last time we did that count,
[00:26:05] SPEAKER_00: it was like between one and two orders of magnitude.
[00:26:08] The vision you have of robotics
[00:26:11] SPEAKER_04: will not be possible until you collect 100x, 1000x more data.
[00:26:15] SPEAKER_04: Well, that's the thing that we don't know that.
[00:26:18] SPEAKER_00: It's certainly very reasonable to infer
[00:26:20] SPEAKER_00: that robotics is a tough problem,
[00:26:23] SPEAKER_00: and probably it requires as much experience
[00:26:27] SPEAKER_00: as the language stuff.
[00:26:28] SPEAKER_00: But because we don't know the answer to that,
[00:26:31] SPEAKER_00: to me, a much more useful way to think about it
[00:26:33] SPEAKER_00: is not how much data do we need to get before we're fully done,
[00:26:38] SPEAKER_00: but how much data do we need to get before we can get started?
[00:26:40] SPEAKER_00: Meaning before we can get a data flywheel
[00:26:44] SPEAKER_00: that represents a self-sustaining
[00:26:46] SPEAKER_00: and ever-growing data collection.
[00:26:48] SPEAKER_00: What are you talking about?
[00:26:50] SPEAKER_04: Is it just like learning on the job
[00:26:51] SPEAKER_04: or do you have something else in mind?
[00:26:52] SPEAKER_04: Learning on the job or acquiring data
[00:26:55] SPEAKER_00: in a way that the process of acquisition of that data
[00:26:58] SPEAKER_00: itself is useful and valuable.
[00:27:01] I see.
[00:27:02] SPEAKER_00: Just some kind of RL.
[00:27:03] SPEAKER_00: Like doing something like actually real.
[00:27:06] SPEAKER_00: Yeah, I mean, ideally, I would like it to be RL
[00:27:07] SPEAKER_00: because you can get away with the robot acting autonomously,
[00:27:10] SPEAKER_00: which is easier.
[00:27:12] So that's a thought out of the question
[00:27:14] SPEAKER_00: that you can have mixed autonomy.
[00:27:16] SPEAKER_00: You can, as I mentioned before, robots
[00:27:18] SPEAKER_00: can learn from all sorts of other signals.
[00:27:20] SPEAKER_00: I described how we can have a robot
[00:27:22] SPEAKER_00: that learns from a person talking to it.
[00:27:23] SPEAKER_00: So there's a lot of middle ground
[00:27:26] SPEAKER_00: in between fully teleoperated robots
[00:27:28] SPEAKER_00: and fully autonomous robots.
[00:27:29] SPEAKER_00: Yeah.
[00:27:29] SPEAKER_00: OK, and how does the Pi model work?
[00:27:31] SPEAKER_04: Yeah.
[00:27:32] SPEAKER_00: So the current model that we have basically
[00:27:34] SPEAKER_00: is a vision-language model that has been adapted for motor control.
[00:27:39] SPEAKER_00: So to give you a little bit of like a fanciful brain analogy,
[00:27:44] SPEAKER_00: a VLM, a vision-language model, is basically an LLM
[00:27:47] SPEAKER_00: that has had a little like pseudo-visual cortex
[00:27:50] SPEAKER_00: grafted to it, a vision encoder.
[00:27:52] SPEAKER_00: So our models, they have a vision encoder,
[00:27:54] SPEAKER_00: but they also have an action expert, an action decoder essentially.
[00:27:58] SPEAKER_00: So it has a little visual cortex,
[00:27:59] SPEAKER_00: and a notionally a little motor cortex.
[00:28:01] SPEAKER_00: And the way that the model actually makes decisions
[00:28:04] SPEAKER_00: is it reads in the sensory information from the robot.
[00:28:06] SPEAKER_00: It does some internal processing,
[00:28:08] SPEAKER_00: and that could involve actually outputting intermediate steps.
[00:28:11] SPEAKER_00: Like you might tell it, clean up the kitchen,
[00:28:12] SPEAKER_00: and it might think to itself like, hey,
[00:28:14] SPEAKER_00: to clean up the kitchen, to pick up the dish,
[00:28:16] SPEAKER_00: and I need to pick up the sponge, and I need to put the dish in this.
[00:28:18] SPEAKER_00: And then eventually it works its way
[00:28:20] SPEAKER_00: through that chain of thought generation
[00:28:22] SPEAKER_00: down to the action expert,
[00:28:24] SPEAKER_00: which actually produces continuous actions.
[00:28:26] SPEAKER_00: And that has to be a different module,
[00:28:27] SPEAKER_00: because the actions are continuous,
[00:28:30] SPEAKER_00: they're high frequencies, they have a different data format
[00:28:32] SPEAKER_00: than text tokens.
[00:28:34] SPEAKER_00: But structurally, it's still an end-to-end transformer.
[00:28:38] SPEAKER_00: And roughly speaking, technically,
[00:28:40] SPEAKER_00: it corresponds to a kind of mixture of expert architecture.
[00:28:43] SPEAKER_04: And like what is actually happening
[00:28:44] SPEAKER_04: is that it's like predicting, actually, do X thing.
[00:28:48] SPEAKER_04: Then there's an image token, then some action tokens,
[00:28:51] SPEAKER_04: like what it actually ends up doing,
[00:28:52] SPEAKER_04: and then more image, more text description,
[00:28:55] SPEAKER_04: more action tokens.
[00:28:57] SPEAKER_04: Basically, I'm like looking at what stream is going on.
[00:28:59] SPEAKER_04: That's right.
[00:29:01] SPEAKER_00: With the exception that the actions are actually
[00:29:02] SPEAKER_00: not represented as discrete tokens,
[00:29:04] SPEAKER_00: it actually uses a flow matching kind of diffusion
[00:29:06] SPEAKER_00: because they're continuous,
[00:29:07] SPEAKER_00: and you need to be very precise with your actions for extra control.
[00:29:10] SPEAKER_00: I find it super interesting that,
[00:29:11] SPEAKER_04: so I think you're using the open source Gemma model,
[00:29:15] SPEAKER_04: which is like Google's LLM that they're really so open source,
[00:29:19] SPEAKER_04: and then adding this action expert on top.
[00:29:21] SPEAKER_04: And if I had a super interesting that the progress
[00:29:24] SPEAKER_04: in different areas of AI is just based on not only
[00:29:29] SPEAKER_04: the same techniques, but literally the same model
[00:29:33] SPEAKER_04: that you can just use in open source LLM
[00:29:35] SPEAKER_04: and then add this action expert on top,
[00:29:37] SPEAKER_04: it is notable that you naively might think
[00:29:41] SPEAKER_04: there's a separate error of researchers robotics,
[00:29:43] SPEAKER_04: and there's a separate error of research called LLM,
[00:29:45] SPEAKER_04: and natural language processing.
[00:29:47] SPEAKER_04: And no, it's like, it's literally the same.
[00:29:49] SPEAKER_04: It's like the considerations are the same,
[00:29:52] SPEAKER_04: the architectures are the same,
[00:29:53] SPEAKER_04: even the weights are the same.
[00:29:54] SPEAKER_04: I know you do more trading on top of these open source models,
[00:29:57] SPEAKER_04: but that defines you pretty interesting.
[00:29:59] SPEAKER_04: Yeah, so one theme here that I think is important to keep in mind
[00:30:02] SPEAKER_00: is that the reason that those building blocks are so valuable
[00:30:06] SPEAKER_00: is because the AI community has gotten
[00:30:09] SPEAKER_00: a lot better at leveraging prior knowledge.
[00:30:11] SPEAKER_00: And a lot of what we're getting from the pre-trained LLMs
[00:30:15] SPEAKER_00: and VLMs is prior knowledge about the world.
[00:30:19] SPEAKER_00: And it's kind of like, it's a little bit abstracted knowledge.
[00:30:21] SPEAKER_00: It's like, you know, you can identify objects,
[00:30:23] SPEAKER_00: you can figure out, like, you know,
[00:30:24] SPEAKER_00: roughly where things are in image, that sort of thing.
[00:30:26] SPEAKER_00: But I think if I had to like summarize in one sentence,
[00:30:30] SPEAKER_00: the big benefit that recent innovations in AI give to robotics
[00:30:34] SPEAKER_00: is really that prior, the ability to leverage prior knowledge.
[00:30:37] SPEAKER_00: And I think the fact that the model is the same model
[00:30:40] SPEAKER_00: that's like, that's kind of always been the case in deep learning.
[00:30:42] SPEAKER_00: But it's that ability to pull in that prior knowledge,
[00:30:44] SPEAKER_00: that abstract knowledge that has,
[00:30:45] SPEAKER_00: that can come from many different sources.
[00:30:47] SPEAKER_00: That's really powerful.
[00:30:47] SPEAKER_00: Yeah.
[00:30:48] SPEAKER_00: Today I'm here with Mark, who is a senior researcher
[00:30:52] SPEAKER_04: at Hudson River Trading.
[00:30:53] SPEAKER_04: He has prepared for us a big data set of market prices
[00:30:57] SPEAKER_04: and historical market data.
[00:30:58] SPEAKER_04: And we're going to try to figure out what's going on
[00:31:01] SPEAKER_04: and whether we can predict future prices
[00:31:03] SPEAKER_04: from historical market data.
[00:31:04] SPEAKER_04: Mark, let's dig in.
[00:31:05] SPEAKER_04: Happy to do it.
[00:31:06] SPEAKER_04: It sounds like the first fun thing to do
[00:31:08] SPEAKER_04: is probably to start looking at what an order book actually
[00:31:11] SPEAKER_03: looks like.
[00:31:12] SPEAKER_03: Yeah, I think so.
[00:31:13] SPEAKER_03: So I've given you like real order book data
[00:31:16] SPEAKER_03: that is snapshots of the top five levels of the order book,
[00:31:19] SPEAKER_03: both on the bit and ass side, for a couple of different tech
[00:31:23] SPEAKER_03: stocks and video, Tesla, AMD, et cetera.
[00:31:26] SPEAKER_03: What is the shape of the prediction?
[00:31:27] SPEAKER_03: Are we predicting what?
[00:31:29] SPEAKER_03: You take a data frame, look at its wide values
[00:31:31] SPEAKER_03: and just kind of like, it's a granite.
[00:31:33] SPEAKER_03: They are centered at zero.
[00:31:34] SPEAKER_03: They're roughly centered at zero.
[00:31:36] SPEAKER_03: But target of what exactly?
[00:31:37] SPEAKER_03: So these things are changes in the mid price
[00:31:40] SPEAKER_03: from like now to some short period time in the future.
[00:31:42] SPEAKER_03: This is actually quite interesting.
[00:31:43] SPEAKER_03: It's just like a mystery to solve.
[00:31:45] SPEAKER_03: And each one of these can be like a sizable chunk of time
[00:31:47] SPEAKER_03: for a researcher.
[00:31:48] SPEAKER_03: If this sounds interesting to you,
[00:31:50] SPEAKER_04: you should consider working at Hussin River Trading.
[00:31:53] SPEAKER_03: Mark, working with people learn more.
[00:31:54] SPEAKER_03: They can learn more at hutsindustrating.com slash.org-
[00:31:57] SPEAKER_03: Amazing.
[00:31:58] I was talking to this researcher,
[00:32:02] SPEAKER_04: a sander at GDM.
[00:32:04] SPEAKER_04: And he works on video and audio models.
[00:32:07] SPEAKER_04: And he made the interesting point that the reason
[00:32:10] SPEAKER_04: in his view, we aren't seeing that much transfer learning
[00:32:13] SPEAKER_04: between different modalities,
[00:32:15] SPEAKER_04: that is to say like training a language model
[00:32:17] SPEAKER_04: on video and images doesn't seem to necessarily make it
[00:32:19] SPEAKER_04: that much better at textual questions and tasks.
[00:32:25] SPEAKER_04: Is that images are represented at a different semantic level
[00:32:28] SPEAKER_04: than text.
[00:32:29] SPEAKER_04: And so his argument is that text has this high level
[00:32:33] SPEAKER_04: semantic representation within the model.
[00:32:35] SPEAKER_04: Whereas images and videos are just like compressed pixels.
[00:32:38] SPEAKER_04: There's not really a semantic.
[00:32:41] SPEAKER_04: When they're embedded, they don't represent
[00:32:43] SPEAKER_04: some high level semantic information.
[00:32:44] SPEAKER_04: They're just compressed pixels.
[00:32:47] SPEAKER_04: And therefore, there's no transfer learning
[00:32:51] SPEAKER_04: at the level at which they're going through the model.
[00:32:53] SPEAKER_04: And obviously, it's a super relevant to the work
[00:32:55] SPEAKER_04: you're doing because your hope is that by training the model
[00:32:58] SPEAKER_04: both on the visual data that the robot sees,
[00:33:00] SPEAKER_04: visual data generally, maybe even from YouTube
[00:33:02] SPEAKER_04: or whatever eventually, plus language information,
[00:33:06] SPEAKER_04: plus action information from the robot itself.
[00:33:09] SPEAKER_04: That would all of this together will make it
[00:33:11] SPEAKER_04: generally robust.
[00:33:13] SPEAKER_04: And then you had a really interesting blog post
[00:33:15] SPEAKER_04: about why video models aren't as robust as language models.
[00:33:19] SPEAKER_04: Sorry, this is not a super well-formed question.
[00:33:21] SPEAKER_04: I just wanted to do a reaction to the class.
[00:33:22] SPEAKER_04: What's up with that?
[00:33:23] SPEAKER_04: Yeah, yeah.
[00:33:25] Yeah, so I have maybe two things I can say there.
[00:33:28] SPEAKER_00: I have some bad news and some good news.
[00:33:30] SPEAKER_00: So the bad news is what you're saying
[00:33:34] is really getting at the core of a long running challenge
[00:33:39] SPEAKER_00: with video and image generation models.
[00:33:46] In some ways, the idea of getting intelligent systems
[00:33:49] SPEAKER_00: by predicting video is even older
[00:33:51] SPEAKER_00: than the idea of getting intelligent systems
[00:33:54] SPEAKER_00: by predicting text.
[00:33:55] SPEAKER_00: But the text stuff turn into use practically useful things
[00:34:00] earlier than the video stuff.
[00:34:02] SPEAKER_00: And I mean, the video stuff is great.
[00:34:03] SPEAKER_00: Like you can generate cool videos
[00:34:04] SPEAKER_00: and I think that the work there that's been done recently
[00:34:06] SPEAKER_00: is like amazing, but it's not like just generating videos
[00:34:11] SPEAKER_00: and images has already resulted in systems
[00:34:13] SPEAKER_00: that have this kind of like deep understanding of the world
[00:34:16] SPEAKER_00: where you can like ask them to like do stuff
[00:34:17] SPEAKER_00: beyond just generating more images and videos.
[00:34:20] SPEAKER_00: Whereas with language clearly it has.
[00:34:21] SPEAKER_00: And I think that this point about representations
[00:34:23] SPEAKER_00: is really key to it.
[00:34:24] SPEAKER_00: One way we can think about it is this
[00:34:26] SPEAKER_00: that if you imagine pointing a camera outside this building,
[00:34:31] SPEAKER_00: there's the sky, there's the clouds are moving around
[00:34:34] SPEAKER_00: the water, cars driving around people.
[00:34:37] If you want to predict everything that'll happen
[00:34:38] SPEAKER_00: in the future, you can do so in many different ways.
[00:34:41] SPEAKER_00: You can say, okay, there's people around.
[00:34:42] SPEAKER_00: So let me get really good at understanding
[00:34:44] SPEAKER_00: like the psychology of what people behave in crowds
[00:34:46] SPEAKER_00: and predict the pedestrians.
[00:34:47] SPEAKER_00: But you could also say like, well, there's clouds moving around.
[00:34:49] SPEAKER_00: Let me like understand everything about water molecules
[00:34:51] SPEAKER_00: and ice particles in the air.
[00:34:53] SPEAKER_00: And you could go super deep on that.
[00:34:55] SPEAKER_00: If you want to like fully understand
[00:34:56] SPEAKER_00: like all down to the subatomic level,
[00:34:59] SPEAKER_00: everything that's going on, like as a person,
[00:35:01] SPEAKER_00: you could spend like decades just thinking about that.
[00:35:03] SPEAKER_00: And you'll never even get to the pedestrians or the water, right?
[00:35:06] SPEAKER_00: So if you want to really predict everything
[00:35:08] SPEAKER_00: that's going on in that scene,
[00:35:10] SPEAKER_00: there's just so much stuff that even if you're doing
[00:35:13] SPEAKER_00: a really great job and capturing like 100% of something,
[00:35:16] SPEAKER_00: by the time you get to everything else,
[00:35:17] SPEAKER_00: like ages will have passed.
[00:35:19] SPEAKER_00: Whereas with Texas,
[00:35:20] SPEAKER_00: it's already been abstract into those bits
[00:35:21] SPEAKER_00: that we assume is care about.
[00:35:23] SPEAKER_00: So the representations are already there
[00:35:24] SPEAKER_00: and they're not just good representations.
[00:35:26] SPEAKER_00: They actually like focus in on what really matters.
[00:35:28] SPEAKER_00: Okay, so that's the bad news.
[00:35:30] Here's the good news.
[00:35:31] SPEAKER_00: The good news is that we don't have to just get everything
[00:35:36] SPEAKER_00: out of like pointing a camera outside this building
[00:35:38] SPEAKER_00: because when you have a robot,
[00:35:39] SPEAKER_00: that robot is actually trying to do a job.
[00:35:42] So it has a purpose.
[00:35:45] SPEAKER_00: Yeah.
[00:35:46] SPEAKER_00: And its perception is in service to fulfilling that purpose.
[00:35:49] SPEAKER_00: And that is like a really great focusing factor.
[00:35:52] SPEAKER_00: We know that for people, this really matters.
[00:35:54] SPEAKER_00: Like literally what you see is affected by what you're trying to do.
[00:35:57] SPEAKER_00: It like there's been no shortage of psychology experiments
[00:36:00] SPEAKER_00: showing that people have like almost a shocking degree
[00:36:02] SPEAKER_00: of tunnel vision where they will like literally not see things
[00:36:05] SPEAKER_00: right in front of their eyes
[00:36:06] SPEAKER_00: if it's not relevant with their shine of a sheet.
[00:36:08] SPEAKER_00: And that is tremendously powerful.
[00:36:09] SPEAKER_00: Like there must be a reason why people do that
[00:36:11] SPEAKER_00: because you know, certainly if you're out in the jungle,
[00:36:13] SPEAKER_00: seeing more is better than seeing less.
[00:36:15] SPEAKER_00: So if you have that powerful focusing mechanism,
[00:36:17] SPEAKER_00: it must be darn important for getting you to achieve your goal.
[00:36:20] SPEAKER_00: And I think robots will have that focusing mechanism
[00:36:22] SPEAKER_00: because they're trying to achieve a goal.
[00:36:23] SPEAKER_00: By the way, the fact that video models aren't as robust
[00:36:26] SPEAKER_04: is that bearish for robotics
[00:36:29] SPEAKER_04: because it will so much of the data you will have to use
[00:36:33] SPEAKER_04: will not, I guess some of you're saying
[00:36:36] SPEAKER_04: a lot of it will be labeled, but like ideally,
[00:36:38] SPEAKER_04: you just want to be able to like throw all of everything
[00:36:42] SPEAKER_04: on YouTube every video we ever recorded
[00:36:44] SPEAKER_04: and have it learn how the physical world works
[00:36:46] SPEAKER_04: and how to like move about et cetera.
[00:36:48] SPEAKER_04: Just see humans performing tasks and learn from that.
[00:36:51] SPEAKER_04: Yeah, I guess you're saying like it's hard to learn
[00:36:53] SPEAKER_04: just from that and it actually like needs to practice
[00:36:55] SPEAKER_04: a task itself.
[00:36:56] SPEAKER_04: Well, let me put it this way.
[00:36:57] SPEAKER_00: Like let's say that I gave you lots of video tapes
[00:37:02] SPEAKER_00: or lots of recordings of different sporting events
[00:37:05] SPEAKER_00: and gave you a year to just watch sports.
[00:37:07] SPEAKER_00: And then after that year, I told you, okay, now your job,
[00:37:10] SPEAKER_00: you're gonna be playing tennis.
[00:37:11] SPEAKER_00: Yeah.
[00:37:12] SPEAKER_00: Okay, that's like, that's pretty dumb, right?
[00:37:14] SPEAKER_00: Whereas if I told you first, like you're gonna be playing tennis
[00:37:16] SPEAKER_00: and then I let you study up, right?
[00:37:19] SPEAKER_00: Like now you really know what you're looking for.
[00:37:21] SPEAKER_00: So I think that actually, like there's a very real challenge
[00:37:25] SPEAKER_00: here, I don't want to understate the challenge,
[00:37:26] SPEAKER_00: but I do think that there's also a lot of potential
[00:37:29] SPEAKER_00: for foundation models that are embodied
[00:37:32] SPEAKER_00: that learn from interaction, from controlling robotic systems
[00:37:35] SPEAKER_00: to actually be better at absorbing the other data sources
[00:37:38] SPEAKER_00: because they know what they're trying to do.
[00:37:39] SPEAKER_00: I don't think that that bite itself is like a silver bullet.
[00:37:41] SPEAKER_00: I don't think it solves everything,
[00:37:42] SPEAKER_00: but I think that it does help a lot.
[00:37:46] SPEAKER_00: And I think that we've already seen the beginnings of that
[00:37:50] SPEAKER_00: where we can see that including web data in training
[00:37:54] SPEAKER_00: for robots really does help with generalization.
[00:37:57] SPEAKER_00: And I actually have the suspicion that in the long run,
[00:37:59] SPEAKER_00: it'll make it easier to use those sources of data
[00:38:01] SPEAKER_00: that have been tricky to use up until now.
[00:38:04] SPEAKER_04: Famously, I'll let them have all these
[00:38:05] SPEAKER_04: emerging capabilities that were never engineered in
[00:38:07] SPEAKER_04: because somewhere in internet text is the data to train
[00:38:10] SPEAKER_04: and to give it the knowledge to do a certain kind of thing.
[00:38:13] SPEAKER_04: With robots, it seems like you are collecting
[00:38:15] SPEAKER_04: all the data manually.
[00:38:17] SPEAKER_04: So there won't be this mysterious new capability
[00:38:19] SPEAKER_04: that is somewhere in the data set
[00:38:21] SPEAKER_04: that you haven't purposefully collected,
[00:38:23] SPEAKER_04: which seems like it should make it even harder
[00:38:26] SPEAKER_04: to then have robust out of distribution kind of capabilities.
[00:38:32] SPEAKER_04: And so I wonder if the track over the next five, 10 years
[00:38:35] SPEAKER_04: will just be like each subtask you have
[00:38:39] SPEAKER_04: to give it thousands of episodes.
[00:38:41] SPEAKER_04: And then it's very hard to actually automate much work
[00:38:45] SPEAKER_04: just by doing subtask.
[00:38:46] SPEAKER_04: So if you look at think about what a barista does,
[00:38:48] SPEAKER_04: what a waiter does, what a chef does.
[00:38:52] SPEAKER_04: Very little bit involved just like sitting at one station
[00:38:54] SPEAKER_04: and like doing stuff, right?
[00:38:55] SPEAKER_04: They're just like, you gotta move around,
[00:38:56] SPEAKER_04: you gotta restock, you gotta fix the machine,
[00:38:59] SPEAKER_04: or et cetera, go between like the counter
[00:39:02] SPEAKER_04: and the cashier and the machine, et cetera.
[00:39:05] SPEAKER_04: So yeah, will it just be like,
[00:39:07] SPEAKER_04: will it just be this long tail of things
[00:39:09] SPEAKER_04: that you had to keep,
[00:39:09] SPEAKER_04: skills you had to keep like adding episodes for manually
[00:39:12] SPEAKER_04: and labeling and seeing how well they did, et cetera.
[00:39:15] SPEAKER_04: Or is there some reason to think that it will progress
[00:39:22] more generally than that?
[00:39:23] SPEAKER_04: Yeah.
[00:39:24] SPEAKER_00: So there's a subtlety here.
[00:39:26] SPEAKER_00: Emerging capabilities don't just come from the fact
[00:39:29] SPEAKER_00: that internet data has a lot of stuff in it.
[00:39:31] SPEAKER_00: They also come from the fact that generalization,
[00:39:34] SPEAKER_00: once it reaches a certain level, becomes compositional.
[00:39:37] SPEAKER_00: There was a cute example that one of my students
[00:39:42] SPEAKER_00: really liked to use in some of his presentations,
[00:39:44] SPEAKER_00: which is, you know what international phonetic alphabet is?
[00:39:49] SPEAKER_00: If you look in a dictionary,
[00:39:51] SPEAKER_00: they'll have the pronunciation of a word
[00:39:53] SPEAKER_00: and written in like kind of funny letters.
[00:39:55] SPEAKER_00: That's basically international phonetic alphabet.
[00:39:57] SPEAKER_00: So it's an alphabet that is pretty much exclusively used
[00:40:00] SPEAKER_00: for writing down pronunciations
[00:40:01] SPEAKER_00: of individual words and dictionaries.
[00:40:03] SPEAKER_00: And you can ask an LLM to write you a recipe
[00:40:07] SPEAKER_00: for like making some meal in international phonetic alphabet.
[00:40:10] SPEAKER_00: And it will do it.
[00:40:11] SPEAKER_00: And that's like holy crap.
[00:40:13] SPEAKER_00: That is definitely not something that is ever seen
[00:40:16] SPEAKER_00: because IPA is only ever used for heading down
[00:40:18] SPEAKER_00: for now, the issue of individual words.
[00:40:20] SPEAKER_00: So that's compositional generalization.
[00:40:22] SPEAKER_00: It's putting together things you've seen like that in new ways.
[00:40:25] SPEAKER_00: And it's like, you know, arguably there's nothing like
[00:40:27] SPEAKER_00: profoundly new here because like, yes,
[00:40:29] SPEAKER_00: you've seen different words written that way,
[00:40:30] SPEAKER_00: but you've figured out that now you can compose
[00:40:32] SPEAKER_00: the words in this other language,
[00:40:33] SPEAKER_00: the same way that you've composed words in English.
[00:40:36] SPEAKER_00: So that's actually where the emergent capabilities come from.
[00:40:40] SPEAKER_00: And because of this, in principle,
[00:40:44] SPEAKER_00: if we have a sufficient diversity of behaviors,
[00:40:47] SPEAKER_00: the model should figure out that those behaviors
[00:40:49] SPEAKER_00: can be composed in new ways as the situation calls for it.
[00:40:53] SPEAKER_00: And we've actually seen things even with our current models,
[00:40:56] SPEAKER_00: which, you know, I should say that,
[00:40:57] SPEAKER_00: I think they're in the grand scheme of things
[00:40:59] SPEAKER_00: like looking back five years from now,
[00:41:00] SPEAKER_00: we'll probably think that these are tiny in scale.
[00:41:02] SPEAKER_00: But we've already seen what I would call emerging capabilities.
[00:41:05] SPEAKER_00: When we were playing around with some
[00:41:06] SPEAKER_00: of our laundry folding policies,
[00:41:07] SPEAKER_00: they actually would discover this by accent,
[00:41:10] SPEAKER_00: the robot accidentally picked up two T-shirts out of the bin
[00:41:12] SPEAKER_00: instead of one, starts folding the first one,
[00:41:14] SPEAKER_00: the other one gets in the way, picks up the other one,
[00:41:16] SPEAKER_00: throws it back in the bin.
[00:41:17] SPEAKER_00: And we're like, we didn't know, we didn't know we'd do that.
[00:41:20] SPEAKER_00: Well, they crap, and then we try to play around with it,
[00:41:21] SPEAKER_00: and it's like, yep, it does that every time.
[00:41:23] SPEAKER_00: Like you can drop in, you know, it's doing its work,
[00:41:25] SPEAKER_00: drop something else on the table, just pick it up, put it back.
[00:41:28] SPEAKER_00: Right?
[00:41:29] SPEAKER_00: Okay, that's cool.
[00:41:30] SPEAKER_00: Shopping bag, it starts putting things in the shopping bag,
[00:41:32] SPEAKER_00: the shopping bag tips over,
[00:41:33] SPEAKER_00: picks it back up and stands it upright.
[00:41:35] SPEAKER_00: We didn't tell anybody to collect data for that.
[00:41:37] SPEAKER_00: I'm sure somebody accidentally, at some point,
[00:41:39] SPEAKER_00: it may be intentionally picked up the shopping bag,
[00:41:41] SPEAKER_00: but it's just, you have this kind of compositionality
[00:41:44] SPEAKER_00: that emerges when you do learning at scale,
[00:41:46] SPEAKER_00: and that's really where all these remarkable capabilities come from.
[00:41:50] SPEAKER_00: And now you put that together with language,
[00:41:52] SPEAKER_00: you put that together with all sorts of chain of thought reasoning,
[00:41:55] SPEAKER_00: and there's a lot of potential
[00:41:56] SPEAKER_00: for the model to compose things in new ways.
[00:41:58] SPEAKER_00: Right, I didn't use an example like this
[00:41:59] SPEAKER_04: when I got it to the robots, by the way, at your office.
[00:42:03] SPEAKER_04: So it was folding shorts,
[00:42:05] SPEAKER_04: and I don't know if there was an episode like this in the,
[00:42:09] SPEAKER_04: in the training set, but we just were fun.
[00:42:11] SPEAKER_04: I took one of the shorts and turned it inside out,
[00:42:15] SPEAKER_04: and then it was able to understand
[00:42:19] SPEAKER_04: that it first needed to get,
[00:42:21] SPEAKER_04: so first of all, the grippers are just like this,
[00:42:23] SPEAKER_04: like two limbs, or just a possible finger and thumb like thing.
[00:42:28] SPEAKER_04: And it's actually shocking how much you can do with just that.
[00:42:32] SPEAKER_04: Yeah, I'd understood that it first needed to fold that inside out
[00:42:35] SPEAKER_04: before folding it correctly.
[00:42:36] SPEAKER_04: I mean, what's especially surprising about that is,
[00:42:39] SPEAKER_04: it seems like this model only has one second of context.
[00:42:43] SPEAKER_04: So as compared to these language models,
[00:42:45] SPEAKER_04: which can often see the entire code base,
[00:42:46] SPEAKER_04: and they're like observing hundreds of thousands of tokens,
[00:42:49] SPEAKER_04: and thinking about them before outputting,
[00:42:50] SPEAKER_04: and they're observing their own chain of thought
[00:42:52] SPEAKER_04: for thousands of tokens before making a plan
[00:42:55] SPEAKER_04: about how to code something up.
[00:42:57] Your model is seeing one image of what happened in the last second,
[00:43:01] SPEAKER_04: and it vaguely knows it's supposed to fold this short,
[00:43:05] SPEAKER_04: and it's seen like the image of what's happened in the last second.
[00:43:08] And I guess it works.
[00:43:09] SPEAKER_04: It's like crazy that it like, no,
[00:43:10] SPEAKER_04: you will just see the last thing that happened,
[00:43:12] SPEAKER_04: and then keep executing on the plan,
[00:43:14] SPEAKER_04: so fold that inside out, then fold it correctly.
[00:43:18] SPEAKER_04: But it's shocking that a second of context is enough
[00:43:22] SPEAKER_04: to execute on a minute long task.
[00:43:25] SPEAKER_04: Yeah, I'm curious why you made that choice in the first place,
[00:43:28] SPEAKER_04: and why it's possible to actually do tasks.
[00:43:30] SPEAKER_04: Like if a human could only like think,
[00:43:31] SPEAKER_04: I had like a second of memory,
[00:43:33] SPEAKER_04: I had to like do physical work.
[00:43:34] SPEAKER_04: I feel like that would just be possible.
[00:43:35] SPEAKER_04: Yeah.
[00:43:36] SPEAKER_04: I mean, it's not that there's something
[00:43:38] SPEAKER_00: good about having less memory to be clear.
[00:43:39] SPEAKER_00: Like I think that adding memory, adding longer context,
[00:43:43] SPEAKER_00: so that stuff, adding higher resolution images,
[00:43:45] SPEAKER_00: I think those things will make the model better.
[00:43:47] SPEAKER_00: But the reason why it's not the most important thing
[00:43:53] SPEAKER_00: for the kind of skills that you saw when you visited it does,
[00:43:56] SPEAKER_00: it at some level, I think it comes back to Morvix Paradox.
[00:44:00] SPEAKER_00: So Morvix Paradox is basically,
[00:44:02] SPEAKER_00: it's like, you know, if you want to know one thing about robotics,
[00:44:06] SPEAKER_00: it's like that's the thing.
[00:44:07] SPEAKER_00: Morvix Paradox says that basically in AI,
[00:44:10] SPEAKER_00: the easy things are hard, and the hard things are easy,
[00:44:13] SPEAKER_00: meaning like the things that we take for granted,
[00:44:14] SPEAKER_00: like picking up objects,
[00:44:16] SPEAKER_00: seeing, you know, perceiving the world, all that stuff.
[00:44:19] SPEAKER_00: Those are all the heart problems in AI,
[00:44:20] SPEAKER_00: and the things that we find challenging,
[00:44:21] SPEAKER_00: like playing chess and doing calculus,
[00:44:23] SPEAKER_00: actually are often the easier problems.
[00:44:25] SPEAKER_00: And I think this memory stuff
[00:44:27] SPEAKER_00: is actually Morvix Paradox in disguise,
[00:44:28] SPEAKER_00: where we think that the cognitively demanding tasks
[00:44:32] SPEAKER_00: that we do, that we find hard,
[00:44:33] SPEAKER_00: that kind of causes to think like,
[00:44:35] SPEAKER_00: oh man, I'm sweating, I'm working so hard.
[00:44:37] SPEAKER_00: Those are the ones that requires to keep lots of stuff in memory,
[00:44:40] SPEAKER_00: lots of stuff in our minds.
[00:44:41] SPEAKER_00: Like if you're solving some big math problem,
[00:44:43] SPEAKER_00: if you're having a complicated technical conversation
[00:44:46] SPEAKER_00: on a podcast, like those are things
[00:44:48] SPEAKER_00: where you have to keep all those pieces,
[00:44:49] SPEAKER_00: all those puzzle pieces in your head.
[00:44:51] SPEAKER_00: If you're doing a well rehearsed task,
[00:44:54] SPEAKER_00: if you are an Olympic swimmer,
[00:44:57] SPEAKER_00: and you're swimming with perfect form,
[00:44:59] SPEAKER_00: and you're like right there in the zone,
[00:45:01] SPEAKER_00: like people even say like, it's in the moment.
[00:45:03] It's in the moment, right?
[00:45:04] SPEAKER_00: Like it's like, you've practiced it so much,
[00:45:06] SPEAKER_00: you've baked it into your neural network in your brain,
[00:45:10] SPEAKER_00: that you don't have to think carefully
[00:45:12] SPEAKER_00: about keeping all that context, right?
[00:45:14] SPEAKER_00: So it really is just Morvix Paradox manifesting itself,
[00:45:19] SPEAKER_00: but that doesn't mean that we don't need the memory.
[00:45:21] SPEAKER_00: It just means that if we want to match the level of dexterity
[00:45:25] SPEAKER_00: and physical proficiency that people have,
[00:45:27] SPEAKER_00: there's other things we should get right first,
[00:45:29] SPEAKER_00: and then gradually go up that stack
[00:45:31] SPEAKER_00: into the more cognitively demanding areas,
[00:45:33] SPEAKER_00: into reasoning, into context, into planning,
[00:45:35] SPEAKER_00: all that kind of stuff.
[00:45:36] SPEAKER_00: That stuff will be important too.
[00:45:37] SPEAKER_00: And how physically will, so you have this like trilema,
[00:45:42] SPEAKER_04: you have three different things,
[00:45:44] SPEAKER_04: which all take more compute during inference
[00:45:47] SPEAKER_04: that you want to increase at the same time.
[00:45:51] SPEAKER_04: You have the inference speed,
[00:45:53] SPEAKER_04: and so humans are processing 24 frames a second
[00:45:54] SPEAKER_04: or whatever it is.
[00:45:55] SPEAKER_04: They were just like, we can react to things extremely fast,
[00:45:58] SPEAKER_04: then you have the context length.
[00:46:01] SPEAKER_04: And for, I think, the kind of robot,
[00:46:05] SPEAKER_04: which is just like cleaning up your house,
[00:46:06] SPEAKER_04: I think it has to kind, it has to be aware of like,
[00:46:09] SPEAKER_04: things that happened minutes ago or hours ago,
[00:46:11] SPEAKER_04: and how that influences its plan
[00:46:14] SPEAKER_04: about the next task is doing.
[00:46:16] SPEAKER_04: And then you have the model size,
[00:46:18] SPEAKER_04: and I guess at least with that elements,
[00:46:19] SPEAKER_04: we've seen that there's gains from increasing
[00:46:21] SPEAKER_04: the amount of parameters.
[00:46:24] SPEAKER_04: And I think currently you have 100 millisecond inference speeds,
[00:46:30] SPEAKER_04: you have a second long context,
[00:46:32] SPEAKER_04: and then the model is what,
[00:46:33] SPEAKER_04: a couple of billion parameters, how many?
[00:46:34] SPEAKER_04: Okay.
[00:46:35] SPEAKER_04: And so each of these, at least two of them
[00:46:38] SPEAKER_04: are many orders of magnitude,
[00:46:40] SPEAKER_04: smaller than what seems to be the human equivalent, right?
[00:46:42] SPEAKER_04: Like the model, if a human brain has like trillions of parameters,
[00:46:46] SPEAKER_04: and this has like two billion parameters,
[00:46:47] SPEAKER_04: and then if humans are processing,
[00:46:50] SPEAKER_04: at least as fast as the model,
[00:46:51] SPEAKER_04: like actually a decent bit faster,
[00:46:53] SPEAKER_04: and we have hours of context,
[00:46:56] SPEAKER_04: depends on how you define human context,
[00:46:57] SPEAKER_04: but hours of context, minutes of context.
[00:46:59] SPEAKER_04: Sometimes decades of context.
[00:47:00] SPEAKER_04: Yeah, exactly.
[00:47:01] SPEAKER_04: So you have to have many order of magnitude improvements
[00:47:04] SPEAKER_04: across all of these three things,
[00:47:07] SPEAKER_04: which seem to oppose each other,
[00:47:09] SPEAKER_04: or like increasing one reduces the amount of,
[00:47:14] SPEAKER_04: reduces the amount of compute you can dedicate towards the other one
[00:47:16] SPEAKER_04: in inference.
[00:47:17] SPEAKER_04: So how are we gonna, how are we gonna solve this?
[00:47:19] SPEAKER_04: Yeah.
[00:47:20] SPEAKER_04: Well, that's a very big question.
[00:47:23] SPEAKER_00: Yeah, let's try to unpack this a little bit.
[00:47:27] I think there's a lot going on in there.
[00:47:29] SPEAKER_00: One thing that I would say is a really interesting technical problem,
[00:47:33] SPEAKER_00: and I think that it's something where we'll see,
[00:47:36] SPEAKER_00: perhaps a lot of really interesting innovation over the next few years,
[00:47:39] SPEAKER_00: is the question of representation for context.
[00:47:44] SPEAKER_00: So if you imagine the, like some examples you gave,
[00:47:48] SPEAKER_00: like if you have a home world bought that's doing something,
[00:47:49] SPEAKER_00: it needs to keep track.
[00:47:51] As a person, there's certainly some things
[00:47:53] SPEAKER_00: where you keep track of them very symbolically,
[00:47:57] SPEAKER_00: like almost in language, like I have my checklist,
[00:47:59] SPEAKER_00: like I'm going shopping, and at least for me,
[00:48:02] SPEAKER_00: I can literally visualize in my mind my checklist,
[00:48:04] SPEAKER_00: pick up the yogurt, pick up the milk, pick up whatever.
[00:48:07] SPEAKER_00: And I'm not picturing the milk shelf with the milk sitting there,
[00:48:12] SPEAKER_00: I'm just thinking milk, right?
[00:48:14] SPEAKER_00: But then there's other things that are much more spatial,
[00:48:17] SPEAKER_00: almost visual, when I was trying to get to your studio,
[00:48:22] SPEAKER_00: I was thinking like, okay, here's what this street looks like,
[00:48:25] SPEAKER_00: here's what that street looks like,
[00:48:27] SPEAKER_00: here's what I expect the door right to look like.
[00:48:29] SPEAKER_00: So representing your context in the right form
[00:48:33] SPEAKER_00: that captures what you really need to achieve your goal,
[00:48:37] SPEAKER_00: and otherwise kind of discards all down to such stuff.
[00:48:39] SPEAKER_00: I mean, that's a really important thing.
[00:48:41] SPEAKER_00: And I think we're seeing the beginnings of that
[00:48:43] SPEAKER_00: with multimodal models, but I think that multimodality
[00:48:46] SPEAKER_00: has so much more to it than just like ImagePlus text.
[00:48:50] SPEAKER_00: And I think that that's a place where there's a lot
[00:48:52] SPEAKER_00: of room for really exciting innovation.
[00:48:53] SPEAKER_00: Ooh, do you mean in terms of how we represent?
[00:48:57] SPEAKER_04: Mm-hmm, okay.
[00:48:58] SPEAKER_04: Yeah, how we represent both context,
[00:49:00] SPEAKER_00: both what happened in the past, and also plans,
[00:49:02] SPEAKER_00: or reasoning as you can call it in all I'm world,
[00:49:05] SPEAKER_00: which is what we would like to happen in the future,
[00:49:07] SPEAKER_00: or intermediate processing stages, in solving a task.
[00:49:10] SPEAKER_00: I think doing that in a variety of modalities,
[00:49:13] SPEAKER_00: including potentially learn modalities
[00:49:14] SPEAKER_00: that are suitable for the job,
[00:49:16] SPEAKER_00: is something that has I think enormous potential
[00:49:18] SPEAKER_00: to overcome some of these challenges.
[00:49:19] SPEAKER_00: Interesting.
[00:49:20] SPEAKER_00: Another question I have is we're discussing
[00:49:22] SPEAKER_04: these like tough trade-offs in terms of inference
[00:49:28] SPEAKER_04: is comparing it to the human brain,
[00:49:30] SPEAKER_04: and figuring out the human brain is able to have
[00:49:33] SPEAKER_04: hours, decades of context, while being able to act
[00:49:38] SPEAKER_04: on the order of 10 milliseconds,
[00:49:40] SPEAKER_04: while having 100 trillion parameters
[00:49:42] SPEAKER_04: or however you want to count it.
[00:49:44] SPEAKER_04: And I wonder if the best way to understand
[00:49:46] SPEAKER_04: what's happening here is that human brain hardware,
[00:49:50] SPEAKER_04: is just way more advanced than the hardware we have in GPUs,
[00:49:55] SPEAKER_04: or that the algorithms for encoding video information
[00:50:00] SPEAKER_04: are way more efficient, and maybe it's some crazy mixture
[00:50:05] SPEAKER_04: of experts where the act of parameters
[00:50:09] SPEAKER_04: is also on the order of billions, a low billions,
[00:50:12] SPEAKER_04: or some mixture of the two.
[00:50:13] SPEAKER_04: Basically, if you had to think about why do we have
[00:50:16] SPEAKER_04: these models that are across many dimensions
[00:50:19] SPEAKER_04: of the order of magnitude less efficient,
[00:50:23] SPEAKER_04: is it hardware or algorithms than the number to the brain?
[00:50:26] SPEAKER_04: Yeah, that's a really good question.
[00:50:29] So I definitely don't know the answer to this.
[00:50:31] SPEAKER_00: I am not by any means well versed in neuroscience,
[00:50:34] SPEAKER_00: but if I had to guess and also provide an answer
[00:50:37] SPEAKER_00: that leans more on things I know, it's something like this,
[00:50:40] SPEAKER_00: that the brain is extremely parallel.
[00:50:43] SPEAKER_00: It kind of has to be just out of,
[00:50:44] SPEAKER_00: just because of the biophysics,
[00:50:47] SPEAKER_00: but it's even more parallel than your GPU.
[00:50:51] SPEAKER_00: Yeah.
[00:50:51] SPEAKER_00: If you think about how a modern multi-modal language model
[00:50:56] SPEAKER_00: processes the input, if you give it some images
[00:50:59] SPEAKER_00: and some text like first that reads in the images,
[00:51:01] SPEAKER_00: then it reads in the text and then proceeds one token
[00:51:04] SPEAKER_00: at a time to generate the output.
[00:51:07] It makes a lot more sense to me for an embodied system
[00:51:09] SPEAKER_00: to have parallel processes.
[00:51:12] SPEAKER_00: Now mathematically, you can actually make close equivalences
[00:51:15] SPEAKER_00: between parallel and sequential stuff.
[00:51:17] SPEAKER_00: Like transformers aren't actually fundamentally sequential.
[00:51:20] SPEAKER_00: You kind of make them sequential
[00:51:21] SPEAKER_00: about putting in position embeddings.
[00:51:23] Transformers are fundamentally actually
[00:51:24] SPEAKER_00: very parallelizable things.
[00:51:25] SPEAKER_00: That's what makes them so great.
[00:51:27] SPEAKER_00: So I don't think that actually mathematically
[00:51:29] SPEAKER_00: this highly parallel thing,
[00:51:31] SPEAKER_00: where you're doing perception and proprioception
[00:51:33] SPEAKER_00: and planning all at the same time is actually necessarily
[00:51:36] SPEAKER_00: needs to look at that different from a transfer,
[00:51:38] SPEAKER_00: although it's practical implementation will be different.
[00:51:40] SPEAKER_00: And you could imagine that the system will in parallel
[00:51:42] SPEAKER_00: think about, okay, here's like my long-term memory.
[00:51:46] SPEAKER_00: Like here's what I've seen a decade ago.
[00:51:48] SPEAKER_00: Here's my short-term kind of spatial stuff.
[00:51:50] SPEAKER_00: Here's my semantic stuff.
[00:51:52] SPEAKER_00: Here's what I'm seeing now.
[00:51:53] SPEAKER_00: Here's what I'm planning.
[00:51:54] SPEAKER_00: And all of that can be implemented in a way that there's some,
[00:51:57] SPEAKER_00: you know, very familiar kind of attentional mechanism,
[00:51:59] SPEAKER_00: but in practice, all running in parallel,
[00:52:01] SPEAKER_00: maybe at different rates, maybe with a more complex things,
[00:52:04] SPEAKER_00: running slower, the faster reactive stuff running faster.
[00:52:08] I'm sure you've been seeing a bunch of fun images
[00:52:09] SPEAKER_04: that people have been generating with.
[00:52:11] SPEAKER_04: Google's new image generation model, Nana Banana.
[00:52:14] SPEAKER_04: My X-feed is full of wild images.
[00:52:16] SPEAKER_04: But you might not realize that this model can also help you do
[00:52:19] SPEAKER_04: less flashy tasks like restoring historical pictures
[00:52:22] SPEAKER_04: or even just cleaning up images.
[00:52:24] SPEAKER_04: For example, I was reading this old paper back
[00:52:26] SPEAKER_04: because I was prepping to interview Sarah Payne
[00:52:28] SPEAKER_04: and it had this really great graph of roller-tru
[00:52:31] SPEAKER_04: ally-chipping that I wanted to overlay in the lecture.
[00:52:33] SPEAKER_04: Now in the past, this would have taken one of my editors
[00:52:35] SPEAKER_04: 20 or 30 minutes to digitize and clean up manually.
[00:52:39] SPEAKER_04: But now, we just took a photo of the page
[00:52:41] SPEAKER_04: and then dropped into Nana Banana and got back a clean version.
[00:52:45] SPEAKER_04: This was a one shot.
[00:52:46] SPEAKER_04: But if Nana Banana doesn't nail it on the first attempt,
[00:52:49] SPEAKER_04: you can try to just go back and forth with it
[00:52:51] SPEAKER_04: until you get a result that you're super happy with.
[00:52:53] SPEAKER_04: We keep finding new use cases for this model
[00:52:55] SPEAKER_04: and honestly, this is one of those tools
[00:52:57] SPEAKER_04: that just doesn't feel real.
[00:52:58] SPEAKER_04: Check out Gemini 2.5 Flash Image Model,
[00:53:01] SPEAKER_04: aka Nana Banana on both Google AI Studio and the Gemini app.
[00:53:06] SPEAKER_04: All right, back to Sarah Payne.
[00:53:08] SPEAKER_04: If in five years we have a system which is like,
[00:53:11] SPEAKER_04: as robust as a human in terms of interacting with the world,
[00:53:15] SPEAKER_04: then what has happened that makes it physically possible
[00:53:18] SPEAKER_04: to be able to run those kinds of models,
[00:53:21] SPEAKER_04: to have video information that is streaming at real time,
[00:53:24] SPEAKER_04: or hours of prior video information
[00:53:26] SPEAKER_04: is somehow being encoded and considered
[00:53:28] SPEAKER_04: while decoding in like a millisecond scale
[00:53:32] SPEAKER_04: and with many more parameters,
[00:53:35] SPEAKER_04: is it just that like Nvidia has shipped
[00:53:36] SPEAKER_04: much better GPUs or that you guys have come up
[00:53:38] SPEAKER_04: with much better like encoders and stuff
[00:53:41] SPEAKER_04: or like what's happened in the five years?
[00:53:43] SPEAKER_04: I think there are a lot of things to this question.
[00:53:46] SPEAKER_00: I think certainly there's like a really fascinating
[00:53:48] SPEAKER_00: systems problem.
[00:53:50] SPEAKER_00: I'm by no means a systems expert,
[00:53:51] SPEAKER_00: but I would imagine that the right architecture in practice,
[00:53:55] SPEAKER_00: especially if you want an affordable local system
[00:53:57] SPEAKER_00: would be to externalize at least part of the thinking.
[00:54:00] SPEAKER_04: You know, you could imagine maybe in the future,
[00:54:01] SPEAKER_00: you'll have a robot that has like,
[00:54:03] SPEAKER_00: you know, if your interconnection is not very good,
[00:54:05] SPEAKER_00: the robot is in kind of like a dumber reactive mode,
[00:54:08] SPEAKER_00: but if you have a good interconnection,
[00:54:10] SPEAKER_00: then it can like be a little smarter.
[00:54:11] SPEAKER_00: That's pretty cool.
[00:54:13] SPEAKER_00: But I think there are also research and algorithms
[00:54:15] SPEAKER_00: things that can help here.
[00:54:17] SPEAKER_00: Like figuring out the right representations
[00:54:20] SPEAKER_00: can precisely representing both your past observations,
[00:54:24] SPEAKER_00: but also changes in observation, right?
[00:54:25] SPEAKER_00: Like, you know, your sensory stream
[00:54:27] SPEAKER_00: is extremely temporarily correlated,
[00:54:28] SPEAKER_00: which means that the marginal information
[00:54:31] SPEAKER_00: gained from each additional observation
[00:54:32] SPEAKER_00: is not the same as the entirety of that observation
[00:54:35] SPEAKER_00: because the image that I'm seeing now
[00:54:36] SPEAKER_00: is very correlated to the image I saw before.
[00:54:38] SPEAKER_00: So in principle, I want to represent it concisely.
[00:54:40] SPEAKER_00: I get away with a much more compressed representation
[00:54:42] SPEAKER_00: than if I represent the images independently.
[00:54:44] SPEAKER_00: So there's a lot that can be done on the algorithms side
[00:54:46] SPEAKER_00: to get this right,
[00:54:47] SPEAKER_00: and that's really interesting algorithms work.
[00:54:49] SPEAKER_00: I think there's also like a really fascinating systems
[00:54:51] SPEAKER_00: problem.
[00:54:52] SPEAKER_00: To be truthful, like, I haven't gotten to the systems problem
[00:54:55] SPEAKER_00: because, you know, you want to implement the system
[00:54:57] SPEAKER_00: once you sort of know the shape of the machine learning
[00:54:59] SPEAKER_00: solution, but I think there's a lot of cool stuff to do there.
[00:55:03] SPEAKER_04: I mean, if you guys just need to hire, like,
[00:55:04] SPEAKER_04: the people who run the YouTube data centers,
[00:55:05] SPEAKER_04: because like they know how to encode video information.
[00:55:09] SPEAKER_04: OK, this is actually a really interesting question,
[00:55:11] SPEAKER_04: which is that with LLMs, of course,
[00:55:14] SPEAKER_04: they're being theoretically, you go running your own model
[00:55:17] SPEAKER_04: on the slap-top or whatever, but realistically,
[00:55:19] SPEAKER_04: what happens is that the largest,
[00:55:21] SPEAKER_04: most effective models are being run in batches
[00:55:25] SPEAKER_04: of thousands and millions of users at the same time,
[00:55:29] SPEAKER_04: not locally.
[00:55:30] SPEAKER_04: Well, the same thing happened in robotics
[00:55:31] SPEAKER_04: because of the inherent deficiencies of batching,
[00:55:34] SPEAKER_04: plus the fact that we have to do this incredibly
[00:55:37] SPEAKER_04: compute intensive inference task.
[00:55:42] SPEAKER_04: And so you don't want to be carrying around, like,
[00:55:46] SPEAKER_04: like $50,000 GPUs per robot or something.
[00:55:49] SPEAKER_04: You just want that to happen somewhere else.
[00:55:52] SPEAKER_04: So yeah, this robotics world should
[00:55:54] SPEAKER_04: be just be anticipating something where you need connectivity
[00:55:57] SPEAKER_04: everywhere.
[00:55:58] SPEAKER_04: You need robots that have superfast
[00:56:01] SPEAKER_04: and you're streaming video information back and forth,
[00:56:04] SPEAKER_04: or at least video information one way.
[00:56:06] Does that have interesting implications
[00:56:07] SPEAKER_04: about how this deployment of robots will actually
[00:56:12] SPEAKER_04: be instantiated?
[00:56:13] SPEAKER_00: I don't know.
[00:56:14] SPEAKER_00: But if I were to guess, I would guess that it will actually
[00:56:17] SPEAKER_00: see both.
[00:56:18] SPEAKER_00: They will see low-cost systems with off-board inference
[00:56:22] SPEAKER_00: and more reliable systems, for example, in settings
[00:56:27] SPEAKER_00: where if you have an outdoor robot or something
[00:56:29] SPEAKER_00: where you can't rely on connectivity that are costly
[00:56:32] SPEAKER_00: and have on-board inference.
[00:56:34] SPEAKER_00: A few things I'll say from a technical standpoint
[00:56:38] SPEAKER_00: that might contribute to understanding this.
[00:56:41] While a real-time system obviously
[00:56:44] SPEAKER_00: needs to be controlled in real-time, often at high frequency,
[00:56:47] SPEAKER_00: the amount of thinking you actually
[00:56:48] SPEAKER_00: need to do for every time step might be surprisingly low.
[00:56:51] SPEAKER_00: And again, we see this in humans and animals.
[00:56:55] SPEAKER_00: When we plan out movements, there is definitely
[00:57:00] SPEAKER_00: a real planning process that happens in the brain.
[00:57:03] SPEAKER_00: If you record from a monkey brain,
[00:57:06] SPEAKER_00: you will actually find neural correlates of planning.
[00:57:09] SPEAKER_00: And there is something that happens in advance of a movement.
[00:57:12] SPEAKER_00: And when that movement actually takes place,
[00:57:14] SPEAKER_00: the shape of the movement correlates
[00:57:16] SPEAKER_00: with what happened before the movement.
[00:57:18] SPEAKER_00: That's planning.
[00:57:20] SPEAKER_00: So that means that you put something in place
[00:57:22] SPEAKER_00: and set the initial conditions of some kind of process
[00:57:25] SPEAKER_00: and then on-rolled up process and that's the movement.
[00:57:27] SPEAKER_04: And that means that during that movement,
[00:57:28] SPEAKER_00: you're doing less processing
[00:57:30] SPEAKER_00: and you kind of batch it up in advance.
[00:57:32] SPEAKER_00: But you're not entirely an open move.
[00:57:34] SPEAKER_00: It's not like you're playing back a tape recorder.
[00:57:36] SPEAKER_00: You are actually reacting as you go.
[00:57:38] SPEAKER_00: You're just reacting at a different level of abstraction,
[00:57:41] SPEAKER_00: a more basic level of abstraction.
[00:57:43] SPEAKER_00: And again, this comes back to representations.
[00:57:44] SPEAKER_00: Figure out which representations are sufficient
[00:57:47] SPEAKER_00: for planning in advance and then enrolling,
[00:57:49] SPEAKER_00: which representations require a tight feedback loop.
[00:57:51] SPEAKER_00: And for that tight feedback loop,
[00:57:52] SPEAKER_00: what is it, where are you doing feedback on?
[00:57:54] SPEAKER_00: If I'm driving a vehicle, maybe I'm doing feedback
[00:57:56] SPEAKER_00: on the position of the lane marker, so that I stay straight.
[00:57:59] SPEAKER_00: And then at a lower frequency,
[00:58:00] SPEAKER_00: I sort of gauge where I am in traffic.
[00:58:02] SPEAKER_00: And then so you have a couple lectures from a few years back
[00:58:05] SPEAKER_04: where you say, even for robotics,
[00:58:07] SPEAKER_04: RL is, in many cases, better than imitation learning.
[00:58:11] SPEAKER_04: But so far, the models are exclusively
[00:58:13] SPEAKER_04: doing imitation learnings.
[00:58:14] SPEAKER_04: I'm curious how you're thinking on this as changed
[00:58:17] SPEAKER_04: or maybe it's not changed,
[00:58:18] SPEAKER_04: but then you need to do this for the RL.
[00:58:20] SPEAKER_04: Like, why can't you do RL yet?
[00:58:22] SPEAKER_04: Yeah.
[00:58:23] SPEAKER_00: So the key here is prior knowledge.
[00:58:24] SPEAKER_00: Yeah.
[00:58:25] SPEAKER_00: So in order to effectively learn from your own experience,
[00:58:29] SPEAKER_00: it turns out that it's really, really important
[00:58:31] SPEAKER_00: to already know something about what you're doing.
[00:58:33] SPEAKER_00: Otherwise, it takes far too long.
[00:58:35] SPEAKER_00: It's just like it takes a person, when they're a child,
[00:58:39] SPEAKER_00: a very long time to learn very basic things,
[00:58:41] SPEAKER_00: to learn to write for the first time, for example.
[00:58:42] SPEAKER_00: Once you already have some knowledge,
[00:58:44] SPEAKER_00: then you can learn new things very quickly.
[00:58:45] SPEAKER_00: So the purpose of training the models
[00:58:50] SPEAKER_00: with supervised learning now is to build out that foundation
[00:58:53] SPEAKER_00: that provides the prior knowledge
[00:58:54] SPEAKER_00: so they can figure things out much more quickly later.
[00:58:57] SPEAKER_00: And again, this is not a new idea.
[00:58:58] SPEAKER_00: This is exactly what we've seen with LMS, right?
[00:59:01] SPEAKER_00: LMS started off being trained purely
[00:59:04] SPEAKER_00: with next token prediction.
[00:59:05] SPEAKER_00: And that provided an excellent starting point,
[00:59:07] SPEAKER_00: first for all sorts of synthetic data generation,
[00:59:10] SPEAKER_00: and then for RL.
[00:59:12] SPEAKER_00: So I think it makes total sense that we would expect,
[00:59:15] SPEAKER_00: basically any foundation model effort
[00:59:16] SPEAKER_00: to follow the same trajectory,
[00:59:17] SPEAKER_00: or we first build out the foundation,
[00:59:20] SPEAKER_00: essentially in like a somewhat brute force way.
[00:59:22] SPEAKER_00: And the stronger that foundation gets,
[00:59:24] SPEAKER_00: the easier it is to then make it even better
[00:59:27] SPEAKER_00: with much more accessible training.
[00:59:29] SPEAKER_04: In 10 years, will the best model for knowledge work
[00:59:32] SPEAKER_04: also be a robotics model,
[00:59:34] SPEAKER_04: or have like an action expert attached to it?
[00:59:36] SPEAKER_04: And the reason I ask you is like,
[00:59:38] SPEAKER_04: so far we've seen advantages
[00:59:40] SPEAKER_04: from using more general models for things,
[00:59:42] SPEAKER_04: and will robotics fall into this bucket
[00:59:45] SPEAKER_04: of we will just have the model,
[00:59:47] SPEAKER_04: which does everything, including physical work
[00:59:49] SPEAKER_04: and knowledge work, or do you think they'll continue
[00:59:52] SPEAKER_04: to stay separate?
[00:59:53] I really hope that they will actually be the same.
[00:59:55] SPEAKER_00: And obviously I'm extremely biased.
[00:59:58] SPEAKER_00: I love robotics.
[00:59:59] SPEAKER_00: I think it's like it's very fundamental to AI,
[01:00:01] SPEAKER_00: but I think that it's optimistically
[01:00:04] SPEAKER_00: that it's actually the other way around
[01:00:05] SPEAKER_00: that the robotics element of the equation
[01:00:10] SPEAKER_00: will make all the other stuff better.
[01:00:12] And there are two reasons for this
[01:00:15] SPEAKER_00: that I could tell you about.
[01:00:17] SPEAKER_00: One has to do with representations and focus.
[01:00:19] SPEAKER_00: So what I said before, with video prediction models,
[01:00:23] SPEAKER_00: if you just want to predict everything that happens,
[01:00:25] SPEAKER_00: it's very hard to figure out what's relevant.
[01:00:27] SPEAKER_04: If you have the focus that comes from actually trying
[01:00:30] SPEAKER_00: to do a task, now that acts to structure
[01:00:32] SPEAKER_00: how you see the world in a way that allows you
[01:00:35] SPEAKER_00: to more fruitfully utilize the other signals,
[01:00:37] SPEAKER_00: that could be extremely powerful.
[01:00:40] SPEAKER_00: The second one is that understanding
[01:00:42] SPEAKER_00: the physical world at a very deep fundamental level,
[01:00:45] SPEAKER_00: at a level that goes beyond
[01:00:46] SPEAKER_00: just what we can articulate with language
[01:00:47] SPEAKER_00: can actually help you solve other problems.
[01:00:50] SPEAKER_00: And we experience this all the time.
[01:00:52] SPEAKER_00: When we talk about abstract concepts, we say,
[01:00:55] SPEAKER_00: this company has a lot of momentum.
[01:00:57] SPEAKER_00: Yeah.
[01:00:58] SPEAKER_00: Right?
[01:00:59] SPEAKER_00: I like, we'll use social metaphors
[01:01:01] SPEAKER_00: to describe inanimate objects.
[01:01:03] SPEAKER_00: My computer hates me.
[01:01:05] SPEAKER_00: Right?
[01:01:05] SPEAKER_00: We experience the world in a particular way
[01:01:07] SPEAKER_00: in our subjective experience, shapes
[01:01:09] SPEAKER_00: how we think about it in very profound ways.
[01:01:11] SPEAKER_00: And then we use that as a hammer to basically hit all sorts
[01:01:13] SPEAKER_00: of other nails that are far too abstract to handle
[01:01:16] SPEAKER_00: any other way.
[01:01:17] SPEAKER_00: I guess there might be other considerations
[01:01:19] SPEAKER_04: that are relevant to physical robots
[01:01:22] SPEAKER_04: in terms of like, inference speed and model size, et cetera,
[01:01:25] SPEAKER_04: which might be different than the considerations
[01:01:27] SPEAKER_04: for knowledge work.
[01:01:28] SPEAKER_04: But then maybe that doesn't change.
[01:01:31] SPEAKER_04: Maybe it's still the same model,
[01:01:32] SPEAKER_04: but then you can serve it in different ways.
[01:01:34] SPEAKER_04: And the advantages of co-training are high enough
[01:01:37] SPEAKER_04: that whenever I'm wondering in five years
[01:01:41] SPEAKER_04: if I'm using a model to code for me,
[01:01:43] SPEAKER_04: does it also know how to do robotic stuff?
[01:01:45] SPEAKER_04: And maybe the advantages of co-training
[01:01:47] SPEAKER_04: on robotics are high enough that it's worth.
[01:01:49] SPEAKER_04: Well, and I should say that the coding is probably
[01:01:52] SPEAKER_00: like the pinnacle of abstract knowledge work
[01:01:55] SPEAKER_00: in the sense that just by the mathematical nature
[01:01:58] SPEAKER_00: of computer programming is an extremely abstract activity,
[01:02:00] SPEAKER_00: which is why people struggle with it so much.
[01:02:02] SPEAKER_00: Yeah.
[01:02:03] SPEAKER_04: I'm a bit confused about why simulation doesn't work better
[01:02:06] SPEAKER_04: for robots.
[01:02:08] SPEAKER_04: If I look at humans, smart humans do a good job
[01:02:12] SPEAKER_04: of if they're intentionally trying to learn noticing
[01:02:16] what about the simulation is similar to real life
[01:02:19] SPEAKER_04: and being attention to that and learning from that.
[01:02:21] SPEAKER_04: So if you have pilots who are learning in simulation
[01:02:24] SPEAKER_04: or F1 drivers who are learning in simulation,
[01:02:26] SPEAKER_04: should it be expected to be a case that is robots get smarter?
[01:02:29] They will also be able to learn more things
[01:02:32] SPEAKER_04: or simulation or is this curse
[01:02:35] SPEAKER_04: that we need real world data forever?
[01:02:36] SPEAKER_04: This is a very subtle question.
[01:02:38] SPEAKER_00: Your example with the airplane pilot
[01:02:41] SPEAKER_00: using simulation is really interesting.
[01:02:43] SPEAKER_00: But something to remember is that when a pilot
[01:02:47] SPEAKER_00: is using a simulator learned to fly an airplane,
[01:02:49] SPEAKER_00: they're extremely goal-directed.
[01:02:50] SPEAKER_00: So their goal in life is not to learn to use a simulator.
[01:02:53] SPEAKER_00: Their goal in life is to learn to fly the airplane.
[01:02:55] SPEAKER_00: They know there will be a test afterwards
[01:02:56] SPEAKER_00: and they know that eventually they'll be in charge
[01:02:58] SPEAKER_00: of like a few hundred passengers
[01:02:59] SPEAKER_00: and they really need to not crash that thing.
[01:03:02] SPEAKER_00: And when we train models on data from multiple different domains,
[01:03:07] SPEAKER_00: the models don't know that they're supposed
[01:03:10] SPEAKER_00: to solve a particular task.
[01:03:11] SPEAKER_00: They just see like, hey, here's one thing I need to master.
[01:03:13] SPEAKER_00: Here's another thing I need to master.
[01:03:15] SPEAKER_00: So maybe like a better analogy there
[01:03:17] SPEAKER_00: is if you're like playing a video game
[01:03:19] SPEAKER_00: where you can fly an airplane
[01:03:20] SPEAKER_00: and then eventually someone puts you in the cockpit
[01:03:22] SPEAKER_00: of a real one.
[01:03:23] SPEAKER_00: Like it's not that the video game is useless,
[01:03:25] SPEAKER_00: but it's not the same thing.
[01:03:26] SPEAKER_00: And if you're trying to play that video game
[01:03:28] SPEAKER_00: and your goal is to like really like master the video game,
[01:03:31] SPEAKER_00: you're not going to go about it in quite the same way.
[01:03:33] SPEAKER_00: Isn't, can you do some kind of meta-RL on this,
[01:03:39] SPEAKER_04: which is like almost identical actually to the,
[01:03:41] SPEAKER_04: there is this really just a paper you wrote in 2017
[01:03:44] SPEAKER_04: where maybe the loss function is not how well it does
[01:03:47] SPEAKER_04: at a particular video game or particular simulation,
[01:03:49] SPEAKER_04: but how well being trained in different video games
[01:03:51] SPEAKER_04: makes it better at some other downstream task.
[01:03:54] SPEAKER_04: I did a terrible job explaining, but I,
[01:03:56] SPEAKER_04: I didn't mean to.
[01:03:57] SPEAKER_04: Yeah, yeah.
[01:03:58] SPEAKER_04: Okay, maybe can you do a better job explaining what I,
[01:03:59] SPEAKER_04: what I was trying to say?
[01:04:00] SPEAKER_00: So I think what you're trying to say is basically that,
[01:04:02] SPEAKER_00: well, maybe if we have like a really smart model
[01:04:05] SPEAKER_00: that's doing meta-learning,
[01:04:06] SPEAKER_00: perhaps it can figure out that it's performance
[01:04:08] SPEAKER_00: on a downstream problem, a real world problem,
[01:04:10] SPEAKER_00: is increased by doing something in a simulator.
[01:04:13] SPEAKER_00: And then specifically make that the loss function, right?
[01:04:15] SPEAKER_04: That's right.
[01:04:16] SPEAKER_04: But here's the thing with this.
[01:04:18] SPEAKER_00: There's a set of these ideas that are all going to be like,
[01:04:22] SPEAKER_00: something like, train to make it better on the real thing
[01:04:25] SPEAKER_00: by leveraging something else.
[01:04:27] SPEAKER_00: And the key linchpin for all of that is
[01:04:29] SPEAKER_00: the ability to train to be better on the real thing.
[01:04:32] SPEAKER_00: The thing is like, I actually suspect in reality,
[01:04:34] SPEAKER_00: we might not even do something quite so explicit
[01:04:36] SPEAKER_00: because meta-learning is emergent
[01:04:39] SPEAKER_00: as you pointed out before, right?
[01:04:40] SPEAKER_00: Like LLMs essentially do a kind of meta-learning
[01:04:43] SPEAKER_00: in via in-context learning.
[01:04:44] SPEAKER_00: I mean, we can debate us to how much that's learning or not.
[01:04:46] SPEAKER_00: But the point is that large powerful models
[01:04:49] SPEAKER_00: trained on the right objective on real data
[01:04:51] SPEAKER_00: get much better at leveraging all the other stuff.
[01:04:53] SPEAKER_00: And I think that's actually the key.
[01:04:55] SPEAKER_00: And coming back to your airplane pilot,
[01:04:58] SPEAKER_00: like the airplane pilot is trained on a real world objective.
[01:05:01] SPEAKER_00: Like their objectives to be a good airplane pilot,
[01:05:03] SPEAKER_00: to be successful, to have a good career.
[01:05:05] SPEAKER_00: And all of that kind of propagates back into the actions
[01:05:07] SPEAKER_00: they take in leveraging all these other data sources.
[01:05:10] SPEAKER_00: So what I think is actually the key here
[01:05:12] SPEAKER_00: to leveraging auxiliary data sources,
[01:05:13] SPEAKER_00: including simulation, is to build the right foundation model
[01:05:16] SPEAKER_00: that is really good that has those emergent abilities.
[01:05:20] SPEAKER_00: And to your point, to get really good like that,
[01:05:24] SPEAKER_00: it has to have the right objective.
[01:05:26] Now, we know how to get the right objective out of real world data.
[01:05:30] SPEAKER_00: Maybe we can get out of other things, but that's harder right now.
[01:05:32] SPEAKER_00: And I think that, again, we can look to the examples
[01:05:35] SPEAKER_00: of what happened in other fields.
[01:05:36] SPEAKER_00: Like these days, if someone trains an LLM
[01:05:39] SPEAKER_00: for solving complex problems, they're
[01:05:42] SPEAKER_00: using lots of synthetic data.
[01:05:44] SPEAKER_00: But the reason they're able to leverage that synthetic data
[01:05:46] SPEAKER_00: effectively is because they have the starting point
[01:05:48] SPEAKER_00: that is trained on lots of real data that kind of gets it.
[01:05:50] SPEAKER_00: And once it gets it, then it's more
[01:05:52] SPEAKER_00: able to leverage all this other stuff.
[01:05:54] SPEAKER_04: So I think perhaps ironically, the key
[01:05:56] SPEAKER_00: to leveraging other data sources, including simulation,
[01:05:58] SPEAKER_00: is to get really good at using real data,
[01:06:00] SPEAKER_00: understand what's up with the world.
[01:06:01] SPEAKER_00: And then now you can fruitfully use all this stuff.
[01:06:04] SPEAKER_00: So once we have this in 2035, 2030, basically the sci-fi world,
[01:06:12] SPEAKER_04: are you optimistic about the ability
[01:06:14] SPEAKER_04: to like true AGIs to build simulations in which
[01:06:16] SPEAKER_04: they are rehearsing skills that no human or AI has ever
[01:06:21] SPEAKER_04: had a chance to practice before?
[01:06:23] SPEAKER_04: Some, they need to practice to be astronauts
[01:06:26] SPEAKER_04: because we're building the Dyson Sphere.
[01:06:27] SPEAKER_04: And they can just do that in simulation.
[01:06:28] SPEAKER_04: Or will the issue with simulation continue to be one,
[01:06:32] SPEAKER_04: regardless of how smart the models get?
[01:06:34] So here's what I would say that deep down,
[01:06:37] SPEAKER_00: at a very fundamental level, the synthetic experience
[01:06:42] SPEAKER_00: that you create yourself doesn't allow you
[01:06:44] SPEAKER_00: to learn more about the world.
[01:06:46] SPEAKER_00: It allows you to rehearse things.
[01:06:47] SPEAKER_00: It allows you to consider counterfactuals,
[01:06:50] SPEAKER_00: but somehow information about the world
[01:06:53] SPEAKER_00: needs to get injected into the system.
[01:06:55] SPEAKER_00: So, and I think the way you pose this question actually
[01:06:58] SPEAKER_00: elucidates this very nicely because in robotics classically,
[01:07:02] SPEAKER_00: people have often thought about simulation
[01:07:04] SPEAKER_00: as a way to inject human knowledge,
[01:07:06] SPEAKER_00: because a person knows how to write down
[01:07:08] SPEAKER_00: like differential equations, they can code it up,
[01:07:09] SPEAKER_00: and that gives the robot more knowledge than had before.
[01:07:12] SPEAKER_00: But I think that increasingly what we're learning
[01:07:15] SPEAKER_00: from experiences in other fields,
[01:07:19] SPEAKER_00: how the video generation stuff goes from synthetic data
[01:07:21] SPEAKER_00: for all LAMs is that actually,
[01:07:23] SPEAKER_00: probably the most powerful way to create synthetic experience
[01:07:25] SPEAKER_00: is from a really good model,
[01:07:27] SPEAKER_00: because the model probably knows more than a person
[01:07:29] SPEAKER_00: does about those fine grain details.
[01:07:31] SPEAKER_00: But then of course, where does that model get the knowledge
[01:07:33] SPEAKER_00: from experiencing the world?
[01:07:35] SPEAKER_00: So in a sense what you said,
[01:07:37] SPEAKER_00: I think is actually quite right in that a very powerful AI system
[01:07:42] SPEAKER_00: can simulate a lot of stuff,
[01:07:44] SPEAKER_00: but also at that point it kind of almost doesn't matter
[01:07:46] SPEAKER_00: because viewed as a black box,
[01:07:48] SPEAKER_00: what's going on with that system
[01:07:49] SPEAKER_00: is that information comes in and capability comes out.
[01:07:51] SPEAKER_00: And whether the way it process that information
[01:07:53] SPEAKER_00: is by imagining some stuff and simulating
[01:07:55] SPEAKER_00: or by some model-free method,
[01:07:57] SPEAKER_00: it's kind of irrelevant in our standing skills.
[01:07:59] SPEAKER_00: It's just what the equivalent is in humans.
[01:08:02] SPEAKER_04: Whatever we're doing when we're daydreaming or sleeping
[01:08:04] SPEAKER_04: or I don't know if you have some sense of like,
[01:08:08] SPEAKER_04: what this auxiliary thing we're doing is,
[01:08:10] SPEAKER_04: but if you had to make an ML analogy for it, what is it?
[01:08:14] Well, yeah, I mean, certainly when you sleep,
[01:08:18] SPEAKER_00: your brain does stuff that looks an awful lot,
[01:08:21] SPEAKER_00: like what it does when it's awake,
[01:08:22] SPEAKER_00: that looks an awful lot like playing back experience
[01:08:24] SPEAKER_00: or perhaps generating new statistically similar experience.
[01:08:30] So I think it's very reasonable to guess
[01:08:32] SPEAKER_00: that perhaps simulation through a learn model
[01:08:35] SPEAKER_00: is like part of how your brain figures out
[01:08:38] SPEAKER_00: like counterfactuals basically.
[01:08:40] SPEAKER_00: But something that's kind of even more fundamental than that
[01:08:43] SPEAKER_00: is that optimal decision making at its core,
[01:08:47] SPEAKER_00: regardless of how you do it,
[01:08:49] SPEAKER_00: requires considering counterfactuals.
[01:08:51] SPEAKER_00: You basically have to ask yourself,
[01:08:52] SPEAKER_00: if I did this instead of that, would it be better?
[01:08:55] And you have to answer that question somehow.
[01:08:57] SPEAKER_00: And whether you answer that question
[01:08:58] SPEAKER_00: by using a learn simulator
[01:09:00] SPEAKER_00: or whether you answer that question
[01:09:01] SPEAKER_00: by using a value function or something like that
[01:09:04] SPEAKER_00: by using a reward model,
[01:09:06] SPEAKER_00: in the end it's kind of all the same.
[01:09:07] SPEAKER_00: Like as long as you have some mechanism
[01:09:08] SPEAKER_00: for considering counterfactuals
[01:09:09] SPEAKER_00: and figuring out which counterfactuals better, you've got it.
[01:09:12] SPEAKER_00: Yeah.
[01:09:13] SPEAKER_00: That I like thinking about it this way
[01:09:15] SPEAKER_00: because it kind of simplifies things,
[01:09:16] SPEAKER_00: it tells us that the key is not necessarily
[01:09:18] SPEAKER_00: to do really good simulation,
[01:09:19] SPEAKER_00: the key is to figure out how to answer counterfactuals.
[01:09:21] SPEAKER_00: Yeah, interesting.
[01:09:22] SPEAKER_04: So a stepping big picture again,
[01:09:25] SPEAKER_04: the reason I'm interested in getting concrete understanding
[01:09:28] SPEAKER_04: of when this robot economy will be deployed
[01:09:31] SPEAKER_04: is because it's actually pretty relevant
[01:09:33] SPEAKER_04: to understanding how fast AGI will proceed.
[01:09:35] SPEAKER_04: In the sense that, well, it's obviously the data flywheel.
[01:09:39] SPEAKER_04: But also, if you just extrapolate out the CAPEX for AGI,
[01:09:44] SPEAKER_04: suppose by 2030, you know,
[01:09:46] SPEAKER_04: people have different estimates,
[01:09:47] SPEAKER_04: but many people have estimates in the hundreds of gigawatts,
[01:09:50] SPEAKER_04: 100, 200, 300 gigawatts.
[01:09:52] SPEAKER_04: And then you can just like crunch numbers on like,
[01:09:54] SPEAKER_04: if you have 200 gigawatts deployed
[01:09:55] SPEAKER_04: or 100 gigawatts deployed by 2030,
[01:09:57] SPEAKER_04: the marginal CAPEX per year is like trillions of dollars.
[01:10:01] SPEAKER_04: It's like two, three, four trillion dollars a year.
[01:10:03] SPEAKER_04: And that corresponds to actual data centers,
[01:10:06] SPEAKER_04: data build, actual chip foundries you have to build,
[01:10:11] SPEAKER_04: actual solar panel factories you have to build.
[01:10:14] SPEAKER_04: And I'm very curious about whether by this time, by 2030,
[01:10:20] if the big bottleneck we have is just like people
[01:10:23] to like lay out the solar panels
[01:10:25] SPEAKER_04: next to the data center or assemble the data center,
[01:10:29] SPEAKER_04: whether the robot economy will be mature enough
[01:10:32] to help significantly in that process.
[01:10:36] SPEAKER_04: So you're basically saying like,
[01:10:38] SPEAKER_00: how much concrete should I buy now to build the data center
[01:10:40] SPEAKER_00: so that by 2030 I can power all the robots?
[01:10:42] SPEAKER_00: Yeah, yeah.
[01:10:43] SPEAKER_00: That is a more ambitious way of thinking about it
[01:10:46] SPEAKER_00: than has occurred to me, but it's a cool question.
[01:10:48] SPEAKER_00: I mean, the good thing of course is
[01:10:49] SPEAKER_00: that the robots can help you build that stuff.
[01:10:51] SPEAKER_00: Right.
[01:10:52] SPEAKER_04: But will they be able to buy the time that like,
[01:10:54] SPEAKER_04: there's some fly, like there's the non robotic stuff,
[01:10:58] SPEAKER_04: which will also like mandate a lot of CAPEX.
[01:11:02] SPEAKER_04: And then there's a robot stuff,
[01:11:03] SPEAKER_04: well you actually have to build robot factories, et cetera.
[01:11:05] SPEAKER_04: But every just excuse me, there will be this industrial
[01:11:07] SPEAKER_04: explosion across the whole stack
[01:11:10] SPEAKER_04: and how much will robotics be able to speed that up
[01:11:11] SPEAKER_04: or making possible?
[01:11:13] SPEAKER_00: I mean, in principle quite a lot, right?
[01:11:15] SPEAKER_00: I think that we have a tendency sometimes
[01:11:19] SPEAKER_00: to think about robots as like mechanical people,
[01:11:22] SPEAKER_00: but that's not the case, right?
[01:11:24] SPEAKER_00: Like people are people and robots are robots.
[01:11:27] SPEAKER_00: Like the better analogy for the robot,
[01:11:28] SPEAKER_00: it's like your car or a bulldozer.
[01:11:31] SPEAKER_00: Like it has much lower maintenance requirements.
[01:11:34] SPEAKER_00: You can put them into all sorts of weird places
[01:11:36] SPEAKER_00: and they don't have to look like people at all.
[01:11:37] SPEAKER_00: You can make a robot that's 100 feet tall.
[01:11:40] SPEAKER_00: You can make a robot that's tiny.
[01:11:42] SPEAKER_00: So I think that if you have the intelligence to power
[01:11:47] SPEAKER_00: very heterogeneous robotic systems,
[01:11:49] SPEAKER_00: you can probably actually do a lot better
[01:11:51] SPEAKER_00: than just having like, you know, mechanical people
[01:11:53] SPEAKER_00: in effect.
[01:11:55] SPEAKER_00: And it can be a big productivity boost for the real people.
[01:11:58] SPEAKER_00: And it can allow you to solve problems
[01:12:00] SPEAKER_00: that are very difficult to solve now.
[01:12:02] SPEAKER_00: Yeah.
[01:12:02] SPEAKER_00: You can, you know, for example,
[01:12:04] SPEAKER_00: I'm not an expert on data centers by any means,
[01:12:06] SPEAKER_00: but you could build your data centers
[01:12:07] SPEAKER_00: in a very remote location because the robots don't have to worry
[01:12:10] SPEAKER_00: about whether there's like a shopping center nearby.
[01:12:12] SPEAKER_00: And then do you have a sense of how,
[01:12:15] SPEAKER_04: so there's like, where would we'll suffer a B?
[01:12:17] SPEAKER_04: And then there's a question of how many physical robots
[01:12:19] SPEAKER_04: will we have?
[01:12:20] SPEAKER_04: So like how many of the kinds of robots
[01:12:23] SPEAKER_04: you're trading in physical intelligence,
[01:12:24] SPEAKER_04: like these tabletop arms,
[01:12:27] SPEAKER_04: are there physically in the world?
[01:12:28] SPEAKER_04: How many will there be by 2030?
[01:12:31] SPEAKER_04: How many will be needed?
[01:12:32] SPEAKER_04: I mean, these are tough questions,
[01:12:33] SPEAKER_04: like how many will we need if we're that?
[01:12:34] SPEAKER_04: There's very tough questions.
[01:12:35] SPEAKER_04: And also, you know, economies of scale in robotics
[01:12:40] SPEAKER_00: so far have not functioned the same way
[01:12:42] SPEAKER_00: that they probably would in the long term, right?
[01:12:45] SPEAKER_00: Just to give you an example,
[01:12:46] SPEAKER_00: when I started working in robotics in 2014,
[01:12:49] SPEAKER_00: I used a very nice research robot called a PR2
[01:12:53] SPEAKER_00: that cost $400,000 to purchase.
[01:12:57] SPEAKER_00: When I started my research lab at UC Berkeley,
[01:12:59] SPEAKER_00: I bought robot arms that were $30,000,
[01:13:02] SPEAKER_00: the kind of robots that we are using now
[01:13:04] SPEAKER_00: at physical intelligence,
[01:13:05] SPEAKER_00: each arm cost about $3,000,
[01:13:08] SPEAKER_00: and we think they can be made for a small fraction of that.
[01:13:11] SPEAKER_00: So these things.
[01:13:12] SPEAKER_00: What is the cause of that learning, right?
[01:13:14] Well, there are a few things.
[01:13:16] SPEAKER_00: So one, of course, has to do with economies of scale.
[01:13:18] SPEAKER_00: So custom build, high-end research hardware,
[01:13:21] SPEAKER_00: of course, is going to be much more expensive
[01:13:23] SPEAKER_00: than kind of more productionized hardware.
[01:13:26] SPEAKER_00: But the other, and then of course,
[01:13:28] SPEAKER_00: is technological element that as we get better
[01:13:31] SPEAKER_00: at building actuated machines, they become cheaper,
[01:13:36] SPEAKER_00: but there's also a software element,
[01:13:38] SPEAKER_00: which is the smarter URI system gets,
[01:13:41] SPEAKER_00: the less you need the hardware
[01:13:43] SPEAKER_00: to satisfy certain requirements.
[01:13:45] SPEAKER_00: So traditional robots and factories,
[01:13:47] SPEAKER_00: they need to make motions that are highly repeatable,
[01:13:50] SPEAKER_00: and therefore it requires a degree of precision
[01:13:53] SPEAKER_00: and robustness that you don't need
[01:13:54] SPEAKER_00: if you can use cheap visual feedback.
[01:13:57] SPEAKER_00: So AI also makes robots more affordable
[01:14:00] SPEAKER_00: and lowers the requirements on the hardware.
[01:14:03] Interesting.
[01:14:04] SPEAKER_04: Okay, so, learning will continue.
[01:14:07] SPEAKER_04: Do you think it will cost hundreds of dollars
[01:14:08] SPEAKER_04: by the end of the decade to buy mobile arms?
[01:14:11] SPEAKER_04: That is a great question for my co-founder,
[01:14:14] SPEAKER_00: Adnan Esmail, who is probably like the best person
[01:14:17] SPEAKER_00: arguably in the world to ask that question of,
[01:14:19] SPEAKER_00: but certainly the drop in cost that I've seen
[01:14:23] SPEAKER_00: has surprised me year after year.
[01:14:25] SPEAKER_04: And how many arms are there probably in the world?
[01:14:27] SPEAKER_04: Is it more than a million, less than a million?
[01:14:28] SPEAKER_04: So I don't know the answer to that question,
[01:14:30] SPEAKER_00: but it's also a tricky question to answer
[01:14:32] SPEAKER_00: because not all arms are made equal.
[01:14:34] SPEAKER_00: Like arguably the kind of robots
[01:14:36] SPEAKER_00: that are like assembling cars in a factory
[01:14:38] SPEAKER_00: are just not the right kind to think about.
[01:14:40] SPEAKER_00: So the kind you want to train on.
[01:14:43] SPEAKER_00: Very few because they are not currently commercially deployed
[01:14:47] SPEAKER_00: unlike the factory.
[01:14:48] SPEAKER_00: So like a less than a hundred thousand.
[01:14:50] SPEAKER_04: I don't know, but probably.
[01:14:52] SPEAKER_04: And we want billions of robots,
[01:14:58] SPEAKER_04: like at least millions of robots.
[01:15:01] SPEAKER_04: If you're just thinking about like the industrial explosion
[01:15:03] SPEAKER_04: that you need to have this AI explicit growth,
[01:15:08] SPEAKER_04: not only do you need the arms,
[01:15:09] SPEAKER_04: but then you need like something that can move around.
[01:15:13] Beasy, I'm just trying to think about like,
[01:15:15] SPEAKER_04: will that be possible by the time that you need
[01:15:18] SPEAKER_04: a lot more labor to power this AI boom?
[01:15:22] SPEAKER_04: Well, you know, economies are very good at filling demand
[01:15:26] SPEAKER_00: when there's a lot of demand, right?
[01:15:27] SPEAKER_00: Like how many iPhones were in the world in 2001, right?
[01:15:29] SPEAKER_00: That's right.
[01:15:30] SPEAKER_00: So I think it's definitely, there's definitely a challenge there.
[01:15:34] SPEAKER_00: And I think it's something that is worth thinking about.
[01:15:37] SPEAKER_00: And a particularly important question
[01:15:39] SPEAKER_00: for researchers like myself is how can AI affect
[01:15:44] SPEAKER_00: how we think about hardware?
[01:15:46] SPEAKER_00: Because there are some things that I think are going to be
[01:15:48] SPEAKER_00: really, really important.
[01:15:49] SPEAKER_00: Like you probably want your thing to like not break all the time.
[01:15:52] SPEAKER_00: There's some things that are firmly in that category
[01:15:54] SPEAKER_00: of like question marks.
[01:15:55] SPEAKER_00: Like how many fingers do we need?
[01:15:56] SPEAKER_00: Like you said yourself before that you were kind of surprised
[01:15:59] SPEAKER_00: that a robot with two fingers can do a lot.
[01:16:01] SPEAKER_00: Okay, maybe you still want like more than that,
[01:16:03] SPEAKER_00: but still like finding the bare minimum that still lets you
[01:16:05] SPEAKER_00: have good functionality that's important.
[01:16:08] SPEAKER_00: That's in the question mark box.
[01:16:09] SPEAKER_00: And there's some things that I think like we probably don't need,
[01:16:11] SPEAKER_00: like we probably don't need the robot to be like super duper precise
[01:16:14] SPEAKER_00: because we know that feedback can compensate for that.
[01:16:16] SPEAKER_00: So I think my job as I see it right now is to figure out
[01:16:21] SPEAKER_00: what's sort of the minimal package we can get away with.
[01:16:23] SPEAKER_00: And I really like to think about robots in terms of minimal package
[01:16:26] SPEAKER_00: because I don't think that we will have like the one ultimate robot,
[01:16:30] SPEAKER_00: like sort of the mechanical person basically.
[01:16:32] SPEAKER_00: I think what we will have is a bunch of things
[01:16:35] SPEAKER_00: that good effect of robots needs to satisfy.
[01:16:38] SPEAKER_00: Just like good smartphones need to have a touch screen.
[01:16:40] SPEAKER_00: Like that's something that we all kind of agreed on.
[01:16:42] SPEAKER_00: And then a bunch of other stuff that's kind of optional depending on the need,
[01:16:45] SPEAKER_00: depending on the cost point, et cetera.
[01:16:47] SPEAKER_00: And I think there will be a lot of innovation where once we have very capable AI systems
[01:16:51] SPEAKER_00: that can be plugged into any robot to endow it with some basic level of intelligence,
[01:16:55] SPEAKER_00: then lots of different people can innovate on how to get the robot hardware
[01:16:59] SPEAKER_00: to be optimal for each niche.
[01:17:01] SPEAKER_00: And so the manufacturers, is there some in video of robotics?
[01:17:05] Not right now, maybe there will be someday.
[01:17:07] SPEAKER_00: I would really like, maybe I'm being idealistic,
[01:17:12] SPEAKER_00: but I would really like to see a world where there's a lot of heterogeneity in robots.
[01:17:16] SPEAKER_00: What is the biggest part of that in the hardware today
[01:17:18] SPEAKER_04: as somebody who's designed the algorithms that run on it?
[01:17:20] SPEAKER_04: It's a tough question to answer,
[01:17:22] SPEAKER_00: mainly because things are changing so fast.
[01:17:24] SPEAKER_00: I think that to me, the things that I spend a significant amount of time
[01:17:29] SPEAKER_00: thinking about on the hardware side is really more like reliability and cost.
[01:17:33] SPEAKER_00: It's not that I'm not that worried about costs,
[01:17:35] SPEAKER_00: it's just that cost translates to number of robots
[01:17:38] SPEAKER_00: with translates to amount of data.
[01:17:40] SPEAKER_00: And being an ML person, I really like having lots of data.
[01:17:42] SPEAKER_00: So I really like having robots that are low cost
[01:17:44] SPEAKER_00: because then I can have more of them and therefore more data.
[01:17:46] SPEAKER_00: And reliability is important, more or less for the same reason.
[01:17:49] SPEAKER_00: But I think it's something that will get more clarity on as things progress,
[01:17:54] SPEAKER_00: because as we, basically, the AI systems of today
[01:17:58] SPEAKER_00: are not pushing the hardware to the limit.
[01:18:00] SPEAKER_00: So as the AI systems get better and better,
[01:18:02] SPEAKER_00: the harder will get pushed to the limit,
[01:18:03] SPEAKER_00: and then we'll hopefully have a much better answer to your question.
[01:18:06] SPEAKER_00: OK, so this is a question I've had for a lot of guests
[01:18:10] SPEAKER_04: and is that if you go through any layer of the AI explosion,
[01:18:16] SPEAKER_04: you find that a bunch of the actual source supply chain
[01:18:23] SPEAKER_04: is being manufactured in China.
[01:18:25] SPEAKER_04: So other than ships, obviously.
[01:18:27] SPEAKER_04: But then, you know, if you talk about data centers and you're like,
[01:18:31] SPEAKER_04: oh, all the way first for solar panels and a bunch of the cells and modules, etc.
[01:18:35] SPEAKER_04: are manufactured in China, and then you just go through the supply chain.
[01:18:39] SPEAKER_04: And then, obviously, robot arms are being manufactured in China.
[01:18:43] SPEAKER_04: And so if we live in this world where the hardware is just incredibly valuable
[01:18:50] SPEAKER_04: to ramp up manufacturing of because each robot can produce some fraction of the value
[01:18:55] SPEAKER_04: that a human worker can produce.
[01:18:58] SPEAKER_04: And not only is that true, but the value of human workers or any kind of worker
[01:19:03] SPEAKER_04: has just tremendously skyrocketed because we just need tons of bodies
[01:19:07] SPEAKER_04: to lay out the tens of thousands of solar, acres of solar farms and data centers and foundries
[01:19:15] SPEAKER_04: and everything. In this boom world, the big bottom line is just like,
[01:19:19] SPEAKER_04: how many robots can you physically deploy? How many can you manufacture?
[01:19:22] SPEAKER_04: Because you guys are going to come up with the algorithms, now we just need the hardware.
[01:19:25] SPEAKER_04: And so this is a question I've asked many guests,
[01:19:29] SPEAKER_04: which is that if you look at the part of the chain that you are observing,
[01:19:35] SPEAKER_04: what is the reason the China does not win by default? If they're producing all the robots,
[01:19:40] SPEAKER_04: and you come up with the algorithms that make those robots super valuable,
[01:19:44] SPEAKER_04: why don't they just win by default?
[01:19:46] SPEAKER_04: Yeah, so this is a very complex question.
[01:19:51] I'll start with the broader themes and then try to drill a little bit into the details.
[01:19:55] SPEAKER_00: So one broader theme here is that if you want to have an economy where
[01:20:05] you get ahead by having a highly educated workforce, by having people that have high productivity,
[01:20:12] SPEAKER_00: meaning that for each person's hour of work, lots of stuff gets done, automation is really,
[01:20:18] SPEAKER_00: really good because automation is what multiplies the amount of productivity that each person has.
[01:20:24] SPEAKER_00: Again, same as like LM coding tools. LM coding tools amplify the productivity of a software engineer,
[01:20:29] SPEAKER_00: robots will amplify the productivity of basically everybody that is doing work.
[01:20:35] SPEAKER_00: Now, that's kind of like a final state, like a desirable final state. Now there's a lot of complexity
[01:20:42] SPEAKER_00: in how you get to that state, how you make that an appealing journey to society,
[01:20:49] SPEAKER_00: how you navigate the geopolitical dimension, that all of that stuff is actually pretty complicated,
[01:20:53] SPEAKER_00: and it requires making a number of really good decisions, like good decisions about investing in
[01:21:01] SPEAKER_00: a balanced robotics ecosystem, supporting both software innovation and hardware innovation.
[01:21:08] SPEAKER_00: I don't think any of those are insurmountable problems. It just requires a degree of
[01:21:16] long-term vision and the right kind of balance of investment. But what makes me really optimistic
[01:21:22] SPEAKER_00: about this is that final state, that if we can all agree that in the United States we would like
[01:21:27] SPEAKER_00: to have the kind of society where people are highly productive, where we have highly educated people
[01:21:34] SPEAKER_00: doing high-value work, and because that end state seems to me very compatible with automation,
[01:21:40] SPEAKER_00: with robotics, there's a lot of, at some level there should be a lot of incentive to get to that state.
[01:21:46] SPEAKER_00: From there, we have to solve for all the details that will help us get there, and that's not easy,
[01:21:51] SPEAKER_00: I think there's a lot of complicated decisions that need to be made in terms of private industry,
[01:21:55] SPEAKER_00: in terms of investment, in terms of the political dimension. But I'm very optimistic about it,
[01:22:00] SPEAKER_00: because it seems to me the light at the end of the tunnel is in the right direction.
[01:22:06] SPEAKER_04: I mean, I guess there's a different question, which is that if the value is bottlenecked by hardware,
[01:22:13] SPEAKER_04: and so you just need to produce more hardware, what is the path by which hundreds of millions of robots,
[01:22:18] SPEAKER_04: or billions of robots, are being manufactured in the US or with allies? I don't know how to
[01:22:23] SPEAKER_04: approach that question, but it seems like a different question than like, okay, well, what is the
[01:22:26] SPEAKER_04: impact on human wages or something? So again, for the specifics of how we make that happen,
[01:22:33] SPEAKER_00: I think that's a very long conversation that I'm probably not the most qualified to, but I think
[01:22:38] SPEAKER_00: that in terms of the ingredients, the ingredient here that I think is important is that robots help with
[01:22:45] physical things, physical work. And if producing robots is itself physical work, then getting
[01:22:53] SPEAKER_00: really good at robotics should help with that. It's a little circular, of course, and as with all
[01:22:59] SPEAKER_00: circular things, you have to like kind of bootstrap it and try to get that engine going. But
[01:23:05] it seems like it is an easier problem to address than, for example, the problem of digital devices,
[01:23:12] SPEAKER_00: where work goes into creating computers, phones, etc. But the computers and phones don't themselves
[01:23:17] SPEAKER_00: help with the work. I guess feedback loops go both ways. They can help you or they can help others.
[01:23:23] SPEAKER_04: And it's a positive sum world, so it's not necessarily bad that they help others. But
[01:23:28] SPEAKER_04: to the extent that a lot of the things that go into this feedback loop, the subcomponent
[01:23:33] SPEAKER_04: manufacturing and supply chain already exists in China, it seems like the stronger feedback loop
[01:23:39] SPEAKER_04: would exist in China. And then there's a separate discussion, maybe that's fine.
[01:23:43] SPEAKER_04: Maybe that's good, and maybe they'll continue exporting this to us. But it's just like notable that,
[01:23:49] SPEAKER_04: I just find it notable that whenever I talk to a guest about different things, it's just like,
[01:23:53] SPEAKER_04: oh yeah, within a few years, the key bottleneck to every single part of the supply chain here
[01:23:58] SPEAKER_04: will be something that China is the 80% world supplier of something.
[01:24:03] Well, yeah, and this is why I said before that I think something really important to get right here
[01:24:07] SPEAKER_00: is a balanced robotics ecosystem. I think AI is tremendously exciting, but I think we should
[01:24:13] SPEAKER_00: also recognize that getting AI right is not the only thing that we need to do. And we need to think
[01:24:19] SPEAKER_00: about how to balance our priorities, our investment, the kind of things that we spend our time on.
[01:24:27] SPEAKER_00: Just as an example, at physical intelligence, we do take hardware very seriously, actually.
[01:24:31] SPEAKER_00: We build a lot of our own things, and we want to have a hardware roadmap alongside our AI roadmap.
[01:24:41] But I think that that's just us, I think that for the United States, for arguably for human
[01:24:48] SPEAKER_00: civilization as a whole, I think we need to think about these problems very holistically.
[01:24:52] SPEAKER_00: And I think it is easy to get distracted sometimes when there's a lot of excitement, a lot of
[01:24:56] SPEAKER_00: progress in one area, like AI, and we are tempted to lose track of other things,
[01:25:03] SPEAKER_00: including things you've said, like, hey, there's a hardware component, there's an infrastructure
[01:25:07] SPEAKER_00: component with compute and things like that. So I think that in general, it's good to have a more
[01:25:11] SPEAKER_00: holistic view of these things, and I wish we had more holistic conversations about that sometimes.
[01:25:16] SPEAKER_00: I do think from the perspective of society as a whole, how should they be thinking about the
[01:25:21] SPEAKER_04: advances in robotics and knowledge work? And I think it's basically like, society should be playing
[01:25:25] SPEAKER_04: for full automation. There will be a period in which people's work is way more valuable,
[01:25:30] SPEAKER_04: because there's this huge boom in the economy where building all these data centers,
[01:25:34] SPEAKER_04: building all these factories. But then eventually, humans can do things with their body,
[01:25:38] SPEAKER_04: and we can do things with their mind. There's not like some secret third thing. So
[01:25:42] SPEAKER_04: what's your society be planning for? It should be full automation of humans, and there will also be
[01:25:48] SPEAKER_04: a society be much wealthier. So presumably there's ways to do this in a way that everybody is
[01:25:53] SPEAKER_04: much better off than they are today. But then like the end state, the light of the end of the
[01:25:57] SPEAKER_04: tunnel is the full automation, plus super wealthy society with some redistribution or whatever
[01:26:03] SPEAKER_04: way to figure that out. I don't know if you disagree with that characterization.
[01:26:07] So I think at some level, that's a very reasonable way to look at things. But I think that if there's
[01:26:15] SPEAKER_00: one thing that I've learned about technology, it's that it rarely evolves quite the way that people
[01:26:20] SPEAKER_00: expect. And sometimes the journey is just as important as the destination. So I think it's
[01:26:25] SPEAKER_00: actually very difficult to plan ahead for an end state. But I think directionally what you said
[01:26:30] SPEAKER_00: makes a lot of sense. And I do think that it's very important for us collectively to think about
[01:26:36] SPEAKER_00: how to structure the world around us in a way that is amenable to greater and great automation
[01:26:40] SPEAKER_00: across all sectors. But I think we should really think about the journey just as much as the
[01:26:46] SPEAKER_00: destination, because things evolve in all sorts of unpredictable ways. And we'll find
[01:26:52] automation showing up in all sorts of places, probably not the places we expect first.
[01:26:56] SPEAKER_00: So I think that the constants here that I think are really important is education is really,
[01:27:01] SPEAKER_00: really valuable. Education is the best buffer somebody has against the negative effects of change.
[01:27:10] SPEAKER_00: So if there is like one single lever that we can pull collectively as a society, it's like
[01:27:16] SPEAKER_00: more education because that's what that's for.
[01:27:18] SPEAKER_00: And more of X paradoxes, like the things which are like most beneficial for education for humans
[01:27:23] SPEAKER_04: might have been the easiest to automate because it's really easy to educate AI is you can
[01:27:27] SPEAKER_04: throw the textbooks that would take you eight years of grad school to do at them in an afternoon.
[01:27:31] SPEAKER_04: Well, what education gives you flexibility? So it's less about the particular facts you know
[01:27:39] SPEAKER_00: as it is about your ability to acquire skills, acquire understanding. So it has to be good education.
[01:27:47] SPEAKER_00: Right. Okay. Serge, thank you so much for coming on the podcast. Thank you for fascinating.
[01:27:51] SPEAKER_04: Yeah, this was intense. That's tough questions.
[01:27:55] SPEAKER_04: I hope you enjoyed this episode. If you did, the most helpful thing you can do is just share it
[01:28:00] SPEAKER_04: with other people who you think might enjoy it. Send it to your friends, your group chats,
[01:28:04] SPEAKER_04: Twitter, wherever else. Just let the word go forth. Other than that, super helpful if you can
[01:28:08] SPEAKER_04: subscribe on YouTube and leave a five star review on Apple podcasts and Spotify.
[01:28:13] SPEAKER_04: Check out the sponsors in the description below. If you want to sponsor a future episode,
[01:28:17] SPEAKER_04: go to doarkash.com slash advertise. Thank you for tuning in. I'll see you on the next one.