'use client'

import { useState } from 'react'
import {
  FloatingChatModal,
  InlineChatPanel,
  SidebarChat,
  ChatAsTab,
  BottomDockedChat
} from '@/components/ChatDesignPrototypes'

/**
 * Demo page to showcase 5 different chat interface design options
 * Navigate to /chat-design-demos to view
 */
export default function ChatDesignDemos() {
  const [activeDemo, setActiveDemo] = useState<number | null>(null)

  const demos = [
    {
      id: 1,
      name: 'Floating Chat Button + Modal',
      description: 'Intercom-style floating button that opens a modal chat window. Non-intrusive, familiar pattern.',
      pros: ['Familiar UX pattern', 'Doesn\'t interfere with reading', 'Always accessible', 'Mobile-friendly'],
      cons: ['Covers content when open', 'Requires switching context', 'Less discoverable'],
      component: <FloatingChatModal />
    },
    {
      id: 2,
      name: 'Inline Chat Panel',
      description: 'Expandable panel between tabs and content. Integrated into the page flow.',
      pros: ['Integrated into page flow', 'No context switching', 'Clearly visible', 'Doesn\'t cover content'],
      cons: ['Pushes content down', 'Takes vertical space', 'May interrupt reading flow'],
      component: <InlineChatPanel />
    },
    {
      id: 3,
      name: 'Sidebar Chat Panel',
      description: 'Slides in from the right side. Great for desktop viewing.',
      pros: ['Side-by-side with content', 'Desktop-optimized', 'Doesn\'t push content', 'Easy to reference transcript'],
      cons: ['Not ideal for mobile', 'Takes horizontal space', 'May feel cramped on smaller screens'],
      component: <SidebarChat />
    },
    {
      id: 4,
      name: 'Chat as Third Tab',
      description: 'Add "Chat" as a third tab alongside Summary and Transcript.',
      pros: ['Clean integration', 'Consistent with existing UI', 'Full-screen experience', 'Very discoverable'],
      cons: ['Requires tab switching', 'Can\'t reference content while chatting', 'Less seamless'],
      component: <ChatAsTab />
    },
    {
      id: 5,
      name: 'Bottom Docked Chat',
      description: 'Expandable panel docked at bottom of page. Always visible but collapsible.',
      pros: ['Stays with you as you scroll', 'Quick access', 'Doesn\'t cover content', 'Good for mobile'],
      cons: ['Takes bottom screen space', 'May feel intrusive', 'Limited height when expanded'],
      component: <BottomDockedChat />
    }
  ]

  return (
    <main className="min-h-screen" style={{ backgroundColor: 'var(--background)' }}>
      {/* Header */}
      <header style={{ borderBottomColor: 'var(--border)' }} className="border-b">
        <div className="container py-8 md:py-12">
          <h1 style={{ color: 'var(--foreground)' }} className="mb-3">
            Chat Interface Design Options
          </h1>
          <p style={{ color: 'var(--muted-foreground)' }} className="text-lg">
            Explore 5 different design approaches for adding chat functionality to episode pages
          </p>
        </div>
      </header>

      {/* Demo Selection */}
      <section className="container py-8 md:py-12">
        <div className="grid gap-6 md:grid-cols-2 lg:grid-cols-3">
          {demos.map((demo) => (
            <button
              key={demo.id}
              onClick={() => setActiveDemo(demo.id)}
              style={{
                backgroundColor: activeDemo === demo.id ? 'var(--accent)' : 'var(--card)',
                borderColor: activeDemo === demo.id ? 'var(--accent)' : 'var(--border)',
                color: activeDemo === demo.id ? 'var(--accent-foreground)' : 'var(--foreground)'
              }}
              className="border rounded-lg p-6 text-left hover:opacity-90 transition-all"
            >
              <h3 className="font-medium mb-2">
                Option {demo.id}: {demo.name}
              </h3>
              <p
                style={{
                  color: activeDemo === demo.id ? 'var(--accent-foreground)' : 'var(--muted-foreground)'
                }}
                className="text-sm mb-4"
              >
                {demo.description}
              </p>
              <div className="text-xs">
                <div className="mb-2">
                  <strong>Pros:</strong> {demo.pros.join(', ')}
                </div>
                <div>
                  <strong>Cons:</strong> {demo.cons.join(', ')}
                </div>
              </div>
            </button>
          ))}
        </div>
      </section>

      {/* Active Demo */}
      {activeDemo && (
        <section
          style={{
            backgroundColor: 'var(--secondary)',
            borderTopColor: 'var(--border)',
            borderBottomColor: 'var(--border)'
          }}
          className="border-y py-8 md:py-12"
        >
          <div className="container">
            <div className="mb-6">
              <h2 style={{ color: 'var(--foreground)' }} className="mb-2">
                Option {activeDemo}: {demos[activeDemo - 1].name}
              </h2>
              <p style={{ color: 'var(--muted-foreground)' }}>
                Interact with the prototype below (non-functional, UI demonstration only)
              </p>
            </div>

            {/* Mock Episode Content */}
            <div
              style={{
                backgroundColor: 'var(--card)',
                borderColor: 'var(--border)'
              }}
              className="border rounded-lg p-6 mb-8 min-h-[600px]"
            >
              <h3 style={{ color: 'var(--foreground)' }} className="text-xl mb-4">
                Sample Episode: Inside Thrive Capital
              </h3>
              <div style={{ color: 'var(--muted-foreground)' }} className="space-y-4 text-sm leading-relaxed">
                <p>
                  This is a sample episode page demonstrating how the chat interface would integrate with actual content.
                  The chat feature allows users to ask questions about the transcript and get AI-powered answers.
                </p>
                <p>
                  Key themes discussed in this episode include venture capital strategies, AI investment landscape,
                  and lessons from portfolio companies like OpenAI, Cursor, and Wiz.
                </p>
                <p>
                  Try clicking the chat interface elements to see how they would work in practice. Each design option
                  offers different trade-offs between accessibility, screen real estate, and user experience.
                </p>
                <p>
                  The ideal solution should blend seamlessly with the existing design while providing easy access
                  to the chat functionality without disrupting the reading experience.
                </p>
              </div>
            </div>

            {/* Render Active Demo */}
            <div className="relative">
              {demos[activeDemo - 1].component}
            </div>
          </div>
        </section>
      )}

      {/* Recommendations */}
      <section className="container py-8 md:py-12">
        <div
          style={{
            backgroundColor: 'var(--card)',
            borderColor: 'var(--border)'
          }}
          className="border rounded-lg p-6"
        >
          <h2 style={{ color: 'var(--foreground)' }} className="mb-4">
            Design Recommendations
          </h2>
          <div style={{ color: 'var(--foreground)' }} className="space-y-4 text-sm">
            <div>
              <h3 className="font-medium mb-2">🏆 Top Pick: Inline Chat Panel (Option 2)</h3>
              <p style={{ color: 'var(--muted-foreground)' }}>
                Best balance of discoverability and non-intrusiveness. Integrates naturally with the existing
                tab structure, stays out of the way when collapsed, and provides ample space when expanded.
                Works well on both desktop and mobile.
              </p>
            </div>
            <div>
              <h3 className="font-medium mb-2">🥈 Runner-up: Sidebar Chat (Option 3)</h3>
              <p style={{ color: 'var(--muted-foreground)' }}>
                Excellent for desktop users who want to reference the content while chatting. Provides the best
                side-by-side experience but may need a different approach for mobile devices.
              </p>
            </div>
            <div>
              <h3 className="font-medium mb-2">💡 Alternative: Chat as Tab (Option 4)</h3>
              <p style={{ color: 'var(--muted-foreground)' }}>
                Cleanest integration with existing UI patterns. Very discoverable and consistent. Good choice if
                users are expected to have dedicated chat sessions rather than quick questions.
              </p>
            </div>
          </div>
        </div>
      </section>

      {/* Footer */}
      <footer style={{ borderTopColor: 'var(--border)' }} className="border-t mt-8">
        <div style={{ color: 'var(--muted-foreground)' }} className="container py-8 text-center text-sm">
          <p>Select an option above to interact with the prototype</p>
        </div>
      </footer>
    </main>
  )
}
