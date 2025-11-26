'use client'

import { useState } from 'react'
import { usePostHog } from 'posthog-js/react'

interface ShareButtonProps {
  url?: string
  title?: string
  refSource?: string // e.g., 'home', 'podcast-page', 'episode-page'
  podcast?: string
  episode?: string
}

export default function ShareButton({ url, title, refSource, podcast, episode }: ShareButtonProps) {
  const [copied, setCopied] = useState(false)
  const posthog = usePostHog()

  const handleCopy = async () => {
    let shareUrl = url || window.location.href

    // Map refSource to share_location for PostHog event
    let shareLocation: 'homepage' | 'podcast_header' | 'episode_header' | undefined
    if (refSource === 'home') {
      shareLocation = 'homepage'
    } else if (refSource === 'podcast-page') {
      shareLocation = 'podcast_header'
    } else if (refSource === 'episode-page') {
      shareLocation = 'episode_header'
    }

    // Track PostHog event
    if (posthog && shareLocation) {
      const eventProperties: Record<string, string> = {
        share_location: shareLocation,
      }

      // Add episode context if available
      if (podcast) {
        eventProperties.podcast_name = podcast
      }
      if (episode) {
        eventProperties.episode_title = episode
      }

      posthog.capture('share_button_clicked', eventProperties)
    }

    // Add ref parameter based on context
    if (refSource) {
      const urlObj = new URL(shareUrl, window.location.origin)

      // Get PostHog distinct_id (user ID)
      const userId = posthog?.get_distinct_id() || 'unknown'

      if (refSource === 'home') {
        urlObj.searchParams.set('ref', `share-home-${userId}`)
      } else if (refSource === 'podcast-page' && podcast) {
        urlObj.searchParams.set('ref', `share-podcast-${encodeURIComponent(podcast)}-${userId}`)
      } else if (refSource === 'episode-page' && podcast && episode) {
        urlObj.searchParams.set('ref', `share-episode-${encodeURIComponent(podcast)}-${encodeURIComponent(episode)}-${userId}`)
      }

      shareUrl = urlObj.toString()
    }

    try {
      await navigator.clipboard.writeText(shareUrl)
      setCopied(true)
      setTimeout(() => setCopied(false), 2000)
    } catch (err) {
      console.error('Failed to copy:', err)
    }
  }

  return (
    <button
      onClick={handleCopy}
      style={{
        color: 'var(--foreground)',
        borderColor: 'var(--border)',
        backgroundColor: 'var(--background)',
        fontSize: 'var(--text-sm)',
        borderRadius: 'var(--radius)'
      }}
      className="px-3 py-2 border hover:opacity-70 transition-opacity whitespace-nowrap"
      aria-label="Copy link to clipboard"
    >
        {copied ? (
          <span className="flex items-center gap-2">
            <svg width="16" height="16" viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M13.5 4L6 11.5L2.5 8" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
            </svg>
            Copied!
          </span>
        ) : (
          <span className="flex items-center gap-2">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              width="16"
              height="16"
              viewBox="0 0 24 24"
              fill="none"
              stroke="currentColor"
              strokeWidth="2"
              strokeLinecap="round"
              strokeLinejoin="round"
            >
              <circle cx="18" cy="5" r="3"></circle>
              <circle cx="6" cy="12" r="3"></circle>
              <circle cx="18" cy="19" r="3"></circle>
              <line x1="8.59" y1="13.51" x2="15.42" y2="17.49"></line>
              <line x1="15.41" y1="6.51" x2="8.59" y2="10.49"></line>
            </svg>
            Spill the Tea
          </span>
        )}
      </button>
  )
}
