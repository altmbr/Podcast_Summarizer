# From "Large and Strong" to "Small and Strong": Density Laws, RL Scaling Laws, and the Distributed Future of Intelligence

**Podcast:** 晚点聊 LateTalk (Investigative Journalism)
**Date:** 2025-12-11
**Participants:** 曼奇, 劉志遠, 蕭朝軍
**Region:** Chinese
**Video ID:** 693b46ec79debc3231f1d7bf
**Video URL:** https://www.xiaoyuzhoufm.com/episode/693b46ec79debc3231f1d7bf
**Transcript:** [View Transcript](./transcript.md)

---

# Podcast Summary: Dancing Law of LLMs - The Density Revolution in AI

## 1. Key Themes

### The Density Law: AI's Moore's Law Equivalent

The research team from Tsinghua University and MiniMax has identified a critical pattern in AI development: model capability density doubles approximately every 3.5 months. This "Dancing Law" represents a fundamental shift from pure scaling to efficiency optimization.

**Substantiation:**
"我們會看到過去六年的時間,就是大家經常提大模型,它的發展的邏輯是規模法則...但是我們會說,規模法則同時給我們帶來的非常大的問題,其實就是你模型勳得更大之後,其實意味著它的訓練成本和它的使用成本都會相應得變得更高" [00:06:30] - Liu Zhiyuan

The team's observation shows that from pre-ChatGPT to post-ChatGPT era, the rate of density improvement actually accelerated from one rate to 3.3 months, and with 2025 models, further to 3.5 months [00:20:20].

### Two Parallel Mainlines: Capability Enhancement and Efficiency Improvement

While the industry focuses heavily on capability improvements (the "bright line"), there's an equally important but less visible development path focused on efficiency (the "dark line"). These aren't opposing forces but complementary developments.

**Substantiation:**
"其實我們會看到,就是這樣一條非常清晰的出現,就是這個模型在變得越來越同有,越來越接近,甚至是超越我們人類的這個智能的水平。那同時的話,就是我和朝軍,我們團隊所發表的這篇論文,其實想給大家呈現另外一條出現,其實就是能效更高" [00:05:40] - Liu Zhiyuan

### The Inevitable Shift to Edge AI and Distributed Intelligence

The future of AI won't be centralized in a few massive cloud models but distributed across edge devices, with each person having their own personalized AI that learns continuously from their data.

**Substantiation:**
"我們其實可以設想未來幾年之後,智能化它也一定是分布式的...所以就是我們認為未來智能化的社會,一定是要在我們的中端的社會上,要為每個人每個智能的中端提供這種智能化的證明一個服務" [01:22:58] - Liu Zhiyuan

By 2030, the team predicts edge devices can support models over 60B parameters with 8B+ active parameters, enabling GPT-4/5 level capabilities on-device [01:03:37].

## 2. Contrarian Perspectives

### Against the "Only Giants Can Build Models" Narrative

In 2023, industry giants claimed the world only needs a few large models, echoing IBM's 1943 claim that the world only needs five computers. The team explicitly rejected this narrative as fundamentally wrong.

**Substantiation:**
"就是在23年初的時候,曾經有過一些這個巨頭說,這個世界上不需要超過幾個大夢形...1943年的時候,IBM的董事長曾經說,全球不需要超過五台主機" [00:00:50] - Liu Zhiyuan

The team's internal calculation showed that training a 140B model to chase GPT-4 would cost "several tens of millions RMB" but wouldn't be commercially viable due to lack of differentiation [00:23:17]. Instead, they pivoted to density optimization.

### Rejecting the API-Only Business Model for Startups

Despite industry trends, the team concluded that providing cloud API services lacks defensibility for startups, especially when large companies can subsidize losses from other profitable businesses.

**Substantiation:**
"我們會認為在雲上來提供APR對於一個創業公司,尤其是加點很不太厚的創業公司,我們認為是一個風險極大的事情" [01:11:55] - Liu Zhiyuan

This prediction proved prescient when DeepSeek sparked a price war in May 2024 [01:12:02].

### Long-Context is Actually About Long Output, Not Input

While the industry obsesses over long input context windows, the real challenge for agents and deep thinking is long output capability. Many linear attention mechanisms fail at this.

**Substantiation:**
"現在大家關注所謂的長文本,其實還是關注在之前那種長輸物的問題上...那面向生思考和A-jump的場景,它更應該處理的內容,就是它會有很長的這種輸出" [00:56:46] - Xiao Chaojun

