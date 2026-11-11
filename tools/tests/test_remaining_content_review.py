"""Coverage and integrity guards for the v2.19.0 Listening/Reading editorial review.

These tests prove inventory coverage and structural stability; they do not replace
manual semantic review of transcripts, passages, grammar, or answer rationales.
"""
import hashlib
import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REGISTRY = json.loads((ROOT / "tools/remaining-content-review-v2.19.0.json").read_text(encoding="utf-8"))
LISTENING = json.loads((ROOT / "data/listening/listening-library.json").read_text(encoding="utf-8"))["listening"]
READINGS = json.loads((ROOT / "data/readings/reading-library.json").read_text(encoding="utf-8"))["readings"]


def selected_items():
    rows = []
    for collection, units, parts in (
        ("listening", LISTENING, {"Part 1", "Part 2", "Part 3", "Part 4"}),
        ("readings", READINGS, {"Part 5", "Part 6"}),
    ):
        for unit in units:
            if unit.get("part") not in parts:
                continue
            for number, question in enumerate(unit.get("questions", []), 1):
                rows.append((collection, unit, number, question))
    return rows


class RemainingContentReviewTests(unittest.TestCase):
    def test_review_registry_tracks_the_historical_148_questions(self):
        actual = {f"{u['id']}#Q{n}" for _, u, n, _ in selected_items()}
        recorded = [row["key"] for row in REGISTRY["items"]]
        self.assertEqual(len(recorded), 148)
        self.assertEqual(len(set(recorded)), 148)
        self.assertTrue(set(recorded).issubset(actual))
        self.assertGreater(len(actual), len(recorded), 'new reserve questions must not invalidate the historical review set')

    def test_part_distribution_matches_learning_blueprint_pool(self):
        expected = {"Part 1": 8, "Part 2": 25, "Part 3": 39, "Part 4": 30, "Part 5": 30, "Part 6": 16}
        self.assertEqual(REGISTRY["partCounts"], expected)
        observed = {}
        for row in REGISTRY["items"]:
            observed[row["part"]] = observed.get(row["part"], 0) + 1
        self.assertEqual(observed, expected)

    def test_reviewed_data_fingerprints_have_not_drifted(self):
        units = {
            'listening': {x['id']: x for x in LISTENING},
            'readings': {x['id']: x for x in READINGS},
        }
        for row in REGISTRY["items"]:
            unit = units[row['collection']][row['unitId']]
            unit_payload = {key: value for key, value in unit.items() if key != 'questions'}
            payload = json.dumps(unit_payload, ensure_ascii=False, sort_keys=True, separators=(',', ':')).encode('utf-8')
            actual = hashlib.sha256(payload).hexdigest()
            self.assertEqual(actual, row['unitContentSha256'], f"Reviewed transcript/unit metadata drifted: {row['unitId']}")
        for row in REGISTRY['items']:
            question = units[row['collection']][row['unitId']]['questions'][row['questionNumber'] - 1]
            payload = json.dumps(question, ensure_ascii=False, sort_keys=True, separators=(',', ':')).encode('utf-8')
            actual = hashlib.sha256(payload).hexdigest()
            self.assertEqual(actual, row['questionSha256'], f"Reviewed question drifted: {row['key']}")

    def test_unreviewed_questions_must_be_marked_reserve_pending(self):
        reviewed = {row["key"] for row in REGISTRY["items"]}
        for _, unit, number, _question in selected_items():
            key = f"{unit['id']}#Q{number}"
            if key not in reviewed:
                self.assertEqual(unit.get("editorialStatus"), "reserve-pending-independent-review", key)

    def test_keys_choices_choice_ids_and_explanations_are_well_formed(self):
        for collection, unit, number, question in selected_items():
            key = f"{unit['id']}#Q{number}"
            choices = question.get("choices", [])
            expected_choice_count = 3 if unit["part"] == "Part 2" else 4
            self.assertEqual(len(choices), expected_choice_count, key)
            self.assertIsInstance(question.get("answerIndex"), int, key)
            self.assertTrue(0 <= question["answerIndex"] < len(choices), key)
            normalized = [re.sub(r"\s+", " ", str(value)).strip().casefold() for value in choices]
            self.assertEqual(len(normalized), len(set(normalized)), key)
            choice_ids = question.get("choiceIds", [])
            self.assertEqual(len(choice_ids), len(choices), key)
            self.assertEqual(len(set(choice_ids)), len(choice_ids), key)
            self.assertTrue(str(question.get("explanation", "")).strip(), key)

    def test_registry_records_conservative_decisions_and_approved_photo_amendments(self):
        amendments = {row['unitId'] for row in REGISTRY.get('approvedAmendments', [])}
        for row in REGISTRY["items"]:
            if row['unitId'] in amendments:
                self.assertEqual(row['decision'], 'approved-photo-description-amendment-preserving-answer-key-and-choice-identity', row['key'])
            else:
                self.assertEqual(row["decision"], "retain-existing-key-and-options", row["key"])
            self.assertTrue(row["reviewChecks"], row["key"])
        self.assertFalse(REGISTRY["reviewPolicy"]["answerKeysChanged"])
        self.assertFalse(REGISTRY["reviewPolicy"]["choiceTextChanged"])
        self.assertFalse(REGISTRY["reviewPolicy"]["choiceOrderChanged"])
        self.assertTrue(REGISTRY["reviewPolicy"]["transcriptAndExplanationAmendments"])
        self.assertFalse(REGISTRY["reviewPolicy"]["personalIndexedDBTouched"])


if __name__ == "__main__":
    unittest.main()
