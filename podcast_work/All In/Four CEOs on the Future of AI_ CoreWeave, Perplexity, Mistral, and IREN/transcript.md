[00:00:00] Jason Calacanis: I'm here at NVIDIA's annual GTC conference and I'm going to interview four amazing AI CEOs. Stick with us. I'm going all in. Our episode is sponsored by the New York Stock Exchange. Are you looking to change the world and raise capital? Do it at the NYSE.

[00:00:23] Jason Calacanis: The NYSE is a modern marketplace and a massive platform built for scale and long-term impact. So, if you're building for the future, the NYSE is where it happens. One of the great companies of the AI era is, of course, CoreWeave. They're building massive infrastructure for these hyperscalers. And in some ways, Michael Dell, welcome to the program.

[00:00:48] Jason Calacanis: You're the original hyperscaler. You guys got in very early and secured your, I don't know which GPUs you wound up getting. You were very early to this trend. How did you get to it so early? And how did you build out this first, I guess at the time, NeoCloud?

[00:01:07] Michael Intrator: Yeah. So, we didn't really start it as a NeoCloud. And I was running an algorithmic hedge fund focused on natural gas. And when you build an algorithmic hedge fund, once the algorithms are built, you're really just monitoring it and testing different theses and doing all that.

[00:01:27] Michael Intrator: But there's also a lot of downtime. And we got super interested in crypto. And, you know, we're pretty nerdy. We kind of dig under the hood. And we started to get interested in this security layer. We looked at Bitcoin and the mining for Bitcoin and we didn't like it. We just thought that, like, there's some brilliant engineer that built the ASIC and they're probably going to be better at running it than we are.

[00:01:49] Michael Intrator: So, we really began to focus on the GPUs, mostly because the GPUs were, you can mine Ethereum with them, but you could also do all these other things. And really, so right from the start, we looked at the compute as an option to be able to deploy our computing power to different use cases.

[00:02:10] Michael Intrator: And so, you know, began the company in 2017, you know, spent the first kind of three years mining crypto, went through a couple of crypto winters. Because we had come from a hedge fund, our, you know, we have real chops in risk management and how we think about capital and risk exposure and allocation and all of that. And so, we were really careful around that right from the start.

[00:02:36] Michael Intrator: So, we weathered crypto winter really well and began to scale the company and immediately started to look for other use cases that you could use this compute for because crypto was pretty volatile.

[00:02:48] Jason Calacanis: Yeah, and crypto was a question mark at that time. Absolutely. Yeah, I mean, Bitcoin was speculative and there were many other speculative projects. The only other people using this type of hardware, quants, medical, researchers.

[00:03:01] Michael Intrator: So, a good way to think about it is like the progression of products that we kind of started to work on. You know, first was crypto, but we immediately moved from crypto to CGI rendering. And we built projects that would allow folks that were trying to animate and render images, you know, kind of what makes the movies cool, right?

[00:03:23] Michael Intrator: And we started to work on that and then we moved to batch computing and started to look at medical research and different ways of using the compute to be able to drive science. And we just kind of kept moving up the stack in terms of complexity on how GPUs could be used. And ultimately, in like, call it like 2020, 2021, we started to really try to figure out how you can go ahead and use GPUs for neural networks.

[00:03:51] Michael Intrator: And that was not something that we knew how to do. And so, we actually went out and bought a bunch of A100s and donated them to a group that was working on Eleuther AI. They were working on an open source project with the thought that these guys are taking the GPU compute because we're donating it. They can't really get pissed at us if we're not very good at it initially. And that worked out really well because they can't complain about the SLA. They kept telling us, like, we need more of this.

[00:04:21] Michael Intrator: You got to work on this. And that began to really give us an understanding of what was necessary to run scale parallelized computing. And, you know, that we went through it. I kind of feel like buying those initial GPUs was the tuition we paid to learn how to run this business. And then one of the interesting things is all of those guys went back to their day jobs because they were all volunteers working on this. They were like-minded scientists.

[00:04:49] Michael Intrator: And when they got to their day jobs, they were all like, I want that infrastructure. It's built the right way. That's the way that researchers are going to want to use it. And that launched our business. It was an amazing story.

[00:05:00] Jason Calacanis: So, you went from crypto to these researchers into academia and deep research. What's the next card to turn over in the poker game?

[00:05:08] Michael Intrator: Yeah. So, what became very clear to us very, very early on was that the scaling laws were going to drive. And remember, this is really back in the, you know, 2020, 2021, before ChatGPT moment occurred. And we began to understand that, like, computing decommoditizes its scale, right? Like, when, you know, anybody can run a GPU, but can you run a cluster that's large enough to train a model that can change the world?

[00:05:37] Michael Intrator: And that's a different question. And so, we really began to think about, like, how do you go about scaling up your delivery of this computing to clients, larger and larger clients? And that was the next card to turn is to think about it from a, okay, you know, there's a component of this that is going to lean into our ability to access the capital to be able to deliver our solution to the broadest possible audience, to the most sophisticated consumers of this compute. Yeah.

[00:06:07] Michael Intrator: And that was really the next card is thinking about it as a business rather than as a engineering project to be able to deliver the infrastructure and the software. And really everything between, you know, when you're thinking about what we do, we kind of live above the NVIDIA GPUs, but below the models. Yeah.

[00:06:28] Michael Intrator: And everything in there, all the software, the integration of software and operations and observability and all the things that you need to be able to build a cloud that's purpose built for this one specific use case, right? So, we don't do everything. We really focus on one use case, which allows us to-

[00:06:46] Jason Calacanis: You want to do web servers. You got AWS.

[00:06:48] Michael Intrator: You know what? They do a great job. It's like, it's a great solution. It was a brilliant solution to solve a problem. We just looked at it and said, there's a new problem. And let's go about looking at this problem and try and come up with a solution to deliver compute that solves that problem.

[00:07:03] Jason Calacanis: And when did the language model start dialing and calling you for, you know, capacity?

[00:07:08] Michael Intrator: Yeah. So, our first, well, our first language model was really a Luther. Yes. But our first like large commercial was inflection. Ah, interesting. And so, you know, we worked with Mustafa and inflection.

[00:07:26] Michael Intrator: And then we really diversified from there into the hyperscalers, into, you know, open AI across the model, the foundation models across, you know, and just kept scaling and scaling with the belief that, you know, once again,

[00:07:45] Michael Intrator: the decommoditization of compute, the ability to deliver a solution, and the solution is building supercomputers that can change the world. And that's really what we began to focus on. That was the lead into training. And now the world has gone through, you know, this moment where we've moved from research into the productization of this.

[00:08:09] Michael Intrator: It's beginning to work its way in from the fringe of organizations into the core of what they do. And you can see that every day in the amount of inference compute that is being driven through, you know, our infrastructure layer, which is just massive, which is just like one of the massive layers.

[00:08:29] Jason Calacanis: And the inference shows your people are consuming it, not just building models, but they're deploying them and utilizing them.

[00:08:35] Michael Intrator: I always think of inference as the monetization of the investment in artificial intelligence. So when we see our compute being used to stand up the massive scale of inference that's hitting our compute every day, and like, you know, inference is when people ask the model a question, it comes back with an answer. That's an inference. Or when you ask the model a question and then to go do something, that's inference, right?

[00:09:02] Michael Intrator: And that's actually where you have the opportunity to really drive value outside of the model itself, but into the real world. And that's really exciting for us. That's what we like to watch. That's what I like to watch in terms of gauging the health. What chips are those?

[00:09:19] Michael Intrator: So really, you know, we are the tip of the spear in bringing the new architecture out of NVIDIA into commercial production at scale. Yeah. And so when, you know, we were the first ones to bring the H100s at scale, we were the first ones to bring the H200s at scale, first ones with the GB200s. And now you've got the GB300s.

[00:09:47] Michael Intrator: And one of the things that's amazing and really fascinating for us is, you know, people are using the bleeding edge GPUs to train models as the new architectures come out. And then they take those GPUs and they move them into different experiments. And then over time, they move them into inference and they continue to use them in inference for a very, very long time.

[00:10:11] Jason Calacanis: What is the shelf life of a 100 right now? Yeah. That's been a big debate is, I think, for your company, for Microsoft, and I guess Michael Burry, you know, who you must have known when you were a quant, you know, saying, oh, my God, the whole industry is the sky's falling. And then we all know in the industry that people don't just throw this hardware away, that they find uses for it. The street finds its own use for technology. So what's the reality of the lifespan of these things?

[00:10:36] Michael Intrator: So my take on the GPU depreciation debate is that it's nonsense, right? It's a debate that is being brought to the forefront by some traders that have a short position in the stock and they're trying to talk down. Look, here's what we know, right? Right. When we buy infrastructure, we're a success based company, right? We're a small company on a relative basis compared to the enormous companies that we're competing with.

[00:11:05] Michael Intrator: And so they come our clients come into us and they buy compute for five years, for six years. Our average contract is five years. So any commentary by anyone either inside or outside of the industry that this stuff becomes obsolete in 16 months or whatever nonsense they're spewing, it doesn't in any way match up with the facts on the ground. The facts on the ground is they're buying it for five years.

[00:11:30] Michael Intrator: Right. And my approach to this has always been if people are willing to pay me for it, it still has value. Correct. Pretty simple way of approaching it. We use a six year depreciation. We believe that the GPUs will last in excess of six years. But we felt like that was a fair and reasonable approach to a technology cycle that's moving at this velocity. The A100s, the amperes this year, the price has appreciated through the year. Why is that?

[00:11:58] Michael Intrator: I think it's because one of the things that happens is as more installed capacity becomes available, you have new companies that come into existence that have new use cases that have different size models that are trying to build new commercial ventures that maybe have been blocked out of the A100s. Yeah. And never had an opportunity to run on that.

[00:12:20] Jason Calacanis: I mean, to make a very simple example for the audience, like when you trade in your iPhone after three or four years, you're like, who's going to use an iPhone 12? And it's like, have you been to South America or Africa where you go to the store and you buy an iPhone 12 or you buy the Pixel 7 and it costs $50? That's still got great life left in it. Absolutely. Yeah. You know.

[00:12:43] Michael Intrator: And so, look, you know, we find these amazing use cases, new companies that have come into existence or existing companies that have integrated new models into their workflow that are able to use the amperes. And so they keep buying any GPUs that we have available. And once again, you know, the concept that a GPU is no longer relevant or commercially viable after 16 more, 18 months or two years. Yeah, that's farcical. It just doesn't make any sense.

[00:13:12] Jason Calacanis: I think sometimes people get caught up in Moore's law or in just how fast our industry is growing. Yeah. And that there's so much at stake that big companies are demanding the most recent products. That doesn't mean that the lifespan has gotten shorter. It means the opportunity and the surface area of the opportunity has gotten much larger.

