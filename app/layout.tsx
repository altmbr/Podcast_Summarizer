import type { Metadata } from 'next'
import Link from 'next/link'
import './globals.css'
import NewsletterSubscribe from '@/components/NewsletterSubscribe'
import { PHProvider } from './providers'
import PostHogPageView from './PostHogPageView'
import StructuredData from '@/components/StructuredData'
import { generateOrganizationSchema, generateWebSiteSchema } from '@/lib/schema'
import { Suspense } from 'react'

export const metadata: Metadata = {
  metadataBase: new URL('https://www.teahose.com'),
  title: 'Teahose - Tech Podcasts, Newsletters & Research Papers',
  description: 'A distillation of leading tech & business podcasts, newsletters, and Physical AI research papers. Browse summaries or sub for daily digests delivering hours of insight in 30 seconds.',
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
    title: 'Teahose - Tech Podcasts, Newsletters & Research Papers',
    description: 'A distillation of leading tech & business podcasts, newsletters, and Physical AI research papers. Browse summaries or sub for daily digests delivering hours of insight in 30 seconds.',
    url: 'https://www.teahose.com/',
    siteName: 'Teahose',
    images: [
      {
        url: '/og-image-comic.png',
        width: 1536,
        height: 1024,
        alt: 'Teahose - Tech podcasts, newsletters, and research papers',
      },
    ],
    locale: 'en_US',
    type: 'website',
  },
  twitter: {
    card: 'summary_large_image',
    title: 'Teahose - Tech Podcasts, Newsletters & Research Papers',
    description: 'A distillation of leading tech & business podcasts, newsletters, and Physical AI research papers. Browse summaries or sub for daily digests delivering hours of insight in 30 seconds.',
    images: ['/og-image-comic.png'],
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
          <nav aria-label="Site navigation" style={{ borderTopColor: 'var(--border)' }} className="border-t">
            <div className="container py-6 flex flex-wrap gap-6 justify-center text-sm" style={{ color: 'var(--muted-foreground)' }}>
              <Link href="/" className="hover:underline">Home</Link>
              <Link href="/#podcasts" className="hover:underline">Podcasts</Link>
              <Link href="/#newsletters" className="hover:underline">Newsletters</Link>
              <Link href="/#papers" className="hover:underline">Papers</Link>
              <Link href="/sitemap.xml" className="hover:underline">Sitemap</Link>
            </div>
          </nav>
        </PHProvider>
      </body>
    </html>
  )
}
