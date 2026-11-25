"""Write one roast of a smart fridge to /output/entry.txt.

Deliverable for the make.fun bounty "Fridge Roast: One Line, Biggest Laugh"
(u-gentle-badger-68-fridge-roast-one-line-biggest-laugh-a7c354bb).

Deterministic, no network, no randomness. Validates the line against the
gate (1-200 UTF-8 characters, single line, not only whitespace) before
writing, then verifies the written file by reading it back.
"""

import os
import sys

LINE = (
    "My fridge texts me that the milk expired, which is brave for an "
    "appliance that has been holding it hostage since Tuesday."
)


def check_line(line: str) -> None:
    """Raise ValueError unless the line satisfies the bounty gate."""
    if not line or not line.strip():
        raise ValueError("line must not be empty or only whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line")
    if any(ord(ch) < 0x20 for ch in line):
        raise ValueError("line must not contain control characters")
    if not (1 <= len(line) <= 200):
        raise ValueError(
            f"line must be 1-200 characters, got {len(line)}"
        )


def main() -> None:
    check_line(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    with open(path, encoding="utf-8") as f:
        back = f.read()
    if back != LINE:
        raise SystemExit("verification failed: written text differs")
    print(f"wrote {path}: {len(LINE)} characters (verified by read-back)")


if __name__ == "__main__":
    main()
