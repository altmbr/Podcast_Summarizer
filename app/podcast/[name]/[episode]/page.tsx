'use client'

import Link from 'next/link'
import { useState, useEffect } from 'react'
import { useParams } from 'next/navigation'
import MarkdownRenderer from '@/components/MarkdownRenderer'

interface EpisodeData {
  title: string
  date?: string
  podcast?: string
  participants?: string
  region?: string
  videoUrl?: string
  summary?: string
  transcript?: string
}

export default function EpisodePage() {
  const params = useParams()
  const podcastName = params.name as string
  const episodeSlug = params.episode as string
  const [episode, setEpisode] = useState<EpisodeData | null>(null)
  const [activeTab, setActiveTab] = useState<'summary' | 'transcript'>('summary')
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState<string | null>(null)

  useEffect(() => {
    const loadEpisode = async () => {
      try {
        const decodedName = decodeURIComponent(podcastName)
        const decodedSlug = decodeURIComponent(episodeSlug)
        const response = await fetch(`/api/podcasts/${encodeURIComponent(decodedName)}/${encodeURIComponent(decodedSlug)}`)
        if (!response.ok) {
          throw new Error(`API error: ${response.status}`)
        }
        const data = await response.json()
        setEpisode(data)
      } catch (error) {
        console.error('Failed to load episode:', error)
        setError('Failed to load episode')
      } finally {
        setLoading(false)
      }
    }

    if (podcastName && episodeSlug) {
      loadEpisode()
    }
  }, [podcastName, episodeSlug])

  return (
    <main className="min-h-screen" style={{ backgroundColor: 'var(--background)' }}>
      {/* Header */}
      <header style={{ borderBottomColor: 'var(--border)' }} className="border-b">
        <div className="container py-8 md:py-12">
          <Link
            href={`/podcast/${encodeURIComponent(podcastName)}`}
            style={{ color: 'var(--muted-foreground)' }}
            className="hover:underline mb-4 block text-sm"
          >
            ← Back to Episodes
          </Link>
          <h1 style={{ color: 'var(--foreground)' }} className="mb-4">{episode?.title || 'Loading...'}</h1>
          {episode?.date && <p style={{ color: 'var(--muted-foreground)' }} className="text-sm mb-2">{formatDate(episode.date)}</p>}
          {episode?.participants && <p style={{ color: 'var(--muted-foreground)' }} className="text-sm">{episode.participants}</p>}
        </div>
      </header>

      {/* Content Tabs */}
      <section className="container py-8 md:py-12">
        <div style={{ borderBottomColor: 'var(--border)' }} className="flex gap-2 mb-8 border-b pb-4">
          <button
            onClick={() => setActiveTab('summary')}
            style={{
              color: activeTab === 'summary' ? 'var(--accent)' : 'var(--muted-foreground)',
              borderBottomColor: activeTab === 'summary' ? 'var(--accent)' : 'transparent',
            }}
            className="px-4 py-2 text-sm font-medium transition-colors border-b-2"
          >
            Summary
          </button>
          <button
            onClick={() => setActiveTab('transcript')}
            style={{
              color: activeTab === 'transcript' ? 'var(--accent)' : 'var(--muted-foreground)',
              borderBottomColor: activeTab === 'transcript' ? 'var(--accent)' : 'transparent',
            }}
            className="px-4 py-2 text-sm font-medium transition-colors border-b-2"
          >
            Transcript
          </button>
        </div>

        {loading ? (
          <div style={{ color: 'var(--muted-foreground)' }} className="text-center py-12">Loading episode...</div>
        ) : error ? (
          <div style={{ color: 'var(--muted-foreground)' }} className="text-center py-12">{error}</div>
        ) : (
          <div>
            {activeTab === 'summary' && episode?.summary ? (
              <MarkdownRenderer content={episode.summary} />
            ) : activeTab === 'transcript' && episode?.transcript ? (
              <MarkdownRenderer content={episode.transcript} />
            ) : (
              <p style={{ color: 'var(--muted-foreground)' }}>No content available</p>
            )}
          </div>
        )}
      </section>

      {/* Footer */}
      <footer style={{ borderTopColor: 'var(--border)' }} className="border-t mt-16 md:mt-20">
        <div style={{ color: 'var(--muted-foreground)' }} className="container py-8 text-center text-sm">
          <p>Reflect on the key insights from this episode.</p>
        </div>
      </footer>
    </main>
  )
}

function formatDate(dateStr: string): string {
  if (!dateStr || dateStr === 'Unknown') return 'Unknown'

  try {
    // Handle YYYY-MM-DD format
    if (/^\d{4}-\d{2}-\d{2}$/.test(dateStr)) {
      const date = new Date(dateStr)
      return date.toLocaleDateString('en-US', {
        year: 'numeric',
        month: 'long',
        day: 'numeric'
      })
    }
    // Handle YYYYMMDD format
    if (/^\d{8}$/.test(dateStr)) {
      const year = dateStr.substring(0, 4)
      const month = dateStr.substring(4, 6)
      const day = dateStr.substring(6, 8)
      const date = new Date(`${year}-${month}-${day}`)
      return date.toLocaleDateString('en-US', {
        year: 'numeric',
        month: 'long',
        day: 'numeric'
      })
    }
    // Handle full date strings
    const date = new Date(dateStr)
    if (!isNaN(date.getTime())) {
      return date.toLocaleDateString('en-US', {
        year: 'numeric',
        month: 'long',
        day: 'numeric'
      })
    }
    return dateStr
  } catch {
    return dateStr
  }
}
