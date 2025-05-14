import argparse
from interview import run_interview
from speech.mic import select_and_save_mic

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Digital Self CLI Interview Tool")
    parser.add_argument("--select-mic", action="store_true", help="Choose microphone input device")
    args = parser.parse_args()

    if args.select_mic:
        select_and_save_mic()
    else:
        run_interview()
