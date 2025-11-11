# How Google’s Nano Banana Achieved Breakthrough Character Consistency

**Podcast:** Training Data
**Date:** 2025-11-11
**Video ID:** 5uutda-R0EY
**Video URL:** https://www.youtube.com/watch?v=5uutda-R0EY

---

[00:00:00] There's something about visual media that really excites people.
[00:00:03] SPEAKER_01: It's the fun thing, but it's not just fun.
[00:00:05] SPEAKER_01: It's exciting.
[00:00:07] SPEAKER_01: It's intuitive.
[00:00:09] SPEAKER_01: The visual space is so much of how we as humans experience life
[00:00:13] SPEAKER_01: that I think I've loved how much it's moved people.
[00:00:17] SPEAKER_01: I think we're really now making it possible to tell stories
[00:00:20] SPEAKER_00: that you never could.
[00:00:21] SPEAKER_00: And in a way, where the camera allowed anyone to capture reality
[00:00:25] SPEAKER_00: when it became very accessible, you're kind of capturing
[00:00:27] SPEAKER_00: people's imagination.
[00:00:29] SPEAKER_00: Like, you're giving them the tools to be able to get the stuff
[00:00:32] SPEAKER_00: that's in their brain, out of paper, visually in a way
[00:00:36] SPEAKER_00: that they just couldn't before because they didn't have the tools
[00:00:39] SPEAKER_00: or the knowledge of the tools.
[00:00:41] SPEAKER_00: That's been really awesome.
[00:00:42] SPEAKER_00: Today, we're talking with Nicole Britova and Hansa Srinivasan,
[00:01:03] SPEAKER_02: the team behind Google's Nano Banana Image Model, which
[00:01:06] SPEAKER_02: started as a 2am code name and has become a cultural phenomenon
[00:01:09] SPEAKER_02: since.
[00:01:10] SPEAKER_02: They walk us through the technical leaps that made
[00:01:12] SPEAKER_02: single image character consistency possible,
[00:01:15] SPEAKER_02: how high quality data, long multimodal context windows,
[00:01:19] SPEAKER_02: and disciplined human e-vails enabled
[00:01:21] SPEAKER_02: reliable character consistency from a single photo,
[00:01:25] SPEAKER_02: and why craft and infrastructure matter as much as scale.
[00:01:29] We discussed the trade-offs between pushing the frontier
[00:01:31] SPEAKER_02: versus broad accessibility and where this technology is headed,
[00:01:35] SPEAKER_02: multimodal creation, personalized learning,
[00:01:38] SPEAKER_02: and specialized UIs that marry fine-grained control
[00:01:41] SPEAKER_02: with hands-off automation.
[00:01:43] SPEAKER_02: Finally, we'll touch on what's still missing for true AGI
[00:01:46] SPEAKER_02: and white space where startups should be building now.
[00:01:49] SPEAKER_02: Enjoy the show.
[00:01:50] SPEAKER_02: NICOLE AND HONZA Thank you so much for joining us today.
[00:01:55] SPEAKER_02: We're so excited to be here at a chat a little bit more
[00:01:57] SPEAKER_02: about Nano Banana, which has taken the world by storm.
[00:02:00] SPEAKER_02: We thought we'd start off with a fun question.
[00:02:03] SPEAKER_02: What have been some of your own personal creations
[00:02:06] SPEAKER_02: using Nano Banana, or some of the most creative things
[00:02:08] SPEAKER_02: you've seen from the community?
[00:02:10] Yeah, so I think for me, one of the most exciting things
[00:02:14] SPEAKER_01: I've been seeing is like the...
[00:02:17] It didn't occur to me, but this is very obvious in hindsight
[00:02:19] SPEAKER_01: is the use with video models to get actually consistent,
[00:02:23] SPEAKER_01: cross-seeing character and scene preservation.
[00:02:28] SPEAKER_01: How fluid is that workflow today?
[00:02:30] SPEAKER_01: How hard is it to do that?
[00:02:31] SPEAKER_01: So what I've been seeing is people are really mixing the tools
[00:02:35] SPEAKER_01: and using different video models from different sources.
[00:02:38] SPEAKER_01: And so I think it's probably not very fluid.
[00:02:40] SPEAKER_01: I know some products out there that are trying to integrate
[00:02:43] SPEAKER_01: with multiple models to make this more fluid,
[00:02:45] SPEAKER_01: but I think the difference in the videos
[00:02:50] SPEAKER_01: I've been seeing from before and after
[00:02:52] SPEAKER_01: the Nano Banana launch has been pretty remarkable.
[00:02:55] SPEAKER_01: And it's much, much smoother and much more like what you'd want
[00:02:59] SPEAKER_01: in the video creating process with scene cuts that feel natural.
[00:03:03] SPEAKER_01: So that's been cool.
[00:03:04] SPEAKER_01: And I don't know why it didn't totally occur to me
[00:03:06] SPEAKER_01: that people would immediately do that.
[00:03:08] SPEAKER_01: But yeah.
[00:03:10] One of my favorite ways that I didn't expect
[00:03:13] SPEAKER_00: is how people have hacked around the model
[00:03:15] SPEAKER_00: to use it for learning new things or digesting information.
[00:03:19] SPEAKER_00: I met somebody last week who has been using
[00:03:22] SPEAKER_00: it to create sketch notes of these varied topics.
[00:03:26] SPEAKER_00: And it's surprising because text rendering
[00:03:28] SPEAKER_00: is not something that...
[00:03:29] SPEAKER_00: It's not where we want it to be,
[00:03:32] but this person has hacked around these massive prongs
[00:03:35] SPEAKER_00: that get the model to output something that's coherent.
[00:03:38] SPEAKER_00: And he's used it to try to understand the work
[00:03:42] SPEAKER_00: that his father's doing.
[00:03:43] SPEAKER_00: He was like, I missed at a university
[00:03:45] SPEAKER_00: and it's a super technical topic.
[00:03:47] SPEAKER_00: And so he's been feeding his lectures to Gemini
[00:03:50] SPEAKER_00: with Nano Banana and then getting these sketch notes
[00:03:53] SPEAKER_00: that are very coherent and visually digestible.
[00:03:56] SPEAKER_00: And for the first time, I think in decades,
[00:03:58] SPEAKER_00: they've been able to have a conversation with each other
[00:04:00] SPEAKER_00: about his dad's work.
[00:04:02] SPEAKER_00: And that was really fun.
[00:04:03] And something that I didn't see coming.
[00:04:05] SPEAKER_00: Yeah, I think people are really working around,
[00:04:09] SPEAKER_01: like this model is amazing, but obviously it's not perfect.
[00:04:12] SPEAKER_01: We have a lot of things we want to improve.
[00:04:14] SPEAKER_01: And I think I've been astounded by the ways
[00:04:15] SPEAKER_01: people have found to work with the model
[00:04:19] SPEAKER_01: in ways we didn't anticipate and give inputs to the models
[00:04:21] SPEAKER_01: in ways we didn't anticipate to bring out
[00:04:23] SPEAKER_01: the best performance and unlock these things
[00:04:26] SPEAKER_01: that are kind of mind-blowing.
[00:04:28] SPEAKER_03: Did you guys in the building of it
[00:04:31] was there a moment, like an aha moment
[00:04:33] SPEAKER_03: where you kind of felt, wow, this thing's going to be pretty good?
[00:04:37] We just talked about this.
[00:04:38] SPEAKER_00: Yeah, I think Nicole had the aha moment.
[00:04:41] I had one where, so we always have an internal demo
[00:04:44] SPEAKER_00: where we play with the models as we're developing them.
[00:04:47] SPEAKER_00: And I had one where I just took an image of myself
[00:04:50] SPEAKER_00: and then I said, like, hey, put me on the red carpet
[00:04:52] SPEAKER_00: and like, just total vanity prompt, right?
[00:04:56] SPEAKER_00: And then it came out and it looked like me
[00:04:58] SPEAKER_00: and then I compared it to all the models that we had before.
[00:05:02] SPEAKER_00: And no other model actually looked like me
[00:05:05] SPEAKER_00: and I was like, so excited.
[00:05:06] SPEAKER_00: Wow.
[00:05:07] SPEAKER_02: And then people looked and they were like,
[00:05:08] SPEAKER_00: OK, we get it.
[00:05:09] SPEAKER_00: You're on the red carpet.
[00:05:11] SPEAKER_00: And then I think it took a couple of weeks
[00:05:14] SPEAKER_00: of other people being able to take their own photos
[00:05:16] SPEAKER_00: and play with it and just kind of realize
[00:05:18] SPEAKER_00: how magical that is when you get it to work.
[00:05:21] And that's kind of the main thing that people have been actually
[00:05:23] SPEAKER_00: doing with the model, right?
[00:05:24] SPEAKER_00: Turning yourself into a 3D figurine
[00:05:27] SPEAKER_00: where it's like, you want a computer, you want a toy box
[00:05:30] SPEAKER_00: and then you as the figurine.
[00:05:31] SPEAKER_00: So like you three times, like that way
[00:05:34] SPEAKER_00: to be able to kind of like express yourself
[00:05:36] SPEAKER_00: and see yourself in new ways and almost kind of like enhance
[00:05:39] SPEAKER_00: your own identity has just been really fun.
[00:05:41] SPEAKER_00: And that for me was like, oh, man, this is awesome.
[00:05:43] SPEAKER_00: What was it about what Nana Banana did
[00:05:45] SPEAKER_02: with you on the red carpet that was miles better
[00:05:48] SPEAKER_02: than whatever one else has?
[00:05:50] SPEAKER_02: It looked like me.
[00:05:51] SPEAKER_00: And it's very difficult for you to be able to judge
[00:05:55] SPEAKER_00: character consistency on people's faces you don't know.
[00:05:59] SPEAKER_00: And so if I saw a version of you that's like an AI version
[00:06:03] SPEAKER_00: of you, I might be OK with it.
[00:06:05] SPEAKER_00: But you would say, oh, no, parts of my face are not quite right.
[00:06:09] SPEAKER_00: And you can really only do it on yourself,
[00:06:10] SPEAKER_00: which is why we now have evals on many team members
[00:06:14] SPEAKER_00: where it's like their own faces and they're looking
[00:06:16] SPEAKER_00: at the models output with their own faces on it.
[00:06:19] SPEAKER_00: Because it's really the only way that you can judge whether or not
[00:06:22] SPEAKER_00: someone looks like you.
[00:06:23] SPEAKER_01: Yourself in like faces you're familiar with.
[00:06:24] SPEAKER_01: I think when we started doing it on ourselves,
[00:06:27] SPEAKER_01: and it's like, I see Nicole a lot.
[00:06:28] SPEAKER_01: So Nicole versus random person we might eval on.
[00:06:33] SPEAKER_01: It's just a very big difference in terms
[00:06:35] SPEAKER_01: of judging the model capabilities.
[00:06:37] SPEAKER_01: And yeah, I think it's one of those things
[00:06:39] SPEAKER_01: that it's so fun.
[00:06:41] SPEAKER_01: That preservation of the identity
[00:06:43] SPEAKER_01: is so fundamental to these models actually being useful and exciting.
[00:06:46] SPEAKER_01: But is surprisingly tricky.
[00:06:51] SPEAKER_01: And that's why we see a lot of other models not quite
[00:06:54] SPEAKER_01: hitting it.
[00:06:55] SPEAKER_03: Well, I was going to ask you, I would imagine
[00:06:57] SPEAKER_03: that character consistency is not just an emergent property of scale.
[00:07:01] SPEAKER_03: And so maybe two questions.
[00:07:03] SPEAKER_03: One, I'm sure there's stuff you can't tell us.
[00:07:05] SPEAKER_03: But what can you tell us about how you achieved it?
[00:07:08] SPEAKER_03: And then two, was that an explicit goal
[00:07:11] SPEAKER_03: heading into the development of this model?
[00:07:14] Yeah, so I would say, I mean, I think there's definitely
[00:07:16] SPEAKER_01: things that are tricky to say here.
[00:07:17] SPEAKER_01: But I would say there's like sort of different genres
[00:07:21] SPEAKER_01: of ways to do image generation.
[00:07:24] SPEAKER_01: And so that plays, that definitely plays
[00:07:26] SPEAKER_01: a part in how good it is.
[00:07:30] SPEAKER_01: And I think it was definitely a goal from the beginning.
[00:07:32] SPEAKER_01: It was definitely a goal because we knew
[00:07:35] SPEAKER_00: it was a gap with the models that we released in the past.
[00:07:38] SPEAKER_00: And generally consistency for us was a goal
[00:07:41] SPEAKER_00: because every time you're editing images, right?
[00:07:44] SPEAKER_00: You want to preserve some parts of it
[00:07:46] SPEAKER_00: and then you want to change something.
[00:07:47] SPEAKER_00: And prior models just weren't very good at that.
[00:07:50] SPEAKER_00: And that makes it not very useful and professional workflows.
[00:07:52] SPEAKER_00: But it also doesn't make use of the things
[00:07:54] SPEAKER_00: like character consistency.
[00:07:55] SPEAKER_00: And we've heard this for years from even advertisers
[00:07:58] SPEAKER_00: who are trying to advertise their products
[00:08:00] SPEAKER_00: and like putting them in lifestyle shots.
[00:08:01] SPEAKER_00: It has to look like your product like 100%.
[00:08:04] SPEAKER_00: Otherwise, you can't put it in an ad.
[00:08:07] SPEAKER_00: So we knew there was demand for it.
[00:08:08] SPEAKER_00: We knew the models had a gap.
[00:08:10] SPEAKER_00: And we felt like we had the right recipe,
[00:08:12] SPEAKER_00: both in terms of the model architecture and the data,
[00:08:15] SPEAKER_00: to finally make it happen.
[00:08:17] SPEAKER_00: I think what surprised us was just how good it was.
[00:08:19] SPEAKER_00: When we actually finally built the model.
[00:08:22] Yeah, right.
[00:08:22] Because I think we felt like we had the recipe exactly,
[00:08:25] SPEAKER_01: as Nicole said, but there's still always
[00:08:27] SPEAKER_01: until you're seeing the model, you finish training,
[00:08:30] SPEAKER_01: you're actually using it.
[00:08:32] SPEAKER_01: You don't know how close you're going to get to that goal.
[00:08:34] SPEAKER_01: And I think you were all surprised by that.
[00:08:37] SPEAKER_01: Yeah.
[00:08:38] SPEAKER_01: And I think the other thing is if we think about what people expect
[00:08:40] SPEAKER_01: out of editing when that you edit on your phone apps
[00:08:42] SPEAKER_01: or Photoshop, you expect a high degree of preservation
[00:08:46] SPEAKER_01: of things you're not touching.
[00:08:48] SPEAKER_01: And depending on how the models are made
[00:08:50] SPEAKER_01: and how the design decisions behind them,
[00:08:55] SPEAKER_01: that's very tricky to do.
[00:08:56] SPEAKER_01: But it's something people really,
[00:08:58] SPEAKER_01: it's one of those things where it's
[00:09:02] shockingly technically difficult, even though it's something,
[00:09:05] SPEAKER_01: I think a lay person who's using the models would be,
[00:09:08] SPEAKER_01: expect to be the basic thing about editing,
[00:09:10] SPEAKER_01: is like you don't mess with the things
[00:09:12] SPEAKER_01: you don't want to be messed with.
[00:09:13] SPEAKER_01: Yeah.
[00:09:14] Back to that moment where you saw yourself
[00:09:16] SPEAKER_03: on the road carpet.
[00:09:18] SPEAKER_03: And wow, that's actually me.
[00:09:21] And it took some of your colleagues a couple of weeks
[00:09:22] SPEAKER_03: to have the same experience because they tried it
[00:09:24] SPEAKER_03: with their own photos.
[00:09:26] SPEAKER_03: The question is beyond, hey, that's actually me,
[00:09:29] SPEAKER_03: the qualitative test.
[00:09:31] SPEAKER_03: Is there some sort of an evil that you can put against that
[00:09:33] SPEAKER_03: to make it quantitative that we have achieved the thing
[00:09:38] SPEAKER_03: that we set out to achieve here?
[00:09:39] SPEAKER_01: Yeah.
[00:09:40] SPEAKER_01: So I actually think face consistency
[00:09:42] SPEAKER_01: exactly for the reason Nicole said is quite hard.
[00:09:44] SPEAKER_01: It's quite hard for other people to do.
[00:09:46] SPEAKER_01: Yeah.
[00:09:47] SPEAKER_01: I will say in general, I think what we found
[00:09:50] SPEAKER_01: with image generation, in particular,
[00:09:52] SPEAKER_01: that's unlocked a lot for us is like human e-veils
[00:09:55] SPEAKER_01: are important.
[00:09:57] SPEAKER_01: And so I think they're a foundational.
[00:09:59] SPEAKER_01: We have a team that works on helping us build
[00:10:02] SPEAKER_01: sort of good tooling and good practices for e-veils
[00:10:05] SPEAKER_01: and having humans actually e-veil these things
[00:10:09] SPEAKER_01: that are very subtle.
[00:10:10] SPEAKER_01: Like if you think about image generation,
[00:10:12] faces aesthetic quality, these are things
[00:10:14] SPEAKER_01: that are very hard to quantify.
[00:10:16] SPEAKER_01: And so I think human e-veils have been, I mean,
[00:10:18] SPEAKER_01: a big game changer for us.
[00:10:20] SPEAKER_01: I think it's a combination of there's human e-veils.
[00:10:23] SPEAKER_00: There is very technical term eyeballing
[00:10:27] of the model results by different people.
[00:10:31] SPEAKER_00: And there's also just community testing.
[00:10:33] SPEAKER_00: And when we do community testing, we start internally.
[00:10:36] SPEAKER_00: And we have artists at Google and at Google
[00:10:39] SPEAKER_00: Define to play with these models.
[00:10:41] SPEAKER_00: Our execs will play with these models.
[00:10:43] SPEAKER_00: And that really helps.
[00:10:44] SPEAKER_00: I think kind of build that qualitative narrative around,
[00:10:48] SPEAKER_00: like, why is this model actually awesome?
[00:10:50] SPEAKER_00: Because if you just look at the quantitative benchmarks,
[00:10:53] SPEAKER_00: you could say, like, oh, it's 10% better
[00:10:55] SPEAKER_00: than this model that we had before.
[00:10:57] SPEAKER_00: And that doesn't quite grok that emotional aspect of like,
[00:11:00] SPEAKER_00: oh, I can now see myself in new ways.
[00:11:02] SPEAKER_00: Or I can now finally edit this family photo
[00:11:05] SPEAKER_00: that I cut up when I was five years old.
[00:11:08] SPEAKER_00: And I probably shouldn't have.
[00:11:09] SPEAKER_00: People have done that.
[00:11:10] When I'm able to restore it, like, I
[00:11:12] SPEAKER_00: think you really need that qualitative user feedback
[00:11:16] SPEAKER_00: in order to be able to tell that emotional story.
[00:11:18] SPEAKER_00: I think this is probably true of many of the Genai and AI
[00:11:22] SPEAKER_01: capabilities.
[00:11:23] SPEAKER_01: But I think it's especially true of visual media
[00:11:28] SPEAKER_01: where it's very subjective.
[00:11:29] SPEAKER_01: Versus if you think about something like math, reasoning,
[00:11:32] SPEAKER_01: logic reasoning, where like, you can really
[00:11:34] SPEAKER_01: ground it in an answer.
[00:11:36] SPEAKER_01: And so it's more easy to have these very objective,
[00:11:39] SPEAKER_01: automated quantitative evils.
[00:11:42] To get to that level of character consistency
[00:11:45] SPEAKER_02: from just one 2D image of someone is really, really hard,
[00:11:50] SPEAKER_02: can you walk us through maybe a little bit?
[00:11:52] SPEAKER_02: What are the technical breakthroughs that
[00:11:53] SPEAKER_02: helped you drive to that level of character consistency
[00:11:56] SPEAKER_02: that we actually haven't seen anywhere else?
[00:11:59] I mean, I think a key thing is like having good data
[00:12:03] SPEAKER_01: that teaches the models to generalize, right?
[00:12:05] SPEAKER_01: And the fact that this is a base, it's a Gemini model.
[00:12:09] SPEAKER_01: It's a multimodal foundational model that's
[00:12:14] SPEAKER_01: had seen a lot of data and has good generalization capabilities.
[00:12:19] SPEAKER_01: And I think that's the secret sauce.
[00:12:21] SPEAKER_01: It's like you really need models that
[00:12:23] generalize well to be able to take advantage of that for this.
[00:12:27] SPEAKER_00: Yeah.
[00:12:28] SPEAKER_00: And I think the other nice part about doing this
[00:12:30] SPEAKER_00: in a model like Gemini is that you also
[00:12:32] SPEAKER_00: get this really long context windows.
[00:12:34] SPEAKER_00: Like yes, you can provide one image of yourself,
[00:12:36] SPEAKER_00: but you can also provide multiple.
[00:12:38] And then on the output side, you can also
[00:12:40] SPEAKER_00: iterate across multiple turns and actually have a conversation
[00:12:44] SPEAKER_00: with the model, which wasn't possible before, right?
[00:12:47] SPEAKER_00: One, two years ago, we were fine tuning on 10 images of you.
[00:12:50] SPEAKER_00: And it took 20 minutes to actually get something
[00:12:53] SPEAKER_00: that looked like you.
[00:12:54] SPEAKER_00: And that's why it never took off in the mainstream, right?
[00:12:58] SPEAKER_00: Because it's just too hard.
[00:13:00] SPEAKER_00: And you don't have that many images of yourself.
[00:13:01] SPEAKER_00: It's too much work.
[00:13:03] SPEAKER_00: And so I think it's both kind of the general, like Gemini
[00:13:06] SPEAKER_00: gets better.
[00:13:07] SPEAKER_00: You benefit from that multi-modal context window
[00:13:09] SPEAKER_00: and you benefit from the like long output and ability
[00:13:12] SPEAKER_00: to like maintain context over a long conversation.
[00:13:15] SPEAKER_00: And then you also benefit from the like actually paying
[00:13:18] SPEAKER_00: attention to the data, focusing on the problem.
[00:13:20] SPEAKER_00: A lot of the things we get better at come down to.
[00:13:23] SPEAKER_00: There's a person on the team was like obsessed
[00:13:25] SPEAKER_00: with making them work.
[00:13:26] SPEAKER_00: Like we have people on the table, you
[00:13:27] SPEAKER_00: more obsessed with text rendering.
[00:13:29] SPEAKER_00: And so our text rendering just keeps getting better.
[00:13:31] SPEAKER_00: Because that person just like is obsessed with the problem.
[00:13:33] SPEAKER_00: Yeah, it's like it's not just about throwing high quantities
[00:13:37] SPEAKER_01: of data in, right?
[00:13:39] SPEAKER_01: I think that's one thing that's really important is
[00:13:41] SPEAKER_01: there's this like attention to detail and quality of all
[00:13:48] SPEAKER_01: the things you're doing with the model.
[00:13:50] SPEAKER_01: There's a lot of small design decisions
[00:13:52] SPEAKER_01: and position points at every point.
[00:13:54] SPEAKER_01: And I think that like detail orientedness of high quality
[00:13:59] SPEAKER_01: is data and selections are really important.
[00:14:02] It's the craft part by thing.
[00:14:05] SPEAKER_00: The AI which we don't talk about a lot,
[00:14:06] SPEAKER_00: but I think it's super important.
[00:14:08] SPEAKER_00: How big was the team that worked on it?
[00:14:10] SPEAKER_03: To ship it, it took a village.
[00:14:12] SPEAKER_00: Yeah, because especially because we
[00:14:13] SPEAKER_01: split ship across many products.
[00:14:15] SPEAKER_01: So I think like there's like sort of the core sort
[00:14:18] SPEAKER_01: of modeling team and then there's our close collaborators
[00:14:21] SPEAKER_01: across like all the surfaces.
[00:14:23] When you put them all together, you easily get into like dozens
[00:14:26] SPEAKER_00: and hundreds, but the team who works on the model
[00:14:29] SPEAKER_00: is much smaller.
[00:14:29] SPEAKER_00: And then the people who actually make all the magic happen.
[00:14:32] SPEAKER_00: We had a lot of infrastructure teams
[00:14:34] SPEAKER_00: like optimizing every part of the stack
[00:14:36] SPEAKER_00: to be able to serve the demand that we were seeing,
[00:14:38] SPEAKER_00: which was really awesome.
[00:14:40] SPEAKER_00: But really like to ship it, we're joking
[00:14:42] SPEAKER_00: that it takes like a small country.
[00:14:44] SPEAKER_00: When you build something like this,
[00:14:45] SPEAKER_03: do you build it with particular personas
[00:14:48] SPEAKER_03: or particular use cases in mind?
[00:14:50] SPEAKER_03: Or do you build it more with a capability first mindset?
[00:14:55] SPEAKER_03: And then once the capabilities emerge,
[00:14:57] SPEAKER_03: you can map it to personas.
[00:14:59] SPEAKER_03: It's a little bit of both, I would say.
[00:15:02] SPEAKER_00: Before we start training any new model,
[00:15:04] SPEAKER_00: we kind of have an idea of what we want the capabilities to be.
[00:15:09] SPEAKER_00: And some design decisions like how fast is it
[00:15:12] SPEAKER_00: at inference time, right?
[00:15:14] SPEAKER_00: They also impact which persona you're going after.
[00:15:17] SPEAKER_00: So this model, because it's kind of a conversational editor,
[00:15:21] SPEAKER_00: we wanted it to be really snappy,
[00:15:23] SPEAKER_00: because you can really have a conversation with a model
[00:15:26] SPEAKER_00: if it takes like a minute or two to generate.
[00:15:28] SPEAKER_00: That's really nice about image models versus video models.
[00:15:31] SPEAKER_00: It just has to weigh that long.
[00:15:32] SPEAKER_00: And so to us from the beginning, it felt
[00:15:34] SPEAKER_00: like a very consumer centric model.
[00:15:38] SPEAKER_00: But obviously, we also have developer products,
[00:15:41] SPEAKER_00: and enterprise products, and all of these capabilities
[00:15:44] SPEAKER_00: end up being useful to them.
[00:15:46] But really, we've seen a ton of excitement
[00:15:48] SPEAKER_00: on the consumer side in a way that I think we haven't before
[00:15:52] SPEAKER_00: with our image models, because it was very snappy
[00:15:55] SPEAKER_00: and it kind of made these like pro-level capabilities,
[00:15:58] SPEAKER_00: which is really easily accessible through a text prompt.
[00:16:01] And so that's kind of how we started it out.
[00:16:03] SPEAKER_00: But then obviously, it ends up being useful
[00:16:05] SPEAKER_00: in other domains as well.
[00:16:08] SPEAKER_00: Yeah. And I think one of the differences in philosophy,
[00:16:11] SPEAKER_01: so like previously we'd worked on the Imagine Line of Models,
[00:16:14] SPEAKER_01: which were straight image generation.
[00:16:15] SPEAKER_01: And I think one of the big philosophical goal changes
[00:16:20] SPEAKER_01: in these Gemini image generation models
[00:16:22] SPEAKER_01: is generalization is like a more foundational capability.
[00:16:28] SPEAKER_01: So I think there is also a lot of,
[00:16:30] SPEAKER_01: there's things where we want this model to be able to be good
[00:16:33] SPEAKER_01: at this, representing people and letting them edit their images
[00:16:38] SPEAKER_01: and have it look like themselves.
[00:16:39] SPEAKER_01: But I think there's also a lot of things
[00:16:41] SPEAKER_01: that are emergent from the goal of just having a baseline
[00:16:46] SPEAKER_01: capable model that reasons about visual information.
[00:16:51] SPEAKER_01: I think one thing that surprised me, I guess,
[00:16:53] SPEAKER_01: is a call back to your early conversation,
[00:16:55] SPEAKER_01: is people can put in math problems,
[00:16:57] SPEAKER_01: drawing of a math problem and ask it to render the solution.
[00:17:02] SPEAKER_01: So you can put in a geometry problem and say,
[00:17:05] SPEAKER_01: what is this angle?
[00:17:07] SPEAKER_01: And that's like an emergent thing of a foundationally capable
[00:17:11] SPEAKER_01: model that has both reasoning, mathematical understanding
[00:17:15] SPEAKER_01: and visual understanding.
[00:17:16] SPEAKER_01: So I think there's both.
[00:17:19] SPEAKER_01: Can you maybe share, I just had a curiosity,
[00:17:21] SPEAKER_02: what's a good way to understand maybe the family mapping
[00:17:24] SPEAKER_02: and the relationship between Gemini, powering,
[00:17:27] SPEAKER_02: nano-banana, VO, all these other adjacent products
[00:17:33] SPEAKER_02: and models that are all driven and benefit
[00:17:35] SPEAKER_02: from the generalization and the scale of Gemini itself,
[00:17:39] how you co-develop and then where
[00:17:41] SPEAKER_02: you want to take it from here.
[00:17:43] SPEAKER_00: Our goal has always been to build the single,
[00:17:46] SPEAKER_00: most powerful model that can do all these things.
[00:17:49] SPEAKER_00: You can take in any modality and you can transform it
[00:17:51] SPEAKER_00: into any modality.
[00:17:53] SPEAKER_00: And that's the North Star.
[00:17:55] SPEAKER_00: We're obviously not quite there yet.
[00:17:57] SPEAKER_00: And so on the way there, we had a lot of sort of specialized
[00:18:00] SPEAKER_00: models that just got you great results in a specific domain.
[00:18:04] SPEAKER_00: So imagine was an example of that for image generation,
[00:18:07] VO is an example of that for video generation and editing.
[00:18:12] SPEAKER_00: And so I think we're both developing these models
[00:18:14] SPEAKER_00: to push the frontier of that modality.
[00:18:17] SPEAKER_00: And you get really useful outputs out of that, right?
[00:18:19] SPEAKER_00: A lot of filmmakers are using VO in their creative process.
[00:18:23] SPEAKER_00: But you're also learning a lot that you can then
[00:18:24] SPEAKER_00: bring back into Gemini and then make it good at that modality.
[00:18:28] SPEAKER_00: Image is always a little bit ahead of the curve
[00:18:31] SPEAKER_00: because you just have one frame, right?
[00:18:33] SPEAKER_00: It's cheaper, both train and at inference time.
[00:18:37] SPEAKER_00: So I think a lot of the developments
[00:18:39] SPEAKER_00: you see in image I expect you to see in video,
[00:18:43] SPEAKER_00: like six, 12 months down the line.
[00:18:46] SPEAKER_00: And so that's always been the goal.
[00:18:48] SPEAKER_00: And so we have separate teams developing these.
[00:18:51] SPEAKER_00: And then I think with image, we're now moving closer
[00:18:54] SPEAKER_00: to Gemini and to that vision of that single most powerful model.
[00:19:00] SPEAKER_00: And you will see that I think with some of the other modalities.
[00:19:02] SPEAKER_00: And along the way, we'll release these experiences
[00:19:04] SPEAKER_00: that are just really powerful and really exciting
[00:19:06] SPEAKER_00: in that modality.
[00:19:07] SPEAKER_00: So VO3 was really awesome because it brought audio
[00:19:11] SPEAKER_00: into video generation, right?
[00:19:12] SPEAKER_00: In a way that we haven't seen before.
[00:19:14] SPEAKER_00: Genie 3 was really awesome because it
[00:19:16] SPEAKER_00: let you in real time kind of navigate a world.
[00:19:20] SPEAKER_00: And so in order to push that frontier,
[00:19:21] SPEAKER_00: it's very hard to do all of that at the same time
[00:19:24] SPEAKER_00: right now in one model.
[00:19:27] SPEAKER_00: And so to some extent, these specialized models
[00:19:29] SPEAKER_00: are kind of a testing ground.
[00:19:30] SPEAKER_00: But I would expect that over time, Gemini
[00:19:33] SPEAKER_00: should be able to do all these things.
[00:19:35] SPEAKER_00: That's so interesting.
[00:19:36] OK, we got to ask you about the name.
[00:19:39] SPEAKER_03: I suspect that the name was a bit of it.
[00:19:41] SPEAKER_03: It's an amazing product.
[00:19:43] SPEAKER_03: I suspect that the name gave it a little bit of a boost
[00:19:48] SPEAKER_03: because it's so easy to remember and so distinct.
[00:19:50] SPEAKER_03: So was it a happy accident?
[00:19:52] SPEAKER_03: Or is there some creative genius who
[00:19:54] SPEAKER_03: knew that this is going to be just the right name?
[00:19:57] SPEAKER_03: It was a happy accident.
[00:19:59] SPEAKER_01: So I think as many people know, the model went out
[00:20:04] SPEAKER_01: on an ILL arena for my models to.
[00:20:06] SPEAKER_01: And part of that is you give a code name.
[00:20:09] SPEAKER_01: If anyone hasn't used ILLA arena,
[00:20:10] SPEAKER_01: you get to put in your prompt.
[00:20:12] SPEAKER_01: You'll get back to your responses from two models.
[00:20:14] SPEAKER_01: They have code names until they're publicly released.
[00:20:18] SPEAKER_01: And I think it was like we had to someone
[00:20:22] SPEAKER_01: we were going at at like 2am.
[00:20:24] SPEAKER_01: And Nicole is our wonderful PM.
[00:20:27] SPEAKER_01: There's another PM you have, Nina.
[00:20:29] SPEAKER_01: And someone messaged her being like, what do we name it?
[00:20:32] SPEAKER_01: And she was really tired and exhausted.
[00:20:35] SPEAKER_01: And she was like, this was the name of stroke of genius
[00:20:39] SPEAKER_01: that came to her at 2am.
[00:20:41] SPEAKER_01: This is you?
[00:20:42] SPEAKER_03: It was Nami.
[00:20:43] SPEAKER_00: It was somebody on my team who named the model.
[00:20:46] SPEAKER_00: I can't take care of this.
[00:20:48] SPEAKER_00: Another one of our PMs.
[00:20:50] SPEAKER_00: But what was really awesome is like A, it was really fun.
[00:20:53] SPEAKER_00: I think that really helps.
[00:20:54] SPEAKER_00: It's easier to pronounce.
[00:20:56] SPEAKER_00: It has an emoji, which is critical for branding.
[00:20:59] SPEAKER_00: She didn't overthink it.
[00:21:00] SPEAKER_01: In this era, but she didn't overthink it.
[00:21:02] SPEAKER_00: And what was awesome is everybody just went with it.
[00:21:04] SPEAKER_00: Once it went live.
[00:21:05] SPEAKER_00: And I think it just like felled very googly and very organic.
[00:21:09] SPEAKER_00: And it ended up looking like the stroke of marketing genius.
[00:21:11] SPEAKER_00: But no, it was a happy accident.
[00:21:13] SPEAKER_00: And it just sort of worked out.
[00:21:14] SPEAKER_00: And people loved it.
[00:21:15] SPEAKER_00: And so we leaned into it.
[00:21:16] SPEAKER_00: And now there's bananas everywhere.
[00:21:18] SPEAKER_00: When you go into the Gemini app, which we did
[00:21:21] SPEAKER_00: because people were complaining that they were having a really
[00:21:24] SPEAKER_00: hard time finding the model when they came into the app.
[00:21:28] SPEAKER_00: And so we just made it easier.
[00:21:29] SPEAKER_00: Yeah.
[00:21:30] SPEAKER_01: Yeah, exactly.
[00:21:31] SPEAKER_01: I think there's like, publicly people were like, nanobanana,
[00:21:33] SPEAKER_01: nanobanana.
[00:21:34] SPEAKER_01: How do I use nanobanana?
[00:21:36] SPEAKER_01: I had someone at Google I work with.
[00:21:38] SPEAKER_01: Be like, how do I use nanobanana?
[00:21:41] SPEAKER_01: And I was like, it's Gemini.
[00:21:43] SPEAKER_01: Because it's right there.
[00:21:46] SPEAKER_01: Just ask for an image.
[00:21:49] SPEAKER_01: Yeah, but I think that's the thing.
[00:21:51] SPEAKER_01: I think Google's always had this really fun brand.
[00:21:53] SPEAKER_01: It's not like it's been a consumer-oriented company
[00:21:58] SPEAKER_01: at its inception.
[00:21:59] SPEAKER_01: And I think it was really nice to play on that image
[00:22:04] SPEAKER_01: people have of Google as a fun, fun place, fun company.
[00:22:10] SPEAKER_01: And have this fun name.
[00:22:12] SPEAKER_00: It's also just like a really nice path to fun being kind
[00:22:16] SPEAKER_00: of a gateway to utility, right?
[00:22:18] SPEAKER_00: I think nanobanana and just the model in general,
[00:22:20] SPEAKER_00: and what you can do with it, like,
[00:22:21] SPEAKER_00: put yourself on the right carpet, do all the childhood dream
[00:22:24] SPEAKER_00: professions you had.
[00:22:25] It's like a really fun entry point.
[00:22:26] SPEAKER_00: But what's been awesome to see is that, once people are in the app
[00:22:29] SPEAKER_00: and they are using Gemini, they start to use it for other things.
[00:22:33] SPEAKER_00: That then become useful in their day-to-day life.
[00:22:35] SPEAKER_00: Like, you use it to study.
[00:22:36] SPEAKER_00: And it's all math problems.
[00:22:38] SPEAKER_00: Or you use it to learn about something else.
[00:22:40] SPEAKER_00: And so I think it's maybe a little bit undervalued sometimes
[00:22:43] SPEAKER_00: to have a little fun.
[00:22:45] SPEAKER_00: Not just with the naming, but also just with the products
[00:22:48] SPEAKER_00: that we build, because it kind of gets people in,
[00:22:49] SPEAKER_00: gets them excited, and then it helps
[00:22:51] SPEAKER_00: them discover other things that the models are awesome at.
[00:22:54] SPEAKER_00: I think other users, my parents and their friends are using it.
[00:22:59] SPEAKER_01: I think it's because they had this reputation.
[00:23:01] SPEAKER_01: It was really easy.
[00:23:02] SPEAKER_01: It was really fun.
[00:23:03] SPEAKER_01: It felt unintimidating to try.
[00:23:06] SPEAKER_01: When you try it, and you're like, actually,
[00:23:07] SPEAKER_01: this is very easy to work.
[00:23:10] SPEAKER_01: This works very easily.
[00:23:11] SPEAKER_01: It's very easy to interact with.
[00:23:12] SPEAKER_01: There's no technology I think can sometimes
[00:23:17] SPEAKER_01: be intimidating to people, especially AI right now.
[00:23:20] SPEAKER_01: And I think the chatbot naturalness has broken a lot of that
[00:23:24] SPEAKER_01: barriers, but maybe more so with younger people.
[00:23:27] SPEAKER_01: And I think this fun, my mom made,
[00:23:32] SPEAKER_01: was making these images and having great time.
[00:23:35] SPEAKER_01: And then realized she can use it to remove people
[00:23:38] SPEAKER_01: from the background of her images.
[00:23:39] SPEAKER_01: These very practical things, starting very silly,
[00:23:42] SPEAKER_01: turn very practical.
[00:23:43] SPEAKER_01: Then people can use it to realize, actually,
[00:23:45] SPEAKER_01: they can give you them diagrams or help them understand stuff.
[00:23:48] SPEAKER_01: So I think there's also a big accessibility component.
[00:23:52] SPEAKER_01: Where do you want to take from here?
[00:23:53] SPEAKER_02: Maybe both from a model side and from our product side.
[00:23:57] SPEAKER_02: On the product side, I think there's kind of a couple areas.
[00:24:01] SPEAKER_00: On the consumer side, I still think we have a long way
[00:24:03] SPEAKER_00: to go to just like maybe things easier to use, right?
[00:24:06] SPEAKER_00: You will notice that a lot of the nano-binana prompts
[00:24:09] SPEAKER_00: are like 100 words long.
[00:24:10] SPEAKER_00: And people actually go in and copy,
[00:24:13] SPEAKER_00: paste them into the Gemini app and go through the work
[00:24:15] SPEAKER_00: to make it work, because the payoff is worth it.
[00:24:18] SPEAKER_00: But I think we have to get past this prompt engineering
[00:24:21] SPEAKER_00: face for consumers and just make things really easy
[00:24:23] SPEAKER_00: for them to use.
[00:24:25] I think on the professional side, we
[00:24:28] SPEAKER_00: need to get into much more precise control,
[00:24:30] SPEAKER_00: kind of robustness, like reproduced ability
[00:24:33] SPEAKER_00: to make it useful in actual professional workflows.
[00:24:37] SPEAKER_00: So yes, we're very good at editing consistency
[00:24:40] SPEAKER_00: and not changing pixels, but we're not 100% there.
[00:24:43] SPEAKER_00: And when you're a professional, you need to be 100% there.
[00:24:46] SPEAKER_00: You really need these precise, maybe even
[00:24:49] SPEAKER_00: gesture-based controls over every single pixel in the frame.
[00:24:53] So we definitely need to go in that direction.
[00:24:55] And then I think there's a general direction
[00:24:57] SPEAKER_00: that I'm really excited about, which
[00:24:58] SPEAKER_00: is just about visualizing information.
[00:25:01] SPEAKER_00: So the example I had about sketch notes at the beginning
[00:25:04] SPEAKER_00: and somebody kind of hacking their way around using
[00:25:06] SPEAKER_00: nano-binana for that use case, you could just imagine
[00:25:09] SPEAKER_00: being able to do that for anything, right?
[00:25:11] SPEAKER_00: And a lot of people are visual learners.
[00:25:13] SPEAKER_00: I think we haven't really exhausted the potential of LLMs
[00:25:17] SPEAKER_00: to be able to help you digest and visualize information
[00:25:21] SPEAKER_00: in whatever way is most natural for you to consume.
[00:25:24] SPEAKER_00: So sometimes it's a diagram, sometimes it's an image,
[00:25:27] SPEAKER_00: and sometimes maybe it's a short video, right?
[00:25:29] SPEAKER_00: Then you want to learn about some concept
[00:25:32] SPEAKER_00: that you're learning in a biology class
[00:25:34] SPEAKER_00: or something like that.
[00:25:35] SPEAKER_00: So I think that's a completely new domain
[00:25:37] SPEAKER_00: that I'm really excited about, just these models getting better.
[00:25:39] SPEAKER_00: And getting past the point where 95% of the outputs
[00:25:44] SPEAKER_00: that you get out of these models are just text, which
[00:25:46] SPEAKER_00: is useful, but it's not how we consume information
[00:25:49] SPEAKER_00: in the real world right now.
[00:25:51] It's really interesting.
[00:25:52] SPEAKER_02: So on the product side, then are you
[00:25:53] SPEAKER_02: alluding to the fact that you might want to vertically
[00:25:55] SPEAKER_02: integrate and build a little bit more product around it?
[00:25:58] SPEAKER_02: And also are you alluding to the fact
[00:25:59] SPEAKER_02: that maybe the way you interact with some of these models
[00:26:03] SPEAKER_02: isn't just through pure language and prompting over time,
[00:26:05] SPEAKER_02: but more UI.
[00:26:08] Yeah, yeah, I definitely think the chatbots,
[00:26:11] SPEAKER_00: I think, are an easy entry point for people
[00:26:13] SPEAKER_00: because you don't have to learn a new UI.
[00:26:15] SPEAKER_00: You just talk to it, and then you say whatever you want to do,
[00:26:18] SPEAKER_00: right?
[00:26:19] SPEAKER_00: I think it starts to become a little bit limiting
[00:26:21] SPEAKER_00: for the visual modalities.
[00:26:23] SPEAKER_00: And I think there's a ton of headroom
[00:26:25] SPEAKER_00: to think about what is the new visual creation canvas
[00:26:29] SPEAKER_00: for the future?
[00:26:31] SPEAKER_00: And how do you build that in a way that doesn't
[00:26:33] SPEAKER_00: become overwhelming?
[00:26:34] SPEAKER_00: Because as these models can do more and more things,
[00:26:38] SPEAKER_00: it's very hard to explain to the user in something
[00:26:40] SPEAKER_00: that's very open-ended.
[00:26:42] SPEAKER_00: What the constraints are, and how do you work around that,
[00:26:44] SPEAKER_00: and how do you actually use it in a productive way.
[00:26:47] SPEAKER_00: So I'm really excited about people building products
[00:26:49] SPEAKER_00: in those directions.
[00:26:51] SPEAKER_00: And for us, we have a team called Labs at Google
[00:26:55] SPEAKER_00: that's led by Josh Woodward.
[00:26:56] SPEAKER_00: And they do a lot of this frontier thinking experimentation.
[00:27:00] SPEAKER_00: They work with us really closely
[00:27:02] SPEAKER_00: where they take our frontier models,
[00:27:03] SPEAKER_00: and they think about what's the future of entertainment
[00:27:06] SPEAKER_00: was the future of creation, was the future of productivity.
[00:27:10] SPEAKER_00: And so they build products like Nordbook Alam
[00:27:12] SPEAKER_00: and flow on the video side.
[00:27:13] SPEAKER_00: And I'm excited that maybe flow could become this place
[00:27:17] SPEAKER_00: where you could do some of this creation
[00:27:18] SPEAKER_00: and think about what that looks like in the future.
[00:27:21] SPEAKER_00: I think in the short term, it's very clear that this model
[00:27:24] SPEAKER_01: has things that it's not perfect at.
[00:27:26] SPEAKER_01: And so in the short term, it's obviously
[00:27:29] SPEAKER_01: it should work the way you expect it to every time, not just
[00:27:32] SPEAKER_01: a lot of the time, and really make it so seamless.
[00:27:37] SPEAKER_01: And fix all these small things where it's just like a little
[00:27:41] SPEAKER_01: bit inconsistent in its performance.
[00:27:44] SPEAKER_01: I think long-term, it's, I think, Nicole covered that,
[00:27:47] SPEAKER_01: which is, to me, it's in order to have that reality
[00:27:53] SPEAKER_01: of really rich, multimodal generation.
[00:27:56] SPEAKER_01: So right now, if you ask Gemini to explain something,
[00:28:00] SPEAKER_01: it'll usually just explain and test text
[00:28:02] SPEAKER_01: unless you ask it for images.
[00:28:03] SPEAKER_01: But if you think about the platforms that have really
[00:28:05] SPEAKER_01: taken off in the last 10, 20 years for learning,
[00:28:10] SPEAKER_01: we think of Khan Academy started on YouTube.
[00:28:12] SPEAKER_01: We think about Wikipedia has a lot of images.
[00:28:16] SPEAKER_01: It's a very image-focus, if you look at any math thing,
[00:28:18] SPEAKER_01: you might like diagrams.
[00:28:18] SPEAKER_01: And so that should become more, like, a natural part
[00:28:24] SPEAKER_01: of the flow and part of the way you use these models.
[00:28:26] SPEAKER_01: And to enable that from a modeling point of view,
[00:28:28] SPEAKER_01: it goes back to like, like we were talking about this multimodal
[00:28:32] SPEAKER_01: understanding and seamless generalization
[00:28:36] SPEAKER_01: between modalities.
[00:28:38] Maybe the other interesting area, as we think about,
[00:28:41] SPEAKER_00: kind of, you know, these models being more proactive
[00:28:44] SPEAKER_00: at pulling in, you know, whether it's code or images
[00:28:46] SPEAKER_00: or video when it's appropriate for the user intent.
[00:28:49] SPEAKER_00: I think there's other exciting here.
[00:28:50] SPEAKER_00: I started out as a consultant in my career.
[00:28:53] SPEAKER_00: And so obviously, I made a lot of slide decks in my time.
[00:28:56] SPEAKER_00: I still do.
[00:28:57] SPEAKER_00: And I think there are some of these use cases
[00:28:59] SPEAKER_00: where you don't actually really want
[00:29:00] SPEAKER_00: to be in the weeds of creation.
[00:29:02] SPEAKER_00: Like what you really want is, let's say,
[00:29:04] you're updating your stakeholders on how a project is going.
[00:29:07] SPEAKER_00: Right?
[00:29:08] SPEAKER_00: You want to pull in some context.
[00:29:09] SPEAKER_00: Maybe it's meeting notice.
[00:29:10] SPEAKER_00: Maybe it's a couple of bullet points.
[00:29:12] SPEAKER_00: Maybe it's, you know, some other deck
[00:29:14] SPEAKER_00: that you've created in the past.
[00:29:16] And then you maybe just one Gemini
[00:29:17] SPEAKER_00: to go off and like do all the work for you, right?
[00:29:20] SPEAKER_00: Like pull that deck together, formatted,
[00:29:23] SPEAKER_00: create appropriate visuals to make it really easy to digest.
[00:29:26] SPEAKER_00: And that's something that you probably don't want
[00:29:28] SPEAKER_00: to be involved in.
[00:29:29] SPEAKER_00: And it gets more into these agent behavior.
[00:29:31] SPEAKER_00: Versus, I think for some of these creative workflows,
[00:29:34] SPEAKER_00: like you actually want to be creating.
[00:29:36] SPEAKER_00: You want to be in the weeds.
[00:29:37] SPEAKER_00: You want to think about what the UI looks like.
[00:29:40] SPEAKER_00: That makes it easy for a user to accomplish
[00:29:42] SPEAKER_00: the goal.
[00:29:42] SPEAKER_00: And so like if I'm designing my house,
[00:29:45] SPEAKER_00: and I'm actually into designing my house,
[00:29:47] SPEAKER_00: then I probably actually want to play with it
[00:29:49] SPEAKER_00: and like play with textures and different colors
[00:29:51] SPEAKER_00: and like mate, what would happen if I remove this wall?
[00:29:54] SPEAKER_00: And so I think there's kind of this spectrum of like very
[00:29:56] SPEAKER_00: hands-off, like just let the model go off
[00:29:58] SPEAKER_00: and like pull in relevant visuals, materials,
[00:30:01] SPEAKER_00: for a task that makes sense.
[00:30:03] SPEAKER_00: All the way to like, how do you actually
[00:30:04] SPEAKER_00: make a creative process like more fun and remove
[00:30:07] SPEAKER_00: the tedious parts and remove the technical barriers that
[00:30:10] SPEAKER_00: exist today with tools that we have?
[00:30:12] SPEAKER_00: This makes of giving the user fine-grained control,
[00:30:14] SPEAKER_01: like the precision control they want,
[00:30:16] SPEAKER_01: but also at the other extreme, having the model be able to
[00:30:21] understand the user quest and anticipate, right?
[00:30:25] SPEAKER_01: Like the need and outcome that it should be
[00:30:27] SPEAKER_01: and do all the intervening work in between.
[00:30:31] It's almost like when you actually hire a professional
[00:30:33] SPEAKER_00: for something today, right?
[00:30:34] SPEAKER_00: Like when you hire a designer, you give them a spec
[00:30:36] SPEAKER_00: and then they go off and then they do all that also
[00:30:38] SPEAKER_00: more that they do because they have all this expertise.
[00:30:41] SPEAKER_00: And so these models should be able to do that
[00:30:43] SPEAKER_00: and they can't really do that in many domains today.
[00:30:47] SPEAKER_03: What do you think the next competitive battleground is
[00:30:50] SPEAKER_03: in this world?
[00:30:52] I think there's still work to be done
[00:30:54] SPEAKER_00: on making these models more capable.
[00:30:56] SPEAKER_00: And so this idea of having a single model that can take
[00:30:59] SPEAKER_00: anything and transform it into anything else,
[00:31:00] SPEAKER_00: I think nobody has really figured that out.
[00:31:04] SPEAKER_00: But I do think in order to actually drive adoption,
[00:31:08] SPEAKER_00: there's hardly two things.
[00:31:09] SPEAKER_00: One is user interfaces.
[00:31:11] SPEAKER_00: Like we still rely very heavily on the chatbots
[00:31:13] SPEAKER_00: and we talked about this.
[00:31:14] SPEAKER_00: Like it's useful for some things
[00:31:16] SPEAKER_00: and it's a great entry point.
[00:31:18] But it maybe isn't useful for all the things.
[00:31:20] SPEAKER_00: And so I think starting to think about much more deeply
[00:31:23] SPEAKER_00: about who are the users, what are they trying to do?
[00:31:26] SPEAKER_00: How can the technology be helpful?
[00:31:28] SPEAKER_00: And then what product do you built around it
[00:31:31] SPEAKER_00: to make that happen?
[00:31:33] SPEAKER_00: It's probably one.
[00:31:35] Do you think Fiverr 10 years from now,
[00:31:36] SPEAKER_03: the frontier will be advancing as quickly
[00:31:39] SPEAKER_03: as it has advanced over these last few years?
[00:31:42] I have to 10 years from now.
[00:31:43] SPEAKER_00: I feel like 20 years from now.
[00:31:45] SPEAKER_00: And just the space, and you guys probably see this too,
[00:31:49] SPEAKER_00: like the space is moving really quickly.
[00:31:52] SPEAKER_00: And if you asked me two years ago,
[00:31:54] SPEAKER_00: I would have told you the space is moving really quickly.
[00:31:56] SPEAKER_00: If you asked me today, I will tell you it's moving faster
[00:31:59] SPEAKER_00: than it was two years ago.
[00:32:01] OK, I'm going to ask you a very different question.
[00:32:03] SPEAKER_03: So I know Google is very careful and very concerned
[00:32:11] SPEAKER_03: about deep fakes and that sort of thing.
[00:32:14] SPEAKER_03: And I have to imagine when you saw how capable
[00:32:16] SPEAKER_03: this model was, there's a big conversation about, OK,
[00:32:18] SPEAKER_03: well, how are we going to make sure people don't use it
[00:32:20] SPEAKER_03: in the wrong sorts of ways?
[00:32:22] SPEAKER_03: How does that sort of a conversation go inside of Google?
[00:32:26] SPEAKER_03: And are you guys sort of like happy with where it ended up?
[00:32:29] SPEAKER_03: I think it's an ever evolving frontier,
[00:32:32] SPEAKER_00: also, because it's this mix of,
[00:32:35] SPEAKER_00: you want to give people the creative freedom
[00:32:38] SPEAKER_00: to be able to use these tools, right?
[00:32:39] SPEAKER_00: And you want to give users control,
[00:32:41] SPEAKER_00: to be able to use these tools in a way
[00:32:43] SPEAKER_00: that don't feel overly restrictive.
[00:32:45] And you want to prevent the worst harm, right?
[00:32:47] SPEAKER_00: I think that's always the balance
[00:32:49] SPEAKER_00: that we spend a lot of time talking about.
[00:32:52] SPEAKER_00: And so obviously, when you look at the outfits of the model,
[00:32:56] there's a visible watermark that says it's
[00:32:57] SPEAKER_00: been generated with Gemini, so that immediately
[00:33:00] SPEAKER_00: indicates that it's AI content.
[00:33:02] SPEAKER_00: And then we also, in every output that we produce
[00:33:06] SPEAKER_00: with our models, image video, audio,
[00:33:09] SPEAKER_00: there's Synth ID embedded, which is invisible watermarking.
[00:33:13] SPEAKER_00: And so those are kind of the visible ways
[00:33:15] SPEAKER_00: or an invisible ways in which we verify
[00:33:17] SPEAKER_00: that our content is AI generated.
[00:33:19] SPEAKER_00: We're very invested in it.
[00:33:20] SPEAKER_00: And we believe that it is really important
[00:33:23] SPEAKER_00: to give users those tools to be able to understand
[00:33:25] SPEAKER_00: that when they're seeing something, it's not a real video,
[00:33:28] SPEAKER_00: it's not a real image.
[00:33:30] SPEAKER_00: And then obviously, when we develop these models,
[00:33:33] SPEAKER_00: we do a ton of testing internally and also
[00:33:36] SPEAKER_00: with external partners to kind of find,
[00:33:39] SPEAKER_00: as the models get more capable, you find new attack vectors,
[00:33:43] SPEAKER_00: and new ways that you have to mitigate for.
[00:33:46] SPEAKER_00: And so that is a very important part
[00:33:48] SPEAKER_00: of model development for us.
[00:33:50] SPEAKER_00: And we continue to invest in it.
[00:33:52] SPEAKER_00: And as the models get better and as there's new things
[00:33:55] SPEAKER_00: that you can do with them, we also
[00:33:57] SPEAKER_00: have to develop new mitigations for making sure
[00:34:00] SPEAKER_00: that we don't create harm, but also still
[00:34:02] SPEAKER_00: give users the creativity and the control
[00:34:05] SPEAKER_00: in order to make these models usable in a product.
[00:34:08] I mean, I think it's a very, very hard
[00:34:10] SPEAKER_01: balance to strike, right?
[00:34:12] SPEAKER_01: Because you will always have people
[00:34:15] SPEAKER_01: using a tool in good faith.
[00:34:16] SPEAKER_01: You'll also always have people using it in bad faith.
[00:34:21] And I think it's hard.
[00:34:23] SPEAKER_01: It's like, is it a tool?
[00:34:25] SPEAKER_01: Is it something that has responsibility?
[00:34:27] SPEAKER_01: So I think we take this very seriously.
[00:34:31] Users obviously are also responsible
[00:34:33] SPEAKER_01: for what they do with the model.
[00:34:35] SPEAKER_01: But SynthID really is an important technology
[00:34:38] SPEAKER_01: that lets us like release these capabilities to people
[00:34:41] SPEAKER_01: and have some faith in that we can still verify, right?
[00:34:45] SPEAKER_01: And have a tool to combat this miss,
[00:34:48] SPEAKER_01: and the risk of misinformation.
[00:34:51] SPEAKER_01: But it's a super tricky conversation.
[00:34:54] SPEAKER_01: And I think it's one that I've seen everyone take very seriously.
[00:34:57] SPEAKER_01: There's a lot of conversations about how to balance both.
[00:35:02] SPEAKER_02: Is that the standard now across the industry?
[00:35:04] SPEAKER_02: SynthID?
[00:35:05] SPEAKER_02: Yeah.
[00:35:06] SPEAKER_02: It's a Google Center.
[00:35:07] SPEAKER_01: I believe there's like every Google,
[00:35:09] SPEAKER_01: like imagine the Imagine Line, Veo,
[00:35:12] SPEAKER_01: they all have SynthID when you use them in any product surface.
[00:35:16] Are you told us we can't go five to 10 years down the road?
[00:35:19] SPEAKER_03: Because things are moving too fast.
[00:35:20] SPEAKER_03: We'll go one to three years down the road.
[00:35:23] SPEAKER_03: Thank you.
[00:35:25] SPEAKER_03: Two questions.
[00:35:27] SPEAKER_03: One, what will be possible that we can only dream about today?
[00:35:34] And two, what will the resulting change be
[00:35:38] SPEAKER_03: to the way that we all live our lives?
[00:35:40] SPEAKER_03: I really hope that a year or two from now,
[00:35:44] SPEAKER_00: you could really get personalized tutors,
[00:35:47] SPEAKER_00: personalized textbooks in a way, right?
[00:35:50] SPEAKER_00: I love it.
[00:35:50] SPEAKER_00: Yeah.
[00:35:51] SPEAKER_00: There's no reason why UNI should be learning
[00:35:54] SPEAKER_00: from the same textbook if we have different learning styles
[00:35:57] SPEAKER_00: and different starting points.
[00:35:58] SPEAKER_00: But that's what we do now, right?
[00:35:59] SPEAKER_00: That's how our learning environment is set up.
[00:36:02] And I think across all these breakthroughs,
[00:36:04] SPEAKER_00: like that should be very possible,
[00:36:06] SPEAKER_00: where you have an LLM tutor that just figures out
[00:36:10] SPEAKER_00: your learning style, what are the things you like?
[00:36:12] SPEAKER_00: Maybe you're into basketball.
[00:36:13] SPEAKER_00: And so I need to explain physics to you
[00:36:15] SPEAKER_00: with basketball analogies, right?
[00:36:17] SPEAKER_00: And so I'm really excited about learning
[00:36:19] SPEAKER_00: just becoming way more personalized.
[00:36:21] SPEAKER_00: And that feels very achievable.
[00:36:24] SPEAKER_00: And we obviously have to make sure that we don't hallucinate.
[00:36:27] SPEAKER_00: And there's like a high bar for factuality.
[00:36:30] SPEAKER_00: And so we need to ground in sort of real world content.
[00:36:32] SPEAKER_00: But that I'm really excited about.
[00:36:35] SPEAKER_00: And that really, I think just, it removes a lot of barriers
[00:36:38] SPEAKER_00: for people, right?
[00:36:39] SPEAKER_00: To your question or like what the impact is going to be.
[00:36:42] SPEAKER_00: I think it just becomes much easier to learn basically anything.
[00:36:47] SPEAKER_00: Yeah.
[00:36:48] SPEAKER_00: So I think that's very tailored to you
[00:36:50] SPEAKER_00: that you just can't do right now.
[00:36:52] Could that be a Google product surface?
[00:36:55] Somebody should look in turn.
[00:36:58] Yeah.
[00:36:58] And I think for the way it'll change how we live and work,
[00:37:03] SPEAKER_01: I think we're working on these technologies.
[00:37:09] SPEAKER_01: I've already seen how it changes the way we work right,
[00:37:11] SPEAKER_01: because we obviously use them a lot.
[00:37:15] SPEAKER_01: I'm getting married.
[00:37:16] SPEAKER_01: Our Save the Dates with our model.
[00:37:18] SPEAKER_01: And so what I really think we'll see is and just work.
[00:37:23] SPEAKER_01: The amount, part of I think the reason
[00:37:25] SPEAKER_01: that the innovation has accelerated
[00:37:28] SPEAKER_01: is we have these models.
[00:37:30] SPEAKER_01: You have like code assistance.
[00:37:32] SPEAKER_01: You have just like you can use models to like filter things
[00:37:36] SPEAKER_01: to analyze huge amounts of data.
[00:37:38] SPEAKER_01: Like it's drastically increased our own workflows.
[00:37:41] SPEAKER_01: Like what I can do this year versus two years ago
[00:37:45] SPEAKER_01: is just like an order of magnitude more work.
[00:37:48] SPEAKER_01: And I think that's true of the tech industry.
[00:37:51] SPEAKER_01: It's not true of a lot of other industries
[00:37:53] SPEAKER_01: just because that integration into their workflows
[00:37:56] SPEAKER_01: or into their tooling hasn't happened.
[00:38:01] So I think you know some people are like, oh,
[00:38:04] it's going to replace me.
[00:38:06] SPEAKER_01: But at least what I've seen is it really just actually
[00:38:09] SPEAKER_01: changes the amount of work and individual can get done.
[00:38:11] SPEAKER_01: What that means like for businesses or economically,
[00:38:14] SPEAKER_01: I'm not sure.
[00:38:15] SPEAKER_01: But I think it means we will just see people
[00:38:16] SPEAKER_01: be more empowered to hopefully do more in the same time.
[00:38:20] SPEAKER_01: Like maybe you don't have to, you know,
[00:38:22] SPEAKER_01: I friends who are in consulting and spent a lot of time,
[00:38:24] SPEAKER_01: they're like, I just spend a lot of time like two hours
[00:38:26] SPEAKER_01: making slides tweaking.
[00:38:28] SPEAKER_01: Moving logos.
[00:38:29] SPEAKER_01: Moving logos around.
[00:38:30] SPEAKER_01: And like hopefully they won't have to do that.
[00:38:33] SPEAKER_01: They can actually spend time thinking about what the content
[00:38:36] SPEAKER_01: of the slides like should be thinking working with clients.
[00:38:40] SPEAKER_01: And I think that that's hopefully what we will see
[00:38:43] SPEAKER_01: in like one to two years.
[00:38:45] Given the trajectory that you see in these capabilities,
[00:38:47] SPEAKER_02: are there interesting areas that you think
[00:38:49] SPEAKER_02: startups should go do that Google itself might not get into?
[00:38:54] I think there's a ton of spaces, even just
[00:38:57] SPEAKER_00: in the creative tools.
[00:38:58] SPEAKER_00: Like I think there's a ton of room for people
[00:39:01] SPEAKER_00: to figure out like what do these UIs of the future look like?
[00:39:04] SPEAKER_00: Like what is the creative control?
[00:39:05] SPEAKER_00: How do you bring everything together?
[00:39:07] SPEAKER_00: We see a lot of people in the creative field work
[00:39:10] SPEAKER_00: across LLM's image video and music in a way
[00:39:14] SPEAKER_00: where they have to go to four separate tools
[00:39:16] SPEAKER_00: to be able to do that.
[00:39:17] SPEAKER_00: So like a lot of people ideate with LLM's, right?
[00:39:21] SPEAKER_00: Like give me some concepts, like use an idea that I have.
[00:39:24] SPEAKER_00: Once you're happy with that, you take it to an image model.
[00:39:27] SPEAKER_00: You start to think about where are the keyframes that I
[00:39:29] SPEAKER_00: want to have in my video.
[00:39:30] SPEAKER_00: You spend a lot of time iterating there.
[00:39:32] SPEAKER_00: Then you take it to a video model, which is yet another surface.
[00:39:35] SPEAKER_00: And then at some point you want to have sound and music
[00:39:38] SPEAKER_00: and mix it all together.
[00:39:39] SPEAKER_00: And then you actually want to do maybe some heavy handed editing
[00:39:42] SPEAKER_00: and you go to some of the traditional software tools.
[00:39:45] SPEAKER_00: That feels like these kind of workflow-based tools
[00:39:48] SPEAKER_00: are probably going to spin up for a lot of different verticals.
[00:39:51] SPEAKER_00: So creative activity is just one example of it.
[00:39:54] SPEAKER_00: But maybe there might be one for consultants
[00:39:56] SPEAKER_00: so that you can more efficiently make slides
[00:39:58] SPEAKER_00: to some presentation and pitch decks to clients.
[00:40:01] SPEAKER_00: And so I think there's a lot of opportunity there
[00:40:04] SPEAKER_00: that some of the companies may not go into.
[00:40:08] SPEAKER_01: There's a lot of how do we make this technology useful
[00:40:11] SPEAKER_01: for X workflow, right?
[00:40:13] SPEAKER_01: Like sales, finite, like I'm saying a lot of things
[00:40:18] SPEAKER_01: I don't know about in companies like financial workflows.
[00:40:20] SPEAKER_01: But I imagine there's a lot of tasks that could be automated,
[00:40:24] SPEAKER_01: could be made much more efficient.
[00:40:28] SPEAKER_01: And I think startups are in a good position
[00:40:30] SPEAKER_01: to really go understand the specific client use case need,
[00:40:34] SPEAKER_01: that niche need, and do that application layer, right,
[00:40:38] SPEAKER_01: versus what we really focus on is the fundamental technology.
[00:40:43] SPEAKER_01: I think I'm just really excited by the number of people
[00:40:48] SPEAKER_01: who've been excited by this model.
[00:40:52] SPEAKER_01: If that makes sense, like a lot of people in my life,
[00:40:55] SPEAKER_01: like a lot of aunts, uncles, parents, like friends,
[00:40:58] SPEAKER_01: like they've used chatbots, they ask it things,
[00:41:02] SPEAKER_01: they get information, my mom loves to ask chatbots health
[00:41:05] SPEAKER_01: about health information.
[00:41:07] SPEAKER_01: But there's something about like visual media
[00:41:10] SPEAKER_01: that really excites people that it's like the fun thing,
[00:41:13] SPEAKER_01: but it's not just fun, it's exciting, it's intuitive.
[00:41:17] SPEAKER_01: The visual space is so much of how we as humans experience life
[00:41:21] SPEAKER_01: that I think I've loved how much it's moved people.
[00:41:25] SPEAKER_01: Like emotionally and excitement wise,
[00:41:29] SPEAKER_01: I think that's been the most exciting part of this for me.
[00:41:32] My kids love it.
[00:41:33] SPEAKER_02: Yeah.
[00:41:34] SPEAKER_02: My three-year-old son tied our dog leash,
[00:41:38] SPEAKER_02: which is this like fraying, brown rope over himself.
[00:41:43] SPEAKER_02: So he looked like a warrior, I took a picture of him,
[00:41:45] SPEAKER_02: and turned him into this warrior super hero.
[00:41:47] SPEAKER_02: Yeah, exactly.
[00:41:48] SPEAKER_02: And it makes him feel super human.
[00:41:50] SPEAKER_02: And my husband will read, so he's Google Storybook
[00:41:54] SPEAKER_02: to read him these stories about lessons
[00:41:57] SPEAKER_02: that he learned in school.
[00:41:59] SPEAKER_02: If there was an incident on the playground with another kid
[00:42:03] SPEAKER_02: or adjusting to a new school, and it's made these characters
[00:42:07] SPEAKER_02: that look like him and my husband and me and our dog
[00:42:11] SPEAKER_02: and our daughter in these fun stories and lessons
[00:42:16] SPEAKER_02: that we're trying to teach him to the personalization
[00:42:18] SPEAKER_02: that you talked about.
[00:42:19] SPEAKER_02: So I really, really love this future.
[00:42:20] SPEAKER_02: It's going to be totally different, growing up.
[00:42:23] SPEAKER_02: And it's awesome, right?
[00:42:24] SPEAKER_00: Because this is a story for one or five people
[00:42:27] SPEAKER_00: that you would have never had made.
[00:42:30] SPEAKER_00: And other people probably don't want to read it.
[00:42:33] SPEAKER_00: And I would love to if you wanted to.
[00:42:34] SPEAKER_00: Yeah.
[00:42:36] SPEAKER_00: But I think we're really now making it possible
[00:42:38] SPEAKER_00: to tell stories that you never could.
[00:42:40] SPEAKER_00: And in a way, where the camera allowed
[00:42:43] SPEAKER_00: anyone to capture reality when it became very accessible,
[00:42:46] SPEAKER_00: you're kind of capturing people's imagination.
[00:42:49] SPEAKER_00: You're giving them the tools to be able to get the stuff
[00:42:52] SPEAKER_00: that's in their brain, out on paper, visually,
[00:42:55] SPEAKER_00: in a way that they just couldn't before
[00:42:57] SPEAKER_00: because they didn't have the tools
[00:42:59] SPEAKER_00: or they didn't have the knowledge of the tools.
[00:43:01] SPEAKER_00: Like that's been really awesome.
[00:43:02] SPEAKER_00: That's a nice way to put it.
[00:43:04] Thank you so much.
[00:43:05] SPEAKER_00: Thank you for having us.
[00:43:06] SPEAKER_03: It was awesome to have you.