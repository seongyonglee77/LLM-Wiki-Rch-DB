import importlib.util
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "prepare_summary_input.py"
sys.path.insert(0, str(ROOT / "scripts"))
SPEC = importlib.util.spec_from_file_location("prepare_summary_input", SCRIPT)
prepare = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(prepare)


class PrepareSummaryInputTests(unittest.TestCase):
    def test_removes_embedded_base64_images_but_keeps_text(self):
        source = "## Findings\n![figure](data:image/png;base64," + ("A" * 500) + ")\nThe finding remains."
        result = prepare.sanitize_summary_source(source)
        self.assertNotIn("base64", result)
        self.assertIn("embedded image omitted for summary", result)
        self.assertIn("The finding remains.", result)


if __name__ == "__main__":
    unittest.main()
