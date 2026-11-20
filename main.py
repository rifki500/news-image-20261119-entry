#!/usr/bin/env python3
"""Entrypoint for the news-image-20261119 entry.

Places the pre-built front page (entry.png, shipped in this repository)
at the grader's output path. Standard library only, no network calls,
no randomness: the same input bytes produce the same output bytes on
every run, so the two grading runs write identical files. The copy is
streamed in fixed-size blocks so memory use stays flat.
"""

import os
import sys

SOURCE_NAME = "entry.png"
TARGET_NAME = "entry.png"
CHUNK = 65536


def output_dir():
    """The grader's output directory: $MAKEFUN_OUTPUT_DIR, else /output."""
    wanted = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return wanted


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, SOURCE_NAME)
    if not os.path.isfile(source):
        sys.stderr.write("missing %s\n" % source)
        return 1
    dest_dir = output_dir()
    os.makedirs(dest_dir, exist_ok=True)
    target = os.path.join(dest_dir, TARGET_NAME)
    with open(source, "rb") as fin, open(target, "wb") as fout:
        while True:
            block = fin.read(CHUNK)
            if not block:
                break
            fout.write(block)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
