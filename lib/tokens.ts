import { createHmac } from 'crypto'

function getTokenSecret(): string {
  const secret = process.env.UNSUBSCRIBE_SECRET || process.env.CRON_SECRET
  if (!secret) throw new Error('UNSUBSCRIBE_SECRET or CRON_SECRET must be configured')
  return secret
}

export function generateUnsubscribeToken(email: string): string {
  const hmac = createHmac('sha256', getTokenSecret())
  hmac.update(email)
  return hmac.digest('base64url')
}

export function verifyUnsubscribeToken(token: string, email: string): boolean {
  return token === generateUnsubscribeToken(email)
}

export function extractEmailFromToken(token: string, allEmails: string[]): string | null {
  for (const email of allEmails) {
    if (verifyUnsubscribeToken(token, email)) {
      return email
    }
  }
  return null
}
