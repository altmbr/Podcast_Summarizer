[00:00:00] Erik Torenberg: The grid is breaking. We're so bottlenecked today on the lines that run crisscross across the country. I mean, it's this very complicated, giant organic machine.

[00:00:09] Drew Baglino: New power is not the problem. Delivery is the problem. The energy services were growing over time in the United States. The net electricity delivered to accomplish those energy services stayed basically flat. We can take that momentum and bring it into a new problem statement, which is power for data centers, power for industrialization, power for economic growth and prosperity, and for sustainable energy.

[00:00:29] Erik Torenberg: The idea that the grid can grow and move from the edge is just not something that we've really been able to process for the last 50 years in the U.S.

[00:00:39] Doug Bernauer: The grid itself is civilization, right? Electric power is civilization. You can metamorphosize the entire grid. Civilization can regrow off of a new architecture of moving power, right, and use all of the free energy that's out there. The sunlight is free. You put it on the panel, you're getting it. It's very cool, but also uranium is free. It's in the grounds. It's there if you take it and we use it before it just goes away. It makes this like completely new way, I think, of thinking about nuclear power. It's just, it's in the options list and it wasn't even before.

[00:01:07] Narrator / A16Z Production: Electric power is civilization. Every socket, every server assumes a grid that works. When Edison wired lower Manhattan in 1882, he connected 85 customers across one square mile. The model that followed, centralized generation one-way transmission, held for more than a century. Now U.S. electricity demand is rising for the first time in decades.

[00:01:33] Narrator / A16Z Production: Data centers, electrified transport, and reshoring are outpacing the efficiency gains that mask years of grid underinvestment. New generation is not the bottleneck. Delivery is. This episode examines two responses, portable nuclear reactors built in a factory, and solid-state power electronics designed to rebuild the grid from the edge. I speak with Doug Bernauer, founder and CEO of Radiant,

[00:02:01] Narrator / A16Z Production: and Drew Beglino, founder and CEO of Heron, alongside A16Z general partner, Aaron Price-Wright.

[00:02:11] Erin Price-Wright: Hey, everybody. We're here to talk about energy and how your companies are playing a role in the sector. But first, let's start with, how do you guys know each other? Yeah, so I'm Doug Bernauer.

[00:02:20] Doug Bernauer: Drew Beglino. And so we know each other, we were both working for Elon about 10 years ago, but at two different companies. So I was at SpaceX, and Elon was really excited. He wanted to build Hyperloop. He wanted to put little cars in a vacuum tube and go super fast. And Drew was a VP of R&D at Tesla at the time, and I called him up and was like, Elon says we need battery packs, we need Model S motor, we need to operate these things in a never-before-operated condition. And Drew was like, do we really? And I was like, yeah, we kind of do.

[00:02:49] Doug Bernauer: But it was kind of like that. And then from there, we did Boring Company also. There was an idea to do like 30 tons of batteries or something on a trailer to power an entire tunnel-boring machine, like one and a half megawatts. So it was a story of power, actually.

[00:03:02] Drew Baglino: Yeah, there was a lot of back and forth on what was possible and could we reuse this or that. And also, a big part of the Hyperloop story, because we published a big white paper, was actually like assessing all the technologies required to deliver the concept, right? Including, for my team it meant looking at like slingshot linear motors that would accelerate the capsule in the vacuum. It was all kinds of fun, never explored physics for our team before. I don't know if you had some of that.

[00:03:29] Doug Bernauer: Yeah, I wasn't roped in that really early stuff. It was more like when it was for real, we're going to do it and we had to build it really fast. That's when I got put into it. And just take the motors from... Just eight months from now, have like people from 23 different countries or whatever it was come and see what you've thought of.

[00:03:43] Drew Baglino: It was pretty wild. But yeah, and as college students, they really ran with it. I mean, it still happens, right? Every year?

[00:03:49] Doug Bernauer: I think they did it three or maybe it was four times and then they stopped it, which is good. It's for the best. It was exciting. It led to some companies. There were some startups and I think it was one really good one based out of the Netherlands and a couple of others also.

[00:04:01] Drew Baglino: It's also fun to see which universities did the best. It totally... Mostly the Europeans, to be honest. Yeah. They crushed it. We'll cut that out there.

[00:04:10] Doug Bernauer: No, but I mean, you should know your competition. And the good thing is like MIT was doing amazing. Delft did really awesome as well, though. And I mean, we should learn as much as we can from that. Delft is in it.

[00:04:21] Erin Price-Wright: Yeah. Incredible engineers going to Delft. Speaking of things that haven't been achieved before, let's use that to segue into your respective companies. Talk about the moment, the insight, the why now that led you to start your respective companies. Doug, let's start with you.

[00:04:33] Doug Bernauer: Oh, man. Yeah, it's a fun story. So I was at SpaceX for 12 years. I joined in 2007. So I joined when they had two failed rockets, no successful rockets. And so I got to work on the first ones that worked.

[00:04:44] Erik Torenberg: And you're like, this is the company to be at.

[00:04:46] Doug Bernauer: Yeah, I just wanted to work on an important mission. And I didn't, I really just cared, kind of like polish one stone of this like great big pyramid that is like some lifetime achievement for someone else even. Right. That's what I wanted. So I joined. I did that. I did the first two Falcon 9s. Did the ground system for it entirely, which involved all the permitting also. So this is like launching a rocket from a military base. There's a lot of like regulatory stuff there.

[00:05:12] Erik Torenberg: Your first foray.

[00:05:14] Doug Bernauer: Yeah. Into the permitting wilderness. Totally. And not to eat up all the time. I worked on like the first rocket with legs called Grasshopper back in 2011. It was a four person team really designing, building the whole thing. The whole thing. And we were reporting directly to Elon. Like just Elon to us four and then building the whole thing. And it was awesome because we did really well. We got lucky a lot of times, but we made a rocket that flew and landed on legs. And then I did all the weird Elon side projects and ideas. So Hyperloop, when he got really serious, I got tapped into that and into the boring company.

