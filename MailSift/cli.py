"""CLI for MailSift."""
import argparse,json
from pathlib import Path
from dotenv import load_dotenv
from agent import MailSiftAgent

def main()->None:
 parser=argparse.ArgumentParser(description="Triage an RFC 5322 email file.")
 parser.add_argument("email_file",type=Path)
 parser.add_argument("--local",action="store_true")
 parser.add_argument("--fail-on-phishing",action="store_true")
 args=parser.parse_args(); load_dotenv()
 report=MailSiftAgent(use_model=not args.local).inspect(args.email_file.read_bytes())
 print(json.dumps(report.to_dict(),indent=2))
 if args.fail_on_phishing and report.phishing_flags: raise SystemExit(2)
if __name__=="__main__": main()
