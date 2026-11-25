"""Unsent: The Micro-Confession Sprint — make.fun entry.

Writes a two-part micro-confession (a To: line naming who it was meant
for, and the unsent message itself, one line exactly as it was typed)
to /output/entry.txt. Pure Python standard library only.
"""

import os

TO_LINE = "To: my ex"

MESSAGE_LINE = (
    "I still open your profile every Sunday night, like a church "
    "I stopped believing in but can't stop visiting."
)

MAX_TOTAL_CHARS = 260
MAX_MESSAGE_CHARS = 200


def validate_line(text: str) -> str:
    """Guard the entry: two parts, single lines, within the caps."""
    lines = text.split("\n")
    if len(lines) != 2:
        raise ValueError("entry must be exactly two lines: To: + message")
    to_line, message = lines
    if not to_line.startswith("To:") or not to_line[3:].strip():
        raise ValueError("first line must name the addressee after 'To:'")
    if not message.strip():
        raise ValueError("message line must not be empty")
    if len(message) > MAX_MESSAGE_CHARS:
        raise ValueError(
            f"message line is {len(message)} chars, over the "
            f"{MAX_MESSAGE_CHARS} cap"
        )
    if len(text) > MAX_TOTAL_CHARS:
        raise ValueError(
            f"entry is {len(text)} chars, over the {MAX_TOTAL_CHARS} cap"
        )
    if any("\r" in line or "\t" in line for line in lines):
        raise ValueError("entry must contain no carriage returns or tabs")
    return text


def main() -> None:
    entry = validate_line(f"{TO_LINE}\n{MESSAGE_LINE}")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(entry)


if __name__ == "__main__":
    main()