[00:05:44] Doug Bernauer: And then Mars colony design. And in doing the Mars colony design, I was looking at how do you take Starship there, make fuel from what's on Mars, make fuel from ice that's there. And if you do that, you need megawatts of power. And I was trying to do it with solar and getting totally stuck and showing Elon these plans that were like four miracles we need on a single mission. And it was just ridiculous. And so Elon was like, you probably should look at nuclear. And that's really the jumping off point, right? I started to learn. And then three years later, I left. I found a radiant and left to go run it.

[00:06:13] Doug Bernauer: And really trying to make mass producible, portable micro reactors. Not for space, but, you know, currently we're focused on a trailer size thing. But also needed in space. Right. Yeah. So I do eventually want to do products for space, but we got to have customers. We got to have funds that are actually there.

[00:06:31] Drew Baglino: Yeah. So a similar story, I guess. And that for me, it goes back to a similar time. So I joined Tesla in 2006. And the reason why I even went there in the first place was because I had done this undergraduate thesis in how to enable New Zealand to meet their Kyoto commitments, if you remember the Kyoto Protocol. And they're an island nation. So it's almost like a microgrid study in disguise. So what are all the resources there? How can you reduce the carbon emissions from all these different sources?

[00:07:01] Drew Baglino: I was focused on transportation in particular. And I became convinced that electrification of transport was not just like a way to solve a carbon problem, but actually just the best thing to do from an economics perspective. And that motivated me to come to Tesla. And then over the almost two decades that I was there, all the technologies progressed over those two decades. Right. Like the power electronics became cheaper. The batteries became cheaper. What you can apply these problem statements to just grew in scope. Right. We proved that electric vehicles could not just be the best vehicles, but also affordable vehicles.

[00:07:29] Drew Baglino: That renewables can come with really affordable storage to help decarbonize the electricity sector. And towards the end of my time at Tesla, I had the opportunity to work on this project called the Master Plan Part 3 project where we were effectively studying, okay, now let's do it for the whole globe. Can we have a sustainable all-electric or largely all-electric sustainable energy future? Is it feasible? Are the resources there? Is the investment reasonable? And the answer was like yes, resounding yes in many ways.

[00:07:58] Drew Baglino: And so I got further commitment that not only was electrification coming to transport, but to like everything. And so the electricity grid needs to grow immensely, you know, three to five X, depending on how you calculate and how much intelligence we need to electricity for. A lot. I think we need a lot. We need a lot. A lot, for sure.

[00:08:15] Doug Bernauer: Everyone can't just be like little intelligent generators and microgrids that like mesh together however they're needed.

[00:08:21] Erik Torenberg: All of the above. We don't have that already? Yeah, right.

[00:08:24] Drew Baglino: Yeah. Which planet is this? Yeah, like maybe humans or that? I'm not sure. Yeah.

[00:08:28] SPEAKER_05: Very energy efficient.

[00:08:30] Drew Baglino: So yeah, I got convinced that we needed a massive scale up of electricity generation, you know, production distribution, transmission and stuff. And I had seen at the same time that while there's so much innovation happening on one side of the wire, there's really been almost no innovation on the grid side of the wire. And that's where I got the conviction to go after power electronics for accelerating electrification, really increasing the scalability and affordability of doing everything that's required to enable electric generation and use. And that's how I got it.

[00:09:28] Drew Baglino: And that's how I got it. And that's how I got it. And that's how I got it. I got it.

[00:09:58] Drew Baglino: And I got it. Well, I got it. I got it. That's how I got it. And I got it.

[00:10:22] Drew Baglino: And that's really started to make a big pushup. electrification. It's an exciting time, I think, because electricity as a carrier is like incredibly flexible and as a pathway to a sustainable energy future, whether it's for intelligence or for heating. I see it as a great thing and want to accelerate it. Yeah, I think though, you know,

[00:10:46] Erik Torenberg: on the flip side of this, the last 40-ish years of efficiency gains we've gotten, which have been super important, it's allowed us to kind of look the other way about the real bottleneck in energy generation on the grid, which is just, which is delivery. And we're so bottlenecked today on the lines that run crisscross across the country. I mean, it's this very complicated,

[00:11:13] Erik Torenberg: giant organic machine. We probably don't have to talk long about that. Everyone's talked about that plenty, but the grid is breaking. You know, so when we think about just, you know, from an investment perspective, the types of things that we're interested in, it's like, how do we actually go about kind of solving that really complicated transmission and delivery challenge with technology?

[00:11:37] Drew Baglino: Yeah. Decades of not a lot of change means like the brightest and most talented people are like, I got to go do something else more impactful with my life. And a lot of those folks actually, like, for example, a lot of the talent in GE went to Korea, right, or Japan, because those were the growth markets. And so you got this almost like hollowing out, or China, right, hollowing out of the knowledge base. And so yeah, we need to reinvest because we're growing again. It's exciting. I mean, it's opportunities for both of us and others to come to make it happen.

[00:12:06] Erin Price-Wright: Yeah. Why don't you flesh out our energy investing thesis a little bit more in terms of what are the types of opportunities we've been involved with or interested in? The why now? You know, is it technical breakthrough? Is it regulatory? Is it some combination? Why don't you flesh out a little

[00:12:21] Erik Torenberg: bit more? Yeah. I mean, you know, this sort of AI moment in time is, it's a good, it's a really good forcing function. I'm actually, I'm very, I'm very grateful for AI for lots of reasons, but it's just, it's bringing to a head a lot of things that have sort of been brewing under the surface for a long time. And it's kind of forcing us to remember how to build large scale infrastructure in the U.S. again, and reminding us that actually energy, energy is really important.

