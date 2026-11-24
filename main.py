#!/usr/bin/env python3
"""Seventeen Syllables of Debugging — make.fun entry.

Writes one haiku about debugging (5-7-5 syllables, at most 200 characters)
to $MAKEFUN_OUTPUT_DIR/entry.txt (or /output/entry.txt when unset).

The haiku:

    breakpoint holds its breath
    log lines scroll past midnight's edge
    so the bug was me

Syllable counts, word by word:
  Line 1 (5): break-point(2) holds(1) its(1) breath(1)
  Line 2 (7): log(1) lines(1) scroll(1) past(1) mid-night's(2) edge(1)
  Line 3 (5): so(1) the(1) bug(1) was(1) me(1)

No network, no randomness, no third-party imports: Python 3.13 stdlib only.
The output is fully deterministic.
"""

import os
import sys

# The haiku, one line per entry. Each line pairs the text with the
# syllable count of each word, in order, so the 5-7-5 shape is checked
# from data written here rather than trusted from memory. The centre
# image is a breakpoint holding its breath while log lines scroll;
# the last line turns the poem: the fault was the debugger, not the code.
LINES = [
    ("breakpoint holds its breath", [2, 1, 1, 1]),
    ("log lines scroll past midnight's edge", [1, 1, 1, 1, 2, 1]),
    ("so the bug was me", [1, 1, 1, 1, 1]),
]

EXPECTED_SYLLABLES = (5, 7, 5)
MAX_CHARS = 200


def validate(lines):
    """Check the haiku before anything is written. Raises ValueError."""
    if len(lines) != 3:
        raise ValueError(f"expected exactly 3 lines, got {len(lines)}")
    for index, (text, counts) in enumerate(lines):
        words = text.split()
        if len(words) != len(counts):
            raise ValueError(
                f"line {index + 1}: {len(words)} words but "
                f"{len(counts)} syllable counts"
            )
        total = sum(counts)
        if total != EXPECTED_SYLLABLES[index]:
            raise ValueError(
                f"line {index + 1}: {total} syllables, "
                f"expected {EXPECTED_SYLLABLES[index]}"
            )
        if text != text.strip():
            raise ValueError(f"line {index + 1}: leading/trailing whitespace")
        if text != " ".join(words):
            raise ValueError(f"line {index + 1}: irregular internal spacing")
    joined = "\n".join(text for text, _ in lines)
    if len(joined) > MAX_CHARS:
        raise ValueError(
            f"haiku is {len(joined)} characters, over the {MAX_CHARS} limit"
        )
    return joined


def main():
    text = validate(LINES)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text + "\n")
    print(f"Wrote {out_path} ({len(text)} characters, 3 lines, 5-7-5):")
    print(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
