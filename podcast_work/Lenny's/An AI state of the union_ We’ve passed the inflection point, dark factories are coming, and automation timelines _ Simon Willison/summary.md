# [An AI state of the union: We’ve passed the inflection point, dark factories are coming, and automation timelines | Simon Willison](https://www.lennysnewsletter.com/p/an-ai-state-of-the-union)

**Podcast:** Lenny's
**Date:** 2026-04-02
**Processed:** 2026-04-03T17:06:15Z
**Participants:** Lenny Rachitsky, Simon Willison
**Episode URL:** https://www.lennysnewsletter.com/p/an-ai-state-of-the-union
**Transcript:** [View Transcript](./transcript.md)

---

# Simon Willison on AI: State of the Union Summary

---

## 1. Key Themes

### The November 2024 Inflection Point: Coding Agents Crossed a Reliability Threshold

The most important structural shift in AI wasn't a new capability — it was reliability crossing a threshold. Before November 2024, coding agents were interesting but unreliable. After, they became trustworthy enough to radically change how software is built.

> "We went from that to almost all of the time it does what you told it to do, which makes all of the difference in the world. Now you can spin up a coding agent and say, hey, build me a Mac application that does this thing." [00:04:57]

> "A lot of people woke up in January and February and started realizing, oh wow, this technology, which I'd been kind of paying attention to, suddenly it's got really, really good." [00:05:26]

This shift was driven by both Anthropic and OpenAI dedicating their 2025 training cycles almost entirely to code, combining reinforcement learning with reasoning models — both of which proved particularly effective for programming tasks.

### The Dark Factory: Software Built Without Anyone Reading the Code

The next leap isn't just AI writing code — it's AI-driven development pipelines where humans don't read the code at all, yet maintain professional quality standards through automated testing swarms and simulated environments.

> "What does it look like if you're not reviewing the code? If you're not looking at that code, but you're also not vibe coding, you're not throwing everything to the wind...you're applying professional practices and quality expectations to code that you're not directly reviewing. The reason it's called the dark factory is there's this idea in factory automation that if your factory is so automated that you don't need any people there, you can turn the lights off." [00:13:03]

StrongDM is the leading public example of this, running $10,000/day in simulated agent QA testers, building fake versions of Slack, JIRA, and Okta from API docs alone to test against.

### Experienced Engineers Are Being Amplified, Not Replaced — The Middle Is in Trouble

The AI transition is creating a barbell effect in engineering talent: senior engineers are dramatically amplified, junior engineers onboard faster, but mid-career engineers face the most risk.

> "The problem is the people in the middle. If you're mid-career, if you haven't made it to sort of super senior engineer yet, but you're not sort of new either, that's the group which ThoughtWorks resolved work probably in the most trouble right now." [00:30:16]

> "Using coding agents well is taking every inch of my 25 years of experience as a software engineer... I can fire up four agents in parallel and have them work on four different problems. By 11 AM, I am wiped out." [00:00:50]

---

## 2. Contrarian Perspectives

### The "Prompt Injection Is Solvable" Belief Is Dangerously Wrong

Most people hear "prompt injection" and assume it's like SQL injection — a known, solved problem. It is not. The analogy is broken and the name itself misleads people into false confidence.

> "SQL injection is solved. We know how to fix this problem. There are reliable ways of saying, no, this is untrusted data. Those solutions don't work for prompt injection. So the name itself is misleading." [00:19:37]

> "You can get like 97% effectiveness on those filters. I think that's a failing grade. That means that three out of 100 of these attacks will steal all of your information." [00:22:09]

The only real mitigation is cutting off one of the three legs of the "lethal trifecta" (private data access + malicious instruction surface + exfiltration channel) — not filtering prompts.

### We Are Heading for a Challenger Disaster — Normalizing Unsafe AI Use Will Eventually Catastrophically Fail

Most AI safety discourse focuses on alignment or existential risk. Simon's concern is mundane and structural: we're accumulating institutional confidence in unsafe practices because nothing has gone wrong yet.

> "Lots of people knew that those little O-rings were unreliable, but every single time you get away with launching a space shuttle without the O-rings failing, you institutionally feel more confident in what you're doing. We've been using these systems in increasingly unsafe ways. This is going to catch up with us. My prediction is that we're going to see a Challenger disaster." [00:01:07]

