[00:00:00] Matthew Steckman: Yeah, I mean you basically can't have a defense company if you don't have a large US business. The government thinks that we can deliver some pretty major stuff now and in the future. There are very few drone programs that would create a material enough amount of revenue to actually create a real business. There are lots of VC companies I would love to buy if I had an unlimited checkbook.

[00:00:20] Harry Stebbings: Is there other like an ethical question of like, do we agree with sending thousands of missiles to Iran?

[00:00:26] Harry Stebbings: This is 20VC with me, Harry Stebbings and today I'm so excited for one of the most current shows we could do. We've got Matthew Steckman, President and CBO, Chief Business Officer for Anduril. Just last week they announced a monster $20 billion contract with the US military, one of the largest ever. We could not have a more apt or pertinent guest as he takes us behind the scenes of both the contract and of Anduril.

[00:00:53] Harry Stebbings: But before we dive into the show today, over 80% of Fortune 100 companies are running their businesses with Airtable. Airtable combines AI with the scale of an award-winning infinitely flexible no-code system. A platform where you can see all of your data in one place and use it to make really big picture decisions. Think of it like mission control for your company.

[00:01:15] Harry Stebbings: Airtable goes beyond organization and automating repetitive tasks. It lets you use your data to inform strategy, monitor progress and take action. Every cell is capable of performing hundreds of AI-powered tasks like web research or localization and using those results to inform and update hundreds or thousands of other cells and workflows in real time.

[00:01:37] Harry Stebbings: Unlock the true scale of your workflows at www.airtable.com forward slash 20vcairtable, the infrastructure of innovation. And just like Airtable organizes your workflow data, MetaView organizes your conversation insights. This episode is brought to you by MetaView. Who says hiring has to be fair? Every founder, VC, and exec I speak with knows this. Your ability to hire is the biggest constraint on your company's growth.

[00:02:05] Harry Stebbings: But recruiting is slow, it's subjective, and only getting more competitive. And that's why teams like Eleven Labs, Brex, Replit, Deal, and 5,000 other organizations use MetaView. The AI company giving high-performance teams a real unfair advantage in hiring. MetaView's built a suite of AI agents that behave like recruiting coworkers. They proactively find candidates, they take interview notes automatically, and they help you surface the best candidates in process.

[00:02:32] Harry Stebbings: For the first time, AI handles the recruiting toil and gives you a single source of truth. That means hours saved per hire and a team focused on what matters most, winning the right candidates as fast as possible. Don't let your competitors out-hire you. MetaView customers close roles 30% faster. Try MetaView today and get a free month of sourcing at metaview.ai forward slash 20VC.

[00:02:58] Harry Stebbings: After MetaView captures what was said, Turing helps you build with the people who can deliver after it. Frontier Labs keep facing the same limitation. Models perform well on benchmarks, but they fall short once they enter real coding tasks, real tools, and real workflows. That disconnect between synthetic evaluation and actual system behavior is now a core blocker for organic models. That's why NVIDIA, Anthropix, Salesforce, Gemini, and other leading lab partners partner with Turing.

[00:03:25] Harry Stebbings: Turing is the research accelerator focused on post-training reliability. They build realistic RL environments, next-generation data quality systems built from real-world operational traces, and coding datasets that stress models under conditions where failures matter, state changes, workflow branching, brittle tool calls, and the coding errors that break RL agents but never appear in benchmark reports.

[00:03:49] Harry Stebbings: In reality, a model may demonstrate correct reasoning in your evaluation setup, yet still select the wrong parameter, or mishandle a code update in a realistic interface. Turing makes that failure visible and gives teams the signal they need to fix it. For labs advancing agentic systems, Turing provides the structure required to understand why these failures occur. To find out how, visit Turing.com forward slash 20VC. That's T-U-R-I-N-G dot com forward slash 20VC.

[00:04:18] Harry Stebbings: You have now arrived at your destination. Matt, I am so excited for this dude. I just got off a chat with Christian Garrett and Matt Grimm, and they gave me incredibly tough questions. So this is going to be a grueling hour for you. Here we go. But thank you for joining me, dude. Yeah, thanks for having me. It's really great to be here. I actually want to start with Trey, weirdly, which was Christian Garrett said that I had to ask this. He said, what was Trey like at Georgetown?

[00:04:47] Harry Stebbings: And what is it about the Andrewill founding team that has made Andrewill so successful?

[00:04:53] Matthew Steckman: Yeah, well, Trey and I were classmates, met freshman year, played Ultimate Frisbee together. So we went on a lot of road trips with one another. I don't think Trey has changed at all. You ever seen the movie Hot Tub Time Machine?

[00:05:05] Harry Stebbings: Yeah.

[00:05:06] Matthew Steckman: Yeah, great movie. Yeah, there's a line in it that's like, every group of friends has an asshole, but Trey is our asshole.

[00:05:12] Harry Stebbings: You know what I'm saying?

[00:05:14] Matthew Steckman: Yeah, that's Trey in a nutshell.

[00:05:16] Harry Stebbings: And he's gone on to such things.

[00:05:17] Matthew Steckman: It's crazy how that works.

[00:05:19] Harry Stebbings: Yeah. It's because hope for you. Do you know what? I've never had such a weird start to a show. There you go. It's like a movie reference. Yeah, we're definitely kicking this off right. And then Trey's our asshole. Yeah, yeah, yeah. He'll love that one. Yeah. In terms of the team itself, I have so many defense companies pitch me. I think, bluntly, the team is always lacking. What do you think it is about the team that Andrew has in terms of founding team that has made it so successful?

[00:05:47] Matthew Steckman: There's kind of some magic in the fact that it's the same leadership team today as it was when we started the company. That implies a whole lot of things. I think mainly it's that we're all friends. So I think that's actually pretty critical. There's a bond there that basically can't be separated by business or stress or life. We all know each other really well.

[00:06:07] Matthew Steckman: But then on top of that, we all come at the industry from really different backgrounds and lenses, especially in defense, which is it's like everything works against you to get into the defense market. It's like every headwind you could possibly imagine. If you don't have a lot of perspective and knowledge about what's about to come, it's hard to think around corners and you get yourself kind of mixed up and gummed up a lot.

