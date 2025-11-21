# [No Priors Ep. 141 | With Sunday Robotics Co-Founders Tony Zhao and Cheng Chi](https://www.youtube.com/watch?v=4-VzXoZqAH0)

**Podcast:** No Priors
**Date:** 2025-11-20
**Participants:** Unknown Host, Unknown Guest, Cheng Chi, Tony Zhao
**Region:** Western
**Video ID:** 4-VzXoZqAH0
**Video URL:** https://www.youtube.com/watch?v=4-VzXoZqAH0
**Transcript:** [View Transcript](./transcript.md)

---

# Podcast Summary: Sundai Robotics with Tony Zhao and Cheng Chi

## 1. Key Themes

### The AI Robotics Inflection Point: Between GPT and ChatGPT Moments

The field of AI robotics has reached a critical juncture where the fundamental algorithms work, but haven't yet scaled to create compelling consumer products. "I think we're kind of in between the GPD moment and the Chad GPD moment. In the context of LMS, what it means is that it seems like we have a recipe that can be scout, but we haven't scaled up yet." [[00:01:21]](https://www.youtube.com/watch?v=4-VzXoZqAH0&t=1m11s) Tony explains that academia has reached consensus on manipulation methods, with clear signs of life in the algorithms, but the industry needs to prove that scaling will improve performance as it did in other AI fields.

