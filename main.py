import argparse
from interview import run_interview
from speech.mic import select_and_save_mic

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Digital Self CLI Interview Tool")
    parser.add_argument("--select-mic", action="store_true", help="Choose microphone input device")
    parser.add_argument("--profile", type=str, help="Path to user profile file", default="profile.txt")
    parser.add_argument("--name", type=str, help="User's name", default=None)
    args = parser.parse_args()


    # look for profile.txt in current directory and load it
    user_profile = None
    try:
        with open("profile.txt", "r") as f:
            user_profile = f.read()
    except FileNotFoundError:
        print("No profile.txt found. Proceeding without user profile.")
    

    if args.select_mic:
        select_and_save_mic()
    else:
        run_interview(user_profile=user_profile, name=args.name)
