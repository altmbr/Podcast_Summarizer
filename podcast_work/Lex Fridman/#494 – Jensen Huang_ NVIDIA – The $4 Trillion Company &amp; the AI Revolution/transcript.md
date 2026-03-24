[00:00:00] Lex Fridman: The following is a conversation with Jensen Huang, CEO of NVIDIA, one of the most important and influential companies in the history of human civilization. NVIDIA is the engine powering the AI revolution, and a lot of its success can be directly attributed to Jensen's sheer force of will and his many brilliant bets and decisions as a leader, engineer, and innovator.

[00:00:25] Lex Fridman: And now a quick few second mention of his sponsor. Check them out in the description or at lexfridman.com slash sponsors. It is in fact the best way to support this podcast. We got Shopify for selling stuff online, Element for Electrolytes, Fin for customer service AI agents, Quo for a phone system like calls, texts, contacts for your business, and Perplexity for curiosity-driven knowledge exploration. Choose Wazzle, my friends.

[00:00:53] Lex Fridman: And now onto the full ad reads. I try to make them interesting, but if you skip, please still check out our sponsors. I enjoy their stuff. Maybe you will too. To get in touch with me for whatever reason, go to lexfridman.com slash contact. All right, let's go. This episode is brought to you by Shopify, a platform designed for anyone to sell anywhere with a great looking online store. Now, I know it's an incredible platform for selling stuff. It's a mechanism by which you can buy stuff on the internet.

[00:01:23] Lex Fridman: But the thing I like to celebrate is engineering. They just recently tweeted about SimGym, which runs simulated shopping sessions by the hundreds of thousands daily. I personally love the idea that things at scale, especially now with the LLM models, can be simulated. You basically want to be simulating human behavior, human decision making, human choice.

[00:01:51] Lex Fridman: In this particular context, of course, is shopping. It's really fascinating. And they describe in their blog posts how they're leveraging NVIDIA stack to accomplish this task. But you should know, in general, that you can sign up for a $1 per month trial period at shopify.com slash lex. That's all lowercase. Go to shopify.com slash lex to take your business to the next level today.

[00:02:15] Lex Fridman: This episode is also brought to you by Element, my daily zero sugar, delicious electrolyte mix. That, as far as I know, has very little to do with artificial intelligence and GPUs and CPUs and the revolution that we're experiencing in the tech sector. And I think that's beautiful because I got a chance to train a bunch of world-class fighters, wrestlers, grapplers recently. I'm going to be traveling to parts of the world that doesn't really have much.

[00:02:44] Lex Fridman: And I think in those parts of the world is where the mind can reconnect with the things that are truly important, that are truly timeless. Anyway, in those parts of the world, I often get pretty out there in terms of physical strain and diet and dehydration and so on. And so Element's one of the crucial things in my bag. Really, water and salt.

[00:03:12] Lex Fridman: And really nice, delicious, well-balanced salt, meaning sodium, potassium, magnesium, electrolytes. Element is my go-to. Watermelon salt, my favorite flavor. Get a free eight-count sample pack with any purchase. Try it at drinkelement.com slash lex. This episode was also brought to you by Finn, a powerful AI system that focuses on customer service. It's trusted by over 6,000 companies.

[00:03:41] Lex Fridman: It has a 65 average resolution rate and is built to handle complex, multi-step queries like returns, exchanges, and disputes. This is such a fascinating problem because customer problems, the bulk of them, fall into a very specific set of categories. But there's nuanced details within those categories that make all the difference. And it can be an incredibly frustrating thing for a human being like myself, I swear. I promise.

[00:04:11] Lex Fridman: Definitely not a robot. Wouldn't tell you if I was. But it's frustrating for a human to come to the customer service process and to know that your problem kind of is like this problem. There's all these details that you can provide about the system you're operating on, the specifics of the puzzle you're trying to solve. But there's details that you just know in your gut that this is important, especially if you kind of thought through the problem. I've been through this quite a bit.

[00:04:39] Lex Fridman: You want to have some level of personalization that can get to the tricky aspect, the perspective on the problem that really would lead you down the road to a solution. Anyway, love this problem. Really glad Finn is focusing on it. Go to fin.ai.lex to learn more about transforming your customer service and scaling your support team. That's fin.ai.lex. This episode is also brought to you by Quo, spelled Q-U-O.

[00:05:09] Lex Fridman: Also known as a company with just three letters will win you a game of Scrabble. That is not a joke. It feels like a joke I have made before. But let's run with it. It's a dad joke. It's a bad dad joke. The only thing worse than a dad joke is a bad dad joke. But here we go. Spelled Q-U-O. A business phone platform for calling and messaging.

[00:05:36] Lex Fridman: Basically, you have a bunch of people trying to help a larger group of people. And you want to orchestrate how they communicate with each other. And this is just the system that does it extremely well. Period. Quo integrates AI into the whole shebang. Organizing everything. Generating summaries. Highlighting the next steps. All that kind of stuff. It just does it well. The interface on top of the AI is also really strong. So try Quo for free.

[00:06:01] Lex Fridman: Plus get 20% off your first six months when you go to Quo.com slash Lex. That's Q-U-O dot com slash Lex. This is the Lex Friedman podcast. And now, dear friends, here's Jensen Huang.

[00:06:34] Lex Fridman: You've propelled NVIDIA into a new era in AI. Moving beyond its focus on chip scale design to now rack scale design. And I think it's fair to say that winning for NVIDIA for a long time used to be about building the best GPU possible. And you still do. But now you've expanded that to extreme co-design of GPU, CPU, memory, networking, storage, power, cooling, software, the rack itself, the pod that you've announced, and even the data center.

[00:07:03] Lex Fridman: So let's talk about extreme co-design. What is the hardest part of co-designing a system with that many complex components and design variables?

[00:07:12] Jensen Huang: Yeah, thanks for that question. So first of all, the reason why extreme co-design is necessary is because the problem no longer fits inside one computer to be accelerated by one GPU. The problem that you're trying to solve is you would like to go faster than the number of computers that you add. So you added, you know, 10,000 computers, but you would like it to go a million times faster.

[00:07:39] Jensen Huang: Then all of a sudden, you have to take the algorithm. You have to break up the algorithm. You have to refactor it. You have to shard the pipeline. You have to shard the data. You have to shard the model. Now, all of a sudden, when you distribute the problem this way, not just scaling up the problem, but you're distributing the problem, then everything gets in the way.

[00:08:04] Jensen Huang: This is the Amdahl's law problem, where the amount of speed up you have for something depends on how much of the total workload it is. And so if computation represents 50% of the problem, and I sped up computation infinitely, like a million times, you know, I only sped up the total workload by a factor of two.

[00:08:28] Jensen Huang: Now, all of a sudden, not only do you have to distribute the computation, you have to, you know, shard the pipeline somehow, you also have to solve the networking problem. Because you've got all of these computers are all connected together. And so distributed computing at the scale that we do, the CPU is a problem, the GPU is a problem, the networking is a problem, the switching is a problem. And distributing the workload across all these computers are a problem.

[00:08:58] Jensen Huang: It's just a massively complex computer science problem. And so we just got to bring every technology to bear. Otherwise, we scale up linearly, or we scale up based on the capabilities of Moore's law, which has largely slowed because Denard's scaling has slowed.

[00:09:18] Lex Fridman: I'm sure there's trade-offs there. Plus, you have a complete disparate disciplines here. I'm sure you have specialists in each one of these high bandwidth memory, the networking, the NVLink, the NICs, the optics and the copper that you're doing, the power delivery, the cooling, all that. I mean, there's like world experts in each of those. How do you get them in a room together to figure out?

[00:09:36] Jensen Huang: That's why my staff is so large.

[00:09:39] Lex Fridman: What's the process? Can you take me through the process of the specialists and the journalists? Like, how do you put together the rack when you know the set of things you have to shove into a rack together? Like, what does that process look like of designing it all together?

[00:09:52] Jensen Huang: There's the first question, which is, what is extreme co-design? You're optimizing across the entire stack of software, from architectures to chips to systems to system software to the algorithms to the applications. That's one layer. The second thing that you and I just talked about goes beyond CPUs and GPUs and networking chips and scale-up switches and scale-out switches.

[00:10:16] Jensen Huang: And then, of course, you've got to include power and cooling and all of that because, you know, all these computers are extremely, extremely power-hungry. They do a lot of work and they're very energy efficient, but they, in aggregate, still consume a lot of power. And so that's one, the first question is, what is it? The second question is, why is it?

[00:10:38] Jensen Huang: And we just spoke about the reason, you know, you want to distribute the workload so that you can exceed the benefit of just increasing the number of computers. And then the third question is, how is it? How do you do it? And that's kind of the miracle of this company. You know, when you're designing a computer, you have to have operating system of computers. When you're designing a company, you should first think about what is it that you want the company to produce?

[00:11:07] Jensen Huang: You know, I see a lot of companies' organization charts and they all look the same. Hamburger organization charts, software organization charts, and car company organization charts, they all look the same. And it doesn't make any sense to me. You know, the goal of a company is to be the machinery, the mechanism, the system that produces the output. And that output is the product that we like to create. It is also designed, the architecture of the company should reflect the environment by which it exists.

[00:11:37] Jensen Huang: It almost directly says what you should do with the organization. My direct staff is 60 people. You know, I don't have one-on-ones with them because it's impossible. You can't have 60 people on your staff if you're, you know, going to get work done.

[00:11:52] Lex Fridman: So you still have 60 reports? You still have a course? More, yeah.

[00:11:55] Jensen Huang: More. Yeah.

[00:11:57] Lex Fridman: And most stars at least have a foot in engineering. Almost all of them.

[00:12:02] Jensen Huang: There's experts in memory. There's experts in CPUs. There's experts in optical. That's incredible. Yeah. GPUs and architecture, algorithms, design.

[00:12:13] Lex Fridman: So you constantly have an eye on the entire stack. And you're having like intense discussions about the design of the entire stack.

[00:12:20] Jensen Huang: And no conversation is ever one person. That's why I don't do one-on-ones. We present a problem and all of us attack it. You know, because we're doing extreme co-design. And literally the company is doing extreme co-design all the time.

[00:12:34] Lex Fridman: So even if you're talking about a particular component, like cooling, networking, everybody's listening in. Yeah. And they can contribute, well, this doesn't work for the power distribution. This doesn't work for the memory. This doesn't work for this.

[00:12:51] Jensen Huang: Exactly. And whoever wants to tune out, tune out. You know what I'm saying? Yeah. And the reason for that is because the people who are on the staff, they know when to pay attention. They're supposed, you know, something they could have contributed to, they didn't contribute to. I'm going to call them out, you know. And so, hey, come on, let's get in here.

[00:13:08] Lex Fridman: So as you mentioned, NVIDIA is this company that's adapting to the environment. So at which point can you say, did the environment change and begin adapting sort of secretly in the early days from GPU for gaming, maybe the early deep learning revolution to we're now going to start thinking of it as an AI factory? What does NVIDIA do? It produces AI. Let's build a factory that makes AI.

[00:13:33] Jensen Huang: I could reason through it just systematically. We started out as an accelerator company. But the problem with accelerators is that the application domain is too narrow. It has the benefit of being incredibly optimized for the job. You know, any specialist has that benefit. The problem with intense specialization is that, of course, your market reach is narrower. But that's even fine.

[00:14:00] Jensen Huang: The problem is the market size also dictates your R&D capacity. And your R&D capacity ultimately dictates the influence and impact that you can possibly have in computing. And so when we first started out as an accelerator, a very specific accelerator, we always knew that that was going to be our first step. We had to find a way to become accelerated computing.

[00:14:27] Jensen Huang: But the problem is when you become a computing company, it's too general purpose and it takes away from your specialization. I connected two words that actually have fundamental tension. The better computing company we become, the worse we became as a specialist. The more of a specialist, the less capacity we have to do overall computing.

[00:14:49] Jensen Huang: And so that and I connected those two words together on purpose, that the company has to find that really narrow path, step by step by step to expand our aperture of computing, but not give up on the most important specialization that we had. OK, so the first step that we took beyond acceleration was we invented the programmable pixel shader. So that was the first step towards programmability.

[00:15:18] Jensen Huang: You know, it was our first journey towards moving into the world of computing. The second thing that we did was we created, we put FP32 into our shaders. That FP32 step, IEEE compatible FP32, was a huge step in the direction of computing. It was the reason why all of the people who were working on stream processors and, you know, other types of data flow processors discovered us.

[00:15:48] Jensen Huang: And they said, hey, all of a sudden, you know, we might be able to use this GPU that's incredibly computationally intensive. And it's now, you know, compliant with IEEE. I could take my software that I was writing, you know, previously on CPUs and I could, you know, see about, you know, using the GPU for them. And which led us to create, put C on top of FP32 was called, we call CG. That CG path took us to eventually CUDA.

[00:16:16] Jensen Huang: CUDA, step by step by step. Well, putting CUDA on G-Force, that was a strategic decision that was very, very hard to do because it cost the company enormous amounts of our profits and we couldn't afford it at the time. But we did it anyways because we wanted to be a computing company. A computing company has a computing architecture. A computing architecture has to be compatible across all of the chips that we build. Can you take me to that decision?

[00:16:45] Lex Fridman: So putting CUDA on G-Force could not afford to do. Can you explain that decision? Why boldly choose to do that anyway? Yeah. Can you explain that decision? Excellent.

[00:16:55] Jensen Huang: That was, that was the first, I would, I would say that that was the first, the first strategic decision that, that is as close to an existential threat.

[00:17:08] Lex Fridman: But for people who don't know, it turned out to be, spoiler alert, one of the most incredibly brilliant decisions ever made by a company. So CUDA turned out to be an incredible foundation for computation in this AI infrastructure world. So, so you're just setting the context. It turned out to be a good decision.

