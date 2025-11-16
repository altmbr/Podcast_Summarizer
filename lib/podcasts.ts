import fs from 'fs';
import path from 'path';
import { Podcast, Episode } from './types';

const PODCAST_WORK_DIR = path.join(process.cwd(), '..', 'podcast_work');
const PODCAST_STATUS_PATH = path.join(process.cwd(), '..', 'podcast_status.json');
const PODCAST_HOSTS_PATH = path.join(process.cwd(), 'podcast_hosts.json');

function slugify(text: string | null | undefined): string {
  if (!text) return '';
  return text
    .toLowerCase()
    .replace(/[^\w\s-]/g, '')
    .replace(/\s+/g, '-')
    .replace(/-+/g, '-')
    .trim();
}

function sanitizeFilename(filename: string): string {
  // Match the sanitization in podcast_summarizer.py
  // Replace invalid filename characters with underscores
  let sanitized = filename.replace(/[<>:"/\\|?*]/g, '_');
  // Remove leading/trailing spaces and dots
  sanitized = sanitized.replace(/^[\s.]+|[\s.]+$/g, '');
  return sanitized;
}

export function loadPodcastStatus() {
  try {
    const statusContent = fs.readFileSync(PODCAST_STATUS_PATH, 'utf-8');
    return JSON.parse(statusContent);
  } catch (error) {
    console.error('Error loading podcast_status.json:', error);
    return { podcasts: {} };
  }
}

function loadPodcastHosts() {
  try {
    const hostsContent = fs.readFileSync(PODCAST_HOSTS_PATH, 'utf-8');
    return JSON.parse(hostsContent);
  } catch (error) {
    console.error('Error loading podcast_hosts.json:', error);
    return {};
  }
}

export function getAllPodcasts(): Podcast[] {
  const statusData = loadPodcastStatus();
  const hostsData = loadPodcastHosts();
  const podcasts: Podcast[] = [];

  // Read from podcast_status.json
  for (const [url, podcastData] of Object.entries(statusData.podcasts || {})) {
    const data = podcastData as any;
    const podcastName = data.podcast_name;

    if (!podcastName) continue;

    const episodes = data.episodes || {};
    const episodeList = Object.values(episodes);

    const transcribedCount = episodeList.filter(
      (ep: any) => ['transcribed', 'summarized'].includes(ep.status)
    ).length;

    const summarizedCount = episodeList.filter(
      (ep: any) => ep.status === 'summarized'
    ).length;

    // Get hosts from config
    const hostConfig = hostsData[podcastName] || {};

    podcasts.push({
      name: podcastName,
      slug: slugify(podcastName),
      episodeCount: episodeList.length,
      transcribedCount,
      summarizedCount,
      hosts: hostConfig.hosts || [],
    });
  }

  // Deduplicate by podcast name (in case multiple URLs for same podcast)
  const uniquePodcasts = podcasts.reduce((acc, podcast) => {
    const existing = acc.find(p => p.slug === podcast.slug);
    if (existing) {
      existing.episodeCount += podcast.episodeCount;
      existing.transcribedCount += podcast.transcribedCount;
      existing.summarizedCount += podcast.summarizedCount;
    } else {
      acc.push(podcast);
    }
    return acc;
  }, [] as Podcast[]);

  return uniquePodcasts.sort((a, b) => a.name.localeCompare(b.name));
}

export function getPodcastBySlug(slug: string): Podcast | null {
  const podcasts = getAllPodcasts();
  return podcasts.find(p => p.slug === slug) || null;
}

export function getEpisodesForPodcast(podcastSlug: string): Episode[] {
  const statusData = loadPodcastStatus();
  const episodes: Episode[] = [];

  // Find the podcast name from slug
  const podcast = getPodcastBySlug(podcastSlug);
  if (!podcast) return [];

  // Search through all URLs to find episodes for this podcast
  for (const [url, podcastData] of Object.entries(statusData.podcasts || {})) {
    const data = podcastData as any;
    const podcastName = data.podcast_name;

    if (slugify(podcastName) !== podcastSlug) continue;

    // Get actual folders from filesystem
    const podcastDir = path.join(PODCAST_WORK_DIR, podcastName);
    if (!fs.existsSync(podcastDir)) continue;

    const folders = fs.readdirSync(podcastDir, { withFileTypes: true })
      .filter(dirent => dirent.isDirectory())
      .map(dirent => dirent.name);

    // For each folder, try to match it to an episode in the JSON
    for (const folderName of folders) {
      const episodeDir = path.join(podcastDir, folderName);
      const summaryPath = path.join(episodeDir, 'summary.md');
      const transcriptPath = path.join(episodeDir, 'transcript.md');

      const hasSummary = fs.existsSync(summaryPath);
      const hasTranscript = fs.existsSync(transcriptPath);

      // Try to extract video ID from summary file
      let videoId = '';
      let episodeTitle = folderName;
      let region = 'Western';
      let uploadDate = '';

      if (hasSummary) {
        try {
          const summaryContent = fs.readFileSync(summaryPath, 'utf-8');
          const videoIdMatch = summaryContent.match(/\*\*Video ID:\*\*\s*([^\s\n]+)/);
          if (videoIdMatch) videoId = videoIdMatch[1];

          const titleMatch = summaryContent.match(/^#\s*\[?([^\]\n]+)\]?/m);
          if (titleMatch) episodeTitle = titleMatch[1].trim();

          const regionMatch = summaryContent.match(/\*\*Region:\*\*\s*([^\n]+)/);
          if (regionMatch) region = regionMatch[1].trim();
        } catch (e) {
          console.error('Error reading summary:', e);
        }
      }

      // Try to find matching episode in JSON by video ID or folder name
      const podcastEpisodes = data.episodes || {};
      let episodeData: any = null;

      if (videoId && podcastEpisodes[videoId]) {
        episodeData = podcastEpisodes[videoId];
        uploadDate = episodeData.upload_date || episodeData.discovered_date || '';
      } else {
        // Fallback: try to match by sanitized title
        for (const [vid, ep] of Object.entries(podcastEpisodes)) {
          const epData = ep as any;
          if (sanitizeFilename(epData.title || '') === folderName) {
            videoId = vid;
            episodeData = epData;
            uploadDate = epData.upload_date || epData.discovered_date || '';
            break;
          }
        }
      }

      // Only include if we found it in the JSON or it has content files
      if (videoId && (hasSummary || hasTranscript)) {
        episodes.push({
          title: episodeTitle,
          slug: slugify(episodeTitle),
          podcastName,
          podcastSlug,
          date: formatDate(uploadDate),
          videoId: videoId || 'unknown',
          videoUrl: videoId ? `https://www.youtube.com/watch?v=${videoId}` : '',
          region,
          hasSummary,
          hasTranscript,
          summaryPath,
          transcriptPath,
        });
      }
    }
  }

  // Sort by date descending
  return episodes.sort((a, b) => {
    const dateA = new Date(a.date).getTime();
    const dateB = new Date(b.date).getTime();
    return dateB - dateA;
  });
}

export function getEpisodeBySlug(podcastSlug: string, episodeSlug: string): Episode | null {
  const episodes = getEpisodesForPodcast(podcastSlug);
  return episodes.find(e => e.slug === episodeSlug) || null;
}

function formatDate(dateStr: string): string {
  if (!dateStr) return 'Unknown';

  // Handle YYYYMMDD format from upload_date
  if (/^\d{8}$/.test(dateStr)) {
    const year = dateStr.substring(0, 4);
    const month = dateStr.substring(4, 6);
    const day = dateStr.substring(6, 8);
    return `${year}-${month}-${day}`;
  }

  // Handle discovered_date format "YYYY-MM-DD HH:MM:SS"
  if (dateStr.includes(' ')) {
    return dateStr.split(' ')[0];
  }

  return dateStr;
}

export async function generateStaticParams() {
  return getAllPodcasts().map((podcast) => ({
    name: podcast.slug,
  }));
}
