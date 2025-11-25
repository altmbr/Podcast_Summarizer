import { kv } from '@vercel/kv'
import type { NextRequest } from 'next/server'
import { readdir, readFile } from 'fs/promises'
import { join } from 'path'
import { parseEpisodeMetadata } from '@/lib/schema'

const EMAILS_KEY = 'newsletter-emails'
const SENDGRID_API_URL = 'https://api.sendgrid.com/v3/mail/send'

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

async function getSubscribers(): Promise<string[]> {
  try {
    const emails = await kv.lrange(EMAILS_KEY, 0, -1)
    return emails as string[]
  } catch (error) {
    console.error('Failed to fetch subscribers:', error)
    return []
  }
}

async function getEpisodesFromLast24Hours(): Promise<Episode[]> {
  const podcastWorkDir = join(process.cwd(), 'podcast_work')
  const now = new Date()
  const cutoffDate = new Date(now)
  cutoffDate.setHours(cutoffDate.getHours() - 24)

  console.log('Current server time:', now.toISOString())
  console.log('Cutoff date (24h ago):', cutoffDate.toISOString())

  const episodes: Episode[] = []

  try {
    const podcastDirs = await readdir(podcastWorkDir, { withFileTypes: true })

    for (const podcastDir of podcastDirs) {
      if (!podcastDir.isDirectory() || podcastDir.name === 'one off episodes') continue

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

async function generateHeaderImage(episodes: Episode[], dateStr: string): Promise<string | null> {
  const googleApiKey = process.env.GOOGLE_API_KEY
  if (!googleApiKey) {
    console.log('GOOGLE_API_KEY not set - skipping header image')
    return null
  }

  // Extract topics from episode titles
  const topics: string[] = []
  for (const ep of episodes.slice(0, 6)) {
    let title = ep.title
    title = title.replace(/^.*?:\s*/, '')
    title = title.split(/\s*[\|\-]\s*/)[0]
    if (title.length > 50) {
      title = title.slice(0, 47) + '...'
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

FOOTER BANNER: Bold text saying "THE DAILY TEAHOSE - ${dateStr}" at the bottom

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

function generateEmailHtml(episodes: Episode[], dateStr: string, hasImage: boolean): string {
  const colors = {
    background: '#f8f7f5',
    foreground: '#2c2c2c',
    card: '#fdfcfb',
    muted_foreground: '#5a5a5a',
    accent: '#5b7f9e',
    border: '#e8e6e1',
  }

  // Use CID reference for inline image attachment
  const headerImgHtml = hasImage
    ? `<img src="cid:header_image" style="width: 100%; max-width: 800px; height: auto; margin: 0 0 32px 0;" alt="Daily Teahose Header">`
    : ''

  let episodeCards = ''

  episodes.forEach((episode, index) => {
    const encodedPodcast = encodeURIComponent(episode.podcast_name)
    const encodedSlug = encodeURIComponent(episode.slug)
    const summaryUrl = `https://teahose.com/podcast/${encodedPodcast}/${encodedSlug}`
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
        <div style="background: ${colors.card}; padding: 24px 16px; margin-bottom: ${marginBottom}; border-radius: 2px; border: 1px solid ${colors.border};">
            <h2 style="margin: 0 0 6px 0; font-size: 24px; font-weight: 600; letter-spacing: -0.02em;">
                <a href="${summaryUrl}" style="color: ${colors.foreground}; text-decoration: none;">${episode.title}</a>
            </h2>
            <p style="color: ${colors.muted_foreground}; font-size: 13px; text-transform: uppercase; letter-spacing: 0.5px; margin: 0 0 4px 0;">${episode.podcast_name}</p>
            ${participantsHtml}
            <p style="color: ${colors.muted_foreground}; font-size: 12px; margin: 0 0 12px 0;">${formattedDate}</p>
            <p style="color: ${colors.foreground}; font-size: 15px; line-height: 1.75; margin: 0;">
                ${episode.description || 'New episode available.'}
            </p>
        </div>`
  })

  return `<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>The Daily Teahose - ${dateStr}</title>
</head>
<body style="font-family: 'Geist', -apple-system, BlinkMacSystemFont, system-ui, sans-serif; line-height: 1.6; color: ${colors.foreground}; max-width: 896px; margin: 0 auto; padding: 10px; background-color: ${colors.background};">

    <div style="background: ${colors.card}; padding: 32px 20px; border-radius: 4px;">

        ${headerImgHtml}

        ${episodeCards}
    </div>

    <div style="text-align: center; padding: 32px 20px; color: ${colors.muted_foreground}; font-size: 14px;">
        <p style="margin: 0;">
            A distillation of insight from the highest signal technology and entrepreneurship podcasts.<br>
            <a href="https://teahose.com" style="color: ${colors.accent}; text-decoration: underline; margin-top: 16px; display: inline-block;">Teahose.com</a>
        </p>
    </div>

</body>
</html>`
}

async function sendEmail(to: string[], subject: string, htmlContent: string, imageBase64: string | null): Promise<boolean> {
  const sendgridKey = process.env.SENDGRID_API_KEY

  if (!sendgridKey) {
    console.error('SENDGRID_API_KEY not set')
    return false
  }

  // SendGrid supports up to 1000 recipients per request
  const personalizations = to.map(email => ({ to: [{ email }] }))

  // Build the request body
  const body: Record<string, unknown> = {
    personalizations,
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
      console.error('SendGrid error:', response.status, errorText)
      return false
    }

    return true
  } catch (error) {
    console.error('Failed to send email:', error)
    return false
  }
}

export async function GET(request: NextRequest) {
  // Verify cron request
  if (!verifyCronRequest(request)) {
    return Response.json({ error: 'Unauthorized' }, { status: 401 })
  }

  console.log('Starting daily email cron job...')

  // Get episodes from last 24 hours
  const episodes = await getEpisodesFromLast24Hours()

  if (episodes.length === 0) {
    console.log('No new episodes in the last 24 hours')
    return Response.json({
      success: true,
      message: 'No new episodes to send',
      episodeCount: 0
    })
  }

  console.log(`Found ${episodes.length} episode(s) from last 24 hours`)

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

  // Generate email HTML (pass boolean for whether image exists)
  const htmlContent = generateEmailHtml(episodes, dateStr, !!headerImageBase64)
  const subject = `The Daily Teahose - ${dateStr}`

  // Send email with image attachment
  const success = await sendEmail(subscribers, subject, htmlContent, headerImageBase64)

  if (success) {
    console.log('Daily email sent successfully!')
    return Response.json({
      success: true,
      message: 'Daily email sent',
      episodeCount: episodes.length,
      subscriberCount: subscribers.length
    })
  } else {
    console.error('Failed to send daily email')
    return Response.json({
      success: false,
      message: 'Failed to send email',
      episodeCount: episodes.length,
      subscriberCount: subscribers.length
    }, { status: 500 })
  }
}
