# [Building AI Systems That Scale | Office Hours w/ Calvin French-Owen](https://www.youtube.com/watch?v=zTsEmtlSeaU)

**Podcast:** Theory Ventures Office Hours
**Date:** 2025-12-16
**Participants:** Tomasz Tunguz, Calvin French-Owen, Unknown Guest
**Region:** Western
**Video ID:** zTsEmtlSeaU
**Video URL:** https://www.youtube.com/watch?v=zTsEmtlSeaU
**Transcript:** [View Transcript](./transcript.md)

---

# Podcast Summary: Calvin French-Owen on AI-Powered Software Development

## 1. Key Themes

### The Shift from Coding to Architecture: Engineering's New Paradigm

The role of software engineers is fundamentally transforming from craftspeople who write every line of code to architects and managers who design systems and guide AI agents. Calvin describes this as moving from "10% planning and 90% execution" five years ago to "80% planning and 20% execution" today. The bottleneck is no longer writing code—it's code review, validation, and ensuring the right things are being built. As Calvin notes: "I think now engineering teams can just produce a lot more code a lot more quickly. And so we're starting to see bottlenecks around like code review. Or like, are we building the right things? How do we deploy it? How do we scale it?" [[00:07:04]](https://www.youtube.com/watch?v=zTsEmtlSeaU&t=6m54s)

