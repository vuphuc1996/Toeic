"""Edge-case regression tests for the canonical Word Family graph audit."""
from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "audit-word-family-graph.py"
SPEC = importlib.util.spec_from_file_location("word_family_graph_audit_edges", SCRIPT)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(MODULE)


def word(headword, pos="noun", meaning="nghĩa", family=None):
    return {
        "word": headword,
        "senses": [{"pos": pos, "meaning_vi": meaning}],
        "word_family": family or [],
    }


def link(headword, pos="noun", meaning="nghĩa"):
    return {"word": headword, "pos": pos, "meaning_vi": meaning}


class WordFamilyGraphEdgeTests(unittest.TestCase):
    def test_nfkc_casefold_and_whitespace_resolve_canonical_target(self):
        data = MODULE.audit_data([
            ("A.json", {"words": [word("alpha", family=[link(" ＢＥＴＡ ")])]}),
            ("B.json", {"words": [word("beta")]}),
        ])
        self.assertEqual(data["missing_targets"], [])
        self.assertEqual(data["self_references"], [])
        self.assertEqual(data["pos_mismatches"], [])
        self.assertEqual(data["meaning_mismatches"], [])

    def test_missing_target_is_reported_without_pos_or_meaning_guess(self):
        data = MODULE.audit_data([
            ("A.json", {"words": [word("alpha", family=[link("absent")])]}),
        ])
        self.assertEqual(len(data["missing_targets"]), 1)
        self.assertEqual(data["missing_targets"][0]["target"], "absent")
        self.assertEqual(data["pos_mismatches"], [])
        self.assertEqual(data["meaning_mismatches"], [])

    def test_target_pos_mismatch_is_reported(self):
        data = MODULE.audit_data([
            ("A.json", {"words": [word("alpha", family=[link("beta", "verb", "chạy")]), word("beta", "noun", "chạy")]}),
        ])
        self.assertEqual(len(data["pos_mismatches"]), 1)
        self.assertEqual(data["pos_mismatches"][0]["target_pos"], ["noun"])

    def test_target_sense_meaning_mismatch_is_reported(self):
        data = MODULE.audit_data([
            ("A.json", {"words": [word("alpha", family=[link("beta", "noun", "nghĩa A")]), word("beta", "noun", "nghĩa B")]}),
        ])
        self.assertEqual(len(data["meaning_mismatches"]), 1)
        self.assertEqual(data["meaning_mismatches"][0]["target_meanings"], ["nghĩa B"])

    def test_nonreciprocal_link_is_review_flag_not_structural_error(self):
        data = MODULE.audit_data([
            ("A.json", {"words": [word("alpha", family=[link("beta")]), word("beta")]}),
        ])
        self.assertEqual(len(data["nonreciprocal_links"]), 1)
        self.assertEqual(data["missing_targets"], [])

    def test_reciprocal_link_is_not_flagged(self):
        data = MODULE.audit_data([
            ("A.json", {"words": [word("alpha", family=[link("beta")]), word("beta", family=[link("alpha")])]}),
        ])
        self.assertEqual(data["nonreciprocal_links"], [])

    def test_duplicate_family_targets_are_reported_after_normalization(self):
        data = MODULE.audit_data([
            ("A.json", {"words": [word("alpha", family=[link("beta"), link(" BETA ")])]}),
        ])
        self.assertEqual(len(data["duplicate_links"]), 1)

    def test_malformed_family_container_and_link_are_reported(self):
        data = MODULE.audit_data([
            ("A.json", {"words": [
                {"word": "alpha", "senses": [], "word_family": "beta"},
                {"word": "beta", "senses": [], "word_family": [{"word": "gamma"}]},
            ]}),
        ])
        self.assertEqual({row["issue"] for row in data["malformed"]}, {"word-family-not-list", "malformed-family-link"})

    def test_duplicate_canonical_headwords_are_reported(self):
        data = MODULE.audit_data([
            ("A.json", {"words": [word("alpha")]}),
            ("B.json", {"words": [word(" ALPHA ")]}),
        ])
        self.assertEqual(len(data["duplicate_headwords"]), 1)

    def test_empty_input_is_safe(self):
        data = MODULE.audit_data([])
        self.assertEqual(data["headwords"], 0)
        self.assertEqual(data["link_count"], 0)
        self.assertEqual(data["malformed"], [])


if __name__ == "__main__":
    unittest.main()
