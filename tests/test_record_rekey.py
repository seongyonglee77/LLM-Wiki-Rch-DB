import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from llm_wiki_common import read_yaml_md, write_yaml_md  # noqa: E402
from rekey_record import rekey_record  # noqa: E402


class RecordRekeyTests(unittest.TestCase):
    def test_summary_metadata_rekeys_all_canonical_artifacts(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            for folder in ("papers", "sources", "cards", "wiki", "logs"):
                (root / folder).mkdir()

            old = "provisional-paper"
            source = root / "sources" / f"{old}.md"
            write_yaml_md(source, {"stem": old, "record_id": f"paper:{old}", "pdf_path": f"papers/{old}.pdf", "source_path": f"sources/{old}.md"}, "## Old title\n\nSource text.\n")
            write_yaml_md(root / "cards" / f"{old}.md", {"stem": old, "record_id": f"paper:{old}", "provenance": {"pdf_path": f"papers/{old}.pdf", "source_path": f"sources/{old}.md"}}, f"- Source: [[../sources/{old}|parsed source]]\n")
            write_yaml_md(root / "wiki" / f"{old}.md", {"stem": old, "record_id": f"paper:{old}"}, f"- Card: [[../cards/{old}|summary card]]\n")
            (root / "papers" / f"{old}.pdf").write_bytes(b"pdf")
            (root / "logs" / f"parse-{old}.json").write_text(json.dumps({"stem": old, "record_id": f"paper:{old}"}), encoding="utf-8")

            evidence = {"title": "Preparing Future Teachers", "authors": ["Miller, Ada", "Chen, Bo", "Patel, Cara"], "year": "2025"}
            new_source, new_stem, new_record_id = rekey_record(root, source, evidence)

            self.assertEqual(new_stem, "2025_Miller-Chen-Patel_Preparing-Future-Teachers")
            self.assertEqual(new_record_id, f"paper:{new_stem}")
            for folder, suffix in (("papers", ".pdf"), ("sources", ".md"), ("cards", ".md"), ("wiki", ".md")):
                self.assertTrue((root / folder / f"{new_stem}{suffix}").exists())
                self.assertFalse((root / folder / f"{old}{suffix}").exists())
            self.assertFalse((root / "logs" / f"parse-{old}.json").exists())
            self.assertTrue((root / "logs" / f"parse-{new_stem}.json").exists())

            source_data, _ = read_yaml_md(new_source)
            self.assertEqual(source_data["stem"], new_stem)
            self.assertEqual(source_data["record_id"], new_record_id)
            card_body = (root / "cards" / f"{new_stem}.md").read_text(encoding="utf-8")
            wiki_body = (root / "wiki" / f"{new_stem}.md").read_text(encoding="utf-8")
            self.assertIn(new_stem, card_body)
            self.assertIn(new_stem, wiki_body)
            self.assertNotIn(old, card_body)
            self.assertNotIn(old, wiki_body)


if __name__ == "__main__":
    unittest.main()
