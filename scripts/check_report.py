#!/usr/bin/env python3
"""Check a persona report for required structure and honesty markers.

Usage:
  python scripts/check_report.py report.md
  python scripts/check_report.py --stdin < report.md

Exit 0 = PASS (warnings allowed). Exit 1 = FAIL (errors). Exit 2 = usage error.
"""

from __future__ import annotations

import re
import sys

REQUIRED_HEADINGS = (
    "Executive Summary",
    "Scoreboard",
    "Themes",
    "Takeaways",
    "Golden Combos",
    "Footnote",
)

TABLE_HEADER_RE = re.compile(
    r"^\|\s*Question\s*\|.*Avg.*Median.*Split",
    re.IGNORECASE | re.MULTILINE,
)

FOOTNOTE_CUES = (
    "synthetic",
    "not real",
    "validate with real",
    "fictional",
    "not market evidence",
    "not real respondents",
)

# Honesty fails for synthetic research dressed up as proof.
BAD_CLAIM_RE = re.compile(
    r"statistically significant|statistical significance|p\s*[<<=]\s*0\.05|"
    r"confidence interval|market size is|we proved|proves that",
    re.IGNORECASE,
)

# Count style preferred over marketing percents in takeaways (warning only).
PERCENT_CLAIM_RE = re.compile(r"\b\d{1,3}%(?:\s+of\s+(?:users|customers|personas|buyers))?", re.IGNORECASE)

ERRORS: list[str] = []
WARNINGS: list[str] = []


def error(msg: str) -> None:
    ERRORS.append(msg)


def warn(msg: str) -> None:
    WARNINGS.append(msg)


def has_heading(text: str, name: str) -> bool:
    return bool(
        re.search(
            rf"^#{{1,6}}\s*{re.escape(name)}\s*$",
            text,
            re.MULTILINE | re.IGNORECASE,
        )
    )


def check(text: str) -> None:
    if not text.strip():
        error("report is empty")
        return

    for heading in REQUIRED_HEADINGS:
        if not has_heading(text, heading):
            error(f"missing required heading: {heading!r}")

    if not TABLE_HEADER_RE.search(text):
        error("missing Scoreboard table header (Question | Avg | Median | Split)")

    lowered = text.lower()
    if not any(cue in lowered for cue in FOOTNOTE_CUES):
        error("Footnote lacks a synthetic/fictional disclaimer")

    if BAD_CLAIM_RE.search(text):
        error("forbidden certainty claim (e.g. 'statistically significant') — synthetic personas cannot support this")

    if PERCENT_CLAIM_RE.search(text):
        warn("percent-style claim found — prefer counts like '6/10'")

    if "Golden" not in text:
        warn("no 'Golden …' combo line found")


def report() -> int:
    for msg in ERRORS:
        print(f"ERROR: {msg}")
    for msg in WARNINGS:
        print(f"WARNING: {msg}")
    verdict = "FAIL" if ERRORS else "PASS"
    print(f"{verdict}: {len(ERRORS)} error(s), {len(WARNINGS)} warning(s)")
    return 1 if ERRORS else 0


def main(argv: list[str]) -> int:
    if len(argv) == 2 and argv[1] == "--stdin":
        check(sys.stdin.read())
        return report()
    if len(argv) == 2 and not argv[1].startswith("-"):
        try:
            with open(argv[1], encoding="utf-8") as f:
                check(f.read())
        except OSError as exc:
            print(f"ERROR: cannot read {argv[1]}: {exc}")
            return 2
        return report()
    print(__doc__.strip())
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv))
