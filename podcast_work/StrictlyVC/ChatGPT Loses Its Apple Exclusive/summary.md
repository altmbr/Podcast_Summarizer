# ChatGPT Loses Its Apple Exclusive

**Podcast:** StrictlyVC
**Date:** 2026-03-27
**Processed:** 2026-03-27T06:11:47Z
**Participants:** Connie Loizos
**Source:** newsletter

---

# StrictlyVC Summary — March 26, 2026

---

## 1. Key Themes

### Apple Ends AI Exclusivity, Opening a Multi-Model Future on iOS
Apple's decision to let users route Siri queries to competing AI assistants signals a platform shift from single-vendor AI integration to a marketplace model. This creates distribution opportunities for every major AI lab — and a new subscription revenue stream for Apple itself.

> "Apple plans to end ChatGPT's exclusive role inside Siri in iOS 27 by letting users route queries to rival AI assistants like Gemini and Claude, opening the iPhone to more chatbot competition and more subscription revenue for Apple."

---

### Defense Tech Is the Hottest Capital Concentration in Venture
The single largest deal in this issue is Shield AI's $2B raise at a $12.7B valuation, and PDW Holdings raised $110M for modular military drones. The breadth of institutional backers — Advent International, Blackstone, JPMorgan, Booz Allen Hamilton, Hanwha — signals that defense tech has moved from niche to mainstream institutional asset class.

> "Shield AI...raised a $2 billion round at a post-money valuation of approximately $12.7 billion... The deal was led by Advent International, with JPMorgan Chase's Security and Resiliency Initiative, Blackstone, and Snowpoint Ventures also participating."

> "PDW Holdings...manufactures modular military drones and mission software for defense, government, and law enforcement customers, raised a $110 million Series B."

---

### Open Source AI Infrastructure Has a Critical Security Vulnerability
The LiteLLM malware incident — credential-harvesting code injected via a dependency, in a package downloaded 3.4 million times per day — exposes how fragile the open-source AI tooling layer is. SOC2 and ISO 27001 certifications clearly did not catch this, raising questions about the value of compliance theater in AI infrastructure.

> "LiteLLM gives developers easy access to hundreds of AI models... downloaded as often as 3.4 million times per day... The malware slipped in through a 'dependency'... It then stole the log-in credentials of everything it touched."

> "LiteLLM, as of March 25 when we looked, still proudly displays on its website that it has passed two major security compliance certifications, SOC2 and ISO 27001. But it used a startup called Delve for those certifications."

---

### Crypto Is Crossing Into Mainstream Consumer Finance
Fannie Mae's reported acceptance of crypto-backed mortgages is a structural inflection point — not a speculative signal. When the government-sponsored enterprise underwriting the U.S. housing market integrates bitcoin into its underwriting process, digital assets gain a new form of institutional legitimacy.

> "Fannie Mae is reportedly set to accept crypto-backed mortgages, a first that would let some homebuyers use holdings like bitcoin as part of the underwriting process and push digital assets deeper into mainstream consumer finance."

---

### AI-Native Health and Pharma is Attracting Serious Capital Across the Stack
Multiple deals this issue span AI in healthcare operations (Adonis, Thesis Care), employer GLP-1 programs (eMed), oral peptide therapeutics (Pinnacle Medicines), and psychiatric drug development (Gilgamesh Pharma). The common thread: AI is being applied not just to diagnostics but to the full drug design, care delivery, and revenue cycle stack.

> "eMed...provides GLP-1 weight-loss programs for employers, raised a $200 million Series A round at a $2+ billion valuation."

> "Pinnacle Medicines...uses AI and physics-based simulations to design and optimize oral peptide therapeutics, raised an $89 million Series B."

> "Thesis Care...uses AI agents and clinicians to handle clinical operations and care management workflows, raised a $45 million Series A."

---

## 2. Contrarian Perspectives

### Security Certifications May Be Meaningless for AI Infrastructure Companies
The standard playbook for enterprise software credibility — get SOC2 and ISO 27001 certified — appears to have provided false assurance in the LiteLLM case. The malware was caught not by compliance processes, but by a researcher whose machine crashed due to a bug in the malicious code itself.

