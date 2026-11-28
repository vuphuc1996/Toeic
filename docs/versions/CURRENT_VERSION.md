# Current Version — TOEIC Dictionary v2.95.81

- Current source: **v2.95.81** — Part 7 Evidence Guard Hardening.
- Sole predecessor baseline: candidate HEAD `a16a3e4a51917e687b92e404ab1c785a393dfb0f` (v2.95.80).
- Release package: `TOEIC_Dictionary_v2.95.81_FullSource.zip`.
- Package status: **NOT GENERATED OR VERIFIED**; the filename is a release target, not proof of an archive.
- Test report: `reports/TEST_REPORT_TOEIC_Dictionary_v2.95.81.md`.
- Canonical version source: `data/manifest.json`; top-level `package.json` is an exact-one checked marker.
- Scope: tighten Part 7 evidence validation and add negative regression coverage for malformed or ambiguous labels and evidence bases.
- Criterion map remains **1,103** links across **638** stable question IDs; TOEIC outcome instrumentation **22/27**, Foundation **6/6**, total **28/33**.
- No new criterion mappings are added; five unsupported TOEIC criteria remain uninstrumented; Listening reserve and editorial-review gates remain unchanged.
- Version/cache inventory: app **17**, Service Worker **42**, mock-engine **1** release-keyed references, all advanced to v2.95.81.
- Verified source/test HEAD: `047781760d0c34788e9153cc402efdec605c3d5f`.
- GitHub Validate: **PASS** ([run 46118675768](https://github.com/vuphuc1996/Toeic/actions/runs/46118675768)); 151/151 steps, 0 failed, 0 skipped; full Python discovery **853 tests PASS**.
- Part 7 validator regressions, canonical mapping audit and version synchronization: **PASS**. Version markers and cache keys: 19 release markers; 17 app, 42 Service Worker and 1 mock-engine keys.
- GitHub Pages build/deploy: **PASS** ([run 46118675714](https://github.com/vuphuc1996/Toeic/actions/runs/46118675714)); build, deployment and status-report jobs succeeded. Environment URL: https://vuphuc1996.github.io/Toeic/.
- Candidate only; no merge to `main` or production promotion decision.
- Candidate only; `main` remains unchanged at `256ca21461e78a7685bed773ddd622a64050e33a`.
- Installed-PWA/offline propagation and physical-device QA: **UNVERIFIED**.
- Production Deployment Accepted: **NOT GRANTED**.
