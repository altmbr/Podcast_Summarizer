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
  const cutoffDate = new Date()
  cutoffDate.setDate(cutoffDate.getDate() - 1)

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
            const episodeDate = new Date(metadata.date)

            // Only include episodes from last 24 hours
            if (episodeDate >= cutoffDate) {
              episodes.push({
                podcast_name: metadata.podcast || podcastDir.name,
                title: metadata.title || episodeDir.name,
                slug: episodeDir.name,
                date: metadata.date,
                summary_content: summaryContent
              })
            }
          }
        } catch {
          // Skip episodes that can't be read
        }
      }
    }
  } catch (error) {
    console.error('Error reading podcast_work directory:', error)
  }

  // Sort by date, newest first
  episodes.sort((a, b) => new Date(b.date).getTime() - new Date(a.date).getTime())
  return episodes
}

function extractKeyThemes(summaryContent: string): string {
  // Find Key Themes section and extract content until next heading
  const lines = summaryContent.split('\n')
  let inThemes = false
  let themesContent: string[] = []

  for (const line of lines) {
    if (/^##?\s*(?:1\.|A\.)\s*Key\s+Themes/i.test(line)) {
      inThemes = true
      continue
    }
    if (inThemes) {
      // Stop at next major heading
      if (/^##\s*\d|^##\s*[A-Z]/.test(line)) {
        break
      }
      themesContent.push(line)
    }
  }

  if (themesContent.length > 0) {
    return themesContent.join('\n').trim().slice(0, 2000)
  }
  return summaryContent.slice(0, 2000)
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

  const prompt = `Write ONE pithy sentence (max 15 words) capturing the most interesting insight from this podcast episode. Be specific, punchy, intriguing.

Episode: ${episode.title}

Key themes:
${summaryExcerpt}

One sentence:`

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
        max_tokens: 100,
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
    layout = '2 panels side by side'
    panelDesc = `Panel 1: "${topics[0]}"\nPanel 2: "${topics[1]}"`
  } else if (numTopics === 3) {
    layout = '3 panels (1 large on left, 2 stacked on right)'
    panelDesc = topics.map((t, i) => `Panel ${i + 1}: "${t}"`).join('\n')
  } else if (numTopics === 4) {
    layout = '4 panels in a 2x2 grid'
    panelDesc = topics.map((t, i) => `Panel ${i + 1}: "${t}"`).join('\n')
  } else if (numTopics === 5) {
    layout = '5 panels: 2 on top, 3 on bottom'
    panelDesc = topics.map((t, i) => `Panel ${i + 1}: "${t}"`).join('\n')
  } else {
    layout = '6 panels in a 3x2 grid'
    panelDesc = topics.map((t, i) => `Panel ${i + 1}: "${t}"`).join('\n')
  }

  const prompt = `Create a vintage 1950s newspaper-style comic header for a daily podcast digest.

LAYOUT: ${layout} in LANDSCAPE format.

STYLE: Vintage Roy Lichtenstein pop art with Ben Day dots, bold primary colors, thick black outlines.

PANEL CONTENT:
${panelDesc}

FOOTER BANNER: Bold text saying "THE DAILY TEAHOSE - ${dateStr}" at the bottom

REQUIREMENTS:
- All ${numTopics} panels clearly visible
- All text legible and bold
- Landscape orientation
- Vintage newspaper comic aesthetic`

  try {
    // Dynamic import for google-genai
    const { GoogleGenerativeAI } = await import('@google/generative-ai')
    const genAI = new GoogleGenerativeAI(googleApiKey)

    const model = genAI.getGenerativeModel({ model: 'gemini-2.0-flash-exp' })
    const result = await model.generateContent(prompt)

    const response = result.response
    for (const part of response.candidates?.[0]?.content?.parts || []) {
      if (part.inlineData) {
        // Return base64 data URL
        return `data:${part.inlineData.mimeType};base64,${part.inlineData.data}`
      }
    }

    console.log('No image data in Gemini response')
    return null
  } catch (error) {
    console.error('Failed to generate header image:', error)
    return null
  }
}

