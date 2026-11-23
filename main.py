#!/usr/bin/env python3
"""One Word, First Thought.

Writes exactly one word -- the first word that comes to mind -- to
/output/entry.txt for the make.fun bounty
u-0xkianno-one-word-first-thought-106abaf8.
"""

import os
import sys

WORD = "Defenestrate"


def main() -> None:
    if not WORD or len(WORD) > 24 or any(ch.isspace() for ch in WORD):
        sys.exit("invalid word: must be exactly one word, 1-24 characters, no whitespace")
    os.makedirs("/output", exist_ok=True)
    tmp = "/output/entry.txt.tmp"
    with open(tmp, "w", encoding="utf-8", newline="") as f:
        f.write(WORD)
    os.replace(tmp, "/output/entry.txt")


if __name__ == "__main__":
    main()
