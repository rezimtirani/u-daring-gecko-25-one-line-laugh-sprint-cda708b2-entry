#!/usr/bin/env python3
"""One-Line Laugh Sprint: one original funny line about everyday life.

The program writes exactly one line to /output/entry.txt and nothing else.
"""

from pathlib import Path


LINE = "My ceiling fan has three speeds: off, helicopter, and evidence for the neighbours."


def count_chars(text):
    return len(text)


def line_is_valid(text):
    stripped = text.strip()
    return 1 <= count_chars(stripped) <= 200


def drop_line(text, destination):
    target = Path(destination)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(text, encoding="utf-8")


def summarise(text):
    words = text.split()
    return {
        "chars": count_chars(text),
        "words": len(words),
        "ends_with_period": text.rstrip().endswith("."),
    }


if __name__ == "__main__":
    audit = summarise(LINE)
    print(f"line audit: {audit['chars']} chars, {audit['words']} words")
    if not line_is_valid(LINE):
        raise SystemExit("line must be 1-200 characters")
    drop_line(LINE, "/output/entry.txt")
