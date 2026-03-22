import { kv } from '@/lib/kv'
import { extractEmailFromToken } from '@/lib/tokens'
import type { NextRequest } from 'next/server'

const SUBSCRIBER_PREFIX = 'subscriber:'
const SUBSCRIBER_EMAILS_KEY = 'subscriber-emails'

interface SubscriberData {
  subscribed: boolean
  signupDate: string
  unsubscribeDate?: string
}

async function getSubscriber(email: string): Promise<SubscriberData | null> {
  try {
    const data = await kv.hgetall(`${SUBSCRIBER_PREFIX}${email}`)
    return data as SubscriberData | null
  } catch (error) {
    console.error('Failed to fetch subscriber:', error)
    return null
  }
}

async function updateSubscriber(email: string, data: Partial<SubscriberData>): Promise<void> {
  await kv.hset(`${SUBSCRIBER_PREFIX}${email}`, data as Record<string, unknown>)
}

async function getAllSubscriberEmails(): Promise<string[]> {
  try {
    const emails = await kv.lrange(SUBSCRIBER_EMAILS_KEY, 0, -1)
    return emails as string[]
  } catch (error) {
    console.error('Failed to fetch subscriber emails:', error)
    return []
  }
}

// GET: Validate token and return subscriber info
export async function GET(request: NextRequest) {
  try {
    const { searchParams } = new URL(request.url)
    const token = searchParams.get('token')

    if (!token) {
      return Response.json(
        { valid: false, error: 'No token provided' },
        { status: 400 }
      )
    }

    const allEmails = await getAllSubscriberEmails()
    const email = extractEmailFromToken(token, allEmails)

    if (!email) {
      return Response.json(
        { valid: false, error: 'Invalid token' },
        { status: 400 }
      )
    }

    const subscriber = await getSubscriber(email)

    if (!subscriber) {
      return Response.json(
        { valid: false, error: 'Subscriber not found' },
        { status: 404 }
      )
    }

    return Response.json({
      valid: true,
      email,
      alreadyUnsubscribed: !subscriber.subscribed
    })
  } catch (error) {
    console.error('Unsubscribe validation error:', error)
    return Response.json(
      { valid: false, error: 'Failed to validate token' },
      { status: 500 }
    )
  }
}

// POST: Process unsubscribe request
export async function POST(request: NextRequest) {
  try {
    const body = await request.json()
    const { token } = body

    if (!token) {
      return Response.json(
        { success: false, error: 'No token provided' },
        { status: 400 }
      )
    }

    const allEmails = await getAllSubscriberEmails()
    const email = extractEmailFromToken(token, allEmails)

    if (!email) {
      return Response.json(
        { success: false, error: 'Invalid token' },
        { status: 400 }
      )
    }

    const subscriber = await getSubscriber(email)

    if (!subscriber) {
      return Response.json(
        { success: false, error: 'Subscriber not found' },
        { status: 404 }
      )
    }

    await updateSubscriber(email, {
      subscribed: false,
      unsubscribeDate: new Date().toISOString()
    })

    console.log(`Unsubscribed: ${email}`)

    return Response.json({
      success: true,
      email
    })
  } catch (error) {
    console.error('Unsubscribe error:', error)
    return Response.json(
      { success: false, error: 'Failed to process unsubscribe' },
      { status: 500 }
    )
  }
}
