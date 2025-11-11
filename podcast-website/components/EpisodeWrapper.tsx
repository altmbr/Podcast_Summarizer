'use client';

import { useState } from 'react';
import EpisodeNav from './EpisodeNav';
import EpisodeContent from './EpisodeContent';

interface EpisodeWrapperProps {
  summaryContent: string;
  transcriptContent: string;
  hasSummary: boolean;
  hasTranscript: boolean;
  podcastSlug: string;
  title: string;
  podcastName: string;
  date: string;
  participants?: string;
}

export default function EpisodeWrapper({
  summaryContent,
  transcriptContent,
  hasSummary,
  hasTranscript,
  podcastSlug,
  title,
  podcastName,
  date,
  participants,
}: EpisodeWrapperProps) {
  const [activeTab, setActiveTab] = useState<'summary' | 'transcript'>('summary');

  return (
    <>
      <EpisodeNav
        podcastSlug={podcastSlug}
        hasSummary={hasSummary}
        hasTranscript={hasTranscript}
        activeTab={activeTab}
        onTabChange={setActiveTab}
      />

      <header className="mb-16 mt-8">
        <h1 className="text-2xl font-bold text-gray-900 mb-4">{title}</h1>

        <div className="space-y-1 text-sm text-gray-500">
          <p>Podcast: {podcastName}</p>
          <p>Date: {date}</p>
          {participants && <p>Participants: {participants}</p>}
        </div>
      </header>

      <EpisodeContent
        summaryContent={summaryContent}
        transcriptContent={transcriptContent}
        hasSummary={hasSummary}
        hasTranscript={hasTranscript}
        activeTab={activeTab}
      />
    </>
  );
}
