'use client'

import Link from 'next/link'
import { useState, useEffect } from 'react'
import { useParams } from 'next/navigation'

interface Episode {
  slug: string
  title: string
  date?: string
  summary?: string
}

export default function PodcastPage() {
  const params = useParams()
  const podcastName = params.name as string
  const [podcast, setPodcast] = useState<any>(null)
  const [episodes, setEpisodes] = useState<Episode[]>([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState<string | null>(null)

  useEffect(() => {
    const loadEpisodes = async () => {
      try {
        const response = await fetch(`/api/podcasts/${podcastName}`)
        if (!response.ok) {
          throw new Error(`API error: ${response.status}`)
        }
        const data = await response.json()
        setPodcast(data.podcast)
        setEpisodes(data.episodes)
      } catch (error) {
        console.error('[v0] Failed to load episodes:', error)
        setError('Failed to load episodes')
      } finally {
        setLoading(false)
      }
    }

    if (podcastName) {
      loadEpisodes()
    }
  }, [podcastName])

  return (
    <main className="min-h-screen" style={{ backgroundColor: 'var(--background)' }}>
      {/* Header */}
      <header style={{ borderBottomColor: 'var(--border)' }} className="border-b">
        <div className="container py-8 md:py-12">
          <Link href="/" style={{ color: 'var(--muted-foreground)' }} className="hover:underline mb-4 block text-sm">
            ← Back to Podcasts
          </Link>
          <h1 style={{ color: 'var(--foreground)' }} className="mb-2">{podcast?.title || podcastName}</h1>
          {podcast?.description && (
            <p style={{ color: 'var(--muted-foreground)' }} className="max-w-2xl">{podcast.description}</p>
          )}
        </div>
      </header>

      {/* Episodes */}
      <section className="container py-12 md:py-16">
        {loading ? (
          <div style={{ color: 'var(--muted-foreground)' }} className="text-center py-12">Loading episodes...</div>
        ) : error ? (
          <div style={{ color: 'var(--muted-foreground)' }} className="text-center py-12">{error}</div>
        ) : episodes.length === 0 ? (
          <div style={{ color: 'var(--muted-foreground)' }} className="text-center py-12">No episodes found</div>
        ) : (
          <div className="space-y-4 md:space-y-6">
            {episodes.map((episode) => (
              <Link
                key={episode.slug}
                href={`/podcast/${podcastName}/${episode.slug}`}
                className="group block p-6 rounded-sm hover:opacity-80 transition-all"
                style={{
                  backgroundColor: 'var(--card)',
                  borderColor: 'var(--border)',
                  color: 'var(--foreground)',
                }}
              >
                <div className="flex items-start justify-between gap-4">
                  <div className="flex-1 min-w-0">
                    <h3 className="text-lg md:text-xl group-hover:underline transition-colors mb-2">
                      {episode.title}
                    </h3>
                    {episode.date && (
                      <p style={{ color: 'var(--muted-foreground)' }} className="text-sm mb-3">{episode.date}</p>
                    )}
                    {episode.summary && (
                      <p style={{ color: 'var(--muted-foreground)' }} className="text-sm line-clamp-2">{episode.summary}</p>
                    )}
                  </div>
                  <span style={{ color: 'var(--accent)' }} className="font-light text-lg flex-shrink-0">→</span>
                </div>
              </Link>
            ))}
          </div>
        )}
      </section>

      {/* Footer */}
      <footer style={{ borderTopColor: 'var(--border)' }} className="border-t mt-16 md:mt-20">
        <div style={{ color: 'var(--muted-foreground)' }} className="container py-8 text-center text-sm">
          <p>Discover the insights within each episode.</p>
        </div>
      </footer>
    </main>
  )
}
