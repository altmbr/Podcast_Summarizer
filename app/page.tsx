import Link from 'next/link'
import ShareButton from '@/components/ShareButton'
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
      if (!podcastDir.isDirectory() || podcastDir.name === 'one off episodes') continue

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
      .slice(0, 10)
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
            <ShareButton />
          </div>
          <p style={{ color: 'var(--muted-foreground)' }} className="text-lg">
            A distillation of leading tech & business podcasts. Browse summaries here or sub for daily digests delivering 2-5 hours of insight in 30 seconds.
          </p>
        </div>
      </header>

      {/* Recent Episodes Section */}
      <section className="container pt-6 pb-8 md:pb-8">
        <h2 style={{ color: 'var(--foreground)' }} className="text-3xl md:text-4xl mb-6">Recent Episodes</h2>
        {recentEpisodes.length === 0 ? (
          <div style={{ color: 'var(--muted-foreground)' }} className="text-center py-12">No recent episodes found</div>
        ) : (
          <div className="grid gap-6 md:gap-8">
            {recentEpisodes.map((episode) => (
              <Link
                key={`${episode.podcast}-${episode.slug}`}
                href={`/podcast/${encodeURIComponent(episode.podcast)}/${encodeURIComponent(episode.slug)}`}
                className="group block p-6 md:p-8 rounded-sm transition-all hover:opacity-80"
                style={{
                  backgroundColor: 'var(--card)',
                  borderColor: 'var(--border)',
                  color: 'var(--foreground)',
                }}
              >
                <h3 className="text-2xl md:text-3xl group-hover:underline transition-colors mb-2">
                  {episode.title}
                </h3>
                <div className="flex items-center justify-between">
                  <span style={{ color: 'var(--muted-foreground)' }} className="text-sm">
                    {episode.date}
                  </span>
                  <span style={{ color: 'var(--accent)' }} className="font-light">→</span>
                </div>
              </Link>
            ))}
          </div>
        )}
      </section>

      {/* Podcasts Section */}
      <section className="container pt-8 md:pt-8 pb-8">
        <h2 style={{ color: 'var(--foreground)' }} className="text-3xl md:text-4xl mb-6">Podcasts</h2>
        {podcasts.length === 0 ? (
          <div style={{ color: 'var(--muted-foreground)' }} className="text-center py-12">No podcasts found</div>
        ) : (
          <div className="grid gap-6 md:gap-8">
            {podcasts.map((podcast) => (
              <Link
                key={podcast.name}
                href={`/podcast/${encodeURIComponent(podcast.name)}`}
                className="group block p-6 md:p-8 rounded-sm transition-all hover:opacity-80"
                style={{
                  backgroundColor: 'var(--card)',
                  borderColor: 'var(--border)',
                  color: 'var(--foreground)',
                }}
              >
                <h3 className="text-2xl md:text-3xl group-hover:underline transition-colors mb-2">
                  {podcast.title}
                </h3>
                <div className="flex items-center justify-between">
                  <span style={{ color: 'var(--muted-foreground)' }} className="text-sm">
                    {podcast.episodeCount || 0} episodes
                  </span>
                  <span style={{ color: 'var(--accent)' }} className="font-light">→</span>
                </div>
              </Link>
            ))}
          </div>
        )}
      </section>
    </main>
  )
}
