#!/usr/bin/env python3
"""Render the CMUdict missing-US-IPA review queue as a compact Markdown report.

The renderer is read-only with respect to canonical vocabulary. ARPABET is kept
as source evidence; it is not converted to IPA or applied automatically.
"""
from __future__ import annotations
import argparse, json
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INPUT = ROOT / 'docs/reports/MISSING_US_IPA_CMUdict_REVIEW_QUEUE.json'

def render(payload: dict) -> str:
    records = payload.get('records', [])
    counts = payload.get('statusCounts', {})
    lines = [
        '# Missing US IPA — CMUdict Review Queue', '',
        f"- Missing US IPA records: **{payload.get('canonicalMissingUsIpaCount', len(records))}**",
        f"- Source: **{payload.get('source', 'unspecified')}**",
        f"- Source package version: **{payload.get('sourcePackage', 'unknown')} {payload.get('sourcePackageVersion', 'unknown')}**",
        '- Policy: **review only; no IPA values are applied automatically**.',
        '- Matching policy: exact normalized headword only; no fuzzy, substring, inflection or word-family fallback.',
        '', '## Status summary', '', '| Status | Records |', '|---|---:|'
    ]
    for key in ('single_pronunciation_candidate', 'multiple_pronunciations_review', 'no_exact_dictionary_entry', 'empty_dictionary_entry'):
        if key in counts:
            lines.append(f'| {key} | {counts[key]} |')
    lines += ['', '## Candidate and review records', '', '| Word | Canonical ID | Status | ARPABET variants | Decision |', '|---|---|---|---|---|']
    for row in records:
        variants = '<br>'.join('`' + ' '.join(v) + '`' for v in row.get('arpabet_variants', [])) or '—'
        safe = lambda value: str(value or '').replace('|', r'\|').replace('\n', ' ')
        lines.append(f"| {safe(row.get('word'))} | `{safe(row.get('id'))}` | {safe(row.get('status'))} | {variants} | {safe(row.get('decision'))} |")
    lines += ['', '## Interpretation boundary',
        '- A single CMUdict match is a candidate for editorial review, not an approved IPA transcription.',
        '- Multiple variants remain unresolved; stress and variant differences must be checked against the intended part of speech and sense.',
        '- No exact match is not evidence that a word has no pronunciation; it means this dictionary source did not provide an exact key.',
        '- Canonical vocabulary files are not changed by this report.', '']
    return '\n'.join(lines)

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input', type=Path, default=DEFAULT_INPUT)
    parser.add_argument('--output', type=Path, default=ROOT / 'docs/reports/MISSING_IPA_REVIEW_QUEUE.md')
    args = parser.parse_args()
    payload = json.loads(args.input.read_text(encoding='utf-8'))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(render(payload), encoding='utf-8')
    print(f"Rendered {len(payload.get('records', []))} IPA review records to {args.output}")
    return 0
if __name__ == '__main__':
    raise SystemExit(main())
