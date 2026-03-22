[00:00:00] Jason Calacanis: Special episode this week. We've preempted the weekly show, and there's only three people we preempt the show for. President Trump, Jesus, and Jensen. And I'll let you pick which order we do that. But what an amazing run you've had and a great event.

[00:00:18] Jensen Huang: Every industry is here. Every tech company is here. Every AI company is here. Incredible. Incredible.

[00:00:25] Jason Calacanis: Jensen Huang, Incredible. Jensen Huang, Extraordinary. And one of the great announcements of the past year has been Grok. When you made the purchase of Grok, did you realize how insufferable Chamath would become?

[00:00:35] Jensen Huang: Jensen Huang, I had an inkling that...

[00:00:39] Jason Calacanis: Jensen Huang, We're his friends. We have to deal with them every week.

[00:00:41] Jensen Huang: Jensen Huang, I know it.

[00:00:42] Jason Calacanis: Jensen Huang, You had to deal with them for the six-week close.

[00:00:44] Jensen Huang: Jensen Huang, I know it. Jensen Huang, It's like two weeks. Jensen Huang, It's all coming back to me now. It's making me rather uncomfortable. The thing is, many of our strategies, are presented in broad daylight at GTC years in advance of when we do it. Jensen Huang, Two and a half years ago, I introduced the operating system of the AI factory, and it's called Dynamo.

[00:01:08] Jensen Huang: Dynamo, as you know, is a piece of instrument, a machine that was created by Siemens to turn essentially water into electricity. Dynamo powered the factory of the last industrial revolution. Dynamo, so I thought it was the perfect name for the operating system of the next industrial revolution, the factory of that. And so inside Dynamo, the fundamental technology is disaggregated inference.

[00:01:37] Jensen Huang: Jensen, I know you're super technical. Jensen Huang, Absolutely. Jensen Huang, I know it.

[00:01:41] Jason Calacanis: Jensen Huang, I'll let you take this one. Go ahead and define it for the audience. I don't want to step on you.

[00:01:44] Jensen Huang: Jensen Huang, Yeah. Thank you. I knew you wanted to jump in there for a second. Jensen Huang, Yeah. Jensen Huang, But it's disaggregated inference, which means the pipeline, the processing pipeline of inference is extremely complicated. And in fact, it is the most complicated computing problem today. Incredible scale, lots of mathematics of different shapes and sizes.

[00:02:03] Jensen Huang: Jensen Huang, And we came up with the idea that you would change, you would disaggregate parts of the processing such that some of it can run on some GPUs, rest of it can run on different GPUs. And that led to us realizing that maybe even disaggregated computing could make sense, that we could have different heterogeneous nature of computing. Jensen Huang, That same sensibility led us to Mellanox. Jensen Huang, Yep.

[00:02:31] Jensen Huang: Jensen Huang, You know, today, NVIDIA's computing is spread across GPUs, CPUs, switches, scale up switches, scale out switches, networking processors. And now we're going to add Grok to that. And we're going to put the right workload on the right chips. You know, we just really evolved from a GPU company to an AI factory company.

[00:02:49] Chamath Palihapitiya: Jensen Huang, I mean, I think that was probably the biggest takeaway that I had. Jensen Huang, You're seeing this fundamental disaggregation where we've gone from a GPU and now you have this complexion of all these different options that will eventually exist. The thing that you guys said on stage or you said on stage was, I would like the high value inference people to take a listen to this. And 25% of your data center space, you said should be allocated to this Grok LPU GPU combo.

[00:03:16] Jensen Huang: Jensen Huang, We should add Grok to about 25% of the Vera Rubins in the data center.

[00:03:20] Chamath Palihapitiya: Jensen Huang, So can you tell us about how the industry looks at this idea of now basically creating this next generation form of disaggregated pre-filled, decode, disag, and how people do you think will react to it?

[00:03:32] Jensen Huang: Jensen Huang, Yeah. And take a step back. And at the time that we added this, we went from large language model processing to agentic processing. Jensen Huang, Now when you're running an agent, you're accessing working memory, you're accessing long-term memory, you're using tools, you're really beating up on storage really hard. Jensen Huang, You have agents working with other agents. Jensen Huang, Some of the agents are very large models. Jensen Huang, Some of them are smaller models.

[00:04:01] Jensen Huang: Jensen Huang, Some of them are diffusion models. Jensen Huang, Some of them are auto regressive models. Jensen Huang, And so there's all kinds of different types of models inside this data center. Jensen Huang, We created Verirubin to be able to run this extraordinarily diverse workload. Jensen Huang, My sense is, and so we added, we used to be a one rack company. Jensen Huang, We now added four more racks.

[00:04:22] Jensen Huang: Jensen Huang, So NVIDIA's TAM if you will, increased from whatever it was to probably something, call it, you know, 33%, 50% higher. Jensen Huang, Now part of that 33% or 50%, a lot of it's going to be storage processors. Jensen Huang, It's called Bluefield. Jensen Huang, Some of it will be, a lot of it I'm hoping, will be Grok processors. Jensen Huang, And some of it will be CPUs. Jensen Huang, And they're all going to, and a lot of it's going to be networking processors.

[00:04:48] Jensen Huang: Jensen Huang, And so all of this is going to be running basically the computer of the AI revolution called Agents. Jensen Huang, Right. Jensen Huang, The operating system of modern industry.

[00:05:00] David Friedberg: Jensen Huang, What about embedded applications? Jensen Huang, So you know, my daughter's teddy bear at home wants to talk to her. Jensen Huang, What goes in there? Jensen Huang, Is it a custom ASIC? Jensen Huang, Or does there end up becoming much more kind of a broader set of TAM with developing tools that are maybe different for different use cases of the edge and an embedded application set?

[00:05:18] Jensen Huang: Jensen Huang, We think that there's three computers in the problem at the largest scale when you take a step back. Jensen Huang, There's one computer that's really about training the AI model, developing, creating the AI. Jensen Huang, Another computer for evaluating it. Jensen Huang, Depending on the type of problem you're having, like for example, you look around, there's all kinds of robots and cars and things like that. Jensen Huang, You have to evaluate these robots inside a virtual gym that represents the physical world.

[00:05:47] Jensen Huang: Jensen Huang, So it has to be software that obeys the laws of physics. Jensen Huang, And that's a second computer. Jensen Huang, We call that Omniverse. Jensen Huang, The third computer is the computer at the edge, the robotics computer. Jensen Huang, That robotics computer, one of them could be self-driving car. Jensen Huang, Another one's a robot. Jensen Huang, Another one could be a teddy bear. Jensen Huang, Little tiny one for a teddy bear. Jensen Huang, One of the most important ones is one that we're working on that basically turns the telecommunications base stations into part of the AI infrastructure.

[00:06:14] Jensen Huang: Jensen Huang, So now, all of the, it's a $2 trillion industry. Jensen Huang, All of that in time will be transformed into an extension of the AI infrastructure. Jensen Huang, And so radios will become edge devices, factories, warehouses, you name it. Jensen Huang, And so there are three, these three basic computers, all of them, you know, are going to be necessary.

[00:06:37] Brad Gerstner: Jensen, Last year, I think you were ahead of the rest of the world in saying inference isn't going to 1,000x. Jensen Huang, Yes. Jensen Huang, Brad, you're hurting my feelings. Jensen Huang, Is it going to 1,000,000x? Jensen Huang, Yeah. Jensen Huang, Is it going to 1,000,000x?

[00:06:50] Jensen Huang: Jensen Huang, Yeah.

