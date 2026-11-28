#!/usr/bin/env python3
"""Report eligible Listening pools, pending reserves and two-form readiness."""
import collections, json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
data=json.loads((ROOT/"data/listening/listening-library.json").read_text(encoding="utf-8"))["listening"]
version=json.loads((ROOT/"data/manifest.json").read_text(encoding="utf-8"))["version"]
parts=("Part 1","Part 2","Part 3","Part 4")
eligible=[u for u in data if not u.get("editorialStatus") or u.get("editorialStatus")=="approved-for-mock"]
pending=[u for u in data if u.get("editorialStatus")=="reserve-pending-independent-review"]
def tally(items):
    c=collections.Counter()
    for u in items:
        c[u.get("part","Unknown")]+=sum(1 for q in u.get("questions",[]) if q.get("mockEligible") is not False)
    return c
e=tally(eligible); p=tally(pending); total=tally(data)
raw_total=sum(len(u.get("questions",[])) for u in data)
practice_only=raw_total-sum(total.values())
batches=collections.defaultdict(lambda: collections.Counter())
for u in pending: batches[u.get("editorialBatch","legacy")][u["part"]]+=len(u.get("questions",[]))
targets={"Part 1":12,"Part 2":50,"Part 3":78,"Part 4":60}
lines=[f"# Listening Readiness — v{version}","","> Đây là kiểm kê cấu trúc và trạng thái biên tập. Reserve chưa được người thứ hai duyệt vẫn bị loại khỏi Mock.","", "## Current pool", "", "| Part | Eligible | Pending review | Total available after approval | Target for two Full forms | Gap after approval |", "|---|---:|---:|---:|---:|---:|"]
for part in parts: lines.append(f"| {part} | {e[part]} | {p[part]} | {total[part]} | {targets[part]} | {max(0,targets[part]-total[part])} |")
lines += [f"| **Total** | **{sum(e.values())}** | **{sum(p.values())}** | **{sum(total.values())}** | **200** | **{sum(max(0,targets[k]-total[k]) for k in parts)}** |", "", "## Pending batches", "", "| Batch | Part 1 | Part 2 | Part 3 | Part 4 | Questions |", "|---|---:|---:|---:|---:|---:|"]
for batch in sorted(batches):
    c=batches[batch]; lines.append(f"| {batch} | {c['Part 1']} | {c['Part 2']} | {c['Part 3']} | {c['Part 4']} | {sum(c.values())} |")
batch_summary=', '.join(f'{name}={sum(counts.values())}' for name,counts in sorted(batches.items()))
lines += ["", "## Interpretation", "", f"- Current mock-eligible pool contains {sum(e.values())} questions; pending questions are excluded until independent review explicitly approves them. Additionally, {practice_only} Part 4 inference items carry `mockEligible: false` (practice-only; raw Listening inventory={raw_total} questions).", f"- Pending review by batch: {batch_summary or 'none'}; pending total={sum(p.values())}.", f"- If all pending questions were approved, the pool would contain {sum(total.values())} questions. Two Full forms require P1=12, P2=50, P3=78 and P4=60; projected part gaps: {', '.join(f'{k}={max(0,targets[k]-total[k])}' for k in parts)}.", f"- Current Part 1 dataset has {total['Part 1']} question records and follows the JPG-only contract with no SVG fallback. Photo sources are mixed: licensed Pexels and one AI-generated image with a separate provenance row. Existing repository-owned JPGs must remain intact.", "- This report is not a second-person editorial certification and does not claim native-speaker audio or ETS equivalence.", ""]
out=ROOT/f"docs/reports/TOEIC_LISTENING_READINESS_v{version}.md"; out.parent.mkdir(parents=True,exist_ok=True); out.write_text("\n".join(lines),encoding="utf-8")
print(out.relative_to(ROOT)); print(f"eligible={sum(e.values())}; pending={sum(p.values())}; practice_only={practice_only}; total={sum(total.values())}; raw_total={raw_total}")
