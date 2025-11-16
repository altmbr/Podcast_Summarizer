# Podcast Summaries Website

A Next.js website for browsing and viewing AI-generated podcast summaries.

## Features

- **Homepage**: Grid view of all podcasts with episode counts and hosts
- **Podcast Detail Pages**: List of all episodes for each podcast
- **Episode Pages**: Full summary with clickable timestamps
- **Static Site Generation**: Fast, pre-rendered pages
- **Responsive Design**: Clean, mobile-friendly interface

## Tech Stack

- **Next.js 16**: React framework with App Router
- **TypeScript**: Type-safe code
- **Tailwind CSS 4**: Utility-first styling
- **React Markdown**: Render markdown summaries
- **Vercel**: Deployment platform

## Project Structure

```
podcast-website/
├── app/                           # Next.js App Router pages
│   ├── page.tsx                  # Homepage
│   ├── podcast/[name]/
│   │   ├── page.tsx             # Podcast detail page
│   │   └── [episode]/page.tsx   # Episode page
│   ├── layout.tsx               # Root layout
│   └── globals.css              # Global styles
├── components/
│   └── MarkdownRenderer.tsx     # Markdown rendering component
├── lib/
│   ├── podcasts.ts              # Data loading utilities
│   ├── markdown.ts              # Markdown parsing
│   └── types.ts                 # TypeScript types
├── podcast_hosts.json           # Podcast hosts configuration
└── public/                      # Static assets
```

## Data Source

The website reads data from:
- `../podcast_status.json` - Episode metadata and status
- `../podcast_work/` - Episode folders with summary.md and transcript.md files

## Local Development

### Prerequisites

- Node.js 18+
- npm or yarn
- The podcast_status.json file in the parent directory
- podcast_work/ folder with episode content

### Installation

```bash
# Install dependencies
npm install

# Run development server
npm run dev
```

Visit http://localhost:3000 to view the website.

### Build for Production

```bash
# Generate static site
npm run build

# Preview production build
npm run start
```

## Configuration

### Adding Podcast Hosts

Edit `podcast_hosts.json` to add or update podcast hosts:

```json
{
  "Podcast Name": {
    "hosts": ["Host 1", "Host 2"],
    "description": "Brief description"
  }
}
```

### Environment Variables

None required! The site reads from local files.

## Deployment to Vercel

### Option 1: GitHub Integration (Recommended)

1. Push code to GitHub repository
2. Visit [vercel.com](https://vercel.com)
3. Click "Import Project"
4. Select your GitHub repository
5. Vercel auto-detects Next.js configuration
6. Click "Deploy"

Vercel will automatically:
- Detect Next.js framework
- Run `npm run build`
- Deploy static files
- Provide a live URL

### Option 2: Vercel CLI

```bash
# Install Vercel CLI
npm i -g vercel

# Login to Vercel
vercel login

# Deploy
vercel
```

### Deployment Configuration

The `next.config.js` is already configured for static export:

```javascript
module.exports = {
  output: 'export',
  images: {
    unoptimized: true,
  },
}
```

### Redeployment

To update the website after adding new episodes:

1. Run `podcast_summarizer.py` to process new episodes
2. Commit changes to Git
3. Push to GitHub
4. Vercel automatically redeploys (if using GitHub integration)

Or manually:
```bash
vercel --prod
```

## URL Structure

- Homepage: `/`
- Podcast: `/podcast/20vc`
- Episode: `/podcast/20vc/episode-slug`

All URLs are SEO-friendly and human-readable.

## Features Roadmap

### Phase 1 (Complete)
- ✅ Homepage with podcast list
- ✅ Podcast detail pages
- ✅ Episode pages with summaries
- ✅ Responsive styling
- ✅ Static site generation

### Phase 2 (Future)
- [ ] Podcast cover images
- [ ] Summary/Transcript toggle
- [ ] Search functionality
- [ ] Date/status filters
- [ ] Dark mode
- [ ] RSS feed

## Troubleshooting

### "Cannot find podcast_status.json"
- Ensure `podcast_status.json` is in the parent directory
- Check that the path in `lib/podcasts.ts` is correct

### "No podcasts found"
- Run `podcast_summarizer.py` to generate episodes
- Check that `podcast_status.json` has content

### Build fails
- Delete `.next` folder and rebuild
- Check that all dependencies are installed
- Ensure TypeScript has no errors

## License

Same as main podcast summarizer project.
