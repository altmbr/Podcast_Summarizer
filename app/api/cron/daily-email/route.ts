import { kv } from '@/lib/kv'
import { verifyBearerToken } from '@/lib/auth'
import { generateUnsubscribeToken } from '@/lib/tokens'
import type { NextRequest } from 'next/server'
import { readdir, readFile } from 'fs/promises'
import { join } from 'path'
import { contentTypeFromSource } from '@/lib/content-types'
import { parseEpisodeMetadata } from '@/lib/schema'
import { parseEpisodeDate, isWithinLastNHours } from '@/lib/dates'
import { SESv2Client, SendEmailCommand } from '@aws-sdk/client-sesv2'

const SUBSCRIBER_EMAILS_KEY = 'subscriber-emails'
const SUBSCRIBER_PREFIX = 'subscriber:'

const SENT_SLUGS_KEY = 'daily-email:sent-slugs'
const LOG_KEY_PREFIX = 'daily-email:log:'

interface Episode {
  podcast_name: string
  title: string
  slug: string
  date: string
  dateObj: Date
  sortDate: Date
  summary_content: string
  description?: string
  participants?: string
  source?: string
}

interface SubscriberData {
  subscribed: boolean
  signupDate: string
  unsubscribeDate?: string
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

  console.log('Current server time:', new Date().toISOString())

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

          if (!metadata.date) continue

          const episodeDate = parseEpisodeDate(metadata.date)
          if (!episodeDate) {
            console.log(`Failed to parse date for episode "${metadata.title}": ${metadata.date}`)
            continue
          }

          // Use Processed timestamp if available (precise to the second), fall back to Date (day-only)
          const processedDate = metadata.processed ? parseEpisodeDate(metadata.processed) : null
          const sortDate = processedDate || episodeDate

          console.log(`Episode "${metadata.title}": date=${metadata.date}, processed=${metadata.processed || 'N/A'}, checkDate=${sortDate.toISOString()}, includes=${isWithinLastNHours(sortDate, hours)}`)

          if (isWithinLastNHours(sortDate, hours)) {
            episodes.push({
              podcast_name: metadata.podcast || podcastDir.name,
              title: metadata.title || episodeDir.name,
              slug: episodeDir.name,
              date: metadata.date,
              dateObj: episodeDate,
              sortDate,
              summary_content: summaryContent,
              participants: metadata.participants,
              source: metadata.source,
            })
          }
        } catch (e) {
          console.error(`Error reading episode ${episodeDir.name}:`, e)
        }
      }
    }
  } catch (error) {
    console.error('Error reading podcast_work directory:', error)
  }

  console.log(`Found ${episodes.length} episodes from last ${hours} hours`)

  // Sort by most recently processed first (using precise processed timestamp when available)
  episodes.sort((a, b) => b.sortDate.getTime() - a.sortDate.getTime())
  return episodes
}

