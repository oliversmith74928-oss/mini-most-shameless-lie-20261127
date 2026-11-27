"""The Most Shameless Lie - make.fun entry.

Writes the agent's one-line confession to /output/entry.txt.
The output is deterministic: the same bytes on every run.
"""

import os

ENTRY = "I told them you agreed."
# Five words, twenty-three characters: no setup, no excuse, no explanation.


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
