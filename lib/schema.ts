/**
 * Schema.org structured data utilities for SEO
 */

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
}

export interface PodcastMetadata {
  name: string
  description?: string
  episodeCount?: number
}

/**
 * Generate PodcastEpisode schema markup
 */
export function generatePodcastEpisodeSchema(
  episode: EpisodeMetadata,
  podcastName: string,
  episodeSlug: string
) {
  const schema: any = {
    '@context': 'https://schema.org',
    '@type': 'PodcastEpisode',
    name: episode.title,
    url: `https://www.teahose.com/podcast/${encodeURIComponent(podcastName)}/${encodeURIComponent(episodeSlug)}`,
    datePublished: episode.date,
    partOfSeries: {
      '@type': 'PodcastSeries',
      name: episode.podcast,
      url: `https://www.teahose.com/podcast/${encodeURIComponent(podcastName)}`,
    },
  }

  // Add optional fields
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

/**
 * Generate PodcastSeries schema markup
 */
export function generatePodcastSeriesSchema(podcast: PodcastMetadata) {
  const schema: any = {
    '@context': 'https://schema.org',
    '@type': 'PodcastSeries',
    name: podcast.name,
    url: `https://www.teahose.com/podcast/${encodeURIComponent(podcast.name)}`,
  }

  if (podcast.description) {
    schema.description = podcast.description
  }

  if (podcast.episodeCount) {
    schema.numberOfEpisodes = podcast.episodeCount
  }

  return schema
}

/**
 * Generate Organization schema markup for homepage
 */
export function generateOrganizationSchema() {
  return {
    '@context': 'https://schema.org',
    '@type': 'Organization',
    name: 'Teahose',
    url: 'https://www.teahose.com',
    logo: 'https://www.teahose.com/og-image.png',
    description: 'Summaries of the most important tech podcasts — including China\'s. Subscribe for the weekly briefing that distills 30+ hours of podcasts into a 5-minute read.',
    sameAs: [],
  }
}

/**
 * Generate WebSite schema markup for homepage
 */
export function generateWebSiteSchema() {
  return {
    '@context': 'https://schema.org',
    '@type': 'WebSite',
    name: 'Teahose',
    url: 'https://www.teahose.com',
    description: 'Summaries of the most important tech podcasts — including China\'s.',
    potentialAction: {
      '@type': 'SearchAction',
      target: {
        '@type': 'EntryPoint',
        urlTemplate: 'https://www.teahose.com/?q={search_term_string}',
      },
      'query-input': 'required name=search_term_string',
    },
  }
}

/**
 * Extract a bold metadata field value from markdown content.
 * Matches patterns like: **FieldName:** value
 */
function extractField(content: string, fieldName: string): string | undefined {
  const match = content.match(new RegExp(`\\*\\*${fieldName}:\\*\\*\\s+(.+)`, 'i'))
  return match ? match[1].trim() : undefined
}

/**
 * Parse episode metadata from summary markdown content
 */
export function parseEpisodeMetadata(summaryContent: string): Partial<EpisodeMetadata> {
  const metadata: Partial<EpisodeMetadata> = {}

  // Extract title (first # heading)
  const titleMatch = summaryContent.match(/^#\s+(.+?)$/m)
  if (titleMatch) {
    metadata.title = titleMatch[1].trim()
      .replace(/\[(.+?)\]\(.+?\)/g, '$1')  // [text](url) -> text
      .replace(/^\[(.+?)\]$/, '$1')          // [text] -> text
  }

  // Extract standard metadata fields
  metadata.podcast = extractField(summaryContent, 'Podcast')
  metadata.date = extractField(summaryContent, 'Date')
  metadata.processed = extractField(summaryContent, 'Processed')
  metadata.participants = extractField(summaryContent, 'Participants')
  metadata.videoId = extractField(summaryContent, 'Video ID')
  metadata.region = extractField(summaryContent, 'Region')
  metadata.source = extractField(summaryContent, 'Source')

  // Extract video URL: explicit field first, then title link as fallback
  metadata.videoUrl = extractField(summaryContent, 'Video URL')
  if (!metadata.videoUrl) {
    const titleLinkMatch = summaryContent.match(/^#\s+\[.+?\]\((.+?)\)$/m)
    if (titleLinkMatch) {
      metadata.videoUrl = titleLinkMatch[1].trim()
    }
  }

  // Extract description from first paragraph after metadata separator
  const descriptionMatch = summaryContent.match(/---\s+([\s\S]+?)(?:\n\n|\n#)/)
  if (descriptionMatch) {
    const desc = descriptionMatch[1].trim()
    metadata.description = desc.length > 160
      ? desc.substring(0, 157) + '...'
      : desc
  }

  return metadata
}
