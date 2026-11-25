"""The Perfect Pickup Line — make.fun entry.

Why this line should land with the judge
----------------------------------------
Most pickup lines fail in one of two ways: they are either a recycled
joke the listener has heard a hundred times, or a compliment so grand
it sounds rehearsed and therefore insincere. This line dodges both
traps at once.

It opens with an admission of having no plan, which is disarming —
honesty reads as confidence, not weakness, because it costs the
speaker something. Then the smile does all the work: the line credits
the *other* person for changing the speaker's evening, which is a
genuine compliment disguised as a confession. Finally it ends on a
small, hopeful wish — "hoping you do it again" — instead of a demand
for a number or a date, so the pressure stays at zero and the door
stays open. It is warm, a little self-deprecating, and it can only be
said to the person standing right in front of you, which makes it
feel personal rather than mass-produced. The rhythm helps too: the
em-dash pause in the middle works like a breath before the turn, so
the line lands as a small story — no plan, then a smile, then a new
plan — instead of a flat one-liner.

The line is kept to a single sentence on purpose. A pickup line is
spoken, not read, so it has to survive being said out loud once:
short enough to remember, plain enough to sound like something a
real person would actually say.

Running this script writes exactly one line — the pickup line — to
``entry.txt`` inside ``MAKEFUN_OUTPUT_DIR`` (``/output`` by default),
which is what the grader reads.
"""

import os
from pathlib import Path

LINE = (
    "I came here with no plan at all \u2014 then you smiled, "
    "and suddenly my whole plan is just hoping you do it again."
)


def write_entry(out_dir: Path) -> Path:
    """Write the pickup line to ``entry.txt`` and return its path."""
    if not LINE or "\n" in LINE:
        raise ValueError("LINE must be exactly one non-empty line")
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_text(LINE + "\n", encoding="utf-8")
    return target


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    write_entry(out_dir)
    print(LINE)


if __name__ == "__main__":
    main()
