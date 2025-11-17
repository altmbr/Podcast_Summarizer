import type { Metadata } from 'next'
import './globals.css'
import NewsletterSubscribe from '@/components/NewsletterSubscribe'
import { PHProvider } from './providers'
import PostHogPageView from './PostHogPageView'
import { Suspense } from 'react'

export const metadata: Metadata = {
  title: 'Teahose - Tech Podcast Summaries',
  description: 'Summaries of the most important tech podcasts — including China\'s. Subscribe for the weekly briefing that distills 30+ hours of podcasts into a 5-minute read.',
  openGraph: {
    title: 'Teahose - Tech Podcast Summaries',
    description: 'Summaries of the most important tech podcasts — including China\'s. Subscribe for the weekly briefing that distills 30+ hours of podcasts into a 5-minute read.',
    url: 'https://teahose.com',
    siteName: 'Teahose',
    images: [
      {
        url: '/og-image.png',
        width: 1536,
        height: 1024,
        alt: 'Teahose - Tech podcast summaries',
      },
    ],
    locale: 'en_US',
    type: 'website',
  },
  twitter: {
    card: 'summary_large_image',
    title: 'Teahose - Tech Podcast Summaries',
    description: 'Summaries of the most important tech podcasts — including China\'s. Subscribe for the weekly briefing that distills 30+ hours of podcasts into a 5-minute read.',
    images: ['/og-image.png'],
  },
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
