import argparse
import json
from pathlib import Path
from agent import ContainerCheckAgent

def main() -> int:
    parser=argparse.ArgumentParser(description="ContainerCheck audits container specifications for root execution, privileged mode, mutable filesystems, and missing resource limits.")
    parser.add_argument("input",help="Path to JSON input")
    args=parser.parse_args()
    try:
        report=ContainerCheckAgent().inspect(json.loads(Path(args.input).read_text(encoding="utf-8")))
    except (OSError,UnicodeError,json.JSONDecodeError,ValueError) as error:
        parser.error(str(error))
    print(json.dumps(report.to_dict(),indent=2))
    return 0 if report.healthy else 2

if __name__=="__main__":
    raise SystemExit(main())
