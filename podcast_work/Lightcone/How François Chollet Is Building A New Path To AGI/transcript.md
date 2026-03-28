[00:00:00] François Chollet: I think we're probably looking at AGI 2030. Around the time that we're going to be releasing, like maybe ARK 6 or ARK 7, you're not going to stop AI progress. I think it's too late for that. And so the next question is, okay, like AI progress is here. It's actually going to keep accelerating. How do you make use of it? How do you leverage? How do you ride a wave? That's the question to ask.

[00:00:30] Host 1 (Y Combinator): Today we're lucky to be joined by François Chollet, founder of the ARK Prize, a global competition to solve the ARK AGI benchmark. His latest project is Endia, a lab exploring a new paradigm in frontier AI research. François is one of the best people in the world to help us understand the current AI moment and where all of this is going. François, thank you so much for joining us today and congrats on the launch of ARK AGI v3.

[00:00:57] François Chollet: Thanks so much for having me. I'm super excited to be here. Super exciting time to talk about AI.

[00:01:02] Host 3 (Y Combinator): So François, tell us a little bit about Endia. So what exactly is it and what are you guys trying to achieve?

[00:01:08] François Chollet: Right. So Endia is this new AGI research lab and we are trying some very different ideas. And so our goal is basically to build this new branch of machine learning that will be much closer to optimal, unlike deep learning.

[00:01:23] Host 1 (Y Combinator): All of us right now are sort of taken by what's going on with code. I have sort of this viral moment right now where I got to 40,000 stars this morning on GStack. So it's like, oh, this is an open source project that now is one of the biggest ones. And I have more than 100 PRs from contributors to deal with. I guess you're, you know, one of the best people to talk to about this because you're actually literally coming up with something that is a totally different pathway.

[00:01:51] François Chollet: That's right. That's right. So what we're doing at Endia is we're doing program synthesis research. And when I talk about program synthesis, often people ask me, oh, so are you doing like Cogen? Are you building an alternative to coding agents?

[00:02:04] François Chollet: And that's actually not at all what we are doing. We are working at a much, much more, much lower level than that. What we're actually doing is that we are trying to build a new branch of machine learning, an alternative to deep learning itself rather than like coding agents. Coding agents are like this very, very high level, last layer piece of the stack.

[00:02:23] François Chollet: And we're actually trying to rebuild the whole stack on top of different foundations. So we're building a new learning substrate that's very different from, you know, parametric learning, deep learning. So if you go back to the problem of machine learning, you have some input data, some target data, and you're trying to find a function that will map the inputs to the targets that will hopefully generalize to new inputs.

[00:02:49] François Chollet: And if you're doing deep learning, what you're doing is that you have this parametric curve that serves as your function, as your model, and you're trying to fit the parameters of the curve via gradient descent. And this is basically what we're doing, except we are replacing the parametric curve with a symbolic model that is meant to be as small as possible. It's like the simplest possible model to explain the data, to model what's going on.

[00:03:17] François Chollet: And of course, if you're doing that, you cannot apply gradient descent anymore. So we are building something that we call a symbolic descent, which is like the symbolic space equivalent of gradient descent. The idea is to build this new machine learning engine that's giving you extremely concise, symbolic models of the data you're feeding into it. And then we are going to make it scale.

[00:03:41] François Chollet: And so everything you're doing with machine learning today, with parametric curves, we should be able to do it with symbolic models in the future in a way that will be much, much closer to optimality. Much closer to optimality in the sense that you're going to need much less data to obtain the models. The models are going to run much more efficiently at inference time because they're going to be so small. And because they're so small, they will also generalize much better and compose much better.

[00:04:09] François Chollet: You know, the minimum description length principle that the model of the data that is most likely to generalize is the shortest. And I think you cannot find a model like this if you're doing parametric learning. You need to try symbolic learning.

[00:04:23] Host 1 (Y Combinator): That's fascinating.

[00:04:23] Host 4 (Y Combinator): So the rest of the industry is just pouring more and more billions of dollars down an approach that was set years ago. Can you, like, help make the case for why you think that it's the right thing to explore alternate approaches instead of just to keep putting more money into the current approach?

[00:04:39] François Chollet: I mean, everybody is, you know, building onto the LLM stack these days, which makes sense because, you know, the returns are there, like it's actually working. So it would seem very sensible for everybody to just be doing what seems to be the currently most proactive path. But our tech is actually, it's counterproductive to have everybody working on the same thing. Like, I personally don't think that machine learning or AI in 50 years is still going to be built on this stack.

[00:05:07] François Chollet: I think this is a stack that is very nice. Maybe it even gets us to HCI, but it's not as efficient as it should be. I think it's inevitable that the world of AI will trend over time towards optimality. And so I'm trying to sort of like leapfrog directly to optimality, like to build the foundations of optimal AI today. But in general, you know, our vision is very ambitious and I'm not saying that we're going to be successful.

[00:05:35] François Chollet: Like we have maybe a 10 or 15% chance of success, but that is enough that it's worth trying, right? And I think in general, like among listeners, if you have a big idea and it has very low chance of success, but if it works, it's going to be big and no one else is going to be working on it, right? It's not something popular. It's not something, if you don't do it, no one else will do it. And this is basically our situation. If you're in this situation, then you should try a chance. You know, you should go and work on it.

[00:06:04] Host 4 (Y Combinator): I mean, that's almost like the mission statement of Y Combinator, the thing that you just said.

[00:06:08] François Chollet: Yeah. Yeah. The reason it's important is that, again, if we don't do it, no one else will do it. Right. So it's worth trying. Even if we don't succeed, it's worth trying.

[00:06:15] Host 3 (Y Combinator): Has the success, well, very specifically of the coding agents, I guess, built on top of the LLM stack, like has their success surprised you at all? And in particular, like say over the last six months or so?

[00:06:26] François Chollet: Yeah, absolutely. I think it has surprised many people. It definitely did surprise me. If you look at why everything is starting to work so well with coding agents, it's really because code provides you with a verifiable reward signal. And I think right now we're in this situation where any problem where the solutions you propose can be formally verified and you can actually trust a reward signal. It's not just some guess made by a model. Any domain like this can be fully automated with current technology, with the LLM-based stack.

