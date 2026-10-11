import argparse,json
from pathlib import Path
from agent import PinDoctorAgent
def main():
    p=argparse.ArgumentParser(description="PinDoctor audits dependency metadata for floating versions, stale releases, untrusted sources, and missing hashes.");p.add_argument("input");a=p.parse_args()
    try:r=PinDoctorAgent().inspect(json.loads(Path(a.input).read_text(encoding="utf-8")))
    except (OSError,UnicodeError,json.JSONDecodeError,ValueError) as e:p.error(str(e))
    print(json.dumps(r.to_dict(),indent=2));return 0 if r.healthy else 2
if __name__=="__main__":raise SystemExit(main())
