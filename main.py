"""One Word for the Boss — entry program.

Writes exactly one word describing a boss to /output/entry.txt
(and a local copy in this entry directory).
"""

import os

ENTRY_DIR = os.path.dirname(os.path.abspath(__file__))

# v2 word: "Hoverer" was accurate but plain — too close to the first
# word anyone reaches for. Revised to a sharper coinage that packs the
# universal idiom "breathing down your neck" into a single word: the
# boss who stands behind you, watching every keystroke, chop and scan.
# Funnier on its own, fresher, and it travels from office to kitchen
# to warehouse without any explanation.
WORD = "Neckbreather"


def main():
    word = WORD.strip()
    assert " " not in word and 1 <= len(word) <= 30, "entry must be 1 word, <=30 chars"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(word)
    with open(os.path.join(ENTRY_DIR, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(word)
    print(word)


if __name__ == "__main__":
    main()
