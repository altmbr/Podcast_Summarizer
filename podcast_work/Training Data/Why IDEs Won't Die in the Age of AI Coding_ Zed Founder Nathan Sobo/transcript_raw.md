# Why IDEs Won't Die in the Age of AI Coding: Zed Founder Nathan Sobo

**Podcast:** Training Data
**Date:** 2025-12-02
**Video ID:** nQP4Wt_6ea8
**Video URL:** https://www.youtube.com/watch?v=nQP4Wt_6ea8

---

[00:00:00] Just doesn't make sense to me that human beings would stop
[00:00:02] SPEAKER_01: interacting at all with source code until we get to like
[00:00:06] SPEAKER_01: AGI, I guess, where human beings aren't going to be doing
[00:00:09] SPEAKER_01: a lot of different things.
[00:00:11] SPEAKER_01: But until then, I think we need to.
[00:00:13] SPEAKER_01: We need to look at code.
[00:00:14] SPEAKER_01: And so then the question is, what's the best user interface
[00:00:18] SPEAKER_01: for doing that?
[00:00:18] SPEAKER_01: Today we're talking with Nathan Sobo, founder of Z, who spent nearly two decades building
[00:00:40] SPEAKER_00: IDE's, first building Adam at GitHub and now Z. Z is a modern IDE written and rust used
[00:00:45] SPEAKER_00: by more than 150,000 active developers and also create to maintain the ACP or agent
[00:00:51] SPEAKER_00: client protocol, which connects different coding agents to different coding surfaces,
[00:00:56] SPEAKER_00: including Z. Nathan shares a contrarian take.
[00:00:59] SPEAKER_00: Despite all the hype around chat and terminal based AI coding tools, he argues that source
[00:01:03] SPEAKER_00: code itself is a language meant for humans to read and that we'll always need visual interfaces
[00:01:08] SPEAKER_00: to understand what AI agents are doing.
[00:01:10] SPEAKER_00: We dig into whether LLMs can actually code what the richer collaboration layer between
[00:01:14] SPEAKER_00: humans and AI might look like for coding.
[00:01:17] SPEAKER_00: And Nathan's vision for turning code into a metadata backbone where conversations, edits,
[00:01:21] SPEAKER_00: and context all hang together.
[00:01:24] SPEAKER_00: Enjoy the show.
[00:01:25] Nathan, thank you for joining us here today.
[00:01:28] SPEAKER_00: Yeah, thanks for having me on.
[00:01:30] SPEAKER_01: I want to start with a hard hitting question.
[00:01:32] SPEAKER_00: There is a lot of internet talk chatter about, is this the death of the IDE?
[00:01:37] SPEAKER_00: So if you roll back two years, everyone was coding primarily in the IDE.
[00:01:41] SPEAKER_00: And now it seems like as people move towards the terminal and more of these conversational
[00:01:45] SPEAKER_00: experiences, there's a question in the air, is this the death of the IDE?
[00:01:49] SPEAKER_00: Yeah, and I've actually asked myself that question at different times and different states
[00:01:55] SPEAKER_01: of anxiety of like, is it the death of the IDE?
[00:01:57] SPEAKER_01: I've spent my entire life grinding toward building the ultimate tool for this.
[00:02:03] SPEAKER_01: And is it not going to matter?
[00:02:04] SPEAKER_01: Are these people right?
[00:02:06] SPEAKER_01: But after mulling it over seriously because I definitely don't want to be gold plating
[00:02:09] SPEAKER_01: buggy whip.
[00:02:11] SPEAKER_01: I think those takes are not realistic.
[00:02:14] SPEAKER_01: It is mind blowing that you can sit down at a terminal and speak English with a script
[00:02:24] SPEAKER_01: talking to an L and make real progress on a code base.
[00:02:28] SPEAKER_01: And there are millions of people doing that, apparently, including me on occasion.
[00:02:34] SPEAKER_01: But the problem I ran into whenever you, you know, the cloud code was the thing I think
[00:02:38] SPEAKER_01: I spent the most time with is when it wants to show you what it just did in your reviewing
[00:02:43] SPEAKER_01: it, you sort of view it through this 10 line or tiny little excerpt in the terminal.
[00:02:49] SPEAKER_01: And as soon as you want to see more, what do you do?
[00:02:54] SPEAKER_01: And so I think if you believe that the IDE is going to die, then I think that requires
[00:03:00] SPEAKER_01: you to believe that human beings are not going to need to interact with source code anymore.
[00:03:05] SPEAKER_01: Like I don't need to take a look and see the context of this edit that the agent just
[00:03:10] SPEAKER_01: made and all the different things that it's connected to and understand that and load
[00:03:15] SPEAKER_01: that into my brain.
[00:03:17] SPEAKER_01: And I just fundamentally think that source code is a language, just like natural language
[00:03:22] SPEAKER_01: is a language.
[00:03:23] SPEAKER_01: So we have this revolutionary new tool for processing natural language that we've never had.
[00:03:27] SPEAKER_01: But it's not like source code is binary that we feed to a processor, right?
[00:03:33] SPEAKER_01: Like it is intended for human consumption.
[00:03:35] SPEAKER_01: Like one of my heroes that I learned a lot from Harold Abelson, he's a computer science
[00:03:41] SPEAKER_01: professor.
[00:03:42] SPEAKER_01: I think he was at MIT.
[00:03:44] SPEAKER_01: He has this great quote that I've always loved, which is like program should be written
[00:03:47] SPEAKER_01: for people to read and only incidentally for machines to execute.
[00:03:52] SPEAKER_01: Which is an extreme stance because it's like why you're writing the program if you don't
[00:03:56] SPEAKER_01: want a machine to execute it.
[00:03:58] SPEAKER_01: There are like a lot of people that program and ask all and stuff that seem to not actually
[00:04:01] SPEAKER_01: care about what gets done with all of this programmatic machination I tend to.
[00:04:08] SPEAKER_01: But I also see a lot of wisdom in that and that like fundamentally programs are about us
[00:04:14] SPEAKER_01: expressing some abstract process in a very precise way.
[00:04:20] SPEAKER_01: And there is no better language for talking about a lot of different sort of touring complete
[00:04:25] SPEAKER_01: programmatic concepts than source code itself.
[00:04:28] SPEAKER_01: So I just doesn't make sense to me that human beings would stop interacting at all with
[00:04:33] SPEAKER_01: source code until we get to like AGI, I guess, where human beings aren't going to be doing
[00:04:39] SPEAKER_01: a lot of different things.
[00:04:41] SPEAKER_01: But until then, I think we need to look at code.
[00:04:45] SPEAKER_01: And so then the question is what's the best user interface for doing that?
[00:04:49] SPEAKER_00: And is the best user interface at GUI then?
[00:04:52] I think so.
[00:04:54] SPEAKER_01: There are a lot of different ways of representing an interface to code.
[00:04:58] SPEAKER_01: Does it need to be graphical?
[00:04:59] SPEAKER_01: I mean, there are a lot of people that are using them, for example.
[00:05:04] SPEAKER_01: Vims not a graphical user interface, but is an interface, right?
[00:05:09] SPEAKER_01: That's optimized around presenting source code, navigating source code.
[00:05:13] SPEAKER_01: And yes, sometimes editing that source code manually, because I think in the same way
[00:05:17] SPEAKER_01: that the best way to understand software is often looking at the software, looking at
[00:05:22] SPEAKER_01: the best human engineered synthetic language we can derive for expressing this abstract
[00:05:30] SPEAKER_01: process.
[00:05:31] SPEAKER_01: Sometimes the best way of expressing it is just to write it directly.
[00:05:36] SPEAKER_01: And I'm not here to say that I'm particularly a big fan of grinding through repetitive work
[00:05:43] SPEAKER_01: or having something that could be written by an LLM.
[00:05:46] SPEAKER_01: Like I'm no desire to write that necessarily, but I do think that they're often, oftentimes
[00:05:51] still in software where the clearest way to articulate something is just to write the
[00:05:56] SPEAKER_01: code, define a data structure.
[00:05:58] SPEAKER_01: I could write a sentence to an LLM describing, I want a struct with the following four fields,
[00:06:04] SPEAKER_01: or even zoom out and describe that on a more abstract level.
[00:06:07] SPEAKER_01: But if I know what I want to express, sometimes source code really is the most efficient way
[00:06:12] SPEAKER_01: to do it.
[00:06:13] SPEAKER_01: And in that world, a tool designed for navigating and editing source code still seems like
[00:06:19] SPEAKER_01: a really relevant tool.
[00:06:20] SPEAKER_01: And I have a feeling that even people that are heavily vibe coding with a tool in the
[00:06:26] SPEAKER_01: terminal are probably running an editor alongside that tool to inspect what's going on.
[00:06:31] SPEAKER_01: You mentioned at the start that you've been working on IDE's for your whole career.
[00:06:34] SPEAKER_00: You are a legend in the IDE space.
[00:06:38] SPEAKER_00: Just maybe for our listeners, just say we're on your background.
[00:06:41] When I graduated from college, I decided I wanted to build my own editor.
[00:06:45] SPEAKER_01: That was 2006 that the year after I graduated college.
[00:06:50] SPEAKER_01: And I've been working my whole career to build the editor I envisioned, which was always
[00:06:55] SPEAKER_01: sort of at the time, text mate was a really popular tool.
[00:06:58] SPEAKER_01: I learned about text mate from DHH, demoing rails or whatever.
[00:07:02] SPEAKER_01: It was just lightweight, simple, approachable, fast.
[00:07:06] SPEAKER_01: I'd used EMAX, I'd use Eclipse, I'd used the JetBrains products, which are still really
[00:07:11] SPEAKER_01: powerful.
[00:07:13] SPEAKER_01: All of them brought something to the table in terms of either extensibility or responsiveness
[00:07:19] SPEAKER_01: or feature richness, but none of them synthesized all those things into one package.
[00:07:25] SPEAKER_01: And so it was like 2006 when I decided I want to build an editor that has the same power
[00:07:32] SPEAKER_01: or more power as the most capable IDE's that take 10 years to start up and feel sluggish
[00:07:41] SPEAKER_01: under my fingertips, but then have the same kind of responsiveness as a text mate or a
[00:07:47] SPEAKER_01: VIM, but also be really extensible, but not have to be extensible in this arcane VIM script
[00:07:52] SPEAKER_01: language where I'm having to have this pet that I'm feeding every weekend or whatever
[00:07:57] SPEAKER_01: in my spare time to make sure that my VIM configuration doesn't break.
[00:08:02] SPEAKER_01: I wrote Adam and VIM.
[00:08:03] SPEAKER_01: So anyway.
[00:08:04] SPEAKER_01: Talk about Adam actually and then lessons from that and then why he started ZEB.
[00:08:07] SPEAKER_00: Yeah.
[00:08:08] SPEAKER_01: I worked at delivering this IDE of my dreams was Adam and I joined GitHub as the first one
[00:08:16] SPEAKER_01: of the first two engineers to work on that project and we wanted it to be extremely
[00:08:21] SPEAKER_01: extensible.
[00:08:22] SPEAKER_01: And so we decided why don't we build it on web technology.
[00:08:25] SPEAKER_01: So in the process of creating Adam, we built the shell around Adam, which we ended up naming
[00:08:31] SPEAKER_01: Electron.
[00:08:32] SPEAKER_01: And Electron went on to be the foundation.
[00:08:35] SPEAKER_01: I just caught that reference.
[00:08:37] SPEAKER_01: Yeah.
[00:08:38] SPEAKER_01: That was Chris Wandsross idea actually, but not mine.
[00:08:41] SPEAKER_01: Yeah.
[00:08:42] SPEAKER_01: And so what we did is we sort of married Node.js, which was getting really popular at the
[00:08:46] SPEAKER_01: time with Chrome and then delivered this framework that kind of let you build a web page that
[00:08:52] SPEAKER_01: looked like a desktop app.
[00:08:56] SPEAKER_01: And it went on to be really successful.
[00:08:57] SPEAKER_01: Adam had it stay in the sun, then Microsoft kind of copied our idea, took Electron, took
[00:09:04] SPEAKER_01: code they already had that was running on the web and moved it over and then the rest
[00:09:09] SPEAKER_01: was history.
[00:09:10] SPEAKER_01: I mean, VS code went on to tick over the industry.
[00:09:12] SPEAKER_01: But at some point, I'd kind of gotten to the point where I felt like Adam had run its
[00:09:15] SPEAKER_01: course.
[00:09:16] SPEAKER_01: I had learned some hard lessons there.
[00:09:18] SPEAKER_01: Some of them were just about like, how do you design a data structure to efficiently represent
[00:09:23] SPEAKER_01: large quantities of text and edit it, which is a language neutral lesson, honestly,
[00:09:30] SPEAKER_01: to some extent.
[00:09:31] SPEAKER_01: And some of the lessons were about not inviting people to bring code onto the main thread and
[00:09:40] SPEAKER_01: destroy the performance of the application by just running random extension code.
[00:09:45] SPEAKER_01: We made it very extensible.
[00:09:46] SPEAKER_01: We were very open, which sort of made it very popular quickly.
[00:09:50] SPEAKER_01: And then we drowned under the promises we had made that were kind of premature.
[00:09:55] SPEAKER_01: But one of the things was, I was just sick of web technology.
[00:09:58] SPEAKER_01: I remember opening up the performance profile that was built into Electron, Chrome's
[00:10:03] SPEAKER_01: dev tools basically.
[00:10:05] SPEAKER_01: And just looking at something that I was trying to optimize, and I'm just like, I need
[00:10:09] SPEAKER_01: to get inside of whatever these little lines are in this, in this flame graph and figure
[00:10:14] SPEAKER_01: out what's going on inside there.
[00:10:15] SPEAKER_01: And I just hit the ceiling, I guess, on how fast I can make this thing.
[00:10:20] SPEAKER_01: And so it was the, I think, 2017 that I decided we need to start over that a web browser is
[00:10:27] SPEAKER_01: actually not a suitable foundation for the tool that I really wanted to build, which
[00:10:32] SPEAKER_01: had a lot to do with performance, which sounds like a no big deal.
[00:10:36] SPEAKER_01: I mean, but performance is not a feature that you can really go back and add later.
[00:10:41] SPEAKER_01: If you've chosen an architecture, you're going to accept the performance capabilities of
[00:10:47] SPEAKER_01: that architecture and the web wasn't it for me.
[00:10:50] You built Zad originally to make it easier for humans to pair program with other humans.
[00:10:56] SPEAKER_00: That ended up being very convenient as AI agents came about and humans started to need
[00:11:01] SPEAKER_00: to collaborate with AI agents.
[00:11:02] SPEAKER_00: Talk about that dynamic a bit.
[00:11:03] SPEAKER_00: I think the whole industry has this idea of how we should all be collaborating together.
[00:11:09] SPEAKER_01: And I was actually at GitHub for the current way that we collaborate, becoming popular.
[00:11:16] SPEAKER_01: And it's all about being asynchronous that you kind of go off in your corner and do a
[00:11:21] SPEAKER_01: bunch of work, take a snapshot of that, upload it, and then in a web browser, someone,
[00:11:26] SPEAKER_01: writes comments on your snapshot and then maybe an hour or maybe a day later, you reply.
[00:11:31] SPEAKER_01: And it's this very like email oriented experience, asynchronous experience, which when you're
[00:11:38] all on the same page, or maybe when you're working on Linux, which is what Git was designed
[00:11:43] SPEAKER_01: for originally.
[00:11:45] SPEAKER_01: And there's people all over the world working on these very disparate things.
[00:11:49] SPEAKER_01: That's an appropriate modality.
[00:11:51] SPEAKER_01: But I always believed that the best way to collaborate on software was including a lot
[00:11:57] SPEAKER_01: more times where we're in the code together, writing code together or talking through code
[00:12:02] SPEAKER_01: together and getting on the same page in a format where we're actually talking to each
[00:12:05] SPEAKER_01: other and get interrupt each other and also relate to each other as human beings in a way
[00:12:12] SPEAKER_01: that I just don't see happening on top of the Git-based flow.
[00:12:17] SPEAKER_01: We use Git all the time and we don't do as much code review as a lot of teams because
[00:12:22] SPEAKER_01: what we prefer to do is just talk to each other in real time in the code.
[00:12:27] But there just wasn't a good tool that enabled that.
[00:12:30] SPEAKER_01: You could use screen sharing, but the problem with screen sharing is one person is very much
[00:12:34] SPEAKER_01: in the passenger seat because you got a round trip keystrokes.
[00:12:38] SPEAKER_01: And so, yeah, the two big problems when I, not knowing the AI was coming, right?
[00:12:44] SPEAKER_01: The two big problems I wanted to solve at the outset were fundamentally better performance.
[00:12:49] SPEAKER_01: When you type a key, I want pixels responding to you on the next sync of the monitor.
[00:12:55] SPEAKER_01: So there's zero perceptible lag.
[00:12:58] SPEAKER_01: We're pretty close.
[00:12:59] SPEAKER_01: I can't say we're 100% perfect, but we're hell of a lot closer than you could ever get
[00:13:02] SPEAKER_01: in a web browser.
[00:13:03] SPEAKER_01: Can you say a word about how you've achieved that?
[00:13:05] SPEAKER_01: Yes, I'm on a digression here.
[00:13:07] SPEAKER_01: But go ahead and say your second thing and then say a word about your G performance.
[00:13:12] SPEAKER_01: But then the other big pillar other than performance at the outset was changing the way
[00:13:16] SPEAKER_01: that developers collaborate on software.
[00:13:20] SPEAKER_01: And so to do that, I really feel like we need to bring the presence of your teammates into
[00:13:28] SPEAKER_01: the authoring environment itself in much the way that Figma did for designers.
[00:13:32] SPEAKER_01: Now designers didn't have a lot of good options.
[00:13:34] SPEAKER_01: They didn't have anything as good as Git, for example, as a compelling alternative, but
[00:13:39] SPEAKER_01: I still think that vision of you're in the tool looking at the actual thing you're creating
[00:13:45] SPEAKER_01: and there are other people there with you was something that even before I saw Figma,
[00:13:49] SPEAKER_01: I wanted to bring to the experience of creating software.
[00:13:52] SPEAKER_01: And so that's why it felt appropriate to own the UI on the speed level now on to the
[00:13:58] SPEAKER_01: rest of your question about what are the implications of that for AI.
[00:14:03] SPEAKER_01: The vision was said was always I want to link conversations to the code in the authoring
[00:14:09] SPEAKER_01: environment where the code's being written.
[00:14:11] SPEAKER_01: And so I actually think that conversations in the code that used to be a kind of a weird
[00:14:17] SPEAKER_01: idea, right?
[00:14:18] SPEAKER_01: Because oh, why would you need to have a conversation in the code?
[00:14:21] SPEAKER_01: You write it by yourself and you push a snapshot and then we'll have a conversation on a website
[00:14:25] SPEAKER_01: about the code you wrote, right?
[00:14:28] SPEAKER_01: But it's starting to feel a lot more relevant in a world where you're having this conversation
[00:14:33] SPEAKER_01: all the time with this like spirit being or whatnot, right?
[00:14:37] SPEAKER_01: Let's go.
[00:14:38] SPEAKER_01: Yeah, all of us, even me included as a big fan of this more synchronous mode of collaboration,
[00:14:45] SPEAKER_01: are having a lot more conversations about code in the code.
[00:14:50] SPEAKER_01: And that's where I see sort of this snapshot oriented paradigm really breaking down.
[00:14:57] SPEAKER_01: Like when I'm interacting with an agent and it goes off and makes some changes and I
[00:15:02] SPEAKER_01: want to give it feedback on those changes.
[00:15:04] SPEAKER_01: Ideally, I want to kind of permanently store the feedback that I gave on those changes
[00:15:10] SPEAKER_01: and have a record of that.
[00:15:14] SPEAKER_01: What tools, I mean, there's no sort of get for that, if that makes sense, right?
[00:15:18] SPEAKER_01: I'm not going to commit on every token the thing emits and then like do a pull request
[00:15:23] SPEAKER_01: review on that, right?
[00:15:24] SPEAKER_01: And so to be real, like, that is very much a work in progress.
[00:15:27] SPEAKER_01: And I think to earn the right to deliver this experience, we first just had to build a
[00:15:32] SPEAKER_01: capable editor that someone would just want to use to create software on their own.
[00:15:37] SPEAKER_01: And I think we made a ton of progress there and are now starting more earnestly on this
[00:15:42] SPEAKER_01: phase two of this fine grained tracking mechanism that's sort of the equivalent.
[00:15:51] SPEAKER_01: It's not exactly how it works, but it's kind of the equivalent of having a commit on
[00:15:54] SPEAKER_01: every keystroke or commit on every edit that the agent streams in and then being able
[00:15:59] SPEAKER_01: to anchor interaction or conversation directly to that.
[00:16:04] SPEAKER_01: So that's something that the tech we're building, I think is something maybe we could have
[00:16:07] SPEAKER_01: built in isolation.
[00:16:11] SPEAKER_01: But then the problem is what experience do you deliver on top of that?
[00:16:15] SPEAKER_01: And I always thought the best possible experience would be this vertically integrated.
[00:16:20] SPEAKER_01: We designed the UI and all the infrastructure top to bottom to deliver this immersive ability
[00:16:27] SPEAKER_01: to interact directly in the code with another being.
[00:16:32] SPEAKER_00: And so you've made the choice to make the IDE almost this Switzerland for humans to collaborate
[00:16:38] SPEAKER_00: with different AI agents.
[00:16:41] SPEAKER_00: Talk about the role that agent coding protocol, because that was a CEP plays in that vision.
[00:16:47] SPEAKER_00: I really view our job as to provide the ultimate interface between the human being, the source
[00:16:54] SPEAKER_01: code, other human beings or other artificial human beings basically.
[00:17:00] SPEAKER_01: And we built our first party agent like earlier this year.
[00:17:06] And then, but as we're doing that and it's quite challenging as tuning the prompts,
[00:17:12] SPEAKER_01: I mean, none of it feels like challenging in the same ways that building an IDE is in
[00:17:19] SPEAKER_01: terms of algorithmic complexity and getting the data structures just right and making
[00:17:25] SPEAKER_01: sure that things are performant.
[00:17:27] SPEAKER_01: The actual like touring complete software parts of that are fairly easy.
[00:17:32] SPEAKER_01: The hard parts are like the AI parts.
[00:17:34] SPEAKER_01: And that's still something that I think we're learning as a team like we come from a very
[00:17:40] SPEAKER_01: different perspective.
[00:17:42] SPEAKER_01: Meanwhile, I see all these teams that all seem to do quite well funded from some of the
[00:17:47] SPEAKER_01: big AI labs like Anthropic and Google, Google with Gemini CLI, they were the first people
[00:17:54] SPEAKER_01: that we integrated with.
[00:17:57] SPEAKER_01: Cloud code, everyone's building an agent, it seems.
[00:18:00] SPEAKER_01: And all these agents are rendering what I consider to be a fairly impoverished kind of
[00:18:05] SPEAKER_01: terminal based experience that would need to be supplemented with an editor.
[00:18:10] SPEAKER_01: So the thought is, okay, we've got a great editor.
[00:18:13] SPEAKER_01: And all these people are trying to solve this problem.
[00:18:15] SPEAKER_01: Like what needs to happen here is the same thing that the language server protocol did.
[00:18:20] SPEAKER_01: So one great thing that Microsoft did with VS Code is they took all the intelligence of
[00:18:26] SPEAKER_01: the IDE that was typically bundled in like JetBrains style, right, where the IDE comes
[00:18:31] SPEAKER_01: pre-configured knowing everything.
[00:18:33] SPEAKER_01: And they moved it out to the community.
[00:18:35] SPEAKER_01: So the PHP has a language server now and there's the TypeScript language server, et cetera.
[00:18:41] SPEAKER_01: We wanted to do the same thing with agents.
[00:18:44] SPEAKER_01: The thought being there's probably going to be different kinds of agents experimenting
[00:18:47] SPEAKER_01: in different domains.
[00:18:49] SPEAKER_01: Maybe there's certain agents that are optimized for particular problems.
[00:18:53] SPEAKER_01: They're agents competing with each other.
[00:18:55] SPEAKER_01: So sometimes one will be the best only to be leapfrog by another, externalizing all
[00:19:00] SPEAKER_01: that and trying to democratize that and say, hey, whatever agent you want to use, we
[00:19:05] SPEAKER_01: want to deliver a great UI for you to interact with that agent and your software.
[00:19:10] SPEAKER_01: That was the thinking behind it.
[00:19:12] SPEAKER_01: And so far it's working out better than I might have expected actually.
[00:19:16] SPEAKER_01: I didn't really know how many people are going to resonate with this idea, but JetBrains
[00:19:21] SPEAKER_01: got on board.