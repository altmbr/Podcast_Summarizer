import { MetadataRoute } from 'next'
import { readdir, readFile } from 'fs/promises'
import { join } from 'path'

const PODCAST_WORK_DIR = join(process.cwd(), 'podcast_work')
const BASE_URL = 'https://teahose.com'

interface Episode {
  podcastName: string
  episodeName: string
  lastModified?: Date
}

async function getAllEpisodes(): Promise<Episode[]> {
  const episodes: Episode[] = []

  try {
    // Read all podcast directories
    const podcasts = await readdir(PODCAST_WORK_DIR)

    for (const podcast of podcasts) {
      // Skip hidden files
      if (podcast.startsWith('.')) continue

      const podcastPath = join(PODCAST_WORK_DIR, podcast)

      try {
        // Read all episode directories
        const episodeNames = await readdir(podcastPath)

        for (const episodeName of episodeNames) {
          // Skip hidden files
          if (episodeName.startsWith('.')) continue

          const episodePath = join(podcastPath, episodeName)

          try {
            // Check if summary.md exists
            const summaryPath = join(episodePath, 'summary.md')
            const summaryContent = await readFile(summaryPath, 'utf-8')

            // Extract date from summary metadata
            const dateMatch = summaryContent.match(/\*\*Date:\*\* (.+)/i)
            let lastModified: Date | undefined

            if (dateMatch) {
              try {
                lastModified = new Date(dateMatch[1])
              } catch {
                // If date parsing fails, use file modification time
                lastModified = undefined
              }
            }

            episodes.push({
              podcastName: podcast,
              episodeName,
              lastModified,
            })
          } catch (err) {
            // Episode directory might not have summary.md yet
            console.error(`Skipping episode ${episodeName} in ${podcast}:`, err)
          }
        }
      } catch (err) {
        console.error(`Error reading podcast ${podcast}:`, err)
      }
    }
  } catch (err) {
    console.error('Error reading podcast_work directory:', err)
  }

  return episodes
}

export default async function sitemap(): Promise<MetadataRoute.Sitemap> {
  const episodes = await getAllEpisodes()

  // Homepage
  const sitemapEntries: MetadataRoute.Sitemap = [
    {
      url: BASE_URL,
      lastModified: new Date(),
      changeFrequency: 'daily',
      priority: 1,
    },
  ]

  // Get unique podcasts
  const uniquePodcasts = [...new Set(episodes.map(e => e.podcastName))]

  // Add podcast index pages
  for (const podcast of uniquePodcasts) {
    sitemapEntries.push({
      url: `${BASE_URL}/podcast/${encodeURIComponent(podcast)}`,
      lastModified: new Date(),
      changeFrequency: 'weekly',
      priority: 0.8,
    })
  }

  // Add episode pages
  for (const episode of episodes) {
    sitemapEntries.push({
      url: `${BASE_URL}/podcast/${encodeURIComponent(episode.podcastName)}/${encodeURIComponent(episode.episodeName)}`,
      lastModified: episode.lastModified || new Date(),
      changeFrequency: 'monthly',
      priority: 0.6,
    })
  }

  return sitemapEntries
}