The old paradigm of classical robotics - the "sense plan act modular approach" - required human-designed interfaces for each specific task and environment. "A paper is you design a task, design environment, and you design interfaces. And then you produce engine work for that specific task. But once you move on to the next task, you throw out your code, all your work and you start over again." [[00:02:42]](https://www.youtube.com/watch?v=4-VzXoZqAH0&t=2m32s) Cheng explains this created a pattern where there was no synergy between different systems, causing the field to run in loops.

### Data Scale and Quality as the Primary Moat

Sundai has achieved unprecedented scale in robotics training data through innovative collection methods. "At this point, we are almost 10 million trajectories being collected in the wild. And those trajectories are not just like, oh, pick up a cup. These long trajectories with like walking with navigation and then like doing this long horizon tasks." [[00:19:23]](https://www.youtube.com/watch?v=4-VzXoZqAH0&t=19m13s) This represents a magnitude beyond what exists elsewhere in the industry.

The company's approach to data quality has evolved significantly. "Data quality really matters. I think we know I always knew data quality matters. But once you scale it up, like it really matters." [[00:24:09]](https://www.youtube.com/watch?v=4-VzXoZqAH0&t=23m59s) Cheng emphasizes that diversity of behavior and hardware failures in real-world environments require constant monitoring and substantial engineering effort. They've built automatic calibration processes and software systems to detect glove malfunctions before data collection, eliminating the need for humans to manually review data quality.

### Full-Stack Integration as Competitive Advantage

Building everything in-house enables rapid iteration that would be impossible with partners. "When you make these as scale right now, we have more than 500 people using these golfs in the wild. Like all the things that could go wrong will go wrong." [[00:38:39]](https://www.youtube.com/watch?v=4-VzXoZqAH0&t=38m29s) Tony describes how their data collection glove has gone through approximately 100 iterations (V0 to V5, with ~20 iterations per version).

The company's philosophy centers on system-level optimization rather than component optimization. "Right now we don't like there's not a existing general purpose home robot out there. And we don't really know what the interface of different system is like what is even good. And in that case, if you're working with the partner, it's actually really hard for them to understand your standard of good because your standard of good is changing all the time." [[00:27:14]](https://www.youtube.com/watch?v=4-VzXoZqAH0&t=27m4s) This uncertainty makes external partnerships impractical, as standards evolve continuously.

## 2. Contrarian Perspectives

### Human Data Collection Outperforms Teleoperation

The team initially worried that glove-based data collection would produce lower quality data than traditional teleoperation. "In the beginning, we worried that the data from glove or only like data has higher quantity, but lower quality compared to teleop. Because of teleop, you're using exactly the same hardware software stack between training and testing is perfectly distribution match." [[00:19:53]](https://www.youtube.com/watch?v=4-VzXoZqAH0&t=19m43s) 

However, they discovered the opposite: "This glove form factor encouraged people to do more text version, more natural movement. And those actually result in a more intelligent behavior on the modeling side. But in terms of data quality, we don't really see a difference in terms of how much like there's a gap between teleop and glove data." [[00:20:10]](https://www.youtube.com/watch?v=4-VzXoZqAH0&t=20m0s) The more natural, dexterous movements from gloves actually produced superior training data after 20+ engineering iterations to bridge the distribution gap.

### Reinforcement Learning Won't Scale for Manipulation

While the industry debates between imitation learning and RL approaches, Sundai has a clear position based on sample efficiency and simulation difficulty. "We see a lot of great promise for RL in local motion. And you know, we think that will continue to be true for local motion. So what we see really felt like RL is a method is very powerful. But it is much less sample efficient compared to imitation learning." [[00:21:03]](https://www.youtube.com/watch?v=4-VzXoZqAH0&t=20m53s)

The key insight is about what's actually hard to simulate: "For the case of local motion, you only need to worry about rigid body dynamics and rigid body contact between the robot and the ground... But for manipulation, it's kind of hard for us to imagine like have does actually the same amount of diversity and the distribution of real object in terms of matching both appearance and physical properties." [[00:21:23]](https://www.youtube.com/watch?v=4-VzXoZqAH0&t=21m13s) Tony elaborates that grasping a transparent cup with orange juice is "ridiculously hard to simulate" in terms of hand deformation, refraction, and rendering, but the actual behavior - moving your hand and closing with appropriate force - is easy to learn from demonstrations. [[00:23:14]](https://www.youtube.com/watch?v=4-VzXoZqAH0&t=23m4s)

### AI-Enabled Hardware Can Be Intentionally "Worse"

Traditional robotics optimizes for precision, speed, and stiffness because industrial robots are "blind" - following pre-programmed trajectories. "Traditionally, most robots are designed for industrial use cases. And the robot are very fast. They are very stiff and never precise." [[00:21:08]](https://www.youtube.com/watch?v=4-VzXoZqAH0&t=20m58s)

But vision-based AI fundamentally changes the hardware requirements: "Because of the brakes we have in AI, like now robots have eyes. So it can actually correct this own mechanical and hardware inaccuracies. So that kind of opened up a new different space of design." [[00:21:28]](https://www.youtube.com/watch?v=4-VzXoZqAH0&t=21m18s) This allows them to use "low cost actuators that's cheap, that's compliant, but they're in precise" while achieving sufficient accuracy through AI correction. The result is robots that are mechanically inherently safe and compliant while maintaining task performance - a complete inversion of traditional robotics design philosophy.

## 3. Companies Identified

### Sundai
**Description:** AI robotics company building general-purpose home robots  
**Why Mentioned:** Founded by the podcast guests, represents cutting-edge approach to home robotics through full-stack integration of data collection, AI training, and hardware development  
**Quotes:** 
- "What we believe in is that if the robot is cheap, safe and capable, everyone will want our robot. And we see a future where we have more than 1 billion of these robots in people's homes within the decades." [[00:00:13]](https://www.youtube.com/watch?v=4-VzXoZqAH0&t=3s)
- "The next step of our plan is to have a better group program, 2026. And what it means is that for people who sign up that we selected, they will have a real robot in their home and it will start doing chores for you." [[00:28:18]](https://www.youtube.com/watch?v=4-VzXoZqAH0&t=28m8s)
- On cost: "What we see is that as we get the scale to a few thousand units, we can drastically reduce the material cost, likely under 10k." [[00:29:56]](https://www.youtube.com/watch?v=4-VzXoZqAH0&t=29m46s)

## 4. People Identified

**Note:** While the guests mentioned their collaboration and meeting each other through their research, no other individuals were specifically called out for their excellence in this conversation.

## 5. Operating Insights

### Build Infrastructure Before Research

Sundai deliberately inverted the typical startup approach of rapid research iteration. "When there is data scarcity, it is really easy to come up with like cute fancy research ideas that doesn't end up scaling very well. And this is why when we build a company, we actually focus on the infrastructure and the scalable data pipeline operations before we start to really dive into research, which we only started to do like three months ago." [[00:26:26]](https://www.youtube.com/watch?v=4-VzXoZqAH0&t=26m16s) This prevented them from pursuing research directions that wouldn't scale to production.

### Design for Ubiquity, Not Laboratory Perfection

When making product design decisions, the team asks what the robot should look like if you see it every single day. "If you start from the most surface level, which is design of the robots, when we design it, we think about what should the robot look like if it is ubiquitous? You need to see it every single day. What should it look like?" [[00:12:22]](https://www.youtube.com/watch?v=4-VzXoZqAH0&t=12m12s) Their answer: "We really think the robot should have a face. It should have a cute face, and it should be very friendly. So instead of like a terminator doing your dishes, we want the robot to feel like it's out of a cartoon movie." [[00:12:41]](https://www.youtube.com/watch?v=4-VzXoZqAH0&t=12m31s)

### Simplify with Constraints, Not Feature Creep

The team's approach to hardware design centers on aggressive simplification. "The core motivation for us is how can we build a useful robot as soon as possible? So whenever we see something that we can accelerate it with simplification, we'll go simplify that." [[00:13:11]](https://www.youtube.com/watch?v=4-VzXoZqAH0&t=13m1s) Their three-finger hand design exemplifies this: "Most of the time when we use those fingers, we use it together. Let it be like grasping a handle, let it be opening the dishwasher. So it really doesn't make sense to add the cost, like multiply by three X to have separate it into three." [[00:13:33]](https://www.youtube.com/watch?v=4-VzXoZqAH0&t=13m23s)

### Automatic Quality Control Over Manual Review

At scale, human review of data quality becomes impossible. "We have our own way of calibrating the glove before we ship it out. And we have this whole software system to catch if a something is broken on the glove. And we can detect it automatically... And we don't need a human to be staring at the data to know that something is wrong." [[00:24:39]](https://www.youtube.com/watch?v=4-VzXoZqAH0&t=24m29s) Building automated quality control systems was essential to scaling to 500+ data collectors.

## 6. Overlooked Insights

### The Sock Folding Force Closure Problem Reveals a Fundamental Limitation of Teleoperation

While discussing dexterous tasks, Tony mentioned something profound about force feedback: "The Saga is a very good example that when you're trying to fold it, your two fingers can clutch. And that forms a, or we call it a force closure. You have a closed loop for the force. And if you roll a stiff, you can apply infinite amount of force at it and doesn't look like anything." [[00:36:23]](https://www.youtube.com/watch?v=4-VzXoZqAH0&t=36m13s)

He earlier explained that "these days, there's not a good tally operation system that can let you feel how much force the robot is feeling. So basically when you're tally operating, your hand is numb." [[00:36:03]](https://www.youtube.com/watch?v=4-VzXoZqAH0&t=35m53s) This suggests that the entire field's reliance on teleoperation for "high-quality" training data may actually be systematically producing overly aggressive robot behaviors because operators can't feel force feedback. Glove-based collection, despite seeming less precise, captures more natural force application because the human actually feels resistance. This could explain why many teleoperated robots appear jerky or aggressive in their movements - the training data itself encodes unnatural force profiles.

### Clothing Cost as the Dominant Variable in Early-Stage Hardware

When discussing robot costs ranging from $6,000 to $20,000, Tony revealed: "This is actually pretty interesting that the big difference here is not like, oh, we find a better actuator. They're usually the same actuators. They're like very low cost. But actually, it's the clotting of the robots. When you're trying to make them at low scale, it's just really expensive. Like the clottings are like a few thousand dollars to make." [[00:29:22]](https://www.youtube.com/watch?v=4-VzXoZqAH0&t=29m12s)

This insight suggests that investors and competitors evaluating robotics companies should focus less on actuator choices (which everyone has access to) and more on manufacturing scale and design-for-manufacturing capabilities. The exterior housing and aesthetic elements - typically considered superficial - actually represent the majority of the cost variance in prototype-stage robots. This explains why so many robotics demos show exposed mechanical components: it's not just an aesthetic choice, but a cost optimization for pre-scale production.