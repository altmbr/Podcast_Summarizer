import { kv } from '@vercel/kv'
import type { NextRequest } from 'next/server'

const SUBSCRIBER_EMAILS_KEY = 'subscriber-emails'
const SUBSCRIBER_PREFIX = 'subscriber:'

interface SubscriberData {
  subscribed: boolean
  signupDate: string
  unsubscribeDate?: string
}

export async function GET(request: NextRequest) {
  try {
    // Get all email addresses
    const allEmails = await kv.lrange(SUBSCRIBER_EMAILS_KEY, 0, -1) as string[]

    if (!allEmails || allEmails.length === 0) {
      return Response.json({
        success: true,
        activeSubscribers: [],
        inactiveSubscribers: [],
        totalActive: 0,
        totalInactive: 0
      })
    }

    const activeSubscribers: any[] = []
    const inactiveSubscribers: any[] = []

    // Check subscription status for each email
    for (const email of allEmails) {
      const data = await kv.hgetall(`${SUBSCRIBER_PREFIX}${email}`) as SubscriberData | null

      if (data && data.subscribed) {
        activeSubscribers.push({
          email,
          signupDate: data.signupDate,
          subscribed: true
        })
      } else if (data) {
        inactiveSubscribers.push({
          email,
          signupDate: data.signupDate,
          unsubscribeDate: data.unsubscribeDate,
          subscribed: false
        })
      }
    }

    return Response.json({
      success: true,
      activeSubscribers,
      inactiveSubscribers,
      totalActive: activeSubscribers.length,
      totalInactive: inactiveSubscribers.length
    })

  } catch (error) {
    console.error('Error fetching subscribers:', error)
    return Response.json({
      success: false,
      error: 'Failed to fetch subscribers'
    }, { status: 500 })
  }
}
