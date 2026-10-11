import argparse
import json
from pathlib import Path
from agent import FirewallLensAgent

def main() -> int:
    parser=argparse.ArgumentParser(description="FirewallLens audits firewall-rule exports for world-open access, unrestricted admin ports, missing owners, and permanent temporary rules.")
    parser.add_argument("input",help="Path to JSON input")
    args=parser.parse_args()
    try:
        report=FirewallLensAgent().inspect(json.loads(Path(args.input).read_text(encoding="utf-8")))
    except (OSError,UnicodeError,json.JSONDecodeError,ValueError) as error:
        parser.error(str(error))
    print(json.dumps(report.to_dict(),indent=2))
    return 0 if report.healthy else 2

if __name__=="__main__":
    raise SystemExit(main())
