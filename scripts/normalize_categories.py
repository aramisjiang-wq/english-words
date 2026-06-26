#!/usr/bin/env python3
"""Normalize the word taxonomy in data/words_merged.json.

The original data split words into two *mutually exclusive* top buckets
("词性" vs "主题"), so every word had a real value for only one of
part_of_speech / theme and "其他" for the other. This script rebuilds a
coherent taxonomy where **every** word has both:

  - part_of_speech : backfilled from the gloss prefix ("v. 放弃" -> 动词),
                     then a category hint, then the existing value.
  - theme          : the existing theme, or "通用" for core vocabulary.
  - parent_category: the theme domain (or "基础词汇").
  - child_category : the part of speech.
  - category       : a cleaned, specific label (frequency buckets folded).

Run:  python3 scripts/normalize_categories.py
"""
import json
import re
from collections import Counter
from pathlib import Path

DATA = Path(__file__).resolve().parent.parent / "data" / "words_merged.json"

POS_SET = {
    "名词", "动词", "形容词", "副词", "介词", "代词", "数词",
    "感叹词", "连词和冠词", "疑问词", "情态动词",
}

# Gloss-prefix abbreviations -> part of speech.
PREFIX = {
    "n": "名词", "v": "动词", "vt": "动词", "vi": "动词",
    "adj": "形容词", "a": "形容词", "adv": "副词", "prep": "介词",
    "pron": "代词", "num": "数词", "int": "感叹词",
    "conj": "连词和冠词", "art": "连词和冠词",
    "aux": "情态动词", "modal": "情态动词",
}

# Specific categories whose members are reliably nouns (days, months,
# currencies, animals, foods, place names…).
CATEGORY_POS = {
    "货币词汇": "名词", "动物词汇": "名词", "颜色词汇": "名词",
    "时间词汇": "名词", "食物烹饪": "名词", "地理词汇": "名词",
    "自然地理": "名词",
}

# Semantic sub-groups worth surfacing as their own browsable theme,
# instead of being hidden inside the broad "通用" bucket.
SEMANTIC_THEME = {
    "时间词汇": "时间",
    "动物词汇": "动物",
    "颜色和天气": "颜色天气",
    "货币词汇": "货币",
    "食物烹饪": "食物",
    "地理词汇": "地理",
    "自然地理": "地理",
}

# Frequency / generic buckets folded into cleaner labels.
CATEGORY_RENAME = {
    "通用词汇": "通用",
    "最常用动词": "核心动词",
    "常用动词": "高频动词",
}


def pos_from_gloss(chinese: str):
    m = re.match(r"\s*([a-zA-Z]{1,5})\.", chinese or "")
    return PREFIX.get(m.group(1).lower()) if m else None


def clean_pos(word: dict) -> str:
    existing = word.get("part_of_speech")
    if existing in POS_SET:
        return existing
    from_gloss = pos_from_gloss(word.get("chinese"))
    if from_gloss:
        return from_gloss
    if word.get("category") in CATEGORY_POS:
        return CATEGORY_POS[word["category"]]
    for field in ("child_category", "category"):
        if word.get(field) in POS_SET:
            return word[field]
    return "其他"


def clean_theme(word: dict) -> str:
    cat = word.get("category")
    if cat in SEMANTIC_THEME:
        return SEMANTIC_THEME[cat]
    theme = word.get("theme")
    if theme and theme not in ("其他", ""):
        return theme
    return "通用"


def normalize(words: list) -> list:
    out = []
    for w in words:
        pos = clean_pos(w)
        theme = clean_theme(w)
        category = CATEGORY_RENAME.get(w.get("category"), w.get("category") or "通用")
        out.append({
            "english": (w.get("english") or "").strip(),
            "phonetic": (w.get("phonetic") or "").strip(),
            "chinese": (w.get("chinese") or "").strip(),
            "example": (w.get("example") or "").strip(),
            "category": category,
            "part_of_speech": pos,
            "theme": theme,
            "parent_category": theme if theme != "通用" else "基础词汇",
            "child_category": pos,
        })
    return out


def main():
    words = json.loads(DATA.read_text(encoding="utf-8"))
    normalized = normalize(words)
    DATA.write_text(
        json.dumps(normalized, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    print(f"normalized {len(normalized)} words")
    for field in ("theme", "part_of_speech"):
        c = Counter(w[field] for w in normalized)
        unknown = c.get("其他", 0)
        print(f"\n{field}: {len(c)} values, '其他'={unknown}")
        for k, v in c.most_common():
            print(f"  {v:>5}  {k}")


if __name__ == "__main__":
    main()
