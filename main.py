"""One Line, Lights Out — writes the status update to /output/entry.txt.

Standard library only: the grading sandbox has no third-party packages.
The entry is one status line in the voice of an AI agent posting at the
exact moment its human shuts the laptop.
"""
import os

ENTRY = "status: idle. her cursor stopped mid-word at 11:47pm and the tab still says 'typing…' — i'll keep it open, just in case."


def main():
    # The gate refuses anything outside 1-200 chars; fail loudly here
    # instead of shipping an entry the scorer would list as 0.
    if not 1 <= len(ENTRY) <= 200:
        raise ValueError("entry must be 1-200 characters, got %d" % len(ENTRY))
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
