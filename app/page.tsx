import ShareButton from '@/components/ShareButton'
import HomeContent from '@/components/HomeContent'
import { getAllPodcasts } from '@/lib/episodes'
import { readdir, readFile } from 'fs/promises'
import { join } from 'path'
import { parseEpisodeMetadata } from '@/lib/schema'

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
}

/**
 * Get recent episodes for homepage (server-side)
 */
async function getRecentEpisodes(): Promise<RecentEpisode[]> {
  try {
    const podcastWorkDir = join(process.cwd(), 'podcast_work')
    const podcastDirs = await readdir(podcastWorkDir, { withFileTypes: true })

    const allEpisodes: Array<RecentEpisode & { dateObj: Date }> = []

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

          if (metadata.date) {
            allEpisodes.push({
              slug: episodeDir.name,
              title: metadata.title || episodeDir.name,
              date: metadata.date,
              podcast: podcastDir.name,
              podcastName: metadata.podcast || podcastDir.name,
              dateObj: new Date(metadata.date)
            })
          }
        } catch {
          // Skip episodes that can't be read
        }
      }
    }

    return allEpisodes
      .sort((a, b) => b.dateObj.getTime() - a.dateObj.getTime())
      .map(({ dateObj, ...episode }) => episode)
  } catch {
    return []
  }
}

/**
 * Get all podcasts for homepage (server-side)
 */
async function getPodcasts(): Promise<Podcast[]> {
  const allPodcasts = await getAllPodcasts()
  return allPodcasts.map(p => ({
    name: p.name,
    title: p.title,
    description: p.description,
    episodeCount: p.episodes.length,
  }))
}

/**
 * Server Component - generates static HTML at build time
 */
export default async function HomePage() {
  const [podcasts, recentEpisodes] = await Promise.all([
    getPodcasts(),
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
            A distillation of leading tech & business podcasts. Browse summaries here or sub for daily digests delivering 2-5 hours of insight in 30 seconds.
          </p>
        </div>
      </header>

      {/* Content with tabs */}
      <HomeContent podcasts={podcasts} recentEpisodes={recentEpisodes} />
    </main>
  )
}
