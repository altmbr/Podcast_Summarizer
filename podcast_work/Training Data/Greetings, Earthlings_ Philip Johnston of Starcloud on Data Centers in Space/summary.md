# [Greetings, Earthlings: Philip Johnston of Starcloud on Data Centers in Space](https://pscrb.fm/rss/p/traffic.megaphone.fm/CPUAI3959632960.mp3)

**Podcast:** Training Data
**Date:** 2026-03-17
**Participants:** Pat Grady, Philip Johnston, Sonya Huang
**Episode URL:** https://pscrb.fm/rss/p/traffic.megaphone.fm/CPUAI3959632960.mp3
**YouTube:** [Watch on YouTube](https://youtube.com/watch?v=FKHENV75b9Q)
**Transcript:** [View Transcript](./transcript.md)

---

# Starcloud: Data Centers in Space — Training Data Podcast Summary

**Participants:** Pat Grady, Sonya Huang (hosts), Philip Johnston (Founder & CEO, Starcloud)

---

## 1. Key Themes

### The Terrestrial Energy Wall Is the Real Driver of Space Data Centers

The fundamental thesis isn't about space being cool — it's that Earth-based data center expansion is hitting a hard ceiling driven by permitting, land costs, and battery storage requirements. The economic crossover point where space becomes cheaper is closer than most realize.

> "The problem with doing this build out on Earth is that the marginal cost on every additional data center goes up every time you add one because we're using all the easy places to build energy projects. In space, the marginal cost goes down for every additional unit because you're manufacturing at rate and the more Starships you fly, the cheaper it gets." [00:00:00](https://youtube.com/watch?v=FKHENV75b9Q&t=0)

> "If you want to build a new 100 megawatt energy project, you're looking at a five to 10 year lead time just on the permitting, particularly in North America." [00:03:26](https://youtube.com/watch?v=FKHENV75b9Q&t=206)

The break-even launch cost is already achievable on the near horizon:

> "We see that break even to be around $500 a kilo. But as the cost of permitted land goes up, which it is going through the roof right now, that break even point actually comes even closer to $1,000 a kilo." [00:04:43](https://youtube.com/watch?v=FKHENV75b9Q&t=283)

---

### The Heat Dissipation Problem Is the Central Engineering Challenge — Not Radiation

Counter to intuition, cold space is not the advantage — vacuum is the problem. 70% of Starcloud's engineering resources go to thermal management, not radiation hardening.

> "Space is cold and in general that's actually once you get far enough down this rabbit hole that ends up being great. What's not great is that space is a vacuum. The only form of heat dissipation you can have is infrared radiation." [00:08:02](https://youtube.com/watch?v=FKHENV75b9Q&t=482)

> "A very small increase in the temperature increases the heat dissipation by a huge amount. And so one of the critical things is we need to run these radiators as hot as possible." [00:08:29](https://youtube.com/watch?v=FKHENV75b9Q&t=509)

Their solution uses heat pumps to artificially elevate radiator temperatures:

> "You can take, for example, 60 degree fluid from the chips, and then you can turn that into 100 degree radiator temperature with heat pumps." [00:08:55](https://youtube.com/watch?v=FKHENV75b9Q&t=535)

---

### Starcloud's Business Model Is Equinix, Not AWS — And That's Strategic

Philip articulates a deliberate decision to be infrastructure/colocation rather than a cloud provider, citing margin, focus, and competitive positioning against hyperscalers.

> "We would much rather be an infrastructure and energy play than a cloud provider and the reason is our core IP of the company and the core skill that we're good at is building satellites that can dissipate heat and protect you from radiation." [00:23:01](https://youtube.com/watch?v=FKHENV75b9Q&t=1381)

> "You can think of us more like Equinix while SpaceX might be more like AWS or something like that." [00:21:05](https://youtube.com/watch?v=FKHENV75b9Q&t=1265)

The key differentiator: customers bring their own chips and architecture.

> "We essentially give people a box and it has power, cooling and connectivity and then they can put whatever chip architecture they want in there and sell to whichever customers they want." [00:21:05](https://youtube.com/watch?v=FKHENV75b9Q&t=1265)

---

## 2. Contrarian Perspectives

### Training Will Become Less Than 1% of All AI Workloads — Inference Is Almost Everything

Most AI capital discussion focuses on training. Philip argues inference will so thoroughly dominate that training is barely worth optimizing for in space infrastructure planning.

> "Training at the end state will be less than one percent of all AI workloads that are being done and so it's just not a very good market to go after anyway." [00:15:11](https://youtube.com/watch?v=FKHENV75b9Q&t=911)

---

### Space Data Centers Will Be Cheaper Than Earth Data Centers — Not Just Competitive

The conventional assumption is that space compute is a premium, niche product. Philip argues the opposite: in the end state, space is the lowest-cost option, with energy costs below half a cent per kilowatt hour all-in.

> "Our all-in energy cost in the end state will be much lower than half a cent per kilowatt hour, including the launch cost." [00:30:51](https://youtube.com/watch?v=FKHENV75b9Q&t=1851)

> "Our infrastructure cost is instead of you know you're looking at 15 to 20 million dollars per megawatt for new infrastructure for a data center on earth... for us it's only less than five million dollars per megawatt." [00:30:24](https://youtube.com/watch?v=FKHENV75b9Q&t=1824)

---

### GPU Workloads Are Inherently Radiation-Resilient Due to Their Stochastic Nature

Most people assume radiation is catastrophic to precision computing. Philip's testing reveals that because GPU inference outputs are probabilistic, bit flips often don't meaningfully degrade output quality.

> "GPU workloads in general are very resilient. And the reason is they're stochastic in nature. So if you type into ChatGPT, write me a poem about space, it will give you two different poems... with a bit flip on any part of that workload, it actually doesn't make a difference to the quality of the output." [00:07:02](https://youtube.com/watch?v=FKHENV75b9Q&t=422)

---

### The Great Filter Is Ahead of Us, Not Behind — AI Killer Drones Are the Likely Mechanism

While not an investment thesis, this is a genuinely contrarian and sobering perspective from someone deep in the technology stack. Philip believes the Fermi Paradox is explained not by life being rare, but by superintelligence being self-terminating.

> "Once you hit super intelligence, you know, it wouldn't take very long for a swarm of a million killer AI drones to make mincemeat of both themselves and the planet. And we're building swarms of a million AI killer drones." [00:35:11](https://youtube.com/watch?v=FKHENV75b9Q&t=2111)

---

### Military / Government Edge Compute in Space Commands 1000x Pricing Premiums

Philip reveals that the military/government space edge market isn't just a bridge strategy — it's extraordinarily lucrative, making it a viable standalone business.

> "They're on the order of a thousand times more dollars per hour for GPU time than a terrestrial contract would be or if you're competing with terrestrial." [00:31:43](https://youtube.com/watch?v=FKHENV75b9Q&t=1903)

---

## 3. Companies Identified

**Starcloud**
- Founder's company. First commercial data center in space (Starcloud One). Building the infrastructure layer (Equinix model) for space-based compute.
- First mover with deployed hardware on orbit, IP in thermal management, and early military contracts.
- > "We will be by far the most advanced in terms of what's deployed on orbit and the engineering team and all the IP that we have." [00:22:04](https://youtube.com/watch?v=FKHENV75b9Q&t=1324)

---

**SpaceX**
- Launch vehicle manufacturer, Starship program. Described as the single most important enabling company for the entire space economy.
- Starcloud's launch partner; the declining cost curve of Starship is the linchpin of the entire business model.
- > "SpaceX like I think they're like unbelievable what they're pulling off... they're just so far ahead of everybody else." [00:19:20](https://youtube.com/watch?v=FKHENV75b9Q&t=1160)
- > "SpaceX are amazing partners. Our company definitely wouldn't exist without the Rideshare program." [00:20:09](https://youtube.com/watch?v=FKHENV75b9Q&t=1209)

---

**Stoke Space**
- Developing a fully reusable rocket with a competitive upper stage.
- Identified as one of the few credible competitors to SpaceX that could become cost-competitive in launch.
- > "The other companies that could [compete] — you need a reasonable upper stage to be anywhere close to cost competitive. So you have Stoke Space..." [00:19:20](https://youtube.com/watch?v=FKHENV75b9Q&t=1160)

---

**Varda Space Industries**
- In-space manufacturing company, doing pharmaceutical crystal growth in microgravity.
- Cited as an example of the emerging space manufacturing business model.
- > "Companies like Varda are doing crystal structures particularly for medicine and other things but that's purely because they want to take advantage of the microgravity." [00:39:47](https://youtube.com/watch?v=FKHENV75b9Q&t=2387)

---

**Planet Labs**
- Earth observation satellite company.
- Cited as a data point on Google's relatively slow pace of moving into space compute (paying Planet Labs for a 2027 demo rather than building internally).
- > "Google for example say they're doing what we're doing — what they're actually doing is they're paying Planet Labs to do a demo in 2027, which I mean, it seems like they're not moving particularly aggressively." [00:22:04](https://youtube.com/watch?v=FKHENV75b9Q&t=1324)

---

**Kepler Communications**
- LEO communications constellation.
- Mentioned as part of the now-solved optical mesh networking layer in space that enables space data center connectivity.
- > "There's a bunch of other constellations coming online — Amazon LEO, Kepler..." [00:14:12](https://youtube.com/watch?v=FKHENV75b9Q&t=852)

---

## 4. People Identified

**Philip Johnston** — Founder & CEO, Starcloud
- Former McKinsey consultant advising space agencies globally. Identified the launch cost inflection point early and built the first commercial space data center.
- Combines systems-level thinking across energy economics, satellite engineering, and AI infrastructure in a rare way.
- > "Three years ago I kind of randomly on a weekend decided to take a trip down to Starbase, Texas, where SpaceX is building the Starship launch vehicle. And I think it just blew me away the scale of the new sort of gigafactories they're building." [00:01:36](https://youtube.com/watch?v=FKHENV75b9Q&t=96)

---

**Ezra (co-founder, Starcloud)**
- Philip's childhood friend and technical co-founder. Has prior experience launching GPUs to space and conducting particle accelerator radiation testing.
- > "My co-founder Ali has previously launched a bunch of GPUs and did all this kind of particle accelerator testing." [00:18:22](https://youtube.com/watch?v=FKHENV75b9Q&t=1102)

*(Note: Philip refers to co-founder interchangeably as Ezra and Ali — likely same person or two co-founders)*

---

**NASA JPL Thermal Engineer (unnamed)**
- Designed the thermal system for NASA's Europa Clipper (NASA's largest, most expensive deep space mission) and Firefly lunar lander thermal systems.
- Recruited to Starcloud specifically for the thermal challenge, which consumes 70% of engineering resources.
- > "The guy from NASA's Jet Propulsion Laboratory who designed all of the thermal system for the Europa Clipper mission... he also designed the thermals on the Firefly lunar lander and for three of the NASA payloads." [00:17:28](https://youtube.com/watch?v=FKHENV75b9Q&t=1048)

---

## 5. Operating Insights

### Set Aggressive Token Consumption Targets as a Proxy for AI Adoption

Rather than tracking AI usage abstractly, Philip sets a concrete dollar-denominated floor for token spend per engineer per month and communicates it loudly as a cultural expectation.

> "I posted monthly reminder that I'm not going to be happy until every engineer is spending ten thousand dollars a month on tokens. I just don't want them to be like... I want to really drum it into them like this is literally what I expect and I will be happy when I'm spending 10 grand a month on tokens." [00:42:01](https://youtube.com/watch?v=FKHENV75b9Q&t=2521)

---

### Use AI Tool Recommendations as Investment/Competitive Signal

Philip notes that the specific tools and infrastructure that AI models recommend are themselves a signal worth tracking — and he's actively mining this for business intelligence.

> "There's a lot of signal in what kind of infrastructure and tools that the models recommend you to use." [00:41:34](https://youtube.com/watch?v=FKHENV75b9Q&t=2494)

---

### Design Your Bridge Revenue to Be 1000x Your Target Market's Pricing

Starcloud's military/edge contracts aren't just survival revenue — they're priced at 1000x commercial rates, making them a high-margin business in their own right while de-risking the Starship timeline dependency entirely.

> "We already are [running workloads for military customers] on Starcloud One... they're on the order of a thousand times more dollars per hour for GPU time than a terrestrial contract would be." [00:31:43](https://youtube.com/watch?v=FKHENV75b9Q&t=1903)

---

## 6. Overlooked Insights

### Space Orbital Slots Are Becoming Scarce Real Estate — And Nobody Is Treating Them That Way Yet

Philip briefly mentions filing for a constellation of 88,000 orbital slots and notes that today it's first-come, first-served — but valuable slots will fill up and become tradeable assets within 10 years. This is an enormous regulatory and real estate arbitrage opportunity that passed almost without comment.

> "For now it's essentially first come first serve... I've just filed for a constellation of 88,000 [slots]... 10 years from now I expect certainly the most valuable slots will get filled up and then it will probably be that whoever got them first will have the right to sell them." [00:24:24](https://youtube.com/watch?v=FKHENV75b9Q&t=1464)

The implication: orbital slot portfolios may become a distinct, highly valuable asset class — analogous to spectrum licenses or domain names — and the window to acquire them cheaply is closing now.

---

### SAR Satellites Are Throwing Away 90% of Their Data — Space Inference Unlocks a Hidden Intelligence Layer

This was mentioned almost in passing, but the magnitude is staggering: synthetic aperture radar satellites are currently discarding the vast majority of what they collect because downlink bandwidth is the bottleneck. Space-based inference directly solves this, creating an entirely new intelligence product from existing satellite infrastructure.

> "A SAR satellite — synthetic aperture radar — they might be collecting five gigabytes of data a second... when they're above a ground station they might be getting one gigabit a second data rate... right now they just throw away 90% of the data they collect." [00:32:34](https://youtube.com/watch?v=FKHENV75b9Q&t=1954)

> "They can ship enormous amounts of data to us through optical in space and then we can run inference workloads on that in space... identifying a vessel in that. At the moment they don't have the processing power on board to do that." [00:33:26](https://youtube.com/watch?v=FKHENV75b9Q&t=2006)

This positions Starcloud not just as compute infrastructure, but as the unlock for a massive latent defense and intelligence market that currently cannot monetize its own data.