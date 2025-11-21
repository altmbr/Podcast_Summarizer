import { MetadataRoute } from 'next'

export default function robots(): MetadataRoute.Robots {
  return {
    rules: [
      {
        userAgent: '*',
        allow: '/',
        disallow: [
          '/api/',
          '/_next/',
          '*/transcript.md',      // Block transcript file paths
          '*/transcript_raw.md',  // Block raw transcript files
          '*/raw_podcast.mp3',    // Block audio files
        ],
      },
    ],
    sitemap: 'https://teahose.com/sitemap.xml',
  }
}