[00:13:33] Michael Intrator: Yeah. One of the things is, is like, you know, the industry has gotten so much attention for the unprecedented scale of capital that is coming to bear on this. Yeah. And because of that, there tends to be a incredible focus on the companies that are building on these most advanced chipsets.

[00:13:58] Michael Intrator: And the truth of the matter is, is, you know, even within those companies, they have a long tail of useful life to provide inference horsepower, to work on other experiments, to do less bleeding edge activity, but still needs to be done.

[00:14:14] Jason Calacanis: And yeah, I mean, rendering comes to mind as well. Or yeah, we're making images on Nano Banana. Like there will be a use for it. There is a moment in time where maybe the compute to power ratio doesn't make sense.

[00:14:26] Michael Intrator: My expectation is, is obsolescence will be defined by the moment in time where the power in the data center for me will be able to be repurposed for a higher margin than the existing infrastructure provides. And, you know, like I said, I fully expect this infrastructure to last in excess of six years.

[00:14:52] Michael Intrator: But the standard in the space has really been used with one exception, which is Amazon, which is, yeah, it's six years. That seems like the right schedule. I'm not making it up. That's what everybody's using.

[00:15:05] Jason Calacanis: Yeah. And the energy cost is the opportunity because, hey, it's just, we need that space. There's a better reward here. And that might get resold, that hardware to somebody else who wants it, a hobbyist or something. It's available.

[00:15:21] Michael Intrator: Or it could be sent someplace else where they have more capacity when they can repurpose it there. But I kind of feel like, you know, we'll deal with that part of the business when we get there. What I know right now is it is extraordinarily profitable. It's very creative to my company to continue to keep the infrastructure that's been up and running, that's been on these long-term contracts.

[00:15:43] Michael Intrator: And as it rolls off, as it's been in use for five years, you know, as it becomes available, I am still able to sell it at a higher price than it was at a year ago.

[00:15:52] Jason Calacanis: There's competition now. When you were buying these from Jensen back in the day, yeah, you could buy them and have them shipped, I would assume, within 30 days or less. Nowadays, what's the wait like even for you, a loyal old customer? And is there a bit of a battle? Is there politics to who gets the servers? Like, you see some, like, very big names talking about they got to get an allocation. Is it still a little bit crazy? What's it like to be in that category, having to buy something everybody wants?

[00:16:22] Michael Intrator: Look, you know, I think of it as an affirmation of the business that we're in, right? Like, the fact that we are attracting competitors means that the business is healthy and there's a lot of people trying to deliver this service because the need for this infrastructure, the need to integrate the infrastructure, you know, into the software layers to deliver it to artificial intelligence,

[00:16:46] Michael Intrator: either at the model level or the inference level or the application level or whatever, you know, level of the five-layer cake that Jensen's, you know, focused on. The fact that there are more people coming into this, it doesn't discourage me. Yeah. As far as getting access to the GPUs, we show up like everybody else with a, you know, we'd like to buy, here's a PO and we're ready to pay.

[00:17:08] Jason Calacanis: The one, what's the wait time like and is it just really competitive or not? Because I talked to Jensen about it. He said, I said, how do you manage all these like big egos and names and companies trying to buy stuff? And he said, well, they order it and we give it to them in the order in which they order it. Is it really like that?

[00:17:27] Michael Intrator: It really is, right? Like, you know, he doesn't want to be in the position of playing favorites or allies. Like that just seems like a bad place to be with your clients. Or auctioning them off. Yeah. So, yeah, that would, that, that. That'd be crazy. Yeah. I don't, I'm not sure that would be good for the long-term business. No. Yeah. So, so our, our, our approach is.

[00:17:49] Jason Calacanis: You might get some sovereigns coming in and saying, I'll pay double. Yeah. They do that with Ferraris too sometimes. I guess these are the Ferraris of computing, right? In a way they are.

[00:17:57] SPEAKER_06: Yeah.

[00:17:57] Jason Calacanis: But I mean.

[00:17:58] Michael Intrator: Bugattis. Our, our approach is to work with clients across the entire space to find opportunities that are really interesting companies that can fit into our contraction, contracting requirements the way we're going to be able to go out and structure the debt that we require in order to go out and, and build infrastructure at this scale. And.

[00:18:21] Jason Calacanis: How does all that debt work? That is something that you guys specialize in. And corporate debt, I'm in the venture business. People are like, why should I be in venture when corporate debt pays so well? Corporate paper is so huge. I'm curious how this fits in and like what interest rate people are paying on, you know, a billion dollars in infrastructure. What do they pay on that?

[00:18:44] Michael Intrator: Yeah. So, so CoreWeave has really been the innovator around a lot of the financing engines that have come to bear on this. We did the first GPU based loans. And like, I think it's important, or I'm going to try to explain this in a way people can understand. So what we do is we go out and we find a client. Let's use Microsoft. You brought them up before. Right. And Microsoft comes to us and says, we'd like to buy some compute for you. And we say, okay, great.

[00:19:14] Michael Intrator: We're going to sign a contract. Once I have a contract in hand, then what I do is I create something. It's not a particularly creative name. It's called the box. Yeah. Right. And what I do with the box is I take my contract with Microsoft and I put it in the box. I go to Jensen and I buy the GPUs. I put it in the box. I take my data center contract. I put it in the box. And now the box governs cash flow. And it has a waterfall of cash flow that comes into it and goes out of it.

[00:19:41] Michael Intrator: And so the way it works is then I build the compute and then I deliver the compute to Microsoft and they pay the box. They don't pay me. Right. It goes into the box. And the first thing it does is it pays the data center. It pays the power bill. It pays the interest and the principal. And then whatever's left flows back to us. Right.

[00:20:02] Michael Intrator: And so it is an incredibly well structured, time tested, pressure tested vehicle to be able to borrow money against client paper and all of the other collateral around the deal. Which is why CoreWeave, which is a company that many people haven't ever heard of, was able to go out and raise $35 billion in 18 months to build infrastructure at scale.

[00:20:27] Michael Intrator: But what's important to understand is the economics in this box are such that within two and a half years of a five year deal, we have paid for everything. The principal has been paid off. The principal has been paid off. The interest has been paid off.

[00:20:43] Michael Intrator: The return into the box is such that we are able to generate returns to our company at the box level, which gives the most sophisticated lenders in the world, whether it's banks or private equity funds or whoever, confidence that they're going to be able to achieve the one rule of lending, which is give me my money back.

[00:21:10] Jason Calacanis: Yes. And so it's better when that happens.

[00:21:11] Michael Intrator: So they look at this box and they're like, wow, we're really confident we're going to get our money. And maybe they want 10 boxes. That's correct.

[00:21:18] Jason Calacanis: And if any one box goes upside down, you can deal with it and it's not as acute.

[00:21:25] Michael Intrator: That's correct. And they don't cross pollinate. They don't cause a contagion across the boxes. They're all independent and discreet. One. And number two is as you do this and as you show the lenders how this financing tool and how this financing mechanism works, what they do is they continue to lend you money at progressively lower rates.

[00:21:48] Michael Intrator: And so when you think about our cost of capital over the last two years, we have dropped our cost of capital by 600 basis points. Wow. It is enormous. Right. And so you're seeing a company that is driving its cost of capital down towards where the hyperscalers borrow, which will enable us to be able to be competitive with them over time.

[00:22:12] Michael Intrator: And we have been extremely militant and diligent about feeding, watering and caring for those boxes so that we continue to have access to the capital markets in a way that allows us to build and drive our business.

[00:22:26] Jason Calacanis: It means you have to say no to maybe some people who want to be in the box.

[00:22:30] Michael Intrator: Yeah. Some customers. We look at some deals and we're just like, you know, they want to buy GPUs for a year. And I look at it and say, that's not a deal that I can do because it's too short for me to amortize the expenses. And so I won't do that. Right. Like once again.

[00:22:46] Jason Calacanis: And they can go to another provider who maybe wants to take that risk on who has extra capacity.

[00:22:49] Michael Intrator: Absolutely. But our business is really built about around the risk management of being able to get to scale. Because in my mind, during this period of disequilibrium, during this period where there were not enough GPUs in the world to provide the compute for all of the different use cases in artificial intelligence,

[00:23:10] Michael Intrator: the part that's important for me and for my company is to get enormously large so we can drive down our cost of capital so that we have information flow coming in from all different parts of the market. The large language models, high speed trading, search, all of these things. And they're feeding information back into us that is letting us know what the next product we need to build is or where, you know, they need help scaling or what type of compute they need.

[00:23:39] Michael Intrator: And all of that information flow is incredibly valuable to us.

[00:23:43] Jason Calacanis: What can you tell us about demand? There's been reports of, hey, maybe the Oracle Starbase thing with open AI has been downsized or maybe not. And then, you know, other folks, Microsoft is going big and Google is going big. Meta is going big. And those people obviously have massive cash flow. Apple seems to be MIA. They don't seem to want to play.

[00:24:07] Michael Intrator: You've named a lot of really big companies with really big balance sheets that have the capacity to drive a lot of demand. Look, I have been truly steadfast in this for years now. For four years, the depth of the demand for the service we provide has been relentless

[00:24:26] Michael Intrator: and overwhelms the global capacity of the world to deliver enough compute to enable all of the demand for artificial intelligence to be stated. And that has been we have been relentless about that.

[00:24:42] Jason Calacanis: We have like Nick's tickets during the Patrick Ewing era. Yeah. Like they got up to 50,000 people on the wait list. So if magically the wait list went away, if the constraint went away and we just had a large amount of GPUs available, a lot of energy available, a lot of data center available, how much capacity would just all of a sudden come out of the system?

[00:25:05] Michael Intrator: So would be deployed, I should say. So remember how we build our business through this box. And it's a five year box. So if we had an air pocket, if demand were suddenly to disappear because of a technology breakthrough, because of a war, anything, right? Like the why from a risk management perspective does not matter. You have to prepare your company for the what happens if it happens.

[00:25:32] Michael Intrator: And so by entering into these long term contracts and entering into contracts with counterparties that have large balance sheets, you are or we are protecting ourselves and our lenders so that we are confident and they are confident because you can see how confident they are by the rate that they're charging us continuing to decline, that they're ultimately going to get their money back. And that is the one rule of lending. And so, you know, if-

[00:26:02] Jason Calacanis: But just in terms of the capacity, if you were unconstrained and NVIDIA Jensen says, hey, order as many as you want, what would happen?

[00:26:09] Michael Intrator: So it's also important to understand the constraints aren't just GPUs. Right. Electricity. It's powered shells. It's memory. It's storage. It's networking. It's optics. All of the things. And there's various throttles that will limit the-

