# We Ran the Benchmarks and Migrated to Harmonic

**Podcast:** Data Driven VC
**Date:** 2026-03-19
**Processed:** 2026-03-19T23:08:31Z
**Participants:** Andre Retterath
**Source:** newsletter

---

# Summary: *We Ran the Benchmarks and Migrated to Harmonic* — Data Driven VC (Andre Retterath)

---

## 1. Key Themes

### Theme 1: The Commoditization of Alternative Data in VC Has Forced a Stack Rethink

What was once a genuine edge — scraping LinkedIn, stacking data vendors, building custom pipelines — has become table stakes. The VC data vendor landscape exploded from ~100 solutions in 2017 to 1,000+ by 2025, causing providers to converge in both coverage and accuracy, eliminating the rationale for running parallel stacks.

> *"In 2022, knowing how to scrape LinkedIn for founders in stealth mode made you one of the best-sourced investors in the room. In 2026, it makes you average."*

> *"Historically, each data provider had a distinct angle: stage focus, industry, geography, which meant you had to stack them to get anywhere near full coverage. That stacking logic gradually broke down as providers converged in both coverage and accuracy."*

---

### Theme 2: A Single Next-Gen Provider Can Now Replace an Entire Stacked Infrastructure

Earlybird's 2025 benchmark across 1,000 companies — spanning stealth founders through growth-stage — showed a decisive gap between legacy providers and Harmonic, enough to justify eliminating most of their custom scraping infrastructure and vendor subscriptions.

> *"Traditional providers landed around 75% coverage against our gold dataset. Harmonic achieved 98%. That was a number we had not seen before. For the first time, a single provider came close to matching the combined output of our entire stacked operation."*

> *"We made a deliberate choice: migrate to Harmonic as our primary public data backbone and ramp down the majority of remaining vendors and internal scraping infra."*

---

### Theme 3: The Architecture of Data — People-First vs. Company-First — Is a Structural Differentiator

The way a database is organized reflects a deeper philosophy about how early-stage investing actually works. Legacy providers are built around companies; next-gen tools like Harmonic are built around people — which aligns with how investors actually make decisions at the pre-seed and seed stages.

> *"Traditional providers treat companies as the primary entity. Harmonic is built people-first: founder tracking, talent movement signals, team composition, network mapping."*

> *"This is not a cosmetic difference, but reflects how early-stage investors actually think. You back people before you back companies."*

---

### Theme 4: Proprietary, Irreplaceable Internal Data — Not Public Data Access — Is Where VC Alpha Now Lives

With public data becoming commoditized, the real moat is institutional memory: IC decisions, investment memos, CRM notes, portfolio company data. The strategic move is to *buy* commoditized public data and *invest* engineering resources in activating private, firm-specific knowledge.

> *"That is where our edge lives. Not in having access to a startup database, but in the private, irreplaceable company- and decision-centric information that three decades of disciplined investing produce."*

> *"If something does not generate alpha and is available to buy, buy it."*

---

### Theme 5: AI-Synthesized Investment Workflows Are Now Operationally Viable

Earlybird built a system using Claude with custom skills that combines public data (Harmonic), private institutional records, IC history, and interaction notes into a single investment proposal workflow — a capability that didn't exist even two years ago.

> *"I can generate an investment proposal for a new company that pulls in everything: people, traction and company data from Harmonic, private context from our own records, prior IC decisions on comparable companies, and notes from every interaction our team has had. The depth is something you could not have imagined even two years ago."*

---

## 2. Contrarian Perspectives

### Perspective 1: More Data Vendors = Less Alpha (Complexity Is the Enemy, Not the Solution)

The intuitive assumption is that stacking more data sources produces better coverage and therefore better deal flow. Earlybird's experience shows the opposite: after a certain threshold, additional vendors create redundancy and operational drag without improving signal quality. The answer is *consolidation*, not accumulation.

> *"In 2024, we reached the peak of complexity and decided to start simplifying, gradually cutting the vendor list in half."*
> *"As redundancy evolved, it got easier to trim."*

Supporting evidence: Harmonic at 98% coverage effectively replicated what an entire multi-vendor stack was producing — validating the consolidation thesis empirically, not just philosophically.

