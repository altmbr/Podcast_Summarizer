[00:00:01] Dmitri Dolgov: Dmitri Dolgov is co-CEO of Waymo. He joined Google's self-driving car project in 2009 as one of its first engineers and was repeatedly promoted until he took it over in 2021. Waymo is Google's most successful moonshot and now provides over 500,000 fully autonomous rides each week. Cheers, by the way. Yeah, cheers.

[00:00:21] Host (Cheeky Pint): You grew up in Russia, right? I grew up in Russia. Then I was actually a Soviet Union. Right, exactly.

[00:00:27] Host (Cheeky Pint): My dad is a physicist. So the Soviet Union started falling apart and then he had a visiting position in Kyoto University for a year. We moved there as a family and then he went to Berkeley and I kind of tagged along. And then I graduated from high school. I was thinking about the next thing I wanted to do. And I really liked that technical school in Russia. The Russians are serious about the physics.

[00:00:55] Host (Cheeky Pint): They are, they are. So I went back to Russia and I got my bachelor's and master's there.

[00:01:00] Dmitri Dolgov: What year was this that you went back to Russia? 1994. Okay. So that was kind of almost peak Russian optimism in a sense where it was opening up.

[00:01:09] Host (Cheeky Pint): It was, it was. Yeah, yeah. No, I actually remember talking to my mom about it and of course my parents grew up in the Soviet Union. They've seen it. Yeah. Yeah. You know, they were worn right before the war and then they saw, you know, they lived through some really tough times. And I remember talking to my mom and saying, she, she, you know, in fact, I got my green card here in the U.S. before I went back and she insisted that I do it. And I was actually at the time, I wasn't thinking of coming back.

[00:01:37] Host (Cheeky Pint): But then I was pretty excited about where Russia is and the trajectory it's on. And, you know, being nine, young and naive, I was like, there's no turning back.

[00:01:47] Dmitri Dolgov: And so why did you decide to come back?

[00:01:49] Host (Cheeky Pint): Um, school, yeah, yeah, no, school, um, it was pretty clear to me. Like I wanted to continue, um, studying, you know, math and computer science. And while the undergrad and master's that I got in physics and applied math, that I think was still an incredibly strong kind of foundational, uh, you know, school of Russian math and science. Uh, graduate school. Yes. It was very clear to me that the best way to do it was in the U.S. So I came back.

[00:02:19] Dmitri Dolgov: I'm struck by the founders of the two most valuable U.K. companies are Russian math nerds who both went to the, uh, the same school. Uh, Nikolai at, uh, Revolution and, uh, Alex Gurko, Alex Gurko at XTX. Um, but yeah, it's a, it's a strong diaspora.

[00:02:39] Host (Cheeky Pint): Uh, there is a company not far from here where one of the founders also has, you know, a similar pedigree.

[00:02:46] Dmitri Dolgov: Mm-hmm.

[00:02:47] Host (Cheeky Pint): Right. A company that we're close to.

[00:02:50] Dmitri Dolgov: Exactly. Exactly. You know, the classic engineering interview question of, um, you know, what happens when I type Google.com and hit enter? Yeah. As you know, uh, talk me through, you know, whatever you like, uh, you know, HTTP and DNS and, you know, BG. You can go down to whatever level of stack you want. Do you want to maybe just describe when I take a ride in a Waymo today, what's happening at a technical level? Like, what is the architecture?

[00:03:14] Host (Cheeky Pint): Let me answer your question. I was happening in real time, but this is going to be only a part of the story because we're going to be talking about kind of the inference, the real-time inference part of it. Uh, and if we want to, you know, have, uh, a deeper, richer technical conversation, I think it would be interesting also to zoom out and talk about, you know, the entire ecosystem of what goes into building, evaluating, and deploying the Waymo driver.

[00:03:39] Host (Cheeky Pint): But when you're driving around or being driven around, you know, we think about what we're building as a driver. Obviously, it's not a car. So it has a number of sensors that are positioned around the vehicle. Uh, we use three different sensing modalities. There's cameras, there's LiDARs or lasers, and there are raders. You know, those are the primary ones. There are, you know, also microphones, directional, you know, microphone arrays, but those are the primary three for sensing the world.

[00:04:09] Host (Cheeky Pint): Um, they all have, uh, very nicely complementary physical properties. They all have 360 degree coverage around the vehicle. So the Waymo driver sees kind of 360, you know, uh, all the time. Uh, so all of the data goes into a computer, you would expect. Uh, and, uh, they're the software that process. Now it's, you know, all AI. I can see a specialized AI in the physical world. Uh, so it processes the sensor data.

[00:04:36] Host (Cheeky Pint): Uh, nowadays, you know, talk about it in the, you know, using AI terminology as, you know, encoders that, you know, take this data in. And then there's the kind of the decoder, the action, you know, the generative part, if you will, in the car. And the generative task there is to, you know, figure out how to drive. Right? And that is, of course, connected, um, through kind of a specialized interface to the car where we can actuate the vehicle. And, you know, that's why you see the steering wheel, you know, turn and it drives you around.

[00:05:04] Dmitri Dolgov: Okay, so I get into my car. There's three main families of sensors, uh, LIDAR, radar, and, um, cameras. And then it is using that to first build a model of what's going on in the world. You know, where are all the other cars and things like that. And then it is, say, make decisions and then actuate that with the car. That is the system that you're living in. And is all that inference done locally or presumably yes? Nothing's in the cloud?

[00:05:29] Host (Cheeky Pint): Uh, nothing real time. Nothing real time in the cloud. And there are some things that can happen, you know, in the cloud, but they're not required. Got it. What's an example of a nice to have that happens in the cloud? Uh, you can imagine a situation where, uh, we do, you know, some of it is not directly related to the task of driving. But, let's say, after you leave the car, we want to check that, uh, you know, the car is not dirty. You didn't leave anything there. If you did leave, you know, an item.

[00:05:56] Host (Cheeky Pint): Uh, well, if you, you know, left in a mess, then, you know, I want to send the car to one of our depots, get it cleaned up. If you left an item there, you know, your phone, all right, we want to, uh, detect that. And then, you know, send it to our lost in phone and let you know. Right? So, uh, that, you know, we do with, uh, kind of, uh, uh, by, um, asking a model that actually lives off board as opposed to having to put it on the car, right? Because it's not a real-time task related to, you know, the driving. So, that's one example of something that...

[00:06:25] Dmitri Dolgov: There are all these debates that go on on Twitter, uh, around self-driving. So, I can think of, you know, end-to-end versus the more kind of modular, uh, approach. There's, uh, cameras only versus array of sensors. And I can't tell, are these debates actually interesting to an expert in the field? Or do you think these are just settled matters and they're just grist for the algorithm?

[00:06:52] Host (Cheeky Pint): I understand where the questions are coming from. I do find that kind of often the way they're posed and the way the debate happens is losing a lot of the nuance and a lot of, uh, detail that really matters. And, uh, to me, the most interesting technical questions are in that level.

