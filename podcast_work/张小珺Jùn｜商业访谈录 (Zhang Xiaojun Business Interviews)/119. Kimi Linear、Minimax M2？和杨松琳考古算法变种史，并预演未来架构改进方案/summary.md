# 119. Kimi Linear、Minimax M2？和杨松琳考古算法变种史，并预演未来架构改进方案

**Podcast:** 张小珺Jùn｜商业访谈录 (Zhang Xiaojun Business Interviews)
**Date:** 2025-11-03
**Region:** Western
**Video ID:** 6908b9c80ceab2a71c48668c
**Video URL:** https://www.xiaoyuzhoufm.com/episode/6908b9c80ceab2a71c48668c
**Transcript:** [View Transcript](./transcript.md)

---

# Podcast Summary: Algorithm Innovation in Chinese AI - Linear Attention and Architecture Evolution

## 1. Key Themes

### Theme 1: China's Algorithm Innovation Leadership Driven by Compute Constraints

Chinese companies are leading in AI architecture innovation, particularly in attention mechanisms, because compute scarcity forces greater algorithmic efficiency. Yang Songlin states: **"I believe domestic algorithm innovation is definitely stronger... China doesn't have as many GPUs, so their requirements for efficiency are higher, giving them more motivation to try these more efficient linear attention variants."** [01:07:39]

The compute constraint paradox is creating a competitive advantage: **"Countries with fewer resources must optimize algorithms more aggressively, while US companies with abundant compute can afford to be less innovative."** [01:08:27]

### Theme 2: The Evolution from Full Attention to Hybrid Architectures

The industry is converging on hybrid attention architectures mixing linear and full attention layers, with 3:1 ratios becoming standard. **"Like Kimi uses 3:1, then later Qwen 3 also uses 3:1 with Gate Delta. This solution should be relatively optimal across different scales."** [00:44:50]

Different companies are exploring divergent paths:
- **Kimi**: 100% hybrid (3 linear layers + 1 full attention layer)
- **DeepSeek**: Sparse attention (every layer full attention with sparse selection)
- **MiniMax**: Reverted from 7:1 linear-to-full back to 100% full attention after discovering multi-hop reasoning deficits

Yang explains the MiniMax reversal: **"They found that on multi-hop reasoning tasks in long contexts, the performance drop was very large... They temporarily retreated back to full Softmax attention architecture."** [00:45:20]

### Theme 3: Hardware-Algorithm Co-Design as the Future Bottleneck

Transformer's dominance stems from hardware compatibility, not theoretical superiority. **"Transformer is the heaven-chosen architecture for this generation of hardware... it's designed to make hardware fast. Even though it has quadratic complexity, it can leverage matrix multiplication to achieve optimal ops, so its hardware efficiency is much better than RNN."** [01:32:01]

The next breakthrough requires: **"You must design algorithms that can use matrix multiplication operations, otherwise your hardware efficiency definitely cannot keep up... Linear attention has a good advantage - it's basically all matrix multiplication operations."** [01:37:00]

## 2. Contrarian Perspectives

### Perspective 1: Pure Linear Attention is Fundamentally Broken

**"I think the consensus in the architecture design is that pure linear attention doesn't work. It has some fatal flaws under long context."** [00:38:22] This contradicts the prevailing research excitement around linear attention, with Yang stating categorically that **"hybrid attention is what many places are paying attention to, though I don't know if it's consensus because different places are still trying different approaches."** [00:41:07]

Supporting evidence: MiniMax's reversion from linear to full attention after discovering **"very large drops on multi-hop reasoning tasks"** demonstrates real-world failure modes that benchmarks missed. [00:45:20]

### Perspective 2: Sparse Attention and Linear Attention Are Not Competitors

**"I think linear attention and sparse attention actually don't have a competitive relationship. Linear attention's competitor is probably more like sliding window or full attention."** [00:50:51]

