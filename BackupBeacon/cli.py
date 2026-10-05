import argparse, json
from pathlib import Path
from agent import BackupBeaconAgent

def main() -> int:
    parser = argparse.ArgumentParser(description="Audit backup freshness, protection, and restore evidence.")
    parser.add_argument("audit", help="Path to backup metadata JSON")
    parser.add_argument("--no-model", action="store_true")
    args = parser.parse_args()
    try:
        payload = json.loads(Path(args.audit).read_text(encoding="utf-8"))
        report = BackupBeaconAgent(use_model=not args.no_model).inspect(payload)
    except (OSError, json.JSONDecodeError, ValueError) as error:
        parser.error(str(error))
    print(json.dumps(report.to_dict(), indent=2))
    return 0 if report.valid else 2

if __name__ == "__main__":
    raise SystemExit(main())