[00:26:27] Jason Calacanis: Memory is a throttle right now, right?

[00:26:28] Michael Intrator: Oh, yeah, it is. Oh, yeah, it is.

[00:26:30] Jason Calacanis: How did memory become the throttle?

[00:26:32] Michael Intrator: If memory and- It has historically been a cyclical business, right? We have seen these waves of demand driving up the cost for memory and then it collapses and then it drives it up. It's a very boom and bust business. It's cyclical in its nature because the fabs are so capital intensive that people invest

[00:26:55] Michael Intrator: in the fabs, build a ton of capacity and then overbuild if there's any type of turn down. And we've seen that cycle again and again. What's happening right now is the confluence of two things, right? One is with all the demand for artificial intelligence and the corresponding demand for compute and the ancillary services around the GPU, the demand is through the roof. That's number one.

[00:27:23] Michael Intrator: Number two is that there was probably an investment cycle that needed to happen back in 2023 that would have brought on the necessary fab capacity to be able to serve- Impossible to predict what just happened.

[00:27:37] Jason Calacanis: Just with energy, it's impossible to predict what just happened. And now people are chasing energy. The data centers are going where the energy is. It's not based on real estate. That's correct.

[00:27:46] Michael Intrator: It's based on where is there some wind? And anytime you have a very cap- Not every, anytime, but many times when you have a capital intensive business like building fabs, you will get this boom and bust cycle, just like in energy. They overbuild. Yeah. And then, you know- Fiber. Yeah. I mean, there's a lot of examples of that. Our approach-

[00:28:09] Jason Calacanis: Some ways, when you look at that, it's a beautiful aspect of capitalism that we're able to have a boom-bust cycle, that we're able to weather it, right? If you think just like capitalism from first principles, something like that happens and we have too much fiber, it creates an opportunity for Google to buy it all up or the next person.

[00:28:27] Michael Intrator: Listen, it does a lot of things having a boom-bust cycle. It clears out the underbrush. Yeah. The strongest companies will be able to survive and take advantage of that. And it sows the seeds of future business. The other thing that it does is you put that infrastructure into the ground. You put the fiber into the ground, which became the backbone of how we watch movies every

[00:28:52] Michael Intrator: day and how we communicate and how we hop on a Zoom and COVID and all of these things were based on that infrastructure that was available to be consumed. Yeah.

[00:29:03] Jason Calacanis: People don't recognize this fact. If you- the premise of YouTube from the founders who I knew, Chad Hurley and his other partner, they basically had the realization, at this curve, storage is coming down so quickly, we could offer free unlimited uploads. And bandwidth is coming down. So I guess we don't have to charge people for sharing a video online. Before that, if your video went viral, people are going to have their minds blown.

[00:29:31] Jason Calacanis: But your server would turn off and it would say, this person needs to pay their bill. Yes. Because they were getting charged for carriage by the Megavit going out.

[00:29:40] Michael Intrator: Yes. I mean, look, and the business models change and evolve. And like you said, Moore's Law, and certainly Jensen will talk about the fact that what is going on within the accelerated compute, say, dwarfs Moore's Law, right? And all of that is going to lead to more opportunity to build more companies that are going to do things like YouTube did, which has really changed the world.

[00:30:09] Jason Calacanis: Yeah. I mean, the concept that, I don't know if it was like a million hours being uploaded every hour or minute, but at some point, Susan Wojcicki, rest in peace, had told me just like how much was being uploaded every minute. And it made no logical sense until you realized, well, there's 3 billion people, 2 or 3 billion people in the service and 1% upload or 0.1, 10 bips upload. It's like, okay, one in a thousand people upload.

[00:30:38] Jason Calacanis: It's a big denominator.

[00:30:40] Michael Intrator: I was sitting on a panel with Sarah Fryer, CFO of OpenAI. And every once in a while, she really puts out interesting information. And so she was talking about the cost of a million tokens when ChatGP3 came out. And it was $32 and change. And now a million tokens cost $0.09. Yeah. Right.

[00:31:08] Michael Intrator: And so you just see like the incredible power of how the capital markets, how capitalism is fueling engineering and fueling competition. And it's become recursive now too.

[00:31:24] Jason Calacanis: I mean, these models, if you say to the model, hey, make yourself more efficient, spend less money and lower the cost of tokens. It'd be like, okay, captain. Yeah. I don't know if you saw Carpathi's recursive thing last weekend, but it's like now civilians who've never worked in a language model done computer science are like, I'm going to try to do something recursive this weekend.

[00:31:43] Michael Intrator: You know, it's one of the things that I talked to the other founders about, you know, and it's like when you think about some of the things that AI does, right, it's lowering the barrier to operations. So if you have a good idea or a great idea, you can open up your model and you can tell

[00:32:10] Michael Intrator: your model, you can vibe code it, you can do all kinds of different things and create things that never existed before. That's amazing, right? Like that's bringing down this incredible barrier that kept human creativity contained. And now all of a sudden this whole new vector of, you know, medical research or different approaches to, you know, baseball cards or whatever you want. If you've got a great idea, if you've got a new creative idea, that's the valuable kernel

[00:32:37] Michael Intrator: right now that allows you to build new things and to create new things. And I just think that's incredibly exciting. Like you're bringing the minds of 8 billion people, a tool that allows them to overcome what was insurmountable for forever.

[00:32:53] Jason Calacanis: For humanity.

[00:32:54] Michael Intrator: Yeah.

[00:32:54] Jason Calacanis: It's a bright new future, Michael. Appreciate you sharing the information with us and the vision. I am really delighted to have Aravind Srinivas on the program. Thank you for having me here, Jason. It's so great. I want to go through three stages in which I fell in love with your product. The first phase was I could go in, pick my language model if I wanted to use OpenAI, if I wanted to use Claude, whatever it was. That was like a real unlock for me.

[00:33:24] Jason Calacanis: And on the sidebar, I noticed you had done essentially like what Yahoo did in the early days. Finance. Sports. Sports. And when I pulled my Nick game up, it gave me a live version of that. When I pulled my stocks up, it summarized the news in real time. And I was like, wow, this execution is great. And I kind of made you my front door to different models and it made it easier to check it. Then you came out with the Comet browser.

[00:33:52] Jason Calacanis: And I was like, holy cow, I can give this a series of instructions. Go to my LinkedIn, find everybody from this company, put them into a Google sheet and boom, you were the first out of the gate with that. And then just the last couple of weeks, I had been claw pilled and using OpenClaw, but you came out with computer and I started using computer. And boy, it's good. It's a really strong start allowing me to do repetitive tasks, very similar in some ways

[00:34:21] Jason Calacanis: to co-work from Claude or basically an engineer or developer using it. So are these the evolution of the company? And I should think about it that way. But how do you look at perplexity now? You have a very loyal fan base. You're making a lot of money. I don't know if you disclose it, but I think it's hundreds of millions to billions. You can tell us. But what is perplexity in the face of, wow, Claude's having a great run. OpenAI still doing strong. Grok doing very well.

[00:34:50] Jason Calacanis: Gemini coming on strong. There's like six or seven of you. And you just happen to be one of my top twos right now. Thank you.

[00:34:57] Aravind Srinivas: So tell me. First of all, thank you. Thank you so much. Perplexity has always been built for people who are always looking for the extra edge, the curious people. So it's very natural that you are one of our flower users. One common theme for us for the last three and a half years is accuracy. Perplexity wants to be the company that's building the most accurate AI. So when you want to give somebody answers, accuracy is very essential for building trust.

[00:35:27] Aravind Srinivas: Because only then the user is going to ask the next set of questions. It turns out it was a great idea to give AI access to the internet to be accurate. So that's the perplexity ask product. It turns out it's a great idea for AI to have full access to a browser so that it can be accurate when you task it to go do something that you would do yourself on a browser. Agenic browsing. Comet. Comet. Now, the last phase is it turns out it's a great idea for AI to be given a full access

[00:35:55] Aravind Srinivas: to a computer so that it can do whatever you do on a computer on its own. Essentially becoming the computer itself. An orchestra of everything AI can do today. Every single capability each individual AI model has. Be it GPT or Cloud or Gemini or anything else. An orchestra of all those capabilities. That's what perplexity computer is. And all these sub-agents that are running inside computer are the musicians.

[00:36:25] Aravind Srinivas: The models are essentially the instruments. And there are like hundreds of models out there, each having their own specialization. Some are good at coding. Some are good at writing. Some are good at multimodal, visual synthesis, image generation, video generation, audio. But what matters is the end output, the music you play. That's the work AI gets done for you. And that's what perplexity computer is. The AI itself is the computer now.

[00:36:50] Jason Calacanis: Still lives inside of a browser. Have you considered giving it desktop root access? Yes. That feels like the next place this is going. But that comes with a lot of security issues, a lot of trust issues. As you mentioned, trust is paramount. Getting the right answer is what builds it. But also not getting hacked and not having it delete your files. So how do you think about root access to my Windows machine? Obviously, iOS, they won't let you. But with an Android phone, it would let you. Yes. So do you have that in the works?

[00:37:20] Aravind Srinivas: Yes. So we announced something called personal computer. Perplexity personal computer. That's essentially going to take all the trust and reliability and the server side execution of perplexity computer, but synchronize it with your local computer so that you can use it from your phone. And we're going to do this with the Mac Mini, where you synchronize your computer with the Mac Mini. So that becomes your local server.

[00:37:44] Aravind Srinivas: All the agent orchestration that has to do with your local private data will run on that local orchestration loop, that runtime with the Mac Mini. Not on your servers, not on Impropics. Exactly.

[00:37:55] SPEAKER_06: Yeah.

[00:37:56] Aravind Srinivas: It could still ping Frontier Models if it needs to, with your permission. But it will be orchestrating everything on your local hardware. Yeah. And if it needs to run on the server side hardware, if you don't want very complicated, long running stats to be running on your local hardware, you can delegate it to run on your server side computer, which is, again, only accessible to you and you alone.

[00:38:20] Aravind Srinivas: So that way we're going to bring this perfect hybrid of trustworthy hybrid between local and server side.

[00:38:29] Jason Calacanis: And you'll make it easy to do it. Just be abstracted.

[00:38:31] Aravind Srinivas: You install one executable. Boom. It's done. It's like open claw for dummies. Right. Nobody needs to learn how to use it. Nobody needs to manage API keys. Nobody needs to manage separate billing across like 100 different services, figure out what you can give access to and not access to. So we take care of that. So it's a Steve Jobs way of doing it, you know, end-to-end integration.

[00:38:50] Jason Calacanis: And how do you think about local models? I have started running Kimi 2.5 on a Mac Studio. It's not as good as Claude or Gemini or Grok. But you can probably do about 80% there for free. Yeah. Essentially.