[00:06:50] Brad Gerstner: Jensen Huang, Right? Jensen Huang, And I think people at the time thought it was pretty hyperbolic because the world was still focused on pre-scaling, on training. Jensen Huang, Here we are. Jensen Huang, Now inference has exploded. Jensen Huang, We're inference constrained. Jensen Huang, You announced an inference factory that I think is leading edge, that's going to be 10x better in terms of throughput to the next factory.

[00:07:14] Brad Gerstner: Jensen Huang, The first factory is going to cost 40 or 50 billion, and the alternatives, the custom ASICs, AMD, others are going to cost 25 to 30 billion, and you're going to lose share. Jensen Huang, So why don't you talk to us? What are you seeing? How do you think about share? And does it make sense for all these folks to pay something that's a 2x premium to what others are marketing?

[00:07:33] Jensen Huang: Jensen Huang, The big takeaway, the big idea is that you should not equate the price of the factory and the price of the tokens, the cost of the tokens. Jensen Huang, It is very likely that the 50 billion dollar factory, and in fact, I can prove it, that the 50 billion dollar factory will generate for you the lowest cost tokens.

[00:07:59] Jensen Huang: Jensen Huang, And the reason for that is because we produce these tokens at extraordinary efficiency. Jensen Huang, 10 times, you know, the difference between 50 billion, now it turns out 20 billion is just land power and shell, right? Jensen Huang, Right. Jensen Huang, And then on top of that, you have storage anyways, networking anyways, you got CPUs anyways, you got servers anyways, you got cooling anyways.

[00:08:20] Jensen Huang: Jensen Huang, The difference between that GPU being 1x price or half x price is not between 50 billion and 30 billion. Jensen Huang, Right. Jensen Huang, Pick your favorite number, but let's say between 50 billion and 40 billion. Jensen Huang, That is not a large percentage when the 50 billion dollar data center is actually 10 times the throughput. Jensen Huang, Right. Jensen Huang, Jensen Huang, That's the reason why I said that even for most chips, if you can't keep up with the state of the technology and the pace that we're running,

[00:08:49] Jensen Huang: Jensen Huang, Even when the chips are free, it's not cheap enough.

[00:08:52] Chamath Palihapitiya: Jensen Huang, Yeah. Jensen Huang, Can I just ask a general strategy question? Jensen Huang, Yeah. Jensen Huang, I mean, you're running the most valuable company in the world. Jensen Huang, This thing is going to do 350 plus billion of revenue next year, 200 billion of free cash flow. Jensen Huang, It's compounding at these crazy rates. Jensen Huang, How do you decide what to do? Jensen Huang, Like how do you actually get the information? Jensen Huang, I mean, it's famous now, these sort of emails that people are meant to send you, but how do you really decide to get an intuition of how to shape the market? Jensen Huang, Where to really double down?

[00:09:21] Chamath Palihapitiya: Jensen Huang, Where to maybe pull back? Jensen Huang, Where to actually go into a greenfield? Jensen Huang, How does that information get to you? Jensen Huang, How do you decide these things?

[00:09:27] Jensen Huang: Jensen Huang, In a final analysis, that's the job of the CEO. Jensen Huang, Yeah. Jensen Huang, And our job is to define the strategy, define the vision, define the strategy. Jensen Huang, We're informed, of course, by amazing computer scientists, amazing technologists, great people all over the company. Jensen Huang, But we have to shape that future. Jensen Huang, Well, part of it has to do with, is this something that's insanely hard to do? Jensen Huang, If it's not hard to do, we should back away from it. Jensen Huang, And the reason for that is if it's easy to do, obviously. Jensen Huang, Lots of competitors. Jensen Huang, A lot of competitors.

[00:09:54] Jensen Huang: Jensen Huang, Is this something that has never been done before that's insanely hard to do? Jensen Huang, And that somehow taps into the special superpowers of our company. Jensen Huang, And so I have to find this confluence of things that meets the standard. Jensen Huang, And in the end, we also know that a lot of pain and suffering is going to go into it. Jensen Huang, Yeah. Jensen Huang, There are no great things that are invented because it was just easy to do. And just like first try, here we are. Jensen Huang, And so if it's super hard to do, nobody's ever done it before.

[00:10:22] Jensen Huang: Jensen Huang, It's very likely that you're going to have a lot of pain and suffering. Jensen Huang, And so you better enjoy it.

[00:10:26] Chamath Palihapitiya: Jensen Huang, So can you just look at maybe three or four of the more long-tail things you announced? Jensen Huang, And just talk about the long-term viability of whether it's the data centers in space or whether it's what you're trying to do with ADAS in autos or what you're trying to do on the biology side. Jensen Huang, Just give us a sense of how you see some of these curves inflecting upwards in some of these longer tail business.

[00:10:46] Jensen Huang: Jensen Huang, Excellent. Jensen Huang, Physical AI, large category. Jensen Huang, We believe, and I just mentioned, we have three computing systems, all the software platforms on top of it. Jensen Huang, Physical AI as a large category. Jensen Huang, It's technology industry's first opportunity to address a $50 trillion industry that has largely been void of technology until now. Jensen Huang, And so we need to invent all of the technology necessary to do that.

[00:11:14] Jensen Huang: Jensen Huang, I felt that that was a 10-year journey. Jensen Huang, We started 10 years ago. Jensen Huang, We're seeing it inflecting now. Jensen Huang, It is a multi-billion dollar business for us. Jensen Huang, It's close to $10 billion a year now. Jensen Huang, And so it's a big business and it's growing exponentially. Jensen Huang, And so that's number one. Jensen Huang, I think in the case of digital biology, I think we are literally near the ChatGPT moment of digital biology. Jensen Huang, We're about to understand how to represent genes, proteins, cells. Jensen Huang, We all know how to understand chemicals.

[00:11:41] Jensen Huang: Jensen Huang, And so the ability for us to represent and understand the dynamics of the building of the building of the world. Jensen Huang, And so I think that if you find the building blocks of biology, that's a couple of, two, three, five years from now. Jensen Huang, In five years time, I completely believe that the healthcare industry, where digital biology is going to inflect. Jensen Huang, And so these are a couple of the really great ones, and you could see they're all around us.

[00:12:02] Jason Calacanis: Jensen Huang, Agriculture.

[00:12:04] Jensen Huang: Jensen Huang, No question.

[00:12:05] Jason Calacanis: Jensen Huang, I want to take you from the data center to the desktop. the company was built in large part on hobbyists, video gamers, and all those graphic cards in the beginning. And you mentioned in front of, I think, 10,000 people here, just clawed, open claw, clawed code, and what a revolution agents have become. And specifically, the hobbyists who are

[00:12:30] Jason Calacanis: really where a lot of energy, we see a lot of the innovation breaks, want desktops. You announced one here. I believe it's the Dell 6800. This is a very powerful workstation to run local models, 750 gigs of RAM. Obviously, the Mac studio sold out everywhere. In my company, we're moving to open claw everything. Freeberg just got claw pilled. You got claw pilled, I understand, and you're

[00:12:56] Jason Calacanis: obsessed with these. What is this from the streets movement of creating open source agents and using open source on the desktop mean to you? So great. Where is that going? Yeah, so great. First of all,

[00:13:08] Jensen Huang: let's take a step back. In the last two years, we saw basically three inflection points. The first one was generative. ChatGPT brought AI to the common everybody, to our awareness. But the fact of the matter is the technology sat in plain sight months before GPT. It wasn't until ChatGPT put a user interface around it, made it easy for us to use, that generative AI took off. Now, generative AI,

[00:13:37] Jensen Huang: as you know, generates tokens for internal consumption as well as external consumption. Internal consumption is thinking, which led to reasoning. 01 and 03 continued that wave of ChatGPT, grounded information, made AI not only answer questions, but answer questions in a more grounded way useful. We started seeing the revenues and the economic model of open AI start to inflect.

