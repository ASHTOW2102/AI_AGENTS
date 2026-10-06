import argparse, json
from pathlib import Path
from agent import FlagDoctorAgent

def main() -> int:
    parser = argparse.ArgumentParser(description="Audit feature-flag lifecycle hygiene.")
    parser.add_argument("inventory", help="Path to feature-flag JSON")
    parser.add_argument("--stale-days", type=int, default=30)
    parser.add_argument("--no-model", action="store_true")
    args = parser.parse_args()
    try:
        payload = json.loads(Path(args.inventory).read_text(encoding="utf-8"))
        report = FlagDoctorAgent(use_model=not args.no_model).inspect(payload, stale_days=args.stale_days)
    except (OSError, json.JSONDecodeError, ValueError) as error:
        parser.error(str(error))
    print(json.dumps(report.to_dict(), indent=2))
    return 0 if report.valid else 2

if __name__ == "__main__":
    raise SystemExit(main())