[00:06:55] François Chollet: And code is sort of like the first domain to fall, but there will be many others in the future. I think mathematics is also primed to see a revolution in the next few years for the same reasons, again, because the domain just gives you verifiable rewards.

[00:07:11] Host 2 (Y Combinator): I guess the challenge for a formally verified domain is you have to somehow take a domain and make it verifiable, which is the trick. I mean, code is very natural. You could test, there's bugs, compiles, et cetera, and mathematics as well, whether all the theorems and proofs work out. I guess it becomes more nebulous when you go a couple degrees off where there are fields that are not naturally formally verified.

[00:07:37] Host 2 (Y Combinator): And you need to come up with a, again, with some sort of a function to come up with that reward that makes it verifiable.

[00:07:46] François Chollet: Yeah, yeah.

[00:07:46] Host 2 (Y Combinator): With very fuzzy things like, let's say, English language and composing the perfect essay. How do you make that formally verifiable?

[00:07:55] François Chollet: Yeah, yeah, absolutely. I mean, writing essays is, you know, the typical example of a domain that's not verifiable. And so what you're going to see is that progress of reasoning models and base LLMs on this type of domain is, you know, it's going to be very slow because the stack we're using, like the LLM stack is very, very reliant on its trained data. It's basically just operationalizing the trained data.

[00:08:19] François Chollet: And for writing essays, the trained data is coming from human experts, like annotating answers. And that's costly. So you're going to see this very, very slow progress. Maybe it's even going to stall. But for any verifiable domain, like tech code, for instance, which was the big unlock is when people started creating this code-based, like training environment for post-training,

[00:08:44] François Chollet: where the reward signal, the verification signal is provided by things like unit tests and so on. And so that means that the model was not just working from human provider annotations. It was actually trying its own things, verifying the answer and generating a lot, lot more trained data in the process, a much denser coverage of the problem space.

[00:09:06] François Chollet: And not just coverage in terms of like, is the answer right or wrong, but also starting to build models of the execution traces, right? So that the models could start incorporating an execution model. Very much the way that human programmers, you know, when they look at code, they're sort of like executing the code in their minds. They keep track of the value of variables and so on. It's also what the models are trying to do now. And this is why it's working so well.

[00:09:31] François Chollet: And it's possible because you're working with this very formal, fully verifiable environment. You cannot do that with assets. You cannot do that with law or many other problems.

[00:09:41] Host 2 (Y Combinator): I think I really like how you define intelligence and how to measure it, which brings to the question of also sharing, having you share the history of ArcGIS.

[00:09:52] François Chollet: Yeah. So my definition of general intelligence, you know, many people around the industry these days, they say AGI is going to be a system that can automate most economically valuable tasks. And to me, that definition is it's about automation. It's not about intelligence. It's not about general intelligence.

[00:10:12] François Chollet: So my definition is AGI is basically going to be a system that can approach any new problem, any new task, any new domain and make sense of it, like model it, become competent at it with the same degree of efficiency as a human could. So meaning it's going to need basically the same amount of training data and training computes as a human would, which is very little. Like humans are really, really data efficient.

[00:10:41] François Chollet: So general intelligence is human level skill acquisition efficiency on the same scope of tasks that humans could potentially learn to do.

[00:10:52] Host 4 (Y Combinator): Do you think it's possible that we will accomplish the first definition of AGI, the automate most economically useful work, before we accomplish your definition? Absolutely.

[00:11:01] François Chollet: I think that's a trajectory that we're on right now. And I think it's already true that in principle, current technology can fully automate at human level or beyond any domain where you have verifiable rewards. Right. And code being the first one. And I think figuring out AGI, figuring out like human level, you know, learning efficiency over arbitrary tasks, that's probably going to take a different sort of technology, a different mindset, a different approach.

[00:11:29] Host 4 (Y Combinator): Do you think that LLMs can be bent to have the same sample efficiency as humans? Or do you think it's like fundamentally just impossible and we need a new approach? And that's, that's the thing that you're hoping, hoping to solve.

[00:11:41] François Chollet: With enough compute, everything starts looking like everything else. Every, like compute is a great equalizer. Every approach starts looking the same. And I think it's possible in principle to build something that looks a lot like AGI on top of the LLM stack. But it's not going to be LLMs per se. It's going to be this new layer. Perhaps, you know, it's going to be even a few layers above, not just one layer above, but a few layers above. But you can build it on top of LLMs because LLMs are kind of computer, right?

[00:12:10] François Chollet: I do believe, however, this would be the wrong thing to do because it would be very inefficient. I think AI, AI research will have to trend towards not just efficiency, but in fact, optimality over time. And for this reason, future AI in a few decades, it's not going to be this harness on top of a reasoning model on top of a basal alum. It's going to be much, much lower than that.

[00:12:35] Host 4 (Y Combinator): To Diana's question, do you want to talk about how you actually designed ArcGi and why it's a good barometer of that?

[00:12:40] François Chollet: I mean, you know, I've been doing deep learning for a very, very long time. And initially, my take, my mindset was that deep learning was going to be able to do everything.

[00:12:49] Host 2 (Y Combinator): You were the creator of Keras before even all the other frameworks became very popular.

[00:12:55] François Chollet: That's right. That's right. I was trained deep learning model for natural language processing, in fact, in 2014. And from that work, you know, I actually started developing this open source library, which I released, in fact, exactly 11 years ago, March 2015. So that was Keras.

[00:13:17] François Chollet: And then it got popular and then I ended up sort of like doing less of the research that I started Keras for and more working on the framework itself. Just because it has really, really good product market fit. And so my take, you know, around that time, around like 2015, 2016, was that deep learning was extremely general, that you could do everything with deep learning, that you didn't need anything else. It was during complete. So my take was basically a deep learning was differentiable programming.

[00:13:45] François Chollet: So anything you would do with software, you could in principle train a deep learning model on the right inputs and outputs to do the same thing. And in 2016, I was doing research at Google Brain on trying to train deep learning models to help with reasoning problems. And in particular, first order logic problems, theorem proving and so on.

