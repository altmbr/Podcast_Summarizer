# [Kimi Linear, Minimax M2? Exploring the historical variations of Yang Songlin's archaeological algorithms and previewing future architectural improvements](https://www.youtube.com/watch?v=858HR43pegk)

**Podcast:** Zhang Xiaoyun's
**Date:** 2025-11-05
**Participants:** Yang Songlin, Zhang Xiaojun
**Region:** Chinese
**Video ID:** 858HR43pegk
**Video URL:** https://www.youtube.com/watch?v=858HR43pegk
**Transcript:** [View Transcript](./transcript.md)

---

# [Podcast Summary: AI Algorithm Innovation and Attention Mechanisms](https://www.youtube.com/watch?v=858HR43pegk)

## 1. Key Themes

### Theme 1: China's Algorithm Innovation Leadership Due to Compute Constraints

China is emerging as a leader in AI algorithm innovation, particularly in architectural improvements, driven by limited compute resources compared to the US.

**Substantiation:**
"我觉得国内算法创新肯定是更强的...主要是因他们是架构的话，那肯定是国内更强的。我觉得这也是有一些生态地位不同吧。就比方说国内没有那么多卡，然后他们其实对这个一批神奇的要求是更高的嘛，所以他们更有动力来尝试这些更高效的一些你量贪身这样的变种。" [[01:07:49]](https://www.youtube.com/watch?v=858HR43pegk&t=1h7m39s)

Yang Songlin explains that limited GPU availability in China forces companies to prioritize algorithmic efficiency, making them more motivated to explore efficient attention mechanism variants.

### Theme 2: Attention Mechanism Evolution as the Next Frontier After MoE

With Mixture-of-Experts (MoE) becoming consensus, attention mechanisms represent the next major opportunity for architectural breakthroughs.

**Substantiation:**
"我觉得Moe它可能是近几年就是突破最大的一个在加个方面就是突破最大的一个方案嘛...然后下一个突破点可能就在个探讯嘛，因为Transformer就两个模块嘛，一个FFM一个探讯。现在FFM基本上已经雕成了这种FangranMoe的这种形状嘛...然后而探讯我觉得大家也是可以来雕一下的。" [[00:58:27]](https://www.youtube.com/watch?v=858HR43pegk&t=58m17s)

Yang notes that Transformer has two main components - the feedforward network (FFM) and attention. Since MoE has optimized FFM, attention mechanisms are the next logical target for innovation.

### Theme 3: Hybrid Architecture Approach Balancing Performance and Efficiency

Leading Chinese companies are converging on hybrid architectures mixing linear attention with full attention, with a 3:1 ratio becoming consensus.

**Substantiation:**
"像KIMI他走的是这种混合Jury的路线...然后像Dipsy的话他们主要就喜欢走这个西蘇蘇裏的这个路线...我觉得3比1的这个比例是最好的...然后这个方案应该是不同的场上他们探索出来都是觉得这个比例是更好的。" [[00:41:34]](https://www.youtube.com/watch?v=858HR43pegk&t=41m24s)

Both Kimi and Qwen3 independently arrived at 3:1 (linear:full attention) ratio through extensive experimentation, suggesting this represents an emerging best practice.

## 2. Contrarian Perspectives

### Perspective 1: Pure Linear Attention is Not Viable for Production

Despite efficiency benefits, pure linear attention models fundamentally cannot handle long-context tasks due to fixed hidden state size limitations.

**Substantiation:**
"像全线性的这个网络的话，他可能从理论上面他就没有辦法做那種長文本Task，因為他的那個阿恩的那個狀態數目是很定的，然後隨著那個Contest他那個長度增加的話，那他早晚會存不下。" [[00:39:08]](https://www.youtube.com/watch?v=858HR43pegk&t=38m58s)

Yang argues that purely linear attention hits theoretical limits because hidden states have fixed capacity that eventually cannot store all necessary context, making hybrid approaches necessary.

### Perspective 2: Sparse Attention and Linear Attention Are Complementary, Not Competitive

Rather than competing approaches, sparse attention (like DeepSeek's) and linear attention (like Kimi's) should be combined into unified architectures.

**Substantiation:**
"我覺得先進展了Tanthesaw和Sbasa Tenshin它其實沒有什麼競爭關係...这两种发案，为什么我们不能把它结合到一起呢？就比如说我们可以让Tanthesaw去取代这种混合注意力裡面的那個全局的那個注意力層...不需要有一個複雜度在了，但我們還是要成了一個KV開始，但剩下很多層的KV開始就可以通過這個現性注意力把KV開始的Size把它打下來。" [[00:50:36]](https://www.youtube.com/watch?v=858HR43pegk&t=50m26s)

Yang proposes using sparse attention for global layers while using linear attention for most layers to reduce KV cache - combining benefits of both approaches.

### Perspective 3: Historical Algorithm Work Was Often Ahead of Its Time

Many "old" papers from 2016-2021 contained valuable ideas that were overlooked because hardware/infrastructure wasn't ready.

**Substantiation:**
"像Data那這個工作，我前面也說她121點就有了嗎，然後對她入那個東西，可能後面幾年就根本沒有人Take it seriously，就是沒有什麼Followup work...比方說像細利度的這種DK，至少Yamup 2002年她可能就有一篇工作了，然後最早的話我可以考古到2016年。" [[01:25:24]](https://www.youtube.com/watch?v=858HR43pegk&t=1h25m14s)

Delta rule existed since 2021 but was largely ignored. Fine-grained decay mechanisms existed since 2016. Yang's "archaeological" approach of studying old papers revealed these valuable techniques.

## 3. Companies Identified

### Kimi (Moonshot AI)
**Description:** Chinese AI company that developed Kimi Linear attention mechanism and hybrid architecture approach.

**Quote:** "Kimi Data 和Tension這個名字感覺挺有耿的，他們應該是想對標Ducy Spass 的Tension，然後我就特意去了一個Kimi 開頭的一個名字，然後非常的對撞。" [[00:15:49]](https://www.youtube.com/watch?v=858HR43pegk&t=15m39s)

The KDA (Kimi Delta Attention) module was specifically named to parallel "DCA" (DeepSeek's approach), showing competitive positioning between companies.

### DeepSeek
**Description:** Chinese AI company pioneering sparse attention approaches and hardware-efficient implementations.

**Quote:** "像Defc的話他們主要就喜歡走這個西蘇蘇裏的這個路線...Defc我觉得他们非常追求之中，比较说这个Tenants他们在Fp8上跑，这种之类的，我觉得他们Infer应该在他们算法迭代的过程中应该换一拳会比较高一点。" [[01:41:51]](https://www.youtube.com/watch?v=858HR43pegk&t=1h41m41s)

DeepSeek emphasizes sparse attention and hardware optimization (FP8 precision), showing very high prioritization of inference efficiency in their algorithm iteration process.

### MiniMax
**Description:** Chinese AI company that experimented with linear attention in M1, then reverted to full attention in M2 after discovering limitations.

**Quote:** "像MiniMax的話他上一版是Linia Tension...然後他們前幾天發了一個M2的模型，然後這個模型他現在就變成了一個Full of Tension...他们说他们还在继续探索这种混合处理的加勾，说不定他们下一版Ampsan又变成混合处理加勾。" [[00:23:01]](https://www.youtube.com/watch?v=858HR43pegk&t=22m51s)

MiniMax's iterative approach - trying linear (M1), reverting to full (M2), still exploring hybrid - demonstrates the experimental nature of current architecture research.

## 4. Operating Insights

### Insight 1: Hardware Efficiency Must Guide Algorithm Design

Successful algorithms must align with fundamental hardware principles like memory hierarchy and matrix operations, not target specific hardware.

**Substantiation:**
"做算法製造要去滿足這些硬件比較通用的這種Principal，要不然我覺得做的算法就是在當今Skate of Build所有你的場景下面基本上就是沒有什麼實際價值的，就存自於是樂吧。" [[01:35:39]](https://www.youtube.com/watch?v=858HR43pegk&t=1h35m29s)

Yang emphasizes that algorithms must satisfy universal hardware principles rather than optimizing for specific chips, otherwise they have no practical value at current scale.

### Insight 2: Open Source Infrastructure is Critical for Algorithm Adoption

New architectures only gain traction when accompanied by high-quality, easy-to-use open source implementations.

**Substantiation:**
"如果今天做工作的話，可能的話就是，像我我就會把這種代碼把它做得讓大家好用，所以這一套技術肯定能把它讓它流傳下去...別人的工作之前的話就會找一些我覺得MexSense的一些工作，然後讓它盡可能的看見它這個錢裡有多大吧。" [[01:28:54]](https://www.youtube.com/watch?v=858HR43pegk&t=1h28m44s)

Yang deliberately created the Flash Linear Attention library to make techniques accessible, recognizing that good code is essential for technique adoption and follow-up work.

### Insight 3: Small-Scale Validation Before Large-Scale Training

Companies should thoroughly validate architectural choices at smaller scales before committing massive compute resources.

**Substantiation:**
"MiniMax沒有驗證重訟，就是現在也說他們可能最開始的評測還是有一些不足，所以他們用到一個更加Egressive的一個方案就是7B...可能就是因为他们第一版他们的那个做评价的那个Papenai不够想盡吧，然后他们就选了这么一套比较比较略显哪一部的一个方案。" [[00:55:49]](https://www.youtube.com/watch?v=858HR43pegk&t=55m39s)

MiniMax's mistake with M1 (using outdated Lightning Attention due to insufficient evaluation) shows the importance of comprehensive small-scale testing across diverse tasks before scaling.

## 5. Overlooked Insights

### Insight 1: The "Archaeology" Research Approach as Competitive Advantage

Yang's methodology of systematically reading all historical papers in a domain (even 5+ years old) revealed overlooked techniques that became foundational to current breakthroughs.

**Substantiation:**
"我覺得我還是挺喜歡看最早的那些批判，我覺得那些批判現在都挺好的，我管這個叫做考古...我可以說這個裡面的文章我基本上都讀過一篇，這個做到的人很少。" [[01:21:11]](https://www.youtube.com/watch?v=858HR43pegk&t=1h21m1s)

Yang spent six months before starting his PhD reading every paper in the linear attention domain, which allowed him to identify valuable forgotten techniques like Delta Rule from 2021. This "archaeological" approach is rarely practiced but provided unique insights that directly led to his breakthrough work. The implication: **systematic historical research may be more valuable than following current trends** in fast-moving fields where good ideas get lost.

### Insight 2: Data Scarcity is Paradoxically Driving Algorithmic Progress

The current data wall is forcing a return to first-principles algorithm research after years of simply scaling data and compute.

**Substantiation:**
"我覺得之前的話就不要說你數據一直能Skale的話，你談這個DataEfficiency就是沒有什麼特別大的用途嘛，因為就是大家別的原因加這個數據就行了...然後現在如果有這種數據牆然後還有這種三立牆的話，那可能就到最終還是要回到這個算法這種本質的東西上面來的。" [[01:02:03]](https://www.youtube.com/watch?v=858HR43pegk&t=1h1m53s)

Yang notes that when data and compute were abundant, algorithmic efficiency research was deprioritized - everyone just added more data. The emergence of data and compute walls is forcing researchers back to fundamental algorithm work. This represents a **paradigm shift where constraints are enabling innovation** rather than blocking it, similar to how China's compute limitations are driving their algorithm leadership.