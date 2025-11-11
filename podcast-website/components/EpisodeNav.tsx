'use client';

import Link from 'next/link';

interface EpisodeNavProps {
  podcastSlug: string;
  hasSummary: boolean;
  hasTranscript: boolean;
  activeTab: 'summary' | 'transcript';
  onTabChange: (tab: 'summary' | 'transcript') => void;
}

export default function EpisodeNav({
  podcastSlug,
  hasSummary,
  hasTranscript,
  activeTab,
  onTabChange,
}: EpisodeNavProps) {
  return (
    <nav className="mb-8 pl-4 text-sm">
      <Link
        href={`/podcast/${podcastSlug}`}
        className="text-gray-500 hover:text-gray-900 transition-colors"
      >
        ← Back
      </Link>

      {hasSummary && hasTranscript && (
        <>
          <span className="mx-3 text-gray-300">|</span>
          <button
            type="button"
            onClick={() => onTabChange('summary')}
            className={`bg-transparent border-0 p-0 cursor-pointer font-inherit text-sm transition-colors underline-offset-2 hover:underline ${
              activeTab === 'summary'
                ? 'text-gray-900'
                : 'text-gray-500 hover:text-gray-700'
            }`}
          >
            Summary
          </button>
          <span className="mx-3 text-gray-300">|</span>
          <button
            type="button"
            onClick={() => onTabChange('transcript')}
            className={`bg-transparent border-0 p-0 cursor-pointer font-inherit text-sm transition-colors underline-offset-2 hover:underline ${
              activeTab === 'transcript'
                ? 'text-gray-900'
                : 'text-gray-500 hover:text-gray-700'
            }`}
          >
            Transcript
          </button>
        </>
      )}
    </nav>
  );
}
