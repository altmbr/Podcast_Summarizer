import { readFile } from 'fs/promises'
import { join } from 'path'

export type ContentType = 'podcast' | 'newsletter' | 'paper'

const VALID_TYPES = new Set<ContentType>(['podcast', 'newsletter', 'paper'])

export function isValidContentType(type: string): type is ContentType {
  return VALID_TYPES.has(type as ContentType)
}

export function getContentLabels(type: ContentType) {
  switch (type) {
    case 'paper':
      return {
        singular: 'paper',
        plural: 'papers',
        backToItem: '← Back to Papers',
        backToHome: '← Back to Home',
        sourcePrefix: 'Lab',
        metaSuffix: 'Paper Summaries',
        metaDescription: (name: string, count: number) =>
          `Browse ${count} paper${count !== 1 ? 's' : ''} from ${name}. AI-generated summaries of Physical AI research papers.`,
        itemNotFound: 'Paper Not Found',
        footerMessage: 'Explore the key findings from this paper.',
      }
    case 'newsletter':
      return {
        singular: 'issue',
        plural: 'issues',
        backToItem: '← Back to Issues',
        backToHome: '← Back to Home',
        sourcePrefix: 'Newsletter',
        metaSuffix: 'Newsletter Summaries',
        metaDescription: (name: string, count: number) =>
          `Browse ${count} issue${count !== 1 ? 's' : ''} from ${name}. AI-generated summaries of newsletter issues.`,
        itemNotFound: 'Issue Not Found',
        footerMessage: 'Explore the key insights from this issue.',
      }
    default:
      return {
        singular: 'episode',
        plural: 'episodes',
        backToItem: '← Back to Episodes',
        backToHome: '← Back to Home',
        sourcePrefix: 'Podcast',
        metaSuffix: 'Podcast Summaries',
        metaDescription: (name: string, count: number) =>
          `Browse ${count} episode${count !== 1 ? 's' : ''} from ${name}. AI-generated summaries and transcripts for tech podcast episodes.`,
        itemNotFound: 'Episode Not Found',
        footerMessage: 'Reflect on the key insights from this episode.',
      }
  }
}

export function contentTypeFromSource(source?: string): ContentType {
  if (source === 'paper') return 'paper'
  if (source === 'newsletter') return 'newsletter'
  return 'podcast'
}

let _newsletterNames: Set<string> | null = null

async function getNewsletterNames(): Promise<Set<string>> {
  if (_newsletterNames) return _newsletterNames
  const names = new Set<string>()
  try {
    const configPath = join(process.cwd(), 'newsletter_config.json')
    const content = await readFile(configPath, 'utf-8')
    const config = JSON.parse(content)
    for (const entry of Object.values(config) as Array<{ name?: string }>) {
      if (entry.name) names.add(entry.name)
    }
  } catch { /* no config */ }
  _newsletterNames = names
  return names
}

export async function getSourceContentType(sourceName: string, firstEpisodeSource?: string): Promise<ContentType> {
  if (firstEpisodeSource === 'paper') return 'paper'
  const newsletters = await getNewsletterNames()
  if (newsletters.has(sourceName)) return 'newsletter'
  return 'podcast'
}
