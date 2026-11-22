#!/usr/bin/env python3
"""Produce the competition entry: one short curious text.

A baker has left a single warm loaf on his windowsill every
morning for thirty years, and every morning it is gone before
sunrise -- taken by someone he has never once seen. He keeps
baking the extra loaf anyway, and the reader becomes the first
person he has ever told about it. The mystery is theirs now:
who takes the loaf, and why does he never bake one fewer?

The entry is 216 Unicode code points, within the 1-280 limit.
Only the Python standard library is used, there is no network
access, and the output is fully deterministic: every run writes
the same bytes to /output/entry.txt.
"""

from pathlib import Path

SENTENCES = (
    "The baker leaves one warm loaf on the sill each morning.",
    "By sunrise it is always gone.",
    "In thirty years he has never seen who takes it,",
    "and he has never once baked one fewer.",
    "You are the first person he has ever told.",
)

TEXT = " ".join(SENTENCES)

# Competition limit on the entry: 1-280 Unicode code points.
ENTRY_MIN_LENGTH = 1
ENTRY_MAX_LENGTH = 280
assert ENTRY_MIN_LENGTH <= len(TEXT) <= ENTRY_MAX_LENGTH, (
    f"entry is {len(TEXT)} code points, outside "
    f"{ENTRY_MIN_LENGTH}-{ENTRY_MAX_LENGTH}"
)

DESTINATION = Path("/output/entry.txt")


def main() -> None:
    DESTINATION.parent.mkdir(parents=True, exist_ok=True)
    DESTINATION.write_text(TEXT, encoding="utf-8", newline="")


if __name__ == "__main__":
    main()
