import {
  getPodcastBySlug,
  getEpisodesForPodcast,
  getEpisodeBySlug,
} from '@/lib/podcasts';
import { getMarkdownContent, splitMetadataFromContent } from '@/lib/markdown';
import { notFound } from 'next/navigation';
import EpisodeWrapper from '@/components/EpisodeWrapper';

export async function generateStaticParams() {
  const podcasts = await import('@/lib/podcasts').then((mod) => mod.getAllPodcasts());

  const params: { name: string; episode: string }[] = [];

  for (const podcast of podcasts) {
    const episodes = getEpisodesForPodcast(podcast.slug);
    for (const episode of episodes) {
      params.push({
        name: podcast.slug,
        episode: episode.slug,
      });
    }
  }

  return params;
}

export default async function EpisodePage({
  params,
}: {
  params: Promise<{ name: string; episode: string }>;
}) {
  const { name, episode: episodeSlug } = await params;
  const podcast = getPodcastBySlug(name);
  const episode = getEpisodeBySlug(name, episodeSlug);

  if (!podcast || !episode) {
    notFound();
  }

  // Load the content and split metadata
  const summaryRaw = episode.hasSummary
    ? getMarkdownContent(episode.summaryPath)
    : '';
  const { metadata: summaryMetadata, content: summaryContent } = summaryRaw
    ? splitMetadataFromContent(summaryRaw)
    : { metadata: {}, content: '' };

  const transcriptContent = episode.hasTranscript
    ? getMarkdownContent(episode.transcriptPath)
    : '';

  return (
    <div className="min-h-screen bg-white">
      <div className="max-w-3xl mx-auto px-6 py-16">
        <div className="pl-4">
          <EpisodeWrapper
            summaryContent={summaryContent}
            transcriptContent={transcriptContent}
            hasSummary={episode.hasSummary}
            hasTranscript={episode.hasTranscript}
            podcastSlug={name}
            title={summaryMetadata.title || episode.title}
            podcastName={summaryMetadata.podcast || podcast.name}
            date={summaryMetadata.date || episode.date}
            participants={summaryMetadata.participants}
          />
        </div>
      </div>
    </div>
  );
}