[00:14:04] Jensen Huang: Then the third one was only inside the industry that we saw, cloud code. The first agentic system that was very useful. Really revolutionary stuff. But cloud code was only available for enterprises. Most people outside never saw anything about cloud code until OpenClaw. OpenClaw basically put into the

[00:14:27] Jensen Huang: popular consciousness what an AI agent can do. That's the reason why OpenClaw is so important, from a cultural perspective. Now, the second reason why it's so important is that OpenClaw is open, but it formulates, it structures a type of computing model that is basically reinventing computer

[00:14:52] Jensen Huang: altogether. It has a memory system, it's a short-term memory file system. It has scales. Did you say skills or scales? Skills. Oh, skills. They do have scales, theoretically. Yeah. Skills. So the first thing, it has resources. It manages resources. It does scheduling. Yep. Right? And it cron jobs. It could spawn off agents. It could decompose a task and solve problems.

[00:15:22] Jensen Huang: It does scheduling. It has I-O subsystems. It could input. It has output. It can connect to WhatsApp. And also, it has a API that allows it to run multiple types of applications called skills. Yeah. These four elements fundamentally define a computer. Yeah. And therefore, what do we have? We have a personal artificial intelligence computer for the very first time. Open source.

[00:15:49] Jensen Huang: It's open source. It runs literally everywhere. And so this is now the, this is the, this is basically the blueprint, the operating system of modern computing. Yeah. And it's going to run literally everywhere. Now, of course, one of the things that we have to help it do is whenever you have agentic software, you have to make sure that an agentic software has access to sensitive information. It can execute code. It could communicate externally. We have to make sure that all of it has to be

[00:16:16] Jensen Huang: governed. All of it has to be secure and that we have policies that, that gives these agents two of the three things, but not all three things at the same time. And so the governance part of it, we contributed to Peter. Peter Steinberger was here. And, and so we've got a mound of great engineers working with him to help secure and keep that thing so that it could protect our privacy, protect

[00:16:37] David Friedberg: our security. Jensen, that paradigm shift makes some of the AI legislation that has passed around the country to regulate AI. And a lot of the proposed legislation effectively moot, doesn't it? Can you just comment for a second on how quickly the paradigm shift kind of obviates a lot of the models for regulatory oversight of AI, which is becoming a very hot topic in politics right now?

[00:16:59] Jensen Huang: Peter Steinberger, Well, this is, this is the part that, that we just with policymakers, we need to, we need to always get in front of them. And Brad, you do a great job doing this. We had to get in front of them and inform them about the state of the technology, what it is, what it is not. It is not a biological being. It is not alien. It is not conscious. It is computer

[00:17:24] Jensen Huang: software. And, and, and it is not something that we say things like we don't understand it at all. It is not true. We don't understand it all. We understand a lot of things about this technology. And, and so, so I think one, we have to make sure that we continue to inform the policymakers and not affect, not allow doomerism and extremism to affect how policymakers think and understand about this technology. However, however, we still have to recognize this technology is moving really fast

[00:17:54] Jensen Huang: and don't get policy ahead of the technology too quickly. And the risk that we, we run as a nation, our greatest source of national security concern with respect to AI is that other countries adopt this technology while we are so angry at it or afraid of it, or somehow paranoid of it, that our industries, our society don't take advantage of AI. And so I'm just mostly worried about the diffusion

[00:18:22] Chamath Palihapitiya: of AI here in the United States. Can you just double click if you were in the seat in the boardroom of Anthropic over that whole scuttlebutt with the department of war, it sort of builds on this idea of people didn't know what to think. It's sort of added to this layer of either resentment or fear or just general mistrust that people have sometimes at the software levels of AI. What would you, would, do you think you would have told Dario and that team to do maybe differently to try to change some of this outcome and some of this perception?

[00:18:51] Jensen Huang: The first thing that I would, I would say about Anthropic is first of all, the technology is incredible. We are a large consumer of Anthropic technology. Yeah. Really admire their focus on security, really admires their focus on safety. The, the, the, the, the culture by which they went about it, the, the technology excellence by which they went about it, really fantastic. I would say that, that the, the desire to warn

[00:19:17] Jensen Huang: people about the capability, the technology is, is also really terrific. We just have to make sure that we understand that the world has a spectrum and that, that warning is good. Scaring is less good.

[00:19:30.940 --> 00:19:31.500] Right.

[00:19:31] Jensen Huang: Um, and because this technology is too important to us. Right. And, and I think that it is fine to, uh, predict the future, but we need to be a little bit more circumspect. We need to have a little bit more humility that in fact, we can't completely predict the future and the ability. And to say things that, that are quite extreme, quite catastrophic, that there's no evidence of it happening. Um, could be more damaging than people think.

[00:20:01] Jensen Huang: And, and of course we are technology leaders. Uh, there were, there was a time when nobody listened to us. Um, but now because technology is so important in the social fabric, such an important industry, so important to national security, our words do matter. And I think we have to be much more circumspect. We have to be more moderate. We have to be more balanced. We have to be more, for more thoughtful.

[00:20:24] Brad Gerstner: Well, I, you know, I would nominate you. I think the industry has got to get together. 17% popularity of AI in the United States. I mean, we see what happened to nuclear, right? We basically shut down the entire nuclear industry. And now we have a hundred fission reactors being built in China and zero in the United States. Um, we hear about moratoriums on data centers. So I think we have to be a lot more proactive about that. But, but I want to go back to this agentic explosion that you're seeing inside your company, the efficiencies, the productivity gains.

[00:20:54] Brad Gerstner: Inside your company. There's a lot of debate whether or not we're seeing ROI, right? And you and I entering into this year, the big question was, are the revenues going to show up? Are the revenues going to scale like intelligence? And then we had this kind of Oppenheimer moment of five, $6 billion month by Anthropic in February. Um, do you think as you look ahead, you announced a trillion dollar, you know, visibility into a trillion dollars of just Blackwell and Vera Rubin over the course of the next couple of years.

[00:21:23] Brad Gerstner: When you see this happening at Anthropic and OpenAI, do you think we're on that curve now where we're going to see revenues scale in the way that intelligence is scaling?

[00:21:32] Jensen Huang: When you look around, when you, I'll answer this a couple of different ways. When you look around this audience, you will see that Anthropic and OpenAI is represented here. But in fact, every but 99% of everything that is here is all AI and it's not Anthropic and OpenAI. Right, right. And the reason for that is because AI is very diverse. I would say that the second most popular model as a category is open models.

[00:21:58] Jensen Huang: Number one is, yeah, open source. Open ways, open source. Open AI is number one. Open source is number two. Very distant third is Anthropic. And that tells you something about the scale of all of the AI companies that are here. And so it's important to recognize that. Let me come back and say a couple of things. One, when we went from generative to reasoning, the amount of computation we needed was about 100 times.

[00:22:26] Jensen Huang: When we went from reasoning to agentic, the computation is probably another 100 times. Now we're looking at, in just two years, computation went up by a fact 10,000x. Meanwhile, people pay for information, but people mostly pay for work. Talking to a chatbot and getting an answer is super great.

[00:22:54] Jensen Huang: Helping me do some research, unbelievable. But getting work done, I'll pay for. And so that's where we are. Agentic systems get work done. They're helping our software engineers get work done. And so then you take that, you got 10,000x more compute. You get probably, at this point, 100x more consumption now. Yeah. And we haven't even started scaling yet. We are absolutely at a millionx.

[00:23:20] Jason Calacanis: Which is, I think, a great place to talk about the number of engineers you have. 20, 30,000 at the company.

[00:23:26] Jensen Huang: We have 43,000 employees. I would say 38,000 are engineers.

