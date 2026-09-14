---
title: UK Housing & Renting Assistant
emoji: 🇬🇧
colorFrom: blue
colorTo: indigo
sdk: gradio
python_version: "3.11"
---

# 🇬🇧 UK Housing & Renting Assistant

A Gradio + OpenAI Agents SDK assistant for practical UK housing and renting
questions. It can search the official GOV.UK Search API and fetch GOV.UK pages
before answering.

## Important: Ollama and Hugging Face Spaces

This project supports Ollama for local development.

A Hugging Face Space cannot use `http://localhost:11434` to reach Ollama running
on your personal computer. For a public Space, use either:

- an OpenAI-compatible hosted endpoint, or
- a remotely reachable Ollama server that you control.

Keep the provider switch in `.env` / Space Secrets.

## Local setup

Install Ollama and pull a chat model, for example:

```powershell
ollama pull gpt-oss:20b
```

Create a virtual environment:

```powershell
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements-local.txt
```

Copy `.env.example` to `.env`, then:

```powershell
python app.py
```

The app will normally be available at the local Gradio URL printed in the
terminal.

## Hosted OpenAI-compatible provider

Set these environment variables:

```text
MODEL_PROVIDER=openai
OPENAI_BASE_URL=https://api.openai.com/v1
OPENAI_API_KEY=...
OPENAI_MODEL=...
```

For another OpenAI-compatible provider, set its base URL and model name.

## Hugging Face Spaces

Create a new **Gradio Space**, then upload:

- `app.py`
- `agent.py`
- `tools/`
- `requirements.txt`
- `README.md`

Do NOT upload `.env`.

Add provider credentials as Space Secrets / environment variables.

For example:

```text
MODEL_PROVIDER=openai
OPENAI_BASE_URL=...
OPENAI_API_KEY=...
OPENAI_MODEL=...
```

If you want Ollama in production, `OLLAMA_BASE_URL` must point to a reachable
Ollama server, not localhost.

## What it does

The assistant can help with:

- rent and rent increases
- deposits
- tenancy agreements
- repairs
- damp and mould
- landlord/tenant responsibilities
- ending a tenancy
- eviction and notices
- rent arrears
- letting agents
- bills and utilities
- council/housing navigation
- homelessness/housing-help navigation

It answers in English, Hindi or Hinglish depending on the user's language.

## Safety

This is an information assistant, not a solicitor or government service.
Housing law differs across England, Scotland, Wales and Northern Ireland. The
agent is instructed to establish the jurisdiction and use current official
sources rather than guessing.

## Architecture

```text
Gradio
   |
   v
Housing Agent (OpenAI Agents SDK)
   |
   +--> GOV.UK Search API
   |
   +--> GOV.UK page fetcher
   |
   +--> Safe calculator
   |
   v
Ollama / OpenAI-compatible model
```
