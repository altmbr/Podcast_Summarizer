'use client'
// Updated to show 10 recent episodes
import Link from 'next/link'
import { useState, useEffect } from 'react'
import ShareButton from '@/components/ShareButton'

interface Podcast {
  name: string
  title: string
  description?: string
  episodeCount?: number
}

interface RecentEpisode {
  slug: string
  title: string
  date: string
  podcast: string
  podcastName: string
}

export default function HomePage() {
  const [podcasts, setPodcasts] = useState<Podcast[]>([])
  const [recentEpisodes, setRecentEpisodes] = useState<RecentEpisode[]>([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState<string | null>(null)

  useEffect(() => {
    const loadData = async () => {
      try {
        // Load both podcasts and recent episodes in parallel
        const [podcastsResponse, episodesResponse] = await Promise.all([
          fetch('/api/podcasts'),
          fetch('/api/recent-episodes')
        ])

        if (!podcastsResponse.ok || !episodesResponse.ok) {
          throw new Error('API error')
        }

        const [podcastsData, episodesData] = await Promise.all([
          podcastsResponse.json(),
          episodesResponse.json()
        ])

        setPodcasts(podcastsData)
        setRecentEpisodes(episodesData)
      } catch (error) {
        console.error('Failed to load data:', error)
        setError('Failed to load data')
      } finally {
        setLoading(false)
      }
    }

    loadData()
  }, [])

  return (
    <main className="min-h-screen" style={{ backgroundColor: 'var(--background)' }}>
      {/* Header */}
      <header style={{ borderBottomColor: 'var(--border)' }} className="border-b">
        <div className="container py-12 md:py-16">
          <div className="flex items-center justify-between mb-2">
            <h1 style={{ color: 'var(--foreground)' }}>Teahose</h1>
            <ShareButton />
          </div>
          <p style={{ color: 'var(--muted-foreground)' }} className="text-lg">
            Summaries of the most important tech podcasts — including China's.
            <br />
            Browse episodes here, and subscribe for the weekly briefing that distills 30+ hours of podcasts into a 5-minute read.
          </p>
        </div>
      </header>

      {loading ? (
        <div style={{ color: 'var(--muted-foreground)' }} className="text-center py-12">Loading...</div>
      ) : error ? (
        <div style={{ color: 'var(--muted-foreground)' }} className="text-center py-12">{error}</div>
      ) : (
        <>
          {/* Recent Episodes Section */}
          <section className="container pt-12 md:pt-16 pb-8 md:pb-8">
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
          <section className="container pt-8 md:pt-8 pb-24">
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
        </>
      )}
    </main>
  )
}