[00:06:32] Matthew Steckman: And so when you meet founding teams, one of the most important things in defense is some of them can be outsiders and brilliant technologists and thinkers. It does take a lot of inside knowledge. One of the things we got right and keep getting right is that blend of the outside-inside process. Who can think differently and bring in sort of commercial perspective, high-tech perspective, add kind of entropy into the system.

[00:06:58] Matthew Steckman: And then who can really deeply represent our customers, how they think. How does that come together uniquely? That becomes super important to having any success in the defense world.

[00:07:09] Harry Stebbings: I think one of the things I most look for, honestly, is like GTM experience and ability in a team that I'm looking at in defense. How should we think about analyzing teams for their ability to actually sell and go through procurement? Does it matter if you've got technologists and people with military and combat experience but no one with GTM experience? How important is that? I know procurement better than fucking anyone.

[00:07:33] Matthew Steckman: It's multidisciplinary, right? So the challenge becomes in defense that if you're missing any of the 12 different types of disciplines it takes to really capture a large program, you will fail. And so one of the things that we've done is over the years we've built up a pretty sophisticated apparatus to kind of round out these teams with all of the various skills in acquisition and budgeting and technology, mission and operational analysis, and doctrinally how these types of technologies will integrate into the military.

[00:08:03] Harry Stebbings: Does it matter if the founding team doesn't have that experience in terms of going through procurement and GTM?

[00:08:09] Matthew Steckman: I think it does. I advise a lot of companies. And if I notice the founding team, at least a portion of it or a person on it hasn't kind of been there, done that. The first thing I recommend is that they have to find someone who represents that piece of the puzzle that that's missing to their team.

[00:08:25] Harry Stebbings: When you meet all of the defense companies that you meet today, again, I'm an investor. I do. We have so many different European drone companies. But when you look at them, what is the most common red flag that you see when you look at the emerging class of defense companies trying to be, as awful as it sounds, the next Andrew? Yeah.

[00:08:44] Matthew Steckman: Basically, two things. It's not realizing that what they are doing already exists. There's too much hubris in the technology market. You know, as high tech people, we can do everything better than everybody else. That causes some companies to think they have an idea that isn't actually an idea because it already exists. And that's pretty common. I'll give you an example. Years and years ago, I'm looking at a pitch or I forgot maybe I was advising someone and here's my idea.

[00:09:12] Matthew Steckman: And I said, well, the thing you don't know is in the 1960s, we invented that. And so there's kind of a hubris to thinking like the technology sector has all the answers when like actually since the 50s, we've had the most brilliant people in the world working on these problems and a heck of a lot already exists. And this is sort of the point of like if you don't actually have the inside knowledge, you don't know what mistakes you're making. So that's one. The second, which will be more familiar to you, is addressable market.

[00:09:39] Matthew Steckman: There's many cases and overestimation of addressable market where like actually what ultimately they're going after is a very small sliver of a problem, which might materialize in a single large contract. But a single large contract is not an enduring business.

[00:09:56] Harry Stebbings: Totally get you and agree with you. And this is one of the big challenges that I face is when we see a company that in France is saying we're selling to the French military. Dude, I don't know how to say it. I upset everyone these days. I just get used to it. The French military spend less than I do in Chanel for my mother. I mean, it's like, fuck all. Can you be a European only next gen prime? Or do you have to be selling to the US as well? How do you think about that?

[00:10:20] Matthew Steckman: Yeah. I mean, you basically can't have a defense company if you don't have a large US business, right? So 50% of defense spending is in the US and 50% is in the rest of the world. And so if you are cutting off half of your market from the get-go, that's probably a big problem. The challenge in Europe is it's not like a European Union in defense spend, right? Each country has its own sovereign companies and has its own sovereign agenda. And so you keep getting winnowed and winnowed and winnowed. And you're like, oh, well, Europe is my market.

[00:10:50] Matthew Steckman: Well, if you're a French company, it kind of isn't. France is your market. And so you have to be really careful around how you're actually analyzing who your ultimate customers can be.

[00:10:59] Harry Stebbings: You mentioned 50% of that spend is in the US. You guys signed a $20 billion contract. My question to you is, what's actually entailed in the $20 billion? Was it like an accumulation of all the little contracts bringing together? Because it's a big headline number, but I didn't actually get it. And I don't think a lot of people did.

[00:11:19] Matthew Steckman: Yeah, yeah. So let's like actually define it because the stuff I saw posted about it was all over the place. It was like a rainbow of interpretations. So think about this as like a credit card limit. So the government has said up to $20 billion they can spend on a class of Andurl's commercial technology. There's no obligated money, but it basically creates a process that reduces a ton of friction

[00:11:45] Matthew Steckman: that you would ordinarily see in defense procurement, where each individual office would have to go through financing and contracting and evaluation. And all of these repeatable things now only have to happen once. And they did. And they just did. And so maybe a fast track is probably the wrong word. It's more like in the arduous process to actually get something contracted. We've cut a lot of the first steps out.

[00:12:14] Matthew Steckman: There's still a lot of hard work. We've just made it slightly easier for the government to access all of our gear.

[00:12:19] Harry Stebbings: Well, when they say like dependent on delivery, what does delivery mean?

[00:12:24] Matthew Steckman: They will obligate the dollars as the products, which is hardware and software, are actually materialized. So delivery is revenue to us in our world. So when I deliver something, I recognize the revenue. Same thing in government. When we deliver something, then the actual procurement orders and dollars flow.

[00:12:42] Harry Stebbings: Again, I'm so sorry for being dumb or naive. I'm a venture capitalist for a living. You should be used to us by now. Is this replacing prime spending? Is this net additional? How should we think about this? And is this just the sign that Andurl is now another prime?

[00:12:56] Matthew Steckman: Yeah. It basically means that we have enough business with the federal government to justify putting together a sophisticated contracting vehicle. So yeah, the short version of it is like, yeah, the government thinks that we can deliver some pretty major stuff now and in the future. It took a lot of work by a lot of people on the government side to actually make this thing happen. They are not going to do that unless they think that it's worth it.

[00:13:20] Harry Stebbings: What do they spend with like a Lockheed or a Northrup for like comparisons?

[00:13:25] Matthew Steckman: So Lockheed, I think is in the like 100 billion revenue a year. I think we'll do a couple billion in revenue this year. So we're still, you know, small in the grand scheme of things.

