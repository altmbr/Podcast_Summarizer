# Stanford AI Club: Jeff Dean on Important AI Trends

**Podcast:** Stanford AI Speaker Series
**Date:** 2025-11-23
**Video ID:** AnTw_t21ayE
**Video URL:** https://www.youtube.com/watch?v=AnTw_t21ayE

---

[00:00:00] For a quick intro on Jeff.
[00:00:03] Jeff throwing Google in 1999 as his 30th employee.
[00:00:08] SPEAKER_00: So we built some of the most foundational infrastructure that I was modern Internet, including
[00:00:12] SPEAKER_00: MapReduce, Bigtable, and Spanner.
[00:00:15] SPEAKER_00: Jeff went on to patent Google Brain in 2011.
[00:00:18] SPEAKER_00: We developed the release TensorFlow, one of the world's most popular deep learning frameworks.
[00:00:23] SPEAKER_00: Jeff now serves as the chief scientist of Google D.Mine in Google Research, where he leads the
[00:00:28] SPEAKER_00: team.
[00:00:29] SPEAKER_00: Jeff is an honor to have you here today.
[00:00:30] SPEAKER_00: I'm going to take you away.
[00:00:31] Thank you.
[00:00:32] I'm going to do the light.
[00:00:35] Fantastic.
[00:00:36] Okay.
[00:00:37] So what I thought I would do today is talk to you about important friends in AI, sort of a
[00:00:47] Jeff Dean: whole bunch of developments that had happened mostly over the past 15 years or so, and you
[00:00:53] Jeff Dean: know how those kind of have fit together well into building sort of the modern capable models
[00:00:59] Jeff Dean: that we have today.
[00:01:01] Jeff Dean: This is presenting the work of many, many people at Google, and some of it is also from elsewhere.
[00:01:07] Jeff Dean: But, you know, I'm sometimes just the messenger, sometimes a collaborator and developer of
[00:01:14] Jeff Dean: some of these things.
[00:01:16] Jeff Dean: So first, a few observations.
[00:01:19] Jeff Dean: I think in the last decade or so, machine learning has really completely changed our expectations
[00:01:24] Jeff Dean: of what we think is possible with computers.
[00:01:27] Jeff Dean: Like 10 years ago, you could not get very natural speech recognition and conversations with your
[00:01:33] Jeff Dean: computer.
[00:01:34] Jeff Dean: You, they weren't really very good at image recognition or understanding what's in visual form.
[00:01:40] Jeff Dean: They didn't really understand my English all that well.
[00:01:43] Jeff Dean: But what has happened is we've discovered that a particular paradigm of deep learning based
[00:01:50] Jeff Dean: methods neural networks and increasing scale has really delivered really good results as we
[00:01:56] Jeff Dean: scaled things up.
[00:01:57] Jeff Dean: And along the way, we've developed really new and interesting algorithmic and model architecture
[00:02:02] Jeff Dean: improvements that have also provided these massive improvements.
[00:02:05] Jeff Dean: And these are often kind of combined well.
[00:02:09] Jeff Dean: So, even bigger things with even better algorithms tend to work even better.
[00:02:15] Jeff Dean: The other thing that's been a bit of a significant effect in the whole computing industry is the
[00:02:20] Jeff Dean: kinds of computations we want to run and the hardware in which we want to run them have dramatically
[00:02:24] Jeff Dean: changed.
[00:02:26] Jeff Dean: Right?
[00:02:27] Jeff Dean: Like 15 years ago, mostly you cared about how fast was your CPU, maybe how many cores did it have?
[00:02:32] Jeff Dean: Could it run Microsoft Word and Chrome or, you know, traditional, you know,
[00:02:38] hand-coded program computations quickly?
[00:02:44] Jeff Dean: Now you care, can it run interesting machine learning computations with all kinds of different kinds of constraints?
[00:02:53] Jeff Dean: Okay.
[00:02:54] Jeff Dean: So, rapid fire advance or whirlwind tour of 15 years of machine learning advances?
[00:03:01] Jeff Dean: How did today's models come to be?
[00:03:03] Jeff Dean: It's going to be like one or two slides per advance.
[00:03:05] Jeff Dean: There's often an archive link or a paper link that you can go learn more.
[00:03:10] Jeff Dean: But I'm going to try to give you just the highest level essence of like why was this idea important?
[00:03:15] Jeff Dean: And what does it help us with?
[00:03:18] Okay.
[00:03:19] Jeff Dean: But I'm going to even go back more than that.
[00:03:21] Jeff Dean: I'll go back like 50 years.
[00:03:23] Jeff Dean: Neural arts turned out these are a relatively old idea.
[00:03:28] Jeff Dean: And this notion of artificial neurons that we have weights on the edges and we can sort of learn to recognize certain kinds of patterns
[00:03:39] Jeff Dean: actually turns out to be really important.
[00:03:41] Jeff Dean: And combined with that, back propagation as a way to learn the weights on the edges turns out to be a really key thing.
[00:03:49] Jeff Dean: Because then you can do end-to-end learning on the entire network from some error signal you have.
[00:03:55] Jeff Dean: And so this was kind of the state of affairs when I first learned about neural networks in 1990, my senior year of college.
[00:04:02] Jeff Dean: And I got like really excited.
[00:04:03] Jeff Dean: I'm like, oh, this is such a great abstraction.
[00:04:05] Jeff Dean: It's going to be awesome.
[00:04:06] Jeff Dean: We could build really great pattern recognition things and solve all kinds of problems.
[00:04:11] So I got really, really excited.
[00:04:13] Jeff Dean: And I said, oh, I'm going to do a senior thesis on parallel training of neural arts.
[00:04:18] Jeff Dean: And so what I ended up doing was like, well, let's just try to use the 32 processor machine in the department instead of a single machine.
[00:04:28] Jeff Dean: And we'll be able to build really impressive neural networks.
[00:04:31] Jeff Dean: So it's going to be really great.
[00:04:32] Jeff Dean: And I essentially implemented two different things that we now call data parallel and model parallel training of neural nets on this funky hypercube-based machine.
[00:04:44] Jeff Dean: And then looked at how that scale as you add in more processors.
[00:04:50] Jeff Dean: So it turns out I was completely wrong.
[00:04:52] Jeff Dean: You needed like a million times as much processing power to make really good neural nets, not 32 times.
[00:04:58] Jeff Dean: But it was a fun exercise.
[00:04:59] Jeff Dean: I really enjoyed writing those thesis.
[00:05:01] Jeff Dean: And then I went off and decided to do other things in grad school.
[00:05:05] Jeff Dean: But this always kind of had a little clinging in the back of my mind.
[00:05:08] Jeff Dean: This could be an important instruction.
[00:05:12] Jeff Dean: So in 2012, I bumped in actually to Andrew In in a microkitchen at Google.
[00:05:20] Jeff Dean: And I'm like, oh, hi, Andrew, how are you?
[00:05:22] Jeff Dean: He's like, what are you doing here?
[00:05:23] Jeff Dean: And he's like, oh, well, I'm starting to spend a day week at Google.
[00:05:26] Jeff Dean: And I haven't really figured out what I'm doing yet here.
[00:05:30] Jeff Dean: But my students at Stanford are starting to get good results with neural nets on various kinds of speech problems.
[00:05:37] Jeff Dean: I'm like, oh, that's cool.
[00:05:39] Jeff Dean: We should train really big neural networks.
[00:05:41] Jeff Dean: So that was kind of the genesis of the Google Brain project was how do we scale large training of neural networks using lots and lots of computation.
[00:05:54] And at that time, we didn't actually have accelerators in our data centers.
[00:05:59] Jeff Dean: We had lots and lots of CPUs with lots of cores.
[00:06:02] Jeff Dean: So we ended up building this software abstraction that we called disbelief in part because people didn't believe it was going to work.
[00:06:10] Jeff Dean: But this ended up supporting both model parallelism and also data parallelism.
[00:06:19] Jeff Dean: And in fact, we did this kind of funky asynchronous training of multiple replicas of the model on the right hand side where before every step with the batch of data, one of the replicas would down on the current set of parameters.
[00:06:32] Jeff Dean: And it would kind of crunch away on doing one batch of training on that and computer gradient update.
[00:06:39] Jeff Dean: That's the Delta W there and send it to the parameter servers who would then add in the Delta W to the current parameters that it was posting.
[00:06:48] Jeff Dean: Now, this is all completely mathematically wrong because at the same time, all the other mathematical model replicas were also computing gradients and asynchronously adding them into this shared set of parameter state.
[00:07:01] Jeff Dean: So that made a lot of people kind of nervous because it's not actually what you're really supposed to do, but it turned out to work.
[00:07:08] Jeff Dean: So that was nice.
[00:07:09] Jeff Dean: And we had systems where we'd have 200 replicas of the model all turning away synchronously and updating parameters.
[00:07:16] Jeff Dean: And a team to work reasonably well.
[00:07:18] Jeff Dean: And we could also have model parallelism where we could divide very large models across many, many computers and end up with.
[00:07:27] You know, so this system enabled us up in 2012 to train 50 to 100 X larger neural network than anyone had ever trained before.
[00:07:37] Jeff Dean: They look really small now, but at that time, we were like, oh, this is crazy.
[00:07:45] Jeff Dean: And so one of the first things we used this system for was what's known as the cat paper, which where we took 10 million random frames from random YouTube videos and just used an unsupervised objective function to be able to learn a representation that we could then use to reconstruct the raw pixels of of each frame.
[00:08:08] Jeff Dean: And learning objective was sort of trying to minimize the error and the reconstruction of the frame given the input frame to don't need any labels.
[00:08:17] Jeff Dean: And in fact, the system never saw any label data for the unsupervised portion.
[00:08:21] But what we found was that at the top of this, this model.
[00:08:27] Jeff Dean: You'd end up with neurons that were sensitive to whether the image contained different kinds of sort of high level concepts, even though it had never been taught, you know, what a cat was.
[00:08:36] Jeff Dean: There was a neuron where the most the strongest stimulus you could give that neuron was something like that.
[00:08:44] Jeff Dean: And so it had sort of come up with the concept of a cat just by being exposed to that.
[00:08:49] Jeff Dean: And also there were also other neurons of like human faces or the backspot S frames or things like that.
[00:08:56] And perhaps more importantly, we got very large increases in state of the art on the more thinly traded image net 22,000 category benchmark.
[00:09:10] Jeff Dean: Most people competed and the one you usually hear about is the 1000 category one.
[00:09:14] Jeff Dean: They're like, well, let's do the 22,000 one.
[00:09:18] Jeff Dean: And so we got actually like a 70% relative improvement in the state of the art on that.
[00:09:23] Jeff Dean: And what we are also able to show is that we did unsupervised pre training.
[00:09:28] Jeff Dean: We actually got a pretty significant increase in the accuracy.
[00:09:36] We also started to think about language and looking at how we could have nice distributed representations of words, rather than representing words is discrete things.
[00:09:47] Jeff Dean: We wanted to have a neural net like representation for every word and then be able to learn those representations so that you end up with these high dimensional vectors that represent each word or phrase in the system.
[00:10:03] Jeff Dean: And when you do that, we had a few different objectives for how do you train this one way you can do it is use the middle representation of use the word in a sequence of words and use its representation to try to predict the other nearby words.
[00:10:17] Jeff Dean: And then you can get an error signal and backproport backproportate into the representations for all the words.
[00:10:25] Jeff Dean: And if you do this and you have a lot of training, which is just raw text that you need to train this on, then what you find is that the nearby words in the high dimensional space that you train it are all quite related.
[00:10:36] Jeff Dean: So CAD and Puma and Tiger are all nearby, but also interestingly we found directions were kind of meaningful.
[00:10:42] Jeff Dean: So if you subtract these vectors, you end up going in the same direction to change the gender of a word, for example, regardless of whether you start at king or you start at man, you end up being able to do that.
[00:10:53] Jeff Dean: And there's other directions for like past tensors of verbs and you know future tensors of verbs. So that was kind of interesting.
[00:11:01] Then my colleagues, Ilya, Oriola and Quack worked on using LSTM. So these kind of recurrent long shorter memory models to work on a particularly nice problem that's traction where you have one sequence.
[00:11:21] Jeff Dean: And you're going to use that to predict a different sequence. And turns out this has all kinds of uses in the world.
[00:11:27] Jeff Dean: So one use that they focused on on the paper was translation. So you have an English sentence, say, and you're going to try to predict the French sentence.
[00:11:37] Jeff Dean: And you have a bunch of training data where you know the correct French translation of an English sentence.
[00:11:43] Jeff Dean: And so you end up using that as a supervised learning objective to then learn good representations in the recurrent model in order to do this translation task.
[00:11:56] Jeff Dean: And if you see enough English French sentence pairs and use the sequence based sequence the sequence based learning objective, then you end up with a quite high quality translation system.
[00:12:07] Jeff Dean: Turns out you can use this for all kinds of other things as well. I will not put about that.
[00:12:15] So one of the other things we started to realize as we were getting more and more success in using neural nets for all kinds of interesting things and speech recognition and vision and language was that.
[00:12:28] Well, actually I did a bit of a back to the envelope calculation with a we had just produced a really high quality speech recognition model that we hadn't rolled out, but we could see that it was, you know, much lower error rate than the current production speech recognition system at Google, which at that time ran in our data centers.
[00:12:48] Jeff Dean: And so I said, oh, well, if speech recognition gets a lot better people are going to want to use it more. And so what if 100 million people want to start to talk to their phones for three minutes a day, just as a random numbers pulled out of my head.
[00:13:04] Jeff Dean: And it turned out if we wanted to run this high quality model on CPUs, which is what we had in the data centers at that time, we would need to double the number of computers Google had in order just to roll out this improved speech recognition feature.
[00:13:19] Jeff Dean: So I said, well, we really should think about specialized hardware because there's all kinds of nice properties for neural net computations that are that we could take advantage of by building specialized hardware.
[00:13:29] Jeff Dean: In particular, they're very tolerant of very low precision computations. So you don't need like 32 bit floating point numbers or anything like that. And all the neural nets that we've been looking at at this time were just different compositions of essentially dense linear algebra operations.
[00:13:49] Jeff Dean: So if you can build specialized hardware that is really, really good at reduced precision linear algebra, then all of a sudden you can have something as much more efficient.
[00:14:01] Jeff Dean: And we started to work with a team of people who chip designers and board designers. And this is kind of the paper we ended up publishing a few years later.
[00:14:14] Jeff Dean: But in 2015, we ended up having these TPUV1, so the 10th or processing unit, which was really designed to accelerate inference.
[00:14:25] Jeff Dean: A roll out into our data center and we were able to do a bunch of nice sort of empirical comparisons and show that it was 15 to 30 times faster than CPUs and GPUs at the time and 30 to 80 times more energy efficient.
[00:14:39] Jeff Dean: So, and this is now the most cited paper in ISK 50 year history. And then working with that same set of people, we realized that we also wanted to look at the training problem because inference is like a nice, you know, small scale problem where you can have a, at that time, a single PCIe card, you could plug into a computer and have a whole bunch of, you know, models that run on that.
[00:15:08] Jeff Dean: But for training, it's a much larger scale problem. And so we started to design, but essentially machine learning supercomputers around the idea of having low precision, a high speed custom network.
[00:15:21] Jeff Dean: And sort of a compiler that could map high level computations onto the, onto the actual hardware. And it ended up with a whole sequence of TPU designs that are sort of progressively faster and faster and larger and larger.
[00:15:37] Jeff Dean: And our most recent one is we've changed our naming scheme. It's no longer what you might expect. It's called Ironwood.
[00:15:46] Jeff Dean: But the pod sizes for this system are, you know, 9,000, 2, and 16 chips all connected in a 3D forest. And quite a lot of bandwidth and capacity. And if you compare that to TPU V2, which is our first ML supercomputing system,
[00:16:06] Jeff Dean: it's about 3,600 times the peak performance per pod, compared to the first one, which be fair was only 256 chips instead of 9,000. But still, every individual chip is also much faster.
[00:16:20] Jeff Dean: And it's also about 30 times as energy efficient as the EPV2. Now some of that comes from scaling of process nodes and so on. But some of it just comes from, you know, looking at energy consumption in all kinds of ways.
[00:16:34] Jeff Dean: And building really energy efficient systems.
[00:16:39] Another thing that's happened is open source tools have really enabled the whole community. So we developed TensorFlow as a successor to our internal disbelief system, which we'd used for hundreds or thousands of kinds of models.
[00:16:53] Jeff Dean: And fixed a bunch of things in it that we didn't like and decided to open source it when we first started building it.
[00:17:00] Jeff Dean: A bunch of people were working a little bit later on a system called Torch that used a language called Lua and didn't get very popular because most people don't want to program them or did not know Lua.
[00:17:14] Jeff Dean: But then they built a version called PyTorch that was Python based that really had a lot of success. And another team at Google has been building a system called Jax that has this nice functional way of expressing machine learning computations.
[00:17:29] Jeff Dean: And those have really enabled the whole community in lots of ways, like many different kinds of applied ML things are doing using some of those frameworks, researchers are using those.
[00:17:41] Jeff Dean: In 2017, several of my colleagues worked on this attention based mechanism building on some earlier work on attention, but coming up with this really nice architecture that is now at the core of most of them sort of exciting language based models that you're seeing today.
[00:18:00] Jeff Dean: And their observation was really unlike an LSTM where you sort of have a word and you consume that word by updating your internal state and then you go on to the next word.
[00:18:11] Jeff Dean: Their observation was, hey, let's not try to force all that state into a vector that we update every step. Instead, let's just be able to save all those states we go through and then let's be able to attend to all of them whenever we're trying to do something based on the context of the path.
[00:18:30] Jeff Dean: And that's really kind of at the core of the attention is all you need in the title. And what they were able to show was that you could get much higher accuracy from the paper with 10 to 100 x less compute.
[00:18:45] Jeff Dean: And in this case, 10 times smaller models. So this is the number of parameters on a log scale for a language model to get down to a particular level of loss.
[00:18:56] Jeff Dean: And what they were able to show is that 10 times fewer parameters in a transformer based model would get you there and also in other data in the paper, they showed 10 to 100 x less compute.
[00:19:11] Another super important development has been just language modeling at scale with unsupervised data. There's lots and lots of text in the world. Self supervised learning on this text can give you almost infinite numbers of training examples where the right answer is known because you have some word that you've removed from the view of the model.
[00:19:33] Jeff Dean: And then you're trying to predict that word. And there are a couple of different flavors. One is all over aggressive where you get to look to the left and try to predict what's the next word given all the words that you've seen before that.
[00:19:45] Jeff Dean: So Stanford blank and the true word is universities. So you make a guess for this word. If you get it right, great. If you get it wrong.
[00:19:55] Then you can use that as an error signal to then do back propagation through your entire model. And looking at that first blank, it's not necessarily obvious it's going to be university.
[00:20:06] Jeff Dean: It could be Stanford is a beautiful campus or something. And so all the effort you put into doing this kind of thing makes it so the model is able to take advantage of all this context and make better and better predictions.
[00:20:24] Jeff Dean: There's another objective you can use where you get to look at a whole bunch more context both to the left and right. And you just try to guess the missing words.
[00:20:34] Jeff Dean: So if you've ever played mad lives, it's a bit like that. You know, the Stanford blank club blank together, blank and computer blank at the least.
[00:20:45] Jeff Dean: So you can some of those you can probably guess some of those are harder to guess. But that's really kind of the key for doing self supervised learning on text, which is at the heart of modern language models.
[00:20:57] Turns out you can also apply these transformer based models to computer vision. And so another set of my colleagues worked on, you know, how can we do that and what they found again was, you know, old face things are the best result for a particular road.
[00:21:14] Jeff Dean: And what they found was these two were theirs in varying sizes of configuration. But roughly, you know, four to 10, four to 20 times less compute, you could get to the best results.
[00:21:29] Jeff Dean: So again, algorithm improvements make a big difference here because now all of a sudden you can train something much bigger or use less compute to get the same accuracy.
[00:21:42] Jeff Dean: So I and a few other people really started to encourage some of our colleagues and gather a small group of people to work on much sparser models.
[00:21:53] Jeff Dean: Because we felt like in a normal neural network, you have the idea model activated for every example or every token you're trying to predict.
[00:22:02] Jeff Dean: And that just seems very wasteful. It'd be much better to have a very, very large model and then have different parts of it be good at different kinds of things.
[00:22:12] Jeff Dean: And then when you call upon the expertise that's needed in the model, you only activate a very small portion of the overall model.
[00:22:19] Jeff Dean: So maybe one to one to five percent of the total parameters in the model are used on any given prediction.
[00:22:28] And again, we were able to see that this was a major improvement in time to compute the act to a given level of accuracy.
[00:22:36] Jeff Dean: That's like this line here, L and M showing about an 8x improvement in training reduction in training cost compute for the same accuracy.
[00:22:47] Jeff Dean: Or you could choose to spend that by just training a much better model with the same compute method.
[00:22:56] And then we've continued to do a whole bunch of research on our models because we think this is quite an important thing.
[00:23:03] Jeff Dean: And indeed, most of the models you hear about today, like Gemini models for example, are sparse models.
[00:23:17] Jeff Dean: In order to support sort of more interesting kind of weird sparse models, we started to build compute abstractions that would let us map interesting ML models onto the hardware where you didn't have to think as much about where particular pieces of the computation were located.
[00:23:37] Jeff Dean: So pathways was the system we built that was really designed to be quite scalable to simplify running with these really large scale training computations in particular.
[00:23:49] Jeff Dean: And oh, well, so one thing, like if each of these is one of these TPU pods, there's a super high speed network between the chips and the pod.
[00:23:59] Jeff Dean: And sometimes you want a job that will span multiple pods. And so then the orange lines are sort of the local data center network in the same building that you can use to communicate between adjacent pods.
[00:24:11] Jeff Dean: And then maybe you have multiple buildings on the same campus where you have some network between the two buildings, the purple line.
[00:24:21] Jeff Dean: And you can even run computations where you're using multiple metro areas and a long distance high speed length to communicate between multiple metro areas.
[00:24:36] Jeff Dean: And one of the things Pathways does is it orchestrates all this computation. So you don't use a ML researcher. Don't have to think about, okay, which network links that I use. It sort of chooses the best thing at the best time and it uses deals with failures of what happens if one of these chips goes down or one of these pods goes down, things like that.
[00:24:55] Jeff Dean: And one of the things that it provides as an attraction is we have a layer underneath jacks that is Pathways runtime system. And so we can then make a single Python process look like it jacks programming environment that instead of having four devices has 10,000 devices.
[00:25:14] Jeff Dean: And you can use all the normal jacks machinery to express, okay, I'd like to run this computation on all these devices.
[00:25:24] Jeff Dean: So another of my colleagues, a set of my colleagues worked on how can we sort of use better prompting of the model to elicit better answers.
[00:25:34] Jeff Dean: And one of their observations was if you, in this case, were giving the model one example of a problem and then we're asking it to solve a different problem but similar to the example we did it.
[00:25:47] Jeff Dean: And if you just tell the model, here's the example problem and it just is told to give the answer, like, you know, the answer is nine, then it doesn't do as well as if you give the model sort of some guidance that it's supposed to show its work and demonstrate that in the first problem.
[00:26:07] Jeff Dean: And then it will actually go ahead and admit it's, you know, show its work for the actual problem, we're trying to get it to solve.
[00:26:17] Jeff Dean: And, you know, one way of thinking about this is because the model gets to do more computation for every token it emits in some sense it's able to use more compute in order to arrive at the answer.
[00:26:29] Jeff Dean: But it also is helpful for it to be able to reason through problems kind of step by step rather than trying to just internally come up with the right answer.
[00:26:39] Jeff Dean: And, you know, this paper showed that you got pretty significant increases in accuracy on GSMHK, which is like a middle school math, benchmark kind of like these problems, if you use this chain of thought prompting versus standard prompting.
[00:26:57] Jeff Dean: Now, remember, this was three years ago, right? And we're really excited that we've now gotten 15% correct on eighth grade math problems of the form, you know, Sean has five toys and for GSMHK got two more.
[00:27:15] Jeff Dean: So we've made a lot of progress on math in the last few years.
[00:27:21] Jeff Dean: Another important technique turns out to be a technique I worked on with Jeff Hinton and Oriol Vinyol's called distillation.
[00:27:29] Jeff Dean: And the idea here is when we're doing this sort of next word prediction, you know, if you're doing self supervised learning, you perform the concerto for blank and the correct answer in the texture you're training on is violent.
[00:27:45] Jeff Dean: But it turns out if you have a really good neural network already, you can use that as a teacher.
[00:27:53] Jeff Dean: And the teacher will give you a distribution of likely words for that missing word.
[00:28:01] And so it turns out that you can use this distribution to give the student model much more information when it gets something wrong.
[00:28:11] Right? Because it's, you know, very likely the word is violent or piano or trumpet, but it's extremely unlikely it's airplane.
[00:28:19] Jeff Dean: And that rich signal actually makes it much easier for the model to learn quickly.
[00:28:25] Jeff Dean: And in particular, what we showed in this paper was that this was a speech data set. So we're trying to predict the sound in a frame of audio correctly.
[00:28:37] Jeff Dean: And the baseline, if you use 100% of the training set, you could get 58.9% on the test frames.
[00:28:46] Jeff Dean: But if you only use 3% of the training data, then you get only 44% test frame accuracy.
[00:28:55] Jeff Dean: So a huge drop in accuracy. But if you use these soft targets in a distillation process, then 3% of the training data, you can get 57% accuracy.
[00:29:05] And so this is why this is such a super important technique because you can train a really, really large model.
[00:29:10] Jeff Dean: And then you can use distillation to take a much smaller model and use the distillation targets to give you a really high quality small model that approximates quite closely the performance of a large model.
[00:29:26] OK, and then in the 2020s, I guess I should say, people have been doing a lot more reinforcement learning for post-trains.
[00:29:35] Jeff Dean: So once you've already trained a model on these self supervised objectives and so on, you then want to sort of encourage the right kind of behavior from your model.
[00:29:45] Jeff Dean: And you want to do that in terms of things like the style of the responses.
[00:29:50] Jeff Dean: Do you want it to be polite? You can give it, unfortunately, in learning feedback or give it examples of being polite and sort of do training on that to sort of coax the polite kind of answers out of the model and suppress the less polite ones.
[00:30:04] Jeff Dean: Safety properties might want the model to just not try to engage with people in certain kinds of topics.
[00:30:11] Jeff Dean: But then you can also enhance the capabilities of the model by showing it how to tackle much more complex problems.
[00:30:18] Jeff Dean: And these can come from many different sources. So one is reinforcement learning from human feedback.
[00:30:23] Jeff Dean: You can use human feedback on the outputs of the model where a human can say, yeah, that's a good answer. No, that's a bad answer. Yes, that was a good answer.
[00:30:33] Jeff Dean: And using lots of those signals, you can get the model to approximate the kinds of behaviors your human reward signals giving you.
[00:30:42] Jeff Dean: RL from machine feedback is you can use machine feedback from another model, often called a reward model, where you prompt the reward model to judge, you know, do you like answer A or B better and use that as an RL signal.
[00:30:59] Jeff Dean: And that then probably one of the most important things is RL and verifiable domains like math or coding.
[00:31:04] Jeff Dean: So here you can try to generate some sort of solution to a mathematical problem and let's say it's a proof.
[00:31:10] Jeff Dean: And then you have a verifiable domain so you can run a more traditional proof checker against the proof that the model has generated.
[00:31:19] Jeff Dean: And then the proof checker can say, yes, that's a correct proof or no, that's an incorrect proof and in particular it's wrong and step 73 or something.
[00:31:29] Jeff Dean: And that can give positive reward to the model when it reasons correctly. You can also do this for coding where you give reward for code that compiles.
[00:31:38] Jeff Dean: And then even more reward for code that compiles and passes the unit tests that you have for some coding problem and you just have a whole slew of problems you asked the model to try to solve and get rewards for when it solves it.
[00:31:51] Jeff Dean: And so this enables the model to really explore the space of potential solutions and over time it gets better and better exploring that space.
[00:32:01] Jeff Dean: So there's been all kinds of innovations at many different levels.
[00:32:06] Jeff Dean: You know, many of which I just talked about, but I think it's important to realize everything from the hardware to the software abstractions and model architecture training algorithms.
[00:32:16] Jeff Dean: All these things have all come together and really contributed and I'm way behind time. So I'm going to speed up.
[00:32:22] Okay, so we've been working on Gemini models at Google which kind of combine a lot of these ideas into pretty interesting.
[00:32:30] Jeff Dean: We think models and our goal with the Gemini effort is really train the world's best multi-models use them all across Google and make them available to external people as well.
[00:32:42] Jeff Dean: And just this week we released our 3.0 pro model.
[00:32:49] Jeff Dean: We wanted it to be multi-model from the start to take all kinds of different modalities as input and also produce lots of modalities as output.
[00:32:57] Jeff Dean: We've been adding more modalities. This is from the original neck report. We've since added the ability to produce video and other kinds of things audio.
[00:33:07] We believe in having a really large context link so that model can look at lots of kinds of in pieces of input and reason about it or summarize it or refer back to it.
[00:33:18] Jeff Dean: That's been pretty important.
[00:33:22] Jeff Dean: 2.0 built on a lot of these kinds of ideas and was a quite capable model 2.5.
[00:33:29] Jeff Dean: It was also quite a good model. And then just to show you how far the mathematical reasoning has come, we used a very end of the 2.5 pro model to compete in the International Mathematical Olympiad this year and also last year.
[00:33:47] Jeff Dean: This year it was like a pure language model based system and we solve 5 of the 6IMO problems correct which gets you a gold medal.
[00:33:58] Jeff Dean: And there's a nice quote from the IMO president.
[00:34:05] Jeff Dean: The way the IMO works is there's two days of competition. Each day you get three problems. The third of the problems on each day.
[00:34:12] Jeff Dean: Problems 3 and problem 6 are the hardest. And this was problem 3 which we did get correct. We didn't get problem 6 correct. But we got all the other ones correct.
[00:34:23] Jeff Dean: So this is the problem statement. This is the input to our model. And this is the kind of output the model is able to produce.
[00:34:37] Jeff Dean: Which kind of goes on. I think the judges like the elegance of our solution which is nice. It goes on for a little while. And therefore we approve QED.
[00:34:51] Jeff Dean: I think it's pretty good to sit back and appreciate how far the mathematical reasoning capabilities these models have come since 2022 when we were trying to solve.
[00:35:00] Jeff Dean: John has four reddits and got two more how many reddits do we have now.
[00:35:08] Jeff Dean: And then earlier this week we released our Gemini 3 models. I'm really excited about it. You can see.
[00:35:14] Jeff Dean: And it performs quite well on a bunch of different benchmarks. There's like way too many benchmarks in the world. But it's a good way to benchmark to assess how good is your model relative to other ones.
[00:35:27] Jeff Dean: Especially for ones that are maybe more interesting or haven't been leaked under the internet quite as much.
[00:35:35] Jeff Dean: We're number one in the LM arena which is a good way of assessing sort of a non benchmark based way where you allow a user to see to random anonymous language model responses to a prompt they give.
[00:35:51] Jeff Dean: And then the user can say I prefer a or b and over time you get an aggregated score from that because you can see if your model generally more preferred to other models.
[00:36:02] Jeff Dean: One of the things that's really happened is we had a huge leap in web dev style coding versus our earlier model.
[00:36:11] Jeff Dean: I'm going to skip this. I'm going to skip. Well, I'll show you that.
[00:36:17] So this is an example of the word Gemini skateboarding or the word Gemini serving.
[00:36:26] Jeff Dean: So it's actually generating code for animating all these kinds of things.
[00:36:31] Jeff Dean: Voting drew view of a landscape here it is as a forest. I like that one.
[00:36:38] Jeff Dean: So the sort of you can give very high level instructions to these models and have them right code and it doesn't always work but when it works it's kind of this nice magical feeling.
[00:36:50] Jeff Dean: Here's another example. This is you know someone had a whole bunch of recipes in various form some in Korean some in English.
[00:36:59] Jeff Dean: And they basically just said okay, I'm going to scan them all in. I'm going to take photos of them.
[00:37:10] Jeff Dean: Great. There we go. They're all in there. Translate and subscribe them. Awesome.
[00:37:18] Jeff Dean: And they're all transcribed. And then our next step is going to be let's see if we can read a bilingual website using these recipes.
[00:37:33] Jeff Dean: So go we've now done this and we've generated some nice imagery for it and there's go.
[00:37:42] Jeff Dean: And now there's your website with your recipes. So it's kind of nice. It combines a whole bunch of capabilities of these models to end up with something that might be kind of useful.
[00:37:52] Jeff Dean: Users generally seem to be enjoying this.
[00:37:57] Jeff Dean: Yeah, I mean there's lots of quotes on the web. We also launched a much better image generation model today.
[00:38:05] Jeff Dean: So that's been kind of exciting. People seem to really like it. It can do pretty crazy things. So you can give it for example.
[00:38:15] Jeff Dean: Turn this blueprint into a 3D image of what the house would look like.
[00:38:22] Jeff Dean: Or take the original attention is all you need. Figure and please annotate it with all the important aspects of that happened in each different spot.
[00:38:34] Jeff Dean: And one of the people who work most on the nano banana work. So one of the things that's interesting about it is it actually reasons in intermediate imagery.
[00:38:45] Jeff Dean: So.
[00:38:48] And you can see this in the thoughts if you use a studio. So the question is you know tell me which bucket the ball lands and use images to solve it step by step.
[00:38:58] Jeff Dean: So this is what the model does. It sort of does what you might think the first it rolls down there. And oh yeah, then it's going to roll the other way on the grand three.
[00:39:08] Jeff Dean: And it's been a role on the ramp five and then it's going to be in B.
[00:39:13] Jeff Dean: It's kind of cool. I mean that's kind of how you would mentally do it.
[00:39:18] Jeff Dean: You know it's pretty good at infographic things so it can you know annotate old historical figures and tell you things.
[00:39:28] Jeff Dean: I posted this image of the solar system. You know and as an example show me a chart of the solar system.
[00:39:35] Jeff Dean: An energy planet with one interesting fact. So that's the image we did turns out if you do that people are really sad.
[00:39:45] Especially people my age are a little bit younger. So that's okay. So make this 21 9 to add Pluto and add a humanist comment.
[00:39:55] Jeff Dean: You know the former planet got demoted to dwarf planet status. You'll grumpy about it.
[00:40:03] Perfect. You're so back.
[00:40:08] Okay. So in conclusion, you know I think I hope you've seen in your own use of these models and also in what I've presented.
[00:40:17] Jeff Dean: But these models are really becoming quite powerful for all kinds of different things.
[00:40:24] Jeff Dean: Further research and innovation is going to continue this trend. It's going to have a dramatic effect on a bunch of different areas.
[00:40:31] Jeff Dean: You know in particular health care education time difference research media creation which we just saw misinformation.
[00:40:39] Jeff Dean: And it potentially makes really deep expertise available to many more people. Right.
[00:40:44] Jeff Dean: Like if you think about the coding examples, there are many people who haven't been trained in how to write code and they can get some.
[00:40:51] Jeff Dean: You know a computer assisted and their their vision can help them generate interesting you know websites for recipes or whatever.
[00:41:01] Jeff Dean: But done well I think our AI assisted future is bright but I'm not completely oblivious like the areas like misinformation is a potential area of concern.
[00:41:11] Jeff Dean: Actually John Hennessy and Dave Patterson and I and a few other who authors worked on a paper last year that kind of touched on all those different areas and look and interview domain experts in all those areas.
[00:41:23] Jeff Dean: And you know looked at ask them what their opinions were and how can we make sure that we get all the amazing benefits in the world for health care and education and scientific research.
[00:41:33] Jeff Dean: But also what can we do to minimize the data full downsides from misinformation and other kinds of things.
[00:41:39] Jeff Dean: So that's what I got.