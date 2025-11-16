import type { Metadata } from 'next'
import './globals.css'

export const metadata: Metadata = {
  title: 'Podcast Summaries',
  description: 'Browse and read AI-generated podcast summaries',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <body className="bg-gray-50 text-gray-900">
        <div className="min-h-screen">
          {children}
        </div>
      </body>
    </html>
  )
}
