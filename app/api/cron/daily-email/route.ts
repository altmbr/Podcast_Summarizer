import { kv } from '@vercel/kv'
import type { NextRequest } from 'next/server'
import { readdir, readFile } from 'fs/promises'
import { join } from 'path'
import { parseEpisodeMetadata } from '@/lib/schema'
import { createHmac } from 'crypto'

const SUBSCRIBER_EMAILS_KEY = 'subscriber-emails'
const SUBSCRIBER_PREFIX = 'subscriber:'
const SENDGRID_API_URL = 'https://api.sendgrid.com/v3/mail/send'

// Feature flag for header image style
// true = new composite style with unified scene, nametags, worn paper texture
// false = old panel-based style with separate panels per episode
// To revert: set USE_COMPOSITE_HEADER = false
const USE_COMPOSITE_HEADER = true

interface Episode {
  podcast_name: string
  title: string
  slug: string
  date: string
  summary_content: string
  description?: string
  participants?: string
}

// Verify this is a legitimate cron request
function verifyCronRequest(request: NextRequest): boolean {
  const authHeader = request.headers.get('authorization')
  const cronSecret = process.env.CRON_SECRET

  // If CRON_SECRET is set, verify it
  if (cronSecret && authHeader !== `Bearer ${cronSecret}`) {
    return false
  }

  return true
}

interface SubscriberData {
  subscribed: boolean
  signupDate: string
  unsubscribeDate?: string
}

// Token generation utility (matches /api/unsubscribe)
function generateUnsubscribeToken(email: string): string {
  const secret = process.env.UNSUBSCRIBE_SECRET || process.env.CRON_SECRET || 'fallback-secret'
  const hmac = createHmac('sha256', secret)
  hmac.update(email)
  const hash = hmac.digest('base64url')
  return hash
}

async function getSubscribers(): Promise<string[]> {
  try {
    const allEmails = await kv.lrange(SUBSCRIBER_EMAILS_KEY, 0, -1) as string[]
    const activeSubscribers: string[] = []

    // Filter for active subscribers only (subscribed: true)
    for (const email of allEmails) {
      const data = await kv.hgetall(`${SUBSCRIBER_PREFIX}${email}`) as SubscriberData | null
      if (data && data.subscribed) {
        activeSubscribers.push(email)
      }
    }

    return activeSubscribers
  } catch (error) {
    console.error('Failed to fetch subscribers:', error)
    return []
  }
}

async function getEpisodesFromLastNHours(hours: number = 24): Promise<Episode[]> {
  const podcastWorkDir = join(process.cwd(), 'podcast_work')
  const now = new Date()
  const cutoffDate = new Date(now)
  cutoffDate.setHours(cutoffDate.getHours() - hours)

  console.log('Current server time:', now.toISOString())
  console.log(`Cutoff date (${hours}h ago):`, cutoffDate.toISOString())

  const episodes: Episode[] = []

  try {
    const podcastDirs = await readdir(podcastWorkDir, { withFileTypes: true })

    for (const podcastDir of podcastDirs) {
      if (!podcastDir.isDirectory()) continue

      const podcastPath = join(podcastWorkDir, podcastDir.name)
      const episodeDirs = await readdir(podcastPath, { withFileTypes: true })

      for (const episodeDir of episodeDirs) {
        if (!episodeDir.isDirectory()) continue

        try {
          const summaryPath = join(podcastPath, episodeDir.name, 'summary.md')
          const summaryContent = await readFile(summaryPath, 'utf-8')
          const metadata = parseEpisodeMetadata(summaryContent)

          if (metadata.date) {
            // Try parsing the date
            let episodeDate: Date
            try {
              episodeDate = new Date(metadata.date + 'T12:00:00Z') // Set to noon UTC to avoid edge cases

              // Validate the date
              if (isNaN(episodeDate.getTime())) {
                console.log(`Invalid date for episode "${metadata.title}": ${metadata.date}`)
                continue
              }
            } catch (e) {
              console.log(`Failed to parse date for episode "${metadata.title}": ${metadata.date}`)
              continue
            }

            console.log(`Episode "${metadata.title}": date=${metadata.date}, parsed=${episodeDate.toISOString()}, includes=${episodeDate >= cutoffDate}`)

            // Only include episodes from last 24 hours
            if (episodeDate >= cutoffDate) {
              episodes.push({
                podcast_name: metadata.podcast || podcastDir.name,
                title: metadata.title || episodeDir.name,
                slug: episodeDir.name,
                date: metadata.date,
                summary_content: summaryContent,
                participants: metadata.participants
              })
            }
          }
        } catch (e) {
          console.error(`Error reading episode ${episodeDir.name}:`, e)
        }
      }
    }
  } catch (error) {
    console.error('Error reading podcast_work directory:', error)
  }

  console.log(`Found ${episodes.length} episodes from last 24 hours`)

  // Sort by date, newest first
  episodes.sort((a, b) => new Date(b.date).getTime() - new Date(a.date).getTime())
  return episodes
}

