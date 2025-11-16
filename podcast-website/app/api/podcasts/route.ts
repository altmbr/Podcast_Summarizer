import { readdir } from 'fs/promises'
import { join } from 'path'

export async function GET() {
  try {
    const podcastWorkDir = join(process.cwd(), 'podcast_work')
    const entries = await readdir(podcastWorkDir, { withFileTypes: true })

    const podcasts = entries
      .filter(entry => entry.isDirectory() && entry.name !== 'one off episodes')
      .map(async (entry) => {
        try {
          const podcastPath = join(podcastWorkDir, entry.name)
          const episodeDirs = await readdir(podcastPath, { withFileTypes: true })
          const episodeCount = episodeDirs.filter(e => e.isDirectory()).length

          return {
            name: entry.name,
            title: entry.name,
            episodeCount
          }
        } catch (error) {
          console.error(`Error reading podcast ${entry.name}:`, error)
          return {
            name: entry.name,
            title: entry.name,
            episodeCount: 0
          }
        }
      })

    const resolvedPodcasts = await Promise.all(podcasts)

    // Sort by episode count descending, then by name
    const sortedPodcasts = resolvedPodcasts.sort((a, b) => {
      if (b.episodeCount !== a.episodeCount) {
        return b.episodeCount - a.episodeCount
      }
      return a.name.localeCompare(b.name)
    })

    return Response.json(sortedPodcasts)
  } catch (error) {
    console.error('Error loading podcasts:', error)
    return Response.json(
      { error: 'Failed to load podcasts' },
      { status: 500 }
    )
  }
}
