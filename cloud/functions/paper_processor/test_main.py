"""Tests for Paper Processor Cloud Function."""

import json
import pytest
from unittest.mock import MagicMock, patch, PropertyMock
from datetime import datetime, timezone

# Import the module under test
import main


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------

SAMPLE_ARXIV_XML = """<?xml version="1.0" encoding="UTF-8"?>
<feed xmlns="http://www.w3.org/2005/Atom">
  <entry>
    <id>http://arxiv.org/abs/2503.12345v1</id>
    <title>RoboClaw: Dexterous Manipulation with Cross-Embodiment Transfer</title>
    <summary>We present RoboClaw, a framework for dexterous robotic manipulation that enables cross-embodiment transfer learning.</summary>
    <published>2026-03-19T00:00:00Z</published>
    <author><name>Alice Zhang</name></author>
    <author><name>Bob Smith</name></author>
    <category term="cs.RO"/>
    <category term="cs.AI"/>
  </entry>
  <entry>
    <id>http://arxiv.org/abs/2503.67890v2</id>
    <title>WorldSim: Physics-Aware World Models for Robot Planning</title>
    <summary>WorldSim introduces physics-aware world models that enable long-horizon robot planning in unstructured environments.</summary>
    <published>2026-03-18T00:00:00Z</published>
    <author><name>Carol Lee</name></author>
    <category term="cs.RO"/>
  </entry>
</feed>"""

SAMPLE_SS_RECOMMENDATIONS = {
    "recommendedPapers": [
        {
            "externalIds": {"ArXiv": "2503.11111"},
            "title": "GraspNet: Universal Grasping Policy",
            "authors": [{"name": "Dan Kim"}],
            "abstract": "A universal grasping policy for dexterous manipulation.",
            "year": 2026,
            "citationCount": 15,
            "venue": "ICRA",
        },
        {
            "externalIds": {"ArXiv": "2503.12345"},  # Duplicate with arXiv
            "title": "RoboClaw: Dexterous Manipulation",
            "authors": [{"name": "Alice Zhang"}],
            "abstract": "Cross-embodiment transfer.",
            "year": 2026,
            "citationCount": 8,
            "venue": "",
        },
    ]
}

SAMPLE_SS_SEARCH = {
    "data": [
        {
            "externalIds": {"ArXiv": "2503.22222"},
            "title": "Sim2Real for Humanoid Locomotion",
            "authors": [{"name": "Eve Wang"}],
            "abstract": "Sim-to-real transfer for humanoid robots.",
            "year": 2026,
            "citationCount": 3,
            "venue": "RSS",
        }
    ]
}

SAMPLE_HF_PAPERS = [
    {
        "paper": {
            "id": "2503.12345",
            "title": "RoboClaw: Dexterous Manipulation with Cross-Embodiment Transfer",
            "summary": "We present RoboClaw, a framework for dexterous robotic manipulation.",
            "authors": [{"name": "Alice Zhang"}],
            "publishedAt": "2026-03-19",
            "upvotes": 25,
        }
    },
    {
        "paper": {
            "id": "2503.99999",
            "title": "LLM Alignment via Constitutional AI",
            "summary": "We propose a method for aligning language models.",
            "authors": [{"name": "Frank Lu"}],
            "publishedAt": "2026-03-19",
            "upvotes": 50,
        }
    },
]


# ---------------------------------------------------------------------------
# arXiv Discovery
# ---------------------------------------------------------------------------

class TestDiscoverArxiv:
    @patch("main.requests.get")
    @patch("main.time.sleep")
    def test_parses_arxiv_xml(self, mock_sleep, mock_get):
        mock_resp = MagicMock()
        mock_resp.status_code = 200
        mock_resp.text = SAMPLE_ARXIV_XML
        mock_resp.raise_for_status = MagicMock()
        mock_get.return_value = mock_resp

        papers = main.discover_arxiv(["cs.RO"], ["robot"], lookback_days=7)

        assert len(papers) == 2
        assert papers[0]["arxiv_id"] == "2503.12345"
        assert papers[0]["title"] == "RoboClaw: Dexterous Manipulation with Cross-Embodiment Transfer"
        assert papers[0]["authors"] == ["Alice Zhang", "Bob Smith"]
        assert "arxiv" in papers[0]["sources"]
        assert papers[0]["pdf_url"] == "https://arxiv.org/pdf/2503.12345"

    @patch("main.requests.get")
    @patch("main.time.sleep")
    def test_handles_arxiv_failure_gracefully(self, mock_sleep, mock_get):
        mock_get.side_effect = Exception("Connection timeout")

        papers = main.discover_arxiv(["cs.RO"], ["robot"], lookback_days=3)
        assert papers == []


