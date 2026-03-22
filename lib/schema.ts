import { BASE_URL } from './constants'

export interface EpisodeMetadata {
  title: string
  podcast: string
  date: string
  processed?: string
  participants?: string
  videoId?: string
  videoUrl?: string
  region?: string
  description?: string
  source?: string
  arxivId?: string
  pdfUrl?: string
}

export interface PodcastMetadata {
  name: string
  description?: string
  episodeCount?: number
}

function episodeUrl(podcastName: string, episodeSlug: string): string {
  return `${BASE_URL}/podcast/${encodeURIComponent(podcastName)}/${encodeURIComponent(episodeSlug)}`
}

function podcastUrl(podcastName: string): string {
  return `${BASE_URL}/podcast/${encodeURIComponent(podcastName)}`
}

const PUBLISHER = {
  '@type': 'Organization',
  name: 'Teahose',
  url: BASE_URL,
}

export function generatePodcastEpisodeSchema(
  episode: EpisodeMetadata,
  podcastName: string,
  episodeSlug: string
) {
  const schema: any = {
    '@context': 'https://schema.org',
    '@type': 'PodcastEpisode',
    name: episode.title,
    url: episodeUrl(podcastName, episodeSlug),
    datePublished: episode.date,
    partOfSeries: {
      '@type': 'PodcastSeries',
      name: episode.podcast,
      url: podcastUrl(podcastName),
    },
  }

  if (episode.description) {
    schema.description = episode.description
  }

  if (episode.participants) {
    schema.description = schema.description
      ? `${schema.description} Featuring: ${episode.participants}`
      : `Featuring: ${episode.participants}`
  }

  if (episode.videoUrl) {
    schema.associatedMedia = {
      '@type': 'MediaObject',
      contentUrl: episode.videoUrl,
    }
  }

  return schema
}

export function generatePodcastSeriesSchema(podcast: PodcastMetadata) {
  const schema: any = {
    '@context': 'https://schema.org',
    '@type': 'PodcastSeries',
    name: podcast.name,
    url: podcastUrl(podcast.name),
  }

  if (podcast.description) {
    schema.description = podcast.description
  }

  if (podcast.episodeCount) {
    schema.numberOfEpisodes = podcast.episodeCount
  }

  return schema
}

export function generateBreadcrumbSchema(
  items: { name: string; url: string }[]
) {
  return {
    '@context': 'https://schema.org',
    '@type': 'BreadcrumbList',
    itemListElement: items.map((item, index) => ({
      '@type': 'ListItem',
      position: index + 1,
      name: item.name,
      item: item.url,
    })),
  }
}

/**
 * Unified Article/ScholarlyArticle schema.
 * Use 'Article' for newsletters, 'ScholarlyArticle' for papers.
 */
export function generateArticleSchema(
  episode: EpisodeMetadata,
  podcastName: string,
  episodeSlug: string,
  type: 'Article' | 'ScholarlyArticle' = 'Article'
) {
  const schema: any = {
    '@context': 'https://schema.org',
    '@type': type,
    headline: episode.title,
    url: episodeUrl(podcastName, episodeSlug),
    datePublished: episode.date,
    publisher: PUBLISHER,
  }

  if (episode.description) {
    schema.description = episode.description
  }

  if (type === 'ScholarlyArticle') {
    if (episode.arxivId) {
      schema.sameAs = `https://arxiv.org/abs/${episode.arxivId}`
    }
    if (episode.pdfUrl) {
      schema.encoding = {
        '@type': 'MediaObject',
        contentUrl: episode.pdfUrl,
        encodingFormat: 'application/pdf',
      }
    }
  }

  return schema
}

export function generateOrganizationSchema() {
  return {
    '@context': 'https://schema.org',
    '@type': 'Organization',
    name: 'Teahose',
    url: BASE_URL,
    logo: `${BASE_URL}/og-image.png`,
    description: 'Summaries of the most important tech podcasts, newsletters, and Physical AI research papers. Subscribe for daily digests delivering hours of insight in 30 seconds.',
  }
}

export function generateWebSiteSchema() {
  return {
    '@context': 'https://schema.org',
    '@type': 'WebSite',
    name: 'Teahose',
    url: BASE_URL,
    description: 'Summaries of the most important tech podcasts, newsletters, and Physical AI research papers.',
    potentialAction: {
      '@type': 'SearchAction',
      target: {
        '@type': 'EntryPoint',
        urlTemplate: `${BASE_URL}/?q={search_term_string}`,
      },
      'query-input': 'required name=search_term_string',
    },
  }
}

function extractField(content: string, fieldName: string): string | undefined {
  const match = content.match(new RegExp(`\\*\\*${fieldName}:\\*\\*\\s+(.+)`, 'i'))
  return match ? match[1].trim() : undefined
}

export function parseEpisodeMetadata(summaryContent: string): Partial<EpisodeMetadata> {
  const metadata: Partial<EpisodeMetadata> = {}

  const titleMatch = summaryContent.match(/^#\s+(.+?)$/m)
  if (titleMatch) {
    metadata.title = titleMatch[1].trim()
      .replace(/\[(.+?)\]\(.+?\)/g, '$1')
      .replace(/^\[(.+?)\]$/, '$1')
  }

  metadata.podcast = extractField(summaryContent, 'Podcast')
  metadata.date = extractField(summaryContent, 'Date')
  metadata.processed = extractField(summaryContent, 'Processed')
  metadata.participants = extractField(summaryContent, 'Participants')
  metadata.videoId = extractField(summaryContent, 'Video ID')
  metadata.region = extractField(summaryContent, 'Region')
  metadata.source = extractField(summaryContent, 'Source')
  metadata.arxivId = extractField(summaryContent, 'arXiv')
  metadata.pdfUrl = extractField(summaryContent, 'PDF')

  metadata.videoUrl = extractField(summaryContent, 'Video URL')
  if (!metadata.videoUrl) {
    const titleLinkMatch = summaryContent.match(/^#\s+\[.+?\]\((.+?)\)$/m)
    if (titleLinkMatch) {
      metadata.videoUrl = titleLinkMatch[1].trim()
    }
  }

  const descriptionMatch = summaryContent.match(/---\s+([\s\S]+?)(?:\n\n|\n#)/)
  if (descriptionMatch) {
    const desc = descriptionMatch[1].trim()
    metadata.description = desc.length > 160
      ? desc.substring(0, 157) + '...'
      : desc
  }

  return metadata
}
