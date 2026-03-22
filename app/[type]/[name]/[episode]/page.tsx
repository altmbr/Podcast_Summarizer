import Link from 'next/link'
import { notFound } from 'next/navigation'
import { Metadata } from 'next'
import dynamic from 'next/dynamic'
import StructuredData from '@/components/StructuredData'
import ShareButton from '@/components/ShareButton'
import { generatePodcastEpisodeSchema, generateArticleSchema, generateBreadcrumbSchema } from '@/lib/schema'
import { BASE_URL } from '@/lib/constants'
import { getEpisode, getAllTypedEpisodeParams, type Episode } from '@/lib/episodes'
import { isValidContentType, getContentLabels, type ContentType } from '@/lib/content-types'
import EpisodeClient from './EpisodeClient'

const TranscriptChat = dynamic(() => import('@/components/TranscriptChat'))

interface EpisodePageProps {
  params: Promise<{
    type: string
    name: string
    episode: string
  }>
}

export async function generateStaticParams() {
  const allParams = await getAllTypedEpisodeParams()
  return allParams.map(({ type, name, episode }) => ({ type, name, episode }))
}

export async function generateMetadata({ params }: EpisodePageProps): Promise<Metadata> {
  const { type, name, episode: episodeSlug } = await params
  if (!isValidContentType(type)) return { title: 'Not Found | Teahose' }

  const sourceName = decodeURIComponent(name)
  const decodedSlug = decodeURIComponent(episodeSlug)
  const episode = await getEpisode(sourceName, decodedSlug)
  const labels = getContentLabels(type)

  if (!episode) return { title: `${labels.itemNotFound} | Teahose` }

  const title = `${episode.title} - ${episode.podcast || sourceName} | Teahose`
  const description = episode.summary
    ? extractPlainDescription(episode.summary, 160)
    : `Read ${episode.title} from ${episode.podcast || sourceName} on Teahose.`
  const canonicalUrl = `${BASE_URL}/${type}/${encodeURIComponent(sourceName)}/${encodeURIComponent(decodedSlug)}`

  return {
    title,
    description,
    openGraph: {
      title, description, url: canonicalUrl, siteName: 'Teahose', type: 'article',
      publishedTime: episode.date,
      images: [{ url: '/og-image.png', width: 1536, height: 1024, alt: `Teahose - ${labels.metaSuffix}` }],
    },
    twitter: { card: 'summary_large_image', title, description, images: ['/og-image.png'] },
    alternates: { canonical: canonicalUrl },
  }
}

function getContentSchema(episode: Episode, contentType: ContentType, sourceName: string, episodeSlug: string) {
  const meta = {
    title: episode.title,
    podcast: episode.podcast || sourceName,
    date: episode.date || '',
    description: episode.summary?.substring(0, 200),
  }

  if (contentType === 'newsletter') {
    return generateArticleSchema(meta, sourceName, episodeSlug)
  }
  if (contentType === 'paper') {
    return generateArticleSchema(
      { ...meta, arxivId: episode.arxivId, pdfUrl: episode.pdfUrl },
      sourceName, episodeSlug, 'ScholarlyArticle'
    )
  }
  return generatePodcastEpisodeSchema(
    { ...meta, participants: episode.participants, videoUrl: episode.videoUrl, region: episode.region },
    sourceName, episodeSlug
  )
}

