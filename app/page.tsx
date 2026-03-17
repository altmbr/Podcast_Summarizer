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
 * Get all podcasts and newsletters for homepage (server-side)
 * Separates them by checking if any episode has source: newsletter
 */
async function getSources(): Promise<{ podcasts: Podcast[], newsletters: Podcast[] }> {
  const allPodcasts = await getAllPodcasts()

  // Also load newsletter_config.json to identify newsletter sources
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

  const podcasts: Podcast[] = []
  const newsletters: Podcast[] = []

  for (const p of allPodcasts) {
    const item = {
      name: p.name,
      title: p.title,
      description: p.description,
      episodeCount: p.episodes.length,
    }
    if (newsletterNames.has(p.name)) {
      newsletters.push(item)
    } else {
      podcasts.push(item)
    }
  }

  return { podcasts, newsletters }
}

/**
 * Server Component - generates static HTML at build time
 */
export default async function HomePage() {
  const [{ podcasts, newsletters }, recentEpisodes] = await Promise.all([
    getSources(),
    getRecentEpisodes(),
  ])

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
            A distillation of leading tech & business podcasts and newsletters. Browse summaries here or sub for daily digests delivering hours of insight in 30 seconds.
          </p>
        </div>
      </header>

      {/* Content with tabs */}
      <HomeContent podcasts={podcasts} newsletters={newsletters} recentEpisodes={recentEpisodes} />
    </main>
  )
}
