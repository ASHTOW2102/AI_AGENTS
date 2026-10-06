import argparse, json
from pathlib import Path
from agent import CronGuardAgent

def main() -> int:
    parser = argparse.ArgumentParser(description="Audit interval-based scheduled jobs for overlap and collision risks.")
    parser.add_argument("schedule", help="Path to scheduled-jobs JSON")
    parser.add_argument("--no-model", action="store_true")
    args = parser.parse_args()
    try:
        jobs = json.loads(Path(args.schedule).read_text(encoding="utf-8"))
        report = CronGuardAgent(use_model=not args.no_model).inspect(jobs)
    except (OSError, json.JSONDecodeError, ValueError) as error:
        parser.error(str(error))
    print(json.dumps(report.to_dict(), indent=2))
    return 0 if report.valid else 2

if __name__ == "__main__":
    raise SystemExit(main())
