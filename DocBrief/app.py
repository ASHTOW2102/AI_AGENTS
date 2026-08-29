"""Gradio UI for the document summarizer agent - deployable directly as a HF Space."""

import time

import gradio as gr
import spaces

from document_loader import extract_text
from model_provider import current_provider_label
from summarizer_agent import summarize


@spaces.GPU
def _zero_gpu_startup_probe():
    # Unused. Hugging Face's ZeroGPU hardware refuses to start a Space unless
    # it detects at least one @spaces.GPU function at import time. This app
    # never needs a GPU (inference runs via a remote API), but declaring this
    # satisfies that check on Spaces that get assigned ZeroGPU hardware, and
    # is a no-op everywhere else.
    return True

CUSTOM_CSS = """
.gradio-container {
    max-width: 1100px !important;
    margin: auto !important;
}
#hero {
    background: linear-gradient(135deg, #4f46e5 0%, #7c3aed 100%);
    color: white;
    padding: 1.75rem 2rem;
    border-radius: 20px;
    margin-bottom: 1rem;
}
#hero h1 { margin: 0; font-size: 1.9rem; }
#hero p { margin: 0.35rem 0 0 0; opacity: 0.92; }
#provider-badge {
    font-family: monospace;
    font-size: 0.85rem;
}
"""

THEME = gr.themes.Soft(primary_hue="indigo", secondary_hue="violet")


def run_summary(pasted_text, uploaded_file, style_label, progress=gr.Progress()):
    style_map = {"Concise": "concise", "Detailed": "detailed", "Bullet points": "bullets"}

    text = ""
    preview = ""
    if uploaded_file is not None:
        with open(uploaded_file.name, "rb") as f:
            file_bytes = f.read()
        try:
            text = extract_text(uploaded_file.name, file_bytes)
        except Exception as exc:
            return "", f"⚠️ {exc}", ""
        preview = text[:1500] + ("..." if len(text) > 1500 else "")
    elif pasted_text and pasted_text.strip():
        text = pasted_text

    if not text.strip():
        return "", "⚠️ Please paste some text or upload a document first.", ""

    progress(0.2, desc="Reading document...")
    start = time.time()
    try:
        progress(0.5, desc="Summarizing...")
        summary = summarize(text, style=style_map.get(style_label, "concise"))
    except Exception as exc:
        return "", f"⚠️ Summarization failed: {exc}", preview

    elapsed = time.time() - start
    original_words = len(text.split())
    summary_words = len(summary.split())
    reduction = 0 if original_words == 0 else round((1 - summary_words / original_words) * 100)
    stats = (
        f"**{original_words}** words → **{summary_words}** words "
        f"(**{reduction}%** shorter) · {elapsed:.1f}s"
    )
    return summary, stats, preview


def clear_upload():
    return None


with gr.Blocks(title="DocBrief") as demo:
    gr.HTML(
        """
        <div id="hero">
            <h1>📄 DocBrief - Document Summarizer Agent</h1>
            <p>Paste text or upload a document and get a clean summary in seconds.</p>
        </div>
        """
    )
    gr.Markdown(f"**Active model:** `{current_provider_label()}`", elem_id="provider-badge")

    with gr.Row():
        with gr.Column(scale=1):
            gr.Markdown("### 1. Provide a document")
            pasted_text = gr.Textbox(
                label="Paste text",
                placeholder="Paste an article, report, email thread, meeting notes...",
                lines=12,
            )
            uploaded_file = gr.File(
                label="...or upload a file (.txt, .md, .pdf, .docx)",
                file_types=[".txt", ".md", ".pdf", ".docx"],
            )
            style_label = gr.Radio(
                ["Concise", "Detailed", "Bullet points"],
                value="Concise",
                label="Summary style",
            )
            with gr.Row():
                clear_btn = gr.Button("Clear")
                submit_btn = gr.Button("✨ Summarize", variant="primary")

        with gr.Column(scale=1):
            gr.Markdown("### 2. Summary")
            stats_md = gr.Markdown("")
            summary_out = gr.Markdown("_Your summary will appear here._")
            with gr.Accordion("Preview extracted text", open=False):
                preview_out = gr.Textbox(show_label=False, lines=10, interactive=False)

    submit_btn.click(
        fn=run_summary,
        inputs=[pasted_text, uploaded_file, style_label],
        outputs=[summary_out, stats_md, preview_out],
    )
    clear_btn.click(
        fn=lambda: ("", None, "Concise", "_Your summary will appear here._", "", ""),
        inputs=[],
        outputs=[pasted_text, uploaded_file, style_label, summary_out, stats_md, preview_out],
    )

if __name__ == "__main__":
    demo.launch(theme=THEME, css=CUSTOM_CSS)
