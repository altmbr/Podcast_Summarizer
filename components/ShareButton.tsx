'use client'

import { useState } from 'react'

interface ShareButtonProps {
  url?: string
  title?: string
}

export default function ShareButton({ url, title }: ShareButtonProps) {
  const [copied, setCopied] = useState(false)

  const handleShare = async () => {
    const shareUrl = url || window.location.href
    const shareTitle = title || 'Teahose - Tech Podcast Summaries'

    // Check if Web Share API is available (mobile devices)
    if (navigator.share) {
      try {
        await navigator.share({
          title: shareTitle,
          url: shareUrl,
        })
      } catch (err) {
        // User cancelled or error occurred
        console.log('Share cancelled or failed')
      }
    } else {
      // Fallback: Copy to clipboard
      try {
        await navigator.clipboard.writeText(shareUrl)
        setCopied(true)
        setTimeout(() => setCopied(false), 2000)
      } catch (err) {
        console.error('Failed to copy:', err)
      }
    }
  }

  return (
    <button
      onClick={handleShare}
      style={{
        color: 'var(--foreground)',
        borderColor: 'var(--border)',
      }}
      className="fixed top-4 right-4 md:top-6 md:right-6 z-40 px-3 py-2 text-sm border rounded-sm hover:opacity-70 transition-opacity bg-[var(--background)]"
      aria-label="Share this page"
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
          <svg width="16" height="16" viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M10 5.5L13.5 2M13.5 2L10 -1.5M13.5 2H8.5C6.01472 2 4 4.01472 4 6.5V7.5M6 10.5L2.5 14M2.5 14L6 17.5M2.5 14H7.5C9.98528 14 12 11.9853 12 9.5V8.5" stroke="currentColor" strokeWidth="1.5" strokeLinecap="round" strokeLinejoin="round"/>
          </svg>
          Share
        </span>
      )}
    </button>
  )
}