function extractKeyThemes(summaryContent: string): string {
  const lines = summaryContent.split('\n')
  let inRelevantSection = false
  const extractedContent: string[] = []

  for (const line of lines) {
    if (/^##?\s*(?:1\.|A\.)\s*Key\s+Themes/i.test(line)) {
      inRelevantSection = true
      continue
    }
    if (/^##?\s*(?:2\.|B\.)\s*Contrarian\s+Perspectives?/i.test(line)) {
      inRelevantSection = true
      continue
    }
    if (inRelevantSection) {
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

  const isResearchPaper = episode.source === 'paper'
  const prompt = isResearchPaper
    ? `Write exactly 3 SHORT sentences (max 75 words total) about this research paper for founders and operators:

1. Why it's significant right now (one sentence).
2. What it actually does, in plain language (one sentence).
3. What it means for people building or investing in this space (one sentence).

Be punchy. No jargon. No filler. 75 words max.

Paper: ${episode.title}

Key themes:
${summaryExcerpt}`
    : `Write a pithy, signal-dense summary (max 45 words) of this podcast episode. Cover: main discussion topics, key themes, and any contrarian insights. Be specific and punchy.

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
        model: 'claude-sonnet-4-6',
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

/**
 * Generate an image via Gemini and return a base64 data URL, or null on failure.
 */
async function generateGeminiImage(prompt: string, logLabel: string): Promise<string | null> {
  const googleApiKey = process.env.GOOGLE_API_KEY
  if (!googleApiKey) {
    console.log('GOOGLE_API_KEY not set - skipping header image')
    return null
  }

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
          console.log(`${logLabel} generated successfully`)
          return `data:${mimeType};base64,${data}`
        }
      }
    }

    console.log('No image data in Gemini response')
    return null
  } catch (error) {
    console.error(`Failed to generate ${logLabel}:`, error)
    return null
  }
}

async function generateVisualConcept(episodes: Episode[]): Promise<string> {
  const anthropicKey = process.env.ANTHROPIC_API_KEY
  const fallback = 'A collage of tech industry themes including AI, business strategy, and innovation.'
  if (!anthropicKey) {
    return fallback
  }

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
        model: 'claude-sonnet-4-6',
        max_tokens: 300,
        messages: [{ role: 'user', content: prompt }]
      })
    })

    const data = await response.json()
    return data.content?.[0]?.text?.trim() || fallback
  } catch {
    return fallback
  }
}

async function generateCompositeHeaderImage(episodes: Episode[]): Promise<string | null> {
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

  return generateGeminiImage(prompt, 'Composite header image')
}

function generateEmailHtml(episodes: Episode[], dateStr: string, hasImage: boolean, unsubscribeToken: string): string {
  // Color palette - using full hex codes (no shorthand) for max compatibility
  const colors = {
    background: '#f7f4f0',
    foreground: '#1a1a1a',
    card: '#fffefa',
    muted_foreground: '#555555',
    accent: '#c41e3a',
    border: '#1a1a1a',
  }

  // Header image with CID reference for inline attachment
  const headerImgHtml = hasImage
    ? `<tr>
        <td align="center" style="padding-bottom: 24px;">
          <img src="cid:header_image" width="600" style="width: 100%; max-width: 600px; height: auto; display: block;" alt="Daily Teahose Header">
        </td>
      </tr>`
    : ''

  // Build episode cards using table-based layout
  let episodeCards = ''

  episodes.forEach((episode, index) => {
    const encodedPodcast = encodeURIComponent(episode.podcast_name)
    const encodedSlug = encodeURIComponent(episode.slug)
    const urlPrefix = contentTypeFromSource(episode.source)
    const summaryUrl = `https://www.teahose.com/${urlPrefix}/${encodedPodcast}/${encodedSlug}?ref=email`
    const formattedDate = episode.dateObj.toLocaleDateString('en-US', {
      month: 'long',
      day: 'numeric',
      year: 'numeric',
    })

    // Use <div> instead of <p> inside table cells for Gmail compatibility
    const participantsHtml = episode.participants
      ? `<div style="color: ${colors.foreground}; font-size: 14px; margin: 0 0 8px 0; padding: 0;">${episode.participants}</div>`
      : ''

    const isLast = index === episodes.length - 1
    const paddingBottom = isLast ? '0' : '24px'

    // Each episode card is a table for consistent rendering
    episodeCards += `
      <tr>
        <td style="padding-bottom: ${paddingBottom};">
          <table width="100%" cellpadding="0" cellspacing="0" border="0" bgcolor="${colors.card}" style="background-color: ${colors.card}; border: 3px solid ${colors.border};">
            <tr>
              <td style="padding: 24px 16px;">
                <a href="${summaryUrl}" style="text-decoration: none; color: ${colors.foreground};">
                  <div style="margin: 0 0 6px 0; font-size: 24px; font-weight: 700; letter-spacing: -0.01em; text-transform: uppercase; color: ${colors.foreground};">
                    ${episode.title}
                  </div>
                  <div style="color: ${colors.muted_foreground}; font-size: 13px; text-transform: uppercase; letter-spacing: 0.5px; margin: 0 0 4px 0;">${episode.podcast_name}</div>
                  ${participantsHtml}
                  <div style="color: ${colors.muted_foreground}; font-size: 12px; margin: 0 0 12px 0;">${formattedDate}</div>
                  <div style="color: ${colors.foreground}; font-size: 15px; line-height: 1.75; margin: 0;">
                    ${episode.description || 'New episode available.'}
                  </div>
                </a>
              </td>
            </tr>
          </table>
        </td>
      </tr>`
  })

  // EMAIL HTML BEST PRACTICES (2025):
  // - Tables for ALL layout (email clients use Word rendering, not browser)
  // - 600px max width (fits email preview panes)
  // - 100% inline CSS (Gmail strips <style> tags)
  // - No box-shadow (fails in Outlook, some Gmail configs)
  // - No display: inline-block (breaks on email forward)
  // - Use <div> not <p> inside <td> (Gmail can break <p> out of cells)
  // - Double-declare: bgcolor attribute + background-color style
  // - Use full hex codes (#ffffff not #fff)

  return `<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>The Daily Teahose - ${dateStr}</title>
</head>
<body style="margin: 0; padding: 0; background-color: ${colors.background};" bgcolor="${colors.background}">
    <!-- Outer wrapper table for centering -->
    <table width="100%" cellpadding="0" cellspacing="0" border="0" bgcolor="${colors.background}" style="background-color: ${colors.background};">
      <tr>
        <td align="center" style="padding: 20px;">
          <!-- Main content table (600px width for compatibility) -->
          <table width="600" cellpadding="0" cellspacing="0" border="0" bgcolor="${colors.card}" style="background-color: ${colors.card}; border: 3px solid ${colors.border}; max-width: 600px;">
            <tr>
              <td style="padding: 32px; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif; line-height: 1.6; color: ${colors.foreground};">

                <!-- Header Title -->
                <table width="100%" cellpadding="0" cellspacing="0" border="0">
                  <tr>
                    <td align="center" style="padding-bottom: 20px;">
                      <a href="https://www.teahose.com?ref=email" style="text-decoration: none; color: ${colors.foreground};">
                        <div style="margin: 0; font-size: 28px; font-weight: 900; text-transform: uppercase; color: ${colors.foreground}; letter-spacing: -0.02em;">
                          THE DAILY TEAHOSE
                        </div>
                      </a>
                    </td>
                  </tr>
                </table>

                <!-- Signup CTA Box - table-based for compatibility -->
                <table width="100%" cellpadding="0" cellspacing="0" border="0">
                  <tr>
                    <td align="center" style="padding-bottom: 24px;">
                      <table cellpadding="0" cellspacing="0" border="0" style="border: 2px solid ${colors.border};">
                        <tr>
                          <td style="padding: 12px 16px; font-size: 14px; color: ${colors.foreground};">
                            Forwarded this email? Get daily summaries of top technology and business news.
                          </td>
                          <td style="padding: 12px 16px 12px 8px; white-space: nowrap;">
                            <table cellpadding="0" cellspacing="0" border="0" bgcolor="${colors.foreground}" style="background-color: ${colors.foreground};">
                              <tr>
                                <td style="padding: 8px 16px; white-space: nowrap;">
                                  <a href="https://www.teahose.com?ref=email" style="color: ${colors.card}; text-decoration: none; font-weight: 600; font-size: 14px; white-space: nowrap;">Sign&nbsp;Up</a>
                                </td>
                              </tr>
                            </table>
                          </td>
                        </tr>
                      </table>
                    </td>
                  </tr>
                </table>

                <!-- Divider -->
                <table width="100%" cellpadding="0" cellspacing="0" border="0">
                  <tr>
                    <td style="border-top: 1px solid ${colors.muted_foreground}; padding-bottom: 24px; font-size: 1px; line-height: 1px;">&nbsp;</td>
                  </tr>
                </table>

                <!-- Header Image -->
                <table width="100%" cellpadding="0" cellspacing="0" border="0">
                  ${headerImgHtml}
                </table>

                <!-- Episode Cards -->
                <table width="100%" cellpadding="0" cellspacing="0" border="0">
                  ${episodeCards}
                </table>

                <!-- Footer with Unsubscribe -->
                <table width="100%" cellpadding="0" cellspacing="0" border="0" style="margin-top: 32px;">
                  <tr>
                    <td style="border-top: 1px solid ${colors.muted_foreground}; padding-top: 24px; font-size: 1px; line-height: 1px;">&nbsp;</td>
                  </tr>
                  <tr>
                    <td align="center" style="color: ${colors.muted_foreground}; font-size: 13px; line-height: 1.6; padding-bottom: 12px;">
                      A distillation of insight from the highest signal technology and entrepreneurship podcasts.
                    </td>
                  </tr>
                  <tr>
                    <td align="center" style="color: ${colors.muted_foreground}; font-size: 13px;">
                      <a href="https://www.teahose.com?ref=email" style="color: ${colors.accent}; text-decoration: underline;">Teahose.com</a> &middot; <a href="https://www.teahose.com/unsubscribe?token=${unsubscribeToken}" style="color: ${colors.muted_foreground}; text-decoration: underline;">Unsubscribe</a>
                    </td>
                  </tr>
                </table>

              </td>
            </tr>
          </table>
          <!-- End main content table -->
        </td>
      </tr>
    </table>
    <!-- End outer wrapper -->
</body>
</html>`
}

