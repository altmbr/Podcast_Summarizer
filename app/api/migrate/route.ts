import { kv } from '@vercel/kv'
import type { NextRequest } from 'next/server'

const OLD_EMAILS_KEY = 'newsletter-emails'
const NEW_EMAILS_KEY = 'subscriber-emails'
const SUBSCRIBER_PREFIX = 'subscriber:'

interface SubscriberData {
  subscribed: boolean
  signupDate: string
}

// One-time migration endpoint - DELETE THIS FILE AFTER RUNNING
export async function GET(request: NextRequest) {
  // Simple password protection
  const { searchParams } = new URL(request.url)
  const password = searchParams.get('password')

  if (password !== 'migrate-now-123') {
    return Response.json({ error: 'Unauthorized' }, { status: 401 })
  }

  try {
    console.log('Starting subscriber migration...')

    // Step 1: Fetch existing subscribers
    console.log('1. Fetching existing subscribers...')
    const emails = await kv.lrange(OLD_EMAILS_KEY, 0, -1) as string[]

    if (!emails || emails.length === 0) {
      return Response.json({
        success: true,
        message: 'No subscribers found in old format. Nothing to migrate.',
        backup: []
      })
    }

    console.log(`   Found ${emails.length} subscriber(s)`)

    // Step 2: Check if migration already done
    console.log('2. Checking for existing new-format data...')
    const existingNewEmails = await kv.lrange(NEW_EMAILS_KEY, 0, -1) as string[]

    if (existingNewEmails.length > 0) {
      return Response.json({
        success: false,
        error: `Migration may have already been run. Found ${existingNewEmails.length} subscribers in new format.`,
        oldCount: emails.length,
        newCount: existingNewEmails.length
      }, { status: 400 })
    }

    // Step 3: Migrate to new format
    console.log('3. Migrating to new hash-based format...')
    const signupDate = new Date().toISOString()

    for (const email of emails) {
      const subscriberData: SubscriberData = {
        subscribed: true,
        signupDate
      }

      // Create hash entry for subscriber
      await kv.hset(`${SUBSCRIBER_PREFIX}${email}`, subscriberData)

      // Add to new email index list
      await kv.lpush(NEW_EMAILS_KEY, email)

      console.log(`   ✓ Migrated: ${email}`)
    }

    console.log(`   Migrated ${emails.length} subscriber(s)`)

    // Step 4: Verify migration
    console.log('4. Verifying migration...')
    const newEmails = await kv.lrange(NEW_EMAILS_KEY, 0, -1) as string[]

    if (newEmails.length !== emails.length) {
      return Response.json({
        success: false,
        error: `Count mismatch! Old: ${emails.length}, New: ${newEmails.length}`,
        oldCount: emails.length,
        newCount: newEmails.length
      }, { status: 500 })
    }

    console.log(`   ✓ Verified: ${newEmails.length} subscribers in new format`)

    // Step 5: Rename old key (don't delete, just rename for safety)
    console.log('5. Archiving old subscriber list...')
    await kv.rename(OLD_EMAILS_KEY, `${OLD_EMAILS_KEY}-archived`)
    console.log(`   ✓ Renamed ${OLD_EMAILS_KEY} to ${OLD_EMAILS_KEY}-archived`)

    return Response.json({
      success: true,
      message: 'Migration complete!',
      migratedCount: emails.length,
      backup: emails,
      note: 'IMPORTANT: Delete this API endpoint (app/api/migrate/route.ts) after confirming migration worked!'
    })
  } catch (error) {
    console.error('Migration error:', error)
    return Response.json({
      success: false,
      error: error instanceof Error ? error.message : 'Unknown error'
    }, { status: 500 })
  }
}
