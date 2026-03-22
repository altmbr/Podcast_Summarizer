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

// Subscriber ref tokens: encode email + HMAC in a single URL-safe string
// Format: base64url(email).hmac_signature
export function generateSubscriberRef(email: string): string {
  const emailB64 = Buffer.from(email).toString('base64url')
  const hmac = createHmac('sha256', getTokenSecret())
  hmac.update(`ref:${email}`)
  const sig = hmac.digest('base64url')
  return `${emailB64}.${sig}`
}

export function verifySubscriberRef(ref: string): string | null {
  const dotIndex = ref.indexOf('.')
  if (dotIndex === -1) return null

  const emailB64 = ref.slice(0, dotIndex)
  const sig = ref.slice(dotIndex + 1)

  let email: string
  try {
    email = Buffer.from(emailB64, 'base64url').toString('utf-8')
  } catch {
    return null
  }

  const hmac = createHmac('sha256', getTokenSecret())
  hmac.update(`ref:${email}`)
  const expectedSig = hmac.digest('base64url')

  if (sig !== expectedSig) return null
  return email
}
