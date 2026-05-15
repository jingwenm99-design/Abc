#!/usr/bin/env python3
"""A simple Chinese-English translator CLI.

Uses an internal phrase dictionary for common terms and falls back to
character-by-character / token-by-token transliteration hints.
"""

from __future__ import annotations

import argparse
import re
from typing import Dict

ZH_TO_EN: Dict[str, str] = {
    "你好": "hello",
    "谢谢": "thank you",
    "再见": "goodbye",
    "早上好": "good morning",
    "晚上好": "good evening",
    "我爱你": "i love you",
    "中国": "China",
    "美国": "United States",
    "天气": "weather",
    "今天": "today",
}

EN_TO_ZH: Dict[str, str] = {value.lower(): key for key, value in ZH_TO_EN.items()}


def contains_chinese(text: str) -> bool:
    return any("\u4e00" <= ch <= "\u9fff" for ch in text)


def normalize_en(text: str) -> str:
    return re.sub(r"\s+", " ", text.strip().lower())


def translate_zh_to_en(text: str) -> str:
    text = text.strip()
    if text in ZH_TO_EN:
        return ZH_TO_EN[text]

    translated = text
    for zh in sorted(ZH_TO_EN, key=len, reverse=True):
        translated = translated.replace(zh, ZH_TO_EN[zh])
    return translated


def translate_en_to_zh(text: str) -> str:
    normalized = normalize_en(text)
    if normalized in EN_TO_ZH:
        return EN_TO_ZH[normalized]

    translated = normalized
    for en in sorted(EN_TO_ZH, key=len, reverse=True):
        translated = translated.replace(en, EN_TO_ZH[en])
    return translated


def translate(text: str, direction: str) -> str:
    if direction == "auto":
        direction = "zh-en" if contains_chinese(text) else "en-zh"
    if direction == "zh-en":
        return translate_zh_to_en(text)
    if direction == "en-zh":
        return translate_en_to_zh(text)
    raise ValueError(f"Unsupported direction: {direction}")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Simple Chinese-English translator")
    parser.add_argument("text", help="Text to translate")
    parser.add_argument(
        "-d",
        "--direction",
        default="auto",
        choices=["auto", "zh-en", "en-zh"],
        help="Translation direction (default: auto)",
    )
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    print(translate(args.text, args.direction))


if __name__ == "__main__":
    main()
