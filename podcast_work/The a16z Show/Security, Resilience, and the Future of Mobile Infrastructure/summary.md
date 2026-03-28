# [Security, Resilience, and the Future of Mobile Infrastructure](https://a16z.simplecast.com/episodes/security-resilience-and-the-future-of-mobile-infrastructure-FE05DDD_)

**Podcast:** The a16z Show
**Date:** 2026-03-26
**Processed:** 2026-03-28T17:05:22Z
**Participants:** David Ulevitch, John Doyle, Justin Fanelli, Unidentified Interjection, a16z (announcer/narrator)
**Episode URL:** https://a16z.simplecast.com/episodes/security-resilience-and-the-future-of-mobile-infrastructure-FE05DDD_
**Transcript:** [View Transcript](./transcript.md)

---

# Security, Resilience, and the Future of Mobile Infrastructure
### a16z Podcast Summary

---

## 1. Key Themes

### The U.S. Telecom Infrastructure Is Fundamentally Compromised — And Almost Nobody Knows It

Salt Typhoon represents one of the most significant national security breaches in U.S. history, yet awareness is shockingly low even among professionals. China has essentially full access to lawful intercept systems across every major American carrier — meaning they can listen to calls, track metadata, and monitor internet activity for any American, including senior government officials. The story has since expanded globally.

> "What we learned was that China has infiltrated major telecommunications carriers in the U.S. for all intents and purposes, fully. So you can listen to the phone calls, the lawful intercept plug-in points. They have control of those, and they can just turn on at any time and listen to this." — John Doyle [00:33:21]

> "I was at Davos last year in a cyber forum and one of the speakers was talking about Salt Typhoon... a room of 60, it was closed door, room of 60 cyber folks. And she's like, wait, how many people know about this? It was five out of 60." — Justin Fanelli [00:32:26]

---

### The "Clean Install" Doctrine: Assume Infrastructure Is Hostile, Build Securely On Top

Rather than attempting to root out adversarial penetration from compromised physical infrastructure — a nearly impossible task — Cape's approach is to deploy a secure software layer on top of known-compromised physical networks. This is a profound strategic reframe that has applicability far beyond telecom.

> "Rather than trying to ferret through the existing carriers on Guam and find all the China and try to get rid of it... the basic idea was let's just do a clean install of a telco on top of the existing physical infrastructure. Just assume it's hostile." — John Doyle [00:35:34]

> "This was literally three months before the Salt Typhoon news broke, and we learned that China had compromised the X1 interface of all these major telcos." — John Doyle [00:37:49]

---

### The Defense Procurement Transformation: From Requirements-Based Buying to Outcome-Driven Adoption

The Navy has fundamentally shifted its acquisition model from slow, requirements-driven procurement (3+ years) toward rapid pilots with clearly defined success metrics, structured challenges, and a "wildcatting" approach that dramatically increases the number of bets placed. This is creating a new, faster flywheel between startups and the government.

> "Defense acquisition system historically hinges on a requirements axis. And that's a slow axis. That's three years to write them... This was ahead of need. And so this is a case where we're looking at things that we think could be game changers, but not following the full formal process and small dollar amounts. And then like ultimately little bets that could turn into big bets if they carry." — Justin Fanelli [00:17:16]

> "You did two pilots last year. How many do you think you could do? Well, if we really pushed it, we could do five. Great. We're going to do 25 this year." — Justin Fanelli [00:18:38]

---

## 2. Contrarian Perspectives

### The Navy Was the Hardest to Sell To — Now It May Be the Best Government Partner

Conventional wisdom in defense tech explicitly told founders to go to the Navy last. That advice may now be dangerously outdated, and founders following it are leaving the best opportunity on the table.

> "The conventional wisdom was if you're going to do a defense tech startup... go to the Navy last because they were the hardest to do business with. The Air Force was fastest... go to the Navy last because they're the slowest to adopt. And that was just conventional wisdom that got repeated over and over and over again." — John Doyle [00:13:16]

The implication: the Navy's transformation is precisely a contrarian opportunity, because most founders are still acting on stale intelligence.

---

### Unclassified, Shareable Third-Party Security Evaluations Are an Underused Fundraising and Sales Weapon

Most startups treat government security evaluations as classified, single-use assets. Cape turned a DIU-funded, independent penetration test into a multi-purpose tool: government sales across agencies, investor due diligence, and credibility building — all from one unclassified report.

> "We had an independent pen tester, a really credible third party come and do a deep dive on the tech... They wrote a 50-page report that DIU paid for... but also they made it unclassified and shareable. And now we can use that across services, we can use that with other customers within the U.S. government. We got permission to share it with investors as we went out to raise more money." — John Doyle [00:22:57]

---

