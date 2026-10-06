import argparse
import json
from pathlib import Path
from agent import ConfigDiffAgent

def main() -> int:
    parser = argparse.ArgumentParser(description="ConfigDiff compares flat JSON configurations and highlights missing keys, changed security controls, new keys, and debug mode.")
    parser.add_argument("input", help="Path to the JSON input")
    args = parser.parse_args()
    try:
        payload = json.loads(Path(args.input).read_text(encoding="utf-8"))
        report = ConfigDiffAgent().inspect(payload)
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError) as error:
        parser.error(str(error))
    print(json.dumps(report.to_dict(), indent=2))
    return 0 if report.healthy else 2

if __name__ == "__main__":
    raise SystemExit(main())