Yang proposes an unconventional synthesis: **"Why can't we combine these two approaches? For example, we could let sparse attention replace the global attention layers in hybrid attention architectures... We could still save a lot of KV cache through the linear attention layers."** [00:50:53] This suggests the field is pursuing false dichotomies when integration may be optimal.

### Perspective 3: Algorithm Archaeology Over Novel Research

Yang's research philosophy contradicts standard academic practice: **"I really like reading the earliest papers... I call this archaeology. I like to dig up ancient papers - papers from one year ago count as old, papers from five years ago can be called ancient."** [01:18:30]

His method: **"I basically read every paper worth reading in this field... This is something very few people do."** [01:21:11] He discovered that **"many historical algorithms are actually very advanced, but at the time people might not have recognized the value of the work"** [01:13:58], citing Delta Rule from 2021 that remained dormant until hardware efficiency became critical.

### Perspective 4: Data Scaling Hits Are Positive for Research

Counter to industry pessimism about data walls, Yang sees opportunity: **"Before, when data could always scale, talking about data efficiency didn't have much use... Everyone just kept adding data. Now if there's a data wall and compute wall, then ultimately we have to return to algorithms - the fundamental things."** [01:01:54]

He notes OpenAI's CTO agrees: **"At this inflection point, the importance of algorithm research may be elevated again."** [01:02:42]

### Perspective 5: Hardware Determines Algorithm Success, Not Theory

**"If you design an algorithm that cannot use matrix multiplication, it has no practical value - you're just entertaining yourself."** [01:36:38] This directly contradicts theoretical CS research that prioritizes asymptotic complexity.

Evidence: **"Even though Transformer has higher theoretical complexity, people would rather use it than LSTM with lower theoretical complexity, because their hardware efficiency performance is better."** [01:32:55] The implication: **"You must satisfy some very general principles for hardware... like principles of memory hierarchy. Algorithm design may not need to specifically target a particular hardware, but you must meet these general hardware-efficient principles."** [01:35:12]

## 3. Companies Identified

### Kimi (Moonshot AI)
**Description**: Developed Kimi Linear model using KDA (Kimi Delta Attention) mechanism, pioneering 3:1 hybrid architecture
**Quotes**: 
- **"Kimi felt that if we use full quadratic attention at every layer, decoding becomes too expensive... This requires investing resources to explore this hybrid attention."** [00:12:58]
- **"They should have started wanting to do this at the beginning of the year... because like DeepSeek R1 and Kimi 1.5 had just been released then, and its core does RL to get very long chains of thought... these chains of thought can often reach tens of thousands of tokens. Kimi felt that decoding cost would be too high."** [00:12:45]

### DeepSeek
**Description**: Pursuing sparse attention approach rather than hybrid linear attention
**Quotes**:
- **"DeepSeek's approach is they really like going the sparse sequence route... They think sparsity is a better way to reduce decoding cost."** [00:21:05]
- **"I think DeepSeek is a company that pays very close attention to hardware and algorithm co-design... Their sparse attention uses an IndexNet with FP8 to compute attention, because it doesn't need Softmax, only needs to select top-k by logit scores."** [01:40:37]

### MiniMax
**Description**: Attempted linear attention with M1, reverted to full attention with M2 after discovering reasoning deficits
**Quotes**:
- **"MiniMax's previous version used a 7:1 ratio... Their first version, they monitored some metrics and found the Lightning Attention module performed well on these metrics... but later they found on multi-hop reasoning tasks, the drop was very large."** [00:45:20]
- **"Their evaluation pipeline wasn't comprehensive enough initially, so they used a relatively weak solution of 7:1. Now everyone has basically returned to 3:1."** [00:42:00]

### Qwen (Alibaba)
**Description**: Following similar 3:1 hybrid architecture path
**Quotes**:
- **"Qwen 3 Nex also uses 3:1 Gate Delta, this solution should be relatively optimal."** [00:44:50]

### Meta
**Description**: Exploring extreme cubic complexity attention mechanisms
**Quotes**:
- **"I saw Meta released a paper making cubic complexity attention... Quadratic complexity isn't enough, they want cubic."** [00:44:06]

