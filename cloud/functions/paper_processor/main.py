"""
Paper Processor Cloud Function
Discovers Physical AI papers from arXiv, Semantic Scholar, and HuggingFace,
scores them with Claude, summarizes the top 1-2, and pushes to git for teahose.com.
Triggered by Cloud Scheduler daily at 5 AM EST.
"""

import functions_framework
import json
import os
import re
import subprocess
import tempfile
import time
import traceback
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta, timezone
from pathlib import Path

import requests
from anthropic import Anthropic
from git import Repo

try:
    import fitz  # PyMuPDF
except ImportError:
    fitz = None


# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

ANTHROPIC_API_KEY = os.environ.get("ANTHROPIC_API_KEY")
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")
NOTIFICATION_EMAIL = os.environ.get("NOTIFICATION_EMAIL", "altmbr@gmail.com")
GITHUB_RAW_BASE = "https://raw.githubusercontent.com/altmbr/Podcast_Summarizer/main"
PAPER_LOOKBACK_DAYS = int(os.environ.get("PAPER_LOOKBACK_DAYS", "3"))

GCS_BACKUP_BUCKET = "gen-lang-client-0111593271-podscan-backups"

ARXIV_NS = {"atom": "http://www.w3.org/2005/Atom"}

PAPER_SUMMARIZATION_PROMPT = """You are summarizing a research paper for an investor and entrepreneur focused on Physical AI (robotics, embodied intelligence, autonomous systems). You are masterful at identifying signal in the noise, translating academic research into operational and strategic implications.

The audience is NOT academic reviewers — they are CTOs, heads of engineering, investors, and operators evaluating companies deploying physical AI systems. Your job is to answer: "Why should someone building or funding robots care about this paper?"

Whenever you make a point, substantiate it with a direct quote or specific finding from the paper, citing the section or page where it appears.

# Notes

1. **IMPORTANT**: Format individual insights within each section as H3 headings (###). For example: `### Scalable Dexterous Manipulation via Cross-Embodiment Transfer` followed by the description paragraph. Do NOT use bold text (**text**) for insight titles.
2. Translate academic jargon into plain language. If a paper says "we achieve 94.3% success rate on the DexGraspNet benchmark," explain what that means practically.
3. Focus on what this enables for real-world deployment, not just benchmark improvements.

## Format

### 1. Key Themes (3-5 themes)
- What did this paper actually achieve? What's the core contribution?
- Substantiate with specific results, metrics, or findings from the paper

### 2. Contrarian Perspectives (2-3 perspectives)
- What does this paper argue that challenges conventional wisdom?
- What would most robotics companies disagree with?
- Include the evidence or reasoning that supports the contrarian view

### 3. Companies Identified (all relevant companies)
- Companies referenced in the paper, whose products/platforms are used, or whose competitive position is affected
- Format: Company Name, Description, Why relevant, Quotes

### 4. People Identified (key researchers)
- Key researchers, their labs, and why they matter in the Physical AI landscape
- Format: Person Name, Lab/Institution, Why notable, Quotes

### 5. Operating Insights (1-3 insights)
- Practical takeaways for someone building or deploying physical AI systems
- What should a CTO or head of engineering pay attention to?

### 6. Overlooked Insights (1-2 insights)
- Buried findings, dataset details, or limitations that have outsized implications
- These should not duplicate anything in other sections"""


def sanitize_title(title: str) -> str:
    """Sanitize title for use as a folder name."""
    return re.sub(r'[<>:"/\\|?*]', '_', title)[:200]


def extract_arxiv_id(id_str: str) -> str:
    """Extract clean arXiv ID from full URL or ID string."""
    # Handle URLs like http://arxiv.org/abs/2503.12345v1
    if "/" in id_str:
        id_str = id_str.split("/")[-1]
    # Remove version suffix
    return re.sub(r'v\d+$', '', id_str)


# ---------------------------------------------------------------------------
# Config and status fetching
# ---------------------------------------------------------------------------

def fetch_paper_config() -> dict:
    """Fetch paper_config.json from GitHub."""
    url = f"{GITHUB_RAW_BASE}/paper_config.json"
    resp = requests.get(url, timeout=15)
    resp.raise_for_status()
    return resp.json()


def fetch_paper_status() -> dict:
    """Fetch paper_status.json from GitHub."""
    url = f"{GITHUB_RAW_BASE}/paper_status.json"
    resp = requests.get(url, timeout=15)
    if resp.status_code == 404:
        return {"papers": {}}
    resp.raise_for_status()
    return resp.json()


