'use client'

import ReactMarkdown from 'react-markdown'
import remarkGfm from 'remark-gfm'
import InsightShareButton from './InsightShareButton'

interface MarkdownRendererProps {
  content: string
  episodeUrl?: string
  enableInsightSharing?: boolean
}

export default function MarkdownRenderer({ content, episodeUrl, enableInsightSharing = false }: MarkdownRendererProps) {
  return (
    <div className="prose prose-sm max-w-none" style={{ color: 'var(--foreground)' }}>
      <ReactMarkdown
        remarkPlugins={[remarkGfm]}
        components={{
          h1: ({ node, ...props }) => (
            <h1 style={{ color: 'var(--foreground)' }} className="text-3xl font-light tracking-tight mt-8 mb-4" {...props} />
          ),
          h2: ({ node, ...props }) => (
            <h2 style={{ color: 'var(--foreground)' }} className="text-2xl font-light tracking-tight mt-6 mb-3" {...props} />
          ),
          h3: ({ node, children, ...props }) => {
            // Extract text content for sharing (remove markdown formatting)
            const getTextContent = (element: any): string => {
              if (typeof element === 'string') return element
              if (Array.isArray(element)) {
                return element.map(getTextContent).join('')
              }
              if (element?.props?.children) {
                return getTextContent(element.props.children)
              }
              return ''
            }

            const headingText = getTextContent(children)

            // Only show share button if:
            // 1. Insight sharing is enabled
            // 2. We have an episode URL
            // 3. The heading text is not empty
            const showShareButton = enableInsightSharing && episodeUrl && headingText.trim().length > 0

            return (
              <h3
                style={{ color: 'var(--foreground)' }}
                className="text-xl font-light tracking-tight mt-5 mb-2 flex items-start gap-2"
                {...props}
              >
                <span className="flex-1">{children}</span>
                {showShareButton && (
                  <InsightShareButton headingText={headingText} episodeUrl={episodeUrl} />
                )}
              </h3>
            )
          },
          p: ({ node, ...props }) => (
            <p style={{ color: 'var(--foreground)' }} className="mb-4 leading-relaxed" {...props} />
          ),
          ul: ({ node, ...props }) => (
            <ul style={{ color: 'var(--foreground)' }} className="list-disc list-inside mb-4 space-y-2" {...props} />
          ),
          ol: ({ node, ...props }) => (
            <ol style={{ color: 'var(--foreground)' }} className="list-decimal list-inside mb-4 space-y-2" {...props} />
          ),
          li: ({ node, ...props }) => (
            <li style={{ color: 'var(--foreground)' }} {...props} />
          ),
          blockquote: ({ node, ...props }) => (
            <blockquote
              style={{ borderLeftColor: 'var(--accent)', color: 'var(--muted-foreground)' }}
              className="border-l-4 pl-4 italic my-4"
              {...props}
            />
          ),
          code: ({ node, className, children, ...props }: any) => {
            const isInline = !className
            return isInline ? (
              <code
                style={{ backgroundColor: 'var(--secondary)', color: 'var(--foreground)' }}
                className="px-2 py-1 rounded font-mono text-sm"
                {...props}
              >
                {children}
              </code>
            ) : (
              <code
                style={{ backgroundColor: 'var(--secondary)', color: 'var(--foreground)' }}
                className="block p-4 rounded overflow-x-auto my-4 font-mono text-sm"
                {...props}
              >
                {children}
              </code>
            )
          },
          a: ({ node, ...props }) => (
            <a style={{ color: 'var(--accent)' }} className="underline hover:opacity-70" {...props} />
          ),
          table: ({ node, ...props }) => (
            <table style={{ borderColor: 'var(--border)' }} className="w-full border-collapse border my-4" {...props} />
          ),
          th: ({ node, ...props }) => (
            <th
              style={{ backgroundColor: 'var(--secondary)', borderColor: 'var(--border)', color: 'var(--foreground)' }}
              className="border p-2 text-left"
              {...props}
            />
          ),
          td: ({ node, ...props }) => (
            <td style={{ borderColor: 'var(--border)', color: 'var(--foreground)' }} className="border p-2" {...props} />
          ),
        }}
      >
        {content}
      </ReactMarkdown>
    </div>
  )
}
