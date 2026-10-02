"""CLI for ChangeScribe."""
import argparse,json
from pathlib import Path
from dotenv import load_dotenv
from agent import ChangeScribeAgent

def main()->None:
 parser=argparse.ArgumentParser(description="Generate release notes from commit messages.")
 parser.add_argument("commits_file",type=Path,help="JSON array of full commit messages")
 parser.add_argument("--output",type=Path);parser.add_argument("--local",action="store_true")
 args=parser.parse_args();load_dotenv()
 messages=json.loads(args.commits_file.read_text(encoding="utf-8"))
 if not isinstance(messages,list) or not all(isinstance(x,str) for x in messages):raise SystemExit("Input must be a JSON array of strings")
 report=ChangeScribeAgent(use_model=not args.local).write(messages)
 rendered=report.polished_markdown or report.markdown
 if args.output:args.output.write_text(rendered,encoding="utf-8")
 else:print(rendered)
if __name__=="__main__":main()
