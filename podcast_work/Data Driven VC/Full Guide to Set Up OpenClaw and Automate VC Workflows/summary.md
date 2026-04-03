# Full Guide to Set Up OpenClaw and Automate VC Workflows

**Podcast:** Data Driven VC
**Date:** 2026-04-03
**Processed:** 2026-04-03T12:43:29Z
**Participants:** Andre Retterath
**Source:** newsletter

---

# Data Driven VC: Full Guide to Set Up OpenClaw and Automate VC Workflows
**Author:** Andre Retterath | **Source:** Danny Chepenko's session at Virtual DDVC Summit 2026

---

## 1. Key Themes

### The Shift from Vendor-Controlled AI to Practitioner-Controlled Agentic Architecture
The most important structural change in AI tooling isn't a new model — it's who controls the harness. The first wave locked users into vendor-defined execution environments. The second wave hands control back to the operator.

> "The first wave of AI products wrapped powerful models inside a proprietary UI with built-in tools… The harness was fixed by the vendor. The second wave changed the underlying contract. Apps and tools like Claude Code and then OpenClaw shifted the model to one where you bring your own tools, define your own memory, and control your own execution environment. The harness became yours."

### Proactive AI Agents Are a Categorically Different Product Class
The defining feature of this new architectural pattern isn't intelligence — it's agency without prompting. The "heartbeat" mechanism separates OpenClaw-style agents from every other AI product on the market.

> "Every other major AI tool today, whether Claude Code, Codex, or any standard chatbot, requires your input to execute a task. OpenClaw does not. It runs a 'heartbeat' mechanism: a cron-triggered loop that fires every few minutes (configurable), reads your memory files and execution logs, builds a plan, and can message you without being asked."

### Skills as Reusable Institutional Process Capital
Skills aren't prompts. They are discrete, agent-selectable capabilities that compound over time into a proprietary operating system. This reframes individual productivity tooling into something closer to durable intellectual infrastructure.

> "Danny's recommendation is to treat skills as the most atomic unit of your actual job. He chunks his own workflows into the smallest meaningful pieces, then writes a skill for each. Over time, the library grows into a reusable operating system for how he works."

### Security Is the Underappreciated Bottleneck to Agentic Adoption
The article frames security not as a future concern but as an active, present-tense risk — with real incident precedents. Model quality is framed as a direct security input, not just a performance variable.

> "There are three primary attack vectors for an OpenClaw-style setup. Prompt injection through connected email or messaging… Malware embedded in ClawHub skills downloaded without inspection. Exposed environment variables that a compromised session can exfiltrate."

### Early Builders Are Accumulating a Compounding Structural Advantage
The article frames this moment as a time-sensitive window, not a permanent opportunity. Proprietary context and skill libraries are positioned as moats that no external tool can replicate.

> "The practitioners who are building these workflows now, at the skill level, at the memory architecture level, are accumulating a compounding advantage. Each skill you write is a reusable unit of institutional process knowledge. Each vault you build is proprietary context that no external tool can replicate."

---

## 2. Contrarian Perspectives

### The "Best" AI Product Is Already Being Commoditized — Bet on Patterns, Not Tools
The consensus in VC and tech circles is to find and back the leading AI product. Danny's view is the opposite: the specific product that pioneered a capability is less important than the architectural pattern it introduced, which will be absorbed by all competitors.

> "Danny's read is that OpenClaw's original innovations — the heartbeat, the persistent session gateway, the messenger integration — are now being adopted across the industry. The product itself peaked in early February 2026. The concept it introduced is only getting started… He is not betting on a single tool. He is betting on the architectural pattern."

### Fewer Dependencies Is a Security Feature, Not an Engineering Shortcut
Conventional wisdom in software development favors mature, feature-rich frameworks. The article argues the opposite: a minimal dependency surface is a deliberate security advantage, and the "less capable" tool is sometimes the more defensible choice.

> "The smaller the dependency surface, the lower the supply chain attack risk. He points to a recent incident with another AI tooling company where malware was embedded in a third-party dependency, not in the core product. With NanoClaw, you generate the implementation code alongside Claude as part of setup, so you can read what is actually running in your environment."

### Slow VC Adoption of Agentic Tools Is Rational, Not Laggard
The narrative around AI adoption in professional services typically frames slow uptake as conservatism or competitive risk. The article reframes measured adoption as the correct risk-calibrated response to a genuinely novel threat surface.

> "The honest answer from Danny, and from the broader audience discussion, is that most VCs are still in the very early stages of trusting agents with real data… That is not a criticism. That is a reasonable approach to a genuinely novel risk surface. The correct posture is controlled expansion, not wholesale adoption."

---

## 3. Companies Identified

**OpenClaw**
- *Description:* Open-source, proactive AI agent that runs inside messaging platforms (WhatsApp, Telegram, Discord)
- *Why mentioned:* Central subject of the article; primary tool for automating VC workflows via a heartbeat mechanism and persistent hybrid memory
- *Quote:* "OpenClaw is an open-source, proactive AI agent that lives in your messenger… It runs a 'heartbeat' mechanism: a cron-triggered loop that fires every few minutes (configurable), reads your memory files and execution logs, builds a plan, and can message you without being asked."

**NanoClaw**
- *Description:* Community-maintained lightweight fork of OpenClaw (~15 source files vs. ~4,000 lines)
- *Why mentioned:* Danny's actual day-to-day tool of choice due to its minimal attack surface and auditability
- *Quote:* "He uses NanoClaw, a community-maintained lightweight fork of about fifteen source files versus OpenClaw's four thousand lines. His reason is control."

