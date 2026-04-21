from datetime import datetime

INITIALS = "ZJ"

def generate_filename(start_time):
    timestamp = start_time.strftime("%Y-%m-%d--%H-%M")
    return f"{INITIALS}--{timestamp}.txt"

def save_session(filename, history):
    with open(filename, "w", encoding="utf-8") as f:
        for line in history:
            f.write(line + "\n")
