"""Regression tests for the traceable TOEIC answer-to-source audit.

Assertions derive their expected scope from the current libraries so new, edited or
removed learning content cannot leave this test pinned to a previous release's counts.
"""
import importlib.util
import json
import re
import subprocess
import sys
import unittest
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / "tools" / "audit-question-evidence.py"
VERSION = json.loads((ROOT / "data" / "manifest.json").read_text(encoding="utf-8"))["version"]
REPORT = ROOT / "docs" / "reports" / f"TOEIC_EDITORIAL_EVIDENCE_AUDIT_v{VERSION}.md"
SPEC = importlib.util.spec_from_file_location("toeic_question_evidence_audit", SCRIPT)
AUDIT = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(AUDIT)


class QuestionEvidenceAuditTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        result = subprocess.run(
            [sys.executable, str(SCRIPT)],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        if result.returncode != 0:
            raise RuntimeError(result.stdout + "\n" + result.stderr)
        cls.report = REPORT.read_text(encoding="utf-8")
        cls.libraries = {
            "Listening": AUDIT.read("data/listening/listening-library.json").get("listening", []),
            "Reading": AUDIT.read("data/readings/reading-library.json").get("readings", []),
        }
        cls.expected = Counter()
        for kind, items in cls.libraries.items():
            for item in items:
                source = AUDIT.get_source(item, kind)
                for question_number, question in enumerate(item.get("questions", []), 1):
                    answer_index = question.get("answerIndex", 0)
                    choices = question.get("choices", [])
                    answer = choices[answer_index] if isinstance(answer_index, int) and 0 <= answer_index < len(choices) else ""
                    question_copy = dict(question)
                    question_copy["_question_number"] = question_number
                    status, _ = AUDIT.evidence_status(kind, item.get("part", ""), item, question_copy, source, answer)
                    cls.expected[(kind, status)] += 1
        cls.total = sum(cls.expected.values())

    def test_every_current_question_is_indexed_once(self):
        listening = sum(len(item.get("questions", [])) for item in self.libraries["Listening"])
        reading = sum(len(item.get("questions", [])) for item in self.libraries["Reading"])
        self.assertIn(f"Questions indexed: **{self.total}** ({listening} Listening + {reading} Reading).", self.report)
        self.assertEqual(self.total, listening + reading)
        headings = [int(value) for value in re.findall(r"^### .+ \((\d+)\)$", self.report, re.M)]
        self.assertEqual(sum(headings), self.total, "Every current question must appear in exactly one evidence report category")

    def test_each_report_category_matches_current_source_classification(self):
        for (kind, _status), count in self.expected.items():
            self.assertGreater(count, 0)
        labels = {
            "direct-text-match": "Direct source phrase",
            "lexical-evidence": "Source lexical evidence (paraphrase may remain)",
            "manual-paraphrase-verified": "Manual paraphrase/inference checked against source",
            "photo-source-reviewed": "Part 1 source description and keyed action reviewed (Pexels or project-generated asset)",
            "response-fit-checked": "Part 2 speech-act / response-fit checked",
            "grammar-checked": "Part 5 sentence grammar checked",
            "context-fit-checked": "Part 6 context/cohesion checked",
            "explicit-source-evidence": "Explicit Part 7 passage/document quotation (v2.33.0 additions)",
            "reserve-pending-independent-review": "Listening reserve — not approved for Mock",
        }
        for (kind, status), count in self.expected.items():
            label = labels[status]
            self.assertIn(f"| {kind} | {label} | {count} |", self.report)

    def test_explicit_part7_evidence_has_no_broken_labels_or_quotes(self):
        explicit_count = self.expected[("Reading", "explicit-source-evidence")]
        self.assertGreater(explicit_count, 0)
        self.assertNotIn("Invalid explicit evidence metadata", self.report)
        self.assertEqual(self.report.count("Explicit source evidence:"), explicit_count)

    def test_reserve_scope_is_derived_from_all_current_reserved_questions(self):
        reserve_count = self.expected[("Listening", "reserve-pending-independent-review")]
        self.assertGreater(reserve_count, 0)
        self.assertIn(f"- {reserve_count} Listening questions remain reserve-pending-independent-review", self.report)
        for item in self.libraries["Listening"]:
            if item.get("editorialStatus") == "reserve-pending-independent-review":
                for question in item.get("questions", []):
                    self.assertEqual(
                        AUDIT.evidence_status("Listening", item.get("part", ""), item, question, AUDIT.get_source(item, "Listening"), "")[0],
                        "reserve-pending-independent-review",
                    )

    def test_all_listening_reserves_report_traceable_evidence_not_approval(self):
        reserve = [item for item in self.libraries['Listening'] if item.get('editorialStatus') == 'reserve-pending-independent-review']
        total = sum(len(item.get('questions', [])) for item in reserve)
        linked = 0
        for item in reserve:
            source = AUDIT.get_source(item, 'Listening')
            for question in item.get('questions', []):
                evidence = str(question.get('evidenceText', '')).strip()
                self.assertTrue(evidence, item['id'])
                self.assertIn(AUDIT.norm(evidence), AUDIT.norm(source), item['id'])
                linked += 1
        self.assertEqual(linked, total)
        self.assertIn(f'Reserve traceability gate: **{linked}/{total}** questions have a transcript evidence pointer', self.report)
        self.assertIn('still require an independent second reviewer', self.report)

    def test_manual_inference_review_registry_is_reflected_without_stale_release_counts(self):
        reviewed_count = len(AUDIT.REVIEWED_INFERENCES)
        self.assertEqual(self.expected[("Listening", "manual-paraphrase-verified")] + self.expected[("Reading", "manual-paraphrase-verified")], reviewed_count)
        self.assertIn(f"{reviewed_count} manually checked low-overlap paraphrase/inference items", self.report)
        self.assertNotIn("Questions indexed: **401**", self.report)
        self.assertNotIn("99 Listening questions remain", self.report)

    def test_distractor_audit_is_linked_and_semantic_review_boundary_is_clear(self):
        self.assertIn(f"TOEIC_DISTRACTOR_AUDIT_v{VERSION}.md", self.report)
        self.assertIn("not proof that distractors are implausible or unique", self.report)
        self.assertIn("independent second reviewer", self.report)


if __name__ == "__main__":
    unittest.main()
