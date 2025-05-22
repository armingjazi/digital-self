import json
from pathlib import Path

OUTFILE = Path("interview_data.jsonl")

def save_qa(question: str, answer: str):
    with open(OUTFILE, "a") as f:
        f.write(json.dumps({"q": question, "a": answer}) + "\n")
        