[00:14:10] François Chollet: And I started finding that you could not really get gradient descent to encode sort of like reasoning style algorithms. It was not because the models could not represent these algorithms. It was because gradient descent could not find them. Right. So the problem was that it wasn't about deep learning not being trained complete or anything like that. Like that was not the problem. The problem was gradient descent. Right. gradient descent would not find generalizable programs.

[00:14:40] François Chollet: It would instead end up doing overfit pattern matching. Right. Over sequences of input tokens.

[00:14:47] Host 1 (Y Combinator): Which I guess people could argue like that's what's happening. I mean, it's useful.

[00:14:51] François Chollet: It's still what's happening today in a slightly higher level version of that.

[00:14:57] Host 2 (Y Combinator): It's with a lot of data. So it doesn't feel like overfitting because the data has a lot more distribution. Yeah.

[00:15:01] François Chollet: With a lot more data. And also I think models today, they're a lot more compressive after data, which is why they generalize better.

[00:15:08] Host 1 (Y Combinator): All models are wrong, but some models are useful. And then I guess what I'm hearing is like your method might find the right model.

[00:15:16] François Chollet: That's right. So that's where the idea came from. And I was like, you know, at the time back in 2016, 2017, I was like, okay, we're going to need a benchmark to capture these ideas. We're going to need a program synthesis benchmark. And my mental model for that was ImageNet. I was like, oh, I'm going to make the ImageNet a freezing. So I started brainstorming a few ideas around like 20s, 2017. I explored many different things.

[00:15:44] François Chollet: I tried working with in particular cellular automata, like a setup where you show a model, cellular automata outputs, and it must recreate the program that generated them, like that sort of thing. And eventually I settled on the ArcGIS format around like early 2018. You know, I was doing this on the side. It was a side project. Like my main project was developing Keras at Google. I wasn't moving very, very fast on that.

[00:16:13] François Chollet: So summer 2018, I wrote the Arc task editor. And then I started just making lots of tasks by hand. And about one year later, I had made 1,000 tasks. And so I wrote up the paper that was explaining what this was about, what the big idea was, like intelligence as skill acquisition efficiency. And I published all of that in 2019.

[00:16:36] Host 2 (Y Combinator): In parallel, GPT-3 2020 was coming out and starting to show signs until the chat GPT moment around 2022, end of the year. And the industry took off with that. And this was one of the benchmark that was really performing really badly. And it was very obscure. I don't think many people knew about it. It was mostly niche research communities that maybe read your paper.

[00:17:00] François Chollet: Yeah. People who worked on programs this knew about it. But a lot of people who worked on deep learning, on scaling up LLMs, stayed in really care for it. And part of the reason why is because LLMs did not work well or at all on the benchmark. For a benchmark to capture the attention of the research community, it needs to start working a little. If it's too hard, people are just going to dismiss it.

[00:17:24] Host 1 (Y Combinator): You're just ahead of your time, clearly, because we're not on Arc AGI 1 anymore. And then 2 is reaching saturation. And then 3 is out now. Yes.

[00:17:36] Host 2 (Y Combinator): And I think the cool thing about Arc AGI, it has been a very good barometer for the industry of the big changes that happen. Because V1 was not working at all for a long time until 2025 when reasoning models came out, right?

[00:17:55] François Chollet: Yeah, absolutely. If you look at frontier performance on Arc V1 first and then V2, so basal lamps were scoring extremely low on V1, like sub 10%, basically. And, I mean, it was true of the original Arc GPT-3, which was scoring zero. But that's even true of the latest basal lamps today, you know, as of March 26.

[00:18:18] Host 1 (Y Combinator): Without reasoning.

[00:18:19] François Chollet: Without reasoning. Without reasoning, yeah. So the base models. So performance of basal lamps on V1 stayed very, very low, even though in the meantime, you know, we had scaled up these models by 50,000x, right? So it was really telling you that, you know, more scale, scaling up pre-training alone was not going to crack the benchmark. This was not enough to demonstrate that the model had fluid intelligence.

[00:18:43] François Chollet: And then, the moment models started performing well on Arc 1 was with the first reasoning models. In particular, the OpenAI 01 and then 03 models, which by the way, they were demonstrated by OpenAI on Arc because it was the one unsaturated reasoning benchmark that was really showing that this model was different. That, that new capabilities that we had not seen before.

[00:19:07] François Chollet: And so with reasoning models, you start seeing this sudden, like, step function change on Arc 1. And so Arc 1 was really the benchmark that signaled that at this moment in time, something was happening. Something big. Yeah, something big. Like, new capabilities were emerging. Like, reasoning was new and different. And it was actually not obvious at the time. Like, you know, I don't know if you remember when 03 preview was announced by OpenAI.

[00:19:36] Host 2 (Y Combinator): That was end of 2024, actually.

[00:19:37] François Chollet: Yeah, December 2024. And, like, sure, it was, like, a huge step function progress on Arc. But it was very expensive. It did not really have product market fit, effectively. But if you looked at Arc results, you knew that this was big and important. And then we released Arc 2, which was the same format, but more difficult, like, with more composition at the level of the reasoning chains.

[00:20:05] François Chollet: And what happened is that, so the earliest reasoning models started very, very low on Arc 2. And then around the same time as coding agents started working, you saw this. Yeah. So very, very recent, just a few months ago, you saw this very, very fast, like, saturation of Arc 2. And so, again, like, Arc 2 signaled that, yes, there was this new set of capabilities emerging.

[00:20:29] François Chollet: So I think the benchmark did a really good job at capturing the advent of reasoning models and then the advent of agentic coding. Like, this new paradigm where if you have verifiable rewards, then you can basically fully automate the domain. Which, by the way, is true of Arc. Like, Arc does provide a verifiable reward.

[00:20:48] Host 1 (Y Combinator): I guess for V2, what caused the... So one was clearly reasoning. Two, a benchmark doesn't care how you solve it. I guess embedded in what you said, like, were people using code gen to then solve V2? That's right.

