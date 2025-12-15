import { readdir, readFile } from 'fs/promises'
import { join } from 'path'
import { parseEpisodeMetadata } from '@/lib/schema'
import { parseEpisodeDate } from '@/lib/dates'

export async function GET() {
  try {
    const podcastWorkDir = join(process.cwd(), 'podcast_work')
    const podcastDirs = await readdir(podcastWorkDir, { withFileTypes: true })

    const allEpisodes: Array<{
      slug: string
      title: string
      date: string
      podcast: string
      podcastName: string
      dateObj: Date
    }> = []

    // Iterate through all podcasts
    for (const podcastDir of podcastDirs) {
      if (!podcastDir.isDirectory()) continue

      const podcastPath = join(podcastWorkDir, podcastDir.name)
      const episodeDirs = await readdir(podcastPath, { withFileTypes: true })

      // Iterate through all episodes in this podcast
      for (const episodeDir of episodeDirs) {
        if (!episodeDir.isDirectory()) continue

        try {
          // Read summary.md to get metadata
          const summaryPath = join(podcastPath, episodeDir.name, 'summary.md')
          const summaryContent = await readFile(summaryPath, 'utf-8')
          const metadata = parseEpisodeMetadata(summaryContent)

          if (metadata.date) {
            const dateObj = parseEpisodeDate(metadata.date)
            if (dateObj) {
              allEpisodes.push({
                slug: episodeDir.name,
                title: metadata.title || episodeDir.name,
                date: metadata.date,
                podcast: podcastDir.name,
                podcastName: metadata.podcast || podcastDir.name,
                dateObj
              })
            }
          }
        } catch (error) {
          // Skip episodes that can't be read
          console.error(`Error reading episode ${episodeDir.name}:`, error)
        }
      }
    }

    // Sort by date, newest first, and take top 10
    const recentEpisodes = allEpisodes
      .sort((a, b) => b.dateObj.getTime() - a.dateObj.getTime())
      .slice(0, 10)
      .map(({ dateObj, ...episode }) => episode) // Remove dateObj from response

    return Response.json(recentEpisodes)
  } catch (error) {
    console.error('Error loading recent episodes:', error)
    return Response.json(
      { error: 'Failed to load recent episodes' },
      { status: 500 }
    )
  }
}
