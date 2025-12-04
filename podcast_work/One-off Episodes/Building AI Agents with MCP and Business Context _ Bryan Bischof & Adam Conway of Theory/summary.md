# [Building AI Agents with MCP and Business Context | Bryan Bischof & Adam Conway of Theory](https://www.youtube.com/watch?v=6GLpCW-394M)

**Podcast:** One-off Episodes
**Date:** 2025-11-14
**Participants:** Adam Conway, Bryan Bischof
**Region:** Western
**Video ID:** 6GLpCW-394M
**Video URL:** https://www.youtube.com/watch?v=6GLpCW-394M
**Transcript:** [View Transcript](./transcript.md)

---

# Podcast Summary: Theory Ventures Engineering Team on Building AI-Augmented Investment Systems

## 1. Key Themes

### Venture Firms as Hedge Funds: Intelligence-Driven Operations
Theory Ventures operates more like a hedge fund than a traditional VC, treating investment as an intelligence problem requiring massive data processing. Bryan Bischof explains: "Similar to a hedge fund will forage for data where we can find it...we're trying to get signals anywhere you can. And the more that you gather the signals, understand the signals and really process them, the more alpha you have on the market." [[00:07:47]](https://www.youtube.com/watch?v=6GLpCW-394M&t=7m37s) This drives their need for sophisticated AI infrastructure to process what Bischof describes as "an order of magnitude larger in unstructured data than almost any job I've ever seen, even having worked in the database for 12 years." [[00:03:14]](https://www.youtube.com/watch?v=6GLpCW-394M&t=3m4s)

### Thesis-Driven Investment vs. Deal-Driven
Theory flips the traditional VC model by doing deep research before finding companies. Adam Conway explains: "Theory goes and says we're going to go and we're going to research the best that we can about technology, the market and generally like what trends are going on from that we're going to form some hypotheses." [[00:10:13]](https://www.youtube.com/watch?v=6GLpCW-394M&t=10m3s) This approach means their diligence and deal flow phases are more integrated than typical VCs, requiring different tooling that supports continuous research rather than episodic evaluation.

### The LMUX Paradigm: Death of Traditional SaaS UX
Rather than building custom UIs, Theory standardized on "Language Model UX" (LMUX) - any interface where users work with language models. Bischof articulates the philosophy: "My deep dislikes in software is that UX is are bad they just like are generally like hard to use they're very hard to learn they're always incredibly inefficient too many clicks." [[00:37:38]](https://www.youtube.com/watch?v=6GLpCW-394M&t=37m28s) The team discovered everyone was already using LM interfaces (Claude Code, Cursor, ChatGPT) and copying data between systems, so they made the strategic decision to "not care what your client is...we don't care if you're using cursor...we don't care if you're using the chat GPT app." [[00:36:31]](https://www.youtube.com/watch?v=6GLpCW-394M&t=36m21s)

## 2. Contrarian Perspectives

### Dashboards and Charts Are Context, Not Compression
Against the trend of assuming LLMs eliminate visualization needs, Bischof argues charts add context rather than compress data: "Charts are really about narrative...they're not about like showing the data they're really about like telling a story from that data and what story well it's the story that like someone needs to hear." [[00:57:20]](https://www.youtube.com/watch?v=6GLpCW-394M&t=57m10s) He provides a compelling example about quarterly sales pacing, showing how a chart adds temporal context that raw contract data lacks. The provocative claim: agents need visual representations as much as humans do because "until you give it the context of where you are in the quarter what the expectations were what the normal quarter looks like...all that context is missing from the LLM." [[00:58:04]](https://www.youtube.com/watch?v=6GLpCW-394M&t=57m54s)

### MCP Distribution Matters More Than Protocol Completeness
While acknowledging MCP's limitations (no transaction support, inconsistent feature support across clients), Theory bet on it primarily for distribution. Conway states: "Five or ten point spread on like tool use accuracy especially before optimization wasn't going to make up for the like incredible difference in flexibility in ergonomics." [[01:07:00]](https://www.youtube.com/watch?v=6GLpCW-394M&t=1h6m50s) This contrasts with the common engineering approach of choosing the technically superior solution - they explicitly chose the worse technical option because it had better distribution to end users.

### PhD Data Scientists Not Dead, Just Different
When asked if PhD data scientists are obsolete, Bischof (himself a data scientist) responds "I'm not dead yet." [[00:31:32]](https://www.youtube.com/watch?v=6GLpCW-394M&t=31m22s) His work at Theory demonstrates the role evolving toward system design and modeling rather than manual analysis. The new competitive advantage is designing data models and business logic that agents can effectively use - deeper work than running analyses.

### First-Party AI Agents Are a Mistake
Bischof's strongest take: "Every company is building their AI agent built into their product and they are putting less effort on their sort of like MCP...if I could go and yell at every growth stage SaaS company it would be please take 10 to 20% of your like AI efforts and dedicate them to this instead of yet another shitty agent." [[01:28:08]](https://www.youtube.com/watch?v=6GLpCW-394M&t=1h27m58s) He argues companies should prioritize making their products consumable by other agents rather than building isolated in-product agents.

## 3. Companies Identified

### **Fireflies**
**Description:** Meeting transcription and recording service
**Quote:** "We happened to use fireflies. There's some specific integration reasons why we chose fireflies." - Bryan Bischof [[00:16:52]](https://www.youtube.com/watch?v=6GLpCW-394M&t=16m42s)
**Context:** Theory uses this as their recording infrastructure for capturing internal investment discussions.

### **Lance (LanceDB)**
**Description:** Multimodal vector database
**Quote:** "I could also build a semantic search on top of it, which we did with Lance neat." - Bryan Bischof [[00:17:41]](https://www.youtube.com/watch?v=6GLpCW-394M&t=17m31s)
**Context:** Theory uses Lance for semantic search over their transcripts and unstructured data.

### **Brouse/Browser Base**
**Description:** Browser automation product built primarily for AI agents
**Quote:** "Isn't Brouse/Browser Base effectively...they're only building a product that is really built for agents to use." - Bryan Bischof [[01:30:35]](https://www.youtube.com/watch?v=6GLpCW-394M&t=1h30m25s)
**Context:** Discussed as potentially the first MCP-native style company (pre-dating the protocol), building exclusively for agent consumption.

### **Prefect**
**Description:** Workflow orchestration company
**Quote:** Used as an example: "If you come into our system and you want to create a new company and you tell your LM client...hey add prefect." - Bryan Bischof [[01:13:35]](https://www.youtube.com/watch?v=6GLpCW-394M&t=1h13m25s)
**Context:** Example of how their system handles named entity recognition and company creation.

## 4. Operating Insights

### Ambient Data Capture > Manual Entry
Theory automatically transcribes all internal investment meetings, pulling out companies, relationships, and theses. Conway explains: "We have, I want to say like three or four weekly meetings with the whole team in a room where we're talking about all of the companies...and we are like debating all of the same points from different angles and then taking notes." [[00:06:38]](https://www.youtube.com/watch?v=6GLpCW-394M&t=6m28s) This creates a continuously-updating knowledge graph without requiring manual documentation, dramatically reducing cognitive overhead.

### The "Exoskeleton" Product Philosophy
Rather than replacing investor judgment, Theory builds tools that amplify capability. Bischof: "I think of the investors as like miners on a foreign planet. And I want to build an exoskeleton for them to go to that planet and just feel safe, but also be able to mine much more efficiently." [[00:04:22]](https://www.youtube.com/watch?v=6GLpCW-394M&t=4m12s) This frames AI tooling as multiplicative rather than substitutive - the goal is "10 or 100x the capability that they normally could." [[00:04:17]](https://www.youtube.com/watch?v=6GLpCW-394M&t=4m7s)

### Embedded Engineering Teams See Different Problems
Having engineers in investment meetings reveals opportunities invisible to external observers. Conway: "The engineering team has opinions on the engineering aspects of a company or a thesis. We've got a salesperson who has an opinion on the sales aspect...and the investors who have their own opinions." [[00:06:51]](https://www.youtube.com/watch?v=6GLpCW-394M&t=6m41s) This tight feedback loop means they can "impose some structure and get immediate feedback from our end users...oh, this sucks to use or this is fine." [[00:22:58]](https://www.youtube.com/watch?v=6GLpCW-394M&t=22m48s)

### Prioritize Top-of-Funnel Automation
Conway identifies where AI has biggest impact: "The top of the funnel in a funnel sentence is like that's where AI and software has the biggest potential to make everyone more efficient because that's where it's just like there's so much volume." [[00:14:55]](https://www.youtube.com/watch?v=6GLpCW-394M&t=14m45s) The team offsets efficiency gains by expanding the funnel: "We've made the funnel more efficient, we're able to put more stuff...the reward for hard work is more hard work." [[00:15:17]](https://www.youtube.com/watch?v=6GLpCW-394M&t=15m7s)

## 5. Overlooked Insights

### The Revertibility/Transaction Problem Will Gate MCP Adoption
Buried in discussion of MCP limitations, Conway identifies a fundamental blocker: "There are two types of tools in an MCP server you have a read tool...and you have a write tool...the obvious next question is like what happens if that's wrong what happens if you're using an agent that's using this right tool and it realizes later that it did the wrong thing." [[01:19:33]](https://www.youtube.com/watch?v=6GLpCW-394M&t=1h19m23s) Bischof elaborates with inheritance of revertibility: "No thing can be revertible if something below it can't be revertible." [[01:22:03]](https://www.youtube.com/watch?v=6GLpCW-394M&t=1h21m53s) This isn't just a nice-to-have feature - it's the difference between MCP being suitable for read-only systems versus production systems that modify state. The lack of transaction semantics in MCP is likely the biggest technical barrier to "MCP-only companies" emerging.

### Data Models Are the New Competitive Moat
While everyone focuses on model quality and prompt engineering, Conway suggests the real differentiation will be data modeling: "I think a lot of MCPs would just become data models like what is the purpose of this MCP to define a data model." [[01:24:28]](https://www.youtube.com/watch?v=6GLpCW-394M&t=1h24m18s) This echoes the Jeff Bezos AWS mandate but for AI: "Jeff Bezos mandated...that every service in AWS needed to be usable via REST APIs...I think I have the same take on your product being used by AI systems and like exposing your data model and your context via MCPs." [[01:26:14]](https://www.youtube.com/watch?v=6GLpCW-394M&t=1h26m4s) Companies that design superior data models for agent consumption - not just human consumption - will have durable advantages as interfaces become commoditized.