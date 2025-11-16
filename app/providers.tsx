'use client'

import posthog from 'posthog-js'
import { PostHogProvider } from 'posthog-js/react'
import { useEffect } from 'react'

export function PHProvider({ children }: { children: React.ReactNode }) {
  useEffect(() => {
    if (typeof window !== 'undefined') {
      const apiKey = process.env.NEXT_PUBLIC_POSTHOG_KEY
      const apiHost = process.env.NEXT_PUBLIC_POSTHOG_HOST || 'https://us.i.posthog.com'

      if (apiKey) {
        posthog.init(apiKey, {
          api_host: apiHost,
          person_profiles: 'identified_only',
          capture_pageview: false, // We'll capture pageviews manually
          capture_pageleave: true,
        })
      }
    }
  }, [])

  return <PostHogProvider client={posthog}>{children}</PostHogProvider>
}
