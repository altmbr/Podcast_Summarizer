'use client'

import { useState } from 'react'
import { usePostHog } from 'posthog-js/react'

export default function NewsletterSubscribe() {
  const [email, setEmail] = useState('')
  const [loading, setLoading] = useState(false)
  const [message, setMessage] = useState<{ type: 'success' | 'error'; text: string } | null>(null)
  const posthog = usePostHog()

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()

    if (!email.trim()) {
      setMessage({ type: 'error', text: 'Please enter an email address' })
      return
    }

    setLoading(true)
    setMessage(null)

    try {
      const response = await fetch('/api/newsletter', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ email }),
      })

      const data = await response.json()

      if (!response.ok) {
        throw new Error(data.message || 'Failed to subscribe')
      }

      // Identify user and track newsletter subscription in PostHog
      if (posthog) {
        // Identify the user with their email as the distinct ID
        posthog.identify(email, {
          email: email,
          newsletter_subscribed: true,
          subscription_date: new Date().toISOString(),
        })

        // Capture the subscription event
        posthog.capture('newsletter_subscribed', {
          email: email,
          timestamp: new Date().toISOString(),
        })
      }

      setMessage({ type: 'success', text: 'Thanks for subscribing!' })
      setEmail('')
    } catch (error) {
      setMessage({
        type: 'error',
        text: error instanceof Error ? error.message : 'Something went wrong',
      })
    } finally {
      setLoading(false)
    }
  }

  return (
    <div style={{ backgroundColor: 'var(--background)', borderTopColor: 'var(--border)' }} className="fixed bottom-0 left-0 right-0 border-t z-50 shadow-lg">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 py-3 sm:py-4">
        <div className="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-3">
          <div className="flex-1 min-w-0">
            <p
              style={{
                color: 'var(--foreground)',
                fontSize: 'var(--text-base)',
                fontWeight: 'var(--font-weight-medium)'
              }}
            >
              Email Podcast Summaries
            </p>
            <p
              style={{
                color: 'var(--muted-foreground)',
                fontSize: 'var(--text-sm)'
              }}
              className="hidden sm:block"
            >
              Get podcast summaries in your inbox
            </p>
          </div>

          <form onSubmit={handleSubmit} className="flex gap-2 w-full sm:w-auto">
            <input
              type="email"
              placeholder="email@example.com"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              disabled={loading}
              style={{
                backgroundColor: 'var(--input)',
                borderColor: 'var(--border)',
                color: 'var(--foreground)',
                fontSize: 'var(--text-sm)',
                borderRadius: 'var(--radius)',
                '--tw-ring-color': 'var(--accent)',
              } as any}
              className="flex-1 sm:flex-none px-3 py-1.5 border placeholder:opacity-50 disabled:opacity-50 transition-colors focus:outline-none focus:ring-1"
              aria-label="Email address"
            />
            <button
              type="submit"
              disabled={loading}
              style={{
                fontSize: 'var(--text-sm)'
              }}
              className="btn-primary px-3 py-1.5 whitespace-nowrap disabled:opacity-50"
              aria-label={loading ? 'Subscribing to newsletter' : 'Subscribe to newsletter'}
            >
              {loading ? 'Loading...' : 'Subscribe'}
            </button>
          </form>
        </div>

        {message && (
          <p
            style={{
              color: message.type === 'success' ? 'var(--color-success)' : 'var(--color-error)',
              fontSize: 'var(--text-sm)'
            }}
            className="mt-2"
          >
            {message.text}
          </p>
        )}
      </div>
    </div>
  )
}
