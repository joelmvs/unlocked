import pdfplumber
import os
import tempfile
from docx import Document

def extract_text_from_file(filename: str, file_bytes: bytes) -> str:
    # Handle PDF
    if filename.endswith(".pdf"):
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_file:
            temp_file.write(file_bytes)
            temp_file_path = temp_file.name

        text = ""
        with pdfplumber.open(temp_file_path) as doc:
            for page in doc.pages:
                text += page.extract_text()

        os.remove(temp_file_path)
        return text.strip()

    # Handle plain text
    elif filename.endswith(".txt"):
        return file_bytes.decode("utf-8").strip()

    # Handle Word (.docx)
    elif filename.endswith(".docx"):
        with tempfile.NamedTemporaryFile(delete=False, suffix=".docx") as temp_file:
            temp_file.write(file_bytes)
            temp_file_path = temp_file.name

        doc = Document(temp_file_path)
        text = "\n".join([para.text for para in doc.paragraphs])
        os.remove(temp_file_path)
        return text.strip()

    # Unsupported file type
    else:
        return "Unsupported file type. Please upload a PDF, DOCX, or plain text file."