This shift has profound implications: Calvin estimates modern engineering organizations can move at roughly "double speed" compared to 10 years ago, with some reaching 50-100% faster execution. However, this comes with a caveat—he observes: "I feel like I write like 100% more code than ever before and I throw away 60% of it. And yet I'm still more productive than I've ever been." [[00:19:23]](https://www.youtube.com/watch?v=zTsEmtlSeaU&t=19m13s)

### The Commoditization of Code and Its Business Model Implications

Calvin's reflection on Segment reveals a startling insight about value migration in software. Segment's core value proposition—writing integrations and adapters for different APIs—is exactly the kind of work AI excels at. As he puts it: "The value of writing code is kind of dropping to like zero...a lot more thinking around like the specs for how it should work and like running these data pipelines at scale." [[00:06:40]](https://www.youtube.com/watch?v=zTsEmtlSeaU&t=6m30s)

This suggests entire categories of software businesses built primarily on integration work or boilerplate code generation may become obsolete. Calvin believes certain business models simply won't exist in this era because "writing code, especially sort of like tricky-ish pieces of code to write, like the value there is going down instead of being replaced by running code." [[00:07:27]](https://www.youtube.com/watch?v=zTsEmtlSeaU&t=7m17s)

### The Critical Importance of Architecture and System Design

While coding becomes commoditized, architecture becomes the differentiating skill. Calvin emphasizes that well-architected systems with "small simple parts" enable agents to work more effectively. He provides a concrete example: "What I found is that like kind of forcing this architecture where each service is like a few hundred lines and you documented how the service is fit together and there's a very clear request flow. The agent's actually quite good at managing that level of complexity where it wouldn't if you just kind of like let it run wild." [[00:16:28]](https://www.youtube.com/watch?v=zTsEmtlSeaU&t=16m18s)

This architectural discipline isn't just about organization—it's about enabling faster iteration loops, which Calvin identifies as the key optimization target. The goal isn't seven-hour autonomous agent runs, but rather: "How quickly do I get something working that then I can like verify is a good thing that's working then I can go on to the next thing." [[00:13:19]](https://www.youtube.com/watch?v=zTsEmtlSeaU&t=13m9s)

## 2. Contrarian Perspectives

### Specs Are More Important Than Ever, Not Less

Counter to the "move fast and break things" ethos that dominated startups for years, Calvin argues that specifications have become dramatically more important in the AI era. He admits that at Segment "for the longest time we didn't have specs you know it's like oh kind of like someone's like I got an idea for a thing it's like let me go write the thing." [[00:10:28]](https://www.youtube.com/watch?v=zTsEmtlSeaU&t=10m18s) But now, with agents capable of producing massive amounts of code rapidly, "being able to steer them effectively and help provide the right plan for them I think actually goes a really long ways and it makes your time more leveraged." [[00:10:48]](https://www.youtube.com/watch?v=zTsEmtlSeaU&t=10m38s)

This is contrarian because the common narrative suggests AI makes everything faster and more informal. Instead, Calvin argues the opposite: you need MORE upfront planning to effectively leverage AI's execution speed.

### EPD (Engineering/Product/Design) Won't Fuse Despite Cross-Functional Capability

While AI enables everyone to code, design, and spec products, Calvin firmly believes specialization still matters. Using the CodeX PM Alex as an example: "He would be using codex to fix issues in small bugs and things. And that was amazing...I don't think he's the person who you'd want making the architecture decisions. But he was the person who was capturing the voice of the customer and prioritizing what should go next." [[00:22:37]](https://www.youtube.com/watch?v=zTsEmtlSeaU&t=22m27s)

This contradicts the popular notion that AI will create "full-stack everything" individuals who can do it all. Calvin's experience suggests AI unlocks NEW capabilities for specialists (PMs can fix small bugs, designers can implement prototypes) but doesn't eliminate the need for deep specialization in core disciplines.

### Green Field Projects Are Harder for AI Than Established Codebases

Counterintuitively, Calvin argues that AI coding agents perform better in existing, well-structured codebases than in brand new projects. "I was actually just telling you like in some ways I think it's actually harder to do in a green field project where there is no code like the agent's just going to go off in a random direction. When you think about like median JavaScript that has been trading on...it's like probably not that good. Versus if you have a lot of like queer patterns in the code base." [[00:15:28]](https://www.youtube.com/watch?v=zTsEmtlSeaU&t=15m18s)

This challenges the assumption that AI is best for starting from scratch. Instead, agents benefit from existing patterns and conventions, suggesting the most leverage comes from using AI to extend and modify existing systems rather than building entirely new ones.

### Manual Evaluation by People with Taste Beats Automated Evals

While the industry rushes to build sophisticated automated evaluation frameworks, Calvin argues: "Often I think that someone who's watching exactly what an agent did and has a small subset of that data...looking at where it went wrong, I think we'll usually be able to provide the right level of intervention more than having a big automated setup." [[00:26:06]](https://www.youtube.com/watch?v=zTsEmtlSeaU&t=25m56s)

He describes the OpenAI approach as having "someone with taste figuring out, hey, here's where the agent went wrong. I'm going to train this behavior in the opposite way, and just paying very close attention." [[00:24:14]](https://www.youtube.com/watch?v=zTsEmtlSeaU&t=24m4s) This is contrarian because it suggests that despite all the talk of scalable ML evaluation, human judgment remains the critical ingredient for improving AI systems.

### Throwing Away Code Is Not Just Acceptable—It's Optimal

Calvin challenges the craftsperson mentality of software engineering by embracing massive code waste. He celebrates the statistic about writing 100% more code and throwing away 60% of it while still being more productive. This echoes the painter's quote he references: "When the art critics get together, they ask like, oh, where can you find the best art? It's like when the painters get together, it's like, where can you find the cheap turpentine? It's like, you kind of just do things a lot." [[00:21:14]](https://www.youtube.com/watch?v=zTsEmtlSeaU&t=21m4s)

This perspective treats code more like clay than marble—something to rapidly mold and discard rather than carefully chisel. It's a fundamental mindset shift that many experienced engineers may resist.

## 3. Companies Identified

### Segment
**Description:** Customer data platform that provided a single API to integrate with multiple tools (Google Analytics, Cusperio, Zendesk, Salesforce).

**Why Mentioned:** As a case study for how AI commoditizes certain types of software value. The core product—integration and adapter layer code—is exactly what AI excels at generating.

**Quote:** "Segment originally was a product that helped you integrate all these different tools, right? So it's like a single API. It's end data to Google Analytics. And it's the same data as it's going to Cuspereio...And now when I kind of think about that business, I'm like, wow, like the value of writing code is kind of dropping to like zero." [[00:06:21]](https://www.youtube.com/watch?v=zTsEmtlSeaU&t=6m11s)

### OpenAI
**Description:** AI research laboratory that developed GPT models and CodeX coding assistant.

**Why Mentioned:** As the proving ground for cutting-edge AI development practices, demonstrating how the most advanced teams build and iterate with AI agents.

**Quote:** "OpenAI, that place moves at like a crazy clip. I think it definitely reset my expectations for how quickly an engineering team can move." [[00:18:25]](https://www.youtube.com/watch?v=zTsEmtlSeaU&t=18m15s)

### Anthropic (Claude/Quad Code)
**Description:** AI safety company developing Claude models and coding tools.

**Why Mentioned:** Specifically praised for superior tool use capabilities and the Benning Machine experiment that revealed current limitations in AI agent reliability.

**Quote:** "I think the inthropic models tend to be very good at tool use. And like they clearly they figured out something that doesn't show in the benchmarks...I think quad code works very well there." [[00:35:26]](https://www.youtube.com/watch?v=zTsEmtlSeaU&t=35m16s)

### Cursor
**Description:** AI-powered code editor.

**Why Mentioned:** Highlighted for exceptional speed with their new model, though with potentially lower intelligence ceiling than alternatives.

**Quote:** "I don't know how many people here have tried the new cursor model. It is exceptionally fast...I think the intelligence ceiling might not be as high as some of the others, but like, if you're just like, oh, I want to make this change across like 10 different files, it's pretty good." [[00:36:02]](https://www.youtube.com/watch?v=zTsEmtlSeaU&t=35m52s)

### Cloudflare Workers
**Description:** Edge computing platform for deploying JavaScript functions.

**Why Mentioned:** As an exemplar of good architecture for AI agent development—small, well-defined services that agents can effectively manage.

**Quote:** "What I think is the right pattern for an agent to work with is like you have a bunch of these little workers around that are bound to databases and the workers combine to each other and you almost have like a little microservice architecture." [[00:16:08]](https://www.youtube.com/watch?v=zTsEmtlSeaU&t=15m58s)

## 4. People Identified

### Peter Wheelender
**Description:** Leader of new products at OpenAI who recruited Calvin.

**Why Mentioned:** For recognizing the opportunity to build internal tooling for researchers and having the vision for what became CodeX.

**Quote:** "Peter Wheelender, who leads new products over at OpenAI, I was saying, hey, there's a new team who's spinning up. They're really focused on a lot of internal tooling for researchers. If you want to kind of see where research is going and understand how it's done, it's probably a good fit for building some new products." [[00:02:42]](https://www.youtube.com/watch?v=zTsEmtlSeaU&t=2m32s)

### Andrew (OpenAI Team Member)
**Description:** Member of Calvin's team at OpenAI who made the breakthrough connection between reasoning models and terminal commands.

**Why Mentioned:** For the pivotal insight that led to CodeX's development by connecting reasoning models to terminal execution.

**Quote:** "Around the time that the reasoning models came out, one member of our team, this guy Andrew, had basically hooked up the reasoning model to like start invoking commands via terminal on his laptop. And he's like, oh, actually, this works really well. And so kind of one thing led to another and we started prototyping and eventually that became CodeX." [[00:03:59]](https://www.youtube.com/watch?v=zTsEmtlSeaU&t=3m49s)

### Alex (OpenAI PM)
**Description:** Product Manager on the CodeX team at OpenAI.

**Why Mentioned:** As an example of how AI enables PMs to be more effective without replacing their core role, demonstrating that specialization still matters.

**Quote:** "Alex, who is the PM on the codex team...He would be using codex to fix issues in small bugs and things. And that was amazing. It'd like freedom up. It's like, oh, I hear a thing from a customer. I'd have fixed it five minutes later. That's great. I don't think he's the person who you'd want making the architecture decisions. But he was the person who was capturing the voice of the customer and prioritizing what should go next." [[00:22:31]](https://www.youtube.com/watch?v=zTsEmtlSeaU&t=22m21s)

## 5. Operating Insights

### Optimize for Feedback Loop Speed, Not Agent Autonomy Duration

Calvin's approach prioritizes rapid iteration over long-running autonomous agents. Rather than celebrating seven-hour agent runs, he focuses on getting to a working state quickly for validation. "If it runs for seven hours and it like went off the rails somewhere and I have a bunch of code review like that actually doesn't help me that much." [[00:13:31]](https://www.youtube.com/watch?v=zTsEmtlSeaU&t=13m21s) The key is reaching "minimum viable loop" where the system works as designed, then progressively adding complexity with validation at each step.

### Implement To-Do Driven Development with AI

Calvin describes a powerful workflow: "I've also been experimenting with to do driven development, where I kind of create the scaffold and architecture for it. And then I say, oh, go implement these to do's." [[00:36:51]](https://www.youtube.com/watch?v=zTsEmtlSeaU&t=36m41s) CodeX has integrated this pattern directly into Cursor with a feature that detects TODOs and offers to "implement with CodeX." This allows human architects to maintain control over structure while delegating implementation.

### Maintain Two Types of Documentation: Plans and Docs

Calvin keeps "two sets of markdown files in my repo. One is plans and I view those as very much like throw away things...The other is docs and for those I will sometimes ask it to update depending. For neither one will it actually really look at it unless I tell it to. In some ways the docs are more for my understanding. The plans are for its understanding and then the code is kind of the source of truth." [[00:16:53]](https://www.youtube.com/watch?v=zTsEmtlSeaU&t=16m43s) This separation clarifies what's ephemeral versus enduring.

### Use AI for PR Review Before Human Review

Calvin has adopted CodeX to auto-review all his PRs before sending to colleagues. "I've started using codex as like an auto review all my PRs feature...At least for even just like being a sanded check." [[00:37:47]](https://www.youtube.com/watch?v=zTsEmtlSeaU&t=37m37s) This respects coworkers' time while catching obvious issues, and addresses one of the key bottlenecks he identified: code review bandwidth.

### Anchor Engineering Progress on Weekly Customer Outcome Demos

Rather than measuring lines of code or PRs merged (which AI inflates), Calvin advocates for outcome-based measurement: "One thing I'd love for engineering teams that worked with is like having a weekly demos or like biweekly demos. Basically, it's always anchored on like a customer outcome." [[00:18:52]](https://www.youtube.com/watch?v=zTsEmtlSeaU&t=18m42s) This keeps teams focused on value delivery rather than activity metrics that become meaningless with AI assistance.

### Match Model Selection to Task Characteristics

Calvin has developed a "model smell" for which tools excel at what: "I think the inthropic models tend to be very good at tool use...I think codex is like a very exceptional job in terms of just like pure like, oh, I want to like surgically like make these changes...I don't know how many people here have tried the new cursor model. It is exceptionally fast...if you're just like, oh, I want to make this change across like 10 different files, it's pretty good." [[00:35:26]](https://www.youtube.com/watch?v=zTsEmtlSeaU&t=35m16s) He actively switches between all three based on the specific task.

## 6. Overlooked Insights

### Green Field Architectures Need Human-Defined Scaffolding to Enable Agent Success

Calvin briefly mentioned something profound that could easily be missed: agents need architectural scaffolding to be effective in new projects. He described spending significant time "trying to find like scaffolds of like tests and the right like initial I don't know kernel of how the code should look such that I think it will stay good for a while." [[00:12:08]](https://www.youtube.com/watch?v=zTsEmtlSeaU&t=11m58s)

This suggests a new critical skill: creating minimal but opinionated starting architectures that give agents the right patterns to follow. The implication is that the most valuable engineers may become those who can quickly create these "scaffolds" or "kernels" that guide agent behavior in the right direction. This is different from traditional architecture (which happens after significant code exists) and different from templates (which are too generic). It's about establishing just enough conventions and patterns that agents can productively extend them.

### The CodeX Team Built the Product Manually Before Using AI to Build It

Buried in the conversation was a remarkable detail about CodeX's development: "The whole sprint to launch CodeX took about seven weeks and then like no code written to like launch product...for the most part of it, it was kind of us figuring out how to architect the system and build it in a kind of queenerm way." [[00:05:29]](https://www.youtube.com/watch?v=zTsEmtlSeaU&t=5m19s) Calvin later notes: "I think as time went on, we started being able to use CodeX to write itself, which was actually really cool. But for the most part of it, it was kind of us figuring out how to architect the system." [[00:05:45]](https://www.youtube.com/watch?v=zTsEmtlSeaU&t=5m35s)

This reveals something critical: even the team building the most advanced AI coding tool initially built it the traditional way, only later using the tool to improve itself. The implication is that new paradigms and novel systems still require human architectural thinking to bootstrap. You can't AI your way to a fundamentally new architecture—you need human insight to create the initial design that the AI can then extend. This suggests limits to AI's creative architectural capabilities and highlights why architectural skills remain so valuable.