[00:39:06] SPEAKER_03: Yeah.

[00:39:06] Jason Calacanis: And so that's quite compelling considering some of my other bills, Claude, and stuff were getting expensive. So do you have one of those? You started testing on your local Mac Studio. I assume you have a Mac Studio and you're doing this yourself? Yeah. Or now, I don't know if you saw Dell and NVIDIA announced a giant workstation. Yeah. Is it a 3,800? Something like that. Something like that. Yeah. With 750 gigs of RAM.

[00:39:31] Jason Calacanis: So what do you think about the desktop going back to workstation slash server status?

[00:39:38] Aravind Srinivas: I think it's very promising. My prediction is to initially start off as a sub-agent. So whatever you need to go, like your tax returns, your personal photos, your emails, your calendar, all that stuff, those local apps, personal notes, very personal notes. You can make sure that the models that access those tokens will be running on your local hardware if you want to, if you're that privacy conscious.

[00:40:09] Aravind Srinivas: And more complicated stuff that accesses your data that's already on the server side. For example, your Google Calendar, your Gmail. This is personal data still. But AI runtime can access that through your connector, your Google Calendar connector, your Google Workspace connector. And that could run on the server side because anyway, the data is on the server. It's not even lying on your device. So that sort of hybrid orchestration is where we are headed to.

[00:40:36] Aravind Srinivas: I don't think it's a dichotomy between fully local versus fully server. It's all about choice. And anyway, when you're on your phone, you don't care actually which server that workload is running from because it's not going to be able to run on your phone anyway. The chips need to exist on a Mac Studio or a Mac Mini and are on the server.

[00:40:56] Jason Calacanis: Or this new Dell that's coming out. And I really think the idea of spending $10,000 on a powerful desktop will appeal to people if it lowers their $500 a month. Yes. Claude bill. Yes. This is an incredible savings. Plus you get the benefit. Yes. Of privacy and not educating the language models on your personal data.

[00:41:18] Aravind Srinivas: Yes. And it's going to be like you're buying a refrigerator. Your internet modem. Like the cost for these will eventually go down. Yeah. But it's not going to feel like you're wasting your money. Every home has a lot of other sensors that runs your home that will also be part of this orchestration loop. Yeah. So that's where it gets exciting because now you can just dictate something to your phone and that can control your entire home.

[00:41:47] Aravind Srinivas: So that's the dream that everybody has. And all that orchestration loop can run on your local hardware. No problem.

[00:41:54] Jason Calacanis: And I'm curious what you think of the operating system. What's eventually going to be the operating system of this workstation?

[00:42:02] Aravind Srinivas: AI is the operating system. Like earlier in the traditional operating system, you execute programmatically. Now you start with objectives, not specific instructions. Right. You come up with a high level objective. Go build this website for me that takes all the transcripts of all in podcasts and tracks the stock price just before the podcast and after. Yeah. And chart it for the max seven.

[00:42:25] Jason Calacanis: Yeah.

[00:42:26] Aravind Srinivas: And chart it over time. You can. So that's the objective. But individually, it's running a file system, a code sandbox, access to the Internet. It's having like its own HTML tools. And like. Yeah. So I think that's basically where, you know, models, systems and files and connectors are all coming together. You would think of that as an OS, except you're operating at an abstraction about that where you're thinking in terms of objectives.

[00:42:51] Jason Calacanis: Yeah. And does it need to eventually become its own operating system in your mind?

[00:42:57] Aravind Srinivas: It could be like people could think about it. It's like, yeah, I have my perplexity computer running all the time, whether it essentially it runs on Linux machines right now. Every server side computer is a Linux machine. Yeah. So I think Mark and recent tweeted this right after our release that turns out Linux computers was the right idea. Desktop. Desktop Linux computers are finally going to work. Yeah.

[00:43:21] Jason Calacanis: I mean, they're stable. Yeah. They're customizable. Exactly. And you're not at the mercy of Apple's desire to contain the experience. Exactly. Or Microsoft's surface area for hackers. Exactly. You build something rock solid and it does feel like Linux might actually become the eventual winner. It may not need to have a front end. Right. That's the thing.

[00:43:43] Aravind Srinivas: You could access the Linux machine on your phone. Right. It could be running iOS or Android. It doesn't matter. Right. The actual valuable runtime is running on Linux on the server.

[00:43:54] Jason Calacanis: You've done great as a consumer company. A lot of love there. Now I'm starting to see corporations with computer starting engaging. In fact, you'll be happy to know this. Last week, I took two people in my back office and I said, stop working on OpenClaw. Your job is to do the back office automation at our venture firm only using perplexity. And they were a perplexity computer. And they were like, oh, okay.

[00:44:23] Jason Calacanis: It doesn't talk well in Slack. It doesn't have an agent in Slack. I was like, it will. I'm going to see Armand. I'll talk to him about that. So we need a really strong Slack connector.

[00:44:34] Aravind Srinivas: It's already out. It is. Okay, great. Computer exists as a Slack bot right now. Okay. That you can add to your Slack workspace on the enterprise plan. And our entire company works like that. People are talking more to computer on Slack than other people.

[00:44:47] Jason Calacanis: In our first volley, we were sending reports in, but it wasn't interactive. That's perfect.

[00:44:53.540 --> 00:44:54.020] Perfect.

[00:44:54] Jason Calacanis: So now you've got your company going in two different directions. This incredible consumer run you have. How many people are using the product every month? Several tens of millions. So tens of millions of people. That's very much similar to the trajectory of the Google and Yahoo consumer business. Now you've got corporate. How are you doing on the corporate side? Thousands of companies?

[00:45:13] Aravind Srinivas: It's the fastest growing business for us. It's growing faster than the consumer and revenue. And things like computer unlock entirely new possibilities. For example, we've saved more than $100 million for our Enterprise Max customers who are on the highest tier of Enterprise. Explain what that is. What does it cost? $200 a month per person? So there are two tiers. One is the Enterprise Pro, which is $40 a month. And there's the Enterprise Max, which is $400 a month.

[00:45:40] Aravind Srinivas: And on a computer, after you run out of your credits, you would pay for the tokens. You pay for the usage.

[00:45:47] Jason Calacanis: Are you making money on the $400 a month, $5,000 a year one? Or at this point in time, are people going so crazy?

[00:45:55] Aravind Srinivas: One thing that Perplexity has is every revenue we make, unlike certain other wrapper companies, every revenue Perplexity makes has positive gross margins.

[00:46:03] SPEAKER_03: Got it.

[00:46:04] Aravind Srinivas: Because we're not just selling tokens. Right. Most of our revenue is recurring because people are paying a subscription fee. And because we route through multiple different models, we're very efficient in terms of how we spend on the tokens. Because we have all this advantage with drag and orchestration and search. We don't actually need to blow up the context window of the models. Yeah. As a result of that, we have positive gross margins on all the revenue. Every single penny we make, we make profits on that.

[00:46:33] Aravind Srinivas: Overall, the company is still yet to be profitable, but we're working towards that. You've had the opportunity to exit.

[00:46:38] Jason Calacanis: A lot of rumors. Apple, other people were like, hey, this is a great team. How many people on the team now?

[00:46:44] Aravind Srinivas: About 400.

[00:46:45] Jason Calacanis: Yeah. You've got a very coveted team. You obviously understand consumer. You obviously understand business. It's a product-driven organization. Reports are you declined. But the world's getting hyper-competitive here. How do you keep up as a 400-person organization when you've got Sam Altman over here raising $100 billion? And then you have Elon putting data centers in space and merging with SpaceX and Twitter. You have Google with unlimited resources.

[00:47:13] Jason Calacanis: Amazon getting in the game. And obviously, Gemini, a very strong product. And Google, really good at consumer. I think we'd all agree Facebook and Meta haven't figured it out yet, except maybe for serving us better ads. But they haven't figured out the consumer case yet. But they'll copy it. They always do. How do you look at the playing field? Because the degree of difficulty, this isn't playing checkers.

[00:47:39] Jason Calacanis: This is like playing against the 10 best chess players in the world. That's what you have to do every day. So how do you think about it? Long-term and independent company. Do you think you'll need to join forces at some point? And why didn't you take the deal? These deals were incredible that you got offered.

[00:47:54] Aravind Srinivas: So one advantage we have that all these companies you mentioned don't have is the multi-model orchestration. We're like Switzerland. We don't have to have one horse in the race. If GPT wins, Gemini wins, Claude wins, Lama wins, it doesn't matter to us. Or even open-source models can win. No problem.

[00:48:16] Jason Calacanis: And you have them on the service.

[00:48:17] Aravind Srinivas: Yes. You have DeepSeek and Kimmy? We have Kimmy, we have Nemotron, and we have a lot of usage of Quinn, Alibaba Quinn. Yeah. Silently under the hood. So for us, like that advantage of being able to take the best in each model and give the user the orchestra of everything they can do. I don't think any of the companies you mentioned can do that. Right. Nor would they. Nor would they. It makes no sense for them.

[00:48:42] Aravind Srinivas: It would be an admission that all the data centers and CapEx they've built out still couldn't produce them the best model. And Dario, CEO of Anthropics, said recently in an interview that models are specializing. Towards the beginning of last year, people thought models are going to commoditize. But towards the end of last year, models started specializing. Even within coding, Cloud Code and Codex have very different capabilities.

[00:49:12] Aravind Srinivas: Our iOS engineers love using Codex. Our backend engineers love using Cloud Code. Yeah. So even within a specialization like coding, models have their own unique specialties. And there are many other use cases outside coding where different models are good at different things. Which means the orchestra conductor that has no one model to the horse in the race can win. By providing a very unique value and service to the customer that each of these amazing names that you mentioned cannot.

[00:49:41] Jason Calacanis: And so you're buying tokens wholesale from them. And then you'll charge customers to do it? Or do you think it's all...

[00:49:50] Aravind Srinivas: We're going to take care of all their orchestration. Yeah. So you don't have to manage tokens across different models.

[00:49:55] Jason Calacanis: Because I authenticate a couple of my different accounts, my pro accounts into Perplexity. But does it... I don't have enough knowledge to know if you're abstracting that and people can just search across them. And it's part of their Perplexity subscription?

[00:50:09] Aravind Srinivas: No, we're not bundling subscriptions into other AIs. Yeah. We just ping the models directly. Got it. What you get in us is the Perplexity or orchestration. Got it. The harness. Right. So when models are kind of specializing, there's a bigger value in the one who knows how to build a great harness. Right. That can take the best in each model. Does it auto-route today or do you still have the dropdown somebody's got to pick? It definitely auto-routes the best model for each prompt.

[00:50:37] Aravind Srinivas: But we also give users the flexibility to pick whatever model they want.

