/** @type {import('next').NextConfig} */
const nextConfig = {
  // Force cache clear - deployment trigger v2
  images: {
    // Enable Next.js image optimization for better Core Web Vitals
    remotePatterns: [
      {
        protocol: 'https',
        hostname: '**',
      },
    ],
  },
}

module.exports = nextConfig