# ---------------------------------------------------------------------------
# Discovery: arXiv
# ---------------------------------------------------------------------------

def discover_arxiv(categories: list[str], keywords: list[str], lookback_days: int) -> list[dict]:
    """Query arXiv API for recent Physical AI papers."""
    papers = []

    # Build category query: (cat:cs.RO OR cat:cs.AI OR ...)
    cat_query = " OR ".join(f"cat:{cat}" for cat in categories)

    # Build keyword query for Physical AI relevance
    kw_query = " OR ".join(f'all:"{kw}"' for kw in keywords[:10])  # Limit to avoid URL length issues

    # Combined: papers in our categories that mention Physical AI keywords
    query = f"({cat_query}) AND ({kw_query})"

    # arXiv uses date ranges in YYYYMMDD format
    start_date = (datetime.now(timezone.utc) - timedelta(days=lookback_days)).strftime("%Y%m%d")
    end_date = datetime.now(timezone.utc).strftime("%Y%m%d")

    try:
        print(f"  Querying arXiv (categories: {categories}, lookback: {lookback_days}d)...")
        resp = requests.get(
            "http://export.arxiv.org/api/query",
            params={
                "search_query": query,
                "start": "0",
                "max_results": "100",
                "sortBy": "submittedDate",
                "sortOrder": "descending",
            },
            timeout=30,
        )
        resp.raise_for_status()
        time.sleep(3)  # arXiv ToS: 1 request per 3 seconds

        root = ET.fromstring(resp.text)

        for entry in root.findall("atom:entry", ARXIV_NS):
            arxiv_id = extract_arxiv_id(entry.findtext("atom:id", "", ARXIV_NS))
            published = entry.findtext("atom:published", "", ARXIV_NS)

            # Filter by date
            if published:
                try:
                    pub_date = datetime.fromisoformat(published.replace("Z", "+00:00"))
                    cutoff = datetime.now(timezone.utc) - timedelta(days=lookback_days)
                    if pub_date < cutoff:
                        continue
                except (ValueError, TypeError):
                    pass

            title = entry.findtext("atom:title", "", ARXIV_NS).strip().replace("\n", " ")
            abstract = entry.findtext("atom:summary", "", ARXIV_NS).strip().replace("\n", " ")

            authors = []
            for author in entry.findall("atom:author", ARXIV_NS):
                name = author.findtext("atom:name", "", ARXIV_NS)
                if name:
                    authors.append(name)

            categories_found = [
                cat.get("term", "") for cat in entry.findall("atom:category", ARXIV_NS)
            ]

            if arxiv_id and title:
                papers.append({
                    "arxiv_id": arxiv_id,
                    "title": title,
                    "authors": authors,
                    "abstract": abstract,
                    "published": published,
                    "categories": categories_found,
                    "pdf_url": f"https://arxiv.org/pdf/{arxiv_id}",
                    "sources": ["arxiv"],
                })

        print(f"  arXiv: found {len(papers)} papers")

    except Exception as e:
        print(f"  WARNING: arXiv discovery failed: {e}")
        traceback.print_exc()

    return papers


# ---------------------------------------------------------------------------
# Discovery: Semantic Scholar
# ---------------------------------------------------------------------------