### AI Makes the Most Ambitious People Work Harder, Not Less — The "Productivity = Leisure" Promise Is Backwards

The conventional narrative is that AI will free up time. The reality for the most advanced users is the opposite: ambient access to productive agents creates addictive over-engagement.

> "I can fire up four agents in parallel... by 11 AM I am wiped out. I've talked to a lot of people who are losing sleep because they're like, my agents could be doing work for me. I'm just going to stay up an extra half hour and set off a bunch of extra things." [00:26:44]

> "Such an interesting contradiction. AI is supposed to make us more productive. It feels like the people that are most AI-pilled are working harder than they've ever worked." [00:00:43]

### Tests Matter More Now, Not Less — The "Skip Tests for Speed" Crowd Is Making a Serious Mistake

A popular position is that with AI-generated code moving so fast, manual and automated testing is a relic. Simon argues the opposite: because code is now cheap, tests become the only reliable quality signal.

> "I run into people who are using AI for coding, and they're like, we don't even have to test it anymore. We've stopped doing tests because it's so quick... I think those people are wrong. I think it's a huge mistake." [00:10:27]

Agents are excellent at writing tests — more tests than humans would bother with — and this is now a feature, not overhead, since updating tests is now also the agent's job.

---

## 3. Companies Identified

### StrongDM
A security access management company. Mentioned as the most advanced public practitioner of the "dark factory" pattern — no one writes code, no one reads code, yet they're building production security software. They built simulated versions of Slack, JIRA, and Okta using API docs to run $10,000/day agent QA swarms.

> "Strong DM started doing back in, I think it was August last year. They said, okay, we're not going to read the code... they had a swarm of simulated employees all in a simulated Slack channel saying things like, hey, could somebody give me access to JIRA? 24 hours a day, they're making requests at an enormous cost... spending $10,000 a day on tokens." [00:16:13]

### Anthropic
AI research company. Mentioned for leading the coding-focused training wave, shipping Claude Code in February 2025, and responsibly disclosing 100+ Firefox vulnerabilities — demonstrating credible AI-assisted security research at scale.

> "Anthropic had discovered a hundred like potential vulnerabilities in Firefox and responsibly reported them to Mozilla, who then fixed them." [00:19:54]

### WorkOS
B2B SaaS infrastructure company. Mentioned as the go-to platform for enterprise authentication/compliance features (SSO, SCIM, RBAC, audit logs), used by OpenAI, Anthropic, Cursor, Vercel, Replit, Sierra, Clay.

> "Literally every startup that I'm an investor in that starts to expand upmarket ends up working with WorkOS. And that's because they are the best." [00:07:15] — Lenny Rachitsky

### Cloudflare and Shopify
Both mentioned for their aggressive intern hiring strategies (1,000 interns each in 2025), with AI drastically reducing onboarding time from a month to a week.

> "If you talk to Cloudflare and Shopify, both said they were hiring a thousand interns over the course of 2025 because the intern onboarding costs, it used to be takes a month before you can do anything useful. Now they're doing something useful within like a week because the AI assistant helps them get up and running faster." [00:29:55]

### Vanta
Compliance and risk automation platform. Mentioned for automated SOC 2, ISO 27001, HIPAA compliance, serving 15,000+ companies including Cursor, Ramp, Duolingo, Snowflake, and Atlassian.

> "Vanta automates compliance and risk management with over 35 security and privacy frameworks." [00:48:09] — Lenny Rachitsky

---

## 4. People Identified

### Simon Willison
Co-creator of Django (the web framework powering Instagram, Pinterest, Spotify). Creator of Datasette (used in investigative journalism). Coined "prompt injection" and "lethal trifecta." Now writing a book on agentic engineering, publishing chapter-by-chapter on simonwillison.net. Considered one of the most credible on-the-ground voices on AI-assisted software development because he builds publicly and in real time.

> "What makes Simon rare is that very few engineers have made the leap from the old way of building to the new way as fully and visibly as he has." [00:02:16] — Lenny Rachitsky