export default async function EpisodeDetailPage({ params }: EpisodePageProps) {
  const { type, name, episode: episodeSlug } = await params
  if (!isValidContentType(type)) notFound()

  const contentType = type as ContentType
  const sourceName = decodeURIComponent(name)
  const decodedSlug = decodeURIComponent(episodeSlug)
  const episode = await getEpisode(sourceName, decodedSlug)
  const labels = getContentLabels(contentType)

  if (!episode) notFound()

  return (
    <main className="min-h-screen" style={{ backgroundColor: 'var(--background)' }}>
      <StructuredData
        data={[
          getContentSchema(episode, contentType, sourceName, decodedSlug),
          generateBreadcrumbSchema([
            { name: 'Home', url: BASE_URL },
            { name: episode.podcast || sourceName, url: `${BASE_URL}/${contentType}/${encodeURIComponent(sourceName)}` },
            { name: episode.title, url: `${BASE_URL}/${contentType}/${encodeURIComponent(sourceName)}/${encodeURIComponent(decodedSlug)}` },
          ]),
        ]}
      />

      <header style={{ borderBottomColor: 'var(--border)' }} className="border-b">
        <div className="container py-8 md:py-12">
          <Link
            href={`/${contentType}/${name}`}
            style={{ color: 'var(--muted-foreground)' }}
            className="hover:underline mb-4 block text-sm"
          >
            {labels.backToItem}
          </Link>
          <div className="flex items-start justify-between gap-4 mb-4">
            <h1 style={{ color: 'var(--foreground)' }} className="flex-1">{episode.title}</h1>
            <ShareButton
              title={episode.title}
              refSource={`${contentType}-page`}
              podcast={sourceName}
              episode={decodedSlug}
            />
          </div>
          {episode.date && <p style={{ color: 'var(--muted-foreground)' }} className="text-sm mb-2">{formatDate(episode.date)}</p>}
          {episode.participants && <p style={{ color: 'var(--muted-foreground)' }} className="text-sm mb-2">{episode.participants}</p>}
          {episode.podcast && <p style={{ color: 'var(--muted-foreground)' }} className="text-sm">{episode.podcast}</p>}
        </div>
      </header>

      <EpisodeClient
        summary={episode.summary}
        transcript={contentType === 'podcast' ? episode.transcript : undefined}
        showTranscript={contentType === 'podcast'}
        episodeUrl={`${BASE_URL}/${contentType}/${name}/${episodeSlug}`}
        podcastName={sourceName}
        episodeTitle={episode.title}
      />

      {contentType === 'podcast' && episode.transcript && (
        <TranscriptChat
          transcript={episode.transcript}
          episodeTitle={episode.title}
          episodeSummary={episode.summary}
          videoUrl={episode.videoUrl}
          podcastName={sourceName}
        />
      )}

      <footer style={{ borderTopColor: 'var(--border)' }} className="border-t mt-16 md:mt-20">
        <div style={{ color: 'var(--muted-foreground)' }} className="container py-8 text-center text-sm">
          <p>{labels.footerMessage}</p>
        </div>
      </footer>
    </main>
  )
}

/**
 * Extract a clean plain-text description from summary markdown.
 * Strips markdown syntax (headings, bold, links, horizontal rules) and
 * skips metadata lines that may remain in the content.
 */
function extractPlainDescription(summary: string, maxLen: number): string {
  const lines = summary.split('\n')
  const textParts: string[] = []

  for (const line of lines) {
    const trimmed = line.trim()
    // Skip empty, headings, horizontal rules, metadata-style lines
    if (!trimmed) continue
    if (trimmed.startsWith('#')) continue
    if (trimmed === '---') continue
    if (/^\*\*(Podcast|Date|Processed|Participants|Source|Episode URL|Transcript|arXiv|PDF):\*\*/.test(trimmed)) continue

    // Strip markdown bold/italic/links
    const plain = trimmed
      .replace(/\*\*(.*?)\*\*/g, '$1')
      .replace(/\*(.*?)\*/g, '$1')
      .replace(/\[(.*?)\]\(.*?\)/g, '$1')
      .replace(/^>\s*/, '')

    if (plain.length > 10) {
      textParts.push(plain)
      const joined = textParts.join(' ')
      if (joined.length >= maxLen) {
        return joined.substring(0, maxLen).trim() + '...'
      }
    }
  }

  const result = textParts.join(' ')
  if (result.length > 0) {
    return result.substring(0, maxLen).trim() + (result.length > maxLen ? '...' : '')
  }
  return `Read this summary on Teahose.`
}

function formatDate(dateStr: string): string {
  if (!dateStr || dateStr === 'Unknown') return 'Unknown'
  try {
    if (/^\d{4}-\d{2}-\d{2}$/.test(dateStr)) {
      return new Date(dateStr).toLocaleDateString('en-US', { year: 'numeric', month: 'long', day: 'numeric' })
    }
    if (/^\d{8}$/.test(dateStr)) {
      const d = `${dateStr.substring(0, 4)}-${dateStr.substring(4, 6)}-${dateStr.substring(6, 8)}`
      return new Date(d).toLocaleDateString('en-US', { year: 'numeric', month: 'long', day: 'numeric' })
    }
    const date = new Date(dateStr)
    if (!isNaN(date.getTime())) {
      return date.toLocaleDateString('en-US', { year: 'numeric', month: 'long', day: 'numeric' })
    }
    return dateStr
  } catch { return dateStr }
}
