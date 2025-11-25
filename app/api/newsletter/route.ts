import { kv } from '@vercel/kv'
import type { NextRequest } from 'next/server'

const EMAILS_KEY = 'newsletter-emails'

async function getEmails(): Promise<string[]> {
  try {
    const emails = await kv.lrange(EMAILS_KEY, 0, -1)
    return emails as string[]
  } catch (error) {
    console.error('Failed to fetch emails:', error)
    return []
  }
}

async function addEmail(email: string): Promise<void> {
  await kv.lpush(EMAILS_KEY, email)
}

export async function POST(request: NextRequest) {
  try {
    const body = await request.json()
    const { email } = body

    if (!email || typeof email !== 'string') {
      return Response.json(
        { message: 'Invalid email address' },
        { status: 400 }
      )
    }

    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/
    if (!emailRegex.test(email)) {
      return Response.json(
        { message: 'Please enter a valid email address' },
        { status: 400 }
      )
    }

    // Check if email already exists
    const emails = await getEmails()
    if (emails.includes(email)) {
      return Response.json(
        { message: 'This email is already subscribed', alreadySubscribed: true },
        { status: 200 }
      )
    }

    // Add email to KV storage
    await addEmail(email)

    return Response.json(
      { message: 'Successfully subscribed to newsletter' },
      { status: 200 }
    )
  } catch (error) {
    console.error('Newsletter error:', error)
    return Response.json(
      { message: 'Failed to process subscription' },
      { status: 500 }
    )
  }
}