### Andrej Karpathy
Former Tesla AI director, OpenAI founding member. Credited with the original, narrower definition of "vibe coding" — hands-off AI-assisted prototyping where you don't look at code.

> "I like Andre Karpathy's original definition of vibe coding, which is when you don't even look at code and you basically just go on the vibes." [00:08:49]

### ThoughtWorks Engineering VPs
The consultancy ThoughtWorks ran an off-site synthesizing the views of engineering VPs across multiple companies, producing the "barbell" insight about AI impact on engineering career levels.

> "ThoughtWorks, the big IT consultancy, did an off-site about a month ago. And they got a whole bunch of engineering VPs in from different companies to talk about this stuff. And one of the interesting theories they came up with is they think this stuff is really good for experienced engineers... The problem is the people in the middle." [00:29:29]

---

## 5. Operating Insights

### Start Every AI Coding Project With a Thin Skeleton Template, Not a Long Claude.md

Instead of writing verbose instruction files for your AI agents, seed your project with a minimal working example — one test, preferred file structure, boilerplate. Agents pattern-match from existing code far more reliably than they follow written instructions.

> "I start with a template that has a single test that just tests that one plus one equals two. And it's laid out in a way that I like, and it's got a few bits of boilerplate... that is part of the reason I'm getting such great results out of agents, is that you can start with just that boilerplate and know that they will stick to that style." [00:15:47]

Simon's templates are public on GitHub for Python libraries, dataset plugins, and CLI tools — directly usable.

### Use "Red/Green TDD" as a Five-Character Prompt to Force Agent Code Verification

Typing "use red/green TDD" is enough to instruct coding agents to write tests before code, watch them fail, then implement and verify they pass — the single most important quality gate when you're not reviewing code yourself.

> "If you use the term red slash green TDD, that's programming jargon... the agents know what that means. So now we've reduced that sort of lengthy paragraph about how to run tests to red slash green TDD, enter, you're done." [00:12:20]

### Build a Public "Hoard" Repository of Solved Problems as Retrievable Agent Context

Maintain a GitHub repository of small working tools and research agent outputs (with actual code run, not just reports). Then feed relevant entries directly to agents when starting new projects — dramatically improving output quality by giving agents verified, opinionated starting points.

> "I'll say things like, check out Simon W slash research from GitHub and look at the ones in there that deal with WebAssembly and Rust, and then use that to feed into solving this new task... it's hard to overstate how good these things are at reusing context." [00:07:33]

---

## 6. Overlooked Insights

### Pre-2022 Human-Written Code Is Becoming a Scarce, Valuable Asset — Like Pre-Nuclear Metal

This was mentioned in passing by Lenny and breezed past — but the implication is significant. Data labeling companies are actively acquiring old GitHub repositories of human-written code at premium prices because it's uncontaminated by AI-generated patterns, which are now in the training loop and creating recursion problems.

> "Data labeling companies are buying old GitHub repos of handwritten code to train their models on. And they're paying a lot of money for like artisanal human written code... They're looking for code pre-2022." [00:39:24] — Lenny Rachitsky

> "The pre-World War Two metal that you can dig up from old shipwrecks, which is before the nuclear, the first nuclear explosions. And so it's not got the radiation baked into the metal. It's that whole thing." [00:39:24] — Simon Willison

The investment implication: any large repository of pre-2022 human-written code (open source or private) may carry increasing asset value. Companies or individuals sitting on this should pay attention.

### The Memory Feature Is the Real AI Moat — But It's Opt-Out and Portable Right Now

Simon dismisses memory features and turns them off — but Anthropic's response to the OpenAI military controversy (a one-click prompt to export ChatGPT memories into Claude) revealed that memory portability is currently trivially easy to break. This is a window: before memory features become deeply embedded and proprietary, the switching cost between models is near zero. That changes when memories become structurally integrated.

> "Anthropic took advantage by saying, hey, why don't you move to Claude? And the way they did that is they had a Claude onboarding page that said, transfer your memories from ChatGPT by clicking this button and then pasting it into ChatGPT. And it was just a prompt." [00:53:31]

This is both a competitive vulnerability for incumbents and an opportunity for any new entrant: whoever builds the most useful persistent memory layer first — and makes it sticky — may define the next phase of AI platform lock-in.