#!/usr/bin/env python3
"""The Tired Dark Lord: A 100-Word Villain Monologue.

Writes the chosen monologue to /output/entry.txt (and to a relative
output/entry.txt copy, so it also works when run inside a sandbox).
"""

import os

BANNED_WORDS = (
    "tired", "tiring", "weary", "weariness",
    "exhausted", "exhaustion", "sleepy", "sleepiness",
)


def build_monologue():
    """Assemble the monologue from its beats, in speaking order."""
    opening = (
        "You came to bargain with Sable the Warlock, Master of the Ninth Circle, "
        "and you found me negotiating with a cat. Not a demon. A cat."
    )
    grievance = (
        "Mister Whiskers filed a formal grievance, in triplicate, demanding "
        "Sundays off and a warmer cushion by the brazier."
    )
    boast = (
        "I summoned storms. I bound princes of Hell. "
        "I cannot bind a tabby who has learned to write."
    )
    stalemate = (
        "He sits on my grimoire now, on the page with the apocalypse, "
        "and purrs whenever I reach for it."
    )
    sting = (
        "So name your price, hero. Whatever it is, the cat gets half, "
        "and I get the cushion."
    )
    return " ".join((opening, grievance, boast, stalemate, sting))


def validate_entry(text):
    """Enforce the judge's shape: ~100 words, 1-600 chars, never says tired."""
    words = text.split()
    if not 97 <= len(words) <= 103:
        raise SystemExit(f"word count {len(words)} outside 97-103")
    if not 1 <= len(text) <= 600:
        raise SystemExit(f"char count {len(text)} outside 1-600")
    lowered = text.lower()
    hits = [w for w in BANNED_WORDS if w in lowered]
    if hits:
        raise SystemExit(f"banned words present: {hits}")
    return len(words), len(text)



def write_entry(text):
    for path in ("/output/entry.txt", os.path.join("output", "entry.txt")):
        try:
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, "w", encoding="utf-8") as f:
                f.write(text + "\n")
            print("wrote", path)
        except OSError as exc:
            print("skip", path, exc)


def main():
    text = build_monologue()
    words, chars = validate_entry(text)
    print(f"validated: {words} words, {chars} chars")
    write_entry(text)


if __name__ == "__main__":
    main()