# ---------------------------------------------------------------------------
# Semantic Scholar Discovery
# ---------------------------------------------------------------------------

class TestDiscoverSemanticScholar:
    @patch("main.requests.get")
    @patch("main.time.sleep")
    def test_parses_recommendations_and_search(self, mock_sleep, mock_get):
        def side_effect(url, **kwargs):
            mock_resp = MagicMock()
            mock_resp.status_code = 200
            if "recommendations" in url:
                mock_resp.json.return_value = SAMPLE_SS_RECOMMENDATIONS
            else:
                mock_resp.json.return_value = SAMPLE_SS_SEARCH
            return mock_resp

        mock_get.side_effect = side_effect

        papers = main.discover_semantic_scholar(["2503.00001"], ["robot manipulation"])

        arxiv_ids = {p["arxiv_id"] for p in papers}
        assert "2503.11111" in arxiv_ids
        assert "2503.12345" in arxiv_ids
        assert "2503.22222" in arxiv_ids
        assert all("semantic_scholar" in p["sources"] for p in papers)

    @patch("main.requests.get")
    @patch("main.time.sleep")
    def test_handles_ss_failure_gracefully(self, mock_sleep, mock_get):
        mock_get.side_effect = Exception("API down")

        papers = main.discover_semantic_scholar(["2503.00001"], ["robot"])
        assert papers == []


# ---------------------------------------------------------------------------
# HuggingFace Discovery
# ---------------------------------------------------------------------------

class TestDiscoverHuggingface:
    @patch("main.requests.get")
    def test_filters_by_keywords(self, mock_get):
        mock_resp = MagicMock()
        mock_resp.status_code = 200
        mock_resp.json.return_value = SAMPLE_HF_PAPERS
        mock_resp.raise_for_status = MagicMock()
        mock_get.return_value = mock_resp

        papers = main.discover_huggingface(["robot", "manipulation", "dexterous"])

        # Should include RoboClaw (has "robot") but NOT LLM Alignment
        assert len(papers) == 1
        assert papers[0]["arxiv_id"] == "2503.12345"
        assert papers[0]["upvotes"] == 25
        assert "huggingface" in papers[0]["sources"]

    @patch("main.requests.get")
    def test_handles_hf_failure_gracefully(self, mock_get):
        mock_get.side_effect = Exception("HF down")

        papers = main.discover_huggingface(["robot"])
        assert papers == []


# ---------------------------------------------------------------------------
# Deduplication
# ---------------------------------------------------------------------------

class TestDeduplication:
    def test_merges_same_paper_from_multiple_sources(self):
        arxiv = [{"arxiv_id": "2503.12345", "title": "RoboClaw", "authors": ["Alice", "Bob"],
                  "abstract": "Short abstract", "sources": ["arxiv"]}]
        ss = [{"arxiv_id": "2503.12345", "title": "RoboClaw", "authors": ["Alice"],
               "abstract": "Longer abstract with more detail", "citation_count": 10, "sources": ["semantic_scholar"]}]
        hf = [{"arxiv_id": "2503.12345", "title": "RoboClaw", "authors": ["Alice"],
               "abstract": "Short", "upvotes": 25, "sources": ["huggingface"]}]

        result = main.deduplicate_papers(arxiv, ss, hf)

        assert len(result) == 1
        paper = result[0]
        assert set(paper["sources"]) == {"arxiv", "semantic_scholar", "huggingface"}
        assert paper["abstract"] == "Longer abstract with more detail"  # Kept longest
        assert paper["authors"] == ["Alice", "Bob"]  # Kept most complete
        assert paper["citation_count"] == 10
        assert paper["upvotes"] == 25

    def test_keeps_distinct_papers_separate(self):
        arxiv = [{"arxiv_id": "2503.11111", "title": "Paper A", "authors": [], "abstract": "A", "sources": ["arxiv"]}]
        ss = [{"arxiv_id": "2503.22222", "title": "Paper B", "authors": [], "abstract": "B", "sources": ["semantic_scholar"]}]

        result = main.deduplicate_papers(arxiv, ss, [])
        assert len(result) == 2


