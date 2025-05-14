from TTS.api import TTS

# Load default English model (local-only)
tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC", progress_bar=False)

def speak(text: str):
    print("🎤 Speaking...")
    tts.tts_to_file(text=text, file_path="temp.wav")
    import os
    os.system("afplay temp.wav")  # macOS; use `aplay` or `play` on Linux
