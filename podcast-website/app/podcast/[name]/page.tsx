import Link from 'next/link';
import { getPodcastBySlug, getEpisodesForPodcast, getAllPodcasts } from '@/lib/podcasts';
import { notFound } from 'next/navigation';

export async function generateStaticParams() {
  const podcasts = getAllPodcasts();
  return podcasts.map((podcast) => ({
    name: podcast.slug,
  }));
}

export default async function PodcastPage({ params }: { params: Promise<{ name: string }> }) {
  const { name } = await params;
  const podcast = getPodcastBySlug(name);

  if (!podcast) {
    notFound();
  }

  const episodes = getEpisodesForPodcast(name);

  return (
    <div className="min-h-screen bg-white">
      <div className="max-w-3xl mx-auto px-6 py-16">
        <nav className="mb-8 pl-4">
          <Link href="/" className="text-sm text-gray-500 hover:text-gray-900 transition-colors">
            ← Back
          </Link>
        </nav>

        <header className="mb-16 pl-4">
          <h1 className="text-3xl font-bold text-gray-900 mb-2">
            {podcast.name}
          </h1>
          <div className="space-y-1 text-sm text-gray-500">
            {podcast.hosts && podcast.hosts.length > 0 && (
              <p>Hosts: {podcast.hosts.join(', ')}</p>
            )}
            <p>Episodes: {episodes.length}</p>
          </div>
        </header>

        <div className="space-y-8 pl-4">
          {episodes.map((episode) => (
            <div key={episode.slug}>
              <h2 className="text-lg font-semibold text-gray-900 mb-1">
                <Link
                  href={`/podcast/${name}/${episode.slug}`}
                  className="hover:text-blue-600 transition-colors"
                >
                  {episode.title}
                </Link>
              </h2>
              <p className="text-sm text-gray-500">{formatDate(episode.date)}</p>
            </div>
          ))}
        </div>

        {episodes.length === 0 && (
          <div className="text-center py-16">
            <p className="text-gray-500">
              No episodes found for this podcast.
            </p>
          </div>
        )}
      </div>
    </div>
  );
}

function formatDate(dateStr: string): string {
  if (!dateStr || dateStr === 'Unknown') return 'Unknown';

  try {
    const date = new Date(dateStr);
    return date.toLocaleDateString('en-US', {
      year: 'numeric',
      month: 'short',
      day: 'numeric'
    });
  } catch {
    return dateStr;
  }
}
