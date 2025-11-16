import { readFile } from 'fs/promises'
import { join } from 'path'
import matter from 'gray-matter'

export async function GET(
  request: Request,
  { params }: { params: Promise<{ name: string; episode: string }> }
) {
  try {
    const { name, episode } = await params
    const podcastName = decodeURIComponent(name)
    const episodeSlug = decodeURIComponent(episode)
    const episodePath = join(process.cwd(), 'podcast_work', podcastName, episodeSlug)

    // Read summary
    const summaryPath = join(episodePath, 'summary.md')
    const summaryContent = await readFile(summaryPath, 'utf-8')
    const { data: summaryData, content: summaryText } = matter(summaryContent)

    // Read transcript
    let transcriptText = ''
    try {
      const transcriptPath = join(episodePath, 'transcript.md')
      const transcriptContent = await readFile(transcriptPath, 'utf-8')
      const { content: transcript } = matter(transcriptContent)
      transcriptText = transcript
    } catch (error) {
      console.error('Error reading transcript:', error)
    }

    return Response.json({
      title: summaryData.title || episodeSlug.replace(/_/g, ' '),
      date: summaryData.date || summaryData.Date || '',
      podcast: summaryData.podcast || summaryData.Podcast || podcastName,
      participants: summaryData.participants || summaryData.Participants || '',
      region: summaryData.region || summaryData.Region || '',
      videoUrl: summaryData['video url'] || summaryData['Video URL'] || '',
      summary: summaryText,
      transcript: transcriptText
    })
  } catch (error) {
    console.error('Error loading episode:', error)
    return Response.json(
      { error: 'Failed to load episode' },
      { status: 500 }
    )
  }
}