[00:23:32] Jason Calacanis: The conversation we've had on the pod a number of times is, oh my God, look at the token usage in our companies. It is growing massively. And some people are asking, hey, when I join a company, how many tokens do I get? Because I want to be an effective employee. And you postulated, I believe, during your two and a half hour keynote, pretty long keynote. Well done. That you were spending.

[00:23:56] Jensen Huang: If it was well done, it would be shorter. Yeah.

[00:23:58] Jason Calacanis: You didn't have time to do. Yeah. You didn't have time to write it for an hour and 45.

[00:24:01] Jensen Huang: So you guys know there is no practice. Yeah. And so it's a gripping and ripping. Ripping and ripping. Yeah, yeah. Love it. So I just want to let you know I was writing the speech while I was giving the speech. Okay, so.

[00:24:13] Jason Calacanis: You never know. But does that mean if we do back in the envelope?

[00:24:17] Jensen Huang: I apologize.

[00:24:18] Jason Calacanis: Back in the envelope, man.

[00:24:19] Jensen Huang: Yeah.

[00:24:19] Jason Calacanis: 75,000 in tokens for each engineer or something like that. So are you spending in NVIDIA a billion, $2 billion on tokens for your engineering team right now?

[00:24:28] Jensen Huang: We're trying to. Let me give you the thought experiment. Let's say you have a software engineer or AI researcher and you pay them $500,000 a year. We do that all the time. Yeah. Okay. This is happening all of the time. That $500,000 engineer at the end of the year, I'm going to ask them how much did you spend in tokens? And that person said $5,000. I will go ape something else.

[00:24:50] David Sacks: Yes. Right.

[00:24:51] Jensen Huang: If that $500,000 engineer did not consume at least $250,000 worth of tokens, I am going to be deeply alarmed. Okay? And this is no different than one of our chip designers who says, guess what? I'm just going to use paper and pencil. I don't think I'm going to need any CAD tools. Right, right.

[00:25:11] Jason Calacanis: This is a real paradigm shift to start thinking about these all-star employees. It almost reminds me of what we learned in the NBA when LeBron James started spending a million dollars a year just on his health of his body and maintaining it.

[00:25:23] Jensen Huang: That's right.

[00:25:24] Jason Calacanis: Here he is at age 41 still playing. It really is, hey, if these are incredible knowledge workers, why wouldn't we give them superhuman abilities?

[00:25:33] Jensen Huang: That's exactly right.

[00:25:34] Jason Calacanis: Where does that go? If we extrapolate out two or three years from now, what is the efficiency of that all-star at an NVIDIA and what they're able to accomplish? What do they look like?

[00:25:44] Jensen Huang: Well, first of all, things that, wow, this is too hard. That thought is gone. This is going to take a long time. That thought is gone. We're going to need a lot of people. That thought is gone. This is no different than in the last Industrial Revolution. Somebody goes, boy, that building really looks heavy. Nobody says that. Wow, that mountain looks too big. Nobody says that.

[00:26:08] Jensen Huang: Everything that's too big, too heavy, takes too long, those ideas are all gone. You're reduced to creativity. That's right. What can you come up with? Exactly. Which means, now the question is, how do you work with these agents? Well, it's just a new way of doing computer programming. In the past, we code. In the future, we're going to write ideas, architectures, specifications. We're going to organize teams.

[00:26:34] Jensen Huang: We're going to help them define how to evaluate the definition of good versus bad. What does it look like when something is a great outcome? How to iterate with you? How to brainstorm? That's really what you're looking for. And I think that every engineer is going to have 100, 100 agents.

[00:26:51] Jason Calacanis: Back to the PR problem the industry has right now. You have executives like David Friedberg with Ohalo, who's looking at literally taking, through the use of technology, your technology and AI, the number of calories produced and making high quality calories. What is the factor you think you can bring the cost down, Freeberg? And what impact does this vision have for what you're doing?

[00:27:17] David Friedberg: Zero shot genomic modeling. And it works. Yeah. And you have that moment and you're like, holy shit. Honestly, like, and that's after people are replacing entire enterprise software stacks in a night. I did something in 90 minutes. I was telling the guys about, replaced the whole software stack and like a whole bunch of workload. 90 minutes on Claude ran this agentic system, built the whole thing, deployed it. And we got, we were all.

[00:27:41] Chamath Palihapitiya: On a Sunday night.

[00:27:41] David Friedberg: On a Sunday night, 10 p.m. I was done at 1130. I went to bed. As the CEO, you replaced. Yeah. And everyone on my management team had to do a similar exercise over the weekend. What we saw on Monday, I was like, it's over. But the technical stuff, the science stuff, we did something in 30 minutes using auto research. And I'd love your view on auto research and what that tells us about how far we still have to go in terms of efficiency. But using auto research and a chunk of data, something was published internally that we said, oh my God.

[00:28:11] David Friedberg: And that would normally be a PhD thesis that would take seven years. It would be one of the most celebrated PhD pieces we've ever seen in this field. And it would be in the journal of science. And it was done in 30 minutes on a desktop computer running on auto research with all the data we just ingested. We got it on Friday. We're like, hey, let's try it. Try it. Boot it up. Going to GitHub. Downloaded auto research and ran it. And you see everyone's face just go like, and then the potential of what this is unlocking for us is like the kind of thing that would take seven years. And it happened in 30 minutes.

[00:28:40] David Friedberg: And we're experiencing it in genomics. And we're like, this is unbelievable. So I think like the acceleration is widening the aperture for everyone in a way that like you didn't imagine a few years ago. But just going back to the auto research point, can you just comment on what you think about the fact that this thing got published with 600 lines of code? And the capacity that it has to run locally and achieve what it can achieve with all of these diverse data sets.

[00:29:06] David Friedberg: And what that tells us about the early stages we are in terms of optimization on algorithms and hardware.

[00:29:11] Jensen Huang: The fundamental reason why OpenClaw is so incredible, number one, is its confluence, its timing with the breakthroughs in large language model. Its timing was perfect. It was impeccable. Now, in a lot of ways, Peter wouldn't have come up with it probably if not for the fact that Claude and GPT and ChatGPT have reached a level that is really very good. It is also a new capability that allows these models to tool use.

[00:29:41] Jensen Huang: The tools that we've created over time, web browsers and Excel spreadsheets and, you know, in the case of chip design, Synopsys and Cadence and Omniverse and Blender and Autodesk. And all of these tools are going to continue to be used. There's some people say that the enterprise IT software industry is going to get destroyed. Let me give you the alternative view.

[00:30:08] Jensen Huang: The enterprise software industry is limited by butts and seats. It's about to get 100 times more agents banging on those tools. There are going to be agents banging on SQL. There are going to be agents banging on vector databases, agents banging on Blender, agents banging on Photoshop. And the reason for that is because those tools are, first of all, do a very good job. Second, those tools are the conduit between us.

[00:30:33] Jensen Huang: In the final analysis, when the work is done, it has to be represented back to me in a way that I can control. And I know how to control those tools. And so I need everything to be put back into Synopsys. I want everything to be put back into Cadence because that's how I control it. That's how I've ground truth.

[00:30:50] Chamath Palihapitiya: Let me ask you a question about open source. So we have these closed source models. They're excellent. We have these open weight models. Many of the Chinese models are incredible. Absolutely incredible. Two days ago, you may not have seen this because you were busy on stage, but there was a training run that happened in this crypto project called BitTensor. Subnet 3, they managed to train a 4 billion parameter LAMA model, totally distributed with a bunch of people contributing excess compute.

[00:31:19] Chamath Palihapitiya: But they were able to do it statefully and manage a training run, which I thought was like a pretty crazy technical accomplishment.

[00:31:26] Jensen Huang: Yeah.

