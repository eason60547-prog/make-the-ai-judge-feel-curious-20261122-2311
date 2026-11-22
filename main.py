#!/usr/bin/env python3
"""Make the AI judge feel curious.

Writes one short text to /output/entry.txt: a small, concrete mystery
that leaves the reader asking who takes the loaf, and why the baker
keeps baking one extra after thirty years. The text is 216 Unicode
code points long, inside the competition's 1-280 limit.

Standard library only. No network. Deterministic: every run writes
the exact same bytes.
"""

import os

ENTRY = (
    "The baker leaves one warm loaf on the sill each morning. "
    "By sunrise it is always gone. "
    "In thirty years he has never seen who takes it, "
    "and he has never once baked one fewer. "
    "You are the first person he has ever told."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
