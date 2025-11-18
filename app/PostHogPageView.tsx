'use client'

import { usePathname, useSearchParams } from 'next/navigation'
import { useEffect } from 'react'
import { usePostHog } from 'posthog-js/react'

export default function PostHogPageView() {
  const pathname = usePathname()
  const searchParams = useSearchParams()
  const posthog = usePostHog()

  useEffect(() => {
    // Guard against undefined values that can occur on mobile/SSR
    if (!pathname || !posthog || typeof window === 'undefined') return

    try {
      let url = window.origin + pathname
      if (searchParams?.toString()) {
        url = url + `?${searchParams.toString()}`
      }
      posthog.capture('$pageview', {
        $current_url: url,
      })
    } catch (error) {
      // Silently fail - analytics errors shouldn't break the page
      console.error('PostHog pageview error:', error)
    }
  }, [pathname, searchParams, posthog])

  return null
}
