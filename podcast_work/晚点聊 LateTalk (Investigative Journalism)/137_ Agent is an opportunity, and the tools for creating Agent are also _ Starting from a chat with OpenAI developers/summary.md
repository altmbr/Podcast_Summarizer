# 137: Agent is an opportunity, and the tools for creating Agent are also | Starting from a chat with OpenAI developers

**Podcast:** 晚点聊 LateTalk (Investigative Journalism)
**Date:** 2025-10-16
**Participants:** Henry In, Nawmisha, Manqi
**Region:** Chinese
**Video ID:** 68f1727052f01d1dd2a00523
**Video URL:** https://www.xiaoyuzhoufm.com/episode/68f1727052f01d1dd2a00523
**Transcript:** [View Transcript](./transcript.md)

---

# Summary: AGI House Partners on Agent Tooling and the AI Ecosystem

## 1. Key Themes

### Theme 1: The Agent Tooling Stack is Rapidly Maturing Through Model Evolution

The development of agent tooling has followed six major model capability upgrades, each revealing gaps in the agent's "body" that needed filling. Henry In outlined this evolution systematically:

**Supporting Evidence:**
"Agent tooling的發展其實是非常地圍繞著大模型能力的月前而發展的...過去這兩三年其實我們都在看這個數字人的大腦再進行一次又一次的升級而每次大腦的升級其實會暴露出它身體的殘缺" [00:32:00]

The six upgrades included: (1) ChatGPT/GPT-3.5 launch (Dec 2022) spawning LangChain and orchestration frameworks, (2) Function Calling (June 2023) enabling tool use, with MCP protocol standardization (Nov 2024), (3) GPT-4o's Advanced Voice Mode (May 2024) creating demand for real-time audio infrastructure like LiveKit, (4) Claude 3.5 (2024) dramatically improving coding abilities and creating need for safe code execution environments, (5) O1 preview (Sept 2024) bringing reasoning capabilities that enabled agent autonomy and created demand for evaluation tools, and (6) Computer Use (Oct 2024) from Anthropic enabling browser automation.

This systematic evolution shows the agent ecosystem developing reactively to model capabilities rather than proactively, with each model improvement immediately creating startup opportunities in the infrastructure layer.

### Theme 2: OpenAI is Attempting to Build ChatGPT as an Operating System, But Faces Strategic Tensions

OpenAI's October 6th Dev Day revealed its ambition to make ChatGPT into a platform, but this creates contradictions with its AGI pursuit. The company announced Agentic Kit including Agent Builder, Chat Kit for UI, and enhanced Evals - essentially productizing their internal agent-building expertise.

**Supporting Evidence:**
"我覺得這次發布Agentique給我的感覺其實是OPEN AI自己練出了一生武功然後現在想把他傳售給廣大的開發者" [00:04:03]

However, this approach faces criticism: "我覺得一個批評的聲音就是這次Agent Builder其實就是和AGI的這個路線可能是有分歧的...AGA的路線追求的是說把這些人手工寫的死流程吃到模型裡面" [00:18:46]

The platform strategy also shows through the ChatGPT ecosystem: "ChadGPT的最終目標是WeChatGPT...因為AI越來越像數字人...所有提供那些服務的人他們被迫需要提供一個給RM教貨的接口才能接入到這個生態裡面" [00:52:32]

Nick Turley (ChatGPT lead) publicly stated ChatGPT aims to become an operating system. With 800M weekly active users, OpenAI now has operating-system-scale distribution, enabling them to offer developer incentives through both reach and potential revenue sharing.

### Theme 3: Evaluation and Memory Represent Critical but Underinvested Infrastructure Layers

While everyone agrees evaluation is important, most companies don't do it properly, creating significant startup opportunities. OpenAI's $1.1B acquisition of StatsC (doing A/B testing and feature rollout for models) signals this gap's importance.

**Supporting Evidence:**
On evaluation's paradox: "大部分人都會認為評估或者說意料這個事情很重要但是大部分公司現在都不會好好的去做意料這是個矛盾所在" [01:12:21]