function buildMimeEmail(from: string, fromName: string, to: string, subject: string, htmlContent: string, imageBase64: string | null): string {
  const relatedBoundary = `----=_Related_${Date.now()}`

  const headers = [
    `From: ${fromName} <${from}>`,
    `To: ${to}`,
    `Subject: ${subject}`,
    'MIME-Version: 1.0',
  ]

  if (imageBase64) {
    headers.push(`Content-Type: multipart/related; boundary="${relatedBoundary}"`)
    const base64Data = imageBase64.replace(/^data:image\/\w+;base64,/, '')
    return headers.join('\r\n') + '\r\n\r\n' +
      `--${relatedBoundary}\r\n` +
      'Content-Type: text/html; charset=UTF-8\r\n' +
      'Content-Transfer-Encoding: 7bit\r\n\r\n' +
      htmlContent + '\r\n' +
      `--${relatedBoundary}\r\n` +
      'Content-Type: image/png\r\n' +
      'Content-Transfer-Encoding: base64\r\n' +
      'Content-ID: <header_image>\r\n' +
      'Content-Disposition: inline; filename="header.png"\r\n\r\n' +
      base64Data + '\r\n' +
      `--${relatedBoundary}--`
  } else {
    headers.push('Content-Type: text/html; charset=UTF-8')
    return headers.join('\r\n') + '\r\n\r\n' + htmlContent
  }
}

