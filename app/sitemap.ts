import { MetadataRoute } from 'next'
import { readdir, readFile } from 'fs/promises'
import { join } from 'path'
import { BASE_URL, PODCAST_WORK_DIR } from '@/lib/constants'
import { parseEpisodeMetadata } from '@/lib/schema'
import { getSourceContentType } from '@/lib/content-types'

interface Episode {
  podcastName: string
  episodeName: string
  lastModified?: Date
  source?: string
}

async function getAllEpisodes(): Promise<Episode[]> {
  const episodes: Episode[] = []

  try {
    const podcasts = await readdir(PODCAST_WORK_DIR)

    for (const podcast of podcasts) {
      if (podcast.startsWith('.')) continue
      const podcastPath = join(PODCAST_WORK_DIR, podcast)

      try {
        const episodeNames = await readdir(podcastPath)

        for (const episodeName of episodeNames) {
          if (episodeName.startsWith('.')) continue

          try {
            const summaryPath = join(podcastPath, episodeName, 'summary.md')
            const summaryContent = await readFile(summaryPath, 'utf-8')
            const metadata = parseEpisodeMetadata(summaryContent)

            let lastModified: Date | undefined
            if (metadata.date) {
              try { lastModified = new Date(metadata.date) } catch { /* skip */ }
            }

            episodes.push({
              podcastName: podcast,
              episodeName,
              lastModified,
              source: metadata.source,
            })
          } catch (err) {
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

  const sitemapEntries: MetadataRoute.Sitemap = [
    { url: BASE_URL, lastModified: new Date(), changeFrequency: 'daily', priority: 1 },
  ]

  // Group episodes by source and determine content type
  const sourceMap = new Map<string, { episodes: Episode[]; type: string }>()
  for (const ep of episodes) {
    if (!sourceMap.has(ep.podcastName)) {
      sourceMap.set(ep.podcastName, { episodes: [], type: 'podcast' })
    }
    sourceMap.get(ep.podcastName)!.episodes.push(ep)
  }

  // Determine content type per source
  for (const [sourceName, data] of sourceMap) {
    const firstSource = data.episodes[0]?.source
    data.type = await getSourceContentType(sourceName, firstSource)
  }

  // Add source index pages and episode pages
  for (const [sourceName, { episodes: sourceEpisodes, type }] of sourceMap) {
    sitemapEntries.push({
      url: `${BASE_URL}/${type}/${encodeURIComponent(sourceName)}`,
      lastModified: new Date(),
      changeFrequency: 'weekly',
      priority: 0.8,
    })

    for (const episode of sourceEpisodes) {
      sitemapEntries.push({
        url: `${BASE_URL}/${type}/${encodeURIComponent(episode.podcastName)}/${encodeURIComponent(episode.episodeName)}`,
        lastModified: episode.lastModified || new Date(),
        changeFrequency: 'monthly',
        priority: 0.6,
      })
    }
  }

  return sitemapEntries
}