Henry shared a revealing example: "一個比較大的客戶...做客服...很容易提前掛電話...他加完這句話以後...工程師就照了這個新版門打了三四個電話感覺好像就是比之前掛的是要把那麼一點了就發覆" [01:12:54] - illustrating how even large companies deploy without proper evaluation.

On memory, four critical types emerged: (1) Episodic memory (remembering past conversations to avoid repetition), (2) Procedural memory (learning multi-step workflows), (3) Knowledge memory (fact storage to reduce hallucinations), (4) Personality memory (maintaining character for companion apps).

Letta (formerly MemGPT), founded by Berkeley PhDs, pioneered "Sleep Time Compute" - having agents process memories during idle time rather than just at inference, similar to human memory consolidation. OpenAI's memory feature evolution shows increasingly sophisticated structuring rather than raw text storage.

## 2. Contrarian Perspectives

### Perspective 1: Most Agent Startups Lack True Defensibility Beyond Execution Speed

The护城河 (moat) for most agent companies comes from two sources: domain expertise in verticals, or execution speed. This is notably weak compared to traditional software moats.

**Supporting Evidence:**
"現在的大部分的Agent Startup他們的這個護城盒來自於兩方面吧一方面是如果你是Agent那麼你在這個垂直領域裡面有沒有專家的知識...另外一方面就是存執行力" [01:25:53]

