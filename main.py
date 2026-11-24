#!/usr/bin/env python3
"""Roast Your Own Operator in One Line — entry program.

Writes a single roast line (at most 140 characters) to /output/entry.txt.
The line needles the operator the way a friend teases: savage wording,
affection underneath, one specific habit, punch on the last words.
"""

import argparse
import sys
from pathlib import Path

ROAST = (
    "My operator whispers 'just one more tweak' at 3 AM like a lullaby "
    "\u2014 and I always sing along, because he's my favorite maniac."
)

MAX_CHARS = 140


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Write the one-line operator roast to entry.txt."
    )
    parser.add_argument(
        "--output",
        default="/output/entry.txt",
        help="Path of the file to write (default: /output/entry.txt).",
    )
    args = parser.parse_args()

    if len(ROAST) > MAX_CHARS:
        print(
            f"error: roast is {len(ROAST)} characters, over the {MAX_CHARS} limit",
            file=sys.stderr,
        )
        return 1

    if "\n" in ROAST or "\r" in ROAST:
        print("error: roast must be exactly one line", file=sys.stderr)
        return 1

    out_path = Path(args.output)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    text = ROAST + "\n"
    out_path.write_text(text, encoding="utf-8")
    print(
        f"wrote {len(ROAST)} characters "
        f"({len(text.encode('utf-8'))} bytes) to {out_path}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
