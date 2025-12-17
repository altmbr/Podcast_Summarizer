# Why the Next AI Revolution Will Happen Off-Screen: Samsara CEO Sanjit Biswas

**Podcast:** Training Data
**Date:** 2025-12-16
**Video ID:** VQXivhM8I-g
**Video URL:** https://www.youtube.com/watch?v=VQXivhM8I-g

---

[00:00:00] But if you think about it, there's like a third shift
[00:00:01] Sanjit Biswas: between midnight and 8 a.m. roughly, right?
[00:00:04] Sanjit Biswas: That people tend not to work because they're sleeping.
[00:00:07] Sanjit Biswas: Imagine if operations like logistics
[00:00:09] Sanjit Biswas: could still run during that shift.
[00:00:11] Sanjit Biswas: Right.
[00:00:12] Sanjit Biswas: And then same thing, imagine your field service technician
[00:00:14] Sanjit Biswas: you need a part, like how amazing would it be
[00:00:16] Sanjit Biswas: if the part could just get delivered to you?
[00:00:18] Sanjit Biswas: Like that is something that's gonna be a nice augment
[00:00:21] Sanjit Biswas: to operation.
[00:00:21] Sanjit Biswas: So it's interesting because typically
[00:00:23] Sanjit Biswas: when you see automation kick in, again, volume increases,
[00:00:27] Sanjit Biswas: right?
[00:00:28] Sanjit Biswas: If you come down, there's way more demand out there
[00:00:30] Sanjit Biswas: than people realize because sometimes you'll say,
[00:00:32] Sanjit Biswas: yeah, I could use that part, but I don't need it delivered.
[00:00:34] Sanjit Biswas: If it's gonna cost 50 bucks for someone to drive it to me.
[00:00:37] Sanjit Biswas: If it costs five bucks or no bucks,
[00:00:39] Sanjit Biswas: like how awesome would that be?
[00:00:40] Sanjit Biswas: So we kind of view it as like it will increase the speed
[00:00:43] Sanjit Biswas: that it will operate on.
[00:00:45] In this episode, we talk with Sanjit Biswas, founder and CEO
[00:01:04] Pat Grady: of Simsara.
[00:01:06] Pat Grady: Sanjit formerly founded Maraki and has a legendary reputation
[00:01:09] Pat Grady: amongst Sequoia-backed founders.
[00:01:11] Pat Grady: So I'm excited to welcome him today
[00:01:12] Pat Grady: for a conversation about physical AI.
[00:01:15] Simsara is a $20 billion market cap public company
[00:01:18] Pat Grady: with sensors deployed in streaming data
[00:01:19] Pat Grady: from millions of vehicles capturing 90 billion miles annually.
[00:01:23] Pat Grady: Sanjit shares his insights about the constraints
[00:01:26] Pat Grady: of physical AI from running inference
[00:01:28] Pat Grady: on two-to-ten-wide-edge devices
[00:01:30] Pat Grady: to why the messy diversity of real world data
[00:01:33] Pat Grady: is both the biggest challenge and opportunity
[00:01:35] Pat Grady: for embodied AI.
[00:01:37] If you're building in robotics or physical AI,
[00:01:39] Pat Grady: this conversation offers a rare perspective
[00:01:41] Pat Grady: from somebody who has actually scaled it.
[00:01:43] Pat Grady: Enjoy the show.
[00:01:44] Sanjit, thank you so much for joining us today.
[00:01:48] Pat Grady: You were a legendary Sequoia founder
[00:01:50] Pat Grady: and it is a delight to have you back at Sequoia.
[00:01:53] Pat Grady: Thanks for having me.
[00:01:53] Pat Grady: It's great to be back.
[00:01:55] I want to start with your background.
[00:01:56] Pat Grady: So you went from MIT's RoofNet project
[00:02:00] Pat Grady: to co-founding Maraki through its $1.2 billion acquisition
[00:02:05] Pat Grady: and you were a now-the-founder and CEO of Simsara,
[00:02:07] Pat Grady: a $23 billion market cap company
[00:02:11] Pat Grady: with the best ticker on the public markets.
[00:02:14] Pat Grady: What's the through line?
[00:02:15] Pat Grady: Tell me about your personal passions and experiences
[00:02:18] Pat Grady: and what the through line is between all of that.
[00:02:20] Pat Grady: Yeah, so I'm an engineer by background.
[00:02:22] Sanjit Biswas: So study, EE and CS.
[00:02:24] Sanjit Biswas: I went to undergrad out here at Stanford,
[00:02:26] Sanjit Biswas: went to MIT for grad school.
[00:02:27] Sanjit Biswas: And that's where we worked on this project called RoofNet.
[00:02:29] Sanjit Biswas: So the through line for me has been about building
[00:02:32] Sanjit Biswas: cool products, cool technologies that have real world impact.
[00:02:35] Sanjit Biswas: And RoofNet, this is like over 20 years ago,
[00:02:38] Sanjit Biswas: the idea was, could you build really big wireless networks?
[00:02:41] Sanjit Biswas: Because, you know, kind of early 2000s,
[00:02:44] Sanjit Biswas: Wi-Fi was not mainstream, it was brand new technology.
[00:02:47] Sanjit Biswas: Internet access was just becoming mainstream
[00:02:49] Sanjit Biswas: and is still pretty expensive.
[00:02:51] Sanjit Biswas: And so we saw this opportunity to take Wi-Fi chips
[00:02:54] Sanjit Biswas: and all that technology and use it
[00:02:55] Sanjit Biswas: to build really big networks.
[00:02:56] Sanjit Biswas: And so we kind of had this idea that Internet access
[00:02:59] Sanjit Biswas: should be everywhere, right?
[00:03:01] Sanjit Biswas: It should be in the air.
[00:03:02] Sanjit Biswas: And how would you do that?
[00:03:03] Sanjit Biswas: And we need to build a big network.
[00:03:04] Sanjit Biswas: So that was RoofNet.
[00:03:05] Sanjit Biswas: And then with SimSara, it's a bit of a different sort of focus.
[00:03:08] Sanjit Biswas: We focus on the world of physical operations.
[00:03:10] Sanjit Biswas: So think all the infrastructure companies,
[00:03:12] Sanjit Biswas: whether it's energy utilities, construction logistics,
[00:03:14] Sanjit Biswas: like all these real world physical industries.
[00:03:17] Sanjit Biswas: And the idea has been real world impact
[00:03:18] Sanjit Biswas: through things like risk production, improving efficiency,
[00:03:22] Sanjit Biswas: improving sustainability, just using all this data now AI.
[00:03:25] Sanjit Biswas: Yeah.
[00:03:26] Physical AI feels like it's finally going through an
[00:03:28] Pat Grady: inflection moment.
[00:03:29] Pat Grady: You've been building SimSara for the better part of a decade now.
[00:03:32] Pat Grady: What did you see at the time?
[00:03:34] Pat Grady: And how has the field changed?
[00:03:36] Pat Grady: Why now?
[00:03:37] Yeah.
[00:03:38] Sanjit Biswas: So if I rewind 10 years to when we were founding the company,
[00:03:40] Sanjit Biswas: we had a couple of sort of intuitive bets or guesses.
[00:03:44] Sanjit Biswas: And the why now for us at that point was connectivity.
[00:03:47] Sanjit Biswas: So we'd been through the Marocka journey
[00:03:48] Sanjit Biswas: and we'd seen Internet access go from being kind of rare
[00:03:52] Sanjit Biswas: and inexpensive to being ubiquitous.
[00:03:54] Sanjit Biswas: So this is 2015 for reference.
[00:03:57] Sanjit Biswas: We saw basically the ability to process large amounts
[00:04:00] Sanjit Biswas: of data really coming online.
[00:04:01] Sanjit Biswas: So the cloud had matured.
[00:04:03] Sanjit Biswas: We were seeing the beginnings of the GPU wave.
[00:04:06] Sanjit Biswas: And if you remember back to 2015, Nvidia was a player
[00:04:10] Sanjit Biswas: and they were doing a lot of interesting embedded GPUs.
[00:04:13] Sanjit Biswas: So if you picked up an Nintendo Switch back then,
[00:04:15] Sanjit Biswas: it had amazing graphics, but it fit in your hand.
[00:04:18] Sanjit Biswas: And so we saw a compute was getting really good.
[00:04:20] Sanjit Biswas: And then we saw sensors really specifically cameras
[00:04:23] Sanjit Biswas: were getting really good because this is probably
[00:04:25] Sanjit Biswas: seven, eight years after the iPhone launch.
[00:04:27] Sanjit Biswas: So cameras had gotten extraordinary.
[00:04:30] Sanjit Biswas: And you combine all these three things together.
[00:04:31] Sanjit Biswas: You've got connectivity, you've got compute
[00:04:33] Sanjit Biswas: and you've got sensor slash cameras.
[00:04:35] Sanjit Biswas: And we said, this is the sort of like makings
[00:04:37] Sanjit Biswas: for a total sea change when it comes to ability
[00:04:41] Sanjit Biswas: to process data in real world context.
[00:04:43] Sanjit Biswas: Wonderful.
[00:04:44] Pat Grady: Okay, I'm excited to know that more about technical questions
[00:04:47] Pat Grady: on the frontier of physical AI.
[00:04:49] Pat Grady: Before we get into it, maybe can you just say a word
[00:04:51] Pat Grady: on Simpsara for our listeners?
[00:04:54] Pat Grady: I guess how much of the business is,
[00:04:55] Pat Grady: I think of it as very much a having it
[00:04:58] Pat Grady: had roots in commercial trucking.
[00:04:59] Pat Grady: How much of the business is that today?
[00:05:01] Pat Grady: And whether you see the ultimate vision
[00:05:02] Pat Grady: of Simpsara being?
[00:05:03] Pat Grady: Yeah, so we really focus on the broad world
[00:05:06] Sanjit Biswas: of physical operations.
[00:05:07] Sanjit Biswas: So think about all these different kinds of industries
[00:05:09] Sanjit Biswas: trucking is definitely one of them.
[00:05:10] Sanjit Biswas: It's about 20, 25% of our business.
[00:05:12] Sanjit Biswas: So logistics and big trucks on the road.
[00:05:15] Sanjit Biswas: A lot of our business now is related field service
[00:05:17] Sanjit Biswas: and construction.
[00:05:18] Sanjit Biswas: So other big kind of frontline industries.
[00:05:21] Sanjit Biswas: But we also are starting to work in like public sector.
[00:05:24] Sanjit Biswas: So we work with local governments.
[00:05:25] Sanjit Biswas: We work with student transit.
[00:05:27] Sanjit Biswas: So we just signed like the largest yellow school bus operator
[00:05:30] Sanjit Biswas: in North America, which is pretty cool.
[00:05:32] Sanjit Biswas: And we work in industries like aviation.
[00:05:34] Sanjit Biswas: So think about labor intensive asset heavy industries
[00:05:38] Sanjit Biswas: that really power the infrastructure of the planet.
[00:05:41] Pat Grady: Can I go back to your comment on?
[00:05:42] Sonya Huang: So at the time, there was a Y now around bandwidth,
[00:05:45] Sonya Huang: compute, and cameras.
[00:05:47] Sonya Huang: Yeah.
[00:05:47] Sonya Huang: And it sounds like you may not have necessarily had a crystal ball
[00:05:51] Sonya Huang: and what was going to happen with AI.
[00:05:53] Sonya Huang: Yeah.
[00:05:53] Sonya Huang: But you kind of felt like you're on the right side of history.
[00:05:56] And that with those raw ingredients,
[00:05:58] Sonya Huang: you'd be able to do increasingly sophisticated stuff
[00:06:00] Sonya Huang: over time.
[00:06:01] Sonya Huang: Yeah.
[00:06:03] Sonya Huang: What I'm curious about, I feel like there
[00:06:04] Sonya Huang: are a lot of founders today who are kind
[00:06:06] Sonya Huang: of in a similar position where nobody has a crystal ball.
[00:06:08] Sonya Huang: We don't really know what's coming.
[00:06:10] But you kind of know that whatever capabilities
[00:06:12] Sonya Huang: you're going to have tomorrow are very different and better
[00:06:14] Sonya Huang: than whatever capabilities you have today.
[00:06:16] Sanjit Biswas: Yeah.
[00:06:16] Sanjit Biswas: So I guess the question is like, since you kind
[00:06:19] Sonya Huang: of had a directional sense for where the world was going,
[00:06:21] Sonya Huang: how did that influence the way you built the business?
[00:06:24] Sonya Huang: Like was there anything specifically you did,
[00:06:26] Sonya Huang: just kind of in anticipation of this inevitable direction
[00:06:29] Sonya Huang: that the world was going?
[00:06:31] Well, actually the historical context
[00:06:33] Sanjit Biswas: is important.
[00:06:33] Sanjit Biswas: So our first company, Maraki, which was funded by Sequoia,
[00:06:37] Sanjit Biswas: we were domain experts.
[00:06:38] Sanjit Biswas: So we knew a ton about networking
[00:06:40] Sanjit Biswas: because that's what we'd been working on in terms of our PhD.
[00:06:42] Sanjit Biswas: With Sam Sar, it was kind of the opposite.
[00:06:44] Sanjit Biswas: We knew nothing about this domain.
[00:06:45] Sanjit Biswas: Like we'd never driven a commercial truck
[00:06:47] Sanjit Biswas: before I'd never worked in a warehouse.
[00:06:49] Sanjit Biswas: And so we were sort of eyes open about it.
[00:06:51] Sanjit Biswas: What we did have was that intuitive sense
[00:06:52] Sanjit Biswas: of the compounding rate of those underlying technologies.
[00:06:55] Sanjit Biswas: So we said, OK, there's this really interesting problem
[00:06:58] Sanjit Biswas: space, this world of physical operations.
[00:07:00] Sanjit Biswas: It's kind of like overlooked, especially 10 years ago,
[00:07:02] Sanjit Biswas: no one was really talking about infrastructure
[00:07:04] Sanjit Biswas: the way they are now.
[00:07:06] Sanjit Biswas: But things are changing very quickly
[00:07:09] Sanjit Biswas: behind the scenes in terms of tooling.
[00:07:10] Sanjit Biswas: So that intuition is exactly sort of what we were powered by.
[00:07:14] Sanjit Biswas: And we said, even if it's not mainstream yet,
[00:07:17] Sanjit Biswas: or it's not ready yet, certainly in five to 10 years, which
[00:07:20] Sanjit Biswas: is about now, it will be possible to do this stuff.
[00:07:23] Sanjit Biswas: So I think for a lot of the current founders,
[00:07:25] Sanjit Biswas: it's kind of like if you look at AI model capabilities,
[00:07:28] Sanjit Biswas: even when the chat GPT moment happened,
[00:07:31] Sanjit Biswas: these models weren't perfect.
[00:07:32] Sanjit Biswas: They've gotten a lot better in the last two, three years,
[00:07:35] Sanjit Biswas: and they're going to get even better in the next two to three years.
[00:07:37] Sanjit Biswas: I think technical people understand that
[00:07:39] Sanjit Biswas: in a way that consumers and customers often may not see yet.
[00:07:43] Pat Grady: So I think given embedded systems background,
[00:07:45] Pat Grady: and you're one of the unique people that's operated
[00:07:49] Pat Grady: at the intersection of the hardware and software worlds,
[00:07:52] Pat Grady: I'm curious, what are the things that make
[00:07:54] Pat Grady: building AI in the physical world different
[00:07:58] Pat Grady: than running AI in big data centers?
[00:08:01] A couple of things.
[00:08:02] Sanjit Biswas: Well, it actually is a lot of fun.
[00:08:04] Sanjit Biswas: So the physical world is very diverse.
[00:08:06] Sanjit Biswas: You see a lot of companies now working
[00:08:08] Sanjit Biswas: on physical intelligence and world models.
[00:08:10] Sanjit Biswas: And it's because the training data set is really broad and vast.
[00:08:14] Sanjit Biswas: So if you think about our products,
[00:08:15] Sanjit Biswas: we have products like dash cams that end up on the roads,
[00:08:18] Sanjit Biswas: on millions of vehicles.
[00:08:19] Sanjit Biswas: They see like 99% of the US roads.
[00:08:22] Sanjit Biswas: It's just an incredible data set.
[00:08:23] Sanjit Biswas: You've got urban, you've got rural,
[00:08:25] Sanjit Biswas: you've got residential, you've got weather.
[00:08:26] Sanjit Biswas: And so we see all these interesting exceptional cases.
[00:08:30] Sanjit Biswas: So the training data is really interesting.
[00:08:32] Sanjit Biswas: And then what we can apply all the inference
[00:08:34] Sanjit Biswas: and basically pattern matching too is also interesting.
[00:08:37] Sanjit Biswas: So I think that's the most fun part.
[00:08:39] Sanjit Biswas: The most challenging part, though,
[00:08:40] Sanjit Biswas: is how messy it is and how distributed it is.
[00:08:43] Sanjit Biswas: So for our products, it's not practical for us to just
[00:08:48] Sanjit Biswas: stream all the data to the cloud.
[00:08:50] Sanjit Biswas: It would be like a crazy bandwidth bill.
[00:08:52] Sanjit Biswas: You need pretty massive data centers
[00:08:54] Sanjit Biswas: if you think about millions of video streams,
[00:08:56] Sanjit Biswas: constantly running inference.
[00:08:58] Sanjit Biswas: And so we have a much more distributed architecture
[00:09:00] Sanjit Biswas: where we actually run in the cameras themselves.
[00:09:03] Sanjit Biswas: And that changes your compute and power footprint.
[00:09:07] Sanjit Biswas: We're talking about two to 10 watts, not like kilowatts,
[00:09:11] Sanjit Biswas: but you can do a lot more because you've got millions of them.
[00:09:14] Sanjit Biswas: And so what is it?
[00:09:16] Pat Grady: Like how do you run, I'm thinking some of these large LLMs,
[00:09:19] Pat Grady: and even the image models are very large right now
[00:09:23] Pat Grady: that people are working with.
[00:09:24] Pat Grady: Are you running just very bespoke small models on two to 10 watts?
[00:09:28] Pat Grady: That doesn't give you much of what the number is.
[00:09:30] Pat Grady: It doesn't give you a lot of room.
[00:09:31] Sanjit Biswas: And that's a fun engineering problem.
[00:09:32] Sanjit Biswas: So if you think about it, these state of the art models,
[00:09:35] Sanjit Biswas: they are very large.
[00:09:35] Sanjit Biswas: So you're talking about hundreds of millions of parameters
[00:09:39] Sanjit Biswas: or billions of parameters.
[00:09:40] Sanjit Biswas: That is simply not possible.
[00:09:42] Sanjit Biswas: So our footprint is much more similar
[00:09:44] Sanjit Biswas: to what you could run on like your mobile phone.
[00:09:46] Sanjit Biswas: So it's not tiny.
[00:09:47] Sanjit Biswas: It's not a microcontroller.
[00:09:49] Sanjit Biswas: It runs Linux.
[00:09:49] Sanjit Biswas: It's got like hundreds of megs of memory, maybe gigs.
[00:09:54] Sanjit Biswas: But it's not like a big data center, right?
[00:09:56] Sanjit Biswas: So what we tend to do is we will train models in the cloud
[00:10:00] Sanjit Biswas: will basically distill them down or use t-shirt models.
[00:10:03] Sanjit Biswas: We'll use a big model to basically instruct a small model
[00:10:06] Sanjit Biswas: that's really designed for our use case
[00:10:08] Sanjit Biswas: because we don't need to be able to answer
[00:10:11] Sanjit Biswas: what the capital France is, right?
[00:10:12] Sanjit Biswas: Like that's not something that Dashcam has to encounter.
[00:10:15] Sanjit Biswas: But we do need to be able to understand
[00:10:17] Sanjit Biswas: what is the risk profile in the road.
[00:10:18] Sanjit Biswas: So we train it with the data that's relevant for the task.
[00:10:21] How much of the data you see 99% of US highways or US roads?
[00:10:25] Sonya Huang: How much of that data can you make use of?
[00:10:28] Sonya Huang: How much of that data do you make use of?
[00:10:29] Sonya Huang: Yeah.
[00:10:31] Sanjit Biswas: We can make use of a lot of it.
[00:10:33] Sanjit Biswas: And we basically have the ability to train over
[00:10:35] Sanjit Biswas: like this entire data set.
[00:10:37] Sanjit Biswas: There is a very practical question of like, okay,
[00:10:39] Sanjit Biswas: you run a tokenizer at the edge,
[00:10:41] Sanjit Biswas: you send all these to the cloud, what do you do with it?
[00:10:44] Sanjit Biswas: And what's cool about that is what we do at this year
[00:10:46] Sanjit Biswas: is so much more interesting
[00:10:48] Sanjit Biswas: than what we could do at the two, three years ago.
[00:10:50] Sanjit Biswas: So two to three years ago,
[00:10:51] Sanjit Biswas: and these products really started around this idea
[00:10:53] Sanjit Biswas: of reducing risk.
[00:10:54] Sanjit Biswas: So if we think about the problem we're trying to solve,
[00:10:56] Sanjit Biswas: it's that our operations customers,
[00:10:59] Sanjit Biswas: they operate on these roads every day.
[00:11:01] Sanjit Biswas: It's actually the riskiest thing that they do
[00:11:03] Sanjit Biswas: is more so than construction or working in oil and gas,
[00:11:06] Sanjit Biswas: driving on the highway, getting to and from the job site,
[00:11:08] Sanjit Biswas: is where they incur most of their fatality
[00:11:11] Sanjit Biswas: or kind of a high severity risk.
[00:11:14] Sanjit Biswas: So the question is how do you go take all these images
[00:11:17] Sanjit Biswas: and tokens and turn it into a risk signal?
[00:11:19] Sanjit Biswas: A couple of years ago, we said,
[00:11:22] Sanjit Biswas: the biggest risk we are seeing right now
[00:11:24] Sanjit Biswas: is mobile phone usage, right?
[00:11:25] Sanjit Biswas: Like people are on their mobile device
[00:11:26] Sanjit Biswas: while driving a big truck, and that's super risky.
[00:11:29] Sanjit Biswas: So we built a detector for that.
[00:11:31] Sanjit Biswas: You do that and you say, okay, we can solve this problem.
[00:11:34] Sanjit Biswas: We can detect mobile phones, what else drives risk?
[00:11:37] Sanjit Biswas: Now we're seeing things like weather, right?
[00:11:39] Sanjit Biswas: And weather's always been a risk factor.
[00:11:40] Sanjit Biswas: It's not a brand new one,
[00:11:42] Sanjit Biswas: but it's now something we can detect
[00:11:43] Sanjit Biswas: using these pretty sophisticated models.
[00:11:46] Sanjit Biswas: Training a weather detector using old school
[00:11:49] Sanjit Biswas: convolutional networks, like an Alex Natshtow model,
[00:11:52] Sanjit Biswas: you would have gotten a lot of things wrong.
[00:11:53] Sanjit Biswas: You couldn't tell the road conditions.
[00:11:55] Sanjit Biswas: Once you use more sophisticated models
[00:11:57] Sanjit Biswas: like the ones we have today, you can really figure it out.
[00:11:59] Sanjit Biswas: So that's a cool thing.
[00:12:01] Sanjit Biswas: Is there these unlocks that happen every couple of years
[00:12:03] Sanjit Biswas: as model capabilities increase
[00:12:04] Sanjit Biswas: and are data set increases?
[00:12:06] Sanjit Biswas: So these two things like really work in our favor.
[00:12:09] Is there an upcoming unlock
[00:12:10] Sonya Huang: that you are most looking forward to?
[00:12:13] Sanjit Biswas: In terms of our product set or just in general?
[00:12:15] Sanjit Biswas: Is there a new capability that's going to unlock
[00:12:16] Sonya Huang: some new use case or feature for your product?
[00:12:20] Sanjit Biswas: You know, I feel like we are seeing
[00:12:22] Sanjit Biswas: just such incredible foundational model capabilities
[00:12:25] Sanjit Biswas: that are making it possible to just
[00:12:28] Sanjit Biswas: inference over huge amounts of data.
[00:12:29] Sanjit Biswas: So historically what we did is we understood
[00:12:32] Sanjit Biswas: like what was happening in the moment, right?
[00:12:33] Sanjit Biswas: So like I said, mobile phone detection
[00:12:35] Sanjit Biswas: or not wearing a seat belt or following distance.
[00:12:38] Sanjit Biswas: Now we can start to really look over the course of a trip.
[00:12:41] Sanjit Biswas: And we're not only detecting like negative
[00:12:43] Sanjit Biswas: like risky downside events,
[00:12:45] Sanjit Biswas: but we can actually detect good behaviors too.
[00:12:47] Sanjit Biswas: And I'm really excited about that
[00:12:48] Sanjit Biswas: because frontline workers,
[00:12:49] Sanjit Biswas: 80, 90% of the time is doing a great job.
[00:12:51] Sanjit Biswas: No one's able to recognize it because no one sees it.
[00:12:54] Sanjit Biswas: So what's awesome is we can now see that someone's doing awesome
[00:12:58] Sanjit Biswas: and give them a high five or like some kind of recognition
[00:13:00] Sanjit Biswas: or kudos, that is like making people's day.
[00:13:03] Sanjit Biswas: And it's a cool like silver lining side effect
[00:13:05] Sanjit Biswas: of having all this stuff running.
[00:13:07] Sanjit Biswas: So anyway, it's kind of an unexpected upside sort of.
[00:13:10] Sanjit Biswas: Yeah.
[00:13:11] Sanjit Biswas: And do you think it'll be video reasoning models
[00:13:14] Pat Grady: that sort of empower that?
[00:13:16] Pat Grady: And then you can't run a ton.
[00:13:17] Pat Grady: You can't run giant models at the edge,
[00:13:19] Pat Grady: but are you doing stuff server side?
[00:13:21] Pat Grady: Like it takes advantage of all of them.
[00:13:22] Pat Grady: Yeah, I should have mentioned that.
[00:13:23] Pat Grady: So the model's connected.
[00:13:26] Sanjit Biswas: We have a ton of inference running at the edge
[00:13:28] Sanjit Biswas: is running continuously because when you're driving,
[00:13:30] Sanjit Biswas: there's like continuous risk.
[00:13:31] Sanjit Biswas: And then we're taking those tokens,
[00:13:33] Sanjit Biswas: we're streaming them up.
[00:13:34] Sanjit Biswas: And in addition, we have images, we have video,
[00:13:37] Sanjit Biswas: we have other kinds of telemetry.
[00:13:39] Sanjit Biswas: And then we can go and run all kinds
[00:13:41] Sanjit Biswas: of sophisticated things in the cloud.
[00:13:43] Sanjit Biswas: So if we need to understand when an accident happened,
[00:13:45] Sanjit Biswas: what really happened, we can run a full video language model,
[00:13:49] Sanjit Biswas: like a reasoning model essentially in the cloud.
[00:13:51] Sanjit Biswas: And that can say, oh, this was actually defensive driving.
[00:13:54] Sanjit Biswas: And this guy got cut off or these were the conditions.
[00:13:57] Sanjit Biswas: So that is really cool.
[00:13:59] Sanjit Biswas: We couldn't have done that five years ago.
[00:14:01] Do you believe in world models?
[00:14:02] Pat Grady: Load the question.
[00:14:04] Sanjit Biswas: I do.
[00:14:05] Sanjit Biswas: I'm cautiously optimistic about them,
[00:14:07] Sanjit Biswas: but I think you need a tremendous amount of data.
[00:14:09] Sanjit Biswas: Yeah.
[00:14:10] Pat Grady: Are you guys training your own world model?
[00:14:12] We are not building our own world model.
[00:14:14] Sanjit Biswas: And I think that requires a very specific kind of focus.
[00:14:17] Sanjit Biswas: But in the same way, we don't train our own base foundation
[00:14:21] Sanjit Biswas: models, but we are looking forward to using them at some point.
[00:14:24] Yeah.
[00:14:24] And imagine you have an incredibly rich data set
[00:14:26] Pat Grady: that might be useful.
[00:14:28] Pat Grady: We do.
[00:14:28] Pat Grady: Yeah.
[00:14:28] Pat Grady: We see about 90 billion miles on our system every year.
[00:14:32] Sanjit Biswas: So it's a lot of driving.
[00:14:34] Yeah.
[00:14:34] It seems like the sensor footprint you've built out
[00:14:37] Pat Grady: is like a tech nerd's dream, right?
[00:14:40] Pat Grady: Most people dream of a connected world.
[00:14:43] Pat Grady: And you should be able to have so much telemetry
[00:14:45] Pat Grady: on all these different attributes with the physical world.
[00:14:48] Pat Grady: But as far as I can tell, you're one of the only companies
[00:14:50] Pat Grady: that's really out gone out and put sensors on the physical world
[00:14:55] Pat Grady: in a really meaningful way.
[00:14:57] Pat Grady: Why do you think that is?
[00:14:58] Pat Grady: And what's the key to actually be able to make that dream happen
[00:15:02] Pat Grady: versus have it just be a tech nerd's dream?
[00:15:05] Yeah.
[00:15:05] First of all, it takes a village to actually get
[00:15:09] Sanjit Biswas: this stuff out there.
[00:15:11] Sanjit Biswas: And I think that's maybe one other big difference
[00:15:13] Sanjit Biswas: between just pure software and physical world
[00:15:15] Sanjit Biswas: is we have to get the products installed.
[00:15:18] Sanjit Biswas: So they're installed on millions of vehicles.
[00:15:20] Sanjit Biswas: We have to train frontline workforces
[00:15:22] Sanjit Biswas: on what the stuff is and what it's doing.
[00:15:25] Sanjit Biswas: And then we have to provide value to all these customers
[00:15:27] Sanjit Biswas: kind of from day one, right?
[00:15:29] Sanjit Biswas: They have to get something out of it.
[00:15:31] Sanjit Biswas: You combine all this together and you get this big footprint.
[00:15:33] Sanjit Biswas: But it's been hard because you need thousands of people
[00:15:36] Sanjit Biswas: at our scale now to do this and to do the change management,
[00:15:39] Sanjit Biswas: like the installs and all that kind of stuff.
[00:15:42] Sanjit Biswas: You know, there are a few companies
[00:15:43] Sanjit Biswas: that have data sets of the scale,
[00:15:44] Sanjit Biswas: but it's like Tesla and then probably us, right?
[00:15:47] Sanjit Biswas: And then Waymo, there's thousands of Waymo's
[00:15:49] Sanjit Biswas: but not millions and maybe it will be millions in the future,
[00:15:52] Sanjit Biswas: but we're not there yet.
[00:15:53] Sanjit Biswas: So that gives you a sense of how much effort
[00:15:56] Sanjit Biswas: is just like sheer willpower is required to get this stuff out there.
[00:15:59] Sanjit Biswas: Speaking of which, I think there are a lot of founders right now
[00:16:04] Sonya Huang: who are technical founders like yourself
[00:16:07] Sonya Huang: who've built something cool and are now encountering
[00:16:13] Sonya Huang: this crazy supercharged race to scale
[00:16:17] Sonya Huang: that the AI wave seems to have brought.
[00:16:20] Sonya Huang: And so I guess the question is, you are a technical founder.
[00:16:24] I think both Sam Sara and Maraki have been known
[00:16:28] Sonya Huang: for go-to-market execution.
[00:16:30] Sonya Huang: And so maybe the question is like,
[00:16:32] Sonya Huang: how important has go-to-market execution been
[00:16:35] Sonya Huang: to your success?
[00:16:36] Sonya Huang: And as a technical founder, was it obvious to you
[00:16:42] Sonya Huang: at the beginning that it was gonna be that important
[00:16:43] Sonya Huang: or kind of what was your journey like
[00:16:45] Sonya Huang: and like appreciating the importance of go-to-market execution?
[00:16:49] Sonya Huang: Does that make sense?
[00:16:50] Sanjit Biswas: Yeah, I'm replaying like 20 years in my head really fast.
[00:16:52] Sanjit Biswas: So when we started Maraki, at that point in time,
[00:16:56] Sanjit Biswas: like I had never sold anything in my life.
[00:16:58] Sanjit Biswas: In fact, like as an engineering nerd,
[00:17:01] Sanjit Biswas: like I avoided any situation where there was like,
[00:17:04] Sanjit Biswas: you know, there's like fundraiser,
[00:17:06] Sanjit Biswas: you have to sell candy bars at school.
[00:17:07] Sanjit Biswas: Like there's like, does anyone need a website for this thing?
[00:17:10] Sanjit Biswas: You're not like, you just like trying to find some way out of it.
[00:17:12] Sanjit Biswas: So I really was not like a salesperson
[00:17:15] Sanjit Biswas: in terms of background and no one in my family had done sales.
[00:17:17] Sanjit Biswas: So it was very foreign.
[00:17:19] Sanjit Biswas: The thing that turned me on to it was this idea
[00:17:22] Sanjit Biswas: of this is what it takes to get the product out there.
[00:17:24] Sanjit Biswas: And if the product's not out there, it's not having impact.
[00:17:25] Sanjit Biswas: So if you're driven by impact, if that's what motivates you,
[00:17:28] Sanjit Biswas: it's fun to see people using it.
[00:17:30] Sanjit Biswas: Right.
[00:17:31] Sanjit Biswas: And then this is what makes this sustainable.
[00:17:32] Sanjit Biswas: So with Marockie, we were growing the company
[00:17:35] Sanjit Biswas: between 2006, it was acquired in 2012.
[00:17:37] Sanjit Biswas: In the middle of that was a great financial crisis, right?
[00:17:41] Sanjit Biswas: There wasn't a lot of funding at the time.
[00:17:43] Sanjit Biswas: Like risk capital was just like turned off.
[00:17:45] Sanjit Biswas: So we basically had to make the company operate at break even, right?
[00:17:48] Sanjit Biswas: Or they're abouts.
[00:17:49] Sanjit Biswas: And that's what really convinced us, like we have to figure out
[00:17:52] Sanjit Biswas: how to have sustainable sales execution
[00:17:55] Sanjit Biswas: and a model that's highly predictable.
[00:17:56] Sanjit Biswas: And as engineers were like, hey,
[00:17:58] Sanjit Biswas: this is actually a big engineering problem, right?
[00:18:01] Sanjit Biswas: And then that stuck with us with Sim.
[00:18:02] Sanjit Biswas: Sorry, we were talking about impact at scale.
[00:18:05] Sanjit Biswas: We raised capital along the way, but actually,
[00:18:07] Sanjit Biswas: we reinvested way more just from the revenue of the company
[00:18:10] Sanjit Biswas: in the gross margin.
[00:18:11] Sanjit Biswas: So if you look at our numbers Republic now,
[00:18:13] Sanjit Biswas: so you can kind of go back through the balance sheet,
[00:18:16] Sanjit Biswas: you can see we've invested probably close to $3 billion
[00:18:19] Sanjit Biswas: just in getting the stuff out there, right?
[00:18:21] Sanjit Biswas: R&D, customer success, all that stuff.
[00:18:23] Sanjit Biswas: That is only possible with a lot of sales.
[00:18:25] Sanjit Biswas: Right.
[00:18:26] Sanjit Biswas: So once you understand the why, you can kind of buy into it
[00:18:29] Sanjit Biswas: and say I'm going to figure this out.
[00:18:31] Sanjit Biswas: It was not natural for us, but it was a pivot
[00:18:33] Sanjit Biswas: that ended up being something we had to do.
[00:18:37] Sanjit Biswas: And I'm really glad we figured it out
[00:18:38] Sanjit Biswas: and have been getting better at it each year.
[00:18:40] Sanjit Biswas: Yeah.
[00:18:41] Maraki were domain experts.
[00:18:42] Pat Grady: Simsara, you were not when you started the company.
[00:18:46] Pat Grady: Why go and fake that domain?
[00:18:49] I think it was curiosity.
[00:18:51] Sanjit Biswas: And this is a little bit of like,
[00:18:53] Sanjit Biswas: you can go back to sort of curious nerd routes.
[00:18:55] Sanjit Biswas: Like you just find yourself like reading books
[00:18:57] Sanjit Biswas: and wondering how stuff works.
[00:18:59] Sanjit Biswas: So after Maraki, we actually didn't have a plan
[00:19:02] Sanjit Biswas: to start another company.
[00:19:03] Sanjit Biswas: There was a while I thought I was going to go back
[00:19:05] Sanjit Biswas: to grad school, finish the PhD kind of thing.
[00:19:08] Sanjit Biswas: Michael founder, John Bickett, he's like,
[00:19:10] Sanjit Biswas: way smarter, he's like, that's never going to work.
[00:19:12] Sanjit Biswas: But you go do that.
[00:19:14] Sanjit Biswas: And in that period of time, I realized
[00:19:16] Sanjit Biswas: that academic research is very long feedback
[00:19:19] Sanjit Biswas: loop kind of slow cycle.
[00:19:20] Sanjit Biswas: But there were a lot of other interesting problems
[00:19:22] Sanjit Biswas: that caught my attention.
[00:19:23] Sanjit Biswas: So I got interested, I think, in energy at that time.
[00:19:26] Sanjit Biswas: So I was like learning about how the electrical grid worked
[00:19:29] Sanjit Biswas: or the time didn't work because photovoltaics
[00:19:31] Sanjit Biswas: and renewables were coming online.
[00:19:33] Sanjit Biswas: I started getting curious about nuclear,
[00:19:35] Sanjit Biswas: about satellites and things like that.
[00:19:38] Sanjit Biswas: So it's kind of fun to be able to just open your mind up
[00:19:40] Sanjit Biswas: to everything when you've been like laser focused on one thing.
[00:19:44] Sanjit Biswas: And then over and over, I found myself
[00:19:46] Sanjit Biswas: and then John found himself like attracted
[00:19:48] Sanjit Biswas: to this world of infrastructure.
[00:19:49] Sanjit Biswas: And so it was just curiosity about this part
[00:19:52] Sanjit Biswas: of the world that felt pretty overlooked.
[00:19:54] Really cool.
[00:19:56] What do you think of autonomy?
[00:19:57] Pat Grady: And that may be a loaded question.
[00:19:59] Pat Grady: But I, two years ago, I avoided getting in LEMO's.
[00:20:02] Pat Grady: Now I don't think, no, I don't think so.
[00:20:03] Pat Grady: I say I've been safer in LEMO, not in one.
[00:20:07] Pat Grady: What's your point of view?
[00:20:09] Sanjit Biswas: Super excited about it, very bullish.
[00:20:10] Sanjit Biswas: I think it's been a long time coming.
[00:20:13] Sanjit Biswas: When I was in undergrad at Stanford,
[00:20:14] Sanjit Biswas: they were doing the first DARPA Grand Challenge cars.
[00:20:17] Sanjit Biswas: It was like 20 plus years ago now.
[00:20:19] Sanjit Biswas: And like you said, LEMO's have gone from kind of like prototype
[00:20:22] Sanjit Biswas: tests to like, I prefer LEMO, right?
[00:20:24] Sanjit Biswas: It's super consistent.
[00:20:26] Sanjit Biswas: There's lots of things to like about it.
[00:20:28] Sanjit Biswas: So our view on it is autonomy happens.
[00:20:31] Sanjit Biswas: And it actually increases the operational intensity
[00:20:33] Sanjit Biswas: of the world, right?
[00:20:34] Sanjit Biswas: So if you think about it, there's
[00:20:35] Sanjit Biswas: like a third shift between midnight and 8 a.m. roughly,
[00:20:39] Sanjit Biswas: that people tend not to work because they're sleeping.
[00:20:42] Sanjit Biswas: Imagine if operations like logistics could still
[00:20:44] Sanjit Biswas: run during that shift.
[00:20:47] Sanjit Biswas: And then same thing, imagine your field service technician,
[00:20:49] Sanjit Biswas: you need a part, like how amazing would it be if the part
[00:20:52] Sanjit Biswas: could just get delivered to you?
[00:20:53] Sanjit Biswas: Like that is something that's going
[00:20:54] Sanjit Biswas: to be a nice augment to operation.
[00:20:56] Sanjit Biswas: So we're a fan of it.
[00:20:58] Sanjit Biswas: Our view on it is we think it's an end, not an or exclusive.
[00:21:02] Sanjit Biswas: And it's interesting because typically when
[00:21:04] Sanjit Biswas: you see automation kick in, again, volume increases, right?
[00:21:08] Sanjit Biswas: Because costs come down.
[00:21:09] Sanjit Biswas: There's way more demand out there than people realize.
[00:21:12] Sanjit Biswas: Because sometimes you'll say, yeah, I could use that part,
[00:21:14] Sanjit Biswas: but I don't need to deliver it if it's going to cost $50
[00:21:16] Sanjit Biswas: for someone to drive it to me.
[00:21:18] Sanjit Biswas: If it costs $5 or no bucks, like how awesome would that be?
[00:21:21] Sanjit Biswas: So we kind of view it as like it will increase the speed
[00:21:24] Sanjit Biswas: that the world operates at.
[00:21:25] Sanjit Biswas: You think it's having on roads only,
[00:21:27] Pat Grady: or you have customers with warehouses and forklifts
[00:21:29] Pat Grady: and all the above, you think autonomy will hit all those sectors?
[00:21:32] Pat Grady: So I think autonomy already hit the warehouse.
[00:21:35] Sanjit Biswas: We have a lot of customers with big logistics warehouses.
[00:21:38] Sanjit Biswas: And really about 10 years ago, they
[00:21:40] Sanjit Biswas: started getting automated and meaningful way.
[00:21:42] Sanjit Biswas: And it's pretty rare for me to go into a heavily industrialized
[00:21:48] Sanjit Biswas: environment without seeing automation.
[00:21:50] Sanjit Biswas: And that's everything from lift systems
[00:21:52] Sanjit Biswas: to big arms moving things.
[00:21:54] Sanjit Biswas: And it actually is welcome by the people in the warehouse
[00:21:57] Sanjit Biswas: because it helps reduce injury.
[00:21:58] Sanjit Biswas: So if you think about it, frontline workers
[00:22:00] Sanjit Biswas: are putting themselves at risk when they do their job every day.
[00:22:03] Sanjit Biswas: It is not a great outcome to get hurt lifting a pallet
[00:22:06] Sanjit Biswas: or doing something like that.
[00:22:08] Sanjit Biswas: So that is I think a good sort of preview
[00:22:12] Sanjit Biswas: of what we're going to see out on the road.
[00:22:13] Sanjit Biswas: And then I think after that, there's
[00:22:15] Sanjit Biswas: a construction site and job site.
[00:22:16] Sanjit Biswas: Yeah.
[00:22:17] Pat Grady: Humanoid sales or no?
[00:22:19] Sanjit Biswas: Cautiously optimistic, a little bit scary.
[00:22:22] Sanjit Biswas: I won't lie.
[00:22:23] Sanjit Biswas: They feel like they're in that kind of creepy uncanny valley.
[00:22:25] Sanjit Biswas: Like when you see them walking around with that heads
[00:22:27] Sanjit Biswas: or hands or something.
[00:22:29] Sanjit Biswas: Have you seen Neo from a guy?
[00:22:31] Pat Grady: That's a friendly one.
[00:22:33] Sanjit Biswas: But I think it reminds me of where self-driving was
[00:22:36] Sanjit Biswas: about 10 years ago.
[00:22:37] Sanjit Biswas: So probably not a tomorrow, but it does feel inevitable.
[00:22:40] Sanjit Biswas: So as a capabilities increase, it's going to be really exciting.
[00:22:44] How does the role that Simpsar plays in the world
[00:22:47] Sonya Huang: change as we have more and more autonomy over time?
[00:22:50] Well, I kind of think of it as digital transformation.
[00:22:53] Sanjit Biswas: So if you zoom way out, that's what customers are excited about
[00:22:56] Sanjit Biswas: is how do we digitize these operations that
[00:22:58] Sanjit Biswas: have been around 50, 100 years in some cases.
[00:23:01] Sanjit Biswas: And most of our customers, they welcome new technology.
[00:23:04] Sanjit Biswas: So they adopted computers for route planning
[00:23:07] Sanjit Biswas: like in the 1970s or something like that.
[00:23:09] Sanjit Biswas: So they're not against technology.
[00:23:11] Sanjit Biswas: It's, is it going to help?
[00:23:12] Sanjit Biswas: Is it going to be relevant?
[00:23:14] Sanjit Biswas: So our take is you're going to want like a platform
[00:23:16] Sanjit Biswas: to see all of your operations for all of these different
[00:23:19] Sanjit Biswas: operations to interact.
[00:23:20] Sanjit Biswas: So you can see your frontline workers,
[00:23:22] Sanjit Biswas: you could see all your vehicles, you could see your assets,
[00:23:25] Sanjit Biswas: know what needs maintenance.
[00:23:26] Sanjit Biswas: All of these problems will be evergreen.
[00:23:28] Sanjit Biswas: You're going to want to maintain your assets like 20, 30 years
[00:23:31] Sanjit Biswas: from now, maybe they're robots, and maybe they move on their own,
[00:23:34] Sanjit Biswas: but they still need maintenance, for example.
[00:23:36] Sanjit Biswas: And then same thing, when you've got customer facing
[00:23:39] Sanjit Biswas: or end customer facing teams, you're still
[00:23:41] Sanjit Biswas: going to need to orchestrate hopefully thousands of people.
[00:23:44] Sanjit Biswas: And they may have help from robots and humanoids,
[00:23:47] Sanjit Biswas: and all kinds of stuff behind the scenes.
[00:23:49] Sanjit Biswas: But how do you kind of run the entire operation?
[00:23:51] Sanjit Biswas: So that's what we focus on as the big picture
[00:23:53] Sanjit Biswas: as opposed to any specific product or technology.
[00:23:56] How do you see the future of humans and AI interacting
[00:24:00] Pat Grady: in the physical world and in the industries that you serve?
[00:24:04] Well, I think they're getting closer and closer.
[00:24:06] Sanjit Biswas: So 10 years ago, when we started Simpshire,
[00:24:09] Sanjit Biswas: most of our customers did run on a lot of like pen and paper
[00:24:12] Sanjit Biswas: process, like 2015.
[00:24:14] Sanjit Biswas: It's not the distant past, right?
[00:24:15] Sanjit Biswas: Like it really has been a change that they've
[00:24:17] Sanjit Biswas: gone from pen and paper to apps.
[00:24:19] Sanjit Biswas: I think as AI kicks in, you see many of them
[00:24:22] Sanjit Biswas: like using voice bots for a freight brokerage, right?
[00:24:26] Sanjit Biswas: That's a brand new phenomenon really in the last year.
[00:24:29] Sanjit Biswas: And they've taken to it very quickly.
[00:24:31] Sanjit Biswas: It's automating tasks.
[00:24:32] Sanjit Biswas: So I kind of think of it as where are there,
[00:24:34] Sanjit Biswas: where's our high task intensity?
[00:24:36] Sanjit Biswas: A lot of like repetitive task work and can AI help?
[00:24:39] Sanjit Biswas: Absolutely.
[00:24:39] Sanjit Biswas: So that's where we're seeing like very high rates of adoption.
[00:24:43] Sanjit Biswas: I think the stuff that's not changing, at least not yet,
[00:24:45] Sanjit Biswas: is the physical work itself is still being done by people
[00:24:48] Sanjit Biswas: because it requires a lot of exception handling.
[00:24:50] Sanjit Biswas: So constructions are a great example.
[00:24:52] Sanjit Biswas: So much diversity in construction.
[00:24:54] Sanjit Biswas: We are not to the point where you can automate it
[00:24:56] Sanjit Biswas: the way you could automate like car manufacturing, for example.
[00:25:00] Do you think AI is, you know, you mentioned,
[00:25:03] Pat Grady: it's something that prevents risky behavior in humans.
[00:25:06] Pat Grady: Are you also seeing it kind of coach humans
[00:25:09] Pat Grady: in these operational environments to actually perform better?
[00:25:12] Yeah.
[00:25:12] So, you know, and first just thinking about risk,
[00:25:16] Sanjit Biswas: coaching makes a big difference.
[00:25:17] Sanjit Biswas: So there's risk detection, like, you know,
[00:25:19] Sanjit Biswas: please put down your mobile phone.
[00:25:21] Sanjit Biswas: But then if it's a habit of yours,
[00:25:23] Sanjit Biswas: we actually want to coach you to help break the habit, right?
[00:25:26] Sanjit Biswas: And if you kind of look at the impact
[00:25:29] Sanjit Biswas: we're able to have with customers,
[00:25:30] Sanjit Biswas: we often reduce risk by 75%.
[00:25:33] Sanjit Biswas: So, you know, three quarters of the risk
[00:25:35] Sanjit Biswas: comes out of the system.
[00:25:36] Sanjit Biswas: Maybe half of that can come from the automated, like in the moment,
[00:25:40] Sanjit Biswas: in Kabalert.
[00:25:41] Sanjit Biswas: And then the other half comes from coaching.
[00:25:43] Sanjit Biswas: And then that same coaching can be applied to like fuel efficiency.
[00:25:46] Sanjit Biswas: You can actually train drivers to operate heavy equipment
[00:25:49] Sanjit Biswas: in really smart ways.
[00:25:50] Sanjit Biswas: And you can gamify it, right?
[00:25:52] Sanjit Biswas: So that's the kind of like cool opportunity that AI has
[00:25:54] Sanjit Biswas: is process just enormous amounts of data
[00:25:57] Sanjit Biswas: more data than any human could do.
[00:25:59] Sanjit Biswas: You look at patterns across thousands or millions of vehicles
[00:26:02] Sanjit Biswas: and then turn it into actionable insight.
[00:26:04] Sanjit Biswas: That's coaching.
[00:26:05] Sanjit Biswas: So you can apply it to safety.
[00:26:07] Sanjit Biswas: You can apply it to efficiency.
[00:26:08] Sanjit Biswas: It's pretty cool.
[00:26:09] What's the organizing principle of your product portfolio?
[00:26:13] Pat Grady: Start from dash cams.
[00:26:14] Pat Grady: It's expanded out from there.
[00:26:15] Pat Grady: Yeah.
[00:26:16] Pat Grady: Maybe just tell us the history of how the product portfolio
[00:26:17] Pat Grady: is expanded and how you see the future.
[00:26:20] Yeah.
[00:26:21] Sanjit Biswas: So we actually started with GPS tracking or telematics.
[00:26:23] Sanjit Biswas: So 2015 dash cams were not quite viable.
[00:26:27] Sanjit Biswas: Yeah.
[00:26:28] Sanjit Biswas: But because of the cost for it.
[00:26:29] Sanjit Biswas: Yeah, cost and both like the backhaul cost of bandwidth,
[00:26:33] Sanjit Biswas: but also the cost of the cameras and things like that.
[00:26:37] Sanjit Biswas: But what was surprising to us was in 2015,
[00:26:40] Sanjit Biswas: most of the operational environments we went into,
[00:26:42] Sanjit Biswas: no one had any idea where their field teams were.
[00:26:45] Sanjit Biswas: They'd not in real time.
[00:26:46] Sanjit Biswas: And there was this like disconnect
[00:26:47] Sanjit Biswas: because Uber and DoorDash had started to happen, right?
[00:26:51] Sanjit Biswas: And so it was weird.
[00:26:52] Sanjit Biswas: The gig economy had real time tracking.
[00:26:54] Sanjit Biswas: But then like the logistics, like long haul logistics
[00:26:57] Sanjit Biswas: economy was still getting like bread crumbs,
[00:26:59] Sanjit Biswas: like every 10 to, I think it was like five to 15 minutes.
[00:27:03] Sanjit Biswas: And this probably predates most of people
[00:27:05] Sanjit Biswas: listen to the show.
[00:27:06] Sanjit Biswas: But there was this platform map quest
[00:27:09] Sanjit Biswas: that predated like Google Maps, right?
[00:27:10] Sanjit Biswas: So like 90s map quests like vintage map, right?
[00:27:13] Sanjit Biswas: So it wasn't around that.
[00:27:14] Sanjit Biswas: You got to print out the map quest directions
[00:27:17] Sonya Huang: and then take your piece of paper
[00:27:19] Sonya Huang: to figure out where you were going.
[00:27:20] Sonya Huang: And it was this kind of like grainy.
[00:27:21] Sanjit Biswas: It looked like Minecraft level graphics.
[00:27:24] Sanjit Biswas: The amazing part was our customers now back then
[00:27:28] Sanjit Biswas: were using map quest printouts.
[00:27:30] Sanjit Biswas: And their system for GPS tracking
[00:27:33] Sanjit Biswas: was built on top of map quest.
[00:27:34] Sanjit Biswas: So I would go on site and I would say,
[00:27:36] Sanjit Biswas: whoa, we can help with this.
[00:27:37] Sanjit Biswas: So that was product number one was GPS tracking.
[00:27:40] Sanjit Biswas: That got, that basically got us off the ground
[00:27:43] Sanjit Biswas: and got us into customers.
[00:27:45] Sanjit Biswas: And from there, we started figuring out,
[00:27:47] Sanjit Biswas: well, really the bigger challenge for them
[00:27:50] Sanjit Biswas: was managing risks because at that point in time,
[00:27:52] Sanjit Biswas: it was mid 2010s.
[00:27:53] Sanjit Biswas: People did have phones in their pockets.
[00:27:55] Sanjit Biswas: And they actually asked us, we're getting a lot of accidents.
[00:27:59] Sanjit Biswas: Do you have a dash cam?
[00:28:00] Sanjit Biswas: You recommend it works well with your system.
[00:28:02] Sanjit Biswas: So he said, if we built one for you, would you use it?
[00:28:04] Sanjit Biswas: And I said, yeah, absolutely.
[00:28:05] Sanjit Biswas: So John, my co-founder, remember, he went to like Amazon
[00:28:08] Sanjit Biswas: ordered like a webcam plugged into the USB port.
[00:28:11] Sanjit Biswas: And like over the weekend, wrote some code
[00:28:13] Sanjit Biswas: to get a basic webcam working.
[00:28:15] Sanjit Biswas: We brought it back to the customers
[00:28:16] Sanjit Biswas: the next week.
[00:28:17] Sanjit Biswas: They tried it.
[00:28:18] Sanjit Biswas: They loved it.
[00:28:18] Sanjit Biswas: And then we were watching the videos with them.
[00:28:21] Sanjit Biswas: And you could see as people were getting the accidents,
[00:28:23] Sanjit Biswas: they like had their phone out.
[00:28:25] Sanjit Biswas: And so he said, could we build a detection for that?
[00:28:27] Sanjit Biswas: So that's where the AI part of the dash cam came from.
[00:28:29] Sanjit Biswas: It was very iterative.
[00:28:31] Sanjit Biswas: And that has now become our largest product.
[00:28:33] Sanjit Biswas: But it's sold with the first product.
[00:28:36] Sanjit Biswas: So you asked about the portfolio strategy.
[00:28:38] Sanjit Biswas: It's concentric circles.
[00:28:39] Sanjit Biswas: It's keep doing what we started with.
[00:28:42] Sanjit Biswas: Core use case, adjacent use case.
[00:28:44] Sanjit Biswas: What else can we do?
[00:28:45] Sanjit Biswas: What else can we do?
[00:28:45] Sanjit Biswas: What else can we do?
[00:28:46] Sanjit Biswas: And now we have about 10 products out there.
[00:28:49] Really cool.
[00:28:49] You mentioned the back hall and network band
[00:28:52] Pat Grady: living, the binding constraints.
[00:28:54] Pat Grady: I'm curious if you think the growing adoption of Starlink
[00:28:57] Pat Grady: and just anywhere is going to change what it's possible
[00:29:00] Pat Grady: to do in the physical world.
[00:29:02] Absolutely.
[00:29:03] Sanjit Biswas: So we started, Simms are right around the 3G, 4G transition.
[00:29:08] Sanjit Biswas: And the unlock was actually YouTube.
[00:29:11] Sanjit Biswas: So if you remember 2015, everyone
[00:29:14] Sanjit Biswas: was starting to watch YouTube and baseball games
[00:29:16] Sanjit Biswas: and stuff on their phone.
[00:29:17] Sanjit Biswas: That drove data consumption way up in the carrier.
[00:29:19] Sanjit Biswas: The marginal cost per gigabyte came way down.
[00:29:23] Sanjit Biswas: And we were able to piggyback on that.
[00:29:25] Sanjit Biswas: And so that was really cool.
[00:29:26] Sanjit Biswas: I think something similar is happening now, not just with 5G,
[00:29:29] Sanjit Biswas: which is like the networks have invested even more.
[00:29:32] Sanjit Biswas: But now with satellite, the cost of building Starlink
[00:29:35] Sanjit Biswas: is enormous.
[00:29:36] Sanjit Biswas: I don't know how much is being spent on.
[00:29:38] Sanjit Biswas: There's like many tens of billions
[00:29:40] Sanjit Biswas: in launch capacity and so on.
[00:29:42] Sanjit Biswas: But the marginal cost to add another device to Starlink
[00:29:45] Sanjit Biswas: is pretty low.
[00:29:46] Sanjit Biswas: And that's the cost for any network effect.
[00:29:49] Sanjit Biswas: So we're excited about that because it'll help us get that last
[00:29:52] Sanjit Biswas: 1% of coverage.
[00:29:54] Sanjit Biswas: And a lot of our customers are in super remote rural areas.
[00:29:58] Sanjit Biswas: We have a lot of customers in energy, like oil and gas.
[00:30:01] Sanjit Biswas: There are no roads where they operate.
[00:30:02] Sanjit Biswas: And so there's not much cellular coverage either.
[00:30:05] Sanjit Biswas: Do you think that does away with some of the constraints
[00:30:07] Pat Grady: of running AI on the edge?
[00:30:09] Pat Grady: Meaning today, you can only use some percentage of,
[00:30:12] Pat Grady: you can only stream back some percentage of the data.
[00:30:14] Pat Grady: Because you do a lot of onboard compute.
[00:30:16] Pat Grady: Yeah.
[00:30:17] Pat Grady: And the world of just internet everywhere
[00:30:18] Pat Grady: where it's just a lot faster and cheaper
[00:30:20] Pat Grady: to send all data back and forth.
[00:30:23] Pat Grady: Could you be doing a lot of it server side?
[00:30:25] Pat Grady: And could you be doing a lot more?
[00:30:26] Pat Grady: You could do more of it.
[00:30:27] Sanjit Biswas: But it's funny how when stuff gets cheaper,
[00:30:30] Sanjit Biswas: you find a way to do more.
[00:30:32] Sanjit Biswas: And so when I think it's like a compression problem.
[00:30:37] Sanjit Biswas: If the workload was static, if you were just
[00:30:39] Sanjit Biswas: trying to get GPS data into the cloud,
[00:30:40] Sanjit Biswas: yes, just stream it all.
[00:30:42] Sanjit Biswas: It's not a big deal.
[00:30:42] Sanjit Biswas: If you were trying to get one frame per second video
[00:30:45] Sanjit Biswas: from an outward facing camera in the cloud, no problem.
[00:30:47] Sanjit Biswas: But if you want HD video from a 360 view of a truck,
[00:30:50] Sanjit Biswas: like eight cameras, that's a lot of video.
[00:30:54] Sanjit Biswas: And then same thing, if you want it with all the other
[00:30:56] Sanjit Biswas: telemetry that we get, it becomes pretty big.
[00:30:59] Sanjit Biswas: So I think you could potentially do it.
[00:31:02] Sanjit Biswas: But if you can push some of that to the edge
[00:31:04] Sanjit Biswas: and kind of like compress it down,
[00:31:06] Sanjit Biswas: everyone benefits from it.
[00:31:08] Pat Grady: Do you think controls in the autonomy
[00:31:10] Pat Grady: could ultimately be running in the cloud?
[00:31:12] Pat Grady: Do you think that's something people always want
[00:31:14] Pat Grady: to run on device?
[00:31:15] That one, I think you're probably
[00:31:17] Sanjit Biswas: going to see edge compute for a long time.
[00:31:20] Sanjit Biswas: And actually, if we kind of go a little technical for a second,
[00:31:23] Sanjit Biswas: one of the challenges there has been around power
[00:31:25] Sanjit Biswas: and computing cost, right?
[00:31:26] Sanjit Biswas: So if you think about a Tesla full self-driving computer,
[00:31:29] Sanjit Biswas: it's a couple of thousand bucks.
[00:31:30] Sanjit Biswas: It takes many hundreds of watts of energy.
[00:31:33] Sanjit Biswas: And they're like the first company
[00:31:34] Sanjit Biswas: to be making it really practical at scale.
[00:31:37] Sanjit Biswas: Way most probably a bit more.
[00:31:39] Sanjit Biswas: And so I do think that we will continue
[00:31:42] Sanjit Biswas: to see those sorts of approaches
[00:31:43] Sanjit Biswas: because safety is such a big deal.
[00:31:45] Sanjit Biswas: Like you've got humans in the cab,
[00:31:47] Sanjit Biswas: you've got humans on the road.
[00:31:49] Sanjit Biswas: You don't want a network outage
[00:31:51] Sanjit Biswas: to affect people's lives.
[00:31:54] Pat Grady: If we're sitting here in 2030,
[00:31:56] Pat Grady: what do you think is the biggest way that AI has transformed
[00:31:59] Pat Grady: the physical world and physical operations?
[00:32:02] I think a couple of thoughts.
[00:32:03] Sanjit Biswas: One is we're pretty early, right?
[00:32:05] Sanjit Biswas: We're at the end of 2025.
[00:32:07] Sanjit Biswas: The sort of AI adoption curve in physical operations
[00:32:11] Sanjit Biswas: were still the base of it.
[00:32:12] Sanjit Biswas: And so by 2030, I think we'll have run up the curve
[00:32:15] Sanjit Biswas: where it'd be much more mainstream.
[00:32:17] Sanjit Biswas: In the same way that like using apps
[00:32:19] Sanjit Biswas: is much more mainstream now than it was five, 10 years ago.
[00:32:22] Sanjit Biswas: So I think you will see the current technology
[00:32:24] Sanjit Biswas: is basically experienced a lot more diffusion.
[00:32:26] Sanjit Biswas: Like get out there.
[00:32:27] Sanjit Biswas: I think we were going to see net new technologies.
[00:32:29] Sanjit Biswas: Like I'm super excited about augmented reality and wearables.
[00:32:32] Sanjit Biswas: Like that's going to make huge difference
[00:32:34] Sanjit Biswas: to frontline workforces where they have to have their hands free.
[00:32:37] Sanjit Biswas: And it brings AI like into their ear.
[00:32:39] Sanjit Biswas: A lot of folks have AirPods in, right?
[00:32:41] Sanjit Biswas: But having like sort of visual feedback,
[00:32:43] Sanjit Biswas: being able to run like a VLM to understand
[00:32:46] Sanjit Biswas: what's going on in an environment.
[00:32:47] Sanjit Biswas: That will be possible in 2030.
[00:32:49] Sanjit Biswas: It's not quite possible yet,
[00:32:51] Sanjit Biswas: but you can just feel it.
[00:32:52] Sanjit Biswas: It's like right on the cusp.
[00:32:54] Pat Grady: Maybe it'll be glasses.
[00:32:56] Pat Grady: Maybe it'll be some of these new devices
[00:32:57] Pat Grady: that are under the wraps that are looking at with the app.
[00:33:01] Pat Grady: What's your favorite personal use of AI?
[00:33:04] Sanjit Biswas: Personal use of AI?
[00:33:06] Sanjit Biswas: Well, I love the sort of voice models.
[00:33:08] Sanjit Biswas: Like I talked to AI.
[00:33:10] Sanjit Biswas: Whenever I'm driving to a firm work,
[00:33:12] Sanjit Biswas: I'm chatting with it.
[00:33:13] Sanjit Biswas: And it's not always about anything specific.
[00:33:15] Sanjit Biswas: Like it's kind of whatever's on my mind.
[00:33:17] Sanjit Biswas: So I love that.
[00:33:19] Sanjit Biswas: I've become a big fan of like chat GPT pulse, for example.
[00:33:23] Sanjit Biswas: It's just cool that it tells you about.
[00:33:24] Sanjit Biswas: For me, events that are happening in the Bay Area,
[00:33:26] Sanjit Biswas: I've got three kids stuff.
[00:33:28] Sanjit Biswas: It kind of knows its interest, right?
[00:33:30] Sanjit Biswas: So that whole idea that AI could know you better than you
[00:33:34] Sanjit Biswas: to some extent is really profound.
[00:33:37] Sanjit Biswas: So I love that on the personal side.
[00:33:38] Sanjit Biswas: It kind of exposes us new experiences
[00:33:40] Sanjit Biswas: that we wouldn't have known about like,
[00:33:41] Sanjit Biswas: you know, a music performance or something like that
[00:33:44] Sanjit Biswas: that might get to like.
[00:33:45] Sanjit Biswas: Yeah.
[00:33:46] Pat Grady: How much of the value that you give customers
[00:33:48] Pat Grady: do you think is thanks to AI versus thanks
[00:33:51] Pat Grady: to all the other technology that you're building?
[00:33:54] It's an interesting question.
[00:33:57] Sanjit Biswas: We don't really just like split it out
[00:33:58] Sanjit Biswas: because like there's value in the data,
[00:34:01] Sanjit Biswas: but if no one looks at the data,
[00:34:03] Sanjit Biswas: it doesn't have impact, right?
[00:34:04] Sanjit Biswas: So one of the things we've heard from customers
[00:34:06] Sanjit Biswas: is this concern about data overload.
[00:34:08] Sanjit Biswas: Like if you have sensor streams from every vehicle
[00:34:11] Sanjit Biswas: and every front-line worker and every asset,
[00:34:14] Sanjit Biswas: what do you do with it all, right?
[00:34:15] Sanjit Biswas: And so AI is pretty awesome in terms of really helping
[00:34:18] Sanjit Biswas: just distill that down to something actionable.
[00:34:21] Sanjit Biswas: So that's why I don't think you can like split
[00:34:22] Sanjit Biswas: the two apart anymore.
[00:34:24] Sanjit Biswas: But it's transformed with its game changing
[00:34:26] Sanjit Biswas: and I spent a lot of time on the road.
[00:34:27] Sanjit Biswas: Like last week I was in Texas like all over
[00:34:32] Sanjit Biswas: a big food distributor, big willing gas company,
[00:34:35] Sanjit Biswas: spent time with like the Home Depot
[00:34:36] Sanjit Biswas: and it's just cool hearing how they're using the data
[00:34:39] Sanjit Biswas: in such creative ways and ones that they didn't have
[00:34:42] Sanjit Biswas: on their sort of road map when they started with us.
[00:34:45] Sanjit Biswas: But they're like, hey, if we can use this data
[00:34:47] Sanjit Biswas: to help do time card punches, right?
[00:34:50] Sanjit Biswas: Like get someone start on the shift
[00:34:51] Sanjit Biswas: and they don't have to walk to the office.
[00:34:53] Sanjit Biswas: That's awesome.
[00:34:54] Sanjit Biswas: Or if we can share this data with our end customer
[00:34:56] Sanjit Biswas: and let them know we're almost there or we're delayed,
[00:34:59] Sanjit Biswas: that's pretty cool.
[00:34:59] Sanjit Biswas: So it's really neat to see these emerging use cases.
[00:35:02] Really cool.
[00:35:03] Pat Grady: It's great to dream on all the way
[00:35:05] Pat Grady: that AI can kind of seep into all these different
[00:35:07] Pat Grady: workflows and everyday lives.
[00:35:09] Pat Grady: Yeah, and it's never any one thing.
[00:35:10] Sanjit Biswas: That's what I love about this is like every quarter
[00:35:13] Sanjit Biswas: we get exposed to some new use case.
[00:35:16] Sanjit Biswas: And a lot of it is just you spend time with the customer,
[00:35:19] Sanjit Biswas: you understand their operation and then you come up
[00:35:22] Sanjit Biswas: with like, hey, if we did that with that,
[00:35:23] Sanjit Biswas: like with a voice bot that made ETA delivery phone calls
[00:35:27] Sanjit Biswas: be useful to you.
[00:35:28] Sanjit Biswas: And many of our customers don't even know that's possible.
[00:35:30] Sanjit Biswas: They've never engaged with a voice bot before.
[00:35:32] Sanjit Biswas: So we'll do a demo for them.
[00:35:34] Sanjit Biswas: We'll do a prototype and they'll say,
[00:35:35] Sanjit Biswas: this is amazing, right?
[00:35:36] Sanjit Biswas: And so that's kind of fun to be able to kind of go back
[00:35:38] Sanjit Biswas: and forth.
[00:35:39] Sanjit Biswas: That's very cool.
[00:35:40] Sanjit Biswas: I'm curious and your point of view on,
[00:35:43] Pat Grady: there's so much talk of US or US or China, geopolitics
[00:35:47] Pat Grady: and our industrial base really needs to catch up.
[00:35:50] Pat Grady: Our robotics are manufacturing our physical AI
[00:35:52] Pat Grady: really needs to catch up.
[00:35:54] Pat Grady: I'm curious if you've seen that actually accelerate
[00:35:56] Pat Grady: customer conversations or have it impact on your business
[00:35:58] Pat Grady: in any way.
[00:36:00] Not in my customer conversations.
[00:36:02] Sanjit Biswas: I do think there's this like palpable sense
[00:36:04] Sanjit Biswas: of we need to modernize.
[00:36:05] Sanjit Biswas: And like how do we, how do we just rethink the way
[00:36:09] Sanjit Biswas: the infrastructure runs?
[00:36:10] Sanjit Biswas: So many of our customers are involved
[00:36:12] Sanjit Biswas: in data center buildouts right now.
[00:36:14] Sanjit Biswas: They're the energy utility, they're the construction company.
[00:36:16] Sanjit Biswas: Like there's a lot going on there.
[00:36:18] Sanjit Biswas: And I think that has everyone thinking,
[00:36:20] Sanjit Biswas: OK, what does this mean for us?
[00:36:22] Sanjit Biswas: And like what should be different about our business?
[00:36:24] Sanjit Biswas: So there's a lot of introspection going on.
[00:36:26] Sanjit Biswas: I haven't gotten a sense it's like US versus China.
[00:36:28] Sanjit Biswas: But it's more of like could we do this differently now?
[00:36:31] Sanjit Biswas: We're like firmly in the 21st century, right?
[00:36:33] Sanjit Biswas: Like it's what should be different now
[00:36:35] Sanjit Biswas: than the way that like you know previous generations
[00:36:37] Sanjit Biswas: ran these operations.
[00:36:39] Wonderful.
[00:36:40] You've been a multi-time legendary founder.
[00:36:43] Pat Grady: Any advice for young technical founders
[00:36:47] Pat Grady: who are out building an AI right now?
[00:36:49] I think it's an amazing time to build.
[00:36:51] Sanjit Biswas: Whether you've done this before or you're
[00:36:53] Sanjit Biswas: starting it for the first time.
[00:36:55] Sanjit Biswas: Just the tools that are available, it's incredible.
[00:36:59] Sanjit Biswas: And like to some extent, you know,
[00:37:02] Sanjit Biswas: everything's getting magnified or amplified, right?
[00:37:04] Sanjit Biswas: So I think about whether it's codex or cursor
[00:37:08] Sanjit Biswas: or all these like automated coding tools,
[00:37:10] Sanjit Biswas: if you have an idea now, you can like sort of manifest
[00:37:13] Sanjit Biswas: it into something real so much more easily
[00:37:16] Sanjit Biswas: than when we started, I'm sorry, even when we started
[00:37:18] Sanjit Biswas: Marockie, like back then we were like racking serve.
[00:37:20] Sanjit Biswas: We'd like buy servers from Dell and like take them to
[00:37:23] Sanjit Biswas: the data center and set them.
[00:37:24] Sanjit Biswas: Like can you imagine?
[00:37:25] Sanjit Biswas: It's just like how slow that feels now?
[00:37:26] Sanjit Biswas: I can't even imagine.
[00:37:27] Sanjit Biswas: It's actually hard to imagine.
[00:37:29] Sanjit Biswas: And but that is happening.
[00:37:30] Sanjit Biswas: And we will look back 10 years from now and say,
[00:37:32] Sanjit Biswas: can you believe we did X, right?
[00:37:34] Sanjit Biswas: I don't even know what X is, but it will feel so different.
[00:37:37] Sanjit Biswas: So it's fun to be on these like exponential curves.
[00:37:40] Sanjit Biswas: And the best place to be on that is to be building, right?
[00:37:43] Sanjit Biswas: Yeah.
[00:37:43] Sanjit Biswas: Really cool.
[00:37:44] Pat Grady: Thank you so much for taking time to share your story
[00:37:46] Pat Grady: and what you all are up to on the AI side at Simpsura.
[00:37:49] Pat Grady: Thanks.
[00:37:49] Pat Grady: Thanks for having me.
[00:37:50] Sanjit Biswas: Yeah.