# User Acceptance Checklist — v2.95.25

## Glossary source backfill
- [ ] Open vocabulary/review UI on a term that uses related-term fallback (e.g. `accept`, `accessible`, `record`).
- [ ] Confirm English definition is no longer the generic placeholder.
- [ ] Confirm Vietnamese gloss remains intact and POS is present.
- [ ] For multi-sense term `record`, confirm combined definitions are readable.
- [ ] Verify fallback/reference terms still work in practice; no duplicate choices or answer-key changes.

## Regression and environment checks
- [ ] iPhone Safari: open, refresh, and inspect vocabulary detail/fallback.
- [ ] Desktop browser at 100% zoom: confirm sidebar/footer still visible.
- [ ] Offline/reconnect: use previously cached shell; then reconnect and confirm no data loss.
- [ ] TTS: confirm actual device voice and cadence (not covered by automated test).
- [ ] Confirm no local vocabulary, review history or settings were reset.

Record device/browser, date, result and any screenshots before approving deployment.