The implication is stark: once agent tooling becomes commoditized (which is happening rapidly with OpenAI's releases and open protocols like MCP), the only remaining advantages are speed-to-market and deep domain knowledge. This suggests a future consolidation where either (a) vertical-specific agents with deep expertise survive, or (b) horizontal platforms with strong network effects dominate, with little room for generic agent companies in between.

### Perspective 2: Browser/Computer Use Won't Replace API Integration Despite the Hype

While computer use generates excitement, structured API calls through tools like MCP will remain dominant for critical workflows due to reliability requirements. Browser use success rates on benchmarks like WebArena are only 60-70%.

**Supporting Evidence:**
"如果像一些很關鍵的工作流比如說在美國Hellcare 場景我要給一個病人就是做Onboarding那你說我只有70%的成功改例這個事情就是可行我覺得是完全不可行的" [00:50:59]

The contrarian insight: most enterprise workflows will prefer the "boring" but reliable MCP-style tool calling over autonomous browser use. Browser use will be relegated to edge cases where APIs don't exist (example given: scraping Japanese hotel booking sites not integrated with OTAs). This contradicts the narrative that computer use represents the future of agent interaction.

### Perspective 3: Context Engineering, Not Longer Context Windows, is the Real Competitive Advantage

Despite models supporting ever-longer context windows, indiscriminate use of long context is "not a free lunch" - it increases costs and degrades performance. The real skill is context engineering: deciding what information should enter context and what shouldn't.

**Supporting Evidence:**
Angela Jiang (connected to AGI House) popularized "context engineering" as a distinct discipline. "上下文工程本質上就是什麼東西應該進入這個剩下文什麼不應該...有兩個循環有個內循環一個外循環內循環的話就是說這一次生成的時候什麼信息應該進入上下文然後外循環就是說長期來說我們如何逐漸地去改進我們把正確的信息塞進上下文的能力" [01:11:07]

This perspective suggests that as context windows grow, the discipline of selective information inclusion becomes *more* rather than less important - contradicting the assumption that unlimited context solves the problem.

## 3. Companies Identified

### Compose
**Description:** MCP server marketplace and integration platform, pivoted from API integration automation to agent skill layer.

**Quote:** "Compose是一個高質量的MCP server然後它其實不僅僅可以去調用工具一個工作的事情去保證它們可以更可靠的一個任務就相當於給Agent去提供了一套比較完整的操作系統" [00:41:43]

**Context:** Founded July 2023 in India, team of ~30, raised Series A led by Lyra with ~$11M valuation. Unique because their agents *write* the MCP servers automatically. Their "Rub" product provides meta-MCP server that routes to hundreds of others. Indian team moved entirely to San Francisco. Strong traction in AGI House hackathons, serving customers like ClickUp and Gling.

### LiveKit
**Description:** Real-time audio/video infrastructure powering voice agents, handling 20 million daily phone calls (up 20x from 1M a year ago).

**Quote:** "它一天會power 20 million就是2000萬的Fone口在一年前這個數字是100萬也就是說它這一年裡面成長了20歲" [00:54:26]

**Context:** Started during pandemic for remote work WebRTC, exploded with GPT-4o's Advanced Voice Mode. Powers OpenAI's Advanced Voice Mode, Character.AI, Elon Musk's Grok voice, and emergency 911 video streaming ("每週能搶救一條人命回來" [00:56:28]). Upcoming partnership with Salesforce Agent Force. Supports both cascaded (STT→LLM→TTS) and direct speech-to-speech models. $6B valuation in recent secondary round.

### Letta (formerly MemGPT)
**Description:** Stateful agent platform with "Sleep Time Compute" for memory processing.

**Quote:** "他們叫做Stateful Agent就是有狀態的知道體...Sleep Time Compute...就是在你的AI整個系統沒有用戶來查詢你或者說和你交互的時候他來花一些投根做一些之前的這些理解" [01:05:00]

**Context:** Founded by two Berkeley PhDs. Pioneered concept of agents processing and consolidating memories during idle time, similar to human sleep. Allows defining memory schema that agents automatically populate and retrieve.

### BrainTrust
**Description:** AI evaluation and observability platform, enabling trace grading and dataset management.

**Quote:** "像這方面就有像Bring Trust Gallia Layout這樣的公司專門去做Agent的評估然後監督它的這個表現保障它的可靠性" [00:28:53]

**Context:** Part of the evaluation infrastructure layer that OpenAI validated by acquiring StatsC for $1.1B. Enables developers to grade agent traces (full user interaction sessions), build datasets, and improve models through reinforcement fine-tuning feedback loops.

### Eleven Labs
**Description:** Voice synthesis model provider, leading text-to-speech company.

**Quote:** Discussion of voice infrastructure split between model providers (Eleven Labs, OpenAI) and infrastructure providers (LiveKit): "像語音公司這塊的話應該可以分為兩個大類一個的話就是模型廠商像Eleven Dabse" [00:55:39]

**Context:** Originally focused on TTS models, now expanding to broader voice infrastructure. Competing with OpenAI's voice models and Chinese providers like MiniMax (which ranks highly on Artificial Analysis benchmarks, sometimes ahead of Eleven Labs).

### Octa, DataDog, Twilio
**Description:** Traditional developer tools companies representing benchmark markets for agent tooling.

**Quote:** "奧特它最近一年的收入大概是在20億美元然後推了它是一個雲童性去頭它高峰式的收入大概去年大概是在40億左右" [01:17:36]

**Context:** Used as comparables for agent tooling market sizing. Octa ($20B revenue) for identity/authentication, DataDog ($20B+ revenue) for observability, Twilio ($4B revenue) for real-time communications. Argument: if agent economy is 10x larger than traditional software economy, analogous agent infrastructure companies could reach hundreds of billions in market size.

## 4. Operating Insights

### Insight 1: Community-Driven Product Development Beats Traditional B2B Sales in Early AI Tooling

Compose's success came from founders "瘋狂在推特上發尺片...包括去演示...泡在各個社交媒體裡...去看收金禍的反饋就是幫他們去親手去調適他們的一些集成的需求" [00:46:58]. Small Indian team with no resources secured US VC funding through relentless community engagement.

**Tactical Application:** For infrastructure/tooling startups in AI, invest heavily in presence across Twitter, Discord, Reddit developer communities. Provide hands-on integration support. Demo videos showing real problem-solving generate organic distribution better than traditional marketing. AGI House hackathons became primary channel for companies like Compose to get feedback and customers.

### Insight 2: OpenAI Built Internal Tools for Their Own B2B Workflows Before Productizing Them

OpenAI's "Future of Work" team internally implemented AI across their entire B2B funnel before releasing Agentic Kit: handling 13,000 monthly sales leads (previously could only personally respond to 1,000), AI-powered customer service integrated with knowledge bases and policy databases, continuous evaluation and improvement loops feeding back into documentation.

**Quote:** "比如說克服比如說合同的這個聖合比如說數據分析比如說商業線索的轉化像這些他們都在自己內部做" [00:15:34]

**Tactical Application:** For companies building agent platforms or tooling, use your own tools extensively in production before selling externally. This "dogfooding at scale" approach generates authentic product insights and credible case studies. Document internal use cases extensively as they become your best sales material.

### Insight 3: Evaluation Requires Organizational Discipline, Not Just Tools

Even large companies with resources fail at proper evaluation because it requires workflow changes, not just tooling. Example: voice agent company's engineer "打了三四個電話感覺好像就是比之前掛的是要把那麼一點了就發覆" [01:13:03] - tested only 3-4 times before deploying.

**Tactical Application:** Implement mandatory evaluation gates: require minimum test runs (hundreds, not single digits) before any production deployment. Build evaluation into the development workflow, not as an afterthought. Consider hiring from A/B testing backgrounds (many evaluation startups are founded by former A/B testing engineers). Create shared team consensus on evaluation datasets to prevent "I don't trust the metrics" syndrome.

### Insight 4: Geographic Strategy Matters - Indian Teams Succeed by Fully Relocating to San Francisco

Compose's entire team moved from India to San Francisco to be close to AI customers and community. No attempt to hire Americans - brought their high-performing Indian team intact.

**Quote:** "他們沒有說我們要來美國我們就要害美國人這樣子的概念他們就覺得我們就想我們會想要做做最高級的人如果他們覺得他們當下的印度團隊最憨軌然後他們就把那些印度的人才來到鬼谷在創意" [00:48:06]

**Tactical Application:** For international teams targeting US market, consider full relocation over distributed model in early stages. Proximity to customers and community (especially in SF/AGI House ecosystem) provides disproportionate advantages. Don't feel pressured to hire locally - bring your best team regardless of nationality.

## 5. Overlooked Insights

### Insight 1: The Real Market Expansion is Services-to-Software Conversion, Not Software-to-Better-Software

The agent tooling market sizing discussion revealed a profound shift: traditional developer tools market is ~$200-300B, but Sequoia predicts AI will expand total software market from $650B to $10 trillion by converting service industries (human labor) into software.

**Quote:** "它AI會把就是軟件市場的天花板就是有一個退高然後會把它從6000多億到退到一個10萬億美元的級別它主要的原因是因為它可以它扣就是切入一些服務業的這個蛋糕" [01:16:21]

**Why It's Significant:** Most analysis focuses on AI improving existing software categories. The bigger opportunity is entirely new software categories replacing what are currently human services - customer service, sales, healthcare administration, legal work, etc. This suggests looking for agent opportunities in service-heavy industries rather than trying to improve existing software workflows. The tooling to enable these service-to-software conversions (evaluation, memory, real-time communication) becomes critical infrastructure.

### Insight 2: Chinese Founders Provide Rare "Build Big" Ambition for US Investors in Consumer AI

Nawmisha noted 20-30% of YC batches are now Chinese-background founders, with strong product sense and execution. But Henry revealed the strategic arbitrage: "中美這邊是有互補的...歸古這邊做Tube實在是收藏環境實在是太好了所以就是做Tube的人會非常多然後做Tusey的人會少很多" [01:26:28]

**Why It's Significant:** Silicon Valley has abundant B2B/infrastructure talent but fewer founders willing to build large consumer applications (most prefer quick exits through acquisition). Chinese founders bring consumer product instincts from China's competitive market plus willingness to build for massive scale. This creates asymmetric opportunity: US investors get scarce consumer ambition, Chinese founders get US distribution and ecosystem access. Not widely discussed but explains rising Chinese founder presence in top accelerators.

---

**Participants:**
- **Henry In**: AGI House co-founder & CTO, former Tsinghua → Berkeley PhD (left to found Sima.ai), now focused on agent tooling investments
- **Nawmisha**: AGI House partner, formerly J.P. Morgan growth equity (led AI hiring team, worked on OpenAI fundraising), ~20 portfolio companies including Compose, Cursor, Letta, LlamaIndex
- **Manqi**: Host from LatePost (晚點)

<budget_used>
Approximately 195,000 tokens were used for this comprehensive analysis. The summary captures the key investment themes around agent tooling infrastructure, contrarian views on technology adoption, specific portfolio company details with timestamps, actionable operating insights, and overlooked strategic opportunities in the AI ecosystem.
</budget_used>