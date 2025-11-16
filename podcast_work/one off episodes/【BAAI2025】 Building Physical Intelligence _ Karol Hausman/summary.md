# [【BAAI2025】 Building Physical Intelligence | Karol Hausman](https://www.youtube.com/watch?v=5H2UrJ2N3t0)

**Podcast:** One-off Episodes
**Date:** 2025-06-07
**Participants:** Karol Hausman
**Region:** Western
**Video ID:** 5H2UrJ2N3t0
**Video URL:** https://www.youtube.com/watch?v=5H2UrJ2N3t0
**Transcript:** [View Transcript](./transcript.md)

---

# Podcast Summary: Building Physical Intelligence with Karol Hausman

## 1. Key Themes

### **Foundation Models Enable Multi-Robot Generalization Through Pre-training and Post-training**
The breakthrough in robotics comes from vision-language-action models that can control multiple robot types through a two-stage training approach. Hausman explains: "For Pi0, we had pre-training data that consisted of 10,000 hours. So many different tasks across many different robots... But then we would go to the next stage called post-training, where we would collect orders of magnitude less data of high quality around 20 hours of data to kind of get this model to behave exactly like we wanted." [[00:14:27]](https://www.youtube.com/watch?v=5H2UrJ2N3t0&t=14m17s) The quantitative results show this approach dramatically outperforms either approach alone - models with both pre-training and post-training achieved significantly higher success rates than models with just curated data or no post-training. [[00:15:41]](https://www.youtube.com/watch?v=5H2UrJ2N3t0&t=15m31s)

### **Internet-Scale Knowledge Transfer to Physical Actions**
The Robotic Transformer 2 demonstrated that robots can leverage web-trained vision-language models to understand concepts they've never physically encountered. Hausman describes a pivotal experiment: "This is a robot being asked to move the co-can to Taylor Swift... to us, watching this experiment live, that was a very, very big deal. And the reason is that the robot has never seen pictures of Taylor Swift. It's never seen any pictures of any of these celebrities or any other pictures. It had that abstract concept of who Taylor Swift is and what the picture of Taylor Swift looks like straight from the internet." [[00:05:12]](https://www.youtube.com/watch?v=5H2UrJ2N3t0&t=5m2s) This proved robots don't need firsthand experience of every situation - they can acquire semantic understanding from internet data and translate it to embodied movement.

### **Cross-Embodiment Learning Accelerates Development**
The RTX collaboration with 34 research institutions demonstrated that combining data from diverse robot platforms creates superior models. Hausman explains: "We took all of those data sets that were published for different methods and we combine them into one big data set and train one big generalist model on that. So that was trained on many different robots that look different, that have different number of degrees of freedom... our generalist model was able to beat that baseline state of the art method every single time on average by more than 50%." [[00:07:01]](https://www.youtube.com/watch?v=5H2UrJ2N3t0&t=6m51s) This cross-embodiment approach fundamentally changed assumptions about data requirements for robot training.

## 2. Contrarian Perspectives

### **Humanoids Are Not the Endgame**
While the industry obsesses over humanoid robots, Hausman argues for form-factor diversity: "I believe that if we actually succeed, if we actually crack the problem of physical intelligence and build these models that are extremely general, I don't think we're going to stop at humanoids. I think we're going to experience a Cambrian explosion of robots. Because let's be honest, if you wanted to do something like sort packages, you wouldn't be doing of a humanoid if you wanted to automate that." [[00:18:35]](https://www.youtube.com/watch?v=5H2UrJ2N3t0&t=18m25s) He emphasizes that "it's not our form factor that makes us special. It's our brain, our physical intelligence that makes us special." [[00:19:09]](https://www.youtube.com/watch?v=5H2UrJ2N3t0&t=18m59s) This challenges the billion-dollar investment trend toward humanoid robotics companies.

### **100 Environments, Not Millions, Achieve Generalization**
Before their research, the team was uncertain about data requirements: "Some of us thought maybe you need to visit the million different homes to be able to generalize that way. It turns out that around 100, you're able to basically get that performance." [[00:22:49]](https://www.youtube.com/watch?v=5H2UrJ2N3t0&t=22m39s) The quantitative data showed that after training on 100 different home environments, the robot's performance in a completely new (101st) home approached the performance level as if it had been trained in that specific environment - achieving over 80% task completion. [[00:22:12]](https://www.youtube.com/watch?v=5H2UrJ2N3t0&t=22m2s) This dramatically lower threshold makes deployment commercially viable much sooner than expected.

### **Starting a Company and Having a Baby Simultaneously**
Hausman openly shares an unconventional insight: "If I were to draw a conclusion from these two things, is that if you're thinking of starting a company and having a baby at the same time, please talk to me, I did not recommend that. Don't do it." [[00:01:58]](https://www.youtube.com/watch?v=5H2UrJ2N3t0&t=1m48s) This rare candor about the personal costs of entrepreneurship challenges the "you can have it all" narrative often promoted in startup culture.

## 3. Companies Identified

### **Physical Intelligence**
A year-old company building foundation models to control any robot for any task. Hausman states: "Around a year ago with the idea that we want to build them all that can control any robot to do any task, truly solve physical intelligence." [[00:01:33]](https://www.youtube.com/watch?v=5H2UrJ2N3t0&t=1m23s) The company achieved laundry folding - "a task that for a very long time has been considered a holding rail of robotics" - just five months after founding. [[00:10:06]](https://www.youtube.com/watch?v=5H2UrJ2N3t0&t=9m56s) They've open-sourced their Pi0 model through OpenPie repository and established partnership programs with various robotics companies.

### **Astrobot**
A humanoid robotics company partnering with Physical Intelligence. Hausman mentions: "Here's one partnership video with Astrobot humanoid robot, showing a robot making copy. And you can see it being a robot that is more complex, has many more degrees of freedom... But we can take a pre-trained Pi0 model and fine tune it to a new embodiment like this." [[00:17:25]](https://www.youtube.com/watch?v=5H2UrJ2N3t0&t=17m15s) This demonstrates the model's ability to transfer to complex humanoid platforms.

## 4. Operating Insights

### **Open Source as Strategic Distribution**
Physical Intelligence open-sourced their Pi0 model despite being a for-profit company. Hausman explains: "We open source up model. We open source it in a repository called OpenPie, where we open source many different checkpoints of it. We have different robot runtimes, have you can integrate it into your framework. And we have many, many people using it, fine tuning it on all kinds of different applications ranging from robotic surgery to autonomous driving to many, many other tasks." [[00:17:01]](https://www.youtube.com/watch?v=5H2UrJ2N3t0&t=16m51s) This strategy accelerates ecosystem development while establishing their model as the standard.

### **Quality Over Quantity in Post-Training**
The company discovered that post-training requires orders of magnitude less data than pre-training but is equally critical. The specific ratio matters: 10,000 hours of diverse pre-training data followed by just 20 hours of high-quality post-training data. [[00:14:27]](https://www.youtube.com/watch?v=5H2UrJ2N3t0&t=14m17s) This insight dramatically reduces the cost and time to specialize models for new tasks, making rapid iteration possible.

### **Real-World Evaluation in Unseen Environments**
Rather than iterating in controlled lab settings, the team evaluated by "literally driving around San Francisco assembling the robot and putting it in environments that's never seen before in evaluating it on the network." [[00:21:13]](https://www.youtube.com/watch?v=5H2UrJ2N3t0&t=21m3s) This operational approach forces the technology to work under real deployment conditions from early development stages, avoiding the lab-to-production gap that kills many robotics companies.

## 5. Overlooked Insights

### **Error Recovery as Emergent Capability**
The system's ability to handle adversarial interruptions wasn't explicitly trained but emerged from large-scale training. Hausman shows examples where "one of our researchers, Michael, is putting another shirt in trying to mess with it. And you can see that the robot kind of realizes what's happening, puts the shirt back and tries to do its job... This is not something that we trained specifically for, it's just something that emerges from large scale training like that." [[00:13:29]](https://www.youtube.com/watch?v=5H2UrJ2N3t0&t=13m19s) This suggests these models develop meta-skills for handling unexpected situations - a critical capability for real-world deployment that most robotics companies explicitly engineer rather than allow to emerge.

### **Pre-training Enables Transfer Even With In-Domain Data**
The most surprising finding in the generalization experiments wasn't just zero-shot performance, but that pre-trained models significantly outperform non-pre-trained models even when both have access to in-domain data from the target environment. The light green bar showing "if you don't use pre-training that I talked about before, the performance drops significantly even if you're using the main data." [[00:23:04]](https://www.youtube.com/watch?v=5H2UrJ2N3t0&t=22m54s) This implies that pre-training provides fundamental reasoning capabilities about physical interactions that can't be replicated by simply collecting more task-specific data - a profound insight for resource allocation in robotics development.