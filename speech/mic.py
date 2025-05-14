import sounddevice as sd
import os

ENV_PATH = ".env"
MIC_KEY = "MIC_DEVICE_INDEX"

def list_input_devices():
    devices = sd.query_devices()
    input_devices = [(i, d["name"]) for i, d in enumerate(devices) if d["max_input_channels"] > 0]
    
    print("\n🎙️ Available Input Devices:")
    for idx, name in input_devices:
        print(f"{idx}: {name}")
    
    return input_devices

def select_and_save_mic():
    devices = list_input_devices()
    
    try:
        choice = int(input("\nEnter the number of the mic device to use: "))
    except ValueError:
        print("Invalid input.")
        return

    if not any(d[0] == choice for d in devices):
        print("Invalid device number.")
        return

    print(f"✅ Selected mic: {devices[choice][1]} (Index {choice})")

    # Write or update .env file
    env_lines = []
    if os.path.exists(ENV_PATH):
        with open(ENV_PATH) as f:
            env_lines = f.readlines()

    with open(ENV_PATH, "w") as f:
        found = False
        for line in env_lines:
            if line.startswith(MIC_KEY):
                f.write(f"{MIC_KEY}={choice}\n")
                found = True
            else:
                f.write(line)
        if not found:
            f.write(f"{MIC_KEY}={choice}\n")