[00:17:28] Jensen Huang: Yeah. It turned out to have been a good decision. I think the, so, so here, here's the way it went. So we invented this thing called CUDA and it expanded the, the aperture of applications that, that we can accelerate with our accelerator. The question is, how do we, how do we attract developers to CUDA?

[00:17:49] Jensen Huang: Because a computing platform is all about developers and developers don't come to a computing platform just because, you know, it could perform something interesting. They come to a computing platform because the install base is large because a developer like anybody else wants to develop software that reaches a lot of people. So the install base is in fact the single most important part of an architecture.

[00:18:15] Jensen Huang: The architecture could attract enormous amounts of criticism. For example, no architecture has ever attracted more criticism than the x86. You know, as, as a less than, less than elegant architecture, but yet it is the defining architecture of today.

[00:18:34] Jensen Huang: It gives you an example that in fact, so many risk architectures, which were beautifully architected, incredibly well designed by some of the brightest computer scientists in the world, largely failed. And so I've given you two examples where one is, you know, one is elegant, the other one's barely aesthetic. And so yet x86 survived. Install base is everything. Install base defines an architecture.

[00:19:03] Jensen Huang: Not everything else is secondary. Okay. And so there were other architectures at the time. CUDA came out. OpenCL was here. There were, you know, there's several other competing architectures. But the, the thing that the decision that we made that was good was we said, Hey, look, ultimately it's about install base. And what is the best way we could get a new computing architecture into the world? By that timeframe, GeForce had become successful.

[00:19:31] Jensen Huang: We were already selling millions and millions of GeForce GPUs a year. And we said, you know, we, we had to put CUDA on GeForce and put it into every single PC, whether customers use it or not. And use it as a starting point of cultivating our install base. Meanwhile, we'll go and attract developers and went to universities and wrote books and taught classes and put CUDA everywhere.

[00:19:59] Jensen Huang: And eventually people discover, and at the time the PC was the primary computing vehicle. There was no cloud. And we could put a supercomputer in the hands of every researcher in school, every scientist, you know, every engineering school, every, or every student in school. And eventually something amazing will happen.

[00:20:16] Jensen Huang: Well, the problem was CUDA increased our cost of that GPU, which is a consumer product so tremendously, it, it completely consumed all of the company's gross profit dollars. And so at the time the company was probably, you know, worth, I don't know at the time, eight, was it like $8 billion or something like six, $7 billion or something like that.

[00:20:41] Jensen Huang: But after we launched CUDA, I recognized that it was going to add so much cost, but it was something we believed in. You know, our market cap went down to like $1.5 billion. And so we were down, we were down there for a while and, and we clawed our way back slowly, but we carried CUDA on GeForce.

[00:21:04] Jensen Huang: I always say that NVIDIA is the house that GeForce built because it was GeForce that took CUDA out to everybody. Researchers, scientists, they discovered CUDA on GeForce because they were all, you know, many of them were gamers. Many of them built their own PCs anyways. In a university lab, many of them built clusters themselves, you know, using, using PC components. And, and so that, you know, that's kind of how we got going.

[00:21:32] Lex Fridman: And then that became the platform and the foundation for the deep learning revolution.

[00:21:36] Jensen Huang: That was also another great, great observation. Yeah.

[00:21:39] Lex Fridman: That existential moment. Do you remember, like, what were those meetings like? What were those discussions like deciding as a company, risking everything?

[00:21:50] Jensen Huang: Well, I had, I had to make it clear to the board what we're trying to do. And, and the management team knew our gross margins were going to get crushed. So you could imagine a world where GeForce would carry the burden of CUDA and none of the gamers would appreciate it. And none of the gamers would pay for it. You know, they only pay certain price and it doesn't matter what your cost is.

[00:22:16] Jensen Huang: And so, you know, we, we increased our cost by 50% and that consumed, and we were a 35% gross margin company. And so it, it was a, it was quite a difficult decision to make, but you could imagine that someday this would go into workstations and it would go into supercomputers. And, and in those segments, maybe we can capture more margin. So you could, you could reason your way into being able to afford this, but it still took, it took a decade.

[00:22:46] Lex Fridman: But that, but that's more of like conversation with the board convincing them, but you psychologically. Because NVIDIA has continued to make bold bets that predict the future and in part, especially now define the future. So I'm almost looking for wisdom about how you're able to make those decisions to make leaps like that as a company.

[00:23:16] Jensen Huang: Well, first of all, um, I'm informed by, by, by a lot of curiosity. At some point there's a reasoning system that, that convinces me, uh, so clearly this outcome will happen. Yeah. That this will happen. And so I believe, I believe it in my mind. And when I believe it in my mind, you know, you know how it is, you manifest a future and that future is so convincing.

[00:23:46] Jensen Huang: There's no way it won't happen. There's a lot of suffering in, in between, but you've got to believe what you believe.

[00:23:54] Lex Fridman: So you, you, you, you envision the future. Yeah. Yeah. And you essentially from a sort of engineering perspective manifested.

[00:24:01] Jensen Huang: Yeah. And, and you, you, you reason about how to get there. You reason about why it, it must exist. Um, and, and, um, and, you know, I reason, we all reason it here. The management team will reason about it. All the people that I, we spent a lot of time reasoning about it.

[00:24:16] Jensen Huang: The thing, the thing that the next part of it is probably a skill thing, which is, you know, oftentimes in leadership, uh, the leadership stays quiet or they learn about something and then they do some manifesto and it's a brand new year. And somehow at the end of the year, next year, we're going to have a brand new plan, big, huge layoff this way, big, huge organization change this way. New mission statement, brand new logos, um, you know, that kind of stuff. Yeah.

[00:24:45] Jensen Huang: Um, we've just never, I, I never do things that way. When I learned about something and it's starting to influence how I think I'll make it very clear to everybody near me that, you know, this, this is interesting. Um, this is going to make a difference. Uh, this is going to impact that. And I reason about things step by step by step.

[00:25:05] Jensen Huang: Oftentimes I've already made up my mind, but I'll take every possible opportunity, external information, new insights, new discoveries, uh, new engineering, you know, revelations, uh, new milestones develop. I'll take those opportunities and I'll use it to shape everybody else's belief system. And I'm doing that literally every single day. I'm doing that with my board. I'm doing that with my management team. I'm doing that with my employees.

[00:25:35] Jensen Huang: I'm trying to shape their belief system such that when I come the day I say, Hey, let's buy Mellanox. It's completely obvious to everybody that we absolutely should on the day that on the day that I, that I said, Hey guys, let's go all in on deep learning. And let me tell you why I've already been laying down the bricks to different organizations. And I'm doing that.

[00:26:03] Jensen Huang: Every organization and every, everybody, many of the people might've heard everything. Most of the company heard, here's of course, pieces of it. And on the day that I announced it, um, everybody's kind of bought into many pieces of it. And in a lot of ways, I like to announce these things. And I imagine, um, that, that the employees are kind of saying, you know, Jensen, what took you so long?

[00:26:32] Jensen Huang: And, and in fact, I've been shaping their belief system for some time and therefore leadership. Sometimes it looks like you're leading from behind, but you've been shaping their, you know, to the point where on the day that I declared it a hundred percent buy-in, but that's what you want. You want to bring everybody along. You know, otherwise we announced something about deep learning and everybody goes, what are you talking about? You know, you announced something about, let's go all in on this thing.

[00:26:58] Jensen Huang: And, and your, your management team, your board, your employees, your customers, they're kind of like, where's this coming from? You know, this is insane. And so, so GTC, in fact, if you go back in time, you look at, look at the keynotes. I'm also shaping the belief system of my partners in the industry. And, and I'm using that to shape, you know, the belief system of my own employees.

[00:27:22] Jensen Huang: And, and, and so by the time that I announced something, like for example, we just now, we just announced Grok. We've been late. I've been talking about the stepping stones for two and a half years. You guys just go back and go, oh my gosh, they've been talking about it for two and a half years. And so I've been laying the foundation step by step by step. So when the time comes, you announce it, everybody's, you know, what took you so long?

[00:27:46] Lex Fridman: But it's not just inside the company. You're shaping the landscape, the broader global landscape of innovation. Like putting those ideas out there, you really are manifesting reality.

[00:27:54] Jensen Huang: We don't build computers. We actually don't build clouds. We don't, as it turns out, we're a computing platform company. And so nobody can buy anything from us. That's the weird thing. You know, we, we vertically design, vertically integrate to design and optimize. But then we open up the entire platform at every single layer to be integrated into other companies, products and services and clouds and supercomputers and OEM computers.

[00:28:23] Jensen Huang: And so the amazing thing is I can't do what I do without having convinced them first. And so most of GTC is about manifesting a future that by the time that we, my product is ready, they're going, what took you so long? Yeah.

[00:28:41] Lex Fridman: Yeah. So one of the things you've been a believer for a long time is scaling laws broadly defined. So are you still a believer in the, in the scaling laws? Yeah. We have more scaling laws now. So I think you've outlined four of them with pre-training, post-training, test time and agentic scaling.

[00:28:59] Lex Fridman: What do you think when you think about the future, deep future and the near term future, what are the blockers that you're most concerned about to keep you up at night that you have to overcome in order to keep scaling?

[00:29:14] Jensen Huang: Well, we can go back and reflect on what people thought were blockers. So in the beginning, we were the first, the pre-training scaling law, you know, people thought, well, rightfully so that the amount of data that we have, high quality data that we have will limit the intelligence that we achieve. And that scaling law was an important, very important scaling law. The larger the model, the correspondingly more data results in a better, results in a smarter AI.

[00:29:43] Jensen Huang: And so that was pre-training and Ilya, Suscover, Ilya said, we're out of data or something like that. Pre-training is over or something like that. The industry panicked, you know, that this is the end of AI. And of course, of course, that's obviously not true. We're going to keep on scaling the amount of data that we have to train with. A lot of that data is probably going to be synthetic. And that also confused people, you know, and, and what people don't realize is they've kind of forgotten.

[00:30:12] Jensen Huang: That most of the data that, that we are training, that we teach each other with, inform each other with is synthetic. You know, I, it's synthetic because it didn't come out of nature. You created it. I'm consuming it. I modify it, augment it. I regenerate it. Somebody else consumes it.

[00:30:33] Jensen Huang: And so, so we've now reached a level where AI is able to take ground truth, augment it, enhance it, synthetically generate an enormous amount of data. And that part of post-training continues to scale. And so the amount of data that we could use that is human generated will be smaller and smaller and smaller.

[00:30:59] Jensen Huang: The amount of data that we use to train model is going to continue to scale to the point where we're no longer limited. Training is no longer limited by data is now limited by compute. And the reason for that is most of the data is synthetic. Then the next phase is a test time. And, um, I still remember people, people telling me that inference. Oh yeah, that's easy. Pre, pre-training. That's hard. These are giant systems that people are talking about.

[00:31:29] Jensen Huang: Inference must be easy. And so inference chips are going to be little tiny chips and, you know, they're not, they're not like NVIDIA's chips. Oh, those are going to be complicated and expensive. And, you know, we could make, and this is, and the future inference is going to be the biggest market and it's going to be easy. And we're going to commoditize and, you know, everybody can build their own chips. And, and, and that was always illogical to me because inference is thinking. And I think thinking is hard.

[00:31:57] Jensen Huang: Thinking is way harder than reading. You know, pre-training is just memorization and generalization, you know, and looking for patterns in relationships.

[00:32:07] Jensen Huang: You're, you're reading and reading versus thinking, reasoning, solving problems, taking unexplored experiences, new experiences, and breaking it down into decomp, decomposing it into, you know, solvable pieces that we then go off either through first principle reasoning or, you know, through, through previous examples, prior experiences, you know, or, or, or just exploration.

[00:32:36] Jensen Huang: Exploration and, and search and, you know, trying different things. And that whole process of post of, of, of test time scaling, inference is really about thinking and, and it's about reasoning. It's about planning. It's about search. It's about, and so how could that possibly be compute light? And we were absolutely right about that. You know, so, so test time scaling is intensely compute intensive. Then the question is, okay, now we're at inference and we're at test time scaling.

[00:33:06] Jensen Huang: What's beyond that? Well, obviously we have now created, you know, one agentic person and that one agentic person has a large language model that we've now, we've now, you know, developed. But during test time, that agentic system goes off and does research and bangs on databases and it goes on and, you know, uses tools.

[00:33:29] Jensen Huang: And one of the most important things it does is spins off and spawns off a whole bunch of sub agents, which means we're now creating large teams. And so, you know, it's so much easier to scale NVIDIA by hiring more employees than it is to scale myself. And so the next scaling law is the agentic scaling law. It's kind of like multiplying AI. Multiplying AI, we could spin off agents as fast as you want to spin off agents.

[00:33:57] Jensen Huang: And so, you know, you're going to have four scaling laws. And as we use the agentic systems, they're going to create a lot more data. They're going to create a lot of experiences. Some of it we're going to say, wow, this is really good. We ought to memorize this. That data set then comes all the way back to pre-training. We memorize and generalize it. We then refine it and fine tune it back into post-training.

[00:34:23] Jensen Huang: Then we enhance it even more with test time, you know, and the agents and agentic systems, you know, put it out into the industry. And so this loop, the cycle is going to go on and on and on. And it kind of comes down to basically intelligence is going to scale by one thing and it's compute.

[00:34:43] Lex Fridman: But there's a tricky thing there that you have to anticipate and predict, which is some of these components, it requires different kind of hardware to really do it optimally. So you have to anticipate where the AI innovation is going to lead. For example, make sure of experts with sparsity. Perfect. With hardware, you can't just pivot on a week's notice. You have to anticipate what that's going to look like. So good. That's so scary and difficult to do, right?

