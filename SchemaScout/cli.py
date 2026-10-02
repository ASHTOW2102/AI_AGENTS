"""Command-line interface for SchemaScout."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from dotenv import load_dotenv

from scout import SchemaScoutAgent, validate_csv


def main() -> None:
    parser = argparse.ArgumentParser(description="Profile CSV files and detect schema drift.")
    subparsers = parser.add_subparsers(dest="command", required=True)
    profile = subparsers.add_parser("profile")
    profile.add_argument("csv_file", type=Path)
    profile.add_argument("--contract", type=Path)
    profile.add_argument("--local", action="store_true")
    validate = subparsers.add_parser("validate")
    validate.add_argument("csv_file", type=Path)
    validate.add_argument("contract_file", type=Path)
    args = parser.parse_args()
    load_dotenv()

    text = args.csv_file.read_text(encoding="utf-8-sig")
    if args.command == "profile":
        report = SchemaScoutAgent(use_model=not args.local).profile(text)
        print(json.dumps(report.to_dict(), indent=2))
        if args.contract:
            args.contract.write_text(json.dumps(report.contract(), indent=2), encoding="utf-8")
        return

    contract = json.loads(args.contract_file.read_text(encoding="utf-8"))
    violations = validate_csv(text, contract)
    print(json.dumps({"valid": not violations, "violations": violations}, indent=2))
    if violations:
        raise SystemExit(2)


if __name__ == "__main__":
    main()
