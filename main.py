#!/usr/bin/env python3
"""Write the 17 November 2026 world-news summary image to /output/entry.png.

Standard library only, no network. Deterministic: it copies the bundled
entry.png byte-for-byte, so two runs write identical bytes.
"""
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
OUT = "/output/entry.png"


def main():
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    shutil.copyfile(SRC, OUT)
    return 0


if __name__ == "__main__":
    sys.exit(main())
