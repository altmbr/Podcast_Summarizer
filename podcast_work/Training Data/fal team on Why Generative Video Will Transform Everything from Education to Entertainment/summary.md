# [fal team on Why Generative Video Will Transform Everything from Education to Entertainment](https://www.youtube.com/watch?v=s_IIjGamN3Y)

**Podcast:** Training Data
**Date:** 2025-12-10
**Participants:** Unknown Guest, Unknown Guest, George Robson, Unknown Guest
**Region:** Western
**Video ID:** s_IIjGamN3Y
**Video URL:** https://www.youtube.com/watch?v=s_IIjGamN3Y
**Transcript:** [View Transcript](./transcript.md)

---

# Podcast Summary: Fall - Generative Video Infrastructure Platform

## 1. Key Themes

### The Overlooked Opportunity in Generative Media Infrastructure

Generative media (image and video) was initially overlooked as an AI market for two key reasons: lack of clear industry use cases and slower research investment compared to LLMs. The market felt like "a toy use case" three years ago, but the team recognized the opportunity early. As one speaker explained: "everyone was over indexed on language models. This like story of AGI was being told and that attracted all the dollars, that attracted all the talent. So everyone was just like working on that where we thought like we had something niche, like growing fast, you know, don't tell anyone" [[00:04:06]](https://www.youtube.com/watch?v=s_IIjGamN3Y&t=3m56s). This early contrarian bet, combined with superior technical execution on inference optimization, positioned Fall uniquely in what has become a massive and rapidly expanding market.

### Video Models Require Fundamentally Different Infrastructure Than LLMs

The technical optimization challenges for video models differ fundamentally from LLMs. While LLMs are memory-bandwidth constrained (moving massive weights from memory), diffusion models are compute-bound because they denoise thousands of tokens simultaneously. "In diffusion models, you're trying to denoise like thousands, tens of thousands of tokens for a video at the same time doing attention of it. So you're essentially saturating all the compute bandwidth of these GPUs" [[00:09:42]](https://www.youtube.com/watch?v=s_IIjGamN3Y&t=9m32s). A standard LLM prompt takes "one X" of compute, an image takes 100X, and a five-second 24fps video takes 10,000X compared to LLMs - with 4K adding another 10X multiplier [[00:18:22]](https://www.youtube.com/watch?v=s_IIjGamN3Y&t=18m12s). This computational intensity requires specialized kernel optimization, distributed computing across 35+ heterogeneous data centers, and what they call "distributed super-computing" architecture [[00:14:21]](https://www.youtube.com/watch?v=s_IIjGamN3Y&t=14m11s).

### The Long Tail of Models Creates Persistent Competitive Advantage

Unlike LLMs where a few dominant models prevail, generative media has an extraordinarily diverse and rapidly changing model ecosystem. Fall's top 100 customers use an average of 14 different models simultaneously [[00:36:42]](https://www.youtube.com/watch?v=s_IIjGamN3Y&t=36m32s), and the top 5 models have a half-life of just 30 days [[00:27:02]](https://www.youtube.com/watch?v=s_IIjGamN3Y&t=26m52s). This happens because specialized models excel at different tasks (upscaling, editing, text generation, VFX) and because visual output differences are immediately perceptible unlike text. As explained: "in the visual domain, ecosystem actually matters more... any small adjustment you make to the model, it can actually have huge implications" [[00:34:13]](https://www.youtube.com/watch?v=s_IIjGamN3Y&t=34m3s). This creates a structural moat: Fall must run 600+ models simultaneously while optimizing each better than labs running single models - requiring both their inference engine expertise and sophisticated infrastructure for routing, caching, and model management across their distributed fleet.

## 2. Contrarian Perspectives

### Omnimodels Won't Dominate - Specialized Models Will Persist

Three years ago, the consensus view post-ChatGPT was that "omnimodels" would emerge - giant models generating video, audio, image, code, and text. Fall bet against this, believing specialized models would persist. "Everyone, like, that's one feedback we got, or there's gonna be omnimodels and there's gonna be a single way of running these. It's gonna be hard to create an edge on the modality, but turns out it's not true, and it actually makes sense to have a technical edge on the modality" [[00:52:51]](https://www.youtube.com/watch?v=s_IIjGamN3Y&t=52m41s). This proved correct: the best upscaling model only does upscaling, the best image editing model differs from text-to-image models, and even within categories, different model "personas" serve different creative needs. The visual domain's subjectivity and the importance of precise aesthetic control drives this specialization in ways that never materialized for text models.

### Open Source Will Thrive in Media Models Unlike LLMs

While open-source LLMs struggle to compete with frontier closed models, Fall believes open source will remain vibrant in generative media. The ecosystem dynamics differ fundamentally: "When the developers are training loras, they are building adapters, they are building on top of your model. It really brings free marketing, but also creates stickiness" [[00:32:48]](https://www.youtube.com/watch?v=s_IIjGamN3Y&t=32m38s). Visual outputs make fine-tuning differences immediately apparent, unlike LLMs where "you can't tell the difference" [[00:33:47]](https://www.youtube.com/watch?v=s_IIjGamN3Y&t=33m37s). Professional creators demand control over aesthetics that requires model customization - "a customer support chatbot does not need personality... But you are talking about filmmakers, marketing teams. They all want to add the personality of their style or their brand" [[00:36:01]](https://www.youtube.com/watch?v=s_IIjGamN3Y&t=35m51s). This fundamental difference in how visual versus text models are used ensures continued open-source vitality, starting with Stable Diffusion and continuing through Black Forest Labs' strategy.

### Hollywood Will Adapt and Remain Relevant (Not Get Disrupted)

Six months ago, Fall believed AI-native studios would overtake Hollywood, which would be "too slow" and "left behind" [[00:47:11]](https://www.youtube.com/watch?v=s_IIjGamN3Y&t=47m1s). This summer their view changed dramatically after engaging with traditional media. Jeffrey Katzenberg drew a parallel to computer animation's adoption: "this is exactly playing out how animation. When it first came out, people revolted against it. It was all hand-drawn before that and computer graphics. It was new and there was a lot of rebellion against computer-driven animation... But there's no way of stopping technology. It's just going to happen. You're either going to be part of it or not" [[00:00:09]](https://www.youtube.com/watch?v=s_IIjGamN3Y&t=0s). Hollywood possesses three durable advantages: existing IP, storytelling/filmmaking expertise, and access to capital for what remains an expensive production process. "We need these deeply technical people who know filmmaking, who has the IP, who know storytelling to actually in the beginning be part of this" [[00:48:42]](https://www.youtube.com/watch?v=s_IIjGamN3Y&t=48m32s). Rather than being disrupted, incumbent studios are positioning to leverage AI while maintaining their core advantages.

## 3. Companies Identified

**Black Forest Labs** - AI image model company (creators of Flux), former Stability AI team. Mentioned for pioneering open-source strategy in generative media, understanding that ecosystem development drives adoption and stickiness. "They first open source stable diffusion and got insane adoption. And almost the same team then started Black Forest Labs and they knew the power of open source" [[00:32:23]](https://www.youtube.com/watch?v=s_IIjGamN3Y&t=32m13s).

**OpenAI (Sora)** - AI research lab, creator of Sora video model. Mentioned as a Fall partner providing day-zero launch access, and for their strategic positioning around personal/social use cases. "Sora really made it about friends, like Cameo... And now you can cameo your pets" [[00:51:08]](https://www.youtube.com/watch?v=s_IIjGamN3Y&t=50m58s), creating better reception than competitors by emphasizing human connection over "slop machine" perception.

**Google DeepMind (Vio)** - AI research division, creator of Vio video model. Mentioned as Fall partner and for demonstrating that resource deployment matters more than novel innovation in current phase: "Google showed this with like their models and how quickly they were able to catch up. They didn't need to innovate that much. It's just like they have the resources they can put more more effort into it" [[00:59:10]](https://www.youtube.com/watch?v=s_IIjGamN3Y&t=59m0s).

**Shopify** - E-commerce platform company. Mentioned for collaborating with Fall on building no-code workflow builder, enabling non-technical team members (PMs, marketing) to experiment with generative media models before productionizing them [[00:37:15]](https://www.youtube.com/watch?v=s_IIjGamN3Y&t=37m5s).

**Canva** - Design and productivity platform. Mentioned as public customer integrating Fall's generative media models into their existing design tooling, representing the "design and productivity" category of Fall's customer base [[00:44:27]](https://www.youtube.com/watch?v=s_IIjGamN3Y&t=44m17s).

**Adobe** - Creative software company. Mentioned alongside Canva as Fall customer integrating generative media into established creative tools, representing traditional design software embracing AI capabilities [[00:44:29]](https://www.youtube.com/watch?v=s_IIjGamN3Y&t=44m19s).

**Faith (Bible App)** - AI-native media application. Mentioned as one of the highest-ranked apps on the App Store, creating generative video stories for each Bible story. "They have like stories for each of the stories from the Bible. And they're like really well produced" [[00:43:46]](https://www.youtube.com/watch?v=s_IIjGamN3Y&t=43m36s), representing the "AI native studios" category and demonstrating educational/religious content as emerging use case.

**Adaptive Security** - Security training company (Brian Long's company). Mentioned for innovative use case generating dynamic security training content on the fly with personalized curriculum. "The trainings are generated on the fly. And the content is all dynamic... the content you get, you know, per person is all dynamic" [[00:43:00]](https://www.youtube.com/watch?v=s_IIjGamN3Y&t=42m50s), representing how generative media enables personalization in corporate training.

**Mid-journey** - AI image generation company. Mentioned for strategic positioning evolution from photorealism pioneer to artistic/artsy aesthetic focus. "They kind of brought this like photorealism, which was, you know, that was like a very big deal at the time... And then now they are more like this artsy model" [[00:28:29]](https://www.youtube.com/watch?v=s_IIjGamN3Y&t=28m19s), demonstrating successful navigation of changing market dynamics and finding defensible niche.

## 4. People Identified

**Jeffrey Katzenberg** - Former CEO of DreamWorks. Mentioned for speaking at Fall's first generative media conference and drawing the parallel between AI adoption resistance and the historical resistance to computer animation versus hand-drawn animation. His perspective validated that technological adoption follows predictable patterns and that resistance is futile: "there's no way of stopping technology. It's just going to happen. You're either going to be part of it or not" [[00:00:29]](https://www.youtube.com/watch?v=s_IIjGamN3Y&t=19s).

**Andrej Karpathy** - AI researcher (former Tesla/OpenAI). Referenced for his tweet about excitement around media models and their educational potential, emphasizing that humans are visual learners and that video can compress concepts more effectively than "wall of text." "He was saying like, he wasn't making a point around like education. And a lot of the like content you consume just to like like learn things" [[00:05:16]](https://www.youtube.com/watch?v=s_IIjGamN3Y&t=5m6s), highlighting the transformative potential of video models for learning.

**David Holtz** - CEO of Mid-journey. Referenced for his philosophy on "curating the aesthetic space with mid-journey" [[00:34:34]](https://www.youtube.com/watch?v=s_IIjGamN3Y&t=34m24s), representing the strategic insight that in generative media, taste and aesthetic curation become increasingly valuable as generation capabilities commoditize.

**PJ A's** (PJ Accetturo) - Content creator and Fall user. Mentioned as one of Fall's favorite creators who shares workflows online and demonstrates how workflows constantly evolve with new model releases. "Every time like he posts things, you know, every month, he actually has like a different kind of workflow. It's really driven by like the new models" [[00:39:47]](https://www.youtube.com/watch?v=s_IIjGamN3Y&t=39m37s), illustrating the dynamic and experimental nature of professional generative media workflows.

## 5. Operating Insights

### Focus Wins the Infrastructure Performance Race

Fall maintains the #1 position on all performance benchmarks not through unique technical approaches, but through singular focus. "I don't think anyone cares about it as much as us. We are literally obsessed with giants in media... everyone is like super obsessed with language models. Everyone is trying to get like one more tokens per second on like deep seek benchmarks, whatever. And like we are like on a different lane" [[00:11:25]](https://www.youtube.com/watch?v=s_IIjGamN3Y&t=11m15s). The technical ceiling is the same hardware for everyone - but Fall stays 3-6 months ahead through pure dedication. When they benchmark PyTorch's latest version against their year-old inference engine, PyTorch has caught up, proving the advantage is temporal, not permanent. The lesson: in competitive technical races, sustained focus on a specific domain beats distributed attention every time.

### Build Marketing Machine as Distribution Moat for Two-Sided Marketplace

Fall's exclusive launch partnerships with model providers (Kling, Minimax, Sora, Vio) stem from their "robust marketing machine" creating a flywheel between developers and model labs. "Every time we release something, this creates another opportunity for us to introduce a new capability, introduce a new model. And model developers also see that and we usually do call marketing together" [[00:31:17]](https://www.youtube.com/watch?v=s_IIjGamN3Y&t=31m7s). This co-marketing creates exclusive access periods, sometimes permanently. The insight: in marketplace businesses, marketing isn't just customer acquisition - it's the mechanism that creates supply-side exclusivity by demonstrating distribution value to partners. Model labs want the "biggest platform" [[00:31:52]](https://www.youtube.com/watch?v=s_IIjGamN3Y&t=31m42s), and visible marketing proves that scale.

### Design for Model Diversity from Day One

Fall's core architectural decision was building a "tracing compiler that traces the execution" with templated kernels rather than optimizing single models. "We didn't want to go optimize a single model, put our eggs into a single basket and then go became invalidated when the next model comes" [[00:08:12]](https://www.youtube.com/watch?v=s_IIjGamN3Y&t=8m2s). This proved prescient: they now run 600+ models simultaneously, each optimized better than if labs ran them individually, while models turn over every 30 days. The insight: in rapidly evolving technical domains, over-indexing on current state-of-the-art creates technical debt. Building flexible abstractions that can adapt to unknown futures wins over point optimizations.

### Tap Heterogeneous Capacity in Scarce Resource Markets

With GPU scarcity, Fall built "distributed super-computing" across 35+ heterogeneous data centers with different specs and networking, scheduling workloads "as if it's a homogeneous cluster" [[00:14:44]](https://www.youtube.com/watch?v=s_IIjGamN3Y&t=14m34s). This required building custom orchestrators, CDNs, and routing infrastructure. "We can tap into capacity wherever it is" [[00:15:04]](https://www.youtube.com/watch?v=s_IIjGamN3Y&t=14m54s) while hyperscalers remain constrained by traditional data center patterns. The insight: in supply-constrained markets, winners build infrastructure to aggregate fragmented capacity rather than waiting for centralized supply. This is increasingly relevant as even hyperscalers now buy from "new clouts" [[00:16:14]](https://www.youtube.com/watch?v=s_IIjGamN3Y&t=16m4s).

## 6. Overlooked Insights

### The Security Training Wedge Hints at Corporate Learning Revolution

Buried in the use case discussion was Adaptive Security's approach to corporate training: generating dynamic security training content personalized per employee, with curriculum adapting on the fly [[00:42:57]](https://www.youtube.com/watch?v=s_IIjGamN3Y&t=42m47s). This represents a massive overlooked opportunity - corporate training is a $370B+ market that's remained largely static despite being universally acknowledged as ineffective. The breakthrough isn't just personalization (which LLMs enable), but that video generation makes training *engaging* in ways text never could. If this works for security training, it works for compliance, onboarding, technical training, and sales enablement across every enterprise. Yet this was mentioned as an afterthought "long tail" use case rather than a primary market opportunity, suggesting the team (and market) may be underweighting the enterprise training transformation that generative video enables.

### Programmatic Personalized Video Ads Could Eclipse UGC and Professional Ads

While discussing ads as a major use case, one comment was particularly revealing: "what we're excited about is also like programmatic ads, right? So where you can do personalized, you know, to the degree of like, like, literally individuals, you know, yourself being the ad or in the movies, whatever" [[00:45:17]](https://www.youtube.com/watch?v=s_IIjGamN3Y&t=45m7s). This was mentioned almost in passing, but represents a potential paradigm shift in digital advertising. Current personalization stops at targeting and copy - but personalized video content (where you're literally the protagonist, or products are styled for your aesthetic) could transform conversion rates and CPMs. If video generation costs drop 100-1000x through infrastructure improvements Fall is building, the economics of individualized video ads become viable. This could be larger than the UGC creator economy they discussed extensively, yet received one sentence. The buried lede suggests even the builders underestimate how their cost reductions enable entirely new ad formats and economics.