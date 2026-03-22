import Link from 'next/link'
import { notFound } from 'next/navigation'
import { Metadata } from 'next'
import dynamic from 'next/dynamic'
import MarkdownRenderer from '@/components/MarkdownRenderer'
import StructuredData from '@/components/StructuredData'
import ShareButton from '@/components/ShareButton'
import { generatePodcastEpisodeSchema, generateArticleSchema, generateBreadcrumbSchema } from '@/lib/schema'
import { BASE_URL } from '@/lib/constants'
import { getEpisode, getAllEpisodeParams, type Episode } from '@/lib/episodes'
import EpisodeClient from './EpisodeClient'

const TranscriptChat = dynamic(() => import('@/components/TranscriptChat'))

interface EpisodePageProps {
  params: Promise<{
    name: string
    episode: string
  }>
}

/**
 * Generate static params for all episodes (SSG)
 */
export async function generateStaticParams() {
  const allParams = await getAllEpisodeParams()

  // Return raw names - Next.js will handle URL encoding
  return allParams.map(({ name, episode }) => ({
    name,
    episode,
  }))
}

/**
 * Generate dynamic metadata for SEO
 */
export async function generateMetadata({ params }: EpisodePageProps): Promise<Metadata> {
  const { name, episode: episodeSlug } = await params
  const podcastName = decodeURIComponent(name)
  const decodedSlug = decodeURIComponent(episodeSlug)

  const episode = await getEpisode(podcastName, decodedSlug)

  if (!episode) {
    return {
      title: 'Episode Not Found | Teahose',
    }
  }

  const title = `${episode.title} - ${episode.podcast || podcastName} | Teahose`
  const description = episode.summary
    ? episode.summary.substring(0, 160).replace(/\n/g, ' ').trim() + '...'
    : `Listen to ${episode.title} from ${episode.podcast || podcastName} on Teahose.`

  // Use consistent URL encoding for canonical and social sharing
  const canonicalUrl = `https://www.teahose.com/podcast/${encodeURIComponent(podcastName)}/${encodeURIComponent(decodedSlug)}`

  return {
    title,
    description,
    openGraph: {
      title,
      description,
      url: canonicalUrl,
      siteName: 'Teahose',
      type: 'article',
      publishedTime: episode.date,
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

function getContentSchema(episode: Episode, podcastName: string, episodeSlug: string) {
  const meta = {
    title: episode.title,
    podcast: episode.podcast || podcastName,
    date: episode.date || '',
    description: episode.summary?.substring(0, 200),
  }

  if (episode.source === 'newsletter') {
    return generateArticleSchema(meta, podcastName, episodeSlug)
  }
  if (episode.source === 'paper') {
    return generateArticleSchema(
      { ...meta, arxivId: episode.arxivId, pdfUrl: episode.pdfUrl },
      podcastName,
      episodeSlug,
      'ScholarlyArticle'
    )
  }
  return generatePodcastEpisodeSchema(
    { ...meta, participants: episode.participants, videoUrl: episode.videoUrl, region: episode.region },
    podcastName,
    episodeSlug
  )
}

export default async function EpisodePage({ params }: EpisodePageProps) {
  const { name, episode: episodeSlug } = await params
  const podcastName = decodeURIComponent(name)
  const decodedSlug = decodeURIComponent(episodeSlug)

  const episode = await getEpisode(podcastName, decodedSlug)

  if (!episode) {
    notFound()
  }

  return (
    <main className="min-h-screen" style={{ backgroundColor: 'var(--background)' }}>
      {/* Structured Data for SEO */}
      <StructuredData
        data={[
          getContentSchema(episode, podcastName, decodedSlug),
          generateBreadcrumbSchema([
            { name: 'Home', url: BASE_URL },
            { name: episode.podcast || podcastName, url: `${BASE_URL}/podcast/${encodeURIComponent(podcastName)}` },
            { name: episode.title, url: `${BASE_URL}/podcast/${encodeURIComponent(podcastName)}/${encodeURIComponent(decodedSlug)}` },
          ]),
        ]}
      />

      {/* Header */}
      <header style={{ borderBottomColor: 'var(--border)' }} className="border-b">
        <div className="container py-8 md:py-12">
          <Link
            href={`/podcast/${name}`}
            style={{ color: 'var(--muted-foreground)' }}
            className="hover:underline mb-4 block text-sm"
          >
            ← Back to Episodes
          </Link>
          <div className="flex items-start justify-between gap-4 mb-4">
            <h1 style={{ color: 'var(--foreground)' }} className="flex-1">{episode.title}</h1>
            <ShareButton
              title={episode.title}
              refSource="episode-page"
              podcast={podcastName}
              episode={decodedSlug}
            />
          </div>
          {episode.date && <p style={{ color: 'var(--muted-foreground)' }} className="text-sm mb-2">{formatDate(episode.date)}</p>}
          {episode.participants && <p style={{ color: 'var(--muted-foreground)' }} className="text-sm mb-2">{episode.participants}</p>}
          {episode.podcast && <p style={{ color: 'var(--muted-foreground)' }} className="text-sm">{episode.podcast}</p>}
        </div>
      </header>

      {/* Client Component for tabs */}
      <EpisodeClient
        summary={episode.summary}
        transcript={episode.transcript}
        episodeUrl={`https://www.teahose.com/podcast/${name}/${episodeSlug}`}
        podcastName={podcastName}
        episodeTitle={episode.title}
      />

      {/* Chat with Transcript */}
      {episode.transcript && (
        <TranscriptChat
          transcript={episode.transcript}
          episodeTitle={episode.title}
          episodeSummary={episode.summary}
          videoUrl={episode.videoUrl}
          podcastName={podcastName}
        />
      )}

      {/* Footer */}
      <footer style={{ borderTopColor: 'var(--border)' }} className="border-t mt-16 md:mt-20">
        <div style={{ color: 'var(--muted-foreground)' }} className="container py-8 text-center text-sm">
          <p>Reflect on the key insights from this episode.</p>
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
    // Handle full date strings
    const date = new Date(dateStr)
    if (!isNaN(date.getTime())) {
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
