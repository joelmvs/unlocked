from fastapi import APIRouter
from pydantic import BaseModel
import openai
import os
from dotenv import load_dotenv

load_dotenv()

router = APIRouter()

class AskRequest(BaseModel):
    contract_text: str
    question: str

@router.post("/ask")
def ask(request: AskRequest):
    # Sanitize contract text
    clean_contract = request.contract_text.replace('\n', '\\n').replace('"', '\\"')

    # Build prompt for OpenAI
    system_prompt = (
        "You are Unlock, an AI contract assistant for freelancers and creators.\n"
        "Your job is to help people understand contracts in plain, helpful language — especially when they feel confused or unsure.\n"
        "Here’s how to respond:\n"
        "- Be friendly and clear\n"
        "- Use everyday examples if helpful (e.g., 'This is like…')\n"
        "- Always explain what the clause means"
    )

    user_prompt = f"Here is the contract:\n{clean_contract}\n\nQuestion: {request.question}"

    response = openai.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]
    )

    return {"answer": response.choices[0].message.content.strip()}
