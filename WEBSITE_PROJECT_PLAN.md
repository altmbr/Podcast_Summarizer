# Podcast Summary Website - Project Plan

## How to Leave Comments in This Document

Use this format to leave comments or questions:
```markdown
> **💬 COMMENT**: For the Podcasts, Participatns should be the hosts. If we don't have that data, let's get it.
> **💬 COMMENT**: Can I ask you to search for and collect the Podcast cover images?
```

I'll respond to comments using:
```markdown
> **✅ RESPONSE**: My response here
```

Example:
> **💬 COMMENT**: Should we add search functionality in v1?
> **✅ RESPONSE**: Let's keep v1 simple without search. We can add it in v2.

---

## Overview

A Next.js web application to browse and view podcast transcripts and summaries. Deployed on Vercel.

**Key Principle**: Start simple, make it work, then make it beautiful.

---

## Tech Stack

### Core
- **Framework**: Next.js 14 (App Router)
- **Language**: TypeScript
- **Styling**: Tailwind CSS
- **Deployment**: Vercel

### Why These Choices?
- **Next.js**: Perfect for Vercel, great performance, simple to deploy
- **TypeScript**: Catches errors early, better developer experience
- **Tailwind**: Fast styling, looks clean with minimal effort
- **No Database Needed**: Read directly from your existing file structure

---

## Architecture

### Data Source
Your existing `podcast_work/` folder structure:
```
podcast_work/
├── 20VC/
│   └── Episode_Name/
│       ├── summary.md
│       └── transcript.md
├── All In/
│   └── Episode_Name/
│       ├── summary.md
│       └── transcript.md
```

### Data Loading Strategy
- Read from filesystem at build time (Static Site Generation)
- Parse `podcast_status.json` for metadata
- Parse markdown files for content
- No database required - your files ARE the database

---

## Pages Structure

### 1. Homepage (`/`)
**URL**: `https://yoursite.com/`

**What You See**:
```
┌─────────────────────────────────────┐
│  Podcast Summaries                   │
├─────────────────────────────────────┤
│  [Cover] 20VC                        │
│  Participants: Various               │
│  Episodes: 15 transcribed, 15 summarized │
├─────────────────────────────────────┤
│  [Cover] All In                      │
│  Participants: Chamath, Jason, ...   │
│  Episodes: 8 transcribed, 8 summarized │
└─────────────────────────────────────┘
```

