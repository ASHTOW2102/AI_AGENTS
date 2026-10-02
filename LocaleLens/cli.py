"""CLI for LocaleLens."""
import argparse,json
from pathlib import Path
from dotenv import load_dotenv
from agent import LocaleLensAgent
def main()->None:
 parser=argparse.ArgumentParser(description="Compare locale JSON with its base catalog.")
 parser.add_argument("base_file",type=Path);parser.add_argument("locale_file",type=Path);parser.add_argument("--local",action="store_true")
 args=parser.parse_args();load_dotenv()
 base=json.loads(args.base_file.read_text(encoding="utf-8"));locale=json.loads(args.locale_file.read_text(encoding="utf-8"))
 report=LocaleLensAgent(use_model=not args.local).inspect(base,locale)
 print(json.dumps(report.to_dict(),indent=2,ensure_ascii=False))
 if not report.valid:raise SystemExit(2)
if __name__=="__main__":main()
