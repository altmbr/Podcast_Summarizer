# OpenAI Sora 2 Team: How Generative Video Will Unlock Creativity and World Models

**Podcast:** Training Data
**Date:** 2025-11-07
**Video ID:** w9oTtvbyLP8
**Video URL:** https://www.youtube.com/watch?v=w9oTtvbyLP8

---

[00:00:00] For opening across the board, it's really important that we kind of like iteratively deploy technology in a way where we're not just like dropping bombshells on the world when there's like some big research breakthrough.
[00:00:08] SPEAKER_04: We want to co-evolve society with the technology.
[00:00:12] And so that's why we really thought it was important to like do this now and like do it in a way where you know we've hit this again this kind of like gpt3.5 moment for video.
[00:00:19] SPEAKER_04: Let's make sure the world is kind of aware of what's possible now.
[00:00:22] And also you know start to get society comfortable and like figuring out the rules of the road for this kind of like longer term vision where there are just copies of yourself running around in Sora and the ether.
[00:00:33] SPEAKER_04: Like doing tasks and like reporting back in the physical world because that's where we're headed long term.
[00:00:52] Today on training data we sit down with the team behind open a eyes Sora, little peoples Thomas Dimson and Rohan Sahai.
[00:01:01] SPEAKER_03: You'll hear about space time tokens, building internal world simulators and how optimizing for creation instead of consumption is just better for social platforms.
[00:01:10] SPEAKER_03: This conversation goes way beyond video generation and into questions about how society will co-evolve with powerful simulation technologies.
[00:01:17] SPEAKER_03: We promise that this was an actual real world conversation and not a video generation.
[00:01:22] SPEAKER_03: We don't know how to prove that to you. Let's jump in.
[00:01:25] SPEAKER_03: Hey guys, thank you for being here at Sequoia. Congratulations on Sora.
[00:01:30] SPEAKER_03: Thank you.
[00:01:31] SPEAKER_03: Maybe you could tell us a little bit about yourselves and how you got to open AI and Sora.
[00:01:36] SPEAKER_03: Yeah, I'm Bill. I'm the head of the Sora team at open AI.
[00:01:39] SPEAKER_04: I had a pretty traditional path came through undergrad doing research on video generation then continue that work at Berkeley.
[00:01:45] SPEAKER_04: Then started at open AI working on Sora from the first day I joined.
[00:01:50] SPEAKER_04: I'm Thomas. I work as an engineering lead inside of Sora.
[00:01:54] SPEAKER_01: I have a bit of a longer story but I was working at Instagram for about seven years doing some of the early machine learning systems and recommender systems there.
[00:02:05] SPEAKER_01: But it was a very tiny company. It was about 40 people.
[00:02:08] SPEAKER_01: Then I quit. Did my own startup for a while which was Minecraft and the browser which we talked about a couple of times.
[00:02:14] SPEAKER_01: I think that open AI noticed that we had a very cracked product team there and so they acquired our company.
[00:02:20] SPEAKER_01: I've been bouncing around different products inside of open AI and on the research side as well.
[00:02:24] SPEAKER_01: I was training but super happy we landed together on Sora to bring this thing to life.
[00:02:30] SPEAKER_03: It was a really cool product in between two like the global illumination product.
[00:02:34] SPEAKER_03: Oh yeah, it's still believing it.
[00:02:35] SPEAKER_03: Yeah, me too.
[00:02:36] Awesome. I'm Rohan. I've been at open AI for about two and a half years.
[00:02:40] SPEAKER_02: Start as an IC on chat GPT.
[00:02:42] SPEAKER_02: But then as soon as I saw the video of general research I got quickly Sora pilled and made my way over there.
[00:02:48] SPEAKER_02: So, probably we had the Sora product team before that just start up big companies within kind of the valley.
[00:02:54] SPEAKER_02: Much of random stuff.
[00:02:56] Cool.
[00:02:57] SPEAKER_03: Well, Bill, you are the inventor of the diffusion transformer.
[00:03:01] SPEAKER_03: Can you tell us what that is?
[00:03:03] SPEAKER_03: Yeah.
[00:03:04] SPEAKER_04: So, most people are pretty familiar with autoregressive transformers which is the cortex that powers a lot of language models that are out there.
[00:03:10] SPEAKER_04: So, there you generate tokens one at a time and you condition on all the previous ones to generate the future.
[00:03:15] SPEAKER_04: Diffusion transformers are a little bit different.
[00:03:17] SPEAKER_04: So, instead of using autoregressive modeling, it's kind of the core objective.
[00:03:21] SPEAKER_04: You're using this technique called diffusion which at a very high level basically involves taking some signal, for example, video, adding a ton of noise to it.
[00:03:29] SPEAKER_04: And then training neural networks to predict the noise that you applied.
[00:03:33] SPEAKER_04: And this is kind of a different kind of iterative generative modeling.
[00:03:36] SPEAKER_04: So, instead of generating token by token as you do in autoregressive models, diffusion models generate by gradually removing noise one step at a time.
[00:03:45] SPEAKER_04: And in Sora 1, we really kind of popularize this technique for video generation model.
[00:03:50] SPEAKER_04: So, if you look at all of the other competitor models that are out there both in the states and in China, most of them are based on DITS diffusion transformers.
[00:03:57] SPEAKER_04: And a big part of that is because DITS are a really powerful inductive bias for video.
[00:04:01] SPEAKER_04: So, because you're generating the whole video simultaneously, you really solve issues where a quality can like degrade or change over time, which is kind of like a big problem for a prior video generation systems, which DITS ended up fixing.
[00:04:12] SPEAKER_04: So, that's kind of why you're seeing them proliferate within video generation stacks.
[00:04:16] SPEAKER_03: When I try to visualize it, I mean, for diffusion, you have a matrix of pixels.
[00:04:21] SPEAKER_03: And then you do the entire video at the same time, which you can basically see as different frames, I imagine.
[00:04:26] SPEAKER_03: Can you visualize that as matrix of matrices that basically transforms over time?
[00:04:32] SPEAKER_03: Yeah, that's a good question.
[00:04:33] SPEAKER_04: So, we really kind of consider things at the granularity of like space-time tokens, which is sort of like an insane phrase.
[00:04:39] SPEAKER_04: But, you know, whereas, you know, for example, characters are very fundamental building block for language.
[00:04:44] SPEAKER_04: For vision, it's really this notion of a space-time patch.
[00:04:47] SPEAKER_04: You can just imagine this little cuboid that composes both X and Y, like spatial dimensions, as well as a temporal locale.
[00:04:55] SPEAKER_04: And that really is kind of like the minimal building block that you can like build visual generative models out of.
[00:05:01] SPEAKER_04: And so, diffusion transformers sort of consider these, almost you can think of it like a voxel by voxel.
[00:05:07] SPEAKER_04: And, you know, in the traditional versions of these diffusion transformer models,
[00:05:13] SPEAKER_04: you have all of these little space-time patches talking with all of the other ones.
[00:05:16] SPEAKER_04: And that's how you actually are able to get properties like object permanence to fall out.
[00:05:20] SPEAKER_04: Because, basically, you have full global context of everything going on in the video at every position in space-time.
[00:05:27] SPEAKER_04: There's like a very powerful property for a neural network to have.
[00:05:30] SPEAKER_04: And is that the equivalent of the attention mechanism as the object's movement throughout the video?
[00:05:36] SPEAKER_03: Yeah, that's right.
[00:05:37] SPEAKER_03: So, in our like, SORL on blog posts, video generation models as world simulators, we kind of laid out some visuals,
[00:05:43] SPEAKER_04: which sort of go into exactly your point here, which is really attention is like a very powerful mechanism, right?
[00:05:48] SPEAKER_04: For sharing communication, like sharing information across space-time.
[00:05:53] SPEAKER_04: And if you represent data in this way, right, where you patchify it into a bunch of these space-time tokens,
[00:05:58] SPEAKER_04: as long as you're, you know, properly using the attention mechanism, that allows you to transfer information throughout the entire video all at once.
[00:06:05] SPEAKER_04: What is the biggest differences between SORL on one and two?
[00:06:08] SPEAKER_00: And I remember with the original SORL one, you were really seeing kind of emergent properties where the more you scale,
[00:06:13] SPEAKER_00: the more it's able to do things like understand physics.
[00:06:16] SPEAKER_00: So, SORL is sort of two purely a function of scaling or one of the biggest differences?
[00:06:20] SPEAKER_00: Yeah, that's a great question.
[00:06:21] SPEAKER_04: You know, we've spent a long time really just doing like core generative modeling research since the SORL one launch to really figure out how we get the next step function improvement in video generation capabilities.
[00:06:31] SPEAKER_04: We really kind of operated from first principles, right?
[00:06:34] SPEAKER_04: So, we really want these models to be extremely good at physics.
[00:06:37] SPEAKER_04: We want them to kind of feel intelligent in a way that I take like most prior video generation models don't.
[00:06:43] SPEAKER_04: So, by that I really mean, you know, if you look at kind of any of the previous set of models that were out there, you'll notice a lot of this kind of like the effects that happen.
[00:06:50] SPEAKER_04: Like if you try to do any sort of complicated sequence of like physical interactions, right?
[00:06:54] SPEAKER_04: For example, like spiking gymnastics classic.
[00:06:57] SPEAKER_04: Writing a dragon like you did.
[00:06:59] SPEAKER_03: Writing a dragon? That was fun. That happened for real actually, Constantine.
[00:07:02] SPEAKER_04: Oh, I'm sorry.
[00:07:03] SPEAKER_04: I'm not sorry.
[00:07:05] SPEAKER_04: You know, they're like very clear problems with the past generation of models that we really like set out to solve with SORL 2.
[00:07:13] SPEAKER_04: And I think one thing that's really cool about this model compared to prior ones is that when the model makes a mistake, it actually fails in a very unique way that we haven't seen before.
[00:07:22] SPEAKER_04: And so concretely, for example, if let's say like the text input to SORL is a basketball star wants to like shoot a hoop, right? Shoot a three throw.
[00:07:31] If he misses in the model, SORL will not just like magically guide the basketball to go into the hoop, right?
[00:07:36] SPEAKER_04: To be over optimistic about respecting what the user asks for, it will actually defer to the laws of physics most of the time.
[00:07:42] SPEAKER_04: And the basketball actually rebound off the backboard.
[00:07:44] SPEAKER_04: And so this is a very interesting distinction right between like model failure and like agent failure agent as in the agent that SORL is like implicitly simulating as it's generating video.
[00:07:54] SPEAKER_04: And we haven't really seen this very unique kind of like semantic failure case in like prior video models. This is really new with SORL 2.
[00:08:00] SPEAKER_04: It's kind of a result of you know, just the investment we put in like really doing like the core generative modeling research to like get this massive improvement capability.
[00:08:08] SPEAKER_04: Okay, so not purely a function of scale. You're actually, you know, there's there's some concept of agents and plus it's in this.
[00:08:15] SPEAKER_00: There's things you're doing beyond just scaling for model.
[00:08:17] SPEAKER_00: Well, the notion of agents I'd say is actually mostly like implicit from from scale.
[00:08:22] SPEAKER_04: Like you know, in the same way where we kind of showed that object permanence right begins to emerge and SORL 1 pre training when you hit some like critical flops threshold.
[00:08:31] SPEAKER_04: We see similar kinds of things happen as we like push the next frontier right. So you begin to see these agents act more intelligently.
[00:08:38] SPEAKER_04: You begin to see the laws of physics be respected in a way that they aren't at like lower compute scales.
[00:08:43] SPEAKER_04: How does the concept of a space time latent patch relate to a space time token relate to object permanence and how things move through the physical world.
[00:08:53] SPEAKER_04: Yeah, that's a great question. So I'd say space time patch and space time token are more or less anonymous with one another.
[00:08:58] SPEAKER_04: I'll use them interchangeably.
[00:09:00] SPEAKER_04: You know what's really beautiful right is when people started scaling up language models from like GPT 1 to GPT 2 to GPT 3.
[00:09:09] SPEAKER_04: We really began to see the emergence of like world models internally in these systems.
[00:09:14] SPEAKER_04: And what's kind of beautiful about this right is there's incredibly simple tokenizers that actually go into like creating the data that we train these systems on.
[00:09:21] SPEAKER_04: But despite this very simple representation right you know like BPE characters what have you.
[00:09:28] SPEAKER_04: When you put enough compute and data into these systems like in order to actually solve this task of predicting the next token.
[00:09:34] SPEAKER_04: You need to develop an internal representation of how the world functions right you need to like simulate things.
[00:09:39] SPEAKER_04: And like you know the models make lots of mistakes right now at like low compute scales.
[00:09:43] SPEAKER_04: But as you continue pushing it from three to four to five.
[00:09:45] SPEAKER_04: You just see these internal world models get more and more robust.
[00:09:48] SPEAKER_04: And it's really analogous for video right and in many ways more explicit.
[00:09:52] SPEAKER_04: So I think it's easier to picture what like a world model or a world simulator looks like with video data right because it is literally representing like the raw observational bits of like all of reality.
[00:10:01] SPEAKER_04: But what's really remarkable right is because these space time patches are just this like very simple and like highly reusable representation that can apply to like any type of data right.
[00:10:10] SPEAKER_04: Whether it's just like video footage of like this set whether it's like anime cartoons like whatever it is.
[00:10:16] SPEAKER_04: You're just able to build like one neural network that can operate on this vast extremely diverse set of data and really build these like incredibly powerful representations that model like very generalizable properties of the world right.
[00:10:29] SPEAKER_04: It's useful to have a world simulator to predict like how a cartoon will unfold and likewise it's useful for predicting how you know this conversation might unfold.
[00:10:35] SPEAKER_04: And so that really puts a lot of optimization pressure on Sora to like rock these like core fundamental concepts in a very like data efficient way.
[00:10:43] SPEAKER_04: Did you have to put effort into selecting the data such that it reflected the physical world for example, unimaginable if you have data from the physical world it all abides the laws of physics.
[00:10:53] SPEAKER_03: But you mentioned anime that might not always abide in laws of physics.
[00:10:58] SPEAKER_03: Did you have to be selective or did it naturally find patterns that separate that out that's a really great question.
[00:11:04] SPEAKER_04: We did spend a lot of time you know really thinking about.
[00:11:07] SPEAKER_04: You know what does like the optimal data mix for like a world simulator kind of look like and to your point you know I think in some cases will make decisions that you know maybe are like making the model really fun.
[00:11:18] SPEAKER_04: Like for example people love generating anime but you know do not necessarily like perfectly represents like the laws of physics that are like directly useful for like real world applications.
[00:11:27] SPEAKER_04: So like to put it another way right I think in anime there are certain primitives that are simplified that are actually probably useful for understanding the real world you know people still local moat through scenes for example.
[00:11:37] SPEAKER_04: But like if there's like some crazy dragon that's like flying around that's probably like not so useful for like rocking aerodynamics or something dragon ball Z is more or less how I learned athletics you know there you go.
[00:11:47] SPEAKER_04: The motion and super saying I think it is an interesting question like that I do not know the answer to whether somehow like pre training on simplified representations of like the visual world whether that's like sketches or like some other modality like you know makes you more efficient like rocking these concepts I think it's actually a very interesting scientific question that we need to understand better.
[00:12:09] SPEAKER_04: Do you think we're close to exhausting the number of pre training tokens there are out there do you think video data is just videos just so massive and it's actually one more untapped that's of data.
[00:12:18] SPEAKER_00: Yeah the way I kind of think about this is the intelligence permit a video is much lower than something like text data but if you integrate over all of the data that really exists out there the total is much higher so to directly answer your question you know I think it's hard to imagine ever fully running out of video data there's just like so many ways that it exists in the world.
[00:12:38] SPEAKER_04: That like you know you will be in a regime where you can continue just like add more and more to these pre training runs and continue to see games for like a very long time I suspect.
[00:12:47] SPEAKER_04: You think we'll ever discover new physics is the LLM world you know Einstein thinking the whiteboard is all I'm thinking there's also just that if you develop a perfect simulator and you just simulate physics better matter you you might learn things about the world that we haven't learned yet.
[00:13:02] SPEAKER_00: So I think that this is like bound to happen one day and like you know I think we probably need even like we probably need one more step function change I'd say in like model quality to really get to a point where for example you can think about doing like scientific experiments and models but like you could imagine right one day you have a world simulator that is like generalized so well to the laws of physics that like you don't even need like a wet lab in the real world anymore right you can just like run biological experiments within sort of itself and like again this needs like a lot of work to like really get to a point where you have a system that's robust enough to do this rely on the world.
[00:13:31] SPEAKER_04: So it's robust enough to do this reliably. But you know internally like again we've used so our one is kind of being like the GPT one moment for video it was like really the first time things started working for that modality.
[00:13:41] SPEAKER_04: So we really view as like GPT 3.5 in terms of like it really being able to like kickstart you know the world's creative juices and like really like breakthrough this kind of usability barrier where we're seeing like mass adoption of these models and we're going to need a GPT 4 breakthrough to really get this to the point where this is useful for like sciences as we're seeing now with GPT 5 right like I feel like every day on Twitter.
[00:14:00] SPEAKER_04: I see another like contacts optimization lower bounds get like improved by GPT 5 pro and I think eventually we're going to see the same thing happening for the sciences with so.
[00:14:10] SPEAKER_04: Do you think you need physical world embodiment to get there or do you think a lot of it can be done and effectively in some you know I am like I'm always amazed.
[00:14:18] SPEAKER_04: Every time we like push another like 10x compute into these models like what just like magically falls out of it with like very limited changes and kind of like what we're training on and like the fundamental like approach to what we're doing.
[00:14:32] SPEAKER_04: You know I suspect some amount of like physical agency will certainly help I have a hard time believing it will like make you worse like you know modeling like collisions or like something else.
[00:14:42] SPEAKER_04: Video only is like quite remarkable though and I wouldn't be surprised if it's actually kind of like a G.I. Complete for like building like a general purpose world simulator.
[00:14:50] SPEAKER_04: So for this concept of a general purpose world simulator world model you know where you can do science experiments in that world.
[00:14:58] SPEAKER_03: You think that video is the sole or some combination of video and text are the combined data inputs and you train it on this type of this type of model or is it going to be this have to be based on more structured laws of physics that are understood and laws of biology that are said.
[00:15:20] SPEAKER_04: I think it probably depends a lot on the specific use case you're kind of envisioning for for the world simulator like for example if you just really want to build like an accurate model of how like a basketball game is played.
[00:15:32] SPEAKER_04: I actually think like only video data and like maybe audio as well like kind of sufficient to build that says not of me playing basketball that would be an inaccurate very bad player of basketball.
[00:15:42] SPEAKER_03: You know you actually like Sora's current understanding of how people play basketball constantly maybe at your level.
[00:15:48] SPEAKER_04: Wow.
[00:15:49] SPEAKER_04: It's possible.
[00:15:51] SPEAKER_04: It's possible.
[00:15:52] SPEAKER_04: I like it just this too.
[00:15:54] SPEAKER_04: It's accurate.
[00:15:56] SPEAKER_00: It's better than mine.
[00:15:57] SPEAKER_00: For what's that was like a Sora one situation.
[00:15:59] SPEAKER_04: You're at Sora too.
[00:16:00] SPEAKER_04: We'll toss some hoops.
[00:16:01] SPEAKER_04: Is that what they'll say?
[00:16:02] SPEAKER_04: You know I'm down.
[00:16:03] SPEAKER_04: I'm down.
[00:16:04] SPEAKER_04: Shoot some hoops.
[00:16:05] SPEAKER_04: Thanks.
[00:16:06] SPEAKER_04: Thomas is first David in the five.
[00:16:09] SPEAKER_04: I'm also a true.
[00:16:10] SPEAKER_04: I think it is an interesting question like what are all of the modalities that should be present in like this kind of general purpose system.
[00:16:20] SPEAKER_04: Like certainly you know if you add more modalities I have a hard time believing it will like decrease the intelligence.
[00:16:24] SPEAKER_04: I also think there's an argument to be made that just you know adding more and more does not provide like significant marginal value compared to like you know full mastery of like video and audio for example.
[00:16:35] SPEAKER_04: I think it's an interesting open question.
[00:16:37] SPEAKER_04: I'm not actually sure right now and it's something we need to understand more.
[00:16:40] SPEAKER_04: Yeah.
[00:16:41] So cool.
[00:16:42] SPEAKER_03: So in a minute ago I mentioned Einstein at a whiteboard and obviously that makes me think of you Thomas in your hair.
[00:16:48] SPEAKER_03: Me too.
[00:16:49] SPEAKER_03: No.
[00:16:50] SPEAKER_03: It was.
[00:16:51] SPEAKER_03: It had to come.
[00:16:52] SPEAKER_03: Like if any hair gives a feeling of space time token.
[00:16:57] SPEAKER_03: Definitely.
[00:16:58] SPEAKER_03: Definitely yours.
[00:17:00] SPEAKER_03: At some point you know Bill you're the creator of this revolutionary technology that has changed the way that.
[00:17:08] SPEAKER_03: Yeah video is created at some point you from so I wanted to sort of to say hey all together you said there needs to be an application around this.
[00:17:15] SPEAKER_03: There's some benefit to an application.
[00:17:17] SPEAKER_03: You brought together some of the best product people in the world.
[00:17:20] SPEAKER_03: How did that crew come together at open AI?
[00:17:23] SPEAKER_03: Yeah it's a I mean the story is never as linear as you might think it is.
[00:17:27] SPEAKER_01: So I think that I mean we've had a product team on Sora to get go.
[00:17:31] SPEAKER_01: Rohan was like spearheading that effort in the Sora one days but I think Bill's right when he says it was really like a GPT one kind of moment we're seeing pockets of very interesting things there.
[00:17:41] SPEAKER_01: But the models were not like you know models without sound videos without sound is like a very different kind of environment and so.
[00:17:48] SPEAKER_01: We're working on that surface mostly target on on kind of like a prosumer demographic and separately and we're probably going to more details of all that.
[00:17:57] SPEAKER_01: Separately we're also just kind of exploring different social applications of AI inside of open AI and like what that could look like we had a lot of prototypes most of which were quite bad.
[00:18:08] SPEAKER_01: And when we started to see some of the magic was actually with image gen before it had been released we were playing with it internally in a social context and the social context was really interesting to see that what people were doing is you'd sort of like take an image and then you'd have like a chain of remixes of that image.
[00:18:26] SPEAKER_01: Where I don't know if it's a duck and then the ducks on somebody's head and now everything's upside down and they're smoking a cigarette like just a lot of weird things.
[00:18:37] SPEAKER_01: And we were seeing this we're like this is kind of like a very interesting thing that like you know nobody can really do that with like social media because it's so hard to create something or riff on something it's such a high barrier to entry action maybe you have to get a camera set up and.
[00:18:53] SPEAKER_01: Not just like thinking of the idea is actually a lot of things involved and so we're like okay this is a very magical behavior how can we kind of productize that behavior and we're mostly thinking about away from so are some of the sort of research was still ongoing and there's signs of life but it wasn't like quite very yet and productize form they'll probably had it in his head so much I can see the future but that's fine i'm a little bit more cats can't quite see the future yet so.
[00:19:20] SPEAKER_01: So we're just exploring that I think we tried a few things and at some point the research was really just showing very clear value of even iterative deployment style value of like oh this is something that people really want and so we went into this project like two or three months ago it was very long was like July 4th.
[00:19:40] SPEAKER_02: Wow yeah wow that's when you disappear Thomas that's when it disappeared yeah exactly so and we just kind of locked in like okay we're finally doing it you know that's always a moment.
[00:19:49] SPEAKER_01: And we started with without any magical features just like okay let's just try to get native video environment where you can hear the audio full screen and we did some quick generations things were showing very they're very cool very fun very interesting and because of that image experience we sort of had thought like okay what's the magical here magical thing here is that like barrier to entries very very low for creation.
[00:20:17] SPEAKER_01: Coming from Instagram that's like possible to get people to create on Instagram and that's the most valuable thing that people do.
[00:20:23] SPEAKER_01: So what does that unlock and it's like okay well that remix thing from image and that kind of could still apply here and so it brainstormed all these things about how could remix his work and like what does a remix mean here.
[00:20:36] SPEAKER_01: One of those was this like cameo thing which I think also built at his head but this isn't either.
[00:20:44] SPEAKER_01: But we just were like hacking together things on the product it was just see if this works.
[00:20:49] SPEAKER_01: I didn't think it would work at all but it was on the list and there were a few other things on the list some of them were pretty crazy it was like why didn't you think it would work.
[00:20:59] SPEAKER_01: I am bad at predicting technology.
[00:21:04] SPEAKER_01: It wasn't super clear to me that you could like take a likeness of a person and have that kind of imagined into a video form and whether it would work or not.
[00:21:15] SPEAKER_01: And so we had early prototypes of different things of like people reacting in the video corner or stuff like that but when we saw cameo is just start to work and even playing internally like Ron remember that day or like.
[00:21:27] SPEAKER_01: Yeah feed is entirely cameo yes entirely just went from you know we didn't have that feature once we had that feature product market fit on team all everything we were generating was all of each other inside the main potential.
[00:21:40] SPEAKER_00: I mean yeah that's I think at first.
[00:21:43] SPEAKER_02: We were just like this is hilarious this is amazing and then like a week later we were like this is still all we do.
[00:21:50] SPEAKER_02: Is there something here yeah I mean at first we were actually a little bit like is this good like yeah hey the cameos it's just all cameos now is anyone else care about this is the people care about other people doing stuff and.
[00:22:02] SPEAKER_01: We kind of got to the point where like no this is actually good like it's actually it feels like I'm coming back to see and it really humanized it a lot where like a lot of AI video is just.
[00:22:14] SPEAKER_01: Kind of static scenes that are quite beautiful quite interesting might have extremely complicated things going on but they lose that human touch and it really felt like it was coming back into it so.
[00:22:25] SPEAKER_01: Another learning from image into like image and took off and had viral moments because I think you could put yourselves in these scenes in accessible ways that weren't possible before obviously this massive like put me in a ghibli scene.
[00:22:38] SPEAKER_02: People taking selfies with their idols and stuff like that and so.
[00:22:43] Once you're actually kind of thought about it's like yeah cameo feature makes a lot of sense you put yourself in all these scenes that's way more exciting you and your friends it's novel it's like that's something you do before yeah and then that combined with remixes cameo's kind of remix begin with but then.
[00:22:57] SPEAKER_01: You start to think about okay well now I can riff on Rohan doing something yeah whatever it is I could bill had you wrapped in an action figure package and it was that's been remixed like yeah.
[00:23:07] SPEAKER_01: And insane number of times yeah it's like just very very crazy things to go on and very emergent a lot of stuff that I would have never thought actually how many generations of you guys have been like public we posted at this point I have no idea I know I'm 11000 or so I was like a little less than that wow yeah yeah what is surprised you about the types of users that are really sticking with Sarah who is it really a hit with.
[00:23:32] SPEAKER_00: If you just go to the latest feed which is just like the fire host of everything it's at its space time Thomas mode wild out there but that gives you a pretty good snapshot into like just everything happening I mean I think we have.
[00:23:47] SPEAKER_02: Like almost 7 million generations happening a day so you imagine there's just a ton of information there it's one of my favorite ways to get product feedback it is so diverse the type of stuff people are doing the type of people they'll be like a complete variety of.
[00:24:01] SPEAKER_02: A variety of age some people just doing envisioning themselves in scenes that seem like motivation oriented people just meaning with their friends people cameoing some of like the public figures on the platform that have done cameos so I think the diversity has has surprised me I was kind of expecting this sort of like you know the Twitter AI crowd to like heavily dominate the feed they definitely dominate like the press cycles.
[00:24:26] SPEAKER_02: At least the ones that you know we're most exposed to but in terms of people actually using this it's quite a wide variety and last thing I'll say is a bigger departure from like the sort of niche AI film crowd that exists before which is great early adopters but now you kind of get these I thought it would start there and it felt like it started with just a way wider range of people I think getting to the top of the app store helps with that just get people who are like browsing and see this thing my mother keeps cameoing Thomas.
[00:24:55] SPEAKER_03: All right.
[00:24:56] SPEAKER_03: So we.
[00:24:59] SPEAKER_03: We have 11000.
[00:25:05] SPEAKER_03: Thomas you wrote the original algorithm I'm right for for the Instagram ranking ranking algo there was a lot in the Saratu blog post about how you guys are clearly being very intentional about how you want to do ranking and the algo can you can you talk a little bit about lessons learn from Instagram and how you're approaching it over at
[00:25:24] SPEAKER_00: so yeah I mean there's a lot to cover in that I think that the first thing to think about when we think about these platforms or think about so specifically is the thing I was mentioning before about creation.
[00:25:37] SPEAKER_01: So so her enables basically everybody to be a creator on this platform and that is a very very different environment than something like Instagram where you have this like extreme power law of the people that are creating and the power law just naturally gets more.
[00:25:52] SPEAKER_01: Narrow it's the right word there but more head happy yes so sometimes I feel like I have to defend myself on the Instagram algorithm side we actually did it for I mean we did for a reason it was to solve a problem it wasn't just kind of like a random decision to you know optimize for ads or something like that and the reason we did that was that we noticed it like what was happening on Instagram over time was because it was chronologically ordered every time we did that we did that.
[00:26:21] SPEAKER_01: So I think I'm going to add I'm going to add I'm going to add I'm going to add I'm going to add I'm going to add I'm going to add I'm going to add I'm going to add I'm going to add I'm going to add I'm going to add I'm going to add I'm going to add I'm going to add I'm going to add I'm going to add I'm going to add I'm going to add I'm going to add I'm going to add I'm going to add I'm going to add I'm going to add I'm going to add I'm going to add I'm going to add I'm going to add I'm going to add I'm going to add I'm going to add I'm going to add I'm going to add I'm going to add I'm going to add I'm going to add I'm going to add I'm going to add I'm going to add I'm going to add I'm going to add I'm going to add I'm going to add I'm going
[00:26:51] SPEAKER_01: And so maybe you follow National Geographic or something,
[00:26:54] SPEAKER_01: not the Dunkin National Graphic.
[00:26:56] SPEAKER_01: I love them.
[00:26:56] SPEAKER_01: But if they're posting 20 times a day, your friends not.
[00:27:00] SPEAKER_01: They don't have the same optimization objective.
[00:27:03] SPEAKER_01: They're probably just a picture of their coffee or something.
[00:27:07] SPEAKER_01: And so you'd have 20 natural geo posts,
[00:27:09] SPEAKER_01: and then one picture that you actually
[00:27:10] SPEAKER_01: were they cared about, that you never really scrolled to.
[00:27:13] SPEAKER_01: And there's not too many solutions to that problem
[00:27:15] SPEAKER_01: if you have a guaranteed ordering.
[00:27:18] SPEAKER_01: One of them is that you have to unfollow all these accounts
[00:27:21] SPEAKER_01: that you maybe care about, but care about not as much
[00:27:24] SPEAKER_01: as the person that posts once a day.
[00:27:26] SPEAKER_01: And the other is that you have to permute the feet.
[00:27:30] SPEAKER_01: And so we went with that path.
[00:27:32] SPEAKER_01: We tried it.
[00:27:33] SPEAKER_01: We tested it out internally.
[00:27:34] SPEAKER_01: It was very controversial to do.
[00:27:37] And but I think that you can actually kind of like math this
[00:27:40] SPEAKER_01: out.
[00:27:40] SPEAKER_01: It's like a proof that basically over time
[00:27:43] SPEAKER_01: you're going to have to take control over distribution
[00:27:45] SPEAKER_01: on the platform in order to prevent these kind of issues
[00:27:47] SPEAKER_01: and show people what they actually care about.
[00:27:49] SPEAKER_01: So that's why we did it.
[00:27:50] SPEAKER_01: And it actually showed a lot of value.
[00:27:52] SPEAKER_01: I remember the early tests that won't get into the numbers
[00:27:54] SPEAKER_01: on them, but they were pretty unambiguous actually
[00:27:57] SPEAKER_01: about this was showing more people
[00:27:59] SPEAKER_01: that you cared about.
[00:28:00] SPEAKER_01: It was improving your experience with the platform.
[00:28:01] SPEAKER_01: It actually moved creation, which is unusual.
[00:28:03] SPEAKER_01: It made people create more because they
[00:28:05] SPEAKER_01: were seeing more content that was like accessible to them.
[00:28:09] SPEAKER_01: But I also think that these things
[00:28:10] SPEAKER_01: can go astray over time.
[00:28:12] SPEAKER_01: And I won't say like the Instagram algorithm
[00:28:14] SPEAKER_01: unequivocally bad or unequivocally good.
[00:28:17] SPEAKER_01: But when we started to open up to more unconnected content
[00:28:20] SPEAKER_01: and ad pressure was very strong,
[00:28:24] SPEAKER_01: there's also a natural company incentive
[00:28:27] SPEAKER_01: to optimize for just blind consumption,
[00:28:29] SPEAKER_01: because that's how you make money.
[00:28:30] SPEAKER_01: So maybe cheaper content or maybe just like get people
[00:28:33] SPEAKER_01: to scroll more and more and more and more.
[00:28:35] SPEAKER_01: And that also can encourage people to create less,
[00:28:38] SPEAKER_01: because it's just like a more mindless scrolling mode.
[00:28:41] SPEAKER_03: But you guys have very concretely
[00:28:43] SPEAKER_03: committed to doing things to prevent that kind of behavior.
[00:28:46] SPEAKER_03: We have a lot of mitigations there in place.
[00:28:49] SPEAKER_01: But I think what it really comes down to me
[00:28:53] SPEAKER_01: is just like, what are we trying to do as a platform?
[00:28:56] SPEAKER_01: And I think the magic of this technology
[00:28:57] SPEAKER_01: is that everybody is a creator.
[00:28:59] SPEAKER_01: And so we want this feed to be optimized for you
[00:29:02] SPEAKER_01: to create, to inspire you to create.
[00:29:05] SPEAKER_01: And that can be like sometimes when
[00:29:07] SPEAKER_01: you think of inspiration, you think of like,
[00:29:09] SPEAKER_01: oh, it's this beautiful, crazy scene that's so elegant.
[00:29:12] SPEAKER_01: When I think about that, I think about like a meme culture
[00:29:15] SPEAKER_01: or something really funny or like, well, that's cool.
[00:29:17] SPEAKER_01: I've got a riff on that.
[00:29:18] SPEAKER_01: And I think that's a very different brain mode
[00:29:20] SPEAKER_01: when you're browsing the feed.
[00:29:23] SPEAKER_01: And of course, we have lots of other things in place.
[00:29:25] SPEAKER_01: So I think it starts with an incentive.
[00:29:27] SPEAKER_01: That's our incentive right here is to encourage more creation
[00:29:29] SPEAKER_01: in the ecosystem.
[00:29:31] SPEAKER_01: But there are certainly use cases we want to prevent.
[00:29:34] SPEAKER_01: We're not going to get them right all the time.
[00:29:36] SPEAKER_01: It's very challenging.
[00:29:38] SPEAKER_01: It's a very living system.
[00:29:39] SPEAKER_01: It's also very hard to write a recommender system
[00:29:41] SPEAKER_01: when you have no data.
[00:29:42] SPEAKER_01: And you don't know what to recommend.
[00:29:43] SPEAKER_01: You don't know how the platform's going to evolve.
[00:29:46] SPEAKER_01: But that's basically how I kind of think
[00:29:48] SPEAKER_01: about the incentives of feed.
[00:29:49] SPEAKER_01: And then we have a lot of mitigations in place
[00:29:52] SPEAKER_01: that I think you've been kind of thinking about
[00:29:54] SPEAKER_01: and maybe even more deeply than I have
[00:29:56] SPEAKER_01: about like preventing maybe the extreme cases.
[00:30:00] SPEAKER_01: And so I don't know if you want to talk a little bit.
[00:30:03] SPEAKER_01: Yeah, happy to.
[00:30:04] SPEAKER_02: But one thing before you, I mean, just one thing
[00:30:05] SPEAKER_02: to add is that the stated intent of like optimizing
[00:30:08] SPEAKER_02: for creation is working really well.
[00:30:10] SPEAKER_02: It's almost 100% of people who get past the invite code
[00:30:14] SPEAKER_02: all that on the app end up creating on day one.
[00:30:17] SPEAKER_02: When they come back, it's like 70% of the time
[00:30:19] SPEAKER_02: they come back, they're creating.
[00:30:20] SPEAKER_02: And 30% of people are actually even posting to the feed.
[00:30:22] SPEAKER_02: So not just like generating for themselves
[00:30:24] SPEAKER_02: are actually like posting into the ecosystem.
[00:30:26] SPEAKER_02: Which is an incredible testament to the model, how fun it is,
[00:30:29] SPEAKER_02: and to like how what we're optimizing for is actually
[00:30:31] SPEAKER_02: working pretty well right now.
[00:30:34] SPEAKER_02: But yeah, beyond that, I mean, like one of the top of mind
[00:30:35] SPEAKER_02: things is I think we don't want this just to be
[00:30:38] SPEAKER_02: like a mindless scroll.
[00:30:40] SPEAKER_02: And beyond just optimizing for creation
[00:30:42] SPEAKER_02: and the ranking algorithm, there are things we can do
[00:30:44] SPEAKER_02: like trying to just get you out of this sort of flow state
[00:30:49] of just like consumption and push you into like creative mode.
[00:30:52] SPEAKER_02: I think there's a great article on this called
[00:30:54] SPEAKER_02: like the curvilinear nature of casinos where they design it
[00:30:57] SPEAKER_02: so you never have to make any decisions.
[00:30:58] SPEAKER_02: It's just like you walk in a circle.
[00:31:00] SPEAKER_02: There's no windows, all that kind of stuff.
[00:31:03] SPEAKER_02: We can be very intentional about not doing that.
[00:31:05] SPEAKER_02: And like, you know, whether it's an in-feed unit
[00:31:08] SPEAKER_02: that's like, okay, you just kind of viewed a couple of videos
[00:31:11] SPEAKER_02: in this domain, why don't you try creating something
[00:31:14] SPEAKER_02: or other ways to just kind of like push you out of that.
[00:31:16] SPEAKER_02: We actually have things like that in the product.
[00:31:19] SPEAKER_02: Yeah, there's just some other things coming up.
[00:31:21] SPEAKER_02: Really commend you guys for what you've done to,
[00:31:24] SPEAKER_00: you know, make sure that there's a version of the world
[00:31:26] SPEAKER_00: where video model as world simulator could have just
[00:31:29] SPEAKER_00: ended up with us, you know, each retreating
[00:31:31] SPEAKER_00: into our own computer screen and just becoming addicted
[00:31:33] SPEAKER_00: and just retreating into ourselves.
[00:31:35] SPEAKER_00: And I think the amount to which you're, you know,
[00:31:39] SPEAKER_00: prioritizing the human elements and the social elements,
[00:31:42] SPEAKER_00: I think that the care you put into that really shows.
[00:31:45] I don't think we would have launched like a feed
[00:31:47] SPEAKER_02: of just like a content that wasn't,
[00:31:49] SPEAKER_02: that didn't have a human feel like just,
[00:31:52] SPEAKER_02: I don't think that excited us.
[00:31:53] SPEAKER_02: And as soon as we, we like had the product,
[00:31:55] SPEAKER_02: we had cameo and we had that feeling internally,
[00:31:58] SPEAKER_02: we're like, okay, this is actually a little different than.
[00:32:00] SPEAKER_02: Yeah, I don't think it was totally obvious again.
[00:32:02] SPEAKER_01: It was like a pretty crazy sprint to go through this.
[00:32:06] SPEAKER_01: It wasn't like super obvious to us what would emerge.
[00:32:10] SPEAKER_01: But I think that the idea, it makes sense in retrospect,
[00:32:14] SPEAKER_01: but it was a completely not obvious product decision
[00:32:16] SPEAKER_01: that cameos would be the thing.
[00:32:17] SPEAKER_01: Yeah.
[00:32:18] SPEAKER_01: Where it's like, of course,
[00:32:19] SPEAKER_01: you just want to see your friends doing cool things.
[00:32:21] SPEAKER_01: So that makes sense.
[00:32:23] SPEAKER_01: But I was never actually that afraid of competitive pressure
[00:32:26] SPEAKER_01: in that crazy product phase because I was like,
[00:32:29] SPEAKER_01: we sort of had these all these non trivial decisions
[00:32:32] SPEAKER_01: that are obvious in retrospect,
[00:32:33] SPEAKER_01: but we're not obvious at the time
[00:32:34] SPEAKER_01: that we're sort of building on top of each other.
[00:32:36] SPEAKER_01: It's like, okay, cameos.
[00:32:37] SPEAKER_01: Well, there's also a version of cameo
[00:32:39] SPEAKER_01: where you have a crazy flow that's just for you.
[00:32:41] SPEAKER_01: And it's a one player mode cameo
[00:32:43] SPEAKER_01: and you like go through this onboarding flow
[00:32:44] SPEAKER_01: and do your stuff.
[00:32:46] But we were already seeing these interesting dynamics
[00:32:48] SPEAKER_01: where it's like, well, I could take a long time.
[00:32:49] In my video, that's crazy.
[00:32:51] SPEAKER_01: And then we can have an RE-made.
[00:32:52] SPEAKER_01: Like, I'm gonna have an anime fight, doesn't matter.
[00:32:56] SPEAKER_01: And I was like, okay, so that's actually the humano.
[00:32:59] That's the magic of this.
[00:33:00] SPEAKER_01: It's actually strangely more social
[00:33:02] SPEAKER_01: than a lot of social networks,
[00:33:04] SPEAKER_01: even though it's all AI generated content.
[00:33:06] SPEAKER_01: So very unintuitive.
[00:33:07] SPEAKER_01: Totally.
[00:33:09] Is it fine tunes version of Sora 2,
[00:33:11] SPEAKER_00: or is it like a separate model
[00:33:13] SPEAKER_00: from what's available over the API, or is it the same?
[00:33:15] Between the app and products,
[00:33:17] so we are currently exposing like the models
[00:33:20] SPEAKER_04: in the same state across API and the app.
[00:33:22] SPEAKER_04: Okay, really interesting.
[00:33:24] SPEAKER_00: What are you saying people do on the API side?
[00:33:26] SPEAKER_00: And is it different from the types of things
[00:33:28] SPEAKER_00: people are doing on the consumer app?
[00:33:30] SPEAKER_00: The motivation behind even launching an API
[00:33:32] SPEAKER_02: is just like the support of these long tail use cases.
[00:33:35] SPEAKER_02: Like we have this vision of enabling, you know,
[00:33:38] SPEAKER_02: chat, GPT scale, level, consumer audience with this tech.
[00:33:42] SPEAKER_02: But there's tons of very niche things out there.
[00:33:44] SPEAKER_02: You can imagine people who are much, you know,
[00:33:46] SPEAKER_02: with Sora 1, we went out and talked in a lot of these studios.
[00:33:49] SPEAKER_02: What we heard from them is that they wanna integrate this
[00:33:51] SPEAKER_02: in this specific part of their stack in this specific way.
[00:33:55] SPEAKER_02: And we'd love to support all these long tail use cases,
[00:33:57] SPEAKER_02: but we don't wanna build a thousand different kind
[00:33:59] SPEAKER_02: of interfaces for this stuff.
[00:34:00] SPEAKER_02: So that's the kind of stuff we're excited to see with the API.
[00:34:03] SPEAKER_02: So far it's been, you know,
[00:34:05] SPEAKER_02: it's been kind of those kind of like a little bit more
[00:34:07] SPEAKER_02: of a niche company not trying to build like a first party
[00:34:10] SPEAKER_02: social app, but maybe, you know, has some either
[00:34:14] SPEAKER_02: filmmaking kind of audience or kind of people
[00:34:17] SPEAKER_02: they're supporting or even just like,
[00:34:19] SPEAKER_02: we've seen some like people trying to, you know,
[00:34:22] SPEAKER_02: I think there was like a some company making.
[00:34:26] SPEAKER_02: They were doing something with CAD where they were like,
[00:34:27] SPEAKER_02: using Sora.
[00:34:28] SPEAKER_02: Yeah, yeah, yeah, yeah.
[00:34:29] SPEAKER_02: Oh, that's cool.
[00:34:31] SPEAKER_02: There's cool use case out there.
[00:34:32] SPEAKER_02: I think we're still getting a sense of what they are.
[00:34:34] SPEAKER_02: Yeah, I think there's a lot that can be done with these things.
[00:34:37] SPEAKER_01: I think about gaming all the time, just basically
[00:34:39] SPEAKER_01: the background and you know, AI and gaming
[00:34:41] SPEAKER_01: is always a very controversial subject,
[00:34:43] SPEAKER_01: but it's very clear that there's a place and there's a role.
[00:34:46] SPEAKER_01: Maybe it doesn't have to interrupt the creative process.
[00:34:49] SPEAKER_01: It's gonna enhance it.
[00:34:49] SPEAKER_01: And I'm pretty excited to see some of those use cases emerge.
[00:34:53] Do you think the video models are good enough now
[00:34:55] SPEAKER_00: for people to be able to build video games on top of the API
[00:34:58] SPEAKER_00: or do you think we're still not a rev for two away?
[00:35:01] I have my own take on this.
[00:35:03] SPEAKER_01: I was gonna say never bet against the ways people
[00:35:04] SPEAKER_02: can be creative with technology to build.
[00:35:06] SPEAKER_02: Like someone will be able to build a game
[00:35:09] SPEAKER_02: and maybe it has built a game already.
[00:35:10] SPEAKER_02: Will it feel, look and feel like a, you know,
[00:35:13] SPEAKER_02: obviously there's latency with this model.
[00:35:15] SPEAKER_02: So you'd have to do all sorts of crazy stuff to get around that.
[00:35:17] SPEAKER_02: But like I think that your mind immediately goes to like
[00:35:20] SPEAKER_01: kind of the obvious sort of things that you would do in gaming
[00:35:22] SPEAKER_01: and we've seen some of that sort of stuff,
[00:35:25] SPEAKER_01: certainly in research blogs and that kind of thing.
[00:35:27] SPEAKER_01: My mind often goes to like,
[00:35:28] SPEAKER_01: okay, this is like a creative tool that's available
[00:35:30] SPEAKER_01: that different.
[00:35:32] SPEAKER_01: And the types of games that really excite me there,
[00:35:34] SPEAKER_01: I'll just go off on one, which is this,
[00:35:36] SPEAKER_01: like there's a game called Infinite Craft,
[00:35:38] SPEAKER_01: which is the world's simplest game, it's a web game
[00:35:40] SPEAKER_01: where you just take elements,
[00:35:42] SPEAKER_01: it's like fire or water earth,
[00:35:43] SPEAKER_01: you have like four elements to start
[00:35:45] SPEAKER_01: and you just drag them in a cool lot of this game.
[00:35:48] SPEAKER_04: It combines into something new.
[00:35:49] SPEAKER_01: And the thing it combines with is like a, it's LLM base.
[00:35:52] SPEAKER_01: So it's like fire and earth might be a volcano.
[00:35:57] SPEAKER_01: And then volcano plus water might be,
[00:36:00] SPEAKER_01: not a water volcano or Godzilla or something like that.
[00:36:03] SPEAKER_01: You always end up in Godzilla for some reason.
[00:36:07] SPEAKER_01: That's a game that like, it's like,
[00:36:08] SPEAKER_01: oh, it kind of makes sense where it's like,
[00:36:10] SPEAKER_01: yeah, you don't really need a crafting tree.
[00:36:12] SPEAKER_01: The LLM can derive this crafting tree
[00:36:14] SPEAKER_01: and it's a process of discovery.
[00:36:16] SPEAKER_01: And so I think there's a lot of untapped stuff
[00:36:19] SPEAKER_01: in that space where again,
[00:36:21] SPEAKER_01: I like the idea of a process to discovery.
[00:36:23] SPEAKER_01: In fact, my full, full, full,
[00:36:26] SPEAKER_01: philosophical view on LLMs and video models
[00:36:28] SPEAKER_01: to some extent is that it is a process of discovery.
[00:36:31] SPEAKER_01: These are all in the weights.
[00:36:32] SPEAKER_01: You're just unlocking it with like a secret code,
[00:36:34] SPEAKER_01: which is your prompt.
[00:36:35] SPEAKER_01: And I love that.
[00:36:37] SPEAKER_01: That is, that is very magical.
[00:36:38] SPEAKER_01: That was always in gaming.
[00:36:40] SPEAKER_01: That was the thing that like excited me the most
[00:36:41] SPEAKER_01: was discovering something new,
[00:36:43] SPEAKER_01: especially if it was a true discovery.
[00:36:45] SPEAKER_01: It wasn't put there by somebody else.
[00:36:47] SPEAKER_01: Maybe they just enabled the mechanics around it.
[00:36:49] SPEAKER_01: So I think there's a huge opportunity in that space
[00:36:52] SPEAKER_01: of gaming.
[00:36:54] SPEAKER_01: When you think about games and just the different thing
[00:36:56] SPEAKER_01: and like embrace this technology in a very different way.
[00:36:58] SPEAKER_01: It reminds me of how some of the early issues cases
[00:37:01] SPEAKER_00: for GPT-3 were the kind of these text games.
[00:37:03] SPEAKER_00: Yeah.
[00:37:04] SPEAKER_00: So it's different from how you think of a, you know,
[00:37:07] SPEAKER_00: like a playable video game,
[00:37:08] SPEAKER_00: but actually a lot of these mechanics are very game like.
[00:37:10] SPEAKER_00: Exactly. Yeah.
[00:37:11] SPEAKER_01: I think there's still constraints.
[00:37:13] SPEAKER_01: And I think that's going to be like the mechanism design.
[00:37:16] SPEAKER_01: That's still very human.
[00:37:18] SPEAKER_01: Like a lot of the early games with GPT-3,
[00:37:20] SPEAKER_01: they're kind of like, yeah, it was fun for a minute
[00:37:21] SPEAKER_01: and then it kind of went off the rails.
[00:37:22] SPEAKER_01: You're like, I don't really know what I'm doing anymore.
[00:37:25] SPEAKER_01: But again, like this is sort of in some way,
[00:37:28] SPEAKER_01: so our feels like a little bit of that
[00:37:29] SPEAKER_01: where it's got a little bit of gaming DNA inside of it
[00:37:32] SPEAKER_01: where it feels very fun and different and exploratory.
[00:37:35] SPEAKER_01: So I like things like that.
[00:37:37] SPEAKER_01: And I think there's going to be more use cases
[00:37:38] SPEAKER_01: that we can't even think of as too creative.
[00:37:40] SPEAKER_01: What are you guys seeing on the creative filmmaking side?
[00:37:43] SPEAKER_00: Like is that an important target market?
[00:37:45] SPEAKER_00: Do you want to do an empowered the long tail
[00:37:46] SPEAKER_00: or do you want to empower the head,
[00:37:48] SPEAKER_00: so to speak, of the creative market?
[00:37:50] It's a really good question.
[00:37:51] SPEAKER_04: You know, we've benefited a lot from creatives
[00:37:56] SPEAKER_04: who are really willing to like go all in on,
[00:37:58] SPEAKER_04: you know, even like the early technology,
[00:38:00] SPEAKER_04: like Dolly-1, Dolly-2,
[00:38:02] SPEAKER_04: and really like help steer us along the path.
[00:38:05] SPEAKER_04: And like I think it's important that we continue
[00:38:08] SPEAKER_04: to build things for those folks
[00:38:11] SPEAKER_04: and we are working on some things
[00:38:12] SPEAKER_04: that are like more targeted towards like creative power users
[00:38:14] SPEAKER_04: long-term.
[00:38:15] SPEAKER_04: At the same time, you know, I do think like AI
[00:38:17] SPEAKER_04: is a very democratizing tool right at its best.
[00:38:19] SPEAKER_04: And so what's kind of beautiful about the sort of platform
[00:38:23] SPEAKER_04: in general, right, is whenever someone kind of strikes
[00:38:25] SPEAKER_04: gold, right, you see one of these like beautiful anime prompts
[00:38:28] SPEAKER_04: that like goes to like the very top of the feed
[00:38:31] SPEAKER_04: for everyone.
[00:38:32] SPEAKER_04: Like anybody can go and remix that, right?
[00:38:35] SPEAKER_04: Everyone has the power to like build on top of that
[00:38:36] SPEAKER_04: and like learn from all of these people who come in
[00:38:39] SPEAKER_04: with this like incredible knowledge about
[00:38:41] SPEAKER_04: how to like really get the most out of these tools.
[00:38:44] SPEAKER_04: And so I am really excited just to see the net creativity
[00:38:47] SPEAKER_04: of humanity just increase as a result of this.
[00:38:49] SPEAKER_04: But I think a big part of that right,
[00:38:51] SPEAKER_04: is continuing to empower people who are always at the frontier,
[00:38:54] SPEAKER_04: which are these like more pro oriented like creator type folks.
[00:38:58] SPEAKER_04: And so we want to keep investing in them as well.
[00:39:00] SPEAKER_04: We've nerded out for a while, like almost a couple years now
[00:39:04] SPEAKER_03: about that vision of feature film.
[00:39:07] SPEAKER_03: Yeah.
[00:39:07] SPEAKER_03: Link content.
[00:39:08] SPEAKER_03: Like yes, you have these amazing cameos and shorter content.
[00:39:12] SPEAKER_03: But at some point, the individual creator has been something
[00:39:15] SPEAKER_03: that you've been excited about for a very long time.
[00:39:17] SPEAKER_03: Yeah.
[00:39:18] SPEAKER_03: When do we get there?
[00:39:19] SPEAKER_03: You know, is there a point where we have a feature film
[00:39:21] SPEAKER_03: that is created on Sora 2?
[00:39:23] SPEAKER_03: Yeah.
[00:39:24] SPEAKER_03: And how do we consume it?
[00:39:26] SPEAKER_03: Is it in the Sora app?
[00:39:27] SPEAKER_03: Is it posted somewhere else online?
[00:39:29] SPEAKER_03: Do you go to movie theater and watch it?
[00:39:31] SPEAKER_03: Yeah, it's a great question.
[00:39:33] SPEAKER_04: I mean, I think this will happen in stages to some extent.
[00:39:35] SPEAKER_04: So like if you guys watch the right the launch video,
[00:39:38] SPEAKER_04: I mean, that was maybe like Daniel Frieden
[00:39:39] SPEAKER_04: who's on the Sora team.
[00:39:41] SPEAKER_04: And he already with these tools, right,
[00:39:43] SPEAKER_04: is able to pump out these like incredibly compelling
[00:39:46] SPEAKER_04: short stories within like days at most.
[00:39:49] SPEAKER_04: I mean, he literally made that like all by himself
[00:39:51] SPEAKER_04: in almost no time.
[00:39:52] SPEAKER_04: And he's been like continuing to like put new ones out there
[00:39:55] SPEAKER_04: on like the OpenAI Twitter sense.
[00:39:57] SPEAKER_04: So clearly this is like massively compressing the latency
[00:40:00] SPEAKER_04: that's associated with like filmmaking.
[00:40:03] SPEAKER_04: I think to get to the point where like really
[00:40:06] SPEAKER_04: anybody can do this, right?
[00:40:07] SPEAKER_04: Like any kid in their home can just like fire up the app
[00:40:11] or sort of calm or something and go and make this.
[00:40:13] SPEAKER_04: You know, it's really like an economics problem
[00:40:15] SPEAKER_04: of like the video models video is the most intensive,
[00:40:18] SPEAKER_04: compute intensive modality to work with.
[00:40:20] SPEAKER_04: It's extremely expensive.
[00:40:21] SPEAKER_04: And you know, we're making good progress on the research team
[00:40:24] SPEAKER_04: like really continuing to figure out ways
[00:40:26] SPEAKER_04: to make this affordable for everyone long term.
[00:40:27] SPEAKER_04: Like right now for example, if the Sora app is like totally free,
[00:40:31] SPEAKER_04: in the future there will probably be ways
[00:40:32] SPEAKER_04: where people can pay money to get more access to the models
[00:40:36] SPEAKER_04: just because that's the only way we can really scale this
[00:40:38] SPEAKER_04: further.
[00:40:39] SPEAKER_04: But you know, I think we are not far off from this world
[00:40:42] SPEAKER_04: where anybody can really like have the tools
[00:40:45] SPEAKER_04: to make amazing content.
[00:40:46] SPEAKER_04: You know, I think there's gonna be like a lot of bad movies
[00:40:48] SPEAKER_04: like it created by this.
[00:40:48] SPEAKER_04: But like wise, you know, there's probably
[00:40:50] SPEAKER_04: the next great film director who is just kind of like
[00:40:53] SPEAKER_04: sitting, you know, in their parents' house
[00:40:55] SPEAKER_04: like still in high school or something
[00:40:57] SPEAKER_04: and just like has not had the investment
[00:40:59] SPEAKER_04: or the tools to be able to like really see their vision
[00:41:01] SPEAKER_04: come to life and we're gonna find like
[00:41:02] SPEAKER_04: absolutely like amazing things from like giving this technology.
[00:41:05] SPEAKER_04: It's like the whole world.
[00:41:06] I'm looking forward to the feature film length
[00:41:08] SPEAKER_00: Constantine's Greek Odyssey.
[00:41:09] SPEAKER_00: Yeah, me too.
[00:41:10] SPEAKER_00: Coming to the theaters near you.
[00:41:12] SPEAKER_00: We're all in it together.
[00:41:13] SPEAKER_03: Yeah, like different characters.
[00:41:15] SPEAKER_03: I play the psych box.
[00:41:16] SPEAKER_03: It's a good one.
[00:41:18] SPEAKER_03: I think just to touch on that one more thing
[00:41:21] SPEAKER_01: that something I've learned from recommender systems
[00:41:23] SPEAKER_01: over and over again is that like oftentimes
[00:41:26] SPEAKER_01: so the tools getting more people more creative
[00:41:28] SPEAKER_01: is gonna be a huge unlock for just, you know,
[00:41:32] SPEAKER_01: making people more creative in general
[00:41:33] SPEAKER_01: and because you don't need this access to this like
[00:41:35] SPEAKER_01: filmmaking equipment, all that sort of stuff.
[00:41:38] SPEAKER_01: But we do consistently see that things content
[00:41:40] SPEAKER_01: is like also a social phenomenon in a way
[00:41:43] SPEAKER_01: in like movies and all that.
[00:41:45] SPEAKER_01: All everything you see out there is kind of
[00:41:47] SPEAKER_01: a bit of a social phenomenon.
[00:41:49] SPEAKER_01: In addition to the actual content itself.
[00:41:52] SPEAKER_01: And so I think we're gonna enter a very interesting world
[00:41:54] SPEAKER_01: where there's so many people creating
[00:41:57] SPEAKER_01: and so much content out there that even the idea
[00:42:00] SPEAKER_01: that people aren't paying attention to
[00:42:01] SPEAKER_01: and watching it is gonna become more and more important.
[00:42:04] SPEAKER_01: And I think that's actually gonna make
[00:42:06] SPEAKER_01: the quality of content just to kind of elevate
[00:42:08] SPEAKER_01: because there's this anybody can create
[00:42:11] SPEAKER_01: and actually it's gonna be the consumption
[00:42:12] SPEAKER_01: that's gonna be quite limited
[00:42:14] SPEAKER_01: which is very different than the world we live in today.
[00:42:16] SPEAKER_01: You guys are very thoughtful and intentional
[00:42:18] SPEAKER_00: about how you treat the IP holders.
[00:42:20] SPEAKER_00: Can you say it were them that?
[00:42:21] You know, we've been in close partnership
[00:42:24] SPEAKER_04: with like a bunch of folks across the industry
[00:42:26] SPEAKER_04: and like really trying to like both show them
[00:42:30] SPEAKER_04: kind of this like new technology, right?
[00:42:32] SPEAKER_04: That is actually like a huge value proposition
[00:42:35] SPEAKER_04: for rights holders across the board, right?
[00:42:36] SPEAKER_04: And like we're hearing so much excitement
[00:42:37] SPEAKER_04: from the folks we're talking with.
[00:42:39] SPEAKER_04: Like they really see this as being like,
[00:42:41] SPEAKER_04: a new frontier for again, like, you know,
[00:42:44] SPEAKER_04: every kid in the world having the ability
[00:42:46] SPEAKER_04: to like go and like use like some of this beloved IP
[00:42:49] SPEAKER_04: and like really like bring it into their lives in a way
[00:42:51] SPEAKER_04: that feels much more personal
[00:42:53] SPEAKER_04: and custom than what's been possible before.
[00:42:55] SPEAKER_04: At the same time, you know,
[00:42:56] SPEAKER_04: we really wanna make sure that we're doing this
[00:42:58] SPEAKER_04: like in the right way.
[00:42:59] SPEAKER_04: So we've been like really trying to take feedback
[00:43:01] SPEAKER_04: and like really steer our road map in a way
[00:43:04] SPEAKER_04: where we know that, you know,
[00:43:05] SPEAKER_04: both users are gonna have an awesome experience
[00:43:07] SPEAKER_04: getting to use this IP,
[00:43:08] SPEAKER_04: but also the rights holders are going to get,
[00:43:10] SPEAKER_04: you know, properly monetize and rewarded.
[00:43:13] SPEAKER_04: In a way that, you know, everyone wins basically.
[00:43:15] SPEAKER_04: So we're right now actively working on trying to scope
[00:43:17] SPEAKER_04: out the exact details about like how we're going to,
[00:43:20] SPEAKER_04: you know, for example, make it.
[00:43:21] SPEAKER_04: So if you wanna cameo your favorite character
[00:43:24] SPEAKER_04: from some like beloved film or something,
[00:43:26] SPEAKER_04: you can do that in a way where you have access to it,
[00:43:29] SPEAKER_04: but like monetization will flow back to the right holder,
[00:43:32] SPEAKER_04: right?
[00:43:33] SPEAKER_04: So really trying to figure out this kind of like new economy
[00:43:35] SPEAKER_04: for creators.
[00:43:36] SPEAKER_04: We kind of just have to create this from scratch right now.
[00:43:38] SPEAKER_04: There's a lot of deep questions
[00:43:40] SPEAKER_04: about how to do this the right way.
[00:43:41] SPEAKER_04: And, you know, as with everything with this app,
[00:43:44] SPEAKER_04: we come into it with like an open mind
[00:43:45] SPEAKER_04: and we hear feedback and we iterate quickly.
[00:43:47] SPEAKER_04: You know, we're not sure where this is gonna totally converge,
[00:43:50] SPEAKER_04: but we're working closely with people to figure it out.
[00:43:52] Really cool.
[00:43:53] SPEAKER_00: What's ahead?
[00:43:56] That's, yeah, I think I mean, one has.
[00:43:59] SPEAKER_04: Sorry, what?
[00:44:00] SPEAKER_04: Put it in the camera, you know, you can't do it.
[00:44:02] SPEAKER_04: There's a lot of fun.
[00:44:03] SPEAKER_04: Is that one of the most demanded features?
[00:44:04] SPEAKER_00: Great, great.
[00:44:05] SPEAKER_00: For me it is.
[00:44:06] SPEAKER_01: Girls demanding.
[00:44:07] SPEAKER_01: I mean, actually, we were just talking about
[00:44:10] SPEAKER_03: curing diseases and world models.
[00:44:11] SPEAKER_03: And now we're to the future.
[00:44:13] SPEAKER_03: That's it.
[00:44:14] SPEAKER_03: This is something.
[00:44:16] SPEAKER_01: No, it's actually, so that's definitely true.
[00:44:17] SPEAKER_01: We've committed to that.
[00:44:18] SPEAKER_01: It's coming.
[00:44:19] SPEAKER_01: Oh, yeah, my problem.
[00:44:21] SPEAKER_01: The, we actually had Bill Stogg as like,
[00:44:25] SPEAKER_01: when we were playing around with this rocket.
[00:44:27] SPEAKER_04: The gooddest boy.
[00:44:28] SPEAKER_04: Yeah.
[00:44:28] SPEAKER_04: And actually was very, very cool to actually feature a pet.
[00:44:32] SPEAKER_01: You can imagine where that goes.
[00:44:33] SPEAKER_01: It doesn't have to necessarily be a pet.
[00:44:36] SPEAKER_01: It could be anything clock or whatever you have.
[00:44:39] SPEAKER_01: Clock.
[00:44:40] SPEAKER_01: Well, yeah.
[00:44:42] SPEAKER_01: Do you have a special clock?
[00:44:43] SPEAKER_01: Actually, it's redess.
[00:44:45] SPEAKER_01: I didn't think he could be so compelling until Thomas
[00:44:47] SPEAKER_04: showed me this clock.
[00:44:47] SPEAKER_04: Yeah, it's like a sentient clock.
[00:44:49] SPEAKER_04: Well, it's like based on like a real clock.
[00:44:51] SPEAKER_04: Yeah, I had a clock, my father.
[00:44:53] SPEAKER_01: My father was a technology person for a while.
[00:44:56] SPEAKER_01: It's company Baratas gave him a clock for his like,
[00:44:59] SPEAKER_01: whatever, it's anniversary.
[00:45:00] SPEAKER_01: Anyway, so I have it on my table somewhere.
[00:45:05] SPEAKER_01: And there's this old Simpson's episode
[00:45:08] SPEAKER_01: when they talk about a walking clock.
[00:45:09] SPEAKER_01: And for some reason that's just been an earworm
[00:45:11] SPEAKER_01: in my head for the last 30 years.
[00:45:13] SPEAKER_01: And so I always, it's like, they're telling some joke.
[00:45:16] SPEAKER_01: And it's like, is it a walking clock?
[00:45:18] SPEAKER_01: It's a walking clock.
[00:45:19] SPEAKER_01: It's like walking clock.
[00:45:20] SPEAKER_01: And then it's like, no, man, it's my dog.
[00:45:21] SPEAKER_01: And so I connected it in my brain where I was like,
[00:45:23] SPEAKER_01: okay, rocket, walking clock.
[00:45:26] SPEAKER_01: And then so I tried it.
[00:45:27] SPEAKER_01: Thomas is great.
[00:45:28] SPEAKER_01: This is what AI enables.
[00:45:31] SPEAKER_01: Yeah.
[00:45:32] SPEAKER_01: Yeah, so connected to my brain and we've been playing
[00:45:35] SPEAKER_01: around with this just to see if we can get it to work.
[00:45:37] SPEAKER_01: And whether there's something special there,
[00:45:39] SPEAKER_01: which is part of the fun of being on the sword team
[00:45:41] SPEAKER_01: is you get to play with his emergent crazy technology.
[00:45:43] SPEAKER_01: And like, maybe it does something you wouldn't even
[00:45:46] SPEAKER_01: expect it.
[00:45:47] SPEAKER_01: So I recorded it to second video of my clock.
[00:45:50] SPEAKER_01: And then I gave it some cameo instructions.
[00:45:53] SPEAKER_01: And I said, you're just a walking clock.
[00:45:54] SPEAKER_01: You're a walk clock.
[00:45:55] SPEAKER_01: You talk like you talk or character.
[00:45:57] SPEAKER_01: And then I generated my first video.
[00:45:59] SPEAKER_01: And it was insane.
[00:46:01] SPEAKER_01: It was crazy.
[00:46:02] SPEAKER_01: It was a walk clock.
[00:46:04] SPEAKER_01: And then I had one where it was stocking to Bill.
[00:46:07] SPEAKER_01: And Bill was like, I didn't think it would ever land.
[00:46:09] SPEAKER_01: The pet cameo feature.
[00:46:11] SPEAKER_01: And walking clocks like, you're am, you know, I just landed.
[00:46:15] SPEAKER_01: So it's coming.
[00:46:17] SPEAKER_01: Solid general means.
[00:46:18] SPEAKER_04: Talk about immersion IP.
[00:46:19] SPEAKER_00: Yeah.
[00:46:20] SPEAKER_00: The standing spokey mind when you can have a walking clock.
[00:46:23] SPEAKER_00: What's the greatest thing?
[00:46:24] SPEAKER_02: One thing that in terms of the feature,
[00:46:25] SPEAKER_02: I think I'm the feature film question sometime,
[00:46:27] SPEAKER_02: something I think about all the time is like, what,
[00:46:30] SPEAKER_02: you know, what would that actually look like?
[00:46:31] SPEAKER_02: I think my, I mean, caveat.
[00:46:33] SPEAKER_02: Bill is the only one who's good at predicting the future here.
[00:46:37] SPEAKER_02: But my sense is that the, you know, as we get to longer forms,
[00:46:42] SPEAKER_02: what are equivalent of a feature film will look
[00:46:45] SPEAKER_02: and feel very, very different from what a feature film is today?
[00:46:48] SPEAKER_02: I don't know exactly what that looks like,
[00:46:49] SPEAKER_02: but I think on the subject of creators
[00:46:53] SPEAKER_02: and what's coming in the world, I think,
[00:46:55] SPEAKER_02: a new medium and a new class of creators.
[00:46:57] SPEAKER_02: New class could include a lot of existing creators
[00:47:00] SPEAKER_02: and support existing sort of mediums and stuff like that.
[00:47:03] SPEAKER_02: But I think we're just in the early innings of what I imagine
[00:47:07] SPEAKER_02: will be the next film industry rather than thinking about this
[00:47:10] SPEAKER_02: being a feature film, but I think there'll be something.
[00:47:12] SPEAKER_02: There's some anecdote.
[00:47:14] SPEAKER_02: I hope this is true because I say it all the time.
[00:47:16] SPEAKER_02: But apparently when the recording camera, like, you know,
[00:47:19] SPEAKER_02: hit the world, the first thing people did was record plays.
[00:47:23] This is like the least interesting thing you could do
[00:47:24] SPEAKER_02: with the recording camera.
[00:47:25] SPEAKER_02: It's like, what's the big idea?
[00:47:26] SPEAKER_02: Oh, we, people don't have to travel around acting.
[00:47:28] SPEAKER_02: We can just film them and distribute it.
[00:47:30] SPEAKER_02: And then someone was like, wait a minute.
[00:47:33] SPEAKER_02: We can make a film and film in all these different areas.
[00:47:35] SPEAKER_02: And I feel like we haven't, we're in like the first inning
[00:47:38] SPEAKER_02: of so many different sort of things
[00:47:40] SPEAKER_02: that people will do with this technology,
[00:47:41] SPEAKER_02: especially as the constraints change with latency
[00:47:44] SPEAKER_02: and length and all that kind of stuff.
[00:47:46] So cool and fun film history nerd fact is one of the original videos,
[00:47:52] SPEAKER_03: and we should check this as well.
[00:47:54] SPEAKER_03: But I think the original video was made just down the peninsula
[00:47:58] SPEAKER_03: to settle a bet on if a horse, when it galloped
[00:48:02] SPEAKER_03: all four legs, it left the ground.
[00:48:05] SPEAKER_03: And I could see a world where you have new,
[00:48:07] SPEAKER_03: that is an example of new scientific discovery.
[00:48:10] People didn't actually have an answer to that.
[00:48:12] SPEAKER_03: Now that you have a new simulation format,
[00:48:15] SPEAKER_03: what are we gonna be able to discover in that?
[00:48:18] It will be crazy.
[00:48:19] SPEAKER_04: And I think one, one broader point here is,
[00:48:22] SPEAKER_04: you know, this app right now feels very familiar
[00:48:24] SPEAKER_04: in a lot of ways, right?
[00:48:25] SPEAKER_04: It's like a social media network at its core.
[00:48:28] SPEAKER_04: But fundamentally like the way that like we really view it
[00:48:31] SPEAKER_04: internally, right, is with cameo,
[00:48:34] SPEAKER_04: we've kind of introduced the lowest bandwidth way
[00:48:37] to give information to Sora about yourself, right?
[00:48:41] SPEAKER_04: Aspects about your appearance, about your voice, et cetera.
[00:48:44] SPEAKER_04: You can imagine over time that like that bandwidth
[00:48:47] SPEAKER_04: will greatly increase, right?
[00:48:48] SPEAKER_04: So the model deeply understands your relationships
[00:48:51] SPEAKER_04: with other people, it understands, you know,
[00:48:53] SPEAKER_04: more than just how you look on any given day.
[00:48:56] SPEAKER_04: That's, you know, seeing your full,
[00:48:57] SPEAKER_04: like how you've grown up,
[00:48:59] SPEAKER_04: all of these details about yourself
[00:49:01] SPEAKER_04: and will really be able to almost function
[00:49:03] SPEAKER_04: as like a digital clone, right?
[00:49:03] SPEAKER_04: So like there's really a world where the Sora app
[00:49:05] SPEAKER_04: almost becomes this like mini alternate reality
[00:49:07] SPEAKER_04: that's running on your phone.
[00:49:08] SPEAKER_04: You have versions of yourself that can go off
[00:49:11] SPEAKER_04: and interact with other people's digital clones.
[00:49:13] SPEAKER_04: You can do knowledge work.
[00:49:14] SPEAKER_04: It's not just for entertainment, right?
[00:49:16] SPEAKER_04: And it really involves more into a platform,
[00:49:19] SPEAKER_04: which is really aligned with kind of where these like
[00:49:20] SPEAKER_04: world simulation capabilities are headed long term.
[00:49:23] SPEAKER_04: And I think when that happens,
[00:49:24] SPEAKER_04: we kind of immersion things we will see are crazy.
[00:49:26] SPEAKER_04: And you know, for opening across the board,
[00:49:29] it's really important that we kind of like
[00:49:30] SPEAKER_04: iteratively deploy technology in a way
[00:49:32] SPEAKER_04: where we're not just like dropping bombshells on the world
[00:49:34] SPEAKER_04: when there's like some big research breakthrough
[00:49:36] SPEAKER_04: we want to co-evolve society with the technology.
[00:49:39] SPEAKER_04: And so that's why we really thought it was important
[00:49:41] SPEAKER_04: to like do this now and like do it in a way where, you know,
[00:49:43] SPEAKER_04: we've hit this again, this kind of like GPT 3.5 moment
[00:49:45] SPEAKER_04: for video.
[00:49:46] SPEAKER_04: Let's make sure the world is kind of aware
[00:49:48] SPEAKER_04: of what's possible now.
[00:49:49] SPEAKER_04: And also, you know, start to get society comfortable
[00:49:52] SPEAKER_04: and like figuring out the rules of the road
[00:49:55] SPEAKER_04: for this kind of like longer term vision,
[00:49:57] SPEAKER_04: for where again, there are just copies of yourself
[00:50:00] SPEAKER_04: running around in Sora and the ether,
[00:50:02] SPEAKER_04: like just doing tasks and like reporting back
[00:50:04] SPEAKER_04: in the physical world,
[00:50:05] SPEAKER_04: because that is where we are headed long term.
[00:50:07] SPEAKER_04: It's so cool.
[00:50:07] SPEAKER_04: So you're building the multiverse?
[00:50:09] SPEAKER_04: Actually kind of, yeah.
[00:50:10] SPEAKER_04: Okay, well can continue to me go and find my soul mate
[00:50:13] SPEAKER_00: somewhere in there?
[00:50:14] I mean, anything is possible in the multiverse.
[00:50:16] SPEAKER_04: That's it.
[00:50:18] SPEAKER_04: It's called for action every longer.
[00:50:20] It is kind of crazy though,
[00:50:21] SPEAKER_00: because now I'm going to sound totally kuku,
[00:50:24] SPEAKER_00: but if we're in a computed, you know, environment,
[00:50:28] you're building the perfect simulator.
[00:50:30] That kind of is the way you ultimately understand
[00:50:32] SPEAKER_00: and break out of the computer environment, right?
[00:50:34] SPEAKER_00: Like, are we getting closer to the heart of the matrix?
[00:50:36] SPEAKER_00: There's a very deep existential question.
[00:50:39] SPEAKER_04: Yeah, yeah.
[00:50:41] SPEAKER_04: What's your guys' pee of were simulated?
[00:50:43] SPEAKER_04: Like this is all rising.
[00:50:46] Yeah, me too.
[00:50:47] SPEAKER_04: What's your pee?
[00:50:48] SPEAKER_03: I'm low.
[00:50:49] SPEAKER_03: Yeah.
[00:50:50] SPEAKER_03: But yeah, it's okay.
[00:50:51] SPEAKER_03: You're really okay.
[00:50:52] SPEAKER_03: I respect that.
[00:50:53] SPEAKER_03: I'm just like, you know what?
[00:50:54] SPEAKER_03: It's gotta be real.
[00:50:56] SPEAKER_03: Yeah.
[00:50:57] SPEAKER_04: I feel like I'm not like solid 60%.
[00:51:00] SPEAKER_04: I don't know.
[00:51:00] SPEAKER_04: More likely than not at this point.
[00:51:02] SPEAKER_04: I'm there too.
[00:51:03] SPEAKER_00: Well, zero.
[00:51:06] SPEAKER_03: So we make a call.
[00:51:08] SPEAKER_03: So you get trippily small.
[00:51:09] SPEAKER_03: But I'm going to be settled back to that.
[00:51:12] SPEAKER_03: What's the Oracle?
[00:51:14] SPEAKER_03: I'm not that sort of 10-million.
[00:51:15] SPEAKER_03: Sort of 10, yeah.
[00:51:18] What do you think are the theoretical limits
[00:51:20] SPEAKER_00: to Sora?
[00:51:21] SPEAKER_00: Yeah, it's actually a great question.
[00:51:25] SPEAKER_04: I thought a little bit about this.
[00:51:26] SPEAKER_04: I think there's a question.
[00:51:28] SPEAKER_04: Can you eventually simulate a GPU cluster, right,
[00:51:30] SPEAKER_04: in Sora or something?
[00:51:31] SPEAKER_04: And I assume there are some very well-defined limits
[00:51:36] SPEAKER_04: on the amount of computation you can run within one
[00:51:41] SPEAKER_04: of these systems.
[00:51:42] SPEAKER_04: Given the amount of compute, you're actually running it on.
[00:51:45] SPEAKER_04: I have not thought deeply enough about this.
[00:51:47] SPEAKER_04: But I think there are some exist
[00:51:50] SPEAKER_04: central questions there that need to get resolved.
[00:51:52] SPEAKER_04: See, this why his piece is so high.
[00:51:55] SPEAKER_00: Fascinating.
[00:51:57] We've got a few lightning round questions for the team.
[00:51:59] SPEAKER_03: We just kind of generated on the fly here.
[00:52:03] SPEAKER_03: And take your time, jump in whenever you have an answer.
[00:52:06] SPEAKER_03: Your favorite cameo on Sora to date.
[00:52:09] SPEAKER_03: And what happened?
[00:52:11] That is so tough.
[00:52:13] I have a hot one.
[00:52:14] SPEAKER_01: Go go go.
[00:52:16] SPEAKER_01: Sure.
[00:52:17] SPEAKER_01: Yeah.
[00:52:18] SPEAKER_01: OK, so there was this TikTok
[00:52:20] SPEAKER_01: trend.
[00:52:22] SPEAKER_01: And I got obsessed with them.
[00:52:23] SPEAKER_01: I don't know why, but these Chinese factory tours,
[00:52:27] SPEAKER_01: where they're like, hello, this is the chili factory.
[00:52:30] SPEAKER_01: They get like one like, and it's me.
[00:52:32] SPEAKER_01: And it's like, they're showing their chili factory.
[00:52:34] SPEAKER_01: And they're like, it's the chili factory.
[00:52:35] SPEAKER_01: This is amazing.
[00:52:37] SPEAKER_01: Or there's an industrial chemical one.
[00:52:40] SPEAKER_01: Is it?
[00:52:43] SPEAKER_01: I've lost the name, but there's an industrial chemical factory.
[00:52:47] SPEAKER_01: And the first day, I had my cameo options open just
[00:52:51] SPEAKER_01: because I was like, I just want to see what happens.
[00:52:54] SPEAKER_01: And the first day, late at night, I opened my cameos.
[00:53:00] SPEAKER_01: And I was starting to get tagged in factory tour cameos
[00:53:05] SPEAKER_01: that were all in Chinese.
[00:53:07] SPEAKER_01: And I was like, I'm in the chili factory.
[00:53:11] SPEAKER_01: And I was so excited.
[00:53:12] SPEAKER_01: I get zero likes.
[00:53:14] SPEAKER_01: I like the, that was just me.
[00:53:15] SPEAKER_01: But I was like, I'm the chili factory guy now.
[00:53:18] SPEAKER_01: I'm like doing the ribbon cutting at the chili factory.
[00:53:20] SPEAKER_01: Amazing.
[00:53:21] SPEAKER_01: Too deep of a cut that.
[00:53:23] SPEAKER_01: Congratulations.
[00:53:24] SPEAKER_01: Fun fact, I actually have done Chinese factory tours.
[00:53:27] SPEAKER_03: They're amazing.
[00:53:27] SPEAKER_03: Real life.
[00:53:28] SPEAKER_03: And they are truly epic.
[00:53:30] SPEAKER_02: There's this one just, I saw Mark Cuban and George
[00:53:33] SPEAKER_02: dancing around.
[00:53:34] SPEAKER_02: That got me.
[00:53:37] SPEAKER_02: But I mean, my more back to the, like, just I scrolling
[00:53:40] SPEAKER_02: the latest feed and just seeing like the wholesome content
[00:53:42] SPEAKER_02: of people like doing things with their friends,
[00:53:44] SPEAKER_02: actually, I think brings me the most joy of,
[00:53:47] SPEAKER_02: they're not like super liked, but it's like people just
[00:53:50] SPEAKER_02: like getting a lot of, you know, value obviously
[00:53:53] SPEAKER_02: from just like making videos with their friends.
[00:53:54] SPEAKER_02: So Sam has so many bangers.
[00:53:57] SPEAKER_04: I like the one of him doing like this K-pop dance routine
[00:54:00] SPEAKER_04: about like GPUs or something.
[00:54:03] SPEAKER_04: It's very good.
[00:54:03] SPEAKER_04: Actually, I would put it on my Spotify.
[00:54:05] SPEAKER_04: It's like, we had the full song.
[00:54:06] SPEAKER_04: Wow.
[00:54:07] SPEAKER_04: It was like generated by Sora.
[00:54:08] SPEAKER_04: It's like, like, very compelling.
[00:54:11] SPEAKER_04: Yeah.
[00:54:11] SPEAKER_04: All right, well, that leads to the next one.
[00:54:13] SPEAKER_03: Could you mention Spotify?
[00:54:14] SPEAKER_03: What does an AI fully generated AI win first?
[00:54:19] SPEAKER_03: Oscar, Grammy, Emmy?
[00:54:23] I think the like logical answer is like a short winning
[00:54:26] SPEAKER_02: an Oscar.
[00:54:28] SPEAKER_02: Yeah.
[00:54:29] SPEAKER_01: I think that's probably right.
[00:54:30] SPEAKER_01: What would we win it for?
[00:54:31] SPEAKER_04: Like for like a George, the George Trilogy.
[00:54:35] SPEAKER_04: The George Trilogy.
[00:54:36] SPEAKER_04: Yeah.
[00:54:37] SPEAKER_04: Yeah.
[00:54:37] SPEAKER_04: We need new content.
[00:54:38] SPEAKER_04: Yeah.
[00:54:39] SPEAKER_04: I do think if people stitch things together
[00:54:41] SPEAKER_01: and interesting way, yeah.
[00:54:43] SPEAKER_01: You can actually start to make some very compelling storytelling
[00:54:45] SPEAKER_01: in that.
[00:54:46] SPEAKER_01: And I don't think it's like, it doesn't really feel like AI anymore.
[00:54:50] SPEAKER_01: The content I'm seeing.
[00:54:51] SPEAKER_01: That was actually something I noticed with Sora as well.
[00:54:53] SPEAKER_01: Just like, it wasn't even noticing it was AI.
[00:54:56] SPEAKER_01: It was just kind of interesting,
[00:54:57] SPEAKER_01: constant.
[00:54:58] SPEAKER_01: That's more interesting question.
[00:54:59] SPEAKER_02: Will we know?
[00:55:00] SPEAKER_02: Oh, yeah.
[00:55:02] Maybe it's already happening.
[00:55:03] SPEAKER_02: Maybe it's already happening.
[00:55:07] SPEAKER_03: I feel like for Oscars, one of the cool things
[00:55:10] SPEAKER_03: it'll be unlocked is this long tail of epic stories
[00:55:14] SPEAKER_03: in history, stories of heroism and struggle
[00:55:18] SPEAKER_03: and all of these things that have been locked up
[00:55:20] SPEAKER_03: because of the cost of creating.
[00:55:23] As a history enthusiast, I cannot wait for AI
[00:55:28] SPEAKER_03: to unlock all of those stories.
[00:55:30] SPEAKER_03: Have you seen the Bible video app?
[00:55:32] No, I haven't.
[00:55:33] SPEAKER_03: Oh, it's really good.
[00:55:33] SPEAKER_03: I'll show it to you after.
[00:55:34] SPEAKER_00: Like, perfect example.
[00:55:35] SPEAKER_03: Yeah.
[00:55:36] SPEAKER_00: Or there's this movie, The Last Dual, a few years ago
[00:55:39] SPEAKER_03: about this really terrible crime that was committed
[00:55:43] SPEAKER_03: in medieval France that was historically relevant.
[00:55:46] SPEAKER_03: And basically says a lot about humanity.
[00:55:49] SPEAKER_03: And it just got picked up because eventually,
[00:55:51] SPEAKER_03: Hollywood picked up this important story about humanity.
[00:55:54] SPEAKER_03: But how many more are there in human history?
[00:55:56] SPEAKER_03: That's going to be really cool.
[00:55:58] SPEAKER_03: Favorite character from any film or TV show?
[00:56:02] I have a really random one.
[00:56:05] SPEAKER_02: Go for it.
[00:56:06] SPEAKER_02: You guys see Matt Agascar?
[00:56:08] SPEAKER_02: King Julian.
[00:56:09] SPEAKER_02: Oh, played by Sasha Baron Cohen.
[00:56:11] SPEAKER_02: He's a lemur.
[00:56:12] SPEAKER_02: He's a lemur gap.
[00:56:13] SPEAKER_02: Absolutely.
[00:56:14] SPEAKER_02: It's just like a banger.
[00:56:15] SPEAKER_02: It's his humor meets kid-friendly storytelling.
[00:56:18] SPEAKER_02: It's just perfect.
[00:56:20] I play a lot of video games.
[00:56:21] SPEAKER_01: So I mean, your classic answer is going to be like Mario
[00:56:24] SPEAKER_01: or something like that.
[00:56:24] SPEAKER_01: Although, I'll do the deeper cut of we're always
[00:56:27] SPEAKER_01: joking about the rapper.
[00:56:28] SPEAKER_01: Yeah.
[00:56:29] SPEAKER_01: For the rapper.
[00:56:30] SPEAKER_01: The old PlayStation game, one of the original rhythm games.
[00:56:33] SPEAKER_01: And it's got a great artistic style.
[00:56:35] SPEAKER_01: And it's got great IP of just this little wall.
[00:56:37] SPEAKER_01: What is he a dog?
[00:56:38] SPEAKER_01: He's a dog.
[00:56:39] SPEAKER_01: Yeah.
[00:56:40] SPEAKER_01: That's a good pick.
[00:56:41] SPEAKER_04: When I was a kid, I played the Pokemon
[00:56:44] SPEAKER_04: trading card game competitively for a while.
[00:56:47] SPEAKER_04: So I was like really in the Pokemon rabbit hole.
[00:56:50] SPEAKER_04: So like, I don't know.
[00:56:51] SPEAKER_04: I speak to you.
[00:56:52] SPEAKER_04: I was in my eyes.
[00:56:53] SPEAKER_04: I speak to you.
[00:56:54] SPEAKER_04: I speak to you.
[00:56:55] SPEAKER_04: Mudkips.
[00:56:56] SPEAKER_04: Mudkips.
[00:56:57] SPEAKER_03: Super non-consensus.
[00:56:58] SPEAKER_03: Because of a fringe, deep cut.
[00:57:03] SPEAKER_03: OK.
[00:57:03] SPEAKER_03: First world model scientific discovery.
[00:57:06] SPEAKER_03: Most specific possible.
[00:57:08] SPEAKER_03: Obviously, you're not going to say the discovery.
[00:57:11] SPEAKER_04: I suspect it will be something related to classical physics.
[00:57:15] SPEAKER_04: A better theory of turbulence or something.
[00:57:18] SPEAKER_04: That would be my guess.
[00:57:19] SPEAKER_04: I was guessing that it's going to be something like that.
[00:57:21] SPEAKER_01: I was like, yeah.
[00:57:22] SPEAKER_01: Navi Stokes.
[00:57:23] SPEAKER_01: I don't know.
[00:57:24] SPEAKER_01: Yeah.
[00:57:24] SPEAKER_01: Some fluid dynamics thing that's maybe hard to understand.
[00:57:27] SPEAKER_01: Now, there's a lot of unsolved kind of problems there.
[00:57:29] SPEAKER_01: I think sometimes they call it like continuum mechanics,
[00:57:31] SPEAKER_01: or it's like in between.
[00:57:33] SPEAKER_01: And we don't have good models of them.
[00:57:35] Something that lends itself to simulation,
[00:57:37] SPEAKER_02: just like the amount of iterations you can do of a simulation,
[00:57:40] SPEAKER_02: unlocking something, which I don't, yeah.
[00:57:43] SPEAKER_02: Something in that realm.
[00:57:44] SPEAKER_02: The last thing will be able to accurately simulate.
[00:57:49] I do think there's a set of physical phenomenon
[00:57:51] SPEAKER_04: for which video data is like a poor choice of representation.
[00:57:55] SPEAKER_04: So for example, is it really efficient
[00:58:01] SPEAKER_04: to learn about high speed particle collisions
[00:58:04] SPEAKER_04: or something from video footage?
[00:58:06] SPEAKER_04: Maybe.
[00:58:09] I really think video is at its best
[00:58:11] SPEAKER_04: when the phenomenon that you're trying to learn about
[00:58:14] SPEAKER_04: is just natively represented in the physical world.
[00:58:18] SPEAKER_04: And so when you need to do quantum mechanics
[00:58:21] SPEAKER_04: or some other discipline where it's more theoretical,
[00:58:25] SPEAKER_04: we don't have video footage beyond that.
[00:58:28] SPEAKER_04: Can't see it.
[00:58:28] SPEAKER_04: Yeah.
[00:58:29] SPEAKER_04: Things that we've manually rendered
[00:58:30] SPEAKER_04: for educational purposes, it feels like a weaker medium
[00:58:34] SPEAKER_04: for understanding those things.
[00:58:35] SPEAKER_04: So I suspect those would come last.
[00:58:37] SPEAKER_04: I guess it's the things we don't have sensors for.
[00:58:39] SPEAKER_04: Right.
[00:58:40] SPEAKER_04: Right.
[00:58:40] SPEAKER_04: Yeah.
[00:58:41] SPEAKER_02: Maybe the last things we care to simulate
[00:58:43] SPEAKER_02: is another way to think about the answer.
[00:58:45] SPEAKER_02: I don't know.
[00:58:45] SPEAKER_02: I mean, people aren't doing much with smell right now.
[00:58:48] SPEAKER_02: True.
[00:58:49] SPEAKER_02: You know, that's green fields.
[00:58:50] SPEAKER_02: I've been meaning to tell you about that.
[00:58:52] SPEAKER_03: Kind of awkward.
[00:58:54] We're still trying to figure out how to simulate Thomas
[00:58:56] SPEAKER_04: with bad hair.
[00:58:57] SPEAKER_04: Oh, yeah.
[00:58:58] SPEAKER_04: Remains, unknown cell phone.
[00:58:59] SPEAKER_04: Not Thomas.
[00:59:00] SPEAKER_04: But Thomas' hair flow, just general.
[00:59:02] SPEAKER_03: Guzzling touch up.
[00:59:03] SPEAKER_03: Yes.
[00:59:03] SPEAKER_03: There was a good round of people being bald.
[00:59:06] SPEAKER_01: We were all dead bald.
[00:59:08] SPEAKER_01: Oh, yeah.
[00:59:08] SPEAKER_01: And this is from all gems.
[00:59:09] SPEAKER_01: We're good.
[00:59:10] SPEAKER_01: Actually, kind of cool.
[00:59:11] SPEAKER_01: That's a use case that doesn't really talk about very much,
[00:59:14] SPEAKER_01: but it's like visualization.
[00:59:16] SPEAKER_01: When you're bald, yeah, everybody wants to be bald though.
[00:59:17] SPEAKER_01: It's just like you just see yourself
[00:59:19] SPEAKER_01: in some different context.
[00:59:20] SPEAKER_01: I think that can be quite powerful, even like therapeutic
[00:59:22] SPEAKER_01: in some ways, where you just like see yourself
[00:59:24] SPEAKER_01: in some context that you either want or don't want yourself
[00:59:27] SPEAKER_01: to be kind of being and just see yourself.
[00:59:29] SPEAKER_01: It's a real use case.
[00:59:30] SPEAKER_02: Yeah.
[00:59:31] Yeah.
[00:59:32] SPEAKER_03: Guys, thank you so much for coming from space-time tokens
[00:59:35] SPEAKER_03: to object permanence, world models
[00:59:38] SPEAKER_03: that will enable scientific discovery,
[00:59:41] SPEAKER_03: the democratization of creation all the way
[00:59:45] SPEAKER_03: to walking clocks.
[00:59:46] SPEAKER_03: You guys have covered it all.
[00:59:48] SPEAKER_03: Thank you so much.
[00:59:49] SPEAKER_03: And the future has been created by you.
[00:59:52] SPEAKER_03: Thanks, Constantine.
[00:59:53] SPEAKER_03: Thank you.
[00:59:54] SPEAKER_02: Thank you.
[00:59:55] Thank you.
[00:59:55] Thank you.
[00:59:56] Thank you.
[00:59:57] Thank you.
[00:59:58] Thank you.
[00:59:59] Thank you.
[01:00:00] Thank you.
[01:00:01] Thank you.
[01:00:02] Thank you.
[01:00:03] Thank you.
[01:00:04] Thank you.
[01:00:05] Thank you.
[01:00:06] Thank you.
[01:00:07] Thank you.
[01:00:08] Thank you.
[01:00:09] Thank you.
[01:00:10] Thank you.
[01:00:11] Thank you.
[01:00:12] Thank you.
[01:00:13] Thank you.
[01:00:14] Thank you.
[01:00:15] Thank you.
[01:00:16] Thank you.
[01:00:17] Thank you.
[01:00:18] Thank you.
[01:00:19] Thank you.
[01:00:20] Thank you.
[01:00:21] Thank you.
[01:00:22] Thank you.