from pdf_loader import load_pdf
from chunker import create_chunks
from vector_store import VectorStore


PDF_PATH = "data/documents/sample.pdf"


def ingest_pdf():

    print("Loading PDF...")

    pages = load_pdf(PDF_PATH)

    print("PDF loaded.")
    print("Pages:", len(pages))

    print("Creating chunks...")

    chunks = create_chunks(pages)

    print("Chunks created:", len(chunks))

    print("Storing chunks in ChromaDB...")

    store = VectorStore()

    store.add_documents(
        chunks,
        source="sample.pdf"
    )

    print("Ingestion completed!")


if __name__ == "__main__":
    ingest_pdf()