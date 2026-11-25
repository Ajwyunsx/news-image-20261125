#!/usr/bin/env python3
"""Deterministic entrypoint for the news-image-20261125 bounty.

Copies the committed front-page render to /output/entry.png and prints its
byte size. No network, no browser, no randomness.
"""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
OUT_DIR = "/output"
OUT = os.path.join(OUT_DIR, "entry.png")


def main() -> None:
    os.makedirs(OUT_DIR, exist_ok=True)
    shutil.copyfile(SRC, OUT)
    print(os.path.getsize(OUT))


if __name__ == "__main__":
    main()