This is why MiniMax moved from linear attention hybrid to full attention for their M2 model [00:57:08].

### AI Unemployment Concerns Miss the Bigger Picture

Rather than worrying about AI-caused unemployment, the real constraint on human progress has been our own knowledge limitations. AI will liberate us to explore vastly more of reality.

**Substantiation:**
"我覺得過去的這幾十年,我覺得人類的發展其實是被棒的住的...被我們人類自己的知識給棒的住了...所以我是覺得,這個智能時代最讓人找米的地方,不只是說我們實現了AI,而是AI能夠讓我們更快的,更好的,能夠認識一個更大的世界" [01:29:08] - Liu Zhiyuan

### Superintelligence Research Restrictions Would Repeat Historical Mistakes

Arguing against superintelligence research is like arguing against electronic computers in the 1940s because they were used for military purposes—fundamentally misguided.

**Substantiation:**
"如果說回到1940年,因為一些人說computer這個東西,電子計算機這個東西是用來做軍事的,所以我們不應該研究它,你覺得是合理的嗎" [01:33:16] - Liu Zhiyuan

## 3. Companies Identified

### DeepSeek

**Description:** Chinese AI company known for efficient model architectures

**Why Mentioned:** Pioneered sparse Mixture-of-Experts (MoE) at scale and validated the density improvement path; triggered industry price war with efficient models

**Quote:** "其實可以看到現在開源界...想簽文也做簽文next,Depthic就跟不用說了,也今年V3.2也是做了細酥的騰訊...所以可以看到現在在加工上去提升文件效率已經成為一個非常共識的一件事情" [00:08:48] - Xiao Chaojun

### MiniMax

**Description:** AI startup focused on edge AI and efficiency optimization

**Why Mentioned:** Released MiniCPM series achieving strong performance with dramatically fewer parameters (2.4B matching 13B models); pioneering commercial deployment in automotive sector

**Quote:** "就是用一個24億的參數就可以實現像這個當時的喇嘛兔的13B,然後像當時的Mitro7B...就是這樣的一個模型的效果...就是在手機上就可以跑了" [00:24:32] - Liu Zhiyuan

### OpenAI

**Description:** Leading AI research company

**Why Mentioned:** Set industry direction with ChatGPT and subsequent models; also pursuing efficiency with mini series despite resource advantages

**Quote:** "那你從閉源界,你就可以也可以看到類似的事情,就像這個open.i它也會去搞各種mini系列的模型" [00:09:01] - Xiao Chaojun

### Geely and Chery (奇瑞汽车)

**Description:** Chinese automotive manufacturers

**Why Mentioned:** First to deploy MiniMax's efficient models in production vehicles for intelligent cabin systems in 2024

**Quote:** "就是我們今年應該最早的落地的是查馬子達的一款車型,然後後面就是吉利這個有一款車型,然後基本上在今年就已經量產" [01:07:01] - Liu Zhiyuan

## 4. People Identified

### Liu Pengfei (劉鵬菲)

**Description:** Young professor at Shanghai Jiao Tong University

**Why Mentioned:** Leading research on "Less is More" - achieving stronger model capabilities with less training data through better data curation

**Quote:** "比如說上海交大有一位教授叫劉鵬菲,這個非常年輕的一個老師,他最近就是做了一系列的工作叫Less Eastmore,就是說我能用更少的數據可以去得到更強的能力" [00:37:11] - Liu Zhiyuan

### Ilya Sutskever

**Description:** Former OpenAI Chief Scientist, co-founder of Safe Superintelligence Inc.

**Why Mentioned:** Left OpenAI due to resource constraints for pursuing safe AGI research, illustrating that even well-resourced companies face compute scarcity

**Quote:** "包括伊莉亞,為什麼會從OPEN AI走,因為它覺得它拿不到足夠多的資源去追尋它的對前央做Safe的一樣" [00:18:30] - Xiao Chaojun

### Sam Altman (implied in "OpenAI研究委員會")

**Description:** OpenAI CEO

**Why Mentioned:** Recent tweets about "Iodoma's magic" and "unhackable environments" signal OpenAI's focus on scaling reinforcement learning environments

**Quote:** "OPEN AI之前這個機前,有那個研究委員的接通委,他就在發推的時候這個Iodoma的Magic,然後他的Matcher的核心在於一個Unhackbo的Invirement,就是不可被Hack的環境" [00:42:41] - Xiao Chaojun

## 5. Operating Insights

### The "Small to Large" Scaling Strategy