[00:07:44] Host (Cheeky Pint): So, that's the foundation. Then we, uh, specialize it into what we call it, three, uh, main off board teachers. There are still large high capacity off board models. Yes. There's the Waymo driver, there is the simulator, and then there's the critic, right? And those then get distilled into smaller models that you can run, you know, inference on faster. So, the Waymo driver becomes, you know, the backbone, the male backbone of what's, uh, in the car.

[00:08:13] Host (Cheeky Pint): Uh, the simulator, of course, is what powers our synthetic generative environment that can run on the cloud for training and for evaluation in close-up of the system. And the critic, does the simulator ever run locally? No. Uh, no, it doesn't. Yeah.

[00:08:28] Host (Cheeky Pint): However, what I think is interesting in a way, the way the decoder works, the way the model works, if you think about the generative task in the simulator of kind of, you know, creating those realistic worlds and how, you know, other people behave, how, you know, cars, pedestrians, cyclists, in order, and the task that you have to solve on the car in real time, there is this task, you know, uh, fundamental.

[00:08:52] Host (Cheeky Pint): And there is this fundamental shared capability of understanding how these objects relate to each other and predicting what they might do in the future if you are running on the car and then generating those, you know, some sampling, those probabilistic behaviors in the simulator. So, it's different models, but there is, you know, this is why the shared foundation model, uh, is, uh, able to power both.

[00:09:16] Host (Cheeky Pint): And similarly, if you think about the critic, like, the job of the critic is to find interesting events and then, you know, be opinionated about what's good behavior and what's bad behavior. Similar fundamental understanding, right? If you're running, you know, inference on the car, you still have to, like, figure out which of the multiple hypotheses of these future worlds you want to, you know, take action to steer towards.

[00:09:38] Dmitri Dolgov: Yes. Okay, and these are all downstream of the same foundation model?

[00:09:43] Host (Cheeky Pint): Let's start with the foundation model. Yep. Uh, you know, uh, then you, you know, specialize in fine-tune, still off-board model. Those are the teachers, and then you distill. Each one of the teachers kind of distill, uh, trains its own student. Yes. And the driver, the simulator, the critic.

[00:09:58] Dmitri Dolgov: Yes. You started working on self-driving 20 years ago. Yeah. As you think about the tech evolution, is this just a scaling law story where we had to be able to throw enough compute at us? Were there architectural approaches we needed to wait to, uh, have be invented? Was it just a story of we needed 20 years of going down the wrong cul-de-sacs before we eventually arrived at the right approach?

[00:10:23] Dmitri Dolgov: You know, could you, knowing what you know now, could you have a successful Waymo in market in 2015? Or was there some enabling technology?

[00:10:33] Host (Cheeky Pint): Uh, no. Technology, uh, breakthroughs that happened over the years were critically important. Primarily in AI. Mm-hmm. Um, but also in other areas. Like, you know, compute. Yeah. You know, the heavy compute, the need to run. Yeah. Now, uh, I wouldn't characterize it as, like, going, you know, a thousand different dead ends. Yes, yes. And then having to retract and then finding, like, the one right path. I would characterize it as, you know, iterative learning and evolution. Yes. And then, you know, transformers came around.

[00:11:02] Host (Cheeky Pint): But, you know, transformers, for example, are very general architecture, right? And powers of a lens, powers, you know, our models. But how you apply them to that space, I think this is where... It doesn't just fall out of transformers. Exactly, right? And then, of course, you know, people like to talk about architectures. Yeah. But architecture, you know, is important. But really, a lot of it comes down primarily to your metrics, to your evaluation mechanisms, to, you know, all of the training recipes. And, of course, new data. Yes.

[00:11:29] Dmitri Dolgov: LLMs are good at text or tokens specifically. And obviously perform best at domains that have some kind of single corpus of text they can work on, like coding, where it's very helpful that everything was just kind of textual already. And part of the success has been creating textual representations for domains such that we can then, you know, put LLMs against them.

[00:11:53] Dmitri Dolgov: Can you describe how you encode the world that you're seeing? I mean, are you just building a 3D map, like a 3D bitmap essentially?

[00:12:06] Host (Cheeky Pint): So this is where I think we can get a bit into this question of what is the interface between the encoder and the decoder parts. And I think that touches also on the, you know, thing you flagged earlier where people like to, you know, debate end-to-end or not end-to-end.

[00:12:28] Host (Cheeky Pint): So the way, you know, talk a little bit about end-to-end and then get back to, like, what is the interface between those two, right? So when you say end-to-end, what do we mean? We mean that it is some large ML model. Typically, you don't build them monolithically. You have, you know, different parts and different subgraphs. But what's important is that you can propagate and backprop the, you know, gradient and the loss function all through the different layers.

[00:12:57] Host (Cheeky Pint): So they can, you know, every layer you can learn, you know, the weights and the representations that matter for the final task. You don't force it through some, you know, narrow funnel between, let's say, the encoder and the decoder.

[00:13:09] Dmitri Dolgov: Yeah, I think of a simple view of end-to-end being, you know, pixels go in and car actions come out, which is maybe a bit of an oversimplification.

[00:13:16] Host (Cheeky Pint): Yeah, that's exactly right. And if, like, this is kind of the basic vanilla version of it, right? If you think about the, you know, what will it take to build the driver that's capable of fully autonomous operations?

[00:13:32] Host (Cheeky Pint): If you think about this entire ecosystem of the driver, the simulator, the critic, if that's all you do, like, pixels in, trajectories out, it becomes very difficult to do all of those three and achieve the high level of safety and performance that we require. And it becomes very difficult to kind of do it at scale. However, if, you know, that's, it's kind of a very easy way to get started, right?

[00:14:01] Host (Cheeky Pint): You collect some data, kind of like, you know, to the LLM world, right? The easiest thing you can do is have, you know, pick a model. The easiest way to get started nowadays would be just, you know, take a VLM. It already has a kind of a language-aligned camera encoder. Yep. And then it has a decoder that, you know, will, can predict, you know, generate text. And you can fine-tune it and say, hey, instead of text, generate trajectories.

[00:14:30] Host (Cheeky Pint): You know, very, very doable. In fact, we, you know, a while ago we published a paper called Emma that did exactly that. Yes. And it will actually, I mean, in the nominal case, drive pretty darn well, which is mind-blowingly impressive. That is very funny, yeah.

[00:14:47] Dmitri Dolgov: And, I mean, there's some intuition. You're saying you can take an off-the-shelf model, which has nothing to do with driving to start with. That's right. And you'll get these good results.

[00:14:54] Host (Cheeky Pint): That's right. You get it. In the nominal case. I just want to be clear. It's orders of magnitude away from what you need. Yeah, you should not try it on the streets, but it works. But, for example, if you...

[00:15:03] Dmitri Dolgov: It's like a talking horse. It's impressive that it's talking, you know? Exactly.

[00:15:05] Host (Cheeky Pint): Exactly. And you can actually, if the product that you wanted to build was maybe a driver-assist system, not a fully autonomous system, then maybe that's all you need to do. Yep. And then, for that, you don't need all this other machinery of the simulator and the critic, because the number of nines is drastically lower. But this is interesting, because there is some intuition behind why that works.

