"""One-line review of the most boring everyday object.

Writes a single review line (1-200 characters) to /output/entry.txt.
Pure standard library. Deterministic: the same bytes on every run.
"""

import os

# The review: the spare button sewn inside a shirt. It waits its whole
# life for a job opening that never comes, then gets thrown out with
# the shirt, still unemployed. Boring, everyday, and true.
REVIEW = (
    "The spare button sewn inside my shirt has waited nine years for "
    "a job opening and will be thrown out with the shirt, still unemployed."
)

OUTPUT_DIR = "/output"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "entry.txt")
MAX_CHARS = 200  # sealed gate: /output/entry.txt must be 1..200 characters


def main() -> None:
    line = REVIEW.strip()
    if not (1 <= len(line) <= MAX_CHARS):
        raise SystemExit(f"review must be 1-{MAX_CHARS} characters, got {len(line)}")
    if "\n" in line or "\r" in line:
        raise SystemExit("review must be a single line")
    # The grader owns /output: create it only if missing, never remove it.
    # Write exactly the line, no trailing newline, so the file's byte
    # count equals the review's character count.
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_FILE, "w", encoding="utf-8", newline="") as f:
        f.write(line)
    print(line)
    print(f"({len(line)} characters -> {OUTPUT_FILE})")


if __name__ == "__main__":
    main()
