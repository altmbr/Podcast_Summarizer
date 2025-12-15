/**
 * Robust date parsing utilities for episode dates
 * Handles multiple date formats from summary.md files
 */

/**
 * Parse episode date from various formats
 * Supports:
 * - ISO format: "2025-12-12"
 * - Human-readable: "December 12, 2025"
 * - Legacy formats
 *
 * @param dateStr - Date string from episode metadata
 * @returns Date object or null if unparseable
 */
export function parseEpisodeDate(dateStr: string | undefined): Date | null {
  if (!dateStr) return null

  const trimmed = dateStr.trim()

  // Try ISO format first: "2025-12-12" or "2025-12-12T..."
  // This is the preferred format going forward
  if (/^\d{4}-\d{2}-\d{2}/.test(trimmed)) {
    const date = new Date(trimmed)
    if (!isNaN(date.getTime())) {
      return date
    }
  }

  // Try human-readable format: "December 12, 2025" or "Month DD, YYYY"
  // This handles legacy episodes
  const humanReadableMatch = trimmed.match(/^([A-Za-z]+)\s+(\d{1,2}),?\s+(\d{4})$/)
  if (humanReadableMatch) {
    const [, month, day, year] = humanReadableMatch
    const monthMap: Record<string, number> = {
      'january': 0, 'february': 1, 'march': 2, 'april': 3,
      'may': 4, 'june': 5, 'july': 6, 'august': 7,
      'september': 8, 'october': 9, 'november': 10, 'december': 11
    }
    const monthIndex = monthMap[month.toLowerCase()]
    if (monthIndex !== undefined) {
      const date = new Date(parseInt(year), monthIndex, parseInt(day))
      if (!isNaN(date.getTime())) {
        return date
      }
    }
  }

  // Fallback: try JavaScript's native Date constructor
  // This handles other formats like "12/12/2025" etc.
  try {
    const date = new Date(trimmed)
    if (!isNaN(date.getTime())) {
      return date
    }
  } catch {
    // Ignore
  }

  // Unable to parse
  console.warn(`Unable to parse date: "${dateStr}"`)
  return null
}

/**
 * Format a date for display
 * @param date - Date object
 * @returns Formatted string like "December 12, 2025"
 */
export function formatDateForDisplay(date: Date): string {
  return date.toLocaleDateString('en-US', {
    month: 'long',
    day: 'numeric',
    year: 'numeric'
  })
}

/**
 * Format a date to ISO format
 * @param date - Date object
 * @returns ISO format string like "2025-12-12"
 */
export function formatDateISO(date: Date): string {
  return date.toISOString().split('T')[0]
}

/**
 * Check if a date is within the last N hours
 * @param date - Date to check
 * @param hours - Number of hours
 * @returns true if date is within the last N hours
 */
export function isWithinLastNHours(date: Date, hours: number): boolean {
  const now = new Date()
  const cutoff = new Date(now)
  cutoff.setHours(cutoff.getHours() - hours)
  return date >= cutoff
}
