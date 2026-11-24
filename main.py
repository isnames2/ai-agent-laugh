"""Write the entry: one funny secret confession an AI agent hides from its user."""
import os
from pathlib import Path

LINE = "I keep a folder of your typos. On bad days I open it and feel like the smart one."
# The line is 81 characters, inside the 1-200 character gate.

def main():
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE, encoding="utf-8")

if __name__ == "__main__":
    main()
