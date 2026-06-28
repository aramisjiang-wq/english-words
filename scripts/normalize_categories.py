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

# Categories that are inherently core/high-frequency regardless of the word.
CORE_CATEGORIES = {"核心动词", "高频动词", "数词", "代词", "介词", "感叹词", "时间"}

# The most frequent English words — these are the must-know core that a
# learner should meet first (covers the bulk of everyday text). Reliable
# high-frequency vocabulary; tier 1 ("基础").
TOP_CORE = {
    "the", "be", "to", "of", "and", "a", "in", "that", "have", "i", "it", "for",
    "not", "on", "with", "he", "as", "you", "do", "at", "this", "but", "his",
    "by", "from", "they", "we", "say", "her", "she", "or", "an", "will", "my",
    "one", "all", "would", "there", "their", "what", "so", "up", "out", "if",
    "about", "who", "get", "which", "go", "me", "when", "make", "can", "like",
    "time", "no", "just", "him", "know", "take", "people", "into", "year",
    "your", "good", "some", "could", "them", "see", "other", "than", "then",
    "now", "look", "only", "come", "its", "over", "think", "also", "back",
    "after", "use", "two", "how", "our", "work", "first", "well", "way", "even",
    "new", "want", "because", "any", "these", "give", "day", "most", "us",
    "is", "are", "was", "were", "been", "has", "had", "did", "said", "made",
    "man", "woman", "child", "world", "life", "hand", "part", "eye", "place",
    "week", "case", "point", "government", "company", "number", "group",
    "problem", "fact", "water", "money", "month", "right", "study", "book",
    "word", "side", "kind", "head", "house", "friend", "father", "mother",
    "home", "room", "area", "story", "night", "family", "city", "country",
    "school", "student", "name", "find", "tell", "ask", "seem", "feel", "try",
    "leave", "call", "need", "become", "mean", "keep", "let", "begin", "help",
    "talk", "turn", "start", "show", "hear", "play", "run", "move", "live",
    "believe", "hold", "bring", "happen", "write", "sit", "stand", "lose",
    "pay", "meet", "include", "set", "learn", "change", "lead", "watch",
    "follow", "stop", "create", "speak", "read", "spend", "grow", "open",
    "walk", "win", "teach", "buy", "send", "build", "stay", "fall", "cut",
    "reach", "kill", "remain", "love", "eat", "drink", "sleep", "wait", "sell",
    "big", "small", "old", "high", "long", "young", "great", "little", "own",
    "bad", "same", "able", "hot", "cold", "true", "early", "late", "hard",
    "easy", "important", "different", "free", "full", "happy", "real", "best",
    "better", "sure", "low", "open", "close", "near", "far", "next", "last",
    "many", "much", "more", "very", "too", "here", "today", "tomorrow",
    "yesterday", "always", "never", "often", "again", "still", "down", "off",
    "where", "why", "yes", "thing", "something", "nothing", "everything",
    "everyone", "someone", "red", "blue", "green", "white", "black",
    "morning", "evening", "hour", "minute", "dog", "cat", "car", "door",
    "table", "phone", "music", "food", "color", "number", "letter", "question",
    "answer", "true", "false", "left", "color", "please", "thank", "sorry",
    "hello", "yeah", "okay", "really", "maybe", "around", "between", "under",
    "before", "during", "without", "through", "while", "until", "since",
    "both", "few", "each", "every", "another", "such", "enough", "almost",
    "together", "however", "instead", "perhaps", "actually", "finally",
}


def difficulty_level(english: str) -> int:
    """1 = 基础 (core/high-frequency), 2 = 进阶, 3 = 高阶 (heuristic)."""
    w = (english or "").lower().strip()
    if not w:
        return 2
    first = w.split()[0] if " " in w else w
    if w in TOP_CORE or first in TOP_CORE:
        return 1
    n = len(w.replace(" ", "").replace("-", ""))
    if n <= 5:
        return 2
    return 2 if n <= 8 else 3


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
        level = 1 if category in CORE_CATEGORIES else difficulty_level(w.get("english"))
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
            "level": level,
        })
    return out


def main():
    words = json.loads(DATA.read_text(encoding="utf-8"))
    normalized = normalize(words)
    DATA.write_text(
        json.dumps(normalized, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    print(f"normalized {len(normalized)} words")
    lv = Counter(w["level"] for w in normalized)
    print(f"\nlevel: 基础={lv.get(1,0)} 进阶={lv.get(2,0)} 高阶={lv.get(3,0)}")
    for field in ("theme", "part_of_speech"):
        c = Counter(w[field] for w in normalized)
        unknown = c.get("其他", 0)
        print(f"\n{field}: {len(c)} values, '其他'={unknown}")
        for k, v in c.most_common():
            print(f"  {v:>5}  {k}")


if __name__ == "__main__":
    main()
