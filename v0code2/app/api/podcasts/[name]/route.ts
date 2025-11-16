export async function GET(
  request: Request,
  { params }: { params: { name: string } }
) {
  try {
    const { name } = params

    const mockEpisodes: Record<string, any> = {
      '20VC': {
        podcast: {
          title: '20VC: Conversations with Emerging Founders & VCs',
          description: 'Weekly episodes exploring venture capital and entrepreneurship.',
        },
        episodes: [
          {
            slug: 'episode-1-startup-funding',
            title: 'How to Raise Your First Round of Funding',
            date: '2024-11-15',
            summary: 'Discussion on fundraising strategies for early-stage startups.',
          },
          {
            slug: 'episode-2-scaling-teams',
            title: 'Building and Scaling High-Performance Teams',
            date: '2024-11-08',
            summary: 'Best practices for hiring and team development.',
          },
        ],
      },
      'masters-of-scale': {
        podcast: {
          title: 'Masters of Scale',
          description: 'Learn from founders and leaders who have scaled organizations.',
        },
        episodes: [
          {
            slug: 'episode-1-growth-mindset',
            title: 'The Growth Mindset Framework',
            date: '2024-11-10',
            summary: 'How companies think about rapid growth and scaling.',
          },
        ],
      },
    }

    const data = mockEpisodes[name]
    if (!data) {
      return Response.json({ error: 'Podcast not found' }, { status: 404 })
    }

    return Response.json(data)
  } catch (error) {
    console.error('Error loading podcast:', error)
    return Response.json({ error: 'Failed to load podcast' }, { status: 500 })
  }
}
