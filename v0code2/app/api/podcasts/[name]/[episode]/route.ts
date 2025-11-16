export async function GET(
  request: Request,
  { params }: { params: { name: string; episode: string } }
) {
  try {
    const { name, episode } = params

    const mockContent: Record<string, any> = {
      '20VC/episode-1-startup-funding': {
        title: 'How to Raise Your First Round of Funding',
        date: '2024-11-15',
        summary: `# Summary

## Key Insights
- Prepare a clear pitch deck before approaching investors
- Focus on traction and market validation
- Build relationships with investors early
- Have a well-defined use of proceeds

## Main Topics
1. Pre-seed vs Seed funding differences
2. Common mistakes when pitching
3. Due diligence process
4. Legal considerations`,
        transcript: `# Transcript

**Host:** Welcome back to 20VC. Today we're discussing how to raise your first round of funding.

**Guest:** Thanks for having me. The first round is all about demonstrating traction and having a clear story about where you're going.

**Host:** What are the most common mistakes you see?

**Guest:** Founders often focus too much on the product and not enough on the market opportunity. Investors want to see that you understand your customers and can reach them.

**Host:** How much should a founder raise?

**Guest:** It depends on runway and milestones. Typically, teams raise 18-24 months of runway so they can focus on building and hitting key metrics.`,
      },
      '20VC/episode-2-scaling-teams': {
        title: 'Building and Scaling High-Performance Teams',
        date: '2024-11-08',
        summary: `# Summary

## Key Points
- Early hires set the culture of your organization
- Hire for values and attitude, train for skills
- Create clear feedback loops and career paths
- Performance management is critical

## Discussion Areas
- Recruiting strategies for startups
- Onboarding best practices
- Building psychological safety`,
        transcript: `# Transcript

**Host:** How do you think about first hires?

**Guest:** Your first 10 people define your culture. You need to hire people who are aligned with your vision and can wear multiple hats.

**Host:** What about compensation?

**Guest:** Early stage, you're often competing with better funded companies, so you need to offer equity, mission, and the opportunity to learn.`,
      },
      'masters-of-scale/episode-1-growth-mindset': {
        title: 'The Growth Mindset Framework',
        date: '2024-11-10',
        summary: `# Summary

## Framework Overview
- Adopt a growth mindset towards your business
- Focus on learning from failures
- Iterate quickly and gather feedback

## Action Steps
1. Define success metrics
2. Run experiments
3. Measure and analyze results`,
        transcript: `# Transcript

**Host:** What does scale really mean?

**Guest:** Scale isn't just about getting bigger. It's about creating leverage—doing more with efficient systems.`,
      },
    }

    const key = `${name}/${episode}`
    const data = mockContent[key]

    if (!data) {
      return Response.json({ error: 'Episode not found' }, { status: 404 })
    }

    return Response.json(data)
  } catch (error) {
    console.error('Error loading episode:', error)
    return Response.json({ error: 'Failed to load episode' }, { status: 500 })
  }
}
