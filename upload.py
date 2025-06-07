from fastapi import APIRouter, UploadFile, File
from services.file_parser_service import extract_text_from_file
from services.summarize_service import summarize_contract

router = APIRouter()

@router.post("/upload")
async def upload_contract(file: UploadFile = File(...)):
    try:
        # Read the raw file content (bytes)
        content = await file.read()

        # Extract text based on file type
        contract_text = extract_text_from_file(file.filename, content)

        # Check if we successfully extracted text
        if "Unsupported file type" in contract_text:
            return {"error": contract_text}

        # Run the summarizer
        summary = summarize_contract(contract_text)

        return {
            "filename": file.filename,
            "summary": summary.strip()
        }

    except Exception as e:
        return {"error": str(e)}