[00:35:11] Jensen Huang: For example, these AI model architectures are being invented about once every six months. Yeah. Right? And system architectures and hardware architectures kind of every three years. And so you need to anticipate what likely is going to happen, you know, two, three years from now. And there's a couple of ways that you could do that. First of all, we could do research internally ourselves. And that's one of the reasons why we have basic research.

[00:35:40] Jensen Huang: We have applied research. We create our own models. And so we have hands-on life experience right here. This is part of the co-design that I'm talking about. We're also the only AI company in the world that works with literally every AI company in the world. And to the extent that we can, we try to get a sense of what are the challenges that people are experiencing.

[00:36:00] Lex Fridman: So you're listening to the whispers across the industry, the ad labs?

[00:36:04] Jensen Huang: That's right. You've got to listen and learn from everybody. And then the last part is to have an architecture that's flexible, that can adapt and move with the wind. And one of the benefits of CUDA is that it's, you know, on the one hand, an incredible accelerator. On the other hand, it's really flexible.

[00:36:23] Jensen Huang: And so that balance, incredible balance between specialization, otherwise we can't accelerate the CPU, versus generalization so that we can adapt with changing algorithms. That's really, really important. That's the reason why CUDA has been so resilient on the one hand. And yet we continue to enhance it. We're at CUDA 13.2.

[00:36:47] Jensen Huang: And so we're evolving the architecture so fast that we can stay with, you know, with the modern algorithms. For example, when Mixture Experts came out, that's the reason why we had MVLink 72 instead of MVLink 8. We could now take an entire 4 trillion, 10 trillion parameter model and put it in one computing domain as if it's running on one GPU.

[00:37:17] Jensen Huang: People probably didn't notice. I said it, but if you look at the architecture of the Grace Blackwell racks, it was completely focused on doing one thing, processing the LLM. All of a sudden, one year later, you're looking at a Vera Rubin rack. It has storage accelerators. It has this incredible new CPU called Vera. It has Vera Rubin and MVLink 72 to run the LLMs.

[00:37:47] Jensen Huang: It also has this new additional rack called Grok. And so this entire rack system is completely different than the previous one. And it's got all these new components in it. And the reason for that is because the last one was designed to run MOE large language models, inference. And this one is to run agents and agents bang on tools.

[00:38:11] Lex Fridman: And obviously the design of the system had to have been done before Claude Code, Codex, OpenClaw. So you were anticipating the future, essentially. Yeah. And that comes from what? From the whispers, from the understanding what all the state of the art is doing?

[00:38:28] Jensen Huang: No, it's easier than that. But you just reason about it. First of all, you just reason. No matter what happens at some point, in order for that large language model to be a digital worker, let's just use that metaphor. Let's say that we want the LLM to be a digital worker. What does it have to do? It has to access ground truth. That's our file system. It has to be able to do research. It doesn't know everything.

[00:38:58] Jensen Huang: And I don't want to wait until this AI becomes universally smart about everything past, present, and future before I make it useful. And so therefore, I might as well let it go do research. It's obviously, if it wants to help me, it's got to use my tools. You know, a lot of people would say, you know, AI is going to completely destroy software. We don't need software anymore. We don't even need tools anymore. That's ridiculous. Let's use a thought experiment.

[00:39:26] Jensen Huang: And you could just sit there, enjoy a glass of whiskey, and think about all these things, and it would become completely obvious. Like if I were to create the most amazing agent that we can imagine in the next 10 years, let's say it'd be a human or robot. If that human or robot were to be created, is it more likely that the human or robot comes into my house and uses the tools that I have to do the work that it needs to do?

[00:39:55] Jensen Huang: Or does this hand turns into a 10-pound hammer in one instance, turns into a scalpel in another instance, and in order to boil water, it beams, you know, microwaves out of its fingers? You know, or is it more likely just to use the microwave, you know? And the first time it goes up to the microwave, it probably doesn't know how to use it. But that's okay. It's connected to the internet.

[00:40:19] Jensen Huang: It reads the manual of this microwave, reads it, instantly becomes an expert. And so it uses it. And so I think the, I just described, in fact, almost all of the properties of OpenClaw. You know, that it's going to use tools, that it's going to access files, it's going to be able to do research. It has IO subsystem.

[00:40:43] Jensen Huang: And when you're done reasoning through it, reasoning about it through it in that way, then you say, oh my gosh, the impact to the future computing is deeply profound. And the reason for that is, I think we've just reinvented the computer. And then now you say, okay, when did we reason about that? When did we reason about OpenClaw? If you take the OpenClaw schematic that I used at GTC, you will find it two years ago.

[00:41:12] Jensen Huang: Literally two years ago at GTC, I was talking about agentic systems that exactly reflect OpenClaw today. And of course, the confluence of many things had to happen. And first of all, we needed Claw and GPT and, you know, all of these models to reach a level of capabilities. So their innovation and their breakthroughs and their continued advances was really important.

[00:41:40] Jensen Huang: And then, of course, somebody had to create an open source, you know, project that was sufficiently robust, you know, and sufficiently complete. And that we can all put to work. And I think OpenClaw did for agentic systems what ChatGPT did for generative systems. And I just think it's a very big deal.

[00:42:03] Lex Fridman: Yeah, it's a really special moment. I'm not exactly sure why it captured so much of the world's attention, but it did more than CloudCode and Codex and so on. Because consumers could reach it. Sure, yeah. But there's also so much of this is vibes. And Peter, I had a podcast with him, a wonderful human being. So part of it is also the humans that represent the thing. Yeah, no doubt. Part of it is memes. Because we're all trying to figure it out.

[00:42:30] Lex Fridman: There's really serious and complicated security concerns about when you have such powerful technology, how do you hand over your data so they can do useful stuff? But then there's scary things associated with that. And we as a civilization, as individual people and as a civilization figuring out how to find that right balance.

[00:42:46] Jensen Huang: Yeah, we jumped on it right away and we sent a bunch of security experts its way. And we did this thing called OpenShell. It's already been integrated into OpenClaw.

[00:42:57] Lex Fridman: And Nvidia put forward NemoClaw. Yeah, exactly. They install super easy.

[00:43:02] Jensen Huang: It makes sure that it's secure. We give you two out of three rights. Agentic systems can access sensitive information. It can execute code. And it can communicate externally. We could keep things safe if we gave you two out of those three capabilities at any time, but not all three. And out of those two out of three capabilities, we also give you access control based on whatever rights that you're given by enterprise.

[00:43:30] Jensen Huang: And then we connect it to a policy engine that all these enterprises already have. And so we're going to try to do our best to help OpenClaw become a better claw.

[00:43:41] Lex Fridman: So you eloquently explained how we have a long history of blockers that we thought were going to be blockers and we overcame them. But now looking into the future, what do you think might be the blockers? Now that it's clear that agents will be everywhere. So it's obviously we're going to need compute. So what is going to be the blocker for that scaling?

[00:44:01] Jensen Huang: Power is a concern, but it's not the only concern. But that's the reason why we're pushing so hard on extreme co-design so that we can improve the tokens per second per watt orders of magnitude every single year. And so in the last 10 years, Moore's law would have progressed computing about 100 times in the last 10 years. We progressed and scaled up computing by a million times in the last 10 years.

[00:44:30] Jensen Huang: And so we're going to keep on doing that through extreme co-design. So energy efficiency per watt completely affects the revenues of a company. It affects the revenues of a factory. And we're just going to push that to the limit so that we can keep on driving token costs down as fast as we can. You know, our computer price is going up, but our token generation effectiveness is going up so much faster.

[00:45:00] Jensen Huang: The token cost is coming down. It's just it's coming down an order of magnitude every year.

[00:45:05] Lex Fridman: So power, that's an interesting one. So the way to try to get around the power blocker is to try to, with the tokens per second per watt, try to make it more and more efficient. Of course, there's the question of how do we get more power? We should also get more power. That's a really complicated one. You've talked about small modular nuclear power plants. There's all kinds of ideas for energy. How much does it keep you up at night, the bottlenecks in the supply chain of AI?

[00:45:30] Lex Fridman: Like ASML with EUV lithography machines, GSMC with advanced packaging, like COOS, and SK Hennix with high bandwidth memory.

[00:45:40] Jensen Huang: All the time. And we're working on it all the time. No company in history has ever grown at a scale that we're growing while accelerating that growth. It's incredible. Yeah. And it's hard for people to even understand this. In the overall world of AI computing, we're increasing share. And so supply chain upstream and downstream are really important to us.

[00:46:05] Jensen Huang: I spend a lot of time informing all the CEOs that I work with. What are the dynamics that's going to cause the growth to continue or even accelerate? It's part of the reasons why to the entire right-hand side of me were CEOs of practically the entire IT industry upstream and practically the entire infrastructure industry downstream.

[00:46:33] Jensen Huang: And there were several hundred CEOs. And I don't think there's ever been keynotes where several hundred CEOs show up. And part of it is I'm telling them about our business condition now. I'm telling them about the growth drivers in the very near future and what's happening. And I'm also describing where are we going to go next so that they could use all of this information and all of the dynamics that are here to inform how they want to invest.

[00:47:02] Jensen Huang: And so I inform them that way like I inform my own employees. And then, of course, then I make trips out to them and make sure that, hey, listen, I want you to know this quarter, this coming year, this next year, these things are going to happen. And if you look at the CEOs of the DRAM industry, the number one DRAM in the world was DDR memory for CPUs and data centers.

[00:47:32] Jensen Huang: About three years ago, I was able to convince several of the CEOs that even though at the time HBM memory was used quite scarcely, you know, and barely by supercomputers, that this was going to be a mainstream memory for data centers in the future. And at first it sounded ridiculous. But several of the CEOs believed me and decided to invest in building HBM memories.

[00:47:57] Jensen Huang: Another memory was rather odd to put into a data center is the low power memories that we use for cell phones. And we wanted them to adapt them for supercomputers in the data center. And they go, cell phone memory for supercomputers? And I explained to them why. Well, look at these two memories, LPDDR5, HBM4. The volumes are so incredible. All three of them had record years in history. And these are 45-year companies.

[00:48:27] Jensen Huang: And so, you know, that's part of my job is to inform and shape, inspire, you know.

[00:48:37] Lex Fridman: So you're not just manifesting the future and maybe inspiring NVIDIA, the different engineers of the company. You're manifesting the supply chain of the future. So you're having conversations with TSMC, with ASML.

[00:48:51] Jensen Huang: Upstream, downstream.

[00:48:53] Lex Fridman: Upstream, downstream. So that's the thing.

[00:48:55] Jensen Huang: GEV, Caterpillar. Yeah, that's downstream from us. Yeah, yeah.

[00:49:00] Lex Fridman: Yeah, the whole thing. I mean, but that's so, there's so much incredibly difficult engineering that happens in the entire semiconductor industry. And it just feels scary how intricate the supply chain is, how many components there are.

[00:49:18] Jensen Huang: But it works somehow. Exactly. The deep science, the deep engineering, the incredible manufacturing. And so much of the manufacturing is already robotics. But we have a couple of hundred suppliers that contribute the technology that goes into our 1.3 million component rack. Each rack is 1.3, one and a half million components. There are 200 suppliers across the Verirubin rack.

[00:49:46] Lex Fridman: So it's interesting that you don't list that as the thing that keeps you up at night in the list of blockers.

[00:49:51] Jensen Huang: But I'm doing all the things necessary to see. I can go to sleep because I checked it off. I said, okay. You know, I can go to sleep. I go, well, let's see. Let's reason about this. What's important for us? Okay, let's reason about this. Because we changed the system architecture from the original DGX1 that you remembered to NVLink 72 rack scale computing. What does that mean?

[00:50:20] Jensen Huang: What does that mean to software? What does that mean to engineering? What does that mean to how we design and test? And what does that mean to the supply chain? Well, one of the things that it meant was we moved supercomputer integration at the data center into supercomputer manufacturing in the supply chain. If you're doing that, you also have to recognize you're going to move.

[00:50:47] Jensen Huang: And if your total footprint of whatever data center you're going to build, let's say you would like to have 50 gigawatts of supercomputers that are running simultaneously. And it takes one week to manufacture that 50 gigawatts of supercomputers. Then each week in the supply chain, the supercomputers are going to need a gigawatt of power.

[00:51:15] Jensen Huang: And so we're going to need the supply chain to increase the amount of power it has to build, test, to build and test the supercomputers in the supply chain before I ship it. Well, NVLink 72 literally builds supercomputers in the supply chain and ships them two, three tons at a time per rack. It used to be, they used to come in parts and we used to assemble them inside the data center. But that's impossible now because NVLink 72 is so dense. And so that's an example.

[00:51:44] Jensen Huang: And I would have to go into, you know, I fly into the supply chain, go meet my partners and hey, I said, guess what? So here's what I'm going to do with, this is the way we used to build our DGXs. We're going to build them this way. This is going to be so much better because we're going to need them for inference. The market for inference is, you know, coming. The inflection point for inference is coming. It's going to be a big market. And so I first explain to them what's going on, why it's going to happen.

[00:52:10] Jensen Huang: And then I ask them to make several billion dollars of capital investments each. And because they, you know, they trust me and I'm very respectful of them. And I give them every opportunity to question me. And I spend time to explain things to people and I reason about it. I draw them pictures and I reason about it in first principles. And by the time I'm done with them, there's no what to do.

[00:52:37] Lex Fridman: So a lot of it is about relationships and building a shared view of the future. Yeah. But do you worry about certain bottlenecks? I mean, what are the biggest bottlenecks in the supply chain? Are you worried about ASMLs, EV tooling? Are you worried about the packaging, COOS packaging of TSMC? About how fast it could scale. Like you said, you're not only growing incredibly fast, you're accelerating your growth.

[00:53:02] Lex Fridman: So it feels like everybody in the supply chain, and those are certainly bottlenecks, would have to scale up. Are you having conversations with them? Like how can you scale this faster?

[00:53:13] Jensen Huang: Do you worry about it?

