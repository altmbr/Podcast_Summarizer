import type { NextRequest } from 'next/server'

/**
 * Verify Bearer token against CRON_SECRET.
 * Returns false (deny) if CRON_SECRET is not configured.
 */
export function verifyBearerToken(request: NextRequest): boolean {
  const secret = process.env.CRON_SECRET
  if (!secret) return false
  return request.headers.get('authorization') === `Bearer ${secret}`
}
