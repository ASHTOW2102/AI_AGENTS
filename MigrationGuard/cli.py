import argparse
import json
from pathlib import Path
from agent import MigrationGuardAgent

def main() -> int:
    parser = argparse.ArgumentParser(description="Audit database migration metadata before rollout.")
    parser.add_argument("input", help="Path to migration JSON")
    parser.add_argument("--no-model", action="store_true")
    args = parser.parse_args()
    try:
        migrations = json.loads(Path(args.input).read_text(encoding="utf-8"))
        report = MigrationGuardAgent(use_model=not args.no_model).inspect(migrations)
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError) as error:
        parser.error(str(error))
    print(json.dumps(report.to_dict(), indent=2))
    return 0 if report.safe else 2

if __name__ == "__main__":
    raise SystemExit(main())
