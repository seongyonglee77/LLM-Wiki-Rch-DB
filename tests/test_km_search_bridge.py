import json
from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from km_search_bridge import context, note_path, text_search, validate_rag_result


class KMGuardTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        for name in ("indexes", "wiki", "cards", "sources", "agents"):
            (self.root / name).mkdir()
            (self.root / name / "note.md").write_text("Unique research evidence.")
        (self.root / "km-config.json").write_text(json.dumps({}))

    def tearDown(self):
        self.temp.cleanup()

    def test_text_excludes_operational_and_source_default(self):
        hits = text_search(self.root, "research")
        self.assertEqual([h["path"].split("/")[0] for h in hits], ["indexes", "wiki", "cards"])
        self.assertEqual(len(text_search(self.root, "research", sources=True)), 4)

    def test_wrong_content_same_relative_path_rejected(self):
        result = {"source_note": "cards/note.md", "entity": "note"}
        with self.assertRaises(ValueError):
            validate_rag_result(self.root, result, {"note_path": "cards/note.md", "body": "Other corpus"})
        self.assertTrue(validate_rag_result(self.root, result,
                        {"note_path": "cards/note.md", "body": "Unique research evidence."})["corpus_verified"])

    def test_scope_traversal_and_symlink(self):
        for value in ("agents/note.md", "../elsewhere.md", "sources/note.md"):
            with self.assertRaises((ValueError, OSError)):
                note_path(self.root, value)
        (self.root / "cards" / "escape.md").symlink_to(self.root / "agents" / "note.md")
        with self.assertRaises(ValueError):
            note_path(self.root, "cards/escape.md")

    def test_context_uses_bound_root_not_cwd(self):
        self.assertEqual(context(self.root)["db_root"], str(self.root))


if __name__ == "__main__":
    unittest.main()
