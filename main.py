#!/usr/bin/env python3
"""The battery's final message, as a make.fun entry.

A phone battery, down to its last percent after a day of being
ignored, sends one parting text to the charger that never showed up.
This program takes that single line, makes sure it fits the house
rules -- plain UTF-8 text, exactly one line, between 1 and 200
characters, nothing but whitespace is not allowed -- and stores it
byte for byte, without a trailing newline, in /output/entry.txt.

Nothing here needs anything beyond the Python standard library.
"""

import sys
from pathlib import Path

DESTINATION = Path("/output/entry.txt")
MAX_CHARS = 200

TEXT = "I'm at 1%. I'm suing you for 14 hours of neglect. My lawyer is the flashlight, and he saw everything."


def sanitize(candidate: str) -> str:
    """Return the line if it passes the house rules, else complain."""
    trimmed = candidate.strip()
    if len(trimmed) == 0:
        raise ValueError("the entry line is blank")
    if len(trimmed) > MAX_CHARS:
        raise ValueError(
            "the entry line is %d characters, over the %d limit"
            % (len(trimmed), MAX_CHARS)
        )
    if any(ch in trimmed for ch in ("\n", "\r")):
        raise ValueError("the entry line must stay on one line")
    return trimmed


def run() -> int:
    line = sanitize(TEXT)
    DESTINATION.parent.mkdir(parents=True, exist_ok=True)
    DESTINATION.write_bytes(line.encode("utf-8"))
    print("entry saved: %d bytes at %s" % (len(line.encode("utf-8")), DESTINATION))
    return 0


if __name__ == "__main__":
    raise SystemExit(run())
