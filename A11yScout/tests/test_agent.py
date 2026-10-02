import pytest
from agent import A11yScoutAgent,audit_html

GOOD='''<!doctype html><html lang="en"><body><h1>Title</h1><img src="x" alt="Chart"><label for="email">Email</label><input id="email"><button>Save</button></body></html>'''

def test_accessible_baseline_passes():
 report=audit_html(GOOD)
 assert report.valid and report.findings==[]

def test_detects_missing_lang_alt_label_and_button_name():
 report=audit_html('<html><body><img src="x"><input><button></button></body></html>')
 codes={x.code for x in report.findings}
 assert {"missing_lang","missing_alt","missing_label","empty_button"}<=codes
 assert not report.valid

def test_detects_heading_jump_as_warning():
 report=audit_html('<html lang="en"><h1>A</h1><h3>B</h3></html>')
 assert report.valid
 assert any(x.code=="heading_jump" for x in report.findings)

def test_aria_names_are_accepted():
 html='<html lang="en"><input aria-label="Search"><button aria-label="Close"></button></html>'
 assert audit_html(html).valid

def test_agent_works_without_key(monkeypatch):
 monkeypatch.delenv("OPENAI_API_KEY",raising=False)
 assert A11yScoutAgent().inspect(GOOD).mode=="local"
