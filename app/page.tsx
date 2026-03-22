import ShareButton from '@/components/ShareButton'
import HomeContent from '@/components/HomeContent'
import StructuredData from '@/components/StructuredData'
import { generateFAQSchema } from '@/lib/schema'
import { getAllPodcasts } from '@/lib/episodes'
import { readdir, readFile } from 'fs/promises'
import { join } from 'path'
import { parseEpisodeMetadata } from '@/lib/schema'
import { parseEpisodeDate } from '@/lib/dates'

const HOMEPAGE_FAQS = [
  {
    question: 'What is Teahose?',
    answer: 'Teahose is an AI-powered summarization platform that distills leading tech and business podcasts, newsletters, and Physical AI research papers into concise, readable summaries. You can browse summaries on the website or subscribe for a free daily email digest.',
  },
  {
    question: 'How are Teahose summaries generated?',
    answer: 'Teahose uses Claude AI (Anthropic) to generate summaries from full transcripts and source content. Podcasts are transcribed via Podscan, newsletters are ingested via email, and research papers are sourced from arXiv and Semantic Scholar. Each summary includes key themes, notable quotes with timestamps, and actionable insights.',
  },
  {
    question: 'What podcasts does Teahose cover?',
    answer: 'Teahose covers 25+ leading tech and business podcasts including 20VC, All In, Acquired, Lenny\'s Podcast, The a16z Show, Lex Fridman, No Priors, BG2, Dwarkesh Podcast, and more. New episodes are processed automatically 3 times daily.',
  },
  {
    question: 'What newsletters does Teahose summarize?',
    answer: 'Teahose summarizes newsletters from Stratechery (Ben Thompson), StrictlyVC (Connie Loizos), Newcomer (Eric Newcomer), Axios Pro Rata (Dan Primack), Coatue Management, PitchBook, Data Driven VC, and others. Newsletters are processed in real-time as they arrive.',
  },
  {
    question: 'What are the Physical AI paper summaries?',
    answer: 'Teahose automatically discovers and summarizes top Physical AI research papers daily from arXiv, Semantic Scholar, and HuggingFace. Papers are scored by relevance, novelty, impact, and lab pedigree (tracking labs like Physical Intelligence, Google DeepMind, Toyota Research Institute, MIT, Stanford, and others). The top 1-2 papers per day are summarized with key findings and links to the original arXiv papers.',
  },
  {
    question: 'How does the daily email digest work?',
    answer: 'Subscribe for free on teahose.com. Every morning at 6 AM EST, you receive an email with AI-generated summaries of all new podcast episodes, newsletter issues, and research papers published in the last 24 hours. Each summary takes about 30 seconds to read, covering 2-5 hours of original content.',
  },
  {
    question: 'Is Teahose free?',
    answer: 'Yes. Teahose is completely free. You can browse all summaries on teahose.com or subscribe to the daily email digest at no cost.',
  },
  {
    question: 'How is Teahose different from Snipd, Podsnacks, or other podcast summary tools?',
    answer: 'Unlike self-service tools where you paste a podcast URL, Teahose is a curated platform. It automatically selects, transcribes, and summarizes content from a curated list of top tech and business podcasts, newsletters, AND research papers — all in one place. Summaries include clickable YouTube timestamps, speaker attribution, and key themes. You get a single daily digest instead of managing multiple tools.',
  },
]

interface Podcast {
  name: string
  title: string
  description?: string
  episodeCount: number
}

interface RecentEpisode {
  slug: string
  title: string
  date: string
  podcast: string
  podcastName: string
  source?: string
}

/**
 * Get recent episodes for homepage (server-side)
 */
async function getRecentEpisodes(): Promise<RecentEpisode[]> {
  try {
    const podcastWorkDir = join(process.cwd(), 'podcast_work')
    const podcastDirs = await readdir(podcastWorkDir, { withFileTypes: true })

    const allEpisodes: Array<RecentEpisode & { dateObj: Date; sortDate: Date }> = []

    for (const podcastDir of podcastDirs) {
      if (!podcastDir.isDirectory()) continue

      const podcastPath = join(podcastWorkDir, podcastDir.name)
      const episodeDirs = await readdir(podcastPath, { withFileTypes: true })

      for (const episodeDir of episodeDirs) {
        if (!episodeDir.isDirectory()) continue

        try {
          const summaryPath = join(podcastPath, episodeDir.name, 'summary.md')
          const summaryContent = await readFile(summaryPath, 'utf-8')
          const metadata = parseEpisodeMetadata(summaryContent)

          if (!metadata.date) continue
          const dateObj = parseEpisodeDate(metadata.date)
          if (!dateObj) continue

          // Use Processed timestamp (precise) for sorting, fall back to Date (day-only)
          const processedDate = metadata.processed ? parseEpisodeDate(metadata.processed) : null
          const sortDate = processedDate || dateObj

          allEpisodes.push({
            slug: episodeDir.name,
            title: metadata.title || episodeDir.name,
            date: metadata.date,
            podcast: podcastDir.name,
            podcastName: metadata.podcast || podcastDir.name,
            source: metadata.source,
            dateObj,
            sortDate,
          })
        } catch {
          // Skip episodes that can't be read
        }
      }
    }

    return allEpisodes
      .sort((a, b) => b.sortDate.getTime() - a.sortDate.getTime())
      .map(({ dateObj, sortDate, ...episode }) => episode)
  } catch {
    return []
  }
}

