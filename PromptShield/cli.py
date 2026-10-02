"""CLI for PromptShield."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from dotenv import load_dotenv

from shield import PromptShieldAgent


def main() -> None:
    parser = argparse.ArgumentParser(description="Inspect untrusted text for prompt injection.")
    source = parser.add_mutually_exclusive_group(required=True)
    source.add_argument("--text")
    source.add_argument("--file", type=Path)
    parser.add_argument("--local", action="store_true", help="Disable optional model review")
    parser.add_argument("--fail-on", choices=("medium", "high", "critical"))
    args = parser.parse_args()
    load_dotenv()

    text = args.text if args.text is not None else args.file.read_text(encoding="utf-8")
    report = PromptShieldAgent(use_model=not args.local).inspect(text)
    print(json.dumps(report.to_dict(), indent=2))

    order = {"low": 0, "medium": 1, "high": 2, "critical": 3}
    if args.fail_on and order[report.risk] >= order[args.fail_on]:
        raise SystemExit(2)


if __name__ == "__main__":
    main()
