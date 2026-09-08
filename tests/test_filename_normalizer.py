import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from filename_normalizer import canonical_stem, collision_stem  # noqa: E402


class FilenameNormalizerTests(unittest.TestCase):
    def test_extracts_year_first_three_authors_and_three_word_title(self):
        source = """## The impact of a chatbot-assisted flipped approach on EFL learner interaction

## Jaeho Jeon 1 and Seongyong Lee 2* and Mira Kim 3

(Accepted May 10, 2024)
"""
        self.assertEqual(canonical_stem(source), "2024_Jeon-Lee-Kim_Impact-Chatbot-Assisted-Flipped")

    def test_uses_body_metadata_and_skips_journal_boilerplate(self):
        darvin = """---
stem: provisional
parsed_at: 2026-09-06
---
## RESEARCH ARTICLE

## Identity and investment in the age of generative AI

Ron Darvin

©TheAuthor(s), 2025.
"""
        roblin = """---
stem: provisional
---
## Computers &amp; Education

[journal homepage](https://example.test)

## Preparing preservice teachers to teach with digital technologies: An update of effective SQD-strategies

Jo Tondeur a , Ottavia Trevisan b , Sarah K. Howard c,* , Johan van Braak d

© 2025 The Authors.
"""
        self.assertEqual(canonical_stem(darvin), "2025_Darvin_Identity-Investment-Age")
        self.assertEqual(canonical_stem(roblin), "2025_Tondeur-Trevisan-Howard_Preparing-Preservice-Teachers")

    def test_collision_suffix_is_deterministic(self):
        self.assertEqual(collision_stem("2024_Lee_AI_Teacher_Agency", set()), "2024_Lee_AI_Teacher_Agency")
        self.assertEqual(collision_stem("2024_Lee_AI_Teacher_Agency", {"2024_Lee_AI_Teacher_Agency"}), "2024_Lee-a_AI_Teacher_Agency")
        self.assertEqual(collision_stem("2024_Lee_AI_Teacher_Agency", {"2024_Lee_AI_Teacher_Agency", "2024_Lee-a_AI_Teacher_Agency"}), "2024_Lee-b_AI_Teacher_Agency")


if __name__ == "__main__":
    unittest.main()
