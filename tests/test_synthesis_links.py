import sys
import json
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from synthesis_map import related_metadata, synthesis_links_for  # noqa: E402


class SynthesisLinkTests(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.root = Path(self.temp_dir.name)
        (self.root / "registry").mkdir()
        (self.root / "registry" / "synthesis-links.json").write_text(
            json.dumps({
                "version": 1,
                "policy": {"mandatory_any_of": ["overviews", "concepts"], "optional": ["projects", "questions"]},
                "papers": {
                    "paper-a": {
                        "overviews": [{"path": "overviews/topic", "label": "Topic", "relation": "anchors the paper"}],
                        "concepts": ["concepts/method"],
                    },
                    "paper-b": {"overviews": ["overviews/topic"]},
                },
            }),
            encoding="utf-8",
        )

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_relationships_are_many_to_many_and_optional_by_category(self):
        paper_a = related_metadata(self.root, "paper-a")
        paper_b = related_metadata(self.root, "paper-b")
        self.assertTrue(paper_a["overviews"] and paper_a["concepts"])
        self.assertEqual(paper_a["projects"], [])
        self.assertTrue(paper_b["overviews"])
        self.assertEqual(paper_b["concepts"], [])

    def test_registry_relationships_have_paths(self):
        links = synthesis_links_for(self.root, "paper-a")
        self.assertTrue(links)
        self.assertTrue(all(item["path"].startswith(("overviews/", "concepts/", "projects/", "questions/")) for item in links))


if __name__ == "__main__":
    unittest.main()
