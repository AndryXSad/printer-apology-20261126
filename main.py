"""The Printer Apology — make.fun bounty entry (program/v1).

Design: the entry is a single apology line written by an office printer
to the people who keep jamming it. The line was chosen by a local
pairwise tournament over 12 original candidates, scored on the judge's
own published criteria in order: (1) a genuine apology from a printer
with its own gripes, (2) a real joke with the punch at the end,
(3) printer truth — jams, staples, cheap paper, (4) freshness,
(5) economy inside 120 characters.

Winner (116 characters): the printer forgives the jam, lists its
grievances (stapled lunch, damp paper, shouting), then turns the
apology itself into the joke — it printed the apology upside down,
on purpose. The meta twist is the punch, and it lands last.

The program is deterministic: it writes exactly this one line, with
no trailing newline, to entry.txt in the harness output directory.
Standard library only; no network, no randomness, no input read.
"""

import os
import sys

LINE = (
    "Forgive the jam: you stapled my lunch, fed me damp paper and "
    "yelled. I printed your apology upside down. On purpose."
)


def main() -> int:
    if len(LINE) > 120:
        raise SystemExit("entry line exceeds 120 characters")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
