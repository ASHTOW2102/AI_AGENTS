"""SpeakScore - Gradio UI for the speaking-practice scoring agent."""

import gradio as gr
import spaces

from model_provider import current_provider_label
from speaking_agent import score_speaking
from transcriber import transcribe_audio

LANGUAGES = [
    "English", "Spanish", "French", "German", "Italian", "Portuguese",
    "Hindi", "Japanese", "Mandarin Chinese", "Korean", "Arabic", "Russian",
]

CUSTOM_CSS = """
.gradio-container { max-width: 1000px !important; margin: auto !important; }
#hero {
    background: linear-gradient(135deg, #0891b2 0%, #4f46e5 100%);
    color: white; padding: 1.75rem 2rem; border-radius: 20px; margin-bottom: 1rem;
}
#hero h1 { margin: 0; font-size: 1.9rem; }
#hero p { margin: 0.35rem 0 0 0; opacity: 0.92; }
.score-card { font-family: inherit; }
.score-card .overall {
    display: flex; align-items: baseline; gap: 0.5rem; margin-bottom: 0.75rem;
}
.score-card .overall .num { font-size: 2.5rem; font-weight: 800; }
.score-card .bar-row { margin: 0.6rem 0; }
.score-card .bar-label { display:flex; justify-content:space-between; font-size:0.85rem; margin-bottom:2px; }
.score-card .bar-track { background: rgba(127,127,127,0.25); border-radius: 6px; height: 8px; overflow:hidden; }
.score-card .bar-fill { height: 100%; border-radius: 6px; background: linear-gradient(90deg,#0891b2,#4f46e5); }
.score-card .comment { font-size: 0.82rem; opacity: 0.75; margin: 2px 0 10px 0; }
"""

THEME = gr.themes.Soft(primary_hue="cyan", secondary_hue="indigo")


@spaces.GPU
def _zero_gpu_startup_probe():
    # See DocBrief for why this no-op exists: satisfies HF's ZeroGPU
    # startup check on Spaces that get auto-assigned that hardware.
    return True


def _bar(label: str, score: int, comment: str) -> str:
    score = max(0, min(100, int(score)))
    return f"""
    <div class="bar-row">
      <div class="bar-label"><span>{label}</span><span>{score}/100</span></div>
      <div class="bar-track"><div class="bar-fill" style="width:{score}%"></div></div>
      <div class="comment">{comment}</div>
    </div>"""


def render_score_card(data: dict) -> str:
    if "raw" in data:
        return f"<div class='score-card'><p>Couldn't parse a structured score, here's the raw feedback:</p><pre>{data['raw']}</pre></div>"

    overall = data.get("overall_score", 0)
    level = data.get("estimated_level", "")
    html = f"""<div class="score-card">
      <div class="overall"><span class="num">{overall}</span><span>/100 - {level}</span></div>
    """
    for key, label in [
        ("fluency_pacing", "Fluency & Pacing"),
        ("grammar", "Grammar"),
        ("vocabulary", "Vocabulary"),
        ("coherence", "Coherence"),
    ]:
        d = data.get(key, {})
        html += _bar(label, d.get("score", 0), d.get("comment", ""))

    corrections = data.get("corrections") or []
    if corrections:
        html += "<p><strong>Corrections</strong></p><ul>"
        html += "".join(f"<li>{c}</li>" for c in corrections)
        html += "</ul>"

    tips = data.get("tips") or []
    if tips:
        html += "<p><strong>Tips</strong></p><ul>"
        html += "".join(f"<li>{t}</li>" for t in tips)
        html += "</ul>"

    html += "</div>"
    return html


def analyze(language, audio_path, progress=gr.Progress()):
    if not audio_path:
        return "⚠️ Record something first.", ""

    progress(0.2, desc="Transcribing your speech...")
    try:
        transcript = transcribe_audio(audio_path)
    except Exception as exc:
        return f"⚠️ Transcription failed: {exc}", ""

    if not transcript.strip():
        return "⚠️ No speech detected - try recording again, a bit closer to the mic.", ""

    words_per_minute = None
    try:
        import soundfile as sf

        info = sf.info(audio_path)
        minutes = info.duration / 60
        if minutes > 0:
            words_per_minute = len(transcript.split()) / minutes
    except Exception:
        pass

    progress(0.6, desc="Scoring your speaking...")
    try:
        data = score_speaking(language, transcript, words_per_minute)
    except Exception as exc:
        return f"⚠️ Scoring failed: {exc}", transcript

    return render_score_card(data), transcript


with gr.Blocks(title="SpeakScore") as demo:
    gr.HTML(
        """
        <div id="hero">
            <h1>🎙️ SpeakScore - Speaking Practice Agent</h1>
            <p>Pick a language, record yourself speaking, and get scored on fluency, grammar, vocabulary, and coherence.</p>
        </div>
        """
    )
    gr.Markdown(f"**Scoring model:** `{current_provider_label()}` · **Transcription:** Hugging Face Whisper")
    gr.Markdown(
        "_Note: this scores what you said (fluency/pacing, grammar, vocabulary, coherence) "
        "from a text transcript - it can't judge your accent or pronunciation, since it never "
        "hears the actual audio quality, only the transcribed words._"
    )

    with gr.Row():
        with gr.Column(scale=1):
            language = gr.Dropdown(LANGUAGES, value="English", label="Language you're practicing")
            audio = gr.Audio(sources=["microphone"], type="filepath", label="Record yourself speaking")
            analyze_btn = gr.Button("🎯 Score My Speaking", variant="primary")
            transcript_out = gr.Textbox(label="Transcript", lines=6, interactive=False)
        with gr.Column(scale=1):
            score_out = gr.HTML("<p style='opacity:0.6'>Your score will appear here.</p>")

    analyze_btn.click(fn=analyze, inputs=[language, audio], outputs=[score_out, transcript_out])

if __name__ == "__main__":
    demo.launch(theme=THEME, css=CUSTOM_CSS)