### The Biggest Opportunity in Defense Software Is Destruction, Not Creation

Founders look to build new systems. The Navy's CTO is explicitly saying the biggest value-add is replacing and eliminating existing ones. The "divest to invest" mandate is real — and building a product that kills five legacy systems is more valuable than building a new one.

> "If you can take out five systems with one application, this is modern service delivery... For almost every domain where we're doing software, there are too many systems. And so if you can do secure data delivery with an intuitive user interface, we will find room for you as long as you're taking things out and sending it to Operation Cattle Drive, sending it to the Boneyard afterwards." — Justin Fanelli [00:28:43]

---

### The MVNO Structure Is a Moat, Not a Weakness

Conventional wisdom treats not owning physical towers as a liability for a telecom company. Cape inverts this: being a mobile virtual network operator (MVNO) creates resilience through redundancy, and the software layer becomes the actual product moat.

> "We become... a network of networks. So we stitched together physical infrastructure wherever we find it. And the result is that you're not reliant on any one physical infrastructure provider... in the last six months, two of the three major U.S. telcos have had significant outages. Those aren't as scary for a Cape subscriber as they are for someone else because there's another network you can fail over to." — John Doyle [00:08:41]

---

### Most Defense Tech Founders Are Solving the Wrong Problem

Justin Fanelli's advice contradicts the typical founder instinct of pattern-matching to publicized problems. The most actionable opportunities are in granular, unsexy pain points discovered on the ground — not the high-profile challenges everyone is already chasing.

> "Don't do that from on high or over there. Be where the problems are and rank them by here is the size of the pain... We don't want to solve three headaches. We want to solve a migraine and then something imminent... The problem that you read about is probably being covered by other people." — Justin Fanelli [00:30:12]

---

## 3. Companies Identified

**Cape**
Global commercial cellular network operating as a secure MVNO, live in 190 countries.
Mentioned as the primary case study for building secure, private, and resilient telecom infrastructure on top of compromised physical networks — directly addressing Salt Typhoon-class threats. Active partner with the U.S. Navy (Guam pilot) and Japanese Self-Defense Forces (Rakuten partnership).
> "CAPE is a global cellular network, commercial cell network... It's live in 190 countries. We're more private, more secure, and more resilient than any other commercial carrier on Earth." — John Doyle [00:06:37]
> "We did a joint U.S. and Japanese self-defense force military exercise on Rakuten's physical infrastructure with Cape's software in Japan. It was really successful." — John Doyle [00:08:11]

---

**Syronic** *(referenced as Sironic)*
Maker of unmanned surface vessels.
Mentioned by David Ulevitch as an a16z portfolio company that represents the kind of private sector innovation the Navy is actively seeking in the maritime domain.
> "I know we're investors in a company called Sironic that makes unmanned surface vessels. I think obviously the subsea domain is interesting." — David Ulevitch [00:25:17]

---

**DIU (Defense Innovation Unit)**
U.S. government body accelerating commercial technology adoption by the military.
Mentioned as a critical funding and validation partner that paid for Cape's unclassified third-party pen test on Guam, enabling a shareable tech evaluation that became a multi-use sales and fundraising asset.
> "We worked with Justin and his office to identify funding from DIU, the Defense Innovation Unit, to help us go faster." — John Doyle [00:14:41]

---

**Palantir**
Enterprise data analytics and defense technology company.
Mentioned as the training ground where John Doyle learned about telecom vulnerabilities and developed the national security expertise that led to founding Cape.
> "My signature contribution to the company was running the national security business from 2017 until I left in 2022... it's also where I had the opportunity to learn about a whole host of vulnerabilities that exist in the commercial cellular network." — John Doyle [00:06:08]

---

**Rakuten (Japan)**
Japanese e-commerce and telecom conglomerate with its own cellular network infrastructure.
Mentioned as Cape's international partner for expanding the secure-network-on-compromised-infrastructure model globally, specifically for allied military use cases.
> "We just announced last week a partnership with Rakuten in Japan. We did a joint U.S. and Japanese self-defense force military exercise on Rakuten's physical infrastructure with Cape's software in Japan." — John Doyle [00:08:11]

---

## 4. People Identified

**John Doyle**
Founder and CEO of Cape. Former Green Beret, Harvard Law graduate, and 9-year Palantir veteran who ran its national security business.
Identified for building a category-defining secure telecom company that anticipated Salt Typhoon years before it became public, and for pioneering a new model of defense-commercial partnership.
> "In 2022, with the help of the American Dynamism team... I left Palantir to start Cape." — John Doyle [00:06:37]
> "Part of the pitch was this idea that China can leverage telecommunications network to basically see everything about you and us, and most importantly, the armed forces and the national security professional in the U.S." — John Doyle [00:34:09]

---

