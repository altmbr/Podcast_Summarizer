# #38 Karol Hausman & Kevin Black: Building A Brain For Any Robot | AI Eating The Physical World

**Podcast:** One-off Episodes
**Date:** 2025-10-21
**Video ID:** qeOvHh4wxhs
**Video URL:** https://www.youtube.com/watch?v=qeOvHh4wxhs

---

[00:00:00] The biggest bottleneck to the entire field of robotics
[00:00:03] SPEAKER_00: is intelligence.
[00:00:04] SPEAKER_00: Today I'm sitting there with Carl Osman
[00:00:06] SPEAKER_00: and Kevin Black from Physical Intelligence.
[00:00:08] SPEAKER_00: Carl is a company's co-founder and CEO
[00:00:10] SPEAKER_00: and Kevin is on the research team over there.
[00:00:12] SPEAKER_00: Physical intelligence also known as PI
[00:00:14] SPEAKER_00: in the robotics industry are building robot
[00:00:16] SPEAKER_00: foundational models and they're goals to build a model
[00:00:18] SPEAKER_00: that can control any robot to do any task.
[00:00:21] SPEAKER_00: If you have a laundry folding robot in your home,
[00:00:23] SPEAKER_01: like if it drops an underwear like one in every 100 times,
[00:00:28] SPEAKER_01: one in every thousand times,
[00:00:29] SPEAKER_01: like you know it's okay, it's still really useful.
[00:00:31] SPEAKER_00: They're on a mission to truly solve physical intelligence.
[00:00:34] SPEAKER_00: They've put together a world-class team of researchers
[00:00:37] SPEAKER_00: and scientists rooted at Stanford University.
[00:00:40] SPEAKER_00: It raised over $400 million from the likes of OpenAI,
[00:00:44] SPEAKER_00: Lux Capital, Thrive Capital, and more.
[00:00:46] SPEAKER_00: They are doing some truly groundbreaking work
[00:00:48] SPEAKER_00: and they're gonna be a key enabling technology
[00:00:50] SPEAKER_00: for us to create more decentralized production
[00:00:52] SPEAKER_00: into decentralized the real economy.
[00:00:54] SPEAKER_00: I hope you enjoy the conversation.
[00:00:55] SPEAKER_00: To remember to go direct.
[00:00:59] Go!
[00:01:00] Go!
[00:01:02] Go!
[00:01:04] Carl, Kevin, how are you doing today?
[00:01:07] Good, thank you for having us.
[00:01:09] SPEAKER_02: Pretty good.
[00:01:09] SPEAKER_02: Great, cool, I'm excited to have you guys on the pod
[00:01:14] SPEAKER_00: and you know, been following PI's work for a little while now,
[00:01:17] SPEAKER_00: so I've been excited to have this conversation.
[00:01:19] SPEAKER_00: So I'm just gonna kind of read PI's stated goal,
[00:01:23] SPEAKER_00: which is to build a model that can control any robot
[00:01:26] SPEAKER_00: to do any task.
[00:01:28] Pretty audacious goal to really solve
[00:01:31] the whole concept of physical intelligence.
[00:01:34] SPEAKER_00: And obviously the whole reason why having this conversation
[00:01:38] SPEAKER_00: is well done for going direct is this is really just
[00:01:40] SPEAKER_00: the heartbeat of a decentralized real economy,
[00:01:42] SPEAKER_00: which is decentralized production of which
[00:01:44] SPEAKER_00: you are the foundation of a foundational piece
[00:01:46] SPEAKER_00: of what will enable decentralized production.
[00:01:49] SPEAKER_00: So thanks again for taking the time.
[00:01:51] Thank you.
[00:01:52] SPEAKER_02: Yeah, thank you.
[00:01:53] SPEAKER_02: All right, so this is all about right turning modern robotics
[00:01:56] SPEAKER_00: into a generalized technology platform.
[00:01:58] SPEAKER_00: And so for the non robotics researchers out there,
[00:02:02] SPEAKER_00: let's maybe just start with this.
[00:02:04] SPEAKER_00: First, I mean, it's a three-parter,
[00:02:07] SPEAKER_00: so I'm gonna state it and I'm gonna take one by one, okay?
[00:02:11] What is a visual language action model?
[00:02:14] And how does that differ from a visual language model?
[00:02:19] Kevin, do you wanna take this one?
[00:02:20] SPEAKER_01: Yeah, yeah, I can take this one.
[00:02:23] SPEAKER_01: I mean, the way I like to explain it is,
[00:02:25] SPEAKER_01: you've got large language models,
[00:02:27] SPEAKER_01: LLMs, which are sort of the first example of
[00:02:30] SPEAKER_01: these models that really when you scale them up
[00:02:33] SPEAKER_01: to billions and billions of parameters
[00:02:34] SPEAKER_01: are able to do very human-like things,
[00:02:36] SPEAKER_01: like answer all sorts of questions, write poetry,
[00:02:39] SPEAKER_01: write code, stuff like that.
[00:02:42] SPEAKER_01: So that was kind of the first and that's trained
[00:02:44] SPEAKER_01: on basically all the text on the internet.
[00:02:46] SPEAKER_01: And then pretty quickly people became interested
[00:02:50] SPEAKER_01: in more like tasks that involves images and videos, right?
[00:02:53] SPEAKER_01: Like you wanna be able to also point your camera at something
[00:02:55] SPEAKER_01: and say, what is this?
[00:02:57] SPEAKER_01: Can you help me make a recipe from these ingredients
[00:03:00] SPEAKER_01: or something?
[00:03:01] SPEAKER_01: So they added essentially an adapter
[00:03:03] SPEAKER_01: to the large language model that lets it take images as input.
[00:03:07] SPEAKER_01: And then they also train it on all sorts of images
[00:03:10] SPEAKER_01: and text from the internet.
[00:03:12] SPEAKER_01: So then that's how you get a vision language model,
[00:03:14] SPEAKER_01: which you mentioned, which you call VLMs usually.
[00:03:16] SPEAKER_01: So the vision language action model,
[00:03:18] SPEAKER_01: which actually started at Google under a Carl Supervision
[00:03:22] SPEAKER_01: was basically taking these VLMs and then adding one more adapter,
[00:03:27] SPEAKER_01: like some sort of component or some way to have them produce
[00:03:30] SPEAKER_01: instead of text or images have them produce robot actions.
[00:03:35] So if you have like a robot or moving the actions
[00:03:38] SPEAKER_01: might be like the position of each joint
[00:03:40] SPEAKER_01: or like the velocity of each joint or something like that.
[00:03:43] SPEAKER_01: And then you just take one of these VLMs
[00:03:45] SPEAKER_01: and you train it out with the actions
[00:03:47] SPEAKER_01: and it turns out to actually work really well.
[00:03:49] SPEAKER_01: You can just control the robot.
[00:03:51] SPEAKER_01: So it's basically images and text in and then actions out.
[00:03:55] And like I said, it was sort of this three stage pipeline
[00:03:57] SPEAKER_01: where first we had the language models
[00:03:59] SPEAKER_01: which are language only then we.
[00:04:01] SPEAKER_01: And when I say like, first we had the language model,
[00:04:03] SPEAKER_01: I mean they literally train it first
[00:04:05] SPEAKER_01: as a language only model.
[00:04:07] SPEAKER_01: Then they add the images.
[00:04:08] SPEAKER_01: So they take an existing language model,
[00:04:10] SPEAKER_01: add the images, turn it into a vision language model.
[00:04:13] SPEAKER_01: Then we take the vision language model
[00:04:14] SPEAKER_01: that's already been trained and add the actions
[00:04:17] SPEAKER_01: and then you get a vision language action model.
[00:04:19] SPEAKER_01: And this is sort of really important for instilling
[00:04:21] SPEAKER_01: the model of general knowledge about like,
[00:04:23] SPEAKER_01: you know what if you say pick up the bottle,
[00:04:25] SPEAKER_01: like what is the bottle?
[00:04:26] SPEAKER_01: It has to know that from its internet free training.
[00:04:31] And now maybe add a little bit more to this
[00:04:33] SPEAKER_02: which is on the high level what we are realizing
[00:04:36] SPEAKER_02: with these large models is that these are
[00:04:39] less of language models for vision language models
[00:04:41] SPEAKER_02: for action models.
[00:04:42] SPEAKER_02: These are just big pattern recognition machines.
[00:04:46] SPEAKER_02: And you can give them a lot of data
[00:04:48] SPEAKER_02: of all kinds of different forms
[00:04:49] SPEAKER_02: and they're able to recognize patterns in that data
[00:04:53] SPEAKER_02: to then produce predictable outputs.
[00:04:55] SPEAKER_02: And if you extrapolate that idea,
[00:04:58] SPEAKER_02: it turns out to be really, really powerful.
[00:05:00] SPEAKER_02: If you apply it to language,
[00:05:01] SPEAKER_02: it results in something like chat GPT.
[00:05:04] If you apply it to vision,
[00:05:06] it results in something that can understand images
[00:05:09] SPEAKER_02: and do it better than the specialized models
[00:05:11] SPEAKER_02: that we've seen in the past.
[00:05:12] SPEAKER_02: So it can do things like describe what's in the image,
[00:05:15] SPEAKER_02: but it can also do some reasoning about the image
[00:05:17] SPEAKER_02: or it could potentially even edit an image.
[00:05:21] SPEAKER_02: And we start saying that you can do the same
[00:05:23] SPEAKER_02: with robotics data as well.
[00:05:25] SPEAKER_02: So now not only you can talk to them,
[00:05:27] SPEAKER_02: they can understand what you see
[00:05:28] SPEAKER_02: or what is being shown in the camera,
[00:05:31] but they can also start outputting actions for the robot.
[00:05:33] SPEAKER_02: Because if it's seen enough,
[00:05:36] SPEAKER_02: if it's so enough patterns on a robotic data,
[00:05:39] SPEAKER_02: it would be able to understand these patterns
[00:05:41] SPEAKER_02: and then output the right actions for a robot.
[00:05:45] And where, when was the actual, would you say,
[00:05:48] SPEAKER_00: kind of, was there a pivotal moment when the VLAs
[00:05:52] SPEAKER_00: started to become a reality,
[00:05:53] SPEAKER_00: like from a technology standpoint?
[00:05:54] SPEAKER_00: Like when did that really start happening
[00:05:56] SPEAKER_00: where you could actually prompt a robotic system
[00:05:59] SPEAKER_00: to do something and it just does it near real time?
[00:06:03] There were a few moments in the past
[00:06:05] SPEAKER_02: where we started seeing some signs that would be possible.
[00:06:09] SPEAKER_02: The one moment that quite a few folks refer to
[00:06:12] SPEAKER_02: is a moment where we run a particular experiment.
[00:06:19] SPEAKER_02: And the experiment is actually like a little bit pathetic.
[00:06:21] SPEAKER_02: So it's not gonna sound really impressive,
[00:06:23] SPEAKER_02: but to us at the time, it was really impressive.
[00:06:26] SPEAKER_02: Which was this setup where we had a robot
[00:06:29] SPEAKER_02: and in front of the robot there was a Coke can.
[00:06:31] SPEAKER_02: And then there were three pictures
[00:06:32] SPEAKER_02: of different celebrities.
[00:06:34] And the prompt was to put the Coke in
[00:06:38] SPEAKER_02: on the picture of Taylor Swift.
[00:06:40] And the caveat was that the robot has never seen
[00:06:44] SPEAKER_02: any data of Taylor Swift.
[00:06:46] SPEAKER_02: So we never collected that data firsthand.
[00:06:49] SPEAKER_02: So it had to transfer that knowledge,
[00:06:51] SPEAKER_02: the concept of Taylor Swift from the internet
[00:06:54] SPEAKER_02: pre-training that it's seen for vision language model
[00:06:57] SPEAKER_02: that it was before.
[00:06:59] And it turned out that it was able to do it.
[00:07:00] SPEAKER_02: So we had this arm very slowly moving arm
[00:07:03] SPEAKER_02: go towards the Coke can, the grasp it
[00:07:05] SPEAKER_02: and then put it on a picture of Taylor Swift.
[00:07:07] SPEAKER_02: And if you see the demo of this,
[00:07:09] SPEAKER_02: it's extremely slow and really pathetic.
[00:07:11] SPEAKER_02: But to us, it really indicated this big shift in that.
[00:07:16] SPEAKER_02: Now no longer robots have to experience
[00:07:18] SPEAKER_02: all of their world firsthand.
[00:07:21] SPEAKER_02: They can get some of that knowledge
[00:07:22] SPEAKER_02: from internet web pre-training.
[00:07:24] SPEAKER_02: And that's set to this trajectory of now.
[00:07:27] SPEAKER_02: How do we make this faster?
[00:07:28] SPEAKER_02: How do we make them a generalized even better?
[00:07:31] SPEAKER_02: And that's what we've been doing at Pi
[00:07:33] SPEAKER_02: and showing that these models can scale very, very well.
[00:07:36] SPEAKER_02: And they can work across many different robots
[00:07:39] SPEAKER_02: to do many different tasks.
[00:07:41] And what year was this?
[00:07:43] The Taylor Swift experiment?
[00:07:48] I think it must have been 23, I think.
[00:07:50] SPEAKER_01: 23?
[00:07:51] SPEAKER_01: Yeah, 22 or not.
[00:07:52] SPEAKER_01: Okay, so recently.
[00:07:54] Yeah, I mean, I think if, you know,
[00:07:56] SPEAKER_01: Carl might be a little biased
[00:07:57] SPEAKER_01: because he was part of this project.
[00:07:58] SPEAKER_01: Like he was called RT2 from Google.
[00:08:00] SPEAKER_01: I mean, I can say I wasn't involved in any of this,
[00:08:04] SPEAKER_01: but I was a PhD student at Berkeley
[00:08:06] SPEAKER_01: and, you know, because my advisor, Sergey Levin,
[00:08:10] SPEAKER_01: is like, he was at Google as well.
[00:08:11] SPEAKER_01: So we were sort of in contact with the RT2 team
[00:08:13] SPEAKER_01: and I actually got to try it in my lab at Berkeley.
[00:08:17] And I was really impressed.
[00:08:19] SPEAKER_01: I mean, I mean, I remember like,
[00:08:20] SPEAKER_01: just giving a random object and being like,
[00:08:22] SPEAKER_01: you know, go pick up the whatever,
[00:08:24] SPEAKER_01: go pick up the toothpaste,
[00:08:25] SPEAKER_01: go pick up like, you know, the wooden bowl
[00:08:27] SPEAKER_01: or the toothbrush.
[00:08:28] SPEAKER_01: And I was like, wow, this is,
[00:08:30] SPEAKER_01: I didn't expect it to actually work in my lab
[00:08:32] SPEAKER_01: with my robot, which is like completely different
[00:08:34] SPEAKER_01: from what they had in the RT2 project.
[00:08:36] SPEAKER_01: So it really was like, you know,
[00:08:38] SPEAKER_01: sort of a moment of where I was feeling impressed.
[00:08:42] SPEAKER_01: Yeah.
[00:08:44] And so just, I'm just kind of just to get into the weeds
[00:08:47] SPEAKER_00: a little bit here.
[00:08:48] SPEAKER_00: So like what actually was it that enabled the ability
[00:08:51] SPEAKER_00: to actually prompt the robot through natural language
[00:08:54] SPEAKER_00: to do that action?
[00:08:55] SPEAKER_00: Like just from a technical standpoint,
[00:08:57] SPEAKER_00: it was fascinating to me.
[00:09:01] I mean, I think I mentioned earlier,
[00:09:02] SPEAKER_01: it was really just the internet retraining,
[00:09:04] SPEAKER_01: like the fact that, you know,
[00:09:05] SPEAKER_01: you see it from a language model,
[00:09:07] SPEAKER_01: which obviously language model knows who Taylor Swift is.
[00:09:09] SPEAKER_01: You know, you ask who is Taylor Swift,
[00:09:11] SPEAKER_01: it'll be able to give you like, you know, a lot of information.
[00:09:14] Then you tack on the vision component
[00:09:16] SPEAKER_01: where it's like, now it's seen pictures of Taylor Swift
[00:09:18] SPEAKER_01: and that knowledge is just inherent in the model weights.
[00:09:21] SPEAKER_01: And I think the part that's sort of,
[00:09:23] SPEAKER_01: you know, non-trivial, that like wasn't obviously true,
[00:09:25] SPEAKER_01: but ended up being true is that now if you start
[00:09:27] SPEAKER_01: tacking on robot actions,
[00:09:29] SPEAKER_01: it does preserve that knowledge
[00:09:30] SPEAKER_01: and it's able to make the connection,
[00:09:32] SPEAKER_01: which is like, this is the picture Taylor Swift.
[00:09:34] SPEAKER_01: These are the actions that move towards Taylor Swift.
[00:09:37] SPEAKER_01: You know, it's actually kind of like,
[00:09:39] perhaps a little surprising that this works so well,
[00:09:41] SPEAKER_01: that it can preserve that knowledge
[00:09:43] SPEAKER_01: and also translate it into a robotics context,
[00:09:45] SPEAKER_01: you know, versus like sort of a pure,
[00:09:48] SPEAKER_01: semantic knowledge context.
[00:09:51] Yeah, and I think the truth is,
[00:09:53] SPEAKER_02: we don't fully understand why it works so well
[00:09:56] SPEAKER_02: and how exactly it works.
[00:09:58] It just turns out that if you have this very generalized
[00:10:01] SPEAKER_02: pattern recognition machine that we've been able to build
[00:10:05] SPEAKER_02: for language mostly,
[00:10:07] SPEAKER_02: if you add more data to it, it starts to generalize
[00:10:10] SPEAKER_02: and it starts to really make connections
[00:10:13] SPEAKER_02: between these different modalities.
[00:10:15] SPEAKER_02: It can make connections between text and images
[00:10:17] SPEAKER_02: and now also robot actions.
[00:10:20] So that was the surprising element
[00:10:21] SPEAKER_02: and that's why I think it was so significant to us
[00:10:24] SPEAKER_02: because none of us really, usually when you do robotic research,
[00:10:27] SPEAKER_02: you aim for a certain capability
[00:10:30] and then when you observe it,
[00:10:32] SPEAKER_02: it's not a surprise because you've been aiming for it
[00:10:34] SPEAKER_02: and you've been developing everything for it.
[00:10:36] Here, I think the significance of it was that
[00:10:39] SPEAKER_02: it was surprising to all of us
[00:10:41] and that doesn't happen very often.
[00:10:44] You might even say emergent, right?
[00:10:45] SPEAKER_01: This is the word that people love to use these days.
[00:10:48] SPEAKER_01: Like, oh, you scale something up
[00:10:49] SPEAKER_01: and suddenly the scalability emerges that you weren't expecting.
[00:10:55] SPEAKER_00: So I recently listened to Sergei in a interview
[00:11:01] SPEAKER_00: and he was discussing kind of the VLA that Pi has developed
[00:11:08] SPEAKER_00: and I believe it's, he's the term I have listed here,
[00:11:10] SPEAKER_00: action expert or decoder if I'm not mistaken.
[00:11:14] SPEAKER_00: So can you just explain to the audience a little bit more?
[00:11:17] SPEAKER_00: I know figures has their helix,
[00:11:19] SPEAKER_00: which is their own version of a VLA
[00:11:21] SPEAKER_00: and just kind of from a first principle standpoint,
[00:11:24] SPEAKER_00: maybe the difference in your approach
[00:11:27] SPEAKER_00: and what you're building at Pi.
[00:11:31] Yeah, I can talk a little bit about the action expert.
[00:11:34] SPEAKER_01: That was sort of like a, you know,
[00:11:37] when we were first developing our models at Pi,
[00:11:40] SPEAKER_01: we had a smaller non-VLA model, I would call it,
[00:11:43] SPEAKER_01: like it wasn't based on a language model.
[00:11:46] And I think that we believe the VLA's work,
[00:11:49] SPEAKER_01: so sort of the challenge was like,
[00:11:51] SPEAKER_01: how do we turn this into a VLA?
[00:11:54] SPEAKER_01: And specifically the reason we couldn't just do exactly
[00:11:56] SPEAKER_01: what RT2 did is because we had much more
[00:11:59] SPEAKER_01: dexterity that we required.
[00:12:02] SPEAKER_01: Like, Carl mentioned, you know,
[00:12:04] SPEAKER_01: that the co-can demo, while I was very impressive,
[00:12:06] SPEAKER_01: like also looked kind of bad
[00:12:09] SPEAKER_01: because the arm was like going really slowly
[00:12:11] SPEAKER_01: and I think it actually knocks over the co-can.
[00:12:12] SPEAKER_01: So like it had the semantic component
[00:12:14] SPEAKER_01: but not really like the dexterity component.
[00:12:16] SPEAKER_01: And at Pi, I think we really wanted to make sure
[00:12:18] SPEAKER_01: we could hit our dexterity goals,
[00:12:20] SPEAKER_01: like folding laundry and stuff like that.
[00:12:23] Uncreated meaning that the control frequency
[00:12:25] SPEAKER_01: is very high, like our robots ran at like 50 hertz.
[00:12:28] SPEAKER_01: Or I think RT2 would run at like five hertz or something
[00:12:31] SPEAKER_01: like that.
[00:12:33] So that was the challenge.
[00:12:34] SPEAKER_01: And that really is like what actually led
[00:12:36] SPEAKER_01: to the action expert architecture,
[00:12:38] SPEAKER_01: which is, you know, if you tried to get it
[00:12:40] SPEAKER_01: to output those actions directly, like RT2 did,
[00:12:45] SPEAKER_01: it just didn't work, it was very slow
[00:12:47] SPEAKER_01: and also trained poorly.
[00:12:49] So the action actor was just like,
[00:12:51] SPEAKER_01: oh, it's like a smaller, it's a modification to the model.
[00:12:55] Sort of like in order to turn an LLM into a VLAM,
[00:12:58] SPEAKER_01: you have to add an image encoder,
[00:12:59] SPEAKER_01: like something that specialized to handle images.
[00:13:02] SPEAKER_01: We added a new component, which we call the action expert,
[00:13:05] SPEAKER_01: which is just a smaller set of weights
[00:13:07] SPEAKER_01: that specifically adapted to handle actions.
[00:13:11] And that's what ended up sort of working well,
[00:13:14] SPEAKER_01: getting both the semantic capabilities of like,
[00:13:16] SPEAKER_01: you know, put the cocaine on Taylor,
[00:13:17] SPEAKER_01: so it's kind of stuff,
[00:13:18] SPEAKER_01: but also the dexterity of like,
[00:13:19] SPEAKER_01: outputting high frequency actions.
[00:13:22] SPEAKER_01: I should also mention that like in parallel,
[00:13:24] SPEAKER_01: we were, you know, we were also exploring other things,
[00:13:26] SPEAKER_01: like different representations of actions.
[00:13:29] So we ended up also coming up with a different method called
[00:13:32] SPEAKER_01: fast, which is basically a way to transform the actions
[00:13:37] SPEAKER_01: so you can directly train on them
[00:13:40] SPEAKER_01: without needing an action expert.
[00:13:42] SPEAKER_01: And that was slower at inference time,
[00:13:45] SPEAKER_01: but it was faster at training time,
[00:13:47] SPEAKER_01: whereas the action expert was faster at inference time,
[00:13:50] SPEAKER_01: the slower at training time.
[00:13:51] SPEAKER_01: So then we actually just combined both of them.
[00:13:52] SPEAKER_01: And now we use both,
[00:13:53] SPEAKER_01: and that's sort of like our latest recipe
[00:13:56] SPEAKER_01: that you can read about in our paper.
[00:13:57] SPEAKER_01: And that works really well.
[00:13:59] Well, and how big is the team now?
[00:14:02] We are a little over 40 people.
[00:14:05] Okay, great.
[00:14:07] SPEAKER_00: All right, so you open source your first model, Pi0.
[00:14:10] SPEAKER_00: And why don't you get your perspective on this,
[00:14:11] SPEAKER_00: because I will talk about Pi0.5.
[00:14:15] SPEAKER_00: 0.5 is that correct?
[00:14:19] So talk to me a little bit about your approach
[00:14:22] SPEAKER_00: to kind of open source first closed
[00:14:25] SPEAKER_00: and kind of around IP and kind of,
[00:14:27] SPEAKER_00: and just talk to me about how you guys think about that.
[00:14:30] SPEAKER_00: Yeah, it was a really intentional decision.
[00:14:34] And I think it really comes from truly internalizing
[00:14:39] SPEAKER_02: what is the biggest risk here?
[00:14:40] SPEAKER_02: And I don't think many people really internalize that.
[00:14:44] And to us, it's very, very clear.
[00:14:46] SPEAKER_02: The biggest risk here is the scientific risk,
[00:14:48] SPEAKER_02: is that the problem is just too hard,
[00:14:50] SPEAKER_02: and it's going to take 30 years instead of like three years.
[00:14:56] SPEAKER_02: And we're off in that estimate.
[00:14:59] So if that's the biggest risk,
[00:15:01] SPEAKER_02: we want to do everything we can to burn it down
[00:15:04] SPEAKER_02: as much as we can.
[00:15:06] And in other words, we are trying to increase the probability
[00:15:11] SPEAKER_02: of the problem being solved as much as we can.
[00:15:13] SPEAKER_02: Because if it is solved,
[00:15:14] SPEAKER_02: then we get to capture some of the value.
[00:15:17] SPEAKER_02: Other players get to capture some of the value,
[00:15:18] SPEAKER_02: but if it's not solved, and none of us captures any value,
[00:15:22] there is no value being created.
[00:15:25] And open sourcing a model,
[00:15:26] SPEAKER_02: because we are so early,
[00:15:27] SPEAKER_02: and this is still the biggest risk,
[00:15:29] SPEAKER_02: increases the probability.
[00:15:31] SPEAKER_02: It allows other people to experience these models,
[00:15:34] SPEAKER_02: to align with our vision,
[00:15:35] SPEAKER_02: of how this problem should be solved,
[00:15:37] SPEAKER_02: contribute to them, make them better.
[00:15:40] Also helps us evaluate these models.
[00:15:42] SPEAKER_02: As these models get more and more capable,
[00:15:45] SPEAKER_02: it becomes quite difficult for us
[00:15:46] SPEAKER_02: to know what their capabilities are.
[00:15:48] SPEAKER_02: We see the same with large language models,
[00:15:51] SPEAKER_02: where now you can release them in a product,
[00:15:53] SPEAKER_02: and often you don't know,
[00:15:54] SPEAKER_02: you think that it's a very good model,
[00:15:56] SPEAKER_02: but then you get a vibe check from the users,
[00:15:59] SPEAKER_02: telling you that it's actually not as good as you thought it was,
[00:16:02] SPEAKER_02: or the other way around.
[00:16:03] And we start to see something similar here,
[00:16:05] SPEAKER_02: where the better the model,
[00:16:07] SPEAKER_02: the harder it is to evaluate it,
[00:16:09] SPEAKER_02: because now you can evaluate it across many different robots,
[00:16:11] SPEAKER_02: across many different tasks.
[00:16:13] SPEAKER_02: For each task,
[00:16:14] SPEAKER_02: you need to run it many, many times
[00:16:15] SPEAKER_02: to understand how good it is.
[00:16:17] SPEAKER_02: By open sourcing it,
[00:16:18] SPEAKER_02: we basically allow anybody to play with it,
[00:16:22] SPEAKER_02: and tell us how it went.
[00:16:24] SPEAKER_02: And we've seen many, many more applications
[00:16:26] SPEAKER_02: that we could have foreseen just here in AtPi.
[00:16:30] SPEAKER_02: We've seen these models being used for surgical robots,
[00:16:32] SPEAKER_02: for autonomous cars, for drones,
[00:16:35] SPEAKER_02: for all kinds of different things,
[00:16:37] SPEAKER_02: and seeing that this model can help in those applications,
[00:16:42] SPEAKER_02: really allows us to better understand the capabilities,
[00:16:44] SPEAKER_02: and where it's still falling short.
[00:16:49] And where does the,
[00:16:50] SPEAKER_00: is there a discord or everything you send GitHub?
[00:16:53] SPEAKER_00: Like where does the developer community hang out
[00:16:55] SPEAKER_00: that's active on the Pi Cloud,
[00:16:57] SPEAKER_00: or on the, that works with the Pi foundational model?
[00:17:01] Mostly GitHub.
[00:17:03] Okay. Yeah, we have an open source repo called OpenPi,
[00:17:07] SPEAKER_01: or we release everything,
[00:17:08] SPEAKER_01: and we try to help people,
[00:17:09] SPEAKER_01: people leave issues,
[00:17:10] SPEAKER_01: and we try to help them get the model working,
[00:17:11] SPEAKER_01: and stuff like that.
[00:17:13] Cool.
[00:17:14] All right.
[00:17:15] So you're obviously focused on building the foundational model
[00:17:19] SPEAKER_00: for robotics.
[00:17:21] SPEAKER_00: How do you think about,
[00:17:23] SPEAKER_00: as you're kind of going forward,
[00:17:26] SPEAKER_00: hardware and building your own machines,
[00:17:28] SPEAKER_00: or robotics systems,
[00:17:30] SPEAKER_00: versus staying really focused on kind of the intelligence layer?
[00:17:33] Yeah, that's a good question.
[00:17:36] SPEAKER_02: It's something where our thoughts have been evolving.
[00:17:39] Initially, when we were starting the company,
[00:17:41] the thought was that maybe we didn't need to build hardware.
[00:17:44] SPEAKER_02: There was so much hardware out there,
[00:17:46] SPEAKER_02: there's so many companies focusing explicitly
[00:17:48] SPEAKER_02: on building hardware,
[00:17:50] SPEAKER_02: that we can just buy that hardware,
[00:17:51] SPEAKER_02: train on that data that we collect with that hardware,
[00:17:53] SPEAKER_02: or even get that data from other partners,
[00:17:56] SPEAKER_02: and just focus on building the intelligence layer.
[00:17:59] We still believe that the biggest bottleneck
[00:18:01] SPEAKER_02: to the entire field of robotics is intelligence.
[00:18:06] SPEAKER_02: It has always been intelligence,
[00:18:07] SPEAKER_02: and I think it is going to be intelligence
[00:18:09] SPEAKER_02: for a very, very long time.
[00:18:11] So we believe that the biggest value unlock
[00:18:14] SPEAKER_02: we can provide is by solving that problem.
[00:18:17] Now, in the meantime,
[00:18:19] SPEAKER_02: we do see that by being at the very forefront of these models,
[00:18:23] SPEAKER_02: we kind of understand what hardware we can build
[00:18:26] SPEAKER_02: so that it really emphasizes where the models are at.
[00:18:29] SPEAKER_02: We know where the capabilities of these models are,
[00:18:32] SPEAKER_02: we know where they're going,
[00:18:33] SPEAKER_02: we know how to push the frontier of these models.
[00:18:36] So we are starting to build more and more hardwareing house,
[00:18:40] but I think we're going to go for both strategies
[00:18:42] SPEAKER_02: at the same time,
[00:18:43] SPEAKER_02: where we'll be building some of that hardwareing house,
[00:18:46] SPEAKER_02: but at the same time, we want to leverage the fact
[00:18:48] SPEAKER_02: that these are very general purpose models,
[00:18:50] SPEAKER_02: so they can control really any hardware,
[00:18:52] SPEAKER_02: and they don't care what are,
[00:18:54] SPEAKER_02: you build a hardwareing house,
[00:18:55] SPEAKER_02: whether it's somewhere else,
[00:18:56] SPEAKER_02: whether it has two arms or three arms,
[00:18:58] SPEAKER_02: whether it's a humanoid with legs,
[00:19:00] SPEAKER_02: or a wheeled humanoid, or a car, or a drone,
[00:19:02] SPEAKER_02: they can really absorb data from all of these
[00:19:05] SPEAKER_02: different form factors that control all of them.
[00:19:08] SPEAKER_02: So I think it will be a two-path strategy
[00:19:11] SPEAKER_02: where we can build platforms to show people
[00:19:14] SPEAKER_02: how good these models are,
[00:19:15] SPEAKER_02: and at the same time,
[00:19:16] SPEAKER_02: allow them to deploy it on their own hardware.
[00:19:21] Kevin, what's your thought on it?
[00:19:23] Yeah, I mean, I think Ezra Robotics Researcher,
[00:19:25] SPEAKER_01: the way I see hardware is sort of as an accelerant.
[00:19:28] SPEAKER_01: I mean, I don't work on the hardware side at all.
[00:19:30] SPEAKER_01: I only touch the model and maybe some code,
[00:19:33] SPEAKER_01: but I'm always really excited to get updates
[00:19:35] SPEAKER_01: on the hardware team,
[00:19:36] SPEAKER_01: because I'm like, wow, we have this,
[00:19:38] SPEAKER_01: it's lighter, it's faster, it's more stable.
[00:19:41] SPEAKER_01: Maybe we can do some cooler tasks.
[00:19:44] SPEAKER_01: Maybe it'll just be easier to put more data.
[00:19:47] It'll just easier to work with,
[00:19:48] SPEAKER_01: because I often, actually, as a researcher,
[00:19:50] SPEAKER_01: sit in front of the robot and watch it do stuff
[00:19:53] SPEAKER_01: and debug things and do all this stuff.
[00:19:55] SPEAKER_01: So I think the better the hardware is,
[00:19:57] SPEAKER_01: sort of the faster we can go
[00:19:59] SPEAKER_01: and the more interesting things we can explore,
[00:20:00] SPEAKER_01: but it's not strictly necessary in the sense that,
[00:20:04] SPEAKER_01: I think you can do really good Robotics Research
[00:20:06] SPEAKER_01: on kind of crappy hardware.
[00:20:09] SPEAKER_01: It might be slower, but the bottleneck
[00:20:11] SPEAKER_01: is more the intelligence.
[00:20:14] It's always better, of course, for things that go smoother
[00:20:16] SPEAKER_01: and to be able to do more iterations
[00:20:18] SPEAKER_01: on the model and stuff like that.
[00:20:19] SPEAKER_01: And this is something that is quite nuanced.
[00:20:21] SPEAKER_02: I think we're probably gonna enter a new era
[00:20:24] SPEAKER_02: of robotic hardware.
[00:20:25] SPEAKER_02: The hardware of the past is really, really expensive,
[00:20:28] SPEAKER_02: because it needs to be extremely precise.
[00:20:31] SPEAKER_02: So the robots that you buy,
[00:20:32] SPEAKER_02: the traditional automation robots
[00:20:34] SPEAKER_02: that are using industrial automation,
[00:20:37] SPEAKER_02: these are really expensive machines.
[00:20:39] SPEAKER_02: And the reason is that the only way we can have them work
[00:20:43] SPEAKER_02: is by going very precisely to a very specific point,
[00:20:46] SPEAKER_02: and if they make any mistake, basically it's irrecoverable.
[00:20:50] SPEAKER_02: So they need to be able to get to that point
[00:20:52] SPEAKER_02: with sub-millimeter precision
[00:20:54] SPEAKER_02: and the higher the precision, the higher the cost
[00:20:56] SPEAKER_02: for these robots.
[00:20:58] SPEAKER_02: We see that if you have better levels of intelligence,
[00:21:03] SPEAKER_02: it actually allows your hardware to be a little bit more crappy
[00:21:06] SPEAKER_02: because intelligence can accommodate for that.
[00:21:09] You, as a person, your own hardware
[00:21:12] SPEAKER_02: is not nearly as precise as modern industrial robot hardware.
[00:21:15] SPEAKER_02: If I were to ask you to put your fingers
[00:21:17] SPEAKER_02: in exact same spot, 100 times in a row,
[00:21:21] SPEAKER_02: the error on that would be fairly large.
[00:21:23] SPEAKER_02: But because you have very good physical intelligence,
[00:21:26] SPEAKER_02: you can adjust that position based on the visual feedback
[00:21:30] SPEAKER_02: or tactile feedback that you're getting from the environment.
[00:21:33] SPEAKER_02: So even though your hardware is much more crappy, in a sense,
[00:21:37] SPEAKER_02: it's actually much more capable
[00:21:38] SPEAKER_02: because intelligence can accommodate for it.
[00:21:41] And I believe this is something we're going to start seeing
[00:21:44] SPEAKER_02: in the robotics industry as well.
[00:21:46] SPEAKER_02: For instance, some of the demos we are showing,
[00:21:49] SPEAKER_02: where we are showing robots doing some of the most complex tasks
[00:21:52] SPEAKER_02: we've ever seen on robots, like floating laundry
[00:21:54] SPEAKER_02: or lighting a candle, busing tables,
[00:21:58] SPEAKER_02: and all kinds of different things,
[00:22:00] SPEAKER_02: we do this on very crappy hardware.
[00:22:03] SPEAKER_02: On the hardware that has a lot of backlash,
[00:22:05] SPEAKER_02: it's not very well calibrated.
[00:22:07] SPEAKER_02: And traditionally, you wouldn't expect these kind of hubbest
[00:22:10] SPEAKER_02: machines to be able to do anything near that level of the
[00:22:13] SPEAKER_02: austerity.
[00:22:15] SPEAKER_02: But it turns out that with the right visual feedback,
[00:22:18] SPEAKER_02: you can do a lot.
[00:22:19] And I suspect that that's what's going to happen
[00:22:21] SPEAKER_02: with robotic hardware industry as well.
[00:22:23] SPEAKER_02: We'll start seeing my cheaper robots
[00:22:25] SPEAKER_02: so they're much more capable.
[00:22:28] Yeah, that's true.
[00:22:29] SPEAKER_01: I mean, I think when I say good robot, I think good hardware,
[00:22:33] SPEAKER_01: actually means something very different than a traditional
[00:22:35] SPEAKER_01: roboticist.
[00:22:36] SPEAKER_01: The thing is, I've never worked as a traditional robotist.
[00:22:39] SPEAKER_01: I don't even calibration.
[00:22:40] SPEAKER_01: I don't even know what that means.
[00:22:42] SPEAKER_01: What I care about is, is it easy to use?
[00:22:45] SPEAKER_01: Is it reliable?
[00:22:47] SPEAKER_01: Will it like, will a motor just burn out
[00:22:49] SPEAKER_01: while I'm doing my e-vals?
[00:22:51] SPEAKER_01: And as long as it's stable, easy to use,
[00:22:53] SPEAKER_01: then I'm really happy, right?
[00:22:54] SPEAKER_01: And maybe if it has some capability that lets it
[00:22:58] SPEAKER_01: do cooler tasks.
[00:22:59] SPEAKER_01: But that has nothing to do with, like Carl said,
[00:23:01] SPEAKER_01: these traditional ideas of repeatability
[00:23:03] SPEAKER_01: and having really fast e-stops that can activate in 10 milliseconds
[00:23:09] SPEAKER_01: or something.
[00:23:10] SPEAKER_01: That really doesn't matter as much when you're working on learn
[00:23:12] SPEAKER_01: models.
[00:23:14] Sure.
[00:23:16] So how do you think about yourself in the ecosystem?
[00:23:20] SPEAKER_00: So is it kind of end-to-end operators,
[00:23:25] SPEAKER_00: is it general platform?
[00:23:27] SPEAKER_00: Are you looking at like, partner with anyone
[00:23:29] SPEAKER_00: else building different parts of the ecosystem?
[00:23:31] SPEAKER_00: How should people think about kind of how
[00:23:34] SPEAKER_00: to work with pie or, yeah?
[00:23:36] SPEAKER_00: I don't know.
[00:23:37] SPEAKER_00: Yeah, I think first we need to acknowledge
[00:23:39] SPEAKER_02: that the ecosystem is very, very early.
[00:23:41] SPEAKER_02: And it barely exists today.
[00:23:44] I think that the ecosystem is going to get much, much bigger.
[00:23:47] SPEAKER_02: And we want to contribute to that.
[00:23:48] SPEAKER_02: We want to create that ecosystem.
[00:23:50] SPEAKER_02: We want to get to the point where, as soon as you have hardware
[00:23:54] SPEAKER_02: or have an idea of how to automate something,
[00:23:58] SPEAKER_02: you would be able to very quickly spin that up.
[00:24:00] SPEAKER_02: The intelligence will be there ready for you.
[00:24:02] SPEAKER_02: And you would be able to automate your tasks very, very quickly.
[00:24:06] Right now, if you wanted to tackle a new problem
[00:24:10] SPEAKER_02: in automation or in robotics, you basically
[00:24:12] SPEAKER_02: need to start a new company.
[00:24:14] SPEAKER_02: You need to build your own hardware for it.
[00:24:16] SPEAKER_02: You need to hire a software team for it.
[00:24:18] SPEAKER_02: You need to train your own models for it.
[00:24:20] SPEAKER_02: You need to connect all of these pipelines together.
[00:24:22] SPEAKER_02: You need to hire a ton of roboticists
[00:24:23] SPEAKER_02: with a lot of experience.
[00:24:25] SPEAKER_02: And only then, after years of effort potentially,
[00:24:28] SPEAKER_02: you will be able to automate this one single new task.
[00:24:32] SPEAKER_02: And this value proposition is not that high anymore,
[00:24:34] SPEAKER_02: because these large tasks where it was viable to do
[00:24:37] SPEAKER_02: have already been automated.
[00:24:39] SPEAKER_02: The environment has been engineered around them,
[00:24:40] SPEAKER_02: and there was enough ROI on them to actually do that.
[00:24:44] SPEAKER_02: So now we are left with a long tail of tasks
[00:24:47] SPEAKER_02: where each one of them is not big enough
[00:24:49] SPEAKER_02: to automate it with these traditional techniques,
[00:24:51] SPEAKER_02: but all of them combined are way bigger
[00:24:54] SPEAKER_02: than all of the tasks we automated so far.
[00:24:56] SPEAKER_02: So we want to make it very, very easy,
[00:24:59] SPEAKER_02: so lower the barrier of entry,
[00:25:00] SPEAKER_02: so that for any task to be automated,
[00:25:02] SPEAKER_02: you can do it very, very quickly.
[00:25:04] And now you can do it either by having your own robots.
[00:25:07] SPEAKER_02: Maybe you're a hardware company,
[00:25:08] SPEAKER_02: and you're building a very capable robot,
[00:25:10] SPEAKER_02: and you want to be able to control that robot.
[00:25:13] SPEAKER_02: So we'll provide intelligence for you to do that.
[00:25:16] Maybe you just want to perform some labor,
[00:25:20] SPEAKER_02: and you don't care what hardware you're using.
[00:25:23] SPEAKER_02: In that case, we might be able to provide you with a solution
[00:25:25] SPEAKER_02: that gives you a labor replacement,
[00:25:28] SPEAKER_02: something that a robot that can try to accomplish this task.
[00:25:33] SPEAKER_02: So we are trying to build out this ecosystem.
[00:25:35] SPEAKER_02: In terms of if you're interested in collaborating with us,
[00:25:40] SPEAKER_02: I would say just reach out.
[00:25:41] SPEAKER_02: We are exploring that space in many different directions.
[00:25:44] SPEAKER_02: We're working with partners, some of which sending us data,
[00:25:46] SPEAKER_02: some of them send us robots,
[00:25:49] SPEAKER_02: some of them just want to collaborate
[00:25:50] SPEAKER_02: and research ideas, reach out,
[00:25:52] SPEAKER_02: and we can figure it out together.
[00:25:54] Great.
[00:25:55] SPEAKER_00: All right, so let's talk about kind of the current state.
[00:25:58] SPEAKER_00: A few months ago, you released Pi 0.5,
[00:26:01] SPEAKER_00: which kind of what you refer to is open world
[00:26:04] SPEAKER_00: of real world generalization.
[00:26:06] SPEAKER_00: And that actually really caught my eye,
[00:26:08] SPEAKER_00: and I think it's important to give the audience
[00:26:12] kind of an understanding of where you're at today.
[00:26:16] SPEAKER_00: And I actually have a quick little video
[00:26:17] SPEAKER_00: I want to just share because it pulled from the website,
[00:26:21] SPEAKER_00: I think is very cool.
[00:26:26] So I'm just going to play it like 20 seconds.
[00:26:29] All right.
[00:26:30] SPEAKER_02: Could you close the cabinet?
[00:26:36] Can you place the dishes in the sink too?
[00:26:41] Can you just clean up the spilled?
[00:26:43] Okay, great.
[00:26:43] So for those of you who are just listening,
[00:27:04] that was a team member of Pi giving instructions
[00:27:08] SPEAKER_00: to a robot inside of an Airbnb in San Francisco.
[00:27:12] SPEAKER_00: Is that right?
[00:27:14] Yeah, it's one of the rents of home, too.
[00:27:16] And that robot had never been inside of the home,
[00:27:21] SPEAKER_00: and she was giving it commands,
[00:27:23] SPEAKER_00: and it was successfully completing those tasks.
[00:27:26] SPEAKER_00: So talk to us a little bit about Pi 0.5
[00:27:28] SPEAKER_00: and kind of where the team's at today.
[00:27:32] Yeah, I mean, I think, yeah, sure.
[00:27:35] SPEAKER_01: I mean, I think Pi, it's a bit of a mouthful.
[00:27:37] SPEAKER_01: I think sometimes we also say Pi 0.5,
[00:27:39] SPEAKER_01: just making it a little easier.
[00:27:41] SPEAKER_01: But yeah, I mean, I think the reason we called it Pi 0.5
[00:27:44] SPEAKER_01: is because it's not so different from the Pi 0 architecture.
[00:27:48] SPEAKER_01: We just really wanted to push on generalization
[00:27:51] SPEAKER_01: and capabilities in completely new environments,
[00:27:55] SPEAKER_01: because that's often seen as one of the hardest things
[00:27:58] SPEAKER_01: in robotics.
[00:28:00] Even in robot learning, anyone can do a demo where you put the things
[00:28:05] SPEAKER_01: in the exact same place down to the millimeter
[00:28:08] SPEAKER_01: and just do the same task over and over.
[00:28:10] SPEAKER_01: But I think to do something in a truly new home
[00:28:12] SPEAKER_01: is really difficult.
[00:28:13] SPEAKER_01: And then that's also where VLAs are showing the most promise
[00:28:17] SPEAKER_01: because of their semantic knowledge
[00:28:19] SPEAKER_01: combined with sort of their robotic knowledge.
[00:28:23] I mean, I think the main, like, aside from the architecture,
[00:28:25] SPEAKER_01: which is pretty similar to Pi 0.5, I think,
[00:28:28] SPEAKER_01: I mean, to Pi 0, I think the main things that we really
[00:28:32] SPEAKER_01: explored in Pi 0.5 were like the data collection,
[00:28:35] SPEAKER_01: like how much diversity do you need in your data
[00:28:39] SPEAKER_01: before you start seeing really good generalization?
[00:28:43] And then also we added this hierarchical system
[00:28:47] SPEAKER_01: where you have sort of like a more of a high level brain,
[00:28:50] SPEAKER_01: a thinking model that tells it what to do next.
[00:28:53] SPEAKER_01: So if you say clean up the kitchen,
[00:28:56] SPEAKER_01: and you want to know what to do first,
[00:28:58] SPEAKER_01: we have a first high level model that says,
[00:29:01] you may be pick up the fork or something.
[00:29:03] SPEAKER_01: And then the policy will go pick up the fork,
[00:29:06] SPEAKER_01: and then the high level model will say, okay, now that you
[00:29:08] SPEAKER_01: have the fork, put it in the sink.
[00:29:10] SPEAKER_01: And that's really important, I think,
[00:29:12] SPEAKER_01: to break down the task into more digestible segments
[00:29:15] SPEAKER_01: because it just makes the learning problem a lot easier.
[00:29:18] SPEAKER_01: One way we describe is it reduces the effect of horizon
[00:29:21] SPEAKER_01: for the low level policy in terms of it doesn't need to understand
[00:29:25] SPEAKER_01: what a kitchen is and what it means to clean up a kitchen.
[00:29:27] SPEAKER_01: It just needs to know, pick up the fork.
[00:29:29] SPEAKER_01: Although I say that, but then I'll also point out
[00:29:32] SPEAKER_01: that in the end, you know, what we found to be true
[00:29:35] SPEAKER_01: and what is often true is machine learning is that
[00:29:37] SPEAKER_01: it actually worked best when these were the same model.
[00:29:39] SPEAKER_01: So we actually put these two capabilities
[00:29:42] SPEAKER_01: into the same model, meaning because it's already
[00:29:45] SPEAKER_01: a language model, so it has the capability to output text.
[00:29:49] We trained it both as what we call the high level policy,
[00:29:52] SPEAKER_01: which describes the next task, like pick up the fork.
[00:29:54] SPEAKER_01: And then we also trained it as the low level policy,
[00:29:58] SPEAKER_01: which is like once it knows the pick up of the fork,
[00:30:00] SPEAKER_01: actually outputs the actions.
[00:30:02] SPEAKER_01: So it's like one model, two different modes,
[00:30:04] SPEAKER_01: and we use them both.
[00:30:05] SPEAKER_01: And that was really important for this open world generalization
[00:30:08] SPEAKER_01: as we call it.
[00:30:10] Well, there's some ways.
[00:30:12] SPEAKER_02: Just to emphasize the significance of that,
[00:30:15] SPEAKER_02: I think, you know, it's kind of hard to get across
[00:30:18] SPEAKER_02: because usually you look at different robotic demos
[00:30:21] SPEAKER_02: or robotic videos and they all kind of look the same.
[00:30:23] SPEAKER_02: You know, whether you fold longer here or there,
[00:30:26] SPEAKER_02: like, who cares?
[00:30:27] SPEAKER_02: They, you know, all seem very, very close to each other.
[00:30:30] And there was a little caveat that basically everyone
[00:30:33] SPEAKER_02: has been doing so far on how you record these demos,
[00:30:37] SPEAKER_02: which is what Kevin described.
[00:30:38] SPEAKER_02: Like you collect data in the exact same environment
[00:30:41] SPEAKER_02: over and over, then you set the environment
[00:30:44] SPEAKER_02: in the exact same way for the demo should.
[00:30:49] You make sure that the lighting is exactly the same
[00:30:51] SPEAKER_02: you do during the same time of the day,
[00:30:53] SPEAKER_02: and then you record it, and then you're done.
[00:30:56] SPEAKER_02: And we are, we've done it in the past.
[00:30:58] SPEAKER_02: I've done it in the past many times
[00:31:00] SPEAKER_02: with my own research projects.
[00:31:02] SPEAKER_02: And we wanted to really break that paradigm.
[00:31:05] SPEAKER_02: And we thought of what would be the hardest version
[00:31:08] SPEAKER_02: of this challenge?
[00:31:09] SPEAKER_02: And the hardest version of this challenge
[00:31:11] SPEAKER_02: is not just to, you know, turn on the lights
[00:31:13] SPEAKER_02: or add another object or change the background a little bit.
[00:31:17] It's to pick an environment that is the most diverse there is,
[00:31:20] SPEAKER_02: which in this case, we believe it's homes.
[00:31:23] SPEAKER_02: Every home is different.
[00:31:24] SPEAKER_02: There's many, many different things that differ in different homes.
[00:31:27] SPEAKER_02: It's not just backgrounds or lighting.
[00:31:28] SPEAKER_02: It's basically everything objects, you know,
[00:31:31] SPEAKER_02: how cabinets work, everything.
[00:31:33] And we wanted to see what it would take
[00:31:35] SPEAKER_02: to bring a robot to a new home
[00:31:38] SPEAKER_02: and get it to generalize to perform as well in this new home
[00:31:41] SPEAKER_02: as if it was trained in that specific home.
[00:31:44] And it was pretty clear that part of the answer there
[00:31:47] SPEAKER_02: is the architectural advancements.
[00:31:49] SPEAKER_02: But a big part of the answer is,
[00:31:51] SPEAKER_02: how much diverse data do you need to see first
[00:31:53] SPEAKER_02: before you generalize to the new home?
[00:31:56] And this was something that before we started the project,
[00:31:58] SPEAKER_02: we really had no idea about.
[00:32:00] We were discussing here, discussing it in the office
[00:32:04] SPEAKER_02: and, you know, the numbers that were floating were something
[00:32:07] SPEAKER_02: like maybe you need to see a million homes
[00:32:09] SPEAKER_02: before you are able to generalize to the million first home
[00:32:11] SPEAKER_02: or, you know, a billion homes or maybe, you know,
[00:32:14] a thousand homes or whatever.
[00:32:16] And it turned out that this number is very tractable.
[00:32:19] SPEAKER_02: It's just a hundred homes.
[00:32:21] So after seeing a hundred different homes,
[00:32:22] SPEAKER_02: you are able to generalize to the hundred first home
[00:32:25] SPEAKER_02: as well as if you were trained in that home.
[00:32:29] And this is something that makes the problem
[00:32:30] SPEAKER_02: very tractable and quite solvable.
[00:32:33] SPEAKER_02: It's also something that was very, very surprising to us.
[00:32:36] SPEAKER_02: And we are not fully sure how to interpret this.
[00:32:38] SPEAKER_02: Whether it's that the models are very, very strong
[00:32:41] SPEAKER_02: or maybe the world is not diverse as we have thought.
[00:32:45] You know, we as people are able to generalize
[00:32:47] SPEAKER_02: fairly well to a new location.
[00:32:50] So maybe the patterns we see are very strong.
[00:32:54] But this was the most surprising aspect of this.
[00:32:57] Yeah, we have a really cool chart in the paper.
[00:32:59] SPEAKER_01: We're like the X-axis is literally the number of homes.
[00:33:02] SPEAKER_01: It's like, you know, one home, two homes,
[00:33:04] SPEAKER_01: 40 homes, 50 homes, and then the performance goes up.
[00:33:07] SPEAKER_01: And it matches the performance of basically just like
[00:33:11] SPEAKER_01: training on the target home around like 80 or 100.
[00:33:14] SPEAKER_01: And you know, we would have been in big trouble
[00:33:16] SPEAKER_01: if it was a billion, like you said,
[00:33:17] SPEAKER_01: but ended up being like on the order of 100,
[00:33:19] SPEAKER_01: which is really cool.
[00:33:22] It's interesting.
[00:33:23] SPEAKER_00: It reminds me a little bit different,
[00:33:24] SPEAKER_00: but I was having a conversation with Baron from 1X.
[00:33:27] SPEAKER_00: And he was kind of saying, obviously,
[00:33:29] SPEAKER_00: it's different.
[00:33:30] SPEAKER_00: It's not environment, but he was saying,
[00:33:32] SPEAKER_00: is it related to tasks, similar thing
[00:33:34] SPEAKER_00: that after you run the same task,
[00:33:36] SPEAKER_00: and he said like 45 or 50 times,
[00:33:40] that incremental accuracy for the robot
[00:33:44] to perform that test better just completely diminished.
[00:33:46] SPEAKER_00: So he said that surprised him a lot too.
[00:33:48] SPEAKER_00: So it's like a similar thing, which is pretty interesting
[00:33:50] SPEAKER_00: that you would think that it would just continue
[00:33:52] to get better and better, but they saw very little improvements
[00:33:56] SPEAKER_00: after that number 50 mark from a task specific standpoint.
[00:34:01] Yeah, it's a slightly different challenge in that.
[00:34:05] SPEAKER_02: At some point you start hitting the diminishing
[00:34:06] SPEAKER_02: of returns when it comes to performance
[00:34:08] SPEAKER_02: on a specific task.
[00:34:10] SPEAKER_02: So if you have certain amount of data for a specific task,
[00:34:13] SPEAKER_02: let's say, you know, passing tables.
[00:34:17] If you just 10X or 100X.data
[00:34:20] SPEAKER_02: in the exact same environment, doing exact same set of actions,
[00:34:23] SPEAKER_02: the performance doesn't improve.
[00:34:26] This is something that we observe as well.
[00:34:29] This has more to do with how these models are actually trained
[00:34:32] SPEAKER_02: and what they're optimizing for.
[00:34:34] SPEAKER_02: Right now the standard is to optimize
[00:34:37] SPEAKER_02: for replicating the actions
[00:34:39] SPEAKER_02: that you've seen in the data set.
[00:34:42] SPEAKER_02: So you're trying to minimize the error
[00:34:43] SPEAKER_02: between your action and the action that you've seen in the past.
[00:34:47] It's a very good objective, very scalable objective
[00:34:50] SPEAKER_02: that allows us to generalize fairly well and so on.
[00:34:53] SPEAKER_02: But on this performance metric,
[00:34:54] SPEAKER_02: it actually doesn't really capture what we truly care about.
[00:34:57] SPEAKER_02: Because we don't care about about
[00:35:00] SPEAKER_02: imitating the actions as closely as possible.
[00:35:03] SPEAKER_02: What we care about is actually the outcome of the task.
[00:35:06] Right? So like if I fold laundry,
[00:35:08] SPEAKER_02: I would really care about this,
[00:35:11] SPEAKER_02: what the pull the t-shirt at the end looks like,
[00:35:13] SPEAKER_02: not necessarily to perform every single action,
[00:35:15] SPEAKER_02: exactly the same as a human operator before.
[00:35:19] SPEAKER_02: And this is something that many people in the field
[00:35:21] SPEAKER_02: are working on.
[00:35:22] SPEAKER_02: I don't think we have a very satisfying solution
[00:35:25] SPEAKER_02: to this problem at this point.
[00:35:28] But yeah, I agree with what Bern was saying.
[00:35:30] SPEAKER_02: I don't think it's just going to happen
[00:35:31] SPEAKER_02: by increasing the amount of data for a specific task.
[00:35:36] All right, I think that these are good segue.
[00:35:37] SPEAKER_00: We're going to drill into,
[00:35:39] SPEAKER_00: I want to drill into the training data side for you
[00:35:41] SPEAKER_00: with you on that point, which is,
[00:35:45] SPEAKER_00: I think it's kind of what you hear over and over again.
[00:35:47] SPEAKER_00: It's about who can, you need to have the largest,
[00:35:50] SPEAKER_00: most diverse data set
[00:35:54] in the space to be able to solve many of these problems.
[00:35:57] SPEAKER_00: And I have kind of three areas I wanted to kind of pick
[00:36:00] SPEAKER_00: both Carl, you're in Kevin's brain zone
[00:36:03] SPEAKER_00: as far as improvement areas and kind of get your perspective on.
[00:36:07] For us to be able to get Kennedy's robotics models
[00:36:09] SPEAKER_00: to work at scale.
[00:36:11] So the three are, and then we'll go one by one,
[00:36:12] SPEAKER_00: the three all this amount, inference speed,
[00:36:14] SPEAKER_00: contents, context, length, and the size of the model.
[00:36:20] So first, let's go to an over to inference speed.
[00:36:25] Kevin actually has some really cool work
[00:36:27] SPEAKER_02: on inference speed and how can we tackle this
[00:36:29] SPEAKER_02: with big of models?
[00:36:31] SPEAKER_02: Kevin, do you want to talk about that?
[00:36:33] Yeah, I mean, this is our most recent release
[00:36:36] SPEAKER_01: as of right now is basically how,
[00:36:38] SPEAKER_01: like how do you deal with the large model
[00:36:41] SPEAKER_01: that might take like, you know, a while to do inference,
[00:36:44] SPEAKER_01: but you have to do it in real time.
[00:36:45] SPEAKER_01: Because in a language model or vision language model
[00:36:48] SPEAKER_01: or coding model or chatbot or anything,
[00:36:51] SPEAKER_01: it's like, you know, if the model's slow,
[00:36:53] SPEAKER_01: that's obviously bad.
[00:36:54] SPEAKER_01: It's like annoying as a user.
[00:36:56] SPEAKER_01: I don't want to type my response to chat GPT
[00:36:58] SPEAKER_01: and then have to wait like 30 seconds
[00:36:59] SPEAKER_01: for it to give an answer.
[00:37:01] But like, even if I do have to wait 30 seconds
[00:37:03] SPEAKER_01: to give an answer,
[00:37:04] SPEAKER_01: the answer's going to be the same quality, right?
[00:37:06] SPEAKER_01: Like, slowness is just slowness.
[00:37:08] SPEAKER_01: It doesn't affect quality.
[00:37:09] SPEAKER_01: In robotics, it's like, it's actually completely different
[00:37:12] SPEAKER_01: because you're dealing with the real world.
[00:37:14] SPEAKER_01: And the world, you know, it evolves
[00:37:17] SPEAKER_01: according to the laws of physics in real time.
[00:37:20] SPEAKER_01: So if your model's sitting there thinking for, you know,
[00:37:23] SPEAKER_01: one second, two seconds, 30 seconds,
[00:37:25] SPEAKER_01: like that's really going to affect performance,
[00:37:28] SPEAKER_01: especially depending on the task,
[00:37:30] SPEAKER_01: if there's any sort of dynamic nature,
[00:37:32] SPEAKER_01: like if something in the world is moving,
[00:37:35] obviously you need to like react quickly
[00:37:36] SPEAKER_01: to like, grasp the object, right?
[00:37:40] That's a big challenge.
[00:37:41] SPEAKER_01: I think not many people are working on actually
[00:37:43] SPEAKER_01: in terms of VLA's because, you know,
[00:37:46] SPEAKER_01: we might see as we make the VLA bigger,
[00:37:48] SPEAKER_01: it outputs better actions,
[00:37:49] SPEAKER_01: but if it does that slower,
[00:37:50] SPEAKER_01: it might not actually be better in the long run.
[00:37:52] SPEAKER_01: So you have to solve this problem.
[00:37:55] SPEAKER_01: The work I did was basically saying, you know,
[00:37:56] SPEAKER_01: it didn't make the model itself faster,
[00:37:58] SPEAKER_01: but it said, given that we have some latency
[00:38:02] SPEAKER_01: as long as it's below some threshold,
[00:38:03] SPEAKER_01: like let's say your latency is below half a second.
[00:38:06] How can we generate actions and execute actions
[00:38:13] SPEAKER_01: in parallel at the same time?
[00:38:15] So the robot doesn't have to stop and think,
[00:38:17] SPEAKER_01: it can like be moving towards an object,
[00:38:20] SPEAKER_01: while also thinking about the next actions
[00:38:23] SPEAKER_01: after-gress the object.
[00:38:26] Because before that, we would actually just have
[00:38:27] SPEAKER_01: the model stop and think every half second or so,
[00:38:31] which is like, it's like mostly okay for most tasks,
[00:38:33] SPEAKER_01: especially if there's like nothing like move,
[00:38:35] SPEAKER_01: you know, something crazy going on, moving around.
[00:38:39] But what I thought was like, even in tasks
[00:38:41] SPEAKER_01: where what we call static, quasi-static or static tasks
[00:38:44] SPEAKER_01: where like nothing in the environment
[00:38:46] SPEAKER_01: is moving super fast,
[00:38:47] SPEAKER_01: it does, it can still improve performance a little bit
[00:38:51] to do this asynchronous or parallel execution
[00:38:54] SPEAKER_01: because when the robot stops,
[00:38:56] SPEAKER_01: it kind of like wiggles a little
[00:38:58] SPEAKER_01: and it changes the physics when it stops.
[00:39:00] SPEAKER_01: And ideally you don't wanna change the physics
[00:39:03] SPEAKER_01: of the arm at test times.
[00:39:04] SPEAKER_01: So, you know, this is sort of only a first step,
[00:39:07] SPEAKER_01: I think like the method that I came up with
[00:39:10] SPEAKER_01: this honestly really just like a stop gap for now
[00:39:14] SPEAKER_01: in my mind, I think we really need to figure out
[00:39:17] SPEAKER_01: as we continue to scale these models
[00:39:19] SPEAKER_01: and do more dynamic tasks as well,
[00:39:21] SPEAKER_01: we really need to figure out how to execute them
[00:39:24] SPEAKER_01: asynchronously without decreasing the performance.
[00:39:29] Is this the chunking, it's called chunking, correct?
[00:39:32] SPEAKER_00: Yeah, it's called real time action chunking.
[00:39:34] SPEAKER_01: Yeah, real time action, okay.
[00:39:35] SPEAKER_00: I took a look at the paper.
[00:39:37] Okay, how about context length?
[00:39:39] SPEAKER_00: This one's very interesting to me.
[00:39:44] What do we need to improve?
[00:39:46] That's a great point too.
[00:39:47] SPEAKER_01: I mean, we need to improve the context length, right?
[00:39:48] SPEAKER_01: It's kind of in the answers in the question.
[00:39:51] SPEAKER_01: I mean, we have been working on this,
[00:39:53] SPEAKER_01: like obviously there are tasks
[00:39:54] SPEAKER_01: where you really need to know,
[00:39:56] SPEAKER_01: you know, what happened in the past,
[00:39:57] SPEAKER_01: like, I mean, there's like sort of more obvious examples,
[00:40:01] SPEAKER_01: you might think of that are more like large language models
[00:40:03] SPEAKER_01: where like you have a user input,
[00:40:05] SPEAKER_01: like a really long sequence of instructions or something.
[00:40:09] Like that's like a pretty trivial example of context length,
[00:40:11] SPEAKER_01: but there's even more subtle ones.
[00:40:15] Like if you try to grasp an object one way and you fail,
[00:40:19] SPEAKER_01: you ideally want the model to be like,
[00:40:20] SPEAKER_01: okay, well, I shouldn't just try that exact same motion again.
[00:40:23] SPEAKER_01: Maybe I should like adjust a little bit.
[00:40:25] We call that in context learning
[00:40:27] SPEAKER_01: and it's super, super important for language models,
[00:40:30] SPEAKER_01: especially these like reasoning models, you know, lately,
[00:40:33] SPEAKER_01: they'll go down one path and then they're trained to actually say,
[00:40:36] SPEAKER_01: wait, let me double check and make sure that like,
[00:40:39] SPEAKER_01: that's correct and that really improves performance.
[00:40:41] SPEAKER_01: And I think it's similar for robotics, like, you know,
[00:40:44] SPEAKER_01: it would be really, the models could be much better
[00:40:46] SPEAKER_01: if they take into account, like what they've just seen
[00:40:49] SPEAKER_01: or like, you know, even the past few seconds of information,
[00:40:52] SPEAKER_01: but it also comes with its own challenges
[00:40:54] SPEAKER_01: both in terms of compute and methods
[00:40:56] SPEAKER_01: because, you know, just naively adding in the last second
[00:41:01] SPEAKER_01: or two of history, we actually found it can actually decrease
[00:41:03] SPEAKER_01: performance surprisingly in some cases.
[00:41:05] SPEAKER_01: So, and it's not totally clear why.
[00:41:07] SPEAKER_01: So these are things that we actually have to figure out.
[00:41:11] So this is also the importance of this is going to increase
[00:41:15] SPEAKER_02: as the horizon of the task we tackle increases.
[00:41:19] SPEAKER_02: So, you know, if the task is very short
[00:41:21] SPEAKER_02: and you can be fairly reactive,
[00:41:23] SPEAKER_02: I just tell you a specific small task to do.
[00:41:26] SPEAKER_02: You might be able to be okay with just being very reactive
[00:41:30] SPEAKER_02: and trying to act based on the current image you're seeing
[00:41:32] SPEAKER_02: and not having much, much history or a very long context length.
[00:41:37] SPEAKER_02: As it becomes more of a long prompt of a job I want you to make,
[00:41:42] SPEAKER_02: this becomes very, very important.
[00:41:43] SPEAKER_02: You need to understand my preferences.
[00:41:45] SPEAKER_02: You need to understand what you've done in the past.
[00:41:47] SPEAKER_02: You need to understand where the objects are
[00:41:49] SPEAKER_02: by somewhere you've put them before or were in some of the else
[00:41:51] SPEAKER_02: put them before.
[00:41:52] SPEAKER_02: So this is going to become bigger and bigger problem
[00:41:55] SPEAKER_02: as we go.
[00:41:58] And like, how do you, when you think about the context length,
[00:42:02] SPEAKER_00: is it when are you, is it just a bunch of if-them statements
[00:42:07] SPEAKER_00: that you're creating like from if this happens
[00:42:10] SPEAKER_00: and these certain outcomes can happen
[00:42:12] SPEAKER_00: then it just keeps going like that.
[00:42:14] SPEAKER_00: Like, depending on the task.
[00:42:19] I think it depends on the type of context length.
[00:42:21] SPEAKER_01: So I think when I was talking about history and in context
[00:42:24] SPEAKER_01: learning I was actually talking about video context.
[00:42:28] So right now the model actually takes in one image at a time.
[00:42:32] SPEAKER_01: So it's just like instantaneous.
[00:42:34] SPEAKER_01: You could imagine taking a few images in the past,
[00:42:39] SPEAKER_01: which is like sort of starts to become closer.
[00:42:41] SPEAKER_01: You know, the more images you have the more you call it a video.
[00:42:45] SPEAKER_01: But yeah, that's I think what I was talking about
[00:42:47] SPEAKER_01: in terms of in context learning.
[00:42:50] SPEAKER_01: So as it can it get as input sort of the past few seconds
[00:42:53] SPEAKER_01: of video rather than just like the instantaneous moment.
[00:42:58] SPEAKER_01: I think you're getting more at the high level,
[00:43:00] SPEAKER_01: what I called earlier the high level, like the language site.
[00:43:04] Which is also important.
[00:43:05] SPEAKER_01: And like I said, this is actually sort of more overlapped
[00:43:07] SPEAKER_01: with LLM research, which is like if you have
[00:43:10] SPEAKER_01: a long multi-step task, how do you like break that down
[00:43:13] SPEAKER_01: and like do sort of a search to figure out the optimal way
[00:43:16] SPEAKER_01: to proceed and that also involves a very long context
[00:43:19] SPEAKER_01: more like in text space, usually.
[00:43:22] And in some ways, it's quite surprising how capable
[00:43:26] SPEAKER_02: the current models are, even how will they know about the world.
[00:43:30] SPEAKER_02: Or how will they know about the world
[00:43:32] SPEAKER_02: when they need to perform an action?
[00:43:35] Because they don't really have access to history
[00:43:37] SPEAKER_02: or not very long history.
[00:43:39] You can think of it as if you were waking up
[00:43:42] SPEAKER_02: every fraction of a second.
[00:43:45] SPEAKER_02: You were given the language command.
[00:43:46] SPEAKER_02: And you don't know what you've done a second ago
[00:43:49] SPEAKER_02: or a little longer than two seconds ago.
[00:43:52] SPEAKER_02: And you need to perform the right action every single time.
[00:43:55] SPEAKER_02: And it turns out that they can still do many, many tasks
[00:43:59] SPEAKER_02: where you would think you require some kind of context
[00:44:02] SPEAKER_02: or some kind of history of what you've done in the past
[00:44:04] SPEAKER_02: to be able to perform the right action.
[00:44:06] SPEAKER_02: But it turns out that they can do quite a lot,
[00:44:08] SPEAKER_02: even with such short history or context.
[00:44:13] As Kevin said, this is a very open area of research.
[00:44:17] SPEAKER_02: It's not as simple as just extending the context window
[00:44:20] SPEAKER_02: and training with more video data of what you've done in the past.
[00:44:25] There is many other challenges that come up there.
[00:44:28] SPEAKER_02: But this is something we're actively working on.
[00:44:31] Great.
[00:44:32] And how many do you think about it in a similar way
[00:44:36] SPEAKER_00: as kind of LLMs and the number of parameters
[00:44:39] SPEAKER_00: when you think about model size?
[00:44:40] SPEAKER_00: Is it a similar thing with the VLAs?
[00:44:44] Yeah, I say a model size is definitely
[00:44:48] one of the number one metrics you look at when you talk about scaling.
[00:44:52] SPEAKER_01: Like, is it context linked?
[00:44:54] SPEAKER_01: You can have the same size model and give it a longer context.
[00:44:56] SPEAKER_01: And obviously, that's more expensive.
[00:44:58] SPEAKER_01: You could also have the same context window
[00:45:00] SPEAKER_01: and increase the number of parameters.
[00:45:01] SPEAKER_01: And that's also more expensive in a different way.
[00:45:05] I would say model size is pretty important.
[00:45:07] SPEAKER_01: It's something that we're thinking about.
[00:45:09] SPEAKER_01: I think, again, I mean, this actually
[00:45:12] SPEAKER_01: loops back around to inference speed.
[00:45:14] SPEAKER_01: But when you see out the model size,
[00:45:16] SPEAKER_01: you have to think about the inference speed a lot more
[00:45:18] SPEAKER_01: than you do in LLMs.
[00:45:19] SPEAKER_01: Because in LLMs, OK, you can run it slowly.
[00:45:21] SPEAKER_01: And it will still do high quality outputs.
[00:45:24] SPEAKER_01: For us, it's like, oh, we doubled the size of the model.
[00:45:27] SPEAKER_01: Maybe it got twice as good, but we don't know
[00:45:28] SPEAKER_01: because it takes so long to produce an action.
[00:45:30] SPEAKER_01: That falls apart when you actually evaluate it.
[00:45:34] Yeah, and you might underwear folded, man.
[00:45:35] SPEAKER_00: Can't be waiting for that.
[00:45:40] How do you decide, when you think about edge case, data
[00:45:47] SPEAKER_00: diversity, how do you decide what to do in house first,
[00:45:51] SPEAKER_00: maybe working with third party service provider
[00:45:54] SPEAKER_00: for data collection?
[00:45:58] Yeah, for data collection, we found that it's really important
[00:46:01] SPEAKER_02: to have all the teams be as close together as possible.
[00:46:06] SPEAKER_02: So we have the operations team right here, hardware team
[00:46:08] SPEAKER_02: right here, research team, software team.
[00:46:11] So you want this interaction to be very, very tight,
[00:46:14] SPEAKER_02: because we don't fully understand what data to collect
[00:46:17] SPEAKER_02: to improve the model performance the most.
[00:46:19] SPEAKER_02: We have this big notions of more diversity is better,
[00:46:24] or very high quality of data is better.
[00:46:28] SPEAKER_02: But then you really need to be able to define it very,
[00:46:30] SPEAKER_02: very crisply to be able to fully outsource it.
[00:46:33] SPEAKER_02: And we don't fully know big diversity,
[00:46:36] SPEAKER_02: what does this exactly mean, or higher quality,
[00:46:39] SPEAKER_02: what does this exactly mean?
[00:46:42] So so far we found that the more we do in house
[00:46:45] SPEAKER_02: where everybody is here, and we can literally see the robots
[00:46:48] SPEAKER_02: all day, every day, that this allows us to just
[00:46:52] SPEAKER_02: iterate much faster and understand these questions better.
[00:46:56] Having said that, I suspect that eventually the way it's
[00:47:00] SPEAKER_02: going to work is as we understand this better,
[00:47:04] SPEAKER_02: the problem better.
[00:47:06] I suspect that for the best models,
[00:47:10] SPEAKER_02: they will be able to absorb data coming from all kinds
[00:47:13] SPEAKER_02: of different sources, whether it's the data that you
[00:47:15] SPEAKER_02: collected in house, or whether it's somebody else
[00:47:18] SPEAKER_02: collected for you, or whether it's a very different robot
[00:47:20] SPEAKER_02: that is running across the ocean, doing a very different task,
[00:47:25] SPEAKER_02: and you don't fully even understand what kind of robot it is.
[00:47:28] SPEAKER_02: I believe that the most successful models will be the ones
[00:47:31] SPEAKER_02: that can absorb all of that data and make sense out of it.
[00:47:34] SPEAKER_02: And this is similar to what we've seen with language,
[00:47:37] SPEAKER_02: where you have this notion of a generalist
[00:47:41] SPEAKER_02: that is way better than specialists at specialist tasks.
[00:47:44] SPEAKER_02: If we take a look at the problem of language translation,
[00:47:47] SPEAKER_02: for instance, we had teams that were focusing
[00:47:50] SPEAKER_02: on language translation for a very long time,
[00:47:52] SPEAKER_02: and at some point they hit a certain ceiling,
[00:47:54] SPEAKER_02: and they couldn't be able to, they
[00:47:56] SPEAKER_02: weren't able to improve beyond that.
[00:47:58] And it turned out that the way to solve language translation
[00:48:00] SPEAKER_02: is to, it's not by focusing on language translation,
[00:48:02] SPEAKER_02: but by focusing on all of language.
[00:48:05] And that then lifts all the boats.
[00:48:07] SPEAKER_02: And I think this is a very, very significant change
[00:48:10] SPEAKER_02: in how we think about generalists versus specialists.
[00:48:14] SPEAKER_02: Because until now, really, if you were able to specialize
[00:48:18] SPEAKER_02: on something small, I mean, that's how entrepreneurship works.
[00:48:22] SPEAKER_02: If you can able to focus on something,
[00:48:24] SPEAKER_02: you would be able to do it much better
[00:48:25] SPEAKER_02: than a bigger company that is trying
[00:48:27] SPEAKER_02: to do all different things.
[00:48:29] SPEAKER_02: And it turns out that with these models,
[00:48:31] SPEAKER_02: that's not necessarily the case.
[00:48:33] SPEAKER_02: If you can, the more data they can absorb,
[00:48:35] SPEAKER_02: the more patterns they can spot based
[00:48:38] SPEAKER_02: on the diversity of data they see,
[00:48:39] SPEAKER_02: the better they perform, even on those specialist tasks.
[00:48:46] So when you think about, I'll be saying an LLM side,
[00:48:51] SPEAKER_00: I'm going back to kind of the third party service provider
[00:48:54] SPEAKER_00: or to helping with data collection.
[00:48:56] SPEAKER_00: And obviously, you have a SCALAI and RECOR
[00:48:59] SPEAKER_00: and several companies that are pretty sizeable,
[00:49:01] SPEAKER_00: businesses, more on the LLM training side,
[00:49:04] SPEAKER_00: mostly on the data annotation, labeling,
[00:49:08] SPEAKER_00: model evaluation.
[00:49:09] SPEAKER_00: And I know there's a bunch of new companies
[00:49:12] SPEAKER_00: that have popped up, focus more on kind of physical AI
[00:49:15] SPEAKER_00: or embodied AI.
[00:49:16] SPEAKER_00: And so from your perspective,
[00:49:19] SPEAKER_00: what is actually needed if folks are looking to help
[00:49:23] SPEAKER_00: solve this data training problem
[00:49:25] SPEAKER_00: that they should be focusing on,
[00:49:28] SPEAKER_00: that stuff that you would be interested in at Pi?
[00:49:33] Interesting question.
[00:49:37] I think there's a few different angles
[00:49:40] SPEAKER_02: that would be helpful.
[00:49:42] SPEAKER_02: I think one is making really good hardware
[00:49:46] SPEAKER_02: and making the ecosystem better.
[00:49:50] So hardware that is capable, that is reliable
[00:49:53] SPEAKER_02: and that is easy to deploy.
[00:49:55] SPEAKER_02: I think that's one of those things
[00:49:57] SPEAKER_02: that will help everybody.
[00:50:00] I think in terms of data labeling and data collection,
[00:50:03] SPEAKER_02: we see a lot of these companies.
[00:50:05] SPEAKER_02: There isn't like a week where we don't hear from multiple
[00:50:09] SPEAKER_02: of them about different data offerings.
[00:50:14] I don't think we are there yet to like fully utilize this
[00:50:17] SPEAKER_02: and I think it's a little oversubscribed at the moment
[00:50:20] SPEAKER_02: because I think the biggest value there is to do a lot of it
[00:50:24] SPEAKER_02: to make yourself so that you can fully understand
[00:50:26] SPEAKER_02: how to do that.
[00:50:28] But I think there are so many hard problems
[00:50:31] SPEAKER_02: in this entire space that I would just focus
[00:50:32] SPEAKER_02: on really, really hard problems.
[00:50:35] So rather than picking kind of the low hanging fruits
[00:50:39] SPEAKER_02: of where you think you can make a little bit more money,
[00:50:44] I would focus on problems that are actually blockers.
[00:50:46] SPEAKER_02: One of them is intelligence.
[00:50:48] SPEAKER_02: The other one is cheap, reliable hardware
[00:50:50] SPEAKER_02: and try to contribute there.
[00:50:55] SPEAKER_00: So how does your team think of,
[00:50:56] SPEAKER_00: you constantly hear kind of edge cases,
[00:50:58] SPEAKER_00: edge cases, edge cases are always like the most,
[00:51:01] SPEAKER_00: sometimes the most difficult things
[00:51:02] SPEAKER_00: to train robotic systems for.
[00:51:05] SPEAKER_00: So how do you all think about kind of handling
[00:51:09] a variety of edge cases when you're doing your training?
[00:51:13] Yeah.
[00:51:15] SPEAKER_02: It's a tough problem.
[00:51:17] SPEAKER_02: I don't think we have a solution yet.
[00:51:20] But it comes back to this problem I described before
[00:51:25] SPEAKER_02: what is the model actually optimizing for?
[00:51:27] SPEAKER_02: And if it's just optimizing for imitating actions,
[00:51:30] SPEAKER_02: it's not really able to reason through the different outcomes
[00:51:34] SPEAKER_02: and or through different actions
[00:51:36] SPEAKER_02: that will lead to the outcome you want.
[00:51:38] SPEAKER_02: And that makes it harder to deal with edge cases.
[00:51:41] SPEAKER_02: We also see that the more diverse the data is,
[00:51:43] SPEAKER_02: the better you can deal with edge cases.
[00:51:46] SPEAKER_02: So you kind of have these two levers.
[00:51:47] SPEAKER_02: One is collect very high quality diverse data
[00:51:51] SPEAKER_02: that would allow you to understand every edge case
[00:51:53] SPEAKER_02: you encounter.
[00:51:55] SPEAKER_02: And the second one is optimize the model
[00:51:57] SPEAKER_02: for what you actually care about,
[00:51:59] SPEAKER_02: optimize for the final outcome for performance.
[00:52:02] I think the first one we understand much better
[00:52:05] SPEAKER_02: than the second one.
[00:52:07] And the second one is something where we just need more innovation.
[00:52:11] SPEAKER_02: We need to understand how to change our algorithms,
[00:52:16] SPEAKER_02: how to optimize for what we actually care about,
[00:52:18] SPEAKER_02: how to describe what we actually care about.
[00:52:21] So it requires more and more research.
[00:52:24] I might add, and maybe it's a bit of a hot take,
[00:52:27] SPEAKER_01: but our edge cases really that important,
[00:52:30] SPEAKER_01: because if you look at LLMs,
[00:52:32] SPEAKER_01: they still have very famous edge cases,
[00:52:34] SPEAKER_01: like count the number of R's and draw very X
[00:52:37] SPEAKER_01: if you put five R's.
[00:52:38] SPEAKER_01: And they can't do that still.
[00:52:40] SPEAKER_01: And our even very simple math question
[00:52:41] SPEAKER_01: is 9.11 greater than 9.9.
[00:52:44] SPEAKER_01: Like they famously fail at these.
[00:52:46] SPEAKER_01: They're obviously still so useful.
[00:52:48] SPEAKER_01: And they can solve, I'm a gold problem now, I guess.
[00:52:51] SPEAKER_01: So it's like, I think it's similar in robotics
[00:52:53] SPEAKER_01: where in traditional robotics,
[00:52:56] SPEAKER_01: it so happens to be that the things
[00:52:58] SPEAKER_01: traditional robotics were good at, like factory automation,
[00:53:00] SPEAKER_01: edge cases were really, really important.
[00:53:02] SPEAKER_01: You need like 99.999% success rate.
[00:53:06] SPEAKER_01: But if you have a laundry folding robot in your home,
[00:53:09] SPEAKER_01: like if it drops in underwear, like one in every 100 times,
[00:53:13] SPEAKER_01: one in every 1000 times, like it's okay,
[00:53:15] SPEAKER_01: it's still really useful actually.
[00:53:17] SPEAKER_01: Well, you know, I think there are the heart of the problem
[00:53:20] SPEAKER_01: almost like the less important edge cases become
[00:53:23] SPEAKER_01: in some sense, which is interesting.
[00:53:27] Cool.
[00:53:28] SPEAKER_00: Carl, give us a quick little just background.
[00:53:30] SPEAKER_00: I know you spent five years, five or six years
[00:53:32] SPEAKER_00: over at Google Brain and after kind of leaving Google,
[00:53:37] SPEAKER_00: tell us this kind of like the quick run through
[00:53:40] SPEAKER_00: the founding story and how the founders came together
[00:53:42] SPEAKER_00: to start pie.
[00:53:44] Yeah, we worked together for quite some time before,
[00:53:47] SPEAKER_02: so we've known each other for more than a decade
[00:53:50] SPEAKER_02: at this point.
[00:53:54] There were a few things that we realized,
[00:53:57] SPEAKER_02: but I think the more significant aspect is that,
[00:54:03] you know, we all spend basically our lives
[00:54:05] SPEAKER_02: working on this problem, trying to figure out
[00:54:08] SPEAKER_02: how to make robots intelligent,
[00:54:09] SPEAKER_02: how to provide real physical intelligence.
[00:54:12] And for a long time for me personally,
[00:54:15] SPEAKER_02: it felt like it's not really possible
[00:54:17] SPEAKER_02: to do the problem's way too hard.
[00:54:19] SPEAKER_02: And if no matter what progress you make in a moment,
[00:54:22] SPEAKER_02: it felt like they're not adding up to each other.
[00:54:25] SPEAKER_02: And even though it seems like a little bit of progress,
[00:54:29] SPEAKER_02: you don't really see a path of solving the entire problem.
[00:54:34] SPEAKER_02: And at some point, it started changing.
[00:54:36] SPEAKER_02: It started changing for me and I think few others
[00:54:38] SPEAKER_02: also started recognizing this shift.
[00:54:42] SPEAKER_02: And that I started seeing the light at the end of the tunnel.
[00:54:47] SPEAKER_02: We started seeing that if you have large enough
[00:54:50] SPEAKER_02: of the data set, if you really create models
[00:54:53] SPEAKER_02: that can absorb that data and you work
[00:54:56] SPEAKER_02: on the right algorithms, you would be able to solve
[00:54:58] SPEAKER_02: this problem fully.
[00:55:00] SPEAKER_02: And what I mean by that is truly having a model
[00:55:03] SPEAKER_02: that can control any robot to do any task.
[00:55:06] SPEAKER_02: And what I saw at that moment is that, well, one,
[00:55:10] SPEAKER_02: kind of from the more personal standpoint,
[00:55:13] SPEAKER_02: once you see that light, you can't unsee it.
[00:55:15] SPEAKER_02: You want to do something about it.
[00:55:17] SPEAKER_02: You see this opportunity that you've
[00:55:18] SPEAKER_02: been waiting for your entire life.
[00:55:21] And secondly, I also didn't see an effort
[00:55:23] SPEAKER_02: that would really give it the gravity that this deserves.
[00:55:28] SPEAKER_02: Now, if we're really able to solve this problem,
[00:55:31] we are solving the problem of labor.
[00:55:34] SPEAKER_02: And this requires, I thought this required,
[00:55:36] SPEAKER_02: its own effort that is fully optimized
[00:55:39] SPEAKER_02: for just solving physical intelligence.
[00:55:42] SPEAKER_02: And it shouldn't be a side project inside the company
[00:55:45] SPEAKER_02: or it shouldn't be a project that is trying to solve
[00:55:48] SPEAKER_02: one specific problem of this particular robot
[00:55:51] SPEAKER_02: means to do this particular task.
[00:55:53] SPEAKER_02: I thought that just that problem is so, so important
[00:55:57] SPEAKER_02: that if we see the signs that this can actually be solved,
[00:56:01] SPEAKER_02: we should sort of accompany who solve
[00:56:02] SPEAKER_02: what was the reason to exist is to solve physical intelligence.
[00:56:07] SPEAKER_02: There were a few more components that needed to be true
[00:56:10] SPEAKER_02: for this to make sense.
[00:56:12] SPEAKER_02: It needs to be an effort more similar to OpenAI,
[00:56:15] SPEAKER_02: where there was a lot of capital.
[00:56:17] SPEAKER_02: There was really, really good team, really top in the world team,
[00:56:21] SPEAKER_02: the right focus, the right urgency.
[00:56:23] SPEAKER_02: All of the components need to be there.
[00:56:25] SPEAKER_02: And once we realized that this is actually possible,
[00:56:28] SPEAKER_02: it was a very, very easy decision.
[00:56:32] Great.
[00:56:33] SPEAKER_00: And Kevin, so you're currently getting your PhD at Berkeley,
[00:56:36] SPEAKER_00: is that right?
[00:56:37] Yeah.
[00:56:38] And so, and I know you did an internship at NASA
[00:56:42] SPEAKER_00: on Jet Propulsion engines and a few experiences more
[00:56:47] SPEAKER_00: in the rocket side.
[00:56:48] SPEAKER_00: So why did you join Pi and to join this journey?
[00:56:52] Oh, that's actually my ancient history.
[00:56:55] SPEAKER_01: Like an undergrad.
[00:56:56] SPEAKER_01: I did a little bit of aerospace research.
[00:56:59] SPEAKER_01: Through that, I became connected to JPL.
[00:57:01] SPEAKER_01: Didn't actually work on rockets.
[00:57:04] SPEAKER_01: Be fair.
[00:57:05] SPEAKER_01: I'm mostly a programmer, a computer scientist.
[00:57:07] SPEAKER_01: I work on that kind of stuff.
[00:57:10] At the time that Pi was founded, I was a second year
[00:57:14] SPEAKER_01: PhD student at Berkeley advised by Sergei, who
[00:57:16] SPEAKER_01: was one of the founders.
[00:57:18] SPEAKER_01: And I think that I had decided by then
[00:57:23] SPEAKER_01: that my research mission was very aligned
[00:57:25] SPEAKER_01: with what became the mission of Pi, which is like,
[00:57:28] SPEAKER_01: how can we solve physical intelligence?
[00:57:30] SPEAKER_01: I think I even remembered telling Sergei
[00:57:32] SPEAKER_01: that the research I'm interested in
[00:57:35] SPEAKER_01: is whatever will solve robotics.
[00:57:36] SPEAKER_01: I mean, that's what I care about.
[00:57:38] SPEAKER_01: And I would like to think that I also
[00:57:40] SPEAKER_01: saw the light at the end of the tunnel.
[00:57:42] SPEAKER_01: Even before RT2, I was like, well,
[00:57:45] SPEAKER_01: obviously, machine learning is so, so good.
[00:57:48] SPEAKER_01: I think it definitely will solve robotics at some point,
[00:57:51] SPEAKER_01: or at least make a lot of progress.
[00:57:54] SPEAKER_01: So that was already what I worked on.
[00:57:56] SPEAKER_01: And when Sergei told his students that he was starting this
[00:57:59] SPEAKER_01: company, I was like, yeah, you know,
[00:58:01] SPEAKER_01: I want to work there.
[00:58:02] SPEAKER_01: It's, you know, it's, it's what I want to do.
[00:58:05] SPEAKER_01: It'll be the same research, just with more resources
[00:58:09] SPEAKER_01: and more focused, because it's already what I was working on.
[00:58:13] SPEAKER_01: Yeah, not to like, you know, put my own horn too much,
[00:58:16] SPEAKER_01: but at the time the RT2 came out, you know,
[00:58:18] SPEAKER_01: I said I was trying it in the Berkeley lab,
[00:58:20] SPEAKER_01: but I was actually working on my own project, you know,
[00:58:22] SPEAKER_01: just purely in the lab that was somewhat similar.
[00:58:25] SPEAKER_01: It was basically how to use internet data to get models
[00:58:28] SPEAKER_01: that are really, really general.
[00:58:31] SPEAKER_01: And it worked really well, at least in my setting,
[00:58:33] SPEAKER_01: it worked as well as RT2.
[00:58:34] SPEAKER_01: So I think at the time I was also kind of like, you know,
[00:58:37] SPEAKER_01: this is really, really promising direction.
[00:58:39] SPEAKER_01: I want to be part of this company.
[00:58:41] SPEAKER_01: And this is also, you know, being researchers.
[00:58:44] I think for me, it was also the realization
[00:58:47] SPEAKER_02: that there was a lot of good ideas that we are exploring,
[00:58:51] SPEAKER_02: and we are not really doing them justice.
[00:58:54] SPEAKER_02: We are not really exploring them at the scale
[00:58:56] SPEAKER_02: that they deserve, and we are not getting the quality
[00:58:58] SPEAKER_02: of signal that we should be getting.
[00:59:00] SPEAKER_02: So we actually might be doing the right things,
[00:59:03] SPEAKER_02: we might be exploring the right ideas,
[00:59:05] SPEAKER_02: and there was a lot of smart people working
[00:59:06] SPEAKER_02: on these problems, but there's so resource constraint
[00:59:10] that they're not really able to understand
[00:59:12] SPEAKER_02: which ideas are good, which aren't,
[00:59:14] SPEAKER_02: or try their ideas at the scale that they deserve.
[00:59:17] SPEAKER_02: And we thought that starting a company
[00:59:21] SPEAKER_02: that can provide these resources
[00:59:23] SPEAKER_02: would really allow us to solve this problem fully.
[00:59:26] SPEAKER_02: And I think so far, this has been maybe one
[00:59:29] SPEAKER_02: of the most gratifying outcomes
[00:59:31] SPEAKER_02: that you can come to Pi to do your research
[00:59:35] SPEAKER_02: that you were always interested in,
[00:59:37] SPEAKER_02: but now do it without the constraints that you had before.
[00:59:40] SPEAKER_02: Now you can do it at a very large scale.
[00:59:41] SPEAKER_02: You can have access to very large data sets.
[00:59:43] SPEAKER_02: You can have access to a lot of compute.
[00:59:45] SPEAKER_02: You can work with best people in the world
[00:59:47] SPEAKER_02: that are trying to help you every day.
[00:59:50] SPEAKER_02: And that is very, very gratifying.
[00:59:53] How does someone that's not a researcher, not technical,
[00:59:57] SPEAKER_00: if you're more on the commercial strategy side,
[01:00:00] SPEAKER_00: and they're looking to help move the field forward?
[01:00:03] SPEAKER_00: Like, if you're not technical,
[01:00:05] SPEAKER_00: is there anything that non-technical people can help with
[01:00:07] SPEAKER_00: to build this ecosystem?
[01:00:10] I think so.
[01:00:11] SPEAKER_00: I think there is a lot to be built here,
[01:00:13] SPEAKER_02: and there's probably new business models
[01:00:16] SPEAKER_02: that are going to come up.
[01:00:19] SPEAKER_02: We've seen this in the world of Ovala Lams,
[01:00:22] SPEAKER_02: where people pay for tokens,
[01:00:23] SPEAKER_02: or they pay for API access.
[01:00:26] SPEAKER_02: And these are just the beginnings.
[01:00:29] SPEAKER_02: I suspect that there is going to be many more innovations
[01:00:32] SPEAKER_02: on the business side,
[01:00:33] SPEAKER_02: they're on the commercial side of things,
[01:00:34] SPEAKER_02: and how these models are actually used.
[01:00:36] SPEAKER_02: We also see a lot of product innovations in the LLM side.
[01:00:40] SPEAKER_02: We see companies built on top of these foundation models,
[01:00:43] SPEAKER_02: like cursor and others that are doing really, really well.
[01:00:46] And I think something similar is going to happen here.
[01:00:49] SPEAKER_02: I think this is going to be a very vibrant ecosystem
[01:00:52] SPEAKER_02: with lots of different players,
[01:00:53] SPEAKER_02: some innovating in the business side of things,
[01:00:56] SPEAKER_02: some innovating on the hardware side of things,
[01:00:58] SPEAKER_02: some innovating in specific applications
[01:01:00] SPEAKER_02: that were ripe for automations,
[01:01:01] SPEAKER_02: but so far they weren't able to do this
[01:01:03] SPEAKER_02: because the technology wasn't there.
[01:01:08] SPEAKER_02: So I think there is going to be a lot of room
[01:01:11] SPEAKER_02: for people with many different expertise,
[01:01:15] SPEAKER_02: types of expertise.
[01:01:17] SPEAKER_02: When it comes to us to physical intelligence,
[01:01:20] SPEAKER_02: we are starting to deploy robots.
[01:01:23] SPEAKER_02: And this is something we're really interested in
[01:01:26] SPEAKER_02: because this is something that allows us to scale things up.
[01:01:29] It's really difficult to collect all the data you need
[01:01:32] SPEAKER_02: in a lab environment,
[01:01:33] SPEAKER_02: where you need to replicate every single thing,
[01:01:35] SPEAKER_02: and you do it in sort of a fake way.
[01:01:39] SPEAKER_02: We believe that the best way to collect that data
[01:01:41] SPEAKER_02: or to learn really on how to deploy these models
[01:01:44] SPEAKER_02: is to start to deploy them in the real world,
[01:01:46] SPEAKER_02: start to have them do really valuable,
[01:01:49] SPEAKER_02: economically viable jobs,
[01:01:51] SPEAKER_02: and then learn from that.
[01:01:53] SPEAKER_02: So we'll start looking to deploying these systems more
[01:01:56] SPEAKER_02: and more, whether it's with partners
[01:01:57] SPEAKER_02: or through first party deployments.
[01:02:00] SPEAKER_02: So if this is something you're interested in
[01:02:02] SPEAKER_02: and you're also interested in the commercial aspects of this,
[01:02:06] SPEAKER_02: please reach out.
[01:02:08] Great, and is there specific use cases
[01:02:10] SPEAKER_00: or areas you're starting with?
[01:02:13] This is some environments.
[01:02:16] SPEAKER_02: Yeah, this is something we're still exploring.
[01:02:19] The main vector there that we are optimizing is
[01:02:24] water the deployment areas that will improve
[01:02:27] SPEAKER_02: the capability of the model the most
[01:02:29] SPEAKER_02: and that will allow us to learn the most
[01:02:31] SPEAKER_02: while minimizing friction.
[01:02:33] So we try to pick the areas where it's fairly easy
[01:02:36] SPEAKER_02: to, or it's hard for the right reasons
[01:02:40] SPEAKER_02: and easy for any other reasons.
[01:02:44] But this is something we're still exploring
[01:02:46] SPEAKER_02: and trying to figure out.
[01:02:49] Great, all right, let's get guys ready to wrap it up
[01:02:50] SPEAKER_00: with a little rapid fire.
[01:02:53] All right, let's do it.
[01:02:54] SPEAKER_02: Let's do it.
[01:02:55] SPEAKER_00: All right, Carl, I'll go over to you first
[01:02:57] SPEAKER_00: and then I'll go over to you Kevin, all right?
[01:03:00] What's one assumption about robotics
[01:03:02] SPEAKER_00: that the AI research community gets completely wrong?
[01:03:15] That we are about to have scaling laws
[01:03:17] SPEAKER_02: that look very, very similar to LLM and VLM scaling laws.
[01:03:20] SPEAKER_02: I think scaling laws and robotics are very hard
[01:03:25] SPEAKER_02: and we don't even know what the Y axis
[01:03:28] SPEAKER_02: of that scaling law should be.
[01:03:31] SPEAKER_02: And I think people tend to just rush towards
[01:03:34] SPEAKER_02: putting something out there that they have
[01:03:36] SPEAKER_02: some kind of scaling law of robotics
[01:03:38] SPEAKER_02: based on what they've seen in LLM and VLM's before.
[01:03:41] But I think this is actually going to be
[01:03:43] SPEAKER_02: much more complicated.
[01:03:46] Kevin?
[01:03:48] That's a good one.
[01:03:49] SPEAKER_01: That's a more unique one, I think.
[01:03:50] SPEAKER_01: I thought it's only very obvious, which is like,
[01:03:53] SPEAKER_01: a lot of people think humanoid's are just the way to go,
[01:03:55] SPEAKER_01: like nothing else matters,
[01:03:56] SPEAKER_01: but getting like really good humanoid robots.
[01:03:59] SPEAKER_01: And I think our ethos as a company is very,
[01:04:01] SPEAKER_01: sort of the opposite of that,
[01:04:02] SPEAKER_01: which is we want to be able to control any robot
[01:04:05] SPEAKER_01: and that having all sorts of different types of robots
[01:04:07] SPEAKER_01: will be very important, not just a humanoid form factor.
[01:04:11] What's one assumption about robotics,
[01:04:14] SPEAKER_00: the public gets completely wrong?
[01:04:19] I guess humanoid one I think is actually both the public
[01:04:22] SPEAKER_01: and some part of the research community,
[01:04:25] SPEAKER_01: both like it's popular both among the public
[01:04:28] SPEAKER_01: and among researchers, I think.
[01:04:31] Yeah, I'll think of another one.
[01:04:33] I think that one is very good.
[01:04:35] The other one, and I don't know if there's like an assumption
[01:04:38] SPEAKER_02: or explicit assumption,
[01:04:39] SPEAKER_02: I could articulate, but I think in general,
[01:04:43] SPEAKER_02: we, including myself, are not very good at judging
[01:04:46] SPEAKER_02: progressing robotics or judging what is impressive
[01:04:49] SPEAKER_02: and what isn't.
[01:04:51] We've seen these incredible videos from bustling dynamics
[01:04:54] SPEAKER_02: from like a decade ago of robots doing backflips
[01:04:57] SPEAKER_02: and all kinds of different like robotics.
[01:05:00] SPEAKER_02: And we usually extrapolate from that.
[01:05:02] SPEAKER_02: And this is something that's very difficult for a person to do
[01:05:04] SPEAKER_02: so you think that the robots are way ahead,
[01:05:07] but then it turns out that something as simple
[01:05:10] SPEAKER_02: as picking a cocan turns out to be very, very difficult
[01:05:14] SPEAKER_02: for these robots.
[01:05:15] SPEAKER_02: So I think we don't have very good understanding
[01:05:18] SPEAKER_02: of what is difficult and what is easy.
[01:05:22] And I wish we just had better intuition on these things,
[01:05:24] SPEAKER_02: but we don't.
[01:05:26] What's that called as a more, is it more of X principle?
[01:05:28] SPEAKER_00: Is that right?
[01:05:29] SPEAKER_00: More of X paradox.
[01:05:31] SPEAKER_01: paradox X.
[01:05:32] SPEAKER_01: Hard, what's the hard, Kevin?
[01:05:33] SPEAKER_00: What's the harder problem perception and manipulation?
[01:05:38] I mean, they're intertwined because of course
[01:05:40] SPEAKER_01: you have to perceive something to manipulate it.
[01:05:42] SPEAKER_01: I think the way you would traditionally use these terms
[01:05:45] SPEAKER_01: within the field, if you use those definitions,
[01:05:49] SPEAKER_01: I think perception is like, I can solve a little bit.
[01:05:52] SPEAKER_01: Like only recently, but I mean, I think large models
[01:05:55] SPEAKER_01: are really, really good at perception.
[01:05:57] SPEAKER_01: They can segment any image, they can build 3D reconstructions,
[01:06:00] SPEAKER_01: they can do all sorts of crazy stuff.
[01:06:02] SPEAKER_01: I didn't think it was possible like a few years ago.
[01:06:06] SPEAKER_01: I think, you know, manipulation is quite obviously
[01:06:08] SPEAKER_01: the hard part is once you actually start
[01:06:09] SPEAKER_01: to interact with the world, it gets way more difficult.
[01:06:12] Having also that split is completely artificial.
[01:06:15] SPEAKER_02: You know, I don't think perception by itself kind of exists.
[01:06:20] SPEAKER_02: I don't think that's this like a thing
[01:06:22] SPEAKER_02: that like you segment the images or you classify them.
[01:06:26] SPEAKER_02: I think the only reason why you do that
[01:06:27] SPEAKER_02: is to manipulate the world around you
[01:06:28] SPEAKER_02: and these two really interact with each other,
[01:06:31] SPEAKER_02: often you manipulate to perceive things better.
[01:06:33] SPEAKER_02: And then when you perceive it better,
[01:06:35] SPEAKER_02: it allows you to accomplish your goal better.
[01:06:38] So I think this is going to change.
[01:06:40] SPEAKER_02: I think both of these are going to become the same problem.
[01:06:44] All right, last one.
[01:06:46] SPEAKER_00: One book you would gift to a young robot assistant engineer.
[01:06:57] Nice, I say Sergei Substak.
[01:07:03] Okay, we'll put that in the link.
[01:07:04] SPEAKER_00: We'll put that in the show notes.
[01:07:09] Sergei Substak, that's pretty good.
[01:07:11] SPEAKER_02: I agree.
[01:07:13] Wow, two for Sergei.
[01:07:14] SPEAKER_00: No, yeah, come on Carl.
[01:07:15] SPEAKER_00: Okay, let's give us one more.
[01:07:21] I think, you know, even though the part I'm exchanging,
[01:07:25] SPEAKER_02: I would still probably read on the fundamental
[01:07:27] SPEAKER_02: of how robots work, how the mechanics of them work,
[01:07:30] SPEAKER_02: how inverse kinematics works, how control algorithms work.
[01:07:33] SPEAKER_02: I think a lot of those things, even though a lot of them
[01:07:37] SPEAKER_02: are getting less and less relevant in today's world,
[01:07:40] SPEAKER_02: I think having these foundations really helps you
[01:07:42] SPEAKER_02: think about problems.
[01:07:45] SPEAKER_02: I don't know if I have specific recommendation there,
[01:07:47] SPEAKER_02: but I would just take a robotics 101 course
[01:07:50] SPEAKER_02: and try to learn as much as possible.
[01:07:53] Great.
[01:07:54] SPEAKER_00: How can folks reach out?
[01:07:55] SPEAKER_00: What's easiest way to connect with you all?
[01:07:59] SPEAKER_02: You can check out our website, PI.website.
[01:08:02] SPEAKER_02: And there's contact emails there.
[01:08:05] SPEAKER_02: There's one called Collaborate at physical intelligence
[01:08:08] SPEAKER_02: of the company.
[01:08:08] SPEAKER_02: You can reach us there.
[01:08:12] We are also active on Twitter.
[01:08:14] SPEAKER_02: Yeah, you should be able to reach out to us fairly easily.
[01:08:18] Great.
[01:08:19] SPEAKER_00: Cool.
[01:08:20] SPEAKER_00: Well, thanks Carl, Kevin.
[01:08:21] SPEAKER_00: We appreciate the time once again.
[01:08:23] SPEAKER_00: And yeah, we look forward to following the progress
[01:08:25] SPEAKER_00: and hopefully we can have many more down the line
[01:08:29] SPEAKER_00: as everything continues to develop.
[01:08:31] SPEAKER_00: So.
[01:08:32] Thank you. This was fun.
[01:08:33] SPEAKER_02: Yeah.
[01:08:34] SPEAKER_02: Thank you.
[01:08:34] SPEAKER_02: This is great.
[01:08:35] Thanks, guys.
[01:08:37] Yeah.
[01:08:38] Two, one, let's go.
[01:08:42] Go, go.