def discover_semantic_scholar(seed_papers: list[str], keywords: list[str]) -> list[dict]:
    """Query Semantic Scholar for recommended and keyword-matched papers."""
    papers = []
    seen_ids = set()

    # Method 1: Recommendations from seed papers
    for seed_id in seed_papers[:5]:  # Limit seed papers to control rate
        try:
            resp = requests.get(
                f"https://api.semanticscholar.org/recommendations/v1/papers/forpaper/ArXiv:{seed_id}",
                params={"limit": "20", "fields": "externalIds,title,authors,abstract,year,citationCount,venue"},
                timeout=15,
            )
            time.sleep(1)  # Rate limit

            if resp.status_code != 200:
                continue

            for paper in resp.json().get("recommendedPapers", []):
                arxiv_id = (paper.get("externalIds") or {}).get("ArXiv")
                if not arxiv_id or arxiv_id in seen_ids:
                    continue
                seen_ids.add(arxiv_id)

                authors = [a.get("name", "") for a in (paper.get("authors") or []) if a.get("name")]

                papers.append({
                    "arxiv_id": arxiv_id,
                    "title": paper.get("title", ""),
                    "authors": authors,
                    "abstract": paper.get("abstract", "") or "",
                    "published": str(paper.get("year", "")),
                    "citation_count": paper.get("citationCount", 0),
                    "venue": paper.get("venue", ""),
                    "sources": ["semantic_scholar"],
                })

        except Exception as e:
            print(f"  WARNING: SS recommendation failed for {seed_id}: {e}")
            continue

    # Method 2: Bulk keyword search
    kw_query = " ".join(keywords[:5])
    try:
        resp = requests.get(
            "https://api.semanticscholar.org/graph/v1/paper/search",
            params={
                "query": kw_query,
                "limit": "50",
                "fields": "externalIds,title,authors,abstract,year,citationCount,venue",
                "year": f"{datetime.now().year - 1}-",
            },
            timeout=15,
        )
        time.sleep(1)

        if resp.status_code == 200:
            for paper in resp.json().get("data", []):
                arxiv_id = (paper.get("externalIds") or {}).get("ArXiv")
                if not arxiv_id or arxiv_id in seen_ids:
                    continue
                seen_ids.add(arxiv_id)

                authors = [a.get("name", "") for a in (paper.get("authors") or []) if a.get("name")]

                papers.append({
                    "arxiv_id": arxiv_id,
                    "title": paper.get("title", ""),
                    "authors": authors,
                    "abstract": paper.get("abstract", "") or "",
                    "published": str(paper.get("year", "")),
                    "citation_count": paper.get("citationCount", 0),
                    "venue": paper.get("venue", ""),
                    "sources": ["semantic_scholar"],
                })

    except Exception as e:
        print(f"  WARNING: SS keyword search failed: {e}")

    print(f"  Semantic Scholar: found {len(papers)} papers")
    return papers


# ---------------------------------------------------------------------------
# Discovery: HuggingFace Daily Papers
# ---------------------------------------------------------------------------

def discover_huggingface(keywords: list[str]) -> list[dict]:
    """Fetch HuggingFace Daily Papers and filter for Physical AI relevance."""
    papers = []
    keyword_set = set(kw.lower() for kw in keywords)

    try:
        print("  Querying HuggingFace Daily Papers...")
        resp = requests.get(
            "https://huggingface.co/api/daily_papers",
            params={"limit": "100"},
            timeout=15,
        )
        resp.raise_for_status()

        for item in resp.json():
            paper = item.get("paper", {})
            title = paper.get("title", "")
            abstract = paper.get("summary", "") or ""
            combined = (title + " " + abstract).lower()

            # Filter: must match at least one Physical AI keyword
            if not any(kw in combined for kw in keyword_set):
                continue

            arxiv_id = paper.get("id", "")
            if not arxiv_id:
                continue

            authors = [a.get("name", "") for a in paper.get("authors", []) if a.get("name")]
            upvotes = item.get("paper", {}).get("upvotes", 0)

            papers.append({
                "arxiv_id": arxiv_id,
                "title": title,
                "authors": authors,
                "abstract": abstract,
                "published": paper.get("publishedAt", ""),
                "upvotes": upvotes,
                "sources": ["huggingface"],
            })

        print(f"  HuggingFace: found {len(papers)} relevant papers")

    except Exception as e:
        print(f"  WARNING: HuggingFace discovery failed: {e}")
        traceback.print_exc()

    return papers


# ---------------------------------------------------------------------------
# Deduplication
# ---------------------------------------------------------------------------

def deduplicate_papers(arxiv_papers: list[dict], ss_papers: list[dict], hf_papers: list[dict]) -> list[dict]:
    """Deduplicate papers by arXiv ID, merging metadata and tracking source counts."""
    merged = {}

    for paper in arxiv_papers + ss_papers + hf_papers:
        arxiv_id = paper["arxiv_id"]
        if arxiv_id in merged:
            existing = merged[arxiv_id]
            # Merge sources
            for src in paper.get("sources", []):
                if src not in existing["sources"]:
                    existing["sources"].append(src)
            # Prefer longer abstract
            if len(paper.get("abstract", "")) > len(existing.get("abstract", "")):
                existing["abstract"] = paper["abstract"]
            # Merge authors if more complete
            if len(paper.get("authors", [])) > len(existing.get("authors", [])):
                existing["authors"] = paper["authors"]
            # Take citation count if available
            if paper.get("citation_count", 0) > existing.get("citation_count", 0):
                existing["citation_count"] = paper["citation_count"]
            # Take upvotes if available
            if paper.get("upvotes", 0) > 0:
                existing["upvotes"] = paper["upvotes"]
        else:
            merged[arxiv_id] = paper.copy()

    result = list(merged.values())
    print(f"  Deduplicated: {len(result)} unique papers")
    return result


# ---------------------------------------------------------------------------
# Scoring
# ---------------------------------------------------------------------------

