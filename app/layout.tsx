import type { Metadata } from 'next'
import './globals.css'
import NewsletterSubscribe from '@/components/NewsletterSubscribe'
import { PHProvider } from './providers'
import PostHogPageView from './PostHogPageView'
import { Suspense } from 'react'

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
      <PHProvider>
        <body className="bg-gray-50 text-gray-900">
          <Suspense fallback={null}>
            <PostHogPageView />
          </Suspense>
          <div className="min-h-screen pb-32">
            {children}
          </div>
          <NewsletterSubscribe />
        </body>
      </PHProvider>
    </html>
  )
}