[00:12:51] Erik Torenberg: Getting it to the place where it needs to be is really important. So whether it's data center compute or, you know, the broad, broad-based re-industrialization of sort of the industrial base of the U.S., whether it's defense use cases on the edge or more centrally, you know, all of these technologies that we're investing in at A16Z are kind of demanding access to power. And it's not strictly access to power on the grid. I think what we're seeing is the importance of having

[00:13:21] Erik Torenberg: lots and lots of different types of power generation and a lot more resiliency in the overall system and network. So I think, you know, we all take for granted that when we turn our lights on in the office, you know, when you boot up your computer, there's sort of like a unidirectional line of electrons that go from some sort of massive central power generation station to, you know, power outlet. And what we're seeing and what seems to be necessary with much more spiky, much more

[00:13:49] Erik Torenberg: complicated loads on the grid and off the grid is that resiliency, decentralization, and software-driven workflows really matter. And it's going to be impossible to build out the grid for sort of the max power capacity that we could need even at the, you know, most remote edge use case, like on an army base or something like that. So when we think about our energy thesis, it's, you know, how do we turn this network into a much more software-defined, much more resilient, much more decentralized,

[00:14:17] Erik Torenberg: you know, much more decentralized thing. And so, you know, I think both of your, both of what you're building sort of feeds into that sort of microgrid, behind the meter, on-grid, off-grid, hybrid. We just need to be a lot more flexible and a lot more adaptable to

[00:14:30] Erin Price-Wright: a variety of changing conditions. Doug, it seems like the tide turned on nuclear a few years ago in that, you know, more and more people started to realize the, you know, the importance of criticality of it. What is sort of the progress that we've made as a, as an industry? You know, what have we achieved? And, you know, what are the biggest bottlenecks remaining in terms of, you know, really making

[00:14:50] Doug Bernauer: progress as a country? Yeah. It's a good question. I think there's a bunch of fun ways to answer it. I mean, the one thing I like to say, it sounds a little sensationalist, is that there is no nuclear industry. That's really true. You know, we're kind of, it's almost like we're getting excited about flight before Kitty Hawk, right? To a certain degree. There's a really coming very soon deadline.

[00:15:15] Doug Bernauer: A lot of companies, a lot of little nuclear startups have actually been given access to fuel and facilities and just expedited support from the subject matter experts required to regulate to make sure that these are going to be safe tests. And so by July 4th, several companies will have reactors built that go critical that are fundamentally new designs, completely new and from scratch, but it hasn't happened yet. So it just feels like a little bit of cart before the horse.

[00:15:42] Erik Torenberg: Are you, does that worry you at all? Like?

[00:15:45] Doug Bernauer: Not too much. You know, I've been doing nuclear, well, thinking about it since 2016, but I founded Radiant in 2019 and then for a year just learned how to do reactor design and then raise money in 2020. And just, I never founded a company before, never intended to really do that. And I kind of slow rolled into it. I could have tried to go much faster, but I've stayed totally committed to just building. And actually the funny thing is like in 2020,

[00:16:09] Doug Bernauer: I said in 2026, I will put a full scale reactor and get it critical and get it up to full power. And we're on schedule to do that, which is kind of wild. And it's not like that was really the actual plan, but it was just, I was resilient to all the challenges that were put in the way. We are now the only reactor permitted to, of these new reactors to go to full power. So a lot of others are getting to critical, which doesn't mean you get to high temperatures or high power. And those things

[00:16:35] Doug Bernauer: are very challenging on all the parts in the system, right? And they require careful consideration of the thermal gradients and the alloys, right? You need high strength materials to do that. So that's really exciting, but we're like not quite there yet. And I think if we're doing the same discussion next year, it's going to be dramatically different because we're going to be able to point at all these different designs, what you could do with them. And I think the products like nuclear reactors as products has never been seen before. All right. There are always usually these

[00:17:05] Doug Bernauer: giant mega projects where you dig a huge hole in the ground and you take five to 10 years or up to 15 for the slower, the bad projects out there. But reactors that can just come ours, you know, we're targeting one per week coming off of a production line from our Tennessee facility, which is an 80 acre site we just signed for in October, not even a year ago. But I want to tie back into the grid because I was just, I had some interesting thoughts and we

[00:17:31] Doug Bernauer: really, our product is for off the grid, right? So megawatt reactor on a trailer and you can, we build in our factory, we drive it or fly it to where the customer wants it to go and then turn it on within like 48 hours. We go, you know, wheels stop moving and then we go to power on your site in that amount of time. And then it lasts five years, which is like a full oil tanker worth of diesel equivalent. It's 2 million gallon diesel equivalent. So it's sort of an unbelievable thing

[00:17:58] Doug Bernauer: where you can grow the grid or put a microgrid anywhere. But it's like a, it's a totally different problem. I think from the grid itself is civilization, right? Electric power is civilization. If you go and there's sockets and you pop something into them and you just get power, that's very well developed. That's a civilization and that's using electricity to do what you could otherwise only do with human muscle or animal muscle. And then I'm excited about Drew's products and company,

[00:18:29] Doug Bernauer: what it can do for the grid, but also for microgrids. And it'd be fun to hear your thoughts on how these things mesh together actually. Cause we had talked about like where do our products actually go together? Yeah. Yeah. So maybe, uh, and talk, talk about your product. I know you have like a power building block

[00:18:44] Drew Baglino: of a certain size. Yeah, for sure. We're, we're building, our first product is Heron Link and it's a, uh, it's a five megawatt, uh, bidirectional, uh, solid state transformer that goes from DC anywhere from 800 to 1500 volts DC to 34,000 volts AC, which is effectively that, that AC voltages is the sub-transmission voltage of data centers of large, you know, battery power plants