SCORING_PROMPT = """You are an expert evaluator of Physical AI research papers. Score each paper on the following dimensions. Return ONLY valid JSON — no markdown, no explanation.

Scoring dimensions (0-10 each):
1. **relevance**: How directly does this paper advance Physical AI? (robotic manipulation, grasping, locomotion, humanoid control, sim-to-real, VLAs, world models for embodied agents, autonomous vehicles, drones, digital twins, physics simulation, tactile sensing, multi-robot systems, robot learning)
2. **novelty**: Does this introduce a genuinely new idea, method, or result — or is it incremental?
3. **impact**: How likely is this to change how companies build or deploy physical AI systems in the next 1-2 years?
4. **pedigree**: Are the authors/labs known for impactful Physical AI work? (Physical Intelligence, Google DeepMind, TRI, Berkeley, Stanford, CMU, MIT, AgiBot, NVIDIA, Skild AI, etc.)

For each paper, return scores as a JSON array:
[
  {"arxiv_id": "2503.12345", "relevance": 8, "novelty": 7, "impact": 9, "pedigree": 8},
  ...
]

Papers to evaluate:
"""


def _score_batch(batch: list[dict], client: Anthropic) -> dict:
    """Score a single batch of papers. Returns {arxiv_id: scores_dict}."""
    paper_descriptions = []
    for p in batch:
        authors_str = ", ".join(p.get("authors", [])[:5])
        desc = f"- arxiv_id: {p['arxiv_id']}\n  Title: {p['title']}\n  Authors: {authors_str}\n  Abstract: {p.get('abstract', 'N/A')[:500]}"
        paper_descriptions.append(desc)

    prompt = SCORING_PROMPT + "\n".join(paper_descriptions)

    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=8000,
        messages=[{"role": "user", "content": prompt}],
    )

    scores_text = response.content[0].text.strip()
    if scores_text.startswith("```"):
        scores_text = re.sub(r'^```\w*\n?', '', scores_text)
        scores_text = re.sub(r'\n?```$', '', scores_text)

    scores_list = json.loads(scores_text)
    return {s["arxiv_id"]: s for s in scores_list}


SCORING_BATCH_SIZE = 25


def score_papers(candidates: list[dict], config: dict) -> list[dict]:
    """Score candidate papers using Claude in batches. Returns candidates with scores added."""
    if not candidates:
        return []

    print(f"  Scoring {len(candidates)} candidates with Claude (batch size {SCORING_BATCH_SIZE})...")

    client = Anthropic(api_key=ANTHROPIC_API_KEY)
    scores_by_id = {}

    # Score in batches to avoid JSON truncation
    for i in range(0, len(candidates), SCORING_BATCH_SIZE):
        batch = candidates[i:i + SCORING_BATCH_SIZE]
        batch_num = i // SCORING_BATCH_SIZE + 1
        total_batches = (len(candidates) + SCORING_BATCH_SIZE - 1) // SCORING_BATCH_SIZE
        print(f"    Batch {batch_num}/{total_batches} ({len(batch)} papers)...")

        try:
            batch_scores = _score_batch(batch, client)
            scores_by_id.update(batch_scores)
        except Exception as e:
            print(f"    WARNING: Batch {batch_num} scoring failed: {e}")
            traceback.print_exc()
            continue

    if not scores_by_id:
        print("  WARNING: All scoring batches failed")
        return []

    # Calculate composite scores
    scoring_config = config.get("scoring", {})
    w_rel = scoring_config.get("relevance_weight", 3)
    w_nov = scoring_config.get("novelty_weight", 2)
    w_imp = scoring_config.get("impact_weight", 3)
    w_ped = scoring_config.get("pedigree_weight", 2)
    w_multi = scoring_config.get("multisource_weight", 1)

    scored = []
    for paper in candidates:
        arxiv_id = paper["arxiv_id"]
        s = scores_by_id.get(arxiv_id)
        if not s:
            continue

        # Multi-source score: 0-3 based on source count and HF upvotes
        source_count = len(paper.get("sources", []))
        hf_upvotes = paper.get("upvotes", 0)
        if source_count >= 3 and hf_upvotes >= 10:
            multi_source = 3
        elif source_count >= 3:
            multi_source = 2
        elif source_count >= 2:
            multi_source = 1
        else:
            multi_source = 0

        composite = (
            s.get("relevance", 0) * w_rel
            + s.get("novelty", 0) * w_nov
            + s.get("impact", 0) * w_imp
            + s.get("pedigree", 0) * w_ped
            + multi_source * w_multi
        )

        paper["scores"] = {
            "relevance": s.get("relevance", 0),
            "novelty": s.get("novelty", 0),
            "impact": s.get("impact", 0),
            "pedigree": s.get("pedigree", 0),
            "multi_source": multi_source,
            "composite": composite,
        }
        scored.append(paper)

    scored.sort(key=lambda p: p["scores"]["composite"], reverse=True)
    print(f"  Scored {len(scored)} papers (top score: {scored[0]['scores']['composite'] if scored else 0})")
    return scored