> "Ironically, a bug in the malware caused his machine to blow up. Because that bit of nasty code was so sloppily designed, he (as well as famed AI researcher Andrej Karpathy) concluded it must have been vibe coded."

> "LiteLLM...still proudly displays on its website that it has passed two major security compliance certifications, SOC2 and ISO 27001. But it used a startup called Delve for those certifications."

The implication: buyers of AI infrastructure tools should be deeply skeptical of compliance badges as a proxy for actual security posture, particularly when those certifications are issued by early-stage startups.

---

### Anduril May Be a Narrative Trade, Not a Proven Operator
Despite its defense-tech-SpaceX branding and elite investor backing, Wired's reporting suggests Anduril is struggling with the hard operational realities of manufacturing at scale — the exact thing that would differentiate it from legacy defense contractors.

> "Anduril Industries is racing to prove it can mass-produce missiles, drones, and submarines like a defense-tech SpaceX, but Wired reports that safety lapses, factory delays, management churn, and missed deadlines are getting in the way."

For investors, this is a caution: the defense tech premium is being priced on the narrative of disruption, not yet on demonstrated manufacturing execution.

---

### OpenAI's Advertising Business May Be More Material Than Its AI Revenue — Already
OpenAI's ads pilot crossing $100M in annualized revenue in under two months is a signal that the company is diversifying away from pure subscription/API revenue faster than most observers anticipated. This quietly changes the competitive calculus — OpenAI is becoming a media and advertising business, not just an AI model company.

> "OpenAI's ads pilot has already crossed $100 million in annualized revenue less than two months after launch."

---

## 3. Companies Identified

| Company | Description | Why Mentioned | Quote |
|---|---|---|---|
| **LiteLLM** | YC-backed open source AI model routing tool | Victim of supply-chain malware attack; security compliance scrutinized | *"downloaded as often as 3.4 million times per day"* |
| **Delve** | Startup providing SOC2/ISO 27001 certifications | Under scrutiny after certifying LiteLLM, which was subsequently compromised | *"LiteLLM...still proudly displays...SOC2 and ISO 27001. But it used a startup called Delve for those certifications."* |
| **Shield AI** | San Diego autonomous software and drone company for military use | Raised $2B at $12.7B valuation; acquiring Aechelon | *"raised a $2 billion round at a post-money valuation of approximately $12.7 billion"* |
| **Anthropic** | AI safety company behind Claude | Won injunction against Pentagon's "supply chain risk" designation; discussing Q4 IPO at $60B+ | *"Anthropic won a preliminary injunction blocking the Pentagon's designation of Claude as a 'supply chain risk'"* |
| **eMed** | Miami employer GLP-1 platform | $200M Series A at $2B+ valuation; high-profile investor syndicate including Tom Brady and Linda Yaccarino | *"raised a $200 million Series A round at a $2+ billion valuation"* |
| **Isara** | SF multi-agent AI coordination startup | $94M raise backed by OpenAI, Stanley Druckenmiller, and Michael Ovitz | *"uses AI to coordinate large groups of agents to communicate and solve complex problems"* |
| **Thrive Holdings** | Thrive Capital offshoot focused on AI in traditional services | Raising $2B+ fund | *"has locked down $1 billion in commitments for its next fund and is in talks to raise at least $1 billion more"* |
| **Xona** | Burlingame GPS-alternative satellite navigation startup | $170M Series C; infrastructure independence from GPS is a growing national security theme | *"building a satellite navigation network as an alternative or backup to GPS"* |
| **Pinnacle Medicines** | PA-based AI/physics drug design startup | $89M Series B for oral peptide therapeutics; only 2 years old | *"uses AI and physics-based simulations to design and optimize oral peptide therapeutics"* |
| **Anduril Industries** | Defense tech manufacturer | Featured in Essential Reads for operational struggles despite its high-profile positioning | *"safety lapses, factory delays, management churn, and missed deadlines are getting in the way"* |
| **Meta** | Social media giant | Back-to-back jury losses in NM and LA threatening Section 230 shield via addictive design theory | *"treating social media's addictive design – not just user-posted content – as the legal problem"* |
| **SpaceX** | Rocket and satellite company | Considering giving retail investors up to 30% of IPO allocation | *"a sharp break from Wall Street convention that would let Elon Musk lean harder on his fan base"* |