[00:21:02] François Chollet: Not necessarily code gen per se, but the Frontier Labs have been targeting Arc V2. And the progress you saw on Arc V2 is actually a result of this very, very large-scale targeting. So what you can do to solve Arc V2 is you ask your reasoning model to make more tasks like those in the benchmark. And then you try to solve them using, let's say, program induction, for instance, still using your reasoning model.

[00:21:31] François Chollet: Then you verify the solution. Again, it's verifiable. So you can trust the answer. And then you fine-tune the model on the successful reasoning chains. And then you keep repeating, like, generate new tasks. You solve them. You verify the solution. You fine-tune the model on the reasoning chains. And you can keep doing this millions of times, right? Like, you just need to spend more money. This is the RL loop that is happening.

[00:21:55] François Chollet: And the new paradigm in AI is basically that any domain where this is true, where you have the ability to generate these true verification signals, you can run this kind of loop, right? If you can run this kind of loop, you can mine. You can brute force mine, effectively, the entire space and get extremely high performance. This is basically the process through which Arc V2 was saturated.

[00:22:18] François Chollet: So what it tells you is that it's not so much that the models have higher fluid intelligence than they did with the first using models. It's just that you have this new paradigm of post-training. And this is exactly what led to agentic coding. So it does matter. It is valuable. It is useful.

[00:22:36] Host 1 (Y Combinator): It's not that the models are smarter. It's that they're suddenly more useful. And it's possible to be more useful in particular domains without being smarter. Yeah, absolutely. Because that means good things for me. I'm not getting any smarter right now at age 45. But I can learn how to do things. And that's sort of what's happening with the models as of late.

[00:23:00] François Chollet: Yeah, absolutely. When it comes to competency, there's always a trade-off between intelligence and knowledge. If you have more knowledge, if you have better training, you need less intelligence to be competent. And that's exactly what happened with the rise of coding agents, right? The models don't have higher fluid intelligence per se. They don't have like a higher IQ, so to speak. It's just that they're way better trained. And they're way better trained in two ways.

[00:23:28] François Chollet: So they're not just trying to complete code anymore. They're actually trained via trial and error in these RL post-training environments with true reward signals. And also, they're trained to embed this model of code execution, right? Where they learn to keep track of the value of variables over an execution cycle. And that's what's leading to this extremely strong product market foods of urgent encoding today. And it's completely changing software engineering.

[00:23:57] Host 2 (Y Combinator): This happened not too long ago, this situation. We actually had the founders of Poetic that came and spoke about the approach, which is really, sounds like this new way of getting LMS to perform is building this agent hardness, right? And the hardness is basically structuring a problem domain into something that can be formally verified. And they did that basically for ARK V2, which when they released it, they were at the top of the benchmark.

[00:24:27] Host 2 (Y Combinator): But then the crazy thing is I actually worked with a company in the winter 26 batch not too long ago called Confluence Lab, which actually ended up saturating the V2 results with 97%. And I think their task cost was a lot more efficient, too. And the approach they basically took is similar to this. I think they built the harnesses on top of it in order to get the LMS to go and build different tasks and program through it.

[00:24:55] Host 2 (Y Combinator): Which then, for me, I was like, wow, is this batch? And during the batch, they only worked on it for a couple of months. And they were able to saturate this benchmark that has been around for a long time. It's like something special is happening.

[00:25:07] François Chollet: Yeah, yeah. There's a lot of progress right now that's driven by custom harnesses around the task. And the harness is basically a way for the human programmer to input into the model or higher level solution strategies, basically. I mean, to me, the fact that you need humans to engineer these harnesses is also a sign that we're short of HGI today. Because if we had HGI, HGI would just make its own harness. It would not need to be told how to solve a problem.

[00:25:36] François Chollet: It would just figure it out. But it is very effective. Like, harnesses, I don't think they get us closer to HGI in any sense. But it's a very valuable area of research because that can lead to task automation at scale.

[00:25:48] Host 1 (Y Combinator): YC's next batch is now taking applications. Got a startup in you? Apply at ycombinator.com slash apply. It's never too early. And filling out the app will level up your idea. Okay, back to the video.

[00:26:02] Host 2 (Y Combinator): Can you tell us about then what V3 is going to measure that's just got released?

[00:26:07] François Chollet: Yeah, absolutely. So if you look at V1, V2, it was really focusing on your ability to produce causal models of a pattern that was just given to you, like the data was given to you. So it was static. It was passive and really focused on modeling. And V3, it's completely different. We are trying to measure agentic intelligence. So it's interactive. It's active. Like the data is not provided to you.

[00:26:37] François Chollet: You must go get it. The idea is that your agent is dropped into a new environment, which is kind of like a mini video game. And it's not provided any instructions. It's not told what to do. It's not told what the goal even is or what the controls even are. And it must figure out everything on its own via trial and error. So we are not just measuring, you know, the AI's ability to model its environment.

[00:27:05] François Chollet: We're also looking at its exploration efficiency, its ability to acquire goals on its own, like goal setting. And of course, its ability to plan through the model of the environment that's created and to execute the plan. And so together, you know, all of these abilities, we call that agentic intelligence. And we are looking for AI systems that could learn to play these games and, you know, crack them with the same degree of action efficiency as a human.

[00:27:35] François Chollet: If you look at the human, they are dropped into this new environment. They try a few things. They start understanding how things work. They can solve the environment, you know, in a few hundreds to thousands of actions. We're trying to look for AI systems that could match this efficiency. And by the way, we know that all of these test environments in R3 are solvable by humans with no prior training because we actually tested them on regular people.

[00:28:00] François Chollet: Yeah, at first you just see this screen and, you know, you have these keys available, but you don't know what they do. And you must figure out everything from scratch. And humans are really good at that, by the way. They're really good at exploring efficiently, making sense of something new and eventually cracking the game. And frontier models today, they are not very good at it.

[00:28:21] Host 4 (Y Combinator): If the reasoning models cracked V1 and the reinforcement learning environments cracked V2, do we need a new advance to crack V3? Do even the best techniques currently not work?

[00:28:33] François Chollet: Yeah, I mean, I'm pretty curious to see how frontier labs are going to react to V3 and how they're going to start targeted. It is designed to be more resistant to the same kind of targeting strategy as what we saw for V2 in particular. Of course, you can try to just make more ARC3-like games and then train your agents in them.

