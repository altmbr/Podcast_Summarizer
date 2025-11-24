'use client'

import { useState } from 'react'

interface InsightShareButtonProps {
  headingText: string
  episodeUrl: string
}

export default function InsightShareButton({ headingText, episodeUrl }: InsightShareButtonProps) {
  const [copied, setCopied] = useState(false)

  const handleShare = async (e: React.MouseEvent) => {
    e.preventDefault()
    e.stopPropagation()

    // Find the next siblings after this heading until we hit another heading
    const heading = (e.currentTarget as HTMLElement).closest('h3')
    if (!heading) return

    let descriptionText = ''
    let currentElement = heading.nextElementSibling

    // Collect paragraphs until we hit another heading
    while (currentElement && !['H1', 'H2', 'H3', 'H4', 'H5', 'H6'].includes(currentElement.tagName)) {
      if (currentElement.tagName === 'P') {
        descriptionText += currentElement.textContent + '\n\n'
      }
      currentElement = currentElement.nextElementSibling
    }

    // Format the text for sharing
    const shareText = `${headingText}\n\n${descriptionText.trim()}\n\n${episodeUrl}`

    try {
      await navigator.clipboard.writeText(shareText)
      setCopied(true)
      setTimeout(() => setCopied(false), 2000)
    } catch (err) {
      console.error('Failed to copy:', err)
    }
  }

  return (
    <button
      onClick={handleShare}
      className="inline-flex items-center justify-center ml-3 p-1.5 rounded hover:opacity-70 transition-opacity"
      style={{
        backgroundColor: copied ? 'var(--accent)' : 'transparent',
        border: '1px solid var(--border)',
        borderRadius: 'var(--radius)'
      }}
      title="Share this insight"
      aria-label={copied ? 'Insight copied to clipboard' : 'Share this insight'}
    >
      {copied ? (
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
          style={{ color: 'white' }}
        >
          <polyline points="20 6 9 17 4 12"></polyline>
        </svg>
      ) : (
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
          style={{ color: 'var(--muted-foreground)' }}
        >
          <circle cx="18" cy="5" r="3"></circle>
          <circle cx="6" cy="12" r="3"></circle>
          <circle cx="18" cy="19" r="3"></circle>
          <line x1="8.59" y1="13.51" x2="15.42" y2="17.49"></line>
          <line x1="15.41" y1="6.51" x2="8.59" y2="10.49"></line>
        </svg>
      )}
    </button>
  )
}