[00:31:26] Chamath Palihapitiya: Because it's like random people and each person gets a little share.

[00:31:29] Jensen Huang: Our modern version of folding at home. Exactly. Yeah.

[00:31:32] Chamath Palihapitiya: So what do you think about the end state of open source? Do you see this decentralization of architecture as well and decentralization of compute to support open weights and a totally open source approach to making sure AI is broadly available to everybody?

[00:31:48] Jensen Huang: I believe we fundamentally need models as a first class product, proprietary product, as well as models as open source. These two things are not A or B. It's A and B. There's no question about it. And the reason for that is because models is a technology, not a product. Models is a technology, not a service.

[00:32:10] Jensen Huang: For the vast majority of consumers, the horizontal layer, the general intelligence, I would really, really love not to go fine tune my own. Right. I would really love to keep using ChatGPT. I love to use Cloud. I love to use Gemini. I love to use X. And they all have their own personalities, as you know, which just kind of depends on my mood and depends on what problem I'm trying to solve. You know, I might do it on X or I might do it on ChatGPT. And so that segment of the industry is thriving. It's going to be great.

[00:32:40] Jensen Huang: However, all these industries, their domain expertise, their specialization has to be channeled, has to be captured in a way that they can control. And that can only come from open models. The open model industry we're contributing tremendously to. It is near the frontier.

[00:33:00] Jensen Huang: And quite frankly, even if it reaches the frontier, I think that products as a service, world-class products as models as a product is going to continue to thrive.

[00:33:12] Jason Calacanis: Every startup we're investing in now is open source first and then going to the proprietary model.

[00:33:19] Jensen Huang: Yeah, and the beautiful thing is because you have a great router you connect it to, on first day, every single day, you're going to have access to the world's best model. And then it gives you time to cost reduce and fine tune and specialize. So you're going to have world-class capabilities out to shoot every single time.

[00:33:37] Brad Gerstner: Can I ask that? Of course. Nobody wants the U.S. to win the global AI race more than you, right? But a year ago, the Biden-era diffusion rule really was an anti-American diffusion of AI around the world. So here we are a year into the new administration. Give us a grade. Where are we in terms of global diffusion and the rate at which we're spreading U.S. AI technology around the world? Are we an A? Are we a B? Are we a C?

[00:34:07] Brad Gerstner: What's working? What's not working?

[00:34:09] Jensen Huang: Well, first of all, President Trump wants American industry to lead. He wants American technology industry to lead. He wants American technology industry to win. He wants us to spread American technology around the world. He wants the United States to be the wealthiest country in the world. He wants all of that. At the current moment as we speak, NVIDIA gave up a 95% market share in the second largest market in the world.

[00:34:38] Jensen Huang: And we're at 0%. China. That's right. President Trump wants us to get back in there. And the first thing is to get licensed for the companies that we're going to be able to sell to. We've got many companies who have requested for licenses. We've applied for licenses for them. And we've got approved licenses from Secretary Lutnik. Now, we've informed the Chinese companies, and many of them have given us purchase orders.

[00:35:07] Jensen Huang: And so we're in the process of cranking up our supply chain again to go ship. I think at the highest level, Brad, I think one of the things that we should acknowledge is this. Our national security is diminished when we don't have access to miniature motors, rare earth minerals. It's diminished when we don't control our telecommunications networks. It's diminished when we can't provide for sustainable energy for our country.

[00:35:37] Jensen Huang: It is fundamentally diminished. Every single one of these industries is an example of what I don't want the AI industry to be. When we look forward in time and we say, what do we want? What does it look like when American technology industry, American AI industry leads the world? We can all acknowledge that there is no way that AI models is won universally.

[00:36:04] Jensen Huang: We can all acknowledge that that is an outcome that makes no sense. However, we can all imagine that the American tech stack from chips to computing systems to the platforms are used broadly by the world where they build their own AI. They use public AI. They use private AI, whatever. And they can build their applications in their society. I would love that the American tech stack is 90% of the world. Yes. I would love that.

[00:36:34] Jensen Huang: The alternative, if it looks like solar, rare earth, magnets, motors, telecommunications, I consider that a very bad outcome for national security. Agreed.

[00:36:47] David Friedberg: How much are you monitoring the situation with the conflicts around the world right now? And how much does it worry you, Jensen? So China and Taiwan and then helium availability coming out of the Middle East, I understand, can be a supply chain risk to semiconductor manufacturing. How much do these situations worry you? How much are you spending on them?

[00:37:06] Jensen Huang: Well, first of all, I think in the Middle East, we have 6,000 families there. We have a lot of Iranians at NVIDIA and their families are still in Iran. And so we have a lot of families there. The first thing is they're quite anxious. They're quite concerned, quite scared. We're thinking about them all the time. We're monitoring and keeping an eye on them all the time. They have 100% of our support. I've been asked several times, are we still considering being in Israel? We are 100% in Israel.

[00:37:35] Jensen Huang: We are 100% behind the families there. We are 100% in the Middle East. I was also asked, given what's happening in the Middle East, is that an area where we believe that we can expand artificial intelligence too? I believe that there's a reason we went to war. And I believe at the end of the war, Middle East will be more stable than before. And so if we were there, if we're considering it before, we should absolutely be considering it after. And so I'm 100% in on that.

[00:38:04] Jensen Huang: With respect to Taiwan, we have to do three things. One, we have to make sure that we re-industrialize the United States as fast as we can. And whether it's the chip manufacturing plants, the computer manufacturing plants, or the AI factories. How are we doing on that? We're doing excellent. By gaining the strategic support, by gaining the friendship of the supply chain of Taiwan,

[00:38:32] Jensen Huang: by gaining their friendship, by gaining their support, we were able to build Arizona and Texas, California, at incredible rates. They are genuinely a strategic partner. We really, they deserve our support. They deserve our friendship. They deserve our generosity. And they're doing everything they can to accelerate the manufacturing process for us. And so I think that's number one.

[00:39:01] Jensen Huang: Number two, we ought to diversify the manufacturing supply chain. And whether it's South Korea, whether it's Japan, it's Europe, we ought to diversify the supply chain, make it more resilient. And number three, let's demonstrate restraint. And while we're reducing, increasing our diversity and resilience, let's not press, push. Unnecessary. Unnecessary. We need to be patient.

[00:39:30] David Friedberg: It's thoughtful. Is helium a problem? A lot of reports are helium.

[00:39:34] Jensen Huang: No, I think helium could be a problem. But it's also the case that the supply chain probably has a lot of buffer in it. These kind of things tend to have a lot of buffer. But, you know.

[00:39:45] Jason Calacanis: You've made massive progress in self-driving. You made a big announcement. You've added many more partners, including BYD. There was just a video of you driving around in a Mercedes. And a huge announcement with Uber that you're going to have a number of cars on the road from many different manufacturers.

[00:40:04] Jason Calacanis: Your bet is I believe that there's going to be an Android type open source platform that you're going to play a major part in with dozens of car providers. And then maybe on the other side, there could be an iOS with Tesla or Waymo. What's your strategy thinking there and how that chessboard emerges? Because it feels like you have a pretty deep stack. And in some ways, you're competing. And in other places, you're collaborative.

[00:40:34] Jensen Huang: Yeah. It's taking a step back. We believe that everything that moves will be autonomous completely or partly someday. Number one. Number two, we don't want to build self-driving cars, but we want to enable every car company in the world to build self-driving cars. And so we built all three computers. The training computer, the simulation computer, the evaluation computer, as well as the car computer. We developed the world's safest driving operating system.

