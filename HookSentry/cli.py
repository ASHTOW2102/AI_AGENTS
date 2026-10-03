from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from agent import HookSentryAgent


def _load(path: str) -> list[dict[str, Any]]:
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    if not isinstance(data, list):
        raise ValueError("trace file must contain a JSON array")
    return data


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Audit webhook delivery traces for security and reliability risks."
    )
    parser.add_argument("trace", help="Path to a JSON webhook trace")
    parser.add_argument("--tolerance-seconds", type=float, default=300.0)
    parser.add_argument("--no-model", action="store_true")
    args = parser.parse_args()

    try:
        report = HookSentryAgent(use_model=not args.no_model).inspect(
            _load(args.trace),
            tolerance_seconds=args.tolerance_seconds,
        )
    except (OSError, json.JSONDecodeError, ValueError) as error:
        parser.error(str(error))

    print(json.dumps(report.to_dict(), indent=2))
    return 0 if report.valid else 2


if __name__ == "__main__":
    raise SystemExit(main())
