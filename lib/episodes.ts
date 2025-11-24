/**
 * Server-side utilities for reading podcast episode data from disk
 * Used for SSG (Static Site Generation)
 */

import { readdir, readFile } from 'fs/promises'
import { join } from 'path'
import { parseEpisodeMetadata } from './schema'

const PODCAST_WORK_DIR = join(process.cwd(), 'podcast_work')

export interface Episode {
  slug: string
  title: string
  date?: string
  podcast?: string
  participants?: string
  region?: string
  videoId?: string
  videoUrl?: string
  summary?: string
  transcript?: string
}

export interface Podcast {
  name: string
  title: string
  description?: string
  episodes: Episode[]
}

/**
 * Get all podcasts and their episodes
 */
export async function getAllPodcasts(): Promise<Podcast[]> {
  const podcasts: Podcast[] = []

  try {
    const podcastDirs = await readdir(PODCAST_WORK_DIR)

    for (const podcastName of podcastDirs) {
      if (podcastName.startsWith('.')) continue

      const podcastPath = join(PODCAST_WORK_DIR, podcastName)
      const episodes = await getEpisodesForPodcast(podcastName)

      if (episodes.length > 0) {
        podcasts.push({
          name: podcastName,
          title: podcastName,
          description: undefined,
          episodes,
        })
      }
    }
  } catch (err) {
    console.error('Error reading podcasts:', err)
  }

  return podcasts
}

/**
 * Get all episodes for a specific podcast
 */
export async function getEpisodesForPodcast(podcastName: string): Promise<Episode[]> {
  const episodes: Episode[] = []
  const podcastPath = join(PODCAST_WORK_DIR, podcastName)

  try {
    const episodeDirs = await readdir(podcastPath)

    for (const episodeSlug of episodeDirs) {
      if (episodeSlug.startsWith('.')) continue

      const episode = await getEpisode(podcastName, episodeSlug)
      if (episode) {
        episodes.push(episode)
      }
    }
  } catch (err) {
    console.error(`Error reading episodes for ${podcastName}:`, err)
  }

  // Sort by date, newest first (episodes without dates go to bottom)
  episodes.sort((a, b) => {
    // Episodes without dates go to the bottom
    if (!a.date && !b.date) return 0
    if (!a.date) return 1
    if (!b.date) return -1

    // Convert date strings to Date objects for proper chronological comparison
    const dateA = new Date(a.date)
    const dateB = new Date(b.date)

    // Sort newest first (descending order)
    return dateB.getTime() - dateA.getTime()
  })

  return episodes
}

/**
 * Strip metadata header and first h1 from episode summary if present
 * Only strips if we detect the standard episode metadata format
 */
function stripMetadataHeader(content: string): string {
  // Look for --- separator, but only in first 2000 chars to avoid
  // false positives from thematic breaks in the actual content
  const startSection = content.substring(0, 2000)
  const separatorMatch = startSection.match(/\n---\n/)

  if (!separatorMatch || separatorMatch.index === undefined) {
    // No separator found in expected location
    return content
  }

  // Check if the content before separator has episode metadata fields
  const beforeSeparator = content.substring(0, separatorMatch.index)
  const hasEpisodeMetadata =
    beforeSeparator.includes('**Podcast:**') &&
    beforeSeparator.includes('**Date:**') &&
    beforeSeparator.includes('**Transcript:**')

  if (hasEpisodeMetadata) {
    // This is a standard episode format - strip the metadata header
    const afterSeparatorIndex = separatorMatch.index + 5 // '\n---\n' is 5 chars
    let strippedContent = content.substring(afterSeparatorIndex).trim()

    // Also strip the first H1 heading if it starts with "# " or "# Podcast Summary"
    // This removes duplicate titles like "# Podcast Summary: Andrew Ng on AI"
    const lines = strippedContent.split('\n')
    if (lines[0] && (lines[0].startsWith('# Podcast Summary') || lines[0].startsWith('# '))) {
      // Remove first line and any empty lines after it
      strippedContent = lines.slice(1).join('\n').trim()
    }

    return strippedContent
  }

  // Not standard format - return original content
  return content
}

/**
 * Get a specific episode by podcast name and episode slug
 */
export async function getEpisode(podcastName: string, episodeSlug: string): Promise<Episode | null> {
  const episodePath = join(PODCAST_WORK_DIR, podcastName, episodeSlug)

  try {
    // Read summary.md
    const summaryPath = join(episodePath, 'summary.md')
    const summaryContent = await readFile(summaryPath, 'utf-8')

    // Parse metadata from summary
    const metadata = parseEpisodeMetadata(summaryContent)

    // Read transcript.md if it exists
    let transcriptContent: string | undefined
    try {
      const transcriptPath = join(episodePath, 'transcript.md')
      transcriptContent = await readFile(transcriptPath, 'utf-8')
    } catch {
      // Transcript may not exist
      transcriptContent = undefined
    }

    return {
      slug: episodeSlug,
      title: metadata.title || episodeSlug,
      date: metadata.date,
      podcast: metadata.podcast || podcastName,
      participants: metadata.participants,
      region: metadata.region,
      videoId: metadata.videoId,
      videoUrl: metadata.videoUrl,
      summary: stripMetadataHeader(summaryContent),
      transcript: transcriptContent,
    }
  } catch (err) {
    console.error(`Error reading episode ${episodeSlug} in ${podcastName}:`, err)
    return null
  }
}

/**
 * Get all podcast names (for generating static params)
 */
export async function getAllPodcastNames(): Promise<string[]> {
  try {
    const dirs = await readdir(PODCAST_WORK_DIR)
    return dirs.filter(dir => !dir.startsWith('.'))
  } catch (err) {
    console.error('Error reading podcast names:', err)
    return []
  }
}

/**
 * Get all episode slugs for a podcast (for generating static params)
 */
export async function getAllEpisodeSlugs(podcastName: string): Promise<string[]> {
  const podcastPath = join(PODCAST_WORK_DIR, podcastName)

  try {
    const dirs = await readdir(podcastPath)
    return dirs.filter(dir => !dir.startsWith('.'))
  } catch (err) {
    console.error(`Error reading episode slugs for ${podcastName}:`, err)
    return []
  }
}

/**
 * Get all podcast/episode combinations (for sitemap and static params)
 */
export async function getAllEpisodeParams(): Promise<{ name: string; episode: string }[]> {
  const params: { name: string; episode: string }[] = []
  const podcasts = await getAllPodcastNames()

  for (const podcastName of podcasts) {
    const episodes = await getAllEpisodeSlugs(podcastName)
    for (const episodeSlug of episodes) {
      params.push({
        name: podcastName,
        episode: episodeSlug,
      })
    }
  }

  return params
}
