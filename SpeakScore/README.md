
# SpeakScore - Speaking Practice Agent

Pick a language, record yourself speaking, and get scored on fluency/pacing,
grammar, vocabulary, and coherence - with specific corrections and tips.
Built with [Strands Agents](https://strandsagents.com) and a [Gradio](https://gradio.app)
UI, deployable directly as a free Hugging Face Space.

**What this does NOT do:** judge your accent or pronunciation. Scoring runs
on a Whisper transcript of what you said, not the raw audio quality, so it
can only assess word choice, grammar, pacing, and coherence - never accent.
The agent's system prompt is written to be upfront about this rather than
bluff a pronunciation score it can't actually produce.

## How it's built

| File | Responsibility |
|---|---|
| `app.py` | Gradio UI - also the Space entrypoint |
| `transcriber.py` | Speech-to-text via Hugging Face's Inference Providers (Whisper) - used for both local dev and deployment, since Ollama doesn't do ASR |
| `speaking_agent.py` | The Strands agent: scores the transcript + speaking pace, returns structured JSON (scores, comments, corrections, tips) |
| `model_provider.py` | The only file that knows which LLM backend scores the transcript - swap Ollama/OpenAI/Anthropic/Hugging Face via `.env`, no code changes |

## Run it locally

```bash
python -m venv .venv
.venv\Scripts\activate        # Windows
pip install -r requirements.txt
cp .env.example .env          # copy .env.example .env on Windows
```

You need **two things** in `.env`:

1. `HF_TOKEN` - always required, for the Whisper transcription step. Get one
   (read scope is enough) at https://huggingface.co/settings/tokens
2. A scoring backend - defaults to Ollama:
   - Install Ollama, `ollama pull llama3.1`, leave `MODEL_PROVIDER=ollama`
   - or set `MODEL_PROVIDER=openai` / `anthropic` / `huggingface` with the
     matching API key instead

Run it: `python app.py` → opens at http://localhost:7860

## Deploy to Hugging Face Spaces

Same pattern as this author's other agents (see `AI_AGENTS/DocBrief` in this
repo): create a Gradio Space, push this folder's contents to it, then add
`HF_TOKEN` (and optionally `MODEL_PROVIDER=huggingface`) as Space secrets.

> **Note on ZeroGPU:** `app.py` declares a harmless no-op `@spaces.GPU`
> function purely to satisfy Hugging Face's ZeroGPU startup check on Spaces
> that get auto-assigned that hardware - this app doesn't actually need a
> GPU, since both transcription and scoring run through remote APIs.

## Tech stack

- [Strands Agents](https://strandsagents.com) - agent framework
- [Gradio](https://gradio.app) - UI + microphone input + native Spaces deployment
- [Hugging Face Inference Providers](https://huggingface.co/docs/inference-providers) (Whisper) - speech-to-text
- Ollama / OpenAI / Anthropic / Hugging Face - pluggable scoring LLM backend