**Features**:
- Grid layout of podcast cards
- Each card shows cover image (we'll need to add these)
- Click any card → go to podcast detail page

### 2. Podcast Detail Page (`/podcast/[name]`)
**URL**: `https://yoursite.com/podcast/20VC`

**What You See**:
```
┌─────────────────────────────────────┐
│  ← Back to Home                      │
│                                      │
│  20VC                                │
│  15 Episodes                         │
├─────────────────────────────────────┤
│  1. Benchmark's GP, Everett Randle   │
│     Nov 10, 2025 | ✅ Summarized     │
├─────────────────────────────────────┤
│  2. Deel CEO, Alex Bouaziz           │
│     Nov 08, 2025 | ✅ Summarized     │
└─────────────────────────────────────┘
```

**Features**:
- List of all episodes for this podcast
- Each row shows: title, date, status badges
- Click episode → go to episode page

### 3. Episode Page (`/podcast/[name]/[episode]`)
**URL**: `https://yoursite.com/podcast/20VC/Benchmark-GP-Everett-Randle`

**What You See**:
```
┌─────────────────────────────────────┐
│  ← Back to 20VC                      │
│                                      │
│  Benchmark's GP, Everett Randle      │
│  [Summary] [Transcript]              │
├─────────────────────────────────────┤
│  # Summary Content                   │
│  ## Key Themes                       │
│  ...                                 │
│  "Quote here" [00:15:30] ← clickable │
└─────────────────────────────────────┘
```

**Features**:
- Toggle between Summary/Transcript tabs
- Render markdown content
- Preserve clickable timestamps (already in your summaries!)
- Clickable title links to video

---

## File Structure

```
podcast-website/
├── app/
│   ├── page.tsx                    # Homepage
│   ├── podcast/
│   │   ├── [name]/
│   │   │   ├── page.tsx           # Podcast detail
│   │   │   └── [episode]/
│   │   │       └── page.tsx       # Episode page
│   └── layout.tsx                  # Root layout
├── lib/
│   ├── podcasts.ts                 # Load podcast data
│   ├── markdown.ts                 # Parse markdown
│   └── types.ts                    # TypeScript types
├── components/
│   ├── PodcastCard.tsx
│   ├── EpisodeList.tsx
│   └── MarkdownRenderer.tsx
├── public/
│   └── covers/                     # Podcast cover images
└── podcast_work/                   # Your existing data (symlink or copy)
```

---

## Phase 1: MVP (Start Here)

### Goals
- [ ] Homepage with list of podcasts
- [ ] Basic podcast detail page
- [ ] Basic episode page showing summary
- [ ] Simple, clean styling
- [ ] Deploy to Vercel

### What We'll Build First
1. **Homepage**: Simple list of podcasts with names, hosts (if available), episode counts
2. **Podcast Page**: Episode list with titles and dates
3. **Episode Page**: Render summary.md with basic markdown styling
4. **No toggle yet**: Just show summary (transcript in Phase 2)
5. **No covers yet**: Use placeholder or just text (covers in Phase 2)

### Timeline Estimate
- Setup & data loading: 2-3 hours
- Homepage: 1 hour
- Podcast page: 1 hour
- Episode page: 2 hours
- Styling: 2 hours
- Deploy: 30 minutes
- **Total: ~8-10 hours of work**

---

## Phase 2: Enhancements

### Features to Add Later
- [ ] Cover images for podcasts
- [ ] Summary/Transcript toggle
- [ ] Search functionality
- [ ] Filter by date/status
- [ ] Participant filtering
- [ ] Weekly summaries page
- [ ] Better mobile responsive design
- [ ] Dark mode
- [ ] RSS feed

---

## Data Models (TypeScript)

```typescript
interface Podcast {
  name: string;
  slug: string;
  coverImage?: string;
  episodeCount: number;
  transcribedCount: number;
  summarizedCount: number;
  participants?: string[];
}

interface Episode {
  title: string;
  slug: string;
  podcastName: string;
  date: string;
  videoId: string;
  videoUrl: string;
  region: string;
  participants?: string[];
  hasTranscript: boolean;
  hasSummary: boolean;
  summaryPath: string;
  transcriptPath: string;
}

interface EpisodeContent {
  metadata: {
    title: string;
    podcast: string;
    date: string;
    participants?: string;
    region: string;
    videoId: string;
    videoUrl: string;
  };
  content: string;
}
```

---

## Key Technical Decisions

### 1. Static Site Generation (SSG)
**Decision**: Generate all pages at build time

**Why**:
- Fast page loads
- No server needed
- Works perfectly with Vercel
- Your content doesn't change frequently

**How**:
- Use Next.js `generateStaticParams()` to generate all podcast and episode pages
- Read files during build
- Vercel will serve static HTML

### 2. No Database
**Decision**: Read directly from file system

**Why**:
- Simpler architecture
- No database to maintain
- Your markdown files are the source of truth
- Rebuild/redeploy when content changes

**How**:
- Use Node.js `fs` module to read files at build time
- Parse `podcast_status.json` for metadata
- Parse markdown files for content

### 3. Markdown Rendering
**Decision**: Use `react-markdown` library

**Why**:
- Handles all markdown syntax
- Supports custom components
- Can preserve your clickable timestamps
- Easy to style

### 4. URL Structure
**Decision**: Use clean, readable URLs

**Examples**:
- Homepage: `/`
- Podcast: `/podcast/20vc`
- Episode: `/podcast/20vc/benchmark-gp-everett-randle`

**Why**:
- SEO friendly
- Easy to share
- Human readable

---

## Styling Approach

### Design Principles
1. **Clean & Minimal**: Lots of whitespace, clear hierarchy
2. **Readable**: Large text, good contrast
3. **Fast**: No animations (at first), focus on content
4. **Mobile-first**: Works on phones first, then desktop

### Color Scheme (Simple)
- Background: White/Light gray
- Text: Dark gray/Black
- Accents: Blue (for links and buttons)
- Status badges: Green (summarized), Yellow (transcribed only)

### Typography
- Headlines: System fonts (clean, fast loading)
- Body: Same system fonts
- Code/Timestamps: Monospace font

---

## Deployment Strategy

### Vercel Setup
1. Connect GitHub repo to Vercel
2. Vercel auto-detects Next.js
3. Set build command: `npm run build`
4. Set output directory: `.next`
5. Deploy!

### Environment Variables (if needed)
None for MVP - everything is read from files

### Redeployment Triggers
- Push to main branch = auto redeploy
- New episodes added = manual redeploy (or GitHub Action)

---

## Open Questions - ANSWERED

> **💬 COMMENT**: Where should we get podcast cover images from?
> **✅ RESPONSE**: Phase 2 feature. Will extract from YouTube channels when we add covers.

> **💬 COMMENT**: Should we show Chinese episodes differently?
> **✅ RESPONSE**: Yes, showing region as a badge. Can add language toggle later if needed.

> **💬 COMMENT**: How do we handle episode length/duration?
> **✅ RESPONSE**: Skipping for MVP. Can add later if you want it.

> **💬 COMMENT**: For the Podcasts, Participants should be the hosts. If we don't have that data, let's get it.
> **✅ RESPONSE**: Perfect! I'll create a `podcast_hosts.json` config file where you can manually specify hosts for each podcast. We'll display this on the homepage.

> **💬 COMMENT**: Can I ask you to search for and collect the Podcast cover images?
> **✅ RESPONSE**: Moved to Phase 2 to keep MVP simple. Will add covers after core functionality works.

---

## Next Steps

1. **Review this plan** - Add comments with questions or changes
2. **I'll create the project structure** - Set up Next.js app with all files
3. **Build Phase 1 MVP** - Get basic site working
4. **Deploy to Vercel** - Get it online
5. **Iterate** - Add Phase 2 features based on feedback

---

## Timeline

| Phase | Task | Time Estimate |
|-------|------|---------------|
| **Phase 0** | Plan review & iteration | 1-2 hours |
| **Phase 1** | Project setup | 1 hour |
| **Phase 1** | Data loading logic | 2 hours |
| **Phase 1** | Homepage | 1 hour |
| **Phase 1** | Podcast detail page | 1 hour |
| **Phase 1** | Episode page | 2 hours |
| **Phase 1** | Basic styling | 2 hours |
| **Phase 1** | Testing & fixes | 1 hour |
| **Phase 1** | Deploy to Vercel | 30 minutes |
| **Total Phase 1** | | **~10-12 hours** |

---

## Success Criteria

Phase 1 is successful when:
- ✅ I can see all my podcasts on the homepage
- ✅ I can click a podcast and see its episodes
- ✅ I can click an episode and read the summary
- ✅ Timestamps in summaries are clickable and work
- ✅ Site is deployed and accessible via Vercel URL
- ✅ Site looks clean and professional

---

**Ready to start?** Add your comments above, and once you approve, I'll begin building Phase 1!
