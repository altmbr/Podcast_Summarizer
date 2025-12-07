'use client'

import { useEffect, useState, Suspense } from 'react'
import { useSearchParams } from 'next/navigation'
import Link from 'next/link'

type State =
  | { status: 'loading' }
  | { status: 'invalid' }
  | { status: 'ready'; email: string; alreadyUnsubscribed: boolean }
  | { status: 'processing' }
  | { status: 'success'; email: string }
  | { status: 'error'; error: string }

function UnsubscribeContent() {
  const searchParams = useSearchParams()
  const token = searchParams.get('token')
  const [state, setState] = useState<State>({ status: 'loading' })

  // Validate token on mount
  useEffect(() => {
    if (!token) {
      setState({ status: 'invalid' })
      return
    }

    fetch(`/api/unsubscribe?token=${encodeURIComponent(token)}`)
      .then(res => res.json())
      .then(data => {
        if (data.valid) {
          setState({
            status: 'ready',
            email: data.email,
            alreadyUnsubscribed: data.alreadyUnsubscribed
          })
        } else {
          setState({ status: 'invalid' })
        }
      })
      .catch(() => {
        setState({ status: 'invalid' })
      })
  }, [token])

  const handleUnsubscribe = async () => {
    if (!token) return

    setState({ status: 'processing' })

    try {
      const res = await fetch('/api/unsubscribe', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ token })
      })

      const data = await res.json()

      if (data.success) {
        setState({ status: 'success', email: data.email })
      } else {
        setState({ status: 'error', error: data.error || 'Failed to unsubscribe' })
      }
    } catch (error) {
      setState({ status: 'error', error: 'Network error' })
    }
  }

  return (
    <div className="min-h-screen bg-background flex items-center justify-center p-4">
      <div className="max-w-md w-full bg-card p-8 border-3 border-foreground shadow-brutal">
        <h1 className="font-display text-3xl font-black uppercase mb-6 text-center">
          Unsubscribe
        </h1>

        {state.status === 'loading' && (
          <div className="text-center text-muted-foreground">
            <p>Verifying your request...</p>
          </div>
        )}

        {state.status === 'invalid' && (
          <div className="text-center">
            <p className="text-muted-foreground mb-6">
              This unsubscribe link is invalid or has expired.
            </p>
            <Link
              href="/"
              className="inline-block bg-foreground text-background px-6 py-3 font-bold uppercase hover:opacity-90 transition-opacity"
            >
              Return Home
            </Link>
          </div>
        )}

        {state.status === 'ready' && state.alreadyUnsubscribed && (
          <div className="text-center">
            <p className="text-muted-foreground mb-2">
              You are already unsubscribed:
            </p>
            <p className="font-mono text-sm mb-6 break-all">
              {state.email}
            </p>
            <Link
              href="/"
              className="inline-block bg-foreground text-background px-6 py-3 font-bold uppercase hover:opacity-90 transition-opacity"
            >
              Return Home
            </Link>
          </div>
        )}

        {state.status === 'ready' && !state.alreadyUnsubscribed && (
          <div className="text-center">
            <p className="text-muted-foreground mb-2">
              Are you sure you want to unsubscribe?
            </p>
            <p className="font-mono text-sm mb-6 break-all">
              {state.email}
            </p>
            <div className="flex gap-4 justify-center">
              <button
                onClick={handleUnsubscribe}
                className="bg-accent text-background px-6 py-3 font-bold uppercase hover:opacity-90 transition-opacity border-3 border-foreground shadow-brutal"
              >
                Yes, Unsubscribe
              </button>
              <Link
                href="/"
                className="inline-block bg-foreground text-background px-6 py-3 font-bold uppercase hover:opacity-90 transition-opacity border-3 border-foreground shadow-brutal"
              >
                Cancel
              </Link>
            </div>
          </div>
        )}

        {state.status === 'processing' && (
          <div className="text-center text-muted-foreground">
            <p>Processing...</p>
          </div>
        )}

        {state.status === 'success' && (
          <div className="text-center">
            <p className="text-lg font-bold mb-2">
              ✓ You've been unsubscribed
            </p>
            <p className="font-mono text-sm text-muted-foreground mb-6 break-all">
              {state.email}
            </p>
            <p className="text-muted-foreground mb-6">
              You will no longer receive daily emails from The Daily Teahose.
            </p>
            <Link
              href="/"
              className="inline-block bg-foreground text-background px-6 py-3 font-bold uppercase hover:opacity-90 transition-opacity"
            >
              Return Home
            </Link>
          </div>
        )}

        {state.status === 'error' && (
          <div className="text-center">
            <p className="text-accent mb-4">
              Error: {state.error}
            </p>
            <Link
              href="/"
              className="inline-block bg-foreground text-background px-6 py-3 font-bold uppercase hover:opacity-90 transition-opacity"
            >
              Return Home
            </Link>
          </div>
        )}
      </div>
    </div>
  )
}

export default function UnsubscribePage() {
  return (
    <Suspense fallback={
      <div className="min-h-screen bg-background flex items-center justify-center p-4">
        <div className="max-w-md w-full bg-card p-8 border-3 border-foreground shadow-brutal">
          <h1 className="font-display text-3xl font-black uppercase mb-6 text-center">
            Unsubscribe
          </h1>
          <div className="text-center text-muted-foreground">
            <p>Loading...</p>
          </div>
        </div>
      </div>
    }>
      <UnsubscribeContent />
    </Suspense>
  )
}
