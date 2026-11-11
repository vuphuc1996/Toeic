#!/usr/bin/env python3
"""Validate the static TOEIC dictionary before publishing to GitHub Pages.

Rule tiers
  STRUCT  structural rules. A violation is always ERROR and is never excused by the baseline.
  DEBT    quality rules. A violation listed in tools/quality-baseline.json is a WARNING
          (known legacy debt); a violation that is NOT listed is an ERROR (regression).
  INFO    statistics only. Never fails the run.

The baseline identifies violations by (rule code, record id, JSON pointer), never by a
total count, so a new defect in one record cannot hide behind a fixed defect in another.
Running the validator never modifies the baseline. Use --init-baseline once and
--tighten-baseline (removes fixed entries only) in a reviewed commit.

Exit code: 0 = no ERROR, 1 = at least one ERROR.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
import unicodedata
from collections import Counter, defaultdict
from pathlib import Path

CEFR_LEVELS = ("A1", "A2", "B1", "B2", "C1")
REQUIRED_RECORD_KEYS = (
    "id", "word", "phonetic", "senses", "topics", "word_family", "verb_forms",
    "examples", "collocations", "cefr_level", "level_basis",
)
VERB_FORM_KEYS = ("v1", "vs_es", "v2", "v3", "ving")
# IPA alphabet currently used by the dictionary. A new symbol is an ERROR until reviewed
# and added here on purpose (IP002).
IPA_ALLOWED = set(" ()./;abdefhijklmnoprstuvwzæðŋɑɔəɚɝɡɪʃʊʌʒˈˌː\u032cθ")
IPA_VOWELS = set("aeiouæɑɔəɚɪʊʌɝ")
# Files under assets/ and data/ that are intentionally not part of the offline shell (SW002).
SHELL_EXCLUDE = (
    re.compile(r"^data/vocabulary/batch-\d+\.json$"),
    re.compile(r"^data/verbs/irregular-verbs\.json$"),
)
SW_ASSET_EXT = r"(?:png|svg|webp|jpg|jpeg|ico|json|js|css|webmanifest)"

# Rule registry: code -> (tier, description). Parameters that change what a DEBT rule
# detects live in RULE_PARAMS and are snapshotted in the baseline (RULE-DRIFT guard).
RULES = {
    "DQ001": ("STRUCT", "JSON hợp lệ và đọc được"),
    "DQ002": ("STRUCT", "ID và headword duy nhất, không rỗng, đúng file chữ cái"),
    "DQ003": ("STRUCT", "Không mất ID so với tools/baseline-ids.json; baseline-ids phải toàn vẹn (count, SHA-256, không trùng)"),
    "DQ004": ("STRUCT", "Đúng kiểu dữ liệu và đủ field bắt buộc"),
    "DQ005": ("STRUCT", "Manifest khớp dữ liệu thực tế"),
    "DQ006": ("STRUCT", "related-terms.json hợp lệ"),
    "VF001": ("STRUCT", "Mọi bản ghi có sense động từ phải có verb_forms"),
    "VF002": ("STRUCT", "verb_forms.v1 phải khớp headword"),
    "FD003": ("STRUCT", "Mọi bản ghi có sense động từ phải có ít nhất một collocation"),
    "EX001": ("STRUCT", "Mỗi từ có ít nhất một ví dụ"),
    "EX002": ("STRUCT", "Ví dụ có en và vi không rỗng"),
    "EX003": ("STRUCT", "Không trùng nguyên văn câu ví dụ tiếng Anh"),
    "EX010": ("STRUCT", "sense_index của ví dụ phải trỏ tới một sense hợp lệ"),
    "EX011": ("STRUCT", "Mỗi sense phải có ít nhất một ví dụ được gắn đúng nghĩa"),
    "DF001": ("STRUCT", "definition_en và meaning_vi không rỗng"),
    "IP002": ("STRUCT", "IPA chỉ chứa ký tự trong bảng cho phép"),
    "CE001": ("STRUCT", "CEFR thuộc A1–C1"),
    "TP001": ("STRUCT", "Topic tồn tại và mỗi từ có ít nhất một topic"),
    "SW001": ("STRUCT", "Mọi đường dẫn trong danh sách cache của sw.js tồn tại"),
    "SW003": ("STRUCT", "Tên cache có tiền tố toeic-vocab- và khớp phiên bản manifest"),
    "DF002": ("DEBT", "Định nghĩa giả: bắt đầu bằng headword + dấu — / : / -"),
    "DF003": ("DEBT", "definition_en chứa ký tự đặc trưng tiếng Việt (NFD)"),
    "DF004": ("DEBT", "Định nghĩa bắt đầu bằng chính headword"),
    "DF005": ("DEBT", "Nhiều sense trong một từ dùng chung định nghĩa"),
    "EX004": ("DEBT", "Câu ví dụ tiếng Anh theo khuôn (lặp sau khi che headword)"),
    "EX005": ("DEBT", "Bản dịch ví dụ theo khuôn (lặp sau khi che headword/nghĩa)"),
    "EX006": ("DEBT", "Ví dụ không chứa headword hoặc biến thể"),
    "EX009": ("DEBT", "Bản dịch ví dụ không có tiếng Việt hoặc trùng câu tiếng Anh"),
    "IP001": ("DEBT", "IPA không đúng dạng /…/ đơn"),
    "IP003": ("DEBT", "IPA nhiều âm tiết không có dấu nhấn"),
    "IP004": ("DEBT", "IPA dùng 'ər' thay cho ɝ/ɚ"),
    "FD001": ("DEBT", "Collocation không chứa headword"),
    "TP002": ("DEBT", "Tệp assets/ được nhắc trong mã nguồn nhưng không tồn tại"),
    "SW002": ("DEBT", "Tệp assets/ hoặc data/ chưa có trong danh sách cache của sw.js"),
    "EX008": ("INFO", "Câu ví dụ dưới 5 từ"),
    "DF006": ("INFO", "Định nghĩa trùng giữa các từ khác nhau"),
    "IP006": ("INFO", "Từ chưa có IPA"),
    "FD002": ("INFO", "Từ đồng/trái nghĩa chưa có nghĩa trong related-terms"),
    "CE002": ("INFO", "CEFR cấp từ khác CEFR cấp sense"),
    "CE003": ("INFO", "Từ C1 và nguồn xếp mức"),
}
RULE_PARAMS = {
    "DF002": {"pattern": "headword + [—–:-]"},
    "DF003": {"markers": "đ ơ ư ă, dot-below, hook-above, tilde, circumflex+tone"},
    "DF004": {"match": "case-insensitive prefix at word boundary"},
    "DF005": {"scope": "same record, casefold"},
    "EX004": {"minRepeat": 3, "mask": "headword + suffix up to word end"},
    "EX005": {"minRepeat": 3, "mask": "headword + meaning_vi parts"},
    "EX006": {"match": "token stem + up to 4 letters"},
    "EX009": {"rule": "no Vietnamese letters or equal to en"},
    "IP001": {"regex": "^/[^/;()\\[\\]]+/$"},
    "IP003": {"minVowelGroups": 2},
    "IP004": {"substring": "ər"},
    "FD001": {"match": "token stem + up to 4 letters"},
    "TP002": {"scan": "assets/js/*.js, index.html, assets/css/*.css; literal assets/ paths and topic file: names"},
    "SW002": {"exclude": [p.pattern for p in SHELL_EXCLUDE]},
}


class Violation:
    __slots__ = ("code", "rid", "at", "msg")

    def __init__(self, code: str, rid: str, at: str, msg: str):
        self.code, self.rid, self.at, self.msg = code, rid, at, msg

    @property
    def key(self) -> tuple[str, str, str]:
        return (self.code, self.rid, self.at)


class Context:
    def __init__(self, root: Path):
        self.root = root
        self.violations: list[Violation] = []
        self.info: dict[str, object] = {}
        self.records: list[dict] = []
        self.manifest: dict = {}
        self.category_ids: set[str] = set()
        self.related_terms: set[str] = set()

    def add(self, code: str, rid: str, at: str, msg: str) -> None:
        self.violations.append(Violation(code, rid, at, msg))


def read_json(ctx: Context, path: Path, rid: str) -> object | None:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:  # noqa: BLE001 - report any read/parse failure
        ctx.add("DQ001", rid, "", f"không đọc được {path.relative_to(ctx.root).as_posix()}: {exc}")
        return None


def rel(ctx: Context, p: str) -> Path:
    return ctx.root / p.replace("./", "", 1) if p.startswith("./") else ctx.root / p


# ---------------------------------------------------------------- text helpers
def stem_pattern(token: str) -> str:
    t = token.lower()
    if len(t) <= 3:
        return r"\b" + re.escape(t) + r"(?:s|es|ed|d|ing)?\b"
    root = t[:-1] if t[-1] in "ey" else t
    return r"\b" + re.escape(root) + r"\w{0,4}\b"


def contains_headword(text: str, word: str) -> bool:
    low = text.lower()
    return all(re.search(stem_pattern(tok), low) for tok in re.findall(r"[\w'-]+", word.lower()))


def has_vietnamese_strong(text: str) -> bool:
    """Marks that do not occur in ordinary English loanwords (cafe, naive, resume...)."""
    if re.search("[đĐ]", text):
        return True
    for ch in unicodedata.normalize("NFD", text):
        if ch in ("\u031b", "\u0306", "\u0323", "\u0309"):  # horn, breve, dot below, hook above
            return True
    nfd = unicodedata.normalize("NFD", text)
    if re.search(r"[aeiouyAEIOUY]\u0303", nfd):  # tilde on a vowel
        return True
    if re.search(r"[aeoAEO]\u0302[\u0300\u0301\u0303\u0309]", nfd):  # circumflex + tone
        return True
    return False


def has_any_diacritic_letter(text: str) -> bool:
    return any(ord(ch) > 127 and unicodedata.category(ch).startswith("L") for ch in text)


def mask_en(rec: dict, text: str) -> str:
    s = re.sub(r"\b" + re.escape(rec["word"].lower()) + r"\w*\b", "◊", text.lower())
    return re.sub(r"\s+", " ", s).strip()


def mask_vi(rec: dict, text: str) -> str:
    s = text.lower()
    for sense in rec.get("senses", []):
        for part in re.split(r"[;,/]", str(sense.get("meaning_vi", "")).lower()):
            part = part.strip().rstrip(".")
            if len(part) >= 2:
                s = s.replace(part, "◊")
    s = re.sub(r"\b" + re.escape(rec["word"].lower()) + r"\w*\b", "◊", s)
    return re.sub(r"\s+", " ", s).strip()


def is_str_list(value: object) -> bool:
    return isinstance(value, list) and all(isinstance(x, str) for x in value)


def has_verb_sense(record: dict) -> bool:
    senses = record.get("senses", [])
    if not isinstance(senses, list):
        return False
    return any(
        isinstance(sense, dict) and "v" in re.split(r"[/,\\s]+", str(sense.get("pos", "")).lower())
        for sense in senses
    )


# ---------------------------------------------------------------- data loading
def load_manifest_and_records(ctx: Context) -> None:
    mpath = ctx.root / "data" / "manifest.json"
    manifest = read_json(ctx, mpath, "manifest")
    if not isinstance(manifest, dict):
        return
    ctx.manifest = manifest
    cat_rel = manifest.get("categories")
    if isinstance(cat_rel, str):
        cdoc = read_json(ctx, rel(ctx, cat_rel), "categories")
        if isinstance(cdoc, dict):
            ctx.category_ids = {c.get("id") for c in cdoc.get("categories", []) if isinstance(c, dict)}
    else:
        ctx.add("DQ005", "manifest", "/categories", "thiếu đường dẫn categories")

    seen_ids: set[str] = set()
    seen_words: set[str] = set()
    letters = manifest.get("letters")
    if not isinstance(letters, list):
        ctx.add("DQ005", "manifest", "/letters", "letters phải là mảng")
        return
    total = 0
    for item in letters:
        if not isinstance(item, dict):
            ctx.add("DQ005", "manifest", "/letters", "mỗi phần tử letters phải là object")
            continue
        letter = str(item.get("letter", "?"))
        file_rel = str(item.get("file", ""))
        doc = read_json(ctx, rel(ctx, file_rel), letter)
        if not isinstance(doc, dict):
            continue
        if doc.get("letter") != letter:
            ctx.add("DQ005", letter, "/letter", f"trường letter của {file_rel} không khớp manifest")
        words = doc.get("words")
        if not isinstance(words, list):
            ctx.add("DQ004", letter, "/words", "words phải là mảng")
            continue
        if len(words) != item.get("count"):
            ctx.add("DQ005", letter, "/count", f"manifest count {item.get('count')} != thực tế {len(words)}")
        for entry in words:
            if not isinstance(entry, dict):
                ctx.add("DQ004", letter, "/words", "bản ghi phải là object")
                continue
            total += 1
            word = str(entry.get("word", "")).strip()
            wid = str(entry.get("id", "")).strip()
            label = wid or word or f"{letter}#{total}"
            if not word:
                ctx.add("DQ002", label, "/word", "headword rỗng")
                continue
            if word[0].upper() != letter:
                ctx.add("DQ002", label, "/word", f"{word} nằm trong file {letter}")
            if not wid:
                ctx.add("DQ002", word, "/id", "thiếu id")
            elif wid in seen_ids:
                ctx.add("DQ002", wid, "/id", f"id trùng: {wid}")
            seen_ids.add(wid)
            if word.casefold() in seen_words:
                ctx.add("DQ002", label, "/word", f"headword trùng: {word}")
            seen_words.add(word.casefold())
            ctx.records.append(entry)
    ctx.info["total_records"] = total


# ---------------------------------------------------------------- STRUCT rules
def check_schema(ctx: Context) -> None:
    for r in ctx.records:
        rid = str(r.get("id", r.get("word", "?")))
        for key in REQUIRED_RECORD_KEYS:
            if key not in r:
                ctx.add("DQ004", rid, f"/{key}", f"thiếu field bắt buộc {key}")
        for key in ("id", "word", "cefr_level", "level_basis"):
            if key in r and not isinstance(r[key], str):
                ctx.add("DQ004", rid, f"/{key}", f"{key} phải là chuỗi")
        ph = r.get("phonetic")
        if "phonetic" in r and not (isinstance(ph, dict) and all(isinstance(v, str) for v in ph.values())):
            ctx.add("DQ004", rid, "/phonetic", "phonetic phải là object chứa chuỗi")
        if "topics" in r and not is_str_list(r["topics"]):
            ctx.add("DQ004", rid, "/topics", "topics phải là mảng chuỗi")
        if "collocations" in r and not is_str_list(r["collocations"]):
            ctx.add("DQ004", rid, "/collocations", "collocations phải là mảng chuỗi")
        wf = r.get("word_family")
        if "word_family" in r:
            if not isinstance(wf, list) or not all(
                isinstance(x, dict) and all(isinstance(x.get(k), str) for k in ("word", "pos", "meaning_vi")) for x in wf
            ):
                ctx.add("DQ004", rid, "/word_family", "word_family phải là mảng {word,pos,meaning_vi}")
        vf = r.get("verb_forms")
        if "verb_forms" in r and vf is not None:
            if not (isinstance(vf, dict) and all(isinstance(vf.get(k), str) for k in VERB_FORM_KEYS)):
                ctx.add("DQ004", rid, "/verb_forms", "verb_forms phải là null hoặc object đủ v1, vs_es, v2, v3, ving")
        senses = r.get("senses")
        if not isinstance(senses, list) or not senses:
            ctx.add("DQ004", rid, "/senses", "senses phải là mảng không rỗng")
            senses = []
        for i, s in enumerate(senses):
            at = f"/senses/{i}"
            if not isinstance(s, dict):
                ctx.add("DQ004", rid, at, "sense phải là object")
                continue
            for key in ("pos", "meaning_vi", "definition_en", "cefr_level"):
                if not isinstance(s.get(key), str):
                    ctx.add("DQ004", rid, f"{at}/{key}", f"{key} phải là chuỗi")
            for key in ("synonyms", "antonyms"):
                if not is_str_list(s.get(key)):
                    ctx.add("DQ004", rid, f"{at}/{key}", f"{key} phải là mảng chuỗi")
        ex = r.get("examples")
        if "examples" in r:
            if not isinstance(ex, list) or not all(
                isinstance(e, dict) and isinstance(e.get("en"), str) and isinstance(e.get("vi"), str) for e in ex
            ):
                ctx.add("DQ004", rid, "/examples", "examples phải là mảng {en, vi} kiểu chuỗi")
        if has_verb_sense(r):
            if vf is None:
                ctx.add("VF001", rid, "/verb_forms", "có sense POS động từ nhưng chưa có verb_forms")
            elif isinstance(vf, dict) and vf.get("v1") != r.get("word"):
                ctx.add("VF002", rid, "/verb_forms/v1", "v1 không khớp headword")
            collocations = r.get("collocations")
            if not isinstance(collocations, list) or not collocations:
                ctx.add("FD003", rid, "/collocations", "có sense POS động từ nhưng chưa có collocation")


def check_struct_content(ctx: Context) -> None:
    en_seen: dict[str, str] = {}
    for r in ctx.records:
        rid = str(r.get("id", r.get("word", "?")))
        senses = [s for s in r.get("senses", []) if isinstance(s, dict)] if isinstance(r.get("senses"), list) else []
        for i, s in enumerate(senses):
            for key in ("definition_en", "meaning_vi"):
                if isinstance(s.get(key), str) and not s[key].strip():
                    ctx.add("DF001", rid, f"/senses/{i}/{key}", f"{key} rỗng")
            lvl = s.get("cefr_level")
            if isinstance(lvl, str) and lvl not in CEFR_LEVELS:
                ctx.add("CE001", rid, f"/senses/{i}/cefr_level", f"CEFR không hợp lệ: {lvl}")
        lvl = r.get("cefr_level")
        if isinstance(lvl, str) and lvl not in CEFR_LEVELS:
            ctx.add("CE001", rid, "/cefr_level", f"CEFR không hợp lệ: {lvl}")
        topics = r.get("topics")
        if isinstance(topics, list):
            if not topics:
                ctx.add("TP001", rid, "/topics", "từ không có topic nào")
            for t in topics:
                if t not in ctx.category_ids:
                    ctx.add("TP001", rid, "/topics", f"topic không tồn tại: {t}")
        ex = r.get("examples")
        if isinstance(ex, list):
            if not ex:
                ctx.add("EX001", rid, "/examples", "không có ví dụ")
            covered_senses: set[int] = set()
            for i, e in enumerate(ex):
                if not isinstance(e, dict):
                    continue
                for key in ("en", "vi"):
                    if isinstance(e.get(key), str) and not e[key].strip():
                        ctx.add("EX002", rid, f"/examples/{i}/{key}", f"ví dụ {key} rỗng")
                sense_index = e.get("sense_index", 0)
                if type(sense_index) is not int or sense_index < 0 or sense_index >= len(senses):
                    ctx.add("EX010", rid, f"/examples/{i}/sense_index", "sense_index không trỏ tới sense hợp lệ")
                else:
                    covered_senses.add(sense_index)
                en = e.get("en")
                if isinstance(en, str) and en.strip():
                    if en in en_seen and en_seen[en] != rid:
                        ctx.add("EX003", rid, f"/examples/{i}/en", f"câu trùng với {en_seen[en]}")
                    en_seen.setdefault(en, rid)
            for sense_index in range(len(senses)):
                if sense_index not in covered_senses:
                    ctx.add("EX011", rid, f"/senses/{sense_index}", "sense chưa có ví dụ minh họa riêng")
        ph = r.get("phonetic")
        if isinstance(ph, dict):
            for key, val in ph.items():
                if isinstance(val, str):
                    bad = sorted({ch for ch in val if ch not in IPA_ALLOWED})
                    if bad:
                        ctx.add("IP002", rid, f"/phonetic/{key}", "ký tự IPA chưa được phép: " + " ".join(bad))


def check_manifest(ctx: Context) -> None:
    m = ctx.manifest
    if not m:
        return
    version = m.get("version")
    if not (isinstance(version, str) and re.fullmatch(r"\d+\.\d+\.\d+", version)):
        ctx.add("DQ005", "manifest", "/version", f"version phải dạng x.y.z, hiện là {version!r}")
    total = ctx.info.get("total_records", 0)
    if m.get("totalWords") != total:
        ctx.add("DQ005", "manifest", "/totalWords", f"totalWords {m.get('totalWords')} != thực tế {total}")
    if "wordCount" in m and m["wordCount"] != total:
        ctx.add("DQ005", "manifest", "/wordCount", f"wordCount {m['wordCount']} != thực tế {total}")
    if "totalTopics" in m and m["totalTopics"] != len(ctx.category_ids):
        ctx.add("DQ005", "manifest", "/totalTopics", f"totalTopics {m['totalTopics']} != {len(ctx.category_ids)}")
    if "cefrLevels" in m:
        actual = Counter(r.get("cefr_level") for r in ctx.records)
        declared = m["cefrLevels"] if isinstance(m["cefrLevels"], dict) else {}
        if {k: v for k, v in declared.items() if v} != {k: v for k, v in actual.items() if v}:
            ctx.add("DQ005", "manifest", "/cefrLevels", f"cefrLevels {declared} != thực tế {dict(actual)}")
    if isinstance(m.get("letters"), list):
        counted = sum(i.get("count", 0) for i in m["letters"] if isinstance(i, dict) and isinstance(i.get("count"), int))
        if counted != m.get("totalWords"):
            ctx.add("DQ005", "manifest", "/letters", f"tổng count {counted} != totalWords {m.get('totalWords')}")


def check_related_terms(ctx: Context) -> None:
    doc = read_json(ctx, ctx.root / "data" / "related-terms.json", "related-terms")
    if not isinstance(doc, dict):
        return
    seen: set[str] = set()
    for entry in doc.get("terms", []):
        term = str(entry.get("term", "")).strip().casefold()
        meaning = str(entry.get("meaning_vi", "")).strip()
        if not term or not meaning:
            ctx.add("DQ006", term or "?", "", "related-terms: mỗi mục cần term và meaning_vi")
        if term in seen:
            ctx.add("DQ006", term, "", f"related-terms: trùng term {term}")
        seen.add(term)
    ctx.related_terms = seen


def id_set_sha256(ids: list[str]) -> str:
    return hashlib.sha256("\n".join(sorted(ids)).encode("utf-8")).hexdigest()


def load_baseline_ids(ids_path: Path) -> tuple[list[str] | None, list[str]]:
    """Read tools/baseline-ids.json and verify the file's own integrity.

    Returns (ids, problems). Any problem means the list cannot be trusted: callers must not
    derive "added" or "missing" IDs from it (a damaged list would make real IDs look new).
    """
    name = ids_path.name
    if not ids_path.exists():
        return None, [f"không có {name}; chạy --init-baseline một lần"]
    try:
        doc = json.loads(ids_path.read_text(encoding="utf-8"))
    except Exception as exc:  # noqa: BLE001
        return None, [f"{name} không đọc được: {exc}"]
    if not isinstance(doc, dict):
        return None, [f"{name}: gốc của file phải là object"]
    ids = doc.get("ids")
    if not isinstance(ids, list) or not all(isinstance(x, str) and x.strip() for x in ids):
        return None, [f"{name}: ids phải là mảng chuỗi không rỗng"]
    problems: list[str] = []
    if doc.get("schemaVersion") != 1:
        problems.append(f"{name}: schemaVersion phải là 1, hiện là {doc.get('schemaVersion')!r}")
    dups = sorted(k for k, c in Counter(ids).items() if c > 1)
    if dups:
        shown = ", ".join(dups[:5]) + (f" … (+{len(dups) - 5})" if len(dups) > 5 else "")
        problems.append(f"{name}: ID trùng trong danh sách baseline: {shown}")
    count = doc.get("count")
    if isinstance(count, bool) or not isinstance(count, int) or count != len(ids):
        problems.append(f"{name}: count {count!r} không khớp số ID thực tế {len(ids)}")
    if doc.get("idSetSha256") != id_set_sha256(ids):
        problems.append(f"{name}: idSetSha256 không khớp SHA-256 tính từ chính danh sách ids")
    return ids, problems


def check_ids_against_baseline(ctx: Context, ids_path: Path, allow_remove: set[str]) -> None:
    current = [str(r.get("id", "")) for r in ctx.records]
    ctx.info["id_set_sha256"] = id_set_sha256(current)
    base_ids, problems = load_baseline_ids(ids_path)
    ctx.info["ids_baseline_valid"] = not problems
    for problem in problems:
        ctx.add("DQ003", "baseline-ids", "", problem)
    if problems or base_ids is None:
        return  # untrusted list: report structural errors only, never "added"/"missing" IDs
    cur_set = set(current)
    missing = sorted(set(base_ids) - cur_set)
    added = sorted(cur_set - set(base_ids))
    ctx.info["ids_missing"] = missing
    ctx.info["ids_added"] = added
    for mid in missing:
        if mid in allow_remove:
            continue
        ctx.add("DQ003", mid, "", "ID có trong baseline nhưng đã mất (dùng --allow-remove nếu cố ý)")


def parse_sw_lists(sw_text: str) -> dict[str, list[str]]:
    lists: dict[str, list[str]] = {}
    for name in ("APP_SHELL", "REQUIRED", "OPTIONAL"):
        m = re.search(r"const\s+" + name + r"\s*=\s*(\[.*?\])\s*;", sw_text, re.S)
        if m:
            lists[name] = json.loads(m.group(1))
    return lists


def check_service_worker(ctx: Context) -> None:
    sw_path = ctx.root / "sw.js"
    if not sw_path.exists():
        ctx.add("SW001", "sw.js", "", "không có sw.js")
        return
    text = sw_path.read_text(encoding="utf-8")
    try:
        lists = parse_sw_lists(text)
    except Exception as exc:  # noqa: BLE001
        ctx.add("SW001", "sw.js", "", f"không phân tích được danh sách cache (cần mảng JSON thuần): {exc}")
        return
    if not lists:
        ctx.add("SW001", "sw.js", "", "không tìm thấy APP_SHELL hoặc REQUIRED/OPTIONAL")
        return
    listed: set[str] = set()
    for name, paths in lists.items():
        for p in paths:
            listed.add(p.replace("./", "", 1) if p.startswith("./") else p)
            if p in ("./", "/"):
                continue
            if not rel(ctx, p).exists():
                # OPTIONAL resources may legitimately be absent from a source snapshot.
                # Required app-shell resources remain hard errors; Part 1 photo binaries
                # are additionally enforced by the strict photo release validator in CI.
                if name == "OPTIONAL":
                    continue
                ctx.add("SW001", p, f"/{name}", f"{name} nhắc tới tệp không tồn tại")
    for sub in ("assets", "data"):
        base = ctx.root / sub
        if not base.exists():
            continue
        for f in sorted(base.rglob("*")):
            if not f.is_file() or f.name.startswith("."):
                continue
            rp = f.relative_to(ctx.root).as_posix()
            if any(p.match(rp) for p in SHELL_EXCLUDE):
                continue
            if rp not in listed:
                ctx.add("SW002", rp, "", "tệp chưa có trong danh sách cache của sw.js")
    manifest_version = ctx.manifest.get("version")
    cache_match = re.search(r"CACHE_NAME\s*=\s*([`'\"])(.*?)\1", text)
    if not cache_match:
        ctx.add("SW003", "sw.js", "", "không tìm thấy CACHE_NAME")
        return
    cache_name = cache_match.group(2)
    if not cache_name.startswith("toeic-vocab-"):
        ctx.add("SW003", "sw.js", "", f"CACHE_NAME phải bắt đầu bằng toeic-vocab-: {cache_name}")
    if "${VERSION}" in cache_name:
        vm = re.search(r"const\s+VERSION\s*=\s*['\"]([^'\"]+)['\"]", text)
        if not vm or vm.group(1) != manifest_version:
            ctx.add("SW003", "sw.js", "", f"VERSION {vm.group(1) if vm else None!r} != manifest {manifest_version!r}")
    elif not cache_name.endswith("v" + str(manifest_version)):
        ctx.add("SW003", "sw.js", "", f"CACHE_NAME {cache_name!r} không khớp phiên bản manifest {manifest_version!r}")


# ---------------------------------------------------------------- DEBT / INFO rules
def check_debt_and_info(ctx: Context) -> None:
    en_counts: Counter = Counter()
    vi_counts: Counter = Counter()
    en_keys: dict[tuple[str, int], str] = {}
    vi_keys: dict[tuple[str, int], str] = {}
    defs_by_text: dict[str, set[str]] = defaultdict(set)
    syn_terms: set[str] = set()
    headwords = {str(r.get("word", "")).lower() for r in ctx.records}
    coverage: Counter = Counter()
    short_examples = 0
    for r in ctx.records:
        if not all(k in r for k in ("id", "word", "senses", "examples")):
            continue
        rid, word = str(r["id"]), str(r["word"])
        if not (isinstance(r["senses"], list) and isinstance(r["examples"], list)):
            continue
        senses = [s for s in r["senses"] if isinstance(s, dict)]
        examples = [e for e in r["examples"] if isinstance(e, dict)]
        # definitions
        seen_defs: dict[str, int] = {}
        for i, s in enumerate(senses):
            d = s.get("definition_en")
            if not isinstance(d, str):
                continue
            at = f"/senses/{i}/definition_en"
            if re.match(r"^\s*" + re.escape(word) + r"\s*[—–:\-]\s*\S", d, re.I):
                ctx.add("DF002", rid, at, f"định nghĩa giả: {d[:60]!r}")
            if has_vietnamese_strong(d):
                ctx.add("DF003", rid, at, f"có tiếng Việt: {d[:60]!r}")
            if re.match(r"^\s*" + re.escape(word) + r"\b", d, re.I):
                ctx.add("DF004", rid, at, "định nghĩa bắt đầu bằng headword")
            norm = re.sub(r"\s+", " ", d.strip().casefold())
            if norm and norm in seen_defs:
                ctx.add("DF005", rid, at, f"trùng định nghĩa với sense {seen_defs[norm]}")
            seen_defs.setdefault(norm, i)
            if norm:
                defs_by_text[norm].add(rid)
            for key in ("synonyms", "antonyms"):
                if isinstance(s.get(key), list):
                    syn_terms.update(x.lower() for x in s[key] if isinstance(x, str))
        # examples
        for i, e in enumerate(examples):
            en, vi = e.get("en"), e.get("vi")
            if isinstance(en, str):
                k = mask_en(r, en)
                en_counts[k] += 1
                en_keys[(rid, i)] = k
                if not contains_headword(en, word):
                    ctx.add("EX006", rid, f"/examples/{i}/en", "ví dụ không chứa headword/biến thể")
                if len(en.split()) < 5:
                    short_examples += 1
            if isinstance(vi, str):
                k = mask_vi(r, vi)
                vi_counts[k] += 1
                vi_keys[(rid, i)] = k
                if not has_any_diacritic_letter(vi) or (isinstance(en, str) and vi.strip() == en.strip()):
                    ctx.add("EX009", rid, f"/examples/{i}/vi", "bản dịch không có tiếng Việt hoặc trùng câu EN")
        # IPA
        ph = r.get("phonetic")
        us = ph.get("us") if isinstance(ph, dict) else None
        if isinstance(us, str):
            if not us.strip():
                coverage["ipa_missing"] += 1
            else:
                coverage["ipa"] += 1
                if not re.fullmatch(r"/[^/;()\[\]]+/", us):
                    ctx.add("IP001", rid, "/phonetic/us", f"IPA không đúng dạng /…/ đơn: {us[:50]!r}")
                if "ər" in us:
                    ctx.add("IP004", rid, "/phonetic/us", f"dùng 'ər': {us}")
                groups = len(re.findall(r"[aeiouæɑɔəɚɪʊʌɝ]+ː?", us))
                if groups >= 2 and "ˈ" not in us and re.fullmatch(r"/[^/;()\[\]]+/", us):
                    ctx.add("IP003", rid, "/phonetic/us", f"nhiều âm tiết nhưng không có dấu nhấn: {us}")
        # collocations
        for i, c in enumerate(r.get("collocations", []) if isinstance(r.get("collocations"), list) else []):
            if isinstance(c, str) and not contains_headword(c, word):
                ctx.add("FD001", rid, f"/collocations/{i}", f"collocation không chứa headword: {c!r}")
        # coverage + CEFR
        coverage["records"] += 1
        coverage["word_family"] += bool(r.get("word_family"))
        coverage["verb_forms"] += bool(r.get("verb_forms"))
        coverage["collocations"] += bool(r.get("collocations"))
        coverage["synonyms"] += any(s.get("synonyms") for s in senses)
        coverage["antonyms"] += any(s.get("antonyms") for s in senses)
        coverage["multi_sense"] += len(senses) > 1
        if any(s.get("cefr_level") != r.get("cefr_level") for s in senses):
            coverage["cefr_word_sense_mismatch"] += 1
        if r.get("cefr_level") == "C1":
            coverage["c1"] += 1
    min_en = RULE_PARAMS["EX004"]["minRepeat"]
    min_vi = RULE_PARAMS["EX005"]["minRepeat"]
    for (rid, i), k in en_keys.items():
        if en_counts[k] >= min_en:
            ctx.add("EX004", rid, f"/examples/{i}/en", f"câu khuôn ({en_counts[k]} lần): {k[:60]!r}")
    for (rid, i), k in vi_keys.items():
        if vi_counts[k] >= min_vi:
            ctx.add("EX005", rid, f"/examples/{i}/vi", f"bản dịch khuôn ({vi_counts[k]} lần): {k[:60]!r}")
    ctx.info["short_examples"] = short_examples
    ctx.info["duplicate_definitions_across_records"] = sum(1 for ids in defs_by_text.values() if len(ids) > 1)
    ctx.info["syn_ant_terms"] = len(syn_terms)
    ctx.info["syn_ant_without_gloss"] = len([t for t in syn_terms if t not in ctx.related_terms and t not in headwords])
    ctx.info["coverage"] = dict(coverage)


def check_asset_references(ctx: Context) -> None:
    """TP002: asset files the code points at must exist (literal paths and topic `file:` names)."""
    scan = sorted((ctx.root / "assets" / "js").glob("*.js")) + sorted((ctx.root / "assets" / "css").glob("*.css"))
    index = ctx.root / "index.html"
    if index.exists():
        scan.append(index)
    literal = re.compile(r"""['"(]\.?/?(assets/[^'")\s`$]+?\.""" + SW_ASSET_EXT + r")")
    topic_file = re.compile(r"""\bfile\s*:\s*['"]([\w.-]+\.(?:webp|svg|png|jpg|jpeg))['"]""")
    seen: set[tuple[str, str]] = set()
    checked = 0
    for f in scan:
        text = f.read_text(encoding="utf-8", errors="replace")
        targets = [m.group(1) for m in literal.finditer(text)]
        if f.suffix == ".js":
            targets += ["assets/topics/" + m.group(1) for m in topic_file.finditer(text)]
        for target in targets:
            key = (f.name, target)
            if key in seen:
                continue
            seen.add(key)
            checked += 1
            if not (ctx.root / target).exists():
                ctx.add("TP002", target, f"/{f.name}", f"{f.name} nhắc tới {target} nhưng tệp không tồn tại")
    ctx.info["asset_references_checked"] = checked


