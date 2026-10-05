# CacheGuard

CacheGuard audits sanitized HTTP response metadata for caching mistakes that can leak user-specific content or waste performance.

It detects:

- sensitive responses without no-store;
- authenticated responses permitted in shared caches;
- public caching on responses that set cookies;
- missing Vary: Authorization where relevant;
- contradictory Cache-Control directives;
- immutable on dynamic responses;
- missing policies and uncached static assets.

It never sends requests and needs no response bodies, cookies, tokens, or URLs beyond a route path. Deterministic checks run without credentials. With OPENAI_API_KEY, the agent explains only sanitized findings.

## Setup

~~~bash
cd CacheGuard
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
~~~

Copy .env.example to .env only for optional AI explanations. Never commit .env.

## Input and usage

Provide a JSON array containing path, method, status, cache_control, vary, and boolean context flags. See example_responses.json.

~~~bash
python cli.py example_responses.json --no-model
python cli.py responses.json
~~~

The CLI exits with 0 for a clean audit, 2 for findings, or an argparse error for malformed input.

## Tests

~~~bash
pip install -r requirements-dev.txt
python -m pytest -q
~~~

## Scope

CacheGuard checks declared metadata. It does not model every browser, proxy, CDN, framework default, or cache-key configuration. Verify fixes in the actual delivery path.
