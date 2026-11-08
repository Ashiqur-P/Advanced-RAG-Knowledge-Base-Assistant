
import os
import secrets
from fastapi import FastAPI, UploadFile, File, HTTPException, Header
from docx import Document
from io import BytesIO

app = FastAPI(title="Bengali DOCX Text Extraction API")

API_KEY = os.getenv("DOCX_API_KEY")


@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "service": "DOCX Text Extraction API"
    }


@app.post("/extract-docx")
async def extract_docx(
    file: UploadFile = File(...),
    x_api_key: str = Header(default=None, alias="X-API-Key")
):
    if not API_KEY:
        raise HTTPException(
            status_code=500,
            detail="API authentication is not configured."
        )

    if not x_api_key or not secrets.compare_digest(x_api_key, API_KEY):
        raise HTTPException(
            status_code=401,
            detail="Invalid or missing API key."
        )

    filename = file.filename or ""

    if not filename.lower().endswith(".docx"):
        raise HTTPException(
            status_code=400,
            detail="Please upload a .docx Word document."
        )

    try:
        file_bytes = await file.read()
        document = Document(BytesIO(file_bytes))

        paragraphs = [
            paragraph.text.strip()
            for paragraph in document.paragraphs
            if paragraph.text.strip()
        ]

        extracted_text = "\n".join(paragraphs)

        if not extracted_text:
            raise HTTPException(
                status_code=422,
                detail="No text found in the DOCX document."
            )

        return {
            "fileName": filename,
            "documentType": "docx",
            "text": extracted_text,
            "characterCount": len(extracted_text)
        }

    except HTTPException:
        raise
    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail=f"DOCX extraction failed: {str(exc)}"
        )
