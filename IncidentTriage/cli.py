"""Command-line interface for IncidentTriage."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from dotenv import load_dotenv

from agent import IncidentTriageAgent


def main() -> None:
    parser = argparse.ArgumentParser(description="Turn an incident report into an action plan.")
    source = parser.add_mutually_exclusive_group(required=True)
    source.add_argument("--text", help="Incident description")
    source.add_argument("--file", type=Path, help="UTF-8 text file containing the incident")
    parser.add_argument("--local", action="store_true", help="Never call an external model")
    args = parser.parse_args()

    load_dotenv()
    incident = args.text if args.text is not None else args.file.read_text(encoding="utf-8")
    report = IncidentTriageAgent(use_model=not args.local).run(incident)
    print(json.dumps(report.to_dict(), indent=2))


if __name__ == "__main__":
    main()
