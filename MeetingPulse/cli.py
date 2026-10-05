from __future__ import annotations

import argparse
import json
from pathlib import Path

from agent import MeetingPulseAgent


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Audit meeting participation, decisions, and action ownership."
    )
    parser.add_argument("meeting", help="Path to a meeting JSON file")
    parser.add_argument("--dominance-threshold", type=float, default=0.65)
    parser.add_argument("--monologue-words", type=int, default=150)
    parser.add_argument("--no-model", action="store_true")
    args = parser.parse_args()

    try:
        payload = json.loads(Path(args.meeting).read_text(encoding="utf-8"))
        report = MeetingPulseAgent(use_model=not args.no_model).inspect(
            payload,
            dominance_threshold=args.dominance_threshold,
            monologue_words=args.monologue_words,
        )
    except (OSError, json.JSONDecodeError, ValueError) as error:
        parser.error(str(error))

    print(json.dumps(report.to_dict(), indent=2, ensure_ascii=False))
    return 0 if report.valid else 2


if __name__ == "__main__":
    raise SystemExit(main())