[00:50:40] Jason Calacanis: What do you think of... I've seen a bunch of startups hack this together, but doing the same query across multiple... We built a thing called Model Council. Model Council, yeah. Yeah.

[00:50:50] Aravind Srinivas: So that's one of the modes in Perplexity where I saw Jensen say in one of the interviews that he puts the same prompt in five different AIs and sees what each of them says. Yes. Everybody does that, yeah. But then you still have to apply a biological compute to read every answer and then figure out where they differ. It's like talking to five lawyers about your trust or your... Five different doctors. Five different doctors trying to figure it out. Exactly. It's dumb.

[00:51:16] Aravind Srinivas: So the Model Council is a feature we built where it will not just give you the answers of each model, but it will tell you exactly where they agree, where they disagree, and where the nuances are.

[00:51:24] Jason Calacanis: And that's in the interface? Yeah. Model Council? I didn't know it was there. It's there. I mean, you release product at a pretty great cadence, huh? Yes. Where did you learn that and what's your philosophy of shipping product?

[00:51:35] Aravind Srinivas: Our philosophy is like speed is our mode. Like, you know, again, one of the things that big companies cannot do is move at the speed we do, serve customers at the speed and quality. It's very hard to maintain quality, speed, and trust at the same time. Yeah. Like Apple takes a long time to ship anything because they're very worried about people not trusting them. Yeah. And so some companies are bureaucratic and they just take forever to ship something. They don't maintain what they ship. They may make a big deal about an event, but nobody even knows how to go and use that feature.

[00:52:05] Jason Calacanis: Yeah. They get abandoned.

[00:52:06] Aravind Srinivas: Exactly. So perplexity has those advantages of being very small. And towards the end of last year, we found that like AI coding tools have made it much faster for us to ship things, which is honestly one of the reasons why we built computer because now even non-engineers are shipping code here by just bringing a slack bot and asking it to fix bugs. Yeah. So the iteration has just been like exponential.

[00:52:29] Jason Calacanis: The moment I had where I became claw-pilled was when I was working with it and I was like, hey, I want to build my network. I know these 20 people in Japan. I had dinner with them during my recent trip. I want to know who they know. So check out LinkedIn and other things and who they're associated with and make me like a mind map of it. And then the next trip, I want to meet with the next circle of those connections. So I started asking. It's like, okay, I got the results. I was like, great.

[00:52:58] Jason Calacanis: And it said, where do you want me to put them? And I was like, well, where can you put them? And it said, well, I can put it in a Google sheet. I can put it in a Notion table. I can put it here. I can give you a PDF. I can give you a CSV file. Or I could write you a CRM. And I was like, yeah, sure. Make me a CRM system. And it made a CRM system. And I think that becomes, I think maybe one out of a thousand people working with AI have had that experience. Maybe it's one in 10,000. Yeah. Where your agent says, I'll make you bespoke software.

[00:53:27] SPEAKER_03: Yeah.

[00:53:27] Jason Calacanis: Have you had that yet? And do you see that as a part of computer that when a person needs a spreadsheet, you don't launch Excel or Google Sheets.

[00:53:38] Aravind Srinivas: You just pop up a spreadsheet. Yeah. Well, we have a board meeting tomorrow. Okay, I'll come. I'll pitch it to the board. Sure. Our computer made the memo. Oh, wow. Yeah. And we had a partner meeting to pitch a partnership idea. And earlier, we would have a design team do the whole deck. Yeah. Computer just one-shotted it. I had a press briefing with a bunch of journalists. Sorry about that.

[00:54:05] Jason Calacanis: Oof. Brutal.

[00:54:07] Aravind Srinivas: And then my comms person would usually give me a memo. A dossier. What to say. Yeah. Computer one-shotted it. So. It's crazy. It's crazy.

[00:54:15] Jason Calacanis: The context is so good because the memory is getting better. Yeah? Yeah. So it's like, I know that journalist from the last time. Yeah. I know the board meeting. Yeah. I have all the previous decks. Yes.

[00:54:28] Aravind Srinivas: When did that happen? I think it happened with Opus 4-5. The anthropic. 4-5. Yeah. 4-5. That was an inflection point when models started being amazingly good at orchestration and reasoning and tool calls. And Cloud Code brought in this new idea in AI that everything can happen inside a sandbox, a console, a terminal with access to tools where tools are just command line tools.

[00:54:56] Jason Calacanis: Yeah.

[00:54:56] Aravind Srinivas: They don't even need to have graphical user interface. So when you did that and when you organize around files and subagents and skills and CLIs, the models started becoming very good at handling the context. So the context window no longer became a problem. It just put whatever necessary into the context whenever it wanted to and dumped them away when it wanted to.

[00:55:19] Jason Calacanis: Yeah.

[00:55:19] Aravind Srinivas: And that made it like suddenly so good at doing very long orchestration tasks.

[00:55:25] Jason Calacanis: Yeah. It's pretty crazy. I have every episode of This Week in Startups, all the transcripts, and then all of All In.

[00:55:32] Aravind Srinivas: That was one of the tasks I did, by the way. I can send it to you. Yeah. I asked it. I want you to download every All In podcast. Yeah. Since the beginning. And I want you to take a mention of all the public companies they mentioned during the episode. Yes. I want you to have a histogram of the counts. And I also want you to chart it across time. And then I want you to analyze the impact on the stock price. And the sentiment of what we said. Exactly. And it did. Like, it clearly said- Are we moving stocks?

[00:56:00] Aravind Srinivas: Around Google's stock going up. Yes. Prior to that, you guys were talking a lot about Google. Yes.

[00:56:06] Jason Calacanis: And it clearly- And I said I made a bet publicly on the thing. Yeah. I said, I am buying a bunch of Google because I believe even though they're behind, it's because they're too precious. You were kind of mentioning a company that might be too precious at times and doesn't release. Yeah. I was like, that's that company. They need to release more. Yeah. And I told Sergey, I was like, give us the good stuff.

[00:56:26] Aravind Srinivas: Yeah. Not only did it do that. They started giving us the good stuff. It literally gives you the timestamps of every single- And then I can go click on it and actually hear exactly- That moment. Yeah. Sweet. Sweet. Yeah. So that's when I was like, damn, I would have had somebody do this as a week-long project.

[00:56:42] Jason Calacanis: It would have been 10 hours a week of researcher. I'm experiencing the same thing. When I do research notes, I've created my own mega prompt.

[00:56:54] SPEAKER_03: Yeah.

[00:56:55] Jason Calacanis: And it will go and tell me where you worked before and who's in your circle, who your competitors are, who your friends are, blah, blah, blah. And then go find- I try to find old podcasts is one of my secrets if you're an interviewer watching. I try to find what was the person talking about five years ago, 10 years ago, and then over 10 years ago. And I've gone into interviews now with Michael Dell and talked about things he was talking about in the 90s. Yeah. And it finds me some ancient stuff.

[00:57:20] Jason Calacanis: Like, you would pay a researcher, a producer, you know, $70,000 a year, $80,000 a year to do this. And they would have done a third of the job in 10 times longer. Yeah. It's really gotten weird just in the last six months. What do you think the next six months looks like?

[00:57:37] Aravind Srinivas: I think the dream that what we are going to try to do is help businesses run as autonomously as possible. You know, everybody talks about this. AI is going to create this one person, $1 billion company. Some people say it's already happened because people pay researchers like $1 billion. But it's not truly moving the GDP by $1 billion. It's not truly creating new value. So the best way to do that is to actually help a small business, people who would otherwise

[00:58:04] Aravind Srinivas: drive Ubers for like extra passive income to like buy like a Mac mini, set up perplexity personal computer and run their business on that or like run it on the server. It doesn't matter. And actually make real money. Yeah. Hundreds of thousands or even millions a year and grow it. Have a computer go and run your ad campaigns on Instagram or Google. I mean, integrate with SEM and SEO tools, find new users and integrate with Stripe, charge

[00:58:34] Aravind Srinivas: them, ship new features, have your own like intercom integration for customer support and like have this all working well. You can be sipping wine in Napa. That's the dream that, you know, it feels awesome to say everybody thinks it's already there. It's not there yet. Someone has to do that hard work. Yeah. That's what we want to do.

[00:58:52] Jason Calacanis: Yeah. It's a great vision because when I watched startups 20 years ago, there were so many checkboxes they had to do. I have to find an office space. I got to put up a bunch of servers. I got to hire an HR firm. I got to hire a PR person, all this stuff. And now I talk to young founders. They got a three person team. They've come out of a 16 Z, my program, launch accelerator, whatever it is, Y Combinator. And I'm like, okay, you raised a half million. You raised a million. Who are you hiring?

[00:59:21] Jason Calacanis: And they're like, um, I don't know if we need to hire anybody. I'm like, if you could hire somebody, what do you hire? They're like, well, I do my own HR. I have this partner and they're, I'm like, how are you doing hiring anyway? And they're like, well, I put out an ad and then, uh, it sorts and ranks the candidates. And then it emails the top 10, ask them a bunch of questions. And then I meet with the last two. And I'm like, that's what a recruiter did. Yeah. Like the entire recruiting job has been abstracted.

[00:59:47] Jason Calacanis: And like a tool like computer is going to make that even faster work to do.

[00:59:52] Aravind Srinivas: Uh, a lot of connectors, a lot of specific workflows. People don't want to like learn how to write like, you know, essay long prompts. You know, it needs to be so quick and fast and autonomous. You just set it up and done. And you have an idea. You can turn it into a business and start making money.

[01:00:09] Jason Calacanis: Yeah. It's, it's an incredible future. Uh, and it feels like it's right here. Do you, how do you think about job displacement? Cause you're actually making the tool that enables people to be a solo entrepreneur and get to a million in revenue, but it's also the same tool that doesn't require them to hire. And we've had this debate a million times on the podcast. Do you, I'm wondering if like me, you have moments where you're like, oh my God, this is really terrifying. Yeah. A lot of people are going to lose their jobs really fast.

[01:00:37] SPEAKER_03: Yeah.

[01:00:38] Jason Calacanis: And then, oh my God, you can learn any skill you want. And all the things that were hard are now easy. Yeah. I go back and forth. I'm 70, 80% super positive about this, but I do worry about like 20% of the time. I'm a little worried.

[01:00:52] Aravind Srinivas: Yeah. Where do you sit? I mean, America has always been about like entrepreneur, entrepreneurship, right? Like we've been about like trying to build new things, discover new things, go explore. Uh, I think this whole like Henry Ford came and built factories and brought in jobs and things like that. And like put people into a box. But, uh, I think the reality is people, most people don't enjoy their jobs. They're doing it. No, they hate them. Exactly.

