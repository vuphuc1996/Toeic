import importlib.util
import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SPEC = importlib.util.spec_from_file_location("objective_criterion_audit", ROOT / "tools/audit-objective-criterion-map.py")
AUDIT = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(AUDIT)

class ObjectiveCriterionMapTests(unittest.TestCase):
    def test_canonical_question_mapping_audit(self):
        result = subprocess.run(
            [sys.executable, str(ROOT / "tools/audit-objective-criterion-map.py")],
            cwd=ROOT, capture_output=True, text=True
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("1103 question-to-criterion links", result.stdout)
        self.assertIn("638 unique stable question IDs", result.stdout)
        self.assertIn("22/27 TOEIC criteria mapped", result.stdout)
        self.assertIn("0 Listening reserve items mapped", result.stdout)

    def test_subminimum_criteria_are_not_misreported_as_mastered(self):
        mapping = json.loads((ROOT / "data/learning-path/objective-criterion-map.json").read_text(encoding="utf-8"))
        counts = mapping["mappingCountsByCriterion"]
        self.assertEqual(counts["grammar-core-form-recognition"], 10)
        self.assertEqual(counts["listening-part-3-speaker-linking"], 10)
        self.assertEqual(counts["listening-part-3-conversation-purpose"], 7)
        self.assertEqual(counts["listening-part-4-talk-purpose"], 2)
        self.assertEqual(counts["reading-part-7-cross-document-link"], 2)
        self.assertEqual(counts["listening-part-1-visual-audio-match"], 8)
        self.assertEqual(counts["listening-part-1-detail-retention"], 8)
        self.assertEqual(mapping["uniqueQuestionCount"], 638)

    def test_part7_cross_document_evidence_requires_reviewed_two_source_quotes(self):
        resource = {"editorialStatus": "internal-editorial-reviewed", "documents": [
            {"label": "CUSTOMER EMAIL", "content": "The order is needed on October 20."},
            {"label": "SUPPLIER REPLY", "content": "We can deliver the order on October 20."},
        ]}
        question = {"evidence": {"sourceLabels": ["CUSTOMER EMAIL", "SUPPLIER REPLY"],
                                "quotes": ["needed on October 20", "deliver the order on October 20"]}}
        self.assertEqual(AUDIT.validate_cross_document_evidence(resource, question), [])
        one_source = {"evidence": {"sourceLabels": ["CUSTOMER EMAIL"], "quotes": ["needed on October 20"]}}
        self.assertTrue(any("at least two distinct sourceLabels" in error for error in AUDIT.validate_cross_document_evidence(resource, one_source)))
        wrong_quote = {"evidence": {"sourceLabels": ["CUSTOMER EMAIL", "SUPPLIER REPLY"], "quotes": ["needed next year", "deliver the order on October 20"]}}
        self.assertTrue(any("does not match" in error for error in AUDIT.validate_cross_document_evidence(resource, wrong_quote)))
        unreviewed = dict(resource, editorialStatus="default")
        self.assertTrue(any("internal-editorial-reviewed" in error for error in AUDIT.validate_cross_document_evidence(unreviewed, question)))

    def test_registry_and_mapping_counts_are_reconciled(self):
        import json
        mapping = json.loads((ROOT / "data/learning-path/objective-criterion-map.json").read_text(encoding="utf-8"))
        registry = json.loads((ROOT / "data/learning-path/objective-outcomes.json").read_text(encoding="utf-8"))
        outcomes = {outcome["id"]: (group["objectiveId"], outcome) for group in registry["objectives"] for outcome in group["outcomes"]}
        counts = {}
        for row in mapping["mappings"]:
            counts[row["criterionId"]] = counts.get(row["criterionId"], 0) + 1
            self.assertIn(row["criterionId"], outcomes)
            self.assertEqual(outcomes[row["criterionId"]][0], row["objectiveId"])
        self.assertEqual(counts, mapping["mappingCountsByCriterion"])
        self.assertEqual(len({row["questionKey"] for row in mapping["mappings"]}), mapping["uniqueQuestionCount"])
        self.assertEqual(len(counts), 22)
        toeic = [outcome for group in registry["objectives"] if not group["objectiveId"].startswith("foundation-") for outcome in group["outcomes"]]
        self.assertEqual(sum(outcome["status"].startswith("instrumented_") for outcome in toeic), 22)
        self.assertEqual(sum(outcome["status"] == "criteria_defined_not_yet_instrumented" for outcome in toeic), 5)


    def test_part7_evidence_rejects_ambiguous_duplicate_document_and_source_labels(self):
        resource = {"editorialStatus": "internal-editorial-reviewed", "documents": [
            {"label": "CUSTOMER EMAIL", "content": "The order is needed on October 20."},
            {"label": " customer   email ", "content": "A different message with conflicting content."},
            {"label": "SUPPLIER REPLY", "content": "We can deliver the order on October 20."},
        ]}
        question = {"evidence": {
            "sourceLabels": ["CUSTOMER EMAIL", "SUPPLIER REPLY"],
            "quotes": ["needed on October 20", "deliver the order on October 20"],
        }}
        self.assertTrue(any("duplicate document label" in error
                            for error in AUDIT.validate_cross_document_evidence(resource, question)))

        clean_resource = {"editorialStatus": "internal-editorial-reviewed", "documents": [
            {"label": "CUSTOMER EMAIL", "content": "The order is needed on October 20."},
            {"label": "SUPPLIER REPLY", "content": "We can deliver the order on October 20."},
        ]}
        repeated = {"evidence": {
            "sourceLabels": ["CUSTOMER EMAIL", " customer email "],
            "quotes": ["needed on October 20", "needed on October 20"],
        }}
        self.assertTrue(any("must not repeat" in error
                            for error in AUDIT.validate_cross_document_evidence(clean_resource, repeated)))

    def test_part7_evidence_rejects_non_string_labels_and_quotes(self):
        resource = {"editorialStatus": "internal-editorial-reviewed", "documents": [
            {"label": "CUSTOMER EMAIL", "content": "The order is needed on October 20."},
            {"label": "SUPPLIER REPLY", "content": "We can deliver the order on October 20."},
        ]}
        bad_label = {"evidence": {
            "sourceLabels": ["CUSTOMER EMAIL", 7],
            "quotes": ["needed on October 20", "deliver the order on October 20"],
        }}
        self.assertTrue(any("only non-empty strings" in error
                            for error in AUDIT.validate_cross_document_evidence(resource, bad_label)))
        bad_quote = {"evidence": {
            "sourceLabels": ["CUSTOMER EMAIL", "SUPPLIER REPLY"],
            "quotes": ["needed on October 20", 7],
        }}
        self.assertTrue(any("only non-empty strings" in error
                            for error in AUDIT.validate_cross_document_evidence(resource, bad_quote)))

    def test_evidence_basis_matches_complete_source_labels_not_substrings(self):
        self.assertTrue(AUDIT.evidence_basis_names_sources(
            "Cross-document evidence cites EVENT SCHEDULE and VENUE OPERATIONS NOTICE.",
            ["EVENT SCHEDULE", "VENUE OPERATIONS NOTICE"],
        ))
        self.assertFalse(AUDIT.evidence_basis_names_sources(
            "The updated EVENT SCHEDULED version was sent.",
            ["EVENT SCHEDULE"],
        ))

if __name__ == "__main__":
    unittest.main()
