from llm.together_client import generate_interview_questions
from speech.tts import speak
from speech.record import record_and_transcribe
from storage.dedup import is_duplicate, load_previous_questions, save_new_questions
from storage.save import save_qa

def run_interview():
    print("🤖 Welcome to your Digital Self Interview!\n")

    print("🔍 Loading previous questions...")
    
    seen = load_previous_questions()

    questions = [q for q in generate_interview_questions() if not is_duplicate(q, seen)]

    save_new_questions(questions)
    

    for i, question in enumerate(questions):
        print(f"\nQuestion {i+1}: {question}")
        speak(question)
        answer = record_and_transcribe()
        print(f"📝 Your answer: {answer}")
        save_qa(question, answer)

    print("\n✅ Session complete. Your answers were saved.")
