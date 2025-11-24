'use client'

import { useState } from 'react'
import MarkdownRenderer from '@/components/MarkdownRenderer'

interface EpisodeClientProps {
  summary?: string
  transcript?: string
  episodeUrl: string
}

export default function EpisodeClient({ summary, transcript, episodeUrl }: EpisodeClientProps) {
  const [activeTab, setActiveTab] = useState<'summary' | 'transcript'>('summary')

  return (
    <section className="container py-8 md:py-12">
      <div
        style={{ borderBottomColor: 'var(--border)' }}
        className="flex gap-2 mb-8 border-b pb-4"
        role="tablist"
        aria-label="Episode content"
      >
        <button
          onClick={() => setActiveTab('summary')}
          style={{
            color: activeTab === 'summary' ? 'var(--accent)' : 'var(--muted-foreground)',
            borderBottomColor: activeTab === 'summary' ? 'var(--accent)' : 'transparent',
            fontSize: 'var(--text-sm)',
            fontWeight: 'var(--font-weight-medium)'
          }}
          className="px-4 py-2 transition-colors border-b-2"
          role="tab"
          aria-selected={activeTab === 'summary'}
          aria-controls="summary-panel"
          id="summary-tab"
        >
          Summary
        </button>
        <button
          onClick={() => setActiveTab('transcript')}
          style={{
            color: activeTab === 'transcript' ? 'var(--accent)' : 'var(--muted-foreground)',
            borderBottomColor: activeTab === 'transcript' ? 'var(--accent)' : 'transparent',
            fontSize: 'var(--text-sm)',
            fontWeight: 'var(--font-weight-medium)'
          }}
          className="px-4 py-2 transition-colors border-b-2"
          role="tab"
          aria-selected={activeTab === 'transcript'}
          aria-controls="transcript-panel"
          id="transcript-tab"
        >
          Transcript
        </button>
      </div>

      <div
        role="tabpanel"
        id={activeTab === 'summary' ? 'summary-panel' : 'transcript-panel'}
        aria-labelledby={activeTab === 'summary' ? 'summary-tab' : 'transcript-tab'}
      >
        {activeTab === 'summary' && summary ? (
          <MarkdownRenderer content={summary} episodeUrl={episodeUrl} enableInsightSharing={true} />
        ) : activeTab === 'transcript' && transcript ? (
          <MarkdownRenderer content={transcript} episodeUrl={episodeUrl} enableInsightSharing={false} />
        ) : (
          <p style={{ color: 'var(--muted-foreground)' }}>No content available</p>
        )}
      </div>
    </section>
  )
}