[00:15:29] Host (Cheeky Pint): If you think about the hard parts of driving, it's not unlike having a conversation.

[00:15:37] Unidentified: Mm-hmm.

[00:15:38] Host (Cheeky Pint): Except, you know, if in the LLM world, right, having, you know, you're modeling language or maybe modeling a dialogue in the space of sentences and words. What makes driving hard is also this kind of multi-agent social interactive part of it. And if I do something that's going to affect you, it's going to affect somebody else. And the history matters. It's not local and just geometric. Context matters. Semantics matters.

[00:16:06] Host (Cheeky Pint): So, but it's in a different, you know, it's not in the language of words. It's in the language of kind of body language, if you know what, right? How? So, and we see that empirically validated if you, you know, do this approach. Okay. So then let's say we build this thing. Just cameras, camera encoder, pixels go in, trajectory go out. The quality is sufficient to, you know, drive in the normal case.

[00:16:29] Host (Cheeky Pint): It's not sufficient to deal with the long tail of, you know, the edge cases and hit the high bar of superhuman safety that we require. So then you start asking the question, what else do you need? Yes. And if all you did was kind of observing how other people drive when you trained the system, maybe observing, you know, just passively how people drive and how they interact,

[00:16:55] Host (Cheeky Pint): maybe also, you know, driving the car yourself and then using imitative learning to train it. Mind that that's not enough. You have to do something in closed loop. You kind of have to, you know, you have to do things like RLFT, which is also, you know, parallel to what we see last time. RLFT? RLFT. Reinforcement Learning Based Fine Tuning. Okay. Yeah, yeah. So, you know, similar to the reinforcement learning with human feedback in the LLM world, right? Yeah.

[00:17:24] Host (Cheeky Pint): You want to do maybe closed loop, proper closed loop driving where, you know, you explore all kinds of different situations and then you give it a reward signal to kind of keep it in distribution. For that, then, you need a realistic simulator, right? You also, you know, if you want to have a good RL system, you need to have an opinion for the reward function. This is where the critic comes in, right? If you have a purely end-to-end system, let's look at the simulator. Now, what do you do?

[00:17:52] Host (Cheeky Pint): You have to, you're then constrained to just go from pixels to trajectory, right? That's all, you know, you can run the system on, right? And it's a very high-dimensional space. So, it's a hard problem to generate everything. But even if you solve that, it just becomes incredibly inefficient to run it in the full way of pixels to trajectories and simulation for training or for evaluation.

[00:18:21] Host (Cheeky Pint): So, this is when intermediate representations come in. There are some intermediate representations in the world, in this task, you know, in the physical world, we know are correct. They're not sufficient, but they're not generally limiting, right? You know, there's an object here. There's, you know, a concept of a road. There's signs. There's speed limits. So, this is where augmenting that learned representation, those learned embeddings from the encoder decoder, with that more structured representation is what we do.

[00:18:50] Host (Cheeky Pint): And we find that this kind of gives us additional knobs to simulate, you know, in that space, just, you know, pixels to trajectories. It allows us to have additional safety validation layers in real-time. And it also allows us, you know, it gives us additional mechanisms to specify the reward function, you know, for evaluation of critic or, you know, for training. So, this is, again, like, we've gone kind of full circle of it. Is it N10? Yes, it is. Yes.

[00:19:18] Host (Cheeky Pint): But if you want to do it at scale for full autonomy, it's augmented with all of this other stuff.

[00:19:24] Dmitri Dolgov: That's very interesting on the simulating point. It's just very hard to simulate for an N10 model because it's easier to deal in N10, or it's easier to deal in intermediate representations rather than coming up with the pixel perfect view of the world.

[00:19:36] Host (Cheeky Pint): You need both. Yeah. So, you know, having N10 architecture that's augmented with that structure allows you to kind of play in both of those worlds.

[00:19:45] Dmitri Dolgov: Yeah, yeah, yeah. What are you looking to do as a self-driving car? I mean, it sounds funny, but I think people maybe don't realize that there are many different things that you're looking to solve for where you're looking to get the person to their destination, you're looking to get them there reasonably promptly, but also drive quite smoothly and also have many lines of safety and also not annoy other drivers and get honked at and, you know, and, and, and.

[00:20:10] Dmitri Dolgov: And so what are some of the reward functions or kind of things you're optimizing for that maybe are not obvious to people?

[00:20:17] Host (Cheeky Pint): So safety is the primary focus, right? But of course, we also want to be a smooth driver so that, you know, for both people in the car and other actors. Yeah. And we also want to be, you know, a predictable well-behaved one so that it can nicely fit into the whole social ecosystem of our, our roadways.

[00:20:40] Dmitri Dolgov: It seems like one of the issues that has quickly emerged with self-driving is the fact that people can't have nice things or, you know, not everyone is nice to the robots. And so, you know, whether you're, you know, driving through a dodgy area or getting blocked or, you know, maybe I'm not going to drop you off here. Maybe I'm going to go around the block and, you know, drop you somewhere better.

[00:21:06] Dmitri Dolgov: But all of these, as you say, kind of other human issues, how do you go about solving this?

[00:21:11] Host (Cheeky Pint): A lot of the ones that you mentioned are just things that, you know, we need to work on. And understanding, honestly, you know, said that if we're not dropping you off where exactly where you want it to be dropped off or, you know, we don't give you kind of a good interface to tell us, that's on us. Right? You just, you know, how to make it better. Yeah.

[00:21:32] Dmitri Dolgov: It feels like the drop-off is actually a pretty nuanced part of the self-driving journey. Like the highway stuff and the, you know, the 35-mile-an-hour roads, like that is all nailed. But there's just like a lot of nuance in the drop-off experience.

[00:21:45] Host (Cheeky Pint): I'd say they're all hard. You picked freeways and you picked drop-offs. For different reasons, right? For drop-offs, there's, you're absolutely right. There are, you know, a few things that are maybe not obvious. You know, you just think about this problem. But it's understanding where you want to go and making it as convenient as possible for you. And pick-ups from drop-offs, it's not exactly symmetrical, right? But then there's also understanding the context of the situation where you, you know, where do you stop? You don't want to block a driveway.

[00:22:15] Host (Cheeky Pint): You don't want to, you know, double park. Although in some cases where if it's a quick one, maybe it's okay. So there's a lot of nuance that goes into doing that well so that it's a smoothness, frictionless experience for the rider. Yes. As well as other folks. Yeah. Freeways, for most of the time, not much happens. They're very well structured because we designed them that way.

[00:22:40] Host (Cheeky Pint): But there is still that long tail of really complicated stuff that happens. Yes. Where the consequences of, you know, a bad event are much more severe, right? The speed is much higher. Everything is, you know, quadratic in speed. So, but we see a lot of stuff. And you imagine grills falling off of freeways. Imagine people getting into accidents and kind of spinning out of control.

