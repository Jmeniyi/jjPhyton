from datetime import datetime
from math import ceil

def save_to_history(text):
    dt = datetime.now().strftime("%d.%m.%Y %H:%M")
    with open("story_Calculator.txt", "a", encoding="utf-8") as file:
        file.write(f"[{dt}] {text}\n")
