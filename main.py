#!/usr/bin/env python3
"""Six Words, One Story — make.fun entry.

Writes the six-word story to /output/entry.txt.
"""

import os

STORY = "She waited at the station. Forever."

def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(STORY)


if __name__ == "__main__":
    main()