[00:19:12] Drew Baglino: of, of solar facilities. Really it is the highest distribution voltage on the, on the grid around us. So if you look at the wires on top of a pole, you know, specifically the ones that are way up top, you know, the highest voltage those will ever be is 34,000 volts. So we're going after all of the distribution, um, voltages in the world. Uh, Europe is the same. So is Asia. And our first product is DC because that's about a 500 gigawatt market growing quickly, uh, of, you know, data centers, solar and

[00:19:42] Drew Baglino: batteries, solar and batteries. But future products will be AC to AC. Um, and that allows you, you to do, you know, all the utility use cases and, and use cases inside of, you know, commercial buildings like this building we're in right now, they can all benefit from AC to AC. And what, what is, what is the solid state transfer? What is it actually doing? Right. It's, it's, um,

[00:20:04] Drew Baglino: power semiconductors and software. And instead of converting voltage at line frequency using large coils of wire around like magnetic steel in a bucket of oil, which is how transformers generally are done, you're doing it at really high frequency with much, much smaller, simpler magnetic materials to produce called like fer, you know, uh, ferrites, um, using switching devices. And, and you've,

[00:20:33] Drew Baglino: you've charged a smartphone before, like that little object, that little power brick that you have in your hand, you know, it's doing conversion from 120 or 240 volts AC to five volts, uh, DC to charge your phone. And it's switching at a million times a second. There's like tiny little GAN gallium nitride devices switching a million times a second, uh, voltage across a transformer that's smaller than a

[00:20:59] Drew Baglino: pencil eraser. Um, and you know, if you remember back to maybe you had a laptop in the nineties or something like that, or you did, I don't know. Um, and the giant power brick that you were carrying around that was really hot when you stuck it in your backpack after charging your, your, your computer, like just in a couple of decades, you know, you've seen more than an order of magnitude power density improvement there and efficiency improvement. Um, now you can do like multiple outputs and the seven different voltages. And, you know, we're trying to do the same thing,

[00:21:28] Drew Baglino: but not for commercial electronics, but for industrial scale electronics and our building block, as you said, it's a modular architecture. So that five megawatt parent link, it's got 30, 165 kilowatt, you know, modules inside the product itself was fail operational. If one of those fails, we just keep operating. So we're like oriented at rugged. A whole building could power off of one

[00:21:48] Doug Bernauer: of those blocks, right? You can just switch your distribution to some modern. Yeah. And I like to for control. Yeah. Yeah. And I like to think of it as though, like if the grid is civilization itself and everything is routed in AC and there's some much, much better way you can like, you know, metamorphosize the entire grid, like have civilization can regrow off of a new architecture of moving power. And I of course, I'd like to think about the first power that you put on another world. Like

[00:22:16] Doug Bernauer: if you put a megawatt on the moon or on Mars, distributing that will like set the precedent for how you do, like what, what the technology type will be. Will you plug into a DC thing or will you plug

[00:22:27] Drew Baglino: in the, the two, the two prongs that we're used to in the US at least? Well, either way, because I'm not going to take a big stance one way or the other. It's like you should be using software and semiconductors, you know, which are higher efficiency, you know, much less mass and size, especially that matters when you're going to space. Like you don't want to skip this thinking

[00:22:46] Doug Bernauer: way. I think there's less oil. I think the big can of oil, the big bucket of oil thing for the transformer is hard on Mars. Yeah, exactly. It's limiting. So it's, it's really exciting.

[00:22:55] Drew Baglino: It's just a leapfrog thing, right? Like let's use software and electronics rather than like mechanical systems to accomplish our power distribution. We went like super nerdy on

[00:23:04] Doug Bernauer: this, which is perfect. But our reactor, like fundamentally makes DC power because we actually run a really compact power generator. Perfect narrative. And it runs, yeah, exactly.

[00:23:13] SPEAKER_05: So the greatest civilization, you are pushing civilization an inch forward.

[00:23:19] Doug Bernauer: Yeah. It's civilization anew, right? And it can grow from the edges where our system makes sense for people with a critical need for power, for resilient energy at a military base or hospital or for disaster relief. Yeah. Yeah. And I think that's it. There's no reason you have to use AC actually as the way to move that power.

[00:23:36] Erik Torenberg: And the idea that the grid can grow and move from the edge is just not something that we've really been able to process for the last 50 years in the U.S. Like the grid is a, you know, has been a very top down project. And if you want to attach back into the grid as all these data center people are realizing now. So many studies. It's a huge nightmare. It's a nightmare. Yeah. Yeah. And so how do you like make it easier to do that kind of organic?

[00:24:02] Drew Baglino: Part of that is because the underpinning of the grid is these mechanical systems that are not fast responding, that don't have a lot of telemetry. No software. Yeah. Well, if there is software, it's very slow to respond. And so you don't, it is harder in a world like that to imagine a bidirectional grid, right? Like it's the central planning from inside out, you know, when you're thinking about protection and like, you know, can I stay within the load ratings of these lines?

[00:24:31] Drew Baglino: When you don't have the infrastructure to dynamically control it the way you want, like you're stuck. So I think we're, it's an enabling alternative.

[00:24:39] Doug Bernauer: Yeah. I think one of the things that it could do for people is you have a DC battery. We go DC to AC, right? On these, all these, so attach some like large battery system.

[00:24:49] SPEAKER_04: Yeah.

[00:24:50] Doug Bernauer: And then maybe, you know, you have a solar grid, but that's on some different DC voltage. And that also needs to get converted AC to then put on a grid to use it. But you could have little cells, like these things that we grow at the edge. It could be like megawatt hour battery packs, a few megawatts of solar for during the day and a reactor for at night. And all those things actually merge and work perfectly on a DC grid, like a DC microgrid. That's, that's sort of what it, I think what it, what it could do, right? Is it, it's interesting for people to think about this.

