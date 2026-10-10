from pathlib import Path
from pypdf import PdfReader


def read_pdf(path: str) -> str:
    """Return all the text from a PDF file as one string."""
    reader = PdfReader(path)
    pages = []
    for page in reader.pages:
        text = page.extract_text() or ""
        pages.append(text)
    return "\n".join(pages)


if __name__ == "__main__":
    for pdf_path in Path("data").glob("*.pdf"):
        text = read_pdf(str(pdf_path))
        print(f"{pdf_path.name}: {len(text)} characters")
        print(text[:500])
        print("-" * 40)