'use client';

import ReactMarkdown from 'react-markdown';
import remarkGfm from 'remark-gfm';

interface MarkdownRendererProps {
  content: string;
}

export default function MarkdownRenderer({ content }: MarkdownRendererProps) {
  return (
    <div className="w-full">
      <ReactMarkdown
        remarkPlugins={[remarkGfm]}
        components={{
          // Customize link rendering to open in new tab
          a: ({ node, ...props }) => (
            <a
              {...props}
              target="_blank"
              rel="noopener noreferrer"
              className="text-blue-600 hover:text-blue-800 underline"
            />
          ),
          // Customize heading styles
          h1: ({ node, ...props }) => (
            <h1 {...props} className="text-3xl font-bold mt-8 mb-4 text-gray-900" />
          ),
          h2: ({ node, ...props }) => (
            <h2 {...props} className="text-2xl font-bold mt-6 mb-3 text-gray-900" />
          ),
          h3: ({ node, ...props }) => (
            <h3 {...props} className="text-xl font-semibold mt-4 mb-2 text-gray-900" />
          ),
          // Customize paragraph styles
          p: ({ node, ...props }) => (
            <p {...props} className="mb-4 text-gray-700 leading-relaxed" />
          ),
          // Customize list styles
          ul: ({ node, ...props }) => (
            <ul {...props} className="list-disc list-inside mb-4 space-y-2 text-gray-700" />
          ),
          ol: ({ node, ...props }) => (
            <ol {...props} className="list-decimal list-inside mb-4 space-y-2 text-gray-700" />
          ),
          // Customize blockquote styles
          blockquote: ({ node, ...props }) => (
            <blockquote
              {...props}
              className="border-l-4 border-blue-500 pl-4 italic my-4 text-gray-700"
            />
          ),
          // Customize code blocks
          code: ({ node, className, children, ...props }: any) => {
            const isInline = !className;
            if (isInline) {
              return (
                <code
                  {...props}
                  className="bg-gray-100 px-1.5 py-0.5 rounded text-sm font-mono text-gray-800"
                >
                  {children}
                </code>
              );
            }
            return (
              <code
                {...props}
                className="block bg-gray-100 p-4 rounded text-sm font-mono text-gray-800 overflow-x-auto"
              >
                {children}
              </code>
            );
          },
        }}
      >
        {content}
      </ReactMarkdown>
    </div>
  );
}
