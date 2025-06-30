from fastapi import APIRouter
from pydantic import BaseModel
from services.summarize_service import summarize_contract

router = APIRouter()

class SummaryRequest(BaseModel):
    contract_text: str

@router.post("/summarize")
def summarize(request: SummaryRequest):
    try:
        clean_contract = request.contract_text.replace('\n', '\\n').replace('"', '\\"')
        summary = summarize_contract(clean_contract)
        return {"summary": summary.strip()}
    except Exception as e:
        return {"error": str(e)}

