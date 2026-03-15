# [Dylan Patel — Deep dive on the 3 big bottlenecks to scaling AI compute](https://www.dwarkesh.com/p/dylan-patel)

**Podcast:** Dwarkesh
**Date:** 2026-03-13
**Participants:** Dwarkesh Patel, Dylan Patel, Producer
**Episode URL:** https://www.dwarkesh.com/p/dylan-patel
**YouTube:** [Watch on YouTube](https://youtube.com/watch?v=mDG_Hx3BSUE)
**Transcript:** [View Transcript](./transcript.md)

---

# Dylan Patel — Deep Dive on the 3 Big Bottlenecks to Scaling AI Compute

---

## 1. Key Themes

### The Semiconductor Supply Chain Is the True Long-Term Bottleneck to AI Scaling

While power and data centers have been the visible bottlenecks, Dylan argues the real ceiling is the semiconductor manufacturing supply chain itself — specifically EUV lithography machines made exclusively by ASML. The bottleneck cascades from ASML's constrained production through logic wafers at TSMC to HBM memory.

> "There's sort of no more capacity for the mobile and PC industries, which used to be the majority of the semiconductor industry, to shift over to AI. NVIDIA is now the largest customer at TSMC. And NVIDIA is the largest customer at SK Hynix, the largest memory manufacturer. So it's sort of impossible for this scaling or the sliding of resources away from the common person — PCs and smartphones — to shift any more towards the AI chips." [00:36:15](https://youtube.com/watch?v=mDG_Hx3BSUE&t=2175)

> "By 28, 29, the bottleneck falls to the lowest rung on the supply chain, which is ASML... Even under very aggressive supply chain expansion, they only get to a little bit over 100 [EUV machines] by the end of the decade." [00:37:03](https://youtube.com/watch?v=mDG_Hx3BSUE&t=2223)

---

### GPUs Are Appreciating Assets, Not Depreciating Ones

Contrary to the bear case (Michael Burry-style) that GPUs should have 2-3 year depreciation cycles, Dylan argues GPU value is actually *increasing* over time because better models run on the same hardware, generating more economic value per chip year over year.

> "An H100 is worth more today than it was three years ago. That's crazy." [00:15:44](https://youtube.com/watch?v=mDG_Hx3BSUE&t=944)

> "Because you are so limited on semiconductors and deployment timelines and all these things, you end up with actually what prices these chips is not, 'what's the comparative thing I can buy today?' It's actually what is the value I can derive out of this chip today." [00:14:26](https://youtube.com/watch?v=mDG_Hx3BSUE&t=866)

> "GPT 5.4 is both way cheaper to run than GPT-4... it can serve more tokens per GPU of 5.4 than if you had ran GPT-4 on it. So it's producing more tokens of a model that is of higher quality." [00:14:45](https://youtube.com/watch?v=mDG_Hx3BSUE&t=885)

---

### The Memory Crunch Will Visibly Destroy Consumer Electronics Markets

AI's insatiable appetite for HBM memory is actively cannibalizing DRAM supply for consumer devices. This is not an abstract financial risk — Dylan projects smartphone volumes collapsing and iPhone prices rising dramatically, with low-end and mid-range segments being hit hardest.

> "Xiaomi and Oppo are cutting low end and mid-range smartphone volumes by half... if smartphone volumes, let's say half, the halving will frankly happen in the low and mid-range, not in the high end." [00:25:36](https://youtube.com/watch?v=mDG_Hx3BSUE&t=1536)

> "It's probably $150 increase on the iPhone. Apple has to either pass that on to the consumer or eat it... that means the end consumer is paying $250 more for an iPhone." [00:24:37](https://youtube.com/watch?v=mDG_Hx3BSUE&t=1477)

> "A third of their capex is going to memory." [00:23:34](https://youtube.com/watch?v=mDG_Hx3BSUE&t=1414)

---

## 2. Contrarian Perspectives

### Anthropic's "Responsible" Compute Strategy Was Actually a Mistake

Dario has publicly positioned Anthropic as the conservative, responsible actor in AI compute. Dylan argues this conservatism has left Anthropic compute-starved at precisely the moment their revenue is exploding, forcing them to pay premium spot prices and work with lower-quality providers they never would have chosen.

> "Dario, when he was on your podcast, was very, very conservative. He's like, 'I'm not going to go crazy on compute because if my revenue inflects at a different rate, I don't want to go bankrupt.' But in reality, he's definitely missed the pooch in terms of going like OpenAI, which was 'let's just sign these crazy fucking deals.'" [00:04:20](https://youtube.com/watch?v=mDG_Hx3BSUE&t=260)

> "The reliability of cloud code is actually quite low because they're so compute constrained." [00:13:21](https://youtube.com/watch?v=mDG_Hx3BSUE&t=801)

---

### ASML Is Irrationally Generous — and It's a Systemic Risk

ASML has a complete monopoly on EUV machines, which every advanced chip in the world depends on, yet it has *never* raised prices faster than it has raised capability. Dylan (and Leopold, referenced) believes ASML is leaving enormous margin on the table that could be used to fund faster capacity expansion, which would accelerate the entire AI buildout.

> "ASML is, you know, maybe one of the most generous companies in the world... they haven't taken price and margins up like crazy. ASML has never risen the price more than they've increased the capability of the tool." [00:45:31](https://youtube.com/watch?v=mDG_Hx3BSUE&t=2731)

> "You can ask, you know, Leopold and they're like, 'let's have the price go up, right? Because they can. The margin is there. You can take the margin. Like, NVIDIA takes the margin. Memory players are taking the margin. But ASML has never done this.'" [00:45:31](https://youtube.com/watch?v=mDG_Hx3BSUE&t=2731)

---

### The Entire Semiconductor Supply Chain Is Structurally "Under-AGI-Pilled"

Every layer of the supply chain is systematically building less than what AI labs actually need, because they don't believe AGI-level demand is coming. This creates a compounding shortfall as you go deeper into the supply chain.

> "OpenAI and Anthropic, they know they need X. NVIDIA is not quite as AGI-pilled and they're building X minus 1. And you go down the supply chain, everyone's doing minus 1. And in some cases, they're doing like divided by 2, because they just don't, they're not AGI-pilled." [00:53:36](https://youtube.com/watch?v=mDG_Hx3BSUE&t=3216)

> "Constantly, we're told our numbers are way too high. And then when they're right, they're like, 'oh yeah, but your next year's numbers are still too high.'" [00:47:02](https://youtube.com/watch?v=mDG_Hx3BSUE&t=2822)

---

### Fast AI Timelines Favor the West; Long Timelines Favor China

This is a clean, non-obvious framing: if AGI arrives fast (say by 2030), the West wins because compounding compute investments and revenue create an insurmountable gap. If AI timelines are slow (2035+), China wins because it will have indigenized its semiconductor supply chain and can scale past the West's fragmented multinational supply chain.

> "Fast timelines, U.S. wins. Long timelines, China wins." [00:15:48](https://youtube.com/watch?v=mDG_Hx3BSUE&t=948)

> "Were they in 2030? Yeah. By 2030, it's possible that they do [have a fully indigenized supply chain]. But if takeoff or timelines are slow enough, then certainly China, I don't see why they wouldn't be able to catch up drastically." [01:07:27](https://youtube.com/watch?v=mDG_Hx3BSUE&t=4047)

---

## 3. Companies Identified

**ASML**
Description: Dutch company that makes EUV lithography machines, the single most critical tool in advanced semiconductor manufacturing. No competitor exists.
Why mentioned: Identified as the ultimate production ceiling for all AI compute through 2030 — 3.5 of their machines enable one gigawatt of AI data center capacity, yet they produce only ~70/year. Also highlighted as paradoxically under-monetizing their monopoly position.
> "The bottleneck falls to the lowest rung on the supply chain, which is ASML... Even under very aggressive supply chain expansion, they only get to a little bit over 100 by the end of the decade." [00:37:03](https://youtube.com/watch?v=mDG_Hx3BSUE&t=2223)

---

**CoreWeave**
Description: GPU cloud provider (NeoCloud) with a large fleet of NVIDIA chips, recently IPO'd.
Why mentioned: Cited as the prototypical NeoCloud with over 90% of contracts locked in long-term (3+ year), meaning it cannot flex pricing upward even as market rates have exploded. Also highlighted as having signed long-term deals with OpenAI at prices that, in hindsight, look cheap.
> "If you look at CoreWeave, their average term duration is like over three years right now for like 90% plus of their compute. So they end up with this conundrum of, well, they can't actually flex price." [00:22:46](https://youtube.com/watch?v=mDG_Hx3BSUE&t=1366)

---

**SK Hynix**
Description: South Korean memory semiconductor manufacturer, the leading producer of HBM (High Bandwidth Memory).
Why mentioned: NVIDIA's largest memory supplier and the central node in the HBM crunch. Identified as one of the few supply chain players actually capturing margin from the AI boom.
> "NVIDIA is the largest customer at SK Hynix, the largest memory manufacturer." [00:36:44](https://youtube.com/watch?v=mDG_Hx3BSUE&t=2204)

---

**Carl Zeiss (Zeiss)**
Description: German optics company that produces the precision mirror/lens systems inside ASML's EUV machines.
Why mentioned: Identified as a critical single point of failure in the EUV supply chain. Their artisanal, low-volume production of optical components is one of the hardest constraints to scale.
> "Each of these tools has, I think, 18 of these lenses effectively... Any defect in this perfect layer... will mess it up. There are a lot of challenges with scaling the production. It's quite artisanal." [00:48:55](https://youtube.com/watch?v=mDG_Hx3BSUE&t=2935)

---

**Cymer (ASML-owned)**
Description: San Diego-based subsidiary of ASML that makes the EUV light source — the component that generates 13.5nm light by laser-blasting tin droplets.
Why mentioned: Named as one of four critical sub-components of an EUV tool, each with its own constrained supply chain that cannot be easily expanded.
> "It has the source, right, which is made by Cymer in San Diego... It drops these tin droplets. It hits it three subsequent times with a laser perfectly... and the tin droplets get excited enough that they release EUV light, 13.5 nanometer." [00:47:33](https://youtube.com/watch?v=mDG_Hx3BSUE&t=2853)

---

**Nebius**
Description: AI cloud infrastructure company (NeoCloud).
Why mentioned: Cited as an example of a NeoCloud experiencing data center construction delays, limiting Blackwell GPU deployment timelines.
> "There are some data center delays — not just those two, but like Nebius and all the other folks, Microsoft, Amazon, Google." [00:08:53](https://youtube.com/watch?v=mDG_Hx3BSUE&t=533)

---

## 4. People Identified

**Dylan Patel**
Description: CEO of SemiAnalysis, the premier semiconductor industry research and analytics firm that tracks data center construction, fab capacity, wafer orders, and supply chain down to individual component suppliers globally.
Why mentioned: Primary expert guest. Provides extraordinarily granular, data-driven analysis of the AI compute supply chain that is unavailable elsewhere publicly.
> "We're tracking every data center. We're tracking every fab. We're tracking all the tools and we're tracking where they're going." [01:11:06](https://youtube.com/watch?v=mDG_Hx3BSUE&t=4266)

---

**Leopold (last name not given)**
Description: Referenced as a knowledgeable figure in the AI/semiconductor ecosystem who has thought deeply about ASML's pricing power.
Why mentioned: Cited as someone who independently believes ASML should raise prices to capture more margin and reinvest in expanding capacity.
> "You go ask, you know, Leopold, and they're like, 'Let's have the price go up, right? Because they can. The margin is there. You can take the margin.'" [00:45:31](https://youtube.com/watch?v=mDG_Hx3BSUE&t=2731)

---

## 5. Operating Insights

### Lock In Long-Term Compute Contracts Early — the Margin Advantage Is Structural

For any company building on AI infrastructure, the single most impactful financial decision is signing long-term compute contracts before demand becomes obvious to the rest of the market. Companies that signed 5-year deals 2-3 years ago are now running at structurally lower cost bases than anyone entering the market today. This is not a temporary advantage — it compounds as new capacity is priced to current (much higher) market rates.

> "The person who committed early has better margins in general. And the percentage of the market that is in long-term contracts is much larger than the percentage of the market in short-term contracts that can be this sort of flex capacity that you add at the last second." [00:22:20](https://youtube.com/watch?v=mDG_Hx3BSUE&t=1340)

> "I've seen deals where certain AI labs have signed at as high as $2.40 for two to three years for H100s, which if you think about the margin — $1.40 for Hopper when you release it across five years. And now two years in, you're signing deals that are $2.40. Those margins are way higher." [00:07:38](https://youtube.com/watch?v=mDG_Hx3BSUE&t=458)

---

### Model Quality Is Becoming More Economically Valuable As Compute Costs Rise — Pursue the Best, Not the Cheapest

Dylan and Dwarkesh's discussion of the Alchian-Allen effect reveals a non-obvious pricing dynamic: as GPU costs rise across the board, the *relative* price difference between the best model and a merely good model shrinks. This pushes rational buyers to pay for the premium model. For operators building AI products, this means competitive differentiation via model quality becomes *more* economically defensible as compute costs rise, not less.

> "The hopper went from two to three dollars. And if a hopper can make a million tokens of Opus and two million tokens of Sonnet, the price differential between Opus and Sonnet has decreased because the price of the GPU has increased by a dollar... all of the volumes are on the best models today, all the revenues on the best models today." [00:21:01](https://youtube.com/watch?v=mDG_Hx3BSUE&t=1261)

---

### Revenue Velocity Justifies Aggressive Compute Commitment — Anthropic Is the Cautionary Tale

For founders and executives deciding how aggressively to pre-commit to infrastructure capacity: Anthropic's experience shows that being conservative about infrastructure when your product is working means you will be *forced* to buy at spot prices, work with lower-quality providers, and share revenue with cloud partners rather than capturing margin directly. The cost of undercommitting when demand materializes is higher than the cost of over-committing when it doesn't.

> "In a sense, Anthropic is constrained... There are not that many incremental buyers of compute yet because Anthropic hit the capabilities here first where their revenue is mooting." [00:09:56](https://youtube.com/watch?v=mDG_Hx3BSUE&t=596)

---

## 6. Overlooked Insights

### Google Sold Anthropic TPU Capacity Before Its Own AI Division Realized It Needed It — and This Is a Repeatable Pattern

Dylan briefly mentions that Anthropic's compute team (staffed by ex-Google employees) negotiated a large TPU capacity purchase from Google Cloud *before Google's own DeepMind/Gemini team understood they needed it*. This caused Google to make emergency requests to TSMC to explain a sudden capacity spike. This is not just a historical anecdote — it reveals a structural vulnerability in any large organization where the cloud/infrastructure revenue team and the internal AI product team have misaligned incentives and information flows.

> "Anthropic was not willing — it kind of had a little bit of commitment issues before their ARR exploded, even though they have far more information asymmetry and see what's coming down the pipe. Google is going to be more conservative than Anthropic, A. And B, Google had even less ARR... The main people on the compute team at Anthropic, they saw this dislocation. They negotiated a deal. And they were able to get access to this compute before Google realized." [00:31:52](https://youtube.com/watch?v=mDG_Hx3BSUE&t=1912)

> "Google even had to go to TSMC and explain to them why they needed this increase in capacity because it was so sudden." [00:32:21](https://youtube.com/watch?v=mDG_Hx3BSUE&t=1941)

The implication: information asymmetry between AI labs and hyperscaler cloud divisions is a *repeatable arbitrage opportunity*. Labs with AGI-pilled compute teams who understand the trajectory of model capabilities will systematically be able to acquire infrastructure capacity from hyperscalers whose cloud revenue teams are optimizing for near-term utilization rates rather than long-term demand curves.

---

### The $50 Billion Data Center Is Held Up by $1.2 Billion Worth of EUV Tools — This Ratio Is an Extraordinary Investment Signal

Dylan makes this point almost in passing, but the ratio is staggering: it takes approximately 3.5 EUV machines (costing ~$1.2 billion total) to enable a full gigawatt of AI data center capacity (costing ~$50 billion). Every dollar of constraint at ASML represents roughly 40x that in constrained downstream economic value.

> "A gigawatt worth of data center capacity of NVIDIA's latest chip... 3.5 EUV tools satisfies a gigawatt. So 3.5 EUV tools at $1.2 [billion]. It's actually quite a lower number — $50 billion worth of AI capex in the data center... It might be $100 billion worth of AI value into the supply chain is held up by this $1.2 billion worth of tooling that simply just cannot expand its supply chain quickly." [00:40:44](https://youtube.com/watch?v=mDG_Hx3BSUE&t=2444)

This means ASML is the single highest-leverage point in the entire AI supply chain, and any company or technology that could expand EUV-equivalent throughput — whether ASML itself raising prices and reinvesting, High-NA EUV, improved overlay enabling multi-patterning efficiency, or even a Chinese competitor reaching mass production — would unlock disproportionate value. ASML's deliberate underpricing relative to its monopoly power is, paradoxically, the most important systemic risk to AI compute scaling timelines.