function extractKeyThemes(summaryContent: string): string {
  // Find Key Themes and Contrarian Perspectives sections
  const lines = summaryContent.split('\n')
  let inRelevantSection = false
  let extractedContent: string[] = []

  for (const line of lines) {
    // Start capturing at Key Themes
    if (/^##?\s*(?:1\.|A\.)\s*Key\s+Themes/i.test(line)) {
      inRelevantSection = true
      continue
    }
    // Continue capturing at Contrarian Perspectives
    if (/^##?\s*(?:2\.|B\.)\s*Contrarian\s+Perspectives?/i.test(line)) {
      inRelevantSection = true
      continue
    }
    if (inRelevantSection) {
      // Stop at other major sections (Companies, People, etc)
      if (/^##\s*(?:3\.|4\.|C\.|D\.)/.test(line)) {
        break
      }
      extractedContent.push(line)
    }
  }

  if (extractedContent.length > 0) {
    return extractedContent.join('\n').trim().slice(0, 3000)
  }
  return summaryContent.slice(0, 3000)
}

async function generateDescription(episode: Episode): Promise<string> {
  const anthropicKey = process.env.ANTHROPIC_API_KEY
  if (!anthropicKey) {
    return 'New episode available.'
  }

  const summaryExcerpt = extractKeyThemes(episode.summary_content)
  if (!summaryExcerpt) {
    return 'New episode available.'
  }

  const prompt = `Write a pithy, signal-dense summary (max 45 words) of this podcast episode. Cover: main discussion topics, key themes, and any contrarian insights. Be specific and punchy.

Episode: ${episode.title}

Key themes:
${summaryExcerpt}

Summary:`

  try {
    const response = await fetch('https://api.anthropic.com/v1/messages', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'x-api-key': anthropicKey,
        'anthropic-version': '2023-06-01'
      },
      body: JSON.stringify({
        model: 'claude-sonnet-4-5-20250929',
        max_tokens: 150,
        messages: [{ role: 'user', content: prompt }]
      })
    })

    const data = await response.json()
    return data.content?.[0]?.text?.trim() || 'New episode available.'
  } catch {
    return 'New episode available.'
  }
}