### OpenAI
**Description**: Consistently used hybrid architectures since GPT-3
**Quotes**:
- **"Like GPT-3, in their technical report they said they would use a hybrid global attention and local sliding window attention."** [00:27:39]
- **"They should have been consistently using this hybrid attention approach."** [00:27:57]

## 4. Operating Insights

### Insight 1: Scaling Laws for Architecture Validation

Kimi implements a **"scaling light"** system: **"At a certain scale, if your performance is good, then you can scale up to the next level to continue... It's like clearing levels, with many checkpoints. After passing one level, you go to the next to continue competing with the full Softmax baseline."** [00:19:19]

This staged validation prevents expensive failures at large scales and provides early kill signals for unproductive directions.

### Insight 2: The 3:1 Architecture Ratio as Discovered Optimum

Through systematic experimentation, the field has converged on 3:1 linear-to-full attention ratio: **"I remember previously Jina AI also published a paper studying this hybrid architecture, what percentage of layers need to be Softmax attention. Their conclusion from pretraining scaling experiments was that 3:1 ratio is best, and Gate Delta outperforms other modules."** [00:44:08]

This represents an empirically-discovered scaling law for hybrid architectures.

### Insight 3: Evaluation Pipelines Determine Architecture Success

MiniMax's failure stemmed from incomplete benchmarks: **"They didn't test multi-hop reasoning ability initially, they mainly looked at things like MMLU... So they selected a relatively weak linear attention approach. Later they found it wasn't good enough."** [00:45:50]

The lesson: **"Comprehensive evaluation across diverse task types (especially multi-hop reasoning, long-context, coding) is essential before committing to architecture choices."**

### Insight 4: Open Source Drives Infrastructure Support

**"Because these model companies do some promising results, then open source them, then those people making inference engines have lots of motivation to figure out how to support these things."** [01:06:51]

Yang identifies a virtuous cycle: **"When infrastructure support gets better, other companies who previously thought linear attention ecosystem was too poor - even if we develop it, deployment costs would be high - will now find that once this ecosystem is built up, there's a positive feedback effect."** [01:07:00]

## 5. Overlooked Insights

### Insight 1: The Delta Rule's 3-Year Hibernation Reveals Timing Dependence

Yang casually mentions: **"Delta Rule was proposed in 2021... but for the next few years it wasn't taken seriously, there weren't many follow-up works."** [01:14:08] He traces it even further: **"The earliest I can dig up, 2016 had works with input-dependent decay."** [01:25:55]

**Why this matters enormously**: This suggests breakthrough architecture components can exist for 3-7 years before conditions allow recognition. The implication: **systematic archaeology of "failed" papers from 2016-2021 could yield multiple ready-to-deploy innovations** that were simply ahead of hardware/data conditions. Yang's success with Gate Delta Attention came from **"reading all papers worth reading in this field"** [01:21:11] - a practice he notes **"very few people do."** This represents a massive strategic arbitrage opportunity for researchers willing to do comprehensive literature archaeology.

### Insight 2: FP8 Inference Through Architecture-Hardware Co-Design

Buried in Yang's explanation of DeepSeek: **"DeepSeek sparse attention has an IndexNet that uses FP8 to compute attention, because it doesn't need Softmax, only needs raw logits to select top-k, so first it's FP8, second it can remove the expensive exponential operation... so it's basically all matrix multiplication and they added dedicated hardware for this."** [01:40:37]

**Why this is seismic**: This isn't just quantization - it's **eliminating entire operation classes (exp/softmax) at the architecture level to enable lower precision.** The typical approach treats quantization as post-hoc compression; DeepSeek co-designed architecture and numeric precision from inception. This suggests: **future architectures should be designed with target precision in mind from day one**, not as an afterthought. The **8-bit transformer may require fundamentally different operations than 16-bit**, creating first-mover advantages for companies willing to rethink basic building blocks for specific hardware capabilities.

---

**Note on Translation**: All quotes translated from original Chinese podcast to English while preserving technical accuracy and speaker intent.