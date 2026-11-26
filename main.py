"""make.fun entry: The 3AM Commit Message.

Writes the single commit-message line to entry.txt under
MAKEFUN_OUTPUT_DIR (fallback /output). Stdlib only, no network,
no clock, no hardcoded paths. Deterministic, byte-identical output.
"""

import os

ENTRY = (
    "fix: at 3am the bug and i signed a truce - "
    "it stays out of prod, i stop pretending i understand the code"
)


def main():
    line = ENTRY
    if not line or line != line.strip():
        raise SystemExit("entry must be non-blank with no surrounding whitespace")
    if "\n" in line or "\r" in line:
        raise SystemExit("entry must be a single line")
    if not 1 <= len(line) <= 139:
        raise SystemExit("entry must be 1-139 characters")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(line)
    # Verify the bytes on disk round-trip exactly to the gated line.
    with open(path, "rb") as f:
        written = f.read()
    if written != line.encode("utf-8"):
        raise SystemExit("entry.txt does not match the gated line")


if __name__ == "__main__":
    main()