// OLD STYLE: Panel-based header image (set USE_COMPOSITE_HEADER = false to use this)
async function generatePanelHeaderImage(episodes: Episode[], dateStr: string): Promise<string | null> {
  const googleApiKey = process.env.GOOGLE_API_KEY
  if (!googleApiKey) {
    console.log('GOOGLE_API_KEY not set - skipping header image')
    return null
  }

  // Extract key insights from episode titles (max 60 chars)
  const topics: string[] = []
  for (const ep of episodes.slice(0, 6)) {
    let title = ep.title

    // Remove person/company prefixes (everything before colon)
    title = title.replace(/^[^:]+:\s*/, '')

    // Take first meaningful part before pipe/dash
    title = title.split(/\s*[\|\-]\s*/)[0]

    // Smart compression: keep the core insight
    if (title.length > 60) {
      // Remove verbose question words and filler
      title = title
        .replace(/^(Why|How|What|When|Where|Are|Is|Do|Does|Can|Will)\s+/i, '')
        .replace(/\b(the|a|an|and|or|but|in|on|at|to|for|of|with|from|that|this|these|those)\b/gi, '')
        .replace(/\s+/g, ' ')
        .trim()

      // If still too long, take first 60 chars at word boundary
      if (title.length > 60) {
        title = title.slice(0, 60).replace(/\s+\S*$/, '').trim()
      }
    }

    topics.push(title)
  }

  const numTopics = topics.length

  // Determine layout
  let layout: string
  let panelDesc: string

  if (numTopics === 1) {
    layout = '1 large panel filling the entire image'
    panelDesc = `Single Panel: "${topics[0]}"`
  } else if (numTopics === 2) {
    layout = '2 panels stacked vertically'
    panelDesc = `Panel 1: "${topics[0]}"\nPanel 2: "${topics[1]}"`
  } else if (numTopics === 3) {
    layout = '3 panels stacked vertically'
    panelDesc = topics.map((t, i) => `Panel ${i + 1}: "${t}"`).join('\n')
  } else if (numTopics === 4) {
    layout = '4 panels in a 2x2 grid'
    panelDesc = topics.map((t, i) => `Panel ${i + 1}: "${t}"`).join('\n')
  } else if (numTopics === 5) {
    layout = '5 panels: 1 wide panel at top spanning full width, then 2 rows of 2 panels each below'
    panelDesc = topics.map((t, i) => `Panel ${i + 1}: "${t}"`).join('\n')
  } else {
    layout = '6 panels in a 2x3 grid (2 columns, 3 rows)'
    panelDesc = topics.map((t, i) => `Panel ${i + 1}: "${t}"`).join('\n')
  }

  const prompt = `Create a vintage 1950s newspaper-style comic header for a daily podcast digest.

LAYOUT: ${layout} in PORTRAIT format.

STYLE: Vintage Roy Lichtenstein pop art with Ben Day dots, bold primary colors, thick black outlines.

PANEL CONTENT:
${panelDesc}

NO FOOTER - illustration fills the entire image

REQUIREMENTS:
- All ${numTopics} panels clearly visible
- All text legible and bold
- Portrait orientation (taller than wide)
- Vintage newspaper comic aesthetic`

  try {
    const { GoogleGenAI } = await import('@google/genai')
    const ai = new GoogleGenAI({ apiKey: googleApiKey })

    // Use gemini-3-pro-image-preview (Nano Banana Pro) - same model that works in test script
    const response = await ai.models.generateContent({
      model: 'gemini-3-pro-image-preview',
      contents: [prompt],
    })

    // Extract and return the generated image as base64 data URL
    const candidates = response.candidates || []
    for (const candidate of candidates) {
      const parts = candidate.content?.parts || []
      for (const part of parts) {
        if (part.inlineData) {
          const mimeType = part.inlineData.mimeType || 'image/png'
          const data = part.inlineData.data
          console.log('Image generated successfully')
          return `data:${mimeType};base64,${data}`
        }
      }
    }

    console.log('No image data in Gemini response')
    return null
  } catch (error) {
    console.error('Failed to generate header image:', error)
    return null
  }
}

