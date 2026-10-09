import argparse
import json
from pathlib import Path
from agent import TokenScopeAgent

def main() -> int:
    parser = argparse.ArgumentParser(description="TokenScope audits API-token inventories for admin scopes, missing expiry, stale usage, and absent owners without reading token values.")
    parser.add_argument("input", help="Path to JSON input")
    args = parser.parse_args()
    try:
        payload=json.loads(Path(args.input).read_text(encoding="utf-8"))
        report=TokenScopeAgent().inspect(payload)
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError) as error:
        parser.error(str(error))
    print(json.dumps(report.to_dict(), indent=2))
    return 0 if report.healthy else 2

if __name__ == "__main__":
    raise SystemExit(main())
