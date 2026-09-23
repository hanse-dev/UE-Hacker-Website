import json

def load(filename):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print("📂 There is no saved game yet.")
        return None

load("gibtsnicht.json")