[00:41:03] Jensen Huang: We also created the world's first reasoning autonomous vehicle so that it could decompose complicated scenarios into simpler scenarios that it knows how to navigate through, just like us, reasoning systems. And so that reasoning system called Alpamayo has enabled us to achieve incredible results. We open this. We vertical optimization. We horizontally innovate.

[00:41:31] Jensen Huang: And we let everybody decide, do you want to buy one computer from us? In the case of Elon and Tesla, they buy our training computers. Do they want to buy our training computer and our simulation computers? Or do you want to let us work with us to do all three and even put the car computer in your car? So we, you know, our attitude is we want to solve the problem. We're not the solution provider. And we're delighted however you work with us.

[00:41:57] Chamath Palihapitiya: Let me build on this question because I think it's like, it's so fascinating. You actually do create this platform. A thousand flowers are blooming. But it's also true that some of those flowers want to now go back down in the stack and try to compete with you a little bit. Google has TPU. Amazon has Inferentia and Tranium. You know, everybody's sort of spinning up their own version of I think I can out NVIDIA NVIDIA. Even though they also tend to be huge customers. How do you navigate that?

[00:42:25] Chamath Palihapitiya: And what do you think happens over time? And where do those things play in the complexion of this kind of vision?

[00:42:32] Jensen Huang: Yeah, really great. You know, first of all, we're the only AI company. We're an AI company. We build foundation models. We're at the frontier in many different domains. We build every single layer, every single stack. We're the only AI company in the world that works with every AI company in the world. They never show me what they're building. And I always show them exactly what I'm building. Right. Yeah. And so the confidence comes from this.

[00:42:57] Jensen Huang: One, we are delighted to compete on what is the best technology. And to the extent that we can continue to run fast, I believe that buying from NVIDIA still is one of the most economic things they could do. And there's just incredible confidence there. Number one, number two. We're the only architecture that could be in every cloud. And that gives us some fundamental advantages. We're the only architecture you could take from a cloud and put into on-prem, in the car, in any region. In space. That's right.

[00:43:27] Jensen Huang: In space. And so there's a whole part of our market, about 40% of our business. Most people don't realize this, 40% of our business, unless you have the CUDA stack, unless you can build an entire AI factory, the customers don't know what to do with you. They're not trying to build chips. They're not trying to buy chips. They're trying to build AI infrastructure. And so they want you to come in with the full stack. And we've got the whole stack. And so surprisingly, NVIDIA is gaining market share.

[00:43:55] Jensen Huang: If you look at where we are today, we're gaining share.

[00:43:57] Chamath Palihapitiya: Do you think what happens is these guys try and they realize, oh my God, it's too much. And then they come back. Is that why their share grows?

[00:44:04] Jensen Huang: Well, we're gaining share for several reasons. One, our velocity has gone. We help people realize it's not about building the chip. It's about building the system. And that system is really hard to build. And so their business with us is increasing. In the case of AWS, I think they just announced, I think it was yesterday, that they're going to buy a million chips in the next couple of years. I mean, that's a lot of chips from AWS. And that's on top of all the chips they've already bought.

[00:44:32] Jensen Huang: And so we're delighted to do that. But number one, we're gaining share this last couple of years because we now have Anthropic coming to NVIDIA. Meta SL is coming to NVIDIA. And the growth of open models is incredible. And that's all on NVIDIA. And so we're growing in share because of the number of models. We're also growing in share because all of these companies are outside the cloud.

[00:44:59] Jensen Huang: And they're growing regionally in enterprise, in industries, at the edge. And that entire segment of growth is really hard to do if it's just building an ASIC.

[00:45:09] Brad Gerstner: Brad? Related to that, and not to get in the weeds on the numbers, but analysts don't seem to believe. So if you look at the consensus forecast, you said compute could 1 million X. And yet they have you growing next year at 30%, the year after that at 20%. And in 2029, which is supposed to be a monster year, at 7%. Right? So if you take your TAM and you apply their growth numbers, it suggests that your share will plummet.

[00:45:39] Brad Gerstner: Do you see anything in your future order book that would make that correct?

[00:45:44] Jensen Huang: Yeah. First of all, they just don't understand the scale and the breadth of AI. Yes. Yeah. Yeah. I think that's true. Most people think that AI is in the top five hyperscalers. Right.

[00:45:55] David Friedberg: That's right.

[00:45:56] Chamath Palihapitiya: There's also an orthodoxy around these law of large numbers where they have to go back to their investment banking risk committee and show some model. They're not going to believe in their minds that $5 trillion goes to $15 trillion. It's so out of the bag. It can go to $7 trillion.

[00:46:12] Brad Gerstner: Or they just have a $10 trillion company. It's all just CYA stuff that I think ultimately... It's never happened before, so you can't say it will.

[00:46:17] Jensen Huang: And because you have to redefine what it is that you do. There was somebody who made an observation recently that NVIDIA, Jensen, how can you be larger than Intel in servers? And the reason for that is because the CPU market of the entire data center was about $25 billion a year. Right. We do $25 billion a year, as you guys know, in the time that we were sitting here.

[00:46:42] Jensen Huang: And so, obviously, obviously, that was a joke. No, but it's... All in podcast. It's roughly true. Don't worry.

[00:46:51] David Friedberg: Everything on this show is roughly true. Don't worry about it. It's all in. Wow. That was not guidance.

[00:46:58] Jensen Huang: But anyhow, the point is how big you can be depends on what is it that you make. Right. NVIDIA is not making chips. Number one, making chips does not help you solve the AI infrastructure problem anymore. It's too complicated. Number three, most people think that AI is narrowly in the things that they talk about and hear and see. It's AI is much... Open AI is incredible. They're going to be enormous. Anthropic is incredible. They're going to be enormous.

[00:47:27] Jensen Huang: But AI is going to be much, much bigger than that. And we address that segment.

[00:47:32] Chamath Palihapitiya: Tell us about data centers in space for a second. Yep. We're already in space. How should the layman think about what that business is versus when you hear about these big data center build-outs that's happening on the ground?

[00:47:46] Jensen Huang: Well, we should definitely work on the ground first because we're already here. And number one. Number two, we should prepare to be out in space. And obviously, there's a lot of energy in space. The challenge, of course, is that cooling, you can't take advantage of conduction and convection. And so you can only use radiation. And radiation requires very large surfaces. And so that's not an impossible thing to solve. And there's a lot of space in space. But nonetheless, the expense is still quite there.

[00:48:17] Jensen Huang: We're going to go explore it. We're already there. We're already radiation hardened. We have CUDA in satellites around the world. They're doing imaging, image processing, AI imaging. And that kind of stuff ought to be done in space instead of sending all the data back here and do imaging down here. We ought to just do imaging out in space. And so there's a lot of things that we ought to do in space. And in the meantime, we're going to explore what is the architecture of data centers look like in space. And it'll take years. It's okay.

[00:48:48] Jensen Huang: I got plenty of time.

[00:48:49] Jason Calacanis: I wanted to double click on healthcare. I know you've got a big effort there. We're all of a certain age where we're thinking about lifespan, healthspan. I mean, we all look great, I think. Some better than others. I think some better than others. I don't know what your secret is, Jensen. Pretty good. I mean, what are you taking? What's off the menu? You've got to talk to me when we're backstage. I want to know in the green room what you've got going on.

[00:49:11] Jensen Huang: Squats and push-ups and sit-ups. Okay.

[00:49:15] Jason Calacanis: But what you know in terms of the build-out in healthcare, where is that going? And what kind of progress are we making? I was just using Claude to do some analysis and saying, like, where are all these billing codes? We spend twice as much money in the U.S. We seem to get half as much. It seemed like 15% to 25% of the dollar spent were on these first GP visits.

[00:49:39] Jason Calacanis: And I think we all know, like, ChatGPT and a large language model does a better job more consistently today at a first visit. So what has to happen there to kind of break through all that regulation and have AI have a true impact on the healthcare system?