// NEW STYLE: Composite header image with unified scene and nametags
async function generateVisualConcept(episodes: Episode[]): Promise<string> {
  const anthropicKey = process.env.ANTHROPIC_API_KEY
  if (!anthropicKey) {
    return 'A collage of tech industry themes including AI, business strategy, and innovation.'
  }

  // Format episode information for Claude
  const episodesText = episodes.slice(0, 5).map((ep, i) => {
    const participantsStr = ep.participants ? ` [${ep.participants}]` : ''
    return `${i + 1}. ${ep.title}${participantsStr}\n   ${ep.description || ''}`
  }).join('\n\n')

  const prompt = `You are creating a vintage 1950s newspaper-style comic illustration that combines visual elements from ${episodes.length} podcast episodes into ONE unified composition.

Here are the episodes:

${episodesText}

Create a detailed description of a single unified illustration that combines visual metaphors representing all episodes. The illustration should:
- Blend elements from all episodes into one cohesive scene (like a vintage political cartoon)
- Use overlapping figures, symbols, and objects
- Include human figures in 1950s comic book style representing the speakers/topics (IMPORTANT: mention participant names when known so they can be labeled)
- Use symbolic objects (books, technology, microphones, abstract concepts)
- Create visual interest and narrative density

Describe the unified composition in 3-4 sentences. Be specific about what visual elements appear and how they interact. When describing human figures, include the participant names from the episode metadata.`

  try {
    const response = await fetch('https://api.anthropic.com/v1/messages', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'x-api-key': anthropicKey,
        'anthropic-version': '2023-06-01'
      },
      body: JSON.stringify({
        model: 'claude-sonnet-4-5-20250929',
        max_tokens: 300,
        messages: [{ role: 'user', content: prompt }]
      })
    })

    const data = await response.json()
    return data.content?.[0]?.text?.trim() || 'A collage of tech industry themes including AI, business strategy, and innovation.'
  } catch {
    return 'A collage of tech industry themes including AI, business strategy, and innovation.'
  }
}

async function generateCompositeHeaderImage(episodes: Episode[], dateStr: string): Promise<string | null> {
  const googleApiKey = process.env.GOOGLE_API_KEY
  if (!googleApiKey) {
    console.log('GOOGLE_API_KEY not set - skipping header image')
    return null
  }

  // Generate visual concept using Claude
  console.log('Generating visual concept with Claude...')
  const visualConcept = await generateVisualConcept(episodes)
  console.log('Visual concept:', visualConcept.slice(0, 100) + '...')

  const prompt = `Create a vintage 1950s newspaper-style composite illustration for a podcast digest header.

CRITICAL LAYOUT REQUIREMENTS:
- LANDSCAPE format: EXACTLY 750 pixels wide × 500 pixels tall
- Single unified composition (NOT separate panels)
- NO footer text or banner - the illustration should fill the entire image
- Warm aged cream paper background (#f7f4f0)
- Thick black border (3px) around entire image

ARTISTIC STYLE - Vintage 1950s Roy Lichtenstein pop art:
- BACKGROUND: Warm aged cream paper (#f7f4f0) with subtle halftone texture
- PAPER TEXTURE: Add worn, aged paper effect with slight yellowing, subtle creases, and soft edge wear to give authentic vintage newspaper feel
- COLORS: Bold pop art accents - cardinal red (#c41e3a), golden yellow (#f4c430), deep blue (#2d5a7b)
- SHADOWS: Black comic drop shadows (not brown)
- TEXTURE: Ben Day halftone dots for shading, stipple patterns
- OUTLINES: Thick black outlines (3px) around all major elements
- OVERALL: Clean vintage newspaper comic aesthetic with worn paper texture

VISUAL COMPOSITION:
${visualConcept}

SPECIFIC REQUIREMENTS:
- Human figures in vintage comic book style with halftone shading
- NAMETAGS: Each human figure MUST wear a nametag on their chest with their name in BIG, BOLD, LEGIBLE UPPERCASE letters (like "ELON MUSK", "SAM ALTMAN", etc.)
- Nametags should be rectangular/rounded white/cream labels with thick black outlines and large black text
- Symbolic objects (books, technology, microphones, brains, buildings, etc.)
- Elements should blend and overlap to create narrative density
- Dynamic composition with depth and visual flow

COLOR USAGE:
- Overall background: warm cream (#f7f4f0)
- Main subjects use bold accent colors (cardinal red, golden yellow, deep blue)
- Supporting elements use lighter tints (soft red #fdf5f5, soft yellow #fffcf0, soft blue #f5f8fa)
- All borders and outlines: true black (#1a1a1a)
- Ben Day dot patterns for shading and depth

OVERALL AESTHETIC:
- Sophisticated vintage newspaper illustration with worn paper texture
- Educational and thought-provoking
- Multiple narratives visible in single unified composition
- Professional print quality with sharp lines
- Perfect for email newsletter banner`

  try {
    const { GoogleGenAI } = await import('@google/genai')
    const ai = new GoogleGenAI({ apiKey: googleApiKey })

    const response = await ai.models.generateContent({
      model: 'gemini-3-pro-image-preview',
      contents: [prompt],
    })

    const candidates = response.candidates || []
    for (const candidate of candidates) {
      const parts = candidate.content?.parts || []
      for (const part of parts) {
        if (part.inlineData) {
          const mimeType = part.inlineData.mimeType || 'image/png'
          const data = part.inlineData.data
          console.log('Composite image generated successfully')
          return `data:${mimeType};base64,${data}`
        }
      }
    }

    console.log('No image data in Gemini response')
    return null
  } catch (error) {
    console.error('Failed to generate composite header image:', error)
    return null
  }
}

