"""Safety tests for sourced related-term glossary patches."""
from __future__ import annotations
import hashlib
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / 'tools' / 'patch-related-terms.py'


class PatchRelatedTermsTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.data = self.root / 'data' / 'related-terms.json'
        self.data.parent.mkdir(parents=True)
        self.original = {'schemaVersion': 1, 'terms': [{'term': 'alpha', 'meaning_vi': 'an-pha'}]}
        self.write_json(self.data, self.original)
        self.patch_path = self.root / 'patch.json'
        self.patch = {
            'schemaVersion': 1,
            'batchId': 'unit-test-related-terms',
            'baseFileSha256': hashlib.sha256(self.data.read_bytes()).hexdigest(),
            'operations': [{
                'term': 'beta', 'expect': {'absent': True},
                'new': {
                    'term': 'beta', 'meaning_vi': 'bê-ta', 'pos': 'n',
                    'definition_en': 'the second letter of the Greek alphabet',
                    'source': 'Cambridge Dictionary',
                    'sourceUrls': ['https://dictionary.cambridge.org/dictionary/english/beta'],
                },
            }],
        }
        self.write_json(self.patch_path, self.patch)

    def tearDown(self):
        self.tmp.cleanup()

    @staticmethod
    def write_json(path, value):
        path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

    def run_patch(self, action):
        return subprocess.run(
            [sys.executable, str(SCRIPT), '--root', str(self.root), '--patch', str(self.patch_path), action],
            capture_output=True, text=True, encoding='utf-8', check=False,
        )

    def test_dry_run_does_not_mutate_and_logs_mode(self):
        before = self.data.read_bytes()
        result = self.run_patch('--dry-run')
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertEqual(self.data.read_bytes(), before)
        rows = [json.loads(line) for line in (self.root / 'logs/patch-related-terms/operations.jsonl').read_text().splitlines()]
        self.assertEqual(rows[0]['mode'], 'dry-run')

    def test_apply_adds_sourced_gloss_and_rollback_removes_only_it(self):
        result = self.run_patch('--apply')
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        data = json.loads(self.data.read_text(encoding='utf-8'))
        self.assertEqual([row['term'] for row in data['terms']], ['alpha', 'beta'])
        result = self.run_patch('--rollback')
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertEqual(json.loads(self.data.read_text(encoding='utf-8')), self.original)
        rows = [json.loads(line) for line in (self.root / 'logs/patch-related-terms/operations.jsonl').read_text().splitlines()]
        self.assertEqual([row['mode'] for row in rows], ['apply', 'rollback'])

    def test_file_hash_mismatch_rejects_without_mutation(self):
        self.data.write_text('{"schemaVersion":1,"terms":[] }\n', encoding='utf-8')
        before = self.data.read_bytes()
        result = self.run_patch('--apply')
        self.assertEqual(result.returncode, 1)
        self.assertEqual(self.data.read_bytes(), before)
        self.assertIn('SHA-256', result.stdout)

    def test_existing_term_is_never_overwritten(self):
        self.patch['baseFileSha256'] = hashlib.sha256(self.data.read_bytes()).hexdigest()
        self.patch['operations'][0]['term'] = 'alpha'
        self.patch['operations'][0]['new']['term'] = 'alpha'
        self.write_json(self.patch_path, self.patch)
        before = self.data.read_bytes()
        result = self.run_patch('--apply')
        self.assertEqual(result.returncode, 1)
        self.assertEqual(self.data.read_bytes(), before)
        self.assertIn('đã tồn tại', result.stdout)

    def test_non_cambridge_source_is_rejected(self):
        self.patch['operations'][0]['new']['sourceUrls'] = ['https://example.com/beta']
        self.write_json(self.patch_path, self.patch)
        before = self.data.read_bytes()
        result = self.run_patch('--dry-run')
        self.assertEqual(result.returncode, 1)
        self.assertEqual(self.data.read_bytes(), before)
        self.assertIn('Cambridge Dictionary', result.stdout)


    def test_cambridge_lookalike_host_is_rejected(self):
        self.patch['operations'][0]['new']['sourceUrls'] = [
            'https://dictionary.cambridge.org.evil.example/dictionary/english/beta'
        ]
        self.write_json(self.patch_path, self.patch)
        before = self.data.read_bytes()
        result = self.run_patch('--dry-run')
        self.assertEqual(result.returncode, 1)
        self.assertEqual(self.data.read_bytes(), before)
        self.assertIn('đúng host Cambridge', result.stdout)

    def test_required_gloss_fields_must_be_nonempty(self):
        self.patch['operations'][0]['new']['definition_en'] = '  '
        self.write_json(self.patch_path, self.patch)
        before = self.data.read_bytes()
        result = self.run_patch('--dry-run')
        self.assertEqual(result.returncode, 1)
        self.assertEqual(self.data.read_bytes(), before)
        self.assertIn('definition_en', result.stdout)

    def test_duplicate_existing_terms_in_target_are_rejected(self):
        document = {'schemaVersion': 1, 'terms': [
            {'term': 'alpha', 'meaning_vi': 'an-pha'},
            {'term': 'ALPHA', 'meaning_vi': 'trùng'},
        ]}
        self.write_json(self.data, document)
        self.patch['baseFileSha256'] = hashlib.sha256(self.data.read_bytes()).hexdigest()
        self.write_json(self.patch_path, self.patch)
        before = self.data.read_bytes()
        result = self.run_patch('--dry-run')
        self.assertEqual(result.returncode, 1)
        self.assertEqual(self.data.read_bytes(), before)
        self.assertIn('term trùng', result.stdout)

    def test_apply_preserves_existing_file_permissions(self):
        self.data.chmod(0o640)
        result = self.run_patch('--apply')
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertEqual(self.data.stat().st_mode & 0o777, 0o640)

    def test_apply_restores_exact_bytes_if_audit_log_cannot_be_written(self):
        before = self.data.read_bytes()
        blocked = self.root / 'logs' / 'patch-related-terms'
        blocked.parent.mkdir(parents=True)
        blocked.write_text('not a directory', encoding='utf-8')
        result = self.run_patch('--apply')
        self.assertEqual(result.returncode, 1)
        self.assertEqual(self.data.read_bytes(), before)
        self.assertIn('APPLY FAIL', result.stdout)

    def test_rollback_restores_applied_bytes_if_audit_log_cannot_be_written(self):
        result = self.run_patch('--apply')
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        applied = self.data.read_bytes()
        log_dir = self.root / 'logs' / 'patch-related-terms'
        for item in log_dir.iterdir():
            item.unlink()
        log_dir.rmdir()
        log_dir.write_text('not a directory', encoding='utf-8')
        result = self.run_patch('--rollback')
        self.assertEqual(result.returncode, 1)
        self.assertEqual(self.data.read_bytes(), applied)
        self.assertIn('ROLLBACK FAIL', result.stdout)


if __name__ == '__main__':
    unittest.main()
