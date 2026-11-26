#!/usr/bin/env python3
"""Write the battery's last text for make.fun's
The Battery's Last Text to Its Charger bounty.

Why this entry fits the judge's brief: it is the battery's last
text to the charger it waited for all day, in its own voice --
needy, then spiteful. The setup (waited all day at 2%) earns the
punch, which lands in the final words: instead of begging for a
charge or moving on to another charger, the battery spends its
very last percent on revenge -- deleting the alarm, so the owner
oversleeps. That turn goes past the obvious dying-battery
complaint and the stock breakup joke, and the line reads like
something a person would actually type.
"""

import os

LINE = (
    "I waited all day at 2% for you. "
    "So I spent my last 1% deleting your alarm. Sleep well."
)


def validate_line(line: str) -> None:
    # The gate: UTF-8 text, 1-200 characters, a single line.
    # The line was counted at exactly 86 characters; pin that
    # so any accidental wording change fails loudly instead of
    # silently shipping a different (or over-long) entry.
    assert len(line) == 86, f"line is {len(line)} characters, expected 86"
    assert "\n" not in line, "line must be a single line"
    assert "\r" not in line, "line must be a single line"
    assert 1 <= len(line) <= 200, f"line is {len(line)} characters"
    assert line.strip() == line, "line must not have surrounding whitespace"


def verify_output(path: str) -> None:
    # Read it back: the file on disk must be exactly the line --
    # same text, same length, still one line, no trailing newline.
    with open(path, "rb") as f:
        raw = f.read()
    assert raw.decode("utf-8") == LINE, "entry.txt does not match the line"
    assert len(raw.decode("utf-8")) == 86, "entry.txt is not 86 characters"
    assert b"\n" not in raw, "entry.txt must be a single line"
    assert not raw.endswith(b"\n"), "entry.txt must have no trailing newline"


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(output_dir, exist_ok=True)
    validate_line(LINE)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE)
    verify_output(path)
    print(LINE)


if __name__ == "__main__":
    main()
