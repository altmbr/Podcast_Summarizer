# 【BAAI2025】 Building Physical Intelligence | Karol Hausman

**Podcast:** One-off Episodes
**Date:** 2025-06-07
**Video ID:** 5H2UrJ2N3t0
**Video URL:** https://www.youtube.com/watch?v=5H2UrJ2N3t0

---

[00:00:00] Hello, thank you for having me and sorry that I can't be there in person.
[00:00:03] SPEAKER_00: I really appreciate the invitation and today I wanted to tell you a little bit about building
[00:00:08] SPEAKER_00: physical intelligence.
[00:00:09] SPEAKER_00: I'm a co-founder and CEO of physical intelligence.
[00:00:14] SPEAKER_00: So unless you've been living under a rock over the past few years, you probably noticed
[00:00:20] SPEAKER_00: that something happened in robotics.
[00:00:23] SPEAKER_00: So the robotics that we are used to looked more like this, where we have robots that can
[00:00:28] do very repeatable tasks go from A to B very well, very fast.
[00:00:33] SPEAKER_00: But as soon as we introduce a little bit of lack of structure, they would very often
[00:00:40] SPEAKER_00: result in something like this, where the robot was not able to deal with the chaos of the
[00:00:45] SPEAKER_00: world and the structure environment and it would basically catastrophically fail.
[00:00:50] But then it seems like something happened and right now robotics looks very different.
[00:00:55] SPEAKER_00: It looks more like this.
[00:00:57] You know, we see extremely smooth, impressive dance moves from many different humanoid robots.
[00:01:05] SPEAKER_00: And we see robots deal with unstructured environments like this one, just fine.
[00:01:10] So the question I want to answer today is, well, what happened?
[00:01:14] SPEAKER_00: There seems to be a very big difference between the robotics of the past and robotics of
[00:01:19] SPEAKER_00: today.
[00:01:22] So over the past year, I've been building physical intelligence and I've been building
[00:01:27] SPEAKER_00: it in two different ways.
[00:01:30] SPEAKER_00: On one hand, I started a company called Physical Intelligence.
[00:01:33] SPEAKER_00: We started around a year ago with the idea that we want to build them all that can control
[00:01:38] SPEAKER_00: any robot to do any task, truly solve physical intelligence.
[00:01:44] SPEAKER_00: On the other hand, I also had a daughter who is around a one year old today.
[00:01:48] SPEAKER_00: So I experienced emergent physical intelligence almost every day these days.
[00:01:53] And if I were to draw a conclusion from these two things, is that if you're thinking
[00:01:58] SPEAKER_00: of starting a company and having a baby at the same time, please talk to me, I did not
[00:02:03] SPEAKER_00: recommend that.
[00:02:04] SPEAKER_00: Don't do it.
[00:02:06] All right.
[00:02:07] SPEAKER_00: So back to the question, what happened?
[00:02:10] I think the very obvious answer is, well, AI happened.
[00:02:15] And there are many different versions of this answer that actually matter here.
[00:02:20] SPEAKER_00: And I think the one in particular that has been really, really important, I want to focus
[00:02:24] SPEAKER_00: on is vision language action models.
[00:02:29] So let me tell you a little bit more about them and why I'm very excited about them.
[00:02:34] So how do they work?
[00:02:36] They work fairly similar to vision language models that we know from products like CHEDGPT.
[00:02:42] So in a vision language model, the way it works is that it takes some data from the
[00:02:46] SPEAKER_00: internet.
[00:02:47] SPEAKER_00: For instance, in the image that you can find on the internet, an image of a cat, then you
[00:02:51] can ask it, what is this?
[00:02:53] SPEAKER_00: What do you see in the image?
[00:02:55] SPEAKER_00: And then this model is trying to answer it in natural language as well.
[00:02:59] SPEAKER_00: So it would answer with the word cat.
[00:03:02] Now it turns out that we can take that model, this vision language model, and adjust it
[00:03:07] SPEAKER_00: a little bit to be practical for robots and actually really, really powerful for them.
[00:03:14] SPEAKER_00: So the way it works is the following.
[00:03:16] We'll take a vision language action model now.
[00:03:19] And instead of having an image from the internet, we would have the camera feed from the robot.
[00:03:23] SPEAKER_00: So what the robot currently sees.
[00:03:26] And instead of asking it in a question that you can answer in natural language, we'll
[00:03:29] SPEAKER_00: ask it to do something.
[00:03:31] SPEAKER_00: We'll ask it to do a task like fold the shirt.
[00:03:34] Now given that that model has also seen robotics data, and in particular data from many different
[00:03:39] SPEAKER_00: robots doing many different tasks, it turns out that it can output an image from the robot.
[00:03:43] SPEAKER_00: It can output an answer that tells you how to do that task.
[00:03:47] SPEAKER_00: So it actually outputs modern commands for the robot to do the motion to accomplish that
[00:03:52] SPEAKER_00: task.
[00:03:53] Now, it's a very simple idea.
[00:03:55] SPEAKER_00: It's basically a vision language model adjusted to deal with robotic data.
[00:04:00] SPEAKER_00: But it turns out it's really, really powerful.
[00:04:05] So why is this, why is this a powerful, why is this a big deal?
[00:04:09] Well, traditionally that kind of thinking where you can train the model fully into end
[00:04:16] SPEAKER_00: that can understand what the robot sees and output the correct actions has been really
[00:04:20] SPEAKER_00: hard because these models require a lot of data.
[00:04:23] But with this idea, the idea of vision language action model, it turns out that you can collect
[00:04:27] SPEAKER_00: data from many other sources.
[00:04:30] So one, you can connect data from the web.
[00:04:34] In the past, we thought that to make a model like this work, you would need to have a robot
[00:04:38] SPEAKER_00: experience the entire world firsthand.
[00:04:40] SPEAKER_00: It would need to experience every single object, every single situation to learn about it.
[00:04:46] But then it turns out that you can take a pre-trained vision language model.
[00:04:49] SPEAKER_00: It was pre-trained on the web data and has some high level understanding of how the world
[00:04:54] SPEAKER_00: works and transfer some of that meaning to robot motion.
[00:05:00] And one particular result that I was an outer off that showed that actually doesn't look
[00:05:06] SPEAKER_00: that impressive, but it was completely mind blowing to us was from Robotic Transformer
[00:05:10] SPEAKER_00: 2 showing the following.
[00:05:12] SPEAKER_00: This is a robot being asked to move the co-can to Taylor Swift.
[00:05:17] Now I'll show it to you again, watch closely, the robot picks up a co-can and moves it to
[00:05:22] SPEAKER_00: the picture of Taylor Swift.
[00:05:24] It doesn't do a great job.
[00:05:25] SPEAKER_00: The co-can falls.
[00:05:26] SPEAKER_00: You can see that it's kind of pathetic.
[00:05:29] But to us, watching this experiment live, that was a very, very big deal.
[00:05:34] And the reason is that the robot has never seen pictures of Taylor Swift.
[00:05:38] SPEAKER_00: It's never seen any pictures of any of these celebrities or any other pictures.
[00:05:43] It had that abstract concept of who Taylor Swift is and what the picture of Taylor Swift
[00:05:48] SPEAKER_00: looks like straight from the internet.
[00:05:52] So it was able to get that knowledge from web scale pre-training and then translate that
[00:05:57] SPEAKER_00: knowledge and connect it to robot motion to actually express that understanding through
[00:06:03] SPEAKER_00: an embodied movement.
[00:06:07] SPEAKER_00: So that for the first time showed us that it's actually possible to get all of that knowledge
[00:06:10] SPEAKER_00: not firsthand.
[00:06:11] SPEAKER_00: The robot doesn't have to experience the world every single situation.
[00:06:14] SPEAKER_00: And it's something to experience quite a bit of it, but can get a lot of that understanding
[00:06:18] SPEAKER_00: from the internet instead.
[00:06:21] SPEAKER_00: So that was one.
[00:06:22] The second one that made it really, really impactful is the fact that not only we can
[00:06:26] SPEAKER_00: connect it to the data from the web, but we can connect it from data from other robots.
[00:06:32] So it turns out that these models don't really care whether all the data comes from a single
[00:06:36] SPEAKER_00: embodiment or many different embodiments or a robot that has one arm or two arms or it's
[00:06:41] SPEAKER_00: a mobile robot or a drone.
[00:06:44] It doesn't really matter.
[00:06:45] SPEAKER_00: At the end of the day, it's a pattern of numbers and pattern of different data that these
[00:06:51] SPEAKER_00: neural networks can find and can understand well.
[00:06:56] So to do this, we run an experiment called RTX where we collaborated with many different
[00:07:01] SPEAKER_00: research institutions around the world, 34 of them, and asked them to send us the most
[00:07:06] SPEAKER_00: recently collected data sets that they used to publish their research.
[00:07:11] SPEAKER_00: Now if you've done academic research, you know that the way it works is you collected
[00:07:14] SPEAKER_00: data set and then you try to get your method that you're about to publish really, really
[00:07:19] SPEAKER_00: work.
[00:07:20] SPEAKER_00: And you're very heavily incentivized to get it to work because that's what you want
[00:07:24] SPEAKER_00: to publish.
[00:07:26] So we took all of those data sets that were published for different methods and we combine
[00:07:30] SPEAKER_00: them into one big data set and train one big generalist model on that.
[00:07:34] So that was trained on many different robots that look different, that have different
[00:07:37] SPEAKER_00: number of degrees of freedom.
[00:07:39] SPEAKER_00: Sometimes it's two arms, sometimes it's one arm, it doesn't really matter.
[00:07:43] And then we send the checkpoint of that model, of that generalist model to these individual
[00:07:47] SPEAKER_00: labs and ask them to compare it to their state of the art method that they just developed.
[00:07:54] Now importantly, it's a different state of the art method in every single lab because
[00:07:59] SPEAKER_00: every single lab develop a specialist solution for the problem that they were trying to publish
[00:08:03] SPEAKER_00: on.
[00:08:05] And then it turned out that as a result, our generalist model was able to beat that baseline that
[00:08:11] SPEAKER_00: state of the art method every single time on average by more than 50%.
[00:08:17] SPEAKER_00: And that points to the fact that these models are really data hungry and they can make
[00:08:20] SPEAKER_00: sense out of data coming from many different embodiments and then can do it much better
[00:08:24] SPEAKER_00: than we can.
[00:08:28] SPEAKER_00: So with these two, we decided that this is a technology that would allow us to build
[00:08:33] SPEAKER_00: a model to control any robot to do any task.
[00:08:36] SPEAKER_00: And that's where we started physical intelligence.
[00:08:39] Now the way we want to do this is to build a generalist model that will be trained on many
[00:08:43] SPEAKER_00: tasks and many robots with the idea that we'll be able to generalize beyond that.
[00:08:48] In particular, it will be a generalist vision language action model that will be trained
[00:08:52] on many tasks and many robots.
[00:08:56] Now as we started that journey, we thought that there was going to be three big challenges
[00:09:01] SPEAKER_00: that we really need to de-rescan understand better.
[00:09:04] These are capability.
[00:09:06] Are these models capable of doing tasks that we've never seen robots do before that are
[00:09:10] SPEAKER_00: very dexterous, long horizon and so on?
[00:09:13] Secondly generalization.
[00:09:15] Can they generalize to an extent where you can put them in a completely new room, in
[00:09:18] SPEAKER_00: a completely new environment and they know how to do it?
[00:09:22] And then third performance.
[00:09:23] SPEAKER_00: Can they perform at a very high clip with very high success rate and be extremely robust?
[00:09:29] So we started with the first one capability.
[00:09:33] Around five months into the company, we arrived at these results.
[00:09:37] SPEAKER_00: This is a demo you might have seen showing one of our robots unloading a dryer, taking
[00:09:43] SPEAKER_00: all of the laundry into a basket, bringing it over to a folding table and then folding
[00:09:49] SPEAKER_00: it one by one.
[00:09:51] You can see that it's not perfect.
[00:09:53] SPEAKER_00: It makes quite a lot of mistakes, but it can correct basically all of them.
[00:09:57] SPEAKER_00: It's still fairly slow.
[00:09:58] SPEAKER_00: It doesn't work every single time.
[00:10:01] SPEAKER_00: But this is a task that for a very long time has been considered a holding rail of robotics.
[00:10:06] This is something that we've been able to achieve five months into the company.
[00:10:10] SPEAKER_00: And this is not a model that is specialized in this particular task.
[00:10:14] The exact same model could do laundry folding like the one you see.
[00:10:18] SPEAKER_00: It could also work on static robots, whether it's single arm or two arm robots.
[00:10:22] SPEAKER_00: It could also work on different mobile robots and do many, many other different tasks.
[00:10:27] So I wanted to tell you a little bit about what we did to make it work.
[00:10:32] So we trained this generalist robot policy.
[00:10:34] SPEAKER_00: We call it Pi0.
[00:10:36] SPEAKER_00: This is our first model that we released in October last year.
[00:10:39] That was pre-trained on many different robot form factors that you see here on the left
[00:10:43] SPEAKER_00: and across many, many different tasks.
[00:10:47] Now we also use a pre-trained vision language model to get that internet scale pre-training
[00:10:52] SPEAKER_00: that I talked about earlier, as well as the open data sets, open source data that I talked
[00:10:57] SPEAKER_00: about as well.
[00:10:59] And then from that we built a single architecture, single vision language action molecule Pi0
[00:11:05] that has an action expert that allows it to actually output actions.
[00:11:10] Now it can do multiple things.
[00:11:12] SPEAKER_00: First it can work zero shot where you can just prompt it and forecast it.
[00:11:15] SPEAKER_00: It's seen before it can perform them fairly well.
[00:11:18] But you can also find unit.
[00:11:21] SPEAKER_00: And you can find unit with what we call post training that is much higher quality data,
[00:11:25] SPEAKER_00: which allows you to do two things.
[00:11:28] SPEAKER_00: One, it allows you to kind of specialize this model for tasks that are particularly difficult.
[00:11:34] SPEAKER_00: So for something like long-refolding, it's not enough to just pre-training.
[00:11:37] SPEAKER_00: You kind of need to find unit to tell it how exactly you want your close to be folded.
[00:11:43] SPEAKER_00: So you can also use it to train new tasks very, very quickly.
[00:11:50] So before I tell you a little bit more about the architecture, I wanted to kind of have
[00:11:54] you appreciate a little bit how hard of a task it is.
[00:11:56] SPEAKER_00: It seems like folding laundry is not that difficult.
[00:11:59] SPEAKER_00: We do it every other day or so.
[00:12:02] But it turns out that it's actually quite tricky.
[00:12:04] SPEAKER_00: So here are a few examples, the same model running on static robots.
[00:12:07] SPEAKER_00: You can see this is a problem where you find a shirt that is in arbitrary configuration.
[00:12:13] SPEAKER_00: And you see how many different motions you need to do to grab the corners correctly.
[00:12:17] SPEAKER_00: You can see that the robot eventually grasped the sleeve correctly.
[00:12:21] SPEAKER_00: It kind of flattens it out a little bit.
[00:12:23] SPEAKER_00: Once it's done, then it grasps the corner well, then it folds it in half, brings the
[00:12:27] SPEAKER_00: shirt a little bit closer to itself, folded again, then it folds it in half, then straight
[00:12:33] SPEAKER_00: on the set out.
[00:12:34] SPEAKER_00: That also takes quite a bit of work.
[00:12:35] SPEAKER_00: And then does this beautiful dynamic motion to fold it one more time, brings the pile over
[00:12:40] SPEAKER_00: and pulls the shirt on top of it.
[00:12:43] Here's another example with a piece of clothing that the robot has never seen before.
[00:12:48] So you can see that the shirt is in some weird configuration.
[00:12:52] SPEAKER_00: The robot tries to flatten it out and it realizes that something is off that tries it a few
[00:12:57] SPEAKER_00: times.
[00:12:58] SPEAKER_00: And then eventually it figures out that it actually didn't grasp the right corner.
[00:13:02] SPEAKER_00: So it means to put it down, grasp it again, grasp the corner correctly, then brings it
[00:13:06] SPEAKER_00: over, folds it in half, folds the other half, and then eventually is able to straighten out
[00:13:12] SPEAKER_00: the shirt to the final dynamic motion at the end and puts it on a pile of clothes.
[00:13:19] In fact, the system is robust enough so that you can interrupt it.
[00:13:23] SPEAKER_00: And it can handle these interruptions quite well.
[00:13:25] SPEAKER_00: So here's a robot mining its own business trying to fold the clothes.
[00:13:29] SPEAKER_00: And then one of our researchers, Michael, is putting another shirt in trying to mess with
[00:13:33] SPEAKER_00: it.
[00:13:34] SPEAKER_00: And you can see that the robot kind of realizes what's happening, puts the shirt back and
[00:13:37] SPEAKER_00: tries to do its job.
[00:13:41] SPEAKER_00: This is not something that we trained specifically for, it's just something that emerges from
[00:13:44] SPEAKER_00: large scale training like that.
[00:13:47] SPEAKER_00: You can also mess with it in other ways.
[00:13:50] SPEAKER_00: Here's the robot trying to fold the shirt in half.
[00:13:52] And while it's kind of halfway through, Michael comes in, now we mean the researcher and
[00:13:56] SPEAKER_00: unfolds it.
[00:13:57] So then the robot starts again, and starts with the other half, Michael comes in and
[00:14:00] SPEAKER_00: undoes it again.
[00:14:01] SPEAKER_00: Now you can see that one of the corners is a little bit off.
[00:14:04] SPEAKER_00: So the robot needs to figure that one out.
[00:14:07] SPEAKER_00: It finds the corner correctly and then eventually folds it and keeps on going.
[00:14:13] So this is what these monsters are capable of.
[00:14:15] SPEAKER_00: But the most important, if I were to distill it into one inside that was really, really important
[00:14:20] SPEAKER_00: to get it to work is the inside of pre-training and post-training.
[00:14:24] And what I mean by this is the following.
[00:14:27] So for Python zero, we had pre-training data that consisted of 10,000 hours.
[00:14:33] SPEAKER_00: So many different tasks across many different robots were in that case, we tried to cram as
[00:14:39] SPEAKER_00: much data into the model as possible, very similar to the pre-training stage for large
[00:14:43] SPEAKER_00: language models.
[00:14:46] But then we would go to the next stage called post-training, where we would collect orders
[00:14:50] SPEAKER_00: of magnitude less data of high quality around 20 hours of data to kind of get this model
[00:14:56] SPEAKER_00: to behave exactly like we wanted.
[00:14:58] SPEAKER_00: So kind of pick the mode of behavior that we actually meant.
[00:15:02] We can do this for laundry folding, we can do it for building boxes or many, many other
[00:15:07] SPEAKER_00: tasks.
[00:15:09] And that turned out to be really, really important to get it to work.
[00:15:14] So in particular, to give you some quantitative evaluation, we can compare three different
[00:15:19] SPEAKER_00: approaches.
[00:15:20] SPEAKER_00: We can compare the approach I just described where we do pre-training and then post-training.
[00:15:24] We'll be comparing it to an approach where we have no robot pre-training.
[00:15:27] SPEAKER_00: So we just train on this curated data set of really, really good high quality data.
[00:15:33] And we'll compare it to an approach where there is no post-training.
[00:15:36] SPEAKER_00: So we just train on all the data and that's it.
[00:15:38] And here are the results.
[00:15:41] So if we do both pre-training and post-training, we see the highest number, this is where
[00:15:47] SPEAKER_00: we can get really, where we can get really foreign this folding task.
[00:15:51] Because it turns out that you kind of need both to first understand the motions of how
[00:15:56] SPEAKER_00: to deal with all kinds of different situations, which you get from pre-training.
[00:16:00] SPEAKER_00: And then you need post-training to really fine tune those motions together to really
[00:16:04] SPEAKER_00: the result you want.
[00:16:07] SPEAKER_00: Now if you just do, if you don't do any pre-training, if you just do curated data set, it turns
[00:16:11] SPEAKER_00: out that the performance drops significantly.
[00:16:14] And the reason for that is that you know how to fold things perfectly, but the real world
[00:16:18] SPEAKER_00: is not perfect.
[00:16:19] SPEAKER_00: You're going to fail, you're going to make mistakes, and you don't know how to deal with that
[00:16:22] SPEAKER_00: diversity, how to correct those behaviors, because you've never seen that situation.
[00:16:26] SPEAKER_00: You've only seen perfect data.
[00:16:29] And then lastly, if you didn't apply any post-training, that means you know more or less how to fold
[00:16:35] SPEAKER_00: close, but you don't really know what exactly we want.
[00:16:39] And that also drops in performance quite a bit.
[00:16:44] So now one question you might ask is, you know this is a generalist model, right?
[00:16:48] SPEAKER_00: That's not just a model used for laundry folding or building boxes or many of the other tasks
[00:16:52] SPEAKER_00: I mentioned.
[00:16:53] It was also trained on many other robots.
[00:16:56] SPEAKER_00: So can you use it?
[00:16:57] SPEAKER_00: Can anyone use it?
[00:16:59] And the answer is yes.
[00:17:01] SPEAKER_00: We open source up model.
[00:17:03] SPEAKER_00: We open source it in a repository called OpenPie, where we open source many different checkpoints
[00:17:07] SPEAKER_00: of it.
[00:17:08] SPEAKER_00: We have different robot runtimes, have you can integrate it into your framework.
[00:17:12] And we have many, many people using it, fine tuning it on all kinds of different applications
[00:17:16] SPEAKER_00: ranging from robotic surgery to autonomous driving to many, many other tasks.
[00:17:22] In addition to this, we also started the partnership program.
[00:17:25] SPEAKER_00: Here's one partnership video with Astrobot humanoid robot, showing a robot making copy.
[00:17:31] SPEAKER_00: And you can see it being a robot that is more complex, has many more degrees of freedom.
[00:17:35] SPEAKER_00: It's kind of harder to control because of that.
[00:17:37] SPEAKER_00: But we can take a pre-trained Pi0 model and fine tune it to a new embodiment like this
[00:17:42] SPEAKER_00: and do a task with this fairly dexterous that the robot can perform fairly well with
[00:17:48] SPEAKER_00: this generalist policy.
[00:17:50] All right.
[00:17:53] SPEAKER_00: So since I mentioned humanoids, I wanted to spend a few more minutes on humanoids.
[00:18:00] SPEAKER_00: You've probably seen that the world went crazy about humanoids.
[00:18:04] SPEAKER_00: There's many different humanoids.
[00:18:06] SPEAKER_00: There isn't a day where you don't hear about a new humanoid being developed.
[00:18:09] There's many different companies making those robots amazing pieces of mechatronics, robots
[00:18:14] SPEAKER_00: that will be capable of many, many things.
[00:18:17] And we've seen all kinds of different applications and demos of these robots, whether it's in the
[00:18:21] SPEAKER_00: home or in some kind of structured home environment where they're collaborating and doing fairly
[00:18:26] SPEAKER_00: dexterous tasks.
[00:18:29] Now I believe that if we actually succeed, if we actually crack the problem of physical
[00:18:35] SPEAKER_00: intelligence and build these models that are extremely general, I don't think we're
[00:18:40] SPEAKER_00: going to stop at humanoids.
[00:18:42] I think we're going to experience a Cambrian explosion of robots.
[00:18:45] SPEAKER_00: Because let's be honest, if you wanted to do something like sort packages, you wouldn't
[00:18:50] be doing of a humanoid if you wanted to automate that.
[00:18:54] If you were to automate it, you would want to do it way better than humans.
[00:18:57] SPEAKER_00: You would do it with a robot like this.
[00:19:00] And that turns out to be true for many different applications.
[00:19:03] SPEAKER_00: You can do much, much better than humans can because it's not our form factor that makes
[00:19:08] SPEAKER_00: us special.
[00:19:09] SPEAKER_00: It's our brain, our physical intelligence that makes us special.
[00:19:13] SPEAKER_00: So we can see all kinds of different robots being applied to many different domains.
[00:19:18] SPEAKER_00: And I believe all of them can be powered by a single, generalist model, like Pi's
[00:19:23] SPEAKER_00: Euro.
[00:19:24] So for instance, if you want to do roofing, you will use a very different robot.
[00:19:29] If you want to do some kind of self assembly or space exploration, you'll do very different,
[00:19:33] SPEAKER_00: you'll do this very different robot.
[00:19:34] SPEAKER_00: If you want to do firefighting, you'll use very different robot.
[00:19:37] SPEAKER_00: If you wanted to do agriculture, you'll use a different robot.
[00:19:40] SPEAKER_00: And if you wanted to do recycling, you'll use a very different robot.
[00:19:43] SPEAKER_00: And there's many, many more applications for those way, better form factors that are
[00:19:46] SPEAKER_00: superhuman in some way.
[00:19:49] But they can be powered by the same general brain.
[00:19:53] All right, so sorry about this small aggression.
[00:19:56] I talked a little bit about capability.
[00:19:59] So next in our journey, we tackle generalization.
[00:20:03] So one caveat about all the demos you've seen, and you see day-to-day about robots is that
[00:20:10] SPEAKER_00: they're always evolving in the environment that they've been trained in.
[00:20:13] So the demo that I showed you earlier in a home where the robot is falling laundry, if
[00:20:17] SPEAKER_00: were to bring it to your home, it probably wouldn't work.
[00:20:19] SPEAKER_00: It hasn't seen that home.
[00:20:22] SPEAKER_00: And this is one of the big, big bottlenecks that prevents us from deploying these machines.
[00:20:27] So as the next step, we wanted to tackle that problem and get robots to generalize to a
[00:20:30] SPEAKER_00: completely new environment they've never seen before.
[00:20:33] And it turns out that it's possible.
[00:20:36] So this is a project we call Pi-0.
[00:20:38] SPEAKER_00: Do you think the battery?
[00:20:40] Where we bring robots to completely new homes that they've never been to before.
[00:20:44] SPEAKER_00: So this is a new Airbnb that we rented in San Francisco.
[00:20:47] SPEAKER_00: And here's our researcher, Laura, asking it to clean the bedroom.
[00:20:52] SPEAKER_00: The robot has never seen the bedroom before.
[00:20:54] SPEAKER_00: It starts putting the clothes away, then it puts trash in the trash can, and then it makes
[00:20:58] SPEAKER_00: the bed at the end.
[00:21:00] In fact, all our evaluation in that work has been done in completely new environments
[00:21:06] SPEAKER_00: that the robot has never seen before.
[00:21:08] SPEAKER_00: So you're literally driving around San Francisco assembling the robot and putting it in environments
[00:21:13] SPEAKER_00: that's never seen before in evaluating it on the network.
[00:21:18] Now the most important quantitative result from the work is this.
[00:21:22] SPEAKER_00: And this is a plot that we've been waiting for for very, very long time.
[00:21:26] So let me describe a little bit what it shows.
[00:21:29] Here on the X-axis, you see a number of locations that the robot was trained on.
[00:21:33] SPEAKER_00: So the robot has seen many different homes.
[00:21:36] SPEAKER_00: And the X-axis is how many homes it's seen in its training data.
[00:21:40] And on the Y-axis, we see the average task progress.
[00:21:43] SPEAKER_00: So the task performance and this is in a new home that the robot has never seen before.
[00:21:49] Now you see here this yellow line shows you the performance in this unseen location using
[00:21:54] SPEAKER_00: our method, our Pi-05 model.
[00:21:58] And it turns out that the performance goes up and up, the more homes you've seen in your
[00:22:02] SPEAKER_00: training data.
[00:22:04] And by the time you've seen 100 different homes, if you go to the 100 first home that
[00:22:09] SPEAKER_00: you've never seen before, turns out that the performance is very high.
[00:22:12] SPEAKER_00: It's over 80%.
[00:22:14] Now you can also compare it to a situation if you had data in that environment.
[00:22:19] SPEAKER_00: So if you just came into that home, collect the data in that home, what is that performance?
[00:22:24] SPEAKER_00: And this is what you see in this bar that is in green.
[00:22:28] SPEAKER_00: So this is if you had in the main data.
[00:22:31] SPEAKER_00: So it turns out that you can visit around 100 homes.
[00:22:33] SPEAKER_00: And by the time you go to the 100 first home that you've never seen before, your performance
[00:22:37] SPEAKER_00: will be similar in that never seen before home to the situation as if you collected data
[00:22:44] SPEAKER_00: in that home.
[00:22:46] And this is something before we started this project was extremely unclear.
[00:22:49] SPEAKER_00: Some of us thought maybe you need to visit the million different homes to be able to
[00:22:52] SPEAKER_00: generalize that way.
[00:22:54] It turns out that around 100, you're able to basically get that performance.
[00:22:59] Now two other really important caveats here is that if you don't use pre-training that
[00:23:04] SPEAKER_00: I talked about before, the performance drops significantly even if you're using the main
[00:23:08] SPEAKER_00: data.
[00:23:09] SPEAKER_00: This is the light green bar.
[00:23:12] SPEAKER_00: Now if you train on all the 104 locations and on your pre-training, the performance
[00:23:16] SPEAKER_00: and the performance even more.
[00:23:19] And this speaks to the power of models that are very general that are trained on many,
[00:23:22] SPEAKER_00: many data sets across many different robots and many different situations.
[00:23:27] They develop better understanding of the world and they can actually work in environments
[00:23:30] SPEAKER_00: that they've never seen before.
[00:23:33] So at this point I would say that we know that these models are capable of incredible
[00:23:37] SPEAKER_00: things that we've never seen robots do before.
[00:23:40] SPEAKER_00: We know that they can generalize to environments they've never been before like homes, the
[00:23:44] SPEAKER_00: most diverse environment there is.
[00:23:46] The last question is can they perform really, really well?
[00:23:50] All the demos I've showed you, they work some of the time, sometimes 80%, sometimes 90%
[00:23:54] SPEAKER_00: sometimes less.
[00:23:55] SPEAKER_00: But they don't work every time.
[00:23:57] SPEAKER_00: And if you really want to deploy this technology and bring it to the world, they need to be
[00:24:01] SPEAKER_00: working 100% of the time, the extremely reliable.
[00:24:05] I'm not going to tell you about this yet, but please stay tuned.
[00:24:08] SPEAKER_00: There's more to come in that access as well.
[00:24:13] All right, so to summarize where are we at and what's still missing, I would say the following.
[00:24:19] SPEAKER_00: We have a prototype of a generalist model that can be trained on many different robots,
[00:24:23] SPEAKER_00: many different tasks, a true generalist.
[00:24:26] And I think it shows kind of sparks of physical intelligence.
[00:24:29] SPEAKER_00: It's not the physical intelligence that I imagined yet, but I think it's starting to, starting
[00:24:35] SPEAKER_00: to get there.
[00:24:36] SPEAKER_00: It starts to work on new robots.
[00:24:37] SPEAKER_00: It's starting to work in new environments.
[00:24:39] SPEAKER_00: It's starting to do tasks that we've never seen robots do before.
[00:24:42] SPEAKER_00: It shows some really interesting behaviors.
[00:24:46] And then even more importantly, we're starting to develop this recipe for training these
[00:24:50] SPEAKER_00: robot foundation models.
[00:24:52] SPEAKER_00: A recipe that you can apply, a recipe that we understand a little bit better, that is
[00:24:57] more repeatable and that many others can be can apply as well.
[00:25:02] SPEAKER_00: Having said that, we are still very, very early.
[00:25:04] SPEAKER_00: There was lots of things that are missing.
[00:25:08] SPEAKER_00: First, we are not yet there when it comes to generalization.
[00:25:11] SPEAKER_00: I showed some signs of really impressive generalization, but if you compare it to something like
[00:25:15] SPEAKER_00: large language models, we are not there yet.
[00:25:19] Secondly, we need to get these models to be much more robust and much more performant.
[00:25:24] SPEAKER_00: As I mentioned towards the end, this is something that we're working on, but we are not there
[00:25:28] SPEAKER_00: yet.
[00:25:29] SPEAKER_00: It's unclear how long it's going to take to get us full either.
[00:25:34] And then lastly, we also need to understand them better.
[00:25:37] SPEAKER_00: We need to understand the recipes.
[00:25:38] SPEAKER_00: We need to understand the scaling loss.
[00:25:40] SPEAKER_00: We need to turn it into a science, similarly to what happened with language and vision.
[00:25:44] We need to have scientists kind of, start to poke at these artifacts and understand
[00:25:50] SPEAKER_00: how to build them better.
[00:25:53] Now at the very end, I wanted to leave you with how I think about this, how it's going
[00:25:59] SPEAKER_00: to transform the world.
[00:26:02] If you think about electricity that we developed a long time ago, initially when humanity
[00:26:11] SPEAKER_00: was working on electricity, it seemed like it would always require so much effort to get
[00:26:15] SPEAKER_00: it.
[00:26:16] It seemed just insurmountable to get it to a place where it's available to everybody.
[00:26:22] But now when you think of electricity, it's available at the flip of a switch.
[00:26:28] And I think something similar is going to happen with labor.
[00:26:33] Right now labor is kind of the clock speed of the world.
[00:26:37] SPEAKER_00: It's something that takes a lot of effort and it's very, very difficult to get.
[00:26:44] But I think if we're successful, if we solve physical intelligence, labor will be available
[00:26:49] SPEAKER_00: at the flip of a switch.
[00:26:51] Thank you.