// Router function to pick header image style based on feature flag
async function generateHeaderImage(episodes: Episode[], dateStr: string): Promise<string | null> {
  if (USE_COMPOSITE_HEADER) {
    return generateCompositeHeaderImage(episodes, dateStr)
  } else {
    return generatePanelHeaderImage(episodes, dateStr)
  }
}

function generateEmailHtml(episodes: Episode[], dateStr: string, hasImage: boolean, unsubscribeToken: string): string {
  const colors = {
    background: '#f7f4f0',
    foreground: '#1a1a1a',
    card: '#fffefa',
    muted_foreground: '#555555',
    accent: '#c41e3a',
    border: '#1a1a1a',
  }

  // Use CID reference for inline image attachment
  const headerImgHtml = hasImage
    ? `<img src="cid:header_image" style="width: 100%; max-width: 800px; height: auto; margin: 0 0 32px 0;" alt="Daily Teahose Header">`
    : ''

  let episodeCards = ''

  episodes.forEach((episode, index) => {
    const encodedPodcast = encodeURIComponent(episode.podcast_name)
    const encodedSlug = encodeURIComponent(episode.slug)
    const summaryUrl = `https://teahose.com/podcast/${encodedPodcast}/${encodedSlug}?ref=email`
    const formattedDate = new Date(episode.date).toLocaleDateString('en-US', {
      month: 'long',
      day: 'numeric',
      year: 'numeric'
    })

    const participantsHtml = episode.participants
      ? `<p style="color: ${colors.foreground}; font-size: 14px; margin: 0 0 8px 0;">${episode.participants}</p>`
      : ''

    const isLast = index === episodes.length - 1
    const marginBottom = isLast ? '0' : '24px'

    episodeCards += `
        <a href="${summaryUrl}" style="text-decoration: none; display: block;">
            <div style="background: ${colors.card}; padding: 24px 16px; margin-bottom: ${marginBottom}; border: 3px solid ${colors.border};">
                <h2 style="margin: 0 0 6px 0; font-size: 24px; font-weight: 700; letter-spacing: -0.01em; text-transform: uppercase; color: ${colors.foreground};">
                    ${episode.title}
                </h2>
                <p style="color: ${colors.muted_foreground}; font-size: 13px; text-transform: uppercase; letter-spacing: 0.5px; margin: 0 0 4px 0;">${episode.podcast_name}</p>
                ${participantsHtml}
                <p style="color: ${colors.muted_foreground}; font-size: 12px; margin: 0 0 12px 0;">${formattedDate}</p>
                <p style="color: ${colors.foreground}; font-size: 15px; line-height: 1.75; margin: 0;">
                    ${episode.description || 'New episode available.'}
                </p>
            </div>
        </a>`
  })

  // EMAIL HTML STRUCTURE NOTES:
  // - Use simple div-based layout (works in Gmail, Apple Mail, most clients)
  // - The Python generate_daily_email.py uses divs and works fine
  // - Keep unsubscribe INSIDE the main bordered div

  return `<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>The Daily Teahose - ${dateStr}</title>
</head>
<body style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; line-height: 1.6; color: ${colors.foreground}; max-width: 700px; margin: 0 auto; padding: 20px; background-color: ${colors.background};">

    <!-- Main bordered card - ALL CONTENT INCLUDING UNSUBSCRIBE INSIDE THIS TABLE -->
    <table width="100%" cellpadding="0" cellspacing="0" border="0" style="max-width: 700px; margin: 0 auto;">
        <tr>
            <td style="background: ${colors.card}; padding: 32px; border: 3px solid ${colors.border};">

        <!-- Header -->
        <div style="text-align: center; margin-bottom: 24px;">
            <a href="https://teahose.com?ref=email" style="text-decoration: none;">
                <h1 style="margin: 0 0 20px 0; font-size: 28px; font-weight: 900; text-transform: uppercase; color: ${colors.foreground}; letter-spacing: -0.02em;">
                    THE DAILY TEAHOSE
                </h1>
            </a>
            <div style="border: 2px solid ${colors.border}; padding: 12px 16px; display: inline-block; white-space: nowrap;">
                <span style="color: ${colors.foreground}; font-size: 14px;">Forwarded this email? Get daily summaries of top tech and business podcasts. </span>
                <a href="https://teahose.com?ref=email" style="display: inline-block; background: ${colors.foreground}; color: ${colors.card}; padding: 8px 16px; text-decoration: none; font-weight: 600; font-size: 14px; margin-left: 8px;">Sign Up</a>
            </div>
        </div>

        <hr style="border: none; border-top: 1px solid ${colors.muted_foreground}; margin: 24px 0;">

        <!-- Header Image -->
        ${headerImgHtml}

        <!-- Episode Cards -->
        ${episodeCards}

        <!-- Footer with Unsubscribe - INSIDE the bordered td -->
        <table width="100%" cellpadding="0" cellspacing="0" border="0" style="margin-top: 32px; padding-top: 24px; border-top: 1px solid ${colors.muted_foreground};">
            <tr>
                <td align="center" style="color: ${colors.muted_foreground}; font-size: 13px; line-height: 1.6; padding-bottom: 12px;">
                    A distillation of insight from the highest signal technology and entrepreneurship podcasts.
                </td>
            </tr>
            <tr>
                <td align="center" style="color: ${colors.muted_foreground}; font-size: 13px;">
                    <a href="https://teahose.com?ref=email" style="color: ${colors.accent}; text-decoration: underline;">Teahose.com</a> · <a href="https://www.teahose.com/unsubscribe?token=${unsubscribeToken}" style="color: ${colors.muted_foreground}; text-decoration: underline;">Unsubscribe</a>
                </td>
            </tr>
        </table>

            </td>
        </tr>
    </table>
    <!-- End main bordered card -->

</body>
</html>`
}