[00:23:09] Dmitri Dolgov: You see one of those flatbed trucks with just like a bunch of stuff piled in it. And you're driving behind it. I don't know. I always find it very nerve-wracking. It looks a bit... I know. Yeah. And we're like, we've seen them, you know, leave a trail. Yes. Yes. Yeah. Okay. So, it's a different set of problems. But I feel like the general sentiment with Waymo is that the driving has mostly now been solved by you guys.

[00:23:36] Dmitri Dolgov: And it's kind of a question of scaling up and maybe some super long tail stuff, really snowy conditions. Like, is that your sense internally? Or is there actually much more nuance to it than that?

[00:23:43] Host (Cheeky Pint): I would say the, yeah, it's not like, you know, we're done with engineering. Yeah. I would say that we've clearly moved past the stage of scientific research and kind of deep core technology development to this new phase of accelerated global scaling and deployment. Yes. So, you know, we still have work to do. Yeah. Right.

[00:24:07] Host (Cheeky Pint): But I don't see today any limitations or any gaps in the core technology.

[00:24:14] Dmitri Dolgov: The driving is good enough now.

[00:24:15] Host (Cheeky Pint): Well, the core technology, I think, is good enough that I can't, you know, think of any, you know, aspect of driving that is not supported by the fundamental technology. Now, that said, there is a lot of work to do in specialization and invalidation before, you know, we can deploy responsibly. Right. We're not driving everywhere in the world. You know, we are planning to start operating in London and in Tokyo this year.

[00:24:45] Host (Cheeky Pint): And, you know, do we have a driver that, you know, you're using today in San Francisco that we can just plop down in London and go? No. Right. Right. But what we're seeing is incredibly encouraging from the perspective of, like, is the core technology there? Right. So now it's a matter of, you know, collecting the data, doing some specialization and validation. And you can, you know, signs are different. You know, in both of those places, people drive on the other side of the road. But, you know, that's actually not that hard for computers. Right.

[00:25:12] Host (Cheeky Pint): And core technology generalizes really well, but you still work that you have to do. What generalizes least well? Well, increasingly we're finding, especially, you know, now that we're able to kind of hook the Waymo AI to the AI in the digital world, the VLMs, and kind of inherit the general world knowledge from VLMs. We're seeing really strong results from like zero shot or few shot learning because of that general knowledge that we bring in.

[00:25:39] Host (Cheeky Pint): But there are a few things like, say, cold weather, cold winter weather, where it affects the entire stack. Right. So it's not just, you know, the AI. We actually have to. Hardware. You know, you have to need the hardware. You need to have the proper cleaning solution. You know, heating elements in it. And then, you know, think about things that are completely solvable by computers like motion control and slippery surfaces. Right. So that takes a bunch of work.

[00:26:06] Host (Cheeky Pint): You don't get that for free from just, you know, pulling in some, you know, VLM decoder.

[00:26:11] Dmitri Dolgov: Was it the case? I mean, my impression, not knowing anything, is that in the early days, there was maybe a lot of San Francisco specific work or Phoenix specific work in the early markets, whether it be mapping or something else, and that you guys seem to either have solved that in generalizing it or just scaled up your ability to do the city specific work. What enabled the kind of the rapid city expansion?

[00:26:43] Host (Cheeky Pint): We usually think about it, you know, the capability of the Wynwood driver as well as deployment, not primarily and directly in that space of, you know, cities or zip codes. We think about the operating domain. Mm-hmm. Right? And then, you know, freeways, cold weather, all this and stuff. Freeways, cold weather, snow, rain, fog, density, et cetera, et cetera. And then that, like, that's what we are building. That's where we're evaluating. And then that maps to, you know, a city, like a particular city, be within the operating domain or outside of it. Right?

[00:27:14] Host (Cheeky Pint): Right? So what, where, you know, if we provide history a little bit, our initial deployment in where we started offering a fully autonomous commercial service for the first time was in 2020 in Chandler, Arizona. So, and that was on what we called the fourth generation of the Wynwood driver. This was the, if you remember, the Pacifica minivans with, you know, different hardware,

[00:27:38] Host (Cheeky Pint): different software there, you know, we were super focused on kind of doing the whole thing end to end, you know, learn how to build the driver, evaluate it, deploy regularly, operate it end to end, 24 seven with customers, learn from the customers. And then we're very focused on that operating domain of, you know, mostly Chandler, which is a medium, low complexity one. Then when we made the jump to the fifth generation of our system, this is, you know, what's on

[00:28:07] Host (Cheeky Pint): the basis today, we really wanted to take a huge bite out of that operating domain. And we collected data all over the United States, all different states, different cities. When we chose to deploy in the hardest parts of San Francisco, hardest parts of Phoenix, we made a big jump on the hardware side and most importantly on the software, the AI side. And I would say that was the big discontinuous jump.

[00:28:35] Host (Cheeky Pint): And that, that's what you're seeing now after we've, you know, scaled up and, you know, iterated on the, you know, all of the aspects of building and deploying driver. This is now why you're seeing us kind of, you know, go in parallel and scaling, you know, in the U S and.

[00:28:50] Dmitri Dolgov: So driver version five was just a much more generalizable stack than version four. And what was it about it that it, was it just that it had been trained on a much wider data set?

[00:29:03] Host (Cheeky Pint): It was when we made this big bet on AI. Yeah. That was, there was a lot more, you know, kind of little AI models and ML models in the fourth generation. Got it. We made a much bigger bet and jump to kind of AI as the backbone for the fifth generation.

[00:29:18] Dmitri Dolgov: AI is the backbone as the core engine, as in, you're saying that Gen four had lots of small little AI subsystems. Okay. Yeah.

[00:29:29] Host (Cheeky Pint): And that's been, so we kind of made that jump and we've been, you know, iterating and improving the model since then.

[00:29:37] Dmitri Dolgov: As we're seeing with Waymo rolling out widespread autonomy, it has second order changes on the entire system. In this case, traffic patterns or other drivers behavior, or eventually how cities are laid out. And autonomous systems are coming in many domains. In commerce, soon agents are going to be transacting without human intervention. We're basically getting driverless commerce. And Stripe is building the economic infrastructure for AI. And as part of that, we're letting payments be initiated by humans or by agents.

[00:30:06] Dmitri Dolgov: So if you want to sell to agents, or if you want to let your agent spend money all around the web, check out Stripe's agent of commerce suite. Can we talk about hardware a second? And so lots of hardware questions, but one is maybe everyone in this space has a very charismatic demo of a vehicle that is custom made for self-driving.

[00:30:33] Dmitri Dolgov: And so, you know, it's often the van with the, you know, no steering wheel, seats facing in both directions. You know, you guys have one. Tesla has the steering wheel-less cyber cab. You know, Cruise had the Cruise origin. And yet, we're still driving in Jaguars that have a steering wheel in the front and are pretty similar to consumer cars.

[00:30:59] Dmitri Dolgov: And it's interesting to me because, you know, if we were talking about this 10 years ago, we might say, well, yeah, developing a custom car, like, that's relatively straightforward. We know how to put a bunch of sensors on a new car. But the software will take a long time. And what's interesting is we've made huge progress in the software. But interestingly, the cars are still derivatives of, you know, cars that people are driving. And so I'm curious why you just think the custom hardware has not happened as of 2026.

