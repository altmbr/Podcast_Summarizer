import { promises as fs } from 'fs'
import { join } from 'path'
import type { NextRequest } from 'next/server'

const DATA_DIR = join(process.cwd(), 'data')
const EMAILS_FILE = join(DATA_DIR, 'newsletter-emails.json')

async function ensureDataDir() {
  try {
    await fs.mkdir(DATA_DIR, { recursive: true })
  } catch (error) {
    console.error('[v0] Failed to create data directory:', error)
  }
}

async function loadEmails(): Promise<string[]> {
  try {
    const content = await fs.readFile(EMAILS_FILE, 'utf-8')
    return JSON.parse(content)
  } catch (error) {
    return []
  }
}

async function saveEmails(emails: string[]): Promise<void> {
  await ensureDataDir()
  await fs.writeFile(EMAILS_FILE, JSON.stringify(emails, null, 2))
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

    const emails = await loadEmails()
    
    if (emails.includes(email)) {
      return Response.json(
        { message: 'This email is already subscribed' },
        { status: 400 }
      )
    }

    emails.push(email)
    await saveEmails(emails)

    return Response.json(
      { message: 'Successfully subscribed to newsletter' },
      { status: 200 }
    )
  } catch (error) {
    console.error('[v0] Newsletter error:', error)
    return Response.json(
      { message: 'Failed to process subscription' },
      { status: 500 }
    )
  }
}
