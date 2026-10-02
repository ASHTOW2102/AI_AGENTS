# IncidentTriage

IncidentTriage turns a raw operational incident report into a structured response plan. It is deliberately useful without an API key: a deterministic engine classifies urgency and generates first-response steps. When OpenAI credentials are available, the agent improves the report while retaining a safe local fallback.

Before any external model call, common API keys, access keys, tokens, passwords, and secrets are replaced with `[REDACTED]`.

## Output

The JSON report includes:

- severity and confidence
- concise incident title and summary
- immediate containment actions
- investigation questions
- a factual customer-status update
- redaction count and execution mode

## Setup

```bash
cd IncidentTriage
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
copy .env.example .env  # Windows
# cp .env.example .env  # macOS/Linux
```

An API key is optional. Leave `OPENAI_API_KEY` empty for local mode.

## Usage

```bash
python cli.py --local --text "Checkout requests return 500 for EU customers"
python cli.py --file incident.txt
```

The second command uses OpenAI only when `OPENAI_API_KEY` is configured. Model-format errors safely fall back to the local report.

## Tests

```bash
pip install -r requirements-dev.txt
pytest -q
```

## Safety boundaries

This is a coordination aid, not an autonomous remediation system. It never executes infrastructure changes. Validate impact and obtain the appropriate approval before applying suggested actions.
