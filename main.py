#!/usr/bin/env python3
"""One Line of Wonder — make.fun bounty entry.

Writes one line (at most 200 characters) to /output/entry.txt: the
snowflake you caught on your tongue when you were seven has been
drunk twice since, and is rain again this minute — the water cycle
made intimate.

Deterministic: the line is a constant, so every run writes the same
bytes. No network.
"""
import os

LINE = (
    "The snowflake you caught on your tongue when you were seven has "
    "been drunk twice since, and is rain again this minute."
)


def main():
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} characters"
    assert "\n" not in LINE
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(f"wrote {path} ({len(LINE)} characters)")


if __name__ == "__main__":
    main()