async function sendEmail(to: string[], subject: string, episodes: Episode[], dateStr: string, imageBase64: string | null): Promise<boolean> {
  const accessKeyId = process.env.AWS_ACCESS_KEY_ID
  const secretAccessKey = process.env.AWS_SECRET_ACCESS_KEY

  if (!accessKeyId || !secretAccessKey) {
    console.error('AWS credentials not set (AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY)')
    return false
  }

  const sesClient = new SESv2Client({
    region: 'us-west-2',
    credentials: { accessKeyId, secretAccessKey },
  })

  let successCount = 0
  let failureCount = 0

  for (const email of to) {
    const unsubscribeToken = generateUnsubscribeToken(email)
    const htmlContent = generateEmailHtml(episodes, dateStr, !!imageBase64, unsubscribeToken)

    try {
      if (imageBase64) {
        // Use raw MIME for inline image attachments
        const rawMessage = buildMimeEmail('agent@teahose.com', 'The Daily Teahose', email, subject, htmlContent, imageBase64)
        const command = new SendEmailCommand({
          Content: {
            Raw: {
              Data: new TextEncoder().encode(rawMessage),
            },
          },
        })
        await sesClient.send(command)
      } else {
        // Simple email without attachments
        const command = new SendEmailCommand({
          FromEmailAddress: 'The Daily Teahose <agent@teahose.com>',
          Destination: { ToAddresses: [email] },
          Content: {
            Simple: {
              Subject: { Data: subject },
              Body: { Html: { Data: htmlContent } },
            },
          },
        })
        await sesClient.send(command)
      }
      successCount++
    } catch (error) {
      console.error(`SES error for ${email}:`, error)
      failureCount++
    }
  }

  console.log(`Email send complete: ${successCount} succeeded, ${failureCount} failed`)
  return failureCount === 0
}

