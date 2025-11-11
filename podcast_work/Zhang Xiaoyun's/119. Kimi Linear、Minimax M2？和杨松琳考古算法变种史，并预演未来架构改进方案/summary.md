**Title:** Unknown
**Podcast:** Zhang Xiaoyun's
**Date:** 2025-11-05
**Participants:** Unknown
**URL:** Unknown
**Transcript:** [transcript.md](transcript.md)

---

# Podcast Summary: Algorithm Innovation in AI - Conversation with Yang Songlin

## 1. Key Themes

### China's Algorithm Innovation Leadership Due to Compute Constraints

**Theme:** China is leading in AI algorithm innovation specifically because of limited compute resources, forcing companies to optimize architectures rather than simply scaling with more GPUs.

**Substantiation:**
Yang Songlin states: "国内的算法创新肯定是更强的...主要是因为生态地位不同，所以它们更有动力来尝试这些更高效的一些...像规固有些公司基本上就是卡太多了，它们就难得高...反正你走你走就有一定要跑得快一点。"

Translation: "Domestic algorithm innovation is definitely stronger... mainly because of different ecosystem positions, so they have more motivation to try these more efficient approaches... Some foreign companies basically have too many cards [GPUs], so they don't bother to optimize... You have to run faster when you have constraints."

He further explains: "像国内公司也感觉在逐漸在用...KIMIT它也是最早吃沒有螃蟹的一個地方...给我的感觉就是美国他们對去年Dipstick Sponsored真正的效果比那个更强。"

Translation: "Domestic companies are gradually adopting... KIMI was the first to eat the crab [take the risk]... My feeling is that China's actual results are stronger than America's."

### The Data Wall is Forcing Architecture Innovation

**Theme:** As high-quality training data becomes scarce, the industry is pivoting from data scaling to architectural improvements, making algorithm research critically important again.

**Substantiation:**
Yang Songlin explains: "我觉得之前的话就不要说你SKILL的话，你談這個Data Efficiency就是沒有什麼特別大的那個用途，因為大家別的原因加這個數據就行了...現在如果有這種數據強然後還有這種算力強的話，那可能就到最終還是要回到這個算法這種本質的東西上面來的。"

Translation: "Previously, when discussing scaling, talking about data efficiency didn't have much use because everyone could just add more data... Now if there's a data wall and compute wall, then ultimately we have to return to the essence of algorithms."

He cites OpenAI's CTO: "我記得之前像Apple Eye的CTO他也說就可能在這個節點上面算法的這個研究重要性可能會被重新抬高。"

Translation: "I remember OpenAI's CTO also said that at this juncture, the importance of algorithm research will likely be elevated again."

### Linear Attention is Resurging for Long-Context Inference

**Theme:** Linear attention mechanisms are making a comeback specifically for long-context reasoning and agent applications, where inference costs become prohibitive with standard attention.

**Substantiation:**
Yang Songlin describes the motivation: "年初的時候...像DFC R1和KIMI1.5那個時候剛剛發...他的核心他會做些R1然後會得到一些非常長的一些思維念...這個思維念的長度能他往往就是能夠到幾萬個頭肯這個長度...KIMI就覺得就是如果我們用每一層都是平方的這個...他要存一個大量的KV開始然後換他每一步現身的這個時間複雜度...也是一個平方的。"

Translation: "At the beginning of the year... when DeepSeek R1 and KIMI 1.5 just launched... their core approach generates very long chains of thought... these thinking chains can reach tens of thousands of tokens... KIMI felt that if every layer uses quadratic complexity... they need to store massive KV caches and each decoding step also has quadratic time complexity."

### Hybrid Architectures (3:1 ratio) Emerging as Consensus

**Theme:** A 3:1 ratio of linear attention to full attention layers is becoming the industry standard for hybrid architectures, balancing efficiency with performance.

