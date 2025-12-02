# [Why IDEs Won't Die in the Age of AI Coding: Zed Founder Nathan Sobo](https://www.youtube.com/watch?v=nQP4Wt_6ea8)

**Podcast:** Training Data
**Date:** 2025-12-02
**Region:** Western
**Video ID:** nQP4Wt_6ea8
**Video URL:** https://www.youtube.com/watch?v=nQP4Wt_6ea8
**Transcript:** [View Transcript](./transcript.md)

---

# Podcast Summary: Nathan Sobo on Z IDE and the Future of Coding

## 1. Key Themes

### The IDE is Not Dead: Source Code as Human Language

Despite hype around terminal-based AI coding tools, Nathan argues that source code is fundamentally a language designed for human comprehension, not just machine execution. He challenges the notion that IDEs will become obsolete, asserting that humans will always need to interact with and understand code visually.

**Substantiation:**
"I just fundamentally think that source code is a language, just like natural language is a language. So we have this revolutionary new tool for processing natural language that we've never had. But it's not like source code is binary that we feed to a processor, right? Like it is intended for human consumption." [[00:03:17]](https://www.youtube.com/watch?v=nQP4Wt_6ea8&t=3m7s) - Nathan Sobo

Nathan references Harold Abelson's philosophy: "programs should be written for people to read and only incidentally for machines to execute" [[00:03:47]](https://www.youtube.com/watch?v=nQP4Wt_6ea8&t=3m37s), emphasizing that even when AI can generate code, humans need sophisticated interfaces to review, understand, and validate what's being created.

### Collaboration Infrastructure: From Asynchronous Git to Synchronous Real-Time

The traditional Git-based, snapshot-oriented workflow is becoming inadequate for the AI era. Nathan envisions a future where conversations, edits, and context are tightly integrated in real-time within the authoring environment, treating code as metadata that supports continuous collaboration rather than discrete snapshots.

**Substantiation:**
"When I'm interacting with an agent and it goes off and makes some changes and I want to give it feedback on those changes. Ideally, I want to kind of permanently store the feedback that I gave on those changes and have a record of that. What tools, I mean, there's no sort of get for that, if that makes sense, right? I'm not going to commit on every token the thing emits and then like do a pull request review on that, right?" [[00:15:02]](https://www.youtube.com/watch?v=nQP4Wt_6ea8&t=14m52s) - Nathan Sobo

He's building infrastructure that's "kind of the equivalent of having a commit on every keystroke or commit on every edit that the agent streams in and then being able to anchor interaction or conversation directly to that" [[00:15:54]](https://www.youtube.com/watch?v=nQP4Wt_6ea8&t=15m44s), creating fine-grained tracking that the current Git paradigm cannot support.

### The Switzerland Strategy: IDE as Platform, Not Agent Builder

Rather than competing to build the best AI coding agent, Z positions itself as the ultimate interface layer between humans, code, and multiple AI agents. Through the Agent Client Protocol (ACP), Z democratizes agent integration similar to how the Language Server Protocol democratized language tooling.

**Substantiation:**
"I really view our job as to provide the ultimate interface between the human being, the source code, other human beings or other artificial human beings basically." [[00:16:50]](https://www.youtube.com/watch?v=nQP4Wt_6ea8&t=16m40s) - Nathan Sobo

On the protocol strategy: "One great thing that Microsoft did with VS Code is they took all the intelligence of the IDE that was typically bundled in like JetBrains style...And they moved it out to the community. So the PHP has a language server now and there's the TypeScript language server, et cetera. We wanted to do the same thing with agents." [[00:18:20]](https://www.youtube.com/watch?v=nQP4Wt_6ea8&t=18m10s) - Nathan Sobo

## 2. Contrarian Perspectives

### Writing Code Manually Remains More Efficient Than Prompting

While the industry races toward natural language interfaces for code generation, Nathan maintains that for many tasks, directly writing code is still the clearest and most efficient form of expression—even more so than describing intent to an LLM.

**Substantiation:**
"I could write a sentence to an LLM describing, I want a struct with the following four fields, or even zoom out and describe that on a more abstract level. But if I know what I want to express, sometimes source code really is the most efficient way to do it." [[00:06:04]](https://www.youtube.com/watch?v=nQP4Wt_6ea8&t=5m54s) - Nathan Sobo

**Experience backing this claim:** Nathan has spent nearly two decades building IDEs and actively uses AI coding tools himself, giving him direct experience with both modalities. His observation that "even people that are heavily vibe coding with a tool in the terminal are probably running an editor alongside that tool to inspect what's going on" [[00:06:26]](https://www.youtube.com/watch?v=nQP4Wt_6ea8&t=6m16s) suggests this isn't just preference but practical necessity.

### Performance is Architecture, Not a Feature

Counter to the prevailing wisdom that performance can be optimized later, Nathan argues that performance characteristics are fundamentally determined by architectural choices and cannot be retrofitted. This led him to abandon Electron (which he helped create) in favor of building Z in Rust from scratch.

**Substantiation:**
"Performance is not a feature that you can really go back and add later. If you've chosen an architecture, you're going to accept the performance capabilities of that architecture and the web wasn't it for me." [[00:10:36]](https://www.youtube.com/watch?v=nQP4Wt_6ea8&t=10m26s) - Nathan Sobo

He describes hitting the ceiling with Adam: "I remember opening up the performance profile that was built into Electron, Chrome's dev tools basically. And just looking at something that I was trying to optimize, and I'm just like, I need to get inside of whatever these little lines are in this, in this flame graph and figure out what's going on inside there. And I just hit the ceiling." [[00:10:03]](https://www.youtube.com/watch?v=nQP4Wt_6ea8&t=9m53s) - Nathan Sobo

### Code Review Culture is Suboptimal Compared to Real-Time Collaboration

Nathan challenges the deeply entrenched asynchronous code review culture popularized by GitHub, arguing that synchronous collaboration in the code itself produces better outcomes and human connection than the "email oriented experience" of pull requests.

**Substantiation:**
"We use Git all the time and we don't do as much code review as a lot of teams because what we prefer to do is just talk to each other in real time in the code." [[00:12:22]](https://www.youtube.com/watch?v=nQP4Wt_6ea8&t=12m12s) - Nathan Sobo

He critiques the standard model: "You kind of go off in your corner and do a bunch of work, take a snapshot of that, upload it, and then in a web browser, someone writes comments on your snapshot and then maybe an hour or maybe a day later, you reply. And it's this very like email oriented experience, asynchronous experience." [[00:11:21]](https://www.youtube.com/watch?v=nQP4Wt_6ea8&t=11m11s) - Nathan Sobo

## 3. Companies Identified

### JetBrains

**Description:** Developer tools company that creates integrated development environments for various programming languages.

**Why mentioned:** JetBrains adopted the Agent Client Protocol (ACP) that Z created, validating the protocol approach and demonstrating industry adoption beyond Z's own IDE.

**Quote:** "I didn't really know how many people are going to resonate with this idea, but JetBrains got on board." [[00:19:16]](https://www.youtube.com/watch?v=nQP4Wt_6ea8&t=19m6s) - Nathan Sobo

### Figma

**Description:** Collaborative design platform that pioneered real-time multiplayer experiences for designers.

**Why mentioned:** Cited as the inspiration for bringing real-time collaborative presence into the software authoring environment, demonstrating the model Z aspires to replicate for developers.

**Quote:** "I really feel like we need to bring the presence of your teammates into the authoring environment itself in much the way that Figma did for designers." [[00:13:28]](https://www.youtube.com/watch?v=nQP4Wt_6ea8&t=13m18s) - Nathan Sobo

### Microsoft (VS Code)

**Description:** Technology company that created VS Code, the dominant code editor.

**Why mentioned:** Referenced multiple times as both competitor (VS Code overtook Adam) and innovator (created the Language Server Protocol that inspired ACP). Represents both the threat and the model for Z's strategy.

**Quote:** "Microsoft kind of copied our idea, took Electron, took code they already had that was running on the web and moved it over and then the rest was history. I mean, VS code went on to tick over the industry." [[00:09:04]](https://www.youtube.com/watch?v=nQP4Wt_6ea8&t=8m54s) - Nathan Sobo

**Additional quote on LSP:** "One great thing that Microsoft did with VS Code is they took all the intelligence of the IDE that was typically bundled in like JetBrains style...And they moved it out to the community." [[00:18:20]](https://www.youtube.com/watch?v=nQP4Wt_6ea8&t=18m10s) - Nathan Sobo

### GitHub (Adam)

**Description:** Code hosting and collaboration platform where Nathan built the Adam editor.

**Why mentioned:** Nathan was one of the first two engineers on the Adam project at GitHub, and in building it, created Electron. The experience and lessons from Adam directly informed Z's design.

**Quote:** "I joined GitHub as the first one of the first two engineers to work on that project and we wanted it to be extremely extensible. And so we decided why don't we build it on web technology. So in the process of creating Adam, we built the shell around Adam, which we ended up naming Electron." [[00:08:16]](https://www.youtube.com/watch?v=nQP4Wt_6ea8&t=8m6s) - Nathan Sobo

### Anthropic (Claude Code)

**Description:** AI safety company that created Claude, an AI assistant.

**Why mentioned:** One of the major AI companies building coding agents that Z integrated with early, representing the competitive/collaborative landscape of AI coding tools.

**Quote:** "All seem to do quite well funded from some of the big AI labs like Anthropic and Google, Google with Gemini CLI, they were the first people that we integrated with. Cloud code, everyone's building an agent, it seems." [[00:17:47]](https://www.youtube.com/watch?v=nQP4Wt_6ea8&t=17m37s) - Nathan Sobo

## 4. People Identified

### Harold Abelson

**Description:** Computer science professor at MIT.

**Why mentioned:** Intellectual influence on Nathan's philosophy about code as human-readable language rather than just machine instructions.

**Quote:** "One of my heroes that I learned a lot from Harold Abelson, he's a computer science professor. I think he was at MIT. He has this great quote that I've always loved, which is like program should be written for people to read and only incidentally for machines to execute." [[00:03:41]](https://www.youtube.com/watch?v=nQP4Wt_6ea8&t=3m31s) - Nathan Sobo

### DHH (David Heinemeier Hansson)

**Description:** Creator of Ruby on Rails and influential figure in web development.

**Why mentioned:** Introduced Nathan to TextMate editor through Rails demos, which influenced Nathan's vision for what an ideal editor should be.

**Quote:** "I learned about text mate from DHH, demoing rails or whatever. It was just lightweight, simple, approachable, fast." [[00:07:02]](https://www.youtube.com/watch?v=nQP4Wt_6ea8&t=6m52s) - Nathan Sobo

### Chris Wanstrath

**Description:** Co-founder of GitHub (though not explicitly stated in transcript, implied by context).

**Why mentioned:** Credited with the idea to name the project "Electron."

**Quote:** "That was Chris Wandsross idea actually, but not mine." [[00:08:38]](https://www.youtube.com/watch?v=nQP4Wt_6ea8&t=8m28s) - Nathan Sobo

## 5. Operating Insights

### Build Vertical Integration When Creating New Interaction Paradigms

Nathan advocates for vertical integration when trying to deliver fundamentally new experiences. He argues that the collaborative coding experience he envisions requires owning the entire stack from UI to infrastructure to deliver properly.

**Substantiation:**
"I always thought the best possible experience would be this vertically integrated. We designed the UI and all the infrastructure top to bottom to deliver this immersive ability to interact directly in the code with another being." [[00:16:20]](https://www.youtube.com/watch?v=nQP4Wt_6ea8&t=16m10s) - Nathan Sobo

This contrasts with typical advice to build on existing platforms and suggests that truly novel experiences may require controlling more of the stack than conventional wisdom suggests.

### Earn the Right to Build Your Vision Through Foundational Excellence

Rather than immediately building the ambitious collaborative and AI-integrated features, Nathan focused first on making Z an excellent standalone editor. This "earn the right" approach builds credibility and user base before tackling more speculative features.

**Substantiation:**
"To be real, like, that is very much a work in progress. And I think to earn the right to deliver this experience, we first just had to build a capable editor that someone would just want to use to create software on their own. And I think we made a ton of progress there and are now starting more earnestly on this phase two." [[00:15:27]](https://www.youtube.com/watch?v=nQP4Wt_6ea8&t=15m17s) - Nathan Sobo

### Choose Architecture Based on 10-Year Performance Requirements

When making fundamental technology choices, Nathan recommends thinking about performance requirements at scale and over the long term, as these decisions become nearly impossible to reverse later.

**Substantiation:**
"It was the, I think, 2017 that I decided we need to start over that a web browser is actually not a suitable foundation for the tool that I really wanted to build, which had a lot to do with performance, which sounds like a no big deal. I mean, but performance is not a feature that you can really go back and add later." [[00:10:27]](https://www.youtube.com/watch?v=nQP4Wt_6ea8&t=10m17s) - Nathan Sobo

This led to the complete rewrite from Electron to Rust, demonstrating willingness to make costly decisions when architectural constraints become clear.

### Democratize Through Protocols When Facing Competitive Uncertainty

When facing numerous well-funded competitors in a rapidly evolving space (AI coding agents), Nathan chose to create an open protocol (ACP) that allows Z to integrate with all of them rather than trying to build the best agent himself.

**Substantiation:**
"Meanwhile, I see all these teams that all seem to do quite well funded from some of the big AI labs like Anthropic and Google...all these agents are rendering what I consider to be a fairly impoverished kind of terminal based experience that would need to be supplemented with an editor. So the thought is, okay, we've got a great editor. And all these people are trying to solve this problem. Like what needs to happen here is the same thing that the language server protocol did." [[00:17:47]](https://www.youtube.com/watch?v=nQP4Wt_6ea8&t=17m37s) - Nathan Sobo

## 6. Overlooked Insights

### Code as Metadata Backbone: The Emerging Version Control Revolution

Nathan briefly mentions building "the equivalent of having a commit on every keystroke" with the ability to "anchor interaction or conversation directly to that" [[00:15:54]](https://www.youtube.com/watch?v=nQP4Wt_6ea8&t=15m44s). This seemingly technical detail actually represents a fundamental reimagining of version control for the AI era. 

The current Git paradigm was designed for asynchronous human-to-human collaboration with discrete chunks of work. But when AI agents are continuously generating and modifying code, and humans need to provide real-time feedback, the notion of a "commit" becomes obsolete. Nathan is building infrastructure where every edit—whether from human or AI—becomes an addressable object that conversations, decisions, and context can attach to.

This could be as foundational as Git was for the open source era, but for the AI collaboration era. The fact that he mentions it almost in passing ("to be real, like, that is very much a work in progress" [[00:15:27]](https://www.youtube.com/watch?v=nQP4Wt_6ea8&t=15m17s)) suggests even he may not be fully marketing the revolutionary nature of this infrastructure. If successful, this fine-grained version control with attached conversations could become the standard for how humans and AI collaborate on any artifact, not just code.

### The Terminal UI is Actually a Design Failure, Not a Feature

When Nathan mentions that AI coding agents from "big AI labs like Anthropic and Google" are "rendering what I consider to be a fairly impoverished kind of terminal based experience that would need to be supplemented with an editor" [[00:18:00]](https://www.youtube.com/watch?v=nQP4Wt_6ea8&t=17m50s), he's making an observation that most people are missing: **the terminal interface for AI coding is a bug, not a feature**.

Many in the industry are treating terminal-based AI coding as a deliberate design choice—a return to simplicity or a new paradigm. But Nathan recognizes it for what it really is: these AI companies are building agents first and UI second (or not at all). They're defaulting to terminal interfaces because that's the easiest way to ship, not because it's the best way to interact with code.

This insight suggests that the current wave of terminal-based AI coding tools may be short-lived as soon as better interfaces emerge. Z's positioning as the interface layer between humans and agents could capture significant value as users eventually recognize that reviewing code diffs in a terminal is fundamentally inferior to doing so in a proper visual environment. The companies building the agents (Anthropic, Google) may eventually realize they're in the wrong business and that owning the interface matters more than owning the agent.