[00:13:35] Harry Stebbings: When you look at the software and the hardware element, how do you guys sit internally? Are you a hardware company? Are you a software company? Are you a services company?

[00:13:44] Matthew Steckman: I think one of the things we've done maybe uniquely is we've given our customers a lot of ways to access our company. What I mean by that is we've been very creative in, okay, a customer wants a piece of software, but it's difficult in government to contract for software. And so we can wrap it in a hardware appliance, right? Or they want a piece of hardware, but they know the software is the sophisticated piece of it. And so they're willing to pay more for it because of that sophistication.

[00:14:11] Matthew Steckman: Or in government, you get these weird things where money is, it's called the color of money. So money is obligated to certain types of spend. So maybe a customer only has money that they can spend on services. Well, okay, can I do an as a service product? And actually one of our first major contracts was with US Special Forces for all of their counter UAS systems. That started as an as a service contract where they weren't buying hardware,

[00:14:39] Matthew Steckman: they weren't buying software, they were literally buying a service that obligated us to defend certain sites from certain types of threats. And as long as we were meeting the KPIs on the contract, we were fulfilling the obligations of the agreement. So quite novel. And that contract has, you know, since gone in a lot of different directions and we do a lot of different things on it. Not just that, but we have been dogged in our approach to this, basically realizing that

[00:15:05] Matthew Steckman: the more ways we give our customers to get at us, the better it's going to go.

[00:15:09] Harry Stebbings: What's the hardest thing about working with the government? When you look at the structures that you have to contort yourself in to get a deal done, what's the hardest thing?

[00:15:19] Matthew Steckman: There's a lot of answers to this question, but maybe from my lens, it is how few and far between the large wins are and how hard it is in between those periods of time. If you look at our business, you know, this year we'll do a couple billion in revenue. We'll do 600 separate contracts this year. Only 20 of those are probably of material revenue size. And so the hardest thing is like, what happens in between the 20? And what are you doing to position yourself for the 21st?

[00:15:47] Matthew Steckman: And because it's so concentrated, every single one of those deals is considered risk to the business, right? If it goes right or if it goes wrong.

[00:15:54] Harry Stebbings: So why specifically is it hard in between? Is that morale? Is that revenue predictability? Is that what is it that's hard in between?

[00:16:03] Matthew Steckman: The government can sometimes tell you where they want you to go, but oftentimes they don't. And so a lot of this is trying to predict an unpredictable system, right? So how many lenses can you look at at sort of the next couple of years? I can look at it through what the government is saying, through their rhetoric and through their budgeting. I can look at it through a warfighting lens and what general officers are saying and what military theorists are saying.

[00:16:29] Matthew Steckman: I can look at it through a technology lens, like what technologies do I think are going to influence the battlefield in the future? And I need to kind of blend all of that together today to make decisions on what I want to build that will be available, you know, five to seven years from now. No one is saying today, this is what I need five to seven years from now. It's all sort of a educated guessing game over time.

[00:16:52] Harry Stebbings: What did you not do that with the benefit of hindsight you wish you had done? And what did you learn?

[00:16:58] Matthew Steckman: There's been a couple of areas that have kind of emerged that maybe we were a bit slow in that we would have accelerated. I'll give you an example. There's a huge movement in not just in the US, but NATO and the rest of the allies into offensive cyber warfare. And you're seeing this now becoming public for the first time, which is really, really interesting. You know, to date, this has been one of the spookiest of all spooky things, right? Like something that just no one ever talks about. And now you're literally seeing public officials talking about it for the first time.

[00:17:26] Matthew Steckman: We should have moved into that seven years ago and been the first, the first in it. We weren't big enough probably to really even understand it seven years ago. But like in hindsight, it was kind of obvious. We'll probably try and play some catch up here and get into the game. But there's a couple of examples like that where you see these things kind of thematically in hindsight. And you're like, well, obviously, five years ago, I should have done it. Right. And you only realize that today.

[00:17:49] Harry Stebbings: What is the fear with offensive cyber when we look at like the worst case scenario, just so I understand it?

[00:17:54] Matthew Steckman: Well, it's a lot of things. So it's both what are our adversaries doing and do we understand it? And are they asymmetrically influencing battlefield tactics? And the answer is yes, they are. And then it's OK, well, if our capability.

[00:18:10] Harry Stebbings: Sorry, can I just stop back again before I get lost in your next statement? What does it mean like asymmetrically influencing battlefield tactics?

[00:18:17] Matthew Steckman: Yep. So one version to think about this is just cost for a very low cost. They can create an effect that has major implications for us, NATO and our allies. That's asymmetric. So often people refer to terrorism as an asymmetric tactic.

[00:18:33] Harry Stebbings: But this would be like a $10,000 drone that hits a one million.

[00:18:37] Matthew Steckman: Drone warfare is an asymmetric battlefield tactic. Exactly. And cyber being not only asymmetric, but you'll often hear the term non-kinetic associated with it.

[00:19:17] Matthew Steckman: How do we respond? Do you respond with a non-kinetic attack by going kinetic? Is that an escalation of force? How is that perceived by the global community, right? So you get into all of these really challenging doctrinal positions because of just how sort of unexplored offensive cyber is. And then on the flip side, right? It's like, do we have the ability to amass cyber effects on our own, right? Because what you would want to do is you would want to do tit for tat.

[00:19:43] Matthew Steckman: You wouldn't want to do it for the most part, a set of like escalatory decisions. You would want to match force with force. Do we have the ability to amass the same kind of force non-kinetically, right? So all of these are super important questions that in my opinion to date have not been debated publicly and absolutely need to be.

[00:20:02] Harry Stebbings: What cyber assets do we care about versus not care about? What do we care about protecting or what do we care about affecting? Both.

[00:20:10] Matthew Steckman: Yeah, well, protecting, right? So probably the main one is like the list of critical industries. The military is included on that list. But think about infrastructure, think about power, think about energy, think about all these things, right?

[00:20:21] Harry Stebbings: Okay, so it's like a foreign adversary impacting energy supplies in large cities or water supplies or healthcare data or financial systems, I guess.

[00:20:32] Matthew Steckman: Yep. But even now, though, on the battlefield, it's a foreign adversary impacting our military systems such that we can either not mount an offense or we can not successfully defend ourselves.

