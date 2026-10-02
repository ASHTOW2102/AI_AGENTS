"""CLI for OpenAPISentry."""
import argparse,json
from pathlib import Path
from dotenv import load_dotenv
from agent import OpenAPISentryAgent

def load_spec(path:Path):
 text=path.read_text(encoding="utf-8")
 if path.suffix.lower() in {".yaml",".yml"}:
  import yaml
  return yaml.safe_load(text)
 return json.loads(text)

def main()->None:
 parser=argparse.ArgumentParser(description="Audit an OpenAPI 3 specification.")
 parser.add_argument("spec_file",type=Path);parser.add_argument("--local",action="store_true")
 args=parser.parse_args();load_dotenv()
 report=OpenAPISentryAgent(use_model=not args.local).inspect(load_spec(args.spec_file))
 print(json.dumps(report.to_dict(),indent=2))
 if not report.valid:raise SystemExit(2)
if __name__=="__main__":main()
