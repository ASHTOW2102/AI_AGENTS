from __future__ import annotations

import argparse
import json
from pathlib import Path

from agent import ADRGuardAgent


def main() -> int:
    parser = argparse.ArgumentParser(description="Audit an Architecture Decision Record.")
    parser.add_argument("adr", help="Path to an ADR Markdown file")
    parser.add_argument("--no-model", action="store_true", help="Disable optional AI explanation")
    args = parser.parse_args()

    path = Path(args.adr)
    try:
        markdown = path.read_text(encoding="utf-8")
        report = ADRGuardAgent(use_model=not args.no_model).inspect(
            markdown,
            source_path=str(path),
        )
    except (OSError, ValueError) as error:
        parser.error(str(error))

    print(json.dumps(report.to_dict(), indent=2))
    return 0 if report.valid else 2


if __name__ == "__main__":
    raise SystemExit(main())