[00:31:27] Dmitri Dolgov: It's obviously, it's a small improvement compared to, you know, Waymo is the big improvement. But it's just interesting that it still hasn't happened.

[00:31:33] Host (Cheeky Pint): Well, let's say our sixth generation of the vehicle and the driver is our version of that. Oh, no, I know it is. It is the Ojai platform, right? So that is, you know, it still has the, you know, we can talk about, you know, whether you want to have the seats pointed backwards or not. I actually, you know, think it looks nice in a demo, but practically speaking, maybe not the way to go. But that is, it is a custom designed vehicle.

[00:31:58] Host (Cheeky Pint): And it is, we put a lot of thought into, you know, moving away from a car that's designed around the driver to a car that's designed around passenger. And it's much more spacious. But it's happening. It's, you know, we're not, it's not open to the public yet. But, you know, I took a ride in it the other day, fully autonomously. And that's coming this year. Yes. How much better is it as a passenger experience? You'll tell me once you give it a try. I love it. Okay.

[00:32:28] Host (Cheeky Pint): So it's, yeah, it's all about the space.

[00:32:31] Unidentified: Yeah.

[00:32:31] Host (Cheeky Pint): And the convenience of, you know, ingress and egress. Yes. And the screens and the interface of the passenger. So we put a lot of thought into every aspect of it. Yes. So it has sliding doors. It's very easy to get in. It has a flat floor. It is, yeah, if you sit in the back, you can like fully stretch out. And there's so much space there. And it looks, you know, from the outside, you know, it looks fairly big. Yes. Right?

[00:32:56] Host (Cheeky Pint): But the actual footprint of that is barely, barely, barely larger than the I-Pace. So it's kind of amazing that, you know, you walk in and just, it feels like you're in the living room.

[00:33:07] Dmitri Dolgov: Yes. I guess my question is just, you know, Waymo does, you know, 25 million rides a year, run-ride-ish, with the Jaguar I-Pace. And it's interesting that so much scaling has happened with self-driving so far on the old, you know, retrofit. Maybe that's to be expected.

[00:33:28] Host (Cheeky Pint): But I think, well, it matches the high. I don't think, you know, it's a given. You're right. But if you think about the value proposition, right, of course there is the safety of it. You don't have to worry about it. There's also the privacy. Yep. Being in the car by yourself, maybe, you know, with other folks, but not having to share that space with another human, right? No, Waymo is a great product, yeah.

[00:33:55] Host (Cheeky Pint): But I guess this is why we're seeing such, you know, consistency in car, you know, drives well, you know, very predictable. And, you know, you can go beyond that, right? You can specialize even more to make the experience even more magical around the rider. But I guess it's, you know, it would have been disappointing if, you know, without the specialized car. And I think I would have been surprised if we leveled off, you know, at some other much lower level of customer. Because, you know, a car seems like, you know, more of an optimization improvement.

[00:34:24] Host (Cheeky Pint): But the core of the value proposition comes from those other factors.

[00:34:28] Dmitri Dolgov: Yes, yes. I guess it's just take risk on one thing at a time. We'll start by, you know, doing the software layer and then we'll build a specialized car or something like that.

[00:34:36] Host (Cheeky Pint): That's right.

[00:34:36] Dmitri Dolgov: That's right.

[00:34:37] Host (Cheeky Pint): Yeah. It's also, well, I mean, as you said, it's a big investment. Yes. So you have to, like, you de-risk the fundamentals. Yes. And, you know, throughout our history, we were very focused on setting the most, you know, the biggest goal for the company to de-risk the most important questions, right? We talked about, you know, the third generation where, you know, we wanted to deploy something and go end to end. We talked about what was the goal with the fourth generation. Oh, sorry, the fifth generation. And then there's the sixth generation, right?

[00:35:05] Host (Cheeky Pint): So there's the sixth generation where it's made sense to go out and spend all this, you know, effort into the custom.

[00:35:10] Dmitri Dolgov: And sixth generation is both the custom vehicle. Is it also a new generation of the driving stack?

[00:35:17] Host (Cheeky Pint): Yeah, it is the new hardware. Yep. The sensors, you know, the hardware, the software and hardware they're putting on the Ojai vehicle is the sixth generation. It is very different from the fifth generation. It is simpler. It is more capable. It is much lower cost. It's a fraction of the cost is, you know, comparable to what you would get like a fancy ATA system. Nowadays, the driver assist system. The software is pretty much the same. So that's another.

[00:35:47] Host (Cheeky Pint): So when we talk about generalizability of the Wiimoo driver, you know, we talk about weather conditions. We talk about cities. But it also generalizes well to different vehicle platforms and different sensor configurations.

[00:35:59] Dmitri Dolgov: Okay, so Gen 6 is a new vehicle and a new sensor stack, but it's almost a tick-tock cycle happening here. It's a similar software. That's right.

[00:36:07] Host (Cheeky Pint): That's right. And then we're going to put the sixth generation Wiimoo driver on other vehicle platforms like the Hyundai Ioniq that's coming, you know, later in the year.

[00:36:19] Dmitri Dolgov: What is different about the sixth generation hardware stack and how did you make it cheaper?

[00:36:24] Host (Cheeky Pint): So it still has the same three sensing modalities, but we've made significant optimizations in all three. Yeah. So unification, simplification, and there's just, you know, the kind of just riding the...

[00:36:40] Dmitri Dolgov: Yeah, is it a classic case of, you know, manufacturing scale where we're not even more...

[00:36:44] Host (Cheeky Pint): Well, scale hasn't fully come in place, but all of those, if you think about the supply chains, the industries, cameras is pretty mature. Radars, way many years ago, used to be bulky, complex, very expensive, you know, when we were putting them on planes. But then we started putting them on cars. Now you can get a decent automotive radar for, you know, tons of dollars.

[00:37:10] Host (Cheeky Pint): There is, you know, a variant of the automotive radar, it's called the imaging radar, and it gives you a richer... So that is also, you know, has come down in cars drastically, but it's a little bit behind your standard automotive radars. Lighters are following the same very predictable, very well-known trend. So we're riding that, and we're also, you know, learning from the previous generation to just make improvements and simplifications and optimizations.

[00:37:36] Dmitri Dolgov: So I have a very silly question. What are lighters versus radars better at in a self-driving complex?

[00:37:42] Host (Cheeky Pint): Lighter...

[00:37:43] Dmitri Dolgov: Are they complementary?

[00:37:44] Host (Cheeky Pint): They're very complementary. You know, it's all blasting, you know... Equalication. Effectively, like, you know, blasting, you know, photons out there, and then they bounce off of something, they come back, you know, you measure what comes back. The frequencies are very different. So laser gives you... It's very, very high resolution.