def select_papers(scored: list[dict], config: dict, status: dict) -> tuple[list[dict], list[dict]]:
    """Select top papers above threshold. Returns (selected, runners_up)."""
    scoring_config = config.get("scoring", {})
    min_score = scoring_config.get("minimum_score", 60)
    max_per_day = scoring_config.get("max_papers_per_day", 2)

    # Filter already processed
    processed_ids = set(status.get("papers", {}).keys())
    qualifying = [
        p for p in scored
        if p["scores"]["composite"] >= min_score and p["arxiv_id"] not in processed_ids
    ]

    selected = qualifying[:max_per_day]
    runners_up = qualifying[max_per_day:max_per_day + 5]

    print(f"  Selection: {len(qualifying)} qualifying, {len(selected)} selected, {len(runners_up)} runners-up")
    for p in selected:
        print(f"    SELECTED: [{p['scores']['composite']:.0f}] {p['title'][:80]}")
    for p in runners_up:
        print(f"    RUNNER-UP: [{p['scores']['composite']:.0f}] {p['title'][:80]}")

    return selected, runners_up


# ---------------------------------------------------------------------------
# PDF fetching and text extraction
# ---------------------------------------------------------------------------

def fetch_paper_text(arxiv_id: str, abstract: str) -> str:
    """Fetch and extract text from arXiv PDF. Falls back to abstract."""
    try:
        print(f"  Fetching PDF for {arxiv_id}...")
        pdf_url = f"https://arxiv.org/pdf/{arxiv_id}"
        resp = requests.get(pdf_url, timeout=60)
        resp.raise_for_status()
        time.sleep(3)  # arXiv rate limit

        if fitz is None:
            raise ImportError("PyMuPDF not installed")
        doc = fitz.open(stream=resp.content, filetype="pdf")
        text_parts = []
        for page in doc:
            text_parts.append(page.get_text())
        doc.close()

        full_text = "\n".join(text_parts)
        if len(full_text.strip()) > 500:
            print(f"  Extracted {len(full_text)} chars from PDF ({doc.page_count} pages)")
            return full_text[:100000]  # Cap at 100K chars

    except Exception as e:
        print(f"  WARNING: PDF extraction failed for {arxiv_id}: {e}")

    # Fallback: try HTML version
    try:
        html_url = f"https://arxiv.org/html/{arxiv_id}"
        resp = requests.get(html_url, timeout=30)
        time.sleep(3)
        if resp.status_code == 200 and len(resp.text) > 1000:
            # Simple HTML text extraction
            text = re.sub(r'<[^>]+>', ' ', resp.text)
            text = re.sub(r'\s+', ' ', text).strip()
            if len(text) > 500:
                print(f"  Extracted {len(text)} chars from HTML fallback")
                return text[:100000]
    except Exception as e:
        print(f"  WARNING: HTML fallback also failed: {e}")

    # Final fallback: abstract only
    print(f"  Using abstract only for {arxiv_id}")
    return f"Abstract:\n{abstract}"


# ---------------------------------------------------------------------------
# Metadata enrichment
# ---------------------------------------------------------------------------

def enrich_with_semantic_scholar(arxiv_id: str) -> dict:
    """Fetch additional metadata from Semantic Scholar."""
    try:
        resp = requests.get(
            f"https://api.semanticscholar.org/graph/v1/paper/ArXiv:{arxiv_id}",
            params={"fields": "authors.name,authors.affiliations,citationCount,venue"},
            timeout=15,
        )
        time.sleep(1)

        if resp.status_code != 200:
            return {}

        data = resp.json()
        affiliations = set()
        for author in data.get("authors", []):
            for aff in (author.get("affiliations") or []):
                if aff:
                    affiliations.add(aff)

        return {
            "affiliations": list(affiliations),
            "citation_count": data.get("citationCount", 0),
            "venue": data.get("venue", ""),
        }

    except Exception as e:
        print(f"  WARNING: SS enrichment failed for {arxiv_id}: {e}")
        return {}


def _lab_matches(lab: str, text: str) -> bool:
    """Check if lab name appears as a whole word/phrase in text."""
    return bool(re.search(r'\b' + re.escape(lab) + r'\b', text, re.IGNORECASE))


