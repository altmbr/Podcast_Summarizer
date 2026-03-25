# [The 20-year journey to fully autonomous cars with Dmitri Dolgov of Waymo](https://share.transistor.fm/s/4d6cad44)

**Podcast:** Cheeky Pint
**Date:** 2026-03-24
**Processed:** 2026-03-25T17:05:00Z
**Participants:** Dmitri Dolgov, Host (Cheeky Pint), Unidentified
**Episode URL:** https://share.transistor.fm/s/4d6cad44
**Transcript:** [View Transcript](./transcript.md)

---

# Summary: The 20-Year Journey to Fully Autonomous Cars with Dmitri Dolgov of Waymo

---

## 1. Key Themes

### The AI Inflection Point Was Waymo's True Unlock

The transition from modular ML systems to a unified AI backbone was the single most important technical leap Waymo made. Gen 4 used many small ML models; Gen 5 made AI the core. This architectural bet is what enabled rapid city expansion and generalization.

> "It was when we made this big bet on AI. Yeah. That was, there was a lot more, you know, kind of little AI models and ML models in the fourth generation. Got it. We made a much bigger bet and jump to kind of AI as the backbone for the fifth generation." [00:29:03]

### Full Autonomy and Driver Assist Are Fundamentally Different Problems, Not a Spectrum

Dolgov pushes back hard on the conventional wisdom that driver assist systems can incrementally evolve into full autonomy. He frames them as qualitatively different engineering challenges, which has massive implications for competitive dynamics in the space.

> "I think it's deceptive to think of them as kind of incremental, you know, on one spectrum of complexity... The hardest parts of building a fully autonomous rider-only system, they are very different from, you know, what you do for a driver assist system." [00:49:35]

### Waymo's Technical Architecture: Foundation Model → Teachers → Students

Waymo's system is built on a shared foundation model that specializes into three "teacher" models — the Waymo Driver, the Simulator, and the Critic — which then distill into smaller student models for real-time inference. This architecture is the operational secret sauce behind their scaling.

> "There's the Waymo driver, there is the simulator, and then there's the critic, right? And those then get distilled into smaller models that you can run, you know, inference on faster." [00:07:44]

---

## 2. Contrarian Perspectives

### End-to-End AI Alone Cannot Achieve Full Autonomy at Scale

While the AI/tech world debates end-to-end vs. modular, Dolgov argues the real answer is more nuanced: pure end-to-end (pixels in, trajectories out) is fine for driver assist but structurally insufficient for full autonomy because it makes simulation, reward function specification, and safety validation nearly impossible at scale.

> "If that's all you do, like, pixels in, trajectories out, it becomes very difficult to do all of those three and achieve the high level of safety and performance that we require... However, if, you know, that's, it's kind of a very easy way to get started." [00:13:32]

### Cameras-Only Is a False Economy for Full Autonomy

Against the Tesla-led narrative that cameras alone are sufficient, Dolgov explains why radar and LiDAR are not redundant — they have genuinely complementary physical properties, especially in adverse conditions where cameras fail entirely.

> "Radar is completely unaffected... you can imagine driving on a freeway, then radar will give you really good returns for, you know, cars that are absolutely, you know, invisible in the, you know, in the camera space." [00:39:07]

### The Industry Will Not Converge from Both Ends of the Autonomy Spectrum

The prevailing assumption is that Level 2/3 systems and Level 4/5 systems will meet in the middle. Dolgov flatly disagrees — Level 2/3 improvements and Level 4 expansion are solving different problems and won't meaningfully converge technologically.

> "I don't believe we will... I see it just as fundamentally two different problems. There's driver assist systems. And then there is full autonomy." [00:48:41]

### Starting Early on Self-Driving Was Not "Too Early" — The Complexity Required It

Many observers suggest Google/Waymo wasted years before AI was ready. Dolgov argues the iterative cycles were necessary and there was no magical moment to "just start" — the problem complexity doesn't disappear with new tools.

> "There are no silver bullets, right?... It's always been the nature of this problem. It's very easy to get started. It's deceptively easy to get started. But it is super hard to go, you know, the full distance." [01:00:15]

### Autonomous Vehicles Will Eliminate Parking Lots, Reshaping Urban Land Use Profoundly

While widely discussed in theory, Dolgov speaks about this with specificity and conviction that suggests it is genuinely near-term and transformative in a way most urban planners haven't priced in.

> "Right now, if you look at, you know, what is our most interesting pieces of land allocated to, you know, it's parking lots, it's garages... If, you know, more cars become fully autonomous, then there's no, you know, that, right?" [00:57:07]

---

## 3. Companies Identified

**Waymo**
- Description: Alphabet's autonomous vehicle company, formerly Google's self-driving car project
- Why mentioned: Operating 3,000 cars, 500,000 rides/week, 4M+ autonomous miles/week, in 11 US cities, launching in London and Tokyo in 2025
- > "We have about 3,000 cars on the roads. We're doing about half a million rides per week. That translates to about, you know, over 4 million fully autonomous miles per week." [00:47:14]

