import re
import sys
import unittest
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

import build_profile
from pixel import text_width


class ProfileTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.assets = build_profile.assets()
        cls.readme = (ROOT / "README.md").read_text(encoding="utf-8")

    def test_assets_are_valid_self_contained_accessible_svg(self):
        self.assertEqual(len(self.assets), 27)
        for name, svg in self.assets.items():
            with self.subTest(asset=name):
                root = ET.fromstring(svg)
                self.assertEqual(root.attrib["role"], "img")
                self.assertTrue(root.find("{http://www.w3.org/2000/svg}title").text)
                self.assertGreater(int(root.attrib["height"]), 0)
                self.assertIn("prefers-reduced-motion:reduce", svg)
                self.assertNotRegex(svg, r"<(?:script|foreignObject|image)\b")
                self.assertNotIn("https://", svg)

    def test_readme_preserves_profile_content_and_links(self):
        for text in (
            "Forward Deployed Engineer @ Microsoft",
            "Community Lead",
            "Multi-agent evals and reliability benchmarks",
            "24/7 software factories",
            "Developer tools and self-optimizing harnesses",
            "Silo, Paradise, Foundation, GOT",
        ):
            self.assertIn(text, self.readme)
        for _, name, description, url in build_profile.PROJECTS:
            self.assertIn(name, self.readme)
            self.assertIn(description, self.readme)
            self.assertIn(url, self.readme)
        for _, _, url in build_profile.LINKS:
            self.assertIn(url, self.readme)
        self.assertIn("THIRD_PARTY_NOTICES.md", self.readme)

    def test_every_readme_asset_exists_and_is_current(self):
        referenced = set(re.findall(r"assets/([\w-]+\.svg)", self.readme))
        self.assertEqual(referenced, set(self.assets))
        for name, expected in self.assets.items():
            self.assertEqual((ROOT / "assets" / name).read_text(encoding="utf-8"), expected)

    def test_portrait_and_typing_animation_are_retained(self):
        for layout in ("light", "dark", "phone"):
            hero = self.assets[f"hero-{layout}.svg"]
            self.assertIn("@keyframes wave-l", hero)
            self.assertIn("@keyframes wave-r", hero)
            self.assertIn("@keyframes lids", hero)
            self.assertIn("@keyframes type", hero)
            self.assertIn("Stephanie Schofield", hero)
        self.assertEqual({len(row) for row in build_profile.AVATAR}, {25})

    def test_descriptions_fit_both_card_layouts(self):
        for width in (build_profile.W, build_profile.M):
            room = build_profile.card_text_room(width)
            for _, _, description, _ in build_profile.PROJECTS:
                for line in build_profile.wrap(description, room, 2):
                    self.assertLessEqual(text_width(line, 2), room)
        for first_or_last in build_profile.NAME.split():
            self.assertLessEqual(text_width(first_or_last, 7), build_profile.M)

    def test_no_reference_person_or_game_is_in_profile(self):
        for text in (self.readme, *self.assets.values()):
            self.assertNotRegex(text, r"Ahmed|Abdelsalam|ahmedabdelsalam02|nim:|NIM-SUM")
            self.assertNotIn("\u2014", text)

    def test_visible_sections_have_semantic_headings(self):
        visible = self.readme.split("<details>", 1)[0]
        headings = re.findall(r"<h2>(.*?)</h2>", visible, flags=re.S)
        self.assertEqual(len(headings), 2)
        for label in ("Currently focused on", "Let's chat about"):
            self.assertTrue(any(f'alt="{label}"' in heading for heading in headings))

    def test_text_only_profile_preserves_project_descriptions_and_links(self):
        fallback = self.readme.split("<details>", 1)[1].split("</details>", 1)[0]
        for _, name, description, url in build_profile.PROJECTS:
            self.assertIn(f"[**{name}**]({url}): {description}", fallback)


if __name__ == "__main__":
    unittest.main()
