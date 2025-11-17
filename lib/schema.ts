/**
 * Schema.org structured data utilities for SEO
 */

export interface EpisodeMetadata {
  title: string
  podcast: string
  date: string
  participants?: string
  videoId?: string
  videoUrl?: string
  region?: string
  description?: string
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
    url: `https://teahose.com/podcast/${encodeURIComponent(podcastName)}/${encodeURIComponent(episodeSlug)}`,
    datePublished: episode.date,
    partOfSeries: {
      '@type': 'PodcastSeries',
      name: episode.podcast,
      url: `https://teahose.com/podcast/${encodeURIComponent(podcastName)}`,
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
    url: `https://teahose.com/podcast/${encodeURIComponent(podcast.name)}`,
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
    url: 'https://teahose.com',
    logo: 'https://teahose.com/og-image.png',
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
    url: 'https://teahose.com',
    description: 'Summaries of the most important tech podcasts — including China\'s.',
    potentialAction: {
      '@type': 'SearchAction',
      target: {
        '@type': 'EntryPoint',
        urlTemplate: 'https://teahose.com/?q={search_term_string}',
      },
      'query-input': 'required name=search_term_string',
    },
  }
}

/**
 * Parse episode metadata from summary markdown content
 */
export function parseEpisodeMetadata(summaryContent: string): Partial<EpisodeMetadata> {
  const metadata: Partial<EpisodeMetadata> = {}

  // Extract title (first # heading)
  const titleMatch = summaryContent.match(/^#\s+(.+?)$/m)
  if (titleMatch) {
    let title = titleMatch[1].trim()
    // Remove markdown link syntax: [text](url) -> text
    title = title.replace(/\[(.+?)\]\(.+?\)/g, '$1')
    // Remove any remaining brackets: [text] -> text
    title = title.replace(/^\[(.+?)\]$/, '$1')
    metadata.title = title
  }

  // Extract podcast name
  const podcastMatch = summaryContent.match(/\*\*Podcast:\*\*\s+(.+)/i)
  if (podcastMatch) {
    metadata.podcast = podcastMatch[1].trim()
  }

  // Extract date
  const dateMatch = summaryContent.match(/\*\*Date:\*\*\s+(.+)/i)
  if (dateMatch) {
    metadata.date = dateMatch[1].trim()
  }

  // Extract participants
  const participantsMatch = summaryContent.match(/\*\*Participants:\*\*\s+(.+)/i)
  if (participantsMatch) {
    metadata.participants = participantsMatch[1].trim()
  }

  // Extract video ID
  const videoIdMatch = summaryContent.match(/\*\*Video ID:\*\*\s+(.+)/i)
  if (videoIdMatch) {
    metadata.videoId = videoIdMatch[1].trim()
  }

  // Extract video URL
  const videoUrlMatch = summaryContent.match(/\*\*Video URL:\*\*\s+(.+)/i)
  if (videoUrlMatch) {
    metadata.videoUrl = videoUrlMatch[1].trim()
  }

  // Extract region
  const regionMatch = summaryContent.match(/\*\*Region:\*\*\s+(.+)/i)
  if (regionMatch) {
    metadata.region = regionMatch[1].trim()
  }

  // Extract description from first paragraph after metadata
  const descriptionMatch = summaryContent.match(/---\s+([\s\S]+?)(?:\n\n|\n#)/)
  if (descriptionMatch) {
    const desc = descriptionMatch[1].trim()
    // Limit to ~160 characters for meta description
    metadata.description = desc.length > 160
      ? desc.substring(0, 157) + '...'
      : desc
  }

  return metadata
}