[00:38:10] Host (Cheeky Pint): So you can, you know, think of it as like a laser beam that goes out, you know, spins around. It, you know, shoots out millions of these laser pulses, you know, per second. And then each one comes back, and you can, you know, you're kind of sampling the 3D structure of the world with very high resolution. So LiDAR for very fine-grained mapping. That's right. Radar has much lower resolution, but because of, you know, the physics of it, it can... It degrades much better in adverse weather conditions.

[00:38:39] Host (Cheeky Pint): So fog, snow, you know, heavy rain... So it's not going to be occluded by particles between it and the target. So imagine driving in super dense fog. Yes. We're close to San Francisco, so probably don't have to think, you know, that hard. It can be really hard to see. So cameras degrade. Yes. Laser, you know, depending on kind of the size of the particulates can degrade better or worse than camera. Radar is not well-affected.

[00:39:07] Host (Cheeky Pint): So, you know, you can imagine driving on a freeway, then radar will give you really good returns for, you know, cars that are absolutely, you know, invisible in the, you know, in the camera space. Oh, that's interesting.

[00:39:17] Dmitri Dolgov: So does that mean there are some environments where you'll be relying significantly more on radar?

[00:39:23] Host (Cheeky Pint): But the performance is good enough? Well, it's a combination of the sensors, right? So we rely on, you know, each one is noisy, right? How the noise characteristics show up in different environments is different. But it is, I mean, it's not like we switch from one to another. It's not like, you know, we estimate, you know, what's happening with the world through cameras. And for radars and for lightars. And then we compare. No, they're like, there's an encoder for camera. There's an encoder for lightars. There's a camera.

[00:39:51] Host (Cheeky Pint): And they all go into the, you know, the system that gives you jointly the best view of what's happening in the world. So if you're, you know, if it's a nice, bright, sunny day, cameras are very valuable. If, you know, it's pitch dark or you have like sun in your face or you're blinded by the headlights from, you know, oncoming car, then camera will degrade. There's still some, you know, noisy signal, but it will degrade. Yes. And radar is completely unaffected. Right.

[00:40:19] Dmitri Dolgov: Are there technical problems that are your white whale or you're just, you're still chasing or you are particularly interested in solving? Even if they're kind of niche for the, you know, we just, we really want to have, you know, driving when it's actually snowing nailed or steep hills in San Francisco or, you know, are there problems you've been very interested in historically or still are?

[00:40:40] Host (Cheeky Pint): I, I'm super excited right now about the accelerating global expansion, more cities in the United States and going internationally. Yes. So being, I don't know, I understand I'm not answering your question about the technology. I'll, you know, come back to that. But really that's the thing that I'm, you know, today most excited about.

[00:41:00] Host (Cheeky Pint): Just, you know, go be, you know, getting to a place where any major, you know, metropolitan area you can fly into the airport and then take a Waymo and go anywhere you want to go. Like that is insanely exciting to me right now. So then, you know, technically what I'm most excited about is all of the rapid progress in AI.

[00:41:29] Host (Cheeky Pint): And the world models, the foundational model work. And it is just such a massive boost to how much we can simplify the system, how much we can bring down the cost and how we can scale globally. And, you know, there's some magic that happens that I don't think I would have anticipated, you know, a few years ago. So that I find from the technical perspective, just insanely thrilling.

[00:41:56] Dmitri Dolgov: Yes. When you talk about kind of the progress in AI, what are the most fun parts of it for you these days?

[00:42:01] Host (Cheeky Pint): I think it's seeing the capability and the scaling laws from this approach of starting, you know, with that cornerstone of the foundational model and then specializing to teachers and then, you know, distilling. It just, you get such big wins in performance across the board.

[00:42:25] Host (Cheeky Pint): And I just, you know, you invest something into the architecture or get a better data or training recipe. Yes. And then, you invest in that early stage and then it just has massive amplification and ripple effects. So that is, you know, in some ways is kind of magical. And then you, I guess, then you see it on the car.

[00:42:47] Host (Cheeky Pint): And I've had some moments where, you know, car does something and, you know, look at a log and I've been surprised. Like it does things that I didn't think it was capable of doing. Right. So it's that, you know, it's...

[00:43:07] Dmitri Dolgov: When you see emergent behavior, that's kind of a proud moment.

[00:43:10] Host (Cheeky Pint): That's right. One example, yeah. You know, it's, you know, when you build a system and then, you know, you think you understand, you know, how it works and you understand fully, you know, the limits of its capability and performance. And then it does something, you know, kind of almost magical. Yes. It's exhilarating. Yes.

[00:43:26] Host (Cheeky Pint): So one example I can give you, I think I've shared some videos of that publicly in some talks, was this example where the situation that happened in San Francisco, a fairly benign situation where at an intersection, our light is red. There's new cross traffic, a buzz goes by and, you know, it stops partially blocking. It stops partially blocking, annoying. Our light turns green. So we start to go.

[00:43:55] Host (Cheeky Pint): We're nudging around the bus. And then you see a pedestrian being detected on the other side of the bus. Right. And then, you know, car responds appropriately. It slows down, goes a little bit wider. Yep. And, you know, then a pedestrian actually emerges from the bus and, you know, we go on our own way. So the first time I looked at that log, what's going on here? Like, I know we have pretty darn good sensors. And the software is very capable. Like, we don't see through stuff. Yeah, yeah, yeah.

[00:44:25] Host (Cheeky Pint): Right? Like, that's not how cameras or lighters and radars work, right? They can find the bus. I saw the pedestrian through the bus. You saw the pedestrian on the other side of the bus. Yeah, yeah, yeah. And it's not like, you know, you look at the windows. You're like, okay, you know, radars shouldn't, this massive metal box. Yeah. Yeah. You know, look at the sensor data. Yes. And, like, it shouldn't, radars shouldn't be able to go through it, right? You know, camera, like, you can't see in the camera because, you know, there's reflections and there's people on the bus. So it's not like you can see through the windows. Right. So, like, what is going on?

[00:44:55] Host (Cheeky Pint): Maybe it's, you know, noise or some coincidence. And I, you know, first time I saw it, I couldn't actually believe it. It's like, no, no, there's something. It doesn't sound right. So what actually turned out was happening is that our peripheral ladders bounce under the bus. And there was just a little bit of very, very noisy reflection of the movement of the person's feet. That was enough for the AI models that, hey, likely there's a pedestrian there. And I'm going to, you know, I'll detect it as such. Yeah, yeah, yeah.

[00:45:24] Host (Cheeky Pint): And moreover, there's enough data there to predict what they're going to do. Yes. It just kind of blew my mind.

[00:45:31] Dmitri Dolgov: Is this the perfect example to explain what we were talking about earlier? The value of one, fusion across a sensor suite. But then secondly, building, I mean, relatedly, building an intermediate representation of what's going on. Where if you're just dealing with pixels, I mean, the person behind the bus does not exist in pixel space.

[00:45:56] Dmitri Dolgov: And so you need to have some representation of the world that exists to be able to reason about the person behind the bus.

[00:46:02] Host (Cheeky Pint): I think it's an example where giving it kind of an using that intermediate representation to boost the level of performance of all parts of the model. Yes. Is what's happening here. Mm-hmm. Just imagine, you know, solving this problem with a black box, you know, purely open loop. Yep. Imitative system. Be, you know, is it, you know, impossible? No. Yeah.