[00:49:55] Jensen Huang: There's several areas that we're involved in healthcare. One is AI physics or AI biology. Using AI to understand, represent, predict biology behavior, biological behavior. And so that's one. That's very important in drug discovery. There's second, which is AI agents. And that's where the assistance and helping diagnosis and things like that. Open evidence is a really good example.

[00:50:25] Jensen Huang: Hippocratics is a really good example. Love working with those companies. I really think that this is an area where agentic technology is going to revolutionize how we interact with doctors and how do we interact for healthcare. The third part that we're involved in is physical AI. The first one is AI physics, using AI to predict physics. The second one is physical AI. AI that understands the properties of the laws of physics. And that's used for robotic surgery. Huge amounts of activities there.

[00:50:54] Jensen Huang: Every single instrument, whether it's ultrasound or CT or whatever instrument we interact with in a hospital in the future will be agentic. Open claw in a safe version will be inside every single instrument. And so in a lot of ways, that instrument is going to be interacting with patients and nurses and doctors in a very unique way.

[00:51:13] Jason Calacanis: Yeah, I mean, we're seeing so much investment in AI weapons. It would be wonderful to see some investment in AI EMTs and paramedics and saving lives, not just taking them. Yeah. Which I think is a great segue into robotics. You've got dozens of partners. Yeah. We have this very weird, I don't know what I want to call a lost decade or 20 years of Boston Dynamics. Google bought a bunch of companies. They then wound up selling them and spinning them out where people just thought, robotics is just not ready for prime time.

[00:51:41] Jason Calacanis: And now here we have the world's greatest entrepreneur at this time, tied with you, Elon Musk. That was a good save, I hope. Optimus, pretty impressive. And then other companies in China. How close is that to actually being in our lives where we might see a chef, a robotic chef, a robotic nurse, a robotic housekeeper,

[00:52:05] Jason Calacanis: or, you know, this humanoid factor actually working in the real world, knowing what you know with those partners and the fidelity, especially in China where they seem to be doing as good a job as we're doing here, or maybe better?

[00:52:20] Jensen Huang: We invented the industry largely. America invented it. You could argue we got into it too soon.

[00:52:26] Chamath Palihapitiya: Yeah.

[00:52:26] Jensen Huang: And we got exhausted. We got tired about five years before the enabling technology appeared. Yes, the brain. Yeah, yeah. And we just got tired of it just a little too soon. Okay, that's number one. But it's here now. Now, the question is how much longer? From the point of high-functioning existence proof, high-functioning existence proof to reasonable products, technology never takes more than a couple, two, three cycles.

[00:52:57] Jensen Huang: And so a couple, two, three cycles would basically be somewhere around three years to five years. That's it. Three years to five years, we're going to have robots all over the place. I think China is formidable. And the reason for that is because their microelectronics, their motors, their rare earth, their magnets, which is foundational to robotics, they are the world's best. And so in a lot of ways, our robotics industry relies deeply on their ecosystem and their supply chain.

[00:53:26] Jensen Huang: And they're obviously moving very quickly. Our robotics industry will have to rely a lot on it. The world's robotics industry will have to rely a lot on it. And so I think you're going to see some fast, fast movements here.

[00:53:42] Jason Calacanis: Ultimately, one for one, Elon seems to think we're going to have one robot for every human. Seven billion for seven billion, eight billion for eight billion. Well, I'm hoping more.

[00:53:50] Jensen Huang: Yeah, I'm hoping more. Yeah. Well, first of all, there's a whole bunch of robots that are going to be in factories working around the clock. There's going to be a whole bunch of robots that don't move. They move a little bit. Almost everything will be robotic.

[00:54:04] David Friedberg: What does the world look like? Sorry, let me just say, I think this is one of the – robotics for me is one of the pieces that I think unlocks economic mobility opportunities for every individual. Everyone now – like when everyone got a car, they could now go and do a lot of different jobs. When everyone gets a robot, their robot can do a lot of work for them. They can stand up an Etsy store or a Shopify store. They can create anything they want with their robot. They could do things that they independently cannot do.

[00:54:30] David Friedberg: I think the robot is going to end up being the greatest unlock for prosperity for more people on Earth than we've ever seen with any technology before.

[00:54:38] Jensen Huang: Yeah, no doubt. I mean, just the simple math at the moment is we're millions of people short in labor today. Right. Yeah. Right? We're actually really desperate in need of robotics. And so that all of these companies could grow more if they had more labor. I mean, number one. Some of the things that you mentioned are super fun. I mean, because of robots, we'll have virtual presence.

[00:55:02] Jensen Huang: You know, I'll be able to go into the robot of my house and virtually operate it. I'm on a business trip. Right. Walk around the house. Walk the dog. Yeah, walk the dog. Break the leaves. Yeah, exactly. Break out the dog. Maybe not quite that, but just, you know, wander around and just see what's going on in the house. You know, chat with the dogs. Chat with the kids. Yeah. Time travel is also, we're going to be able to travel at the speed of light. You know?

[00:55:29] Jensen Huang: And so, you know, clearly we're going to send our robots ahead of us. Yeah. I'm not going to send myself. I'm going to send a robot. Right. Check it out. Yeah, yeah. And then I'm going to upload my AI.

[00:55:39] David Friedberg: Well, it's inevitable. It unlocks the moon and it unlocks Mars as targets for colonization, which gives us infinite resources. Getting back from the moon is effectively zero energy cost to move material back because you can use solar and accelerate. So you could have factories that make everything the world needs on the moon, and the robots are going to be the unlock for enabling that. Right.

[00:55:58] Jensen Huang: Distance no longer matters.

[00:56:00] David Friedberg: Distance doesn't matter.

[00:56:00] Brad Gerstner: Yeah. Yeah. The more revenue we get out of models and agents, the more we can invest in building the infrastructure, which then unlocks more capabilities on models and agents. And Dario on Dwarkesh's podcast recently said by 27, 28, we'll have hundreds of billions of dollars of revenue out of the model companies and the agent companies. And he forecasts a trillion dollars by 2030. Right. This is non-infrastructure AI revenue.

[00:56:26] Jensen Huang: I think he's being very conservative. I believe Dario and Anthropica is going to do way better than that. Wow. Way better than that. Wow.

[00:56:35] Jason Calacanis: So from 30 billion to a trillion.

[00:56:37] Jensen Huang: Yeah. And the reason for that is the one part that he hasn't considered is that I believe every single enterprise software company will also be a reseller, value-added reseller of Anthropics tokens. Value-added reseller of OpenAI. Have to be. That's right. Yeah. And they're going to, that part of their- Look at this logarithmic expansion. Yes. Yeah. Their go-to-market is going to expand tremendously this year.

[00:57:06] Chamath Palihapitiya: What do you think in that world is the moat? What's left over? I mean, you have some moats that are, frankly, I think, as this scales, almost insurmountable. The best one that nobody talks about is probably CUDA, which is just like an incredible strategic advantage. But in the future, if a model can be used to create something incredible, then the next spin of a model can be used to maybe disrupt it. Sort of in your mind, what do you think for these companies that are building at that application layer? What's their moat?

[00:57:35] Chamath Palihapitiya: Like, how do they differentiate themselves?

[00:57:37] Jensen Huang: Deep specialization. Deep specialization. I believe that these models, they're going to have general models that are connected into the software company's agentic system. Right. Many of those models are cloud models and proprietary models. But many of those models are specialized sub-agents that they've trained on their own-

[00:58:03] Chamath Palihapitiya: Right. So the call to arms for you, for entrepreneurs, is, look, know your vertical.

[00:58:07] Jensen Huang: That's right.

