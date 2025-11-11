import Link from 'next/link';
import { getAllPodcasts } from '@/lib/podcasts';

export default function HomePage() {
  const podcasts = getAllPodcasts();

  return (
    <div className="min-h-screen bg-white">
      <div className="max-w-3xl mx-auto px-6 py-16">
        <header className="mb-16 pl-4">
          <h1 className="text-3xl font-bold text-gray-900 mb-2">
            Podcast Summaries
          </h1>
          <p className="text-base text-gray-500">
            AI-generated summaries of podcast episodes
          </p>
        </header>

        <div className="space-y-8 pl-4">
          {podcasts.map((podcast) => (
            <div key={podcast.slug}>
              <h2 className="text-xl font-semibold text-gray-900 mb-2">
                <Link
                  href={`/podcast/${podcast.slug}`}
                  className="hover:text-blue-600 transition-colors"
                >
                  {podcast.name}
                </Link>
              </h2>

              <div className="space-y-1 text-sm text-gray-500">
                <p>
                  Hosts: {podcast.hosts && podcast.hosts.length > 0
                    ? podcast.hosts.join(', ')
                    : 'Unavailable'}
                </p>
                <p>Summaries: {podcast.summarizedCount}</p>
              </div>
            </div>
          ))}
        </div>

        {podcasts.length === 0 && (
          <div className="text-center py-16">
            <p className="text-gray-500">
              No podcasts found. Check your podcast_status.json file.
            </p>
          </div>
        )}
      </div>
    </div>
  );
}