**Substantiation:**
Yang Songlin states: "我覺得3B1應該就是一個在這個不共識的這個Hybrid Nini裡面的一個共識，就是大家用3B1的一個比例來混這個模型...像MiniMax他上一版是Linia Tension他應該算是這種混合這種混合線性和平方助理的一個先曲因為他年初發的M1的版本的話是一個非常大規模的混合助理的一個時間...然後像前面三Ness他也是用到3B1然後混GIGI.DON的這個訪案。"

Translation: "I think 3:1 should be a consensus within this non-consensus Hybrid approach, everyone uses a 3:1 ratio to mix the model... MiniMax's previous version used linear attention in a very aggressive hybrid architecture... then Qwen 3 Next also uses 3:1 mixing with gated delta networks."

### Hardware-Algorithm Co-evolution Driving Innovation

**Theme:** Algorithm design must respect hardware principles (matrix multiplication efficiency, memory hierarchy) to be practical, and current hardware evolution favors matrix-multiplication-heavy approaches.

**Substantiation:**
Yang Songlin emphasizes: "我覺得就一定要吧只有你與里面值得看的文章全部都看一遍...我觉得做算法至少要去满足这些硬件比较通用的这种Principal要不然我觉得做的算法就是能在当今这个Belated所有你的这个场景下面基本上就是没有什么实际价值的就存自於自乐吧。"

Translation: "I think you must read all the worthwhile papers in the field... I think algorithm design must at least satisfy these relatively universal hardware principles, otherwise the algorithms you create basically have no practical value in today's scenarios, it's just self-entertainment."

He explains the hardware trend: "硬件会变成Transformer更喜欢的模样...因为现在要加个硬件大家会发现它就是为了去优化举真成...然后让它举真成越快越好...像Tanthcore然后像这种TMI这种东西然后像最近的 Blackwell上面它有一些专门针对这种举真成它有一些单独的那种类传上面单独的那种Mimery。"

Translation: "Hardware is evolving to become what Transformer prefers... because current hardware is designed to optimize matrix multiplication... making matrix multiplication faster and faster... like TensorCore, TMI, and recently Blackwell has dedicated memory specifically for matrix multiplication."

## 2. Contrarian Perspectives

### Pure Linear Attention Models Don't Work - Hybrid is Necessary

**Contrarian View:** Despite years of research into linear attention as a replacement for standard attention, pure linear attention architectures fail on long-context tasks, and hybrid approaches are the only viable path.

**Substantiation:**
Yang Songlin states: "我覺得Ninliant Tension我現在現在的公式的設計就是說Tryton Ninliant Tension是不 work的...就是它在這種長文本下面它是有一些比較翻到漫頭的一些缺陷的...現在大家一般都不會去嘗試這種純陷信的這種模型。"

Translation: "I think with current linear attention designs, purely linear attention doesn't work... under long-context scenarios it has some fundamental defects... now people generally don't try these pure linear models."

He explains why: "像全線性的這個網絡的話它可能從理論上面它就沒有辦法做那種長文本Task因為它的那個阿恩的那個狀態數目是很定的然後隨著那個Contest它那個長度增加的話那它早晚會存不下那早晚會損失很多那種金度在裡面。"

Translation: "For fully linear networks, theoretically they cannot handle long-context tasks because their hidden state size is fixed, and as context length increases, they will eventually be unable to store everything and lose a lot of precision."

### MiniMax's Retreat from Linear Attention Reveals Multi-Hop Reasoning Gap

**Contrarian View:** MiniMax discovered that linear attention models have a critical weakness in multi-hop reasoning that wasn't detected by standard benchmarks, forcing them to revert to full attention despite efficiency gains.

**Substantiation:**
Yang Songlin reveals: "然後後面他們發現就是如果他們在一些比方說那種叫做Motivop Reasoning就是多跳的這個Rhythm Need上面這種Tasks的話他發現這個調點會非常的大...因為他們最開始沒有去檢測這種多跳推力的這個能力然後他們主要只看那些比方說MML UR然後J的這種能力...結果來說的話我覺得那個Nighting Need Tension的話他其實是一個比較弱的一個先行注意力。"