def resolve_institution(paper: dict, enrichment: dict, tracked_labs: list[str]) -> str:
    """Resolve the primary institution/lab for a paper."""
    affiliations = enrichment.get("affiliations", [])

    # Check affiliations against tracked labs (word-boundary match)
    for aff in affiliations:
        for lab in tracked_labs:
            if _lab_matches(lab, aff):
                return lab

    # Use first affiliation if available (more reliable than abstract guessing)
    if affiliations:
        # Still try to clean it up against tracked labs with looser matching
        first_aff = affiliations[0]
        for lab in tracked_labs:
            if lab.lower() in first_aff.lower():
                return lab
        return first_aff

    return "arXiv Physical AI"


# ---------------------------------------------------------------------------
# Summarization
# ---------------------------------------------------------------------------

def summarize_paper(
    paper_text: str,
    title: str,
    authors: list[str],
    institution: str,
    abstract: str,
    arxiv_id: str,
    published: str,
) -> str:
    """Summarize paper with Claude and format with metadata header."""
    print("  Summarizing with Claude Sonnet...")

    client = Anthropic(api_key=ANTHROPIC_API_KEY)

    authors_str = ", ".join(authors[:10])
    if len(authors) > 10:
        authors_str += f", et al. ({len(authors)} total)"

    prompt = f"""{PAPER_SUMMARIZATION_PROMPT}

Paper: {title}
Authors: {authors_str}
Institution: {institution}
Abstract: {abstract}

Full Paper Text:
{paper_text[:100000]}"""

    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=16000,
        messages=[{"role": "user", "content": prompt}],
    )

    summary_content = response.content[0].text

    # Format date
    try:
        dt = datetime.fromisoformat(published.replace("Z", "+00:00"))
        date_formatted = dt.strftime("%Y-%m-%d")
    except (ValueError, TypeError):
        date_formatted = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    processed_at = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    # Format participants
    if len(authors) <= 3:
        participants = ", ".join(authors)
    else:
        participants = f"{authors[0]}, {authors[-1]}, et al. ({institution})"

    header = f"""# {title}

**Podcast:** {institution} Research
**Date:** {date_formatted}
**Processed:** {processed_at}
**Participants:** {participants}
**Source:** paper
**arXiv:** {arxiv_id}
**PDF:** https://arxiv.org/pdf/{arxiv_id}

---

"""

    result = header + summary_content
    print(f"  Summary generated ({len(summary_content)} chars)")
    return result


# ---------------------------------------------------------------------------
# Git operations (mirrored from newsletter_processor)
# ---------------------------------------------------------------------------

def verify_github_auth():
    """Verify GitHub token has push access."""
    print("Verifying GitHub auth...")
    result = subprocess.run(
        ["git", "ls-remote", f"https://{GITHUB_TOKEN}@github.com/altmbr/Podcast_Summarizer.git", "HEAD"],
        capture_output=True, text=True, timeout=15,
    )
    if result.returncode != 0:
        raise RuntimeError(f"GitHub auth failed: {result.stderr.strip()}")
    print("  GitHub auth verified")


def clone_repo(work_dir: Path) -> Repo:
    """Clone the repository."""
    repo_path = work_dir / "repo"
    auth_url = f"https://{GITHUB_TOKEN}@github.com/altmbr/Podcast_Summarizer.git"
    print("Cloning repository...")
    repo = Repo.clone_from(auth_url, repo_path)
    repo.config_writer().set_value("user", "name", "Paper Processor").release()
    repo.config_writer().set_value("user", "email", "papers@teahose.com").release()
    print("  Repository cloned")
    return repo


def backup_to_gcs(repo: Repo):
    """Save a git bundle to GCS if push fails."""
    try:
        from google.cloud import storage
        bundle_path = Path(repo.working_dir).parent / "backup.bundle"
        repo.git.bundle("create", str(bundle_path), "--all")
        client = storage.Client()
        bucket = client.bucket(GCS_BACKUP_BUCKET)
        timestamp = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
        blob = bucket.blob(f"bundles/paper_{timestamp}.bundle")
        blob.upload_from_filename(str(bundle_path))
        print(f"  Backup saved to gs://{GCS_BACKUP_BUCKET}/{blob.name}")
    except Exception as e:
        print(f"  WARNING: Backup to GCS also failed: {e}")