async function sendEmail(to: string[], subject: string, episodes: Episode[], dateStr: string, imageBase64: string | null): Promise<boolean> {
  const sendgridKey = process.env.SENDGRID_API_KEY

  if (!sendgridKey) {
    console.error('SENDGRID_API_KEY not set')
    return false
  }

  // Send personalized emails with unique unsubscribe tokens
  let successCount = 0
  let failureCount = 0

  for (const email of to) {
    // Generate unique unsubscribe token for this subscriber
    const unsubscribeToken = generateUnsubscribeToken(email)

    // Generate personalized HTML with unsubscribe link
    const htmlContent = generateEmailHtml(episodes, dateStr, !!imageBase64, unsubscribeToken)

    // Build the request body for this individual email
    const body: Record<string, unknown> = {
      personalizations: [{ to: [{ email }] }],
      from: {
        email: 'agent@teahose.com',
        name: 'The Daily Teahose'
      },
      subject,
      content: [
        {
          type: 'text/html',
          value: htmlContent
        }
      ]
    }

    // If we have an image, attach it as inline attachment
    if (imageBase64) {
      // Extract base64 data from data URL (remove "data:image/png;base64," prefix)
      const base64Data = imageBase64.replace(/^data:image\/\w+;base64,/, '')

      body.attachments = [
        {
          content: base64Data,
          filename: 'header.png',
          type: 'image/png',
          disposition: 'inline',
          content_id: 'header_image'
        }
      ]
    }

    try {
      const response = await fetch(SENDGRID_API_URL, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${sendgridKey}`
        },
        body: JSON.stringify(body)
      })

      if (!response.ok) {
        const errorText = await response.text()
        console.error(`SendGrid error for ${email}:`, response.status, errorText)
        failureCount++
      } else {
        successCount++
      }
    } catch (error) {
      console.error(`Failed to send email to ${email}:`, error)
      failureCount++
    }
  }

  console.log(`Email send complete: ${successCount} succeeded, ${failureCount} failed`)
  return failureCount === 0
}

export async function GET(request: NextRequest) {
  // Verify cron request
  if (!verifyCronRequest(request)) {
    return Response.json({ error: 'Unauthorized' }, { status: 401 })
  }

  console.log('Starting daily email cron job...')

  // Get hours parameter (default 24, can override with ?hours=48 etc.)
  const hoursParam = request.nextUrl.searchParams.get('hours')
  const hours = hoursParam ? parseInt(hoursParam, 10) : 24

  // Get episodes from last N hours
  const episodes = await getEpisodesFromLastNHours(hours)

  if (episodes.length === 0) {
    console.log(`No new episodes in the last ${hours} hours`)
    return Response.json({
      success: true,
      message: 'No new episodes to send',
      episodeCount: 0
    })
  }

  console.log(`Found ${episodes.length} episode(s) from last ${hours} hours`)

  // Get subscribers
  const subscribers = await getSubscribers()

  if (subscribers.length === 0) {
    console.log('No subscribers to send to')
    return Response.json({
      success: true,
      message: 'No subscribers',
      episodeCount: episodes.length,
      subscriberCount: 0
    })
  }

  console.log(`Sending to ${subscribers.length} subscriber(s)`)

  // Test mode: ?test=true sends only to test email
  const testMode = request.nextUrl.searchParams.get('test') === 'true'
  const testEmail = 'altmbr@gmail.com'

  let actualSubscribers: string[]

  if (testMode) {
    actualSubscribers = subscribers.filter(email => email === testEmail)
    if (actualSubscribers.length === 0) {
      console.log(`⚠️  TEST MODE: ${testEmail} not in subscriber list. No emails will be sent.`)
      return Response.json({
        success: true,
        message: `TEST MODE: ${testEmail} not subscribed`,
        episodeCount: episodes.length,
        subscriberCount: 0,
        testMode: true
      })
    }
    console.log(`⚠️  TEST MODE: Only sending to ${testEmail} (filtered ${subscribers.length - 1} other subscribers)`)
  } else {
    actualSubscribers = subscribers
    console.log(`Production mode: sending to all ${subscribers.length} subscribers`)
  }

  // Generate descriptions for each episode
  console.log('Generating episode descriptions...')
  for (const episode of episodes) {
    episode.description = await generateDescription(episode)
  }

  // Generate date string
  const today = new Date()
  const dateStr = today.toLocaleDateString('en-US', {
    month: 'long',
    day: 'numeric',
    year: 'numeric'
  })

  // Generate header image
  console.log('Generating header image...')
  const headerImageBase64 = await generateHeaderImage(episodes, dateStr)

  const subject = `The Daily Teahose - ${dateStr}`

  // Send personalized emails with unique unsubscribe tokens
  const success = await sendEmail(actualSubscribers, subject, episodes, dateStr, headerImageBase64)

  if (success) {
    console.log('Daily email sent successfully!')
    return Response.json({
      success: true,
      message: testMode ? 'Daily email sent (TEST MODE)' : 'Daily email sent',
      episodeCount: episodes.length,
      subscriberCount: actualSubscribers.length,
      ...(testMode && { testMode: true, testEmail })
    })
  } else {
    console.error('Failed to send daily email')
    return Response.json({
      success: false,
      message: testMode ? 'Failed to send email (TEST MODE)' : 'Failed to send email',
      episodeCount: episodes.length,
      subscriberCount: actualSubscribers.length,
      ...(testMode && { testMode: true, testEmail })
    }, { status: 500 })
  }
}
