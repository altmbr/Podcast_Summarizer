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
  source?: string
}

interface HomeContentProps {
  podcasts: Podcast[]
  newsletters: Podcast[]
  papers: Podcast[]
  recentEpisodes: RecentEpisode[]
}

type Tab = 'episodes' | 'podcasts' | 'newsletters' | 'papers'

const TABS: { id: Tab; label: string; resetsCount?: boolean }[] = [
  { id: 'episodes', label: 'Recent Content', resetsCount: true },
  { id: 'podcasts', label: 'Podcasts' },
  { id: 'newsletters', label: 'Newsletters', resetsCount: true },
  { id: 'papers', label: 'Papers', resetsCount: true },
]

interface TabButtonProps {
  tab: typeof TABS[number]
  isActive: boolean
  onClick: () => void
}

function TabButton({ tab, isActive, onClick }: TabButtonProps) {
  return (
    <button
      onClick={onClick}
      className="px-6 py-3 text-xl md:text-2xl font-medium transition-colors relative"
      style={{
        color: isActive ? 'var(--foreground)' : 'var(--muted-foreground)',
        borderBottom: isActive ? '2px solid var(--accent)' : '2px solid transparent',
      }}
    >
      {tab.label}
    </button>
  )
}

interface SourceCardProps {
  title: string
  subtitle: string
  href: string
}

function SourceCard({ title, subtitle, href }: SourceCardProps) {
  return (
    <Link
      href={href}
      className="group block p-6 md:p-8 rounded-sm transition-all hover:opacity-80"
      style={{
        backgroundColor: 'var(--card)',
        borderColor: 'var(--border)',
        color: 'var(--foreground)',
      }}
    >
      <h3 className="text-2xl md:text-3xl group-hover:underline transition-colors mb-2">
        {title}
      </h3>
      <div className="flex items-center justify-between">
        <span style={{ color: 'var(--muted-foreground)' }} className="text-sm">
          {subtitle}
        </span>
        <span style={{ color: 'var(--accent)' }} className="font-light">→</span>
      </div>
    </Link>
  )
}

function EmptyState({ message }: { message: string }) {
  return (
    <div style={{ color: 'var(--muted-foreground)' }} className="text-center py-12">
      {message}
    </div>
  )
}

export default function HomeContent({ podcasts, newsletters, papers, recentEpisodes }: HomeContentProps) {
  const [activeTab, setActiveTab] = useState<Tab>('episodes')
  const [displayCount, setDisplayCount] = useState(20)

  const visibleEpisodes = recentEpisodes.slice(0, displayCount)
  const hasMore = displayCount < recentEpisodes.length

  function handleLoadMore() {
    setDisplayCount(prev => Math.min(prev + 20, recentEpisodes.length))
  }

  function handleTabClick(tab: typeof TABS[number]) {
    setActiveTab(tab.id)
    if (tab.resetsCount) setDisplayCount(20)
  }

  return (
    <>
      {/* Tab Toggle */}
      <section className="container pt-6 pb-0">
        <div className="flex gap-0 border-b" style={{ borderBottomColor: 'var(--border)' }}>
          {TABS.map(tab => (
            <TabButton
              key={tab.id}
              tab={tab}
              isActive={activeTab === tab.id}
              onClick={() => handleTabClick(tab)}
            />
          ))}
        </div>
      </section>

      {/* Recent Content Section */}
      {activeTab === 'episodes' && (
        <section className="container pt-6 pb-8 md:pb-8">
          {recentEpisodes.length === 0 ? (
            <EmptyState message="No recent content found" />
          ) : (
            <>
              <div className="grid gap-6 md:gap-8">
                {visibleEpisodes.map((episode) => (
                  <SourceCard
                    key={`${episode.podcast}-${episode.slug}`}
                    title={episode.title}
                    subtitle={`${episode.podcastName} · ${episode.date}`}
                    href={`/podcast/${encodeURIComponent(episode.podcast)}/${encodeURIComponent(episode.slug)}`}
                  />
                ))}
              </div>

              {/* Episode count and Load More */}
              <div className="mt-8 flex flex-col items-center gap-4">
                <div style={{ color: 'var(--muted-foreground)' }} className="text-sm">
                  Showing {visibleEpisodes.length} of {recentEpisodes.length}
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
            <EmptyState message="No podcasts found" />
          ) : (
            <div className="grid gap-6 md:gap-8">
              {podcasts.map((podcast) => (
                <SourceCard
                  key={podcast.name}
                  title={podcast.title}
                  subtitle={`${podcast.episodeCount || 0} episodes`}
                  href={`/podcast/${encodeURIComponent(podcast.name)}`}
                />
              ))}
            </div>
          )}
        </section>
      )}

      {/* Newsletters Section */}
      {activeTab === 'newsletters' && (
        <section className="container pt-6 pb-8 md:pb-8">
          {newsletters.length === 0 ? (
            <EmptyState message="No newsletters yet" />
          ) : (
            <div className="grid gap-6 md:gap-8">
              {newsletters.map((newsletter) => (
                <SourceCard
                  key={newsletter.name}
                  title={newsletter.title}
                  subtitle={`${newsletter.episodeCount || 0} issues`}
                  href={`/podcast/${encodeURIComponent(newsletter.name)}`}
                />
              ))}
            </div>
          )}
        </section>
      )}

      {/* Papers Section */}
      {activeTab === 'papers' && (
        <section className="container pt-6 pb-8 md:pb-8">
          {papers.length === 0 ? (
            <EmptyState message="No papers yet" />
          ) : (
            <div className="grid gap-6 md:gap-8">
              {papers.map((paper) => (
                <SourceCard
                  key={paper.name}
                  title={paper.title}
                  subtitle={`${paper.episodeCount || 0} papers`}
                  href={`/podcast/${encodeURIComponent(paper.name)}`}
                />
              ))}
            </div>
          )}
        </section>
      )}
    </>
  )
}
