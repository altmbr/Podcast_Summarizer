import Link from 'next/link'
import { Metadata } from 'next'
import { BASE_URL } from '@/lib/constants'

export const metadata: Metadata = {
  title: 'About Teahose - AI-Powered Podcast, Newsletter & Research Paper Summaries',
  description: 'Teahose summarizes 25+ tech podcasts, 10+ newsletters, and Physical AI research papers using Claude AI. Free daily email digests delivering hours of insight in 30 seconds.',
  alternates: { canonical: `${BASE_URL}/about` },
  openGraph: {
    title: 'About Teahose',
    description: 'AI-powered summaries of the best tech podcasts, newsletters, and research papers. Free daily email digests.',
    url: `${BASE_URL}/about`,
    siteName: 'Teahose',
    type: 'website',
  },
}

export default function AboutPage() {
  return (
    <main className="min-h-screen" style={{ backgroundColor: 'var(--background)' }}>
      <header style={{ borderBottomColor: 'var(--border)' }} className="border-b">
        <div className="container py-8 md:py-12">
          <Link href="/" style={{ color: 'var(--muted-foreground)' }} className="hover:underline mb-4 block text-sm">
            ← Back to Home
          </Link>
          <h1 style={{ color: 'var(--foreground)' }}>About Teahose</h1>
        </div>
      </header>

      <article className="container py-12 md:py-16 max-w-3xl">
        <div className="space-y-8" style={{ color: 'var(--foreground)' }}>
          <section>
            <h2 className="mb-4">What is Teahose?</h2>
            <p style={{ color: 'var(--muted-foreground)' }} className="text-sm leading-relaxed mb-4">
              Teahose is an AI-powered platform that summarizes the best tech and business podcasts, newsletters, and Physical AI research papers into concise, readable summaries.
            </p>
            <p style={{ color: 'var(--muted-foreground)' }} className="text-sm leading-relaxed">
              Instead of spending hours listening to podcasts or reading newsletters, Teahose delivers the key insights in 30-second summaries. Browse on the website or subscribe for a free daily email digest at 6 AM EST.
            </p>
          </section>

          <section>
            <h2 className="mb-4">What We Cover</h2>
            <div className="grid gap-6 md:grid-cols-3">
              <div className="p-6 rounded-sm" style={{ backgroundColor: 'var(--card)' }}>
                <h3 className="mb-2 text-lg">25+ Podcasts</h3>
                <p style={{ color: 'var(--muted-foreground)' }} className="text-sm leading-relaxed">
                  20VC, All In, Acquired, Lenny's Podcast, The a16z Show, Lex Fridman, No Priors, BG2, Dwarkesh, My First Million, DOAC, and more. New episodes processed 3x daily.
                </p>
              </div>
              <div className="p-6 rounded-sm" style={{ backgroundColor: 'var(--card)' }}>
                <h3 className="mb-2 text-lg">10+ Newsletters</h3>
                <p style={{ color: 'var(--muted-foreground)' }} className="text-sm leading-relaxed">
                  Stratechery (Ben Thompson), StrictlyVC, Newcomer (Eric Newcomer), Axios Pro Rata (Dan Primack), Coatue, PitchBook, Data Driven VC, and more. Processed in real-time.
                </p>
              </div>
              <div className="p-6 rounded-sm" style={{ backgroundColor: 'var(--card)' }}>
                <h3 className="mb-2 text-lg">Physical AI Papers</h3>
                <p style={{ color: 'var(--muted-foreground)' }} className="text-sm leading-relaxed">
                  Top 1-2 research papers daily from arXiv, Semantic Scholar, and HuggingFace. Tracking 14 labs including Physical Intelligence, Google DeepMind, Toyota Research Institute, MIT, and Stanford.
                </p>
              </div>
            </div>
          </section>

          <section>
            <h2 className="mb-4">How It Works</h2>
            <ol className="space-y-4" style={{ color: 'var(--muted-foreground)' }}>
              <li className="text-sm leading-relaxed">
                <strong style={{ color: 'var(--foreground)' }}>1. Automated discovery</strong> — Teahose monitors podcast feeds via Podscan, ingests newsletters via email, and queries arXiv for new papers. No manual curation needed.
              </li>
              <li className="text-sm leading-relaxed">
                <strong style={{ color: 'var(--foreground)' }}>2. Full transcript extraction</strong> — Podcast episodes are fully transcribed with speaker labels and timestamps. Newsletters are extracted from HTML. Papers are downloaded as PDFs and parsed.
              </li>
              <li className="text-sm leading-relaxed">
                <strong style={{ color: 'var(--foreground)' }}>3. AI summarization</strong> — Claude AI (Anthropic) generates structured summaries with key themes, notable quotes with clickable YouTube timestamps, contrarian perspectives, and actionable insights.
              </li>
              <li className="text-sm leading-relaxed">
                <strong style={{ color: 'var(--foreground)' }}>4. Instant publishing</strong> — Summaries are automatically committed and deployed to teahose.com within minutes of processing.
              </li>
              <li className="text-sm leading-relaxed">
                <strong style={{ color: 'var(--foreground)' }}>5. Daily digest</strong> — Every morning at 6 AM EST, subscribers get an email with all new summaries from the last 24 hours, including a custom AI-generated header image.
              </li>
            </ol>
          </section>

          <section>
            <h2 className="mb-4">What Makes Teahose Different</h2>
            <p style={{ color: 'var(--muted-foreground)' }} className="text-sm leading-relaxed mb-4">
              Unlike self-service tools (Snipd, NoteGPT, Podsqueeze) where you paste a URL and get a summary, Teahose is a curated, always-on platform:
            </p>
            <ul className="space-y-2" style={{ color: 'var(--muted-foreground)' }}>
              <li className="text-sm leading-relaxed"><strong style={{ color: 'var(--foreground)' }}>All-in-one</strong> — Podcasts, newsletters, and research papers in a single feed</li>
              <li className="text-sm leading-relaxed"><strong style={{ color: 'var(--foreground)' }}>Fully automated</strong> — No URLs to paste, no accounts to manage. Content is discovered and summarized automatically.</li>
              <li className="text-sm leading-relaxed"><strong style={{ color: 'var(--foreground)' }}>Clickable timestamps</strong> — Jump to the exact moment on YouTube from any quote</li>
              <li className="text-sm leading-relaxed"><strong style={{ color: 'var(--foreground)' }}>Speaker attribution</strong> — Know who said what with speaker-labeled transcripts</li>
              <li className="text-sm leading-relaxed"><strong style={{ color: 'var(--foreground)' }}>Free daily digest</strong> — One email, everything you need to know</li>
              <li className="text-sm leading-relaxed"><strong style={{ color: 'var(--foreground)' }}>Chat with transcripts</strong> — Ask questions about any podcast episode directly on the page</li>
            </ul>
          </section>

          <section>
            <h2 className="mb-4">Pricing</h2>
            <p style={{ color: 'var(--muted-foreground)' }} className="text-sm leading-relaxed">
              Teahose is completely free. Browse all summaries on teahose.com or subscribe to the daily email digest at no cost.
            </p>
          </section>
        </div>
      </article>

      <footer style={{ borderTopColor: 'var(--border)' }} className="border-t mt-16 md:mt-20">
        <div style={{ color: 'var(--muted-foreground)' }} className="container py-8 text-center text-sm">
          <p>
            <Link href="/" className="hover:underline" style={{ color: 'var(--accent)' }}>Browse summaries</Link>
            {' '} or subscribe for the free daily digest.
          </p>
        </div>
      </footer>
    </main>
  )
}
