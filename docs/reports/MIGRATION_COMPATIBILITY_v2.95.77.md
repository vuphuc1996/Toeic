# Migration Compatibility Audit — TOEIC Dictionary v2.95.77

## Overview

This report documents the reconciliation of historical migration repair profiles (`releaseRepairProfiles` in `data/manifest.json` and `tools/tests/vocabulary-release-integrity.mjs`) for the 1,221-word inventory introduced in `v2.95.76` / `v2.95.77`.

## Cumulative Migration Profile Comparison

| Previous Snapshot Size | Previous Registered Additions | Extended Additions (Including Batch 028) | Status |
|---|---:|---:|---|
| **979** | 202 | **242** | Verified & Reconciled |
| **992** | 189 | **229** | Verified & Reconciled |
| **1,026** | 155 | **195** | Verified & Reconciled |
| **1,063** | 118 | **158** | Verified & Reconciled |
| **1,100** | 81 | **121** | Verified & Reconciled |
| **1,137** | 44 | **84** | Verified & Reconciled |
| **1,141** | 40 | **80** | Verified & Reconciled |
| **1,181** | — (New) | **40** (Batch 028) | Added & Verified |

## Safety & Invariant Rules

1. **Exact-match safety:** `detectLegacyReleaseAdditionRepair()` requires strict matching of `legacyBaseIds.size === previousTotalWords` and `currentTotalWords - previousTotalWords === releaseRepairProfile.releaseAdditionIds.length`.
2. **Zero false-positive triggers:** Partial deletion fingerprints, empty legacy records, or unknown snapshot sizes return empty arrays (`[]`).
3. **No vocabulary loss:** All 1,221 canonical headwords and historical release additions are preserved.