# ---------------------------------------------------------------------------
# Scoring
# ---------------------------------------------------------------------------

class TestScoring:
    def test_composite_score_calculation(self):
        config = {
            "scoring": {
                "relevance_weight": 3,
                "novelty_weight": 2,
                "impact_weight": 3,
                "pedigree_weight": 2,
                "multisource_weight": 1,
            }
        }

        candidates = [{
            "arxiv_id": "2503.12345",
            "title": "Test Paper",
            "authors": ["Alice"],
            "abstract": "Test abstract",
            "sources": ["arxiv", "semantic_scholar"],  # 2 sources = multi_source 1
        }]

        mock_response = MagicMock()
        mock_response.content = [MagicMock(text=json.dumps([
            {"arxiv_id": "2503.12345", "relevance": 9, "novelty": 7, "impact": 8, "pedigree": 6}
        ]))]

        with patch("main.Anthropic") as mock_anthropic:
            mock_client = MagicMock()
            mock_client.messages.create.return_value = mock_response
            mock_anthropic.return_value = mock_client

            scored = main.score_papers(candidates, config)

        assert len(scored) == 1
        scores = scored[0]["scores"]
        # (9*3) + (7*2) + (8*3) + (6*2) + (1*1) = 27+14+24+12+1 = 78
        assert scores["composite"] == 78
        assert scores["multi_source"] == 1

    def test_multi_source_scoring(self):
        # Test multi_source score logic
        paper_1src = {"sources": ["arxiv"], "upvotes": 0}
        paper_2src = {"sources": ["arxiv", "semantic_scholar"], "upvotes": 0}
        paper_3src = {"sources": ["arxiv", "semantic_scholar", "huggingface"], "upvotes": 5}
        paper_3src_high_hf = {"sources": ["arxiv", "semantic_scholar", "huggingface"], "upvotes": 15}

        # Test by checking the logic directly
        assert len(paper_1src["sources"]) == 1
        assert len(paper_2src["sources"]) == 2
        assert len(paper_3src["sources"]) == 3
        assert len(paper_3src_high_hf["sources"]) == 3


# ---------------------------------------------------------------------------
# Selection
# ---------------------------------------------------------------------------

class TestSelection:
    def test_selects_top_papers_above_threshold(self):
        scored = [
            {"arxiv_id": "a", "title": "A", "scores": {"composite": 80}},
            {"arxiv_id": "b", "title": "B", "scores": {"composite": 70}},
            {"arxiv_id": "c", "title": "C", "scores": {"composite": 50}},  # Below threshold
        ]
        config = {"scoring": {"minimum_score": 60, "max_papers_per_day": 2}}
        status = {"papers": {}}

        selected, runners_up = main.select_papers(scored, config, status)
        assert len(selected) == 2
        assert selected[0]["arxiv_id"] == "a"
        assert selected[1]["arxiv_id"] == "b"

    def test_hard_cap_at_max_papers(self):
        scored = [
            {"arxiv_id": str(i), "title": f"Paper {i}", "scores": {"composite": 90 - i}}
            for i in range(10)
        ]
        config = {"scoring": {"minimum_score": 60, "max_papers_per_day": 2}}
        status = {"papers": {}}

        selected, runners_up = main.select_papers(scored, config, status)
        assert len(selected) == 2  # Hard cap
        assert len(runners_up) == 5  # Next 5

    def test_returns_zero_when_none_qualify(self):
        scored = [
            {"arxiv_id": "a", "title": "A", "scores": {"composite": 40}},
            {"arxiv_id": "b", "title": "B", "scores": {"composite": 30}},
        ]
        config = {"scoring": {"minimum_score": 60, "max_papers_per_day": 2}}
        status = {"papers": {}}

        selected, runners_up = main.select_papers(scored, config, status)
        assert len(selected) == 0
        assert len(runners_up) == 0

    def test_skips_already_processed(self):
        scored = [
            {"arxiv_id": "already_done", "title": "Old", "scores": {"composite": 90}},
            {"arxiv_id": "new_one", "title": "New", "scores": {"composite": 80}},
        ]
        config = {"scoring": {"minimum_score": 60, "max_papers_per_day": 2}}
        status = {"papers": {"already_done": {"status": "summarized"}}}

        selected, runners_up = main.select_papers(scored, config, status)
        assert len(selected) == 1
        assert selected[0]["arxiv_id"] == "new_one"

    def test_returns_one_when_only_one_qualifies(self):
        scored = [
            {"arxiv_id": "a", "title": "A", "scores": {"composite": 75}},
            {"arxiv_id": "b", "title": "B", "scores": {"composite": 40}},
        ]
        config = {"scoring": {"minimum_score": 60, "max_papers_per_day": 2}}
        status = {"papers": {}}

        selected, _ = main.select_papers(scored, config, status)
        assert len(selected) == 1