[00:46:31] Host (Cheeky Pint): But in practice, what would it take to achieve that level of performance? Yes. Very, very difficult.

[00:46:35] Dmitri Dolgov: What metrics can you share on just where the business is at today in terms of rides, revenues, cars on the roads?

[00:46:44] Host (Cheeky Pint): We have about 3,000 cars on the roads. We're doing about half a million rides per week. That translates to about, you know, over 4 million fully autonomous miles per week. We are operating in a fully autonomous mode in 11 cities in the U.S. And 10 of those, we have riders, public, you know, riders.

[00:47:14] Host (Cheeky Pint): What's the ghost city? The ghost city is Nashville. We just started there. Okay. So we just opened it up to riders in four new cities in one day. That was one of those, you know, little but super exciting moments where I thought back to the history. Like, how long did it take us from the first time we started fully autonomous rider-only operation to the first time we had external riders in four cities? It was about eight years.

[00:47:44] Host (Cheeky Pint): And then, you know, like the other week, we just launched four in one day.

[00:47:48] Dmitri Dolgov: Yes, yes. It seems now clear that in 15 years, most miles that are driven will be autonomous. Like, there'll be some burn-in period and, you know, there's lots of old cars on the road. Like, I think it'll actually take a little while. And some of that will be by level four, level five systems expanding in new cities and that expansion continuing.

[00:48:13] Dmitri Dolgov: Some of it will be, you know, you referenced existing driver assist systems and kind of getting up to, you know, level two and level three and existing systems in across current car brands getting more and more capable. What do you think that working your way up from the lower levels versus working your way expanding from existing products like Waymo? What will that convergence look like? Because we're going to eat it from both sides.

[00:48:41] Host (Cheeky Pint): I don't believe we will. And I actually think this. That's a great answer. You know, cars will get smarter. There's going to be, you know, advances in driver assist systems. And if there is, you know, at the same time from level four autonomy, you know, there is simplification. And, you know, the sensors of today are not going to be the sensors of tomorrow. So they'll be much more integrated. They'll be simpler. There'll be much lower cost.

[00:49:08] Host (Cheeky Pint): So from that perspective, they're going to, you know, there is a path of convergence. Yep. And there's also, you know, a path of convergence from, you know, the product lines. Right hailing and what, you know, you can take, you know, a ride through the Waymo app today. You know, eventually they'll be on your personal car. So that I see. And talk about the technology. And I see it just as fundamentally two different problems. There's driver assist systems. And then there is full autonomy.

[00:49:35] Host (Cheeky Pint): And I think it's deceptive to think of them as kind of incremental, you know, on one spectrum of complexity.

[00:49:43] Dmitri Dolgov: Okay. But you think one cannot work one's way up from driver assist systems to full self-driving? You think you have to start building a full self-driving system?

[00:49:53] Host (Cheeky Pint): I think you have to tackle, if I think about the hardest parts of building a fully autonomous rider-only system, they are very different from, you know, what you do for a driver assist system. Yep. And, of course, you know, some work in this space helps you, right? So, you know, I don't want to say you can't make the jump, but it is a qualitative jump.

[00:50:18] Dmitri Dolgov: Yes. When can I buy a Waymo so that I don't need to wait for it when I want to go? I can just, like, when I'm ready, I can walk out the door and it's there.

[00:50:26] Host (Cheeky Pint): I'm not going to give you a date today, but you're not the first person to bring this up as a product request. Do we know it? Okay. I'll add it to the list.

[00:50:37] Dmitri Dolgov: You know, that waiting for the car, it should be nice just in the garage there and keep your stuff in it and everything. It's not the first time you've heard that request. So, it seems to me operationally very intensive and very hard. Like, a self-driving car is actually not self-driving. It takes a village. You have all of the human operator ready to step in.

[00:51:03] Dmitri Dolgov: And, you know, there was that thundering herd incident that you guys talked about in San Francisco that kind of highlighted that for people. And then there's just, like, keeping the cars clean and, you know, keeping everything running in that regard. And so, can you describe just what the operational infrastructure that sits behind Waymo looks like?

[00:51:20] Host (Cheeky Pint): Sure. And I will say that we are overall, you know, in all of those areas on a path of increasing efficiency and automation. Yep. All right. So, you know, the number of manual steps that one had to do, you know, five years ago to, you know, launch Waymo versus where we are today is drastically different.

[00:51:50] Host (Cheeky Pint): Right? So, you know, but nowadays, if you look at one of our depots as like a fully automatically orchestrated, you know, dance of autonomous vehicles. So, the way it looks, you know, what it looks like today is cars will automatically, you know, go on there, you know, to pick up their riders, you know, serve their trips.

[00:52:17] Host (Cheeky Pint): If for some reason, you know, they need to come back, you know, maybe they're low on energy, maybe somebody, you know, left a mess on the car, they will, you know, automatically come to the depot. Right? If it is, so cleaning today is a manual process, right? So, it'll get flagged in the car, you know, we have fleet management systems. Say, hey, you know, car, you know, number, you know, 378 needs cleaning. And we'll actually, on the sensor dome, we're able to, you know, display icons.

[00:52:46] Host (Cheeky Pint): So, we'll, you know, show you like a little, you know, emoji. Put the handouts. Yeah. Yeah, and, you know, there's, you know, people whose job it is to clean the car still come and, you know, clean it up. If that's, you know, cleaning is not required and it's just charging, you know, we'll say, you know, pull, automatically pull into a charging stall. And we'll say, hey, you know, I need charging. We don't yet have automated charging. In the future, you can imagine that being fully automated, right? But, you know, a person will come in and, you know, plug in a cable and the car will charge and then say, hey, you know, now I'm ready to go.

[00:53:12] Host (Cheeky Pint): And, you know, it will get unplugged and the car will, you know, pull out of the, you know, its parking stall and then go, you know, on its merry way.

[00:53:19] Dmitri Dolgov: One of the new Porsches, I think it is, has inductive charging, like just like your iPhone where you just drive over the charging mat. I was amazed that that works at car scale. But, yeah, presumably in the future they'll just be able to drive on with the charging mat. Or do you think just robotic plug-in will be easier? We'll see. We'll see.

[00:53:36] Host (Cheeky Pint): I don't know. I think there's, you know, some questions about, you know, efficiency and, you know, how that plays into the overall cost and which one will be, you know, most cost beneficial, you know, remains to be seen, I think.

[00:53:45] Dmitri Dolgov: How well behaved are the Waymo riding population in terms of not living a mess in the car?

[00:53:53] Host (Cheeky Pint): We have wonderful riders. We have the most amazing customers in the world. Generally, I would say they are very good. But I think, you know, there is something about, you know, I talked about not having, you know, a person in the car. It's not somebody else's car. In some ways, you kind of like want to preserve the, I think generally people want to kind of preserve the nice aspects of it. It's a broken window thing.