[01:01:17] Aravind Srinivas: So there's suddenly a new possibility, a new opportunity to go use these tools, learn them and start your own mini business. And if it pays for your needs for a year or multiple years and lets you have a high quality life and good work-life balance and true feeling of agency and ownership and passion to like get your ideas out there. I think that is, even if there is temporary job displacement to deal with, that sort of glorious future is what we should look forward.

[01:01:45] Jason Calacanis: I, I, I think you're exactly right. If there will be some displacement, but then there's also gonna be so many opportunities open up and it requires the individual to not be passive. Exactly. They have to be rugged individualists. They have to be resilient. Yeah. And they have to be resourceful. And I think once you start playing with these tools, that's what happens. Exactly. You, you all of a sudden feel like-

[01:02:06] Aravind Srinivas: I'm the best in you if you truly are in a good space. Yeah. Yeah.

[01:02:10] Jason Calacanis: I, and then today a comment for iOS is out. Yeah. I'm a comment super fan. I required everybody. You were nice enough when I, I emailed Joe. I was like, can you send me some licenses? You said, you don't remember, you sent me a bunch of licenses. I said, everybody put this on because it was $300 a month when you first came out with the common browser. Now it's free. I think for all users highly recommend it, highly recommend getting a pro account. It's only 20 bucks a month to get into perplexity, which is a joke. So you can get on board for nothing, less than a dollar a day.

[01:02:40] Jason Calacanis: But what does iOS allow me to do? And how does it connect to computer? Because that's another thing I'm having. Yeah. Cloud code, computer. There's not a good enough integration with this mobile device yet.

[01:02:54] Aravind Srinivas: Yeah. So computer is already on the perplexity app. So you can just toggle the computer and start using it. Comet's uniqueness and perplexity for the company and the strategy is the fact that you can control the browser. So the browser also becomes a tool for computer. Yeah. Just like your Google workspace and all these other things. Until the whole world is organized around CLIs and tools. Yeah.

[01:03:20] Aravind Srinivas: There's still a lot of tasks we have to do manually on the web, on the browser, open tabs, fill up forms, click on things, upload stuff. All that stuff, if you want to automate, you need a browser. You need an AI that can natively control the browser. So that is Comet. And that's why no matter how many other tools in the market exist, like OpenClaw or like Cloud Cowork. Yeah. Executing tasks on a browser, on the server side, along with all the other things is something uniquely perplexity can do.

[01:03:50] Jason Calacanis: Yeah. My dream is that you'll create an Android app that roots my Android phone. Yeah. And that you just take over and see everything. Because one of the blockers I have now is some of the websites have gotten a little persnickety. Yeah. I don't want to mention too many, but Reddit, LinkedIn. Yeah. And like, they're just, I am a great Reddit user. I'm a great LinkedIn supporter. But sometimes like I need to get my in-mail from my LinkedIn.

[01:04:20] Jason Calacanis: And I just need to, you know, find seven people at a company. Is there going to be a solution between the LinkedIn and Reddits of the world and the claws and perplexities? Yeah. How is that? I mean, the API is... Negotiation going. You don't have to speak about any specific ones unless you want to.

[01:04:37] SPEAKER_03: Yeah.

[01:04:37] Jason Calacanis: But it feels like there's got to be a solution. And I'm willing to pay for it as a user. I'm willing to play Reddit to allow my bot to show up and behave properly.

[01:04:46] Aravind Srinivas: Well, I cannot speak about any particular company, but we are happy to work with anyone. Right. So I think with Comet, our idea is to give people the flexibility to set things up on their own. Yeah. And any official APIs that anyone's willing to offer, we're always happy to put that as part of computer. Here's what I think should happen.

[01:05:08] Jason Calacanis: Let me see if you agree. And this is for Steve Huffman at Reddit. I go on Reddit. I do a pro account for 20 bucks a month. And when I do that, I can authenticate whatever tool I want to do a series of well-behaved things a certain number of times a day. Yeah. So it's not unlimited. I'm not going to scrape the whole site.

[01:05:32] Jason Calacanis: But I would like it to just let perplexity or computer go and just tell me, hey, what are people saying on this week in startups and all in subreddit? Summarize it for me so I get the customer feedback. And I would literally name my agent. And I would say it won't post on my behalf. It won't vote on my behalf. Just need it to do a couple of little read-only things. This would be an easy solution. Or LinkedIn, I already pay LinkedIn like 50 bucks a month.

[01:06:01] Jason Calacanis: They should just let the $50 a month one work with computer. Yeah.

[01:06:05] Aravind Srinivas: Absolutely. I mean...

[01:06:06] Jason Calacanis: Okay. This is for Satya Nadella. Let LinkedIn work with perplexity and the other players and we'll pay you extra. Perfect. It's a revenue stream. Don't you think API access for customers is a revenue stream?

[01:06:18] Aravind Srinivas: I think so. I think fundamentally giving users a choice and setting it up as a win-win for both the business and the user is where the world should head to. Yeah. And I would say the same thing applies to any website in the world. Like if you want an AI to use it on your behalf, it should be okay for it. Because that's what the user wants.

[01:06:37] Jason Calacanis: I mean, I have a paid New York Times subscription. Like let me go in there and do, you know, whatever, 100 searches a day, a week, a month, whatever they choose. But that would make the subscription that much more sticky. Exactly. All right. But Arvind, love the product. Anybody at home, it's just tremendous. Go learn computer and get the Comet browser. It has changed my business for the last two years. Thank you, Jason. Love the product.

[01:07:05] Jason Calacanis: And we'll have you back soon when you launch your operating system and come up with your own server and desktop server. But business is the focus. Yeah. Yes. All right. Thank you, Jason. Great seeing you. Thank you. We have an amazing guest, Aravind Srinivas here, the CEO of Mistral AI. How are you doing, sir? Great. Thank you for having me. And so you're here at NVIDIA's big conference, big announcement.

[01:07:29] Jason Calacanis: You're going to be working with NVIDIA to build models, to open source them. What is the big announcement here?

[01:07:37] Arthur Mensch: Well, we're announcing that we are going to be training the next generation of Frontier models with NVIDIA. It's something that we've been doing before with NVIDIA, with Mistral Nemo, something we did like 18 months ago. And the point for us is really to be able to produce the best open source models out there so that we can actually use those assets to specialize them through products that we do for our customers, like Forge, that helps us customize the models for the enterprise we work with in engineering, in physics, in science, in making them better at certain languages

[01:08:07] Arthur Mensch: when we work with governments, et cetera.

[01:08:09] Jason Calacanis: And Mistral, obviously, based in France, you're the leading AI company there. What's it like running the company and building a large language model in Europe? Obviously, there's regulations and all kinds of considerations. Privacy. The French are known for protecting privacy. In the United States, we're known for taking it away. How is the landscape there? And what do you have to deal with there that maybe you wouldn't have to deal with in America? What's the pros and the cons?

[01:08:35] Arthur Mensch: Let's say, first, we have 25% of our business in the US and 25% of our researchers are actually here. So I actually spend a lot of time here as well as in France, as well as in the UK, in Singapore, where we are. So, of course, it's different markets. It's markets where you have language, which is a topic where there's much more manufacturing. Manufacturing is a bigger piece of the cake than it is here. And I'd say our strength has been to also work with European companies that are a bit

[01:09:04] Arthur Mensch: lagging behind and that wants to adopt the technology to leap forward. And we've been able to do that through a forward deployment engineering engagement, through our Forge product, for our studio product that allows to deploy agents that do end-to-end automation. But on top of that, the thing that we have announced today, like Forge, is something that is actually being used today with customers in the US because they come to us with needs for post-training, for making models specifically good at financial services. And what's happening is that we have this product and we can bring the models to specialize

[01:09:34] Arthur Mensch: them as well.

[01:09:35] Jason Calacanis: And so your belief is specialized, verticalized models, healthcare, finance, engineering, different verticals will win the day? Or a global model will win the day that does everything?

[01:09:48] Arthur Mensch: Well, you need general purpose models to do the orchestration parts, etc. But at some point, enterprises sits on a lot of intellectual property, on a lot of signals coming from physical systems, from factories, from tools. And it's actually not trivial to connect those systems, to connect those data to models that are closed source. If you have open models, you can actually add new parameters. You can make a lot of deeper things that you cannot do with closed models.

[01:10:15] Arthur Mensch: We can also, and that's something that we do, not only do we work at the model side, but also at the orchestration side. We sit with subject matter experts to understand their needs and we build business applications that are fully bespoke to their needs by modifying the models, but also modifying the harness on top, etc. So we believe that eventually building on open source technology is a way to save cost, is a way to have better control because you can see the thing on every cloud that you want, on your hardware if you want, you can deploy it on the edge if you want.

[01:10:42] Arthur Mensch: And eventually, from a customization perspective and from leveraging your decades of IP that you've been accruing in financial services, in heavy manufacturing, like companies like ISML, for instance, they do benefit from working with us because we take their data and we build models that are specifically good for their purposes.

[01:10:59] Jason Calacanis: This training data using experts to come in and refine a model. Most people don't know this business that well, but this has become a very large part of the industry. Obviously, Scale AI was doing it. They went to Facebook, lost a lot of the customer base who didn't want to send their data, I guess, over to Meta. We're investors in a company called Micro One that's doing pretty well in this space. There's other folks doing it.

[01:11:24] Jason Calacanis: Explain to the audience what you're doing specifically for companies and how this training works in a verticalized way, and then how you silo that data. Because if you're working with one customer in aerospace or fintech, they might have a need set, but they may not want that training to go to a competitor.

[01:11:42] Arthur Mensch: I can use a few examples. I think overall, the data segregation is super important. And the way we have solved that is through a portable platform. So our technology is a set of services, a set of training tools, a set of data processing tools that I can take and that I can put on the infrastructure of my customers. So suddenly, from an IT perspective, and when we talk to the CIOs, they realize that from security perspective, the flow of data doesn't go. There's no data flow coming back to Mistral because everything stays there.

[01:12:10] Arthur Mensch: Now, the way we then use that technology that has been deployed is that we're going to be working with the teams that is doing image scanning and default detection with ISML, for instance. And we're going to be sending forward deployment engineers, scientists, they're all PhDs, they know how to train models. And they spend some time with the subject matter experts that can explain how an image is being detected, how do you detect defaults, et cetera. And based on that, we're going to work out what kind of data needs to be used to train the

[01:12:40] Arthur Mensch: models that it's going to solve the task in itself. And so we send the technology. Typically, we send a little bit of scientists because you do need that expertise transfer and that knowledge transfer in between our teams and the vertical experts. And then we make sure that eventually our team no longer needs to be there to retrain the models, to get more data access, et cetera. So that combination of data segregation, expertise transfer, knowledge transfer is the one thing