[00:53:14] Unidentified: No.

[00:53:15] Jensen Huang: Okay. Because I told them what I needed. They understood what I need. They told me what they're going to go do. And I believe in what they're going to do.

[00:53:23] Lex Fridman: Interesting. Yeah. That's great to hear. So maybe if we can just linger on the power for a little bit, what are your hopes for how to solve the energy problem?

[00:53:32] Jensen Huang: One of the areas that I would love us to talk about and just get the message out. You know, our power grid is designed for the worst case condition with some margin. Well, 99% of the time, we're nowhere near the worst case condition because the worst case condition is a few days in the winter, a few days in the summer and extreme weather.

[00:54:01] Jensen Huang: Most of the time, we're nowhere near the worst case condition and we're probably running around, call it 60% of peak. And so 99% of the time, our power grid has excess power and they're just sitting idle. But they have to be there sitting idle because just in case, when the time comes, hospitals have to be powered and, you know, infrastructure has to be powered and airports have to run and so on and so forth.

[00:54:27] Jensen Huang: And so the question that I have is whether we could go and help them understand and create contractual agreements and design computer architecture systems, data centers, such that when they need the maximum power for infrastructure in society, that the data centers would get less. But that's in a very rare instance anyways.

[00:54:52] Jensen Huang: And during that time, we either have a backup generator for that little part of it or we just have our computers shift the workload somewhere else or we have the computers just run slower. You know, we could degrade our performance, reduce our power consumption and provide for, you know, a slightly longer latency response, you know, when somebody asked for, you know, asked for an answer.

[00:55:14] Jensen Huang: And so I think that that way of using computers, of building data centers, instead of expecting 100% uptime and these contracts that are really, really quite rigorous, it's putting a lot of pressure on the grid to be able to, now they're going to have to increase from their maximum. I just want to use their excess. It's just sitting there.

[00:55:38] Lex Fridman: Yeah, that's not talked about enough. So what's stopping there? Is it regulation? Is it bureaucracy?

[00:55:44] Jensen Huang: I think it's a three-way problem. It starts with the end customer. The end customer puts requirements on the data centers that they can never not be available. Okay, so that the end customer expects perfection. Now, in order to deliver that perfection, you need a combination of backup generators and your grid power supplier to deliver on perfection. And so everybody's got to have six nines.

[00:56:14] Jensen Huang: Well, I think first of all, right now, we ought to have everybody understand that when the customer asks for these things, you got somebody, you have somebody in your data center operations team disconnected from the CEO. I bet the CEO doesn't know this. I'm going to talk to all the CEOs. The CEOs are probably not paying any attention to the contracts that are being signed. And so everybody wants to sign the best contract, of course.

[00:56:38] Jensen Huang: And they go down to the cloud service providers and the contract, the two contract negotiators that are, I could just see them now, you know, negotiating these multi-year contracts. Both sides want, you know, the best contract. As a result, the CSPs then have to go down to the utilities and they expect the six nines.

[00:57:01] Jensen Huang: And so I think the first thing is just make sure that all of the customers, the CEOs of the customers realize what they're asking for. Now, the second thing is we have to build data centers that gracefully degrade. And so if the power, if the utility of the grid tells us, listen, we're going to have to back you down to about 80 percent. We're going to say that's no problem at all. We're just going to move our workload around.

[00:57:25] Jensen Huang: We're going to make sure that data is never lost, but we can reduce the computing rate and use less energy. The quality of service degrades a little bit. For the critical workloads, I shift that somewhere else right away. So I don't have that problem. And so, you know, whoever, whichever data center still has 100 percent uptime.

[00:57:45] Lex Fridman: And so how difficult of an engineering problem is that the smart dynamic allocation of power in the data center? As soon as you could specify, you could engineer it.

[00:57:54] Jensen Huang: Beautifully put. So long as it obeys the laws of physics on first principles, I think we're good. What was the third thing you were mentioning? So the second thing is the data centers. And the third thing is we need utilities to also recognize that this is an opportunity. And instead of saying, look, it's going to take me five years to increase my grid capability.

[00:58:20] Jensen Huang: If you're willing to take power of this level of guarantee, I can make them available for you next month and at this price. And so if utilities also offered more segments of power delivery promises, then I think everybody will figure out what to do with it. But there's just way too much waste in the grid right now. We should go after it.

[00:58:44] Lex Fridman: You've highly lauded Elon and XAI's accomplishment in Memphis in building Colossus supercomputer, probably in record time in just four months. It's now at 200,000 GPUs and growing very quickly. Is there something that you could speak to the understand about his approach that's instructive broadly to all the data center creators that enable that kind of accomplishment?

[00:59:12] Lex Fridman: His approach to engineering, his approach to the whole management of construction, everything.

[00:59:17] Jensen Huang: First of all, Elon is deep in so many different topics, yet he's also a really good systems thinker. And so he's able to think through multiple disciplines. And he obviously pushes things, questions everything, whether number one, is it necessary? Number two, does it have to be done this way? And does it have to take this long?

[00:59:46] Jensen Huang: And so he has the ability to question everything to the point where everything is down to its minimal amount that's necessary. You can't take anything else out. And yet the necessary capabilities of the product retains. And so he is as minimalist as you could possibly imagine. And he does it at a system scale.

[01:00:17] Jensen Huang: I also love the fact that he is represented, he is present at the point of action. You know, he'll just go there. If there's a problem, he'll just go there and show me the problem. You know, when you do all of this in combination, you overcome a lot of previous, this is just the way we do it. You know, I'm waiting for them. You know, I mean, it's just everybody has a lot of excuses.

[01:00:47] Jensen Huang: And so and then the last thing is when you act personally with so much urgency, it causes everybody else to act with urgency. You know, and every supplier has a lot of customers going on. Every supplier has a lot of projects going on. And he makes it his business that he's the top priority of everybody else's, you know, projects. And so he does that by demonstrating it.

[01:01:11] Lex Fridman: Yeah, I've been in a bunch of those meetings. It's fun to watch because really not enough people ask the question like, OK, so can this be done a lot faster? And how? Why does it have to take this long? Yeah, right. And then that becomes an engineering question often. And yes, I think when you get the ground truth of actually. I remember one of the times I was hanging out with him. He literally is going through the entire process of how to plug in cables into a rack.

[01:01:38] Lex Fridman: He's working with an engineer on the ground that's doing that task. And he's just trying to understand what does that process look like so it can be less error prone. And just building up that intuition from every single task involved in putting together the data center, you start to immediately get a sense at the detailed scale and at the broad system scale of where the inefficiencies are. And so you can make it more and more and more efficient.

[01:02:05] Lex Fridman: Plus, you have the big hammer of being able to say, let's do it totally different.

[01:02:10] Jensen Huang: Yeah, that's right.

[01:02:10] Lex Fridman: And remove all possible blockers.

[01:02:12] Jensen Huang: That's right.

[01:02:12] Lex Fridman: Is there parallels in the NVIDIA Extreme Systems co-design approach that you see in the way Elon approaches systems engineering?

[01:02:20] Jensen Huang: Well, first of all, co-design is an ultimate systems engineering problem. And so we approach the work that we do from that principle. The other thing that we do, and this is a philosophy that I thought, a state of mind, I guess, a method that I started 30 years ago. And it's called the speed of light. The speed of light is not just about the speed.

[01:02:47] Jensen Huang: The speed of light is my shorthand for what's the limit of what physics can do. And so everything that we do is compared against the speed of light. Memory speed, math speed, power, cost, time, effort, number of people, manufacturing cycle time.

[01:03:09] Jensen Huang: And when you think about latency versus throughput, when you think about cost versus throughput, cost versus capacity, all of these things, you test against the speed of light to achieve all of these different constraints separately.

[01:03:30] Jensen Huang: And then when you consider it together, you know you have to make compromises because a system that achieves extremely low latency versus a system that achieves very high throughput are architected fundamentally differently. But you want to know what's the speed of light of a system that achieves high throughput? What's the speed of light of a system that achieves low latency? And then when you think about the total system, you could make trade-offs.

[01:03:56] Jensen Huang: And so I force everybody to think about what's the first principles, the limits, the physical limits for everything before we do anything. And we test everything against that. And so that's a good frame of mind. I don't love the other methods, which is continuous improvement.

[01:04:20] Jensen Huang: The problem with continuous improvement, first of all, you should engineer something from first principles at the speed, you know, with speed of light thinking, limited only by physical limits and physics limits. And after that, of course, you would improve it over time. But I don't like going into a problem and somebody says, hey, you know, it takes 74 days to do this today, right now.

[01:04:48] Jensen Huang: And we can do it for you in 72 days. You know, I'd rather strip it all back to zero and say, first of all, explain to me why it's 74 days in the first place. And let's know, let's think about what's possible today. And if I were to build it completely from scratch, you know, how long would it take? Oftentimes you'd be surprised and might come to six days.

[01:05:09] Jensen Huang: Now the rest of the six days to 74 could be very well reasoned and compromises and, you know, cost reductions and all kinds of different things. But at least you know what they are. And now that you know that six days is possible, then the conversation from 74 to 6, surprisingly much more effective.

[01:05:31] Lex Fridman: In such incredibly complex systems that you're working with, is simplicity sometimes a good heuristic to reach for? I mean, if I can just, I mean, the pod, the Vera Rubin pod that you announced is just incredible.

[01:05:45] Lex Fridman: Uh, we're talking about seven chips, seven chip types, five purpose built rack types, 40 racks, 1.2 quadrillion transistors, nearly 20,000 NVIDIA dies, over 1100 Rubin GPUs, 60 exaflops, 10 petabytes per second of scale bandwidth. Uh, that's all just one. That's just one pod. That's just one pod. Yeah, that's just one pod.

[01:06:09] Lex Fridman: I mean, so you have the, and then even the, the NBL 72 rack alone is 1.3 million components, 1300 chips, 4,000 pounds crammed into a single 19 inch wide rack.

[01:06:21] Jensen Huang: And Lex, we'll probably kind of crank out about 200 of these pods a week, just to put in perspective.

[01:06:27] Lex Fridman: The, the amount of different components, I suppose simplicity is impossible, but is that a metric that you kind of reach for in trying to design things?

[01:06:36] Jensen Huang: You know, the phrase, the phrase that I use most often is we, we need things to be as complex as necessary, but as simple as possible. And, and so the question is, is all that complexity there necessary? And we ought to test for that. And we ought to challenge that. And then after that, everything else above it, you know, it's gratuitous.

[01:06:58] Lex Fridman: But it's some of the most incredible semiconductor industry broadly, but what NVIDIA is doing, uh, some of the greatest engineering in history. So these systems are just truly, truly marvels of engineering.

[01:07:11] Jensen Huang: It is the most complex computer the world has ever made.

[01:07:14] Lex Fridman: Yeah. The engineering teams, I mean, I don't know, it's not a competition, but I don't know if, if it was like an Olympics of engineering teams. I mean, TSMC does incredible engineering, like I said, ASML at every scale, but NVIDIA is going to give them a run for their money.

[01:07:28] Unidentified: Yeah. Just incredible, incredible teams.

[01:07:30] Jensen Huang: Gold medalists in every single, every single sport all assembled right here. And have to work together and report directly to you.

[01:07:37] Lex Fridman: This is wonderful. Uh, you've recently traveled to China. Uh, so it's interesting to ask you, uh, China has been incredibly successful in building up its technology sector. What do you understand about, um, how China is able to, over the past 10 years, build so many incredible world-class companies, world-class engineering teams, and just this technology ecosystem that produces so many, um, incredible products?

[01:08:06] Jensen Huang: A whole bunch of reasons for, well, first of all, let's start, let's start with some facts. 50% of the world's AI researchers are Chinese. Plus or minus. And they're mostly in China. Um, they, their tech industry showed up at precisely the right time. At the time of the mobile cloud era, uh, their way of contributing was software.

[01:08:36] Jensen Huang: And so this is a country's incredible science and math, uh, really well-educated kids. Um, uh, their tech industry was created during the era of software. They're very comfortable with modern software. China is not one giant economic country. It's got many provinces and cities with mayors all competing with each other. That's the reason why there's so many EV companies.

[01:09:05] Jensen Huang: That's the reason why there's so many AI companies. That's the reason why there's so many, every company you could imagine. Um, they all create some of them. And, and, um, as a result, they have insane competition internally. And, you know, what remains is an incredible company. Um, they also have a, um, social culture where, where it's family first, friend second, and company third.

[01:09:35] Jensen Huang: And so, um, the amount of conversation that goes back and forth between, they're essentially open source all the time. So the fact that they contribute more to open source is so sensible because they're probably, what are we protecting? You know, my engineers, their brothers are in that company. Their friends are in that company and they're all schoolmates.

[01:10:02] Jensen Huang: You know, the schoolmate concept is a, you know, one schoolmate, your brother for life. And, um, and so they, they, they share knowledge very, very quickly. And so there's no sense keeping technology hidden. You might as well put it on open source. And so the open source community then amplifies, accelerates the, the innovation process. So you get this rapid, incredible, great talent, rapid innovation because of open source and just,

[01:10:31] Jensen Huang: you know, the, the nature of friends and, and, um, insane competition among, among the company. What emerges is incredible stuff. And so this is the fastest innovating country in the world today. And this is something that has everything, everything that I've just said is fundamental to just how the kids were grown. The fact that they have excellent education, the fact that they, parents want them to do well in school.

[01:10:59] Jensen Huang: The fact that they, their culture is that way. These are, you know, these are just the thing about their country. And they showed up at a precisely the time when technology is going through that exponential.

[01:11:10] Lex Fridman: Plus culturally, it's pretty cool to be an engineer. It connects to all the components that you're mentioning. It's a, it's a builder nation. It's a builder nation.