[00:28:57] François Chollet: But the thing is, we've deliberately tried to create a private set of environments that is significantly different from the public set. Like, you can look at the public set. It's not actually giving you that much information about what's in the private set. In the private set, you will have very different games with very different concepts. And also, the public set is meant to be substantially easier. Your performance on the public set is not representative of how well the system will do on the private.

[00:29:25] François Chollet: So for this reason, it's going to be harder to target. And that makes it a better test of fluid intelligence as opposed to a test of how much effort you put into cracking it. I'm so curious. How do you come up with these games? They're so creative. Yeah, we set up an entire video game studio to create them. So we got over 250 games. And they're pretty quick to play.

[00:29:49] François Chollet: Each game takes you maybe 10 minutes or a bit less to play from scratch, like upon first contact. And we have like 250 plus. And we set up this very productive game studio where we had any given week, we had multiple games in progress. So we had like this pipeline, including design, implementation, review, human testing, and many iteration cycles to make sure that the game comes out right.

[00:30:18] François Chollet: Who's working in the studio? Right. Who are the creators? Yeah, we hired a team of game developers. And we built our own game engine.

[00:30:26] Host 4 (Y Combinator): Wow. So it's actually people who like previously worked in the game, in the video game industry.

[00:30:32] François Chollet: That's right. That's right. So one thing to be in mind though, is that the games in Arc 3 are unique, right? They're trying to not borrow elements, concepts from previous video games. They're built entirely on top of core knowledge priors. Like things like just, you know, elementary knowledge, like basic physics, understanding of objects, understanding of the notion of agents, for instance. Like an agent in objects with goals and intentions.

[00:31:01] François Chollet: But we are not incorporating any language, any like cultural symbols, like, you know, arrows, for instance. Or the color green meaning go and color red meaning stop, that sort of thing. There's no external knowledge that's involved in these games.

[00:31:16] Host 2 (Y Combinator): It's like one of those IQ tests that are just pattern matching, but now it has time series.

[00:31:20] François Chollet: Yeah. Yeah. And it's not just time series. It's interactive. Interactive. You must create your own path through game space, right? You must, you know, in an IQ test like problem, like, you know, what Arc 1 and 2 is, the data that you must model is provided to you. You already have the data. You just need to find a causal rule to explain it. With Arc 3, you actually must gather the data. And you must do so efficiently.

[00:31:48] François Chollet: Like, of course, you could say, well, I'm just going to, you know, brute force mine the space of every possible game state. And then I find the solution. You cannot do that because if you try to do that, you would score extremely low. Even if you manage to solve the level. Because you're scored on your efficiency. You must match human level efficiency.

[00:32:06] Host 1 (Y Combinator): It's funny. It's like almost a coming full circle. This level of AGI with games sort of is the match pair to OpenAI writing. I mean, you know, Tom Brown, one of the co-founders of Anthropic, had to write, like, the harness code to allow, like, you know, pre-GPT AI at OpenAI to play StarCraft.

[00:32:26] François Chollet: Yeah, yeah. OpenAI worked on, in particular, on Dota 2. They had the OpenAI 5 model, which was, if I recall correctly. So this was, like, not just pre-GPT, but also mostly pre-Transformers because they were working with a stack of LSTM layers, if I recall correctly. And even before OpenAI, DeepMind worked a lot on video games, you know, solving video games via DeepIsle.

[00:32:54] François Chollet: And they were the first to do Atari games, right, back in 2013. You know, they were very, very early, very visionary in that sense to work on this problem so early with these methods, which are still very modern methods. So the big difference is that if you look at Atari games, for instance, or even Dota, you're training on the same environment as what you use for testing. So effectively, you're just trying to memorize the best strategies.

[00:33:23] François Chollet: You're trying to, at training time, explore the full space of possible game states and productionize, operationalize that knowledge into the model. And then at inference time, you're basically just recalling that knowledge. And that's explicitly what you're trying to avoid with ARK3. You're not playing games that you've seen before.

[00:33:50] François Chollet: You're not playing games that you've been trained on, like, for millions of hours. Like, the OpenAI 5 model, for instance, was playing a restricted version of Dota 2. And it was trained on, like, tens of thousands of hours of gameplay, effectively. I think maybe in millions. But it's just an insane amount of training data. With ARK3, you're being evaluated on games that you're seeing for the very first time. And every action you spend exploring is counted towards your efficiency score, right?

[00:34:18] François Chollet: So you're really focused on measuring fluid intelligence, your ability to efficiently explore, efficiently produce a world model of the environment, and then use this model to infer goals, plan towards these goals, and eventually crack the game.

[00:34:35] Host 1 (Y Combinator): One of the arguments for NDIA is that you're able to do all of the intelligent tasks for, you know, an ARK task might be like 0.3 cents for an ARK task. But, you know, for the same task on a foundation model with LLMs, it's, you know, $1 to $10.

[00:34:54] Host 1 (Y Combinator): And then there's this other aspect that we've been tracking where it seems like more and more intelligence, at least on the LLM side, can be distilled down into smaller and smaller models. And so on the one hand, like, they're scaling up, but then they're like distilling smarter and smarter small models.

[00:35:14] Host 1 (Y Combinator): I guess your approach might indicate that it's not billions of parameters, like the, you know, NDIA achieving AGI might not be, you know, sort of inherently a scale thing at all. There's a platonic ideal of the NDIA model that achieves AGI. Yeah. Do you ever think about it in terms of like, well, it would fit on a floppy disk?

[00:35:35] François Chollet: Well, okay. There are two things to separate. There's the sort of like fluid intelligence engine. I think it's going to be a very, very small code base and a very small set of models that's suited with it. And it's probably going to be on the order of megabytes, right? And then you have the knowledge base, so to speak, that's going to be layered below this fluid intelligence engine.

[00:36:00] François Chollet: Like, you know, fluid intelligence has to draw on some knowledge and that knowledge is going to take up a lot more space. I think it's important to differentiate the two. I do believe that, you know, when you create AGI, retrospectively, it will turn out that it's a code base that's less than 10,000 lines of code. And that if you had known about it back in the 1980s, you could have done AGI back then using the computer resources available back then.

