import Link from 'next/link'
import { notFound } from 'next/navigation'
import { Metadata } from 'next'
import StructuredData from '@/components/StructuredData'
import ShareButton from '@/components/ShareButton'
import { generatePodcastSeriesSchema } from '@/lib/schema'
import { getEpisodesForPodcast, getAllTypedSourceParams } from '@/lib/episodes'
import { isValidContentType, getContentLabels, type ContentType } from '@/lib/content-types'
import { BASE_URL } from '@/lib/constants'

interface SourcePageProps {
  params: Promise<{
    type: string
    name: string
  }>
}

export async function generateStaticParams() {
  const sources = await getAllTypedSourceParams()
  return sources.map(({ type, name }) => ({ type, name }))
}

export async function generateMetadata({ params }: SourcePageProps): Promise<Metadata> {
  const { type, name } = await params
  if (!isValidContentType(type)) return { title: 'Not Found | Teahose' }

  const sourceName = decodeURIComponent(name)
  const episodes = await getEpisodesForPodcast(sourceName)
  const labels = getContentLabels(type)

  const title = `${sourceName} - ${labels.metaSuffix} | Teahose`
  const description = labels.metaDescription(sourceName, episodes.length)
  const canonicalUrl = `${BASE_URL}/${type}/${encodeURIComponent(sourceName)}`

  return {
    title,
    description,
    openGraph: {
      title, description, url: canonicalUrl, siteName: 'Teahose', type: 'website',
      images: [{ url: '/og-image.png', width: 1536, height: 1024, alt: `Teahose - ${labels.metaSuffix}` }],
    },
    twitter: { card: 'summary_large_image', title, description, images: ['/og-image.png'] },
    alternates: { canonical: canonicalUrl },
  }
}

export default async function SourcePage({ params }: SourcePageProps) {
  const { type, name } = await params
  if (!isValidContentType(type)) notFound()

  const contentType = type as ContentType
  const sourceName = decodeURIComponent(name)
  const episodes = await getEpisodesForPodcast(sourceName)
  const labels = getContentLabels(contentType)

  if (episodes.length === 0) notFound()

  return (
    <main className="min-h-screen" style={{ backgroundColor: 'var(--background)' }}>
      <StructuredData
        data={generatePodcastSeriesSchema({
          name: sourceName,
          description: `AI-generated summaries from ${sourceName} on Teahose.`,
          episodeCount: episodes.length,
        })}
      />

      <header style={{ borderBottomColor: 'var(--border)' }} className="border-b">
        <div className="container py-8 md:py-12">
          <Link href="/" style={{ color: 'var(--muted-foreground)' }} className="hover:underline mb-4 block text-sm">
            {labels.backToHome}
          </Link>
          <div className="flex items-center justify-between mb-2">
            <h1 style={{ color: 'var(--foreground)' }}>{sourceName}</h1>
            <ShareButton
              title={`${sourceName} - ${labels.metaSuffix}`}
              refSource={`${contentType}-page`}
              podcast={sourceName}
            />
          </div>
          <p style={{ color: 'var(--muted-foreground)' }} className="text-sm">
            {episodes.length} {episodes.length !== 1 ? labels.plural : labels.singular}
          </p>
        </div>
      </header>

      <section className="container py-12 md:py-16">
        <div className="grid gap-6 md:gap-8">
          {episodes.map((episode) => (
            <Link
              key={episode.slug}
              href={`/${contentType}/${encodeURIComponent(sourceName)}/${encodeURIComponent(episode.slug)}`}
              className="group block p-6 md:p-8 rounded-sm hover:opacity-80 transition-all"
              style={{ backgroundColor: 'var(--card)', borderColor: 'var(--border)', color: 'var(--foreground)' }}
            >
              <h2 className="text-2xl md:text-3xl group-hover:underline transition-colors mb-2">
                {episode.title}
              </h2>
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

      <footer style={{ borderTopColor: 'var(--border)' }} className="border-t mt-16 md:mt-20">
        <div style={{ color: 'var(--muted-foreground)' }} className="container py-8 text-center text-sm">
          <p>{labels.footerMessage}</p>
        </div>
      </footer>
    </main>
  )
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
    return dateStr
  } catch { return dateStr }
}