Translation: "Later they discovered that on tasks like multi-hop reasoning, the performance drop was very large... because initially they didn't test multi-hop reasoning ability, they mainly looked at MMLU and general capabilities... In the end, I think Lightning [Linear] Attention is actually a relatively weak linear attention."

He adds context: "他們就暫時退回了這個全部都是Somai's Tension的這個富爾Tension的這個加勾...但他們說他們還在繼續探索這種混合處理的加勾說不定他們下一版Ampsan又變成混合處理加勾。"

Translation: "They temporarily retreated to full softmax attention architecture... but they said they're still exploring hybrid architectures, maybe their next version will be hybrid again."

### Sparse Attention vs. Linear Attention Address Different Bottlenecks

**Contrarian View:** Rather than competing approaches, sparse attention and linear attention solve complementary problems and should be combined - sparse for maintaining full attention capability, linear for reducing KV cache.

**Substantiation:**
Yang Songlin argues: "我觉得现性的彈省和Spaasa的彈省它其实没有什么競爭關係吧我覺得現性的彈省的這個競爭對手可能更多的是Slighting window的彈省...像DFC的話他們主要就喜歡走這個西蘇蘇裏的這個路線...然後像混合Jury的話他就是不僅他能減少KiriCatch他能減少很多KiriCatch因為他覺得都是層都是這種類似Yahana的這種層。"

Translation: "I think linear attention and sparse attention don't really have a competitive relationship. Linear attention's competitor is more sliding window attention... DeepSeek mainly likes the sparse route... while hybrid approaches can not only reduce KV cache but reduce a lot of KV cache because most layers are RNN-like layers."

His proposed synthesis: "我覺得可能就是我目前心中比較理想的一個高校的一個價格就是...我們可以讓Spaasa彈省去取代這種混合注意力裡面的那個全局的那個注意力層這樣的話我們就不需要有一個全局注意力的那個複雜都在了那個KV開始但剩下很多層的KV開始就可以通過這個現性注意力把KV開始的Size把它打下來。"

Translation: "I think my current ideal efficient architecture is... we can let sparse attention replace the global attention layers in hybrid attention architectures, so we don't need the complexity of global attention and its KV cache, but the remaining layers can use linear attention to reduce KV cache size."

### Historical Algorithms Are Often Superior But Lacked Infrastructure

**Contrarian View:** Many "old" algorithms from 2-5 years ago were actually superior designs but failed to gain adoption due to lack of optimized implementations, not fundamental limitations.

**Substantiation:**
Yang Songlin explains: "我覺得其實很多歷史的算法他其實是很先進的但是可能當時同好沒有意識到這個工作的價值然後可能那個工具不會買摸了...也有可能就是那個工作他的配套比如說那些代碼開源代碼做的太難了然後其他人想服務也沒法服務。"

Translation: "I think many historical algorithms were actually very advanced, but perhaps the community didn't realize the value of the work at the time and that tool wasn't adopted... or perhaps the supporting infrastructure like open-source code was too difficult, so others couldn't follow up even if they wanted to."

He uses Delta Rule as example: "像得他入那這個工作我前面說他上兩年就有了...然後得他入那個東西可能後面幾年就根本沒有人taggy seriously就是沒有什麼follow work...從時間內也見上來說呢也話來說呢可能有一些技術比較時像這種系力度的這種疑望可能很多年前就有了比方說像這個系力度的這種dk至少i'mapp二年二年他可能就有一篇工作了然後最早的話我可以考古的二年一六年。"

Translation: "Like Delta Rule, I mentioned it existed two years ago... but for several years after, basically no one took it seriously, there was no follow-up work... Some techniques like fine-grained decay existed many years ago, at least in 2022 there was work on it, and the earliest I can trace back is 2016."

### Theoretical Complexity Matters Less Than Hardware Efficiency

