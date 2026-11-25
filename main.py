#!/usr/bin/env python3
"""make.fun entry — news-image-20261125.

The front page is already drawn and committed as entry.png, so this program
only has to place those exact bytes where the harness looks for them. Reading
the file as a binary stream (rather than shelling out to cp) keeps the run
free of any dependency beyond the Python standard library, and copying bytes
verbatim is what makes two runs of the program identical.

    python3 main.py        ->  /output/entry.png
"""

import os
import sys

HERE = os.path.dirname(os.path.realpath(__file__))
SOURCE = os.path.join(HERE, "entry.png")
OUTPUT_DIR = "/output"
TARGET = os.path.join(OUTPUT_DIR, "entry.png")


def main():
    # /output may not exist yet on a fresh harness container.
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    with open(SOURCE, "rb") as page:
        pixels = page.read()
    if not pixels.startswith(b"\x89PNG\r\n\x1a\n"):
        sys.exit("entry.png is not a PNG")

    with open(TARGET, "wb") as out:
        out.write(pixels)

    print(len(pixels))


if __name__ == "__main__":
    main()