**Claude Code (Anthropic)**
- *Description:* Agentic coding and research tool from Anthropic with a new "Dispatch Mode"
- *Why mentioned:* Used by Danny for heavy research and development tasks; contrasted with OpenClaw on session persistence; also moving toward heartbeat-style proactive architecture
- *Quote:* "He uses Claude Code for heavy research and development tasks where a $200/month subscription delivers more than enough compute… Claude Code's new 'Dispatch Mode' lets you leave an agent running locally and interact with it from your phone."

**Perplexity**
- *Description:* AI search and orchestration company
- *Why mentioned:* Cited as a competitor now replicating OpenClaw's architectural pattern via a cloud-hosted orchestrator requiring no self-hosting
- *Quote:* "Perplexity recently released a cloud-hosted orchestrator that requires no self-hosting."

**Granola**
- *Description:* AI meeting note-taker with MCP (Model Context Protocol) integration
- *Why mentioned:* Tool integrated into Danny's personal CRM workflow to pull meeting context proactively
- *Quote:* "His NanoClaw instance connects to Granola (his AI note-taker via MCP), his calendar, and a personal vault of previous conversation notes."

**Harmonic**
- *Description:* Startup discovery and data engine for investors
- *Why mentioned:* Newsletter sponsor; described as the backbone of Earlybird's data stack
- *Quote:* "Discover why our team at Earlybird migrated to Harmonic as the backbone of our data stack."

**ClawHub**
- *Description:* Community registry for OpenClaw skills
- *Why mentioned:* Flagged as a potential security risk — skills should not be imported without thorough inspection or rewriting
- *Quote:* "He also cautions strongly against importing skills from the ClawHub registry without reading them. The community security mechanisms have improved, but he still recommends having Claude Code rewrite any external skill before putting it in your environment."

**Codex (OpenAI)**
- *Description:* OpenAI's agentic coding tool
- *Why mentioned:* Cited as another incumbent moving toward proactive, heartbeat-style agent architecture
- *Quote:* "Codex is moving in the same direction."

---

## 4. People Identified

**Danny Chepenko**
- *Description:* VC practitioner and agentic workflow builder; presenter at Virtual DDVC Summit 2026
- *Why mentioned:* Delivered the live demo of OpenClaw/NanoClaw workflows; primary source of all tactical insights in the article
- *Quote:* "Danny walked us through something most people only talk about… A live, working agentic VC workflow built on top of OpenClaw, running on his laptop, sending him meeting briefs in real time via Telegram. It was one of the clearest on-the-ground views we have had into how the agentic stack is actually being used in the venture world today."

**Andre Retterath**
- *Description:* Author of Data Driven VC newsletter; partner at Earlybird Venture Capital
- *Why mentioned:* Newsletter author and event organizer; reference point for Harmonic adoption at Earlybird
- *Quote:* "Hi, I'm Andre and welcome to my newsletter Data Driven VC which is all about becoming a better investor with data and AI."

---

## 5. Operating Insights

### Enforce Strict Permission Boundaries Between Agent and Data Systems
The default instinct is to give agents maximum access to maximize utility. Danny's operating principle is the opposite: start with zero write permissions and separate agents by function. This enables trust-building without catastrophic failure modes.

> "He gives the agent zero write permissions to any system. Read-only, local data dump, proactive output… He also separates agents by function. His personal CRM instance only touches Granola and his calendar. His research instance only touches a local file vault. There is no single agent with access to everything."

### Build a Skill Library as the Smallest Atomic Unit of Your Workflow
Rather than writing monolithic prompts or automations, decompose your job into its smallest meaningful tasks and write a discrete skill for each. The library becomes an auditable, reusable operating system that compounds in value.

> "A skill is a markdown file with a YAML header containing a name and description. That header gets stored in the system prompt of every agent… Danny's recommendation is to treat skills as the most atomic unit of your actual job. He chunks his own workflows into the smallest meaningful pieces, then writes a skill for each."

### Use Hybrid Memory Architecture to Eliminate the Cold-Start Problem in Research
Storing structured content (e.g., newsletters as markdown) in a searchable local vault — queried via combined semantic and keyword search — allows an agent to provide relevant, personalized first drafts rather than generic outputs.

> "He stores every newsletter he reads as a markdown file in a local vault. When writing a new article, he runs a skill that does a hybrid search across that vault, identifies thematic angles, checks his previous content for his existing positions and writing style, and produces a first-draft structure. He describes it as solving the cold start problem."

---

## 6. Overlooked Insights

### Model Quality Is a Direct Security Investment, Not Just a Performance Choice
This point is embedded in the security section but deserves independent emphasis: paying for a more capable frontier model is not purely about output quality — it is a direct mitigation against prompt injection attacks. Cheaper models are materially more vulnerable.

> "Use the smartest model you can afford because frontier models are more resistant to injection than cheaper alternatives."

### The VC Adoption Curve for Agents Is a Predictable, Stagebound Progression
The article briefly sketches an adoption sequence that could serve as a practical roadmap for any organization deploying agents: creative tasks → writing tasks → personal assistant tasks with read-only personal data → CRM/deal flow access. This staged trust model is mentioned in passing but represents a replicable framework for responsible enterprise AI deployment.

> "The adoption curve goes: creative tasks, then writing tasks, then personal assistant tasks with read-only access to personal data, then gradually, as trust is earned, access to richer data sources like CRM or deal flow pipelines."