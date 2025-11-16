export async function GET() {
  try {
    const mockPodcasts = [
      {
        name: '20VC',
        title: '20VC: Conversations with Emerging Founders & VCs',
        description: 'Insights on venture capital, entrepreneurship, and building companies.',
        episodeCount: 12,
      },
      {
        name: 'masters-of-scale',
        title: 'Masters of Scale',
        description: 'How to build and scale successful organizations.',
        episodeCount: 8,
      },
      {
        name: 'the-tim-ferriss-show',
        title: 'The Tim Ferriss Show',
        description: 'Interviews with world-class performers.',
        episodeCount: 15,
      },
    ]

    return Response.json(mockPodcasts)
  } catch (error) {
    console.error('Error loading podcasts:', error)
    return Response.json(
      { error: 'Failed to load podcasts' },
      { status: 500 }
    )
  }
}
