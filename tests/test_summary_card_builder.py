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
            "<!-- page: 1 -->\n## Introduction\nThe review identifies a persistent evidence gap. Prior work focused on access. The authors call for situated evidence.\n"
            "<!-- page: 2 -->\n## Findings\nParticipants reported greater confidence after the intervention. Attendance also increased. Interviews showed stronger transfer.\n"
            "<!-- page: 3 -->\n## Discussion\nTeacher mediation remained essential for responsible use. The authors recommend contextual support. The discussion returns to the evidence gap.\n",
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
            "summary_depth": {"level": "deep"},
            "one_sentence": "The study links a targeted intervention to confidence while retaining teacher mediation.",
            "purpose": "To test a citation-grounded summary workflow.",
            "unique_contributions": "It connects confidence, attendance, and transfer in one evidence-backed account.",
            "future_work": "Future work should test the intervention in additional contexts.",
            "literature_use": "Use the study to support a discussion of evidence-grounded intervention design.",
            "citation_notes": "All claims use exact parsed-source quotations; page-level review remains required when markers are unavailable.",
            "keywords": ["intervention", "confidence"],
            "sections": [
                {"heading": "Theory & Literature Review", "overview": "The paper situates the intervention in a gap around contextual evidence.", "claims": [
                    {"claim": "The study identifies an evidence gap.", "interpretation": "The gap motivates the study.", "why_it_matters": "It explains why the intervention was tested.", "quote": "The review identifies a persistent evidence gap.", "page": 1, "verification": "source_page"},
                    {"claim": "Prior work focused on access.", "interpretation": "The authors distinguish access from sustained use.", "why_it_matters": "It frames the study's contribution.", "quote": "Prior work focused on access.", "page": 1, "verification": "source_page"},
                    {"claim": "The authors call for situated evidence.", "interpretation": "The study answers that call.", "why_it_matters": "It connects the literature review to the design.", "quote": "The authors call for situated evidence.", "page": 1, "verification": "source_page"},
                ]},
                {"heading": "Findings", "overview": "The intervention affected confidence, attendance, and transfer.", "claims": [
                    {"claim": "Participants reported greater confidence.", "interpretation": "The intervention was associated with confidence gains.", "why_it_matters": "Confidence is a central outcome.", "quote": "Participants reported greater confidence after the intervention.", "page": 2, "verification": "source_page"},
                    {"claim": "Attendance also increased.", "interpretation": "Engagement changed alongside confidence.", "why_it_matters": "It broadens the result beyond self-report.", "quote": "Attendance also increased.", "page": 2, "verification": "source_page"},
                    {"claim": "Interviews showed stronger transfer.", "interpretation": "Participants applied learning beyond the intervention.", "why_it_matters": "Transfer clarifies the practical significance.", "quote": "Interviews showed stronger transfer.", "page": 2, "verification": "source_page"},
                ]},
                {"heading": "Discussion", "overview": "The authors interpret the results as dependent on sustained mediation and context.", "claims": [
                    {"claim": "Teacher mediation remains necessary.", "interpretation": "The intervention is not self-sufficient.", "why_it_matters": "It qualifies the implementation claim.", "quote": "Teacher mediation remained essential for responsible use.", "page": 3, "verification": "source_page"},
                    {"claim": "The authors recommend contextual support.", "interpretation": "Implementation should fit local conditions.", "why_it_matters": "It guides future adoption.", "quote": "The authors recommend contextual support.", "page": 3, "verification": "source_page"},
                    {"claim": "The discussion returns to the evidence gap.", "interpretation": "The results are positioned as a response to the opening problem.", "why_it_matters": "It closes the argumentative sequence.", "quote": "The discussion returns to the evidence gap.", "page": 3, "verification": "source_page"},
                ]},
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
        self.assertIn("## Unique Contributions", body)
        self.assertNotIn("## Directly Citable Evidence", body)

    def test_template_uses_the_consolidated_yaml_schema(self):
        data, _ = summary_builder.read_yaml_md(ROOT / "templates" / "template-paper-summary.md")
        self.assertTrue({"record_id", "stem", "citation_info", "summary", "provenance", "verification"} <= set(data))
        self.assertTrue({"wiki", "overviews", "concepts", "projects", "questions", "supersedes", "superseded_by"} <= set(data["related"]))
        self.assertTrue({"level", "status", "structure_policy"} <= set(data["summary"]))
        self.assertNotIn("review_log", data)
        for obsolete in ("paper_id", "file_name", "topics", "projects", "summary_level", "status", "structure_policy", "review_log"):
            self.assertNotIn(obsolete, data)

    def test_rejects_quote_not_found_in_its_declared_page(self):
        evidence = self.evidence()
        evidence["sections"][1]["claims"][0]["page"] = 1
        with self.assertRaisesRegex(ValueError, "not found on source page 1"):
            summary_builder.build_summary_card(self.root, self.root / "sources" / "sample.md", evidence)

    def test_rejects_shallow_major_section(self):
        evidence = self.evidence()
        evidence["sections"][1]["claims"] = evidence["sections"][1]["claims"][:2]
        with self.assertRaisesRegex(ValueError, "at least 3 substantive claims"):
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