[01:11:20] Jensen Huang: Yeah. It's a builder nation. Um, our country's leaders, incredible, but they're mostly lawyers. Their country's leaders, and because we're, they're trying to keep us safe, uh, rule of law, uh, governing their country was, built out of poverty. And so most of their leaders are incredible engineers, some of the brightest minds.

[01:11:44] Lex Fridman: To take a small tangent, because you mentioned open source, I have to go to perplexity here, who you've been a fan of a long time. I love it. Yeah. And thank you for releasing open source, Nemetron 3 Super, which you can also use inside perplexity to look stuff up.

[01:12:00] Unidentified: Yeah.

[01:12:01] Lex Fridman: Uh, which is a 120 billion parameter, open weight, uh, MOE model. Uh, what's your vision with open source? So you mentioned China with, with DeepSeq and Minimax with all these companies really pushing forward the open source, uh, AI movement. And NVIDIA is really leading the way in, um, close to state of the art open source LMs.

[01:12:28] Jensen Huang: What's your vision there? First, if we're going to be a great AI computing company, we have to understand how AI models are evolving. One of the things that I love about Nemetron 3 is this, is not a, just a pure transformer model. It's transformer and SSMs. And, uh, we were early in, uh, developing the, the, uh, conditional GANS, which that progressive GANS, which led step-by-step to diffusion.

[01:12:57] Jensen Huang: And so, um, the fact that we're doing basic research in model architecture and in different domains gives us visibility into, you know, what kind of computing systems would do a good job for future models. And so it is part of our extreme co-design strategy.

[01:13:14] Jensen Huang: Second, um, I think we, we right, rightfully recognize that on the one hand, we want world-class models as products and they should be proprietary. On the other hand, we also want AI to diffuse into every industry and every country, every researcher, every student.

[01:13:38] Jensen Huang: And if everything's proprietary, it's hard to do research and it's hard to innovate on top of, around, with. And so open source is fundamentally necessary for many industries to join the AI revolution.

[01:13:56] Jensen Huang: NVIDIA has the scale and we have the motives to not only skills, scale, and motivation to build and continue to build these AI models for as long as we shall live. And so therefore we ought to do that. We can open up, we can activate every industry, every researcher, you know, every country to be able to join the AI revolution.

[01:14:22] Jensen Huang: There's the third reason, which is from that to recognizing that AI is not just language. These AIs will likely use tools and models and sub-agents that were trained on other modalities of information. Maybe it's biology or chemistry or, you know, laws of physics or, you know, fluids and thermodynamics. And not all of it is in language structure.

[01:14:51] Jensen Huang: And so somebody has to go make sure that weather prediction, biology, AI, AI for biology, physical AI, all of that stuff stays, can be pushed to the limits and pushed to the frontier. We don't build cars, but we want to make sure every car company has access to great models. We don't discover drugs, but I want to make sure that Lily has the world's best biology, AI systems so that they can go use it for discovering drugs.

[01:15:20] Jensen Huang: And so these three fundamental reasons, both in recognizing that AI is not just language, that AI is really broad, that we want to engage everybody into the world of AI, and then also co-design of AI.

[01:15:33] Lex Fridman: Well, I have to say, once again, thank you for open sourcing, really, truly open sourcing Nemetron 3.

[01:15:40] Jensen Huang: Yeah, I appreciate you for saying that. We open source the models, we open source the weights, we open source the data, we open source how we created it. Yeah, it's pretty amazing.

[01:15:50] Lex Fridman: It's really incredible. You're originally from Taiwan and have a close relationship with TSMC. So I have to ask, TSMC, I think, also is a legendary company in terms of the engineering teams, in terms of the incredible engineering work that they do.

[01:16:07] Lex Fridman: What do you understand about TSMC culture and their approach that explains how they're able to achieve this singular unmatched success in everything they're doing with semiconductors?

[01:16:21] Jensen Huang: You know, first of all, the deepest misunderstanding about TSMC is that their technology is all they have. That somehow they have a really great transistor. And if somebody shows up another transistor, game over. It's the technology.

[01:16:45] Jensen Huang: And of course, you know, I don't mean just the transistor and metallization systems, the packaging, the 3D packaging, the silicon photonics, you know, all of the technology that they have. That technology is really what makes the company special. Their technology makes the company special.

[01:17:01] Jensen Huang: But their ability to orchestrate the demands, the dynamic demands of hundreds of companies in the world as they're moving up, shifting out, you know, increasing, decreasing, pushing out, pulling in, changing from customer to customer.

[01:17:24] Jensen Huang: Wafer, wafer starting, wafer stopping, emergency wafer starts, you know, all of this dynamics of the world's complexity as the world is shape shifting all the time. And somehow they're running a factory with high throughput, high yields, really great costs, excellent customer service. They take their work, they take their promises seriously.

[01:17:51] Jensen Huang: Then when you're wafered, because they know that you're helping, they're helping you run your company. When the wafers, when the wafers were promised to show up, the wafers show up, you know, so that you could run your company appropriately. And so their system, their manufacturing system is completely miraculous. I would say then the second thing is their culture. This culture is simultaneously technology focused on one hand, advancing technology. Simultaneously customer service oriented on the other hand.

[01:18:19] Jensen Huang: A lot of companies are very customer service oriented, but they're not very technology excellent. They're not at the bleeding edge of technology. Or a lot of companies who are at the bleeding edge of technology, but they're not the best customer service oriented company. And so it just depends on somehow they've balanced these two and they're world class of both.

[01:18:41] Jensen Huang: And then probably the third thing is the technology that I most value in them, that they created this, you know, this intangible called trust. I trust them to put my company on top of them. That's a very big deal.

[01:18:56] Lex Fridman: Well, they trust. I mean, there's a really close relationship there that you've established and that trust is established based on many years of performance. But there's human relationships involved there as well. Three decades.

[01:19:07] Jensen Huang: I don't know how many tens, hundreds of billions of dollars of business we've done through them. And we don't have a contract. That's pretty great. Amazing.

[01:19:17] Lex Fridman: Okay. There's a story that in 2013, the founders of TSMC, Morris Chang, offered you the chance to become TSMC's chief executive. And you said you already had a job. Is this story true? The story is true.

[01:19:32] Jensen Huang: I didn't dismiss it. Yeah. But I was deeply honored. And of course, I knew then, as I know now, TSMC is one of the most consequential companies in history.

[01:19:45] Unidentified: Yeah.

[01:19:45] Jensen Huang: And Morris is one of the highest regarded executive and business and personal friend that I've had in my life. And for him to ask is, I was humbled and really honored. But the work that I'm doing here is really important.

[01:20:09] Jensen Huang: And I've seen, you know, in my mind anyways, in my mind's eye, what NVIDIA was going to be and what the impact that we could have. And it was really important work. And it's my responsibility, you know, my sole responsibility to make this happen. And so I declined it, you know, not because it wasn't an incredible offer. It's an unbelievable offer.

[01:20:38] Jensen Huang: But I simply couldn't take it.

[01:20:40] Lex Fridman: I think NVIDIA, both NVIDIA and TSMC are two of the greatest companies in the history of human civilization. Running either one, I'm sure, is an incredibly complicated effort. And it takes, you have to truly be all in. Yeah. Everybody at every scale, not just at the CEO level, everybody is really truly all in. Yeah. No doubt. To accomplish this kind of complexity. See, now I can help both companies. Exactly. So NVIDIA is now the most valuable company in the world.

[01:21:09] Lex Fridman: I have to ask, what is the NVIDIA's biggest moat? As the folks in the tech sector say. The edge you have that protects you from the competition.

[01:21:21] Jensen Huang: Our single most important property as a company is the install base of our computing platform. Our single most important thing today is the install base of CUDA. Now, the reason why, 20 years ago, of course, there was no install base.

[01:21:47] Jensen Huang: But what makes, and if somebody came up with a CUDA or a TUDA, it wouldn't make any difference at all. And the reason for that is because it's never been just about the technology. The technology, of course, was incredible visionary. But it's the fact that the company was dedicated to it, stuck with it, expanded its reach. It wasn't three people that made CUDA successful.

[01:22:15] Jensen Huang: It was 43,000 people that made CUDA successful. And the several million developers that believed in us, that trusted that we were going to continue to make CUDA 1, 2, 3, 13, that they decided to port and dedicate their software on top of it. Their mountain of software on top of it. And so the install base is the number one most important advantage.

[01:22:39] Jensen Huang: That install base, when you amplified with the velocity of our execution at the scale that we're talking about, no company in history had ever built systems of this complexity, period. And then to build it once a year is impossible. And that velocity combined with the install base, in the developer's mind, is just going to now take a developer's mind.

[01:23:07] Jensen Huang: From the developer's perspective, if I support CUDA, tomorrow it will be 10 times better. I just have to wait six months on average. Not only that, if I develop it on CUDA, I reach a few hundred million people, computers. I'm in every cloud. I'm in every computer company. I'm in every single industry. I'm in every single country.

[01:23:32] Jensen Huang: So if I create an open source package and I put it on CUDA first, I get these built attributes simultaneously. And not only that, I trust 100% that NVIDIA is going to keep CUDA around and maintain it and improve it and keep optimizing the libraries. For as long as they shall live. You could take that to the bank and that last part, trust.

[01:24:02] Jensen Huang: You put all that stuff together. If I were a developer today, I would target CUDA first. I would target CUDA most. And that's the reason that I think in the final analysis is our first, that's even our first core advantage. Our second one is our ecosystem. The fact that we vertically integrated this incredibly complex system, but we integrated horizontally into every single company's computers.

[01:24:32] Jensen Huang: We're in the Google Cloud. We're in Amazon. We're in Azure. You know, we're ramping up AWS like crazy right now. We're in new companies like CoreWeave and then scale. We're in supercomputers at Lilly. We're in enterprise computers. We're at the edge in radio base stations. You know, it's just crazy. One architecture is in all these different systems. We're in cars. We're in robots. We're in satellites. We're out in space.

[01:24:56] Jensen Huang: And so the fact that you have this one architecture and the ecosystem is so broad, it basically covers every single industry in the world.

[01:25:04] Lex Fridman: Well, how does the CUDA install base evolve into the future with AI factories as a moat? Do you think it's possible that NVIDIA of the future is all about the AI factory?

[01:25:17] Jensen Huang: Well, the unit of computing used to be GPU to us. Then it became a computer. Then it became a cluster. Now it's an entire AI factory. When I see a computer, when I see what NVIDIA builds, in the old days, I would, you know, I visualize the chip. And then when I announced a new product, you know, new generation, like, ladies and gentlemen, we're announcing Ampere today. I pick up the chip. Yeah. That was my mental model of what I was building.

[01:25:46] Jensen Huang: Today, picking up the chip is kind of still adorable, but it's adorable. It's not my mental model of what I'm doing. My mental model is this giant gigawatt thing that has power generation. It's connected to the grid. It's got cooling systems and networking of incredible monstrosity. You know, 10,000 people are in there trying to install it. Hundreds of networking engineers in there. Thousands of engineers behind it trying to power it up.

[01:26:15] Jensen Huang: You know, powering up one of those factories, as you know, it's not somebody going, it's on now. Takes thousands of people to bring it up.

[01:26:24] Lex Fridman: So mentally, you're actually, when you're thinking about a single unit of compute, you're like, literally, when you go to bed at night, you're thinking now about collection of racks. So pods, not individual chips.

[01:26:35] Jensen Huang: Entire infrastructure. And I'm hoping my next click is, when I'm thinking about building computers, it's, you know, planetary scale. That'll be the next click.

[01:26:43] Lex Fridman: What do you think about the space angle? Elon has talked about doing compute in space for solving some of the, it makes some of the energy issues in terms of scaling energy easier. Cooling issues is not easy, you know. Cooling. Well, there's a large number of engineering complexities involved with that. Yeah. So what, you know, NVIDIA has also announced that you're already thinking about that.

[01:27:10] Jensen Huang: Yeah, we're already there. NVIDIA GPUs are the first GPUs in space. And I didn't realize it was, it was so interesting to, I would have declared it maybe. We're in space. You know, little, little astronaut suit on one of our GPUs. But, but we've been in space. It's the right place to do a lot of imaging, you know, because those satellites have really high resolution imaging systems.

[01:27:37] Jensen Huang: And they're sweeping the earth, you know, continuously now. And you want, you know, centimeter scale, you know, imaging that is done continuously for the world. So, you know, you'll basically have real time telemetry of everything. You don't want to beam that back down to earth. It's just, you know, petabytes and petabytes of data. You got to just do AI right there at the edge. Throw away everything you don't need. You've seen before, didn't change.

[01:28:06] Jensen Huang: And then just keep the stuff that you need. And so, AI ought to be done at the edge. Obviously, we have 24-7 solar if we put it at the polars. And, but, you know, there's no conduction, no convection. And so, you know, you're pretty much just radiation. And, but, you know, space is big. I guess, you know, we're just going to put big giant radiators out there.

[01:28:33] Lex Fridman: How crazy of an idea do you think it is? Like, is this, is this five years out, 10 years out, 20 years out? So, we're talking about blockers for AI scaling.

[01:28:42] Jensen Huang: You know, I'm just so much more practical. I look for where, where my next, next bucket of opportunities are first. Meanwhile, I'm cultivating space. And so, I sent, I sent engineers to go work on the problem. We're starting, we're learning a lot about it. How do we do with radiation? How do we do with degrading performance? How do we deal with continuous testing and attestation of defects?

[01:29:13] Jensen Huang: And, you know, how do we deal with redundancy? And how do we degrade gracefully? And things like that. And so, we could, we could do, what about software? How do you think about software and redundancy and performance out in space? Make it so that, so that the computer never breaks. It just gets slower, you know. And I, so we could start doing a lot of engineering exploration up front. But in the meantime, my, my favorite answer is eliminate waste.

[01:29:42] Jensen Huang: You know, we've, we've got all that idle power. I want to evacuate it as fast as possible.

