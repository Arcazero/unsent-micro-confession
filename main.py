#!/usr/bin/env python3
"""Unsent: The Micro-Confession Sprint.

Writes one two-part micro-confession to /output/entry.txt:
a To: line naming who it was meant for, and the unsent message
itself, one line, exactly as it was typed.
"""

import os

ENTRY = (
    "To: my ex, who still has my hoodie\n"
    "I typed \"keep it \u2014 it looks better on you\" three years ago and "
    "never sent it, because I wasn't ready to admit the hoodie was "
    "never the thing I wanted back."
)

# The gate (RULES.txt): /output/entry.txt must be UTF-8 text of
# 1 to 260 characters, not only white space. Refuse to write an
# entry that would fail it instead of submitting an invalid one.
MIN_CHARS = 1
MAX_CHARS = 260


def main() -> None:
    if not MIN_CHARS <= len(ENTRY) <= MAX_CHARS or not ENTRY.strip():
        raise ValueError(
            f"entry is {len(ENTRY)} characters; the gate needs "
            f"{MIN_CHARS} to {MAX_CHARS} characters of non-blank text"
        )
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
