from app.pdf_loader import load_pdf
from app.chunker import create_chunks


pdf_path = "data/documents/sample.pdf"

text = load_pdf(pdf_path)

chunks = create_chunks(text)

print("Total chunks:", len(chunks))

for i, chunk in enumerate(chunks[:3]):
    print("\n--- Chunk", i + 1, "---")
    print(chunk)
