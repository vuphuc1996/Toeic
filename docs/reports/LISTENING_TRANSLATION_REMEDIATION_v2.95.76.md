# Listening Translation Remediation — v2.95.76

**Baseline:** v2.95.75 · commit `d5648916cf62b3f07b1ffb9b98425c48ff3e63fe`  
**Change:** added Vietnamese transcript translations to 8 existing Listening units (4 Part 3 conversations and 4 Part 4 talks).

## Remediated resources

| Part | Resource ID | Translation |
|---|---|---|
| Part 3 | `batch026-part3-vendor-call` | Added |
| Part 3 | `batch026-part3-training-room` | Added |
| Part 3 | `batch026-part3-invoice-correction` | Added |
| Part 3 | `batch026-part3-access-card` | Added |
| Part 4 | `batch026-part4-building-notice` | Added |
| Part 4 | `batch026-part4-travel-update` | Added |
| Part 4 | `batch026-part4-product-launch` | Added |
| Part 4 | `batch026-part4-policy-reminder` | Added |

## Resulting coverage

- Part 3 transcript translations: 111/123 → **123/123** question contexts.
- Part 4 transcript translations: 90/102 → **102/102** question contexts.
- All 295 Listening questions now have a Vietnamese transcript translation available at unit level.
- Only `transcriptTranslation` was added. Unit IDs, question IDs, choice IDs, answer keys, transcript segments and editorial statuses were not changed.
- All 193 pre-existing Listening reserve questions remain excluded from Mock. No content was promoted to Mock by translation completion.
