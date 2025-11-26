import Link from 'next/link'
import { notFound } from 'next/navigation'
import { Metadata } from 'next'
import StructuredData from '@/components/StructuredData'
import ShareButton from '@/components/ShareButton'
import { generatePodcastSeriesSchema } from '@/lib/schema'
import { getEpisodesForPodcast, getAllPodcastNames } from '@/lib/episodes'

interface PodcastPageProps {
  params: Promise<{
    name: string
  }>
}

/**
 * Generate static params for all podcasts (SSG)
 */
export async function generateStaticParams() {
  const podcasts = await getAllPodcastNames()

  // Return raw names - Next.js will handle URL encoding
  return podcasts.map((name) => ({
    name,
  }))
}

/**
 * Generate dynamic metadata for SEO
 */
export async function generateMetadata({ params }: PodcastPageProps): Promise<Metadata> {
  const { name } = await params
  const podcastName = decodeURIComponent(name)

  const episodes = await getEpisodesForPodcast(podcastName)

  const title = `${podcastName} - Podcast Summaries | Teahose`
  const description = `Browse ${episodes.length} episode${episodes.length !== 1 ? 's' : ''} from ${podcastName}. AI-generated summaries and transcripts for tech podcast episodes.`

  // Use consistent URL encoding for canonical and social sharing
  const canonicalUrl = `https://teahose.com/podcast/${encodeURIComponent(podcastName)}`

  return {
    title,
    description,
    openGraph: {
      title,
      description,
      url: canonicalUrl,
      siteName: 'Teahose',
      type: 'website',
      images: [
        {
          url: '/og-image.png',
          width: 1536,
          height: 1024,
          alt: 'Teahose - Tech podcast summaries',
        },
      ],
    },
    twitter: {
      card: 'summary_large_image',
      title,
      description,
      images: ['/og-image.png'],
    },
    alternates: {
      canonical: canonicalUrl,
    },
  }
}

/**
 * Server Component - generates static HTML at build time
 */
export default async function PodcastPage({ params }: PodcastPageProps) {
  const { name } = await params
  const podcastName = decodeURIComponent(name)

  const episodes = await getEpisodesForPodcast(podcastName)

  if (episodes.length === 0) {
    notFound()
  }

  return (
    <main className="min-h-screen" style={{ backgroundColor: 'var(--background)' }}>
      {/* Structured Data for SEO */}
      <StructuredData
        data={generatePodcastSeriesSchema({
          name: podcastName,
          description: undefined,
          episodeCount: episodes.length,
        })}
      />

      {/* Header */}
      <header style={{ borderBottomColor: 'var(--border)' }} className="border-b">
        <div className="container py-8 md:py-12">
          <Link href="/" style={{ color: 'var(--muted-foreground)' }} className="hover:underline mb-4 block text-sm">
            ← Back to Podcasts
          </Link>
          <div className="flex items-center justify-between mb-2">
            <h1 style={{ color: 'var(--foreground)' }}>{podcastName}</h1>
            <ShareButton
              title={`${podcastName} - Podcast Summaries`}
              refSource="podcast-page"
              podcast={podcastName}
            />
          </div>
          <p style={{ color: 'var(--muted-foreground)' }} className="text-sm">
            {episodes.length} episode{episodes.length !== 1 ? 's' : ''}
          </p>
        </div>
      </header>

      {/* Episodes */}
      <section className="container py-12 md:py-16">
        <div className="grid gap-6 md:gap-8">
          {episodes.map((episode) => (
            <Link
              key={episode.slug}
              href={`/podcast/${encodeURIComponent(podcastName)}/${encodeURIComponent(episode.slug)}`}
              className="group block p-6 md:p-8 rounded-sm hover:opacity-80 transition-all"
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
                {episode.date && (
                  <span style={{ color: 'var(--muted-foreground)' }} className="text-sm">
                    {formatDate(episode.date)}
                  </span>
                )}
                <span style={{ color: 'var(--accent)' }} className="font-light">→</span>
              </div>
            </Link>
          ))}
        </div>
      </section>

      {/* Footer */}
      <footer style={{ borderTopColor: 'var(--border)' }} className="border-t mt-16 md:mt-20">
        <div style={{ color: 'var(--muted-foreground)' }} className="container py-8 text-center text-sm">
          <p>Discover the insights within each episode.</p>
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
    return dateStr
  } catch {
    return dateStr
  }
}
