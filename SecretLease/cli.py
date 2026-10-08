import argparse
import json
from pathlib import Path
from agent import SecretLeaseAgent

def main() -> int:
    parser = argparse.ArgumentParser(description="SecretLease audits secret metadata without reading secret values, finding overdue rotation, missing owners, broad scope, and absent expiry.")
    parser.add_argument("input", help="Path to the JSON input")
    args = parser.parse_args()
    try:
        payload = json.loads(Path(args.input).read_text(encoding="utf-8"))
        report = SecretLeaseAgent().inspect(payload)
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError) as error:
        parser.error(str(error))
    print(json.dumps(report.to_dict(), indent=2))
    return 0 if report.healthy else 2

if __name__ == "__main__":
    raise SystemExit(main())