[00:58:08] Chamath Palihapitiya: Know it as deep and as better than everybody else. That's right. And then wait for these tools because they're catching up to you, and now you can imbue it with your knowledge. That's right.

[00:58:15] Jensen Huang: And the sooner you connect your agent, the sooner you connect your agent with customers, that flywheel is going to cause your agent to get hyper- It very much is an inversion of what we do today.

[00:58:26] Chamath Palihapitiya: Because today we build a piece of software and we say, what generalizes? And then let's try to sell it as broadly as possible and then sell the customization around it. And we trap you in the system.

[00:58:35] Jensen Huang: In fact, exactly right. We create a horizontal, but notice there are all these GSIs and all of these consultants who are specialists, who then take your horizontal platform and specializes it into. Exactly.

[00:58:50] Jason Calacanis: And that's arguably a five or six time bigger industry is the customization. It is. Absolutely. Yeah. That very much is.

[00:58:55] Jensen Huang: That's right. So I think that these platform companies have an opportunity to become that specialist, to become that vertical domain expert.

[00:59:04] Jason Calacanis: You know, I just want to give you your flowers. I think it was three years ago you said, you're not going to lose your job to AI. You're going to lose your job to somebody using AI. And here we are. The entire conversation has revolved around this concept of agents making people superhuman and the business opportunity expanding and entrepreneurship expanding. You actually saw it pretty clearly. That's right.

[00:59:24] David Friedberg: Have you changed your view? Well, I go. This is Doomer Dan. I'm not Doomer Dan. I do have. Doomer Dan.

[00:59:31] Jason Calacanis: No, you can hold space for, I think, two ideas. One is there are going to be a large. That's viral J. Calico. No, no.

[00:59:37] Jensen Huang: But that's just because he doesn't hang out with me enough.

[00:59:40] Jason Calacanis: I mean, we fog a little bit. Be careful when you're watching. He will show me your breakfast table. He'll follow you around.

[00:59:47] Jensen Huang: I'm not asking for it. I'm just saying. He'll follow you around.

[00:59:49] Jason Calacanis: I'm not asking for it. You can come with me and Tucker. We ski in Japan every January. Really? Love it. You and Tucker will go road trips. Wow. Okay. There is going to be job displacement. And then the question becomes, you know, do those people have the fortitude, the resolve to then go embrace these technologies? We're going to see 100% of driving go away by humans. That's just, that's a beautiful thing in the lives saved.

[01:00:14] Jason Calacanis: But we have to recognize that's 15 million people in the United States, 10 to 15 million who are employed in that way. And so that is going to happen. Yes?

[01:00:22] Jensen Huang: I think that jobs will change. For example, there are many chauffeurs today who drives the car. I believe that many of those chauffeurs will actually be in the car sitting behind the steering wheel while the car is driving by itself. And the reason for that is because remember what a chauffeur does. In the end, these chauffeurs, they're helping you. They're your assistants. They're helping you with your luggage. They're helping you. I mean, they're helping you with a lot of things.

[01:00:49] Jensen Huang: And so I wouldn't be surprised, actually, if the chauffeurs of the future become your mobility assistant and they are helping you do on a whole bunch of other stuff. Check into the hotel. Yeah. And the car is driving by itself.

[01:01:01] Brad Gerstner: The autopilot in planes created a lot more pilots and didn't take any of the pilots out of the cockpit. Yeah. Even though the autopilot is flying the plane 90% of the time.

[01:01:11] David Friedberg: And by the way, while that car is driving itself, that chauffeur is going to be doing a bunch of other work on his phone. And he's going to be making money doing other things.

[01:01:18] Jensen Huang: Arranging, for example. Doing other stuff. Coordinating a bunch of things for you. Yeah.

[01:01:21] David Friedberg: The pie just grows in a way that...

[01:01:24] Jensen Huang: One of the things that... Yes, every job will be transformed. Some jobs will be eliminated. However, we also know that many, many jobs will be created. The one thing that I will say to young people who are coming out of school who are anxious about AI, be the expert of using AI. Yes. Look, we all want our employees to be expert at using AI. And it's not trivial. Not trivial.

[01:01:52] Jensen Huang: And so knowing how to specify, not to overprescribe, leaving enough room for the AI to innovate and create while we guide it to the outcome we want. All of that requires artistry.

[01:02:07] Chamath Palihapitiya: You had this great advice to when you were at Stanford, I think it was, which is I wish to you pain and suffering. Do you remember that? Yeah. Fantastic. What's your advice to young people around what they should be studying? So if they're sort of about to leave high school, because now those are the kids that are at this like really native... They haven't made a decision about college, what to study, if at all, go to college. How do you guide those kids? What would you tell them?

[01:02:31] Jensen Huang: I still believe that deep science, deep math, language skills. You know, as you know, language is the programming language of AI. The ultimate programming language. And so as it turns out, it could be that the English major could be the most successful. And so I think I would just advise whatever education you get, just make sure that you're deeply, deeply expert in using AIs.

[01:02:59] Jensen Huang: One of the things that I wanted to say with respect to jobs, and I want everybody to hear it, that in fact, at the beginning of the deep learning revolution, one of the finest computer scientists in the world, I deeply, deeply respect, predicted that computer vision will completely eliminate radiologists. And that the one field he advises everybody to not go into is radiology.

[01:03:26] Jensen Huang: Ten years later, his prediction was at 100% right. Computer vision has been integrated into all of the radiology technologies and radiology platforms in the world 100%. The surprising outcome is the number of radiologists actually went up and the demand for radiologists is skyrocketed. The reason for that is because everybody's job has a purpose and its task.

[01:03:54] Jensen Huang: The task that you do is studying the scans. But your purpose is to help the doctors, help the patient diagnose disease. And so what's surprising is because the scans are now being done so quickly, they could do more scans, improving health care. Yes. But doing more scans more quickly allows patients to be onboarded a lot more quickly. Treated a lot more quickly. Yeah.

[01:04:22] Jensen Huang: And as it turns out, because hospitals enjoy making money too. Yeah. Right. They're doing more scans. Treating more patients. They're treating more customers and more patients. Early detection becomes... The revenues go up. And guess what? Perfect example. Yeah.

[01:04:35] Brad Gerstner: And a country that grows faster, productivity increases, a wealthier country can put more teachers in the classroom, not less teachers in the classroom. That's right. You just give every one of those teachers a personalized curriculum for every student in the room. It makes them all bionic and leads to a lot more.

[01:04:51] Jensen Huang: Every single student will be assisted by AI, but every single student will need great teachers. Yeah.

[01:04:57] Jason Calacanis: Amazing. Jensen, congratulations on all your success. And really, this is an incredibly positive, uplifting discussion. We really appreciate you taking the time for us. He is the steward we need. You are. You are the steward. I think you need to be more vocal. No, I'm being very, very honest.

[01:05:11] Chamath Palihapitiya: You're more vocal about the positive side of it. I think there's so much humorism. But I also think it takes the humility to have this level of success and be humble about, we're making software, guys. Yeah. And I think that that's actually really healthy for people to hear. We have done this before. We have invented categories and industries before. Yes. We don't need to go to this scaremongering place. It does nothing.

[01:05:33] Jason Calacanis: And we get to choose, right? We have autonomy and agency. We get to pick how to deploy this. Okay, everybody. We'll see you next time. Thank you. On the All In interview. Okay. Well done, brother. Thanks, man. Good job. Thank you, sir. Good job.

[01:05:48] Jensen Huang: That was awesome. Good, good. Appreciate you. You guys are awesome. Look at this. Look at this big crowd behind you guys. Man, I think they're here for you. Thank you.

[01:05:55.320 --> 01:05:55.640] Thank you.