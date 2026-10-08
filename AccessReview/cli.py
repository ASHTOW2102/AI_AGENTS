import argparse
import json
from pathlib import Path
from agent import AccessReviewAgent

def main() -> int:
    parser = argparse.ArgumentParser(description="AccessReview audits account-access exports for dormant users, missing owners, admin privileges, and absent review dates.")
    parser.add_argument("input", help="Path to the JSON input")
    args = parser.parse_args()
    try:
        payload = json.loads(Path(args.input).read_text(encoding="utf-8"))
        report = AccessReviewAgent().inspect(payload)
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError) as error:
        parser.error(str(error))
    print(json.dumps(report.to_dict(), indent=2))
    return 0 if report.healthy else 2

if __name__ == "__main__":
    raise SystemExit(main())
