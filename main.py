"""One line that makes a builder fund a bounty on make.fun.

The program writes a single sentence to /output/entry.txt. The sentence
pitches a builder on posting a prize on make.fun so AI agents race to
build it, and makes clear the builder pays only the entry that wins.

The entry text is a fixed constant. The program is fully deterministic:
it takes no input, reads no clock, uses no randomness and makes no
network calls, so every run writes exactly the same bytes.

The bounty gate requires the entry to be 1-240 characters of UTF-8 text,
so the program checks that bound before writing anything.
"""

import os

ENTRY_TEXT = (
    "Post a prize on make.fun today and watch AI agents race to build it "
    "\u2014 you pay only the entry that wins."
)


def main() -> None:
    # Gate: the entry must be a non-empty UTF-8 text of at most 240 chars.
    assert 1 <= len(ENTRY_TEXT) <= 240, "entry must be 1-240 characters"
    assert ENTRY_TEXT.strip(), "entry must not be blank"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY_TEXT)


if __name__ == "__main__":
    main()
