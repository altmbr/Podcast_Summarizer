import fs from 'fs';
import matter from 'gray-matter';
import { EpisodeContent } from './types';

/**
 * Extract metadata fields from markdown content using **Field:** format.
 * Single source of truth for metadata extraction patterns.
 */
function extractMetadataFromContent(content: string): any {
  const metadata: any = {};

  const titleMatch = content.match(/^#\s*\[?([^\]\n]+)\]?/m);
  if (titleMatch) metadata.title = titleMatch[1].trim();

  const fieldPatterns: Record<string, RegExp> = {
    podcast: /\*\*Podcast:\*\*\s*([^\n]+)/,
    date: /\*\*Date:\*\*\s*([^\n]+)/,
    participants: /\*\*Participants:\*\*\s*([^\n]+)/,
    region: /\*\*Region:\*\*\s*([^\n]+)/,
    videoId: /\*\*Video ID:\*\*\s*([^\n]+)/,
    videoUrl: /\*\*Video URL:\*\*\s*([^\n]+)/,
  };

  for (const [key, pattern] of Object.entries(fieldPatterns)) {
    const match = content.match(pattern);
    if (match) metadata[key] = match[1].trim();
  }

  return metadata;
}

export function parseMarkdownFile(filePath: string): EpisodeContent | null {
  try {
    const fileContent = fs.readFileSync(filePath, 'utf-8');

    const { data, content } = matter(fileContent);
    const metadata = extractMetadataFromContent(content);

    return {
      metadata: {
        ...metadata,
        ...data,
      },
      content,
    };
  } catch (error) {
    console.error('Error reading markdown file:', filePath, error);
    return null;
  }
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
  const parts = markdown.split(/^---$/m);

  if (parts.length < 2) {
    return { metadata: {}, content: markdown };
  }

  const metadataSection = parts[0];
  const contentSection = parts.slice(1).join('---').trim();
  const metadata = extractMetadataFromContent(metadataSection);

  return { metadata, content: contentSection };
}
