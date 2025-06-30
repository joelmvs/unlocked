from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
client = OpenAI()

def generate_contract_response(contract_text: str, question: str) -> str:
    prompt = f"""
You are Unlock, an AI contract assistant for freelancers and creators.

Your job is to help people understand contracts in plain, helpful language — especially when they feel confused or unsure.

Here’s how to respond:
- Be friendly and clear
- Use everyday examples if helpful (e.g., “This is like...”)
- Always explain what the clause means and why it matters
- Suggest what the user might want to ask, push back on, or change — but don’t use legal jargon

Contract Text:
{contract_text}

User's Question:
{question}
"""
    response = client.chat.completions.create(
        model="gpt-4-turbo",
        messages=[
            {"role": "system", "content": "You are Unlock, an AI contract assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7
    )
    return response.choices[0].message.content.strip()
