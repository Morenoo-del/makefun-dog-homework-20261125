#!/usr/bin/env python3
"""The Dog Ate My Homework: Funniest Excuse.

Writes a single line, in the dog's own voice, to /output/entry.txt.
Deterministic: no input, no network, no randomness.
"""

import os

ENTRY = (
    # Gate: /output/entry.txt must be 1-200 UTF-8 characters, not only
    # whitespace. This line is 118 characters: a dog's verdict, delivered
    # with total confidence and zero remorse.
    "The homework never threw the ball once. Not once. "
    "So I promoted it to chew toy \u2014 that is a career change, not a crime."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