[01:13:06] Arthur Mensch: that makes us quite unique and allows us to serve the most critical use cases, the most critical processes in industries that actually need to take their data and put it into models for it to work.

[01:13:15] Jason Calacanis: Yeah. This seems to be once the entire open web, what was available legally, gray market, et cetera. I wouldn't have your comment on that controversy. But we kind of exhausted what's in the open crawl. Yeah, we have. And it's time to actually either make synthetic data or actually use experts. Do you believe in synthetic data? And where does that work and where does it fail?

[01:13:42] Arthur Mensch: We use synthetic data as a way to warm up the models. It's a way to actually be quite efficient at the beginning. If you have a large model and you want to train a small model, you will use your large model to process and to produce a lot of synthetic data at the beginning. But eventually, you do need to have human signal. So the human signal is something that is always a bit costly to acquire because you need to talk to the experts. They need to give feedback to the machines. And so at the beginning, synthetic data allows you to do the compression, to further compress the models.

[01:14:12] Arthur Mensch: At the end, you do need to go and get data that is produced by humans. So yeah, it's mostly an efficient way of training models to have bigger models that are used as teachers for smaller models. But it's not enough. And so you also need human signal.

[01:14:27] Jason Calacanis: Arthur, we've seen an incredible explosion. We're sitting here on AO52 after OpenClaw, the year of our Lord, 52 days. When you first saw OpenClaw and saw the reaction of hackers, founders, startup CEOs, just the amount of energy and it racing to the top of GitHub with the most number of stars and likes

[01:14:52] Jason Calacanis: and all these contributors, what did that say to you as an executive in the space who's been grinding on this for many years?

[01:15:01] Arthur Mensch: What does that OpenClaw moment mean? Well, it resonated a lot with what we were doing with our customers because pretty quickly, enterprises realized that if they wanted to make some gains with artificial intelligence, they would need to automate full processes. And to automate the full process as an enterprise, well, you can use OpenClaw, but it's going to be, it's actually not really enough because you have data problems. You have governance problems. You can't observe the process that is running and you can't control it.

[01:15:29] Arthur Mensch: In many cases, when you run a KYC process, if you're HSBC, for instance, one of our customers, you will want to have deterministic gates that are going to always do the same thing in a way that is observable and that you can guarantee the CAO that it's always going to go through these gates. And that's not something that OpenClaw is providing because it doesn't have the kind of primitives that you need to work on collective productivity, observable productivity, and to work on mission critical systems.

[01:15:56] Arthur Mensch: On the other hand, the autonomy it gives and the autonomy it brings to people that are just individuals that are hacking together things is a way to also show to enterprises that if you set up the right control plane, if you set up the right sandboxes, if you connect to the right data sources, if you make sure that your access controls are well respected, then you can actually unleash the power of agents doing things for your employees. And that's going to work on the platform because otherwise you will not be at ease when you're sleeping.

[01:16:24] Jason Calacanis: It is definitely something you have to be thoughtful about. When I installed it, I gave it just for my agent, root access to my Google Docs and my G Suite, my Notion, my Zoom and my Notion and G Calendar, everything. And then I realized, wow, I can with my enterprise edition of Gmail, essentially, I can just summarize for my entire 21 person investment company, every conversation going

[01:16:53] Jason Calacanis: on in Gmail and then correlate it with every conversation in Slack. And then I realized, oh my gosh, there's compensation discussions going on. And there is a person on a pip who we put them on a performance improvement plan, perhaps, or something like that. Oh, I have to make sure nobody else can access this because the power comes from giving it access to data. But with great power comes great responsibility. And I think people are learning that in real time.

[01:17:20] Arthur Mensch: Yeah, it's a big problem because the enterprise data is not a single thing that you want to put into a single system that is going to be accessible by everyone. And so you need to have this layer that actually understands what is in the data. You need to have a semantic of what can actually be proposed to HR or what can be proposed to engineering. And typically, compensation is one of these things. You want to make sure that the compensation data does not flow back to all of the enterprise,

[01:17:48] Arthur Mensch: because you're going to have a lot of problems if that's the case. And so what you actually need, which is hard to do, is what we call a context engine. So a mapping of where the data sits that comes with a certain number of metadata that is telling you that this data is actually not accessible to this part of the company. And if you actually have someone in engineering that is asking for something related to comp, the thing is actually going to tell you, look, you actually can't access that data. Yeah. So that's hard. It's actually hard.

[01:18:15] Arthur Mensch: You need to rethink entirely the way your IT systems are being connected. And at some point, you also need to think about your management, because your information flow is completely different today if you're connecting agents together with your data sources than it used to be. And suddenly, maybe you don't need that manager whose only purpose was to take information from the bottom and put the information on the top, etc. So there's some IT problems to solve, and you need the right primitives, you need sound boxes, you need airbag, air-based access control, and these kind of things.

[01:18:45] Arthur Mensch: And you have change to do. You need to rethink your entire customer service department, because suddenly you actually don't need that much transfer of information operated by humans.

[01:18:55] Jason Calacanis: All right. You have to go. You've got a flight to catch. I have. It is so great to see you, Arthur. Continued success with Mistral. Thank you very much. Cheers. I'm really lucky to have Daniel Roberts here. He's the co-CEO and co-founder, along with his brother of IREN. They are a publicly traded company. They started in BTC. Welcome to the All-In Interview Program.

[01:19:15] Daniel Roberts: Thanks, Jason. Pleasure to be here.

[01:19:16] Jason Calacanis: Yeah. And so you started in Sydney. You and your brother, it was seven, eight years ago, and you got in early on Bitcoin. And all these Bitcoin miners wanted to have data centers, huh?

[01:19:30] Daniel Roberts: Yeah, that's directionally right. So the thesis we saw was this explosion of the digital world, the growth in the online, and at some point the real world was going to struggle. So we set about to build out large scale data centers. Yes, the first use case was Bitcoin mining. But as we said to our seed investors, use that to bootstrap the platform, generate cash flow, layer in higher and better use cases over time as they emerge. Here we are today with AI. We are swapping out all the Bitcoin for AI chips.

[01:19:57] Jason Calacanis: When did you first start seeing the demand in the company shift from, hey, Bitcoin miners, we need some H100s, whatever it is, to, hey, we're this nonprofit open AI. Hey, we're this research lab. We need some AI compute. When did that start hitting?

[01:20:17] Daniel Roberts: Look, we had a bit of a false dawn, I would say, back in 2020. We signed an MOU with Dell to start bringing out customers and compute. But in hindsight, it was too early. So we went back to Bitcoin, kept bootstrapping the platform. But I would say about two years ago and month by month,

[01:20:32] Jason Calacanis: the demand just continues to escalate. And you were in so early that when you were looking at data center space in the United States, you were one of one looking at the space, one of two or three people looking at the space. They were trying to sell you on space, yeah?

[01:20:49] Daniel Roberts: Yeah. So we actually developed the data centers ourselves. So we go and find the land, we go and get the permits, we go and apply for grid connections. And we were doing it at a scale that just amazed people at the time. Like 750 megawatts is our flagship Texas site. Four years ago was unheard of. In the middle of the desert, we're building these big data centers. The traditional data center industry going, what are you guys doing? We're saying, we believe in the future digitization, high performance computing, and obviously now today's

[01:21:16] Jason Calacanis: paying dividends. Yeah. I don't think anybody could have predicted when ChatGPT came out, open claw recently as a turning point. And then Microsoft, Google, and everybody embracing this. And that's your big partner, Microsoft. Yes, Microsoft's one of our early partners. We signed

[01:21:35] Daniel Roberts: a $9.7 billion contract with them late last year. But as I was explaining to you before the show, that's 5% of our capacity. So things are busy at the moment. Yeah. And when you do these build outs,

[01:21:48] Jason Calacanis: the big conversation today is no longer the number of GPUs putting in. It's just power. Power is the constraint today. Yeah. Look, for many of the industry it is. But for us,

[01:22:02] Daniel Roberts: because we started eight years ago, tying up all this land and power, it's not. So we've got four and a half gigawatts. For context, that's almost as much power annually as the Bay Area uses in its entirety. Wow. It's huge. So for us, the hurdle or the constraint is really time to compute.

[01:22:20] Jason Calacanis: And that's emerging across the industry as well. And time to compute means tradespeople coming to West Texas, living in a trailer that you set up to then break around on a data center, build foundations, build water cooling systems. This is hard manual labor going on. Yeah?

[01:22:42] Daniel Roberts: Exactly. And this is the whole real world challenge to respond to these digital exponential demand curves that are unconstrained by the real world in terms of their appetite. And it just compounds. You need thousands of people out in these locations that haven't supported it. You put stress on supply chains. We're seeing what's happening with the memory, every aspect of it. So it's just permanent whack-a-mole, permanent solving fires to try and bring online this compute.

[01:23:07] Jason Calacanis: And you get to spend time there. What's it like when you set up a town or you bring a thousand people or 2000 people to what's a pretty much remote small town? I'm assuming that when you bring a thousand, there might only be 500 living there right now. So what are those towns like? It sounds to me like something out of the gold mining era when people first went and were prospectors.

[01:23:35] Daniel Roberts: Yeah. You're prospecting down? Pretty much. I mean, the barbecue is great. That was the drawcard. But apart from that, look, we've always had a policy of hiring locals, supporting the local community. This year, we're hitting a million dollars in community grants cumulatively. That's things like local playgrounds, supporting the fire departments. But we will hire locally. Once we can't find that trade locally, we will expand the radius by 20 miles and hire out of that and so on and so on.

[01:24:00] Jason Calacanis: That's very thoughtful. Yeah. And these folks are coming, say an electrician or a construction worker, they're coming having built houses or maybe building corporate offices. And now they come for a tour of duty here and the salaries go up massively, but they got to leave their family for a three month

[01:24:23] Daniel Roberts: tour or something. Yes and no, because typically where we locate is where there's heavy electrical infrastructure. Where there's heavy electrical infrastructure is typically where old manufacturing and industry has closed down. So we go in, leverage that sunk capex, re-hire, retrain local workforces, and bring a new industry to town in these data centers.

[01:24:45] Jason Calacanis: Has that workforce now been completely depleted and we need to train another generation, a younger generation to be generation two belt and really embrace the trades?

[01:24:57] Daniel Roberts: A hundred percent. We're partnering with universities, trade colleges, absolutely.

[01:25:01] Jason Calacanis: And you go to a trade school, you go to a college, people are getting degrees in philosophy and English literature. They're going 50K a year in debt, 200K a year in debt. What's the starting salary for a trades person working on a data center doing electrical or construction or HVAC? What's the

[01:25:21] Daniel Roberts: ballpark range? Oh, look, I won't talk specifics, but they are going up. The price is going up. Depends on the level. But yes, there is a rush for a good way. I'm hearing 150 to like 300K. Am I in the ballpark? The lower end directionally you're right. Yeah. Yeah. I mean, it's incredible when you think