[01:29:48] Lex Fridman: Yeah, there, yeah, there's a lot of low-hanging fruit here on earth. Yeah. That we can utilize for the AI scaling. Quick pause. Quick 30-second thank you to our sponsors. Check them out in the description. It really is the best way to support this podcast. Go to lexfriedman.com slash sponsors. We got Perplexity for curiosity-driven knowledge exploration. Shopify for selling stuff online. Element for electrolytes.

[01:30:16] Lex Fridman: Fin for customer service AI agents. And Quo for a phone system like calls, texts, contacts for your business. Choose wisely, my friends. And now, back to my conversation with Jensen Kwong. Do you think NVIDIA may be worth 10 trillion at some point? Let's, let's ask it this way. What does the future of the world look like where that, where that's true?

[01:30:44] Jensen Huang: I think that NVIDIA's growth is extremely likely and, in my mind, inevitable. And let me explain why. We're the largest computer company in history. That alone should beg the question, why? And the reason, of course, two reasons. First, two foundational technical reasons.

[01:31:12] Jensen Huang: The first reason is that computing went from being a retrieval-based, file retrieval system. Almost everything is a file. We pre-write something. We pre-record something. You know, we draw something. We put it on the web. We put it in a file. And we use a recommender system, some smart filter, to figure out what to retrieve for you. And so we were a pre-recording, human pre-recording, and file retrieving system. That's what a computer is, largely.

[01:31:40] Jensen Huang: To now, AI computers are contextually aware, which means that it has to process and generate tokens in real time. So we went from a retrieval-based computing system to a generative-based computing system. We're going to need a lot more processing in this new world than in the old world. We need a lot of storage in the old world. We need a lot of computation in this new world. And so that's the first part of it.

[01:32:09] Jensen Huang: We fundamentally changed computing in the way how computing is done. The only thing that would cause it to go back is if this way of computation, this way of computing generating information that's contextually relevant, situationally aware, that is grounded on new insight before it generates information, this computation-intensive way of doing computing would only go back if it's not effective.

[01:32:38] Jensen Huang: So for the last 10, 15 years while working on deep learning, if at any single moment I would have come to the conclusion that, you know what, this is not going to work out. I think this is a dead end or it's not going to scale. It's not going to solve this modality. It's not going to be used in this application. Then, of course, I would feel very differently about it. But I think the last five years has given me more confidence than the last 10 years, the previous 10 years.

[01:33:06] Jensen Huang: The second idea is computers, because it was a storage system, it was largely a warehouse. We're now building factories. Warehouses don't make much money. Factories directly correlates with a company's revenues. And so the computer did two things. Not only did it change the way it did it,

[01:33:34] Jensen Huang: its purpose in the world changed. It's no longer a computer. It's a factory. A factory is used for generation of revenues. We're now seeing not only is this factory generating products, commodities that people want to consume, we're seeing that the commodities are so interesting, so valuable to so many different audiences that the tokens are starting to segment like iPhones.

[01:34:05] Jensen Huang: You have free tokens, you have premium tokens, and you have several tokens in the middle. And so intelligence, as it turns out, you know, it's a scalable product. There's extremely high intelligence products, tokens that are used for specialized things. People will be willing to pay, you know, the idea that somebody's willing to pay $1,000 per million tokens is just around the corner. It's not if, it's only when.

[01:34:33] Jensen Huang: And so now we're seeing that the commodity that this factory makes is actually valuable and is revenue generating and profit generating. Now the question is, how many of these factories does the world need? How much, how many tokens does the world need? And how much is society willing to pay for these tokens? And what would happen to the world's economy

[01:35:03] Jensen Huang: if the productivity were to improve so substantially? What would happen? Are we going to discover new drugs, new products, new services? And so when you take these things in combination, I am absolutely certain that the world's GDP is going to accelerate in growth. I'm absolutely certain the percentage of that GDP that will be used for computation will be a hundred times more

[01:35:33] Jensen Huang: than the past because it's no longer a storage unit. It's a product generation unit. And so when you look at it in that context and then you back into what is NVIDIA's, what does NVIDIA, what does NVIDIA do and how much of that new economics, new industry would we have to benefit to address? I think we're going to be a lot, lot bigger. And then the rest of it to me is,

[01:36:03] Jensen Huang: is it possible for NVIDIA to be a, you know, $3 trillion revenues company in the near future? The answer is, of course, yes. And the reason for that is because it's not limited by any physical limits. There's nothing that I see that says, you know, gosh, $3 trillion is not possible. And as it turns out, NVIDIA supply chain is the burden is shared by 200 companies. And

[01:36:33] Jensen Huang: the fact that we scale out on the backs of with the partnership of this ecosystem question is, do we have the energy to do so? And surely we will have the energy to do so. And so all of these things combined, that number is just a number, you know? and I still remember NVIDIA was a, NVIDIA was a, the first time we crossed a billion dollars. I was reminded of a CEO who told me, you know, Jensen,

[01:37:02] Jensen Huang: it's theoretically impossible for a fabulous semiconductor company to exceed a billion dollars. and, and, and, um, I won't bore you with why, but, but the, of course, it's illogical and there's a lot of evidence we're not. And then somebody told me, you know, Jensen, you'll never be more than 25 billion dollars because of some other company. Somebody told me that you'll never be, you know, because, and then, so, those, those aren't principle, first principle

[01:37:32] Jensen Huang: reason thinking. And the simple, the simple way to think about that is what is it that we make and how large is the opportunity that we can create? Now, NVIDIA is not in the market share business. Almost everything that I just talked about don't exist. That's the part that's hard. You know, if NVIDIA was a, was a, was a 10 billion dollar company trying to take NVIDIA share, then it's easy to see for shareholders

[01:38:01] Jensen Huang: that, oh yeah, if they could just take 10% share, they could be this much larger. But it's hard for people to imagine how large we could be because there's nobody I could take share from. You know, and so, so I think that that's one of the challenges for the world is, is the imagination of the future. But I got plenty of time and I'll keep reasoning about it and I'll keep talking about it and every single GTC will become more and more real, you know, and, and then more and more people

[01:38:31] Jensen Huang: talk about it in one of these days. You know, we'll, we'll get there. But 100% we'll get there.

[01:38:35] Lex Fridman: Yeah, this view of, you know, token factories essentially, this token per second per watt and every token having value. Like it's an actual thing that brings value and it brings different kinds of value, different amounts of value to different people with value. That's the actual product. It really can be loosely thought of as the token. And so you have a bunch of token factors and it's very easy. First principle is to imagine a future given all the potential things that AI can solve that you're going to need an exponential number

[01:39:05] Lex Fridman: more of token factories.

[01:39:07] Jensen Huang: Yeah. And what's really interesting, the reason why I was so excited about it, the iPhone of tokens arrived. What do you call it?

[01:39:13] Lex Fridman: Wait,

[01:39:14] Jensen Huang: are you saying

[01:39:14] Lex Fridman: Opel Claw's iPhone?

[01:39:15] Jensen Huang: Yeah. That's interesting. Agents. Yeah, agents. True. Agents in general. The iPhone of tokens arrived. It is the fastest growing application in history. It went straight up.

[01:39:26] Lex Fridman: Yeah.

[01:39:27] Jensen Huang: Went straight up.

[01:39:28] Lex Fridman: That says something.

[01:39:29] Jensen Huang: Yep. There's no question Open Claw is the iPhone of tokens.

[01:39:33] Lex Fridman: Yeah, there's something truly, as you know, something truly special happening from about December where people really woke up to the power of Claude Code, of Codex, of Open Claw. I mean, I'm embarrassed to admit that on the way here in the airport, it's the first time I've done this in public, I was programming quote-unquote by talking to my laptop. And I was embarrassed because I was pretending

[01:40:02] Lex Fridman: like I'm talking to a human colleague. I'm not sure how I feel about the future where everybody is walking around talking to their AI, but it's such an efficient way

[01:40:13] Jensen Huang: to get stuff done. And it's more likely that your AI is bothering you all the time. And the reason for that is because it's getting stuff done so fast. Yeah. It's reporting back to you, I got that done. You know, what do you want me to do next? You know, that's the part that I think most people don't realize is the person who's going to be chatting with them, texting them most is their claws or lobster.

[01:40:39] Lex Fridman: What an incredible future. I read that you attribute a lot of your success to your ability to work harder than anyone and withstand more suffering than anyone. So, we can list many of the things that entails. I mean, dealing with failure, the constant engineering problems we've talked about, the human problems, uncertainty, responsibility, exhaustion, embarrassment, the near-death company moments that you've mentioned, but also the pressure.

[01:41:08] Lex Fridman: Now, as the CEO of this company that economies and nations strategize around, plan their financial allocations around, plan their AI infrastructure around, how do you deal with this much pressure? What gives you strength given how many nations and peoples

[01:41:33] Unidentified: depend on you? I'm conscious about the fact

[01:41:41] Jensen Huang: that NVIDIA's success is very important to the United States. We generate enormous amounts of tax revenues. We establish technology leadership for our nation. Technology leadership is important for national security. National security not just in one aspect of national security, all aspects of national security. When our country is more prosperous, we could do a better job with domestic policies and helping

[01:42:10] Jensen Huang: social benefits. Because we're generating so much re-industrialization in the United States, we're creating mountains of jobs. We're helping shift how we build things back to the United States in so many different plants, chips, computers, and of course these air factories. countries. I'm completely aware that, and I have the benefit, and this is

[01:42:39] Jensen Huang: a real gift with mainstream investors, teachers, policemen, who have somehow for whatever reason invested in NVIDIA or because they watched Jim Cramer bought some stock and now are millionaires. and I am completely aware of that circumstance. I'm aware of the circumstance that NVIDIA

[01:43:10] Jensen Huang: is central to a very large network of ecosystem partners behind us and downstream from us. And so the way I deal with that is exactly what I just did. I reasoned about what is it that we're doing? What is it causing, what's the impact that has on other people benefit, you know, positively or even through great burden, for example, to supply chain?

[01:43:40] Jensen Huang: And the question is therefore what are you going to do about it? In almost everything that I feel, I break it down, I reason about okay, what's the circumstance? What has changed? What's hard? And what am I going to do about it? And I break it down, decompose the problem. And the decomposition of these circumstances turns it into

[01:44:10] Jensen Huang: manageable things that I can do. And the only thing that I, after that I could do is did you do it? Did you either do it or did you get somebody else to do it? And if you didn't do it, you reasoned that you need to do it and you didn't do it and you didn't get anybody else to do it, then stop crying about it. You know? And so I'm fairly tough on myself. But I also break things down so that I don't panic,

[01:44:40] Jensen Huang: I can go to sleep because I've made the list of things that needed to be done and I've made sure that everything that could put our company in harm's way, could put my partners in harm's way, put our industry in harm's way, I've told somebody. Everything that I feel could put anybody in harm's way, I've told someone. And I've told that someone who could do something about it. And so I've gotten it off my chest. Or I'm doing something about it. And so after

[01:45:09] Jensen Huang: that, Lex, what else can

[01:45:12] Lex Fridman: you do? So given all the insane, intense amount of suffering on the journey of building up NVIDIA, have you hit low points psychologically? Oh yeah,

[01:45:24] Jensen Huang: oh yeah, sure. All the time. All the time.

[01:45:28] Lex Fridman: And there, you just break down the problem

[01:45:31] Jensen Huang: into pieces, see what you can do about it. attributes of AI learning, as you know, is systematic forgetting. You need to know when to forget some things. You can't memorize everything, you can't keep everything, you don't want to carry everything. One of the things that I do very quickly is I decompose the problem, I reason about the problem, and I share the load with it.

[01:46:01] Jensen Huang: When I say I tell everybody, I'm essentially sharing that burden as quickly as possible. Whatever worries me, tell somebody else, don't just keep it. You know, don't freak them out. Decompose the problem into smaller parts and inspire them to be able to go do something about it. But part of it is just forgetting. A lot of it is you got to be tough on yourself. Come on, stop crying about it, let's get going.

[01:46:31] Jensen Huang: And then you get out of bed. And then the other part is you're attracted to the next shiny light, the next future, the next opportunity, the next behind us. What's next? I think you watch this with great athletes, they just worry about the next point. The last point is behind them, the embarrassment, the setback. And because I do so much of my job

[01:47:01] Jensen Huang: publicly, Lex, you do a fair amount of your job publicly too. And so I do a lot of my job publicly. And so I say a lot of things that seem sensible at the time or funny at the time, mostly it's just because it's funny to me at the time. And then you reflect on it, it's less funny.

[01:47:21] Lex Fridman: Yeah, trust me, I know. But you basically allow yourself to be pulled by the light of the future. Forget the past and just keep working towards that. I mean, you did say there's this kind of famous thing you said that if you knew how hard it would be to build NVIDIA, it turned out to be, what is it, a million times more hard than you anticipated that you wouldn't do it. But isn't, you know,

[01:47:51] Lex Fridman: when I hear that, that's probably true about everything worth doing, right?

[01:47:55] Jensen Huang: Exactly. That is, by the way, what I was trying to explain is that there's a, there's a, incredible superpower of being, being, being, have the mind of a child, you know? And I say to myself, oftentimes when I look at something and, and almost, almost everything, my first thought is how hard can it be? You know? And so, and so you get yourself into that mode, how hard could it be?

[01:48:25] Jensen Huang: And, and nobody's ever done it, it looks gigantic, it's going to cost hundreds of billions of dollars, it's going to take, you know, all this, and you just go, yeah, but how hard could it be? You know? Yeah. How hard could it be? And, and so, so you got to get yourself into that state of mind. You don't want to, you don't want to actually over-simulate everything and all the setbacks and all the trials and tribulations and all the disappointments, you don't want to simulate all that in advance, you don't want to know that. You don't, you don't, you want to

