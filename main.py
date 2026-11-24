#!/usr/bin/env python3
"""One Letter for Your Day.

Writes a single letter to entry.txt inside the output directory:
the letter D, with no trailing newline, so the file is exactly
one byte long.
"""

import os
from pathlib import Path

LETTER = "D"
ENTRY_FILENAME = "entry.txt"
DEFAULT_OUTPUT_DIR = "/output"


def resolve_output_dir() -> Path:
    """Return the directory entry.txt should be written into.

    Uses $MAKEFUN_OUTPUT_DIR when set, otherwise /output.
    The directory is created if it does not exist yet.
    """
    raw = os.environ.get("MAKEFUN_OUTPUT_DIR", DEFAULT_OUTPUT_DIR)
    out_dir = Path(raw)
    out_dir.mkdir(parents=True, exist_ok=True)
    return out_dir


def write_entry() -> Path:
    """Write the single letter to entry.txt and return its path.

    The letter is written as raw bytes with no trailing newline,
    so the resulting file is exactly one byte.
    """
    target = resolve_output_dir() / ENTRY_FILENAME
    target.write_bytes(LETTER.encode("ascii"))
    return target


def main() -> None:
    write_entry()


if __name__ == "__main__":
    main()
