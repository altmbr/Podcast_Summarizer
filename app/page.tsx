import ShareButton from '@/components/ShareButton'
import HomeContent from '@/components/HomeContent'
import { getAllPodcasts } from '@/lib/episodes'
import { readdir, readFile } from 'fs/promises'
import { join } from 'path'
import { parseEpisodeMetadata } from '@/lib/schema'
import { parseEpisodeDate } from '@/lib/dates'

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
    </main>
  )
}
