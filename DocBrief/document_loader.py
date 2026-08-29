"""Extracts plain text from uploaded documents (.txt, .md, .pdf, .docx)."""

from io import BytesIO


def extract_text(filename: str, file_bytes: bytes) -> str:
    ext = filename.lower().rsplit(".", 1)[-1] if "." in filename else ""

    if ext in ("txt", "md"):
        return file_bytes.decode("utf-8", errors="ignore")

    if ext == "pdf":
        from pypdf import PdfReader

        reader = PdfReader(BytesIO(file_bytes))
        return "\n".join(page.extract_text() or "" for page in reader.pages)

    if ext == "docx":
        from docx import Document

        doc = Document(BytesIO(file_bytes))
        return "\n".join(p.text for p in doc.paragraphs)

    raise ValueError(f"Unsupported file type: .{ext}. Use .txt, .md, .pdf, or .docx")
