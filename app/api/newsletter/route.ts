import { kv } from '@vercel/kv'
import type { NextRequest } from 'next/server'

const SUBSCRIBER_EMAILS_KEY = 'subscriber-emails'
const SUBSCRIBER_PREFIX = 'subscriber:'

interface SubscriberData {
  subscribed: boolean
  signupDate: string
  unsubscribeDate?: string
}

async function getEmails(): Promise<string[]> {
  try {
    const emails = await kv.lrange(SUBSCRIBER_EMAILS_KEY, 0, -1)
    return emails as string[]
  } catch (error) {
    console.error('Failed to fetch emails:', error)
    return []
  }
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

async function addEmail(email: string): Promise<void> {
  // Add to subscriber hash with metadata
  const subscriberData: SubscriberData = {
    subscribed: true,
    signupDate: new Date().toISOString()
  }
  await kv.hset(`${SUBSCRIBER_PREFIX}${email}`, subscriberData)

  // Add to email index list
  await kv.lpush(SUBSCRIBER_EMAILS_KEY, email)
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
    const subscriber = await getSubscriber(email)

    if (subscriber) {
      // If already subscribed (active)
      if (subscriber.subscribed) {
        return Response.json(
          { message: 'This email is already subscribed', alreadySubscribed: true },
          { status: 200 }
        )
      }

      // If previously unsubscribed, resubscribe them
      await kv.hset(`${SUBSCRIBER_PREFIX}${email}`, {
        subscribed: true,
        signupDate: subscriber.signupDate, // Keep original signup date
        unsubscribeDate: undefined // Clear unsubscribe date
      })

      return Response.json(
        { message: 'Successfully resubscribed to newsletter' },
        { status: 200 }
      )
    }

    // Add new subscriber to KV storage
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
