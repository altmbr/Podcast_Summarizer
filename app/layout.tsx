import type { Metadata } from 'next'
import './globals.css'
import NewsletterSubscribe from '@/components/NewsletterSubscribe'
import { PHProvider } from './providers'
import PostHogPageView from './PostHogPageView'
import StructuredData from '@/components/StructuredData'
import { generateOrganizationSchema, generateWebSiteSchema } from '@/lib/schema'
import { Suspense } from 'react'

export const metadata: Metadata = {
  metadataBase: new URL('https://www.teahose.com'),
  title: 'Teahose - Tech Podcast Summaries',
  description: 'Distillation of high-signal tech & business podcasts, including China\'s. Browse episode summaries or subscribe for daily digests — 2-5 hours → 30 seconds.',
  icons: {
    icon: [
      { url: '/favicon.ico', sizes: '48x48', type: 'image/x-icon' },
      { url: '/favicon-32x32.png', sizes: '32x32', type: 'image/png' },
      { url: '/favicon-96x96.png', sizes: '96x96', type: 'image/png' },
      { url: '/favicon-512x512.png', sizes: '512x512', type: 'image/png' },
    ],
    apple: { url: '/apple-touch-icon.png', sizes: '180x180', type: 'image/png' },
  },
  openGraph: {
    title: 'Teahose - Tech Podcast Summaries',
    description: 'Distillation of high-signal tech & business podcasts, including China\'s. Browse episode summaries or subscribe for daily digests — 2-5 hours → 30 seconds.',
    url: 'https://www.teahose.com',
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
    description: 'Distillation of high-signal tech & business podcasts, including China\'s. Browse episode summaries or subscribe for daily digests — 2-5 hours → 30 seconds.',
    images: ['/og-image.png'],
  },
  alternates: {
    canonical: '/',
  },
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <head>
        <StructuredData
          data={[generateOrganizationSchema(), generateWebSiteSchema()]}
        />
      </head>
      <body>
        <PHProvider>
          <Suspense fallback={null}>
            <PostHogPageView />
          </Suspense>
          <div className="min-h-screen pb-32">
            {children}
          </div>
          <NewsletterSubscribe />
        </PHProvider>
      </body>
    </html>
  )
}
