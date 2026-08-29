---
title: DocBrief
emoji: 📄
colorFrom: indigo
colorTo: purple
sdk: gradio
sdk_version: 6.26.0
app_file: app.py
pinned: false
---

# DocBrief - Document Summarizer Agent

DocBrief is a small AI agent that summarizes text or uploaded documents
(`.txt`, `.md`, `.pdf`, `.docx`). It's built with the
[Strands Agents](https://strandsagents.com) SDK, has a [Gradio](https://gradio.app)
UI, and deploys directly as a free, public
[Hugging Face Space](https://huggingface.co/spaces/AshishChaturvedi7/docbrief) -
usable by anyone with the link, no login required.

**Live demo:** https://huggingface.co/spaces/AshishChaturvedi7/docbrief

## Features

- Paste raw text or upload a `.txt`, `.md`, `.pdf`, or `.docx` file
- Three summary styles: concise, detailed, or bullet points
- Handles long documents via a map-reduce pass (summarizes chunks, then
  merges them) so it isn't limited by a small model's context window
- Word-count and reduction-percentage stats on every summary
- **Model-agnostic**: the LLM backend is swappable with a one-line config
  change - no code edits - between a local Ollama model, OpenAI, Anthropic,
  or Hugging Face's hosted Inference Providers

## How it's built

| File | Responsibility |
|---|---|
| `app.py` | Gradio UI - also the entrypoint Hugging Face Spaces runs |
| `summarizer_agent.py` | The actual Strands agent: system prompt, summary styles, map-reduce chunking for long documents |
| `model_provider.py` | **The only file that knows which LLM backend is active.** Everything else calls `get_model()` and never imports a provider SDK directly |
| `document_loader.py` | Extracts plain text from uploaded `.pdf` / `.docx` / `.txt` / `.md` files |

The `model_provider.py` abstraction is the core design idea: switching from a
local Ollama model to OpenAI, Anthropic, or Hugging Face's own hosted models
is a `.env` (or Space secret) edit, never a code change.

## Run it locally

Requires Python 3.10+.

```bash
git clone https://github.com/ASHTOW2102/AI_AGENTS.git
cd AI_AGENTS/DocBrief
python -m venv .venv
.venv\Scripts\activate        # Windows; use `source .venv/bin/activate` on macOS/Linux
pip install -r requirements.txt
```

### Option A: local model with Ollama (free, offline, default)

1. Install Ollama: https://ollama.com/download
2. Pull a model, e.g. `ollama pull llama3.1`
3. Copy the env template: `copy .env.example .env` (Windows) or
   `cp .env.example .env` (macOS/Linux) - the defaults already point at
   `http://localhost:11434` and `llama3.1`
4. Run it: `python app.py` → opens at http://localhost:7860

### Option B: a hosted model (OpenAI / Anthropic / Hugging Face)

Skip Ollama and set the provider in `.env` instead - see
[Switching providers](#switching-providers) below.

## Deploy your own copy to Hugging Face Spaces (free, global)

This repo is already shaped like a Space - the YAML block at the top of this
README is Space metadata (`sdk: gradio`, `app_file: app.py`).

**Ollama can't run inside a Gradio Space** (no way to run a background system
process there), so the deployed Space is configured to use
`MODEL_PROVIDER=huggingface` instead, which calls Hugging Face's own free
Inference Providers API. Local development keeps using Ollama; nothing else
about the code changes.

1. Create the Space: https://huggingface.co/new-space → SDK **Gradio** → any
   name → visibility **Public**.
2. Push this repo's contents to it:
   ```bash
   huggingface-cli login          # run this yourself - it's interactive
   git remote add space https://huggingface.co/spaces/<your-username>/<space-name>
   git push space main
   ```
   (Or drag-and-drop the files into the Space's "Files" tab in the browser.)
3. In the Space's **Settings → Repository secrets**, add:
   - `MODEL_PROVIDER` = `huggingface`
   - `HF_TOKEN` = a token from https://huggingface.co/settings/tokens
     (`read` scope is enough)
   - optionally `HF_MODEL` to use a different model (default:
     `meta-llama/Llama-3.1-8B-Instruct`)
4. The Space rebuilds automatically and is live at
   `https://huggingface.co/spaces/<your-username>/<space-name>`.

`.env` is only used locally - it's git-ignored and never committed; secrets
for the deployed Space are set on its Settings page instead.

> **Note on Space hardware:** Hugging Face may auto-assign new Gradio Spaces
> "ZeroGPU" hardware, which refuses to start unless it detects at least one
> `@spaces.GPU`-decorated function. This app doesn't need a GPU (inference
> runs through a remote API), so `app.py` declares a harmless no-op one
> (`_zero_gpu_startup_probe`) purely to satisfy that check - it works
> identically on CPU-only hardware too.

## Switching providers

Edit `.env` (local) or the Space's secrets (deployed) - nothing else in the
project needs to change:

```env
MODEL_PROVIDER=ollama
OLLAMA_HOST=http://localhost:11434
OLLAMA_MODEL=llama3.1
```

```env
MODEL_PROVIDER=openai
OPENAI_API_KEY=sk-...
OPENAI_MODEL=gpt-4o-mini
```

```env
MODEL_PROVIDER=anthropic
ANTHROPIC_API_KEY=...
ANTHROPIC_MODEL=claude-sonnet-5
```

```env
MODEL_PROVIDER=huggingface
HF_TOKEN=hf_...
HF_MODEL=meta-llama/Llama-3.1-8B-Instruct
```

## Tech stack

- [Strands Agents](https://strandsagents.com) - agent framework
- [Gradio](https://gradio.app) - UI, and native Hugging Face Spaces deployment
- [Ollama](https://ollama.com) / [OpenAI](https://platform.openai.com) /
  [Anthropic](https://www.anthropic.com) / [Hugging Face Inference Providers](https://huggingface.co/docs/inference-providers)
  - pluggable LLM backends
- [pypdf](https://pypi.org/project/pypdf/) / [python-docx](https://pypi.org/project/python-docx/) - document text extraction