---

### Perspective 2: Scraping Infrastructure Is No Longer a Competitive Moat for VCs

Building proprietary web-scraping infrastructure has been a calling card of "data-driven" VC for years. The article argues this is now a value-destroying activity — expensive to maintain and no longer differentiated.

> *"Do we still generate alpha with our large-scale scraping infra and public data layering?"*

The answer implied by the benchmark: no. The decision to *ramp down* internal scraping infra in favor of a vendor — previously unthinkable for a data-driven fund — signals a meaningful market shift.

---

### Perspective 3: "Taste" and Institutional Decision History Are More Valuable Than Any Data Feed

Against the prevailing belief that better external data = better investment decisions, Retterath argues the real differentiator is codified firm judgment — specifically, documented reasons for *rejecting* companies, which powers reinforcement learning on what deals actually fit a fund's thesis.

> *"500+ documented IC outcomes. 100k+ companies in our platform EagleEye that got reviewed by our investment team. That's 100k+ documented decisions with reasons for excitement or rejection. That data drives the reinforcement learning, codifying the 'taste of Earlybird' and prioritizing not only high 'probability of success' opportunities, but the subset of those which are most likely to go through our IC."*

---

## 3. Companies Identified

**Harmonic**
- *Description:* Next-generation startup discovery and data platform; markets itself as "The Startup Discovery Engine"
- *Why mentioned:* Achieved 98% coverage in Earlybird's 2025 benchmark vs. ~75% for legacy providers; selected as Earlybird's primary public data backbone after full migration
- *Quote:* *"Harmonic achieved 98%. That was a number we had not seen before."*

**Scout (by Harmonic)**
- *Description:* AI agent for investors built on Harmonic's data; described as "the AI for investors" that understands private markets
- *Why mentioned:* Positioned as an accessible alternative for firms without Earlybird's institutional depth; can map markets, find founders, generate diligence reports, and draft outreach in a single conversation
- *Quote:* *"It can find companies, screen against a thesis, generate diligence reports and market maps, and run deep research in a single conversation."*

**Crunchbase**
- *Description:* Widely used startup/funding database
- *Why mentioned:* Cited as Earlybird's original baseline data provider, now described as insufficient on its own for serious early-stage sourcing
- *Quote:* *"For data, Crunchbase was our baseline, with dozens of additional sources like Pitchbook, CBInsights, or Preqin layered on top."*

**PitchBook**
- *Description:* Financial data and research platform covering private markets
- *Why mentioned:* Named as one of the legacy providers that consistently underperformed at the stealth/pre-seed end of the coverage spectrum
- *Quote:* *"Where PitchBook, CBInsights, Crunchbase, and others consistently fell short was at the stealth, pre-seed, and pre-announcement end."*

**CBInsights**
- *Description:* Market intelligence and startup analytics platform
- *Why mentioned:* Grouped with PitchBook and Crunchbase as legacy providers that showed ~75% coverage in benchmarking
- *Quote:* *"Traditional providers landed around 75% coverage against our gold dataset."*

**Preqin**
- *Description:* Alternative assets data provider
- *Why mentioned:* Cited as one of the legacy providers layered into Earlybird's previous data stack
- *Quote:* *"Crunchbase was our baseline, with dozens of additional sources like Pitchbook, CBInsights, or Preqin layered on top."*

**EagleEye (Earlybird internal platform)**
- *Description:* Earlybird's internal investment platform
- *Why mentioned:* Cited as the repository for 100k+ reviewed companies and documented IC decisions, forming the backbone of their proprietary data advantage
- *Quote:* *"100k+ companies in our platform EagleEye that got reviewed by our investment team."*

**Anthropic / Claude**
- *Description:* AI model used to power Earlybird's internal investment synthesis workflows
- *Why mentioned:* Named as the AI layer connecting Earlybird's private data, Harmonic data, and IC history into investment proposals
- *Quote:* *"We have built significant internal systems using Claude with a library of custom skills assembled over months."*

**n8n**
- *Description:* Workflow automation platform
- *Why mentioned:* Referenced as a tool being used by top-tier VC firms (Accel, Bessemer, etc.) for generating alpha, mentioned in the context of the Virtual DDVC Summit
- *Quote:* *"Learn how Accel, Atomico, Bessemer, BlackRock, NEA, NFX, LocalGlobe, Point Nine, and more use tools like OpenClaw, Claude, n8n or Harmonic to generate alpha."*