def commit_and_push(repo: Repo, papers: list[dict]):
    """Commit and push. Backs up to GCS if push fails."""
    repo.git.add(A=True)

    if not repo.index.diff("HEAD") and not repo.untracked_files:
        print("No changes to commit")
        return

    titles = [p["title"][:80] for p in papers]
    commit_msg = f"Add {len(titles)} paper summary(ies)\n\n"
    commit_msg += "\n".join(f"- {t}" for t in titles)
    commit_msg += "\n\n🤖 Generated with Paper Processor"

    repo.index.commit(commit_msg)
    print("  Changes committed")

    try:
        origin = repo.remote("origin")
        origin.push()
        print("  Pushed to GitHub")
    except Exception as e:
        print(f"  ERROR: Push failed: {e}")
        print("  Saving backup to GCS...")
        backup_to_gcs(repo)
        raise


# ---------------------------------------------------------------------------
# Status tracking
# ---------------------------------------------------------------------------

def update_paper_status(repo: Repo, status: dict, arxiv_id: str, title: str, institution: str, score: float):
    """Update paper_status.json in the repo."""
    status.setdefault("papers", {})[arxiv_id] = {
        "title": title,
        "institution": institution,
        "status": "summarized",
        "score": round(score, 1),
        "processed_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
    }

    status_path = Path(repo.working_dir) / "paper_status.json"
    status_path.write_text(json.dumps(status, indent=2, ensure_ascii=False), encoding="utf-8")


# ---------------------------------------------------------------------------
# Notification
# ---------------------------------------------------------------------------

def send_processing_report(
    selected: list[dict],
    runners_up: list[dict],
    failed: list[dict],
    source_stats: dict,
    total_candidates: int,
):
    """Send processing report via AWS SES."""
    aws_key = os.environ.get("AWS_ACCESS_KEY_ID")
    aws_secret = os.environ.get("AWS_SECRET_ACCESS_KEY")
    if not aws_key or not aws_secret:
        print("WARNING: No AWS credentials — report NOT sent")
        return

    html_parts = [
        "<html><body>",
        "<h2>Paper Processor Report</h2>",
        f"<p>Discovered {total_candidates} candidates across sources</p>",
        "<h3>Source breakdown:</h3><ul>",
    ]
    for source, count in source_stats.items():
        html_parts.append(f"<li>{source}: {count} papers</li>")
    html_parts.append("</ul>")

    if selected:
        html_parts.append(f"<h3>Selected ({len(selected)}):</h3><ul>")
        for p in selected:
            score = p.get("scores", {}).get("composite", 0)
            html_parts.append(
                f"<li><strong>[{score:.0f}]</strong> {p['title'][:100]}"
                f"<br/><small>arXiv: {p['arxiv_id']}</small></li>"
            )
        html_parts.append("</ul>")

    if runners_up:
        html_parts.append(f"<h3>Runners-up ({len(runners_up)}):</h3><ul>")
        for p in runners_up:
            score = p.get("scores", {}).get("composite", 0)
            html_parts.append(f"<li><strong>[{score:.0f}]</strong> {p['title'][:100]}</li>")
        html_parts.append("</ul>")

    if failed:
        html_parts.append(f"<h3>Failed ({len(failed)}):</h3><ul>")
        for f_item in failed:
            html_parts.append(f"<li>{f_item['title'][:80]}: {f_item.get('error', '?')}</li>")
        html_parts.append("</ul>")

    html_parts.append("</body></html>")

    subject = f"Papers: {len(selected)} published"
    if failed:
        subject += f", {len(failed)} failed"

    try:
        import boto3
        ses = boto3.client("ses", region_name="us-west-2",
                           aws_access_key_id=aws_key, aws_secret_access_key=aws_secret)
        ses.send_email(
            Source="Paper Processor <papers@teahose.com>",
            Destination={"ToAddresses": [NOTIFICATION_EMAIL]},
            Message={
                "Subject": {"Data": subject},
                "Body": {"Html": {"Data": "\n".join(html_parts)}},
            },
        )
    except Exception as e:
        print(f"Failed to send report email: {e}")


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