[00:20:43] Harry Stebbings: Got you. That's the cyber assets that matter on the defense side. On the kind of offense side. Yeah. Do we think the same in terms of proactive?

[00:20:51] Matthew Steckman: Everything that they would do, we would do too. Exactly. That's the way to think about it.

[00:20:54] Harry Stebbings: Is there any part of you that's like Northrop or Lockheed have $100 billion spend? With the greatest of respects, we have a $20 billion spend. We're nowhere in offensive cyber. Let's not try and catch up. Let's progress. I mean, in a nice way, you can laugh at me. And maybe I'm going to get killed for this, but I don't really care. Like, let's just accelerate where we're doing great. Like, why bother catching up when you're seven years behind?

[00:21:17] Matthew Steckman: Let's like talk about just like our strategy as a whole. So when we started the company, we knew we had to go really wide, really quickly. Because to the point of like, what do other defense companies or newer founders getting wrong? It's that addressable market question. In every technology class in defense, there's probably one, sometimes two actual programs that if you capture them, you have a business. And if you don't, you have no business. Take small drones as an example.

[00:21:43] Matthew Steckman: There are very few drone programs for small drones that would create a material enough amount of revenue to like actually create a real business, right? You're basically shooting the moon. You have to create a monopoly. We knew that. And so what we did is we created a bunch of fundamental technologies that are applicable to a lot of different types of problems. If you read about us, this is called Lattice in a lot of our published literature.

[00:22:08] Matthew Steckman: It's fundamental tech that allows you to consume data, make sense of it, and then manipulate robots, basically. Like that's what it is. And so those technologies apply to tons of different things. And so we have 20 different P&Ls at the company, all that are going after different parts of the defense apparatus that take a lot of these fundamental technologies that we build and kind of piece them together in different ways.

[00:22:33] Harry Stebbings: So just so I understand, it's kind of like a horizontal foundational technology that you then verticalize and specialize.

[00:22:39] Matthew Steckman: Lattice is a software platform. Exactly. Like I can talk about software platforms with you. It's hard to actually talk about software platforms with a lot of people because it's like if you don't actually understand like what we're talking about, it gets a bit weird. Yeah. Lattice is basically just a software platform that we can branch from. And it's led us into all of these interesting places. So like as a really crazy example, the first product we built was a sensing tower that just allowed us to automatically through a bunch of computer vision technologies. And this was, by the way, pre-cool AI.

[00:23:08] Matthew Steckman: This was like old school CV AI in 2017. Just allowed you to spot threats at distance, right? But automatically without a person having to look at a screen. There are pieces of that technology that are resident in our autonomous jet fighter today. Not all of it, right? Like there's been a lot of advancements since then, but there are code blocks, right? That are shared in common between all of our pieces of technology. That becomes like pretty magical when you approach whatever the next problem is because

[00:23:37] Matthew Steckman: you've already got pieces of it solved. Gives us a head start, allows us to get to market at usually reduced cost, usually a better schedule, kind of hitting all of the performance characteristics that our customers care about. So, okay. So back to the actual question on cyber, right? So why go after it? Like we kind of have to go wide and we have to believe that we have parts of the problem already solved with the platform in order to even approach a market. We wouldn't get into a market if we didn't think we already had applicable technology

[00:24:06] Matthew Steckman: or a technology tailwind. But where we do, we're definitely going to go after it.

[00:24:10] Harry Stebbings: What you said was fascinating to me. You were like basically, you have to assume a monopoly market if you want to build a big enough company for drones. Why the fuck are there so many drone companies then? Yeah. I don't know. I've seen so many, like 30, 40 in Europe, just European ones. Yeah.

[00:24:29] Matthew Steckman: There'll be one that wins, right? It's going to be really hard to pick it, I think is the problem. But there will definitely be one winner. I think the challenge for investors is actually figuring out which one it is.

[00:24:39] Harry Stebbings: So we should invest in offensive cyber and defensive cyber. How do we think next then? Your CBO, your president, are you like, great, we should put a billion dollars against it and build that out as a separate business unit? And please tell me where I'm primed. What's the subsequent thought to that?

[00:24:57] Matthew Steckman: Yeah. So the way that we do this is when we have a new idea, we basically start a really small tiger team that we generally piece together from various parts of the business. We kind of match our own internal motivation and spend our own IRAD to what the market is whispering to us. So in government, what this generally looks like is you piece together some tech really, really quickly so that you have a demonstrator or at least a dart to throw.

[00:25:25] Matthew Steckman: And then you start to pulse the market and you see how close was that dart throw to what the customer actually cares about, how they think about the problem. Do you modify it where you're totally off and you just need to scrap it and start over again? In government, uniquely, you know you have something when the customer's excitement starts to match your own. And all of a sudden, you're kind of walking down a path together as opposed to this weird like vendor customer relationship. But that's always how we kind of identify that we're onto something.

[00:25:55] Matthew Steckman: I would say all of these things can be characterized by like a singular champion on the other side of the table that gets it, that believes in it, that wants to shepherd it. Actually, you mentioned Sham. He talks a lot about this kind of like heroism. Like it actually comes down to a single person in government a lot of times. Same experience for us. If you do it right, it kind of tracks similarly. You know, the first year's low dollar spend, but there's a lot of learning. And you sort of jump from, I tend to use this like lily pad example.

[00:26:24] Matthew Steckman: You kind of jump from pad to pad. And this is what I mean by the 600 contracts in between the 20 that matter. You're basically jumping from contract to contract trying to figure out, do I have it right? Is the customer excited? Are they telling me things? Do we keep going? Do we keep spending? And ultimately, the thing you're trying to jump at is something very large.

[00:26:43] Harry Stebbings: How do you know when you have something really special and when you should concentrate capital? Again, as I think the best founding teams are the best resource allocators. When do you unleash the funding tab and open it up versus constrain and move from little lily pad to lily pad?

[00:26:58] Matthew Steckman: Yeah, there's a lot of ways to look at our business. But one way I think you hit on it is we've been very good at allocating capital. Like we basically guess right most of the time. If you do this correctly, you have enough data to develop conviction to open the tab, right? And so I think in the beginning, we were working in areas where if we made a mistake, it wasn't we weren't like too far in on spend that if we pulled back, it wasn't like a disaster for the company. I think a lot of the stuff we're building now is quite sizable and expensive.

