import argparse
import json
from pathlib import Path

from agent import CacheGuardAgent


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Audit sanitized HTTP response metadata for cache-safety risks."
    )
    parser.add_argument("responses", help="Path to a JSON response array")
    parser.add_argument("--no-model", action="store_true")
    args = parser.parse_args()
    try:
        payload = json.loads(Path(args.responses).read_text(encoding="utf-8"))
        report = CacheGuardAgent(use_model=not args.no_model).inspect(payload)
    except (OSError, json.JSONDecodeError, ValueError) as error:
        parser.error(str(error))
    print(json.dumps(report.to_dict(), indent=2))
    return 0 if report.valid else 2


if __name__ == "__main__":
    raise SystemExit(main())
