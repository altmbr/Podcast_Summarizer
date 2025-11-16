import fs from 'fs';
import matter from 'gray-matter';
import { EpisodeContent } from './types';

export function parseMarkdownFile(filePath: string): EpisodeContent | null {
  try {
    const fileContent = fs.readFileSync(filePath, 'utf-8');

    // Parse frontmatter if it exists
    const { data, content } = matter(fileContent);

    // Extract metadata from the markdown header
    const metadata = extractMetadataFromContent(content);

    return {
      metadata: {
        ...metadata,
        ...data, // Override with frontmatter if present
      },
      content,
    };
  } catch (error) {
    console.error('Error reading markdown file:', filePath, error);
    return null;
  }
}

function extractMetadataFromContent(content: string): any {
  const metadata: any = {};

  // Extract title from # heading or **Podcast:** format
  const titleMatch = content.match(/^#\s*\[?([^\]\n]+)\]?/m);
  if (titleMatch) {
    metadata.title = titleMatch[1].trim();
  }

  // Extract fields from **Field:** format
  const podcastMatch = content.match(/\*\*Podcast:\*\*\s*([^\n]+)/);
  if (podcastMatch) metadata.podcast = podcastMatch[1].trim();

  const dateMatch = content.match(/\*\*Date:\*\*\s*([^\n]+)/);
  if (dateMatch) metadata.date = dateMatch[1].trim();

  const participantsMatch = content.match(/\*\*Participants:\*\*\s*([^\n]+)/);
  if (participantsMatch) metadata.participants = participantsMatch[1].trim();

  const regionMatch = content.match(/\*\*Region:\*\*\s*([^\n]+)/);
  if (regionMatch) metadata.region = regionMatch[1].trim();

  const videoIdMatch = content.match(/\*\*Video ID:\*\*\s*([^\n]+)/);
  if (videoIdMatch) metadata.videoId = videoIdMatch[1].trim();

  const videoUrlMatch = content.match(/\*\*Video URL:\*\*\s*([^\n]+)/);
  if (videoUrlMatch) metadata.videoUrl = videoUrlMatch[1].trim();

  return metadata;
}

export function getMarkdownContent(filePath: string): string {
  try {
    return fs.readFileSync(filePath, 'utf-8');
  } catch (error) {
    console.error('Error reading file:', filePath, error);
    return '';
  }
}

export function splitMetadataFromContent(markdown: string): { metadata: any; content: string } {
  // Split by --- separator
  const parts = markdown.split(/^---$/m);

  if (parts.length < 2) {
    // No separator found, return empty metadata
    return { metadata: {}, content: markdown };
  }

  const metadataSection = parts[0];
  const contentSection = parts.slice(1).join('---').trim();

  // Extract metadata from the header section
  const metadata: any = {};

  // Extract title from # heading
  const titleMatch = metadataSection.match(/^#\s*\[?([^\]\n]+)\]?/m);
  if (titleMatch) {
    metadata.title = titleMatch[1].trim();
  }

  // Extract fields from **Field:** format
  const podcastMatch = metadataSection.match(/\*\*Podcast:\*\*\s*([^\n]+)/);
  if (podcastMatch) metadata.podcast = podcastMatch[1].trim();

  const dateMatch = metadataSection.match(/\*\*Date:\*\*\s*([^\n]+)/);
  if (dateMatch) metadata.date = dateMatch[1].trim();

  const participantsMatch = metadataSection.match(/\*\*Participants:\*\*\s*([^\n]+)/);
  if (participantsMatch) metadata.participants = participantsMatch[1].trim();

  const regionMatch = metadataSection.match(/\*\*Region:\*\*\s*([^\n]+)/);
  if (regionMatch) metadata.region = regionMatch[1].trim();

  const videoIdMatch = metadataSection.match(/\*\*Video ID:\*\*\s*([^\n]+)/);
  if (videoIdMatch) metadata.videoId = videoIdMatch[1].trim();

  const videoUrlMatch = metadataSection.match(/\*\*Video URL:\*\*\s*([^\n]+)/);
  if (videoUrlMatch) metadata.videoUrl = videoUrlMatch[1].trim();

  return { metadata, content: contentSection };
}
