# How OpenAI Builds for 800 Million Weekly Users: Model Specialization and Fine-Tuning

**Podcast:** A16z Podcast
**Date:** 2025-11-28
**Video ID:** 3x0jhpEj_6o
**Video URL:** https://www.youtube.com/watch?v=3x0jhpEj_6o

---

[00:00:00] We want Chatchy BTS first party up.
[00:00:02] SPEAKER_00: First party up is a really great way to get 800 million
[00:00:05] SPEAKER_00: while it was at whatever now.
[00:00:06] SPEAKER_00: 10th of the globe, right?
[00:00:08] Yeah, yeah, 10th of the globe uses it really.
[00:00:10] SPEAKER_00: Every week, every week.
[00:00:11] SPEAKER_00: Yeah, even with an opening eye, the thinking was that there would be like one model that rose from all.
[00:00:14] SPEAKER_00: It's like definitely completely changed.
[00:00:15] SPEAKER_00: It's like coming increasing and clearer that there will be room for a bunch of specialized models.
[00:00:19] SPEAKER_00: There will likely be a proliferation of other types of model.
[00:00:21] SPEAKER_00: Companies just have giant treasure troves of data that they are sitting on.
[00:00:25] SPEAKER_00: The big unlock that has happened recently is with the reinforcement fine tuning.
[00:00:28] SPEAKER_00: With that set up, we're now letting you actually run out of rail, which allows you to leverage your data way more.
[00:00:33] SPEAKER_00: Sure, and thanks very much for joining.
[00:00:41] SPEAKER_01: So we're being joined by Sherman Wu.
[00:00:43] SPEAKER_01: It'd be great actually if you provided the long form of your background as we get into this just for those that may not know you.
[00:00:48] SPEAKER_01: I mean, I've used Sherman as one of the top AI thought leaders, so I'm really looking forward to this.
[00:00:53] SPEAKER_01: Yeah, yeah, thanks for having me.
[00:00:54] SPEAKER_00: I'm really excited to be on the podcast.
[00:00:56] SPEAKER_00: Yeah, so a little bit more of my background.
[00:00:58] SPEAKER_00: So I'm maybe starting from President A. Go backward.
[00:01:01] SPEAKER_00: I currently lead the engineering team for OpenAI's developer platform.
[00:01:05] SPEAKER_00: So the biggest product in there, of course, is the API.
[00:01:09] SPEAKER_00: Is there more for the developer platform than the API?
[00:01:11] SPEAKER_01: I just kind of assume there is synonymous.
[00:01:13] SPEAKER_01: I also think about other things that we put into our platform side.
[00:01:17] SPEAKER_00: So technically our government work is also offering to sing into different areas.
[00:01:22] SPEAKER_00: Yeah, like I've talked about.
[00:01:23] SPEAKER_00: Oh, like so do you have like a local deployment like?
[00:01:26] SPEAKER_01: Yeah, so we actually do have a local deployments Atlas Alamos National Labs.
[00:01:29] SPEAKER_00: It's super cool. I went to visit it.
[00:01:31] SPEAKER_00: It's like very different than what am used to.
[00:01:34] SPEAKER_00: But yeah, in a like, you know, classified a supercomputer with our with our model running there.
[00:01:39] SPEAKER_00: Oh, that's cool.
[00:01:40] SPEAKER_00: So there's that.
[00:01:41] SPEAKER_00: But like mostly the API.
[00:01:43] SPEAKER_00: Did you go to Los Alamos?
[00:01:45] SPEAKER_00: We did. Yeah, I did go to Los Alamos.
[00:01:46] SPEAKER_00: That's great.
[00:01:47] SPEAKER_00: They showed us around.
[00:01:48] SPEAKER_00: They showed us some of the historic sites.
[00:01:50] SPEAKER_00: Yeah, I just work at Livermore, man.
[00:01:52] SPEAKER_01: So I've got like, oh, yeah, yeah.
[00:01:53] SPEAKER_01: Yeah, you're showing about a college.
[00:01:54] SPEAKER_01: So right, right, right.
[00:01:55] SPEAKER_01: You saw the next.
[00:01:56] SPEAKER_01: Yeah, yeah, yeah.
[00:01:57] SPEAKER_01: Well, we hope to.
[00:01:58] SPEAKER_00: We hope to.
[00:01:59] SPEAKER_00: But yeah, so I work on the developer platform.
[00:02:02] SPEAKER_00: I've been working on it for around three years now.
[00:02:05] SPEAKER_00: So I joined in 2022.
[00:02:07] SPEAKER_00: It was basically higher to work on the API product, which at the time was the only product that that opened I had.
[00:02:12] SPEAKER_00: Yeah.
[00:02:13] SPEAKER_00: And I've basically just worked on it the entire time.
[00:02:15] SPEAKER_00: I've always been super interested in the developer side and kind of like the startup story of this technology.
[00:02:19] SPEAKER_00: And so it's been really, really cool to kind of see this evolve.
[00:02:22] SPEAKER_00: And so that's my time in OpenAI.
[00:02:24] SPEAKER_00: Before OpenAI, I was at Open Door for around six years.
[00:02:28] SPEAKER_00: I was working on the pricing side.
[00:02:30] SPEAKER_00: My my journal background was for.
[00:02:31] SPEAKER_00: I think it's such a dissident like, yeah, pricing at OpenNord till I'm like running API.
[00:02:36] SPEAKER_01: It's such a different.
[00:02:37] SPEAKER_01: It's been fascinating actually for me to see the differences between the companies.
[00:02:40] SPEAKER_00: Yeah.
[00:02:41] SPEAKER_00: They're run so differently.
[00:02:42] SPEAKER_00: They both have opened in the name.
[00:02:43] SPEAKER_00: So I just got some overlap.
[00:02:44] SPEAKER_00: But like that's that's pretty much it.
[00:02:47] SPEAKER_00: But yeah, I was there for around six years working on the pricing team.
[00:02:50] SPEAKER_00: So our team basically would run the ML models.
[00:02:53] SPEAKER_00: This is actually pricing the assets on Open Door.
[00:02:55] SPEAKER_01: Yeah, yeah, the inventory.
[00:02:57] SPEAKER_01: Exactly.
[00:02:58] SPEAKER_00: So open door would buy and sell homes.
[00:03:00] SPEAKER_00: And their main product was buying homes directly from people selling them with all cash offers.
[00:03:04] SPEAKER_00: And so my team was responsible for how much we would pay for them.
[00:03:07] SPEAKER_00: And so it was a really fun like ML challenge.
[00:03:10] SPEAKER_00: It had a huge operational element to it as well because not everything was automated obviously.
[00:03:15] SPEAKER_00: But it was a really fascinating technical challenge.
[00:03:17] SPEAKER_00: And is there any sense of that on the API side like like GPU capacity buying or is it just totally unrelated on the API side?
[00:03:24] SPEAKER_00: There is a small bit of like how we price the models.
[00:03:28] SPEAKER_00: But I don't think we do anything as sophisticated as OpenNord.
[00:03:34] SPEAKER_00: OpenNord was just like such a hard problem.
[00:03:36] SPEAKER_00: It's like such a like expensive asset.
[00:03:38] SPEAKER_00: It's like the holding costs are very expensive.
[00:03:42] SPEAKER_00: You're like holding onto it for like months at a time.
[00:03:44] SPEAKER_00: There's like a variability in like the holding time.
[00:03:46] SPEAKER_01: And that's a long tail of like potential things.
[00:03:48] SPEAKER_01: Long tail.
[00:03:49] SPEAKER_01: Yes.
[00:03:50] SPEAKER_00: And like you know you have to so you like try to think about it from a portfolio perspective.
[00:03:52] SPEAKER_00: And like if one of them just like you're holding on it for two years it blows everything.
[00:03:55] SPEAKER_00: Everything like goes negative.
[00:03:57] SPEAKER_00: So it's a very very different.
[00:03:59] SPEAKER_00: Six years.
[00:04:00] SPEAKER_00: Different challenge.
[00:04:01] SPEAKER_00: Yeah. Yeah.
[00:04:02] SPEAKER_00: Six years there.
[00:04:03] SPEAKER_00: Lots of up and downs.
[00:04:04] SPEAKER_00: Saw a lot of the booms.
[00:04:05] SPEAKER_00: Saw a lot of the struggles.
[00:04:06] SPEAKER_00: And then we IPO'd before I lied.
[00:04:10] SPEAKER_00: But yeah just in general is a very great experience.
[00:04:12] SPEAKER_00: I think for me it was also just like had such a varied like business operations.
[00:04:18] SPEAKER_00: Yeah.
[00:04:19] SPEAKER_00: And like a very like by the book type of culture.
[00:04:21] SPEAKER_00: Whereas OpenNord is like very different.
[00:04:23] SPEAKER_00: So interesting.
[00:04:24] SPEAKER_01: I was just thinking about it now.
[00:04:25] SPEAKER_01: It's like even for a company like that.
[00:04:26] SPEAKER_01: Like you don't think about it as a tech company.
[00:04:27] SPEAKER_01: But if there is a deep technology problem and actually is the pricing right.
[00:04:30] SPEAKER_01: It's actually an ML problem.
[00:04:31] SPEAKER_01: Yeah. That's what it's trying to come.
[00:04:32] SPEAKER_01: It's not like the website is not.
[00:04:33] SPEAKER_01: Yeah.
[00:04:34] SPEAKER_01: Yeah.
[00:04:35] SPEAKER_01: Yeah.
[00:04:36] SPEAKER_01: It's not the platform.
[00:04:37] SPEAKER_01: It's like it's not the API is literally that.
[00:04:38] SPEAKER_00: And that's what it's trying to me to.
[00:04:39] SPEAKER_00: I think that was was was interesting.
[00:04:41] SPEAKER_00: It's also a way like lower margin business then open AI.
[00:04:45] SPEAKER_00: Because you're like making a tiny spread on these homes.
[00:04:48] SPEAKER_00: They talk about like basis points like eating bits for breakfast and all that.
[00:04:51] SPEAKER_00: So yeah.
[00:04:52] SPEAKER_00: And it was all that open open door for around six years.
[00:04:55] SPEAKER_00: And then before that was my first job out of college.
[00:04:57] SPEAKER_00: Which was at Kora with Adam D. Ansfield.
[00:04:59] SPEAKER_00: No, I'm kind of there.
[00:05:00] SPEAKER_00: Yeah.
[00:05:01] SPEAKER_00: So I was working on the newsfeed.
[00:05:02] SPEAKER_00: Oh yeah.
[00:05:03] SPEAKER_00: So worked on newsfeed ranking for a bit.
[00:05:04] SPEAKER_00: Worked on the product side.
[00:05:05] SPEAKER_00: Yeah.
[00:05:06] SPEAKER_00: But was that was actually my first exposure to like actual ML and industry and learned a lot
[00:05:12] SPEAKER_00: from from the engineers at Kora.
[00:05:15] SPEAKER_00: We basically hired a lot of the early like feed engineers.
[00:05:18] SPEAKER_00: Charlie still there.
[00:05:19] SPEAKER_01: But you were there.
[00:05:20] SPEAKER_00: Charlie was not there when I.
[00:05:21] SPEAKER_00: Oh, right.
[00:05:22] SPEAKER_00: Yeah.
[00:05:23] SPEAKER_00: Yeah.
[00:05:24] SPEAKER_01: Yeah.
[00:05:25] SPEAKER_00: That was a really legendary team.
[00:05:26] SPEAKER_00: I was still it's still known to be kind of this of super iconic founding team.
[00:05:29] SPEAKER_01: Yeah.
[00:05:30] SPEAKER_00: Yeah.
[00:05:31] SPEAKER_00: The early founding team was really solid.
[00:05:32] SPEAKER_00: I still think that even while I was there, I was I still like him amazed at the quality of the talent.
[00:05:36] SPEAKER_00: That we had.
[00:05:37] SPEAKER_00: So no, I think there's like when the company was like 50 to 100 people, but like, yeah, like a bunch of the
[00:05:42] SPEAKER_00: perplexity team was there.
[00:05:43] SPEAKER_00: Dennis was on the feed team with me.
[00:05:45] SPEAKER_00: Yeah.
[00:05:46] SPEAKER_00: Johnny Ho, Jerry Ma.
[00:05:49] SPEAKER_00: That's right.
[00:05:50] SPEAKER_00: And then Alexander the scale.
[00:05:52] SPEAKER_00: Yeah, that's the way.
[00:05:53] SPEAKER_00: You know, like it was there.
[00:05:55] SPEAKER_00: He was he was there between high school and college.
[00:05:58] SPEAKER_00: It was an incredible team.
[00:05:59] SPEAKER_00: I don't think I think I kind of took it for granted.
[00:06:01] SPEAKER_00: All is there.
[00:06:02] SPEAKER_00: I was a good group.
[00:06:03] SPEAKER_00: But how did you get to Kora?
[00:06:06] SPEAKER_01: What did you study in the undergrad?
[00:06:08] SPEAKER_01: Yeah.
[00:06:09] SPEAKER_00: So before that, I was at MIT for undergrad.
[00:06:10] SPEAKER_00: I studied computer science.
[00:06:12] SPEAKER_00: I did like one of those like computer science and the master's degree kind of like I've printed in.
[00:06:17] SPEAKER_00: I ended up a core because I got in what we call an externship there.
[00:06:22] SPEAKER_00: So like at MIT, you actually get January off.
[00:06:25] SPEAKER_00: So there's like the fall semester and then January's off.
[00:06:27] SPEAKER_00: And then you have the spring semester.
[00:06:29] SPEAKER_00: And so it's kind of this is called independent activities period.
[00:06:32] SPEAKER_00: So some people just like take classes.
[00:06:33] SPEAKER_00: Some people just do nothing.
[00:06:34] SPEAKER_00: But it's some people do like month long internships.
[00:06:38] SPEAKER_00: And some crazy companies will like offer a month long internship to a college student.
[00:06:41] SPEAKER_00: And it really is just kind of like a way to get people in.
[00:06:44] SPEAKER_00: Did you come out here from Boston?
[00:06:46] SPEAKER_01: Yeah, he was.
[00:06:47] SPEAKER_01: Yeah, it was crazy.
[00:06:48] SPEAKER_00: So so so you had to apply.
[00:06:51] SPEAKER_00: I remember.
[00:06:52] SPEAKER_00: Yeah, this is like I think 2013's January or something.
[00:06:56] SPEAKER_00: You had to apply.
[00:06:57] SPEAKER_00: And I remember the core internship was the one that just paid the most.
[00:06:59] SPEAKER_00: They paid I think it was like 8,000, 9,000.
[00:07:01] SPEAKER_00: And it was like, well, it's like a month and you're kind of wrapping up like half the time.
[00:07:05] SPEAKER_00: I can eat for a year.
[00:07:06] SPEAKER_00: Yeah, yeah.
[00:07:07] SPEAKER_01: As a college student, it's like great.
[00:07:08] SPEAKER_01: And you get a and yeah, they would they would kind of like fly out.
[00:07:11] SPEAKER_00: You'd fly you out here.
[00:07:12] SPEAKER_00: And so I did the interviews and then luckily gone off.
[00:07:14] SPEAKER_00: And so yeah, I came out for a January.
[00:07:17] SPEAKER_00: That was right when they moved into their new Mountain View office.
[00:07:19] SPEAKER_00: And I basically, yeah, honestly just ramped up for like two weeks.
[00:07:23] SPEAKER_00: And then have like two weeks of good productivity working on the feed team.
[00:07:26] SPEAKER_00: So that was that on the.
[00:07:27] SPEAKER_00: Was that like user facing?
[00:07:29] SPEAKER_01: Yeah, user facing product work.
[00:07:31] SPEAKER_01: Yeah, I distinctly remember my externship project for those two weeks was just to like add a couple features who are a future store.
[00:07:37] SPEAKER_00: Yeah.
[00:07:38] SPEAKER_00: And like that would make it sway into the model.
[00:07:40] SPEAKER_00: Okay.
[00:07:41] SPEAKER_00: I was going to say my, I remember my mentor there was his tutor who is now running I think it's called harmonic labs.
[00:07:47] SPEAKER_00: Yeah, yeah, yeah.
[00:07:48] SPEAKER_00: Crazy team.
[00:07:49] SPEAKER_00: Crazy team.
[00:07:50] SPEAKER_01: I mean, by the way, I think it's one of the untold stories of Silicon Valley's like how good that original team and a course.
[00:07:55] SPEAKER_01: I mean, a lot of them still, you know, they're still good, but like the diaspora from Kora's everywhere.
[00:08:00] SPEAKER_01: Yeah, yeah.
[00:08:01] SPEAKER_00: That's actually how I ended up at OpenAI to kind of like, you know, fast-forwarding from there.
[00:08:04] SPEAKER_00: Because I, OpenAI kind of kept a quiet profile ish.
[00:08:07] SPEAKER_00: But I'd always kind of kept out some them because a bunch of the Kora,
[00:08:11] SPEAKER_00: a core people I knew kind of like ended up there.
[00:08:13] SPEAKER_00: Yeah, it's kind of like checking in on on on it.
[00:08:15] SPEAKER_00: And they were like, yeah, something crazy is happening here.
[00:08:17] SPEAKER_00: You know, you should definitely check it out.
[00:08:19] SPEAKER_00: So yeah, I definitely owe a lot to Kora.
[00:08:21] SPEAKER_00: But yeah, part of the reason why I went there versus other options as a new grad was the team was just so incredible.
[00:08:26] SPEAKER_00: And I just felt like I could learn a ton from them.
[00:08:29] SPEAKER_00: I didn't think about everything afterwards.
[00:08:30] SPEAKER_00: I was just like, man, in fact, I just like absorbed some knowledge from this like, you know, group of people.
[00:08:34] SPEAKER_00: It would be great.
[00:08:35] SPEAKER_00: Awesome.
[00:08:36] SPEAKER_01: So one place I wanted to start is something that I find very unique about OpenAI is it's both a pretty horizontal company.
[00:08:46] SPEAKER_01: Like it's got an API.
[00:08:47] SPEAKER_01: Like I would say we've got this massive portfolio of companies right now.
[00:08:51] SPEAKER_01: I would say a good fraction of them use the API.
[00:08:55] SPEAKER_01: And then it's also a vertical company in that you've got full on apps.
[00:08:59] SPEAKER_01: Right?
[00:09:00] SPEAKER_01: Yeah.
[00:09:01] SPEAKER_01: You know, like everybody uses a chatGPT for example.
[00:09:03] SPEAKER_01: And so, you know, you're responsible for like the API and kind of the DevTool size.
[00:09:08] SPEAKER_01: So maybe just to begin with, like, is there an internal tension between the two?
[00:09:13] SPEAKER_01: Like is that a discussion like, you know, like the API may, whatever, it may help a competitor to like the vertical version.
[00:09:22] SPEAKER_01: Or is it not, the things are just growing so fast as that initial.
[00:09:26] SPEAKER_01: I'll just love to how you think about that.
[00:09:28] SPEAKER_01: By the way, it's very unusual for companies to have both of that.
[00:09:30] SPEAKER_01: Yeah.
[00:09:31] SPEAKER_01: Yeah.
[00:09:32] SPEAKER_00: Yeah.
[00:09:33] SPEAKER_00: Completely great.
[00:09:34] SPEAKER_00: I think there is, there's some amount of tension.
[00:09:36] SPEAKER_00: I would say it's, I think one thing that really helps here is Sam and Greg just from a like founder perspective.
[00:09:42] SPEAKER_00: Yeah.
[00:09:43] SPEAKER_00: Have since day one just been very principled in the way in which we approach this.
[00:09:47] SPEAKER_00: They've always, you know, have kind of told us, you know, we want chatGPT as a first party app.
[00:09:51] SPEAKER_00: We also want the API.
[00:09:53] SPEAKER_00: And then, and the nice thing is I think they're able to do this because at the end of the day kind of comes back to the mission of OpenAI, which is to Great Asia.
[00:10:00] SPEAKER_00: And then to distribute the benefits as broadly as possible.
[00:10:02] SPEAKER_00: Yeah.
[00:10:03] SPEAKER_00: And so if you interpret this, you want it in as many surfaces as you want.
[00:10:06] SPEAKER_00: And the first party app is a really great way to get, you know, it was like 800 million a while or whatever now.
[00:10:11] SPEAKER_00: Yeah.
[00:10:12] SPEAKER_00: But the 100 million a while.
[00:10:13] SPEAKER_00: Yeah.
[00:10:14] SPEAKER_00: It's pretty, it's actually mind boggling to think about.
[00:10:17] SPEAKER_00: I don't think many people listening to this don't understand how big that is.
[00:10:21] SPEAKER_01: Yeah.
[00:10:22] SPEAKER_01: It's crazy.
[00:10:23] SPEAKER_01: It's going to be like actually historic for the time it's taken to get 800 million.
[00:10:27] SPEAKER_01: It's historic.
[00:10:28] SPEAKER_00: It's also just like, yeah, the amount of time and just like how much we've had to scale up.
[00:10:31] SPEAKER_00: I think 10th of the globe.
[00:10:33] SPEAKER_01: Yeah.
[00:10:34] SPEAKER_01: Yeah.
[00:10:35] SPEAKER_00: Yeah.
[00:10:36] SPEAKER_00: 10th of the globe uses it every week.
[00:10:37] SPEAKER_00: Every week.
[00:10:38] SPEAKER_01: Yeah.
[00:10:39] SPEAKER_00: And at some point, you know, it'll hit like, you know, it'll go even higher than that.
[00:10:42] SPEAKER_00: And so, um, so yeah, like obviously the reach there is unmatched.
[00:10:44] SPEAKER_00: But then also just like being able to have a platform where we can reach even more than just that.
[00:10:49] SPEAKER_00: Like one thing we talk about internally sometimes is, like what does our end user reach from the API?
[00:10:53] SPEAKER_00: Like it's actually, it was like really, really, it's really broad.
[00:10:56] SPEAKER_00: It might even, it's hard because chatchabies growing so quickly.
[00:10:59] SPEAKER_00: But like, like at some point, it was definitely larger than than chatchabit.
[00:11:02] SPEAKER_00: And the fact that we're able to get tap in all this and get the reach that we want, I think is really good.
[00:11:07] SPEAKER_00: Yeah.
[00:11:08] SPEAKER_00: But yeah, I mean, there's definitely some tension sometimes.
[00:11:09] SPEAKER_00: I think the, um, I think it's come up in a couple of places.
[00:11:12] SPEAKER_00: I think one of them is on the product side.
[00:11:14] SPEAKER_00: So as you mentioned, you know, sometimes there are competitors kind of like building on our, yeah, on our platform,
[00:11:20] SPEAKER_00: who, you know, might not be happy if chatchabit launches something that can piece with them.
[00:11:24] SPEAKER_00: Yeah.
[00:11:25] SPEAKER_01: Um, I mean, that, you know, that's the tale of the old is the cloud operating systems or what.
[00:11:28] SPEAKER_01: Yeah.
[00:11:29] SPEAKER_01: So like that's, you know, I think it's more like, does chatchabit work about the competitor.
[00:11:34] SPEAKER_01: Yeah.
[00:11:35] SPEAKER_01: You know, type thing like, you know, you enabling a competitor.
[00:11:38] SPEAKER_01: Yeah.
[00:11:39] SPEAKER_00: Yeah.
[00:11:40] SPEAKER_00: So I mean, uh, the interesting thing is like, I would say not particularly, most of just because we've been growing so quickly.
[00:11:44] SPEAKER_00: Because it's like, you know, it's such a, you know, force right now.
[00:11:47] SPEAKER_01: Yeah.
[00:11:48] SPEAKER_01: Yeah.
[00:11:49] SPEAKER_00: Growth solves so many, so many different things.
[00:11:50] SPEAKER_00: And like, and the other way we think about is like, everyone's kind of building, building around AGI, building towards AGI.
[00:11:55] SPEAKER_00: Of course, there's going to be some overlap here.
[00:11:57] SPEAKER_00: Um, so yeah, I mean, but, but I would say like, at least in my position, I feel more of the tension from the customer, like the API customers themselves.
[00:12:03] SPEAKER_00: Like, oh, my gosh, you know, you like, are you going to build this thing that I'm working on?
[00:12:06] SPEAKER_00: Yeah, that's that story is this old.
[00:12:08] SPEAKER_00: Yeah, yeah, yeah.
[00:12:09] SPEAKER_01: There's never been a platform that didn't have that problem.
[00:12:12] SPEAKER_01: So, so okay, so I kind of go back and forth in this one.
[00:12:15] SPEAKER_01: I want to try one out on you, um, which is the, the problem historically with, you know, offering, um, a core services and APIs, you can get disinimediated, right?
[00:12:26] SPEAKER_01: And so I can build on top of it, but then, you know, the user doesn't know, like whatever, I build on top of the cloud.
[00:12:32] SPEAKER_01: I just don't remediate from the cloud and then I can switch to another cloud or whatever.
[00:12:36] SPEAKER_01: And it occurs to me that that's kind of hard to do with these models because the models are so hard to abstract away.
[00:12:43] SPEAKER_01: Like they're just, they're just unruly, right?
[00:12:45] SPEAKER_01: If you try to like have traditional software drive them, they just don't kind of manage very well.
[00:12:50] SPEAKER_01: So part of me thinks that it's almost like this, like anti-disinder mediation technology that you kind of have to expose it to the, to the user directly.
[00:13:00] SPEAKER_01: Yep. Does that make sense? And so I'm wondering if like, so even if I think chat GPD is really just trying to expose the model to the user, the APIs kind of just trying to expose the models to the user.
[00:13:08] SPEAKER_01: So I think there's almost this argument that's like, if the real value is in the models, it doesn't really matter how you get it to them.
[00:13:15] SPEAKER_01: Because it's going to be very tough for someone who's going to to abstract it away.
[00:13:17] SPEAKER_01: And in the, in the classic sense of computer science of like they don't know if they're using the model.
[00:13:21] SPEAKER_01: Like you always know you're using GPD five.
[00:13:23] SPEAKER_01: Yeah. And the interesting thing is I think like the entire industry kind of has slowly changed their mind around this too.
[00:13:28] SPEAKER_00: I think like in the beginning we kind of thought like, oh, these are all going to be interchangeable.
[00:13:31] SPEAKER_00: It's just like software. Yeah, exactly.
[00:13:33] SPEAKER_01: So she's afraid I just swap out. Yeah.
[00:13:35] SPEAKER_00: But I think we're learning this on the product side with like, you know, the GPD five launch and like four O and like help so many people like to three and four O and all of that.
[00:13:42] SPEAKER_00: I felt that when it changed. I'm like, I'm like, who not as nice to be here.
[00:13:47] SPEAKER_01: Like I like the validation.
[00:13:49] SPEAKER_01: Yeah. It's actually fun because I really loved GPD five's personality.
[00:13:53] SPEAKER_00: I think it's like the way I use you know, chat GPT was very utilitarian.
[00:13:56] SPEAKER_00: Oh, it's like, you know, mostly for work or just like information.
[00:13:59] SPEAKER_00: Yeah, I've definitely come around to see you know, but like I actually felt a distance when it changed.
[00:14:02] SPEAKER_01: It's like it's like, yeah, like there's this emotional thing that goes on.
[00:14:05] SPEAKER_01: But it's almost like it's an anti, you know, dissonant mediation technology.
[00:14:09] SPEAKER_01: Yeah. Like you kind of have to show this to the user.
[00:14:11] SPEAKER_01: Yeah. Yeah.
[00:14:12] SPEAKER_00: And then you see a lot of like, you know, more successful products like cursor like do this directly, especially the coding products where users want more control.
[00:14:18] SPEAKER_00: We've even seen some like, you know, like more general consumer products do this.
[00:14:22] SPEAKER_00: And so it's definitely been sure on the on the consumer side.
[00:14:24] SPEAKER_00: The interesting thing is I think it's also been sure on the API side.
[00:14:27] SPEAKER_00: And that's also something that I think.
[00:14:28] SPEAKER_00: No, exactly.
[00:14:29] SPEAKER_00: It's exactly what I'm saying.
[00:14:30] SPEAKER_00: Yeah.
[00:14:31] SPEAKER_00: So like the argument could be that I could use the API to disinmediate you.
[00:14:34] SPEAKER_01: But like you don't see that happening because it's so hard to put a layer of software between a model and a person.
[00:14:40] SPEAKER_01: You almost have to expose the model.
[00:14:42] SPEAKER_01: Yes.
[00:14:43] SPEAKER_01: Yes.
[00:14:44] SPEAKER_00: And I think if anything, I think the models are like almost like diverging in terms of like what they're good at.
[00:14:49] SPEAKER_00: And like there's a specific use case.
[00:14:50] SPEAKER_00: And I think there's going to be more and more of this.
[00:14:52] SPEAKER_00: But yeah, basically it's been surprisingly hard for like the retention of people building on our API is like surprisingly high.
[00:15:00] SPEAKER_00: Especially when people thought you could just kind of swap things around.
[00:15:02] SPEAKER_00: You might have, you know, like even tools that help you swap things around.
[00:15:06] SPEAKER_00: But yeah, the stickiness of the model itself has been surprising.
[00:15:10] SPEAKER_00: And then do you think that is because of a relationship between the user and the model.
[00:15:14] SPEAKER_01: Or do you think it's more of a technical thing, which is like my evals work for like open AI and this, you know, and like the correctness means tanes or yeah.
[00:15:25] SPEAKER_00: Yeah.
[00:15:26] SPEAKER_00: Yeah.
[00:15:27] SPEAKER_00: I think it's both.
[00:15:28] SPEAKER_00: So I think there's definitely an end user piece here, which is what we've heard from from some of our customers.
[00:15:30] SPEAKER_00: Like they just get familiar with the model itself.
[00:15:32] SPEAKER_00: But I also think there's a technical piece, which is like the also as a developer, especially with startups, you're like really going deep with these models.
[00:15:39] SPEAKER_00: And like really like iterating on it, trying to get get it really good within your particular harness.
[00:15:44] SPEAKER_00: You're iterating on your harness itself.
[00:15:46] SPEAKER_00: You're giving it different tools here and there.
[00:15:48] SPEAKER_00: And so you really do end up like building a product around the model.
[00:15:51] SPEAKER_00: And so there is a technical piece where, you know, as you kind of keep building with a particular product like GPT-5, you're actually like building more around it so that your product worked uniquely well with that with that model.
[00:16:03] SPEAKER_00: So I use cursor.
[00:16:06] SPEAKER_01: And a lot of just for like a lot of something like fighting blogs and like, you know, we're investors and I use it for sometimes for coding.
[00:16:14] SPEAKER_01: And it's remarkable how many models I use in cursor.
[00:16:17] SPEAKER_01: So like literally might go to model at GPT-5.
[00:16:19] SPEAKER_01: Yeah.
[00:16:20] SPEAKER_01: I love GPT-5.
[00:16:21] SPEAKER_01: I think it's a phenomenal like, you know, and then like I use like Max mode with GPT-5 for planning.
[00:16:26] SPEAKER_01: And then but you know, like I mean, I like the tab complete model that's in cursor and like, you know, the new model they just dropped is for like some basic, you know, some stuff is good.
[00:16:34] SPEAKER_01: Yeah, it's composed once good.
[00:16:36] SPEAKER_01: And so like, you know, and I think that like kind of reflects this too, because it's like, you see a particular model for each particular you say.
[00:16:44] SPEAKER_00: Like I've talked to a bunch of people who use the new composer model and it's just really good for like fast, like first pass, like keep you in flow kind of thing.
[00:16:52] SPEAKER_00: And then you kind of like bubble out to another model if you want like, you know, deeper thing.
[00:16:55] SPEAKER_00: I mean, let me sit down.
[00:16:56] SPEAKER_00: I literally sit down on GPT-5 to help me plan something out.
[00:16:59] SPEAKER_01: And then you know, like when I'm coding and I'm doing like the quick chat thing, then I'll use composer and then there's like whatever there's like some crazy bug or something like that.
[00:17:08] SPEAKER_01: So, you know, do you remember like in the early days of all of this where like there's going to be one model and I mean like, even like investors like we will never invest in a model company because like the only B1 model and it's going to be a GI but like the reality
[00:17:22] SPEAKER_01: it feels like there's this massive proliferation of models like you said before they're doing many things and so maybe two questions, maybe two Blunt or two crafts, but the first one is what does that mean to eight for a GI and the second was what does that mean for opening I like does that mean that like
[00:17:36] SPEAKER_01: you end up with a model portfolio do you select a subset do you think this all gets superseded by some God model in the future like how does that play out because it's against what most people thought most people thought this is all going towards one large model that does every day.
[00:17:48] SPEAKER_01: Yeah, I think the crazy thing about all this is just like how everyone's thinking has just changed over time like the I distinctly remember this like and the crazy thing is not that long ago.
[00:17:57] SPEAKER_00: It's just like three like two or three years ago. I remember like even within opening the thinking was that there would be like one model that rules them all and it's like why would you I mean like this kind of goes to fine tuning API product.
[00:18:07] SPEAKER_00: There's like why would you even have a fine tuning product why would you even want to like iterate on it. There's going to be this one model that just subsumes everything.
[00:18:13] SPEAKER_00: And that was also kind of the that is also like the most simplistic like view of what the what the AGI will look like.
[00:18:19] SPEAKER_00: And yeah, it's like definitely completely changed since then I think one and then the other thing to keep in mind is like it might continue to change like you and from where we are today.
[00:18:29] SPEAKER_00: But it's like becoming increasing and clear I think that there will be room for a bunch of specialized models. There will likely be a proliferation of other types of models.
[00:18:37] SPEAKER_00: I mean, you see us do this with like the codex model. It's only itself. We have like a way like GPT 41 and like 40 and like five and and and all of this.
[00:18:46] SPEAKER_00: And so I don't think there's room for all for all this. I don't think that's bad for what's worth like if anything. I think you know as we've tried to move towards AGI things have just been very unexpected.
[00:18:57] SPEAKER_00: And I think the market just evolved and the product portfolio evolves because of that. So I don't think it's a bad thing at all.
[00:19:02] SPEAKER_00: What I do think it's easy. I get very good for open AI and very good for like the model companies to like yeah because not have like you know winner take all consolidated dynamics right.
[00:19:12] SPEAKER_01: I mean, you just have to help your ecosystem a lot more solutions. You can provide a lot. Yeah, you know. Yeah. And as as you can some grows it generally is helpful.
[00:19:19] SPEAKER_00: Like this is one thing we actually think about a lot too is as the general like yeah, you can see some grows like opening. I just stands to benefit a lot from this.
[00:19:25] SPEAKER_00: And this is also why we've like some of our parts we've been started opening up to other models like our e-valls product now allows you to bring in other models.
[00:19:34] SPEAKER_00: It's all this we think it's like any any rising tide generally helps us here.
[00:19:38] SPEAKER_00: But yeah, I think as we move into a world where there would be a bunch more models. This is why we've kind of invested in our model customization product with fine tuning API with the reinforcement fine tuning opening that up as well.
[00:19:48] SPEAKER_00: It's also why part of why we open sourced GPT OSS as well because we want to be able to you know, physical take on that.
[00:19:54] SPEAKER_00: Super I want to talk about that in just a bit. The open source is actually very interesting. I mean actually I thought the open source model was great. Yeah.
[00:20:01] SPEAKER_01: But clearly something that company has to be careful with.
[00:20:04] SPEAKER_01: But before that, I want to talk a little bit about the fine tuning API. So so I've noticed that you are moving towards kind of more sophisticated use of things like you know like fine tuning.
[00:20:15] SPEAKER_01: Which you know in a way you could read that as a bit of a capitulation not like.
[00:20:20] You know there is product specific data and this product specific use cases that a general model will do to your point right.
[00:20:27] SPEAKER_01: So like as opposed to proliferation model you do that. It seems like a lot of that data is actually very very valuable right. And so you know to what extent is there.
[00:20:37] SPEAKER_01: Like interest in almost a tit for tat where you can like expose.
[00:20:44] SPEAKER_01: You know the ability to get product data into fine tuning and then you also benefit from that data because.
[00:20:51] SPEAKER_01: Oh yeah the vendors provide it to you versus like this is a hundred percent you know like they keep their own data and there's kind of no interest in that.
[00:21:00] SPEAKER_01: Because I feel to me like the next level of scaling this is kind of where I'm right. And so this kind of curious how.
[00:21:05] SPEAKER_01: Yeah so I mean maybe even like taking a step back the main reason why we even invested in a fine tuning API in the very beginning is one there's been huge demand from people to be able to customize them all.
[00:21:17] SPEAKER_00: It kind of goes into like prompt engineering and also like I think the industry's change our mind on that as well like it's evolved.
[00:21:22] SPEAKER_00: The second thing is exactly what you said which is the companies just have giant treasure troves of data that they're sitting on that they would like to utilize in some fashion in this AI wave.
[00:21:32] SPEAKER_00: And you can you know the simple things to put it in like you know some like vector like do rag with it or something.
[00:21:37] SPEAKER_00: Yeah.
[00:21:38] SPEAKER_00: But there's also you know if they have a more technical team they do want to see how they can use it to customize the models.
[00:21:42] SPEAKER_00: And so that is actually the main reason why we've invested in in this.
[00:21:46] SPEAKER_00: The interesting thing was way back kind of back in like 2223 are fine tuning offering was I'd say like too limited so that it was very difficult people to to tap into and use this data.
[00:21:57] SPEAKER_00: So it was just like an asset like a supervised fine tuning.
[00:22:00] SPEAKER_00: Yeah and like we're like oh you can kind of use it but in practice it really is only useful for like like it's honestly just like instruction following plus plus you like kind of change the tone.
[00:22:09] SPEAKER_00: And you're really constructing it.
[00:22:11] SPEAKER_00: But I think the big unlock that has happened recently is with the reinforcement fine tuning model because with that setup we're now letting you actually run actually run a real which is more finicky and it's like harder and you know like you need to invest more in it.
[00:22:23] SPEAKER_00: But it allows you to leverage your data way more.
[00:22:25] SPEAKER_00: But this is just a naive question from which is it feels from just my understanding from my own portfolio feels like there's two modalities of use.
[00:22:34] SPEAKER_01: One of them is I've got a treasure trove data that I've had for a long time and I create my model on that treasure trove data and all that happens offline and then I deploy that.
[00:22:42] SPEAKER_01: Yeah. There's another one which is like I actually have the product being used a real time. I've got a bunch of users.
[00:22:47] SPEAKER_01: Yeah. And like I can actually get much closer to the user. I can kind of a be test and decide which data and like it's kind of more of a near real time thing is is like is this focus on like more product stuff or more.
[00:23:00] SPEAKER_01: Yeah. So the dream with the fine tuning API was that we should be able to handle both right. It's like it's like we actually have this dream and we have this whole like Laura set up with the fine tuning inference where we should just be able to scale to like millions and millions of of these fine tune models which is usually what would happen if you have like this online learning.
[00:23:14] SPEAKER_00: Exactly. In practice, it's mostly been the the form in process. Most even like the offline data that they've like already created or they are creating with experts or something and like using their product that they're that they're able to use here.
[00:23:26] SPEAKER_00: But the main thing I was trying to say around the reinforcement fine tuning APIs it kind of changes the paradigm away from just like small incremental input like tone improvements, which is what SFT did to actually improving the model to potentially soda level on a particular use case that you know about.
[00:23:42] SPEAKER_00: Like that's where people have really started using the reinforcement fine tuning API and that's why it's it's gone more more more uptake because if if the discussion is less like hey I can make this model you know not like speak in a certain way better it's less compelling but if it's like hey for like you know medical insurance coding or for like coding planning,
[00:24:01] SPEAKER_00: Agente planning or something you can create the world's best model using your data set with RFT and it becomes a lot more and will you ever like or maybe do you will you ever like find ways to get access to that data like yeah so this and if I had the data and I wanted cheap GPUs I'd trade you for it.
[00:24:17] SPEAKER_01: Yeah, I mean we we've talked about this and we've actually been piloting some pricing here too where it's like because this data is like really helpful and it's kind of hard to get and if you actually build with the reinforcement fine tuning API you can actually
[00:24:29] SPEAKER_00: get discounted in France and potentially free training to if you're willing to share the data it's always kind of you know it's up to the customer there but if they do it is helpful for us and there would be benefits for the for the customer as well.
[00:24:40] SPEAKER_00: That's awesome. Okay, you said that's a views on prompt engineering have changed. Yeah, I was actually I wasn't aware of that. All the other things I wasn't aware of this one I wasn't. How was it?
[00:24:51] SPEAKER_01: I mean I think the prevailing view this is back in 2022 I remember I was talking to so many people and they're basically I mean this is similar to like the single model AGI view as well which is like like prompt engineering is just not going to be a thing and you're just not going to have to think about what you're putting in the in the context window in the future like the model would just be good enough.
[00:25:08] SPEAKER_00: It will just like no you don't know what what you need to do. Yeah, that's something not a thing. Yeah, but like I don't know maybe people forget it but like that was like a very common.
[00:25:16] SPEAKER_00: Yeah, it's like scaling laws or what are something scaling laws and like you'll just mind meld with the model and like you just like like prompting and like instruction falling will just will be so good that you won't really need to do it.
[00:25:26] SPEAKER_00: And if anything like yeah, it's like clearly been wrong and yeah, yeah, yeah.
[00:25:29] SPEAKER_00: But it is interesting because I think it's a slightly different world that we're in now where the models have gotten really really good at instruction following relative to the like GB 35 or something.
[00:25:39] SPEAKER_00: Yeah, but I think the name of the game now is is less on like prompt engineering as we have thought about it two years ago.
[00:25:44] SPEAKER_00: It's more of like it's like the context engineering site where it's like what are the tools you give it.
[00:25:48] SPEAKER_00: What is like the data that it pulls in when does it pull on the right data? It's very interesting.
[00:25:51] SPEAKER_00: I mean, I mean, to reduce it to like an almost absurdly simplistic level like the weird thing about rag.
[00:25:58] SPEAKER_01: For example, the classic use of rag is like you're using like cosine similarity to choose something that you're going to feed into a super intelligence.
[00:26:05] SPEAKER_01: You know, you're like, I'm the random thing. I'm like randomly grabbed this thing.
[00:26:10] SPEAKER_01: Yeah, like fucking embedding space.
[00:26:13] SPEAKER_01: And then I'm like, you know, when you want the super intelligence to decide the thing to do.
[00:26:17] SPEAKER_01: And so it's like pushing intelligence in that retrieval.
[00:26:20] SPEAKER_01: Yeah, clearly is something that makes sense.
[00:26:22] SPEAKER_01: Yeah, and to be like the pushing the intelligence out in a way.
[00:26:25] SPEAKER_01: Exactly. And to be fair, I think like rag was kind of introduced when the models were like it's like pre-reasing model.
[00:26:30] SPEAKER_00: So it was like, you only had to kind of like one shot to like do this and it wasn't that smart.
[00:26:33] SPEAKER_00: But now that we do have the reasoning models, now that we have, I mean, if you like one of my favorite models is actually 03 because it was like one of the most diligent models.
[00:26:41] SPEAKER_00: It was like, it would just like do all these tool calls.
[00:26:44] SPEAKER_00: And it's like really the intelligence itself trying to like do the you know, tool calls or rag or anything like that.
[00:26:50] SPEAKER_00: Or write the code to execute.
[00:26:52] SPEAKER_00: And so the paradigm has shifted there.
[00:26:54] SPEAKER_00: But yeah, because of that, I think like Conducts engineering, Prompt Engineering, what you put, what you give the models they extra important.
[00:27:00] SPEAKER_00: Yeah.
[00:27:01] SPEAKER_01: Okay, so you have API, so the API which is horizontal, you've got chat GPT and other products which are vertical.
[00:27:06] SPEAKER_01: We haven't even talked about pixel, so I'll just just language.
[00:27:09] SPEAKER_01: Are agents in new modality? Is that something else?
[00:27:12] SPEAKER_01: Like, you know, like codex or what do you mean by modality?
[00:27:17] SPEAKER_01: Like, um, and they feel both vertical and horizontal to me in a way.
[00:27:22] SPEAKER_01: Like to me, chat GPT is a product, right?
[00:27:25] It's like it's a product and like my mom uses it, right?
[00:27:27] SPEAKER_01: And an API is a dev thing.
[00:27:30] SPEAKER_01: You kind of give it to a developer and like a CLI is kind of somewhere in between to me.
[00:27:34] SPEAKER_01: Is it a product? Is it like it is horizontal?
[00:27:37] SPEAKER_01: Yeah.
[00:27:38] SPEAKER_01: How is it handled internally?
[00:27:40] SPEAKER_01: Is it a totally separate team that does agents or no?
[00:27:43] So it's um, yeah, it's interesting because like I think the way that I, the way that you frame it just now almost seen like agents was like this like singular concept that like, you know, might, or like might have its own particular.
[00:27:55] SPEAKER_00: Maybe a better question. What is an agent to you?
[00:27:58] SPEAKER_01: Yeah, yeah, yeah, yeah.
[00:27:59] SPEAKER_01: Even getting a language is like important for the conversation.
[00:28:03] SPEAKER_01: So I don't actually don't even know if you're helpful for me to share about my general take on agents is it's a, it's an AI that will take actions on your behalf that can work over long time prizes.
[00:28:12] SPEAKER_00: Okay.
[00:28:13] SPEAKER_00: And I think that's the, that's the more pretty general.
[00:28:15] SPEAKER_00: Military.
[00:28:16] SPEAKER_00: But like if you think about it that way, yeah, I mean, maybe this is what you mean by modality, but it is just a like way of like using AI.
[00:28:24] SPEAKER_00: And it is a, I guess it could be viewed as a modality, but we don't view it as like a separate thing separate from.
[00:28:29] SPEAKER_00: Well, let me just, let me just try and kind of, you know, give you a sense of where this question is coming from.
[00:28:35] SPEAKER_01: Like I know how to build a product like, and we know how to do go to market for products.
[00:28:38] SPEAKER_01: We know how to do like, you know, we know the implications of turning them into platforms.
[00:28:43] SPEAKER_01: Like it's just we've been doing this for a very long time, right?
[00:28:46] SPEAKER_01: We know how to do the same thing for APIs, right?
[00:28:48] SPEAKER_01: We know how to do billing, you know, like the tension of like people build on top of it and all of that stuff.
[00:28:53] SPEAKER_01: And like what I've been trying to, and this is just maybe a personal inquiry, it's just not clear for me for an agent.
[00:29:00] SPEAKER_01: If you, if it sits in one of those two camps, is it more like the product camp?
[00:29:04] SPEAKER_01: Is it more like the, or is it because it's kind of both.
[00:29:09] SPEAKER_01: Like I could like literally give you code.
[00:29:11] SPEAKER_01: Yeah.
[00:29:12] SPEAKER_01: As a user, and then you just talk to it, or I could like build in a way kind of embed it in like my app.
[00:29:19] SPEAKER_01: And so like, but then that means something to you as far as like, you know, how do you price it?
[00:29:24] SPEAKER_01: And what does it mean for ecosystem?
[00:29:25] SPEAKER_01: Like, for example, like would you be fine if I started a company and just I built it around codex?
[00:29:29] SPEAKER_01: Is that a thing?
[00:29:30] SPEAKER_01: Starting company and billing it around codex?
[00:29:33] SPEAKER_00: Yeah.
[00:29:34] SPEAKER_00: I actually think that would be great.
[00:29:35] SPEAKER_00: Like it's a, we like release like the codex SDK and we like want people to be able to build it in and hack on it.
[00:29:39] SPEAKER_00: Yeah. Actually, I think this might be what you're getting at, which is, and this is like a kind of a unique thing about OpenAI.
[00:29:45] SPEAKER_00: And it kind of reflects on how it's run, which is at the end, like at the end of the day, OpenAI is like an AGI company.
[00:29:51] SPEAKER_00: It's like an intelligence company.
[00:29:52] SPEAKER_00: And so agents are just like one way in which this intelligence kind of manifested.
[00:29:56] SPEAKER_00: And so the way that I'd say we actually think about internally is all of our different product lines,
[00:30:01] SPEAKER_00: sore, codex, API, chat, GPT are just different interfaces and different ways of deploying this.
[00:30:06] SPEAKER_00: So you don't really need to.
[00:30:07] SPEAKER_00: So there's no like single things like this is, you know, like thinking about agents.
[00:30:10] SPEAKER_00: I would say the way that it manifests itself more is like each product area thinks about like what is, you know,
[00:30:15] SPEAKER_00: this intelligence is actually turning into a form where like you can actually,
[00:30:18] SPEAKER_00: Agentec behavior is more possible.
[00:30:20] SPEAKER_00: What would that look like in a first party product like chat GPT?
[00:30:23] SPEAKER_00: What would that look like?
[00:30:24] SPEAKER_00: This is actually why codex ended up becoming its own products.
[00:30:26] SPEAKER_00: Like what would it look like in a coding style product?
[00:30:28] SPEAKER_00: Yeah.
[00:30:29] SPEAKER_00: Like we explored it in chat GPT, like kind of worked there, but like actually the client interface actually makes a lot more sense.
[00:30:33] SPEAKER_00: That's another interface to deploy it.
[00:30:35] SPEAKER_00: And then if you look about the API itself, it's like this is another interface to deploy it.
[00:30:39] SPEAKER_00: It's, you're thinking about it in a slightly different way because the developer first mindset
[00:30:42] SPEAKER_00: we're helping other people build it.
[00:30:44] SPEAKER_00: The pricing is slightly different, but it's all these like different manifestations of this core like intelligence.
[00:30:49] SPEAKER_00: That is the the agent behavior.
[00:30:51] SPEAKER_00: It is so remarkable how much of this entire economy is basically just token laundering.
[00:30:55] SPEAKER_01: That's right.
[00:30:56] SPEAKER_01: I think I can do to get like like English or like a natural language in and then like, you know,
[00:31:03] SPEAKER_01: the intelligence out.
[00:31:05] SPEAKER_01: I mean, and it's because these are so resistant to layering.
[00:31:09] SPEAKER_01: It's so hard to layer a language out like, you know, like, I could even do it easily, pretty easily with like codex.
[00:31:14] SPEAKER_01: I could just like use it, you know, as a component of a program and just, you know, basically longer intelligence.
[00:31:20] SPEAKER_01: I mean, of course, you know, I'd be charged to do that.
[00:31:22] SPEAKER_01: So I actually, my view of this and having seen now so many kind of launches of different products.
[00:31:27] SPEAKER_01: I've seen agent launches in the definition that you have of, definitely seen APIs.
[00:31:31] SPEAKER_01: And I've seen products on these as like, they're actually quite different than like what were you used to?
[00:31:39] SPEAKER_01: Like the cogs is different.
[00:31:41] SPEAKER_01: The defensibility is different.
[00:31:42] SPEAKER_01: So they were kind of rewriting it.
[00:31:44] SPEAKER_01: And so it's kind of like, you know, you came from a kind of pricing background.
[00:31:49] SPEAKER_01: I mean, you're working on it.
[00:31:50] SPEAKER_01: No, no, no, no.
[00:31:51] SPEAKER_01: It's pricing. Now you have the API.
[00:31:52] SPEAKER_01: So I just love your thoughts on like, I mean, how how have you evolved your thinking on how do you price these, you know, access to intelligence?
[00:32:00] SPEAKER_01: Where, you know, you don't know how many people can use it.
[00:32:04] SPEAKER_01: It's almost certainly usage based billing.
[00:32:06] SPEAKER_01: Yeah.
[00:32:07] SPEAKER_01: Something else like, can you talk about just a bit about like philosophy around pricing on these things?
[00:32:11] SPEAKER_01: Is it different for product for SAPI?
[00:32:13] SPEAKER_01: Yeah. I think the, the, the, the honest right there is like, it's evolved over time as well.
[00:32:18] SPEAKER_00: And like, I actually think the simplest, like the reason why we've done usage based pricing on the API, honestly, is because it's been like, it's closest to how it's actually being used.
[00:32:26] SPEAKER_00: And so that's kind of how we, how we started.
[00:32:29] SPEAKER_00: I actually think usage based pricing on the API has has has like surprisingly held strong and like, I actually think this might be something that we'll keep doing for quite a long time.
[00:32:38] SPEAKER_00: Mostly because the cogs are so high, I don't know how you don't do usage based.
[00:32:42] SPEAKER_01: Yeah, yeah, yeah, yeah.
[00:32:43] SPEAKER_01: Just don't know how that, yeah.
[00:32:44] SPEAKER_01: And then, and then there's also the strategy of like how we price it.
[00:32:47] SPEAKER_00: And, and internally one thing we do is, is we always make sure that we actually price our, our usage based pricing from a like cosplay perspective.
[00:32:54] SPEAKER_00: Like when we're actually just like trying to make sure that we're being responsible for making some of our perspective.
[00:32:59] SPEAKER_00: But I mean, this is a huge shift in the industry in general just because like I remember the shift from on prem to, to recurring.
[00:33:05] SPEAKER_01: Yeah, that was a big, big deal. Like that created Zora, like a like created whole company.
[00:33:09] SPEAKER_01: Yeah, yeah, yeah.
[00:33:10] SPEAKER_01: And like, like consultants on how you do this to change like, you know, and like, I think the shift to, to usages is as bigger, bigger.
[00:33:18] SPEAKER_01: And it's also a really hard technical problem.
[00:33:20] SPEAKER_01: Yeah.
[00:33:21] SPEAKER_01: I can't even imagine 800 million.
[00:33:24] SPEAKER_01: Wow, like how do you build?
[00:33:26] SPEAKER_01: Yeah, well, well, 800 million.
[00:33:27] SPEAKER_01: Wow is a little easier because it's, it's not usage based pricing.
[00:33:30] SPEAKER_00: It's subscription.
[00:33:31] SPEAKER_00: So it's like, that was like, wait, wait, that's way, but I mean, there's still like a, like a lot of users on the API that we need to like, you know, manage all the building side.
[00:33:38] SPEAKER_00: There's some like overages or stuff you've got to deal with on that or what do you mean by overages? Like, I don't know.
[00:33:43] SPEAKER_00: I guess, I don't know what kind of like, you know, like max.
[00:33:47] SPEAKER_00: That's because that we don't let people go over, but like in practice, these quotas are like pretty, pretty massive.
[00:33:51] SPEAKER_00: That would literally be like one of the most complex systems somebody's ever built of you would do who usage based on that scale.
[00:33:56] SPEAKER_01: I mean, these are very, very, very, and like, you have to be correct.
[00:33:58] SPEAKER_01: Like, these are very hard systems to scale.
[00:34:00] SPEAKER_01: Yep, yep, yep, yeah.
[00:34:01] SPEAKER_00: Yeah, I mean, we have a whole team thing about this now internally.
[00:34:04] SPEAKER_00: Yeah, I mean, usage for pricing is also interesting.
[00:34:06] SPEAKER_00: So there's a, we required this company called Roxette a while ago a founder of his name is Vencott.
[00:34:12] SPEAKER_00: He's very interesting.
[00:34:13] SPEAKER_00: And now awesome.
[00:34:14] SPEAKER_00: Thank God it's awesome.
[00:34:15] SPEAKER_00: Awesome credible.
[00:34:16] SPEAKER_01: He's one of the best, like Ben kind of you're listening,
[00:34:18] SPEAKER_01: we're huge hands.
[00:34:18] SPEAKER_01: I mean, I'm a huge fan.
[00:34:19] SPEAKER_01: He's gonna love this.
[00:34:21] SPEAKER_00: So he's great.
[00:34:22] SPEAKER_00: And he's a legend.
[00:34:23] SPEAKER_00: Anyways, I was talking to him about pricing as well.
[00:34:25] SPEAKER_00: And his take is that pricing is kind of like a one way
[00:34:29] SPEAKER_00: ratchet.
[00:34:29] SPEAKER_00: And like basically once you get a taste of usage based pricing,
[00:34:32] SPEAKER_00: you're never gonna go back to like the per se,
[00:34:34] SPEAKER_00: like per se, like per deployment.
[00:34:36] SPEAKER_00: Pricing and then that's definitely true.
[00:34:38] SPEAKER_00: And I think it's just because it's getting,
[00:34:39] SPEAKER_00: it gets closer and closer to like your true utility,
[00:34:41] SPEAKER_00: you're getting all this thing.
[00:34:42] SPEAKER_00: The main pain point is like you have to maintain
[00:34:44] SPEAKER_00: all this info.
[00:34:45] SPEAKER_00: Yeah, to like get it to.
[00:34:46] SPEAKER_00: Super.
[00:34:47] SPEAKER_00: But if you do have it, he thinks it's like a one way
[00:34:48] SPEAKER_00: ratchet where like there's just like no, no going back.
[00:34:51] SPEAKER_00: And then and I think the hot new thing now is like,
[00:34:53] SPEAKER_00: oh, with AI, you can now kind of measure like outcomes.
[00:34:55] SPEAKER_00: And so that's like another, you know, like step forward.
[00:34:57] SPEAKER_00: And if that works, like maybe it's a one way ratchet.
[00:35:00] SPEAKER_00: So we thought about that is like, you know,
[00:35:02] SPEAKER_00: is there some type of like outcome based pricing?
[00:35:03] SPEAKER_00: This is more on the first party side on an APS kind of,
[00:35:06] SPEAKER_00: yeah, that's a measure.
[00:35:07] SPEAKER_01: That's very hard.
[00:35:08] SPEAKER_01: I mean, that's hard because you end up having to price
[00:35:12] SPEAKER_01: and value non computer science infrastructure, right?
[00:35:15] SPEAKER_01: Like literally going into verticalization now.
[00:35:17] SPEAKER_01: Like you're like, I mean, listen, if it's like
[00:35:20] SPEAKER_01: porting a code base, maybe you'd have some expertise,
[00:35:22] SPEAKER_01: but if it's like whatever, like increasing crop yields.
[00:35:25] SPEAKER_01: Yeah, yeah.
[00:35:26] SPEAKER_01: You're like, you're so level.
[00:35:27] SPEAKER_01: You need to like, but there could be a world where like the AI
[00:35:30] SPEAKER_00: is like, I don't know where I can like actually, you know,
[00:35:31] SPEAKER_00: make judgments of these and do it in an accurate enough way.
[00:35:34] SPEAKER_00: We're going tied to, to billing.
[00:35:35] SPEAKER_00: I think this is a problem with AI conversations.
[00:35:37] SPEAKER_01: Cause like at any point in time, you're like,
[00:35:38] SPEAKER_01: but it could get good.
[00:35:40] SPEAKER_01: Yeah, yeah.
[00:35:41] SPEAKER_01: It's not a problem anymore.
[00:35:42] SPEAKER_01: Yeah, yeah.
[00:35:43] SPEAKER_01: At some point it'll be so.
[00:35:44] SPEAKER_01: It's so much like the front engineering and the single
[00:35:46] SPEAKER_01: AGI I think before.
[00:35:48] SPEAKER_01: Yeah.
[00:35:48] SPEAKER_01: Yeah.
[00:35:49] SPEAKER_00: It's like when you reach that level of,
[00:35:50] SPEAKER_00: when you push it that far, everything's
[00:35:52] SPEAKER_00: hand assault on outcome based pricing, it sounds very appealing.
[00:35:56] SPEAKER_00: Like if it can work and it can work.
[00:35:57] SPEAKER_00: But one thing that we've started realizing is it actually ends up
[00:36:02] SPEAKER_00: correlating quite a bit with uses based pricing, especially
[00:36:04] SPEAKER_00: with test time compute.
[00:36:05] SPEAKER_00: Like if the thing is just like thinking quite a bit like actually,
[00:36:08] SPEAKER_00: you know, if you charge just by usage race,
[00:36:10] SPEAKER_00: usage based and not outcome based,
[00:36:12] SPEAKER_00: you're like basically approximating outcome based at this point.
[00:36:15] SPEAKER_00: If the thing is like thinking for like so long,
[00:36:17] SPEAKER_00: it's like highly correlated with with what it's doing.
[00:36:19] SPEAKER_00: It's exciting more value.
[00:36:20] SPEAKER_00: Yeah, exactly.
[00:36:21] SPEAKER_00: Exactly.
[00:36:22] SPEAKER_00: And so like maybe at the end of the day,
[00:36:23] SPEAKER_00: like uses based pricing, all you need.
[00:36:24] SPEAKER_00: And so like we're just going to like, you know,
[00:36:26] SPEAKER_00: live in this in this world forever.
[00:36:28] SPEAKER_00: But yeah, I don't know.
[00:36:29] SPEAKER_00: It's constantly evolving, I think our chain,
[00:36:32] SPEAKER_00: our thinking has evolved here as well.
[00:36:34] SPEAKER_00: I personally am like keeping track of if the outcome based pricing
[00:36:38] SPEAKER_00: setups can actually work here.
[00:36:40] SPEAKER_00: But at least on the API side, I think, you know,
[00:36:42] SPEAKER_00: it's such a usage based setup.
[00:36:43] SPEAKER_00: We have to get infrastructure around this.
[00:36:45] SPEAKER_00: And so I think we'll probably stay with that for a while.
[00:36:46] SPEAKER_00: So how do you think about open source?
[00:36:48] SPEAKER_01: I mean, you know, I think you're the only big lab
[00:36:51] SPEAKER_01: that's releasing open sources at Google has some of theirs.
[00:36:55] SPEAKER_00: Okay.
[00:36:55] SPEAKER_00: Yeah, it's mostly smaller models on their side.
[00:36:57] SPEAKER_01: Yeah, yeah, yeah.
[00:36:58] SPEAKER_00: So how do you think about open source vis-a-vis,
[00:37:01] you know, competition, capitalization, you know,
[00:37:04] SPEAKER_01: like what's the strategic goal?
[00:37:07] SPEAKER_01: What's the complexity?
[00:37:09] SPEAKER_01: Yeah.
[00:37:10] SPEAKER_00: So I personally love open source.
[00:37:14] SPEAKER_00: Like I think it's great that there's a-
[00:37:15] SPEAKER_00: All of us grew up with it, right?
[00:37:16] SPEAKER_00: Yeah, all of us grew up with it.
[00:37:17] SPEAKER_00: Like the internet wouldn't exist without it.
[00:37:19] SPEAKER_00: Like, you know, so much of the world's built in half of it.
[00:37:21] SPEAKER_00: Cloud wouldn't exist without it.
[00:37:23] SPEAKER_00: Yeah, I think it would exist without it.
[00:37:25] SPEAKER_00: Yeah.
[00:37:25] SPEAKER_00: For maybe Windows.
[00:37:26] SPEAKER_01: And so it was interesting because like I felt like
[00:37:28] SPEAKER_00: over the last years before we launched the open source model,
[00:37:30] SPEAKER_00: I know Sam feels the same as well.
[00:37:31] SPEAKER_00: It's like there's this like weird like, you know,
[00:37:35] SPEAKER_00: mindset where because opening I hadn't launched anything,
[00:37:37] SPEAKER_00: you just seemed like it was super like anti-
[00:37:39] SPEAKER_00: like opening I was like super anti open source.
[00:37:42] SPEAKER_00: Yeah.
[00:37:43] SPEAKER_00: But I'd actually been having conversations with Sam
[00:37:44] SPEAKER_00: ever since I joined about open sourcing a model.
[00:37:46] SPEAKER_00: We were trying to think about like,
[00:37:47] SPEAKER_00: well, how can we sequence it?
[00:37:49] SPEAKER_00: What compute is always a hard thing?
[00:37:50] SPEAKER_00: Is like, do we have the compute to kind of like train this thing?
[00:37:53] SPEAKER_00: Yeah.
[00:37:54] SPEAKER_00: So we've always wanted to kind of do this.
[00:37:54] SPEAKER_00: I'm really glad that we were able to finally do it.
[00:37:57] SPEAKER_00: I think was early, was it earlier this year?
[00:37:59] SPEAKER_00: Mm-hmm.
[00:38:00] SPEAKER_00: Like, lost us at time.
[00:38:01] SPEAKER_00: AI time is so good.
[00:38:02] SPEAKER_00: Yeah, I was like, was the last year, no, is this year.
[00:38:04] SPEAKER_01: Yeah, when GTO SS came out.
[00:38:05] SPEAKER_01: Yeah.
[00:38:06] SPEAKER_00: And so I was just really glad that we did that.
[00:38:09] SPEAKER_00: The way that I generally think about it is one,
[00:38:11] SPEAKER_00: I think as a, this is also particularly true for OpenAI
[00:38:16] SPEAKER_00: because as you said, we are a vertical and a horizontal company.
[00:38:18] SPEAKER_00: It's like, we want to continue investing in the ecosystem
[00:38:21] SPEAKER_00: and just from like brand perspective, I think it's good.
[00:38:23] SPEAKER_00: But then also, I think from OpenAI perspective,
[00:38:28] SPEAKER_00: if the AI ecosystem grows more and more,
[00:38:30] SPEAKER_00: it's like arising in terms of itself.
[00:38:32] SPEAKER_00: And like, yeah, it's all like really helpful for us.
[00:38:35] SPEAKER_00: And if we can launch an open source model
[00:38:37] SPEAKER_00: and it helps unlock a whole bunch of other use cases
[00:38:39] SPEAKER_00: in the other industries, I think that's actually not good for us.
[00:38:43] SPEAKER_00: I'll say what people talk about a lot is like,
[00:38:46] SPEAKER_01: how well these open source AI business models actually work?
[00:38:50] SPEAKER_01: Because this is very, like the Kennel or LayZation risk
[00:38:53] SPEAKER_01: is actually very low.
[00:38:56] SPEAKER_01: And like, you don't really enable competitors a lot
[00:38:58] SPEAKER_01: because I mean, when we say open source,
[00:38:59] SPEAKER_01: you really mean open weights, right?
[00:39:00] SPEAKER_01: It's not like they could recreate it.
[00:39:02] SPEAKER_01: Right, you know?
[00:39:03] SPEAKER_01: And like, I can distill your APIs as well
[00:39:05] SPEAKER_01: as I can distill, like you giving me the weights in some way.
[00:39:07] SPEAKER_01: Like, and so it doesn't really change that dynamic a lot.
[00:39:10] SPEAKER_01: But yeah, I mean, to be clear,
[00:39:12] SPEAKER_00: like we have not seen Kennel or LayZation at all.
[00:39:14] SPEAKER_00: Yeah, of course not.
[00:39:15] SPEAKER_00: I mean, it seems like a very different set of use cases.
[00:39:18] SPEAKER_00: The customers tend to be like slightly different.
[00:39:20] SPEAKER_00: The use cases are very different.
[00:39:23] SPEAKER_00: And by the way, it turns out inference is super hard.
[00:39:24] SPEAKER_01: Like to actually have like stable, fast performance.
[00:39:27] SPEAKER_01: Yeah, that's a hard, hard problem.
[00:39:29] SPEAKER_00: Yeah, so like, I'd say the way that I personally think
[00:39:31] SPEAKER_00: about open source in relation to the API business
[00:39:33] SPEAKER_00: in particular is, well, one,
[00:39:34] SPEAKER_00: it hasn't shown Kennel or risk.
[00:39:36] SPEAKER_00: So, you know, I'm not particularly worried about that.
[00:39:39] SPEAKER_00: But also like, especially for all these major labs,
[00:39:41] SPEAKER_00: like they're usually like two or three models
[00:39:42] SPEAKER_00: where like that is where you're making
[00:39:44] SPEAKER_00: all of your impact, all of your revenue.
[00:39:46] SPEAKER_00: And those are the ones where we're throwing
[00:39:47] SPEAKER_00: a bunch of resources into improving the model
[00:39:49] SPEAKER_00: and these tend to be the larger ones
[00:39:51] SPEAKER_00: that are like extremely hard to inference.
[00:39:53] SPEAKER_00: We have a really cracked inference team at OpenAI.
[00:39:55] SPEAKER_00: And so my sense is like, even if we just like,
[00:39:57] SPEAKER_00: you know, open source, like if we just literally open source
[00:40:00] SPEAKER_00: to GPD5 or something,
[00:40:02] SPEAKER_00: it would be really, really hard to inferncy it
[00:40:03] SPEAKER_00: at the level that we are able to get it to do.
[00:40:06] SPEAKER_00: There's also, by the way, like feedback loop
[00:40:08] SPEAKER_00: between the inference team, like the training team too,
[00:40:10] SPEAKER_00: so like we can kind of like open source all of that.
[00:40:12] SPEAKER_01: Can you, like, is it possible to verticalize models
[00:40:14] SPEAKER_00: for products?
[00:40:16] I have trained models specifically for products.
[00:40:18] SPEAKER_00: Yeah, I mean, to actually, yeah.
[00:40:21] SPEAKER_00: I think, I mean, we've kind of done this
[00:40:22] SPEAKER_00: with GPD5 codex, right?
[00:40:24] SPEAKER_00: Or do you mean like even more verticalization?
[00:40:26] SPEAKER_00: I mean, like deep, deep, deep verticalization
[00:40:28] SPEAKER_01: where like, you know, like the, like the,
[00:40:31] SPEAKER_01: the released model wouldn't, you know,
[00:40:33] SPEAKER_01: it's like actually part of a product.
[00:40:36] SPEAKER_01: I think we're like basically starting to move
[00:40:39] SPEAKER_00: in that direction.
[00:40:41] SPEAKER_00: I think there's a question of how deeply you verticalize it.
[00:40:44] SPEAKER_00: I think most of what we've done is mostly at like the post
[00:40:46] SPEAKER_00: training, like the tool use level.
[00:40:48] SPEAKER_00: Like codex is particularly good at using the,
[00:40:50] SPEAKER_00: sorry, GPD5 codex, particularly good at using the codex harness.
[00:40:54] SPEAKER_00: But there's like even deeper verticalization you can do,
[00:40:57] SPEAKER_00: like that one, I think it's more of an open source.
[00:40:59] SPEAKER_00: Yeah, so like a lot of my,
[00:41:00] SPEAKER_01: I mean, a lot of my mental model,
[00:41:01] SPEAKER_01: this comes from the pixel space, which is like, you,
[00:41:05] SPEAKER_01: you know, you can lower a bunch of image models, right?
[00:41:11] SPEAKER_01: And you can, you can do a bunch of stuff
[00:41:12] SPEAKER_01: to make it better and more suitable for some products,
[00:41:14] SPEAKER_01: for example.
[00:41:16] SPEAKER_01: But like these open source models are really, really good.
[00:41:20] SPEAKER_01: And like, you would believe that you could like,
[00:41:23] SPEAKER_01: verticalize a model for like editing
[00:41:25] SPEAKER_01: or cutting paste or this or that, you know,
[00:41:26] SPEAKER_01: like that's actually part of this.
[00:41:28] SPEAKER_01: So you actually don't see that happen.
[00:41:30] SPEAKER_01: Yeah, it's almost always like you're just kind of exposing
[00:41:34] SPEAKER_01: like a model, not something like specific to a product.
[00:41:37] SPEAKER_01: Yeah, I think, I think, so I think there's a distinction to be made
[00:41:39] SPEAKER_00: between the, like the image model space and the text model space.
[00:41:42] SPEAKER_00: Yeah, but also because the image models tend to be way smaller
[00:41:45] SPEAKER_00: and like you can iterate on it a lot faster.
[00:41:46] SPEAKER_00: Like that's why you got that crazy cool
[00:41:48] SPEAKER_00: proliferation of like an image model side.
[00:41:50] SPEAKER_00: Whereas like, I don't know, for the text models,
[00:41:53] SPEAKER_00: there's always going to be this like really big
[00:41:54] SPEAKER_00: that free training step that like you have invested in.
[00:41:56] SPEAKER_00: And then even the post training side is like, you know,
[00:41:58] SPEAKER_00: it's not that it's not like the easiest thing.
[00:42:00] SPEAKER_00: Like it's, you know, we all like just from a compute perspective,
[00:42:04] SPEAKER_00: obviously it's much smaller, but like it's still pretty heavy
[00:42:06] SPEAKER_00: to do like a full mid train or like a post training run.
[00:42:08] SPEAKER_00: And so I actually think like that's one of the bigger,
[00:42:10] SPEAKER_00: bigger bottlenecks because I think you're,
[00:42:13] SPEAKER_00: you're, you are right that like on the image side, yeah,
[00:42:15] SPEAKER_00: you can like fine tune a like image, if you're small,
[00:42:18] SPEAKER_00: to be like extremely good at like editing faces.
[00:42:20] SPEAKER_00: Yeah, like, you know, like something very specific
[00:42:21] SPEAKER_00: of the product around that.
[00:42:22] SPEAKER_00: And it's like, yeah, you can just kind of put all these
[00:42:24] SPEAKER_00: resources into it and iterate on that one specific model.
[00:42:26] SPEAKER_00: Whereas it's much, it's a much heavier motion.
[00:42:28] SPEAKER_00: I think that on the text side, I got to say,
[00:42:31] SPEAKER_01: it is a bit of an anti pattern to do both languages,
[00:42:35] SPEAKER_01: like language based models and diffusion,
[00:42:37] SPEAKER_01: like pixel models in the same company, like most that have tried,
[00:42:41] SPEAKER_01: like it's found a very clunky to do it.
[00:42:44] SPEAKER_01: But I mean, you and Google are the two kind of counter examples
[00:42:48] SPEAKER_01: for this. And so like, is it possible to even like
[00:42:51] SPEAKER_01: converge the infrastructures on these things?
[00:42:53] SPEAKER_01: Like, I mean, is it totally different orgs?
[00:42:56] SPEAKER_01: Is it shared infrastructure?
[00:42:57] SPEAKER_01: Like, yeah, how do you operationalize?
[00:42:59] SPEAKER_00: Yeah, I think, I think it totally writes an anti pattern.
[00:43:02] SPEAKER_00: It's pretty tough to pull off.
[00:43:05] SPEAKER_00: I think honestly, like props to mark on our research team
[00:43:07] SPEAKER_00: for like, you know, structuring things in a way we're,
[00:43:10] SPEAKER_00: we're able to do it.
[00:43:11] SPEAKER_00: For my perspective, I think the biggest thing is I think
[00:43:13] SPEAKER_00: are like image, like our,
[00:43:16] SPEAKER_00: I think all like the world simulation team,
[00:43:18] SPEAKER_00: like the team up builds Sora and all that under Dittia.
[00:43:21] SPEAKER_00: It's just extremely solid.
[00:43:23] SPEAKER_00: Like they are probably it's like the highest concentration of like talent
[00:43:26] SPEAKER_00: that I've seen a while, but is it the same?
[00:43:29] SPEAKER_01: Is it the same?
[00:43:30] SPEAKER_01: Is it like, are they like totally separate infrastructure to these?
[00:43:32] SPEAKER_01: The same infrastructure?
[00:43:32] SPEAKER_01: Yeah, yeah, yeah.
[00:43:33] SPEAKER_01: So it's it's actually like pretty separate.
[00:43:35] SPEAKER_00: So and I think that's part of the reason why we're able to kind of do this.
[00:43:38] SPEAKER_00: Well, it's like one is like, the team needs to be extremely strong,
[00:43:39] SPEAKER_00: which which they are.
[00:43:40] SPEAKER_00: And then two is they're they're they're they're run very separately.
[00:43:43] SPEAKER_00: They're kind of like thinking about their own particular roadmap.
[00:43:46] SPEAKER_00: They think about productization very separately as well, right?
[00:43:49] SPEAKER_00: Which is how like the Sora app kind of came came came out of that as well.
[00:43:53] SPEAKER_00: And then yeah, even like the inference stacks are are slightly different,
[00:43:56] SPEAKER_00: are kind of like different.
[00:43:58] SPEAKER_00: They they they own a lot more around their inference stack and they
[00:44:01] SPEAKER_00: optimize their inference stack pretty pretty separately.
[00:44:03] SPEAKER_00: And so maybe you get that that contributes to helping us run things in RL,
[00:44:08] SPEAKER_00: but it's it's pretty hard to pull off for sure.
[00:44:10] SPEAKER_00: Maybe maybe you can educate this on me like, so I think about APIs as mostly text
[00:44:15] SPEAKER_01: based from opening.
[00:44:16] SPEAKER_01: I do guys do actual do you do actual?
[00:44:18] SPEAKER_01: Yeah, so they stuff.
[00:44:18] SPEAKER_01: Yeah, yeah, we do we have a bunch.
[00:44:20] SPEAKER_00: So dolly dolly, of course, in the API, the OG model, dolly,
[00:44:26] SPEAKER_00: two is in the API dolly.
[00:44:27] SPEAKER_00: I was like the first real text image.
[00:44:28] SPEAKER_01: All right.
[00:44:29] SPEAKER_01: Yeah, yeah, yeah.
[00:44:30] SPEAKER_00: That was actually the model that got me to go to open AI because the summer when I was
[00:44:34] SPEAKER_00: looking for, I was thinking about something new.
[00:44:36] SPEAKER_00: It's when dolly two came out and it just completely blew my mind.
[00:44:39] SPEAKER_00: Wow.
[00:44:40] SPEAKER_00: And I distinctly remember I was like asking it to do the simplest thing like draw picture
[00:44:43] SPEAKER_00: of a duck or something.
[00:44:44] SPEAKER_00: There's like the simplest thing now.
[00:44:46] SPEAKER_00: And it's like it generated a picture of a white duck.
[00:44:49] SPEAKER_00: And so that was actually the thing that kind of got me to open and the first place.
[00:44:54] SPEAKER_00: But yeah, we have a bunch in our in our API, the image gen model as well as in our API.
[00:44:59] SPEAKER_00: And then so or two is in our API we launched that dev days.
[00:45:01] SPEAKER_00: Actually been a huge hit.
[00:45:02] SPEAKER_00: I've been very, very surprised.
[00:45:04] SPEAKER_00: Neymar GPUs for that.
[00:45:06] SPEAKER_00: But the amount of use cases.
[00:45:08] SPEAKER_00: And then from your standpoint, like you can converge that like the API infrastructure
[00:45:12] SPEAKER_01: probably like that.
[00:45:13] SPEAKER_01: Yeah.
[00:45:13] SPEAKER_01: So there's yeah, I'd say on the API side, a lot of the infrastructure is shared for
[00:45:17] SPEAKER_00: those.
[00:45:18] SPEAKER_00: But once you reach the infinite level, they're separate right because you got to inference
[00:45:20] SPEAKER_00: them differently.
[00:45:21] SPEAKER_00: And it is that team that has just like been really laser focused on making that side
[00:45:25] SPEAKER_00: particularly efficient and yeah, and work well separate from the text models.
[00:45:31] SPEAKER_00: But yeah, we have image gen, we have video gen, and we'll continue adding more to the
[00:45:36] SPEAKER_00: API there.
[00:45:37] SPEAKER_01: So it feels like we've been evolving our thinking as an industry on a bunch of stuff.
[00:45:42] SPEAKER_01: Like one of them for sure is like the models like we've talked about.
[00:45:45] SPEAKER_01: The other one is like context engineering.
[00:45:47] SPEAKER_01: It seems to me that like actually how you build agents and expose them has evolved to
[00:45:51] SPEAKER_01: so maybe you can talk a bit about that.
[00:45:52] SPEAKER_01: Yeah.
[00:45:53] SPEAKER_01: Yeah, I think so at Dev Day this year when we launched our agent builder, I got a bunch
[00:45:57] SPEAKER_00: of questions around this because the agent builder is like the bunch of different nodes
[00:46:01] SPEAKER_00: and it's like the deterministic thing.
[00:46:03] SPEAKER_00: And I was like, oh, is this really like the future future agents?
[00:46:05] SPEAKER_00: And we obviously put a lot of thought into this when we were thinking about building that
[00:46:09] SPEAKER_00: product.
[00:46:10] SPEAKER_00: But the way I think about it is.
[00:46:11] SPEAKER_00: I think it came from a point of being constrained by the way, they're like, oh, this is too
[00:46:14] SPEAKER_01: constraining.
[00:46:15] SPEAKER_00: Yeah, I think people are like it's too constraining.
[00:46:17] SPEAKER_00: It's not like a GI forward.
[00:46:18] SPEAKER_00: I know.
[00:46:19] SPEAKER_00: I know.
[00:46:20] SPEAKER_00: I know that.
[00:46:21] SPEAKER_00: I know that at the end of the day, the AGI will do everything.
[00:46:22] SPEAKER_00: And so like why not?
[00:46:23] SPEAKER_00: Why have nodes in this like node builder thing?
[00:46:25] SPEAKER_00: Just tell them what to do.
[00:46:26] SPEAKER_00: Yeah.
[00:46:27] SPEAKER_00: And so I think there's like two things that play here.
[00:46:28] SPEAKER_00: One of them is like there is a like practicality components.
[00:46:31] SPEAKER_00: And then the other thing is I think they're actually like different types of work that exist
[00:46:34] SPEAKER_00: out there that could be automated into agents.
[00:46:36] SPEAKER_00: And so on the practicality side is yeah, like the models today just like maybe in some
[00:46:40] SPEAKER_00: future world instruction following would be so good that you just like ask it to do this
[00:46:45] SPEAKER_00: four step process.
[00:46:46] SPEAKER_00: And it like always does the four step process exactly.
[00:46:49] SPEAKER_00: We're still not there yet.
[00:46:50] SPEAKER_00: And in the meantime, you know, this entire industry being born and a lot of, you know, people
[00:46:54] SPEAKER_00: still want to use these models.
[00:46:55] SPEAKER_00: So what can you build for them?
[00:46:56] SPEAKER_00: So there's a practicality component of it.
[00:46:58] SPEAKER_00: When did you launch that?
[00:47:00] SPEAKER_01: Debt day.
[00:47:01] SPEAKER_00: So it feels like forever ago.
[00:47:04] SPEAKER_00: Earlier this month, October, it was like October 6th or something.
[00:47:07] SPEAKER_00: Yeah.
[00:47:08] SPEAKER_00: Yeah.
[00:47:09] SPEAKER_00: Yeah.
[00:47:10] SPEAKER_00: Okay.
[00:47:11] SPEAKER_00: It's been, it's been crazy seeing the reception to it by the way.
[00:47:16] SPEAKER_00: Like it's the, I think the video where Christina on my team demos, agent builders, like one
[00:47:20] SPEAKER_00: of the most viewed videos on our YouTube channel now.
[00:47:23] SPEAKER_00: I will say, I will say just anecdotally from kind of my perspective.
[00:47:26] SPEAKER_01: People love it.
[00:47:27] SPEAKER_01: That's great.
[00:47:28] SPEAKER_01: But I also saw the dissonance too.
[00:47:29] SPEAKER_01: Like I saw when I came here.
[00:47:30] SPEAKER_01: Yeah.
[00:47:31] SPEAKER_01: People were like, wait, what is this?
[00:47:32] SPEAKER_01: Exactly.
[00:47:33] SPEAKER_01: No code, no code.
[00:47:34] SPEAKER_00: Yeah, that's another low code thing.
[00:47:35] SPEAKER_00: I know people love it.
[00:47:36] SPEAKER_00: Yeah.
[00:47:37] SPEAKER_00: Yeah.
[00:47:38] SPEAKER_00: Yeah.
[00:47:39] SPEAKER_00: And we were talking to our customers.
[00:47:40] SPEAKER_00: We've realized that there's like, because at the end of the day, a lot of this, the agent
[00:47:44] SPEAKER_00: work is just trying to automate work and like what people do in their day to day jobs.
[00:47:47] SPEAKER_00: It's like, actually like two different types of work.
[00:47:50] SPEAKER_00: There's the work that we think about, which is like maybe what like software engineers
[00:47:53] SPEAKER_00: do, which is like, it's very undirected.
[00:47:54] SPEAKER_00: There's like a high level goal.
[00:47:56] SPEAKER_00: And then you have like, you know, you have your cursor and you're just like writing, writing
[00:47:59] SPEAKER_00: code.
[00:48:00] SPEAKER_00: And you're kind of like exploring things and going towards an objective.
[00:48:04] SPEAKER_00: That's like, I don't know, more like knowledge-based work.
[00:48:05] SPEAKER_00: Like data analysis, maybe like that, like coding is kind of like this.
[00:48:09] SPEAKER_00: But then there's another type of work, which is actually what we realize is like maybe
[00:48:12] SPEAKER_00: even more prevalent in industry than software.
[00:48:15] SPEAKER_00: We're just not aware of it, which is work tends to be very procedural, very like SOP-oriented.
[00:48:20] SPEAKER_00: Like customer support is a good example of this.
[00:48:22] SPEAKER_00: Like customer support, there's like very clear policy that these agents and people have
[00:48:25] SPEAKER_00: to follow.
[00:48:26] SPEAKER_00: And it is actually not great for them to deviate from this and like try something else.
[00:48:30] SPEAKER_00: It's like the team really, the people running these teams just really want the SOPs to
[00:48:34] SPEAKER_00: be followed.
[00:48:35] SPEAKER_00: And this pattern actually generalizes to do some different work.
[00:48:38] SPEAKER_00: Standard operating procedure.
[00:48:39] SPEAKER_00: Yeah, sorry.
[00:48:40] SPEAKER_00: So it's like the way in which you need to operate the support team.
[00:48:46] SPEAKER_00: But like this extensive like marketing, this extensive like sales, extensive like a bunch,
[00:48:50] SPEAKER_00: way more than it has any right to.
[00:48:52] SPEAKER_00: And what we realize is like there's a huge need on that side to have determinism here,
[00:48:56] SPEAKER_00: of which an agent builder with nodes that helps enforce this thing ends up being very,
[00:49:01] SPEAKER_00: very helpful.
[00:49:02] SPEAKER_00: But I think a lot of us especially in Silicon Valley don't really appreciate that there's
[00:49:04] SPEAKER_00: like a ton of work that actually falls into this camp.
[00:49:06] SPEAKER_00: I got to say like there's a pattern that's similar to this.
[00:49:09] SPEAKER_01: I'm wondering if you've seen it that I've seen where some regulated industries actually
[00:49:12] SPEAKER_01: can't let any generated content go to a user.
[00:49:15] SPEAKER_01: Yeah, right.
[00:49:16] SPEAKER_00: And so what they do is they get so interesting though like either pass in like a conversation
[00:49:23] SPEAKER_01: tree and that you can choose something from here.
[00:49:25] SPEAKER_01: Yeah.
[00:49:26] SPEAKER_00: So there's some human elements to it.
[00:49:28] SPEAKER_00: So it was part of the prompt.
[00:49:29] SPEAKER_01: They're like here are the viable things you can say choose which one to say.
[00:49:33] SPEAKER_01: So language reasoning has happened by the model, but nothing generated comes out.
[00:49:36] SPEAKER_01: Interesting.
[00:49:37] SPEAKER_00: Does that make sense?
[00:49:38] SPEAKER_00: Yeah.
[00:49:39] SPEAKER_01: And then another thing I've seen is like actual pseudocomp, some of that's like a Python
[00:49:42] SPEAKER_01: function.
[00:49:43] SPEAKER_00: And then we'll ask a human to like use the pseudocode to write actual code that makes it
[00:49:47] SPEAKER_00: in or.
[00:49:48] It actually has a response catalog as part of it and it has like the logic to apply and
[00:49:54] SPEAKER_01: then interesting.
[00:49:55] SPEAKER_01: And so like the model takes the language in from the human user and then well like you
[00:50:03] SPEAKER_01: know, the logic of how to respond is I can Python code because it just turns out that
[00:50:06] SPEAKER_01: like there's been a lot of code written for these types of things and then it actually
[00:50:10] SPEAKER_01: includes the responses that you would send out.
[00:50:12] SPEAKER_01: Does that make sense?
[00:50:13] SPEAKER_01: Actually a lot of NPCs are done this way.
[00:50:15] SPEAKER_01: Like actually did your game NPCs.
[00:50:16] SPEAKER_01: So yeah.
[00:50:17] SPEAKER_01: So because the way that I think about it is like, you know, so that way the with the
[00:50:21] SPEAKER_00: NPCs, it's the actual coding generated by the model is not what ends up making it to
[00:50:25] SPEAKER_00: the end user just to the.
[00:50:27] SPEAKER_00: That's it's not like the code is not being generated by the model.
[00:50:30] SPEAKER_01: It's the prompt has the code.
[00:50:31] SPEAKER_01: So like, so let's say that I have an NPC and want the NPC like let's say you're the
[00:50:37] SPEAKER_01: gamer.
[00:50:38] SPEAKER_01: And so you're coming in and you're talking to my NPC, but my NPC has some logic that it
[00:50:42] SPEAKER_01: needs to do.
[00:50:43] SPEAKER_01: Like if you say a certain thing, I'll give you a key or maybe a little barter.
[00:50:47] SPEAKER_01: Like describing the game logic in English just doesn't work.
[00:50:49] SPEAKER_01: Yeah.
[00:50:50] SPEAKER_01: Actually, if you try and do it and then like actually scripting the output doesn't work
[00:50:54] SPEAKER_01: either if you need to use it in a game context.
[00:50:56] SPEAKER_01: Like you would have to know like give like a specific direction or specific this and
[00:51:00] SPEAKER_01: that.
[00:51:01] SPEAKER_01: Well, how do you make these things behave in a more constrained way?
[00:51:04] SPEAKER_01: People pass in functions like they like to describe the logic and Python.
[00:51:09] SPEAKER_01: So like my prompt will be like you're an NPC in a video game.
[00:51:13] SPEAKER_01: The user just asked you a question.
[00:51:15] SPEAKER_01: Here's the logic you should go through.
[00:51:16] SPEAKER_01: If the user says this and do this is like the pseudocode like if the user has this,
[00:51:21] SPEAKER_01: you know, in the belt to do this like whatever, whatever, whatever.
[00:51:23] SPEAKER_01: And then here the set of valid responses.
[00:51:25] SPEAKER_01: And so you're almost constraining.
[00:51:27] SPEAKER_01: I see.
[00:51:28] SPEAKER_00: I see.
[00:51:29] SPEAKER_01: So if you guys do a response, you can you can validate that it's one of those responses.
[00:51:32] SPEAKER_01: I see.
[00:51:33] SPEAKER_01: It's like highly structured.
[00:51:34] SPEAKER_00: Yeah.
[00:51:35] SPEAKER_00: Yeah.
[00:51:36] SPEAKER_00: Okay.
[00:51:37] SPEAKER_00: So the NPC still only exists in that like the space that it can act in is still only within
[00:51:38] SPEAKER_00: the space of the program that you give.
[00:51:40] SPEAKER_01: Yeah.
[00:51:41] SPEAKER_01: Well, the logic is in there.
[00:51:42] SPEAKER_01: So it can have a normal conversation.
[00:51:44] SPEAKER_01: Yeah.
[00:51:45] SPEAKER_01: But like in as much as you're trying to guide the logic for like like like like game designer
[00:51:48] SPEAKER_01: game logic.
[00:51:49] SPEAKER_01: I see.
[00:51:50] SPEAKER_01: So you see this for the NPCs, but you also see this with regulated industries for that.
[00:51:53] SPEAKER_01: I literally can't have it like.
[00:51:54] SPEAKER_01: Yeah.
[00:51:55] SPEAKER_00: I was going to say what you described kind of sounds like, you know, giving the the SOPs
[00:51:58] SPEAKER_00: to like your set of human operators to like the stick to it.
[00:52:01] SPEAKER_00: Please say these three things and he was like the design.
[00:52:04] SPEAKER_00: And like you cannot give a refund if it's like less than this amount.
[00:52:06] SPEAKER_00: Yeah.
[00:52:07] SPEAKER_00: Yeah.
[00:52:08] SPEAKER_00: Yeah.
[00:52:09] SPEAKER_00: Very interesting.
[00:52:10] SPEAKER_00: Yeah.
[00:52:11] SPEAKER_00: I mean, I mean, yeah.
[00:52:12] SPEAKER_00: I don't want to quit them to NPCs, but like this is there's some very to some like.
[00:52:13] SPEAKER_00: I'm just saying it's actually like if you want if you want to really guarantee what happens,
[00:52:18] SPEAKER_01: you had there's like a set of techniques that you do.
[00:52:20] SPEAKER_01: And like there's some situations where you want to constrain what they do.
[00:52:23] SPEAKER_01: It could be from a regulatory standpoint.
[00:52:25] SPEAKER_01: It could be because you wanted to run for a long time.
[00:52:27] SPEAKER_01: And it also could because I actually have game logic and my game logic is a traditional
[00:52:30] SPEAKER_01: program like I have like a monetary system.
[00:52:33] SPEAKER_01: I have an item system.
[00:52:34] SPEAKER_01: I have a battle system like you can't describe that in English.
[00:52:37] SPEAKER_01: Like you have to kind of give it to them so it can behave within that.
[00:52:39] SPEAKER_01: Yes.
[00:52:40] SPEAKER_00: And that is exactly the problem.
[00:52:41] SPEAKER_00: I think we're trying to solve here.
[00:52:42] SPEAKER_00: That's awesome.
[00:52:43] SPEAKER_00: So like if you do not give it any of this, like you can just kind of go off and do whatever.
[00:52:46] SPEAKER_00: And yet they're like regular regulatory concerns around this.
[00:52:48] SPEAKER_00: Yeah.
[00:52:49] SPEAKER_00: And that is the exact use case that I think we're trying to target with Asian building.
[00:52:52] SPEAKER_00: It's awesome.
[00:52:53] SPEAKER_00: Well, so we're running out of time and there's a million more things I want to ask you.
[00:52:56] SPEAKER_01: But I really appreciate your time to come in.
[00:52:58] SPEAKER_01: It was a great kind of survey and like what's going on.
[00:53:01] SPEAKER_01: And particularly like teasing apart horizontal versus vertical in this page.
[00:53:05] SPEAKER_01: Yeah.
[00:53:06] SPEAKER_01: Which I really want to do.
[00:53:07] SPEAKER_01: So thank you so much.
[00:53:08] Yeah.
[00:53:09] Thank you.
[00:53:10] Yeah.
[00:53:11] Yeah.
[00:53:12] Yeah.
[00:53:13] Yeah.
[00:53:14] Yeah.
[00:53:15] Yeah.
[00:53:16] Yeah.
[00:53:17] Yeah.
[00:53:18] Yeah.
[00:53:19] Yeah.
[00:53:20] Yeah.
[00:53:21] Yeah.
[00:53:22] Yeah.
[00:53:23] Yeah.
[00:53:24] Yeah.
[00:53:25] Yeah.