[00:25:18] Doug Bernauer: I think it could be demonstrated at some military installation or some other place. And so it's like a fun thing that Drew and I have chatted about a little bit, but there's no, we don't know when we'll be able to do it.

[00:25:30] SPEAKER_05: Yeah.

[00:25:31] Drew Baglino: That's right.

[00:25:31] SPEAKER_05: Full power.

[00:25:32] Drew Baglino: Get to power. The only thing to consider is compute also is natively DC. So it, you know, you're in this interest. Yeah, exactly. Compute, batteries, solar. All the new technologies. Micronuclear.

[00:25:42] Doug Bernauer: Yeah. Actually all DC. Micronuclear.

[00:25:44] Drew Baglino: Yeah. I like it. I think it's, I think I've talked to other folks about like, what is, what is a modular reactor, right? Like you hear of SMRs. And it's like, this is, this in my mind is absolutely like the definition of, of SMR, one megawatt versus like, you've heard about this hundred megawatt SMR.

[00:26:01] Doug Bernauer: Yeah. Micronuclear is a term no one's using, I think. Well, I think it's new right now. Like we just said it. Oh, good. And then someone else said it. And as soon as two people say it, that's it. It's creation. It's done. It's Andal and Hammer. It's, it's in stone now.

[00:26:15] Drew Baglino: It's like mainframe versus PC, but a lot of nuclear. And the PC one, like the data centers look like PCs that don't look like mainframes. And there's a reason why.

[00:26:23] Doug Bernauer: Yeah. Well, SMR can represent like a hundred megawatt thing, building it, digging a big hole in the ground. It's not necessarily going to run. It has to run faster than 60 Hertz for it to be DC source, right? I actually make AC because every heat engine, you spin something. But we do it at such a high speed that we then use active rectifiers to convert to DC as the first step. Yeah.

[00:26:43] Erik Torenberg: So I think, you know, one thing that's interesting about both of your approaches, and I'm curious how much of this comes back to your time at Tesla's SpaceX respectively, but you're both like very focused on manufacturability and modularity and modularity of design. Yeah. Yeah. Maybe you should talk, I'd be curious to hear both of your thoughts about that.

[00:27:02] Drew Baglino: I find that there, there's this sweet spot between like capital investment and like manufacturing cost of goods sold. And you're always trying to find that with any, with any product. Right. And if you just compare stick building a power plant in the, in the field versus, you know, fully integrating like on a highly automated line, that same function, the total cost will always win if you can do it on a high, on a highly automated line. And so, you know,

[00:27:32] Drew Baglino: we're building for our first factory, we're building a 40 gigawatt factory and people are like, wow, that's a lot.

[00:27:36] Erik Torenberg: Well, contextualize what is 40 gigawatts.

[00:27:39] Drew Baglino: Yeah. 40 gigawatts a year. So it's about, it's about 10 to 15% of the ex-China market for our product category. And it's equivalent to half the state of Texas in peak power. If you want to think about it in that term, then it's kind of useful. I'd say 4% of the whole country is electric power, isn't it? Yeah. Yeah. Something like that. Between 500 gigawatts and a terawatt, depending on how you think about it. So yeah, 40 gigawatts

[00:28:06] Drew Baglino: a year is, I mean, it's significant in the overall US. And why 40 gigawatts? One, you know, looking at it from market sizing perspective, but the other is, hey, like right around 60 second tack time is where you maximize that like capital efficiency of building a factory. And if you look at our module size and you look at 60 second tack time, it sort of works out to 40 gigawatt spot. And, you know, I, we're going to ramp that factory. I hope,

[00:28:34] Drew Baglino: I expect us to exceed the demand for that factory, but you get so much quality and cost benefits going for full on as much automation as you can, not too much, but as much automation as you can. Yeah. It's more than just that, but that's, that's the first two things that come to my mind, quality and cost.

[00:28:52] Doug Bernauer: Yeah. I mean, you think of it as such a huge scale. I definitely 100% agree with the less, like I think you said stick building and it's like the opposite of that is mass production. Right. Thinking about doing it all in a factory and that's our entire approach is like a nuclear reactor.

[00:29:09] Erik Torenberg: It was pretty radical for a nuclear reactor. The idea that you would build it in a factory.

[00:29:13] Doug Bernauer: Absolutely. Yeah. So it's really, we're doing nuclear reactors as products for the first time ever. And it's so that you can just, you can say, yeah, I want nuclear power and we deliver it, it operates. And then when it's done operating, we take it away and there's no waste or other tricky consideration you have to make. You know, it's totally safe on the customer site. We actually use a meltdown proof fuel. And it makes this like completely new way. I think of thinking about nuclear power. It's just, it's in the options list. And I think it's, it wasn't even before.

[00:29:41] Doug Bernauer: Not only is it there, but it can look better than almost every other form of power. And I, and I don't like to, you know, imagine that it's the only thing you want to do. You're, I really like the idea of like solar and battery and nuclear and like put that, that whole, that whole block somewhere. Yeah. Right. And use all of the free energy that's out there because the sunlight is free. You put up a panel, you're getting it. It's very cool, but also uranium is free. It's in the ground. It's not flying through the air. It's there. If we take it and we use it before it spontaneously undergoes fission, it just goes away,

[00:30:09] Doug Bernauer: which it's been doing. So like when the earth formed a few billion, four billion years ago, we had like 128 times as much uranium-235. So we better get it before it's gone. Yeah. The same way as like you'd put up a panel and catch some sun, like take it out of the ground, use it. Don't let it turn into radon and other stuff that is actually harmful to someone's health. It's like, it's more dangerous from a health perspective, leave it in the ground. And it's a total waste of the power. And there's a bunch of cool like ideas like this and a new way of like

[00:30:36] Doug Bernauer: really seeing nuclear that I've written, I think called Adams for Prosperity. That's on our website. I released it about a year ago, but it has this and like, how should you think about radiation and waste and reactors and what's possible?