@functions_framework.http
def paper_processor(request):
    """HTTP entry point triggered by Cloud Scheduler."""
    print("Paper processor triggered")

    # Allow dry-run via query param
    dry_run = False
    if request:
        dry_run = request.args.get("dry_run", "false").lower() == "true"

    if not ANTHROPIC_API_KEY:
        return {"status": "error", "message": "ANTHROPIC_API_KEY not set"}, 500
    if not GITHUB_TOKEN and not dry_run:
        return {"status": "error", "message": "GITHUB_TOKEN not set"}, 500

    try:
        # Fetch config and status
        config = fetch_paper_config()
        status = fetch_paper_status()

        # Verify GitHub auth before doing any expensive work
        if not dry_run:
            verify_github_auth()

        # ---- Discovery ----
        print("\n=== Discovery Phase ===")
        categories = config.get("arxiv_categories", ["cs.RO", "cs.AI"])
        keywords = config.get("physical_ai_keywords", ["robot"])
        seed_papers = config.get("seed_papers", [])

        arxiv_papers = discover_arxiv(categories, keywords, PAPER_LOOKBACK_DAYS)
        ss_papers = discover_semantic_scholar(seed_papers, keywords)
        hf_papers = discover_huggingface(keywords)

        source_stats = {
            "arXiv": len(arxiv_papers),
            "Semantic Scholar": len(ss_papers),
            "HuggingFace": len(hf_papers),
        }

        # Deduplicate
        candidates = deduplicate_papers(arxiv_papers, ss_papers, hf_papers)
        total_candidates = len(candidates)

        if not candidates:
            print("No candidates found")
            send_processing_report([], [], [], source_stats, 0)
            return {"status": "ok", "message": "No candidates found", "count": 0}

        # ---- Scoring ----
        print("\n=== Scoring Phase ===")
        scored = score_papers(candidates, config)

        # ---- Selection ----
        print("\n=== Selection Phase ===")
        selected, runners_up = select_papers(scored, config, status)

        if not selected:
            print("No papers met the quality threshold")
            send_processing_report([], runners_up, [], source_stats, total_candidates)
            return {"status": "ok", "message": "No papers above threshold", "count": 0,
                    "total_candidates": total_candidates}

        # ---- Processing ----
        print(f"\n=== Processing {len(selected)} paper(s) ===")

        with tempfile.TemporaryDirectory() as work_dir:
            work_path = Path(work_dir)

            if not dry_run:
                repo = clone_repo(work_path)
            else:
                repo_path = work_path / "repo"
                repo_path.mkdir(parents=True)
                repo = Repo.init(repo_path)
                (repo_path / "podcast_work").mkdir()

            tracked_labs = config.get("tracked_labs", [])
            processed = []
            failed = []

            for paper in selected:
                try:
                    arxiv_id = paper["arxiv_id"]
                    title = paper["title"]

                    print(f"\n{'='*60}")
                    print(f"Processing: {title}")
                    print(f"arXiv: {arxiv_id}")
                    print(f"{'='*60}")

                    # Fetch full text
                    paper_text = fetch_paper_text(arxiv_id, paper.get("abstract", ""))

                    # Enrich metadata
                    enrichment = enrich_with_semantic_scholar(arxiv_id)
                    institution = resolve_institution(paper, enrichment, tracked_labs)
                    print(f"  Institution: {institution}")

                    # Summarize
                    summary = summarize_paper(
                        paper_text, title, paper.get("authors", []),
                        institution, paper.get("abstract", ""),
                        arxiv_id, paper.get("published", ""),
                    )

                    # Write files
                    sanitized = sanitize_title(title)
                    source_name = f"{institution} Research" if institution != "arXiv Physical AI" else institution
                    episode_dir = Path(repo.working_dir) / "podcast_work" / source_name / sanitized
                    episode_dir.mkdir(parents=True, exist_ok=True)
                    (episode_dir / "summary.md").write_text(summary, encoding="utf-8")
                    print(f"  Wrote to podcast_work/{source_name}/{sanitized}")

                    # Update status
                    update_paper_status(
                        repo, status, arxiv_id, title, institution,
                        paper["scores"]["composite"],
                    )

                    processed.append(paper)

                except Exception as e:
                    print(f"  Error processing paper: {e}")
                    traceback.print_exc()
                    paper["error"] = str(e)
                    failed.append(paper)

            # Commit and push
            if processed and not dry_run:
                commit_and_push(repo, processed)

            # Send report
            send_processing_report(processed, runners_up, failed, source_stats, total_candidates)

            result = {
                "status": "ok",
                "processed": len(processed),
                "failed": len(failed),
                "dry_run": dry_run,
                "total_candidates": total_candidates,
                "papers": [
                    {"title": p["title"], "arxiv_id": p["arxiv_id"], "score": p["scores"]["composite"]}
                    for p in processed
                ],
            }

            if failed:
                result["errors"] = [
                    {"title": p["title"], "error": p.get("error", "Unknown")}
                    for p in failed
                ]

            print(f"\nDone: {len(processed)} processed, {len(failed)} failed")
            return result

    except Exception as e:
        print(f"Fatal error: {e}")
        traceback.print_exc()
        return {"status": "error", "message": str(e)}, 500
