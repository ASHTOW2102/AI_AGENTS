import argparse
import json
from pathlib import Path
from agent import PIIGuardAgent, redact_json

def main() -> int:
    parser = argparse.ArgumentParser(description="Detect and mask likely personal data in text, JSON, or CSV files.")
    parser.add_argument("path", help="Input .txt, .log, .csv, or .json file")
    parser.add_argument("--output", help="Optional path for redacted content")
    parser.add_argument("--no-model", action="store_true")
    args = parser.parse_args()
    try:
        path = Path(args.path)
        text = path.read_text(encoding="utf-8")
        report = PIIGuardAgent(use_model=not args.no_model).inspect(text)
        redacted = json.dumps(redact_json(json.loads(text)), indent=2) if path.suffix.lower() == ".json" else report.redacted
        if args.output:
            Path(args.output).write_text(redacted, encoding="utf-8")
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError) as error:
        parser.error(str(error))
    payload = report.to_dict()
    payload["redacted"] = "<written to output>" if args.output else redacted
    print(json.dumps(payload, indent=2))
    return 0 if report.safe else 2

if __name__ == "__main__":
    raise SystemExit(main())