[00:27:28] Matthew Steckman: And so you're looking for certain proof points along the way. And that can be formal feedback from a customer. That can be informal. That can be successful operator feedback. That can be successful engagements with the legislative branch. Like remember in the US, like your funder is the Congress, right? And so they have a say in all of this. What actually it is, it's all of those things pieced together.

[00:27:53] Matthew Steckman: And so we run like basically an investment committee internally where these Tiger teams ultimately have to present, here's what we did. Here's what we discovered. Here's what we want to do next. Here are the gates. Here's what it'll cost. And very similarly to how most financial institutions do it, the investment committee says go. And I think maybe uniquely when we say go, we have the ability to do it faster and at a higher level of spend than most of our peers, which is a huge advantage.

[00:28:20] Matthew Steckman: And so when we actually develop conviction in something, we pretty much believe we can get there faster than everybody else because of it.

[00:28:26] Harry Stebbings: If we think about it as an investment committee, we're speaking a language that I know now, which Tiger team was the most successful bet and which was the least successful bet?

[00:28:35] Matthew Steckman: The most surprising cases to the upside right now is in our missiles portfolio. So we started our missiles business a couple of years ago. The best example we call the Barracuda family of systems. So it's basically a set of cruise missile systems, different sizes, different shapes, things like that. We basically got into the missiles business looking mainly at sort of this, the actual like military warfare lens. Like there is clearly a gap in capability.

[00:29:05] Matthew Steckman: We clearly believe that we can be ahead of everybody else if we've already developed it. And when the customer asks for it, we'll have it. And that turned out to be quite, quite prescient. Now, I don't know if you've seen, but there's like a war going on with Iran.

[00:29:20] Harry Stebbings: I have seen, yes.

[00:29:22] Matthew Steckman: Yeah. And so it's like, OK, so we got into this market years ago with a certain set of theses and geopolitics now has dramatically changed what those theses are to the upside. When you say it's changed them, do you mean it's confirmed them? It's confirmed them, but it's confirmed them in such a way where it feels wholly different.

[00:29:41] Harry Stebbings: How so?

[00:29:42] Matthew Steckman: You know, I think the original theory was we have to get low cost. We have to get more ubiquitous. We have to have a mix of exquisite systems and mass. Like all of these kind of major theories of warfare are kind of all converging at the same time. We have to be able to build something that takes advantage of commercial supply and commercial manufacturing techniques as opposed to aerospace and defense supply and technique. This kind of like crazy crystallization of a lot of things at the same time. And now there's a war in Iran.

[00:30:11] Matthew Steckman: We fire a lot of our arsenal, you know, and now there's public reporting that large percentage of our offensive and defensive missile systems have been expended and they're really hard to replace. They take a really long time and they're very expensive because they take advantage of parts of the market that are kind of strange and very specific and very exquisite. You know, just to give you an example, the cruise missile we build, the actual airframe is built like you build a bathtub.

[00:30:37] Matthew Steckman: And so we can take advantage of tons of contract manufacturers in the United States that can actually build a bathtub, right? So just thinking through the design differently from the very beginning has led us to build something that can just turn on. It's like another way to think about it is you can handle elasticity of demand for the first time. That's not really a thing that's ever existed in the missiles business, right? Where you have a fairly labor intensive process to increase or frankly, sometimes decrease demand.

[00:31:06] Matthew Steckman: We are onto something in that we've built kind of a first of its kind that can handle the ebb and flow of geopolitics and warfare. We can turn lines on and off. We can scale up and down based on the number of contract manufacturers that we engage.

[00:31:20] Harry Stebbings: What do margins look like for these types of products? What is good?

[00:31:24] Matthew Steckman: Yeah. As a business, we run sort of 40% plus gross margin across the board, by the way, in hardware and defense is quite good. But every product kind of lives along a spectrum, as you can imagine. The best way to think about this is things that you make more of, like missiles, where you're selling thousands and thousands tend to be a little bit lower gross margin and things that you make less of, you can tend to get a decent price for it.

[00:31:48] Harry Stebbings: Sorry, I'm naive. Why is that? I thought the more you produce, the better the margins be because you have bulk materials, bulk buying. No? Help me understand that.

[00:31:57] Matthew Steckman: Mostly comes down to customer expectation for what these things should cost over time. And then your ability to gain back margin by cost saving in the long run. Yes, you can close a firm fixed price contract. It doesn't necessarily mean that you can fix that cost forever. And again, it's just like another weird aspect of government business.

[00:32:17] Harry Stebbings: Can I ask you a weird one? But Matt did say I could ask it. Is there either like an ethical question of like, do we agree with sending thousands of missiles to Iran? I'm not saying right or wrong, but is there either an ethical question of how your products are used?

[00:32:32] Matthew Steckman: If you work in defense and if you start a defense company, your moral compass tends to be pretty clear on this question, which is we have a democratically elected set of governments that represent the US, the alliance, NATO, all of the countries participating. They set the rules. And we abide by those rules. And if you start to mess around with anything within that framework, you create a pretty dramatic set of slippery slopes that if you play the actual thought experiment to its end,

[00:33:02] Matthew Steckman: end up in a pretty messy situation. The key here is people that live in the world that I live in, we tend to think a little bit differently than a person not connected to the national security community on this front. We tend to think a bit more long term as well, where I'm building missile systems that might only field in 2035. And so if you fundamentally lack trust in democratic institutions, this is not the game and this is not the business for you.

[00:33:29] Harry Stebbings: As weird as it sounds and as horrible as it sounds, is war not great for business?

[00:33:34] Matthew Steckman: I think that's the wrong view. Again, if you look at things that span multiple decades, which is probably the right horizon to think through, everything kind of nets out. And so, yes, you'll have spikes in conflict. But like as an example, there are many companies that are profiting off of the war in Ukraine. I would posit that for the most part, if those companies are myopically focused on that conflict, they will not have a business coming out the other end.

