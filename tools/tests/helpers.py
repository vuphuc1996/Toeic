"""Shared helpers: build a tiny synthetic project in a temp directory (never touches real data)."""
from __future__ import annotations

import copy
import json
import subprocess
import sys
from pathlib import Path

TOOLS = Path(__file__).resolve().parents[1]
VALIDATOR = TOOLS / "validate-data.py"
SYNC = TOOLS / "sync-version.py"

CATEGORIES = {"schemaVersion": 1, "categories": [
    {"id": "OFFICE", "label": "Văn phòng", "description": "x"},
    {"id": "TIME", "label": "Thời gian", "description": "x"},
]}
SHELL_EXCLUDE_PREFIXES = ("data/vocabulary/batch-", "data/verbs/irregular-verbs.json")


def rec(word: str, **over) -> dict:
    r = {
        "id": f"{word}-n",
        "word": word,
        "phonetic": {"us": "/ˈæl.fə/"},
        "senses": [{
            "pos": "n", "meaning_vi": "một thứ dùng để thử nghiệm",
            "definition_en": f"A thing that is used when checking item number {word.upper()}.",
            "synonyms": [], "antonyms": [], "cefr_level": "A1",
        }],
        "topics": ["OFFICE"],
        "word_family": [],
        "verb_forms": None,
        "examples": [{
            "en": f"We keep the {word} in the usual place on Monday.",
            "vi": f"Chúng tôi giữ {word} ở chỗ quen thuộc vào thứ Hai.",
        }],
        "collocations": [f"{word} test"],
        "cefr_level": "A1",
        "level_basis": "editorial-estimate",
    }
    r.update(over)
    return r


class Repo:
    """A synthetic project. Mutate .words / .manifest_over / .sw_over then call save()."""

    def __init__(self, tmp: Path):
        self.root = Path(tmp)
        self.words: dict[str, list[dict]] = {"A": [rec("alpha")], "B": [rec("bravo")]}
        self.manifest_over: dict = {}
        self.cache_name = "toeic-vocab-github-only-v1.0.0"
        self.sw_extra_paths: list[str] = []
        self.sw_omit: set[str] = set()
        self.extra_assets: list[str] = []
        self.save()

    def write(self, rel: str, text: str) -> None:
        p = self.root / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(text, encoding="utf-8")

    def dump(self, rel: str, doc: object) -> None:
        self.write(rel, json.dumps(doc, ensure_ascii=False, indent=2) + "\n")

    def save(self) -> None:
        letters = []
        for letter in sorted(self.words):
            self.dump(f"data/vocabulary/{letter}.json", {"letter": letter, "words": self.words[letter]})
            letters.append({"letter": letter, "file": f"./data/vocabulary/{letter}.json", "count": len(self.words[letter])})
        allrecs = [r for ws in self.words.values() for r in ws]
        cefr: dict[str, int] = {}
        for r in allrecs:
            cefr[r["cefr_level"]] = cefr.get(r["cefr_level"], 0) + 1
        manifest = {
            "schemaVersion": 1, "version": "1.0.0", "letters": letters, "categories": "./data/categories.json",
            "totalWords": len(allrecs), "cefrLevels": cefr, "totalTopics": len(CATEGORIES["categories"]),
        }
        manifest.update(self.manifest_over)
        self.dump("data/manifest.json", manifest)
        self.dump("data/categories.json", CATEGORIES)
        self.dump("data/related-terms.json", {"terms": [{"term": "x", "meaning_vi": "y"}]})
        self.write("assets/css/app.css", "body{}\n")
        self.write("assets/js/app.js", "console.log('x');\n")
        for extra in self.extra_assets:
            self.write(extra, "x")
        shell = ["./", "./index.html"]
        for sub in ("assets", "data"):
            for f in sorted((self.root / sub).rglob("*")):
                rp = f.relative_to(self.root).as_posix()
                if f.is_file() and not rp.startswith(SHELL_EXCLUDE_PREFIXES) and rp not in self.sw_omit:
                    shell.append("./" + rp)
        shell += self.sw_extra_paths
        self.write("index.html", "<html></html>\n")
        self.write("sw.js", f"const CACHE_NAME = '{self.cache_name}';\nconst APP_SHELL = {json.dumps(shell)};\n")

    def run(self, *args: str) -> tuple[int, str]:
        return run_tool(VALIDATOR, "--root", str(self.root), *args)

    def init_baseline(self, force: bool = False) -> tuple[int, str]:
        return self.run("--init-baseline", *(["--force"] if force else []))

    def baseline_path(self) -> Path:
        return self.root / "tools" / "quality-baseline.json"


def run_tool(script: Path, *args: str) -> tuple[int, str]:
    proc = subprocess.run([sys.executable, str(script), *args], capture_output=True, text=True, encoding="utf-8")
    return proc.returncode, proc.stdout + proc.stderr


def clone(obj):
    return copy.deepcopy(obj)

# Reading Part 7 source blocks that existed before v2.33.0. This snapshot keeps
# the historical v2.17 answer-position certificate scoped to its original 63 items
# while allowing later batches to append new questions to those same passages.
PART7_BASELINE_QUESTION_COUNTS_V232 = {
    'office-schedule': 3,
    'meeting-notice': 3,
    'business-travel': 3,
    'invoice-payment': 3,
    'shipping-update': 3,
    'job-opening': 3,
    'customer-service': 3,
    'facility-maintenance': 3,
    'customer-refund-email': 1,
    'facility-maintenance-notice': 1,
    'job-posting-analyst': 1,
    'supplier-invoice-followup': 1,
    'travel-itinerary': 1,
    'double-passage-order': 1,
    'training-announcement': 1,
    'triple-passage-meeting': 1,
    'part7-single-equipment-memo': 4,
    'part7-single-training-email': 4,
    'part7-double-order-delay': 4,
    'part7-triple-conference-arrangements': 5,
    'part7-double-equipment-order': 4,
    'part7-double-training-reimbursement': 4,
    'part7-triple-regional-sales-meeting': 3,
    'part7-triple-facility-renovation': 3,
}
