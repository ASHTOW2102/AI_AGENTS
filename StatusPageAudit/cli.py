import argparse,json
from pathlib import Path
from agent import StatusPageAuditAgent
def main():
    p=argparse.ArgumentParser(description="StatusPageAudit audits service status metadata for hidden components, stale tests, missing subscriptions, and absent owners.");p.add_argument("input");a=p.parse_args()
    try:r=StatusPageAuditAgent().inspect(json.loads(Path(a.input).read_text(encoding="utf-8")))
    except (OSError,UnicodeError,json.JSONDecodeError,ValueError) as e:p.error(str(e))
    print(json.dumps(r.to_dict(),indent=2));return 0 if r.healthy else 2
if __name__=="__main__":raise SystemExit(main())
