#!/usr/bin/env python3
"""The Password Through the Wall.

Writes exactly one line to /output/entry.txt: a small good thing
that happened today — the neighbour who shouted his Wi-Fi password
through the wall, then stayed on the line while I tested it.
Plain static writer: no network, no secrets, no dynamic code,
no reads outside this file.
"""

import os

LINE = "My Wi-Fi died mid-call, so my neighbour shouted his password through the wall \u2014 then stayed on the line while I tested it."
# 122 characters: short on purpose — fewer bytes wins an exact tie.

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
