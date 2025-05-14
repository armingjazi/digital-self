import os
import sounddevice as sd
import tempfile
import scipy.io.wavfile
from faster_whisper import WhisperModel
from pynput import keyboard
import threading
import numpy as np

SAMPLE_RATE = 16000
MAX_DURATION = 120
device_index = int(os.getenv("MIC_DEVICE_INDEX", -1))

model = WhisperModel("base", compute_type="auto")

stop_flag = threading.Event()

def on_key_press(key):
    stop_flag.set()
    return False  # stop listener

def record_and_transcribe() -> str:
    stop_flag.clear() 
    print("🎙️ Recording... Press any key to stop.")
    
    recording = []

    def record():
        try:
            with sd.InputStream(samplerate=SAMPLE_RATE, channels=1, dtype='int16', device=device_index) as stream:
                while not stop_flag.is_set():
                    frame, _ = stream.read(1024)
                    recording.append(frame)
        except Exception as e:
            print(f"⚠️ Error during recording: {e}")
            stop_flag.set()

    # Start key listener
    key_listener = keyboard.Listener(on_press=on_key_press)
    key_listener.start()

    # Start recording
    record_thread = threading.Thread(target=record)
    record_thread.start()

    # Wait for key press or timeout
    stop_flag.wait(timeout=MAX_DURATION)

    print("⏹️ Got Key, Stopping recording...")
    key_listener.stop()
    record_thread.join()

    if not recording:
        print("⚠️ No audio was recorded. Try again.")
        return ""

    print("🔊 Processing audio...")
    # Merge all frames
    audio_np = b''.join(recording)

    audio_np = np.concatenate(recording, axis=0)

    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as tmpfile:
        scipy.io.wavfile.write(tmpfile.name, SAMPLE_RATE, audio_np)
        print(f"🎧 Recorded {len(audio_np)/SAMPLE_RATE:.2f} seconds of audio.")
        print("🔎 Transcribing...")
        segments, _ = model.transcribe(tmpfile.name)
        transcript = " ".join([segment.text for segment in segments])

    print(f"📝 Transcript: {transcript}")
    return transcript.strip()