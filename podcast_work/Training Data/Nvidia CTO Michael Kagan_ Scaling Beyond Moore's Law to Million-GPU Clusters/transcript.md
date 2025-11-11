# Nvidia CTO Michael Kagan: Scaling Beyond Moore's Law to Million-GPU Clusters

**Podcast:** Training Data
**Date:** 2025-10-29
**Video ID:** H9JjlTA2Il8
**Video URL:** https://www.youtube.com/watch?v=H9JjlTA2Il8

---

[00:00:00] One of the interesting things about NVIDIA is the culture of Vidwin.
[00:00:05] Michael Kagan: We are not after taking a bigger piece of existing pie.
[00:00:10] Michael Kagan: We are after baking our bigger pie for everybody.
[00:00:16] Michael Kagan: And our success is our customer success.
[00:00:20] Michael Kagan: It's not our success is not the failure of our competition.
[00:00:24] Michael Kagan: And I think fusing together conventional computing
[00:00:29] Michael Kagan: for one human machines and accelerated computing
[00:00:33] Michael Kagan: that provides the NVIDIA,
[00:00:34] Michael Kagan: it actually gives NVIDIA and Intel channels
[00:00:41] Michael Kagan: to the market, or expanding the market,
[00:00:43] Michael Kagan: and serving the markets that otherwise was more challenging.
[00:00:59] We are delighted to hear today from one of the legends
[00:01:06] Unknown Host: of the semiconductor industry, Michael Cagan, the CTO of NVIDIA.
[00:01:11] Unknown Host: Michael was formerly chief architect at Intel
[00:01:14] Unknown Host: and then co-founder and CTO of Melanox,
[00:01:16] Unknown Host: which NVIDIA acquired for $7 million in March 2019.
[00:01:20] Unknown Host: In the time since,
[00:01:21] Michael has been a major driver of NVIDIA's dominance
[00:01:24] Unknown Host: as the AI compute platform in large part due to the role
[00:01:27] Unknown Host: of Melanox and interconnect in driving chips beyond Moore's law.
[00:01:32] The AI race is ultimately a silicon race
[00:01:34] Unknown Host: to squeeze the most intelligence possible out of each unit of silicon.
[00:01:37] Unknown Host: And Michael takes us down in Jeremy about how the compute frontier has evolved
[00:01:41] Unknown Host: from squeezing more transistors onto a single chip
[00:01:44] Unknown Host: to bringing together thousands and hundreds of thousands of chips
[00:01:47] Unknown Host: into a single fabric connected by networking or an AI data center.
[00:01:52] Michael has been driving the compute frontier forward
[00:01:54] Unknown Host: for more than four decades
[00:01:55] Unknown Host: and we're honored to have him on today's show.
[00:01:59] OK, we're here with Michael Cagan, the CTO of NVIDIA,
[00:02:03] Unknown Host: currently the world's most valuable company, Michael.
[00:02:05] Unknown Host: Thank you for joining us.
[00:02:06] Unknown Host: Thank you, Michael.
[00:02:08] Unknown Host: So I thought we could start.
[00:02:10] Unknown Host: Our partner, Sean, likes to make the case about every six months
[00:02:14] Unknown Host: that NVIDIA would not be in NVIDIA without Melanox.
[00:02:17] Unknown Host: NONOX is a company that you co-founded some 25 years ago
[00:02:21] Unknown Host: and have been a part of through this day.
[00:02:23] Unknown Host: So can you paint that picture for us?
[00:02:26] Unknown Host: Why is it that the Melanox acquisition was so critical to NVIDIA?
[00:02:33] Michael Kagan: You know, there was a huge transition in the world
[00:02:36] Michael Kagan: in terms of computing and the need for computing.
[00:02:40] Michael Kagan: And it grows exponentially.
[00:02:43] Michael Kagan: And one of the things that we usually estimate linearly
[00:02:48] Michael Kagan: but the world was exponential.
[00:02:51] Michael Kagan: The exponential growth now is actually accelerated.
[00:02:53] Michael Kagan: It used to be like MOLLO, which is a basic silicon.
[00:02:58] Michael Kagan: And it was twice every other year.
[00:03:03] Michael Kagan: And regardless, you know, the discussion that MOLLO
[00:03:07] Michael Kagan: in terms of physics is not quite running anymore.
[00:03:11] Michael Kagan: The once AI kicked in, which was in the 2010, 2011,
[00:03:19] Michael Kagan: and kicked in when GPU from graphic processing unit
[00:03:23] Michael Kagan: became general processing unit actually
[00:03:26] Michael Kagan: where it was running workloads were the first time.
[00:03:29] Michael Kagan: The AI workload was run on the GPU,
[00:03:33] Michael Kagan: taking advantage of the programmability
[00:03:35] Michael Kagan: and parallel nature of this machine.
[00:03:39] Michael Kagan: The requirements for performance started to grow up
[00:03:43] Michael Kagan: at much higher coefficient.
[00:03:45] Michael Kagan: So the model is started to go up
[00:03:49] Michael Kagan: in terms of size and capacity to X every three months,
[00:03:54] Michael Kagan: which requires now 10X or 16X a year performance growth
[00:03:59] Michael Kagan: versus old school of 2X twice every other year.
[00:04:07] Michael Kagan: And in order to grow this scale,
[00:04:09] Michael Kagan: you need to innovate and you need to develop solutions
[00:04:14] Michael Kagan: at much higher scale than just basic component.
[00:04:18] Michael Kagan: And that's where network kicks in.
[00:04:20] Michael Kagan: That's where the network is.
[00:04:22] Michael Kagan: And there are multiple layers of scaling performance
[00:04:28] Michael Kagan: that requires high speed networks and high performance networks.
[00:04:32] Michael Kagan: The one is what we call scale up.
[00:04:35] Michael Kagan: Basically, if you're going back to the CPU days,
[00:04:39] Michael Kagan: scaling up was MOLLO, more transistors,
[00:04:42] Michael Kagan: and also some advances in the microarchitecture
[00:04:45] Michael Kagan: like auto-forward execution and at some point,
[00:04:47] Michael Kagan: multi-core and so on and so forth.
[00:04:49] Michael Kagan: But so this is the basic building block of computing.
[00:04:53] Michael Kagan: In the GPU world, the basic building block is the GPU.
[00:04:58] Michael Kagan: And in order to scale it up more than you can do
[00:05:02] Michael Kagan: on a single piece of silicon with a lot of advances
[00:05:06] Michael Kagan: that we are doing with the microarchitecture and the dogs technologies,
[00:05:11] Michael Kagan: you actually need to do something on the scale,
[00:05:14] Michael Kagan: on the sort of multi-core CPU, but a much larger scale.
[00:05:19] Michael Kagan: And that's what we are doing with the Enviling.
[00:05:20] Michael Kagan: That's the scale up solution.
[00:05:22] Michael Kagan: So our GPU, what we call GPU today, is a rock size machine.
[00:05:28] Michael Kagan: You need the forklift to lift it.
[00:05:31] Michael Kagan: So if you order just GPU on Amazon,
[00:05:36] Michael Kagan: just don't wonder that you will show up this huge rack of...
[00:05:39] Michael Kagan: People think, check, but it's really a system.
[00:05:42] Michael Kagan: Right. And that's just one GPU.
[00:05:44] Michael Kagan: Yeah. Okay. So basic building block,
[00:05:47] Michael Kagan: a very basic computer that application software is running on,
[00:05:53] Michael Kagan: is this GPU, and it is not just silicon,
[00:05:57] Michael Kagan: it's not just hardware, it's not just wires,
[00:05:59] Michael Kagan: but there is also software layer that exposes CUDA as the API.
[00:06:05] Michael Kagan: And that's what actually enables to pretty much seamlessly scale.
[00:06:10] Michael Kagan: I'm simplifying a little bit the story,
[00:06:12] Michael Kagan: but seamlessly scale from one component that used to be single GPU,
[00:06:17] Michael Kagan: all the way up to 72,
[00:06:19] Michael Kagan: maintaining the same software interface.
[00:06:22] Michael Kagan: And once you get this building block as big as it,
[00:06:27] Michael Kagan: it can be built in terms of power cost efficiency,
[00:06:36] Michael Kagan: then you start scaling out.
[00:06:39] Michael Kagan: And scale out means you take many of these building blocks,
[00:06:44] Michael Kagan: connect them together.
[00:06:45] Michael Kagan: And now on the algorithm level, on the application level,
[00:06:49] Michael Kagan: you actually split your application to multiple pieces
[00:06:52] Michael Kagan: running in parallel on these big machines.
[00:06:55] Michael Kagan: And that's again, where network comes in.
[00:06:58] Michael Kagan: And there's a, so if you talk about scale up,
[00:07:01] Michael Kagan: we basically made memory like domain to go beyond single compute node,
[00:07:11] Michael Kagan: a single single GPU.
[00:07:12] Michael Kagan: And that's actually the first thing that were melanox technology comes in
[00:07:17] Michael Kagan: because before melanox acquisition,
[00:07:20] Michael Kagan: the scaling up of Nvidia with the end building was limited to a single node.
[00:07:25] Michael Kagan: Machine going outside of single compute node,
[00:07:29] Michael Kagan: if the 72 GPUs are, it's actually 36 computers.
[00:07:34] Michael Kagan: Each one has two GPUs and they're wired together,
[00:07:37] Michael Kagan: so present all this as a single GPU.
[00:07:40] Michael Kagan: Getting connectivity outside of the single node,
[00:07:43] Michael Kagan: it's not just plugging in the wire to the connector.
[00:07:47] Michael Kagan: It's a lot of software,
[00:07:48] Michael Kagan: it's a lot of technology within the network,
[00:07:51] Michael Kagan: how to make multiple nodes to work as the single machine.
[00:07:57] Michael Kagan: And that's where melanox first,
[00:08:00] Michael Kagan: just immediate in terms of, you know,
[00:08:02] Michael Kagan: the way we go upstream, that's the first one.
[00:08:06] Michael Kagan: The second one is how do you split the operation across multiple machines?
[00:08:13] Michael Kagan: And the way to do it, if I have a task that it takes one GPU to do one second,
[00:08:19] Michael Kagan: if I want to accelerate it, I split it to 10,000 pieces
[00:08:25] Michael Kagan: and send each piece to different GPU.
[00:08:27] Michael Kagan: And now in one millisecond, I get done whatever I was doing in the second,
[00:08:32] Michael Kagan: but you need to communicate this partial job split, split the task,
[00:08:40] Michael Kagan: then you need to consolidate the results.
[00:08:42] Michael Kagan: And every time you are, and you run this multiple times,
[00:08:48] Michael Kagan: you have multiple iterations or multiple applications running to us,
[00:08:53] Michael Kagan: so that there is a part of doing communication, part of doing computation.
[00:08:57] Michael Kagan: Now the thing is that you want to split it to as many pieces as you possibly can,
[00:09:03] Michael Kagan: because that's your speed up factor.
[00:09:06] Michael Kagan: But then if your communication is actually blocking you,
[00:09:09] Michael Kagan: you waste time, you waste energy, you waste everything.
[00:09:13] Michael Kagan: So what you need to do, you need to have a very fast communication.
[00:09:16] Michael Kagan: So you split it to the many, many pieces.
[00:09:19] Michael Kagan: And so each piece takes very little time,
[00:09:23] Michael Kagan: but then there is another piece that is communicated,
[00:09:25] Michael Kagan: and you need to feed it this time, so that's just pure bandwidth.
[00:09:30] Michael Kagan: And the other thing is that when you tune your application,
[00:09:34] Michael Kagan: you tune your application so that communication can be hidden behind computation.
[00:09:40] Michael Kagan: And it means that if communication for some reason gets longer,
[00:09:45] Michael Kagan: then everybody waits.
[00:09:47] Michael Kagan: So it means that what you need to do in the network,
[00:09:50] Michael Kagan: you need to have not only just draw performance,
[00:09:53] Michael Kagan: like what's called hero numbers,
[00:09:55] Michael Kagan: I can get to that many gigabits per second.
[00:09:57] Michael Kagan: I also need to make sure that no matter who's communicate to whom,
[00:10:01] the latency, the time it takes, is distribution is very narrow.
[00:10:07] Michael Kagan: So if you look at other network technologies or other network products,
[00:10:11] Michael Kagan: you go to the hero numbers, sending bit from one place to another,
[00:10:15] Michael Kagan: it's basically physics.
[00:10:17] Michael Kagan: Yeah, it's pretty much close to everyone.
[00:10:21] Michael Kagan: You know, we are a little bit better,
[00:10:23] Michael Kagan: but that's not the big advantage.
[00:10:26] Michael Kagan: But when you do it thousands of times,
[00:10:29] Michael Kagan: and it takes the same time to do it,
[00:10:31] Michael Kagan: versus very wide distribution of other technologies,
[00:10:35] Michael Kagan: then machine becomes less efficient.
[00:10:38] Michael Kagan: So instead of being able to split your job to 1000 GPUs,
[00:10:43] Michael Kagan: you can split it only to 10 GPUs,
[00:10:45] Michael Kagan: because you need to accommodate for the jitter on the network
[00:10:49] Michael Kagan: within the computation phase.
[00:10:52] Michael Kagan: So inherently, network determines the performance of this cluster.
[00:10:58] Michael Kagan: And we look at this data center
[00:11:01] Michael Kagan: as basically single unit of computing.
[00:11:03] Michael Kagan: Yeah.
[00:11:03] Michael Kagan: Okay, single unit of computing means that you look at this,
[00:11:06] Michael Kagan: you start architecting your components,
[00:11:10] Michael Kagan: your software and your hardware
[00:11:13] Michael Kagan: at the point where this is the data center,
[00:11:16] Michael Kagan: this is 100,000 GPUs that we want to make them work together.
[00:11:21] Michael Kagan: We need to make multiple chips, compute chips, two network chips, five.
[00:11:29] Michael Kagan: Okay, so this is a scale just, in terms of what's the impact?
[00:11:35] Michael Kagan: And what's the investment you need to make
[00:11:38] Michael Kagan: to create this single unit of computing?
[00:11:42] Michael Kagan: So that's where Melanox technology came in.
[00:11:46] Michael Kagan: And another aspect of this is there is a,
[00:11:50] Michael Kagan: we talked about network that connects the GPUs to run the task.
[00:11:57] Michael Kagan: But there is another side of this machine, which is customer facing.
[00:12:01] Michael Kagan: So you need to, this machine needs to save,
[00:12:05] Michael Kagan: to serve multiple tenants.
[00:12:08] Michael Kagan: And this machine needs to run operating system,
[00:12:11] Michael Kagan: you know, every computer runs operating system.
[00:12:13] Michael Kagan: And another part of the Melanox technology is what we call
[00:12:18] Michael Kagan: Bluefield GPU, data processing unit,
[00:12:21] Michael Kagan: which is actually the computing platform
[00:12:24] Michael Kagan: to run the operating system of the data center.
[00:12:27] Michael Kagan: In conventional computer, we have a CPU that runs operating system
[00:12:30] Michael Kagan: and runs applications software.
[00:12:32] Michael Kagan: And there are many things we can talk about, you know,
[00:12:37] Michael Kagan: the advantage versus this advantage,
[00:12:39] Michael Kagan: but there are two key things.
[00:12:42] Michael Kagan: One is how much time do you spend on your general purpose computing
[00:12:47] Michael Kagan: to run the application?
[00:12:48] Michael Kagan: You need to, you want to maximize it?
[00:12:50] Michael Kagan: And another thing is how do you isolate your infrastructure
[00:12:54] Michael Kagan: computing from the application computing?
[00:12:57] Michael Kagan: Because, you know, viruses and the cyber attacks and so on and so forth.
[00:13:03] Michael Kagan: And being able to run infrastructure computing
[00:13:08] Michael Kagan: on a different computing platform
[00:13:11] Michael Kagan: actually reduces significantly the attack front versus,
[00:13:18] Michael Kagan: especially in the side channel attacks versus what happens
[00:13:21] Michael Kagan: if you run it on the same computer.
[00:13:23] Michael Kagan: If you remember, there was a five or well,
[00:13:25] Michael Kagan: a few more than almost ten years ago,
[00:13:27] Michael Kagan: there was a meltdown and all this cyber attacks of the side channel
[00:13:32] Michael Kagan: on CPUs and this cannot happen over.
[00:13:37] Michael Kagan: The attack surface is reduced significantly
[00:13:40] Michael Kagan: when you run the different.
[00:13:42] Michael Kagan: So on the other side of the network,
[00:13:44] Michael Kagan: we have also technology.
[00:13:47] Michael Kagan: So that's what makes DERES Center to be more efficient.
[00:13:50] Michael Kagan: And I, well, I may be not objective,
[00:13:54] Michael Kagan: but I do agree that this merger of Melonox and Nvidia
[00:13:58] Michael Kagan: and it actually goes both way.
[00:14:00] Michael Kagan: I don't think that networking business of now it's Nvidia,
[00:14:05] Michael Kagan: the previous Melonox could have been growing that significantly.
[00:14:10] Michael Kagan: Yeah.
[00:14:11] Michael Kagan: As a growth now, I think we are the fastest growing internet business.
[00:14:16] Michael Kagan: You know, let long and we link and then Finneband.
[00:14:21] Michael Kagan: Yeah.
[00:14:22] Michael Kagan: Just internet business is the fastest growing business ever.
[00:14:26] What are the things that break as you get to 100,000,
[00:14:30] Unknown Host: maybe eventually a million GPU clusters?
[00:14:32] Unknown Host: And how do you use software to help design it on that?
[00:14:35] It's a multi-stage challenge.
[00:14:40] Michael Kagan: One of the things that you need to keep in mind
[00:14:46] Michael Kagan: is not very obvious for all the engineers that when you design the machine
[00:14:49] Michael Kagan: or think how to operate it.
[00:14:51] Michael Kagan: Well, you know, you have these components and they are working
[00:14:54] Michael Kagan: and now just let's figure out.
[00:14:56] Michael Kagan: Okay.
[00:14:57] Michael Kagan: So the thing is that the hardware component works at 99.99,
[00:15:01] Michael Kagan: whatever percent of the time.
[00:15:04] Michael Kagan: And it's usually okay if you are dealing with single box with a couple of them.
[00:15:09] Michael Kagan: But if you are building 100,000 component machine,
[00:15:14] Michael Kagan: a counter GPU machine, which means in terms of components,
[00:15:17] Michael Kagan: there is a millions of them.
[00:15:19] Michael Kagan: The chance that everything works is zero.
[00:15:21] Michael Kagan: So something is definitely broken.
[00:15:24] Michael Kagan: And you need to design it both from hardware and from software perspective
[00:15:30] Michael Kagan: to keep going, to keep going as efficient as you can,
[00:15:34] Michael Kagan: to keep, you know, your performance,
[00:15:36] Michael Kagan: you keep your power efficiency and of course keep the service running.
[00:15:41] Michael Kagan: So this is challenge number one, even before we go to millions.
[00:15:45] Michael Kagan: It's, this challenge actually starts at, you know, few tens of thousands.
[00:15:49] Michael Kagan: That's number one.
[00:15:51] Michael Kagan: Number two is when you are running these workloads,
[00:15:57] Michael Kagan: it is really important to, it sometimes you run single job on the entire entire data center.
[00:16:05] Michael Kagan: And then it's, you know, you need to write the software and you need to provide
[00:16:10] Michael Kagan: all the interfaces to the software to place the different parts of the job,
[00:16:15] Michael Kagan: jobs more efficiently.
[00:16:17] Michael Kagan: Building networks at this scale is a very different story than building network,
[00:16:24] Michael Kagan: compute network on this scale.
[00:16:25] Michael Kagan: This is a very different story than build just zero purpose data center network.
[00:16:29] Michael Kagan: The entire purpose data center network is Internet, it's not a big deal.
[00:16:32] Michael Kagan: Well, it is a big deal, but it is, it is different deal.
[00:16:36] Michael Kagan: It's, you are, you are serving, you know, loosely coupled, collaborative
[00:16:42] Michael Kagan: microservices that create the, you know, service that you, that you see as a,
[00:16:47] Michael Kagan: as a customer from outside.
[00:16:49] Michael Kagan: Here you are running one single application on 100,000 machines.
[00:16:54] Michael Kagan: Yeah.
[00:16:54] Michael Kagan: Is that specific to training workloads?
[00:16:56] Unknown Host: Or is that also true with inference workloads?
[00:16:58] Unknown Host: It's true, it's true for everything.
[00:17:00] Michael Kagan: Okay.
[00:17:01] Michael Kagan: You know, it depends on what scale and the inference is yet another, yet another topic
[00:17:06] Michael Kagan: that we, the, when it actually, you know, till recently training was the key thing,
[00:17:11] Michael Kagan: you know, a lot of GPUs and there is a very specific way of trainings being done.
[00:17:16] Michael Kagan: You basically copy this way, another model on multiple, multiple machines,
[00:17:22] Michael Kagan: on multiple sets of machines and run them, then consolidate the results and so on and so forth.
[00:17:27] Michael Kagan: On the inference, it's the story is a little bit different.
[00:17:31] Michael Kagan: But the thing is that you need to provide the hooks on the hardware and on the
[00:17:36] Michael Kagan: your low level software, system software for application and for scheduler to place
[00:17:42] Michael Kagan: the job and place the different parts of the job in the most efficient way on the,
[00:17:48] Michael Kagan: you know, and as long as, as your machine fits a building,
[00:17:55] Michael Kagan: which is about 100,000 GPUs now talking about, you know, giga, but it's all,
[00:17:59] Michael Kagan: all power driven.
[00:18:01] Michael Kagan: Okay.
[00:18:01] Michael Kagan: The challenge is that for many reasons, reasons,
[00:18:05] Michael Kagan: you want to split your workloads across multiple data centers.
[00:18:11] Michael Kagan: And sometimes the data centers are at the distance of many kilometers, many miles.
[00:18:17] Michael Kagan: It's a, it may be across across the continent.
[00:18:21] Michael Kagan: And this, you know, it comes with the yet another challenge, which is speed of light.
[00:18:26] Michael Kagan: Yeah.
[00:18:27] Michael Kagan: Okay.
[00:18:27] Michael Kagan: Now the latency variance between different parts of your machine is dramatically different.
[00:18:35] Michael Kagan: And what is even more challenging is that when you talk about networks,
[00:18:42] Michael Kagan: the congestion on the network is one of the key problems that deteriorate network
[00:18:49] Michael Kagan: performance.
[00:18:49] Michael Kagan: Yeah.
[00:18:50] Michael Kagan: And managing congestion across such a latency, latency difference is not like,
[00:18:56] Michael Kagan: you know, in all, all telco days, you put some box in the edge of your data center with
[00:19:01] Michael Kagan: a huge buffer and it's a shock absorber for congestion.
[00:19:05] Michael Kagan: Huge buffer is, is, is not, is not good.
[00:19:09] Michael Kagan: You know, some bigger is not better.
[00:19:12] Michael Kagan: There is a, there is a famous statement from very famous who won.
[00:19:17] Michael Kagan: And so, so we need to, and these buffers are basically, these devices are basically
[00:19:24] Michael Kagan: to isolate the external world from the internals.
[00:19:29] Michael Kagan: And, but when you want to run a single workload across data centers that are distant
[00:19:35] Michael Kagan: by kilometers, you need to be every machine on one side to be aware,
[00:19:42] Michael Kagan: what, whom does it communicate to whether it's short, short, short communication,
[00:19:46] Michael Kagan: long communication and adjust all the communication patterns accordingly.
[00:19:51] Michael Kagan: So you don't need these big buffers because big buffers is a jitter.
[00:19:54] Michael Kagan: Yeah.
[00:19:55] Unknown Host: And so we have a, we have a technology we actually developed recently technology,
[00:20:00] Michael Kagan: you know, although Ethernet network is Spectrum X.
[00:20:04] Michael Kagan: And this is the device that we designed and developed based on the spectrum,
[00:20:11] Michael Kagan: spectrum switch that we put on the edge of the data center and it provides
[00:20:17] Michael Kagan: all the information and telemetry needed for, for the endpoints to adjust for the
[00:20:24] Michael Kagan: position. Yeah.
[00:20:25] Michael Kagan: Can we talk a little bit more about training versus inference?
[00:20:28] Unknown Host: Like, how does the shape of workload differ when you're doing, I guess, I guess
[00:20:32] Unknown Host: backprops, a lot more compassion intensive forward past less so.
[00:20:36] Unknown Host: But like, how does the workload differ?
[00:20:39] Unknown Host: And then are you seeing customer demands start to shift from pre-training towards
[00:20:44] Unknown Host: inference? Or do you think it's still very training?
[00:20:46] Unknown Host: Have it right now?
[00:20:46] Unknown Host: And if I could just ask a quick follow up question about will people be running
[00:20:50] Unknown Host: inference workloads on the same data centers that they use for training or
[00:20:53] Unknown Host: these end up being too separate?
[00:20:56] Because they're different optimizations people end up using two different sets of
[00:20:59] Unknown Host: data centers.
[00:21:01] Okay, yeah, that's, that's great question.
[00:21:03] Michael Kagan: And let me start with the first one.
[00:21:07] Michael Kagan: So, so training has two phases.
[00:21:10] Michael Kagan: One is inference, which is just for the propagation and then backpropagation
[00:21:15] Michael Kagan: to adjust the weights.
[00:21:17] Michael Kagan: And for data parallel training, it's yet another phase to consolidate the result
[00:21:23] Michael Kagan: of the weights update across multiple model copies.
[00:21:29] Michael Kagan: So, till recently it was a main driver of the compute,
[00:21:35] Michael Kagan: because till not very long ago, it's maybe two years, which is ages in the AI,
[00:21:45] Michael Kagan: AI era, the inference or AI was mainly perceptual.
[00:21:50] Michael Kagan: So, you show the picture, that's a dog.
[00:21:53] Michael Kagan: You show, you know, the photo of the person and he is that's that's Michael and that's
[00:21:59] Michael Kagan: Sonia.
[00:21:59] Michael Kagan: And that's so that's single path and that's it.
[00:22:05] Michael Kagan: Then came became a generative AI, where actually you get the recursive
[00:22:12] Michael Kagan: generation.
[00:22:12] Michael Kagan: So, when you post the prompt, then it's not just one inference.
[00:22:19] Michael Kagan: It's many inferences.
[00:22:20] Michael Kagan: Because for every token, when you generate text, generate picture, for every new token,
[00:22:24] Michael Kagan: you need to go through the entire machine all over again.
[00:22:28] Michael Kagan: So, instead of one shot, one shot, there is more.
[00:22:33] Michael Kagan: And then now there is a reasoning, which means the machine starts, you know, sort of thinking.
[00:22:40] Michael Kagan: Yeah.
[00:22:40] Michael Kagan: If you ask me what time is it now, I can tell you, it's easy, right?
[00:22:43] Michael Kagan: What time is it now?
[00:22:44] Michael Kagan: But if you ask me more complicated question, then I need to think.
[00:22:49] Michael Kagan: I probably need to wait or compare multiple solutions or multiple paths.
[00:22:56] Michael Kagan: And every such a thing is inference.
[00:22:59] Michael Kagan: Yeah.
[00:22:59] Michael Kagan: Every such a thing is inference.
[00:23:01] Michael Kagan: An interest itself has actually two phases.
[00:23:06] Michael Kagan: One is much more compute, compute intensive and the other one is memory intensive.
[00:23:12] Michael Kagan: It's a typical pre-fuel.
[00:23:15] Michael Kagan: Because when you do the inference, you have some sort of background, which is prompt,
[00:23:21] Michael Kagan: which is some relevant data, that you need to process and create the context for the
[00:23:27] Michael Kagan: to generate the answer.
[00:23:28] Michael Kagan: And this is very compute intensive.
[00:23:30] Michael Kagan: It's not much memory intensive.
[00:23:33] Michael Kagan: And the other part is actually generating the answer, which is the decode part of the inference,
[00:23:42] Michael Kagan: where you generate token by token.
[00:23:45] Michael Kagan: Well, there are some technologies that you can generate more than one token, but it's still,
[00:23:50] Michael Kagan: you know, single path is much less than the final answer.
[00:23:55] So if you combine all these things together, inference,
[00:24:00] Michael Kagan: inference demand for computing is not actually not less than training.
[00:24:05] Michael Kagan: It's actually even more.
[00:24:07] Michael Kagan: And there are two reasons for this.
[00:24:09] Michael Kagan: One is that what I explained that there's a much more computing than it used to be
[00:24:14] Michael Kagan: for the inference.
[00:24:15] Michael Kagan: The other thing is, you know, you train model once, but you infer many times.
[00:24:19] Michael Kagan: Yeah.
[00:24:19] Michael Kagan: You know, chat GPT, you know, billion of people, or it's almost billion of people, right?
[00:24:25] Michael Kagan: There's customers that are pounding them all the time.
[00:24:27] Michael Kagan: It's the same model.
[00:24:28] Michael Kagan: They trained it once.
[00:24:29] Michael Kagan: Now they're making videos.
[00:24:30] Unknown Host: So that's right.
[00:24:31] Unknown Host: Now they make videos and you can generate them.
[00:24:34] Michael Kagan: And then, you know, everybody is doing the inference.
[00:24:39] Michael Kagan: My wife, I think she talks to chat GPT more than to me.
[00:24:43] Michael Kagan: Once she discovers that's her best friend.
[00:24:47] Michael Kagan: So in terms of, now, to your question about machines,
[00:24:54] Michael Kagan: you can infer on the phone.
[00:24:57] Michael Kagan: Okay, so there is a definitely going to be much smaller scale installations.
[00:25:05] Michael Kagan: For inference, yeah, it's like mobile devices.
[00:25:09] Michael Kagan: If you look at the data center scale, the data center scale, and on the,
[00:25:16] Michael Kagan: it's efficiency of the programming, programmability is much more viable than optimizations
[00:25:25] Michael Kagan: for hardware.
[00:25:29] Michael Kagan: And you know, every hardware instance, it has its own cost and its own drawback.
[00:25:39] Michael Kagan: So as long as you don't identify and I don't think, besides, you know, this, we actually did,
[00:25:48] Michael Kagan: it's very similar GPU.
[00:25:50] Michael Kagan: It's same programming model as the GPU for pre-fill versus decode.
[00:25:57] Michael Kagan: I think I don't remember when it happened, but actually we announced that we are building
[00:26:03] Michael Kagan: the GPU skew that is optimized for pre-fill.
[00:26:09] Michael Kagan: So you will have, it can do decode and decode GPU can do pre-fill.
[00:26:16] Michael Kagan: But you can equip your data center with the skews or the pre-fill versus skews that are
[00:26:24] Michael Kagan: for decode to optimize for like typical use.
[00:26:28] Michael Kagan: But if your workload shifts for more decode or for more pre-fill, you can use either one of them
[00:26:36] Michael Kagan: to compensate.
[00:26:39] Michael Kagan: And this is the, this is the importance of programmability.
[00:26:44] Michael Kagan: The same interfaces for GPUs, it's based on code and the end up, which is, that's what made
[00:26:51] Michael Kagan: Nvidia and VD before me, don't know.
[00:26:55] Can I ask you a question about data center scaling?
[00:26:57] Unknown Host: So for many decades, we had Moore's Law and chips got more and more dense and produced better
[00:27:03] Unknown Host: and better performance and then we ran into the laws of physics and chips just couldn't get
[00:27:08] Unknown Host: more dense because there are quantum mechanical properties cause them to break down.
[00:27:12] Unknown Host: And so then we had to scale up to the rack level and now we got to scale up to the data center level.
[00:27:17] Unknown Host: Is there some analogous law of data center scaling that says when data centers get too big,
[00:27:25] Unknown Host: the communication overhead causes the performance to break down or just said differently,
[00:27:30] Unknown Host: maybe said more simply, is there a natural limit to how big data centers can get?
[00:27:35] Unknown Host: I think there is a practical limit of how much energy you can consume within, within given size
[00:27:43] Michael Kagan: of the data center.
[00:27:44] Michael Kagan: But if you were surrounded by nuclear power plants and the energy was available,
[00:27:49] Unknown Host: with the data center itself performed?
[00:27:53] Michael Kagan: I don't know, I'm not an expert in the construction even, but if you surround,
[00:27:59] Michael Kagan: there's an energy coming in, now the heat is going out.
[00:28:02] Michael Kagan: So there is a whole, we are now basically moved pretty much entirely to the liquid cooling.
[00:28:10] Michael Kagan: One of the reasons we did it is to enable much denser compute power.
[00:28:15] Michael Kagan: We couldn't build as dense computing as we're building now with the air cooling.
[00:28:21] Michael Kagan: So there's a whole bunch of technologies coming to help this more and more denser now.
[00:28:30] Michael Kagan: Last big data center, which is like XAI scale is 150 megawatt.
[00:28:37] Michael Kagan: Now we're talking about gigawatt data centers, people talking about 10 gigawatt data centers.
[00:28:43] Michael Kagan: So there is a looking forward to build much bigger data centers.
[00:28:48] Michael Kagan: Are you selling the data centers to other space?
[00:28:50] Unknown Host: Very cool.
[00:28:51] Michael Kagan: I think one of the things that determines the speed of data center deployment is how fast
[00:29:02] Michael Kagan: concrete gets stable.
[00:29:08] Unknown Host: So before starting Melanox, you were at Intel.
[00:29:11] Unknown Host: That's right.
[00:29:11] Unknown Host: 16 years.
[00:29:13] Unknown Host: 16 years.
[00:29:13] Unknown Host: Mechim G. Parkitect.
[00:29:15] Unknown Host: In VD and Intel recently announced a partnership.
[00:29:18] Unknown Host: Can you share a little bit about what the vision for that might be?
[00:29:21] The starting point is that computing changed in last decade or a little bit more than decade.
[00:29:29] Michael Kagan: Nvidia started its accelerated computing company.
[00:29:35] Michael Kagan: Video games was the first.
[00:29:38] Michael Kagan: And then it evolved to AI, which is the new way of data processing.
[00:29:43] Michael Kagan: So you cannot just general one human machine just is not capable of
[00:29:53] Michael Kagan: being used as a platform to solve the problem like programming one human machine is just explaining
[00:29:59] Michael Kagan: somebody what to do.
[00:30:01] Michael Kagan: Okay, I can explain many things and I can explain many people what to do.
[00:30:07] Michael Kagan: But I can't explain how to distinguish between cat and dog.
[00:30:11] Michael Kagan: Right.
[00:30:11] Michael Kagan: So there is a new challenges that AI solves and you need acceleration there.
[00:30:16] Michael Kagan: And our partnership with Intel is actually fusing accelerated computing with the general
[00:30:24] Michael Kagan: purpose computing because general purpose computing is not going away.
[00:30:28] Michael Kagan: Everything will be accelerated but we accelerate the purpose computing.
[00:30:32] Michael Kagan: We accelerate the applications.
[00:30:33] Michael Kagan: We accept.
[00:30:35] Michael Kagan: So and you know, X-R-E-Six is the architecture that is dominant there and you know it would
[00:30:44] Michael Kagan: serve greatly both companies.
[00:30:46] Michael Kagan: That's actually one of the interesting things about Nvidia.
[00:30:49] Michael Kagan: It's the culture of VWIN.
[00:30:52] Michael Kagan: Okay.
[00:30:53] Michael Kagan: We are not after taking a bigger piece of existing pie.
[00:30:59] Michael Kagan: We are after making our bigger pie for everybody.
[00:31:05] Michael Kagan: And the success, our success is our customer success.
[00:31:11] Michael Kagan: It's not our success is not the failure of our competition.
[00:31:15] Michael Kagan: Our success is successful our customers and success of ecosystem.
[00:31:20] Michael Kagan: And I think fusing together conventional computing,
[00:31:25] Michael Kagan: one human machines and accelerated computing that provide with an
[00:31:29] Michael Kagan: Invinia is actually it's probably open yet another dimension that I'm not sure what it is but
[00:31:37] Michael Kagan: it basically gives you know on the practical you know short term view is it's gives
[00:31:45] Michael Kagan: Nvidia and Intel channels to the market or expanding the market and serving the markets that
[00:31:53] Michael Kagan: otherwise was more challenging.
[00:31:56] You mentioned the culture of Invinia.
[00:31:58] Unknown Host: So when Melanox became part of Invinia in 2019, the market cap of the combined company was about
[00:32:04] Unknown Host: 100 billion which is no joke.
[00:32:06] Unknown Host: But the market cap today is about four and a half trillion.
[00:32:10] Unknown Host: So 45X growth in value in six years is pretty phenomenal.
[00:32:15] Unknown Host: How has that changed the culture of Invinia?
[00:32:17] Unknown Host: How has Invinia different today now that it's one of the most admired companies in the world,
[00:32:23] Unknown Host: if not the most admired versus six years ago?
[00:32:26] Unknown Host: Yeah, about this you know when we just joined,
[00:32:30] Michael Kagan: Jensen was in Israel and I presented him you know that I believe that one plus one will be 10
[00:32:37] Michael Kagan: and I actually was offered by Factor of four.
[00:32:40] Michael Kagan: Yeah.
[00:32:42] Michael Kagan: So but Melanox and Invinia in a sense it's sort of similar.
[00:32:49] Michael Kagan: The culture was very similar to begin with but there is nothing absolutely similar and
[00:32:58] Michael Kagan: I was the only founder that left in Melanox after a real
[00:33:03] Michael Kagan: resigned a few months after the acquisition and my main focus at the beginning you know
[00:33:11] Michael Kagan: things what do you think about in the shower was how to make sure that this acquisition will succeed.
[00:33:17] Michael Kagan: Yeah, you know Invinia paid seven billion dollars for company that I founded and you know
[00:33:26] Michael Kagan: it's all the mixed feelings that were there but once it's done it's done now I have to make it
[00:33:32] Michael Kagan: successful. Yeah, so eventually it worked.
[00:33:38] Michael Kagan: Most of the most of the Israeli employees are state I think it's 85 or 90% of
[00:33:46] Michael Kagan: regional employees state actually Invinia grew more than two X in Israel in terms of
[00:33:55] Michael Kagan: main power. Yeah, so we growing and we are announced that we're actually going to build a campus
[00:34:02] Michael Kagan: in Israel, New Campus for Invinia and so that's where I think the overall the merger was
[00:34:13] Michael Kagan: very successful. I did my best to make sure it succeeds and besides the technology that I
[00:34:25] Michael Kagan: was looking at this part of which is sort of technology but it's technology and
[00:34:31] Michael Kagan: theology and there are many other things to make sure that people are comfortable that you know
[00:34:38] Michael Kagan: from being in the center of Melanox which is the headquarters on Israel don't feel left
[00:34:46] Michael Kagan: you know somewhere in the faraway and Jensen its campus sizes the networking
[00:34:53] Michael Kagan: as the critical part of Melanox and Invinia success and he's right. Yeah, so I think it was the
[00:35:03] Michael Kagan: it's it's it's considered to be the most successful merger in the in the history of the technology.
[00:35:08] Michael Kagan: I am you guys probably trying to try to do things better than than I am but overall I think it was
[00:35:16] Michael Kagan: great move. Yeah, what are the science fiction things that you spend your time thinking about?
[00:35:21] Unknown Host: You're just even wondering like for example optical interconnects do you think do you think that will
[00:35:25] exist? Do you think AI will ever be better at physics than us and better at data time than us?
[00:35:31] Unknown Host: Well, what I what I thinking you know in the if you look about science fiction is how to make
[00:35:38] Michael Kagan: history to be experimental science you know you can physics do try something and then you know
[00:35:44] Michael Kagan: see with works and then time time and girls in history time goes one direction but you have a good
[00:35:49] Michael Kagan: simulation of the world you can make history experience and we have earth to climate simulator
[00:35:57] Michael Kagan: and with this type of technology we can actually simulate how what we do today will impact
[00:36:04] Michael Kagan: global warming 50 years from now. Okay, experimental science you know you you try something you see
[00:36:10] Michael Kagan: what happens 50 years later. So that's that's that's the science fiction part. Yeah and you know
[00:36:19] Michael Kagan: on the physics now we are moving from reasoning and so on and so forth now we once we get AI
[00:36:27] Michael Kagan: models to understand physics we actually can learn physics. AI can teach us physics because the way
[00:36:35] Michael Kagan: we we we get to the laws of physics that we observe at theoretical physics right you observe
[00:36:43] Michael Kagan: some phenomena and you generalize it and you compose the rule that basically the law the physics
[00:36:51] Michael Kagan: law that stays underneath of this phenomena and AI is really great of generalizing and data
[00:37:01] Michael Kagan: processing and observing so AI can help us to get to know some laws of physics that we don't even
[00:37:07] Michael Kagan: imagine. Now yeah. Moore's law was 2x every two years. Huang plus Kagan's law is what what is the
[00:37:15] Unknown Host: slope and how long do you think you can sustain it? Well the slope is somewhere in the range of
[00:37:22] Michael Kagan: 10x or few orders of magnitude a year and that's what we are doing by the way now we are we are we are
[00:37:28] Michael Kagan: since about two or three years ago we accelerated our product introduction from every other year to
[00:37:35] Michael Kagan: every year. Now we introduce a new new new wave of products every every year and it's a
[00:37:45] Michael Kagan: order of magnitude higher performance and it's not it's not on the chip level performance it's on
[00:37:51] Michael Kagan: machine that you can build with this performance that's what we are looking at it's a single
[00:37:56] Michael Kagan: unit of computing and how long it will stay I don't know I don't know but we'll do our best to
[00:38:04] Michael Kagan: to maintain it as long as needed and probably even accelerate it's it's all about it's all about
[00:38:09] Michael Kagan: exponent it's all about exponent it's hard to imagine you know you if you look at this
[00:38:15] Michael Kagan: Moodlow curves or any any rollercoars they usually plot it on the logarithmic scale so it looks
[00:38:23] Michael Kagan: like linear but that's wrong thing to look you can't predict what's what's going to happen who could
[00:38:28] Michael Kagan: predict that when iPhone was first introduced or smartphone was first introduced you know that's
[00:38:36] Michael Kagan: 15 years ago 2017 yeah 2017 all 17 years ago okay who could who could imagine that this smartphone
[00:38:46] Michael Kagan: the least used function at least for me is a phone yeah unless it's eco-immersive it's texting
[00:38:53] Michael Kagan: it's news it's mail it's basically running running your life from this machine yeah so your
[00:39:00] Michael Kagan: authentication your idea is there it's so you know now who can imagine what's going to happen you
[00:39:07] Michael Kagan: know 10 years from now is all these developments that we are doing we are doing today but we are
[00:39:12] Michael Kagan: building the platform for innovation what is the your commentary on who can imagine not
[00:39:18] Unknown Host: withstanding what is the most optimistic view of our future with AI that you like to think about
[00:39:25] Unknown Host: like what what could AI do for the world 5 10 15 years ago Steve Jobs called
[00:39:32] Michael Kagan: computer to be the bicycle of of mind yeah okay so AI is it's maybe I don't know if it's
[00:39:42] Michael Kagan: it's probably spaceship because there's a lot of things that I would like to do but I I just
[00:39:51] Michael Kagan: don't have enough time don't have resources to do it with AI I will have it and it doesn't mean that
[00:39:58] Michael Kagan: you know I will do twice as much maybe I do I will do 10 times as much but the thing is that I
[00:40:04] Michael Kagan: will want to do 100 times as much as I want to do today and that's where and that's where and you
[00:40:09] Michael Kagan: know you go to to to any project leader and nobody says you know I have enough I have enough
[00:40:15] Michael Kagan: I have enough resources I don't need anymore okay if you give him resources which is twice as
[00:40:20] Michael Kagan: efficient he will do four times more yeah and he will want to do 10 times more so it's like electricity
[00:40:28] Michael Kagan: changes the world right instead of using you know and in the land and you still still see this
[00:40:34] Michael Kagan: gas lamps and this infrastructure to to use the gases as the source of energy
[00:40:43] who could think that you know once this electricity was invented it will change the world that
[00:40:49] Michael Kagan: you know we can't live without electricity the same the same with AI beautiful please
[00:40:54] Unknown Host: thank you so much for joining us today I love this conversation thank you thank you thank you for
[00:41:24] the