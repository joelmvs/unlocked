from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
client = OpenAI()

def summarize_contract(contract_text: str) -> str:
    prompt = f"""
You are a warm, friendly legal assistant helping a creator understand a contract they just uploaded.

Summarize the contract below using simple, clear, and approachable language. Focus on these key areas:
- Payment terms (how much, when)
- Contract duration (how long the agreement lasts)
- Exclusivity (whether they can work with other clients)
- Ownership or IP rights (who owns the work or content)
- Termination clause (how the contract can be ended)

Please output 3 to 5 short bullet points. Each should be under 25 words and written in plain English.

If any legal jargon appears in the contract, define it clearly in the summary.
If there’s an opportunity to teach the user something helpful about a term, include a brief explanation.

Write like you're talking to a smart, non-legal friend who works in the creator economy.

Contract text:
{contract_text}
"""
    response = client.chat.completions.create(
        model="gpt-4-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content.strip()