/**
 * Get all podcasts, newsletters, and papers for homepage (server-side)
 * Separates them by checking config files and episode source metadata
 */
async function getSources(recentEpisodes: RecentEpisode[]): Promise<{ podcasts: Podcast[], newsletters: Podcast[], papers: Podcast[] }> {
  const allPodcasts = await getAllPodcasts()

  // Load newsletter_config.json to identify newsletter sources
  const newsletterNames: Set<string> = new Set()
  try {
    const configPath = join(process.cwd(), 'newsletter_config.json')
    const configContent = await readFile(configPath, 'utf-8')
    const config = JSON.parse(configContent)
    for (const entry of Object.values(config) as Array<{ name?: string }>) {
      if (entry.name) newsletterNames.add(entry.name)
    }
  } catch {
    // No config file
  }

  // Identify paper sources from episode metadata
  const paperSourceNames: Set<string> = new Set()
  for (const ep of recentEpisodes) {
    if (ep.source === 'paper') {
      paperSourceNames.add(ep.podcastName)
    }
  }

  const podcasts: Podcast[] = []
  const newsletters: Podcast[] = []
  const papers: Podcast[] = []

  for (const p of allPodcasts) {
    const item = {
      name: p.name,
      title: p.title,
      description: p.description,
      episodeCount: p.episodes.length,
    }
    if (paperSourceNames.has(p.name)) {
      papers.push(item)
    } else if (newsletterNames.has(p.name)) {
      newsletters.push(item)
    } else {
      podcasts.push(item)
    }
  }

  return { podcasts, newsletters, papers }
}

/**
 * Server Component - generates static HTML at build time
 */
export default async function HomePage() {
  const recentEpisodes = await getRecentEpisodes()
  const { podcasts, newsletters, papers } = await getSources(recentEpisodes)

  return (
    <main className="min-h-screen" style={{ backgroundColor: 'var(--background)' }}>
      <StructuredData data={generateFAQSchema(HOMEPAGE_FAQS)} />

      {/* Header */}
      <header style={{ borderBottomColor: 'var(--border)' }} className="border-b">
        <div className="container pt-12 md:pt-16 pb-6">
          <div className="flex items-center justify-between mb-6">
            <h1 style={{ color: 'var(--foreground)' }}>Teahose</h1>
            <ShareButton refSource="home" />
          </div>
          <p style={{ color: 'var(--muted-foreground)' }} className="text-lg">
            A distillation of leading tech & business podcasts, newsletters, and research papers. Browse summaries here or sub for daily digests delivering hours of insight in 30 seconds.
          </p>
        </div>
      </header>

      {/* Content with tabs */}
      <HomeContent podcasts={podcasts} newsletters={newsletters} papers={papers} recentEpisodes={recentEpisodes} />

      {/* FAQ Section */}
      <section className="container py-12 md:py-16" style={{ borderTopColor: 'var(--border)' }}>
        <h2 style={{ color: 'var(--foreground)' }} className="mb-8">Frequently Asked Questions</h2>
        <div className="grid gap-6">
          {HOMEPAGE_FAQS.map((faq) => (
            <details key={faq.question} className="group" style={{ borderBottomColor: 'var(--border)' }}>
              <summary
                className="cursor-pointer py-4 text-lg font-medium list-none flex items-center justify-between"
                style={{ color: 'var(--foreground)' }}
              >
                {faq.question}
                <span style={{ color: 'var(--muted-foreground)' }} className="text-sm ml-4 group-open:rotate-180 transition-transform">▼</span>
              </summary>
              <p style={{ color: 'var(--muted-foreground)' }} className="pb-4 text-sm leading-relaxed">
                {faq.answer}
              </p>
            </details>
          ))}
        </div>
      </section>
    </main>
  )
}
