/**
 * Migration Script: Convert newsletter subscriber list to hash-based storage
 *
 * This script:
 * 1. Backs up current subscriber list to a .md file
 * 2. Migrates from Redis list to hash storage with metadata
 * 3. Preserves all existing subscribers as active
 *
 * Run once with: npx tsx scripts/migrate-subscribers.ts
 */

import { kv } from '@vercel/kv'
import { writeFile } from 'fs/promises'
import { join } from 'path'

const OLD_EMAILS_KEY = 'newsletter-emails'
const NEW_EMAILS_KEY = 'subscriber-emails'
const SUBSCRIBER_PREFIX = 'subscriber:'

interface SubscriberData {
  subscribed: boolean
  signupDate: string
}

async function backupToMarkdown(emails: string[]): Promise<string> {
  const date = new Date().toISOString().split('T')[0] // YYYY-MM-DD
  const filename = `subscribers_backup_${date}.md`
  const filepath = join(process.cwd(), filename)

  const content = `# Newsletter Subscriber Backup

**Date:** ${new Date().toISOString()}
**Total Subscribers:** ${emails.length}

## Subscriber List

${emails.map(email => `- ${email}`).join('\n')}

---
*This backup was created before migrating to the new hash-based storage system.*
`

  await writeFile(filepath, content, 'utf-8')
  console.log(`✓ Backup saved to: ${filename}`)
  return filepath
}

async function migrateSubscribers() {
  console.log('Starting subscriber migration...\n')

  // Step 1: Fetch existing subscribers
  console.log('1. Fetching existing subscribers...')
  const emails = await kv.lrange(OLD_EMAILS_KEY, 0, -1) as string[]

  if (!emails || emails.length === 0) {
    console.log('   No subscribers found in old format.')
    console.log('   Nothing to migrate.')
    return
  }

  console.log(`   Found ${emails.length} subscriber(s)`)

  // Step 2: Backup to .md file
  console.log('\n2. Creating backup...')
  await backupToMarkdown(emails)

  // Step 3: Check if migration already done
  console.log('\n3. Checking for existing new-format data...')
  const existingNewEmails = await kv.lrange(NEW_EMAILS_KEY, 0, -1) as string[]

  if (existingNewEmails.length > 0) {
    console.log(`   WARNING: Found ${existingNewEmails.length} subscribers already in new format!`)
    console.log('   Migration may have already been run.')
    console.log('   Aborting to prevent duplicates.')
    console.log('\n   If you want to re-run migration, manually delete:')
    console.log(`   - Key: ${NEW_EMAILS_KEY}`)
    console.log(`   - Keys: ${SUBSCRIBER_PREFIX}*`)
    return
  }

  // Step 4: Migrate to new format
  console.log('\n4. Migrating to new hash-based format...')
  const signupDate = new Date().toISOString()

  for (const email of emails) {
    const subscriberData = {
      subscribed: true,
      signupDate
    }

    // Create hash entry for subscriber
    await kv.hset(`${SUBSCRIBER_PREFIX}${email}`, subscriberData as Record<string, unknown>)

    // Add to new email index list
    await kv.lpush(NEW_EMAILS_KEY, email)

    console.log(`   ✓ Migrated: ${email}`)
  }

  console.log(`\n   Migrated ${emails.length} subscriber(s)`)

  // Step 5: Verify migration
  console.log('\n5. Verifying migration...')
  const newEmails = await kv.lrange(NEW_EMAILS_KEY, 0, -1) as string[]

  if (newEmails.length !== emails.length) {
    console.log(`   ⚠ WARNING: Count mismatch! Old: ${emails.length}, New: ${newEmails.length}`)
  } else {
    console.log(`   ✓ Verified: ${newEmails.length} subscribers in new format`)
  }

  // Step 6: Rename old key (don't delete, just rename for safety)
  console.log('\n6. Archiving old subscriber list...')
  await kv.rename(OLD_EMAILS_KEY, `${OLD_EMAILS_KEY}-archived`)
  console.log(`   ✓ Renamed ${OLD_EMAILS_KEY} to ${OLD_EMAILS_KEY}-archived`)

  console.log('\n✓ Migration complete!')
  console.log('\nNext steps:')
  console.log('1. Verify the backup .md file contains all subscribers')
  console.log('2. Test the new system')
  console.log(`3. If everything works, you can manually delete: ${OLD_EMAILS_KEY}-archived`)
}

// Run migration
migrateSubscribers()
  .then(() => {
    console.log('\nDone!')
    process.exit(0)
  })
  .catch((error) => {
    console.error('\n❌ Migration failed:', error)
    process.exit(1)
  })