[00:33:58] Matthew Steckman: You have to be very careful around over-rotating on the problems of today because it can really mess up your strategic thinking. Do you think you took advantage enough of the opportunity in Ukraine? We were still a baby company when the conflict started. You know, just as a reminder, we were zero people in 2017 when we started the company. We're about 8,000 people today. We were quite small, a couple of hundred people when the war in Ukraine started. And just sort of as a reminder, and now this is kind of lived experience for me and my colleagues,

[00:34:28] Matthew Steckman: you go to war with what you have. That saying is very, very true. Like you do not invent new stuff along the way. You take what you have and you see if it works and then you adjust. And so we had some stuff in Ukraine, but we were just too small. I think if you play that forward to today, we're heavy participants in the current conflict in the Middle East. Mainly on the defensive side, we build some pretty sophisticated air defense systems that are widely deployed. So it's a wholly different experience because we're a wholly different company.

[00:34:55] Harry Stebbings: Are android drones used in Iran?

[00:34:57] Matthew Steckman: I can't speak to specific weapon systems used in specific situations, but we are, for the most part, a defensive company in the Middle East, as in we are defending against incoming threats. So if you've read about the Shahid drone, as an example, we're one of the principal systems to defend against that threat in the Middle East. Other than that, it's hard to get into specifics.

[00:35:21] Harry Stebbings: Yeah, I would hate for you to reveal some inherent military secrets on 20 BC.

[00:35:26] Matthew Steckman: You become pretty good at talking around these things when you do this work.

[00:35:30] Harry Stebbings: No, that's not in my interest either. Please don't. I'm really comfortable with my nice life. Can I ask you, if I gave you an unlimited checkbook, what would you spend on that you're not spending on today? That's a great question.

[00:35:48] Matthew Steckman: I'll give you a funny answer. I think there are some venture capitalist-backed defense companies that are making some really, really awesome technology, and they are entirely unaffordable to us today.

[00:36:00] Harry Stebbings: Because of... And when you say they're unaffordable, you mean they won't sell at an appetizing price to you, given the amount of money that they've raised? Correct.

[00:36:07] Matthew Steckman: Their valuations are just too high for us to justify the buy. We've bought, I think, almost a dozen companies, maybe more. But for the most part, they've been more traditional-style defense companies with what you would command in the commercial market for that type of company. There are lots of VC companies I would love to buy if I had an unlimited checkbook. But right now, the multiples today are... They put it out of reach for us.

[00:36:29] Harry Stebbings: This was going to be one of my questions, which is, is there a universe of buyers for the massive VC-funded companies that have been generated in the last few years? And what happens to them?

[00:36:41] Matthew Steckman: Actually, Trey, I will always remember when he said this, that never be surprised around how long a company can continue to exist. Meaning, like, you know, I think we were sitting around a table being like, oh, like, it's going to come to the point where the multiples will decrease and all this stuff. And Trey's point was, Trey has this annoying tendency to mostly be right. I don't know if you know that about him.

[00:37:05] Harry Stebbings: But he's our asshole. Yeah, yeah, exactly. He's our asshole.

[00:37:08] Matthew Steckman: His point was like, we don't know, but it might be a while before we can actually buy these companies. And so I don't know. There's still a lot of investment in defense tech. Multiples are still very high. I actually think our multiple is quite low compared to most of them. Why would you say your multiple is low? Because it is.

[00:37:23] Harry Stebbings: Hit me.

[00:37:24] Matthew Steckman: I think we're like 10 or 14x forward, something like that. But you're seeing deals in 20, 30, 40x forward.

[00:37:32] Harry Stebbings: My dear friend, you're seeing deals a lot more than that. You're sorely mistaken on that one. Great. So it's even worse. 20, 30, 40. Why don't you times that by five? Dude, I see like 200. Who would you most like to buy?

[00:37:49] Matthew Steckman: Oh, man. But calm. No, that's a tough one for me to answer. I probably either compliment or offend people that I don't want to compliment or offend. But I'll give you like the classes of technology. Super interested in space domain. Like there's a couple of companies that are doing some absolutely fascinating things, both ground segment and on orbit.

[00:38:07] Harry Stebbings: Why is ground segment and on orbit interesting?

[00:38:11] Matthew Steckman: There's this like interesting thing happening in space domain where you've got the legacy primes on the military side that have these very large contracts. But they perform sort of traditionally, right? So it's going to be very, very high performance. But it'll come at a cost and it'll probably take a while to get there. And then you have SpaceX, which is just dominating on the commercial side. And when their commercial tech applies, you know, they do a bunch of government business as well.

[00:38:39] Matthew Steckman: There's a weird kind of gap in between those two types of companies where the government wants to move really fast, but it's not necessarily commercially adjacent to what SpaceX is doing. And so there's a kind of a dearth of providers. And it's certainly something that we want to run at. Right now, we do a bunch of partnerships. We build a bunch of our own stuff. We integrate a bunch of really interesting technologies. But it's a huge open hole, I think, in the market that is something we definitely would run at.

[00:39:10] Harry Stebbings: So we have that as one. Any other categories that you're like, that's like prime for the taking. I wish we had more money for that.

[00:39:16] Matthew Steckman: Most of the rest are like kind of uninteresting. It's just consolidating around where we're already winning. Do you respect Helsing as a competitor? I respect everybody as a competitor. I think the worst thing you can do in this business, again, you know, at the start of the conversation, I mentioned Hubris. I think it's like the second you think you're better than everybody else, you're going to get knocked on your ass. And so I think I, in particular, on our leadership team, hopefully people would agree, I provide a check against the Hubris. You have to respect that.

[00:39:45] Harry Stebbings: You do. You're unusually humble for the Andrewl founding team. You're honestly, dude. Like, I love Grimm. But I wouldn't say he's like super humble. Yeah, I don't think I would say that either. I know Palmer. Great dude. Wouldn't say he's super humble. It takes all types. You're so thoughtful and kind. You're nice.

[00:40:08] Matthew Steckman: Never forget, I am an international arms dealer. So just keep that in the back of your mind. Oh, well, there we go.

[00:40:13] Harry Stebbings: It's like the Nicolas Cage movie. Have you seen this movie? Yeah, yeah, yeah. But okay, I will push back on you. Andrewl's one of the hottest companies in a world where capital concentrates towards the few outcomes that are interesting. I mean, you don't need to comment on the fundraisers, but it's reportedly raising four or five or six billion, whatever it is, at 60 billion. The amount of SPVs for Andrewl. Matt Grimm tweets about it all the time. I see it.

