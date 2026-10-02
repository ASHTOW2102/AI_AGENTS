# MailSift

MailSift is a privacy-aware email triage agent for local EML files. It produces structured JSON without connecting to an inbox or sending messages.

The offline engine parses email, redacts sensitive identifiers, scores urgency, flags common phishing signals, and extracts action-oriented sentences. With an OpenAI key, it adds a briefing based only on the redacted report; raw email is never sent to the model.

## Setup

```bash
cd MailSift
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
copy .env.example .env
```

## Usage

```bash
python cli.py message.eml --local
python cli.py suspicious.eml --fail-on-phishing
```

The second command exits with status 2 when phishing indicators appear.

## Tests

```bash
pip install -r requirements-dev.txt
pytest -q
```

## Safety

Indicators are not proof that mail is safe or malicious. Never open links or attachments solely because of this output. Verify consequential requests through a separate trusted channel.
