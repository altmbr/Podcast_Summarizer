'use client'

import Link from 'next/link'
import { useState, useEffect } from 'react'

interface Podcast {
  name: string
  title: string
  description?: string
  episodeCount?: number
}

export default function HomePage() {
  const [podcasts, setPodcasts] = useState<Podcast[]>([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState<string | null>(null)

  useEffect(() => {
    const loadPodcasts = async () => {
      try {
        const response = await fetch('/api/podcasts')
        if (!response.ok) {
          throw new Error(`API error: ${response.status}`)
        }
        const data = await response.json()
        setPodcasts(data)
      } catch (error) {
        console.error('Failed to load podcasts:', error)
        setError('Failed to load podcasts')
      } finally {
        setLoading(false)
      }
    }

    loadPodcasts()
  }, [])

  return (
    <main className="min-h-screen" style={{ backgroundColor: 'var(--background)' }}>
      {/* Header */}
      <header style={{ borderBottomColor: 'var(--border)' }} className="border-b">
        <div className="container py-12 md:py-16">
          <h1 style={{ color: 'var(--foreground)' }} className="mb-2">Teahose</h1>
          <p style={{ color: 'var(--muted-foreground)' }} className="text-lg">
            Summaries of the most important tech podcasts — including China's.
            <br />
            Browse episodes here, and subscribe for the weekly briefing that distills 30+ hours of podcasts into a 5-minute read.
          </p>
        </div>
      </header>

      {/* Podcasts Grid */}
      <section className="container py-12 md:py-16">
        {loading ? (
          <div style={{ color: 'var(--muted-foreground)' }} className="text-center py-12">Loading podcasts...</div>
        ) : error ? (
          <div style={{ color: 'var(--muted-foreground)' }} className="text-center py-12">{error}</div>
        ) : podcasts.length === 0 ? (
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
                <h2 className="text-2xl md:text-3xl group-hover:underline transition-colors mb-2">
                  {podcast.title}
                </h2>
                {podcast.description && (
                  <p style={{ color: 'var(--muted-foreground)' }} className="mb-4 line-clamp-2">{podcast.description}</p>
                )}
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

      {/* Footer */}
      <footer style={{ borderTopColor: 'var(--border)' }} className="border-t mt-16 md:mt-20">
        <div style={{ color: 'var(--muted-foreground)' }} className="container py-8 text-center text-sm">
          <p>Explore, learn, and reflect on compelling ideas.</p>
        </div>
      </footer>
    </main>
  )
}