**Contrarian View:** Transformer succeeded despite higher theoretical complexity (O(n²)) than RNNs (O(n)) because hardware efficiency trumps asymptotic complexity in practice.

**Substantiation:**
Yang Songlin explains: "像Euthansion它就算它是平方的复杂度它复杂度比A&N搞了一个级别但是它就可以通过局任程法然后来算到那个OPU所以它的硬件清盒是比A&N要好很多的所以大家会宁愿去用理论复杂度更高的Transformer也不会来用这个理论复杂度更定的这个ISTM因为他们这个硬件清盒表现完全不要。"

Translation: "Although attention has quadratic complexity, one level higher than RNNs, it can leverage parallel computation on GPUs, so its hardware efficiency is much better than RNNs. So people would rather use theoretically more complex Transformers than theoretically more efficient LSTMs because their hardware efficiency performance is completely different."

## 3. Companies Identified

### Kimi (Moonshot AI)
**Description:** Chinese AI company that developed hybrid linear-attention architecture (KDA - Kimi Delta Attention) with 3:1 ratio of linear to full attention layers, specifically optimized for long-context reasoning and agent applications.

**Quotes:**
- "Kimi他走的是这种混合Jury的路线...然后像Kimi的话他还是有一些全局Jury Needle然后他的那些比较快速的那些层是一些线性Jury Needle层然后这个好处的话就是说他可以使很多的KiriCatch。" (Kimi uses hybrid approach... it still has some global attention layers and fast linear attention layers, which allows saving a lot of KV cache.)

