# [Fully autonomous robots are much closer than you think – Sergey Levine](https://www.youtube.com/watch?v=48pxVdmkMIE)

**Podcast:** One-off Episodes
**Date:** 2025-09-12
**Participants:** Sergey Levine, Dwarkesh Patel
**Region:** Western
**Video ID:** 48pxVdmkMIE
**Video URL:** https://www.youtube.com/watch?v=48pxVdmkMIE
**Transcript:** [View Transcript](./transcript.md)

---

# Podcast Summary: Sergey Levine on Physical Intelligence and Robotics

## 1. Key Themes

### The Foundation Model Approach to Robotics is Just Beginning
Physical Intelligence aims to build robotic foundation models that can control any robot to perform any task. Sergey emphasizes they've only laid the basic building blocks: "What we're doing at Physical Intelligence right now is really the very, very early beginnings. Just like putting in place the basic building blocks on top of which we can then tackle all these really tough problems." [[00:01:14]](https://www.youtube.com/watch?v=48pxVdmkMIE&t=1m4s)

The ultimate vision is far more ambitious than current demos suggest: "What you really want from a robot is not to tell it, hey, please fold my t-shirt. What you want from a robot is to tell it, hey, robot, you're now doing all sorts of home tasks for me. I like to have dinner made at 6 p.m. I wake up and go to work at 7 a.m...And by the way, check in with me every Monday to see what I want you to pick up when you do the shopping. That's the prompt. And then the robot should go and do this for six months, a year. That's the duration of the task." [[00:02:46]](https://www.youtube.com/watch?v=48pxVdmkMIE&t=2m36s)

### The Data Flywheel Starts Before Full Capability
Rather than waiting for complete autonomous capability, the key milestone is getting robots deployed in useful but limited capacities where they can learn on the job. Sergey explains: "To me, what I tend to think about a lot in terms of timelines is not the date when it will be done, but the date when it will, when the flywheel starts, basically." [[00:04:43]](https://www.youtube.com/watch?v=48pxVdmkMIE&t=4m33s)

His median estimate is that robots doing practically useful work could emerge within 1-2 years, with the flywheel fully spinning in approximately 5 years: "I think five is a good median" for when robots can autonomously run a household. [[00:10:43]](https://www.youtube.com/watch?v=48pxVdmkMIE&t=10m33s)

The flywheel advantage for robotics is unique: "If you're folding the t-shirt and you messed up a little bit, it's pretty obvious. You can reflect on that, figure out what happened and do it better next time." This is easier than with LLMs where "if you answer a question, you just answered it wrong. It's like, well, it's not like you can just go back and tweak a few things." [[00:07:46]](https://www.youtube.com/watch?v=48pxVdmkMIE&t=7m36s)

### Prior Knowledge from Foundation Models is the Key Unlock
The breakthrough enabling modern robotics is leveraging prior knowledge from pre-trained vision-language models. Sergey states: "If I had to summarize in one sentence, the big benefit that recent innovations in AI give to robotics is really that prior, the ability to leverage prior knowledge." [[00:30:30]](https://www.youtube.com/watch?v=48pxVdmkMIE&t=30m20s)

This prior knowledge serves multiple purposes. Robots can now learn from language instructions, not just teleoperation: "Once the model was good enough by supervising it not just with low level actions, but actually literally instructing it through language. Now you need a certain level of competence before you can do that. But once you have that level of competence, just standing there and telling the robot, okay, now, now pick up the cup, put the cup in the sink...just with words. Already actually gives the robot information that it can use to get better." [[00:15:14]](https://www.youtube.com/watch?v=48pxVdmkMIE&t=15m4s)

## 2. Contrarian Perspectives

### Robotics May Be Easier to Deploy Than Autonomous Driving
Unlike autonomous driving where mistakes have severe consequences, many manipulation tasks allow for error recovery and learning: "For a lot of tasks that we want to do with robotic manipulation, there's potential to make mistakes and correct those mistakes. And when you make a mistake and correct it, well, first you've achieved the task because you've corrected, but you've also gained knowledge that allows you to avoid that mistake in the future." [[00:20:15]](https://www.youtube.com/watch?v=48pxVdmkMIE&t=20m5s)

He contrasts this with driving: "You would not trust your teenage child to learn to drive just on their own, just drop them in the car and say, like, go for it...But if you want somebody to clean the dishes, like dishes can break too, but you would probably be okay with a child trying to do the dishes without somebody constantly, like, you know, sitting next to them with a break, so to speak." [[00:19:43]](https://www.youtube.com/watch?v=48pxVdmkMIE&t=19m33s)

### Video Prediction Models Miss the Point - Embodied Action Provides Focus
While many believe video prediction is the path to world models, Sergey argues that having a task to accomplish fundamentally changes what information matters: "If you imagine pointing a camera outside this building, there's the sky, there's the clouds are moving around the water, cars driving around people. If you want to predict everything that'll happen in the future, you can do so in many different ways...If you want to really predict everything that's going on in that scene, there's just so much stuff that even if you're doing a really great job and capturing like 100% of something, by the time you get to everything else, like ages will have passed." [[00:34:26]](https://www.youtube.com/watch?v=48pxVdmkMIE&t=34m16s)

The solution is embodied AI with purpose: "When you have a robot, that robot is actually trying to do a job. So it has a purpose. And its perception is in service to fulfilling that purpose. And that is like a really great focusing factor." [[00:35:38]](https://www.youtube.com/watch?v=48pxVdmkMIE&t=35m28s)

### Robotics Models Will Make Better Knowledge Work Models
Contrary to the assumption that robotics and knowledge work require separate models, Sergey believes robotics training will improve all AI capabilities: "I really hope that they will actually be the same. And obviously I'm extremely biased. I love robotics. I think it's like it's very fundamental to AI, but I think that it's optimistically that it's actually the other way around that the robotics element of the equation will make all the other stuff better." [[00:59:53]](https://www.youtube.com/watch?v=48pxVdmkMIE&t=59m43s)

His reasoning: "Understanding the physical world at a very deep fundamental level, at a level that goes beyond just what we can articulate with language can actually help you solve other problems. And we experience this all the time. When we talk about abstract concepts, we say, this company has a lot of momentum...We experience the world in a particular way in our subjective experience, shapes how we think about it in very profound ways." [[01:00:40]](https://www.youtube.com/watch?v=48pxVdmkMIE&t=1h0m30s)

### Moravec's Paradox Explains Why Simple Context is Sufficient
Despite having only one second of visual context, their robots can execute complex multi-step tasks. Sergey explains this through Moravec's Paradox: "If you are an Olympic swimmer, and you're swimming with perfect form, and you're like right there in the zone, like people even say like, it's in the moment...you've practiced it so much, you've baked it into your neural network in your brain, that you don't have to think carefully about keeping all that context, right? So it really is just Morvix Paradox manifesting itself." [[00:44:59]](https://www.youtube.com/watch?v=48pxVdmkMIE&t=44m49s)

The implication: "The things that we take for granted, like picking up objects, seeing, you know, perceiving the world, all that stuff. Those are all the heart problems in AI, and the things that we find challenging, like playing chess and doing calculus, actually are often the easier problems." [[00:44:10]](https://www.youtube.com/watch?v=48pxVdmkMIE&t=44m0s)

## 3. Companies Identified

### Physical Intelligence
Sergey's company building robotic foundation models. Description: "Physical Intelligence aims to build robotic foundation models. And that basically means general purpose models that could in principle control any robot to perform any task." [[00:00:31]](https://www.youtube.com/watch?v=48pxVdmkMIE&t=21s)

Current capability demonstration: "We can get a robot that will fold laundry and that will go into a new home and try to clean up the kitchen." [[00:01:11]](https://www.youtube.com/watch?v=48pxVdmkMIE&t=1m1s) The company has been operating for one year and is focused on industrial-scale deployment rather than pure research.

### LaboBox
Data collection company for robotics training. Description: Provides teleoperation services and robotics training data at scale. "LaboBox can get you millions of episodes of robotics data for every single robotics platform and sub-task that you want to train on." [[00:16:17]](https://www.youtube.com/watch?v=48pxVdmkMIE&t=16m7s)

Their output consists of synchronized camera streams and robot movement data packaged for training: "What you're looking at is actually the final output that is then delivered to the labs which then they used to train the models." [[00:16:57]](https://www.youtube.com/watch?v=48pxVdmkMIE&t=16m47s)

### Hudson River Trading
High-frequency trading firm mentioned as sponsor. Uses sophisticated machine learning for market prediction, working with real order book data and training models to predict price movements. [[00:52:05]](https://www.youtube.com/watch?v=48pxVdmkMIE&t=51m55s)

## 4. Operating Insights

### Scale the Right Axes, Not Just Volume
When asked why not immediately 100x data collection, Sergey explains strategic scaling: "The challenge here is in understanding which axes of scale contributes to which axis of capability...If we wanted to expand capability horizontally, meaning like the robot knows how to do 10 things now and I'd like it to do 100 things later, that can be addressed by just directly horizontally scaling what we already have. But we want to get robots to a level of capability where they can do practical useful things in the real world and that requires expanding along other axes too." [[00:24:11]](https://www.youtube.com/watch?v=48pxVdmkMIE&t=24m1s)

The insight: figure out which specific capabilities need improvement (robustness, speed, edge case handling) before scaling data collection massively.

### Human-Robot Collaboration Accelerates Learning More Than Pure Autonomy
Rather than waiting for full autonomy, design for human-in-the-loop deployment: "Robot plus human is much better than just human or just robot...when it's robot plus human, now there's a lot more potential for the robot to actually learn on the job but acquire new skills." [[00:14:44]](https://www.youtube.com/watch?v=48pxVdmkMIE&t=14m34s)

The model can learn from multiple signal types: "Learning is not, for these systems is not just learning from real action. It's also learning from words, eventually be learning from observing what people do, from the kind of natural feedback that you receive when you're doing a job together with somebody else." [[00:15:44]](https://www.youtube.com/watch?v=48pxVdmkMIE&t=15m34s)

### Representations Matter More Than Raw Scale for Efficiency
When discussing inference constraints across latency, context, and model size: "Representing your context in the right form that captures what you really need to achieve your goal, and otherwise kind of discards all down to such stuff. I mean, that's a really important thing...multimodality has so much more to it than just like ImagePlus text." [[00:48:33]](https://www.youtube.com/watch?v=48pxVdmkMIE&t=48m23s)

The practical implication: invest heavily in representation learning for temporal information, spatial information, and planning rather than just scaling model parameters.

## 5. Overlooked Insights

### Hardware Costs Have Dropped 100x Due to AI Software, Not Just Manufacturing
Sergey reveals a stunning cost trajectory that's rarely discussed: "When I started working in robotics in 2014, I used a very nice research robot called a PR2 that cost $400,000 to purchase. When I started my research lab at UC Berkeley, I bought robot arms that were $30,000, the kind of robots that we are using now at physical intelligence, each arm cost about $3,000, and we think they can be made for a small fraction of that." [[00:13:02]](https://www.youtube.com/watch?v=48pxVdmkMIE&t=12m52s)

Crucially, this isn't just manufacturing scale—it's algorithmic: "AI also makes robots more affordable and lowers the requirements on the hardware...Traditional robots and factories, they need to make motions that are highly repeatable, and therefore it requires a degree of precision and robustness that you don't need if you can use cheap visual feedback." [[00:13:53]](https://www.youtube.com/watch?v=48pxVdmkMIE&t=13m43s)

This suggests a compounding advantage where better AI enables cheaper hardware which enables more robots which enables better AI—a feedback loop that's just beginning.

### The Real Sim-to-Real Gap is About Objective Functions, Not Fidelity
When discussing why simulation hasn't revolutionized robotics despite high-quality simulators, Sergey identifies a subtle but crucial insight: "When a pilot is using a simulator learned to fly an airplane, they're extremely goal-directed. So their goal in life is not to learn to use a simulator. Their goal in life is to learn to fly the airplane...And when we train models on data from multiple different domains, the models don't know that they're supposed to solve a particular task. They just see like, hey, here's one thing I need to master. Here's another thing I need to master." [[01:04:02]](https://www.youtube.com/watch?v=48pxVdmkMIE&t=1h3m52s)

The implication: the blocker isn't simulation quality but getting models to optimize for real-world performance while training in simulation. The key to using synthetic data is "to get really good at using real data, understand what's up with the world. And then now you can fruitfully use all this stuff." [[01:06:01]](https://www.youtube.com/watch?v=48pxVdmkMIE&t=1h5m51s)

This completely reframes the sim-to-real problem from a graphics/physics fidelity question to a meta-learning and objective specification question.