---

## 4. People Identified

| Person | Description | Why Mentioned | Quote |
|---|---|---|---|
| **Callum McMahon** | Research scientist at FutureSearch | Discovered, documented, and disclosed the LiteLLM malware | *"The malware caused McMahon's machine to shut down after he downloaded LiteLLM. That event prompted him to investigate and discover it."* |
| **Andrej Karpathy** | Famed AI researcher | Independently concluded the LiteLLM malware was "vibe coded" due to its sloppy construction | *"famed AI researcher Andrej Karpathy...concluded it must have been vibe coded"* |
| **David Sacks** | Venture capitalist | Stepping down as White House AI and crypto czar after 130-day limit; staying involved via advisory council | *"stepping down from his role as the White House AI and crypto czar after hitting the 130-day limit for special government employees"* |
| **Tom Brady** | Athlete and investor; Chief Wellness Officer | Investor in eMed's $200M Series A | Listed as investor alongside Linda Yaccarino and Joe Lonsdale in eMed round |
| **Linda Yaccarino** | CEO of X | Investor in eMed's $200M Series A | Mentioned as part of eMed's high-profile investor syndicate |
| **Stanley Druckenmiller** | Legendary macro investor | Backed Isara's $94M round alongside OpenAI | Listed as investor in Isara alongside Michael Ovitz and OpenAI |

---

## 5. Operating Insights

### Open Source Dependencies Are a Hidden Enterprise Risk — Audit Them Now
The LiteLLM incident illustrates that even well-credentialed, heavily-used open source tools can be compromised through third-party dependencies, not the core package itself. For operators building on open source AI tooling, the attack surface extends to every library your tools rely upon.

> "The malware slipped in through a 'dependency,' meaning other open source software that LiteLLM relied upon. It then stole the log-in credentials of everything it touched."

**Tactical takeaway:** Conduct a dependency audit of all AI infrastructure tools in your stack. Do not treat SOC2 or ISO 27001 badges — especially from early-stage certifiers — as sufficient due diligence.

---

### Section 230 Is Eroding — Addictive Design Is the New Legal Vector
For operators of consumer platforms (social, gaming, media), the legal threat is no longer just about user-generated content. Courts are now entertaining the theory that platform design itself — recommendation algorithms, engagement mechanics — constitutes actionable harm, bypassing Section 230 protections entirely.

> "Back-to-back jury losses against Meta in New Mexico and Los Angeles are giving plaintiffs a new path around Section 230 by treating social media's addictive design – not just user-posted content – as the legal problem, potentially opening the door to years of copycat litigation."

**Tactical takeaway:** Consumer platform companies should audit their product design decisions for liability exposure now, before litigation arrives. This is no longer a hypothetical risk.

---

### Advertising Is a Faster Path to AI Revenue Scale Than Subscriptions
OpenAI's $100M annualized ads run rate in under two months — while still operating a subscription business — suggests that ad-supported AI may generate revenue faster and at greater scale than pure SaaS models. Operators building AI products should evaluate whether an ad-supported tier could accelerate monetization.

> "OpenAI's ads pilot has already crossed $100 million in annualized revenue less than two months after launch."

---

## 6. Overlooked Insights

### Vertical SaaS in Fragmented, Unglamorous Industries Can Still Command Large Rounds
Cents, a business management platform for **laundromats and dry cleaners**, raised a $110M Series C. This is a reminder that deeply vertical, unsexy operational software targeting fragmented SMB categories can scale meaningfully — and attract institutional capital — if it becomes the de facto system of record for an underserved industry.

> "Cents, a seven-year-old New York startup that runs a business management platform for laundromats and dry cleaners, raised a $110 million Series C round led by Sumeru Equity Partners."

---

### GPS Redundancy Is Becoming an Investable Infrastructure Theme
Xona's $170M Series C for an alternative satellite navigation network flew under the radar in this issue, but the strategic logic is significant: GPS dependency is a national security vulnerability, and the investor syndicate (Craft Ventures, ICONIQ, Samsung Next, Woven Capital) suggests this is being treated as serious infrastructure, not a moonshot.

> "Xona...is building a satellite navigation network as an alternative or backup to GPS, raised a $170 million Series C round led by Mohari Ventures Natural Capital."