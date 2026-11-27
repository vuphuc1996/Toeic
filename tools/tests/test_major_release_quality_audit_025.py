"""Data contract tests for the version-aware cross-domain release audit."""
import importlib.util, unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sp=importlib.util.spec_from_file_location('major_release_audit_025',ROOT/'tools/audit-major-release.py')
mod=importlib.util.module_from_spec(sp); sp.loader.exec_module(mod)
class MajorReleaseQualityAudit025(unittest.TestCase):
    @classmethod
    def setUpClass(cls): cls.audit=mod.audit()
    def test_vocabulary_coverage_metrics_are_bounded(self):
        v=self.audit['vocabulary']; self.assertEqual(v['headwords'],mod.read('data/manifest.json')['totalWords'])
        for key,value in self.audit['vocabularyFieldCoverage'].items():
            self.assertGreaterEqual(value['count'],0); self.assertLessEqual(value['count'],v['headwords'])
            self.assertGreaterEqual(value['percent'],0); self.assertLessEqual(value['percent'],100)
    def test_glossary_metrics_are_consistent(self):
        g=self.audit['relatedGlossary']
        rows=mod.read('data/related-terms.json')['terms']
        normalized={mod.normalize_relation_term(row.get('term')) for row in rows}
        normalized.discard('')
        # v2.95.45 Batch 038 adds five verified relation-target glosses
        # after the v2.95.44 Batch 037 inventory; guarded sense fixes do not add rows.
        self.assertEqual(len(rows),567)
        self.assertEqual(g['entries'],len(rows))
        self.assertEqual(g['uniqueEntries'],len(normalized))
        self.assertEqual(g['duplicateEntries'],len(rows)-len(normalized))
        self.assertEqual(g['uniqueEntries'],567)
        self.assertEqual(g['duplicateEntries'],0)
        self.assertLessEqual(g['coveredUniqueTerms'],g['referencedUniqueTerms'])
        self.assertEqual(g['unglossedUniqueTerms'],g['referencedUniqueTerms']-g['coveredUniqueTerms'])
        self.assertEqual(g['canonicalVocabularySourceEntries'], sum(row.get('source') == 'canonical-vocabulary-senses' for row in rows))
        self.assertEqual(g['canonicalVocabularySourceEntries'],205)
        report = mod.REPORT.read_text(encoding='utf-8')
        self.assertIn('cumulative inventory; not this release delta', report)
        self.assertNotIn('Canonical headword sense backfills in this release', report)
    def test_content_inventory_is_nonempty_and_known(self):
        c=self.audit['contentInventory']; self.assertEqual(c,{'grammarLessons':58,'listeningResources':145,'readingResources':73,'part5PracticeQuestions':80})
    def test_outcome_instrumentation_is_not_claimed_complete(self):
        o=self.audit['learningOutcomes']; self.assertEqual(o['criteria'],33); self.assertEqual(o['instrumentedCriteria'],6); self.assertLess(o['instrumentedPercent'],100)
    def test_outcome_status_distribution_matches_detail_rows(self):
        o=self.audit['learningOutcomes']
        self.assertEqual(len(o['criteriaDetail']),o['criteria'])
        self.assertEqual(sum(o['statusCounts'].values()),o['criteria'])
        self.assertEqual(o['statusCounts']['criteria_defined_not_yet_instrumented'],27)
        self.assertEqual(o['statusCounts']['instrumented_practice_evidence'],2)
        self.assertEqual(o['statusCounts']['instrumented_learner_self_report'],2)
        self.assertEqual(o['statusCounts']['instrumented_delayed_recall'],2)
    def test_outcome_detail_has_no_missing_evidence_contract_fields(self):
        for row in self.audit['learningOutcomes']['criteriaDetail']:
            self.assertTrue(row['objectiveId'])
            self.assertTrue(row['outcomeId'])
            self.assertTrue(row['title'])
            self.assertTrue(row['status'])
            self.assertIn(row['evidenceMetric'],mod.read('data/learning-path/objective-outcomes.json')['policy']['scoreTypes'])
            self.assertGreater(row['masteryThreshold'],0)
            self.assertGreaterEqual(row['minimumUniqueItems'],1)
    def test_evidence_matrix_lists_each_criterion(self):
        matrix=mod.OUTCOME_REPORT.read_text(encoding='utf-8')
        version=self.audit['version']
        self.assertIn(f'Learning Outcome Evidence Matrix — v{version}',matrix)
        self.assertEqual(sum(1 for line in matrix.splitlines() if line.startswith('| ') and not line.startswith('| Objective |') and not line.startswith('|---')),33)
        self.assertIn('learner completion, mastery',matrix)
    def test_reports_have_current_release_marker(self):
        version=self.audit['version']
        self.assertIn(f'v{version}',mod.REPORT.read_text(encoding='utf-8'))
if __name__=='__main__': unittest.main()
