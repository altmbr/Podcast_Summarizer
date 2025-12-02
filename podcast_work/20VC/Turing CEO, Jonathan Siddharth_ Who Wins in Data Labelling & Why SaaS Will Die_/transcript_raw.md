# Turing CEO, Jonathan Siddharth: Who Wins in Data Labelling & Why SaaS Will Die?

**Podcast:** 20VC
**Date:** 2025-12-01
**Video ID:** yQLOicn2vPU
**Video URL:** https://www.youtube.com/watch?v=yQLOicn2vPU

---

[00:00:00] I think the era of data labeling companies is over and it's now the era of research accelerators.
[00:00:05] SPEAKER_00: Today I do not pull any punches with Jonathan Sedard, found and see of Churren,
[00:00:10] SPEAKER_01: a company that he has scaled over 350 million in annual current revenue.
[00:00:15] SPEAKER_01: All knowledge work is going to be automated. It's only a matter of time. I don't see an AI bubble.
[00:00:21] SPEAKER_00: These models are incredibly powerful today. Sass as we know it, I think it's over. I think it's
[00:00:27] SPEAKER_00: completely over. Ready to go.
[00:00:40] Jonathan, I've been so looking forward to this. Thank you so much for joining me in person.
[00:00:44] SPEAKER_01: It's such a treat to it in person while you're in London. Thank you for having me, Harry.
[00:00:48] SPEAKER_00: Now, I want to start with a little bit of definitions because everyone thinks that talent market
[00:00:54] SPEAKER_01: places and then everyone pushes back on talent market places. How do you describe it?
[00:00:59] SPEAKER_01: And why are we not dealing with talent marketplaces anymore?
[00:01:02] SPEAKER_01: So I think of a talent marketplace as something that's basically matching talent to something.
[00:01:09] SPEAKER_00: Maybe it's an opportunity. So, so Turing is not a talent marketplace.
[00:01:17] What we do at Turing is we're training superintelligence. We work with seven out of the eight
[00:01:22] SPEAKER_00: frontier labs. To get to superintelligence, you need research, compute, and data.
[00:01:29] SPEAKER_00: Research the labs do in-house with OpenAI, Anthropic, DeepMind, etc. For compute, we have
[00:01:34] SPEAKER_00: Jensen to thank and maybe Nvidia as well. But on the data side, Turing powers the data pillar.
[00:01:41] SPEAKER_00: On the data side, there's been a significant shift in the last couple of years.
[00:01:46] So a few years back, the models weren't quite smart enough. And as the models have gotten
[00:01:53] SPEAKER_00: increasingly smarter, the data needed to improve them has become harder to generate.
[00:01:58] SPEAKER_00: And this is because it's more sophisticated data that's required to improve the models.
[00:02:02] SPEAKER_01: It's like vertically specific people in task and workflows that isn't so obvious like cap pictures.
[00:02:09] That's correct. That's correct. And it's there's a shift in the data going from simple to complex.
[00:02:14] SPEAKER_00: Let's take coding, for example. A few years ago, the kind of dataset, a contractor who
[00:02:20] SPEAKER_00: could generate might look like, hey, write a Python program to sort some numbers. Today,
[00:02:26] SPEAKER_00: the data that's generated might be write a B2B marketplace app that connects doctors with patients.
[00:02:34] SPEAKER_00: And write it on for Android, with Kotlin Java, write it for iOS with Swift, and write it on the web,
[00:02:42] SPEAKER_00: like with NextJS or something. That's the complexity. So there's a shift in going from simple to
[00:02:47] SPEAKER_00: complex. So it's no longer the kind of data that low skilled medium skilled contractors can generate.
[00:02:54] SPEAKER_00: You need export humans in every domain. The second shift is we've gone from teaching AI to take tests
[00:03:02] SPEAKER_00: and pass tests to teaching AI to do real work. It's less about having AI pass the bar.
[00:03:10] SPEAKER_00: It's more about can AI do the job of a lawyer? Can it do the job of a privacy lawyer, a compliance
[00:03:15] SPEAKER_00: lawyer, a paralegal? So having AI be good at doing economically valuable work. So that's a shift.
[00:03:24] SPEAKER_00: The third shift is we've gone from chatbots to agents, right? Like we started off with
[00:03:31] SPEAKER_00: chat GPT where you're asking questions, getting answers, which is great. But now it's about
[00:03:36] SPEAKER_00: the model's becoming agentic where they can execute complex multi-step workflows in a real-world
[00:03:42] SPEAKER_00: business setting. And the type of data you need for that is totally different. How is that
[00:03:47] SPEAKER_00: different? That's interesting. So in the transition from chatbots to agents, how does the data
[00:03:50] SPEAKER_01: require change with that transition? When you are training a chatbot, you'd usually do a lot of
[00:03:59] SPEAKER_00: SFT and RLHF. SFT where you're giving the model input prompts and output completions,
[00:04:06] SPEAKER_00: you kind of teach the model to imitate experts. With RLHF, like you're basically
[00:04:14] SPEAKER_00: teaching the model to produce responses that a human would tend to prefer, RLHF is used to train
[00:04:19] SPEAKER_00: what's called a reward model. And then the model is trying to produce completions that give it
[00:04:25] SPEAKER_00: a high reward, right? With agents, and let's define an agent, I mean different people define agents
[00:04:30] SPEAKER_00: in the field. I would define an agent as something that's capable of taking action in the real world,
[00:04:40] SPEAKER_00: or in the physical world, something that's executing a multi-step workflow, calling different functions,
[00:04:47] SPEAKER_00: the agent could be operating a computer or making back-end API calls to actually do stuff,
[00:04:57] SPEAKER_00: right? You might have an agent to file your taxes, you might have an agent to prepare your monthly
[00:05:03] SPEAKER_00: financials. So to train an agent, you would also want to teach the model how to do tool use. So you
[00:05:13] SPEAKER_00: teach the model how to call other functions, how to use other applications to be more leveraged.
[00:05:19] SPEAKER_00: Today, the dominant paradigm is reinforcement learning. And oftentimes, these agents are trained
[00:05:27] SPEAKER_00: through reinforcement learning, where you'd build what's called an RL environment, which is like a
[00:05:32] SPEAKER_00: mini-world model for business. And in that RL environment, you have input prompts, output
[00:05:38] SPEAKER_00: verifiers, and you'd have the full system state tracked along with the data model. Let me give you
[00:05:44] SPEAKER_00: an example. Imagine a workflow for a salesperson that an SDR would go through, where before a sales call,
[00:05:54] SPEAKER_00: let's say the salesperson has to research the prospect, look up salesforce to see whether
[00:05:59] SPEAKER_00: somebody from the team has already spoken with this human, and maybe if needed, looking up this
[00:06:06] SPEAKER_00: person's contact information, maybe using zoom in for something like that to reach out to them.
[00:06:10] SPEAKER_00: Right. This required this human to use three different tools, LinkedIn, salesforce, and zoom in for.
[00:06:16] SPEAKER_00: Right. In an RL environment setup, you'd create a mini-world model with clones of these applications
[00:06:24] SPEAKER_00: that are created with a fake database with like synthetic data. And the prompt might be, hey,
[00:06:32] SPEAKER_00: prepare for a call with this person, and then after the call is done, update salesforce. Right,
[00:06:39] SPEAKER_00: like let's say that's the prompt. And you have what's called a verifier to check whether the agent
[00:06:45] SPEAKER_00: completed the task. Right. And in this case, and this is where I think it's AI is kind of beautiful
[00:06:50] SPEAKER_00: and somewhat magical, you set up the agents in this environment, and the agent is going to try
[00:06:55] SPEAKER_00: different trajectories, try different tool calls to try to complete the task. And you would set this up
[00:07:02] SPEAKER_00: so that the curriculum is optimally defined. If you create the curriculum is the set of tasks that
[00:07:09] SPEAKER_00: you have this agent do. If it's too easy and the agent completes everything, the model doesn't
[00:07:14] SPEAKER_00: learn much. If it's too difficult, the model doesn't learn much. You'd ideally want like the right
[00:07:20] SPEAKER_00: mix where the model is kind of getting positive and negative feedback. It's very similar to
[00:07:27] SPEAKER_00: the technique that alpha zero used in mastering go with the model played against itself.
[00:07:33] SPEAKER_00: So this is like another, it's kind of like a form of synthetic data because the agent is trying
[00:07:38] SPEAKER_00: different approaches by itself. But it's humans. I mean, in this case, at Turing, we create these
[00:07:43] SPEAKER_00: oral environments at massive scale for every workflow you can think of across every function,
[00:07:48] SPEAKER_00: across every industry. And so you create the oral environments to create the data that then allow
[00:07:53] SPEAKER_01: the models to train to have further use cases like that. Correct. And we create oral environments for
[00:08:01] SPEAKER_00: every industry you can think of. Retail healthcare life sciences. Imagine like this four
[00:08:05] SPEAKER_00: dimensional matrix where the first dimension is every industry like financial services retail,
[00:08:09] SPEAKER_00: healthcare, podcasting. Maybe it's one of the dimensions. Please. The second dimension could be
[00:08:15] SPEAKER_00: every function software engineering, marketing sales, finance, etc. The third dimension could be
[00:08:20] SPEAKER_00: every role in that org chart. Let's say in sales, there was SDR as like a role. The fourth dimension
[00:08:25] SPEAKER_00: is a workflow that a human goes through in that role. You can think of every role a human has as
[00:08:30] SPEAKER_00: like a composite of workflows, right? And we are creating oral environments for every workflow,
[00:08:36] SPEAKER_00: for every role in every function in every industry. That's like $30 trillion of knowledge work.
[00:08:42] Is that possible to have that breadth and quality? Yes. How? Time and lots of money.
[00:08:51] Because I was speaking to candidly one of your competitors, board members, the other day in
[00:08:56] SPEAKER_01: prep for this. And he said the big thing that we all got wrong was we are sowing innings one of
[00:09:02] SPEAKER_01: the acquisition of verticalised data. Like there is so much room to run in the data acquisition for
[00:09:09] SPEAKER_01: dental for SDRs for product managers, you name whatever function you want. Do you see us very
[00:09:16] SPEAKER_01: much in innings one of the data acquisition for these very specific vertically focused workflows?
[00:09:22] Absolutely. It's innings one. And I believe in slow takeoff. I'm sorry to poor cold water on all the
[00:09:29] SPEAKER_00: AI rumors that might be listening to this. But we are not in a rapid takeoff scenario. I believe in
[00:09:36] SPEAKER_00: slow steady takeoff for a GI and eventually super intelligence. So we're still innings one.
[00:09:42] SPEAKER_00: It's going to take a while before we get all of this data into the models.
[00:09:48] SPEAKER_00: So when we think about then the breadth that we go after and us specializing in our
[00:09:55] SPEAKER_01: oral environments, just so I understand like the marketplace that we're sitting because there is
[00:09:58] SPEAKER_01: your macaws, there's your searches. How do you differ for those for people who are wondering,
[00:10:03] SPEAKER_01: how in a minute I thought they were one? So Turing is a fundamentally different animal. So what we do
[00:10:09] SPEAKER_00: is we're training super intelligence for all these frontier labs.
[00:10:14] SPEAKER_00: The to get to super intelligence requires research, compute and data. The data needs have
[00:10:20] SPEAKER_00: significantly changed. It's more complex data rather than simple data. It's more real world data.
[00:10:27] SPEAKER_00: Data that touches how real humans do knowledge work. And you need data to train these agentic
[00:10:35] SPEAKER_00: systems. So what the labs need in a partner in this new world is somebody that has research DNA
[00:10:45] SPEAKER_00: that could be a proactive research partner for them because these paradigm keep changing.
[00:10:52] SPEAKER_00: Last year at this time we were not talking about reinforcement learning at all, but then two
[00:10:56] SPEAKER_00: things happened. Owen dropped in December, DeepSeek launched in Jan and now it's all about
[00:11:02] SPEAKER_00: oral environments. It's not just imitation learning, it's also reinforcement learning. So the labs need
[00:11:08] SPEAKER_00: a data partner that's more research oriented. Second, the labs need a data partner that also
[00:11:15] SPEAKER_00: touches the real world. So at Turing, we don't just generate data to train the models for the
[00:11:22] SPEAKER_00: frontier labs. We also work with enterprises. We work with Disney, Pepsi, BlackRock, Pfizer,
[00:11:29] SPEAKER_00: Johnson and Johnson to build fine tuned custom models to solve real world
[00:11:35] SPEAKER_00: enterprise problems for those enterprises. So this is our FTEs that you send in to go and
[00:11:40] SPEAKER_01: go and post custom models. Correct. So we touch reality. We know where the models break in the real
[00:11:45] SPEAKER_00: world. How much of business is that? The FTE is deploying custom models versus more horizontal.
[00:11:51] SPEAKER_01: So the horizontal business is bigger, but this business is also fast growing.
[00:11:57] And third, you need a platform with the world's smartest humans on it, as well as experts in
[00:12:04] SPEAKER_00: different domains so that you can build these oral environments. And you need that platform to be
[00:12:09] SPEAKER_00: really good at sourcing talent, vetting talent, matching talent and generating data.
[00:12:14] SPEAKER_00: Right. So I think the era of data labeling companies is over. Turing is a research accelerator,
[00:12:22] SPEAKER_00: and it's now the era of research accelerators. The labs want to work with a proactive partner that
[00:12:28] SPEAKER_00: can think about what types of data are likely to be helpful for these models and can make recommendations
[00:12:34] SPEAKER_00: to them. Why would you need a custom model? When you look at a lot of the customers that you mentioned
[00:12:38] SPEAKER_01: there, for the ones where you have FTEs who go and build custom models, what is the reasoning
[00:12:43] SPEAKER_01: around that? And is that a temporary moment in time or is that a permanent requirement from them
[00:12:48] SPEAKER_01: for a certain reason? I think it's a permanent requirement. I'll give you an example.
[00:12:54] SPEAKER_00: Let's pick an insurance company. Right. And for insurance companies, two really important
[00:13:00] SPEAKER_00: problems they have to solve are underwriting and claims processing. Let's pick underwriting,
[00:13:04] SPEAKER_00: for example. So with underwriting, the problem statement is you might get multiple types of
[00:13:11] SPEAKER_00: unstructured medical data. It could be somebody taking a picture of their medical history on
[00:13:18] SPEAKER_00: a on their smartphone, or it could be some OCR data from somebody's medical history or data
[00:13:24] SPEAKER_00: and PDFs, etc. And a human has to look at that person's medical information and then decide,
[00:13:30] SPEAKER_00: is this person high risk medium risk or low risk? What medical conditions do they have? Do they have
[00:13:36] SPEAKER_00: cardiovascular? Do they have renal? And how do you price insurance for somebody like this? Do
[00:13:40] SPEAKER_00: you even take them on as a client if you're an insurance company? Right. Now this is a problem that
[00:13:48] SPEAKER_00: an LLM can solve really well with a human-in-the-loop system. Now you may not need a truly
[00:13:55] SPEAKER_00: in parameter world model to do a task like this. In fact, there's lots of research that shows a
[00:14:03] SPEAKER_00: smaller language model will actually be faster and more accurate at a task like this,
[00:14:09] SPEAKER_00: than a giant world model. And the insurance company also may not want their data to go back to
[00:14:17] SPEAKER_00: like a frontier model. So oftentimes in these cases, what we would do is we would work with
[00:14:25] SPEAKER_00: a frontier lab, take one of their smaller models, maybe something in the half a billion
[00:14:32] SPEAKER_00: parameters to 10 billion parameter regime. Have an AI system built that's on-prem with the customer
[00:14:43] SPEAKER_00: that's fine tuned on that enterprises proprietary data because this insurance company might have
[00:14:50] SPEAKER_00: data from like the last decade of humans making judgments, right? You want to make use of that data,
[00:14:55] SPEAKER_00: but you don't want to help other competing insurance companies with your own data. So
[00:15:01] SPEAKER_00: normally for these cases, you would have a smaller fine-tuned model that's fine-tuned on your
[00:15:08] SPEAKER_00: proprietary data distilling your proprietary human knowledge into the models. That human underwriter
[00:15:14] SPEAKER_00: that's been doing this job, like has a lot of institutional knowledge in their brains. So you'd
[00:15:18] SPEAKER_00: want to distill that into the LLMs. And this human that I mentioned who's doing this job
[00:15:24] SPEAKER_00: underwriting, they might be using other internal tools inside this insurance company. You might
[00:15:28] SPEAKER_00: want to automate those toolcalls in the agent. So you'd build basically a version of almost like
[00:15:35] SPEAKER_00: a chat GPT agent that's smaller and fine-tuned for that specific workflow and use case. I do think
[00:15:43] SPEAKER_00: this will become more popular across the board and it'll be a big market for the frontier labs.
[00:15:50] SPEAKER_00: If you want like a general-purpose assistant, I think you need a trillion parameter model,
[00:15:56] SPEAKER_00: right? Like that can answer anything to be a universal assistant.
[00:15:58] SPEAKER_00: Is that a good business fee? When you think about taking someone else's model
[00:16:02] SPEAKER_01: retrofitting it to a business, doing a lot of custom work with your own engineering teams in
[00:16:07] SPEAKER_01: those businesses? Is that a good business? I think it would be a good business. Like we're still
[00:16:12] SPEAKER_00: early, but it's growing pretty fast. I think like the, we have this unique vantage point where
[00:16:21] SPEAKER_00: because we are generating data for all the frontier labs, we get to see a glimpse of the future
[00:16:29] SPEAKER_00: before it arrives. And the glimpse of the future that I see is that all knowledge work is going to
[00:16:36] SPEAKER_00: be automated. If a human's job involves looking at a computer, analyzing what's on the screen,
[00:16:43] SPEAKER_00: using different tools, using a keyboard and a mouse, it's going to be automated. It's only a matter
[00:16:48] SPEAKER_00: of time. So I mean, these computer-use agents are going to keep improving over the next decade.
[00:16:55] SPEAKER_00: And that's $30 trillion of digital knowledge work. My question to you is I, I spend a lot of time
[00:17:01] SPEAKER_01: with very large companies, mostly where I speak to them. The thing that I'm astounded by is we
[00:17:06] SPEAKER_01: hugely underestimate the pace of AI progression in terms of technological capabilities. But consistently,
[00:17:13] SPEAKER_01: what I see is the laughable state of internal data, internal processes. I mean, Jonathan,
[00:17:20] SPEAKER_01: these guys are so far off adopting slack and notion, let alone building custom models and
[00:17:26] SPEAKER_01: embracing the latest AI tools. I respectfully push back on the all knowledge work automated,
[00:17:33] SPEAKER_01: maybe in 20 years, but not in a 10-year time frame. Am I wrong?
[00:17:39] What do you think is the biggest constraint or obstacle?
[00:17:43] The inability for them to try and implement new tooling.
[00:17:47] SPEAKER_01: But what if the cost is too high? If they didn't do that, if the hypothetical insurance company
[00:17:52] SPEAKER_00: that I told you about, if there was a competitor of theirs that could operate with 100th the headcount,
[00:18:00] SPEAKER_00: while delivering a better experience to their customers by pricing insurance deals better,
[00:18:06] SPEAKER_00: making more money from insurance premiums less claims payouts, they'll get their lunch, Eden.
[00:18:12] SPEAKER_00: I think they will. I think you'll see this transfer of value from old incumbent who can't adopt
[00:18:18] SPEAKER_01: new tools to start up company. Hence why we invest, who is eating their lunch absolutely.
[00:18:24] Ah, I see. So your theory is that the incumbents won't adapt and we'll just be of a farce fire and
[00:18:30] SPEAKER_00: you'll just 100%. We will be on a 10 to 20-year decline of incumbents who are unable and unwilling
[00:18:35] SPEAKER_01: to adopt new tools because of data, because of permissioning, because of internal buying processes.
[00:18:40] SPEAKER_01: I, that's an interesting point, Harry. I, I mean, I go to a European bank, you will be astounded
[00:18:47] SPEAKER_01: by how bad it is internally, respectfully, the poor quality of the processes of buying technology,
[00:18:55] SPEAKER_01: it's just, it's, it's a warrant. I have a hypothesis. My hypothesis is that
[00:19:01] SPEAKER_00: companies will be very slow with back office automation, but in the front office, for example,
[00:19:08] SPEAKER_00: I speak with financial services clients in New York, like some of the biggest, uh, biggest companies.
[00:19:15] SPEAKER_00: I speak with the C suite of these companies and they are extremely interested in applying AI
[00:19:22] SPEAKER_00: to help them make better investment decisions because it directly translates into helping them make
[00:19:28] SPEAKER_00: more money. And I've found it, it's a lot easier to like convince people to use
[00:19:34] SPEAKER_00: at piece of technology to make more money than to save money. And in financial services,
[00:19:39] SPEAKER_00: it's pretty brutal, right? Like it's kind of like an efficient market. If you don't,
[00:19:43] SPEAKER_00: if there is alpha to be found in like how you can allocate capital better, make investment
[00:19:49] SPEAKER_00: decisions better, figure out what opportunities to invest in, price deals better,
[00:19:53] SPEAKER_00: you'll get killed if you don't, if you're not at the bleeding edge. And I've heard, uh,
[00:19:58] SPEAKER_00: Mark Chend, the head of research at OpenAI say this about how financial services is usually
[00:20:06] SPEAKER_00: at the bleeding edge among all the other industries in the S&P 500. But even they are like about
[00:20:12] SPEAKER_00: two years behind usually, like relative to the state of the art. Um, so I agree with you that
[00:20:21] SPEAKER_00: in back office automation, it'll probably be very slow and it'll, it'll, it'll probably be
[00:20:26] SPEAKER_00: the upstarts that'll do things well. I think the change management will be too slow.
[00:20:33] SPEAKER_00: But I'm optimistic about front office, especially in financial services, life sciences,
[00:20:38] SPEAKER_00: pharma, where if you can like accelerate the time to discover a drug or to get to a molecule,
[00:20:45] SPEAKER_00: like there are like these, um, if you can help somebody win in like the main thing that they care
[00:20:52] SPEAKER_00: about in their, in their industry, uh, I think they'll adopt it faster. I'm always told by a
[00:20:59] SPEAKER_01: dear friend, Rory O'Triscoll at scale. I don't know if you know Rory, but fantastic investor.
[00:21:03] SPEAKER_01: He always says, listen, value generation from AI is fundamentally dependent on one simple question.
[00:21:10] SPEAKER_01: Will we see the transfer of budget from human labor to AI technology? And if we see that transfer
[00:21:17] SPEAKER_01: of budget, oh my god, the $30 trillion that you said it does. And if we don't, we operate in maybe
[00:21:25] SPEAKER_01: a slightly larger software technology budget world, but by no means a world that we can have the
[00:21:31] SPEAKER_01: valuations and the money that we have going in, when you look at that, are there any areas
[00:21:37] SPEAKER_01: truly stay where you're like, we have seen the full transition from human labor budgets to AI
[00:21:43] SPEAKER_01: technology budgets? I think the transfer is pretty high in areas like, uh, customer support,
[00:21:51] SPEAKER_00: um, copywriting, um, SEO, like some of these marketing related areas, as you would expect
[00:22:02] SPEAKER_00: the transfer is faster in these low risk to fail areas, like when it's, when it's relatively easy.
[00:22:10] SPEAKER_00: But I encourage your listeners to look up GDP value, which is this paper by OpenAI,
[00:22:17] SPEAKER_00: where they measured the impact of today's AI models in automating all types of economically
[00:22:26] SPEAKER_00: valuable work. It's a lovely piece of research and great everybody to read it, where they did the
[00:22:32] SPEAKER_00: study, where they looked at, I think like, 44 different, uh, nine verticals and 44 occupations,
[00:22:42] SPEAKER_00: they took like a very diverse sampling of different types of knowledge work, everything from
[00:22:46] SPEAKER_00: financial services to real estate, to, um, uh, healthcare, to, to law. And they took very specific
[00:22:53] SPEAKER_00: occupations and in those specific occupations, they took real tasks where like a real deliverable
[00:23:00] SPEAKER_00: has to be produced. Imagine an engineer, like a civil engineer creating a blueprint for a building
[00:23:05] SPEAKER_00: that are about to build or somebody who's at the set of a movie studio coming up with a schedule
[00:23:10] SPEAKER_00: for how you organize your cruise, like real work, right? And according, you can imagine like a real
[00:23:15] SPEAKER_00: world software engineering project. Um, and they saw that today's models were quite good at achieving
[00:23:25] SPEAKER_00: parity with, uh, the best human experts in that field. Uh, we were roughly at like, um, I say,
[00:23:34] SPEAKER_00: we, at which side am I on? I mean, the set of the, I, sorry, the, I mean, from that positioning,
[00:23:41] SPEAKER_01: that would be fast. Yes. Yes. But cheering is like a blurry line. Right? Like, maybe, maybe,
[00:23:45] SPEAKER_00: I mean, as the CEO of cheering, like passing the cheering test is about not being able to tell the
[00:23:50] SPEAKER_00: difference. So, um, so what I noticed was, um, about 50% of the time in, in GDP value, like the
[00:24:00] SPEAKER_00: best models were producing work, uh, that was indistinguishable from a human expert, which is
[00:24:06] SPEAKER_00: remarkable. And could use to open AI where they also flagged that the number one model was Claude
[00:24:12] SPEAKER_00: for Opus. Um, although GPT-5 was quite good also. Um, and, uh, and, and this was for relatively
[00:24:21] SPEAKER_00: simple tasks, like imagine just, uh, a task requiring one single step, whereas in the real world,
[00:24:27] SPEAKER_00: if I give you a task to do a certain project, you won't just go off and do it. You might ask for
[00:24:32] SPEAKER_00: clarifying information. You might do other things to acquire more context. You might go brainstorm
[00:24:37] SPEAKER_00: with other, other humans to do that task and you would do it in a sequence of steps. So there's more
[00:24:42] SPEAKER_00: room to go. Um, but I think we are well on our way to AI eventually automating all types of
[00:24:50] SPEAKER_00: knowledge work. What happens in that world? If AI automates all types of knowledge work,
[00:24:56] SPEAKER_01: what, what happens then? Three things that will happen. Uh, first, I think we are all going to be,
[00:25:06] we'll all have the potential to be a hundred X-mo productive. Today, I'm able to run one company.
[00:25:13] SPEAKER_00: Elon can run maybe like five companies, but in a world where I'm a hundred X-mo productive,
[00:25:18] SPEAKER_00: maybe I'm able to run a hundred companies. Elon maybe runs 600 companies. Um, I think every
[00:25:24] SPEAKER_00: human will just be so much more leveraged. Um, the nature of a job itself could change,
[00:25:32] SPEAKER_00: where there could be, today we are accustomed to the idea of like one person doing one job.
[00:25:37] SPEAKER_00: Um, but people could be doing multiple jobs at the same time. People could be running different
[00:25:44] SPEAKER_00: companies at the same time. The second implication, I think, is it's going to be wonderful for entrepreneurship.
[00:25:51] SPEAKER_00: So you, Harry, I think are going to be very happy because today, if I think of like for a lot of ideas,
[00:25:59] SPEAKER_00: founders are intelligence constrained. Um, I think of being capital constrained as a form of being
[00:26:05] SPEAKER_00: intelligence constrained. For example, if you pick a a therapist who wants to start a mental health
[00:26:13] SPEAKER_00: startup, today that founder would have to raise at least a few hundred K, if not a few million,
[00:26:19] SPEAKER_00: to recruit some software engineers, maybe as a marketing person or a growth person, maybe a
[00:26:25] SPEAKER_00: product manager. But in a future where AGI exists, this person will recruit a marketing GPT,
[00:26:32] SPEAKER_00: a software engineer GPT, a PM GPT, and get off the ground for a lot less capital. A million
[00:26:39] SPEAKER_00: flowers will bloom. Lots and lots of non technical founders will start companies. We'll see a broader
[00:26:44] SPEAKER_00: distribution of founders than just those who live in London or Palo Alto who are kind of connected
[00:26:50] SPEAKER_00: to these pools of capital who might start companies, which I think is wonderful for the world.
[00:26:54] SPEAKER_00: Do you think we will? What I mean by that is the six and a half million people today in the UK
[00:26:59] SPEAKER_01: have the working population who actively do not work because of an inability to work. I'm not
[00:27:06] SPEAKER_01: going to get into the analysis around that because I'll get in trouble for it. Um, I think we
[00:27:11] SPEAKER_01: grossly overestimate the intelligence of the general population. And I know that sounds incredibly
[00:27:16] SPEAKER_01: arrogant, but most people say actually a lot of people just don't want to work and are not at the
[00:27:22] SPEAKER_01: level of recruiting GPT's assistance. Do you not worry that it will widen the chasm between
[00:27:29] SPEAKER_01: those that have and those that haven't? I'm an optimist and I think the opposite will happen
[00:27:34] SPEAKER_00: because what we are really doing when we're training superintelligence is you'll be basically
[00:27:40] SPEAKER_00: training intelligence as an API. And what's the alternative to that? It's like hiring a human to
[00:27:45] SPEAKER_00: provide you with that intelligence that human is quite expensive, right? And if anything that creates
[00:27:51] SPEAKER_00: an even broader gap between the halves and the have-nots, whereas for $20 a month, if you had access
[00:27:58] SPEAKER_00: to the smartest experts in coding, in STEM, in sales, in marketing, I feel like more people will be
[00:28:06] SPEAKER_00: able to start companies and produce active, like valuable work. I also think I believe that when
[00:28:15] SPEAKER_00: we have access to superintelligence, I firmly believe this, we are not all going to chill out on a
[00:28:21] SPEAKER_00: beach somewhere and contemplate what do we do next. I think we're going to solve, we humans,
[00:28:26] SPEAKER_00: like we are tool builders, we are problem solvers, we'll solve problems at higher and higher levels
[00:28:31] SPEAKER_00: of instruction. And I feel like in a world where we have AGI, we'll just solve much more
[00:28:38] SPEAKER_00: exciting problems, maybe we'll cure diseases, reverse aging, maybe go to the stars. There's all
[00:28:43] SPEAKER_00: sorts of fun things we'll do. I don't think we'll be bored. I'm glad I often hear the UBI and we're
[00:28:49] SPEAKER_01: going to sit in the right part, and I think that might be a little bit challenging. When technology
[00:28:54] SPEAKER_01: is not the mode, what is the mode? I had the founder of base 44 on and he said 99% of the code in
[00:29:01] SPEAKER_01: that year will be written by AI. Technology is no longer the mode. What is the mode in that world?
[00:29:08] SPEAKER_01: I think one mode will be data-driven feedback loops. For example, one reason Google had
[00:29:18] SPEAKER_00: such a great lead in search for a while was these data-driven feedback loops that come from
[00:29:28] SPEAKER_00: people using your product and generating data that gives you the algorithm developer a high
[00:29:36] SPEAKER_00: quality gradient for which direction to step in. So the importance of PageRank was known.
[00:29:43] SPEAKER_00: The recipe for ranking search results was well known among Google, Yahoo, Microsoft, and a few others.
[00:29:49] SPEAKER_00: Obviously, people move around these companies all the time, but the advantage Google had was
[00:29:55] SPEAKER_00: because everybody preferred Google and liked working, liked that search engine,
[00:30:04] SPEAKER_00: you saw a much more representative set of queries. You had data from clickstream,
[00:30:12] SPEAKER_00: from the clickstream of what results people were clicking on. That helps your algorithms improve
[00:30:17] SPEAKER_00: at a much faster rate. I think data-driven feedback loops will be key for all types of
[00:30:23] SPEAKER_00: enterprise applications also. Today, OpenAI and ChagGPT has a good data-driven feedback loop.
[00:30:32] SPEAKER_00: In enterprises, again, I think it's wide open. Whoever is deploying the right custom fine-tuned
[00:30:40] SPEAKER_00: models and agents for specific workflows or roles or functions or companies,
[00:30:47] SPEAKER_00: if you get in first and solve a customer's problem really well, you start getting that flywheel going
[00:30:54] SPEAKER_00: where you will discover first where the models don't work well. You will use that data to work
[00:31:00] SPEAKER_00: with a company like Turing to generate additional data to plug that gap so you will improve.
[00:31:07] SPEAKER_00: And this is what I mean by it's important for the models to touch reality. I feel like the models
[00:31:12] SPEAKER_00: have touched reality in consumer. We haven't yet touched reality in enterprise and the only way we'll
[00:31:18] SPEAKER_00: improve is by deployment. And that deployment is fundamentally predicated on handholding?
[00:31:24] SPEAKER_01: Right. Yes, handholding. And I feel like there's still a lot of first-mile schlep and last-mile
[00:31:30] SPEAKER_00: schlep that needs to be handled. What does that mean? First-mile schlep and last-mile schlep?
[00:31:34] SPEAKER_00: When I say first-mile schlep, I mean for that underwriting co-pilot example that I gave you for
[00:31:40] SPEAKER_00: that insurance company, I painted a pretty rosy picture of how you take this model, you find
[00:31:45] SPEAKER_00: tune it on your proprietary underwriting data. In the real world, it doesn't work that way.
[00:31:51] SPEAKER_00: First-mile schlep is, let's say I'm talking to the CEO of this insurance company or the CTO
[00:31:55] SPEAKER_00: of this insurance company, they'll say, our data is a mess. It's in silos. It's super fragmented.
[00:32:01] SPEAKER_00: Some of the data is in spreadsheets. Some of the data is in a file that Bob has. And Bob
[00:32:06] SPEAKER_00: doesn't work here anymore. The data is all over the place. You first have to acquire the data,
[00:32:14] SPEAKER_00: convert the unstructured data into structured data into a format to find tune LLMs.
[00:32:20] SPEAKER_00: You might want to set up good infrastructure for e-vals. You'd want to create good e-vals for
[00:32:26] SPEAKER_00: models or agents. You might want to build a workflow designed for partial autonomy.
[00:32:33] SPEAKER_00: Human underwriter that's about to use this model to evaluate these medical histories. You might
[00:32:40] SPEAKER_00: want to build a cursor-like interface for them so that they can work alongside the AI to do their
[00:32:46] SPEAKER_00: job. Also, training the humans in these new workflows. You want to make sure you're collecting data
[00:32:53] SPEAKER_00: the right way. The way, for example, we do deployments is like a tandem system where you'd have a
[00:33:02] SPEAKER_00: human and an AI doing the same job for a period of time, where a manager can see the output of both.
[00:33:10] SPEAKER_00: If the agent is right and the human is wrong, you train the human. If the human is right and the
[00:33:15] SPEAKER_00: agent is wrong, you've created a data point to fine tune the next iteration of the agent. So the
[00:33:20] SPEAKER_00: agent is steadily improving over time. If the agent is right and the human is wrong, why didn't you
[00:33:24] SPEAKER_01: just fire the human? It depends on at what frequency. You track things like precision and recall.
[00:33:35] SPEAKER_00: You'd want to analyze this over a period of time. You wouldn't fire them over a single mistake.
[00:33:40] SPEAKER_00: Behrhash. What's the margin on that business? It varies. We're also in the early innings of figuring
[00:33:48] SPEAKER_00: out how to price that. Today, we do it in a relatively simple way, where we're just
[00:33:58] SPEAKER_00: building these things for time. I don't think that's the right way to do it. We'll switch to a more
[00:34:04] SPEAKER_00: value-oriented pricing model at some point. Right now, we're just laser-focused on
[00:34:11] SPEAKER_00: the frontier eight labs. So, an enterprises for us is a longer term plate. When you look at revenue
[00:34:21] SPEAKER_00: numbers in this space, a lot of people shout back. They're not revenue numbers at GMV.
[00:34:28] SPEAKER_01: And given our understanding now that, Bonnie, there's no talent acquisition from your business.
[00:34:34] SPEAKER_01: It's all an RL environment creation business. When you look at the other announcements of
[00:34:40] SPEAKER_01: all-turns of providers, can you help me understand all the revenue or all the GMV?
[00:34:46] SPEAKER_01: Is there mislabeling being done here? I don't want to comment on other companies, but we think about
[00:34:54] SPEAKER_00: revenues differently. The way we think about revenues is more in terms of gap revenues in terms of
[00:35:07] traditional revenue numbers. I'm an investor, Jonathan. I'm trying to understand and learn from
[00:35:13] SPEAKER_01: you of how I should wait revenue in today's AI world versus the previous historical world.
[00:35:19] SPEAKER_01: Should I be impressed by these revenue numbers or should I not? I think it depends on the type of
[00:35:24] SPEAKER_00: revenue. I think these are not SAS ARR numbers. These are not those types of revenues.
[00:35:32] SPEAKER_00: This is a different beast. I think this requires thinking from first principles.
[00:35:39] SPEAKER_00: There is, the revenue here is reoccurring in the sense that oftentimes when you're working
[00:35:49] SPEAKER_00: with a lab on helping the models improve in some area. And I'll speak to Turing. I don't
[00:35:57] SPEAKER_00: want to speak to other companies. When we are helping a lab, let's say, improve their models for
[00:36:02] SPEAKER_00: coding or multi-modality or tool use or working on RL environments for automating all types of
[00:36:09] SPEAKER_00: professional knowledge work, it's usually a reoccurring project where there is projects will start,
[00:36:17] SPEAKER_00: projects will end. And as long as you're doing a good job, there is lots and lots of demand.
[00:36:27] SPEAKER_00: But you have to consistently keep doing a good job. And we also take, it's also important to be
[00:36:33] SPEAKER_00: a trustworthy partner to the labs. We take secrecy very seriously. We make sure that
[00:36:42] SPEAKER_00: our projects are all firewalled between labs. Oftentimes, even with teams within the labs,
[00:36:49] SPEAKER_00: sometimes that's the level of secrecy that you'd need. I'm reminded a little bit about
[00:36:53] SPEAKER_00: how I've been told Foxconn operates. I mean, I don't know anything about that. But I've been told
[00:36:58] SPEAKER_00: that they have different floors where maybe on one floor, the iPhone is getting made and another
[00:37:03] SPEAKER_00: phone, another floor maybe a pixel phone is getting made. And obviously you have to like firewall
[00:37:08] SPEAKER_00: all of that. Of the eight largest providers, do they not spend with all of you?
[00:37:13] SPEAKER_01: They spend with a handful of companies. They do that for to have some level of
[00:37:23] SPEAKER_00: resilience. And I imagine there's some price benefits to having more than one person that they
[00:37:29] SPEAKER_00: could work with. But I think the resilience piece is important. I mean, we know what happened with
[00:37:33] SPEAKER_00: the, you know, when the scale investment happened again, like the it was, the labs did benefit from
[00:37:42] SPEAKER_00: having other partners that they could work with. I would say it's a small handful. It's a small
[00:37:48] SPEAKER_00: handful that are trusted. And of course, there's probably a giant pool of smaller startups. But it's
[00:37:54] SPEAKER_00: a small handful of big companies in the space. Which one do you worry about most? So this is just a
[00:38:00] SPEAKER_00: big, big market that's growing super fast. I'm excited for like all the companies in the space.
[00:38:08] SPEAKER_00: I feel like different companies come into this world with a different DNA. Which lead it to
[00:38:14] SPEAKER_00: you most respect. Sam Altman, Elon Musk. Of the data providers, Jonathan. Of the data.
[00:38:20] SPEAKER_01: I'm pushing you. This one I'm going to get them. I mean, I have a lot of respect for
[00:38:29] SPEAKER_00: Alex Wang from Scale AI. I feel like Alex and Scale were prescient in seeing the importance of data.
[00:38:41] SPEAKER_00: And I admired how having started in autonomous labeling, like how they kind of navigated the ups and
[00:38:49] SPEAKER_00: downs. And yeah, I really like the way he operates as well. I feel like there are certain elements of
[00:39:00] SPEAKER_00: leadership that that I think I share with him. So and I think he did. He did a great job for
[00:39:11] SPEAKER_00: scale. How did Scale being a quiet impact? Sure, he's business. We just got flooded with a lot of
[00:39:18] SPEAKER_00: demand. A lot of demand. And we've also amped up pretty significantly in multi-modality.
[00:39:26] SPEAKER_00: Multi-modality was something I think scale was quite strong in. Multi-modality is
[00:39:34] SPEAKER_00: teaching the models to operate well with not just text but audio video image, etc.
[00:39:41] SPEAKER_00: And outside in I've heard that because of their roots in autonomous labeling, like they were
[00:39:52] SPEAKER_00: quite good in multi-modal stuff. And it was good primarily from just increasing demand.
[00:40:04] SPEAKER_00: And I think they were the company that had been working in this space the longest.
[00:40:13] SPEAKER_00: Do they have a business left? Again, I mentioned Rarajaska. I think he said in a show in
[00:40:17] SPEAKER_01: recent years that this kind of carcass or husk left behind. But if everyone benefited from that
[00:40:24] SPEAKER_01: being bought, they can't be doing that well. I don't know enough about their business.
[00:40:31] SPEAKER_00: Like in terms of... Do you pay attention to competitors? I pay attention to
[00:40:39] SPEAKER_00: competitors in terms of things that they do well and when there are
[00:40:47] SPEAKER_00: any significant learning opportunities from them that could help us so our customers better.
[00:40:54] Do you worry about revenue concentration? You said about kind of A to the biggest labs.
[00:40:59] SPEAKER_01: Say if you look at it like an open AI, they have, I don't know, whatever it is,
[00:41:03] SPEAKER_01: you will know these numbers much better than me. Say 100 million paying customers. I'm just
[00:41:06] SPEAKER_01: taking a 10% on a billion people but give it all take 100 million, whatever.
[00:41:11] SPEAKER_01: And then you look at say a business like ours here, but there's like seven core customers.
[00:41:17] How do we feel about revenue concentration? The last time I checked, like I was told that
[00:41:23] SPEAKER_00: NVIDIA for NVIDIA, 39% of their revenue comes from two clients. And roughly 50% was like four clients.
[00:41:34] SPEAKER_00: I expect the extraordinary. Extraordinary. For a five trillion dollar company.
[00:41:40] SPEAKER_01: Wow, that's nuts. You think about like Apple is not even a comparable in market cap size,
[00:41:46] SPEAKER_01: but what is that like three billion customers? I mean, wow, what a comparison.
[00:41:52] SPEAKER_01: Yes. So I, so in this market, I don't worry that much about revenue concentration. I think we are
[00:42:01] SPEAKER_00: in the same boat as NVIDIA in that there will be lots and lots of spend from these big eight companies.
[00:42:09] SPEAKER_00: And I expect the this market to, I mean, look at the scale of the spend, right? Like Stargate
[00:42:16] SPEAKER_00: is like a hundred billion a year investment on compute. And there's going to be significant
[00:42:23] SPEAKER_00: amounts of spend on compute, energy and data. It's a little weird to have this level of concentration.
[00:42:30] SPEAKER_00: But things could change. I think it's also possible that governments spend even more. I think it
[00:42:37] SPEAKER_00: would make sense for governments to build their own internal versions of some of these models,
[00:42:43] SPEAKER_00: which would require proprietary data again to be collected. Do you not think they'll have to?
[00:42:48] SPEAKER_01: And what I mean by that is like we'll see sovereignty of models. Like I do not think there's
[00:42:52] SPEAKER_01: any way you'll have the German health care system working with American model providers. Sorry to say.
[00:42:58] SPEAKER_01: I think you're right. I think it'll it'll be necessary. In that world, do you provide that FDE
[00:43:03] SPEAKER_01: service to governments? Yes. I think it'll be the work that we are doing in not just training
[00:43:12] SPEAKER_00: superintelligence, but in deploying superintelligence is with that goal in mind. For these governments,
[00:43:17] SPEAKER_00: I imagine we'll help them not just with fine tuning their models with data and e-vals, but also
[00:43:23] SPEAKER_00: helping them with the first mile schlep and the last mile schlep to make these systems actually work.
[00:43:28] SPEAKER_00: And you might want to have like full control over what type of human data is going into these models.
[00:43:34] SPEAKER_00: Like if you are if you're the German government, presumably you want German nationals to be the ones
[00:43:39] SPEAKER_00: that are contributing data, whether it's for SFT or reinforcement learning.
[00:43:43] SPEAKER_00: So I'm worried that we are potentially not going to see AI deliver the immediate revenues that
[00:43:49] SPEAKER_01: we've promised. And we're going to go through a kind of cooling period, whichever I kind of suggest
[00:43:54] SPEAKER_01: and things that we're going to go through in the next six to 18 months, which is as I said, it doesn't
[00:43:59] SPEAKER_01: hit the revenues that we said it would and kind of the AI bubble kind of deflate slowly.
[00:44:05] SPEAKER_01: To what extent do you think that's possible or we'll see this continuing gradual increase
[00:44:12] SPEAKER_01: as we kind of touched on that? I don't see an AI bubble. Like I feel like these models are
[00:44:19] SPEAKER_00: incredibly powerful today. Like GPT-5 is like fucking awesome. I don't know what people were
[00:44:25] SPEAKER_00: talking about when they're talking about, you know, I know there was some chatter. I think we've
[00:44:29] SPEAKER_00: just gotten used to magic and it's like the some of the I feel like A, these models are incredibly
[00:44:37] SPEAKER_00: powerful today and they're the worst they'll ever be. They're only going to keep improving.
[00:44:43] SPEAKER_00: And I say that about the German I Pro models, the GROC models, the Claude models,
[00:44:49] SPEAKER_00: like these models are amazing. And there is a very significant model capability overhang.
[00:44:55] SPEAKER_00: By that, what I mean is the models are capable of X but what we are getting out of the models is
[00:45:01] SPEAKER_00: X minus delta. There is with the right agentics scaffold around these models in terms of the
[00:45:12] SPEAKER_00: right system prompts, the right user prompts giving the models access to the right context,
[00:45:19] SPEAKER_00: teaching the models how to acquire additional context, teaching the models how to use the
[00:45:25] SPEAKER_00: right internal tools. There is significant amount of capability that can be unlocked with today's
[00:45:30] SPEAKER_00: models. For example, you, Harry, I imagine when you do an interview with somebody, one of the things
[00:45:37] SPEAKER_00: you probably do is you apply your secret sauce to pull out the right clips from the interviews
[00:45:42] SPEAKER_00: to like what to highlight, what are the catchphrases, what will sort of drive more engagement.
[00:45:47] SPEAKER_00: That can be done by a model with the right agentics scaffold that's fine tuned on all the work
[00:45:53] SPEAKER_00: that you've done in the past. And you might not. I wish every weekend I go through every single show.
[00:45:59] SPEAKER_01: Yes. And I pick out 15s, 20 clips per show and then I make notes on each one.
[00:46:03] SPEAKER_01: Yeah. Are you saying, Harry, that you want to use Turing?
[00:46:06] If you could fucking make it work, dude, I'll pay you a lot of money.
[00:46:10] SPEAKER_00: Yeah, maybe we should, we should partner.
[00:46:12] SPEAKER_00: Be right. Seriously, every weekend I spend probably three hours per show.
[00:46:17] SPEAKER_01: I definitely 12 hours a weekend doing that. So I think there is this model capability overhang
[00:46:24] SPEAKER_00: where the full potential of the model has not been unlocked by humans yet. And no, I don't think
[00:46:29] SPEAKER_00: there's an AI bubble. I think the, I think there are some growing pains. What are the growing pains?
[00:46:36] SPEAKER_01: I think everybody, like, keeps citing that MIT report about how 95% of pilots fail.
[00:46:43] SPEAKER_00: But because we are in the business of deploying AGI in enterprises, I can tell you like why I think
[00:46:49] SPEAKER_00: that happens, which is one of the growing pains. Step one is that most enterprises need to do some work
[00:46:58] SPEAKER_00: to structure their data in the right way. Again, that first mile schlep has to be done.
[00:47:04] Second, you should surround the model with the right agentics scaffold that I just described.
[00:47:13] SPEAKER_00: The right prompting, the right context engineering, the right internal tool calls that
[00:47:17] SPEAKER_00: you should teach the model to call. All of those have to be distilled into the models.
[00:47:22] SPEAKER_00: You need really good e-vals. You also need a workflow designed for partial autonomy.
[00:47:28] SPEAKER_00: Andre Karpati articulated this first. When talking about why cursor works so well,
[00:47:34] SPEAKER_00: because it's not designed for full autonomy, it's designed today for partial autonomy for
[00:47:39] SPEAKER_00: humans to collaborate with the AI to do that specific task. So that cursor for X needs to be built
[00:47:46] SPEAKER_00: for every role, for every workflow to help humans work more easily with the models.
[00:47:51] SPEAKER_00: Does every role need to go through that pathway of cursor for X before it goes to full autonomy,
[00:47:56] SPEAKER_01: or are there some roles like customer service where it just goes to full autonomy?
[00:48:00] I think for some roles where you can see that the models are quite good at matching humans,
[00:48:10] SPEAKER_00: I think we don't need that intermediate step. There are certain roles where
[00:48:19] SPEAKER_00: by virtue of how the models are trained, where they are trained with tokens on the internet,
[00:48:26] SPEAKER_00: and then of course with talent from research accelerators like Turing, that's fine Turing the models.
[00:48:33] But there are certain types of roles where the tokens from the internet give it sufficient
[00:48:37] SPEAKER_00: intelligence to do the job well. Customer support is an example. But if you pick other roles,
[00:48:44] SPEAKER_00: like for example, if you picked the role of let's say an AI researcher,
[00:48:49] SPEAKER_00: or you pick the role of a lawyer specializing in venture capital financing,
[00:48:58] SPEAKER_00: it's possible there's not enough of those tokens on the internet. So the models will be relatively
[00:49:04] SPEAKER_00: weak there out of the box. And also the way, I don't know, the way a Wilsonson Cine does financing might
[00:49:10] SPEAKER_00: look different from the way a Cooley does it, maybe they have their own way. So you might want to
[00:49:15] SPEAKER_00: fine tune them on your own proprietary data, distal the proprietary intelligence of humans working there.
[00:49:25] SPEAKER_00: So for those things like you may need to do some fine tuning, the models may not work very well
[00:49:31] SPEAKER_00: out of the box. A lot of people suggest the circular deals between some of the large providers
[00:49:35] SPEAKER_01: suggest the strains in the ecosystem or the bubble light tendencies. Do you think that's fair or not?
[00:49:41] SPEAKER_01: I sort of categorize the world into two classes. Class one is those that believe in AGI,
[00:49:53] SPEAKER_00: that we, let's call it the AGI-pilled group that believe that we are on the path to getting to
[00:50:00] SPEAKER_00: AGI. And let's define AGI as an AI system capable of at least matching humans in almost all types
[00:50:08] SPEAKER_00: of intellectual knowledge work. Then there is a world that is a maybe another category of people
[00:50:14] SPEAKER_00: that don't believe this will happen, we'll hit a wall. And in the past, there have been other AI
[00:50:19] SPEAKER_00: paradigms where we did hit a wall. So for the camp that believes in AGI, and I believe in AGI,
[00:50:28] SPEAKER_00: unsurprisingly, but I love AI and it's been my passion for like the last 20 years.
[00:50:34] SPEAKER_00: The, I really believe that we will get there. If you believe that, the grand prize is so amazing.
[00:50:43] SPEAKER_00: Right? Like if you've solved intelligence, you've solved all of humanity's grandest problems
[00:50:48] SPEAKER_00: from curing diseases to potentially pausing aging to like interstellar travel to energy. Like
[00:50:56] SPEAKER_00: all of our problems are intelligence constrained. Right? So if you've, so the prize is so large,
[00:51:02] SPEAKER_00: I mean, whoever wins the super intelligence race will probably win search, will probably win consumer
[00:51:08] SPEAKER_00: devices, will probably win operating systems, will probably win cloud, like business productivity
[00:51:13] SPEAKER_00: software. It's like the prize is so massive that it's worth placing big forward bets in these
[00:51:21] SPEAKER_00: areas because the cost of not winning is too high. Whoever wins AGI would also probably win social
[00:51:26] SPEAKER_00: networking. So you can see why the big eight are excited about it because it's, you're playing for
[00:51:32] SPEAKER_00: everything. It's like whoever wins this could be responsible for that $30 trillion of knowledge work
[00:51:38] SPEAKER_00: with full. Well, if you're, if you're a zark, you spend $100 billion on it. If you lose or fail,
[00:51:47] SPEAKER_01: likely everyone else will fail in which case you're behind just like they are and you've lost
[00:51:51] SPEAKER_01: $100 billion, which isn't a huge amount of your free cash flow, maybe 12 to 18 months of free cash flow.
[00:51:55] SPEAKER_01: If you don't spend the $100 billion and someone else does and wins, you lose two trillion,
[00:52:00] SPEAKER_01: three trillion dollars of market cap. Correct. You have to play. You have to play. Imagine if somebody
[00:52:05] SPEAKER_00: built a more engaging social network and social networks have just one unit, which is attention.
[00:52:11] SPEAKER_00: I mean, if we all only have like maybe, you know, a few, maybe 45 hours a day to spend on an app.
[00:52:17] SPEAKER_00: If there was a more engaging app than yeah, that's, that's, that's those are high sticks.
[00:52:22] SPEAKER_00: Do you agree then with the notion that if you believe in AGI, you cannot be investing in SaaS apps.
[00:52:30] SaaS as we note, I think is over. I feel like quite a few SaaS apps were built at a time when
[00:52:42] SPEAKER_00: software was relatively hard to build and complex to build. Imagine if you were building some
[00:52:50] SPEAKER_00: customer support software, some customer support bought. To build a company like that, you would
[00:52:56] SPEAKER_00: have had to hire some Stanford PhDs in NLP. You'll collect data for six months. You'll have like,
[00:53:03] SPEAKER_00: you'll use like a support vector machine or a neural network that'll kind of sort of work.
[00:53:07] SPEAKER_00: And then you'll deploy it and you'll grind away for a while. There is a significant amount of
[00:53:12] SPEAKER_00: capital that needs to be invested to get an app like that to work well. So it made sense for
[00:53:17] SPEAKER_00: many companies to not bother doing that. If that's not their core business, let me just use
[00:53:22] SPEAKER_00: like some third-party SaaS app. Now, many of these AI applications are incredibly easy to build
[00:53:32] SPEAKER_00: on top of these LLMs. So I feel like most companies will start building custom software super
[00:53:38] SPEAKER_00: easily. I mean, we help companies build some of these custom apps. And the bar to
[00:53:45] SPEAKER_00: create many of these apps significantly comes down. So that's one risk. Risk number one companies do
[00:53:51] SPEAKER_00: it themselves. Risk number two is that you get Sonic boomed by the foundation model companies.
[00:54:01] SPEAKER_00: Sonic boomed by meaning... So today, they move into the app slide and just create it themselves.
[00:54:07] Yes. I mean, it could happen, right? Like the you could... The models are becoming agentic. I mean,
[00:54:14] SPEAKER_00: you've seen many of these agents, right? It's fundamentally it's about computer use agents.
[00:54:20] If the models get better and better there, it's possible like the model is all you need. Like the...
[00:54:26] SPEAKER_00: I mean, imagine if you wanted the model to... Hey, update my... Let's say I'm doing some HR thing.
[00:54:39] SPEAKER_00: Hey, update my medical benefits information to add. We've just had a new daughter. We want to update
[00:54:50] SPEAKER_00: my medical information. If the model is agentic and it is sufficiently integrated into the
[00:54:59] SPEAKER_00: knowledge, into the database of the organization, you could... You don't need anything else in the
[00:55:05] SPEAKER_00: middle. So that's the second risk. The model is becoming more agentic. The third, and I worry about
[00:55:10] SPEAKER_00: this a lot, I feel like a lot of our software was designed to be used by humans, humans navigating
[00:55:17] SPEAKER_00: a GUI and clicking around and doing things. I think that's going to go away. Like with the multi-modal...
[00:55:24] SPEAKER_00: Again, this way, I think of four pillars to superintelligence. It's multi-modality reasoning,
[00:55:30] SPEAKER_00: tool use encoding. Multi-modality is important because we humans interact in natural language. We talk,
[00:55:36] SPEAKER_00: this video, all of that. I think the future might look like some type of ambient AI that you
[00:55:44] SPEAKER_00: talk to that will just go and do things. And maybe it'll use the GUI of the current SAS application
[00:55:53] SPEAKER_00: as like an intermediate step or it'll use MCP and use tool calls and get what it needs.
[00:55:58] SPEAKER_00: The GUI was designed for a world where humans were using a keyboard and a mouse and clicking
[00:56:04] SPEAKER_00: around and doing things. I think humans can do better things with their time than click around and...
[00:56:11] SPEAKER_00: As you want big change, I have it. I never actually type emails anymore. I use whisper flow and it's
[00:56:16] SPEAKER_01: so good in transcription that I didn't have a type email. Now the intrubbt is everyone knows
[00:56:21] SPEAKER_01: what I'm saying in my emails. The Whistleful founders interned at Turing back today. No way.
[00:56:26] SPEAKER_00: Yeah. Wow. So how do I feel about it? No, I don't agree. Why? Because the average company
[00:56:36] SPEAKER_01: today has between 80 and 100 different SAS products that they engage with. One, just the multitude
[00:56:42] SPEAKER_01: of how many that have to create. Number one, number two, at maintaining them, you think they're
[00:56:47] SPEAKER_01: going to maintain 80 to 100? Oh my god, you're going to have like just teams and teams of people
[00:56:52] SPEAKER_01: doing maintenance and updates and debugging. I don't think so either. And that is for the
[00:56:56] SPEAKER_01: technology savvy. Let's talk about every plumbing provider, law firm, accounting firm, restaurant
[00:57:04] SPEAKER_01: that can barely use Whistle's Squarespace. Let alone build out their own CRM system and POS
[00:57:10] SPEAKER_01: system. Not a freaking chance. And then we moved to foundation model companies moving into very
[00:57:16] SPEAKER_01: vertically specific elements. We're in a business that does AI for patent creation, updates
[00:57:23] SPEAKER_01: and collaboration. Asam is not going there. Sam has health, you know, solving cancer, energy
[00:57:31] SPEAKER_01: utilization. I don't think Sam's touching patent creation and updating. And so I think for
[00:57:38] SPEAKER_01: the more verticalized you go, the more defensibility you have. And so I think for those reasons,
[00:57:43] SPEAKER_01: SaaS has life. Mine is a very biased perspective because it's my job. Is that all wrong again?
[00:57:50] SPEAKER_01: That you're the master here, John. And so like VCs are literally middlemen.
[00:57:55] SPEAKER_01: I'd say, Harry, like you have an interesting data set because you invest in a ton of startups.
[00:58:01] SPEAKER_00: So I would be curious looking at your sample of startups that you've invested in. And just
[00:58:07] SPEAKER_00: tally how many SaaS apps they use today at every stage and see if that has changed, like post
[00:58:14] SPEAKER_00: chat GPT, like see, like I'd be cute. My hypothesis is that today's companies use fewer SaaS apps
[00:58:22] SPEAKER_00: and have fewer people. Do you think we have more or less software engineers in 10 years? More.
[00:58:28] Help me understand that. I think the definition of a software engineer will change.
[00:58:32] SPEAKER_00: A Stanford doctor who's in oncology who has an idea for like some, you know, cancer detection type
[00:58:44] SPEAKER_00: app. Now that person will be able to create like a very simple version of an app that somebody could
[00:58:50] SPEAKER_00: check by themselves and send as do like a home diagnosis. I think it'll, I think there'll be more
[00:58:59] SPEAKER_00: software engineers because if you define a software engineer as somebody who's capable of building
[00:59:06] SPEAKER_00: a software product to solve a real problem, that pool of builders is going to expand way beyond
[00:59:12] SPEAKER_00: people who've graduated with like a four year computer science degree. So we have more software
[00:59:17] SPEAKER_01: engineers creating more software and the problem then becomes discovering. How do we solve the
[00:59:23] SPEAKER_01: discovery problem in a world of infinite software? You might have an agent for yourself that's
[00:59:28] SPEAKER_00: talking to other agents on the internet. Like the, have you seen her? The movie? Yeah. Yeah.
[00:59:34] SPEAKER_00: I really think like we'll have, you might have like, there's probably an agent for Harry that's
[00:59:43] SPEAKER_00: just tasked with discovering what pieces of software Harry should be using. And that might be talking to,
[00:59:51] SPEAKER_00: I mean, I might have an agent that is maybe talking about what types of, that's marketing things
[00:59:57] SPEAKER_00: that I've built or that I have. And it would be, and I think we'll just be in a world where we have
[01:00:04] SPEAKER_00: digital targets of ourselves that are communicating with other digital targets. I, you might have an
[01:00:12] SPEAKER_00: agent of yourself that's like discovering startups to invest in. And while you and I are chatting,
[01:00:18] SPEAKER_00: there's probably, I don't know, you might be having like a million conversations with entrepreneurs
[01:00:24] SPEAKER_00: from all over the world, who today you're, you're kind of constrained by space and time. But
[01:00:29] SPEAKER_00: in the future, you'll only be compute and data constrained. Do we lose the phone as the interface
[01:00:34] SPEAKER_01: to this world? We obviously see Sam and Johnny, I've, you know, this room is appendent and some
[01:00:39] SPEAKER_01: hardware devices are not asking you to comment on that. I'm just saying, does the phone become,
[01:00:43] SPEAKER_01: still remain the primary interface and design device? We'll have some type of a device
[01:00:50] SPEAKER_00: that is, that will carry that's always on and processing multimodal tokens. For example, as I'm
[01:01:00] SPEAKER_00: talking to you, if I were to envision my perfect device, it would be something that has,
[01:01:07] it should have cameras. So maybe it's a wearable as a glass or something that I'm having on me that's
[01:01:13] SPEAKER_00: processing visual input because I want to be able to read your body language. I might have like
[01:01:20] SPEAKER_00: airport like thing in my year that's whispering to me that maybe says, Jonathan, as you were talking
[01:01:26] SPEAKER_00: about multimodality, Harry seemed less interested. His, his body cues suggest that he was losing interest.
[01:01:32] SPEAKER_00: But when we were talking about AR, he worked up. So those types of feedback and cues, I think
[01:01:36] SPEAKER_00: would be good. So I envision a device that I think of it in terms of sensors and effectors. In
[01:01:43] SPEAKER_00: terms of sensors, like obviously, it has to be listening to stuff. It has to be seeing stuff.
[01:01:50] SPEAKER_00: But in terms of effectors, it'll probably also be speaking in my year.
[01:01:56] SPEAKER_00: Ideally, it should be something that you can talk to and have it do things later. For example,
[01:02:01] SPEAKER_00: I might say, remind me to follow up with Harry on that idea for using Turing to automate clip
[01:02:10] SPEAKER_00: generation. Right? Like the, so it has to like remember that and come back later. So I do think
[01:02:16] SPEAKER_00: there'll be all sorts of new devices and glasses hearing like these airport type devices
[01:02:27] seem obvious. There could be like, have you, do you remember this device that was called the meeting
[01:02:33] SPEAKER_00: owl? No. Like during like the COVID era, like the one of the tools that sort of spiked was like this,
[01:02:41] SPEAKER_00: it was basically like a speaker phone for like having conference, having better distributed
[01:02:49] SPEAKER_00: team zoom meetings. Okay. When somebody's talking, it would focus on them like with like a camera
[01:02:54] SPEAKER_00: and it would, it was also a decent speaker. So I can imagine devices like that that people have like
[01:03:02] SPEAKER_00: when, yeah. So it's hard, it's hard to predict. But the thing that I almost feel confident about
[01:03:10] SPEAKER_00: is that the phone will look so different. I mean, when we think of our smartphone, it's basically
[01:03:16] SPEAKER_00: a computer with like a phone app in it, right? Like the phone app is like the least interesting
[01:03:20] SPEAKER_00: part of the phone. And I think even for for an AI device, the it'll probably have some phone app
[01:03:27] SPEAKER_00: in it. But everything else I feel like will be magical. Like I feel like I would definitely benefit
[01:03:33] SPEAKER_00: from a device that's constantly listening to everything that I'm listening to constantly processing
[01:03:40] SPEAKER_00: all the video audio input that I'm processing. And something that's paging things to memory,
[01:03:48] SPEAKER_00: like maybe it'll like write things down and be able to look it up later. I see it almost like an
[01:03:52] SPEAKER_00: extension of my brain. Before we move into the quick fire out, I do just have to ask what does your
[01:03:58] SPEAKER_01: market and the data provisioning market look like in 10 years? I always try and think about like
[01:04:03] SPEAKER_01: market composition and dynamics. Is it a winner take-oo? Is it a very fragmented? Is it a 304?
[01:04:10] SPEAKER_01: What does that look like? The market will reward players with research depth because
[01:04:18] SPEAKER_00: the pace of AI research is so rapid. Like all these oral environments like this
[01:04:25] SPEAKER_00: spiked in like the last 12 months after O1 came out in December and deep seek came out in Jan.
[01:04:33] SPEAKER_00: So now it's like in addition to imitation learning, we are in this reinforcement learning regime.
[01:04:37] SPEAKER_00: One year ago, one year later, it could be something totally different. So I think the market will
[01:04:42] SPEAKER_00: reward a company with research DNA. And it'll reward a company that can move fast and
[01:04:52] SPEAKER_00: adapt very quickly because this is I mean when you're so- Do you think this is a monopoly market or
[01:04:58] SPEAKER_01: do you think there will be many winners? I think there'll be a few winners. I think there'll be a few
[01:05:03] SPEAKER_00: winners. A few because I do think for the labs it helps them to have a few partners for resiliency.
[01:05:15] SPEAKER_00: And I imagine also for price competitiveness. I think there'll be a few winners. In the realm of
[01:05:25] SPEAKER_00: robotics and embodied AI, we are still very early. At Turing, we are scaling up on the
[01:05:29] SPEAKER_00: robotics side as well in terms of data that we generate. But there's so much data that's missing
[01:05:36] SPEAKER_00: that the models need to see that they haven't seen yet. I can totally imagine some newer companies
[01:05:40] SPEAKER_00: also coming up that don't exist today. If you do investing companies in your space,
[01:05:46] SPEAKER_01: where would you invest? Probably in robotics or embodied AI. The vertical stuff, like I mean,
[01:05:53] SPEAKER_00: we are scaling up pretty massively in generating data for different verticals. So I don't see that
[01:06:02] SPEAKER_00: as like a big white space. But I think everybody is relatively early with robotics.
[01:06:07] SPEAKER_00: And robotics is such a fast realm that there could be interesting things to do there. One way I see
[01:06:14] SPEAKER_00: the space, Harry, is again, think of like these three dimensions. The first dimension being the
[01:06:25] SPEAKER_00: type of intelligence that you're baking into the models that could be encoding in STEM,
[01:06:31] SPEAKER_00: in functional expertise like sales, marketing, software engineering, or vertical expertise,
[01:06:37] SPEAKER_00: like healthcare, legal finance, etc. So the first dimension is the type of intelligence. I do a
[01:06:42] SPEAKER_00: cross product of that with the modality. So audio video image, computer use. So that's multi-modality.
[01:06:49] SPEAKER_00: That's the second dimension. The third dimension is multi-linguality, like different languages.
[01:06:53] SPEAKER_00: Right. And the fourth dimension is different learning paradigms, like imitation learning,
[01:07:01] SPEAKER_00: reinforcement learning, pre-training as well, which is unsupervised learning. And all of those
[01:07:07] SPEAKER_00: may require different platforms to be built. Like we've had to adapt our platform for imitation
[01:07:12] SPEAKER_00: learning, for reinforcement learning, for multi-modality. So I feel like in this matrix, there's like all
[01:07:20] SPEAKER_00: sorts of new opportunities that could emerge. And I only listed like the digital intelligence. I
[01:07:30] SPEAKER_00: didn't talk about physical intelligence. So I think robotics is like wide open. I mean the kind
[01:07:34] SPEAKER_00: of data that a robot that is in someone's home is totally different from like a robot that's
[01:07:42] SPEAKER_00: doing things in a factory. And humanoid versus non-humanoid robots. I can talk to you all day. I
[01:07:47] SPEAKER_01: do want to move into a quick fire answer. I say a short statement. You give me your immediate
[01:07:50] SPEAKER_01: thoughts. What's one widely held belief about AI that you think is wrong? I don't think we'll see
[01:07:57] SPEAKER_00: rapid takeoff. I think we'll see incremental continuous improvement in AI. I actually think this
[01:08:05] SPEAKER_00: is good for the world because if what we believe happens, which is all types of digital knowledge
[01:08:14] SPEAKER_00: work gets automated. I think humanity needs time to prepare its workflows. I think we could use the
[01:08:23] SPEAKER_00: extra time to upskill humans to rethink education to make sure there isn't massive job displacement.
[01:08:30] SPEAKER_00: I also think in the steady continuous improvement in AI models, there'll be value realized every
[01:08:39] SPEAKER_00: step of the way. Unlike self-driving cars, I feel like people have this wrong model for
[01:08:44] SPEAKER_00: AI that comes from self-driving cars where you get 99% of the way accurate and you, if you can't
[01:08:50] SPEAKER_00: solve the last one percent, they're not useful. AgeEI is not like that. I think when we automate the
[01:08:55] SPEAKER_00: job of an underwriter or a claims processor or a CEO, there's incremental value that's unlocked
[01:09:01] SPEAKER_00: for every percentage improvement in the model's becoming more reliable. So I believe in slow and
[01:09:07] SPEAKER_00: steady takeoff and that's actually going to be great for the world. You mentioned deep seeking
[01:09:11] SPEAKER_00: couple of times. Do you think we underestimate China? It depends on who you ask. The folks that I work
[01:09:20] SPEAKER_00: closely with don't underestimate China. It's very impressive, like the progress that they've made
[01:09:27] SPEAKER_00: in open source with deep seek, Kimi K2, Kwen. These models are state-of-the-art.
[01:09:34] SPEAKER_00: So no, I don't think at least among the frontier AI circles that I'm in, I think there's a
[01:09:45] clear realization of how close they are. The world seems to be moving to close models.
[01:09:54] SPEAKER_00: Is that good or bad? I think it depends on the application. I feel like
[01:10:02] SPEAKER_00: in the firstly in enterprises, it's often a mix of between proprietary and closed models. I wouldn't,
[01:10:13] SPEAKER_00: sorry, between closed and open models. We do see demand from enterprises that want either.
[01:10:23] SPEAKER_00: The closed models often are easier to get started with, but there are some cases where
[01:10:31] SPEAKER_00: enterprises prefer open models for cost, customizability. I'm talking about the small language model
[01:10:41] SPEAKER_00: regime between the half a billion parameters to 10 billion parameters. I worry a little about
[01:10:50] SPEAKER_00: frontier models. I feel like for frontier models, there is some value in keeping
[01:10:58] SPEAKER_00: some of the technology closed. Just because of how powerful they are, and I feel like the US labs
[01:11:15] SPEAKER_00: are extremely responsible and safety conscious in how they think about training these models,
[01:11:21] SPEAKER_00: deploying them. Do you think Elon is? You mentioned reading his book earlier. Elon is often
[01:11:26] SPEAKER_01: chastised for his lack of care around some of the training elements. Do you think he is? Do you
[01:11:35] SPEAKER_01: think he'll benefit from not having that? God rail. I think Elon is also, he cares a lot about
[01:11:43] SPEAKER_00: humanity too. In his book, one of the things I recall reading is his motivation for getting into AI
[01:11:53] SPEAKER_00: was that he wanted an AI that was species and loves humanity. That was one of his reasons to
[01:12:04] SPEAKER_00: get into it. Everything I see about the Grog team, I feel like their goals are much like any of the
[01:12:14] SPEAKER_00: frontier labs, like quite noble in terms of having this powerful AI that can help humanity understand
[01:12:21] SPEAKER_00: the universe, solve some of our biggest problems. What did you believe that you now no longer believe?
[01:12:27] SPEAKER_00: I used to believe that to build a enduring valuable company, you hire a strong
[01:12:40] SPEAKER_00: exact team and operate with a lot of leverage. Basically, hire strong people and get out of the way.
[01:12:48] SPEAKER_00: I used to believe that. Now I believe you hire great people and work really closely with them
[01:12:55] SPEAKER_00: and their directs and their directs and get as close to the ground as you can, where ground truth
[01:13:05] SPEAKER_00: usually exists with the customers. The next step to customers is the engineers writing code
[01:13:11] SPEAKER_00: and the salespeople talking to your customers. Now I believe in being, basically, I used to,
[01:13:19] SPEAKER_00: for lack of a better word, follow the org chart a little bit. This was also part of one of my
[01:13:24] SPEAKER_00: learnings from Elon's biography is that he was so hands-on. He would be walking the factory floor
[01:13:31] SPEAKER_00: and asking an engineer why this door in the Model 3 has three bolts instead of maybe two.
[01:13:38] SPEAKER_00: It is a different way to operate, where you're in the details of the most important things that
[01:13:47] SPEAKER_00: matter, completely working in a flat structure and just operating as close to the ground truth as you
[01:13:55] SPEAKER_00: can. Generally, I feel like in the early days of starting Turing, now that I think about it,
[01:14:03] SPEAKER_00: I may have had a subconscious desire to be liked. I think I must have. Now I don't. Now I just
[01:14:13] SPEAKER_00: think about just doing things that would solve our customers problem the best.
[01:14:20] SPEAKER_00: What was the most unpopular decision you've taken with Turing? Turing is switching from a distributed
[01:14:27] SPEAKER_00: team to a hub-and-spoke model. We are now working from an office in San Francisco and we've
[01:14:35] SPEAKER_00: recently opened an office in Palo Alto. We're going to be opening an office in London as well.
[01:14:41] SPEAKER_00: Very exciting. For some people, that wasn't very popular. Until you fired them.
[01:14:46] SPEAKER_00: Some of them left. We like in person. We're big fans of in person here. Final one,
[01:14:54] SPEAKER_01: when you look forward to the next decade, what are you most excited for? For me, my mother has
[01:15:00] SPEAKER_01: MS. I think we'll have some pretty groundbreaking breakthroughs in MS drug discovery that we haven't
[01:15:05] SPEAKER_01: had for, whatever. That excites me. I'm excited about AI making new discoveries and automating AI
[01:15:17] SPEAKER_00: research itself. To get to a point where AI is in some self-improvement loop,
[01:15:29] SPEAKER_00: we could get to superintelligence faster. Automating AI research and getting AI to the point of
[01:15:37] SPEAKER_00: making new breakthrough discoveries. I'm excited by that. I've always been fascinated by AI
[01:15:45] SPEAKER_00: as this exoskeleton that makes you a lot more productive. Have you watched the Iron Man movies?
[01:15:52] SPEAKER_00: Yeah. In the early Iron Man movies, he's wearing the suit and the suit is obviously giving him
[01:16:00] SPEAKER_00: superpowers. Later, once the suit is quote-unquote, agentic where he has these drone suits, where there's
[01:16:08] SPEAKER_00: an army of suits that go off and do things, I'm excited about a future like that where
[01:16:14] SPEAKER_00: every human on the planet has access to agentic AIs that help them amplify their fullest potential.
[01:16:24] Today, Harry might have 100 ideas, but Harry's able to do maybe two of them really well. I like a
[01:16:32] SPEAKER_00: future where Harry can do the remaining 98. And I like that for like the 7 billion humans on Earth.
[01:16:40] SPEAKER_00: I like that too for my weekends, sake to be honest. Jonathan, I love conversations which are
[01:16:45] SPEAKER_01: very natural and free-flowing. You can tell that I don't really pay much attention to the schedule,
[01:16:51] SPEAKER_01: but you've been fantastic. So thank you so much for joining me.
[01:16:54] SPEAKER_01: Thank you, Harry, for having me.