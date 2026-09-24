from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from pathlib import Path
import shutil

from app.rag_pipeline import RAGPipeline
from app.pdf_loader import load_pdf
from app.chunker import create_chunks
from app.vector_store import VectorStore


app = FastAPI(
    title="AI Research Assistant API",
    description="RAG-based document research assistant",
    version="1.0.0"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


rag = RAGPipeline()

UPLOAD_DIR = Path("data/documents")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)


class QuestionRequest(BaseModel):
    question: str
    source: str | None = None


@app.get("/")
def home():
    return {
        "message": "AI Research Assistant API is running"
    }


@app.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):

    if not file.filename.lower().endswith(".pdf"):
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are allowed."
        )

    file_path = UPLOAD_DIR / file.filename

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    pages = load_pdf(str(file_path))

    if not pages:
        raise HTTPException(
            status_code=400,
            detail="Could not extract text from this PDF."
        )

    chunks = create_chunks(pages)

    store = VectorStore()
    store.add_documents(
        chunks,
        source=file.filename
    )

    return {
        "message": "PDF uploaded and indexed successfully.",
        "filename": file.filename,
        "pages": len(pages),
        "chunks": len(chunks)
    }


@app.post("/ask")
def ask_question(request: QuestionRequest):

    answer, sources = rag.ask(
    request.question,
    request.source
)

    return {
        "answer": answer,
        "sources": sources
    }