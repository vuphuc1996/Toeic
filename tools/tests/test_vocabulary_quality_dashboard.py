"""Regression tests for the consolidated vocabulary/glossary dashboard."""
from __future__ import annotations
import hashlib, importlib.util, json, subprocess, sys, unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
SPEC = importlib.util.spec_from_file_location('vocabulary_quality_dashboard_test', ROOT / 'tools/build-vocabulary-quality-dashboard.py')
MODULE = importlib.util.module_from_spec(SPEC); SPEC.loader.exec_module(MODULE)

class VocabularyQualityDashboardTests(unittest.TestCase):
    def test_normalization_uses_nfkc_casefold_and_collapsed_whitespace(self):
        self.assertEqual(MODULE.norm('Ｆｏｒｍ  Ａ'), 'form a')
        self.assertEqual(MODULE.norm(' form\u00a0A '), 'form a')

    def test_real_repository_dashboard_is_deterministic_and_reconciled(self):
        first = MODULE.build(ROOT); second = MODULE.build(ROOT)
        self.assertEqual(first, second)
        self.assertEqual(first['release'], json.loads((ROOT / 'data/manifest.json').read_text(encoding='utf-8'))['version'])
        self.assertTrue(first['readOnly'])
        self.assertEqual(first['glossary']['flaggedEntries'], len(first['priorityQueue']))
        self.assertGreaterEqual(first['relationshipGraph']['headwords'], first['relationshipGraph']['uniqueHeadwords'])

    def test_summary_is_compact_reconciled_and_preserves_guardrails(self):
        data = MODULE.build(ROOT)
        summary = MODULE.summarize(data)
        self.assertEqual(summary['release'], data['release'])
        self.assertEqual(summary['priorityQueueCount'], len(data['priorityQueue']))
        self.assertEqual(summary['missingGlossaryCandidateCount'], len(data['missingGlossaryCandidates']))
        self.assertEqual(summary['guardrails'], data['guardrails'])
        self.assertNotIn('priorityQueue', summary)
        self.assertNotIn('missingGlossaryCandidates', summary)

    def test_dashboard_build_does_not_modify_source_data(self):
        tracked = [ROOT / 'data/manifest.json', ROOT / 'data/related-terms.json', ROOT / 'data/glossary.json']
        tracked.extend(sorted((ROOT / 'data/vocabulary').glob('*.json')))
        before = {path: hashlib.sha256(path.read_bytes()).hexdigest() for path in tracked if path.exists()}
        MODULE.build(ROOT)
        after = {path: hashlib.sha256(path.read_bytes()).hexdigest() for path in tracked if path.exists()}
        self.assertEqual(before, after)

    def test_summary_cli_emits_parseable_json_only(self):
        script = ROOT / 'tools/build-vocabulary-quality-dashboard.py'
        result = subprocess.run([sys.executable, str(script), '--summary-json'], cwd=ROOT,
                                check=True, capture_output=True, text=True, encoding='utf-8')
        parsed = json.loads(result.stdout)
        self.assertEqual(parsed['release'], MODULE.build(ROOT)['release'])
        self.assertTrue(parsed['readOnly'])
        self.assertEqual(parsed['priorityQueueCount'], len(MODULE.build(ROOT)['priorityQueue']))

    def test_guardrails_prohibit_mutation_and_reserve_promotion(self):
        data = MODULE.build(ROOT)
        self.assertTrue(all(value is False for value in data['guardrails'].values()))

    def test_render_contains_read_only_and_no_auto_import_policy(self):
        report = MODULE.render(MODULE.build(ROOT)).lower()
        self.assertIn('read-only', report)
        self.assertIn('no automatic definition copying or import', report)
        self.assertIn('reserve pools are not promoted', report)

if __name__ == '__main__': unittest.main()