# ---------------------------------------------------------------- baseline handling
def build_baseline(ctx: Context) -> dict:
    rules: dict[str, dict] = {}
    for code, (tier, _desc) in RULES.items():
        if tier != "DEBT":
            continue
        entries = sorted({(v.rid, v.at) for v in ctx.violations if v.code == code})
        rules[code] = {
            "params": RULE_PARAMS.get(code, {}),
            "violations": [{"id": rid, "at": at} for rid, at in entries],
        }
    return {
        "schemaVersion": 1,
        "createdFrom": {
            "version": ctx.manifest.get("version"),
            "totalWords": ctx.info.get("total_records"),
            "idSetSha256": ctx.info.get("id_set_sha256"),
        },
        "note": "Nợ chất lượng đã biết. Không sửa tay; chỉ siết lại bằng --tighten-baseline trong commit được duyệt.",
        "rules": rules,
    }


def load_baseline(path: Path) -> dict | None:
    if not path.exists():
        return None
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, doc: object) -> None:
    path.write_text(json.dumps(doc, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


# ---------------------------------------------------------------- reporting
def evaluate(ctx: Context, baseline: dict | None) -> dict:
    base_keys: dict[str, set[tuple[str, str]]] = {}
    drift: list[str] = []
    if baseline:
        for code, spec in baseline.get("rules", {}).items():
            base_keys[code] = {(e["id"], e["at"]) for e in spec.get("violations", [])}
            if code in RULE_PARAMS and spec.get("params") != RULE_PARAMS[code]:
                drift.append(code)
    levels: dict[str, dict[str, list[Violation]]] = defaultdict(lambda: defaultdict(list))
    for v in ctx.violations:
        tier = RULES[v.code][0]
        if tier == "STRUCT":
            levels[v.code]["ERROR"].append(v)
        elif tier == "DEBT":
            known = baseline is not None and (v.rid, v.at) in base_keys.get(v.code, set())
            levels[v.code]["WARNING" if known else "ERROR"].append(v)
        else:
            levels[v.code]["INFO"].append(v)
    current_keys: dict[str, set[tuple[str, str]]] = defaultdict(set)
    for v in ctx.violations:
        current_keys[v.code].add((v.rid, v.at))
    resolved = {
        code: sorted(keys - current_keys.get(code, set())) for code, keys in base_keys.items()
        if keys - current_keys.get(code, set())
    }
    return {"levels": levels, "resolved": resolved, "drift": drift}


def print_report(ctx: Context, result: dict, verbose: bool, baseline_present: bool) -> int:
    levels = result["levels"]
    errors = sum(len(vs["ERROR"]) for vs in levels.values())
    warnings = sum(len(vs["WARNING"]) for vs in levels.values())
    print(f"TOEIC data validation — {ctx.info.get('total_records', 0)} bản ghi, "
          f"version {ctx.manifest.get('version')}, baseline {'có' if baseline_present else 'KHÔNG CÓ'}")
    for code in sorted(levels):
        for level in ("ERROR", "WARNING"):
            vs = levels[code][level]
            if not vs:
                continue
            records = len({v.rid for v in vs})
            print(f"[{level}] {code} {RULES[code][1]}: {len(vs)} vi phạm / {records} bản ghi")
            limit = None if verbose else (8 if level == "ERROR" else 0)
            for v in vs[:limit]:
                print(f"    - {v.rid} {v.at}: {v.msg}")
            if limit is not None and len(vs) > limit > 0:
                print(f"    … còn {len(vs) - limit} mục (dùng -v để xem đủ)")
    for code in result["drift"]:
        errors += 1
        print(f"[ERROR] RULE-DRIFT {code}: tham số luật khác với baseline; không được nới luật mà không duyệt baseline")
    info_bits = []
    for code in sorted(levels):
        if levels[code]["INFO"]:
            info_bits.append(f"{code}={len(levels[code]['INFO'])}")
    if ctx.info.get("ids_baseline_valid") is False:
        print("ID: KHÔNG so sánh được — baseline-ids.json không toàn vẹn (xem lỗi DQ003); "
              "không coi ID nào là mới hay đã mất")
    else:
        ids_added = ctx.info.get("ids_added") or []
        ids_missing = ctx.info.get("ids_missing") or []
        print(f"ID: thêm {len(ids_added)}, mất {len(ids_missing)}; sha256 tập ID {str(ctx.info.get('id_set_sha256'))[:16]}…")
    resolved_total = sum(len(v) for v in result["resolved"].values())
    print(f"Baseline: legacy (WARNING) {warnings}, mới (ERROR từ luật DEBT) "
          f"{sum(len(levels[c]['ERROR']) for c in levels if RULES[c][0] == 'DEBT')}, đã sửa (resolved) {resolved_total}")
    for code, keys in sorted(result["resolved"].items()):
        print(f"    resolved {code}: {len(keys)} mục")
    cov = ctx.info.get("coverage", {})
    if cov:
        n = cov.get("records", 0) or 1
        print("Coverage: " + ", ".join(
            f"{k}={cov.get(k, 0)} ({100 * cov.get(k, 0) / n:.0f}%)"
            for k in ("ipa", "word_family", "verb_forms", "collocations", "synonyms", "antonyms", "multi_sense")))
        print(f"INFO: ví dụ <5 từ={ctx.info.get('short_examples')}, định nghĩa trùng giữa các từ="
              f"{ctx.info.get('duplicate_definitions_across_records')}, IPA thiếu={cov.get('ipa_missing', 0)}, "
              f"syn/ant chưa có nghĩa={ctx.info.get('syn_ant_without_gloss')}/{ctx.info.get('syn_ant_terms')}, "
              f"CEFR từ≠sense={cov.get('cefr_word_sense_mismatch', 0)}, C1={cov.get('c1', 0)}, "
              f"tham chiếu asset đã kiểm={ctx.info.get('asset_references_checked', 0)}")
    if errors:
        print(f"RESULT: FAILED — {errors} ERROR")
        return 1
    print(f"RESULT: PASS — 0 ERROR, {warnings} WARNING (legacy)")
    return 0


# ---------------------------------------------------------------- main
def run(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    ap.add_argument("--baseline", type=Path, help="mặc định: <root>/tools/quality-baseline.json")
    ap.add_argument("--baseline-ids", type=Path, help="mặc định: <root>/tools/baseline-ids.json")
    ap.add_argument("--no-baseline", action="store_true", help="coi mọi vi phạm DEBT là ERROR")
    ap.add_argument("--allow-remove", default="", help="danh sách ID được phép mất, cách nhau bằng dấu phẩy")
    ap.add_argument("--init-baseline", action="store_true", help="tạo baseline và baseline-ids từ trạng thái hiện tại")
    ap.add_argument("--tighten-baseline", action="store_true", help="xóa khỏi baseline các mục đã sửa; không bao giờ thêm")
    ap.add_argument("--update-ids", action="store_true", help="ghi lại baseline-ids khi chỉ THÊM ID (hoặc dùng cùng --allow-remove)")
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--json", type=Path, help="ghi báo cáo JSON")
    ap.add_argument("-v", "--verbose", action="store_true")
    args = ap.parse_args(argv)

    root = args.root.resolve()
    baseline_path = args.baseline or root / "tools" / "quality-baseline.json"
    ids_path = args.baseline_ids or root / "tools" / "baseline-ids.json"
    allow_remove = {x.strip() for x in args.allow_remove.split(",") if x.strip()}

    ctx = Context(root)
    load_manifest_and_records(ctx)
    check_schema(ctx)
    check_struct_content(ctx)
    check_manifest(ctx)
    check_related_terms(ctx)
    ctx.info["id_set_sha256"] = id_set_sha256([str(r.get("id", "")) for r in ctx.records])
    if not args.init_baseline:
        check_ids_against_baseline(ctx, ids_path, allow_remove)
    check_service_worker(ctx)
    check_debt_and_info(ctx)
    check_asset_references(ctx)

    if args.init_baseline:
        structural = [v for v in ctx.violations if RULES[v.code][0] == "STRUCT"]
        if structural:
            print(f"Không tạo baseline: còn {len(structural)} lỗi cấu trúc (không được đưa vào baseline).")
            for v in structural[:10]:
                print(f"  - {v.code} {v.rid} {v.at}: {v.msg}")
            return 1
        if (baseline_path.exists() or ids_path.exists()) and not args.force:
            print("Baseline đã tồn tại; không ghi đè (dùng --force nếu thực sự cần và có duyệt).")
            return 1
        baseline_path.parent.mkdir(parents=True, exist_ok=True)
        write_json(baseline_path, build_baseline(ctx))
        ids = sorted(str(r["id"]) for r in ctx.records)
        write_json(ids_path, {"schemaVersion": 1, "createdFrom": ctx.manifest.get("version"),
                              "idSetSha256": id_set_sha256(ids), "count": len(ids), "ids": ids})
        print(f"Đã tạo {baseline_path} và {ids_path} ({len(ids)} ID).")
        for code, spec in json.loads(baseline_path.read_text(encoding="utf-8"))["rules"].items():
            recs = len({e["id"] for e in spec["violations"]})
            print(f"  {code}: {len(spec['violations'])} vi phạm / {recs} bản ghi")
        return 0

    baseline = None
    if not args.no_baseline:
        try:
            baseline = load_baseline(baseline_path)
        except Exception as exc:  # noqa: BLE001
            print(f"ERROR: không đọc được baseline: {exc}")
            return 1
    result = evaluate(ctx, baseline)

    if args.tighten_baseline:
        if baseline is None:
            print("Không có baseline để siết.")
            return 1
        new_debt = [v for c in result["levels"] for v in result["levels"][c]["ERROR"] if RULES[c][0] == "DEBT"]
        if new_debt or result["drift"]:
            print("Từ chối siết baseline: còn vi phạm mới hoặc tham số luật đã đổi. Sửa các lỗi này trước.")
            return 1
        removed = 0
        for code, keys in result["resolved"].items():
            gone = set(keys)
            before = baseline["rules"][code]["violations"]
            baseline["rules"][code]["violations"] = [e for e in before if (e["id"], e["at"]) not in gone]
            removed += len(before) - len(baseline["rules"][code]["violations"])
        write_json(baseline_path, baseline)
        print(f"Đã siết baseline: xóa {removed} mục đã sửa; không thêm mục nào.")
        return 0

    if args.update_ids:
        if ctx.info.get("ids_baseline_valid") is False:
            print("Từ chối cập nhật baseline-ids: file hiện tại không toàn vẹn (count/SHA-256/trùng ID). "
                  "Khôi phục từ Git trước, không ghi đè để che lỗi.")
            return 1
        missing = ctx.info.get("ids_missing") or []
        unexpected = [m for m in missing if m not in allow_remove]
        if unexpected:
            print(f"Từ chối cập nhật baseline-ids: còn {len(unexpected)} ID bị mất ngoài --allow-remove.")
            return 1
        ids = sorted(str(r["id"]) for r in ctx.records)
        write_json(ids_path, {"schemaVersion": 1, "createdFrom": ctx.manifest.get("version"),
                              "idSetSha256": id_set_sha256(ids), "count": len(ids), "ids": ids})
        print(f"Đã cập nhật {ids_path}: {len(ids)} ID.")
        return 0

    if args.json:
        payload = {
            "version": ctx.manifest.get("version"),
            "records": ctx.info.get("total_records"),
            "violations": [
                {"code": v.code, "id": v.rid, "at": v.at, "level": lvl, "msg": v.msg}
                for c, groups in result["levels"].items() for lvl, vs in groups.items() for v in vs
            ],
            "resolved": {c: [list(k) for k in keys] for c, keys in result["resolved"].items()},
        }
        write_json(args.json, payload)
    return print_report(ctx, result, args.verbose, baseline is not None)


if __name__ == "__main__":
    sys.exit(run(sys.argv[1:]))