[00:36:28] Host 4 (Y Combinator): Wow, that's a crazy prediction.

[00:36:29] François Chollet: I think retrospectively, this will turn out to be true.

[00:36:33] Host 4 (Y Combinator): Wow. So it was just like hiding under our noses in plain sight for like 40 years. It took us like 40 years to figure it out.

[00:36:38] Host 1 (Y Combinator): That's right. That's right. Well, that second thing sounds like Douglas Lenat's like psych project, or is that the wrong way to think about it? It's like there's sort of knowledge about the world. Yeah. And then there's methods. Like the program, what I hear is like the program might be 10,000 lines and then it operates on like...

[00:36:55] François Chollet: On knowledge base, it's very large. So the problem with psych, I mean, there were many issues with it, but one of the big issues is that there was no learning involved. Yeah.

[00:37:05] Host 1 (Y Combinator): It's just the knowledge. Like the knowledge was encrafted. It was like purely symbolic knowledge and it was probably inaccurate.

[00:37:10] François Chollet: The way you want to be building a GI is that you want to be removing humans from the improvement loop as much as possible. You don't want a system where every improvement in system capability has to involve a human engineer doing something. And it's actually the strength of deep learning and foundation models is that you can just scale up the knowledge base. Like an LLM is effectively a knowledge base.

[00:37:34] François Chollet: It's a bank of, you know, modular vector programs that map patterns of input tokens to patterns of output tokens. And you can scale up that knowledge base by just adding training data and training compute with no further human involvement. I mean, of course, there's still a little bit of human involvement in making sure the training job completes, but it's minor. You've managed to remove humans from this improvement as much as possible. And that's also what we want for our system.

[00:38:03] François Chollet: We want a system that's self-improving where the improvements are compounding, meaning that every time the system increases capabilities, it's also increasing the rate at which it increases capabilities.

[00:38:15] Host 1 (Y Combinator): I think this is a PG-ism. It's like, I'm sorry the essay is so long. If I had more time, I would make it shorter. Yeah.

[00:38:22] François Chollet: When you're looking at a hard problem, it's actually harder to produce a short, elegant, concise solution than a messy, over-engineered solution.

[00:38:32] Host 1 (Y Combinator): You can brute force it, but, you know, the more elegant version is very, very short. And that's kind of like what you said with how this might come about.

[00:38:39] François Chollet: Yeah. This is literally the shape of the type of AI approach we are creating. And I think this is also the shape of science itself. Like science is fundamentally a symbolic compression process where you're looking at a big mess of observations, like, you know, the position of planets in the sky or something like that. And you're compressing that down to a very simple symbolic rule.

[00:39:07] François Chollet: You're saying like, yeah, like all these new thousands of observations, actually just all this one simple equation. That's symbolic compression. And to do this, by the way, you need the model to be symbolic. Like you could not fit a curve and say, well, you know, that curve is my model. That would never be optimal. It would never be concise or elegant enough. And that's not what science is doing. Science is not about curve fitting.

[00:39:32] François Chollet: Science is about finding the equation, finding the most compressive symbolic model of your pile of observation. And that's the process that you are trying to recreate in software form. Like you could say that the NDI approach to program synthesis is that we are building science incarnate, science, the scientific method in algorithmic form.

[00:39:51] Host 4 (Y Combinator): I'm curious if you compare it to biology. Clearly, LLMs don't learn the way that humans do because no baby reads the whole internet. Do you think program synthesis is closer to the way that humans learn? Or do you think that's yet a third branch where even if program synthesis is correct, there will be some yet as undiscovered third way to do it, which is the thing that we do?

[00:40:13] François Chollet: I think so. I do think humans do some amount of program synthesis. I think the way humans learn and the way the human mind works is very messy. It's not like there's one simple, elegant principle behind it all. It's an implementation of fundamental principles, the fundamental principles of intelligence, which, you know, I think we can identify these principles and reimplement intelligence from scratch, from first principles.

[00:40:41] François Chollet: In a way, it will be much more efficient than the human brain. I think the human brain is messy and it can be a good source of inspiration for AI. But I think it would be counterproductive to just try to, you know, observe it and reimplement it like and make it biologically plausible. I think that's counterproductive. It's not what we're trying to do at NDI. We're only trying to find what are the first principles of intelligence and what is the system that would best implement them.

[00:41:09] François Chollet: But yeah, I do believe the human mind does at the highest level something that looks a lot like programs. It's like we're currently building causal models of our surroundings. Like we're describing our surroundings in our mind as, you know, a set of objects and agents and narrations between objects that are fundamentally symbolic and causal in nature.

[00:41:32] François Chollet: This is exactly the process that lets us generalize so well and adapt so well to novelty on the fly.

[00:41:40] Host 3 (Y Combinator): I'm curious about India, the company as you're building it. We've all heard of the OpenAI founding story. And something that's always struck with me is just like both Sam and Greg say that it was a little odd in the early days because they didn't actually know what to do. It's sort of just like a bunch of people like hanging out in an apartment. And then I would love to hear kind of what's that been like for India? Like what did like the day one look like?

[00:42:03] Host 3 (Y Combinator): And just maybe for just people who are interested in starting these alternative approaches who don't have sort of a researchy background, how should they think about that? Yeah.

[00:42:11] François Chollet: So we started on day one with the symbolic learning vision. Like we basically knew that we wanted to do symbolic program synthesis that you wanted to create a new approach to machine learning where you replace parametric curves with the shortest possible symbolic models. And then the big question was, okay, so how do we find these models?

[00:42:31] François Chollet: We started from the base idea, which is still the idea that we're following today, which is that we are going to do deep learning guided program search. You have a symbolic search space to explore and it's big. It's in fact combinatorial. You're not going to make progress if you just use brute force. It's not going to scale. You have to break the combinatorial wall. And the way to do it is to add deep learning guidance.