**Stripe**
- Description: Global payments infrastructure company
- Why mentioned: Called out as building the economic infrastructure for AI agents, enabling agent-initiated commerce
- > "Stripe is building the economic infrastructure for AI. And as part of that, we're letting payments be initiated by humans or by agents." [00:29:37]

**XTX Markets**
- Description: Quantitative trading firm based in the UK
- Why mentioned: Co-founder Alex Gurko cited as an example of the Russian mathematical diaspora producing world-class technical founders
- > "I'm struck by the founders of the two most valuable U.K. companies are Russian math nerds who both went to the same school. Uh, Nikolai at Revolution and Alex Gurko at XTX." [00:02:19]

---

## 4. People Identified

**Dmitri Dolgov**
- Description: Co-CEO of Waymo; joined Google's self-driving project in 2009 as one of its first engineers
- Why mentioned: Led the technical and organizational journey from research project to 500K rides/week commercial operation; the primary speaker sharing deep technical and strategic insight
- > "Dmitri Dolgov is co-CEO of Waymo. He joined Google's self-driving car project in 2009 as one of its first engineers and was repeatedly promoted until he took it over in 2021." [00:00:01]

**Larry Page & Sergey Brin**
- Description: Co-founders of Google/Alphabet
- Why mentioned: Credited with having the long-term conviction to fund Waymo through its 20-year journey, which most investors or corporate parents would have abandoned
- > "I just have to give credit and huge kudos and gratitude to Larry and Sergey and Alphabet Leadership Center company. It is part of the culture and the DNA of the company is to have that vision and have the stamina and conviction to go the distance." [00:58:47]

**Alex Gurko**
- Description: Co-founder of XTX Markets, one of the UK's most valuable companies
- Why mentioned: Cited as an example of elite Russian mathematical training producing exceptional technical founders in the West
- > "Alex Gurko at XTX... it's a strong diaspora." [00:02:19]

---

## 5. Operating Insights

### Sequenced De-Risking as a Product Development Framework

Waymo explicitly structured each hardware generation around answering the single most critical open question at that moment, rather than trying to solve everything at once. This is a transferable principle for any deep tech company managing long development cycles.

> "Throughout our history, we were very focused on setting the most, you know, the biggest goal for the company to de-risk the most important questions, right?... there's the sixth generation where it's made sense to go out and spend all this, you know, effort into the custom." [00:35:05]

### Tick-Tock Product Strategy for Hardware/Software Co-Evolution

Waymo's Gen 6 deploys dramatically new hardware (custom Ojai vehicle, cheaper sensor stack) on essentially the same software stack as Gen 5. This deliberate separation of innovation vectors reduces integration risk and allows both hardware and software teams to make maximal progress without blocking each other.

> "Gen 6 is a new vehicle and a new sensor stack, but it's almost a tick-tock cycle happening here. It's a similar software. That's right." [00:35:59]

### Depot Operations as a Leading Indicator of Unit Economics

Waymo's depot automation — cars self-routing to charging, flagging cleaning needs via sensor dome emoji displays, autonomously pulling into charging stalls — is the operational variable that will most directly drive down cost per ride. Investors should track depot automation milestones as a proxy for margin improvement.

> "Cars will automatically, you know, go on there, you know, to pick up their riders, you know, serve their trips. If for some reason, you know, they need to come back, you know, maybe they're low on energy, maybe somebody, you know, left a mess on the car, they will, you know, automatically come to the depot." [00:51:50]

---

## 6. Overlooked Insights

### Waymo's Sensor Fusion Discovered Emergent Capabilities Nobody Designed

Dolgov briefly mentioned — almost as an aside — that Waymo's car detected a pedestrian hidden behind a bus by bouncing peripheral LiDAR pulses under the vehicle's chassis to pick up foot movement. This was not a designed capability. It emerged from the AI learning to fuse noisy, multi-modal sensor data. The implication is profound: Waymo's system is developing perceptual capabilities that exceed what any engineer explicitly built, and the team is still discovering them. This suggests the performance ceiling of their current architecture is not yet known — even internally.

> "What actually turned out was happening is that our peripheral ladders bounce under the bus. And there was just a little bit of very, very noisy reflection of the movement of the person's feet. That was enough for the AI models that, hey, likely there's a pedestrian there... It just kind of blew my mind." [00:44:55]

### The VLM Zero-Shot Generalization to New Cities Is a Structural Moat Accelerant

Dolgov briefly mentioned that by connecting Waymo's physical AI to vision-language models (VLMs), they are achieving "really strong results from zero-shot or few-shot learning" in new geographic domains. This was glossed over in the conversation, but it means the cost and time to enter a new city is dropping dramatically — not just due to operational learnings, but because general world knowledge from internet-scale VLMs is now being inherited by the driving stack. The implication: Waymo's international expansion economics (London, Tokyo) may be far better than the historical city-by-city effort would suggest, creating a compounding geographic moat that competitors building from scratch cannot replicate.

> "Increasingly we're finding, especially, you know, now that we're able to kind of hook the Waymo AI to the AI in the digital world, the VLMs, and kind of inherit the general world knowledge from VLMs. We're seeing really strong results from like zero shot or few shot learning because of that general knowledge that we bring in." [00:25:39]