import argparse,json
from pathlib import Path
from agent import ReplicationWatchAgent
def main():
    p=argparse.ArgumentParser(description="ReplicationWatch audits replica metadata for excessive lag, unhealthy state, missing failover tests, and cross-region gaps.");p.add_argument("input");a=p.parse_args()
    try:r=ReplicationWatchAgent().inspect(json.loads(Path(a.input).read_text(encoding="utf-8")))
    except (OSError,UnicodeError,json.JSONDecodeError,ValueError) as e:p.error(str(e))
    print(json.dumps(r.to_dict(),indent=2));return 0 if r.healthy else 2
if __name__=="__main__":raise SystemExit(main())
