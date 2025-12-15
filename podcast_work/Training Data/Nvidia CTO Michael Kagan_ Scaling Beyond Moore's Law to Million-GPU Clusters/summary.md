# [Nvidia CTO Michael Kagan: Scaling Beyond Moore's Law to Million-GPU Clusters](https://www.youtube.com/watch?v=H9JjlTA2Il8)

**Podcast:** Training Data
**Date:** 2025-10-29
**Participants:** Unknown Host, Unknown Host, Michael Kagan
**Region:** Western
**Video ID:** H9JjlTA2Il8
**Video URL:** https://www.youtube.com/watch?v=H9JjlTA2Il8
**Transcript:** [View Transcript](./transcript.md)

---

# [Default Summarization Prompt - NVIDIA CTO Michael Kagan Interview](https://www.youtube.com/watch?v=H9JjlTA2Il8)

## 1. Key Themes

### **Network Infrastructure as the Critical Enabler of AI Scale**

The acquisition of Mellanox was transformational because it enabled NVIDIA to think beyond single chips to entire data centers as single computing units. Michael explains: "If you order just GPU on Amazon, just don't wonder that you will show up this huge rack... People think chip, but it's really a system... That's just one GPU." The network became critical because AI model requirements grew at 10-16X per year (models doubling every 3 months), far exceeding Moore's Law's 2X every two years. 

Michael Kagan elaborates on why this matters: "When you tune your application, you tune your application so that communication can be hidden behind computation. And it means that if communication for some reason gets longer, then everybody waits." The key differentiator isn't raw bandwidth but **latency consistency**: "You go to the hero numbers, sending bit from one place to another, it's basically physics... But when you do it thousands of times, and it takes the same time to do it, versus very wide distribution of other technologies, then machine becomes less efficient. So instead of being able to split your job to 1000 GPUs, you can split it only to 10 GPUs."

### **The Exponential Shift from Training to Inference Computing Demand**

Contrary to conventional wisdom, inference now demands equal or greater compute than training. Michael explains: "Till recently it was a main driver of the compute... the inference or AI was mainly perceptual. So you show the picture, that's a dog... Then came became a generative AI, where actually you get the recursive generation... for every token, when you generate text, generate picture, for every new token, you need to go through the entire machine all over again."

He adds: "Now there is a reasoning, which means the machine starts... thinking. If you ask me what time is it now, I can tell you, it's easy, right? But if you ask me more complicated question, then I need to think... And every such a thing is inference." The key insight: "You train model once, but you infer many times... chat GPT... billion of people... are pounding them all the time. It's the same model." This fundamentally changes data center economics and architecture requirements.

### **Building for Inevitable Failure at 100K+ GPU Scale**

At massive scale, the assumption that hardware works 99.99% of the time becomes a fatal design flaw. Michael states: "If you are building 100,000 component machine... in terms of components, there is millions of them. The chance that everything works is zero. So something is definitely broken. And you need to design it both from hardware and from software perspective to keep going, to keep going as efficient as you can."

This represents a fundamental shift in systems architecture - from assuming reliability to designing for continuous partial failure while maintaining performance and power efficiency. The challenge starts "at few tens of thousands" of GPUs, not at the million-GPU scale people imagine.

## 2. Contrarian Perspectives

### **Programmability Trumps Hardware Optimization for Inference**

While the industry rushes to build specialized inference chips, Michael argues: "As long as you don't identify and I don't think, besides... it's very similar GPU. It's same programming model as the GPU for pre-fill versus decode... if your workload shifts for more decode or for more pre-fill, you can use either one of them to compensate. And this is the importance of programmability."

NVIDIA's approach is to create GPU variants optimized for pre-fill vs decode phases, but maintain the same CUDA programming interface. This allows flexibility as workloads shift, whereas custom ASICs lock you into specific use cases. The experience backing this: "The same interfaces for GPUs, it's based on code and the end up, which is, that's what made Nvidia."

### **Win-Win Over Zero-Sum Competition**

Michael describes NVIDIA's culture: "We are not after taking a bigger piece of existing pie. We are after making our bigger pie for everybody. And the success, our success is our customer success. It's not our success is not the failure of our competition." 

This explains the Intel partnership: "Fusing together conventional computing, one human machines and accelerated computing... it basically gives Nvidia and Intel channels to the market or expanding the market and serving the markets that otherwise was more challenging." This is contrarian because most tech companies view partnerships with competitors as weakness, but NVIDIA views it as market expansion that benefits everyone.

### **Bigger Buffers Are Not Better in Networks**

Contradicting traditional networking wisdom that uses large buffers for congestion management, Michael states: "Huge buffer is not good. You know, some bigger is not better... these devices are basically to isolate the external world from the internals. But when you want to run a single workload across data centers that are distant by kilometers, you need to be every machine on one side to be aware, what, whom does it communicate to whether it's short communication, long communication and adjust all the communication patterns accordingly. So you don't need these big buffers because big buffers is a jitter."

This led to Spectrum X technology that provides telemetry for endpoints to adjust for congestion without massive buffers, fundamentally different from traditional telco approaches.

## 3. Companies Identified

### **Mellanox (acquired by NVIDIA)**
**Description:** Networking technology company co-founded by Michael Kagan, acquired by NVIDIA for $7 billion in March 2019, providing critical interconnect technology for AI data centers.

**Quotes:** 
- "I do agree that this merger of Melonox and Nvidia... I don't think that networking business of now it's Nvidia, the previous Melonox could have been growing that significantly... I think we are the fastest growing internet business."
- "We announced that we're actually going to build a campus in Israel, New Campus for Nvidia... 85 or 90% of original employees state actually Nvidia grew more than two X in Israel... it's considered to be the most successful merger in the history of the technology."

### **Intel**
**Description:** Traditional CPU manufacturer partnering with NVIDIA to fuse general-purpose and accelerated computing.

**Quotes:**
- "Our partnership with Intel is actually fusing accelerated computing with the general purpose computing because general purpose computing is not going away."
- "X-R-E-Six is the architecture that is dominant there and you know it would serve greatly both companies."

### **XAI**
**Description:** AI company (presumably xAI by Elon Musk) operating large-scale data centers.

**Quotes:**
- "Last big data center, which is like XAI scale is 150 megawatt. Now we're talking about gigawatt data centers, people talking about 10 gigawatt data centers."

### **ChatGPT/OpenAI**
**Description:** Leading generative AI service demonstrating massive inference demand.

**Quotes:**
- "Chat GPT... billion of people, or it's almost billion of people, right? There's customers that are pounding them all the time. It's the same model. They trained it once."
- "My wife, I think she talks to chat GPT more than to me. Once she discovers that's her best friend."

## 4. Operating Insights

### **Product Cadence as Competitive Moat**

Michael reveals a deliberate acceleration: "Since about two or three years ago we accelerated our product introduction from every other year to every year. Now we introduce a new wave of products every year and it's order of magnitude higher performance... it's not on the chip level performance it's on machine that you can build with this performance." This creates a 10X annual improvement vs Moore's Law's 2X every two years, making it nearly impossible for competitors to catch up.

### **Design for the System, Not the Component**

The critical operating principle: "We look at this data center as basically single unit of computing... you start architecting your components, your software and your hardware at the point where this is the data center, this is 100,000 GPUs that we want to make them work together." This systems-level thinking from day one prevents the common trap of optimizing individual components that don't scale efficiently together.

### **Post-Acquisition Integration Through Technology and Culture**

Michael's shower thoughts post-acquisition: "My main focus at the beginning... was how to make sure that this acquisition will succeed... Nvidia paid seven billion dollars for company that I founded... once it's done it's done now I have to make it successful." The result: 85-90% employee retention and 2X headcount growth in Israel. The key was ensuring Israeli employees "don't feel left somewhere in the faraway" and Jensen "emphasizes the networking as the critical part of Melanox an