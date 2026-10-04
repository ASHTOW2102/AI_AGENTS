from __future__ import annotations

import argparse
import json
from pathlib import Path

from agent import CoverageCompassAgent


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Prioritize risky test gaps from coverage.py JSON."
    )
    parser.add_argument("report", help="Path to coverage.json")
    parser.add_argument("--threshold", type=float, default=80.0)
    parser.add_argument("--top", type=int, default=10)
    parser.add_argument("--no-model", action="store_true")
    args = parser.parse_args()

    try:
        payload = json.loads(Path(args.report).read_text(encoding="utf-8"))
        report = CoverageCompassAgent(use_model=not args.no_model).inspect(
            payload,
            threshold=args.threshold,
            top=args.top,
        )
    except (OSError, json.JSONDecodeError, ValueError) as error:
        parser.error(str(error))

    print(json.dumps(report.to_dict(), indent=2))
    return 0 if report.valid else 2


if __name__ == "__main__":
    raise SystemExit(main())