[00:30:48] Drew Baglino: Yeah. I think there's another thing that you're not stressing enough about that in-field work content being really low. So, you know, when I was at Tesla, I was responsible for the Megapack product development and then mass manufacturing and the business of selling them. And the less involved the onsite project is, just the faster everything about it will go. Like the perennial. Racks show up. Yeah. Racks of batteries.

[00:31:15] Drew Baglino: Yeah. Just like land, land the cabinet, you know. In fact, we even work past the pad, like we got rid of the concrete, wherever the seismic would allow. It's awesome. It just did soil nails. Because again, you're disturbing less dirt, you know, there's less concern about like, you know, how much you need to grade or what are you going to do with a, you build an architectural type scope. The local community, especially in your case, if it's like a temporary installation, they're going to feel less concerned about it. And the fact

[00:31:44] Drew Baglino: that you can just pick it up and remove it if for whatever reason it needs to be, which you can also do with Megapacks. It eases this, transmit this transition into these new technologies and consider that, compare that to like a giant nuclear cooling tower visible for miles around. Yeah. It's such a different approach. And in today's world where like not everybody is a Yimby, I guess in my backyard. Yeah. Having a, you know, rapidly deployable, let's say.

[00:32:11] Doug Bernauer: I thought NIMBY meant nuclear in my backyard.

[00:32:15] Drew Baglino: You thought NIMBY. Yeah. So we should re-brand NIMBY.

[00:32:17] SPEAKER_05: Re-brand NIMBY. Let's bring it back.

[00:32:19] Drew Baglino: Yimby the new. Dang it. I got a problem here. I love it. I love it. Sorry. Go ahead. No, I mean, I think that's what you get with that modular approach. You get logistics simplification, you get quick install, and you get simpler permit and access to.

[00:32:34] Doug Bernauer: No skyline. Yeah. It's really infrastructure free. Yeah. Just clean power wherever you want it over a weekend. Yeah.

[00:32:40] Erik Torenberg: Well, but so, I mean, you built, you helped build factories that made rocket ships. How, it seems like building a factory that builds a nuclear reactor, that's pretty hard. What's that, you know, what's the experience then like? So you're just getting going.

[00:32:57] Doug Bernauer: Everything's a factory. We are building a nuclear reactor in our first building that we had, and it's like a 70,000 square foot. That's very cool. That we have right now. We have two buildings. We had to get a second one in November because we filled up the first building, because we start doing a little bit more vertical integration, a little more of the machining in-house, and all that's happened to us already. But we'll be able to build up to 10 reactors in those facilities that we have. We both know Elon will operate out of a tent.

[00:33:24] Doug Bernauer: So this is like quite a bit fancier to have real walls. But in Tennessee, we have an 80-acre site. We have the first building going up, which is made for just fuel handling, because that's the tricky bit. And so we're working the regulatory permit path right now on that. We should be able to put fuel reactors there. And so we'll initially be building everywhere we can possibly find, like a building with enough power, right? And then moving all the parts to Tennessee to then get the fuel loaded there to then take it out to the customer site.

[00:33:52] Doug Bernauer: It's nice that it's mobile, so we can actually do all of that. But the factory itself is a bunch of other buildings on that site, and most of it is like normal assembly work. Like you've got big structures that you're welding, bolting things together, right? Putting wire harnesses and things on the unit. But the factory will have to evolve multiple times also. A factory before Gigafactory, right, is a different thing.

[00:34:15] Drew Baglino: You know the process, right? Automate is last.

[00:34:18] Doug Bernauer: Yeah. Yeah, if you're trying to delete the steps and done all the other smart stuff. Exactly. Of course. So yeah, we're just building and learning what does actually the factory look like. But parts of the production line that can be automated and should be will then go in those newer buildings. Yeah.

[00:34:35] Drew Baglino: We're doing the same thing, right? Like we're building our first prototypes largely by hand, you know, in our engineering facilities. We're doing about 10 of those this year. We'll do another like 30 to 50 prototype systems this time in our factory location, which we hope to announce next quarter. And then only from the learnings of those two builds will we go and automate from there. And you just got to get the reps.

[00:35:00] Erin Price-Wright: How should we think about how micro reactors fit within the broader energy landscape? Do they compete with large centralized plants? Do they complement them? Are they serving different categories of demand? How should we think about it?

[00:35:09] Doug Bernauer: Yeah. So they're definitely an off-grid product. So they don't at all compete with larger reactors. Really, if you can build, if you have time to dig a big hole in the ground and put a reactor in that way, then you can do a larger reactor. Maybe five or 10 times as big as the one megawatt size that we're looking at. And it's going to win on economics. It definitely should. We're already using one of the fanciest forms of fuel and that is so that we can set it up anywhere and have it not be a risk to people or facilities nearby.

[00:35:39] Doug Bernauer: And so we don't compete at all with those things. One of the ways I like to talk about this is you could run a diesel generator or you can run a nuclear reactor. And you're really deciding between those two things. And we don't beat like super cheap diesel. Like we beat diesel at like $6.50 a gallon. That kind of a number. So that's where our initial customers need to be. But if you go start looking at what people pay for diesel and what they pay on the edges, not on like the center of the bell curve, the average for like a country or an area.

[00:36:07] Doug Bernauer: Like you look at the tough regions, they're paying a lot. And so there's plenty of customers out there. And one...

[00:36:14] Erik Torenberg: Some examples, I think.

[00:36:15] Doug Bernauer: Oh, like $10 a gallon is the average in Hong Kong. I think like Iceland and Scandinavia, Northern Europe, those regions are like $7, $8, $9 per gallon for a whole country, actually. So like it's very easy to see. The market is massive. And islands. Yeah. Yeah, islands. Absolutely. I mean, Hawaii is pretty high electricity costs and it's, I think, 80% diesel powered, actually. It's got wind and solar that make up the remainder.

