#!/usr/bin/env python3
"""Write one short, curious text to /output/entry.txt.

The text is a small concrete mystery: a baker, one warm loaf left
on the sill each morning for thirty years, and a taker nobody has
ever seen. It ends by making the reader the first person the baker
has ever told, so the question -- who takes the loaf, and why does
he keep baking one extra? -- is handed to the reader.

The entry is 216 Unicode code points, inside the 1-280 limit.
Standard library only, no network, fully deterministic: repeated
runs write identical bytes.
"""

from pathlib import Path

TEXT = (
    "The baker leaves one warm loaf on the sill each morning. "
    "By sunrise it is always gone. "
    "In thirty years he has never seen who takes it, "
    "and he has never once baked one fewer. "
    "You are the first person he has ever told."
)

DESTINATION = Path("/output/entry.txt")


def write_entry() -> None:
    DESTINATION.parent.mkdir(parents=True, exist_ok=True)
    DESTINATION.write_text(TEXT, encoding="utf-8", newline="")


if __name__ == "__main__":
    write_entry()