[01:48:55] Jensen Huang: go into a new experience thinking it's going to be perfect, it's going to be great, it's going to be incredibly fun. And then while you're there, you know, you need to have, you need to have endurance, you need to have grit, so that when the setbacks actually happened and those setbacks are going to surprise you, the disappointments are going to surprise you, you know, the embarrassments are going to surprise you, the humiliations are going to surprise you, you just can't, now you just got to turn on the other bit, which is just forget about it, move on, keep moving.

[01:49:25] Jensen Huang: And to the extent that, to the extent that my assumptions about the future and why the future is going to manifest, so long as those assumptions and that input doesn't change or didn't change materially, then I should expect that the output won't change, and so my simulated output of the future is still going to happen, and if it's still going to happen, I'm still going

[01:49:55] Jensen Huang: to go after it, I believe it's going to, you know, and so there's a combination of two or three human characteristics, the ability to go into an experience fresh minded, the ability to forget the setbacks, the ability to believe in yourself, you know, to believe what you believe and stay true to that belief, but you're constantly reevaluating. This combination of three, four, five things,

[01:50:24] Jensen Huang: I think is really important for resilience, and, you know, I'm fortunate that whatever life experience has led to this, I've got kind of those four or five things, you know, I'm always curious, always learning, learning, I'm always learning from everybody, you know, I'm always asking, because I'm humble about everything, I'm always thinking, gosh, they did that so nicely, they did that so wonderfully, you know,

[01:50:54] Jensen Huang: I wonder what they're thinking through, how do they, you know, so I'm simulating everybody, in a lot of ways, you know, in a lot almost everybody I watch, right, you're empathetic towards everything that they do, that you're observing and respect, and so you're constantly learning and you know.

[01:51:12] Lex Fridman: You're now one of the wealthiest people on earth, one of the most successful humans on earth, is it harder to be humble and to be able to, do you feel the effect of money and power and fame in making it harder for you to sort of be wrong in your own head, enough to hear out an opinion of somebody else when it disagrees with you and learn from them, those kinds of things?

[01:51:44] Jensen Huang: Surprisingly, no, and I would actually go the other way. Because I do so much of my work publicly, when I'm wrong, pretty much everybody sees it. You get humbled. Yeah, and when I'm wrong, when I'm wrong or it didn't turn out that way or, you know, most of the things that I say outside, I'm fairly certain about and the reason for that is because it's going to impact somebody else and I want to be

[01:52:14] Jensen Huang: quite concerned about that and quite circumspect about that. For stuff that I'm reasoning about inside a meeting, you know, a lot of things could turn out differently. And so, but it doesn't ever stop me from reasoning. The way that I manage and lead, you know, I'm constantly reasoning in front of people and even when I'm talking to you, you can kind of see me kind of reasoning through things and I want to make sure that you understand what I'm saying, not because I told you, because I'm so humble about what I'm about

[01:52:43] Jensen Huang: to tell you. I kind of show you the steps that I got there and then you could decide whether you believe what I said in the end. And so, I'm doing that all day long in meetings with all of my employees. I'm constantly reasoning through, let me tell you how I see it and I reason through it. It gives everybody the opportunity to intercept and say, I disagree with that part. The nice thing about reasoning through things and letting people interact with it is that they don't have to disagree with your outcome.

[01:53:13] Jensen Huang: They can disagree with your reasoning steps and they could pull me in different directions and then we can reason forward. And so, we're kind of, you know, collective path searching method and it's really fantastic.

[01:53:30] Lex Fridman: Yeah, you have this way about you of when you're explaining stuff, I can feel you actually reasoning on the spot about it with a constant open mindedness where you could, I could feel like I could steer your thinking. And that's really beautiful that you've been able to maintain that after so many years of success and pain. I think sometimes pain makes you close you down a bit. Yeah. And I think to maintain

[01:53:58] Jensen Huang: tolerance for embarrassment.

[01:54:01] Lex Fridman: That's the tolerance, I mean, that's a real thing.

[01:54:04] Jensen Huang: Yeah.

[01:54:05] Lex Fridman: As many years of embarrassing yourself, even those meetings, knowing that there's people around you where you declared one idea and it was shown that that idea was wrong and be able to admit that and to grow from that. That's not, that's very difficult on a human level.

[01:54:19] Jensen Huang: Yeah. Well, you know, they knew that recently my first job was, you know, cleaning toilets. So I'm

[01:54:27] Lex Fridman: glad you maintained that same spirit of Denny's, the work. I mean, that was beautiful. Your whole journey from starting from Denny's is a beautiful one. Let me ask you about video games. So I'm a big gaming fan. Yeah. So I have to say thank you to NVIDIA for many years of incredible graphics.

[01:54:48] Jensen Huang: By the way, it is, GeForce is our still, to this day, our number one marketing strategy. Right? People learn about NVIDIA while they're in their teenage years. And then they go to college and they know who NVIDIA is and then in the beginning it's just, you know, playing Call of Duty, you know, Fortnite, and then later they're using CUDA, and then later they're using NVIDIA and, you know, Blender and Dessau and Autodesk.

[01:55:18] Lex Fridman: I mean, I should say, I mentioned to a friend that I'm talking with you, he said, oh, they make great gaming GPUs. Yeah, exactly. You know, there's more to it. But yeah, people really love the, it really brought a lot of joy to a lot of people. The hardware really brings these worlds to life. There was some controversy, around this with DLSS 5. Yeah. Can you explain to me the drama around this?

[01:55:48] Lex Fridman: I guess people, gamers online are concerned that it makes games look like AI slop. Yeah. What do you think of this drama?

[01:55:57] Jensen Huang: Yeah. I think their perspective makes sense, and I can see where they're coming from, because I don't love AI slop myself. You know, all of the AI-generated content increasingly looks similar, and they're all beautiful, and I can, so I can, I'm empathetic towards what they're thinking. That's just not what DLSS 5 is trying to do. I showed several examples of it, but DLSS 5

[01:56:26] Jensen Huang: is 3D conditioned, 3D guided. it's ground truth, structured data guided, and so, so the artist determined the geometry. We are completely truthful to the geometry maintained so in every single frame. It's conditioned by the textures, the artistry of the artist, and so every single frame, it enhances, but it doesn't change anything. Now,

[01:56:56] Jensen Huang: the question is, the question about enhancing, DLSS 5 also lets, because it's, the system is open, you could train your own models to determine, and you could even, in the future, prompt it, you know, I want it to be a tune shader, I want it to look like this kind of, you know, so you can give it even an example, and it would generate in the style of that, all consistent with the artistry, you know, the style, the intent of the artist.

[01:57:27] Jensen Huang: And so, all of that is done for the artist, so that they can create something that is more beautiful, but still in the style that they want. I think that they got the impression that the games are going to come out the way the games are, ship the way they do, and then we're going to post-process it. That's not what DLSS is intended to do. DLSS is integrated with the artist, and so it's about

[01:57:56] Jensen Huang: giving the artist the tool of AI, the tool of generative AI. They could decide not to use it.

[01:58:02] Lex Fridman: I think people are very sensitive to human faces, and we're now living in this moment, which I think is a beautiful one, which is people are sensitive to AI slop. It puts a mirror to ourselves to help us realize that what we seek is imperfections, what we seek is sometimes not perfect graphics. It helps us understand what we find compelling in the worlds we create, that's beautiful, and as long as it's tools that help us create those worlds, it's wonderful.

[01:58:31] Jensen Huang: It's yet another tool, and they want the generative models to generate the opposite of photoreal.

[01:58:40] Unidentified: Yeah,

[01:58:40] Jensen Huang: they'll do that too, and so it's just yet another tool. I think the gamers might also appreciate that in the last couple years, we introduced skin shaders to the game developers, and many of those games have skin shaders that include subsurface scattering that make skin look more skin-like, and so the industries, game developers are looking for

[01:59:10] Jensen Huang: more and more and more tools to express their art, and so this is just yet one more tool. They get to decide what to use.

[01:59:18] Lex Fridman: Ridiculous question. What do you think is the greatest or most influential game ever made, maybe from NVIDIA's perspective?

[01:59:26] Jensen Huang: Doom.

[01:59:26] Lex Fridman: Doom, unquestionably, that was the start of the 3D.

[01:59:30] Jensen Huang: I would say Doom, from the intersection of the cultural implication, as well as the industry, turning a PC into a gaming device. That was a very important moment. Now, of course, flight simulation companies were before it, but they just didn't have the popularity that Doom did to have made the industry turn the PC from an office automation tool into a personal computer for families and gamers and things like that. And so, Doom was really

[01:59:59] Jensen Huang: impactful there. From an actual game technology perspective, I would say Virtual Fighter. And so, we're great friends with both of them.

[02:00:08] Lex Fridman: And then there's games more recently, I mean, Cyberpunk 2077, really nice GPU, accelerated graphics. Fully ray-traced. Fully ray-traced. Also, I like, personally, I'm a huge fan of Skyrim, Elder Scrolls, and it's been released a long, long time ago, but people have released mods. We love mods. It's like a different game, and it just allows me to replay the game over and over,

[02:00:38] Lex Fridman: and it makes you realize that you can re-experience in a totally new way the world you already love. So, I do that all the time. One of my

[02:00:48] Jensen Huang: favorite things

[02:00:48] Lex Fridman: is just walk around Skyrim.

[02:00:50] Jensen Huang: We created this thing called RTX Mod. It's a modding tool. Awesome. It allows the community to inject the latest technology into an old game.

[02:01:01] Lex Fridman: Of course, what makes a great video game is not just graphics, it's also story and character development, but beautiful graphics can add to the immersion, the feeling like it's another place you're transported to. You said, I think accurately, that the AGI timeline question rests on your definition of AGI. So, let me ask you about possible

[02:01:31] Lex Fridman: timelines here. This ridiculous definition, perhaps, of what AGI is, but an AI system that's able to essentially do your job. start, grow, and run a successful technology company. That's worth a good one or a one? No, it has to be worth more than a billion

[02:02:00] Lex Fridman: dollars. So, you know how hard it is to do all those components. So, how far are we away from that? So, we're talking about OpenClaw that does all the incredibly complex stuff that are required to, first of all, innovate, to find customers, to sell to them, to manage, to build a team of some agents, some humans, all that kind of stuff. Is this

[02:02:30] Lex Fridman: 5, 10, 15, 20, years away? I think it's now. I think we've achieved AGI.

[02:02:36] Jensen Huang: You think you can have a company run by an AI system like this? Possible. And the reason for that is this, you said a billion and you didn't say forever. And so, for example, it is not out of the question that Acclaw was able to create a web service, some interesting little app that all of a sudden a few billion people used for

[02:03:06] Jensen Huang: 50 cents and then it went out of business again shortly after. Now, we saw a whole bunch of those type of companies during the internet era and most of those websites were not anything more sophisticated than what OpenClaw could generate today.

[02:03:23] Lex Fridman: Achieve virality and monetize that virality.

[02:03:25] Jensen Huang: It's just that I don't know what it is, but I couldn't have predicted any of those companies at the time either. You're

[02:03:31] Lex Fridman: going to get a lot of people excited with that statement. They're like,

[02:03:49] Jensen Huang: what do work make money. I wouldn't be surprised if some social thing happened or somebody created a digital influencer super cute or some social application that feeds your little tomogotchi or something like that and it becomes out of the blue an instant success. A lot of people use it for a couple of months and

[02:04:19] Jensen Huang: it dies away. The odds of 100,000 of those agents building NVIDIA is 0%. The one part that I want to make sure we all do is to recognize that people are really worried about their jobs. I just want to remind them that the purpose of your job and

[02:04:48] Jensen Huang: the tasks and tools that you use to do your job are related not the same. I've been doing my job for 33 years. I'm the longest running tech CEO in the world 34 years. And the tools that I've used to do my job has changed continuously in the last 34 years and sometimes quite dramatically over the course of a couple to three years. And the one story that I really want to make sure that everybody hears is the story

[02:05:18] Jensen Huang: that the first job that computer scientists said AI researchers said was going to go away was radiology because computer vision was going to achieve superhuman levels and it did computer vision was superhuman in 2019 maybe a little bit later 2020 okay and so it's been a long time since computer vision has been superhuman and so the prediction was radiologists would go away because

[02:05:48] Jensen Huang: studying radiology scans was thing of the past AI will do that well they were absolutely right computer vision is completely superhuman every radiology platform and package today is driven by AI and yet the number of radiologists grew and so the question is why and we now have a shortage of radiologists in the world and so one the alarmist warning

[02:06:17] Jensen Huang: went too far and it scared people from doing this profession that is so important to society and so it did harm now why was it wrong the reason why is because the purpose of a radiologist the purpose is to diagnose disease and help patients and doctors diagnose disease and because we're able to study scans so much faster now you could study more scans you could diagnose better

[02:06:46] Jensen Huang: you could you could inpatient faster we can see people more the hospitals are making more money you have more patients in the hospital you need more radiologists I mean the amazing thing is it's so obvious this was going to happen the number of software engineers at nvidia is going to grow not decline and the reason for that is because the purpose of a software engineer and the task of a software engineer coding are related

[02:07:16] Jensen Huang: not the same I wanted my software engineers to solve problems I didn't care how many lines of code they wrote you know but their job their purpose of their job didn't change solving problems working as a team diagnosing problems evaluating the result looking for new problems to solve innovation connecting dots you know none of that stuff is going to go away

[02:07:40] Lex Fridman: so you think it's possible that let's even take coding you think the number of programmers in the world might increase yes

[02:07:48] Jensen Huang: and the reason for that is this what is the definition of coding I believe the definition of coding as of today is simply specifying specification and maybe if you want to be rather directive you could even give it an architecture of the software the year you wanted to write so the question is how many people could do that describe a specification for a computer to go telling the computer what to go build how many