- "張玉完的這個KDA他就是把這個E度比較粗的一個衰簡率把它換成了一個E度比較細了一個衰簡率就是現在的話就是一個Tanzen害了下面不同的位度他有一個自己的這個衰簡率。" (Zhang Yu's KDA replaced coarse-grained decay with fine-grained decay, where each dimension has its own decay rate.)

### DeepSeek
**Description:** Chinese AI company pursuing sparse attention route, developing dynamic sparse attention mechanisms that select important tokens rather than using fixed patterns.

**Quotes:**
- "像DFC的話他們主要就喜歡走這個西蘇蘇裏的這個路線他們那個Kimi Spassal Tension然後包括他們之前發的那個Late Spassal Tension都是這種走的西蘇的路線然後他們覺得可能西蘇是一種更好的方式來降低這種DCoding的Cost。" (DeepSeek mainly likes the sparse route, their sparse attention mechanisms are what they believe is a better way to reduce decoding cost.)

- "我覺得Divisic他是一個非常出重這種硬件和算法鞋桶設計的一個公司像Divis Spassal Tanthan的話他會有一個那個他就是Fp8來做這個算這個Tanthan他不需要Softmax他只需要算那個Loget然後來做Tanthan可以來選Score。" (I think DeepSeek is a company that emphasizes hardware-algorithm co-design. Their sparse attention uses FP8 and doesn't need softmax, only logits for scoring.)

### Qwen (Alibaba)
**Description:** Alibaba's AI division that developed Qwen 3 Next using hybrid architecture with gated delta networks, achieving strong performance with 3:1 linear-to-full attention ratio.

**Quotes:**
- "然後後面千萬3 Next的話它也是用到3B1然後混GIGI.DON的這個訪案...然後這個訪案應該是不同的廠商他們探索出來都是覺得這個比例是更好的。" (Qwen 3 Next also uses 3:1 ratio mixing with gated delta networks... this approach seems to be what different manufacturers have explored and found to be better.)

### MiniMax
**Description:** Chinese AI company that initially used aggressive 7:1 linear attention ratio in M1, then reverted to full attention in M2 after discovering multi-hop reasoning deficiencies, demonstrating the risks of insufficient evaluation.

**Quotes:**
- "像MiniMax的話他上一版是Linia Tension他應該算是這種混合這種混合線性和平方助理的一個先曲因為他年初發的M1的版本的話是一個非常大規模的混合助理的一個時間然後他們前幾天發了一個M2的模型然後這個模型他現在就變成了一個Full of Tension。" (MiniMax's previous version used linear attention in a very aggressive hybrid, their M1 was large-scale hybrid, but they recently released M2 which reverted to full attention.)

- "他們的這個負責團對他們非常的 open然後他們分享了很多這種經驗然後我覺得這個經驗都是很寶貴的...他們說是由OCA來做這種Contest Compression。" (Their team is very open and shared many valuable experiences... they mentioned using something to do context compression.)

### Meta
**Description:** Mentioned for exploring cubic complexity attention mechanisms, pushing beyond standard quadratic attention.

**Quotes:**
- "我看上次Mata還放了一個論文就是搞一個三次方的彈省就是寫平方複雜度他還不夠他還要搞一個三次方的。" (I saw Meta released a paper on cubic complexity attention, as if quadratic wasn't enough, they want cubic.)

### Hazyy Research (Stanford)
**Description:** Stanford research group led by Chris Ré that influenced Yang Songlin's research direction on efficient sequence modeling and linear attention mechanisms.

**Quotes:**
- "應該是到時候看到很多斯丹夫一個一個research的一個Groper叫做Hazzy Research就是吹到Airbird他們在斯丹夫的那個Nab然後到時候看到很多他們寫的寶克然後覺得虛列鍵模是一個非常有意思的問題。" (I saw a lot of work from a Stanford research group called Hazyy Research... I saw many of their blog posts and felt sequence modeling was a very interesting problem.)

## 4. Operating Insights

### Build Infrastructure Before Expecting Adoption

**Insight:** Algorithm innovations require accessible, optimized implementations to gain adoption. Creating easy-to-use libraries (like Flash Linear Attention) is as important as the algorithm itself.

**Substantiation:**
Yang Songlin emphasizes: "我覺得今天做工作的話可能的話就是不然像我我就會把這種代碼把它做的讓大家好用所以這一套技術肯定能把它讓他流傳下去...別人的工作之前的話我就會會找一些我覺得MexSense的一些工作然後讓他讓他盡可能地看見他這個錢力有多大吧。"

Translation: "If doing work today, I would make the code easy for everyone to use so this technology can be passed down... For others' work, I would find some that make sense and try to show their potential as much as possible."

He describes the virtuous cycle: "像這些做寂寞的廠商他們去做一些ProMizing的結果然後開源把這些為了把它發出來然後那些就是做推理引擎的人就會有很多動力來想辦法來東西...當這些音法的配套更好的時候然後比如說別的公司可能就是覺得向您聊探視它的音法的生態太差了...可能就算做出來這個生態不好可能它實際上Deploy它的成本也很高但現在只要這個生態做起來了然後就會有一個真相型環的一個作用。"

Translation: "Model companies produce promising results and open source them, then inference engine developers have motivation to support them... When the infrastructure ecosystem improves, other companies that previously thought the ecosystem was too poor... even if they built something, deployment costs were high. But now once the ecosystem is built, there's a virtuous cycle effect."

### Use Scaling Laws to Validate Before Full Training

**Insight:** Kimi uses internal "scaling law" checkpoints - validating architectures at smaller scales before committing to full training runs, treating it like "levels in a game."

**Substantiation:**
Yang Songlin reveals: "像Kimi甚至在之前的工作的技術上面新開發一個KDA...他在看頭寫了說他們是第一個驗證了就性能超越了附貪胜的混合臨届層胜加購...因為他們KIMI內部它是有一個叫做Skelling Light的一個東西就是說你在一個規模你就到下面一個規模去繼續Skelling就有點像通關它有很多很多關卡過了一關它有到下一關就繼續跟彈省去比。"

Translation: "Kimi even developed new KDA based on previous work... they wrote they were first to verify performance exceeding full attention in hybrid architectures... because Kimi internally has something called Scaling Law - you validate at one scale then continue to next scale, like levels in a game, many checkpoints, pass one level then go to next level to continue comparing with baselines."

### Evaluation Gaps Can Sink Architectures

**Insight:** Insufficient evaluation benchmarks led MiniMax to ship an architecture with critical weaknesses. Multi-hop reasoning and long-context capabilities require specific testing beyond standard benchmarks.

**Substantiation:**
Yang Songlin explains: "他們第一版的話他們監控了一些指標就是發現他們用到的Lighting Need Tension的模塊在這些指標上面表現得很好...所以他們最後就上這個Lighting Need Tension...然後後面他們發現就是如果他們在一些比方說那種叫做Motivop Reasoning就是多跳的這個Rhythm Need上面這種Tasks的話他發現這個調點會非常的大因為他們最開始沒有去檢測這種多跳推力的這個能力。"

Translation: "In their first version, they monitored some metrics and found their Linear Attention module performed well on those metrics... so they ultimately used Linear Attention... Later they discovered on tasks like multi-hop reasoning, the performance drop was very large because initially they didn't test multi-hop reasoning capability."

### Hardware Constraints Drive Better Solutions

**Insight:** Limited compute resources force algorithmic innovation that can ultimately produce superior architectures, as evidenced by China's leadership in efficient model architectures.

**Substantiation:**
Yang Songlin states: "我覺得國內的算法創新肯定是更強的主要是英特爾加購的話肯定是國內更強的我覺得這也是有一些生態地位不同就像所以它們更有動力來嘗試這些更高效的一些你量它它也生這樣的變種...像規固有些公司基本上就是卡太多了它們就難得高反正你走你走就有一定要跑得快一點對它們有算力那也能綽合跑。"

Translation: "I think domestic algorithm innovation is definitely stronger, mainly architecture innovation is stronger domestically. This is also because of different ecosystem positions, so they have more motivation to try these more efficient approaches... Some foreign companies basically have too many cards [GPUs], they don't bother to optimize, they can just run whatever. But you have to run faster [when constrained]."

### Academic Research Should Balance Principles with Practicality

**Insight:** Successful algorithm research requires both mathematical/ML soundness AND hardware efficiency awareness from the start, not hoping hardware vendors will optimize later.

**Substantiation:**
Yang Songlin argues: "我覺得模型還是肯定要結合當前硬件的結會有些人說呀那我設計一個算法它足夠好那硬件公司來幫我優化呀那怎麼可能呢那你這算法你是金質座的還是赢質座的然後硬件公司來天天幫你優化呀那是不可能的...你不論看不同類型的哈利亞它基本上都是會增存這種原則...你這些算法你可能沒必要去專門比方說針對Hallway的去優化但我覺得做算法至少要去滿足這些硬件比較通用的這種Principal。"

Translation: "I think models must definitely combine with current hardware. Some people say 'I'll design an algorithm that's good enough and hardware companies will optimize for me' - how is that possible? Is your algorithm gold or silver tier that hardware companies will optimize for you every day? That's impossible... Looking at different types of hardware, they basically all follow certain principles... You don't need to specifically optimize for one hardware, but I think algorithm design must at least satisfy these relatively universal hardware principles."

## 5. Overlooked Insights

### The "Archaeology" Research Method as Competitive Advantage

**Overlooked Insight:** Yang Songlin's systematic approach of reading ALL papers in linear attention history (back to 2016-2017) gave him unique insights that led to breakthrough work. This "archaeological" method of deeply understanding historical work is a repeatable research strategy that most researchers skip.

**Substantiation:**
Yang Songlin reveals his method: "我覺得我還是挺喜歡看最早的那些paper我覺得那些paper現在都挺好的然後我管這個叫做考股...因為我就喜歡考那些古代的paper就古代的話可能要你要一年也算古代吗因為原來現在一年前的paper叫老paper那五年前的paper那可以叫做古代的paper...像這個做到的人很少是吧對我覺得不同的人有不同的錄色是philosophy我覺得就一定要吧只有你與里面值得看的文章全部都看一遍。"

Translation: "I still really like reading the earliest papers, I think those papers are quite good now, and I call this 'archaeology'... because I like to study those ancient papers. Ancient might mean even one year ago is ancient, because now a one-year-old paper is called old, so a five-year-old paper can be called ancient... Very few people do this. I think different people have different philosophies. I think you must read all the worthwhile papers in the field."

He spent six months on this before starting his PhD: "獨PST之前花半年去調研...就之前申請完半年嘛就申請完之後有半年可以自由的時光然後當時就基本上就是在調研這種架構的這種paper然後當時獨了很多比較老的paper就比方說像德塔奈特他最早是2021年...然後當時我就在這個工作有印象。"

Translation: "Before PhD, spent half a year on research... after applications, had half a year of free time, and basically spent it researching architecture papers, read many old papers like Delta Net from 2021... and I had an impression of this work."

The competitive advantage: "因為之前的這個整個領域他把握得非常的通撤所以我知道就是如果領域大家其他其他人關心這個問題的話我應該從什麼角度去切入然後我也知道他前面工作有什麼問題...我覺得就是如果當你很清楚你要做什麼的時候你其實不會遇到什麼錯誤的就是接觸的太可愿的那種川普我覺得都是有辦法把他搞定的對我覺得更大的參議就是你不知道你要做什麼東西你不知道做什麼東西是有用的我覺得這個才是最大的參議。"

Translation: "Because I had a very thorough grasp of the entire field, I knew if others in the field care about this problem, from what angle should I approach it, and I also knew what problems previous work had... I think if you're very clear about what you want to do, you actually won't encounter major setbacks. Technical challenges are solvable. I think the bigger challenge is not knowing what to do, not knowing what's useful - that's the biggest challenge."

### Fine-Grained Decay Rates Were Known Since 2016 But Ignored

**Overlooked Insight:** The key innovation in KDA (fine-grained, per-dimension decay rates) was actually published as early as 2016, but the community ignored it for 6-8 years because the infrastructure wasn't ready. This suggests many "new" breakthroughs are actually rediscoveries of ignored historical work.

**Substantiation:**
Yang Songlin reveals: "從時間內也見上來說呢也話來說呢可能有一些技術比較時像這種系力度的這種疑望可能很多年前就有了比方說像這個系力度的這種dk至少i'mapp二年二年他可能就有一篇工作了然後最早的話我可以考古的二年一六年...但後面的話表現rein i2023年他反而用的是一個疑望數據跟數據的一個dk所以我覺得可能就是之前的技術不能更好的傳承下來吧。"

Translation: "From a timeline perspective, some techniques existed long ago. Like fine-grained decay, at least in 2022 there was work on it, and the earliest I can trace back is 2016... But later, RetNet in 2023 instead used input-independent decay. So I think previous techniques weren't well passed down."

He explains the pattern: "有一些好工作的話可能就會因為沒有follow up然後被埋摸在文現海里面呢比方說像data那這個工作我前面說他上兩年就有了然後得他入那個東西可能後面幾年就根本沒有人taggy seriously就是沒有什麼follow work...然後我有比較喜歡把所有的之前所有的技術全部重新重新審視一遍然後悬言一下我覺得最mexnc的技術來做然後可能這邊說像得他入這個技術又可以重現光芒吧對但如果如果沒有我來follow的話可能就不好說了可能可能這一套技術路線可能就會演藏在文線海里面。"

Translation: "Some good work might be buried in the literature sea due to lack of follow-up. Like Delta Rule, I mentioned it existed two years ago, but for several years basically no one took it seriously, no follow-up work... I prefer to re-examine all previous techniques and select what I think makes most sense to do. Like Delta Rule, this technique can shine again. But if I didn't follow up, it might have remained buried in the literature sea."

**Implication:** Systematically reviewing "ancient" papers (3-10 years old) in any rapidly moving field could uncover powerful techniques that failed due to poor timing or infrastructure, not fundamental limitations. This is a high-ROI research strategy that few pursue.
