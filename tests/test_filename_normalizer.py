import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from filename_normalizer import canonical_stem, collision_stem  # noqa: E402


class FilenameNormalizerTests(unittest.TestCase):
    def test_extracts_year_first_three_authors_and_three_word_title(self):
        source = """## The impact of a chatbot-assisted flipped approach on EFL learner interaction

## Alex Morgan 1 and Taylor Chen 2* and Dana Kim 3

(Accepted May 10, 2024)
"""
        self.assertEqual(canonical_stem(source), "2024_Morgan-Chen-Kim_Impact-Chatbot-Assisted-Flipped")

    def test_uses_body_metadata_and_skips_journal_boilerplate(self):
        first_fixture = """---
stem: provisional
parsed_at: 2026-09-06
---
## RESEARCH ARTICLE

## Identity and investment in digital learning

Riley Morgan

The Author(s), 2025.
"""
        second_fixture = """---
stem: provisional
---
## Computers &amp; Education

[journal homepage](https://example.test)

## Preparing novice teachers to teach with digital tools: An update of effective strategies

Alex Rivera a , Casey Park b , Jordan Smith c,* , Morgan Lee d

2025 The Authors.
"""
        self.assertEqual(canonical_stem(first_fixture), "2025_Morgan_Identity-Investment-Digital")
        self.assertEqual(canonical_stem(second_fixture), "2025_Rivera-Park-Smith_Preparing-Novice-Teachers")

    def test_collision_suffix_is_deterministic(self):
        self.assertEqual(collision_stem("2024_Lee_AI_Teacher_Agency", set()), "2024_Lee_AI_Teacher_Agency")
        self.assertEqual(collision_stem("2024_Lee_AI_Teacher_Agency", {"2024_Lee_AI_Teacher_Agency"}), "2024_Lee-a_AI_Teacher_Agency")
        self.assertEqual(collision_stem("2024_Lee_AI_Teacher_Agency", {"2024_Lee_AI_Teacher_Agency", "2024_Lee-a_AI_Teacher_Agency"}), "2024_Lee-b_AI_Teacher_Agency")


if __name__ == "__main__":
    unittest.main()
