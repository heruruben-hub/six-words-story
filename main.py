#!/usr/bin/env python3
"""Six Words, One Story — make.fun entry.

Writes the six-word story to /output/entry.txt.
"""

import os

# The story, kept as its two clauses so the wording stays reviewable.
_STORY_PARTS = ["She waited at the station.", "Forever."]


def build_story(parts: list[str]) -> str:
    """Join the story clauses into the single six-word line."""
    return " ".join(part.strip() for part in parts)


STORY = build_story(_STORY_PARTS)

def validate_story(text: str) -> None:
    """The entry must be exactly six words and fit in 1-60 characters."""
    words = text.split()
    if len(words) != 6:
        raise ValueError(f"story must be exactly 6 words, got {len(words)}")
    if not 1 <= len(text) <= 60:
        raise ValueError(f"story must be 1-60 chars, got {len(text)}")


def main() -> None:
    validate_story(STORY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(STORY)


if __name__ == "__main__":
    main()