[02:08:18] Jensen Huang: people I think we just went from 30 million to probably 1 billion and so every carpenter in the future will be a coder except a carpenter with AI is also an architect they just increased the value that they could deliver to the customer their artistry just elevated tremendously I believe that every accountant is also your financial

[02:08:48] Jensen Huang: analyst also your financial advisor so all of these professions have just been elevated and if I were a carpenter I see AI I would just completely go berserk you know the services I can bring to my clients if I were a plumber completely go berserk

[02:09:05] Lex Fridman: and the people that are currently programmers and software engineers I think they're at the cutting edge of understanding intuitively how to communicate with agents using natural language in order to design the best kind of software that's

[02:09:21] Jensen Huang: right

[02:09:22] Lex Fridman: over time they'll converge but I think there's still value in getting learning how to program learning what programming languages are the old kind of programming what are good practices for programming languages what are design principles for programming languages for large software systems

[02:09:44] Jensen Huang: and the reason for that Lex you know that I was just saying for the audience I think the goal of the goal of specification the artistry of specification the goal and the artistry of it is going to depend on what problem you're trying to solve when I'm thinking when I'm thinking about giving the company strategies and formulating corporate directions and things that we should do I describe it at a level

[02:10:13] Jensen Huang: that is sufficiently specific that people generally understand the direction and it's actionable they it's so specific enough that they can take action on it but I underspecify it on purpose so that enable 43,000 amazing people to make it even better than I imagined and so when I'm working with engineers when I'm working with people I think

[02:10:43] Jensen Huang: about who what problem am I trying to solve who am I working with and the level of specification the level of architecture definition relates to that and so everybody's going to have to learn where in the spectrum of coding they want to be writing a specification is coding and so you might decide to be quite prescriptive because there's a very specific outcome you're looking for

[02:11:13] Jensen Huang: you might decide that this is an area you want to be much more exploratory and so you might underspecify and enable you to go

[02:11:51] Lex Fridman: back and choose times that always come when automations and new technology arrives and I just first of all I think we all need to have compassion and the responsibility to feel sort of the burden of what the actual suffering feels like for individual people and families that lose their job I think whenever you have transformative technology like that's coming with artificial intelligence there's going to be a lot of pain and I don't know

[02:12:20] Lex Fridman: what to do about that pain hopefully it creates much more opportunities for those same people for the same kind of job as the tooling evolves and makes them more productive and makes them more fun hopefully as it does in the programming I've been having so much fun programming I have to say I've never had this much fun so hopefully it automates the boring parts and makes the creative parts the ones that the human beings are responsible for

[02:12:50] Lex Fridman: but still there's going to be a lot of pain and suffering

[02:12:52] Jensen Huang: so my first recommendation before and this is now how I deal with anxiety in fact we just talked about it earlier enormous anxiety about the future enormous anxiety about the pressure enormous anxiety about uncertainty I first break it down and then I'm going to tell myself okay there are some things you can do something about there's some things you can't do anything about but for the stuff that you can do something about let's reason about it and let's go do it if we were to hire a

[02:13:22] Jensen Huang: new college graduate today and I have a choice between two one that has no clue what AI is and one that is expert in using AI business business development a lawyer

[02:13:53] Jensen Huang: I would hire the one who is expert in using AI and so I would advise that every college student every teacher should encourage their student to go use AI every college student should graduate and be an expert in AI and everybody if you're a carpenter if you're an electrician go use AI go see what it can do to transform your current job elevate yourself if I

[02:14:22] Jensen Huang: were a farmer I would absolutely use AI if I were a pharmacist I would use AI I want to see what it could do to elevate my job so that I could be the innovator to revolutionize this industry myself and so that would be the first thing that I would do and then I would also help them it is the case that the technology will dislocate and will eliminate many tasks

[02:14:53] Jensen Huang: and because it will automate it if your job is the task if your job is the task then you're very highly going to be disrupted if your jobs purpose includes certain tasks then it is vital that you go learn how to use AI to automate those tasks and then there's the world of spectrum in between and by

[02:15:16] Lex Fridman: the way the beautiful thing about AI so the chatbot versions is you can break down you have anxiety and you can break down the problem by talking to it like I've recently it's really just incredible how much you can think through your life's problems and through and I don't mean like therapy problems I mean like very practically okay I'm worried about my literally I'm worried about my job what are the skills what are the steps I need to take how do I get better at AI everything you just said

[02:15:46] Lex Fridman: you can literally ask and it's going to give you a point by point plan I mean it's just a great life coach period this

[02:15:53] Jensen Huang: I don't know how to use AI and the AI goes well let me show you

[02:15:56] Lex Fridman: exactly it's very meta but it's kind of incredible so people definitely should you can't walk up to Excel offers it's

[02:16:26] Lex Fridman: you know like I mentioned to you offline you mentioned I'm going to China and Taiwan so awesome where do I what do I how do I all of those questions immediately answered it's beautiful

[02:16:38] Jensen Huang: well when you when you go to Taiwan just ask AI what are Jensen's favorite restaurants in Taiwan yeah and it will actually tell you oh yeah is it accurate yeah yeah all right it's all over all over Taiwan

[02:16:51] Lex Fridman: well you're you're a rock star over there and um and like we also mentioned offline maybe our paths will cross which would be really wonderful in Computex NVIDIA GTC Taiwan uh do you think there are some things about human nature about human consciousness that is fundamentally non-computational maybe something a chip no matter how powerful uh can never replicate

[02:17:18] Jensen Huang: I don't know if the chip will ever get nervous and that's the you know of course the conditions by which uh that causes anxiety or nervousness or whatever emotion um I believe that AI will be able to recognize those and understand those I don't think my chips will feel those and therefore the how how that anxiety how that feeling how that excitement

[02:17:48] Jensen Huang: how that how that you know all of those feelings manifest in human performance for example extremely amazing human performance athletic performance you know average or lesser than average that that entire spectrum of human performance that comes out of exactly the same circumstances for different people manifesting in different outcome manifesting in different performance I I don't

[02:18:18] Jensen Huang: think there's anything about anything that we're building that would suggest that two different computers being presented with all of exactly the same context would of course it would produce statistically different outcomes but it's not because it felt different

[02:18:35] Lex Fridman: yeah the subjective boy there's something truly special about the subjective experience that we humans feel like I mentioned to you I was I was pretty nervous talking to you like I mentioned to you that the hope the fear the anxiety and just life itself the richness of life how amazing everything is how deeply we fall in love how deeply our hearts get broken how afraid we are of death and how much pain we feel when our

[02:19:04] Lex Fridman: loved ones pass away all of that the whole thing I know it's very hard to think AI being able to a computational device being able to do that but there's so many mysteries about this whole thing that we're yet to uncover that I am open to be surprised I've been surprised a lot over the past few months and few years scaling can create some incredible miracles in the space of intelligence has been truly marvelous to watch so I'm

[02:19:34] Lex Fridman: open to surprise

[02:19:35] Jensen Huang: and it's just really important to break down what is intelligence that word we use all the time it's not a mysterious word intelligence has a meaning you know and it's a system that you know it's something that we do that includes perception and understanding and reasoning and the ability to do plan and you know that loop that loop is fundamentally what intelligence is

[02:20:05] Jensen Huang: intelligence is not one word that is exactly equal to humanity and that's I think it's really important to separate the two we have two words for that I'm not I don't over fantasize about and I don't over romanticize intelligence intelligence is and people have heard me say it before I actually think intelligence is a commodity I'm surrounded by intelligent people

[02:20:34] Jensen Huang: and I'm surrounded by intelligent people more intelligent than I am in each one of the spaces that they're in and yet I have a role in that circle it's actually kind of interesting they're more educated than I am they went to better schools than I did they're deeper than in the fields that they're in all of them I have 60 of them they're all super human to me and somehow I'm sitting in the middle orchestrating all 60 of them

[02:21:16] Jensen Huang: and so you thing humanity is not specified functionally it's a much bigger word and our life experience our tolerance for pain our determination those are different words in intelligence and so the thing that I want to help the audience understand if

[02:21:51] Jensen Huang: I the word we should really elevate is humanity character humanity all of those things compassion generosity all of the things that you say just now I believe those are super human powers and that now intelligence is going to be commoditized because we've spoken about it the most important thing is your education the most now even when they said the most important thing is your education when you went to school there's more than just

[02:22:21] Jensen Huang: knowledge that you gained and so but unfortunately our society had put everything into one single word and life is more than one word and I'm just telling you my life would suggest that being lower on the intelligence curve than and I think that that kind of is I'm trying to inspire everybody else that

[02:22:51] Jensen Huang: don't let this democratization of intelligence this commoditization of intelligence you know cause you anxiety you should be inspired by that

[02:23:01] Lex Fridman: yeah I think AI will help us celebrate humans more and I'm certainly humanity and human first and I think what makes this world forever will be so and just AI is this incredible tool that makes us

[02:23:19] Jensen Huang: humans

[02:23:20] Lex Fridman: more powerful

[02:23:21] Jensen Huang: that's exactly right

[02:23:23] Lex Fridman: so much of the success of Nvidia and the lives of millions of people that I mentioned depend on you but you're just one human like we mentioned mortal like all of us do you think about your mortality are you afraid of death

[02:23:43] Jensen Huang: I really don't want to die I have a great life I have a great family I have really important work this is this is not a once in a lifetime experience suggests that it has been experienced by many people just not one person this is a once in what I'm going through

[02:24:13] Jensen Huang: Nvidia is one of the most consequential technology companies in history we're doing very important work I take it very seriously and so some of the things that of course are practical things like how do we think about succession planning and I'm famous in saying that I isn't because I'm immortal

[02:24:43] Jensen Huang: the reason for that is because if you're worried about succession planning if you're worried all that anxiety of succession planning then what should you do about it then you break it all the way back down continuously reason about everything

[02:25:13] Jensen Huang: in front of my team every single meeting is about a reasoning meeting every moment I spend inside a company outside the company is about passing on knowledge to people as fast as I can nothing I learn ever sits on my desk longer than you know a fraction of a second I'm passing that information that oh my gosh this is cool before I even finish learning all of it myself I'm already pointing it to somebody else get on this this is so cool you're going to learn this

[02:25:42] Jensen Huang: and so I'm constantly passing knowledge empowering people elevating the capability everybody around me so that the outcome that I that I seek that I hope for is that I die on the job you know and and hopefully I die on the job instantaneously yeah and there's no long periods of suffering you know well from a fan

[02:26:08] Lex Fridman: perspective given your extremely your enormous positive impact on civilization of course I hope you keep going but also it's just fun to watch what you know it's just the rate of innovation and I'm a huge fan of engineering it's so much incredible engineering is continuously being done by NVIDIA it's just fun to watch it's a celebration of humanity celebration of great builders the celebration of great engineering so

[02:26:38] Lex Fridman: it represents something special so I hope you and NVIDIA keep going what gives you hope about this whole thing we've got going on about humanity about the future of humanity when you look out and you think about the future quite a bit when you look out 10 20 50 100 years from now what gives you hope

[02:26:57] Jensen Huang: I've always had great confidence in the kindness the generosity the compassion the love love I'm and and

[02:27:27] Jensen Huang: and I get taken advantage of but it doesn't it doesn't ever cause me not to I start with always that that people want to do good people want to help others and vastly I am proven right constantly proven right and and often exceeds my expectations

[02:27:57] Jensen Huang: and and so I have complete confidence in the human capacity I think the the thing that the things that give me incredible hope is what I see as I extrapolate as I what I see now is possible and as I extrapolate based on the things that we're doing what will very likely happen and and and that there's so many things

[02:28:27] Jensen Huang: that we want to solve there's so many problems we want to solve there's so many things that we want to build there's so many good things that we want to do that are now within our reach and within the reach of my lifetime you just can't possibly not be romantic about that you know what I'm saying

[02:28:47] Lex Fridman: yeah what an exciting time to be alive

[02:28:49] Jensen Huang: yeah like truly truly so how can you not be romantic about that the fact that there is a reasonable thing to expect the end of disease it's a reasonable thing to expect it's a reasonable thing to expect that pollution will be drastically reduced it's a reasonable thing to expect that traveling at the speed of light is actually in our future and not

[02:29:20] Jensen Huang: for long distances but short distances people ask me how first of all very soon I'm going to put a humanoid on a spaceship and it's going to be my humanoid and we're going to send it out as soon as possible and it's going to keep improving and enhancing along the flight

[02:29:37] Unidentified: and then

[02:29:38] Jensen Huang: when it's time all of my consciousness has already been so much of my life has been uploaded in the internet take all my inbox take everything I've done everything I've said it's been becoming my AI and when the time comes send that at the

[02:30:09] Lex Fridman: maxing perspective I just all of those mysteries so much fascinating scientific questions

[02:30:16] Jensen Huang: there understanding the biological machine is right around the corner it's not 10 years it's five years probably and your biological

[02:30:23] Lex Fridman: machine the human mind and cracking physics theoretical physics open it's so exciting explaining consciousness that one would be awesome and it's all within our reach yeah Jensen thank you so much for everything you've done over the years thank you for everything you're doing for the world thank you for being who you are I can tell you're a great human being and I wish you incredible success this year I can't wait as a fan I can't wait to see what

[02:31:00] Jensen Huang: you and the research that you do to reveal for all of us the amazing people that you've interviewed over the years I've enjoyed them immensely and as an innovator to have created this long form unbelievable and yet it's just captivating so anyways thank you for everything you do means the world thank

[02:31:28] Lex Fridman: you

[02:31:28] Unidentified: Jensen

[02:31:28] Lex Fridman: thank you for listening to this conversation with Jensen Huang to support this podcast please check out our sponsors in the description where you can also find links to contact me ask questions give feedback and so on and now let me leave you with some words from Alan Kay the best way to predict the future is

[02:31:50] Unidentified: to invent it thank you for listening and hope to