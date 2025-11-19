# [How End-to-End Learning Created Autonomous Driving 2.0: Wayve CEO Alex Kendall](https://www.youtube.com/watch?v=8x_O8BeGNTw)

**Podcast:** Training Data
**Date:** 2025-11-18
**Participants:** Pat Grady, Sonya Huang, Alex Kendall
**Region:** Western
**Video ID:** 8x_O8BeGNTw
**Video URL:** https://www.youtube.com/watch?v=8x_O8BeGNTw
**Transcript:** [View Transcript](./transcript.md)

---

# Podcast Summary: Alex Kendall, CEO of Wayve

### 1. Key Themes

### The Architectural Shift from AV 1.0 to 2.0: End-to-End Neural Networks Over Modular Hand-Coded Systems

The fundamental transformation in autonomous driving is moving from hand-engineered, modular systems requiring extensive infrastructure to a single end-to-end neural network with onboard intelligence. Alex Kendall explained: "When we started the company in 2017, the opening pitch in our C-deck was all about the classical robotics approach at the time was to take a perception, planning, mapping, control, essentially break down the autonomy problem into a bunch of different components and largely hand engineer them. And our pitch was that, okay, we think that the future of robotics is not going to be a system that's hand engineer to drive with a lot of infrastructure like high-definition maps. But instead, we thought that the future of robots would be intelligent machines that have the onboard intelligence to make their own decisions." [[00:02:01]](https://www.youtube.com/watch?v=8x_O8BeGNTw&t=1m51s)

This approach was deeply contrarian for years, as Kendall noted: "typical arguments were, look, it's not safe. It's not interpretable. You can't understand what it's doing or even simply, it doesn't make sense. We haven't heard of this AI thing." [[00:02:22]](https://www.youtube.com/watch?v=8x_O8BeGNTw&t=2m12s)

### Foundation Model Strategy for Embodied AI: One Intelligence Across Multiple Applications

Rather than building separate neural networks for each vehicle or application, Wayve is pursuing a single foundation model approach that can generalize across different vehicles, sensor configurations, and use cases. Kendall articulated: "our ambition is to be the embodied AI foundation model for all of the best fleets and manufacturers around the world. And to do that, unless we want to overload the company by building a separate neural network for each application, we need to be able to generalize. We need to be about it, amortize our cost over one large intelligence and about a very quickly adapt to each different application that our customers care about." [[00:00:05]](https://www.youtube.com/watch?v=8x_O8BeGNTw&t=0s)

This was demonstrated when they unveiled a vehicle with Nissan in Tokyo: "Just four months earlier, was the first time we'd even driven in Tokyo and got hands on this vehicle. Four months later, we were having media driving the car, experience it, and that was a new country and a new vehicle for us." [[00:21:41]](https://www.youtube.com/watch?v=8x_O8BeGNTw&t=21m31s)

### Automotive OEM Partnership as Path to Scale: Software Integration Over Vertical Integration

Wayve's go-to-market strategy focuses on partnering with major automotive manufacturers rather than building vertically integrated robot taxis. Kendall explained the rationale: "there are 90 million cars built each year. And so some manufacturers that are building the autonomy systems themselves like Tesla built a couple of million, but the vast majority of the market, I think there's an opportunity partner to work with some of these innovative platforms and to bring our AI to market to make these autonomous products possible... by avoiding retrofitting our own hardware on these vehicles, by putting them in natively as a software integration, we can move fast at scale, we can build low-cost vehicles that can be homologated all around the world. And this is going to be the path to see tens and hundreds of thousands of robot taxis rolled out around the world at an affordable price." [[00:22:11]](https://www.youtube.com/watch?v=8x_O8BeGNTw&t=22m1s)

### 2. Contrarian Perspectives

### Safety Through Intelligence, Not Constraints: Embracing Complexity Over Interpretability

While the industry demanded "interpretable" and "constrained" AI systems for safety, Kendall argues that true intelligence requires embracing complexity. He stated: "I think if you have the ambition to build any intelligent machine, I think it's naive to think you can build a complex intelligent machine and actually make it you know, let's say, strictly interpretable to the point where you can point to a single line of code or a single thing that causally made the outcome occur. The beauty of intelligent machines is that they are so wonderfully complex." [[00:06:01]](https://www.youtube.com/watch?v=8x_O8BeGNTw&t=5m51s)

He noted that even today, "I still see a lot of folks still say, yes, we need into an AI. They've brought the big tech narrative around the future of AI, but they say things like we need into an AI with hard constraints or with safety guarantees. And still, there's still can be some belief that some hybrid approach is the way to go, where you want to try and take a rules-based stack and an end-to-end lens stack, but often these approaches can get the worst of both worlds or just ag costs and complexity." [[00:08:43]](https://www.youtube.com/watch?v=8x_O8BeGNTw&t=8m33s)

### Camera-Plus-Radar-Lidar Is Not About the Sensor Debate, It's About Superhuman Performance

Contrary to the heated Twitter debates about sensor fusion, Kendall dismisses this as "the wrong debate to be having. It's not the frontier question." [[00:23:56]](https://www.youtube.com/watch?v=8x_O8BeGNTw&t=23m46s) His perspective: "for a driver assistance system, camera only can work for a human level driverless system or of course, I should clarify, 90 something you can look at different stats, but 95% or above accidents unfortunately are caused by human error. So not only can you be human level, but you can eliminate a lot of human attention and accidents caused by that. But there are still accidents that to be able to solve would require perception capabilities that could be on vision. And if we want to tackle that long tail, there are many ways to solve it. One of the ways would be to bring in some other sensing modalities like radar and light hours." [[00:25:01]](https://www.youtube.com/watch?v=8x_O8BeGNTw&t=24m51s)

The industry has "really coalesced around a common architecture of a surround camera, surround radar, and a front-facing light-air stack. Now, this costs under $2,000. So it's automotive grade components, not the retrofit robot taxi components you see today." [[00:24:02]](https://www.youtube.com/watch?v=8x_O8BeGNTw&t=23m52s)

### Resource Constraints Drive Innovation: Working Lean Forces Efficiency Breakthroughs

Rather than viewing limited resources as a handicap, Kendall sees them as catalysts for innovation: "working under resource constraints as a forced out team to develop so many innovations, I'd also call out just the workflow. Because in traditional robotics, when you're tuning parameters or algorithms or designing geometric maps and things like this, there's very well established cultures and workflows. But our team, when we have 50 model developers working on one main production model, or when we have an end-to-end net that we need to understand and interest back to, or even the way that we deploy these systems to simulation or to the road and feedback, we've developed the entire culture from the ground up way that's been developed for embodied AI for end-to-end deep learning for driving." [[00:17:26]](https://www.youtube.com/watch?v=8x_O8BeGNTw&t=17m16s)

### 3. Companies Identified

**Wayve** - Autonomous driving software company selling AI driving stacks to automotive OEMs. Mentioned for pioneering end-to-end neural network approach to autonomous driving since 2017, achieving rapid generalization across 500+ cities globally, and partnering with major manufacturers like Nissan. "we've driven in over 500 cities this year and so when you're driving at that level of scale, of course you see things that you've never seen before." [[00:28:33]](https://www.youtube.com/watch?v=8x_O8BeGNTw&t=28m23s)

**Tesla** - Electric vehicle manufacturer with Full Self-Driving (FSD) software. Mentioned as validation of the consumer autonomous driving experience and as one of few manufacturers building their own autonomy systems. "Tesla FSD is just such a game-changing product. And you know, my friends have it. It's just they can't imagine driving any other way." [[00:23:02]](https://www.youtube.com/watch?v=8x_O8BeGNTw&t=22m52s)

**Nissan** - Major automotive manufacturer. Mentioned as a key Wayve partner choosing their AV stack. "a couple of weeks ago, in September this year, we unveiled a vehicle to media with Nissan in Tokyo. Just four months earlier, was the first time we'd even driven in Tokyo and got hands on this vehicle." [[00:21:41]](https://www.youtube.com/watch?v=8x_O8BeGNTw&t=21m31s)

**Nvidia** - GPU and AI computing company. Mentioned for providing next-generation automotive compute platforms. "some of the next generation compute, for example, the Nvidia Thor that our next year in development vehicle is going to be with will be large enough to run it on board." [[00:32:05]](https://www.youtube.com/watch?v=8x_O8BeGNTw&t=31m55s)

### 4. People Identified

**Alex Kendall** - CEO and founder of Wayve, former PhD researcher in embodied AI. Mentioned for pioneering end-to-end neural network approach to autonomous driving since 2017, building Wayve into a leader in AV 2.0 architecture, and establishing partnerships with major global automotive manufacturers. "When we started the company in 2017, the opening pitch in our C-deck was all about the classical robotics approach at the time... our pitch was that, okay, we think that the future of robotics is not going to be a system that's hand engineer to drive with a lot of infrastructure like high-definition maps." [[00:02:01]](https://www.youtube.com/watch?v=8x_O8BeGNTw&t=1m51s)

### 5. Operating Insights

### Culture as Product Engine: Mission-Driven Conviction Under Constraints

Kendall emphasized that their entire organizational culture was purpose-built for end-to-end deep learning: "The data infrastructure, the simulation, the safety licensing before we put systems on the road, this is not being a hedge or a side-bet for us, but this is the entire essence of our culture. And I think doing this under resource constraints and doing this with full mission-driven conviction has led to a bunch of interesting innovations that look getting to where we are today, everything is about iteration speed." [[00:18:15]](https://www.youtube.com/watch?v=8x_O8BeGNTw&t=18m5s)

### Four Pillars of Performance Improvement

Kendall outlined his framework for driving performance: "I usually talk about four factors that drive performance. There's of course data and compute. But then also the algorithmic capabilities and the embodiment, the what is the hardware and capability on the robots. And I think we need to push all four." [[00:35:26]](https://www.youtube.com/watch?v=8x_O8BeGNTw&t=35m16s) On the algorithmic side, he highlighted measurement as critical: "How do you actually measure and quantify these systems? How do you respond quickly? Find regressions? Be able to really have a simulator that closes the real-world gap at scale and can run efficiently." [[00:35:42]](https://www.youtube.com/watch?v=8x_O8BeGNTw&t=35m32s)

### Learning from Automotive Industry: Reliability, Efficiency, Brand Differentiation

The transformation from AI research lab to product company came from automotive partnerships: "I think some of the main things I'll call out have been efficiency and reliability, the difference between technology and a product will be some of the main themes. I mean, the level of reliability required, but also the level of quality that is seen to really robustly prove these systems out before deployment and the pride that these companies take in that has been exceptional." [[00:19:52]](https://www.youtube.com/watch?v=8x_O8BeGNTw&t=19m42s) They also learned about "the sense of brand differentiation and the desire for do you want your car to drive? How can your driving personality really match the brand's preferences?" [[00:20:18]](https://www.youtube.com/watch?v=8x_O8BeGNTw&t=20m8s)

### 6. Overlooked Insights

### The Exponential Data Efficiency Curve Across Geographies

While Kendall mentioned it briefly, there's a hugely significant insight about data efficiency improvements: "We needed hundreds of hours of data to be able to drive within 10% of our frontier performance. But then when we went to Europe and to Germany, of course, we'd already learn to drive on the right side of the road, coming to the US would learn to do right turns of red lights. We then came into Germany... it gets more efficient each time with exponentially less data in each new market because you've seen some of those things before." [[00:29:31]](https://www.youtube.com/watch?v=8x_O8BeGNTw&t=29m21s) This suggests that the marginal cost of expanding to new markets decreases exponentially as the foundation model matures—a powerful economic moat that compounds over time.

### Vision-Language-Action Models as Regulatory and Safety Infrastructure

Kendall briefly mentioned their 2021 work on "lingo, which is the first vision language action model in autonomous driving" [[00:30:41]](https://www.youtube.com/watch?v=8x_O8BeGNTw&t=30m31s) that "could not only drive a car, see the world driver car, but also converse and language." [[00:30:53]](https://www.youtube.com/watch?v=8x_O8BeGNTw&t=30m43s) Beyond the product features, he noted: "you could imagine regulators or our engineering team conversal the system in language to really diagnose why it's doing what it's doing or get it to explain its reasoning." [[00:31:44]](https://www.youtube.com/watch?v=8x_O8BeGNTw&t=31m34s) This suggests that VLA models may become essential infrastructure for regulatory approval and safety certification of embodied AI systems—a non-obvious requirement that could become a significant barrier to entry as physical AI scales.