[00:40:40] Harry Stebbings: Like, you could raise another billion or two billion on some crazy price and go and buy these companies. Why don't you? It's not the company we want to run.

[00:40:47] Matthew Steckman: We want to create an enduring public company. And so we're running it like that. We're running it like that right now, even though we're pre-public. Protecting the valuation is important. Not getting over our skis is important. The work is still hard. We will get knocked back if we make a mistake. We don't have the luxury of making mistakes. You know, a lot of our competitors, the really big ones, if they make a mistake, they get paid to fix it. I think if we make a mistake, we lose money and we lose contracts.

[00:41:15] Matthew Steckman: So there is a bit of conservativism on the team, but I think it's warranted in terms of the market and overall. Right. It's like we want to be a company in 2050 and 2060. And we're already thinking like that.

[00:41:27] Harry Stebbings: Totally understand. But what I don't understand is why you want to go public. We see companies like Stripe who are able to never go public, be a brilliant business and avoid the glare of public markets very efficiently. Why would you want to go public?

[00:41:41] Matthew Steckman: Yeah, there's a pedigree to it in the work that we do. And ultimately, if you are a part of the national security apparatus in the United States, I wouldn't say it's like an expectation and no one would ever say it out loud. But when you are a public company, there is an additional level of trust that is afforded to you that you don't have when you're a private company. Do you want to get public in 26? Still a couple of years out, but we're close. We're in the window.

[00:42:06] Harry Stebbings: It's in the sniff zone. Yeah, yeah, yeah.

[00:42:08] Matthew Steckman: Like we're already spending an insane amount of money trying to do all the internal system stuff and all that kind of stuff.

[00:42:14] Harry Stebbings: What do you not have ready yet that needs to be ready to be public?

[00:42:19] Matthew Steckman: So I mentioned we have 20 products and only about a quarter of those are in any kind of rate production and throwing money back to the business. Everything else is in low rate or development, meaning they're losing money. It's kind of your standard product J curve. So we need more of those 20 core products to come up the curve, to throw money back to the business. And then you trigger the bulk of that.

[00:42:42] Harry Stebbings: What does that J curve look like from a duration standpoint? Is it months? Is it years? And then how long do you put up with a losing product before you shoot it?

[00:42:52] Matthew Steckman: Yeah. In defense, in a traditional sort of product curve, it's seven to 10 years. We're doing it in three to five, which is kind of part of the magic of the company. And the thing we've become known for with our customers is like you're effectively having the traditional path to rate production. Roadrunner is a good example. Roadrunner was, I think, 24 months from like a back of a napkin drawing to a fielded system. How much goes in in that three to five period? Oh, so much. It's a crazy amount of money.

[00:43:20] Harry Stebbings: But just like from my naive brain, it's like 100 million or like 500 million or like a billion?

[00:43:25] Matthew Steckman: Yeah, so Roadrunner is a moderately sized air defense kinetic intercept system. And that's you're over 100 million easily before you're generating revenue. Okay.

[00:43:37] Harry Stebbings: And we have 20 of these separate products?

[00:43:40] Matthew Steckman: Yeah. So it's a lot of investment, right? So you really have to believe that they're going to come up the curve. And then to your other question about like when you when you schwack a product, the better way to think about it is like don't even enter the curve if you don't have faith that it's going to come through the other end. And so we kill a lot of developmental products well before they ever get into high spend, because once you get into that curve, you're 10, 20, 50, 100 million plus in.

[00:44:02] Harry Stebbings: We spoke about what did you not do? And you said offensive cyber and the cyber that we discussed earlier. What did you do that you shouldn't have done? And what do you learn from that?

[00:44:10] Matthew Steckman: That's a good question. Way early. I mean, we got into some tech that we weren't ready for. We got into some markets that we weren't ready for. We tried to early on build a pretty sophisticated aerial system. We didn't have the core building blocks. We didn't have the core team. I think we were 20 million or 40 million in before we kind of realized that it was a scrap. We didn't have the sophistication with the customer. We didn't know how the customer was going to buy a vehicle of that sophistication.

[00:44:38] Matthew Steckman: The kind of crazy part about all of this is like, well, OK, given all of that and given that that was not a good business decision, clearly by most metrics, do we even get to build the autonomous jet fighter if we had never made that mistake? I don't think so. Part of that failure was a stepping stone to getting to success. Yeah, we probably spent too much money on it and could have gotten out quicker.

[00:45:00] Matthew Steckman: But like, I think we had to learn that lesson in order to then re-approach the aviation market in a new way, which obviously has been quite successful for us in recent history. And so if you look at a lot of these failed things that we've done, it's hard to separate that from what came after it.

[00:45:16] Harry Stebbings: Final one before we do a quick fire. I always think to this question of like the biggest challenges in life are not like iron or gold, but unmade decisions. I never made the decision to move to Silicon Valley. And everyone always reminds me that it will be the decision that haunts my career. Is there an unmade decision that ever haunts you?

[00:45:37] Matthew Steckman: No, but I'm kind of weird that way. I don't know. Like, I have trouble separating indecision and failed decisions from the current success that we're actually seeing as a company. I just do. People talk a lot about, I think, like these overblown sort of ideas around like, oh, you have to learn from failure and fail fast. Like, yes, all that's true. Most people suck at actually doing that. So for me, it's I deeply learn from indecision and from bad decisions.

[00:46:05] Matthew Steckman: But it doesn't like haunt me and it doesn't like I'm not going to like kill myself over it. Right. I'm going to I'm going to move on. I'm going to make the next best decision.

[00:46:12] Harry Stebbings: Dude, I want to do a quick fire with you. So I say a short statement. You give me your immediate thoughts. Does that sound OK? What's one belief you have about modern warfare that most people think is insane?

[00:46:23] Matthew Steckman: I think a lot of my beliefs and our beliefs that we started the company on are now becoming a bit more commonplace. You know, when we started the company, maybe we were a bit out of on a limb of like, could I replace every single mission that the current set of technology provides us with an autonomous system? I believe that that is true in the long run. I also believe that we're not even close to where a lot of people think we are on it. Like I think we're still in the early days on tons of this tech.

