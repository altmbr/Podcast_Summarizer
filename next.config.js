/** @type {import('next').NextConfig} */
const nextConfig = {
  // Force cache clear - deployment trigger
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
