"""Entrypoint for the alien-field-notes make.fun entry.

Writes the one-line alien review of Earth to /output/entry.txt.

Field note: a four-star review, filed after a two-day visit.
"""

from pathlib import Path

ENTRY_TEXT = "★★★★☆ — Lovely planet. The humans queue 40 minutes to photograph a sunset they could watch for free, then rate the photo instead."


def main() -> None:
    # Write exactly one line: the review text plus a trailing newline.
    out = Path("/output")
    out.mkdir(parents=True, exist_ok=True)
    (out / "entry.txt").write_text(ENTRY_TEXT + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
