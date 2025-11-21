# [Stanford AI Club: Guillermo Rauch on Building the AI Cloud](https://www.youtube.com/watch?v=Uac2ZCpuU2Y)

**Podcast:** Stanford AI Speaker Series
**Date:** 2025-11-21
**Participants:** Guillermo Rauch
**Region:** Western
**Video ID:** Uac2ZCpuU2Y
**Video URL:** https://www.youtube.com/watch?v=Uac2ZCpuU2Y
**Transcript:** [View Transcript](./transcript.md)

---

# Podcast Summary: Guillermo Rauch on Vercel's AI Cloud Vision

## 1. Key Themes

### The Fundamental Shift from Pages to Agents

The web is experiencing a fundamental architectural transformation where static or semi-static pages defined by engineers are giving way to agent-driven, dynamically generated experiences. This represents a complete reimagining of how humans interact with computers and consume information.

**Substantiation:** Guillermo Rauch explained: "We're just riffing on an idea of what would it look like if ChatGPT was behind every page render that happens on the internet? Today, the way that this page is going to create it is engineers go out and define a bunch of react render functions. They bring in a lot of data. It's kind of like deterministic, right? A lot of what I think people actually need in order to solve problems is not to consume UI and interact with the UI directly. A lot will happen in the foreground, and a lot will happen through conversational interfaces instead of generic UIs." [[00:05:50]](https://www.youtube.com/watch?v=Uac2ZCpuU2Y&t=5m40s)

### Building the AI Cloud: Infrastructure for a New Computing Paradigm

Vercel is pivoting from being a traditional cloud platform to becoming what they call the "AI Cloud" - infrastructure specifically designed for AI applications with fundamentally different characteristics than traditional web applications. This includes rethinking compute pricing, execution models, and developer experience.

**Substantiation:** Rauch stated: "Our latest new idea and our focus for the foreseeable future will be in building what we call the AI cloud. When Vercel was started, the main problem that I was scratching is I saw a huge amount of potential in cloud computing, but it was broadly inaccessible. We see a similar opportunity with AI because if you have an idea for the next big assistant agent or AI application, there's significant friction and bringing that to reality." [[00:03:11]](https://www.youtube.com/watch?v=Uac2ZCpuU2Y&t=3m1s)

### From Speed to Correctness: A Computational Value Shift

The core metric of success in computing is shifting from minimizing latency (the 100ms response time optimization of the traditional web) to maximizing correctness and quality of response, even if it takes significantly longer. This represents a fundamental reorientation of cloud infrastructure priorities.

**Substantiation:** Rauch explained: "When AWS first came out, a lot of what the cloud was looking to solve was you go to Amazon.com, you want to respond to 100 milliseconds. 100 milliseconds of latency has an impacting conversion, speed is king, right? And as we evolved towards this AI cloud, I think we're going to see a shift towards, well, it's not so important anymore than computation happens instantaneously. What actually matters more is that you get the right response. We see this all the time when, for example, you use ChatGPT and you say, GPT-5 Pro mode. You don't care so much that you get an answer instantaneously. As long as you get some feedback over time, so you get a stream of token, so you get a stream of reasoning traces, et cetera, as long as you get the right answer of that right solution that you were after, you're happy." [[00:06:37]](https://www.youtube.com/watch?v=Uac2ZCpuU2Y&t=6m27s)

## 2. Contrarian Perspectives

### Observability as Bad News: The Problem-Solution Inversion

The entire multi-billion dollar observability market is fundamentally misaligned with where computing should be headed because it focuses on delivering problems to humans rather than solutions. This is a direct challenge to companies like Datadog and New Relic whose business models depend on human operators monitoring dashboards.

**Substantiation:** Rauch argued: "A lot of companies in the cloud infrastructure space, even public ones are, for example, predicated on the idea of observability. There's a huge market of observability that basically all it gives you is mostly bad news of the kind of, here's a chart of how your latency has gotten worse. Here's a chart of errors over time... Our goal is to switch to a world of complete autonomy, where the cloud offers you solutions or other problems." [[00:11:24]](https://www.youtube.com/watch?v=Uac2ZCpuU2Y&t=11m14s) He went on to describe their solution: "Whenever something bad happens at runtime, whether it's the US East to one meltdown that happened the other day, it should result in actionable solutions." [[00:12:16]](https://www.youtube.com/watch?v=Uac2ZCpuU2Y&t=12m6s)

### Active CPU Pricing: Challenging Serverless Economics

Traditional serverless computing pricing (including AWS Lambda) is fundamentally broken for AI workloads because it charges for wall-clock time rather than actual compute consumption. This creates massive inefficiencies when agents are "thinking" but not actively using CPU.

**Substantiation:** Rauch explained: "If you have an LLM that is thinking for 30 minutes, the way that old serverless compute primitive is charged to you is 30 minutes of wall time. Now, we multiply that by, you have 1,000 users. You get 1,000 instances of 30 minutes of wall time that you get charged for. So we had to innovate and we created something called fluid. It optimizes for packing compute more densely or requests more densely within the same unit of compute. And the other really interesting thing, we created a new pricing multiple active CPU. We only charge for the computation that actually happens." [[00:10:20]](https://www.youtube.com/watch?v=Uac2ZCpuU2Y&t=10m10s)

### Evangelism to Agents Over Humans

Developer advocacy and documentation should prioritize agents over human developers, fundamentally inverting the traditional model of technical communication and community building. This suggests that the primary "users" of frameworks and tools will soon be AI agents, not humans.

**Substantiation:** Rauch stated: "Traditionally what Next.js has done in order to grow, in order to be a reliable and successful piece of software is we write code in the form of compiler and runtime. Then we write unit tests and integration tests and end-to-end tests. And then we evangelize on X and other forums. I think the evangelism to humans will give way to evangelism to agents. So this is our way of saying, hey, agents, like here's the exams that you need to take in order to be a proficient Next.js agent or Next.js engineer." [[00:15:48]](https://www.youtube.com/watch?v=Uac2ZCpuU2Y&t=15m38s)

## 3. Companies Identified

### Vercel

**Description:** Cloud platform company originally focused on frontend deployment and hosting, now pivoting to become the "AI Cloud" infrastructure provider.

**Why Mentioned:** The company is being repositioned as the infrastructure layer for AI applications, having served over 1 trillion requests per month with 10+ million customers. They're building fundamental primitives like the Vercel Sandbox (EC2 for AI), AI Gateway (CDN for tokens), and Fluid compute.

**Quotes:** 
- "Vercel itself hosts and delivers websites, which is recently passed a trillion requests per month. And we started over 10 million customers." [[00:01:48]](https://www.youtube.com/watch?v=Uac2ZCpuU2Y&t=1m38s)
- "Yesterday was the 10th year anniversary of Vercel incorporating. And for us, it's always day zero. When we started this company, LLMs were not a thing. The AI SDK was not a thing. Not even Next.js was a thing." [[00:02:42]](https://www.youtube.com/watch?v=Uac2ZCpuU2Y&t=2m32s)

### Stanford University

**Description:** Elite research university and educational institution.

**Why Mentioned:** Highlighted as a prestigious early adopter of Vercel's platform, with their FTL.Stanford.edu site now hosted on Vercel, with more departments coming.

**Quotes:** "Happy to announce that Stanford is now on Vercel. So I tweeted about this yesterday. We're hosting FTL, Stanford.edu, with a lot more departments coming." [[00:00:35]](https://www.youtube.com/watch?v=Uac2ZCpuU2Y&t=25s)

## 4. People Identified

### Andy Jassy

**Description:** CEO of Amazon Web Services (AWS) and previously CEO of Amazon.

**Why Mentioned:** Rauch shared his mental model about the shift from speed-optimized to correctness-optimized computing directly with Jassy, indicating high-level strategic dialogue about the future of cloud computing.

**Quotes:** "I have this mental model that I've been working for a while. I actually recently shared this with Andy Jassy at AWS, and we kind of riffed on. When AWS first came out, a lot of what the cloud was looking to solve was you go to Amazon.com, you want to respond to 100 milliseconds." [[00:06:37]](https://www.youtube.com/watch?v=Uac2ZCpuU2Y&t=6m27s)

## 5. Operating Insights

### Build for 10-Year Horizons, Not Current Reality

When starting a company or building a product, especially in infrastructure, you must architect for a decade-long vision because the technology landscape will be completely different. Vercel started before LLMs, AI SDK, or even Next.js existed, yet managed to position itself for the AI era.

**Substantiation:** Rauch reflected: "Also, if you're looking to make a dent in the world or a startup here, I think you have to look at 10 years into the future. So yeah, fun enough. Yesterday was the 10th year anniversary of Vercel incorporating. And for us, it's always day zero. When we started this company, LLMs were not a thing. The AI SDK was not a thing. Not even Next.js was a thing. So keep that in mind as you continue to iterate and come up with new ideas." [[00:02:37]](https://www.youtube.com/watch?v=Uac2ZCpuU2Y&t=2m27s)

### Developer Experience for Agents, Not Just Humans

Companies building developer tools should now optimize their APIs, documentation, and tooling primarily for consumption by AI agents rather than human developers. This means creating "non-lossy" APIs that perfectly model underlying capabilities and building evaluation frameworks to test agent performance.

**Substantiation:** Rauch explained: "One thing that elements traditional struggle is keeping up with API version changes or variance in APIs. So app writer comes out or Next.js 16 comes out and there's a new directive or there's a new API. Can the agent successfully discover what is the Next.js version being used, what is the right API to use in this case, et cetera." [[00:14:43]](https://www.youtube.com/watch?v=Uac2ZCpuU2Y&t=14m33s) He emphasized: "Our goal with this module is to provide an API that's not lossy, meaning if OpenAI or Anthropic come out with a new API or a new way of doing caching or whatever, the SDK can perfectly model it." [[00:13:43]](https://www.youtube.com/watch?v=Uac2ZCpuU2Y&t=13m33s)

### Reuse Infrastructure Across Different Use Cases

Vercel's strategy of building micro-VMs for their build process, then repurposing that same infrastructure for agent code execution demonstrates how infrastructure investments can compound. The same security and isolation primitives serve multiple purposes.

**Substantiation:** Rauch described: "Every single day when you push code to Vercel, we create what we call a micro VM, or an ephemeral virtual machine that takes in your code, and then you can build it and optimize it for production. You can think of us having reused that infrastructure that we've built for the build process, and now we're giving it to agents, so that agents can basically write and execute any kind of code in a secure fashion." [[00:09:19]](https://www.youtube.com/watch?v=Uac2ZCpuU2Y&t=9m9s)

## 6. Overlooked Insights

### TypeScript's Resurgence Signals AI Coding Tool Success

GitHub's data showing TypeScript overtaking Python as the #1 language again is not just a language preference shift—it's actually a proxy metric for the success of AI coding tools that generate TypeScript code. This suggests monitoring language adoption trends could be an early indicator of which AI coding tools are gaining real traction.

**Substantiation:** Rauch noted: "GitHub just also mentioned the other day that TypeScript is the number one language again. We're so back. Python was the number one language last year. The hypothesized this is a byproduct of Python. There are so many tools out there, like v0, where you prompt and you end up with a bunch of TypeScript code that is placed at Vercel itself." [[00:01:27]](https://www.youtube.com/watch?v=Uac2ZCpuU2Y&t=1m17s)

### The "GitHub for Model Performance" Platform Play

While Rauch presented Next.js Evals as a testing framework for agents, the underlying strategic insight is more profound: Vercel is positioning to become the canonical platform for evaluating and ranking AI model performance across specific tasks—essentially creating a new category of infrastructure that could become as foundational as GitHub is for code. This could give them unique insight into which models are actually winning in production use cases.

**Substantiation:** Rauch revealed: "We hope that this becomes a broader effort, much like GitHub for storing code. We can sort of spearhead the GitHub of model performance evaluations." [[00:16:30]](https://www.youtube.com/watch?v=Uac2ZCpuU2Y&t=16m20s) Combined with their AI SDK becoming the fastest-growing SDK: "It looks like we're in track to actually surpass OpenAI probably sometimes this year or early next year. So if this module becomes the prevalent way that TypeScript JavaScript and soon Python engineers access AI, we'll be able to allow for that portability and hopefully the emergence of more open solutions." [[00:14:00]](https://www.youtube.com/watch?v=Uac2ZCpuU2Y&t=13m50s)