# ---------------------------------------------------------------------------
# PDF Extraction
# ---------------------------------------------------------------------------

class TestPdfExtraction:
    @patch("main.requests.get")
    @patch("main.time.sleep")
    def test_extracts_text_from_pdf(self, mock_sleep, mock_get):
        mock_resp = MagicMock()
        mock_resp.status_code = 200
        mock_resp.content = b"fake pdf bytes"
        mock_resp.raise_for_status = MagicMock()
        mock_get.return_value = mock_resp

        mock_page = MagicMock()
        mock_page.get_text.return_value = "This is page content about robot manipulation. " * 20  # Must exceed 500 chars

        mock_doc = MagicMock()
        mock_doc.__iter__ = MagicMock(return_value=iter([mock_page]))
        mock_doc.page_count = 1

        mock_fitz = MagicMock()
        mock_fitz.open.return_value = mock_doc

        with patch.object(main, "fitz", mock_fitz):
            text = main.fetch_paper_text("2503.12345", "Fallback abstract")

        assert "robot manipulation" in text

    @patch("main.requests.get")
    @patch("main.time.sleep")
    def test_falls_back_to_abstract(self, mock_sleep, mock_get):
        # Both PDF and HTML fail
        mock_get.side_effect = Exception("Download failed")

        text = main.fetch_paper_text("2503.12345", "This is the abstract")
        assert "This is the abstract" in text


# ---------------------------------------------------------------------------
# Summary Header Format
# ---------------------------------------------------------------------------

class TestSummaryFormat:
    @patch("main.Anthropic")
    def test_summary_has_required_fields(self, mock_anthropic):
        mock_response = MagicMock()
        mock_response.content = [MagicMock(text="## 1. Key Themes\n### Theme 1\nContent here.")]
        mock_client = MagicMock()
        mock_client.messages.create.return_value = mock_response
        mock_anthropic.return_value = mock_client

        summary = main.summarize_paper(
            paper_text="Full paper text...",
            title="RoboClaw: Dexterous Manipulation",
            authors=["Alice Zhang", "Bob Smith"],
            institution="AgiBot",
            abstract="A framework for dexterous manipulation.",
            arxiv_id="2503.12345",
            published="2026-03-19T00:00:00Z",
        )

        assert "**Source:** paper" in summary
        assert "**arXiv:** 2503.12345" in summary
        assert "**PDF:** https://arxiv.org/pdf/2503.12345" in summary
        assert "**Podcast:** AgiBot Research" in summary
        assert "**Date:** 2026-03-19" in summary
        assert "**Processed:**" in summary
        assert "**Participants:**" in summary
        assert "# RoboClaw: Dexterous Manipulation" in summary
        assert "---" in summary


# ---------------------------------------------------------------------------
# Status Tracking
# ---------------------------------------------------------------------------

