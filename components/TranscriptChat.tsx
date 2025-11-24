'use client'

import { useState, useRef, useEffect, ReactElement } from 'react'
import { X, Send, Sparkles, Loader2 } from 'lucide-react'
import { usePostHog } from 'posthog-js/react'

interface Message {
  role: 'user' | 'assistant'
  content: string
}

interface TranscriptChatProps {
  transcript: string
  episodeTitle: string
  episodeSummary?: string
  videoUrl?: string
  podcastName?: string
}

export default function TranscriptChat({ transcript, episodeTitle, episodeSummary, videoUrl, podcastName }: TranscriptChatProps) {
  const [isOpen, setIsOpen] = useState(false)
  const [message, setMessage] = useState('')
  const [messages, setMessages] = useState<Message[]>([
    {
      role: 'assistant',
      content: `Hi! I can help you explore "${episodeTitle}". Ask me anything about the transcript, key insights, or specific topics discussed.`
    }
  ])
  const [isLoading, setIsLoading] = useState(false)
  const messagesEndRef = useRef<HTMLDivElement>(null)
  const posthog = usePostHog()

  // Debug: Log videoUrl when component mounts
  useEffect(() => {
    console.log('TranscriptChat videoUrl:', videoUrl)
  }, [videoUrl])

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' })
  }

  useEffect(() => {
    scrollToBottom()
  }, [messages])

  // Function to convert timestamps to clickable YouTube links
  const makeTimestampsClickable = (text: string): ReactElement => {
    if (!videoUrl) {
      return <>{text}</>
    }

    // Only process YouTube URLs
    if (!videoUrl.includes('youtube.com') && !videoUrl.includes('youtu.be')) {
      return <>{text}</>
    }

    // Match timestamps in all common formats: [HH:MM:SS], [MM:SS], [00:01:06], etc.
    // Also handles ranges like [00:01:06-00:01:32]
    const timestampRegex = /\[(\d{1,2}):(\d{2}):(\d{2})(?:-(\d{1,2}):(\d{2}):(\d{2}))?\]/g
    const parts: (string | ReactElement)[] = []
    let lastIndex = 0
    let match: RegExpExecArray | null
    let matchIndex = 0

    while ((match = timestampRegex.exec(text)) !== null) {
      // Store match data before using in closures (TypeScript null safety)
      const matchText = match[0]
      const matchIndex_current = match.index
      const matchLength = matchText.length

      // Add text before the timestamp
      if (matchIndex_current > lastIndex) {
        parts.push(text.substring(lastIndex, matchIndex_current))
      }

      // Parse the timestamp (use first time if range)
      const hours = parseInt(match[1], 10)
      const minutes = parseInt(match[2], 10)
      const seconds = parseInt(match[3], 10)

      // Convert to total seconds and subtract 10 seconds
      const totalSeconds = Math.max(0, hours * 3600 + minutes * 60 + seconds - 10)

      // Format for YouTube URL
      const hoursForUrl = Math.floor(totalSeconds / 3600)
      const minutesForUrl = Math.floor((totalSeconds % 3600) / 60)
      const secondsForUrl = totalSeconds % 60

      let timeParam = ''
      if (hoursForUrl > 0) {
        timeParam = `${hoursForUrl}h${minutesForUrl}m${secondsForUrl}s`
      } else if (minutesForUrl > 0) {
        timeParam = `${minutesForUrl}m${secondsForUrl}s`
      } else {
        timeParam = `${secondsForUrl}s`
      }

      // Create YouTube link
      const youtubeUrl = `${videoUrl}&t=${timeParam}`

      parts.push(
        <a
          key={`timestamp-${matchIndex}`}
          href={youtubeUrl}
          target="_blank"
          rel="noopener noreferrer"
          style={{ color: '#5b7f9e' }}
          className="underline hover:opacity-70"
          onClick={(e) => {
            console.log('Timestamp clicked:', matchText, 'URL:', youtubeUrl)
            // Track timestamp clicked
            posthog?.capture('chat_timestamp_clicked', {
              timestamp: matchText,
              youtube_url: youtubeUrl,
              podcast_name: podcastName,
              episode_title: episodeTitle,
            })
          }}
        >
          {matchText}
        </a>
      )

      lastIndex = matchIndex_current + matchLength
      matchIndex++
    }

    // Add remaining text
    if (lastIndex < text.length) {
      parts.push(text.substring(lastIndex))
    }

    return <>{parts}</>
  }

  const handleSend = async () => {
    if (!message.trim() || isLoading) return

    const userMessage = message.trim()
    setMessage('')
    setMessages(prev => [...prev, { role: 'user', content: userMessage }])
    setIsLoading(true)

    // Track message sent
    posthog?.capture('chat_message_sent', {
      message: userMessage,
      podcast_name: podcastName,
      episode_title: episodeTitle,
      video_url: videoUrl,
      message_length: userMessage.length,
    })

    try {
      const response = await fetch('/api/chat', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          message: userMessage,
          transcript,
          episodeTitle,
          episodeSummary,
          conversationHistory: messages
        }),
      })

      if (!response.ok) {
        throw new Error('Failed to get response')
      }

      const data = await response.json()
      const aiResponse = data.response
      setMessages(prev => [...prev, { role: 'assistant', content: aiResponse }])

      // Track AI response received
      posthog?.capture('chat_ai_response_received', {
        user_message: userMessage,
        ai_response: aiResponse,
        podcast_name: podcastName,
        episode_title: episodeTitle,
        video_url: videoUrl,
        response_length: aiResponse.length,
      })
    } catch (error) {
      console.error('Chat error:', error)
      setMessages(prev => [
        ...prev,
        {
          role: 'assistant',
          content: 'Sorry, I encountered an error. Please try again.'
        }
      ])

      // Track error
      posthog?.capture('chat_error', {
        error: error instanceof Error ? error.message : 'Unknown error',
        podcast_name: podcastName,
        episode_title: episodeTitle,
      })
    } finally {
      setIsLoading(false)
    }
  }

  const handleKeyPress = (e: React.KeyboardEvent) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault()
      handleSend()
    }
  }

  return (
    <>
      {/* Trigger Button - Fixed on right side */}
      <button
        onClick={() => {
          setIsOpen(true)
          // Track chat opened
          posthog?.capture('chat_opened', {
            podcast_name: podcastName,
            episode_title: episodeTitle,
            video_url: videoUrl,
          })
        }}
        style={{
          backgroundColor: '#ffffff',
          borderColor: '#e8e6e1',
          color: '#000000'
        }}
        className="fixed right-0 top-1/2 -translate-y-1/2 border border-r-0 rounded-l-lg px-3 py-6 shadow-lg hover:opacity-90 flex flex-col items-center gap-2 z-40 transition-all"
        aria-label="Open chat"
      >
        <Sparkles className="w-5 h-5" style={{ color: '#000000' }} />
        <span className="text-sm font-medium" style={{ writingMode: 'vertical-rl' }}>
          Chat
        </span>
      </button>

      {/* Sidebar Panel */}
      <div
        className={`fixed inset-y-0 right-0 w-full md:w-96 z-50 transition-transform duration-300 ${
          isOpen ? 'translate-x-0' : 'translate-x-full'
        }`}
      >
        <div
          style={{
            backgroundColor: '#ffffff',
            borderLeftColor: '#e8e6e1'
          }}
          className="h-full border-l shadow-2xl flex flex-col"
        >
          {/* Header */}
          <div
            style={{ borderBottomColor: '#e8e6e1' }}
            className="flex items-center justify-between p-4 border-b"
          >
            <div className="flex items-center gap-2">
              <Sparkles className="w-5 h-5" style={{ color: '#000000' }} />
              <h3 style={{ color: '#000000' }} className="font-medium text-sm md:text-base">
                Chat with Episode
              </h3>
            </div>
            <button
              onClick={() => {
                setIsOpen(false)
                // Track chat closed
                posthog?.capture('chat_closed', {
                  podcast_name: podcastName,
                  episode_title: episodeTitle,
                  messages_sent: messages.filter(m => m.role === 'user').length,
                })
              }}
              style={{ color: '#7f7f7f' }}
              className="hover:opacity-70"
              aria-label="Close chat"
            >
              <X className="w-5 h-5" />
            </button>
          </div>

          {/* Messages */}
          <div className="flex-1 overflow-y-auto p-4 space-y-4">
            {messages.map((msg, i) => (
              <div
                key={i}
                className={`flex ${msg.role === 'user' ? 'justify-end' : 'justify-start'}`}
              >
                <div
                  style={{
                    backgroundColor: msg.role === 'user' ? '#e8e6e1' : '#f0f0f0',
                    color: '#000000'
                  }}
                  className="max-w-[85%] rounded-lg px-4 py-2 text-sm leading-relaxed"
                >
                  {makeTimestampsClickable(msg.content)}
                </div>
              </div>
            ))}
            {isLoading && (
              <div className="flex justify-start">
                <div
                  style={{
                    backgroundColor: '#f0f0f0',
                    color: '#000000'
                  }}
                  className="rounded-lg px-4 py-2 text-sm flex items-center gap-2"
                >
                  <Loader2 className="w-4 h-4 animate-spin" />
                  Thinking...
                </div>
              </div>
            )}
            <div ref={messagesEndRef} />
          </div>

          {/* Input */}
          <div
            style={{ borderTopColor: '#e8e6e1' }}
            className="p-4 border-t pb-24 md:pb-20"
          >
            <div className="flex gap-2">
              <input
                type="text"
                value={message}
                onChange={(e) => setMessage(e.target.value)}
                onKeyPress={handleKeyPress}
                placeholder="Ask about the episode..."
                disabled={isLoading}
                style={{
                  backgroundColor: '#f8f8f8',
                  color: '#000000',
                  borderColor: '#e8e6e1'
                }}
                className="flex-1 px-3 py-2 text-sm border rounded disabled:opacity-50"
              />
              <button
                onClick={handleSend}
                disabled={!message.trim() || isLoading}
                style={{
                  backgroundColor: '#000000',
                  color: '#ffffff'
                }}
                className="px-4 py-2 rounded hover:opacity-90 disabled:opacity-50 disabled:cursor-not-allowed"
                aria-label="Send message"
              >
                <Send className="w-4 h-4" />
              </button>
            </div>
            <p
              style={{ color: '#7f7f7f' }}
              className="text-xs mt-2"
            >
              Powered by Gemini 2.0 Flash
            </p>
          </div>
        </div>
      </div>

      {/* Backdrop */}
      {isOpen && (
        <div
          className="fixed inset-0 bg-black/20 z-40"
          onClick={() => setIsOpen(false)}
        />
      )}
    </>
  )
}
