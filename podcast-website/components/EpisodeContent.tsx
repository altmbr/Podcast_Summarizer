'use client';

import { useState } from 'react';
import MarkdownRenderer from './MarkdownRenderer';

interface EpisodeContentProps {
  summaryContent: string;
  transcriptContent: string;
  hasSummary: boolean;
  hasTranscript: boolean;
  activeTab: 'summary' | 'transcript';
}

export default function EpisodeContent({
  summaryContent,
  transcriptContent,
  hasSummary,
  hasTranscript,
  activeTab,
}: EpisodeContentProps) {
  // If only one is available, show that one
  if (!hasSummary && hasTranscript) {
    return (
      <div>
        <MarkdownRenderer content={transcriptContent} />
      </div>
    );
  }

  if (!hasSummary && !hasTranscript) {
    return (
      <div className="text-center py-12">
        <p className="text-gray-600 text-lg">
          No content available for this episode yet.
        </p>
      </div>
    );
  }

  return (
    <div>
      {activeTab === 'summary' ? (
        <MarkdownRenderer content={summaryContent} />
      ) : (
        <MarkdownRenderer content={transcriptContent} />
      )}
    </div>
  );
}
