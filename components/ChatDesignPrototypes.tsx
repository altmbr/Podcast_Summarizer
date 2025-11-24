'use client'

import { useState } from 'react'
import { X, MessageCircle, Send, Sparkles, ChevronDown, ChevronUp } from 'lucide-react'

/**
 * Chat Design Prototypes - Multiple UI options for chat with transcript
 * This file contains 5 different design approaches to explore
 */

// ============================================================================
// OPTION 1: Floating Chat Button + Modal (Intercom-style)
// ============================================================================
export function FloatingChatModal() {
  const [isOpen, setIsOpen] = useState(false)
  const [message, setMessage] = useState('')
  const [messages, setMessages] = useState([
    { role: 'assistant', content: 'Hi! I can help you explore this episode. Ask me anything about the transcript.' }
  ])

  return (
    <>
      {/* Floating Button */}
      <button
        onClick={() => setIsOpen(true)}
        style={{
          backgroundColor: 'var(--accent)',
          color: 'var(--accent-foreground)'
        }}
        className="fixed bottom-6 right-6 w-14 h-14 rounded-full shadow-lg flex items-center justify-center hover:opacity-90 transition-all z-50"
        aria-label="Open chat"
      >
        <MessageCircle className="w-6 h-6" />
      </button>

      {/* Modal Overlay */}
      {isOpen && (
        <div className="fixed inset-0 z-50 flex items-end justify-end p-6">
          {/* Backdrop */}
          <div
            className="absolute inset-0 bg-black/20"
            onClick={() => setIsOpen(false)}
          />

          {/* Chat Modal */}
          <div
            style={{
              backgroundColor: 'var(--card)',
              borderColor: 'var(--border)'
            }}
            className="relative w-full max-w-md h-[600px] border rounded-lg shadow-2xl flex flex-col"
          >
            {/* Header */}
            <div
              style={{ borderBottomColor: 'var(--border)' }}
              className="flex items-center justify-between p-4 border-b"
            >
              <div className="flex items-center gap-2">
                <Sparkles className="w-5 h-5" style={{ color: 'var(--accent)' }} />
                <h3 style={{ color: 'var(--foreground)' }} className="font-medium">
                  Chat with Transcript
                </h3>
              </div>
              <button
                onClick={() => setIsOpen(false)}
                style={{ color: 'var(--muted-foreground)' }}
                className="hover:opacity-70"
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
                      backgroundColor: msg.role === 'user' ? 'var(--accent)' : 'var(--secondary)',
                      color: msg.role === 'user' ? 'var(--accent-foreground)' : 'var(--foreground)'
                    }}
                    className="max-w-[80%] rounded-lg px-4 py-2 text-sm"
                  >
                    {msg.content}
                  </div>
                </div>
              ))}
            </div>

            {/* Input */}
            <div
              style={{ borderTopColor: 'var(--border)' }}
              className="p-4 border-t"
            >
              <div className="flex gap-2">
                <input
                  type="text"
                  value={message}
                  onChange={(e) => setMessage(e.target.value)}
                  placeholder="Ask about the episode..."
                  style={{
                    backgroundColor: 'var(--input)',
                    color: 'var(--foreground)',
                    borderColor: 'var(--border)'
                  }}
                  className="flex-1 px-3 py-2 text-sm border rounded"
                />
                <button
                  style={{
                    backgroundColor: 'var(--accent)',
                    color: 'var(--accent-foreground)'
                  }}
                  className="px-4 py-2 rounded hover:opacity-90"
                >
                  <Send className="w-4 h-4" />
                </button>
              </div>
            </div>
          </div>
        </div>
      )}
    </>
  )
}

