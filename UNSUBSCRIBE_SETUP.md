# Unsubscribe Feature Setup Guide

This guide explains how to deploy the new unsubscribe feature for the Daily Teahose newsletter.

## What Was Added

1. **Unsubscribe API** (`/api/unsubscribe`)
   - GET: Validates unsubscribe tokens
   - POST: Processes unsubscribe requests

2. **Unsubscribe Page** (`/unsubscribe`)
   - User-friendly confirmation UI
   - Two-step process: view → confirm

3. **Data Schema Migration**
   - Old: Simple list of emails
   - New: Hash storage with metadata (subscribed status, signup date, unsubscribe date)

4. **Personalized Emails**
   - Each email now includes a unique unsubscribe link
   - Emails only sent to active subscribers (subscribed: true)

5. **Resubscribe Support**
   - Users who previously unsubscribed can re-subscribe through the homepage

## Environment Variables

Add to your Vercel project environment variables:

```
UNSUBSCRIBE_SECRET=<generate-a-random-secret-here>
```

Or reuse your existing `CRON_SECRET` (the code falls back to it automatically).

To generate a random secret:
```bash
openssl rand -base64 32
```

## Migration Steps

### 1. Deploy the Code

```bash
git add .
git commit -m "Add unsubscribe feature for newsletter"
git push
```

Vercel will automatically deploy the changes.

### 2. Run the Migration Script

The migration script will:
- Backup current subscribers to `subscribers_backup_YYYY-MM-DD.md`
- Convert from list to hash storage
- Preserve all existing subscribers as active
- Archive the old data (doesn't delete it)

**Run migration:**

```bash
# Install tsx if you don't have it
npm install -g tsx

# Pull environment variables from Vercel
vercel env pull .env.local

# Run the migration
npx tsx scripts/migrate-subscribers.ts
```

**Expected output:**
```
Starting subscriber migration...

1. Fetching existing subscribers...
   Found 25 subscriber(s)

2. Creating backup...
   ✓ Backup saved to: subscribers_backup_2025-01-15.md

3. Checking for existing new-format data...
   No existing data found.

4. Migrating to new hash-based format...
   ✓ Migrated: user1@example.com
   ✓ Migrated: user2@example.com
   ...
   Migrated 25 subscriber(s)

5. Verifying migration...
   ✓ Verified: 25 subscribers in new format

6. Archiving old subscriber list...
   ✓ Renamed newsletter-emails to newsletter-emails-archived

✓ Migration complete!
```

### 3. Verify the Backup

Check the generated `subscribers_backup_YYYY-MM-DD.md` file and make sure it contains all your subscribers.

**Keep this file safe!** It's your backup in case anything goes wrong.

### 4. Test the System

1. **Subscribe a test email:**
   - Go to https://www.teahose.com
   - Enter a test email address
   - Verify it's added to the database

2. **Trigger a test daily email:**
   - Visit: `https://www.teahose.com/api/cron/daily-email`
   - Check that you receive an email with an unsubscribe link

3. **Test unsubscribe flow:**
   - Click the unsubscribe link in the email
   - Should land on `/unsubscribe?token=xxx`
   - Click "Yes, Unsubscribe"
   - Verify success message

4. **Verify unsubscribe worked:**
   - Check Vercel KV dashboard
   - Find `subscriber:your-test@email.com`
   - Should show `subscribed: false`

5. **Test resubscribe:**
   - Go back to https://www.teahose.com
   - Enter the same email you just unsubscribed
   - Should get "Successfully resubscribed to newsletter"

### 5. Clean Up (Optional)

Once you've verified everything works for a few days:

1. Delete the archived key from Vercel KV:
   - Go to Vercel Dashboard → Storage → Your KV Database
   - Search for `newsletter-emails-archived`
   - Delete it

## Data Structure

### Before Migration
```
newsletter-emails: ["email1@example.com", "email2@example.com"]
```

### After Migration
```
subscriber-emails: ["email1@example.com", "email2@example.com"]  // Index for listing
subscriber:email1@example.com: { subscribed: true, signupDate: "2025-01-15T10:00:00Z" }
subscriber:email2@example.com: { subscribed: false, signupDate: "2025-01-10T08:30:00Z", unsubscribeDate: "2025-01-14T12:00:00Z" }
```

## Token Security

- Tokens are generated using HMAC-SHA256
- Secret key is stored in environment variables
- Tokens are deterministic (same email = same token)
- Tokens never expire (CAN-SPAM requirement)
- Cannot be forged without the secret key

## CAN-SPAM Compliance

✅ Unsubscribe link in every email
✅ One-click unsubscribe (no login required)
✅ Processed immediately (no 10-day wait)
✅ Unsubscribe honored permanently
✅ Clear sender identification

## Rollback Instructions

If something goes wrong during migration:

1. **Restore from archived list:**
   ```typescript
   // In Vercel KV dashboard or CLI:
   await kv.rename('newsletter-emails-archived', 'newsletter-emails')
   ```

2. **Or restore from .md backup:**
   - Read `subscribers_backup_YYYY-MM-DD.md`
   - Manually re-add emails to the old `newsletter-emails` list

3. **Revert code changes:**
   ```bash
   git revert HEAD
   git push
   ```

## Troubleshooting

**"Migration already run" warning:**
- The script detected existing new-format data
- This prevents duplicate migrations
- If you want to re-run, manually delete `subscriber-emails` and `subscriber:*` keys first

**Emails not sending after migration:**
- Check that `getSubscribers()` is returning emails
- Verify subscriber hashes have `subscribed: true`
- Check Vercel deployment logs

**Unsubscribe link not working:**
- Verify `UNSUBSCRIBE_SECRET` is set in Vercel environment variables
- Check browser console for errors
- Test token validation: `/api/unsubscribe?token=xxx`

## Support

If you encounter issues:
1. Check the backup .md file
2. Review Vercel deployment logs
3. Check Vercel KV data browser
4. Verify all environment variables are set