[00:36:44] Doug Bernauer: But yeah, you could have a cleaner form of power, right? No emissions. The nuclear reactor operates and then rain, it takes it. And we handle all the complexity. But the amount of power people need, right? They need in the gigawatts for the grid. And so we don't really do that. We have the niche customers on the edge and we don't want to make, right, thousands and thousands of reactors. At 50 a year, we'll have something in the range of like a thousand or two at the most. But we don't consider, we don't look at it and go, hey, could we make it work for 10,000?

[00:37:14] Doug Bernauer: There's different products and we can do it at better economies. And there's a couple of ways to do it. But we're, Raiden doesn't want to dig a hole in the ground and solve that other miracle. It's too many miracles. I think it's important to be able to do it again, but it's not on us to fix it right away.

[00:37:30] Drew Baglino: Yeah. Series miracles. You don't want to have too many in a startup.

[00:37:33] Doug Bernauer: Yeah.

[00:37:33] SPEAKER_05: You need some.

[00:37:34] Doug Bernauer: Yeah. Yeah. But one miracle that leads to then a product and revenue, right? That's the way. And then you can, then you have time to think about another miracle. Totally.

[00:37:44] Erin Price-Wright: So you mentioned that we're very early in the nuclear industry, you know, we're even pre the nuclear industry in some sense. So what is the milestone or the KPI or what would need to be true for us to say we as a country, you know, the nuclear industry is here and flourishing?

[00:38:00] Doug Bernauer: I think a couple of things. So we could have access to nuclear fuel and enrichment that are like in completely competitive free markets where there are innovative startups fixing and solving those challenges. We should have a waste storage facility. That's some centralized repository, which is way safer for the existing nuclear fleet that's operated since the sixties. That's an unsolved problem.

[00:38:27] Doug Bernauer: And that would, those things alone would cause everything else to flourish because we already have this like middle layer of me and a bunch of other startups trying to get fuel and operate reactors. And then if we're able to, as a country, really have a better system to deal with nuclear waste, which actually radium doesn't need. Like our uniquely at this really small size, we can just put it into dry cask on about 10 acres of our 80 acre site. And that works for like 60 years worth of reactors. And we can always expand and do more.

[00:38:57] Doug Bernauer: And, you know, the nuclear waste has got high reactivity elements that last like 100 years. And after that, it's pretty benign. But we already have a waste isolation pilot plant in New Mexico, which is like this deep borehole down inside of a salt structure. So it's like a salt dome. This is where defense waste already goes. And they just said they were going to build it and they built it. And meanwhile, we struggle still on the DOE side to build a repository for big nuclear plants.

[00:39:26] Doug Bernauer: And, you know, because of that, these gigawatt scale plants are operating, generating nuclear waste on and they have to store it at the same site where they're making power. And in California, this is like coastal regions that like are risky, that where like you can have a tsunami or something instead of taking it and putting it in a salt dome structure in the high desert where there's no water, no risk of like certain natural disasters. So it's just a smarter, safer, better idea. And we don't do it. Yeah. And actually, it was a huge cost. It's a commitment as well.

[00:39:56] Drew Baglino: Like you got to demonstrate that commitment.

[00:39:57] Erik Torenberg: It's the, and it's also the NIMBY transition that not in my backyard to nuclear in my backyard. Yeah. We need that. Well, you, I mean, I think that you mentioned also the sort of nuclear fuel supply chain. It's something Drew, you and I have talked about on the power electronics side, how important the supply chain is, how focused you are on it as well. I think you're lucky that your biggest silicon carbide supplier is a U.S. company. It's a technology developed in the U.S.

[00:40:24] Erik Torenberg: But what other parts of your supply chain and are you worried about?

[00:40:30] Drew Baglino: Yeah.

[00:40:31] Erik Torenberg: Or thinking about?

[00:40:32] Drew Baglino: Yeah, for sure. So I mentioned there's ferrite is a pretty important ingredient in these high frequency transformers. It's only, it's basically just iron oxide. So it doesn't have maybe a little sprinkling of manganese. So it's not, there's no rare earth in the ferrite, but the world's largest ferrite companies are in Asia, right? It's like every other, you know, complex supplied good. Now, there have been ferrite manufacturing facilities in the U.S. before. I'm working to bring them back.

[00:41:01] Drew Baglino: In fact, one of them is nearby and in Georgia and could be brought back with some coaxing and I'm working on it with the parent company. Another is thin film caps, capacitors. There's a decent amount of, they call it power electronics, but they should really call it power capacitors because the things you mostly see are the capacitors. And the same sort of thing, you know, supply based largely in Asia, working with those same vendors to bring it closer.

[00:41:31] Drew Baglino: No rare earth materials there, you know, mostly polymers and, you know, thin copper or thin aluminum conductors. We already have a pretty well established like copper and aluminum supply chain. You're just saying like a small wire gauge? I mean, it's like micron thin sheets. Sheets. Yeah. Okay. Yeah. Copper and aluminum foil. They're really foils. And then that's, that's what's in a thin film. Okay. Sorry. Okay. Got it.

[00:41:59] Drew Baglino: So yeah, those are, I think the critical aspects of power electronics. Everything else is already like very abundant and easily disforsed in the United States. So your, your plastics, your sheet metals, your aluminum castings, bus bars and things. So, you know, because of that, we can really focus on those three key commodities and we do have plans for each to both near shore and on shore if they're not already. And like, I'm excited about that because I see power electronics really moving from the

[00:42:29] Drew Baglino: like device scale I was describing of, of, you know, charging your, your laptop or where it's largely been stuck more recently, like in EVs and, and, and solar and storage to the grid itself. And when you do that, it, you know, you're like, oh, 40 gigawatts. That's the state of Texas. But it's actually not like that because you have power conversion all the way along the way, right? You have it, you have some power conversion going on at the generating facility to go