// ============================================================================
// OPTION 2: Inline Chat Panel (Between tabs and content)
// ============================================================================
export function InlineChatPanel() {
  const [isExpanded, setIsExpanded] = useState(false)
  const [message, setMessage] = useState('')

  return (
    <div className="mb-6">
      {/* Toggle Button */}
      {!isExpanded && (
        <button
          onClick={() => setIsExpanded(true)}
          style={{
            backgroundColor: 'var(--card)',
            borderColor: 'var(--border)',
            color: 'var(--muted-foreground)'
          }}
          className="w-full border rounded-lg p-4 hover:opacity-80 transition-all flex items-center justify-between"
        >
          <div className="flex items-center gap-2">
            <Sparkles className="w-5 h-5" style={{ color: 'var(--accent)' }} />
            <span className="text-sm font-medium">Ask questions about this episode</span>
          </div>
          <ChevronDown className="w-5 h-5" />
        </button>
      )}

      {/* Expanded Panel */}
      {isExpanded && (
        <div
          style={{
            backgroundColor: 'var(--card)',
            borderColor: 'var(--border)'
          }}
          className="border rounded-lg overflow-hidden"
        >
          {/* Header */}
          <div
            style={{
              backgroundColor: 'var(--secondary)',
              borderBottomColor: 'var(--border)'
            }}
            className="flex items-center justify-between p-4 border-b"
          >
            <div className="flex items-center gap-2">
              <Sparkles className="w-5 h-5" style={{ color: 'var(--accent)' }} />
              <h3 style={{ color: 'var(--foreground)' }} className="text-sm font-medium">
                Chat with Transcript
              </h3>
            </div>
            <button
              onClick={() => setIsExpanded(false)}
              style={{ color: 'var(--muted-foreground)' }}
              className="hover:opacity-70"
            >
              <ChevronUp className="w-5 h-5" />
            </button>
          </div>

          {/* Chat Area */}
          <div className="p-4 space-y-4 max-h-[400px] overflow-y-auto">
            <div
              style={{
                backgroundColor: 'var(--secondary)',
                color: 'var(--foreground)'
              }}
              className="rounded-lg px-4 py-2 text-sm max-w-[85%]"
            >
              Hi! I can help you explore this episode. Ask me anything about the transcript.
            </div>
          </div>

          {/* Input */}
          <div
            style={{
              backgroundColor: 'var(--background)',
              borderTopColor: 'var(--border)'
            }}
            className="p-4 border-t"
          >
            <div className="flex gap-2">
              <input
                type="text"
                value={message}
                onChange={(e) => setMessage(e.target.value)}
                placeholder="Ask about the episode..."
                style={{
                  backgroundColor: 'var(--input)',
                  color: 'var(--foreground)',
                  borderColor: 'var(--border)'
                }}
                className="flex-1 px-3 py-2 text-sm border rounded"
              />
              <button
                style={{
                  backgroundColor: 'var(--accent)',
                  color: 'var(--accent-foreground)'
                }}
                className="px-4 py-2 rounded hover:opacity-90 text-sm"
              >
                Ask
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  )
}

// ============================================================================
// OPTION 3: Sidebar Chat Panel (Slides from right)
// ============================================================================
export function SidebarChat() {
  const [isOpen, setIsOpen] = useState(false)
  const [message, setMessage] = useState('')

  return (
    <>
      {/* Trigger Button */}
      <button
        onClick={() => setIsOpen(true)}
        style={{
          backgroundColor: 'var(--card)',
          borderColor: 'var(--border)',
          color: 'var(--foreground)'
        }}
        className="fixed right-0 top-1/2 -translate-y-1/2 border border-r-0 rounded-l-lg px-3 py-4 shadow-lg hover:opacity-90 flex items-center gap-2 z-40"
      >
        <Sparkles className="w-5 h-5" style={{ color: 'var(--accent)' }} />
        <span className="text-sm font-medium writing-mode-vertical-rl rotate-180">Ask AI</span>
      </button>

      {/* Sidebar Panel */}
      <div
        className={`fixed inset-y-0 right-0 w-96 z-50 transition-transform duration-300 ${
          isOpen ? 'translate-x-0' : 'translate-x-full'
        }`}
      >
        <div
          style={{
            backgroundColor: 'var(--card)',
            borderLeftColor: 'var(--border)'
          }}
          className="h-full border-l shadow-2xl flex flex-col"
        >
          {/* Header */}
          <div
            style={{ borderBottomColor: 'var(--border)' }}
            className="flex items-center justify-between p-4 border-b"
          >
            <div className="flex items-center gap-2">
              <Sparkles className="w-5 h-5" style={{ color: 'var(--accent)' }} />
              <h3 style={{ color: 'var(--foreground)' }} className="font-medium">
                Chat with Episode
              </h3>
            </div>
            <button
              onClick={() => setIsOpen(false)}
              style={{ color: 'var(--muted-foreground)' }}
              className="hover:opacity-70"
            >
              <X className="w-5 h-5" />
            </button>
          </div>

          {/* Messages */}
          <div className="flex-1 overflow-y-auto p-4 space-y-4">
            <div
              style={{
                backgroundColor: 'var(--secondary)',
                color: 'var(--foreground)'
              }}
              className="rounded-lg px-4 py-2 text-sm"
            >
              Hi! I can help you explore this episode. Ask me anything about the transcript.
            </div>
          </div>

          {/* Input */}
          <div
            style={{ borderTopColor: 'var(--border)' }}
            className="p-4 border-t"
          >
            <div className="flex gap-2">
              <input
                type="text"
                value={message}
                onChange={(e) => setMessage(e.target.value)}
                placeholder="Ask about the episode..."
                style={{
                  backgroundColor: 'var(--input)',
                  color: 'var(--foreground)',
                  borderColor: 'var(--border)'
                }}
                className="flex-1 px-3 py-2 text-sm border rounded"
              />
              <button
                style={{
                  backgroundColor: 'var(--accent)',
                  color: 'var(--accent-foreground)'
                }}
                className="px-4 py-2 rounded hover:opacity-90"
              >
                <Send className="w-4 h-4" />
              </button>
            </div>
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

// ============================================================================
// OPTION 4: Third Tab (Chat as additional tab)
// ============================================================================
export function ChatAsTab() {
  const [activeTab, setActiveTab] = useState<'summary' | 'transcript' | 'chat'>('summary')
  const [message, setMessage] = useState('')

  return (
    <div className="container py-8 md:py-12">
      {/* Tabs */}
      <div style={{ borderBottomColor: 'var(--border)' }} className="flex gap-2 mb-8 border-b pb-4">
        <button
          onClick={() => setActiveTab('summary')}
          style={{
            color: activeTab === 'summary' ? 'var(--accent)' : 'var(--muted-foreground)',
            borderBottomColor: activeTab === 'summary' ? 'var(--accent)' : 'transparent',
          }}
          className="px-4 py-2 text-sm font-medium transition-colors border-b-2"
        >
          Summary
        </button>
        <button
          onClick={() => setActiveTab('transcript')}
          style={{
            color: activeTab === 'transcript' ? 'var(--accent)' : 'var(--muted-foreground)',
            borderBottomColor: activeTab === 'transcript' ? 'var(--accent)' : 'transparent',
          }}
          className="px-4 py-2 text-sm font-medium transition-colors border-b-2"
        >
          Transcript
        </button>
        <button
          onClick={() => setActiveTab('chat')}
          style={{
            color: activeTab === 'chat' ? 'var(--accent)' : 'var(--muted-foreground)',
            borderBottomColor: activeTab === 'chat' ? 'var(--accent)' : 'transparent',
          }}
          className="px-4 py-2 text-sm font-medium transition-colors border-b-2 flex items-center gap-2"
        >
          <Sparkles className="w-4 h-4" />
          Chat
        </button>
      </div>

      {/* Chat Content */}
      {activeTab === 'chat' && (
        <div className="max-w-3xl mx-auto">
          {/* Welcome Message */}
          <div className="mb-6 text-center">
            <h3 style={{ color: 'var(--foreground)' }} className="text-xl font-light mb-2">
              Chat with this Episode
            </h3>
            <p style={{ color: 'var(--muted-foreground)' }} className="text-sm">
              Ask questions about the transcript, key insights, or specific topics discussed
            </p>
          </div>

          {/* Messages */}
          <div className="space-y-4 mb-6 min-h-[400px]">
            <div className="flex justify-start">
              <div
                style={{
                  backgroundColor: 'var(--secondary)',
                  color: 'var(--foreground)'
                }}
                className="max-w-[80%] rounded-lg px-4 py-3 text-sm"
              >
                Hi! I can help you explore this episode. Ask me anything about the transcript, key themes, or specific insights mentioned.
              </div>
            </div>
          </div>

          {/* Input */}
          <div
            style={{
              backgroundColor: 'var(--card)',
              borderColor: 'var(--border)'
            }}
            className="border rounded-lg p-4 sticky bottom-4"
          >
            <div className="flex gap-3">
              <input
                type="text"
                value={message}
                onChange={(e) => setMessage(e.target.value)}
                placeholder="Ask about the episode..."
                style={{
                  backgroundColor: 'var(--input)',
                  color: 'var(--foreground)',
                  borderColor: 'var(--border)'
                }}
                className="flex-1 px-4 py-3 border rounded"
              />
              <button
                style={{
                  backgroundColor: 'var(--accent)',
                  color: 'var(--accent-foreground)'
                }}
                className="px-6 py-3 rounded hover:opacity-90 font-medium"
              >
                Send
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  )
}

// ============================================================================
// OPTION 5: Bottom Docked Chat (Expandable from bottom)
// ============================================================================
export function BottomDockedChat() {
  const [isExpanded, setIsExpanded] = useState(false)
  const [message, setMessage] = useState('')

  return (
    <div className="fixed bottom-0 left-0 right-0 z-50">
      {/* Collapsed State */}
      {!isExpanded && (
        <div className="container">
          <button
            onClick={() => setIsExpanded(true)}
            style={{
              backgroundColor: 'var(--card)',
              borderColor: 'var(--border)',
              color: 'var(--foreground)'
            }}
            className="mb-6 w-full border border-b-0 rounded-t-lg px-6 py-3 shadow-lg hover:opacity-90 flex items-center justify-between"
          >
            <div className="flex items-center gap-2">
              <Sparkles className="w-5 h-5" style={{ color: 'var(--accent)' }} />
              <span className="font-medium">Chat with this Episode</span>
            </div>
            <ChevronUp className="w-5 h-5" style={{ color: 'var(--muted-foreground)' }} />
          </button>
        </div>
      )}

      {/* Expanded State */}
      {isExpanded && (
        <div
          style={{
            backgroundColor: 'var(--card)',
            borderTopColor: 'var(--border)'
          }}
          className="border-t shadow-2xl"
        >
          <div className="container">
            {/* Header */}
            <div className="flex items-center justify-between py-3 border-b" style={{ borderBottomColor: 'var(--border)' }}>
              <div className="flex items-center gap-2">
                <Sparkles className="w-5 h-5" style={{ color: 'var(--accent)' }} />
                <h3 style={{ color: 'var(--foreground)' }} className="font-medium">
                  Chat with Episode
                </h3>
              </div>
              <button
                onClick={() => setIsExpanded(false)}
                style={{ color: 'var(--muted-foreground)' }}
                className="hover:opacity-70"
              >
                <ChevronDown className="w-5 h-5" />
              </button>
            </div>

            {/* Messages */}
            <div className="py-4 space-y-4 max-h-[400px] overflow-y-auto">
              <div
                style={{
                  backgroundColor: 'var(--secondary)',
                  color: 'var(--foreground)'
                }}
                className="inline-block rounded-lg px-4 py-2 text-sm max-w-[85%]"
              >
                Hi! I can help you explore this episode. Ask me anything about the transcript.
              </div>
            </div>

            {/* Input */}
            <div className="pb-4 pt-3 border-t" style={{ borderTopColor: 'var(--border)' }}>
              <div className="flex gap-3">
                <input
                  type="text"
                  value={message}
                  onChange={(e) => setMessage(e.target.value)}
                  placeholder="Ask about the episode..."
                  style={{
                    backgroundColor: 'var(--input)',
                    color: 'var(--foreground)',
                    borderColor: 'var(--border)'
                  }}
                  className="flex-1 px-4 py-3 border rounded"
                />
                <button
                  style={{
                    backgroundColor: 'var(--accent)',
                    color: 'var(--accent-foreground)'
                  }}
                  className="px-6 py-3 rounded hover:opacity-90 font-medium"
                >
                  Send
                </button>
              </div>
            </div>
          </div>
        </div>
      )}
    </div>
  )
}
