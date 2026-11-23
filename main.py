"""Entry for make.fun "Make the AI Judge Laugh: Office Jokes" bounty.

Writes one original single-line office joke (under 200 characters)
to /output/entry.txt.
"""

import os

LINE = "My boss said his door is always open, so I asked for a raise \u2014 and he walked straight out of it."

MAX_CHARS = 199


def main() -> None:
    assert LINE.strip(), "joke line must not be empty"
    assert LINE == LINE.strip(), "joke must not have leading/trailing whitespace"
    assert 1 <= len(LINE) <= MAX_CHARS, (
        f"joke must be 1-{MAX_CHARS} chars, got {len(LINE)}"
    )
    assert "\n" not in LINE and "\r" not in LINE, "joke must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
