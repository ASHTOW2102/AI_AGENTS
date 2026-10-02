"""CLI for A11yScout."""
import argparse,json
from pathlib import Path
from dotenv import load_dotenv
from agent import A11yScoutAgent

def main()->None:
 parser=argparse.ArgumentParser(description="Audit static HTML accessibility basics.")
 parser.add_argument("html_file",type=Path);parser.add_argument("--local",action="store_true")
 args=parser.parse_args();load_dotenv()
 report=A11yScoutAgent(use_model=not args.local).inspect(args.html_file.read_text(encoding="utf-8"))
 print(json.dumps(report.to_dict(),indent=2))
 if not report.valid:raise SystemExit(2)
if __name__=="__main__":main()