[00:54:20] Dmitri Dolgov: It's so clean to begin with. I know. Yeah.

[00:54:22] Host (Cheeky Pint): It's kind of like, you know, I think that that's the general trend that we see, right? And it's like because there's not somebody else's space, you know, you're in it. It feels like it's your own. Yeah. So you don't like want to mess up, you know, your own space. I think, I mean, I don't want to speculate too much on the psychology of things. However, I will say that it varies. And you can imagine, you know, a college town on a, you know, Saturday night. And, you know, that's a different distribution. Yes. Yes.

[00:54:48] Dmitri Dolgov: Will I be able to get Waymo at any address that has USPS service in the U.S.? Or will there be some head-tail dynamic where Ketchikan, Alaska is just never worth it?

[00:55:04] Host (Cheeky Pint): Eventually it will. Absolutely. Right. There's no doubt in my mind. I think it's just a matter of when and, you know, what modality would make the most commercial sense. This is for your ride share versus privately owned. For ride, you know, it's not a technical problem. I mean, you know, technology is solved. Yes. But then, you know, if you're in the middle of nowhere and there's just not enough density of the trips, does it make sense for the ride-hailing service that, you know, Waymo is running to, you know, have cars on standby? Yes. Yes. Yes. Yes. Yes. Probably not, right?

[00:55:31] Host (Cheeky Pint): They can be deployed, you know, somewhere else and you probably don't want, you know, a horribly bad ETA. And this is where, you know, a personally owned vehicle that is equipped with the Waymo driver is maybe, you know, how you will see it materialized.

[00:55:45] Dmitri Dolgov: Relatedly, what will the second order effects of, say, majority autonomous traffic be? Like, it feels like a lot of things will work better where, as you say, you know, when someone merges into a lane very poorly and everyone all the way back has to, you know, slam on the brakes, that's kind of anti-social behavior. And so it feels like higher quality and more pro-social driving will just, I mean, basically reduce traffic a little bit, even for the same number of cars on the road.

[00:56:09] Dmitri Dolgov: But presumably there'll be other second order effects, like we'll want higher throughput traffic lights and, yeah, how else will things change?

[00:56:17] Host (Cheeky Pint): So the first thing I think, you know, that you mentioned is, I think that's a huge deal. I just need to think about traffic jams. Yep. What's that saying? The Navy SEALs, slow is smooth and smooth is fast. That's what, like, you know, traffic jams are, like, you know, you accelerate abruptly, then you come to a stop and, you know, sometimes you have a traffic jams. Like, what happened? Yes.

[00:56:42] Host (Cheeky Pint): Well, like, you know, an old lady crossed the road three hours ago and we still have the standing wave there, right? So if everybody, you know, was a kind of a smooth, predictable driver and a consistent driver and you would still have those, you know, traffic jams at the time off. Yeah. But then the time constant to clean it out, I think would be very different. But longer term, you know, things like parking lots.

[00:57:07] Host (Cheeky Pint): Right now, if you look at, you know, what is our most interesting pieces of land allocated to, you know, it's parking lots, it's garages. And why is that? Yes. Well, because, again, you know, your car is just sitting there 90% of the time, right? If, you know, more cars become fully autonomous, then there's no, you know, that, right?

[00:57:28] Host (Cheeky Pint): And, like, then imagine, just imagine what you can do with, you know, your favorite city in the world if you don't have to spend that money, you know, that huge fraction of it on, you know, just keeping your, these chunks of metal sitting around.

[00:57:42] Dmitri Dolgov: Yeah, I don't think people often realize how big a deal parking minimums are for the layout of the urban landscape. The coffee shop here where I am would like to have outdoor seating but can't because it would reclaim parking spots. Yeah, wouldn't that be wonderful?

[00:57:54] Dmitri Dolgov: I have a few more questions, but I'm curious to talk about Google's relationship with self-driving where, again, it feels like right now Waymo is, aside from everything else, AI-related, kind of the most exciting thing happening at Google. But it was a very long journey to get here.

[00:58:19] Dmitri Dolgov: I mean, I feel like you could say that Google almost started working on it too early because you were saying there's been a bunch of recent enabling technologies. And so did it require Google starting when it did so early or could one have spun up this project in 2015, 2020? And then how did Google keep the faith when it always felt like it was perennially two years away?

[00:58:47] Host (Cheeky Pint): Yeah, no, on the latter part, I just have to give credit and huge kudos and gratitude to Larry and Sergey and Alphabet Leadership Center company. It is part of the culture and the DNA of the company is to have that vision and have the stamina and conviction to go the distance.

[00:59:19] Host (Cheeky Pint): So to the other part of the question, was it too early? I don't know. I think what we've been seeing, you know, clearly all of the breakthroughs that we've seen over the years have changed, you know, how we're building the system. But the complexity of the problem is such that, like, you need to go through these iterative cycles, right?

[00:59:45] Host (Cheeky Pint): It's not, you know, still, and we've seen many waves of technology, right? There's, you know, breakthroughs in, you know, 2013, ImageNet came around. Okay, like, that is the right time to start. Like, that would be a self-driving company. And, you know, Transformers came around and, you know, VLMs. And all of those are super powerful. And, you know, have applications in other spaces. In the digital world, they certainly have an impact on, you know, our AI and the physical world.

[01:00:15] Host (Cheeky Pint): But there are no silver bullets, right? They kind of, they drastically reshape that early part of the curve. Like, it's always been the nature of this problem. It's very easy to get started. It's deceptively easy to get started. But it is super hard to go, you know, the full distance and get... In the case, to mean... Well, it's, you know, the number of nines, right? That you have to, like, there's the standard, you know, engineering rule of thumb that, you know, every next nine takes, you know, 10x more. Right? So, I...

[01:00:44] Host (Cheeky Pint): Yeah, maybe there is a more optimal path, but I don't see there's, you know, that there's some magical moment where the true complexity of the problem goes away. And then you can just take some off-the-shelf components and you're a business, right? Because if that were the case, then I think the industry would look, you know, very different today.

[01:01:00] Dmitri Dolgov: Yeah, yeah. Last question I have. You've been promoted a lot at Google. It feels like Google really recognized your talents. Just what do you think Google does? Like, Google is famously one of the very best in the world. As a technical talent and say, you know, the current AI wave more broadly happening, you know, is either stuff happening at Google or generally Google alumni. But just what have you observed firsthand from how Google does this so well?

[01:01:30] Host (Cheeky Pint): Yeah, I would say Google, you know, that culture of Google of not accepting the status quo. Having, you know, having a big vision and investing in technical talent, the people who can, you know, go the distance and realize the vision. That is part of the culture. I think this is what you're seeing.

[01:01:55] Host (Cheeky Pint): And with the breakthroughs in AI in the digital world and, like, all of the early investments in, you know, transformers and other fundamental technologies. You know, quantum computing. Yeah. And, you know, I guess we're not unlike those efforts as well.

[01:02:13] Dmitri Dolgov: Thank you.

[01:02:14] Host (Cheeky Pint): Yeah. Thank you. Thank you. Thank you.