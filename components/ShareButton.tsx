'use client'

import { useState } from 'react'

interface ShareButtonProps {
  url?: string
  title?: string
}

export default function ShareButton({ url, title }: ShareButtonProps) {
  const [copied, setCopied] = useState(false)

  const handleCopy = async () => {
    const shareUrl = url || window.location.href

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
      }}
      className="px-3 py-2 text-sm border rounded-sm hover:opacity-70 transition-opacity bg-[var(--background)] whitespace-nowrap"
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
            <svg width="16" height="16" viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M8 2V8M8 8V14M8 8H14M8 8H2" stroke="currentColor" strokeWidth="1.5" strokeLinecap="round"/>
              <circle cx="8" cy="8" r="7" stroke="currentColor" strokeWidth="1.5"/>
            </svg>
            Share the Tea
          </span>
        )}
      </button>
  )
}