**Justin Fanelli**
CTO of the U.S. Navy. Engineer by training (Air Force, electrical engineering), with tours at DARPA, Space Development Agency, ARPA-H, and Defense Health.
Identified as the rare government official who operates with the mentality of a venture investor — running structured pilots, defining crisp success metrics, wildcatting investments, and building a "network of networks" of innovation champions across the military.
> "There were four VCs making investments in the space. There's 168 now by my last count, 42X in seven years... We went from a group of just straight builders trying to build everything to gardeners." — Justin Fanelli [00:11:24]

---

**Steve McGee**
Marine Corps Lieutenant Colonel, initiator of the Marine Corps innovation challenge.
Briefly highlighted as a key internal champion and amplifier who funnels commercial innovation into the military — an exemplar of the "warrior engineer" archetype.
> "We have a handful of the Marine Corps lieutenant colonel who started the innovation challenge, Steve McGee. He made things happen. And he is, again, an amplifier who is funneling things in." — Justin Fanelli [00:38:42]

---

## 5. Operating Insights

### Define "World-Class Alignment Metrics" Before Any Pilot Begins

Cape initially found it annoying to iterate extensively on success metrics before the Guam pilot. In retrospect, it was the single most important move — it created shared language, accelerated the program, and made the outcome legible enough to spread across the entire government.

> "Insist from the beginning on defining success metrics... Let's be rigorous and specific at the outside. What does winning look like?... We iterated with your team several times on the whams. But we got them really crisp and we got really strong alignment between the Navy and between Cape on what success looked like. And then we went and executed this pilot and it was ahead of schedule and under budget and we hit all the whams." — John Doyle [00:15:10]

---

### Bad News Travels Six Times Faster Than Good News in Government Sales — Engineer for Good News

In government markets, failure is near-permanent and spreads instantly. The implication: underpromise aggressively, define success narrowly and achievably, and use every win as a deployable reference asset.

> "The one thing that's been true forever is if you fail, that gets around fast... bad news travels six times faster than good news. Right. And so you just need more good news or a way to carry." — Justin Fanelli and John Doyle [00:22:26]

---

### Attack One Indispensable Module, Not a Whole System

When trying to displace a legacy government system, the blocker is always the one module out of ten that is truly indispensable. Make your solution fully severable and go after that single hard piece — not the whole problem.

> "What often happens is if there's 10 modules, nine of them don't matter, but one is indispensable. And these are severable tasks. And so whenever I say turn something off, find a way to make it fully severable... go after that, not a whole problem, but a chunk of a problem and pull the plug on the hardest piece." — Justin Fanelli [00:31:09]

---

## 6. Overlooked Insights

### The CALEA Vendor Ecosystem Is a Systemic, Unpatched National Security Hole

This was mentioned almost in passing, but it is enormously significant. The lawful intercept compliance vendor industry — a small group of "cottage industry" providers that virtually every U.S. telecom relies on to handle FBI wiretap requests — had plaintext credential files with usernames and passwords for every client sitting unencrypted in an installer package. Cape discovered this accidentally. This means Salt Typhoon may not have required sophisticated hacking at all: a basic installer review could have handed China the keys to every major U.S. carrier's intercept system.

> "Our SRE team was evaluating the connection and looking at it. And they discovered in the installer that the vendor sent us when they unpacked it, there was an unencrypted text file that had the usernames and passwords for every single client of that vendor... And this was literally three months before the Salt Typhoon news broke, and we learned that China had compromised the X1 interface of all these major telcos. I don't have specific knowledge. That doesn't seem like it was that hard for them to do." — John Doyle [00:36:54]

The investment and policy implication: the CALEA compliance vendor space is broken and ripe for a security-first rebuild. Any startup that can offer a secure, modern lawful intercept compliance solution would immediately have a captive, legally-mandated market across every U.S. telecom.

---

### The Navy's "Innovation Adoption Kit" Is a Replicable Commercial Go-To-Market Template

Justin briefly mentioned an "Innovation Adoption Kit" that has spread organically across the military — including into special operations communities that are now self-directing its use. This is essentially the Navy having productized its startup adoption process into a scalable, self-propagating playbook. For defense tech startups, understanding and aligning to this kit's framework is likely the highest-leverage GTM action available.

> "We have an innovation adoption kit. We wanted to make sure these tools scaled. And a cool story recently is I was with the special ops community and they said, yep, we're doing an exercise. And through the innovation adoption kit, we found these pilots and we're going to send them into horizon one. I was like, who told you to say that?" — Justin Fanelli [00:20:42]

The non-obvious point: this kit is already in the Defense Authorization Act via "Structured Challenges." Startups that format their pitches and pilots around this framework are not just selling — they are plugging into a mandated, funded, and already-scaling government adoption mechanism.