**OpenClaw**
- *Description:* Referenced as a tool alongside Claude and n8n in AI-powered VC workflows
- *Why mentioned:* Listed among tools being adopted by top-tier firms to generate alpha in sourcing and diligence
- *Quote:* *"Learn how Accel, Atomico, Bessemer, BlackRock, NEA, NFX, LocalGlobe, Point Nine, and more use tools like OpenClaw, Claude, n8n or Harmonic to generate alpha."*

---

## 4. People Identified

**Andre Retterath**
- *Description:* Partner at Earlybird Venture Capital; author of the *Data Driven VC* newsletter
- *Why mentioned:* Author of the article; has led Earlybird's data infrastructure strategy since 2017 and published multiple benchmarking studies on VC data providers
- *Quote:* *"In today's episode, I share what our external data stack actually looked like, what our 2025 benchmark revealed, why we migrated to Harmonic as our primary data backbone, and where we believe the real edge in data is moving."*

---

## 5. Operating Insights

### Insight 1: Apply a "Buy vs. Build" Filter to Every Element of Your Data Stack

The clearest tactical framework in the article: if a capability doesn't generate differentiated alpha and can be purchased off the shelf, stop building it internally. Reserve engineering resources for proprietary, non-replicable systems.

> *"If something does not generate alpha and is available to buy, buy it."*

**Application:** Audit your current data and tooling stack. Any vendor or internal build that is directionally replicated by a consolidating platform (like Harmonic) is a candidate for elimination. Redeploy that engineering capacity toward activating proprietary internal data.

---

### Insight 2: Document IC Rejections as Rigorously as Wins — They Are Training Data for Firm "Taste"

Most firms track portfolio companies and deal memos. Few systematically document *why* they passed. Earlybird treats rejection data as the core input for reinforcement learning — surfacing not just high-probability opportunities, but ones most likely to clear the firm's specific investment committee.

> *"100k+ documented decisions with reasons for excitement or rejection. That data drives the reinforcement learning, codifying the 'taste of Earlybird' and prioritizing not only high 'probability of success' opportunities, but the subset of those which are most likely to go through our IC."*

**Application:** Start logging structured pass reasons in your CRM today. Even a small firm with 500 documented IC outcomes has a meaningful proprietary dataset within a few years.

---

### Insight 3: Coverage at the Pre-Seed and Stealth Stage Is the Highest-Leverage Differentiator in Data

Not all coverage gaps are equal. Legacy providers cover well-known, announced companies well. The gap that matters competitively is at the earliest, least-visible end of the funnel — where early-stage investors can actually gain access before valuation compression.

> *"The gap between Harmonic and traditional providers is most pronounced at the early end of the spectrum... Where PitchBook, CBInsights, Crunchbase, and others consistently fell short was at the stealth, pre-seed, and pre-announcement end, exactly where early-stage investors can make a huge difference."*

---

## 6. Overlooked Insights

### Insight 1: Funding Data Coverage Is Now Reliable Enough to Replace Cross-Provider Verification

A common workflow for data-driven investors is to cross-reference funding data across multiple providers due to inconsistencies and gaps. Retterath notes — almost in passing — that Harmonic's funding data was strong enough to eliminate this redundant step, which has non-trivial workflow and cost implications.

> *"Funding data was also stronger than we expected. This is an area where many investors typically cross-reference across providers, and Harmonic's coverage was thorough enough to rely on."*

---

### Insight 2: The "People Graph" Architecture of New Platforms Enables Talent Signal-Based Sourcing at Scale

Retterath flags Harmonic's people-first data architecture as enabling "talent movement signals" and "network mapping" — use cases that go beyond company discovery into monitoring where top operators and repeat founders are moving *before* they announce a new venture.

> *"Harmonic is built people-first: founder tracking, talent movement signals, team composition, network mapping."*

This is briefly mentioned but represents a distinct sourcing methodology — tracking talent flows as a leading indicator of new company formation — that is underexplored in the article's main narrative.