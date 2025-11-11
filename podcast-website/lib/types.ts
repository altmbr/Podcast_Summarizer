export interface Podcast {
  name: string;
  slug: string;
  coverImage?: string;
  episodeCount: number;
  transcribedCount: number;
  summarizedCount: number;
  participants?: string[];
  hosts?: string[];
}

export interface Episode {
  title: string;
  slug: string;
  podcastName: string;
  podcastSlug: string;
  date: string;
  videoId: string;
  videoUrl: string;
  region: string;
  participants?: string[];
  hasTranscript: boolean;
  hasSummary: boolean;
  summaryPath: string;
  transcriptPath: string;
}

export interface EpisodeContent {
  metadata: {
    title: string;
    podcast: string;
    date: string;
    participants?: string;
    region: string;
    videoId: string;
    videoUrl: string;
  };
  content: string;
}