function generateEmailHtml(episodes: Episode[], dateStr: string, headerImageDataUrl: string | null): string {
  const colors = {
    background: '#f8f7f5',
    foreground: '#2c2c2c',
    card: '#fdfcfb',
    muted_foreground: '#5a5a5a',
    accent: '#5b7f9e',
    border: '#e8e6e1',
  }

  const headerImgHtml = headerImageDataUrl
    ? `<img src="${headerImageDataUrl}" style="width: 100%; max-width: 800px; height: auto; margin-bottom: 30px;" alt="Daily Teahose Header">`
    : ''

  let episodeCards = ''

  for (const episode of episodes) {
    const encodedPodcast = encodeURIComponent(episode.podcast_name)
    const encodedSlug = encodeURIComponent(episode.slug)
    const summaryUrl = `https://teahose.com/podcast/${encodedPodcast}/${encodedSlug}`
    const formattedDate = new Date(episode.date).toLocaleDateString('en-US', {
      month: 'long',
      day: 'numeric',
      year: 'numeric'
    })

    episodeCards += `
        <div style="background: ${colors.card}; padding: 24px 32px; margin-bottom: 24px; border-radius: 2px; border: 1px solid ${colors.border};">
            <div style="margin-bottom: 8px;">
                <span style="color: ${colors.muted_foreground}; font-size: 14px;">${formattedDate}</span>
            </div>
            <h2 style="margin: 0 0 8px 0; font-size: 24px; font-weight: 600; letter-spacing: -0.02em;">
                <a href="${summaryUrl}" style="color: ${colors.foreground}; text-decoration: none;">${episode.title}</a>
            </h2>
            <p style="color: ${colors.muted_foreground}; font-size: 12px; text-transform: uppercase; letter-spacing: 0.5px; margin: 0 0 12px 0;">${episode.podcast_name}</p>
            <p style="color: ${colors.foreground}; font-size: 15px; line-height: 1.75; margin: 0;">
                ${episode.description || 'New episode available.'}
            </p>
        </div>`
  }

  return `<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>The Daily Teahose - ${dateStr}</title>
</head>
<body style="font-family: 'Geist', -apple-system, BlinkMacSystemFont, system-ui, sans-serif; line-height: 1.6; color: ${colors.foreground}; max-width: 896px; margin: 0 auto; padding: 20px; background-color: ${colors.background};">

    <div style="background: ${colors.card}; padding: 40px; border-radius: 4px;">

        ${headerImgHtml}

        <p style="color: ${colors.muted_foreground}; font-size: 14px; margin-bottom: 32px;">
            <strong>${episodes.length}</strong> new episode${episodes.length !== 1 ? 's' : ''} published today
        </p>

        ${episodeCards}
    </div>

    <div style="text-align: center; margin-top: 32px; padding-top: 24px; border-top: 1px solid ${colors.border}; color: ${colors.muted_foreground}; font-size: 14px;">
        <p style="margin: 0 0 8px 0;">Discover the insights within each episode.</p>
        <p style="margin: 0;"><a href="https://teahose.com" style="color: ${colors.accent}; text-decoration: underline;">teahose.com</a></p>
    </div>

</body>
</html>`
}

async function sendEmail(to: string[], subject: string, htmlContent: string): Promise<boolean> {
  const sendgridKey = process.env.SENDGRID_API_KEY

  if (!sendgridKey) {
    console.error('SENDGRID_API_KEY not set')
    return false
  }

  // SendGrid supports up to 1000 recipients per request
  const personalizations = to.map(email => ({ to: [{ email }] }))

  try {
    const response = await fetch(SENDGRID_API_URL, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${sendgridKey}`
      },
      body: JSON.stringify({
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
      })
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
  const headerImageDataUrl = await generateHeaderImage(episodes, dateStr)

  // Generate email HTML
  const htmlContent = generateEmailHtml(episodes, dateStr, headerImageDataUrl)
  const subject = `The Daily Teahose - ${dateStr}`

  // Send email
  const success = await sendEmail(subscribers, subject, htmlContent)

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
