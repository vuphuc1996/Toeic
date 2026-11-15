# TOEIC Dictionary — Owner Design Brief

**Purpose:** collect design decisions before changing the canonical UI profile. This brief is a preference specification, not a second stylesheet. After approval, selections are translated into `design/design-profile.json`; the shared CSS is generated/validated through `tools/sync-design-profile.py`.

**Current implemented baseline:** `Calm Study Blue` — professional and calm, light neutral canvas, white surfaces, navy-blue primary actions, green positive progress, system font stack, comfortable text scale, balanced density, shared borders and subtle shadows.

Choose one option per row. Keep the current baseline where you do not want a change. You may add a custom value or an example in the final column. Nothing is treated as approved until the owner confirms.

| Parameter | Options | Current baseline | Your choice / custom value |
|---|---|---|---|
| Overall visual direction | A. Modern professional / B. Minimal clean / C. Friendly learning / D. Dense analytics workspace | A | |
| Main color | A. Navy-blue / B. Teal-green / C. Indigo-purple / D. Neutral charcoal | A | |
| Accent color | A. Green for progress / B. Cyan / C. Amber / D. Monochrome | A | |
| Background mode | A. Cool light canvas + white cards / B. Warm ivory + white cards / C. Dark mode / D. Light and dark themes | A | |
| Font family | A. System UI (fast, offline, platform-native) / B. Noto Sans (Vietnamese-first) / C. Inter (self-hosted asset required) / D. Other | A | |
| Typography size | A. Comfortable (body 15–16 px) / B. Large (16–17 px) / C. Compact (14–15 px) | A | |
| Card density | A. Airy (more whitespace) / B. Balanced / C. Compact | B | |
| Card appearance | A. Flat border / B. Soft shadow / C. Border + subtle shadow | C | |
| Corner radius | A. 10–12 px / B. 14–16 px / C. 18–22 px | B (card 16 / panel 18) | |
| Page width | A. Focused (max 1280 px) / B. Balanced (max 1440 px) / C. Wide (max 1600 px) | C | |
| Sidebar | A. Always full / B. Collapsible / C. Icon rail on tablet, full sidebar on desktop | C | |
| Motion | A. Nearly none / B. Subtle / C. More expressive | B | |
| Dashboard density | A. Spacious overview / B. Balanced metrics + content / C. Information dense | B | |
| TOEIC exam screen | A. Exam-like minimal / B. Modern app with helpful context / C. Split workspace | B | |

## Additional notes

- Reference apps/sites or colors you like:
- Things you dislike / want removed:
- Main device/browser used most often:
- Preferred body text size at 100% browser zoom:
- Preferred font weight (normal / medium / strong):
- Any accessibility needs for contrast or reading:
- Any other visual rule that must always be followed:

## Approval

- [ ] I approve the current `Calm Study Blue` baseline.
- [ ] Apply my answers and show a review/preview before replacing the baseline.
- [ ] I approve applying the updated profile across every module.

**Governance rule:** do not implement a private module theme while this brief is pending. If a new component is needed, use the existing semantic tokens and component recipes in `docs/DESIGN_SYSTEM.md`.
