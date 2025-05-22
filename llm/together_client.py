import os
import re
from dotenv import load_dotenv
import requests

load_dotenv()

TOGETHER_API_KEY = os.getenv("TOGETHER_API_KEY")

MODEL = "meta-llama/Meta-Llama-3.1-70B-Instruct-Turbo" 
TOGETHER_API_URL = "https://api.together.xyz/v1/chat/completions"

HEADERS = {
    "Authorization": f"Bearer {TOGETHER_API_KEY}",
    "Content-Type": "application/json"
}

def generate_interview_questions(old_questions, user_profile, name, n=10) -> list[str]:
    system_prompt = "You are an expert at designing interview questions to uncover someone's personality, values, ambitions, and deeper motivations. Avoid superficial questions. Ask questions that make the person reflect deeply."

    # add old questions to the system prompt
    if old_questions:
        system_prompt += f"\n\nHere are some previous questions:\n{old_questions}"

    # add user profile to the system prompt
    if user_profile:
        system_prompt += f"\n\nHere is the user's profile:\n{user_profile}"

    # add name to the system prompt
    if name:
        system_prompt += f"\n\nThe user's name is {name}. Use it in the questions to make them more personal."

    system_prompt += "\n\nNow, please generate new questions. Make sure they are unique and not similar to the previous ones."
    
    user_prompt = f"Please generate {n} unique, deep, reflective questions to understand a person's inner world. The idea is that these questions can be used to train an LLM act as digital twin of this person later on. Just return the questions as a numbered list, nothing else."

    payload = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        "temperature": 0.9,
        "top_p": 0.95
    }

    response = requests.post(TOGETHER_API_URL, headers=HEADERS, json=payload)
    response.raise_for_status()

    text = response.json()["choices"][0]["message"]["content"]
    lines = text.strip().splitlines()

    # Filter: only real questions
    questions = []
    for line in lines:
        clean = line.strip("-• ").strip()
        if re.match(r"^\d+\.", clean):
            # Remove "1. " from start
            q = re.sub(r"^\d+\.\s*", "", clean)
            questions.append(q)
        elif clean.endswith("?") and len(clean.split()) > 5:
            questions.append(clean)

    return questions