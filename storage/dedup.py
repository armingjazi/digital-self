import json
from pathlib import Path

HISTORY_FILE = Path("question_history.jsonl")

def load_previous_questions() -> set[str]:
    if not HISTORY_FILE.exists():
        return set()
    with open(HISTORY_FILE, "r") as f:
        return set(json.loads(line)["question"].strip().lower() for line in f)

def is_duplicate(q: str, seen: set[str]) -> bool:
    norm = q.strip().lower()
    return norm in seen  # can upgrade to fuzzy match later

def save_new_questions(questions: list[str]):
    with open(HISTORY_FILE, "a") as f:
        for q in questions:
            f.write(json.dumps({"question": q}) + "\n")
