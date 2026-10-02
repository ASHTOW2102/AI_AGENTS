"""CLI for EnvDoctor."""
import argparse,json
from pathlib import Path
from dotenv import load_dotenv
from agent import EnvDoctorAgent

def main()->None:
 parser=argparse.ArgumentParser(description="Compare an env file with its template safely.")
 parser.add_argument("template",type=Path);parser.add_argument("actual",type=Path)
 parser.add_argument("--local",action="store_true")
 args=parser.parse_args();load_dotenv()
 report=EnvDoctorAgent(use_model=not args.local).inspect(args.template.read_text(encoding="utf-8"),args.actual.read_text(encoding="utf-8"))
 print(json.dumps(report.to_dict(),indent=2))
 if not report.valid:raise SystemExit(2)
if __name__=="__main__":main()
