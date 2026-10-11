import argparse,json
from pathlib import Path
from agent import EnvParityAgent
def main():
    p=argparse.ArgumentParser(description="EnvParity audits environment metadata for drift, missing owners, debug mode, and untracked overrides.");p.add_argument("input");a=p.parse_args()
    try:r=EnvParityAgent().inspect(json.loads(Path(a.input).read_text(encoding="utf-8")))
    except (OSError,UnicodeError,json.JSONDecodeError,ValueError) as e:p.error(str(e))
    print(json.dumps(r.to_dict(),indent=2));return 0 if r.healthy else 2
if __name__=="__main__":raise SystemExit(main())