[00:46:52] Matthew Steckman: But as time goes to infinity, like absolutely every single mission can be replaced with this new way of thinking. In 2017, when we started the company, not only was that not widely held, that was a headwind for us. I think that's changed pretty dramatically.

[00:47:07] Harry Stebbings: What do VCs fund in defense that you think will most go to shit?

[00:47:12] Matthew Steckman: What are you like? Oh, it's really companies that there is only one large program to capture. That's like fundamentally what it is. In defense, you have to be wide by the very nature of how acquisitions occur. And so I think anything is a risk where it's like, nope, there's kind of one program. And if you don't win it, you're not a good company.

[00:47:33] Harry Stebbings: When you think about your kids, what do you tell your kids or kids graduating college about the world when it comes to career advice, knowing and seeing all that you do?

[00:47:43] Matthew Steckman: Yeah, I mostly say a couple of things. I think it's about the community that you surround yourself with. That's a reflection on sort of my own personal story. I mean, everything that I've done in my career has been the community of people around me that have helped me, have gotten me jobs, have afforded me responsibility. You know, it's not like some big machine or process. It's really just the people you surround yourself with. And I like to think I made some pretty good choices early on that helped.

[00:48:11] Matthew Steckman: And then the other piece would be people tend to overthink a lot of their steps and don't appreciate how much you just can learn along the way. You know, I talk to a lot of military folks that are transitioning out into the commercial world. I would say for the most part, they kind of like hem and haw over what company they should go to. You know, my main advice is I actually think you just need to start. You're actually a really smart person. If you don't like it, you can leave. If you like it, you got lucky. You should talk to a lot of companies.

[00:48:39] Matthew Steckman: You should pick and you should change your mind when you need to. And I think oftentimes there's a hesitance to change your mind, right? And I don't think that's actually true. It doesn't need to be true.

[00:48:49] Harry Stebbings: Final one for you. And this is the most unfair of all and that will get you most in trouble. When you look at the founding team in a hypothetical world in 10 years time, you start another company, but you can only take one of them with you as your co-founder. Which one and why?

[00:49:05] Matthew Steckman: I can't take them all? No. No. Well, it's a trick question because there's no way that I'm starting another company after Andrew. I don't know if you know this, but starting companies is really tiring. No, I'm a venture capitalist. We know it's tiring. We're much wiser than you. I'm just going to retire to the countryside and live with my family and I'm going to do that. Dude, you've got to choose one. Yeah. I'm not choosing. Don't make me choose. You know, I live in Washington, D.C. I'm very good at not answering questions.

[00:49:35] Matthew Steckman: Maybe it's Bobbick just because the contrast of his baldness in my hair would make us a pretty formidable duo. Do you think Palmer's brand is helpful? I do. Unequivocally. In defense, anything highly regulated, right? Every single thing is a headwind. The main thing you do to cut through headwind is you try and establish trust relationships with people who matter. Palmer is an N of one when it comes to establishing trust relationships with people who matter.

[00:50:02] Harry Stebbings: I've loved this. This is so not how I thought it would be, to be totally honest. It was so nice. It was so fun. I learned. I totally didn't do anything that I kind of thought I would. But thank you. It reminds me why I love doing what I do.

[00:50:15] Matthew Steckman: This was great. Honestly, it was great to meet you. I do listen to the pod most episodes. I love listening to it. So thanks for having me on. It was cool.

[00:50:24] Harry Stebbings: But before we leave you today, over 80% of Fortune 100 companies are running their businesses with Airtable. Airtable combines AI with the scale of an award-winning, infinitely flexible no-code system. A platform where you can see all of your data in one place and use it to make really big picture decisions. Think of it like mission control for your company. Airtable goes beyond organization and automating repetitive tasks.

[00:50:50] Harry Stebbings: It lets you use your data to inform strategy, monitor progress, and take action. Every cell is capable of performing hundreds of AI-powered tasks like web research or localization, and using those results to inform and update hundreds or thousands of other cells and workflows in real time. Unlock the true scale of your workflows at www.airtable.com forward slash 20VC. Airtable, the infrastructure of innovation.

[00:51:18] Harry Stebbings: And just like Airtable organizes your workflow data, MetaView organizes your conversation insights. This episode is brought to you by MetaView. Who says hiring has to be fair? Every founder, VC, and exec I speak with knows this. Your ability to hire is the biggest constraint on your company's growth. But recruiting is slow, it's subjective, and only getting more competitive. And that's why teams like Eleven Labs, Brex, Replit, Deal, and 5,000 other organizations use MetaView.

[00:51:47] Harry Stebbings: The AI company giving high-performance teams a real unfair advantage in hiring. MetaView's built a suite of AI agents that behave like recruiting co-workers. They proactively find candidates, they take interview notes automatically, and they help you surface the best candidates in process. For the first time, AI handles the recruiting toil and gives you a single source of truth. That means hours saved per hire, and a team focused on what matters most, winning the right candidates as fast as possible.

[00:52:16] Harry Stebbings: Don't let your competitors out-hire you. MetaView customers close roles 30% faster. Try MetaView today and get a free month of sourcing at metaview.ai forward slash 20VC. After MetaView captures what was said, Turing helps you build with the people who can deliver after it. Frontier Labs keep facing the same limitation. Models perform well on benchmarks, but they fall short once they enter real coding tasks, real tools, and real workflows.

[00:52:43] Harry Stebbings: That disconnect between synthetic evaluation and actual system behavior is now a core blocker for organic models. That's why NVIDIA, Anthropix, Salesforce, Gemini, and other leading lab partners partner with Turing. Turing is the research accelerator focused on post-training reliability. They build realistic RL environments, next-generation data quality systems built from real-world operational traces, and coding datasets that stress models under conditions

[00:53:10] Harry Stebbings: where failures matter, state changes, workflow branching, brittle tool calls, and the coding errors that break RL agents but never appear in benchmark reports. In reality, a model may demonstrate correct reasoning in your evaluation setup, yet still select the wrong parameter or mishandle a code update in a realistic interface. Turing makes that failure visible and gives teams the signal they need to fix it. For labs advancing agentic systems, Turing provides the structure required to understand why these failures occur.

[00:53:40] Harry Stebbings: To find out how, visit turing.com forward slash 20VC. That's T-U-R-I-N-G dot com forward slash 20VC.