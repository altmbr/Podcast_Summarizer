import Link from 'next/link'
import { Metadata } from 'next'

export const metadata: Metadata = {
  title: 'Page Not Found | Teahose',
  description: 'The page you are looking for could not be found.',
}

export default function NotFound() {
  return (
    <main className="min-h-screen flex items-center justify-center" style={{ backgroundColor: 'var(--background)' }}>
      <div className="container text-center py-16">
        <h1 style={{ color: 'var(--foreground)' }} className="text-6xl md:text-8xl mb-4">404</h1>
        <h2 style={{ color: 'var(--foreground)' }} className="text-2xl md:text-3xl mb-6">Page Not Found</h2>
        <p style={{ color: 'var(--muted-foreground)' }} className="text-lg mb-8 max-w-md mx-auto">
          The page you're looking for doesn't exist or may have been moved.
        </p>
        <div className="flex flex-col sm:flex-row gap-4 justify-center">
          <Link
            href="/"
            className="inline-block px-6 py-3 rounded-sm transition-all hover:opacity-80"
            style={{
              backgroundColor: 'var(--foreground)',
              color: 'var(--background)',
            }}
          >
            Go to Homepage
          </Link>
          <Link
            href="/"
            className="inline-block px-6 py-3 rounded-sm border transition-all hover:opacity-80"
            style={{
              borderColor: 'var(--border)',
              color: 'var(--foreground)',
            }}
          >
            Browse Podcasts
          </Link>
        </div>
      </div>
    </main>
  )
}
