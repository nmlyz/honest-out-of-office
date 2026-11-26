#!/usr/bin/env python3
"""Write one line to /output/entry.txt: a painfully honest out-of-office
auto-reply that stays polite enough for a manager to let it stand.

The line was picked from 36 candidates by pairwise judging against the
brief (honesty first, then politeness, then the turn of phrase). It is
built in two clauses: the polite version of the message, then the honest
version — the reply performs the honesty it claims. The program checks
the result against the entry gate (length, single line, no leading or
trailing space) before writing it, then reads the file back to confirm
the bytes match.
"""

import os
import sys

LINE = (
    "I am out of office, and the polite version of this message is that "
    "I am resting; the honest version is that I am hiding from my inbox."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = os.path.join(out_dir, "entry.txt")
    if not (1 <= len(LINE) <= 200):
        sys.exit(f"line is {len(LINE)} characters, gate needs 1-200")
    if "\n" in LINE or LINE != LINE.strip():
        sys.exit("line must be a single line with no surrounding space")
    if LINE.count(".") != 1 or not LINE.endswith("."):
        sys.exit("line must be a single sentence")
    data = (LINE + "\n").encode("utf-8")
    os.makedirs(out_dir, exist_ok=True)
    with open(path, "wb") as f:
        f.write(data)
    os.chmod(path, 0o644)
    with open(path, "rb") as f:
        if f.read() != data:
            sys.exit("read-back mismatch")
    print(f"wrote {len(data)} bytes to {path}")


if __name__ == "__main__":
    main()
