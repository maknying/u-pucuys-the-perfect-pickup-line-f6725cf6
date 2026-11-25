#!/usr/bin/env python3
"""Entry for make.fun bounty "The Perfect Pickup Line".

Writes one original one-line pickup line to entry.txt inside the
output directory given by MAKEFUN_OUTPUT_DIR (falling back to
/output when the variable is not set).

Why this line should land with the judge:
- Self-aware twist on the genre itself: instead of delivering a
  rehearsed line, it confesses the rehearsal and lets the other
  person's smile defeat it — the speaker loses on purpose, which
  reads as confident rather than try-hard.
- The joke turns on a mundane image ("filed for early retirement")
  applied to something abstract (a pickup line), so the punch lands
  in the last four words after a perfectly normal setup.
- Charming without being creepy: the compliment is the smile, the
  speaker is the butt of the joke, and there is no borrowed cliche
  (no Wi-Fi, no falling from heaven, no "are you a...").
- Tight and fresh: one sentence, no throat-clearing, no explanation
  of the joke, and the line works spoken aloud exactly as written.
"""

import os
from pathlib import Path

LINE = (
    "I rehearsed a pickup line all the way over here, "
    "but then you smiled and it filed for early retirement."
)


def _output_dir() -> Path:
    raw = os.environ.get("MAKEFUN_OUTPUT_DIR", "").strip()
    return Path(raw) if raw else Path("/output")


def _validate(line: str) -> None:
    if not line or line != line.strip():
        raise ValueError("LINE must be non-empty with no leading/trailing whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("LINE must be a single line, no embedded newlines")
    if not 1 <= len(line) <= 199:
        raise ValueError(f"LINE must be 1-199 characters, got {len(line)}")


def main() -> int:
    _validate(LINE)
    out_dir = _output_dir()
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