[00:43:00] François Chollet: It's actually very similar to the principles that underlies something like AlphaGo or AlphaZero. That was our starting point. We also didn't have very clear ideas about how to build it. So we tried many different things. We tried many, many different ideas. And it took us half a year roughly to get to good foundations where we could start building a system that compounds.

[00:43:24] François Chollet: And I think that's what's really important when doing a lab like this, that you don't want to be in a situation where you're constantly trying something new. It's not reusing any learnings, any findings from the previous approaches. You want a compounding stack. You want to build reusable foundations and then the next layer and then the next layer. And of course, you want to be building onto the right foundation.

[00:43:48] François Chollet: So don't commit to the foundation layer too early, but also make sure that at some point you're building this compounding structure. And that's the situation that we're in now.

[00:43:58] Host 4 (Y Combinator): Is Arc3 the end or will there be an Arc4, 5, 6? Can you keep making it harder?

[00:44:04] François Chollet: Yeah, yeah. I think there will absolutely be Arc4 and Arc5. I mean, we're currently planning Arc5. The point of the ArcGIS benchmark series is not to say that, well, you know, here's this test. If you pass it, this is a GI. Instead, what we're trying to do is we are targeting the residual gap of fair capabilities.

[00:44:26] François Chollet: Like Frontier is advancing and we're saying, well, if you compare it to human abilities, there's all these tasks, all these things. It's now doing well. So we are going to create a benchmark to target that. And so it's a moving target, right? It's not fixed points, it's a moving target. There will be Arc4, which will be in the spirit of Arc3, but more focused on continual learning and curriculum learning at longer time scales.

[00:44:53] François Chollet: So you're going to have fewer games, but they're going to have way more levels. And the levels are going to be compounding, meaning that for each level, you need to reuse stuff that you've learned before. And then that's going to be Arc5. And I'm actually really, really excited with Arc5. It's very, very new and different. It's all about invention. And I mean, you will see what that means. Eventually, I expect we will run out of things to test.

[00:45:18] François Chollet: Like as we get closer to AGI, eventually there will be no measurable difference between human capabilities and particular human learning efficiency and Frontier AI. And when that happens, when it becomes effectively impossible to measure the gap, this is the AGI moment.

[00:45:36] Host 1 (Y Combinator): Well, then the machines will take over and then they will create ArcASI 1. Yes, ArcASI. And then it'll continue from there. Yeah. Yeah. If you had to put a guess, I mean, years, decades, months.

[00:45:50] François Chollet: My timeline to AGI, you know, if you just try to extrapolate from the current rate of progress and the amount of investment that's going into not just the LLM stack, but also like side ideas, side bets that might work out. Like, you know, India, for instance. I think we're probably looking at AGI 2030, early 2030s, most likely.

[00:46:16] François Chollet: So around the time that we're going to be releasing, like maybe Arc 6 or Arc 7, that's probably going to be AGI.

[00:46:25] Host 4 (Y Combinator): You guys are doing a different approach to LLMs. Do you think there's room for more startups to explore other new approaches? And are there any other ones that you think are promising but don't have time to explore yourself?

[00:46:37] François Chollet: Yeah, absolutely. I mean, there are many different approaches that you could try. I've said like compute is a great equalizer. I think if you look at the amount of compute and resources that we've thrown at deep learning and gradient descent and scaling that up, if you had thrown the same amount of investment into almost anything else, you would also have seen extremely exciting results. Like genetic algorithms, for instance. If you try to scale up genetic algorithms, I mean, I'm sure you can do incredible things with that.

[00:47:08] François Chollet: You could, in fact, probably do new science because that's based on search and search is the best fit for automating the scientific method. I think so right now there's also like approaches that build on top of the current stack with a slightly alternative like state space models, for instance. That's the XLSCM architecture.

[00:47:30] François Chollet: Like you can basically, you know, current frontiers, it's a stack of things and you can take any layer in the stack and try to propose an alternative. Like if you propose an alternative architecture, you can be doing, for instance, like, yeah, like more like recurrent models instead of transformers for the architecture. Or you can do even lower level. You're going to be like, okay, we're still going to be training parametric curves, but you're going to get rid of current descent. Right. We're going to use like search.

[00:47:59] François Chollet: Maybe you're going to do new evolution. That's the slower level. And the lowest level is the level where we're operating, where we're saying, well, actually, forget about curves. Forget about parametric learning. Forget about current descent. We're just going to do something completely different. And I think if you want to build optimal AI, you're kind of forced to go back to the foundation of the stack. It cannot be like one layer added on top of the pile.

[00:48:28] Host 2 (Y Combinator): So do you think for aspiring researchers to want to do a new neolab with different approach, they should be reading research papers from the 70s or 80s and go deeply in those with approaches that were not as invested nowadays?

[00:48:41] François Chollet: That is actually a great idea because earlier in the history of the AI research timeline, people were exploring more things and very different things. You've had this sort of like collapse of everything into one approach. It's actually kind of a bad idea. Consider that not too long ago, like about 20 years ago.

[00:49:03] Host 2 (Y Combinator): We had the collapse into SVMs too.

[00:49:05] François Chollet: Yeah. I mean, I wouldn't describe it as a collapse because there weren't that many people doing SVMs. And AI was a much, much smaller field back then. But there was this widespread understanding that neural networks were a failed approach, that neural networks didn't work. And it was a waste of time to keep trying that.

[00:49:25] Host 2 (Y Combinator): In the 90s, right?

[00:49:26] François Chollet: Yeah. Yeah. No, even in the late 2000s, this was a set of things. Basically, when I got into AI, people were telling me like, hey, neural networks, don't try that. I was like, yeah, but it looks a lot like what the brain is doing. Like, I'm interested in that. If everybody is working on something, you are discarding ideas that will actually turn out to be very proactive ideas. Right? And yeah, like back in the 70s, back in the 80s, people are trying more things.

[00:49:54] François Chollet: And I think genetic algorithms are actually a very good example of that. But I think this is an approach that has a tremendous amount of potential. But not too many people are looking into scaling it up deeply.

[00:50:07] Host 1 (Y Combinator): Are there any characteristics that you would be looking for? I mean, is it as simple as like, if there's a scaling law that could happen, then even if it's different? Or is that too, like, you know, thinking by analogy?

