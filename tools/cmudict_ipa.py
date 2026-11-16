#!/usr/bin/env python3
"""Apply/check the audited CMUdict ARPABET -> project US IPA backfill ledger.

The full CMUdict is not bundled. Only source ARPABET lines for selected dictionary
headwords are retained with attribution; see the companion CMUdict data license.
"""
from __future__ import annotations
import argparse, json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "docs/reports/CMUDICT_IPA_BACKFILL_v2.71.0.json"
VOWELS = {"AA":"ɑ","AE":"æ","AH":"ʌ","AO":"ɔ","AW":"aʊ","AY":"aɪ","EH":"e","ER":"ɝ","EY":"eɪ","IH":"ɪ","IY":"i","OW":"oʊ","OY":"ɔɪ","UH":"ʊ","UW":"u"}
CONSONANTS = {"B":"b","CH":"tʃ","D":"d","DH":"ð","F":"f","G":"ɡ","HH":"h","JH":"dʒ","K":"k","L":"l","M":"m","N":"n","NG":"ŋ","P":"p","R":"r","S":"s","SH":"ʃ","T":"t","TH":"θ","V":"v","W":"w","Y":"j","Z":"z","ZH":"ʒ"}
PHONE_MAP = {**VOWELS, **CONSONANTS}
VOWEL_PHONES = set(VOWELS)
SINGLE_ONSETS = set(CONSONANTS.values()) - {"ŋ"}
LEGAL_ONSETS = {"pl","pr","bl","br","tr","dr","kl","kr","gl","gr","fl","fr","θr","sp","st","sk","sm","sn","sl","sw","tw","dw","kw","gw","spl","spr","str","skr","skw"}
IPA_ALLOWED = set(" ()./;abdefhijklmnoprstuvwzæðŋɑɔəɚɝɡɪʃʊʌʒˈˌː\u032cθ")


def arpabet_to_ipa(arpabet: list[str]) -> str:
    phones: list[tuple[str, str | None, str]] = []
    for token in arpabet:
        match = re.fullmatch(r"([A-Z]+)([012])?", token)
        if not match:
            raise ValueError(f"Invalid ARPABET token: {token}")
        base, stress = match.groups()
        if base not in PHONE_MAP:
            raise ValueError(f"Unsupported ARPABET phone: {base}")
        symbol = PHONE_MAP[base]
        if base == "AH" and stress == "0":
            symbol = "ə"
        elif base == "ER" and stress == "0":
            symbol = "ɚ"
        phones.append((base, stress, symbol))

    vowel_indices = [i for i, phone in enumerate(phones) if phone[0] in VOWEL_PHONES]
    if not vowel_indices:
        raise ValueError("Pronunciation has no vowel nucleus")
    primary_stress_count = sum(phone[1] == "1" for phone in phones if phone[0] in VOWEL_PHONES)
    if primary_stress_count > 1:
        raise ValueError("Pronunciation has multiple primary stresses")

    syllable_onsets = [0]
    for previous_vowel, current_vowel in zip(vowel_indices, vowel_indices[1:]):
        cluster = phones[previous_vowel + 1:current_vowel]
        onset_length = 0
        for length in range(1, min(3, len(cluster)) + 1):
            suffix = "".join(phone[2] for phone in cluster[-length:])
            if (length == 1 and suffix in SINGLE_ONSETS) or (length > 1 and suffix in LEGAL_ONSETS):
                onset_length = length
        syllable_onsets.append(previous_vowel + 1 + len(cluster) - onset_length)

    onset_to_vowel = dict(zip(syllable_onsets, vowel_indices))
    output = ""
    for index, (_, _, symbol) in enumerate(phones):
        if index in onset_to_vowel and len(vowel_indices) > 1:
            if index > 0:
                output += "."
            stress = phones[onset_to_vowel[index]][1]
            if stress == "1":
                output += "ˈ"
            elif stress == "2":
                output += "ˌ"
        output += symbol

    ipa = f"/{output}/"
    if set(ipa) - IPA_ALLOWED:
        raise ValueError(f"IPA contains unsupported characters: {sorted(set(ipa) - IPA_ALLOWED)}")
    if len(vowel_indices) > 1 and "ˈ" not in ipa and "ˌ" not in ipa:
        raise ValueError("Multisyllabic pronunciation lacks stress")
    return ipa


def load_records() -> tuple[dict[str, dict], dict]:
    manifest = json.loads((ROOT / "data/manifest.json").read_text(encoding="utf-8"))
    records: dict[str, dict] = {}
    for item in manifest["letters"]:
        path = ROOT / item["file"].replace("./", "", 1)
        data = json.loads(path.read_text(encoding="utf-8"))
        for record in data["words"]:
            records[record["id"]] = record
    return records, manifest


def check() -> int:
    ledger = json.loads(LEDGER.read_text(encoding="utf-8"))
    records, _ = load_records()
    seen: set[str] = set()
    errors: list[str] = []
    for row in ledger["records"]:
        rid = row["id"]
        if rid in seen:
            errors.append(f"duplicate ledger id: {rid}")
            continue
        seen.add(rid)
        record = records.get(rid)
        if not record:
            errors.append(f"missing canonical record: {rid}")
            continue
        if record.get("word", "").casefold() != row["word"].casefold():
            errors.append(f"headword mismatch: {rid}")
        try:
            generated = arpabet_to_ipa(row["arpabet"])
        except ValueError as exc:
            errors.append(f"{rid}: {exc}")
            continue
        if generated != row["phoneticUs"]:
            errors.append(f"converter drift: {rid} expected {row['phoneticUs']} got {generated}")
        actual = (record.get("phonetic") or {}).get("us", "")
        if actual != row["phoneticUs"]:
            errors.append(f"canonical IPA drift: {rid} expected {row['phoneticUs']} got {actual}")
    if len(seen) != ledger.get("recordCount"):
        errors.append(f"ledger recordCount mismatch: {len(seen)} != {ledger.get('recordCount')}")
    if errors:
        print("CMUdict IPA backfill check: FAIL")
        for error in errors[:80]:
            print(" -", error)
        if len(errors) > 80:
            print(f" - ... {len(errors)-80} additional errors")
        return 1
    print(f"CMUdict IPA backfill check: PASS ({len(seen)} source-linked records)")
    return 0


def apply() -> int:
    ledger = json.loads(LEDGER.read_text(encoding="utf-8"))
    _, manifest = load_records()
    file_data: dict[Path, dict] = {}
    records: dict[str, dict] = {}
    for letter in manifest["letters"]:
        path = ROOT / letter["file"].replace("./", "", 1)
        data = json.loads(path.read_text(encoding="utf-8"))
        file_data[path] = data
        for record in data["words"]:
            records[record["id"]] = record
    for row in ledger["records"]:
        record = records.get(row["id"])
        if not record:
            raise SystemExit(f"Missing canonical record: {row['id']}")
        expected = arpabet_to_ipa(row["arpabet"])
        if expected != row["phoneticUs"]:
            raise SystemExit(f"Ledger conversion mismatch: {row['id']}")
        current = (record.get("phonetic") or {}).get("us", "")
        if current and current != expected:
            raise SystemExit(f"Refusing to overwrite existing IPA: {row['id']}")
        record.setdefault("phonetic", {})["us"] = expected
    for path, data in file_data.items():
        path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return check()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--check", action="store_true")
    group.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    return apply() if args.apply else check()

if __name__ == "__main__":
    raise SystemExit(main())