[01:25:37] Jason Calacanis: about it. There's concern about, hey, AI taking jobs and then on this other side of the ledger, can't find enough talent to service it. Talk to me about energy sources and how you think about that. President Trump, Chris Wright, the administration, they kind of started with, hey, clean, beautiful coal. Year two, they're like all sources matter. Nuclear. Obviously, Nat gas is plentiful in that area. We

[01:26:06] Jason Calacanis: don't know this about Texas. In the United States, the number one source of solar installations. Yeah.

[01:26:14] Daniel Roberts: Talk to us about energy. So our philosophy has been sustainability from day one. We have used 100% renewable energy since inception. What? 100%. Wait, how is that possible? We use hydro in British Columbia. We use wind and solar in West Texas. In West Texas, where we're located, there's around 45 to 50 gigawatts of wind and solar. Yeah. The transmission line to export that down to the load centers in Dallas and Houston is 12 gigawatts. Oh.

[01:26:40] Daniel Roberts: So you go and locate to the source of low cost excess renewable energy, monetize it into this digital commodity, export it at the speed of light as tokens. Great arbitrage. And the wind is producing

[01:26:51] Jason Calacanis: a lot, but it's harder to get from those areas where people are willing to put up. I mean, people don't understand how big West Texas is. It is an incredible amount of land. And you're coming from Australia. Australia, where also on the West side, people don't understand exactly how much just pure nature land there is. Yeah. Undeveloped.

[01:27:11] Daniel Roberts: So much land. And the issue is distance. You've got to spend billions of dollars on this transmission connection infrastructure to move that power to where people actually want it. You can build wind farms, you can build solar farms, but if you build it in the desert and no one can use it, then what's the point? Yeah. So the whole opportunity for our industry is to go to the source of that power and monetize it.

[01:27:29] Jason Calacanis: So the data centers follow the wind turbines, the solar installations. How do you think about batteries? And are you able to put those online? Because obviously you're going to have periods where, hey, it's not a windy day. In Texas, we have very few days when it's overcast. So that problem is pretty much solved, but you're going to have 50 days where the sun's not beating down. So how do you deal with the demand and softening that duck curve?

[01:27:55] Daniel Roberts: We don't need to. The utility does that on our behalf. So this is why these grid connections are so scarce, so hard to get, and so highly valued. Because once you get that grid connection, the utility underwrites all of that variability. They guarantee you 24-7 reliable power.

[01:28:11] Jason Calacanis: Got it. So on their side, they're figuring it out. Yeah. Something goes down and they could fall back, even though you're 100% committed to renewables. If they needed to fall back to gas or whatever, they have that ability out there. So you have that as a backup. A lot of talk about, or a debate, are we getting ahead of our skis? Are people slowing down? There was some talk about the OpenAI project, maybe downscaling a little bit. Is OpenAI a partner as well, or? I can't comment.

[01:28:40] Jason Calacanis: Can't comment. Okay. So we'll read into that whatever we want. But are there pockets where people are saying, hey, let's slow down, or is it still gangbusters?

[01:28:51] Daniel Roberts: It's right up the end of the spectrum. It's gangbusters. We cannot meet demand. That's why the whole industry now is around time to compute. There are no idle GPUs in the world sitting in a

[01:29:01] Jason Calacanis: data center. Yeah. And what's your take on when software makes, and this is a big discussion from Jensen himself during his two and a half hour keynote yesterday. We're sitting here Wednesday. I think he did his keynote on Tuesday. He was talking about, hey, software is going to make it 50 times more, lower the cost of tokens, 50x. And then you have

[01:29:25] Jason Calacanis: transport also contributing to that. When do you think the curve goes from parabolic to simply growing a ridiculous level? Is there a slowdown coming or how are you planning for the future?

[01:29:38] Daniel Roberts: Look, I think it's actually the opposite. I think it feeds on itself. So I'll give you one example. You go into chat GPT today and you generate an image. You enter the prompt. It's like the dial up internet days. It is. Right? It takes minutes. You're like, I better get this prompt right. Yeah. Finally, two minutes later it comes. Now I'll give you an example. If we 10x the amount of compute available, which is an enormous task from where we are today, and those images take five to 10 seconds,

[01:30:02] Jason Calacanis: are we going to generate more or less images? Oh, many more. This is Jevin's paradox. This is the theory of induced traffic. You build a couple more lanes. People start to think, well, maybe the distance from Bondi Beach to the central business district in Sydney terms would be an acceptable commute. Love the analogy. Yeah. So what do you think about, or what are you seeing? I mean, we're here at NVIDIA. Obviously they make the leading edge ships. They just bought Grock. So now you've got

[01:30:32] Jason Calacanis: two of the leading edge chips coming out of the same company, but custom silicon becoming a big discussion. Has that started to land in the data centers yet? Obviously Google, don't know if they're a customer you can tell us, but they're making custom silicon. Amazon is making custom silicon. Meta is making custom silicon. Talk to me about that revolution and is it actually making it to the

[01:30:55] Daniel Roberts: data centers yet? Look, to various degrees it is. They're promoting their products. They're trying to tie up data center capacity. So yes, there's multiple silicon looking for homes. I think it's fair to say NVIDIA has a massive head start. The ecosystem they've incubated, the standards that they're setting. So I would say the safest pathway to build out at scale early is to follow the NVIDIA roadmaps. But absolutely over time we are seeing these chips emerge.

[01:31:20] Jason Calacanis: And in terms of desktop computing, I don't know if you saw the announcement that Dell and NVIDIA are making a really powerful desktop, 750 gigs of RAM, a lot of power. You're going to be

[01:31:44] Jason Calacanis: the models out in China. Has the hacker group, which I think you started in like I did probably in similar time periods. People are starting to get really obsessed with having a 10 or 20 thousand dollar desktop setup and running this local. What do you think of that trend? I'm curious.

[01:32:00] Daniel Roberts: Yeah, I mean the breakthroughs we're seeing in software, the way it's distributing power to every man and every woman in every house and their ability to code and use products like OpenClaw, the generation of demand and appetite for computer at a local level all the way through to these mega data centers. It's absolutely real. And as we see the emergence of agents using more and more, as we see autonomous vehicles and other automation, robotics, it's absolutely going to compound.

[01:32:25] Jason Calacanis: And what about nuclear? The Trump administration really seemed to flip the switch on a growing belief that, hey, wait, nuclear is pretty great. It's clean. It's the original renewable in a way. And these new modular reactors have nothing to do with Chernobyl, Fukushima or Three Mile Island. They're much safer. They're completely different architecture. Have those started to land yet?

[01:32:55] Jason Calacanis: And are you since you followed correctly in the great state of Texas where I'm from, you followed correctly that time. Are you following nuclear? I think you have to. I think the reality

[01:33:05] Daniel Roberts: is it's going to take a decade, a bit longer by the time big projects can come into commissioning. But now is the time to start that conversation, put in place policies, mobilize capital and start

[01:33:16] Jason Calacanis: that ball rolling. Yeah. Do you have a data center going up near nuclear? No, not at the moment. Not at the moment, but you're actively tracking that activity. Yes. Yeah. This seems pretty inevitable. Yeah. Feels like it. And if that happens, what impact does it have on your industry? If you could, because obviously it's happening in China and people always put the Bitcoin miners. They were like the canary in the coal mine near the hydro dams and near the nuclear where there was excess capacity.

[01:33:46] Jason Calacanis: What impact do you think this has if you could actually have small modular reactors next to data

[01:33:51] Daniel Roberts: centers? Well, I think it just opens up the market and enhances the US's competitive advantage in this space. Like AI is inevitable. Robotics is inevitable. The reality is the correlation between human progress and energy consumption is really, really high over a very long time period. So if we can find a way to unlock new generation, clean generation as nuclear and locate that more at the source and enable more compute on a distributed basis, all those use cases we just discussed become

[01:34:18] Daniel Roberts: easier, more fluid, faster. And then you get that positive flywheel around Jevons Paradox and demand.

[01:34:24] Jason Calacanis: Talk to me about the architecture today of ethernet and data moving between data centers within data centers. That backbone is going through a paradigm shift as well. Yeah.

[01:34:39] Daniel Roberts: Yeah, it is. And Jensen coins the term, the data center is the new computer. Yeah. So you need to step back and you say, right, this big building is essentially the old desktop PC we had under our desk at home. Yeah. Right. How does that work? So all the cabling, the latency, the number of hops between each GPU, how they talk to each other, the fabric around InfiniBand, ethernet, it's absolutely critical because every millisecond matters in terms of performance of that cluster.

[01:35:06] Jason Calacanis: Yeah. And where do you think or what do you think of Elon's vision? It's obviously a longer term vision of putting data centers in space and there's a couple other people working on it as well.

[01:35:22] Daniel Roberts: Yeah. I mean, it's very hard to argue with Elon. He's been very right on a number of things for a very long time. I think sitting here today, it feels exceptionally difficult given the cost of moving things to space, the challenges around radiation. There's a huge amount of engineering challenges, but that's never scared Elon before. Yeah. So I'm not really qualified and he's,

[01:35:43] Jason Calacanis: he's inevitably right, but sometimes he's late. He might be late to the party. He might be late to the dinner party. He might show up at dessert, but generally he nails it. How much of an issue is getting the data out of the data center to consumers today? Is that not something people are worried about when you're building something out in West Texas, all that data fiber, all that's been taken

[01:36:08] Jason Calacanis: care of, or does that become a gating issue at some point? So this was one of the big myths that we had

[01:36:14] Daniel Roberts: to bust when we started this business. Cause everyone said data centers must be located close to population centers, metropolitan areas. Latency is really important. And we say, yeah, that's right. Latency is important. But the reality is in the U S Texas, especially there is fiber everywhere underneath the ground, lots and lots and lots of it. And when you look at latency from our site in the middle of the desert in West Texas, down to Dallas, the big carrier hotel, six millisecond

[01:36:40] Daniel Roberts: round trip latency. What's six milliseconds? There's a thousand seconds, milliseconds in a second. Yeah. We're talking six. It's adjacent.

[01:36:48] Jason Calacanis: Yeah. It's, it's not even a, yeah, it's definitely not material. Uh, listen, continued success. Uh, and, uh,

[01:36:58] Daniel Roberts: you're hiring a lot of people. Yeah. Yeah. I think we've got 129 job advertisements up at the moment.

[01:37:04] Jason Calacanis: All right. So everybody go to the IRAN website, uh, and listen, company's doing fantastic. Thanks for spending some time with us here at all in at GTC. Thanks Jason. Appreciate it.

[01:37:17] SPEAKER_06: I'm going