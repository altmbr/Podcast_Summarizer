'use client'

import { useState } from 'react'
import Link from 'next/link'

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

interface HomeContentProps {
  podcasts: Podcast[]
  recentEpisodes: RecentEpisode[]
}

type Tab = 'episodes' | 'podcasts'

export default function HomeContent({ podcasts, recentEpisodes }: HomeContentProps) {
  const [activeTab, setActiveTab] = useState<Tab>('episodes')
  const [displayCount, setDisplayCount] = useState(20)

  const visibleEpisodes = recentEpisodes.slice(0, displayCount)
  const hasMore = displayCount < recentEpisodes.length

  const handleLoadMore = () => {
    setDisplayCount(prev => Math.min(prev + 20, recentEpisodes.length))
  }

  return (
    <>
      {/* Tab Toggle */}
      <section className="container pt-6 pb-0">
        <div className="flex gap-0 border-b" style={{ borderBottomColor: 'var(--border)' }}>
          <button
            onClick={() => setActiveTab('episodes')}
            className="px-6 py-3 text-xl md:text-2xl font-medium transition-colors relative"
            style={{
              color: activeTab === 'episodes' ? 'var(--foreground)' : 'var(--muted-foreground)',
              borderBottom: activeTab === 'episodes' ? '2px solid var(--accent)' : '2px solid transparent',
            }}
          >
            Recent Episodes
          </button>
          <button
            onClick={() => setActiveTab('podcasts')}
            className="px-6 py-3 text-xl md:text-2xl font-medium transition-colors relative"
            style={{
              color: activeTab === 'podcasts' ? 'var(--foreground)' : 'var(--muted-foreground)',
              borderBottom: activeTab === 'podcasts' ? '2px solid var(--accent)' : '2px solid transparent',
            }}
          >
            Podcasts
          </button>
        </div>
      </section>

      {/* Recent Episodes Section */}
      {activeTab === 'episodes' && (
        <section className="container pt-6 pb-8 md:pb-8">
          {recentEpisodes.length === 0 ? (
            <div style={{ color: 'var(--muted-foreground)' }} className="text-center py-12">
              No recent episodes found
            </div>
          ) : (
            <>
              <div className="grid gap-6 md:gap-8">
                {visibleEpisodes.map((episode) => (
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
                        {episode.podcastName} · {episode.date}
                      </span>
                      <span style={{ color: 'var(--accent)' }} className="font-light">→</span>
                    </div>
                  </Link>
                ))}
              </div>

              {/* Episode count and Load More */}
              <div className="mt-8 flex flex-col items-center gap-4">
                <div style={{ color: 'var(--muted-foreground)' }} className="text-sm">
                  Showing {visibleEpisodes.length} of {recentEpisodes.length} episodes
                </div>
                {hasMore && (
                  <button
                    onClick={handleLoadMore}
                    className="px-8 py-3 rounded-sm font-medium transition-all hover:opacity-80"
                    style={{
                      backgroundColor: 'var(--accent)',
                      color: 'white',
                    }}
                  >
                    Load More
                  </button>
                )}
              </div>
            </>
          )}
        </section>
      )}

      {/* Podcasts Section */}
      {activeTab === 'podcasts' && (
        <section className="container pt-6 pb-8 md:pb-8">
          {podcasts.length === 0 ? (
            <div style={{ color: 'var(--muted-foreground)' }} className="text-center py-12">
              No podcasts found
            </div>
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
      )}
    </>
  )
}
