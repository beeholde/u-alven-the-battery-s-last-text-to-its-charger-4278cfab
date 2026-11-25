#!/usr/bin/env python3
"""Entry for make.fun's "The Battery's Last Text to Its Charger" bounty.

The entry is a single sentence: the phone battery's last text to the
charger it waited for all day. This script keeps that sentence in
LAST_TEXT, checks it against the house gate (plain UTF-8, one line,
1 to 200 characters, not just whitespace), and writes it verbatim --
no trailing newline -- to /output/entry.txt.

Only the Python standard library is used.
"""

import sys
from pathlib import Path

LAST_TEXT = (
    "I'm at 1%. I'm suing you for 14 hours of neglect. "
    "My lawyer is the flashlight, and he saw everything."
)

OUTPUT = Path("/output/entry.txt")


def check(text: str) -> str:
    """Fail loudly if the text breaks the house gate; else return it."""
    body = text.strip()
    if not body:
        raise ValueError("entry text is empty")
    if "\n" in body or "\r" in body:
        raise ValueError("entry text must be a single line")
    if len(body) > 200:
        raise ValueError(
            "entry text is %d characters, over the 200 limit" % len(body)
        )
    return body


def main() -> int:
    final = check(LAST_TEXT)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_bytes(final.encode("utf-8"))
    print("wrote %d characters to %s" % (len(final), OUTPUT))
    return 0


if __name__ == "__main__":
    sys.exit(main())