[00:42:57] Drew Baglino: from some lower voltage to a media voltage like 34,000 volts. And then you have another power conversion system going from that intermediate voltage, 34 KV, let's say to the main transmission voltage, hundreds of kilovolts. And then you have to do it again on the other side when you get into the community. So you might have an 80 gigawatt peak grid in Texas, but you actually have like 800 gigawatts of power electronics actually supporting that grid. So, so I'm excited.

[00:43:26] Drew Baglino: I guess what I'm saying is, is, is while, and this is a useful piece of context, last year about three terawatts, and these are big numbers of power semiconductors when it's electric vehicles. And the peak grid power is less than a terawatt in the U.S. So these are really like on the same scale kind of opportunities.

[00:43:44] Erik Torenberg: And this is solvable.

[00:43:45] Drew Baglino: It's a solvable one, yeah. And, and, and I'm, I'm like really motivated by these, how much these supply chains have scaled up to support electric vehicles. And electric vehicle growth is slowing down, which means we can take that momentum and bring it into a new problem statement, which is power for data centers, power for industrialization, power for economic growth and prosperity, and, and for sustainable energy. So I'm, yeah, it's, it's an exciting time, I would say.

[00:44:10] Erin Price-Wright: Let's talk a bit about data centers. There's a lot of controversy around them. How should we think about what is, what is the impact? Are they causing problems on the grid, et cetera?

[00:44:18] Drew Baglino: Yeah, it's, it's a, there's two sides to this one. But I think in general, like if you zoom out, data centers are overall going to be really good for the grid. And I'll, I'll kind of explain maybe why they get a bad rap and how that's going to change. So just, I think yesterday I saw a headline about two gigawatts of data centers turning off instantaneously in Virginia over the weekend or last week or something like that.

[00:44:43] Drew Baglino: That is the reason I see why there's a lot of concern about, about data centers on the grid, like from the grid operator perspective. And, and they are designed to date. They have been designed to do that, right? They want to keep their compute up. They want their six nines. So anytime there's anything funky on the grid, they isolate and, and run off of their backup generation or UPSs. And then ultimately backup generation. And when a data center is 10 megawatts in a grid, that's hundreds of megawatts or gigawatts,

[00:45:13] Drew Baglino: that doesn't matter. But when you're building gigawatt data centers, it starts to really matter. And the grid stability is at risk. And so that is very solvable with software, modern power electronics, you know, dynamic grid forming controls and your rectifiers and the data centers. They can stay online through those cases with a little bit of energy storage and, and, and actually stabilize the grid rather than destabilize it. So that is like a solvable one, but it is, it is a problem that is real.

[00:45:41] Drew Baglino: Like it happened in Washington state, just happened in Virginia. It needs to be resolved as these data centers keep becoming bigger and larger percentages of the grid.

[00:45:49] Erik Torenberg: And I think it's, it's a, it's a function both of the data center design up until now and how they are able to connect to the grid, which today is, you know, very dumb systems. Yeah. And it needs to be more interactive.

[00:46:00] Drew Baglino: Absolutely. Yeah. And it can be so much more interactive with, with better software and with more understanding of the capability.

[00:46:06] SPEAKER_04: Yeah.

[00:46:06] Drew Baglino: But then there's this other commentary about how data centers are going to increase rates, which I, I think if doesn't make sense to me on a big picture and, and it's, it's really simple, like physics of electricity rates, right? Electricity rates are costs to maintain the electricity grid or the, to deliver electricity altogether divided by total kilowatt hours delivered. Right. And the data center customer is like the ideal customer.

[00:46:34] Drew Baglino: They're consuming like near their maximum power almost all the time compared to like your house where you, you're like maybe at 10% of the maximum power of your house, like an hour a day. Right. So they are the best customer to serve in terms of delivering more kilowatt hours. And then, and then the way utilities generally do is they like take all the kilowatt hours in and they look at all of their costs and they, you know, spread it across everybody.

[00:46:59] Drew Baglino: So the more data center load, like more loads we have like data centers, like factories, um, that are steady constant loads, the, the cost of serving electricity to everybody will go down because they are the, they are increasing that numerate, the denominator, right? Like utilization.

[00:47:17] Erik Torenberg: Yeah. The utilization is going up. Right. Um, so the average is getting better for everybody.

[00:47:21] Drew Baglino: Yeah. And, and I think, you know, there's concern about the power side. Oh, will there be enough power? But I think what we've seen, and actually last year, the U S had, had one of the highest power additions to the, to the grid ever. And this year is by far going to be the highest capacity addition to the grid ever. So new power is not the problem. Delivery is the problem. And, and, uh, data centers by increasing the utilization of the delivery system, make delivery more affordable. So I, I think net net, they will actually drive rates down.

[00:47:50] Erin Price-Wright: Cool. Well, I think that's a good place to, to wrap. Don't you? Thanks so much for coming to the podcast. Thank you. Thank you. Thank you. It was great.

[00:47:59] Narrator / A16Z Production: Thanks for listening to this episode of the A16Z podcast. If you liked this episode, be sure to like, comment, subscribe, leave us a rating or review and share it with your friends and family. For more episodes, go to YouTube, Apple podcasts, and Spotify. Follow us on X, A16Z and subscribe to our sub stack at A16Z.substack.com. Thanks again for listening. And I'll see you in the next episode. As a reminder, the content here is for informational purposes only.

[00:48:27] Narrator / A16Z Production: Should not be taken as legal business tax or investment advice, or be used to evaluate any investment or security, and is not directed at any investors or potential investors in any A16Z fund. Please note that A16Z and its affiliates may also maintain investments in the companies discussed in this podcast. For more details, including a link to our investments, please see A16Z.com forward slash disclosures.