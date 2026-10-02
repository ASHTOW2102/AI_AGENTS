"""CLI for PlanGraph."""
import argparse,json
from pathlib import Path
from dotenv import load_dotenv
from agent import PlanGraphAgent

def main()->None:
 parser=argparse.ArgumentParser(description="Analyze task dependencies and critical path.")
 parser.add_argument("plan_file",type=Path)
 parser.add_argument("--local",action="store_true")
 args=parser.parse_args(); load_dotenv()
 data=json.loads(args.plan_file.read_text(encoding="utf-8"))
 if not isinstance(data,list): raise SystemExit("Plan JSON must be a list of tasks")
 report=PlanGraphAgent(use_model=not args.local).analyze(data)
 print(json.dumps(report.to_dict(),indent=2))
if __name__=="__main__": main()