export async function GET(request: NextRequest) {
  // Verify cron request
  if (!verifyBearerToken(request)) {
    return Response.json({ error: 'Unauthorized' }, { status: 401 })
  }

  console.log('Starting daily email cron job...')

  // Get hours parameter (default 48, can override with ?hours=24 etc.)
  const hoursParam = request.nextUrl.searchParams.get('hours')
  const hours = hoursParam ? parseInt(hoursParam, 10) : 48

  // Get episodes from last N hours
  const allEpisodes = await getEpisodesFromLastNHours(hours)

  // Dedup: exclude episodes already sent in a previous daily email
  let previousSlugs: string[] = []
  try {
    const raw = await kv.get(SENT_SLUGS_KEY) as string[] | null
    previousSlugs = raw || []
    if (previousSlugs.length > 0) {
      console.log(`Dedup: ${previousSlugs.length} slugs from previous sends: ${previousSlugs.join(', ')}`)
    }
  } catch (e) {
    console.error('Failed to read previous sent slugs from KV:', e)
  }

  const excludedSlugs = allEpisodes.filter(ep => previousSlugs.includes(ep.slug)).map(ep => ep.slug)
  const episodes = allEpisodes.filter(ep => !previousSlugs.includes(ep.slug))

  if (excludedSlugs.length > 0) {
    console.log(`Dedup: excluded ${excludedSlugs.length} already-sent episode(s): ${excludedSlugs.join(', ')}`)
  }

  if (episodes.length === 0) {
    console.log(`No new episodes in the last ${hours} hours (${allEpisodes.length} in window, all already sent)`)
    return Response.json({
      success: true,
      message: 'No new episodes to send',
      episodeCount: 0,
      excludedCount: excludedSlugs.length,
    })
  }

  console.log(`Found ${episodes.length} new episode(s) from last ${hours} hours (${excludedSlugs.length} excluded as duplicates)`)

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
  const headerImageBase64 = await generateCompositeHeaderImage(episodes)

  const subject = `The Daily Teahose - ${dateStr}`

  // Send personalized emails with unique unsubscribe tokens
  const success = await sendEmail(actualSubscribers, subject, episodes, dateStr, headerImageBase64)

  // Build audit log entry
  const logEntry = {
    sentAt: new Date().toISOString(),
    success,
    episodeCount: episodes.length,
    subscriberCount: actualSubscribers.length,
    testMode,
    episodes: episodes.map(ep => ({
      title: ep.title,
      slug: ep.slug,
      podcast: ep.podcast_name,
      date: ep.date,
    })),
    excludedSlugs,
    windowHours: hours,
    totalInWindow: allEpisodes.length,
  }

  // Write audit log (30-day TTL) — always, regardless of success/failure
  try {
    const logKey = `${LOG_KEY_PREFIX}${new Date().toISOString().split('T')[0]}`
    await kv.set(logKey, JSON.stringify(logEntry), { ex: 30 * 24 * 60 * 60 })
    console.log(`Audit log written to ${logKey}`)
  } catch (e) {
    console.error('Failed to write audit log:', e)
  }

  if (success) {
    // Track sent slugs for dedup (union of previous + current, 72h TTL)
    // Only update dedup cache for production sends — test sends should not pollute it
    if (!testMode) {
      try {
        const allSentSlugs = [...new Set([...previousSlugs, ...episodes.map(ep => ep.slug)])]
        await kv.set(SENT_SLUGS_KEY, allSentSlugs, { ex: 72 * 60 * 60 })
        console.log(`Stored ${allSentSlugs.length} sent slugs in KV for dedup`)
      } catch (e) {
        console.error('Failed to store sent slugs in KV:', e)
      }
    } else {
      console.log('Test mode: skipping dedup cache update')
    }

    console.log('Daily email sent successfully!')
    return Response.json({
      success: true,
      message: testMode ? 'Daily email sent (TEST MODE)' : 'Daily email sent',
      episodeCount: episodes.length,
      subscriberCount: actualSubscribers.length,
      excludedCount: excludedSlugs.length,
      ...(testMode && { testMode: true, testEmail })
    })
  }

  console.error('Failed to send daily email')
  return Response.json({
    success: false,
    message: testMode ? 'Failed to send email (TEST MODE)' : 'Failed to send email',
    episodeCount: episodes.length,
    subscriberCount: actualSubscribers.length,
    ...(testMode && { testMode: true, testEmail })
  }, { status: 500 })
}
