from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from agent import RetryRightAgent


def _load(path: str) -> list[dict[str, Any]]:
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    if not isinstance(data, list):
        raise ValueError("trace file must contain a JSON array")
    return data


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Audit an HTTP retry trace for resilience and safety mistakes."
    )
    parser.add_argument("trace", help="Path to a JSON retry trace")
    parser.add_argument("--max-attempts", type=int, default=4)
    parser.add_argument("--min-delay-ms", type=float, default=100.0)
    parser.add_argument(
        "--no-model",
        action="store_true",
        help="Disable optional AI explanations",
    )
    args = parser.parse_args()

    try:
        report = RetryRightAgent(use_model=not args.no_model).inspect(
            _load(args.trace),
            max_attempts=args.max_attempts,
            min_delay_ms=args.min_delay_ms,
        )
    except (OSError, json.JSONDecodeError, ValueError) as error:
        parser.error(str(error))

    print(json.dumps(report.to_dict(), indent=2))
    return 0 if report.valid else 2


if __name__ == "__main__":
    raise SystemExit(main())
