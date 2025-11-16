# Vercel KV Setup for Newsletter Subscriptions

The newsletter subscription feature uses **Vercel KV** (Redis-compatible key-value storage) to store email addresses privately and securely.

## Setup Steps

### 1. Create Vercel KV Database

1. Go to your [Vercel Dashboard](https://vercel.com/dashboard)
2. Select your project (teahose)
3. Go to the **Storage** tab
4. Click **Create Database**
5. Select **KV** (Key-Value Store)
6. Give it a name (e.g., "newsletter-emails")
7. Click **Create**

### 2. Connect to Your Project

1. After creating the database, click **Connect to Project**
2. Select your project from the dropdown
3. Choose the environment(s): **Production**, **Preview**, and **Development**
4. Click **Connect**

Vercel will automatically inject the required environment variables (`KV_REST_API_URL`, `KV_REST_API_TOKEN`, etc.) into your deployments.

### 3. Set Up Local Development (Optional)

To test the newsletter feature locally:

1. Install Vercel CLI if you haven't:
   ```bash
   npm i -g vercel
   ```

2. Link your local project to Vercel:
   ```bash
   vercel link
   ```

3. Pull environment variables:
   ```bash
   vercel env pull .env.local
   ```

This creates a `.env.local` file with your KV credentials for local development.

### 4. Deploy

Once KV is set up and connected, deploy your changes:

```bash
git add .
git commit -m "Update newsletter to use Vercel KV"
git push
```

Vercel will automatically deploy with the KV connection configured.

## How It Works

- Emails are stored in a Redis list at key `newsletter-emails`
- Each subscription adds the email using `LPUSH`
- Duplicate emails are prevented by checking the existing list
- Data is private and only accessible through your Vercel project
- No data is stored in GitHub or local files

## Accessing Subscriber Emails

### Via Vercel Dashboard

1. Go to **Storage** > Your KV database
2. Click **Data Browser**
3. Search for key: `newsletter-emails`
4. View all subscribed emails

### Via CLI (Advanced)

You can also query the database using the Vercel CLI or Redis CLI with your KV credentials.

## Cost

Vercel KV has a generous free tier:
- **100K requests per month**
- **256 MB storage**
- **1 GB bandwidth**

For a newsletter email list, this should be more than sufficient. Each subscription is just 2 requests (1 read to check duplicates, 1 write to add).

## Troubleshooting

**"Failed to process subscription" error:**
- Check that KV is connected to your project in Vercel dashboard
- Ensure environment variables are set (check Vercel project settings > Environment Variables)
- Redeploy after connecting KV

**Local testing not working:**
- Make sure you've run `vercel env pull .env.local`
- Check that `.env.local` contains `KV_REST_API_URL` and `KV_REST_API_TOKEN`
- Restart your dev server after pulling env vars

**Emails not being saved:**
- Check Vercel deployment logs for errors
- Verify KV connection in Storage tab
- Test the API endpoint directly: `curl -X POST https://teahose.com/api/newsletter -H "Content-Type: application/json" -d '{"email":"test@example.com"}'`
