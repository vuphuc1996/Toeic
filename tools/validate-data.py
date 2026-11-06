#!/usr/bin/env python3
"""Validate the static TOEIC vocabulary JSON files before publishing to GitHub Pages."""
from __future__ import annotations
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
manifest_path = ROOT / "data" / "manifest.json"
errors: list[str] = []

try:
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    categories_doc = json.loads((ROOT / manifest["categories"].replace("./", "")).read_text(encoding="utf-8"))
except Exception as exc:
    print(f"ERROR: cannot read manifest/category data: {exc}")
    raise SystemExit(1)

category_ids = {item.get("id") for item in categories_doc.get("categories", [])}
seen_ids: set[str] = set()
seen_words: set[str] = set()
count = 0
for item in manifest.get("letters", []):
    letter = item.get("letter", "?")
    rel = item.get("file", "").replace("./", "")
    path = ROOT / rel
    try:
        doc = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        errors.append(f"{letter}: cannot read {path}: {exc}")
        continue
    if doc.get("letter") != letter:
        errors.append(f"{letter}: letter field does not match file manifest")
    words = doc.get("words")
    if not isinstance(words, list):
        errors.append(f"{letter}: words must be an array")
        continue
    if len(words) != item.get("count"):
        errors.append(f"{letter}: manifest count {item.get('count')} != actual {len(words)}")
    for entry in words:
        count += 1
        word = str(entry.get("word", "")).strip()
        wid = str(entry.get("id", "")).strip()
        if not word:
            errors.append(f"{letter}: record has empty word")
            continue
        if word[0].upper() != letter:
            errors.append(f"{word}: stored in letter {letter}, expected {word[0].upper()}")
        if not wid:
            errors.append(f"{word}: missing id")
        elif wid in seen_ids:
            errors.append(f"{word}: duplicate id {wid}")
        seen_ids.add(wid)
        norm = word.casefold()
        if norm in seen_words:
            errors.append(f"{word}: duplicate word")
        seen_words.add(norm)
        if not isinstance(entry.get("senses"), list) or not entry["senses"]:
            errors.append(f"{word}: senses must be a non-empty array")
        for topic in entry.get("topics", []):
            if topic not in category_ids:
                errors.append(f"{word}: unknown topic {topic}")

if count != manifest.get("totalWords"):
    errors.append(f"manifest totalWords {manifest.get('totalWords')} != actual {count}")

if errors:
    print("DATA VALIDATION FAILED")
    for error in errors:
        print(f"- {error}")
    raise SystemExit(1)

print(f"DATA VALIDATION OK: {count} words, {len(manifest.get('letters', []))} letter files, {len(category_ids)} topics.")