Teams can conduct extensive experiments on small models to predict large model behavior, dramatically reducing the cost of finding optimal configurations before expensive training runs.

**Substantiation:**
"我們能不能做到一小間大,我們做大量的小的模型的實驗,我們書籍的這些經驗的這種數據,能夠讓我們預測出我們即將要訓練的那個大模型在什麼參數,什麼數據配置下,然後它能夠達到更高的效果" [00:28:50] - Liu Zhiyuan

### The L0-L4 Data Processing Pipeline

MiniMax employs a five-level data curation framework: L0 (raw data collection), L1 (filtering/deduplication), L2 (quality selection), L3 (synthesis), and L4 (verification). This systematic approach achieved 10x data efficiency.

**Substantiation:**
"就是我們用我們的這套數據預處理的這個PAPLIN,把這個翻外版的我們做了一個經驗...得到了一個它的十分之一不到的這麼一個叫做Ouch翻外版,那我們就會發現用這個Ouch翻外版訓練的這個模型能力比這個原始的這個翻外版訓練的模型能力還要再高" [00:36:20] - Liu Zhiyuan

### Hardware-Software Co-Design as Core Advantage

Winning architectures throughout neural network history (including Transformer) succeeded because they maximized hardware utilization. Future competitive advantage requires co-optimization across algorithm, architecture, and hardware.

**Substantiation:**
"像Transformer這早的提出,其實核心的問題就是,因為它認為吞噬這種架構是能夠把GPU利用率達滿的,所以它提出來這個點" [00:50:25] - Xiao Chaojun

### The Strategic Pause: Fleet Fungibility Over Rapid Expansion

In late 2023, rather than spending tens of millions RMB to train a 140B model chasing GPT-4, the team pivoted to building model infrastructure and exploring efficiency, leading to the 2.4B MiniCPM breakthrough that differentiated them.

**Substantiation:**
"所以我們就會認為,如果說這個配方都沒有什麼變化,你只是把模型參數變大了,然後把數據動多一點,再訓一個GP4模型,對我們來講在商業上是講不通的" [00:23:47] - Liu Zhiyuan

### Standardized Fine-Tuning Toolchains Enable Rapid Deployment

MiniMax's success in automotive (going from partnership to production in 6 months) stems from highly standardized SFT toolchains and data synthesis processes, allowing rapid adaptation to 100+ function points per vehicle model.

**Substantiation:**
"就譬如我們的模型,然後我們其實會內部會有一個非常這個標準化的這麼一個SFT的這麼一個工具鏈,然後以及就是如何去做相應的這個數據合成的這麼一個規範,所以就差不多反正是相對是比較高效的這麼一個模式" [01:10:26] - Liu Zhiyuan

## 6. Overlooked Insights

### The 12x Edge-to-Cloud Compute Ratio

According to China Academy of Information and Communications Technology, in 2023, the total compute power on mobile phones in China was **12 times** the compute power in all data centers combined. This fundamentally challenges cloud-centric AI narratives and suggests the ultimate distribution of intelligence will mirror information technology—distributed at the edge.

**Substantiation:**
"就是二二四年初中國電信研究院的統計,它就是說二三年的時候全國的端策的就是手機上的算力加在一起的總量是全國的是數據中心的算力的12倍" [01:21:36] - Liu Zhiyuan

This statistic powerfully validates the Dancing Law thesis but was mentioned almost in passing. If edge compute already dominates by 12x, and density improvements continue exponentially, the implications for AI deployment architecture are revolutionary.

### AGI as "AI-Producing AI" Rather Than "Human-Replacing AI"

The traditional Turing-test definition of AGI ("can do what humans do") may be fundamentally wrong. A more useful definition might be AGI as a system that can produce specialized AI systems on demand—essentially "manufacturing intelligence" rather than "being intelligent."

**Substantiation:**
"未來的一個可能AGA的形態是一個生產AI的AI...就是說未來我們現在你可以看到我們會有很多的公司很多的這種需要僱傭人去做很多的生產勞動,但是我覺得未來的可能就是會有AGA來幫人家的事情,就是我跟他說現在我想要有一個自動駕駛的模型,然後跟AGA說,AGA開始就是去構建這個模型" [01:35:17] - Xiao Chaojun

This reframes the entire AGI question: rather than one system that can do everything (which may be impossible or undesirable), AGI could be the meta-system that creates specialized systems. This parallels how the industrial revolution's key was "machines making machines" [01:36:23]. This insight didn't get the attention it deserved but could reshape how we think about and build toward AGI.