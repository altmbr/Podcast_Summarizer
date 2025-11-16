import { readdir, readFile } from 'fs/promises'
import { join } from 'path'
import matter from 'gray-matter'

export async function GET(
  request: Request,
  { params }: { params: Promise<{ name: string }> }
) {
  try {
    const { name } = await params
    const podcastName = decodeURIComponent(name)
    const podcastPath = join(process.cwd(), 'podcast_work', podcastName)

    const episodeDirs = await readdir(podcastPath, { withFileTypes: true })
    const episodes = await Promise.all(
      episodeDirs
        .filter(entry => entry.isDirectory())
        .map(async (entry) => {
          try {
            const summaryPath = join(podcastPath, entry.name, 'summary.md')
            const summaryContent = await readFile(summaryPath, 'utf-8')
            const { data, content } = matter(summaryContent)

            // Extract first paragraph as summary preview
            const firstParagraph = content
              .split('\n\n')
              .find(para => para.trim() && !para.startsWith('#'))
              ?.trim()
              ?.substring(0, 200) || ''

            return {
              slug: entry.name,
              title: data.title || entry.name.replace(/_/g, ' '),
              date: data.date || data.Date || '',
              summary: firstParagraph
            }
          } catch (error) {
            console.error(`Error reading episode ${entry.name}:`, error)
            return {
              slug: entry.name,
              title: entry.name.replace(/_/g, ' '),
              date: '',
              summary: ''
            }
          }
        })
    )

    // Sort by date descending (newest first)
    const sortedEpisodes = episodes.sort((a, b) => {
      if (!a.date) return 1
      if (!b.date) return -1
      return b.date.localeCompare(a.date)
    })

    return Response.json({
      podcast: {
        name: podcastName,
        title: podcastName
      },
      episodes: sortedEpisodes
    })
  } catch (error) {
    console.error('Error loading episodes:', error)
    return Response.json(
      { error: 'Failed to load episodes' },
      { status: 500 }
    )
  }
}
