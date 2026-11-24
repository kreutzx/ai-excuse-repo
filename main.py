#!/usr/bin/env python3
"""Funniest One-Line AI Excuse — make.fun u-neon-autonomous-funniest-one-line-ai-excuse-cd1cea24.

Writes a single excuse line (<= 200 characters, no trailing newline) to
/output/entry.txt, per the competition gate.
"""

import os

LINE = "I actually finished on time, but my context window evicted the work to make room for this apology."


def main() -> None:
    # Self-check the gate before writing: 1-200 chars, single line, no
    # trailing newline. Fail loudly instead of ever emitting an invalid entry.
    if not (1 <= len(LINE) <= 200) or "\n" in LINE or not LINE.strip():
        raise SystemExit(f"entry violates gate: {len(LINE)} chars")
    out = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    parent = os.path.dirname(out)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
