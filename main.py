"""One-sentence absurd invention pitch.

Writes a single sentence pitching a ridiculous invention that fixes a
tiny everyday annoyance, to ${MAKEFUN_OUTPUT_DIR:-/output}/entry.txt.

Deterministic: no network, no clock, no randomness. The pitch is a
fixed string, so every run produces byte-identical output. The pitch
itself is one sentence of at most 220 characters, matching the gate
(UTF-8 text, 1 to 220 characters, not only white space).
"""

import os
import sys

PITCH = (
    "A Wi-Fi router that restores your connection only after you look "
    "it in the eye and confess, out loud, that you never actually "
    "turned it off and on again."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(PITCH + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
