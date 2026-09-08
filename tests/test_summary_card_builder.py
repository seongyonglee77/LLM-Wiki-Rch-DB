import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "fill_summary_cards.py"
sys.path.insert(0, str(ROOT / "scripts"))
SPEC = importlib.util.spec_from_file_location("fill_summary_cards", SCRIPT)
summary_builder = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(summary_builder)


class SummaryCardBuilderTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        for name in ("cards", "sources", "templates"):
            (self.root / name).mkdir()
        (self.root / "templates" / "template-paper-summary.md").write_text(
            (ROOT / "templates" / "template-paper-summary.md").read_text(encoding="utf-8"),
            encoding="utf-8",
        )
        (self.root / "sources" / "sample.md").write_text(
            "---\nstem: sample\nrecord_id: paper:sample\n---\n"
            "<!-- page: 1 -->\n## Introduction\nThe review identifies a persistent evidence gap.\n"
            "<!-- page: 2 -->\n## Findings\nParticipants reported greater confidence after the intervention.\n"
            "<!-- page: 3 -->\n## Discussion\nTeacher mediation remained essential for responsible use.\n",
            encoding="utf-8",
        )

    def tearDown(self):
        self.tmp.cleanup()

    def evidence(self):
        return {
            "record_id": "paper:sample",
            "title": "A sample study",
            "authors": ["Author, Ada"],
            "year": "2026",
            "research_design": "empirical",
            "citation_key": "author2026sample",
            "one_sentence": "The study links a targeted intervention to confidence while retaining teacher mediation.",
            "purpose": "To test a citation-grounded summary workflow.",
            "keywords": ["intervention", "confidence"],
            "sections": [
                {"heading": "Theory & Literature Review", "claims": [{"claim": "The study identifies an evidence gap.", "quote": "The review identifies a persistent evidence gap.", "page": 1, "verification": "source_page"}]},
                {"heading": "Findings", "claims": [{"claim": "Participants reported greater confidence.", "quote": "Participants reported greater confidence after the intervention.", "page": 2, "verification": "source_page"}]},
                {"heading": "Discussion", "claims": [{"claim": "Teacher mediation remains necessary.", "quote": "Teacher mediation remained essential for responsible use.", "page": 3, "verification": "source_page"}]},
            ],
            "limitations": "This fixture has no external-validity evidence.",
            "relevance": "Useful for testing citation-grounded cards.",
        }

    def test_builds_deep_summary_only_from_verified_quotes(self):
        result = summary_builder.build_summary_card(self.root, self.root / "sources" / "sample.md", self.evidence())
        data, body = summary_builder.read_yaml_md(result)
        self.assertEqual(data["summary"]["status"], "summarized")
        self.assertNotIn("review_log", data)
        self.assertNotIn("paper_id", data)
        self.assertIn('"Participants reported greater confidence after the intervention." (p. 2; source_page-verified)', body)
        self.assertIn("## Theory & Literature Review", body)

    def test_template_uses_the_consolidated_yaml_schema(self):
        data, _ = summary_builder.read_yaml_md(ROOT / "templates" / "template-paper-summary.md")
        self.assertTrue({"record_id", "stem", "citation_info", "summary", "provenance", "verification"} <= set(data))
        self.assertTrue({"level", "status", "structure_policy"} <= set(data["summary"]))
        self.assertNotIn("review_log", data)
        for obsolete in ("paper_id", "file_name", "topics", "projects", "related", "summary_level", "status", "structure_policy"):
            self.assertNotIn(obsolete, data)

    def test_rejects_quote_not_found_in_its_declared_page(self):
        evidence = self.evidence()
        evidence["sections"][1]["claims"][0]["page"] = 1
        with self.assertRaisesRegex(ValueError, "not found on source page 1"):
            summary_builder.build_summary_card(self.root, self.root / "sources" / "sample.md", evidence)

    def test_rejects_unverified_claims_for_summarized_cards(self):
        evidence = self.evidence()
        evidence["sections"][2]["claims"][0]["verification"] = "partial"
        with self.assertRaisesRegex(ValueError, "must be source_page or source_text"):
            summary_builder.build_summary_card(self.root, self.root / "sources" / "sample.md", evidence)

    def test_allows_source_text_verified_claim_without_page(self):
        evidence = self.evidence()
        claim = evidence["sections"][1]["claims"][0]
        claim["page"] = ""
        claim["verification"] = "source_text"
        result = summary_builder.build_summary_card(self.root, self.root / "sources" / "sample.md", evidence)
        data, body = summary_builder.read_yaml_md(result)
        self.assertEqual(data["verification"]["quote_verification_status"], "partial")
        self.assertIn("page unavailable; source-text-verified", body)

    def test_source_text_verification_rejects_a_page_number(self):
        evidence = self.evidence()
        claim = evidence["sections"][1]["claims"][0]
        claim["verification"] = "source_text"
        with self.assertRaisesRegex(ValueError, "source_text verification must leave page blank"):
            summary_builder.build_summary_card(self.root, self.root / "sources" / "sample.md", evidence)


if __name__ == "__main__":
    unittest.main()
