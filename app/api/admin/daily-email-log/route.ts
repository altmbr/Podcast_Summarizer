import { kv } from '@/lib/kv'
import { verifyBearerToken } from '@/lib/auth'
import type { NextRequest } from 'next/server'

interface LogEpisode {
  title: string
  slug: string
  podcast: string
  date: string
}

interface LogEntry {
  sentAt: string
  success: boolean
  episodeCount: number
  subscriberCount: number
  testMode: boolean
  episodes: LogEpisode[]
  excludedSlugs: string[]
  windowHours: number
  totalInWindow: number
}

/**
 * GET /api/admin/daily-email-log?days=7
 *
 * Returns daily email send history with duplicate detection.
 * Use this to audit what was sent and verify no duplicates.
 */
export async function GET(request: NextRequest) {
  if (!verifyBearerToken(request)) {
    return Response.json({ error: 'Unauthorized' }, { status: 401 })
  }

  const days = parseInt(request.nextUrl.searchParams.get('days') || '7')

  const logs: Array<{ date: string } & LogEntry> = []
  const now = new Date()

  for (let i = 0; i < days; i++) {
    const date = new Date(now)
    date.setDate(date.getDate() - i)
    const dateStr = date.toISOString().split('T')[0]
    const logKey = `daily-email:log:${dateStr}`

    try {
      const raw = await kv.get(logKey) as string | null
      if (raw) {
        const entry = typeof raw === 'string' ? JSON.parse(raw) : raw
        logs.push({ date: dateStr, ...entry })
      }
    } catch {
      // Skip entries that can't be read
    }
  }

  // Detect duplicates across consecutive days
  const duplicates: Array<{
    dates: [string, string]
    overlappingSlugs: string[]
  }> = []

  for (let i = 0; i < logs.length - 1; i++) {
    const today = logs[i]
    const yesterday = logs[i + 1]
    if (today.episodes && yesterday.episodes) {
      const todaySlugs = new Set(today.episodes.map(ep => ep.slug))
      const yesterdaySlugs = new Set(yesterday.episodes.map(ep => ep.slug))
      const overlap = [...todaySlugs].filter(s => yesterdaySlugs.has(s))
      if (overlap.length > 0) {
        duplicates.push({
          dates: [today.date, yesterday.date],
          overlappingSlugs: overlap,
        })
      }
    }
  }

  // Get current dedup state
  let currentSentSlugs: string[] = []
  try {
    const raw = await kv.get('daily-email:sent-slugs') as string[] | null
    currentSentSlugs = raw || []
  } catch {
    // ignore
  }

  return Response.json({
    logs,
    duplicates,
    currentSentSlugs,
    summary: {
      totalDays: logs.length,
      totalEpisodesSent: logs.reduce((sum, l) => sum + (l.episodeCount || 0), 0),
      duplicateIncidents: duplicates.length,
    },
  })
}
