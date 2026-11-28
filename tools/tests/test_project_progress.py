import json, subprocess, sys, unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]

def pct(n, d): return f"{(n/d*100):.1f}%" if d else "Chưa đo được"

class ProjectProgressTests(unittest.TestCase):
    def test_report_uses_explicit_targets_and_marks_unknown_targets(self):
        result=subprocess.run([sys.executable,'tools/report-project-progress.py'],cwd=ROOT,text=True,capture_output=True,check=True)
        out=result.stdout
        manifest = json.loads((ROOT / 'data/manifest.json').read_text(encoding='utf-8'))
        vocab_files = [ROOT / x['file'].replace('./', '', 1) for x in manifest['letters']]
        vocab_records = []
        for p in vocab_files:
            vocab_records.extend(json.loads(p.read_text(encoding='utf-8')).get('words', []))
        total_vocab = len(vocab_records)
        us_ipa_count = sum(bool((x.get('phonetic') or {}).get('us')) for x in vocab_records)
        wf_headwords = sum(bool(x.get('word_family')) for x in vocab_records)
        wf_links = sum(len(x.get('word_family') or []) for x in vocab_records)

        self.assertIn(f'{total_vocab:,} | 3,000 minimum | **{pct(total_vocab, 3000)}**', out)
        self.assertIn(f'{total_vocab:,} | 5,000 planning ceiling | **{pct(total_vocab, 5000)}**', out)
        self.assertIn('16/16 | All diagnostic questions | **100.0%**',out)
        self.assertIn('Chưa đo được',out)
        self.assertIn('not editorial approval',out)
        self.assertIn(f'US IPA | {us_ipa_count:,}/{total_vocab:,} | **{pct(us_ipa_count, total_vocab)}**', out)
        self.assertIn(f'Word family | {wf_headwords:,}/{total_vocab:,} | **{pct(wf_headwords, total_vocab)}**', out)
        self.assertIn(f'Word-family directed links | {wf_links:,} links', out)
        self.assertIn('Related-term glossary exact reference join | 556/804 | **69.2%** | 248 distinct terms / 249 occurrences remain unglossed',out)
        self.assertIn('| Guided pathway stages represented | 3/6 | Pre-A1, A1, A2, B1, B2, C1 | **50.0%** |',out)
        self.assertIn('| Canonical objective-resource links | 379/379 |',out)
        self.assertIn('| Foundation outcome evidence wired | 6/6 | 100.0% |',out)
        self.assertIn('| Outcomes with evidence instrumentation | 29/33 | 87.9% |',out)
        self.assertIn('| TOEIC sub-skill criteria with item-level mapping | 23/27 | 85.2% |',out)
        self.assertIn('1,119 explicit stable-ID links across 638 unique question IDs',out)
        self.assertIn('4 TOEIC criteria remain visible without criterion-level scoring',out)
        self.assertIn('Foundation outcome evidence now records recognition',out)
        self.assertIn('Independent-review handoff queue: 193 Listening questions across 89 units + 87 Reading Part 7 questions across 22 resources + 80 separate Part 5 questions = 360 item-level decisions',out)
        self.assertIn('Independent review queue | 193 Listening + 87 Reading Part 7 + 80 Part 5 = 360 questions',out)
    def test_report_includes_foundation_listening_bank_coverage(self):
        result=subprocess.run([sys.executable,'tools/report-project-progress.py'],cwd=ROOT,text=True,capture_output=True,check=True)
        self.assertIn('Foundation Listening core scripts mapped | 23/23 | **100.0%**',result.stdout)
        self.assertIn('Foundation Listening questions | 59 core + 39 supplementary | Chưa đo được',result.stdout)
        self.assertIn('Foundation Reading | 23/23 passages / 59 questions',result.stdout)
        self.assertIn('Foundation Listening | 23/23 core scripts / 59 core questions + 13 supplementary A2 scripts / 39 questions',result.stdout)
        self.assertIn('not authentic ETS recordings',result.stdout)
    def test_report_includes_alphabet_sound_bank_coverage_without_mastery_claim(self):
        result=subprocess.run([sys.executable,'tools/report-project-progress.py'],cwd=ROOT,text=True,capture_output=True,check=True)
        self.assertIn('Foundation A–Z letter records | 26/26 | **100.0%**',result.stdout)
        self.assertIn('action count is not pronunciation mastery',result.stdout)
        self.assertIn('toeic:alphabet-sound-progress:v1',result.stdout)
    def test_report_does_not_mislabel_inventory_as_completion(self):
        result=subprocess.run([sys.executable,'tools/report-project-progress.py'],cwd=ROOT,text=True,capture_output=True,check=True)
        self.assertIn('Content counts do not equal completed learning outcomes.',result.stdout)
        self.assertIn('independent review',result.stdout)
if __name__=='__main__': unittest.main()
