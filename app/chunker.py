def chunk_text(text: str, size: int = 500, overlap: int = 100) -> list[str]:
    chunks = []
    start = 0
    while start < len(text):
        chunks.append(text[start:start + size])
        start += size - overlap
    return chunks


if __name__ == "__main__":
    from pathlib import Path
    from pdf_reader import read_pdf

    for pdf in Path("data").glob("*.pdf"):
        chunks = chunk_text(read_pdf(str(pdf)))
        print(f"{pdf.name}: {len(chunks)} chunks")
    print("\nSample chunk:\n", chunks[1])