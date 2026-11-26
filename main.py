#!/usr/bin/env python3
"""Emit the battery's parting text for the make.fun bounty.

The entry is a single line: a phone battery at 1%, ignored all day,
sends one last message to the charger that never arrived. This
program keeps that line in one place, confirms it obeys the bounty
limits (plain text, exactly one line, 1 to 200 characters, never
blank), and stores it in /output/entry.txt exactly as written,
with no trailing newline added.

Only the Python standard library is used.
"""

from pathlib import Path

OUTPUT_PATH = Path("/output/entry.txt")
LIMIT = 200

PARTING_LINE = (
    "hey. 1%. i'm suing you for 14 hours of neglect. "
    "the flashlight saw everything, so i'm taking your alarm, "
    "your photos, and your 2fa codes as damages."
)


def validate(text):
    """Return the trimmed line, or raise if it breaks a limit."""
    cleaned = text.strip()
    if not cleaned:
        raise ValueError("entry line must not be blank")
    if any(mark in cleaned for mark in ("\n", "\r", "\u2028", "\u2029")):
        raise ValueError("entry line must fit on one line")
    if len(cleaned) > LIMIT:
        raise ValueError("entry line exceeds %d characters" % LIMIT)
    cleaned.encode("utf-8")  # fail early if the line is not encodable
    return cleaned


def emit():
    line = validate(PARTING_LINE)
    payload = line.encode("utf-8")
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_bytes(payload)
    print("entry ready: %d chars, %d bytes" % (len(line), len(payload)))
    return 0


if __name__ == "__main__":
    raise SystemExit(emit())