[00:50:21] François Chollet: I think you are looking for approaches that scale. Yeah. I think it's a non-starter. If you're working on something, but the only way to increase the capabilities of the system is to have human engineers and researchers spend time on it, it will not work. Because even if the idea is very clever and very elegant and works really well, capabilities are going to be bounded. They're going to be bounded by human investment. Right?

[00:50:47] François Chollet: You want to be in a setup where the system can improve its capabilities with no human in the loop, with no human bottleneck.

[00:50:54] Host 1 (Y Combinator): So you would say like, don't just do it the way we did it like 10 years ago. Do it with the idea that recursive self-improvement is baked in at the beginning.

[00:51:02] François Chollet: Yeah. Not necessarily recursive self-improvement because deep learning, for instance, is not recursively self-improving. But with the idea of scaling up with no human bottlenecks, you want to remove the human from the improvement loop. The great strength of deep learning is that the models got better and better simply by adding training, training compute and training data. I mean, it's a little bit of caricature because, of course, just adding these factors requires a lot of human involvement.

[00:51:30] François Chollet: But basically, that's the idea that you have this decoupling from the improvement curve and the amount of human effort that's needed to be injected into the system.

[00:51:39] Host 4 (Y Combinator): I guess, or human effort that's already happened. Because the LMs do actually require an enormous amount of human effort. It's just it was the human effort to build the internet and we'd already built it.

[00:51:47] François Chollet: Yeah. Actually, less and less now that we are doing training in interactive verifiable environments. Because then you only need a small amount of human effort to create the environment. And from that small amount of effort, you're creating exponentially more trained data. But at first, I think to sort of like prime the machine, you need this tremendous amount of human generated abstractions and coding in text data.

[00:52:15] François Chollet: And if you don't start from that, you cannot get the system into this loop.

[00:52:21] Host 1 (Y Combinator): Do you have any advice for me starting a open source project? Things to do, things not to do in the AI space? Because I am not sure how I signed up for this in the last 14 days. But I think I have, I don't know, on the order of like 10,000 to 30,000 people using GStack every day.

[00:52:42] François Chollet: That's wild. Yeah.

[00:52:44] Host 1 (Y Combinator): I don't know. Like, I have a job. I guess like, you know, what was it like to start Keras? And how did you keep maintaining it? What's a good maintainer? Like, what did you learn from that? I don't know. This might be a whole hour.

[00:52:57] François Chollet: I mean, lots of learnings from growing Keras. So right now, I'm less involved with it. There's a big team at Google that's working on it. And they're doing an amazing job.

[00:53:09] Host 1 (Y Combinator): So it is possible to not, you know, to put people together to like. It is possible to start something.

[00:53:14] François Chollet: It is possible to start something. That's a relief. And then get more people involved. And at some point, it becomes its own thing. And just, you know, it used to be your baby. But now it's all grown up. It's all adult. And going on is its own life. So if you ask me the factors that we made Keras successful, I mean, first of all, is that there was this big focus on making the API simple and intuitive. There was this big focus on usability. And this was inspired by Scikit-learn.

[00:53:44] François Chollet: Like Scikit-learn was sort of like the OG machine learning library for Python. And what made it successful was that it was so easy to get started with it. So at first, I was like, okay, I'm going to package all this functionality I've created. And there are really, really simple APIs. It's going to be like the Scikit-learn API. That was like the big idea. The focus on usability is not just making sure the API is simple. It's also making sure the entire onboarding experience is nice and easy.

[00:54:12] François Chollet: Like the docs should be very informative. You should, you know, the docs should be not just telling you about how to use this thing. They should actually be teaching you about the domain in the first place. Because the folks who land on your website, they're not going to be already deep learning experts. They're going to be people looking to maybe start using deep learning. And so you have to teach them not just how to use the tool, but what the tool is good for and the entire field around it.

[00:54:40] François Chollet: And then, you know, you have to put a lot of investment into community building. One thing we did a bit at Google, in fact, you know, Google made it kind of difficult, and I was sad about that, is hire your power users. Like hire your fans. This is a really, really good idea. Like find the most enthusiastic users from your community and just hire them on your team. Amazing. Yeah.

[00:55:07] François Chollet: And these are always the best people, right?

[00:55:11] Host 1 (Y Combinator): All right. Time to start gstack.org. Put in a bunch of my own money and then hire a bunch of people to work on it. That sounds good. I think you've been a leader and pioneer and we're so lucky to have you sit with us. There are people watching who are at the beginning of their, you know, adulthood even. Like they're certainly their professional careers or actually like people just around the world. They're like trying to understand like what does this mean as intelligence becomes broadly applicable?

[00:55:39] Host 1 (Y Combinator): Like what would you tell, you know, if you were 18 right now, what would you tell them?

[00:55:44] François Chollet: Yeah. I mean, there's a lot of people today who have very pessimistic, very negative takes about the rise in the accountability. They say, oh, you know, I'm going to be out of a job soon. And there's going to be mass unemployment. AI is just going to take over completely. And my take is actually, you know, the more you know, the more expertise you have, but things like programming, for instance, the better you're able to use and leverage these tools for your own benefit.

[00:56:14] François Chollet: And with the right kind of expertise, all this AI progress is actually empowerment. Like it's something that you can leverage for yourself. I mean, that's exactly what you did with your project, right? And yeah, more people should have this mindset of trying to learn as much as possible, not just about AI, but about the domain that they want to apply AI to. Right.

[00:56:36] François Chollet: So that they should seek to turn this new development into an opportunity, into a tool they can use for themselves to improve their own lives. I think that's the right mindset because, you know, you're not going to stop AI progress. I think it's too late for that. And so the next question is, okay, like AI progress is here. It's actually going to keep accelerating. How do you make use of it? How do you leverage? How do you ride a wave? That's the question to ask.

[00:57:03] Host 1 (Y Combinator): I wish we could keep going for a couple hours because I'm sure we could. Francois, thank you so much for spending time with us. Thanks so much for having me.

[00:57:10.780 --> 00:57:12.120] Thanks. Go to Versace. Thank you.