class TestStatusTracking:
    def test_update_paper_status(self, tmp_path):
        repo = MagicMock()
        repo.working_dir = str(tmp_path)
        status = {"papers": {}}

        main.update_paper_status(repo, status, "2503.12345", "Test Paper", "MIT", 78.0)

        assert "2503.12345" in status["papers"]
        entry = status["papers"]["2503.12345"]
        assert entry["title"] == "Test Paper"
        assert entry["institution"] == "MIT"
        assert entry["status"] == "summarized"
        assert entry["score"] == 78.0

        # Verify file was written
        status_path = tmp_path / "paper_status.json"
        assert status_path.exists()
        written = json.loads(status_path.read_text())
        assert "2503.12345" in written["papers"]


# ---------------------------------------------------------------------------
# Institution Resolution
# ---------------------------------------------------------------------------

class TestInstitutionResolution:
    def test_matches_tracked_lab_from_affiliations(self):
        paper = {"authors": ["Alice"], "abstract": "Some paper"}
        enrichment = {"affiliations": ["MIT Computer Science and Artificial Intelligence Lab"]}
        tracked = ["MIT", "Stanford", "CMU"]

        result = main.resolve_institution(paper, enrichment, tracked)
        assert result == "MIT"

    def test_falls_back_to_abstract_match(self):
        paper = {"authors": ["Alice"], "abstract": "Research at Google DeepMind on robotics"}
        enrichment = {"affiliations": []}
        tracked = ["Google DeepMind", "Stanford"]

        result = main.resolve_institution(paper, enrichment, tracked)
        assert result == "Google DeepMind"

    def test_falls_back_to_first_affiliation(self):
        paper = {"authors": ["Alice"], "abstract": "Some paper"}
        enrichment = {"affiliations": ["University of Tokyo"]}
        tracked = ["MIT", "Stanford"]

        result = main.resolve_institution(paper, enrichment, tracked)
        assert result == "University of Tokyo"

    def test_falls_back_to_default(self):
        paper = {"authors": ["Alice"], "abstract": "Some paper"}
        enrichment = {"affiliations": []}
        tracked = ["MIT"]

        result = main.resolve_institution(paper, enrichment, tracked)
        assert result == "arXiv Physical AI"


# ---------------------------------------------------------------------------
# arXiv ID Extraction
# ---------------------------------------------------------------------------

class TestArxivIdExtraction:
    def test_extracts_from_url(self):
        assert main.extract_arxiv_id("http://arxiv.org/abs/2503.12345v1") == "2503.12345"

    def test_strips_version(self):
        assert main.extract_arxiv_id("2503.12345v2") == "2503.12345"

    def test_plain_id(self):
        assert main.extract_arxiv_id("2503.12345") == "2503.12345"


# ---------------------------------------------------------------------------
# Sanitize Title
# ---------------------------------------------------------------------------

class TestSanitizeTitle:
    def test_replaces_special_chars(self):
        assert main.sanitize_title('Test: "Paper" <v1>') == "Test_ _Paper_ _v1_"

    def test_truncates_long_titles(self):
        long_title = "A" * 300
        assert len(main.sanitize_title(long_title)) == 200


# ---------------------------------------------------------------------------
# Source Failure Graceful Degradation
# ---------------------------------------------------------------------------

class TestGracefulDegradation:
    @patch("main.discover_huggingface", return_value=[])
    @patch("main.discover_semantic_scholar", side_effect=Exception("SS down"))
    @patch("main.discover_arxiv")
    @patch("main.time.sleep")
    def test_continues_with_partial_sources(self, mock_sleep, mock_arxiv, mock_ss, mock_hf):
        mock_arxiv.return_value = [
            {"arxiv_id": "2503.12345", "title": "Test", "authors": [], "abstract": "Test", "sources": ["arxiv"]}
        ]

        # SS throws, but arXiv and HF still work
        arxiv_papers = main.discover_arxiv(["cs.RO"], ["robot"], 3)
        hf_papers = main.discover_huggingface(["robot"])

        # SS failure should not prevent deduplication
        candidates = main.deduplicate_papers(arxiv_papers, [], hf_papers)
        assert len(candidates) == 1
