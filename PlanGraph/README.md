# PlanGraph

PlanGraph converts a JSON task list into an explainable project schedule. Its offline graph engine validates dependencies, detects cycles, calculates earliest start and finish times, finds the critical path, and warns about high-fan-out bottlenecks.

With an OpenAI key, it can add a delivery-risk briefing based only on the computed schedule.

## Input format

```json
[
  {"id": "design", "duration": 2},
  {"id": "build", "duration": 5, "depends_on": ["design"]},
  {"id": "test", "duration": 2, "depends_on": ["build"]}
]
```

Durations may represent hours, days, or story-point time, but must use one consistent unit.

## Setup and usage

```bash
cd PlanGraph
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
copy .env.example .env
python cli.py plan.json --local
```

## Tests

```bash
pip install -r requirements-dev.txt
pytest -q
```

## Limitations

The schedule assumes unlimited parallel resources and deterministic durations. Review resource constraints, calendars, uncertainty, and external dependencies before committing to dates.
