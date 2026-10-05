# MeetingPulse

MeetingPulse privately audits structured meeting notes for participation balance and follow-through.

It detects:

- one speaker contributing more than a configurable share of words;
- long turns by word count or duration;
- listed attendees with no recorded speaking turn;
- actions without an owner or ISO due date;
- meetings with no recorded decision.

The deterministic analysis works locally without credentials. With OPENAI_API_KEY, the agent can suggest improvements using only aggregate metrics and findings. Transcript text is never sent to the model.

## Setup

~~~bash
cd MeetingPulse
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
~~~

Copy .env.example to .env only for optional AI explanations. Never commit .env.

## Input

Provide JSON with participants, chronological turns, decisions, and actions. Each turn needs speaker and text; duration_seconds is optional. Each action needs task, owner, and an ISO date.

See example_meeting.json.

## Usage

~~~bash
python cli.py example_meeting.json --no-model
python cli.py meeting.json --dominance-threshold 0.70 --monologue-words 180
~~~

The CLI prints JSON and exits with 0 when all checks pass, 2 for findings, or an argparse error for invalid input.

## Tests

~~~bash
pip install -r requirements-dev.txt
python -m pytest -q
~~~

## Privacy and scope

MeetingPulse measures observable transcript and action metadata. It does not infer personality, intent, protected traits, or employee performance. Automated transcripts may contain errors, so findings should support facilitation—not personnel decisions.
