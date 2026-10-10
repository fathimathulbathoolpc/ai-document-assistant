from pathlib import Path
import chromadb
from pdf_reader import read_pdf
from chunker import chunk_text

client = chromadb.PersistentClient(path="chroma_db")
collection = client.get_or_create_collection("docs")


def index_documents():
    for pdf in Path("data").glob("*.pdf"):
        chunks = chunk_text(read_pdf(str(pdf)))
        collection.upsert(
            ids=[f"{pdf.name}-{i}" for i in range(len(chunks))],
            documents=chunks,
            metadatas=[{"source": pdf.name, "chunk": i} for i in range(len(chunks))],
        )


def search(question: str, n: int = 3):
    return collection.query(query_texts=[question], n_results=n)


if __name__ == "__main__":
    index_documents()
    q = input("Ask a question: ")
    res = search(q)
    for doc, meta in zip(res["documents"][0], res["metadatas"][0]):
        print(f"\n[{meta['source']} #{meta['chunk']}]\n{doc}")