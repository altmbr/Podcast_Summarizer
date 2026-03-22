'use client'

import { useSearchParams } from 'next/navigation'
import { useEffect, useRef } from 'react'
import { usePostHog } from 'posthog-js/react'

export default function SubscriberIdentify() {
  const searchParams = useSearchParams()
  const posthog = usePostHog()
  const identified = useRef(false)

  useEffect(() => {
    if (identified.current) return
    const ref = searchParams?.get('ref')
    if (!ref || !posthog || ref.indexOf('.') === -1) return

    identified.current = true

    fetch(`/api/verify-ref?ref=${encodeURIComponent(ref)}`)
      .then((res) => res.ok ? res.json() : null)
      .then((data) => {
        if (data?.email) {
          posthog.identify(data.email, {
            email: data.email,
            newsletter_subscribed: true,
            identified_via: 'email_clickthrough',
          })
        }
      })
      .catch(() => {})
  }, [searchParams, posthog])

  return null
}
